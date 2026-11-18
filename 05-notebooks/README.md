# Notebooks

> **05 / BUILD** · Inspect executable examples using synthetic data and visible outputs.

[← Enablement](../04-enablement/README.md) · [Playbook home](../README.md) · [Next: Roadmap →](../06-roadmap/README.md)

---

**For:** People analytics and data science teams. **Start with:** [Attrition risk model with fairness audit](attrition-risk-modeling.ipynb).

Executable Jupyter notebooks for HR AI workflows: real code, run against synthetic data, with the actual cell outputs (including charts) saved in the file. Open them directly on GitHub to read the rendered output, or clone the repo and run them yourself. Never run them against real employee data without first reviewing the [risk assessment template](../03-governance/risk-assessment-template.md).

## Contents

| File | Purpose |
|---|---|
| [hr-qa-agent-demo.ipynb](hr-qa-agent-demo.ipynb) | Working demo of the HR Q&A agent: loads the eval set, defines an opinionated system prompt, walks through 5 representative scenarios (routine, edge-case, adversarial, sensitive, escalation) |
| [attrition-risk-modeling.ipynb](attrition-risk-modeling.ipynb) | Baseline attrition risk model on synthetic data: logistic regression + gradient boosting, calibration analysis, a three-part fairness audit (four-fifths selection rates, calibration by group, error-rate parity with small-group cautions), segment-level output, and stated limitations; individual scores are used only to validate the model |
| [skills-gap-analysis.ipynb](skills-gap-analysis.ipynb) | Identify priority L&D investments by mapping employee skill assessments against a competency framework |

## Running locally

Use Python 3.11 or later. Start in the **repository root**, not `05-notebooks`.
Follow the [locked environment setup](../docs/reproducible-setup.md#install),
including the verified bootstrap, locked install, and dependency check.

Then, in the same activated environment and repository root:

```bash
python -m ipykernel install --sys-prefix --name=python3
python - <<'PY'
from pathlib import Path
import nbformat
from nbclient import NotebookClient

for path in sorted(Path("05-notebooks").glob("*.ipynb")):
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    NotebookClient(
        notebook, timeout=300, kernel_name="python3",
        resources={"metadata": {"path": str(path.parent)}},
    ).execute()
    print(f"Executed: {path.name}")
PY
```

Run with no `ANTHROPIC_API_KEY` configured for an offline Q&A demonstration.
The kernel is installed inside this virtual environment. The execution command
does not save notebook outputs, but the skills-gap example writes its ignored
synthetic CSV in `05-notebooks`.

The Q&A notebook's no-key path returns **hand-authored reference responses**.
It illustrates intended tone and routing. It does not measure live model
behavior, policy accuracy, or reliability. A separately configured provider run
requires its own recorded model, date, inputs, outputs, and limitations, and may
incur costs. No live provider run is required by this setup.

Each notebook generates fictional sample data. Review its limitations and the
[risk assessment](../03-governance/risk-assessment-template.md) before considering
any adaptation. Passing synthetic execution does not authorize real HR use.

CI executes all three notebooks on pushes to `main` and pull requests targeting
`main`, as configured in `.github/workflows/ci.yml`.

## Not covered yet

Compensation equity analysis (deliberately: see [pay equity governance](../03-governance/pay-equity-governance.md) on why that work is attorney-directed) and onboarding effectiveness measurement. Contributions welcome via [CONTRIBUTING.md](../CONTRIBUTING.md).
