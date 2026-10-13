# Technical evidence and setup

[Playbook home](../README.md)

Inventory reviewed 12 October 2026. Counts describe repository contents, not effectiveness, independent validation, or HR outcomes. Run `python scripts/verify_claims.py` from the repository root to recompute every count on this page from the tree.

## What the repository contains

This is an actively developed reference toolkit using synthetic data. It is not a production HR system. Templates need local adaptation and review by HR, Legal, Privacy, and Security, as appropriate, before use.

- 37 vetted HR AI use cases. Here, vetted means included in this curated reference collection, not independently approved or validated for use.
- Six installable agent skills, four architecture patterns, and a 4-module literacy curriculum. These are reference materials that require review before adoption.
- Three notebooks execute in CI on every push, using synthetic data only. The HR Q&A notebook can use reference responses without an API key; those outputs are not evidence of live model quality.

## What the tools do, and what that proves

- Four HR workflows expose six MCP tools, backed by a 52-test suite. No tool calls an LLM internally, so their behavior is reproducible and auditable.
- The comp banding, resume screening, and recruiter intake tools always return `human_review_required: true`, with no code path that turns it off, and their tests check it. That flag is not an authenticated approval system. The policy Q&A tool instead always returns a not-legal-advice disclaimer, also tested.
- The 29-case eval runner exits non-zero when a refusal, escalation, or empty-response gate fails, so it can block a launch. Its scorer and LLM judge have 49 tests of their own, and the runner can measure the judge's agreement with human labels (Cohen's kappa). No labeled run has been done yet, so judge verdicts are not a launch gate.
- The [prompt library smoke tests](../09-evals/README.md#prompt-library-smoke-tests) are set up. No results are recorded yet, so no prompt is described as tested.
- The [People Partner case study](../01-use-cases/work-redesign-people-partner.md) explains the work-design decisions. It is a proposal informed by prototype failures, with no measured business outcome or completed employee pilot.
- [Resolve](https://github.com/ellehelvig/peopleops-resolution-agent) is a separate executable prototype with its own evaluation evidence and production hold.
- Nothing assumes a specific HRIS, ATS, or model provider.

Technical checks support narrow implementation claims. They do not establish reliable HR advice, fairness, legal compliance, or production readiness.

## How to read results

Use these labels when reading or adding a result to this repository.

| Label | Meaning | What it needs |
|---|---|---|
| Observed | Measured or directly demonstrated | The version, dataset, method, date, and scope. A synthetic test shows behavior in that test, not business impact or production readiness. |
| Estimated | Calculated or projected from stated assumptions | The assumptions, method, and uncertainty. Projected capacity is not observed savings. |
| Illustrative | A hypothetical or simulated example used to explain a framework | A label wherever readers meet the inputs and outputs. |

Results reported without measurement context stay unverified. Controls are described separately as demonstrated, simulated, proposed, or not yet validated. Passing tests do not override a stop criterion.

## Setup and a first example

Use the [locked local and CI setup](reproducible-setup.md) for dependency
consistency and validation details. The lock supports tested deterministic tools
and synthetic notebooks. It does not validate prompts, model judges, or
governance templates for real HR use.

The templates can be read and adapted without installing anything. For the Python tools and local checks, use Python 3.11 or later:

```bash
git clone https://github.com/ellehelvig/hr-ai-transformation-playbook.git
cd hr-ai-transformation-playbook
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-lock.txt
python -m pip check
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

Expected output: `True`. This example uses illustrative benchmark data, not real pay data. The tool does not approve compensation. See [the handoff notes](../10-mcp-agents/comp_banding/ENABLEMENT.md) for the required historical-pay declaration and other limits.

For notebooks, follow [their setup instructions](../05-notebooks/README.md). For an MCP client, use the [server quick start](../10-mcp-agents/README.md#quickstart). Live model evaluations are optional and may incur provider costs. Keep API credentials in environment variables or platform secrets.
