# Technical evidence and setup

[Playbook home](../README.md)

Inventory reviewed 10 October 2026. Counts describe repository contents, not effectiveness, independent validation, or HR outcomes.

37 vetted HR AI use cases is the legacy inventory label checked by the script; here, vetted means included in this curated reference collection, not independently approved or validated for use. Six installable agent skills, four architecture patterns, and a 4-module literacy curriculum are reference materials requiring review.

## Current status and evidence

This is an actively developed reference toolkit using synthetic data. It is not a production HR system. Templates need local adaptation and specialist review before use.

- Three notebooks execute in CI. The HR Q&A notebook can use reference responses without an API key; those outputs are not evidence of live model quality.
- Four workflow packages expose six MCP tools, backed by a 52-test suite. No tool calls an LLM internally. Compensation, screening, and recruiter-intake tools require human review in their outputs. That flag is not an authenticated approval system.
- The 29-case eval runner blocks failed refusal, escalation, and empty-response gates. Its scorer and LLM judge have 49 tests of their own.
- The first prompt smoke-test run is recorded in the [evaluation notes](../09-evals/README.md#prompt-library-smoke-tests). Human review is pending. The judge's agreement with human labels has not been measured, so its verdicts are not a launch gate.
- The [People Partner case study](../01-use-cases/work-redesign-people-partner.md) explains the work-design decisions. [Resolve](https://github.com/ellehelvig/peopleops-resolution-agent) is a separate executable prototype with its own evaluation evidence and production hold.

Run `python scripts/verify_claims.py` from the repository root to compare these dated counts with the repository. Published counts describe this code and content, not field outcomes.


## Setup and a first example

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

