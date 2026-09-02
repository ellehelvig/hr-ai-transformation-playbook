"""
server.py
==========
Single MCP server exposing four HR agent tools on shared rails: comp
banding, bias-mitigated resume screening, recruiter intake calibration,
and a governance policy Q&A citation-finder.

Each tool's implementation lives in its own folder as a standalone,
independently testable module (run `pytest` inside any of comp_banding/,
resume_screen/, recruiter_intake/, or policy_qa/ on its own -- see that
folder's ENABLEMENT.md). This file's only job is registering them behind
one MCP surface, the way a real internal platform consolidates related
tools on shared rails instead of standing up a server per use case.

Every tool here returns `human_review_required: true` (or, for the policy
tool, a fixed not-legal-advice disclaimer) with no code path that removes
it. That is enforced in each tool's own test suite, not just asserted in
this docstring. See README.md for how this maps to the playbook's
governance model.

Run:
    pip install -r requirements.txt
    python server.py

Inspect interactively with the MCP dev inspector:
    mcp dev server.py

Connect from Claude Desktop by adding to claude_desktop_config.json:
    {
      "mcpServers": {
        "hr-ai-agents": {
          "command": "python",
          "args": ["/absolute/path/to/10-mcp-agents/server.py"]
        }
      }
    }
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

from mcp.server.fastmcp import FastMCP

BASE_DIR = Path(__file__).parent


def _load_module(name: str, relative_path: str):
    """Load each folder's tool.py as an independent module. Using
    importlib instead of a shared package namespace keeps every tool
    folder genuinely standalone -- an SME can `cd comp_banding && pytest`
    without this server or the other three tools existing at all."""
    module_path = BASE_DIR / relative_path
    spec = importlib.util.spec_from_file_location(name, module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


comp_banding = _load_module("comp_banding_tool", "comp_banding/tool.py")
resume_screen = _load_module("resume_screen_tool", "resume_screen/tool.py")
recruiter_intake = _load_module("recruiter_intake_tool", "recruiter_intake/tool.py")
policy_qa = _load_module("policy_qa_tool", "policy_qa/tool.py")

mcp = FastMCP("hr-ai-agents")


@mcp.tool()
def comp_band_position(
    role_family: str,
    level: str,
    location_tier: str,
    base_pay: float,
    used_historical_pay_as_input: bool = False,
) -> dict:
    """Estimate where a proposed base pay falls against benchmark bands for a
    role/level/location. Always advisory, never returns a go/no-go, and
    refuses to bless a number derived from someone's own pay history."""
    return comp_banding.get_band_position(
        role_family, level, location_tier, base_pay, used_historical_pay_as_input
    )


@mcp.tool()
def comp_list_known_bands() -> list[dict]:
    """List every role/level/location-tier combination the comp banding tool
    has benchmark data for, so an agent can check coverage before a lookup."""
    return comp_banding.list_known_bands()


@mcp.tool()
def screen_resume_against_jd(jd_text: str, resume_text: str) -> dict:
    """Compare a resume against a JD's stated requirements as an evidence map
    (never a score or rank), plus a bias-language lint on the JD itself."""
    return resume_screen.screen_candidate(jd_text, resume_text)


@mcp.tool()
def lint_jd_language(jd_text: str) -> dict:
    """Scan job description or HR-facing text for gendered-coded wording and
    protected-class-proxy phrases (e.g. 'culture fit', 'digital native')."""
    return resume_screen.lint_bias_language(jd_text)


@mcp.tool()
def calibrate_recruiter_intake(
    job_title: str,
    must_haves: list[str],
    nice_to_haves: list[str] | None = None,
    trainable: list[str] | None = None,
    disqualifiers: list[str] | None = None,
    day_in_the_life: str = "",
) -> dict:
    """Turn a raw hiring-manager intake into a structured calibration: skill
    buckets, a working Boolean search string, and clarifying questions for
    whatever the intake left vague (too many must-haves, no disqualifiers, etc.)."""
    intake = {
        "job_title": job_title,
        "must_haves": must_haves,
        "nice_to_haves": nice_to_haves or [],
        "trainable": trainable or [],
        "disqualifiers": disqualifiers or [],
        "day_in_the_life": day_in_the_life,
    }
    return recruiter_intake.build_calibration_doc(intake)


@mcp.tool()
def ask_governance_policy(question: str) -> dict:
    """Answer an HR-AI governance question by citing the actual sections of
    03-governance/*.md that address it. Returns no match, never a fabricated
    answer, when the corpus doesn't actually cover the question."""
    return policy_qa.search_policy(question)


if __name__ == "__main__":
    mcp.run()
