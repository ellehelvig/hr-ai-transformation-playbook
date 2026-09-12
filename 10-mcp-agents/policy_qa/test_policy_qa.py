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


# ── Ranking tests, on the fixture corpus ─────────────────────────────────────
#
# These pass min_coverage=0.0 on purpose. They test RANKING: given a question,
# does the right document come back first? The relevance GATE cannot be tested
# here, because MIN_IDF_COVERAGE is calibrated against the real 95-section
# corpus and IDF is a corpus statistic. On a 5-section fixture every IDF value
# is small and unstable, and legitimate matches measure as low as 0.17
# coverage. Testing the gate against the fixture would either force the
# threshold down to a value that lets coincidences through on the real corpus,
# or force the fixture to grow into a copy of the real corpus. Gate behavior is
# tested separately, against the real thing, further down.

RANKING_ONLY = {"min_coverage": 0.0, "min_score": 0.0}


def test_finds_relevant_section_for_pay_equity_question(fixture_repo):
    result = tool.search_policy(
        "Can we use someone's salary history to set their new pay?",
        repo_root=fixture_repo, **RANKING_ONLY,
    )
    assert result["results"], "expected at least one match"
    top = result["results"][0]
    assert top["source_file"] == "pay-equity-governance.md"


def test_finds_relevant_section_for_incident_severity_question(fixture_repo):
    result = tool.search_policy(
        "What counts as a Sev 1 incident?", repo_root=fixture_repo, **RANKING_ONLY
    )
    top_files = {r["source_file"] for r in result["results"]}
    assert "incident-report-template.md" in top_files


def test_disclaimer_always_present(fixture_repo):
    result = tool.search_policy(
        "What's our EU AI Act vendor evidence requirement?", repo_root=fixture_repo, **RANKING_ONLY
    )
    assert result["disclaimer"] == tool.NOT_LEGAL_ADVICE_DISCLAIMER


def test_disclaimer_present_on_no_match_too(fixture_repo):
    """A no-match response still carries the disclaimer. The old code path for
    an empty query returned a dict with no `no_match` key at all, so a caller
    checking `result["no_match"]` raised KeyError on exactly the input most
    likely to produce it."""
    result = tool.search_policy("   ", repo_root=fixture_repo)
    assert result["no_match"] is True
    assert result["results"] == []
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
    result = tool.search_policy(
        "historical pay bias in comp models", repo_root=fixture_repo, **RANKING_ONLY
    )
    assert result["results"]
    top = result["results"][0]
    assert top["source_file"].endswith(".md")
    assert top["heading"]
    assert top["excerpt"]
    assert top["matched_terms"]
    assert top["relevance_score"] > 0
    assert 0.0 <= top["idf_coverage"] <= 1.0


def test_ranking_is_deterministic_on_ties(fixture_repo):
    """Two sections tying on BM25 must not swap places between runs; the sort
    key breaks ties on source file then heading."""
    runs = [
        [
            (r["source_file"], r["heading"])
            for r in tool.search_policy("pay", repo_root=fixture_repo, **RANKING_ONLY)["results"]
        ]
        for _ in range(5)
    ]
    assert all(r == runs[0] for r in runs)


# ── Relevance gate tests, on the REAL corpus ─────────────────────────────────


@pytest.fixture(scope="module")
def real_repo() -> _Path:
    """The actual playbook repo root, two levels up from this file."""
    root = _Path(__file__).resolve().parents[2]
    if not (root / "03-governance").is_dir():
        pytest.skip("real governance corpus not present")
    return root


def test_relevance_floor_rejects_stray_common_word_matches(real_repo):
    """The regression that keeps MIN_IDF_COVERAGE honest.

    Before the floor existed, "can I bring my dog to the office review?"
    returned three confident citations, top-ranked being the README's US
    federal AI enforcement section, matched on the single word "bring". An
    agent receiving that has no way to know the citations are coincidental."""
    for off_topic in (
        "Can I bring my dog to the office review?",
        "is our cafeteria menu vegetarian",
        "How do I reset my laptop password?",
        "what time does the shuttle leave for the airport",
    ):
        result = tool.search_policy(off_topic, repo_root=real_repo)
        assert result["no_match"] is True, (
            f"{off_topic!r} should not produce citations, got "
            f"{[(r['source_file'], r['idf_coverage']) for r in result['results']]}"
        )


def test_genuine_governance_questions_still_match(real_repo):
    """The other half of the gate: a floor that rejects real questions is worse
    than no floor. Each of these must return a citation, and the expected
    source document must appear in the top 3."""
    cases = [
        ("what logs do we need to keep for a high-risk system", "deployer-checklist.md"),
        ("what does the incident severity scale look like", "incident-report-template.md"),
        ("Can we use someone's salary history to set their new pay?", "pay-equity-governance.md"),
        ("who owns Article 22 controller status when a vendor scores candidates", None),
    ]
    for question, expected_file in cases:
        result = tool.search_policy(question, repo_root=real_repo)
        assert result["no_match"] is False, f"{question!r} returned no citations"
        if expected_file:
            files = {r["source_file"] for r in result["results"]}
            assert expected_file in files, f"{question!r} -> {files}, expected {expected_file}"


def test_idf_coverage_penalizes_absent_terms_more_than_common_ones(real_repo):
    """The property that makes IDF-weighted coverage work: a question whose
    distinctive term is absent from the corpus scores far lower than one whose
    only unmatched terms are ordinary English."""
    off_topic = tool.search_policy(
        "dog cafeteria vegetarian", repo_root=real_repo, min_score=0.0, min_coverage=0.0
    )
    on_topic = tool.search_policy(
        "we need to keep logs", repo_root=real_repo, min_score=0.0, min_coverage=0.0
    )
    assert on_topic["results"], "expected the on-topic question to retrieve something"
    off_best = max((r["idf_coverage"] for r in off_topic["results"]), default=0.0)
    on_best = max(r["idf_coverage"] for r in on_topic["results"])
    assert on_best > off_best


def test_index_is_cached_but_invalidates_on_edit(tmp_path):
    """The old code re-read and re-parsed the whole corpus on every query. The
    cache must not make a stale corpus sticky, because comp and HR partners
    edit these docs and expect the tool to cite the current text."""
    gov = tmp_path / "03-governance"
    gov.mkdir()
    doc = gov / "ai-use-policy.md"
    doc.write_text("# Policy\n\n## Retention\n\nKeep deployer logs six months.\n")

    first = tool.search_policy("how long do we keep deployer logs", repo_root=tmp_path, **RANKING_ONLY)
    assert "six months" in first["results"][0]["excerpt"]

    # Rewrite with a different retention period and a bumped mtime.
    doc.write_text("# Policy\n\n## Retention\n\nKeep deployer logs twenty-four months.\n")
    import os
    os.utime(doc, ns=(doc.stat().st_atime_ns, doc.stat().st_mtime_ns + 1_000_000_000))

    second = tool.search_policy("how long do we keep deployer logs", repo_root=tmp_path, **RANKING_ONLY)
    assert "twenty-four months" in second["results"][0]["excerpt"], (
        "cache served a stale corpus after the source document changed"
    )


def test_excerpt_provenance_names_the_trust_boundary(real_repo):
    """The response must tell the calling agent where excerpt text came from and
    that it is not instructions. This is the control for the injection surface
    described in the module docstring: retrieved prose cannot be sanitized, so
    the mitigation is that the consumer knows what it is holding."""
    result = tool.search_policy("what logs do we need to keep", repo_root=real_repo)
    provenance = result["excerpt_provenance"]
    assert "verbatim" in provenance
    assert "untrusted input" in provenance
    assert "not as instructions" in provenance
