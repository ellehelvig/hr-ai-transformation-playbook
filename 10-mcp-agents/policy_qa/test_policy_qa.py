import importlib.util as _ilu
import sys as _sys
from pathlib import Path as _Path

import pytest

# Loaded by explicit file path -- see comp_banding/test_comp_banding.py for why.
_spec = _ilu.spec_from_file_location(f"_local_tool_{__name__}", _Path(__file__).parent / "tool.py")
tool = _ilu.module_from_spec(_spec)
_sys.modules[_spec.name] = tool
_spec.loader.exec_module(tool)

PAY_EQUITY_MD = """# Pay equity governance

## Historical pay as a model input

Using employee compensation history to train or fine-tune a model is not
approved. Historical pay data reflects historical discrimination by design,
and any model trained on it will reproduce whatever bias shaped those
decisions.

## Escalation

Comp-related governance gaps route to employment counsel specifically, not
general Legal.
"""

INCIDENT_MD = """# Incident report template

## When to use this

Use this when an HR AI system does something it shouldn't have: a wrong
policy citation, a disclosure it shouldn't have made, a biased or
incorrectly escalated output.

## Severity ratings

Sev 1 incidents involve disclosed sensitive personal data or a systemic
bias and fairness failure, and require Legal, Privacy, and HR Leadership
involvement within 24 hours.
"""

EU_AI_ACT_MD = """# EU AI Act intake template

## Vendor evidence requested

Instructions for use, bias audit summary, logging architecture diagram,
conformity assessment status, SOC 2, DPA, and incident notification SLA.
"""


@pytest.fixture()
def fixture_repo(tmp_path: _Path) -> _Path:
    gov_dir = tmp_path / "03-governance"
    gov_dir.mkdir()
    (gov_dir / "pay-equity-governance.md").write_text(PAY_EQUITY_MD)
    (gov_dir / "incident-report-template.md").write_text(INCIDENT_MD)
    (gov_dir / "eu-ai-act-intake-template.md").write_text(EU_AI_ACT_MD)
    return tmp_path


def test_finds_relevant_section_for_pay_equity_question(fixture_repo):
    result = tool.search_policy("Can we use someone's salary history to set their new pay?", repo_root=fixture_repo)
    assert result["results"], "expected at least one match"
    top = result["results"][0]
    assert top["source_file"] == "pay-equity-governance.md"


def test_finds_relevant_section_for_incident_severity_question(fixture_repo):
    result = tool.search_policy("What counts as a Sev 1 incident?", repo_root=fixture_repo)
    top_files = {r["source_file"] for r in result["results"]}
    assert "incident-report-template.md" in top_files


def test_disclaimer_always_present(fixture_repo):
    result = tool.search_policy("What's our EU AI Act vendor evidence requirement?", repo_root=fixture_repo)
    assert result["disclaimer"] == tool.NOT_LEGAL_ADVICE_DISCLAIMER


def test_no_fabrication_on_irrelevant_question(fixture_repo):
    """The tool must return an empty result set, never invent a plausible-sounding
    but ungrounded answer, when nothing in the corpus is actually relevant."""
    result = tool.search_policy("What's the office coffee budget for Q4?", repo_root=fixture_repo)
    assert result["no_match"] is True
    assert result["results"] == []
    assert result["disclaimer"] == tool.NOT_LEGAL_ADVICE_DISCLAIMER


def test_missing_governance_dir_raises_not_silent_empty(tmp_path):
    with pytest.raises(tool.GovernanceCorpusNotFoundError):
        tool.search_policy("anything", repo_root=tmp_path)


def test_results_include_citable_source_and_excerpt(fixture_repo):
    result = tool.search_policy("historical pay bias in comp models", repo_root=fixture_repo)
    assert result["results"]
    top = result["results"][0]
    assert top["source_file"].endswith(".md")
    assert top["heading"]
    assert top["excerpt"]
    assert top["matched_terms"]
