# Notebooks

Executable Jupyter notebooks for HR AI workflows: real code, run against synthetic data, with the actual cell outputs (including charts) saved in the file. Open them directly on GitHub to read the rendered output, or clone the repo and run them yourself. Never run them against real employee data without first reviewing the [risk assessment template](../03-governance/risk-assessment-template.md).

## Contents

| File | Purpose |
|---|---|
| [hr-qa-agent-demo.ipynb](hr-qa-agent-demo.ipynb) | Working demo of the HR Q&A agent: loads the eval set, defines an opinionated system prompt, walks through 5 representative scenarios (routine, edge-case, adversarial, sensitive, escalation) |
| [attrition-risk-modeling.ipynb](attrition-risk-modeling.ipynb) | Baseline attrition risk model on synthetic data: logistic regression + gradient boosting, calibration analysis, fairness audit, HRBP workflow integration |
| [skills-gap-analysis.ipynb](skills-gap-analysis.ipynb) | Identify priority L&D investments by mapping employee skill assessments against a competency framework |

## Running locally

```bash
pip install -r ../requirements.txt jupyter ipykernel
jupyter notebook
```

`hr-qa-agent-demo.ipynb` runs end to end with no API key: if `ANTHROPIC_API_KEY` is not set, `call_agent()` falls back to a hand-authored reference response for each scenario instead of a live model call, so the notebook always produces meaningful output. Set `ANTHROPIC_API_KEY` and install `anthropic` to compare live model output against the reference.

Each notebook is self-contained and generates its own synthetic sample data in the first few cells. Replace the sample data generation with your own data source to adapt a notebook for real use, see each notebook's "Adapting this for your organization" section.

CI executes all three notebooks on every push (see `.github/workflows/ci.yml`) to catch breakage before it merges.

## Coming soon

Compensation equity analysis and onboarding effectiveness measurement. Contributions welcome via [CONTRIBUTING.md](../CONTRIBUTING.md).
