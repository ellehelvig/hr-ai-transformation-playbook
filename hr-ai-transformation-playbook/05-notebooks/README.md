# Notebooks

Jupyter notebooks for HR analytics and AI use case development.

## Setup

```bash
pip install pandas scikit-learn matplotlib seaborn jupyter
jupyter notebook
```

## Contents

| Notebook | What it does |
|---|---|
| [attrition-risk-model.ipynb](attrition-risk-model.ipynb) | Baseline logistic regression model for attrition risk, with fairness audit and HRBP export |

## Important

All notebooks contain synthetic data for development. Replace data loading cells with your HRIS exports before running on real data.

Complete the [Risk Assessment Template](../03-governance/risk-assessment-template.md) before using any notebook output in production decisions.

## Data requirements

Notebooks in this repo require an anonymized HRIS export. **Do not commit real employee data to this repository.** Add your data files to `.gitignore` before working with real exports.
