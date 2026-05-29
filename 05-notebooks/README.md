# Notebooks

Jupyter notebooks and demo writeups for HR AI workflows. All examples use synthetic data. Never run them against real employee data without first reviewing the [risk assessment template](../03-governance/risk-assessment-template.md).

## Contents

| File | Purpose |
|---|---|
| [hr-qa-agent-demo.md](hr-qa-agent-demo.md) | Working demo of the HR Q&A agent: loads the eval set, defines an opinionated system prompt, walks through 5 representative scenarios (routine, edge-case, adversarial, sensitive, escalation) |
| [attrition-risk-modeling.md](attrition-risk-modeling.md) | Baseline attrition risk model on synthetic data: logistic regression + gradient boosting, calibration analysis, fairness audit, HRBP workflow integration |
| [skills-gap-analysis.ipynb](skills-gap-analysis.ipynb) | Identify priority L&D investments by mapping employee skill assessments against a competency framework |

## Running locally

The code in the `.md` demos is runnable. Copy the cells into a Jupyter notebook or Python script.

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter anthropic pyyaml
jupyter notebook
```

The HR Q&A demo uses a placeholder response unless you set `ANTHROPIC_API_KEY` in your environment, in which case it makes live model calls.

Each demo is self-contained and includes synthetic sample data. Replace the sample inputs with your own data structures.

## Coming soon

Compensation equity analysis and onboarding effectiveness measurement. Contributions welcome via [CONTRIBUTING.md](../CONTRIBUTING.md).
