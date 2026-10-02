# HR AI Transformation Playbook

This toolkit helps People teams prioritize AI use cases, design controls, and plan adoption. It is for HR and talent leaders, enablement partners, and engineers who need a shared way to decide what to build and how to evaluate it.

[Browse the playbook](https://ellehelvig.github.io/hr-ai-transformation-playbook/) · [People Partner work redesign](01-use-cases/work-redesign-people-partner.md) · [Try the ROI calculator](https://ellehelvig.github.io/hr-ai-transformation-playbook/08-roi-measurement/dashboard.html)

[![Tests](https://img.shields.io/github/actions/workflow/status/ellehelvig/hr-ai-transformation-playbook/ci.yml?branch=main&style=flat-square&label=tests)](https://github.com/ellehelvig/hr-ai-transformation-playbook/actions/workflows/ci.yml)

## Why I built this

HR AI adoption needs more than a tool choice. It needs a useful problem, clear ownership, controls that people can inspect, and a plan to change the work. I built this playbook to connect those decisions in one practical toolkit. I defined the HR problems, operating model, and governance approach, and built the implementation with AI-assisted development.

## Start here

| You want to | Start with |
|---|---|
| Understand where AI belongs in an HR role | [People Partner work redesign](01-use-cases/work-redesign-people-partner.md) |
| Choose an initial use case | [Prioritization matrix](01-use-cases/prioritization-matrix.md) |
| Review risk and ownership | [AI use policy](03-governance/ai-use-policy.md) and [risk assessment](03-governance/risk-assessment-template.md) |
| Inspect runnable tools | [MCP tools](10-mcp-agents/README.md) |
| Plan training and adoption | [Enablement](04-enablement/README.md) |

## Setup and a first example

The templates can be read and adapted without installing anything. For the Python tools and local checks, use Python 3.11 or later:

```bash
git clone https://github.com/ellehelvig/hr-ai-transformation-playbook.git
cd hr-ai-transformation-playbook
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt -r 10-mcp-agents/requirements.txt ruff
python -m pytest 10-mcp-agents 09-evals -q
```

On Windows, activate the environment with `.venv\Scripts\Activate.ps1` in PowerShell.

Inspect a synthetic compensation benchmark without calling a model:

```bash
python - <<'PY'
import sys
sys.path.insert(0, "10-mcp-agents")
from comp_banding.tool import get_band_position
result = get_band_position("Recruiter", "IC3", "tier1", 105000, False)
print(result["human_review_required"])
PY
```

Expected output: `True`. This example uses illustrative benchmark data, not real pay data. The tool does not approve compensation. See [the handoff notes](10-mcp-agents/comp_banding/ENABLEMENT.md) for the required historical-pay declaration and other limits.

For notebooks, follow [their setup instructions](05-notebooks/README.md). For an MCP client, use the [server quick start](10-mcp-agents/README.md#quickstart). Live model evaluations are optional and may incur provider costs. Keep API credentials in environment variables or platform secrets.

## What is included

| Stage | Contents |
|---|---|
| Decide | [01 · Use cases](01-use-cases/README.md): 37 vetted HR AI use cases and prioritization; [06 · Roadmap](06-roadmap/README.md): an 18-month template |
| Govern | [03 · Governance](03-governance/README.md): use policy, risk assessment, EU AI Act intake, vendor review, and incident response |
| Build | [02 · Prompts](02-prompt-library/README.md), [05 · Notebooks](05-notebooks/README.md), [07 · Workflow patterns](07-agentic-patterns/README.md): four architecture patterns, [09 · Evals](09-evals/README.md), [10 · MCP tools](10-mcp-agents/README.md), and [11 · Skills](11-skills/README.md): six installable agent skills |
| Adopt and measure | [04 · Enablement](04-enablement/README.md): a 4-module literacy curriculum and adoption plan; [08 · ROI](08-roi-measurement/README.md): business-case templates and a calculator |

## Current status and evidence

This is an actively developed reference toolkit using synthetic data. It is not a production HR system. Templates need local adaptation and specialist review before use.

- Three notebooks execute in CI. The HR Q&A notebook can use reference responses without an API key; those outputs are not evidence of live model quality.
- Four workflow packages expose six MCP tools, backed by a 52-test suite. No tool calls an LLM internally. Compensation, screening, and recruiter-intake tools require human review in their outputs. That flag is not an authenticated approval system.
- The 29-case eval runner blocks failed refusal, escalation, and empty-response gates. Its scorer and LLM judge have 49 tests of their own.
- The first prompt smoke-test run is recorded in the [evaluation notes](09-evals/README.md#prompt-library-smoke-tests). Human review is pending. The judge's agreement with human labels has not been measured, so its verdicts are not a launch gate.
- The [People Partner case study](01-use-cases/work-redesign-people-partner.md) explains the work-design decisions. [Resolve](https://github.com/ellehelvig/peopleops-resolution-agent) is a separate executable prototype with its own evaluation evidence and production hold.

Run `python scripts/verify_claims.py` to compare the counts above with the repository. Published counts describe this code and content, not field outcomes.

## Scope and maintenance

The governance materials cover the EU, US federal and selected state and city requirements, the UK, and Ontario. They do not cover every jurisdiction. Review the [key legal dates](03-governance/README.md#key-dates-for-hr) and have Legal and Privacy review materials before adoption. This is not legal advice.

MIT licensed. [Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md) · [Security](SECURITY.md) · [Cite this work](CITATION.cff) · [Elle Helvig on LinkedIn](https://www.linkedin.com/in/ellehelvig/)
