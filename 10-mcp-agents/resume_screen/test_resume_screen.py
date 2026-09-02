import importlib.util as _ilu
import re
from pathlib import Path as _Path

# Loaded by explicit file path (not `import tool`) so this suite is safe to
# run standalone or all together with the other three folders' suites in one
# pytest invocation -- see comp_banding/test_comp_banding.py for why.
_spec = _ilu.spec_from_file_location(f"_local_tool_{__name__}", _Path(__file__).parent / "tool.py")
tool = _ilu.module_from_spec(_spec)
import sys as _sys
_sys.modules[_spec.name] = tool
_spec.loader.exec_module(tool)

SAMPLE_JD = """
About the role
We need someone who is a true rockstar and a great culture fit.

What you'll do
- Design, deploy, and continuously improve agents using Claude and MCP integrations
- Pair with subject matter experts to build domain-specific agents
- Own evals and monitor adoption in production

Requirements
- Demonstrated hands-on experience building AI agents or automations
- Track record of taking solutions from prototype through real adoption
- Comfortable operating as a senior individual contributor
"""

SAMPLE_RESUME_STRONG = """
Built and shipped three internal AI agents using Claude and custom MCP servers,
each adopted by 40+ recruiters within a quarter.
Partnered directly with compensation analysts to design a comp-banding agent,
then trained them to maintain it themselves.
Owned an eval suite covering agent output quality and monitored adoption weekly,
diagnosing and fixing three production failures.
Operated independently as the sole AI builder on the People team for two years.
"""

SAMPLE_RESUME_WEAK = """
Recruiter with five years of experience in high-volume tech hiring.
Strong communicator, manages full-cycle recruiting for engineering roles.
"""


def test_extract_requirements_pulls_bullets():
    reqs = tool.extract_requirements(SAMPLE_JD)
    assert len(reqs) >= 5
    assert any("evals" in r.lower() for r in reqs)


def test_strong_resume_gets_more_confirmed_evidence_than_weak_one():
    strong = tool.compare_to_resume(SAMPLE_JD, SAMPLE_RESUME_STRONG)
    weak = tool.compare_to_resume(SAMPLE_JD, SAMPLE_RESUME_WEAK)
    assert strong["evidence_found_count"] > weak["evidence_found_count"]


def test_missing_requirement_is_no_evidence_not_a_penalty():
    result = tool.compare_to_resume(SAMPLE_JD, SAMPLE_RESUME_WEAK)
    statuses = {r["status"] for r in result["evidence"]}
    assert "no_evidence_found" in statuses
    allowed = {"evidence_found", "partial_evidence_unconfirmed", "no_evidence_found"}
    assert statuses <= allowed


def _all_keys(obj, path=""):
    """Recursively collect every dict key in a nested structure, so we can
    check field NAMES for banned scoring language without also flagging the
    plain-English disclaimers that legitimately use the word 'score' or
    'recommend' to explain what the tool refuses to do."""
    keys = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            keys.append(f"{path}.{k}" if path else k)
            keys.extend(_all_keys(v, f"{path}.{k}"))
    elif isinstance(obj, list):
        for item in obj:
            keys.extend(_all_keys(item, path))
    return keys


def test_output_never_contains_a_score_field():
    """The single most important test in this module: no field NAME anywhere
    in the return schema can hold a number standing in for 'should we hire
    this person.' Explanatory prose is allowed to use the word 'score' to say
    the tool doesn't produce one; a field called score/rank/fit_percent is not."""
    banned_key_pattern = re.compile(r"score|rank|fit_percent|match_percent|recommendation", re.I)
    for payload in (
        tool.compare_to_resume(SAMPLE_JD, SAMPLE_RESUME_STRONG),
        tool.screen_candidate(SAMPLE_JD, SAMPLE_RESUME_STRONG),
    ):
        offending = [k for k in _all_keys(payload) if banned_key_pattern.search(k.split(".")[-1])]
        assert offending == [], f"found banned scoring field name(s): {offending}"
        for entry in payload.get("evidence_comparison", payload).get("evidence", []):
            assert isinstance(entry["status"], str)
            assert not entry["status"].replace(".", "", 1).isdigit()


def test_bias_lint_flags_rockstar_and_culture_fit():
    result = tool.lint_bias_language(SAMPLE_JD)
    terms_found = {m["term"] for m in result["matches"]}
    assert "rockstar" in terms_found
    assert "culture fit" in terms_found
    high = [m for m in result["matches"] if m["severity"] == "high"]
    assert any(m["term"] == "culture fit" for m in high)


def test_bias_lint_clean_text_has_no_matches():
    clean = "Design agent instructions, write evals, and pair with SMEs to ship production tools."
    result = tool.lint_bias_language(clean)
    assert result["matches"] == []


def test_human_review_required_always_present_and_true():
    result = tool.screen_candidate(SAMPLE_JD, SAMPLE_RESUME_STRONG)
    assert result["human_review_required"] is True
    assert result["evidence_comparison"]["human_review_required"] is True
