# Notebooks

Jupyter notebooks for workforce analytics. All notebooks use synthetic data — never run them against real employee data without first reviewing the [risk assessment template](../03-governance/risk-assessment-template.md).

## Contents

| File | Purpose |
|---|---|
| [skills-gap-analysis.ipynb](skills-gap-analysis.ipynb) | Identify priority L&D investments by mapping employee skill assessments against a competency framework |

## Running locally

```bash
pip install pandas numpy matplotlib seaborn jupyter
jupyter notebook
```

Each notebook is self-contained and includes synthetic sample data. Replace the sample inputs with your own data structures — every notebook flags the cells you need to edit.

## Coming soon

Attrition risk modeling, compensation equity analysis, and onboarding effectiveness. Contributions welcome via [CONTRIBUTING.md](../CONTRIBUTING.md).
