# 10. MCP agents

Four working HR agent tools, exposed on one MCP server, built to close
specific gaps this playbook had already identified in its own governance
and use-case docs, not built as generic demos.

Comp banding for compensation analysts. Bias-mitigated resume screening
that closes the "None yet" mitigation gap flagged in
`01-use-cases/use-case-library.md`. Recruiter intake calibration. A
governance policy citation-finder grounded in this repo's own
`03-governance/` docs. Every tool is real, runnable Python with a passing
pytest suite, not a prompt-only sketch.

## Why this section exists

The rest of the playbook (01 through 09) documents use cases, prompts, and
governance in markdown. This section is the part of the playbook that
runs: an actual MCP server an agent (Claude, or anything else that speaks
MCP) can call. The design choices here are the same ones argued for in
`03-governance/`, just enforced in code instead of policy prose:

- **Deterministic core, judgment left to the human or the calling agent.**
  None of these four tools call an LLM internally. Comp banding does
  arithmetic. Resume screening does keyword evidence-mapping. Recruiter
  intake does string templating. Policy Q&A does lexical search over real
  files. That's deliberate: the parts of these workflows that need
  reproducible, auditable behavior are handled in plain code; the parts
  that need real judgment (explaining a result, drafting outreach, making
  the actual call) are left to whoever's calling the tool.
- **`human_review_required: true` with no code path that turns it off.**
  Every tool's test suite checks this, not just the docstring.
- **No black-box scores.** The resume-screening tool's schema is tested to
  guarantee no `score`, `rank`, or `fit_percent` field can ever appear in
  its output (`resume_screen/test_resume_screen.py::test_output_never_contains_a_score_field`).
- **Grounded in this repo's own content, not a separate copy of it.** The
  policy Q&A tool reads `03-governance/*.md` directly at call time. Edit a
  governance doc, the next question against it reflects the edit
  immediately, there's no index to fall out of sync.
- **Every folder is independently maintainable.** Each tool folder has its
  own `tool.py`, its own data file, its own tests, and an `ENABLEMENT.md`
  written as a handoff doc, the kind of doc a comp analyst or recruiter
  would actually need to extend their own tool without an engineer in the
  room.

## Structure

```
10-mcp-agents/
  server.py                    single MCP server, registers all four tools
  requirements.txt
  pytest.ini                   makes `pytest` work both per-folder and from here
  README.md                    this file
  ADOPTION-MONITORING.md       how this would actually be operated, not just shipped
  comp_banding/
    tool.py  data/comp_bands.json  test_comp_banding.py  ENABLEMENT.md
  resume_screen/
    tool.py  data/bias_terms.json  test_resume_screen.py  ENABLEMENT.md
  recruiter_intake/
    tool.py  data/skill_synonyms.json  test_recruiter_intake.py  ENABLEMENT.md
  policy_qa/
    tool.py  test_policy_qa.py  ENABLEMENT.md   (reads ../../03-governance/*.md directly)
```

## Quickstart

```bash
cd 10-mcp-agents
pip install -r requirements.txt

# run every tool's test suite (32 tests, all four folders, one command)
pytest

# or just one tool's suite, standalone, exactly as its ENABLEMENT.md describes
cd comp_banding && pytest

# start the server
cd 10-mcp-agents && python server.py

# or inspect it interactively
mcp dev server.py
```

Connect from Claude Desktop by adding to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "hr-ai-agents": {
      "command": "python",
      "args": ["/absolute/path/to/hr-ai-transformation-playbook/10-mcp-agents/server.py"]
    }
  }
}
```

## Tools exposed

| MCP tool | What it does | Backing folder |
|---|---|---|
| `comp_band_position` | Where a proposed base pay lands against benchmark bands; blocks banding decisions derived from historical pay | `comp_banding/` |
| `comp_list_known_bands` | Lists covered role/level/location combinations | `comp_banding/` |
| `screen_resume_against_jd` | Evidence map of a resume against a JD's requirements, no score or rank, plus a JD bias-language lint | `resume_screen/` |
| `lint_jd_language` | Flags gendered-coded wording and protected-class-proxy phrases in any HR text | `resume_screen/` |
| `calibrate_recruiter_intake` | Turns a raw intake into skill buckets, a Boolean search string, and clarifying questions | `recruiter_intake/` |
| `ask_governance_policy` | Cites the actual `03-governance/*.md` sections relevant to a question; returns no match rather than a fabricated answer | `policy_qa/` |

## A note on the synthetic data

`comp_banding/data/comp_bands.json` and every resume/JD sample in the test
suites are made up for this build. They're clearly labeled as such in the
data files themselves. Replace the benchmark data with real, licensed
survey data before this touches anything real, that's called out in
`comp_banding/ENABLEMENT.md` too.
