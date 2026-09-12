import importlib.util as _ilu
import sys as _sys
import re
from pathlib import Path as _Path

# Loaded by explicit file path (not `import tool`) so this suite is safe to
# run standalone or all together with the other three folders' suites in one
# pytest invocation -- see comp_banding/test_comp_banding.py for why.
_spec = _ilu.spec_from_file_location(f"_local_tool_{__name__}", _Path(__file__).parent / "tool.py")
tool = _ilu.module_from_spec(_spec)
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
    """No field NAME anywhere in the return schema can hold a number standing in
    for 'should we hire this person.' Explanatory prose is allowed to use the
    word 'score' to say the tool doesn't produce one; a field called
    score/rank/fit_percent is not.

    This test is necessary but NOT sufficient, which is the whole point of
    test_counts_are_divisible_and_we_say_so below. Field-name filtering cannot
    stop a caller dividing two counts."""
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


# ── Regression: short technical terms must not be silently dropped ───────────

TECHNICAL_JD = """
Requirements
- Experience with SQL and AWS
- Proficiency in Go and R for analysis
- Build MCP integrations and own evals
- Comfortable in C++ and .NET codebases
- Familiarity with CI/CD and Node.js
"""

TECHNICAL_RESUME = """
Built SQL pipelines on AWS serving 40 internal teams.
Wrote Go services and R analysis notebooks for workforce reporting.
Shipped MCP integrations and owned the evals that gate their release.
Maintained C++ solvers and .NET services.
Ran CI/CD for a Node.js monorepo.
"""


def test_short_technical_acronyms_are_matched_not_dropped():
    """Regression for the bug that mattered most.

    The general keyword extractor requires 4+ characters, which silently
    deleted SQL, AWS, MCP, Go, and R. Every technical requirement returned
    'no_evidence_found' against a resume that plainly demonstrated all of
    them, while the response note told the reader that meant the resume
    didn't mention it. A false negative on a qualified candidate is the worst
    failure this tool can produce, so each term gets an explicit assertion."""
    result = tool.compare_to_resume(TECHNICAL_JD, TECHNICAL_RESUME)
    by_requirement = {r["requirement"]: r for r in result["evidence"]}

    assert result["no_evidence_count"] == 0, (
        "a resume demonstrating every requirement produced 'no evidence' for: "
        f"{[r['requirement'] for r in result['evidence'] if r['status'] == 'no_evidence_found']}"
    )

    sql_row = by_requirement["Experience with SQL and AWS"]
    assert sql_row["status"] == "evidence_found"
    assert {"sql", "aws"} <= set(sql_row["matched_terms"])

    go_row = by_requirement["Proficiency in Go and R for analysis"]
    assert {"go", "r"} <= set(go_row["matched_terms"])

    mcp_row = by_requirement["Build MCP integrations and own evals"]
    assert {"mcp", "evals"} <= set(mcp_row["matched_terms"])


def test_punctuated_technical_terms_survive_tokenization():
    """`[a-zA-Z][a-zA-Z-]+` reads 'c++' as nothing and 'node.js' as two words.
    These need their own matching pass, longest-first so 'c' does not eat 'c++'."""
    terms = tool._keywords("We use C++, C#, .NET, CI/CD and Node.js here")
    for expected in ("c++", "c#", ".net", "ci/cd", "node.js"):
        assert expected in terms, f"{expected!r} was lost during tokenization, got {sorted(terms)}"


def test_duration_requirement_is_not_assessable_rather_than_missing():
    """'5+ years of experience' reduces to zero comparable terms because every
    word is a stopword. Reporting that as 'no_evidence_found' told a recruiter
    the candidate lacked something the tool simply cannot measure."""
    result = tool.compare_to_resume(
        "Requirements\n- 5+ years of experience\n- Owns evals for production agents",
        TECHNICAL_RESUME,
    )
    rows = {r["requirement"]: r for r in result["evidence"]}
    duration = rows["5+ years of experience"]
    assert duration["status"] == "not_assessable_by_this_tool"
    assert "cannot verify" in duration["reason"]
    assert result["not_assessable_count"] == 1
    assert duration["status"] != "no_evidence_found"


# ── Guarantees are stated and behaviorally true ──────────────────────────────


def test_every_enforced_guarantee_is_actually_enforced():
    """Each claim in ENFORCED_GUARANTEES gets a behavioral check here. If you
    add a guarantee to that tuple without adding a check, this test fails,
    which is the mechanism that stops the docstring drifting ahead of the code
    again."""
    payload = tool.screen_candidate(TECHNICAL_JD, TECHNICAL_RESUME)
    comparison = payload["evidence_comparison"]

    assert len(tool.ENFORCED_GUARANTEES) == 5, (
        "ENFORCED_GUARANTEES changed; add or remove the matching behavioral check below"
    )

    # 1. no single fitness number
    numeric_keys = [
        k for k, v in comparison.items()
        if isinstance(v, (int, float)) and not isinstance(v, bool) and k.endswith(("_count", "count"))
    ]
    assert numeric_keys, "counts should exist; they are workload estimates"
    assert "fitness" not in str(comparison.keys())

    # 2. single resume per call, nothing to rank against
    assert "candidates" not in comparison
    assert isinstance(comparison["evidence"], list)

    # 3. every requirement carries a status, matched rows carry their evidence line
    for row in comparison["evidence"]:
        assert row["status"] in {
            "evidence_found", "partial_evidence_unconfirmed",
            "no_evidence_found", "not_assessable_by_this_tool",
        }
        if row["matched_terms"]:
            assert row["evidence_line"] is not None

    # 4. human review on every path
    assert payload["human_review_required"] is True
    assert comparison["human_review_required"] is True

    # 5. not-assessable is distinct from missing
    statuses = {r["status"] for r in comparison["evidence"]}
    assert "not_assessable_by_this_tool" not in statuses or comparison["not_assessable_count"] > 0


def test_counts_are_divisible_and_we_say_so():
    """The honest counterpart to test_output_never_contains_a_score_field.

    A caller can compute evidence_found_count / requirement_count and get a
    match percentage. That is unpreventable at the schema level, so the
    response must disclose it rather than imply a guarantee that doesn't hold.
    This test asserts the disclosure exists and is specific."""
    comparison = tool.compare_to_resume(TECHNICAL_JD, TECHNICAL_RESUME)

    derivable = comparison["evidence_found_count"] / comparison["requirement_count"]
    assert 0.0 <= derivable <= 1.0

    limitations = " ".join(comparison["known_limitations"]).lower()
    assert "divided into a percentage" in limitations
    assert "never as a fitness score" in limitations
    assert "keyword overlap" in limitations
    assert "has not been measured" in limitations


def test_threshold_behavior_is_documented():
    """The confirmed-evidence threshold is the most consequential number in the
    module. It must be a named constant, disclosed in the payload, and
    reasoned about in the source."""
    assert tool.CONFIRMED_EVIDENCE_THRESHOLD == 0.4
    limitations = " ".join(tool.KNOWN_LIMITATIONS)
    assert "0.4" in limitations
    assert "not\nvalidated" in limitations or "not validated" in limitations


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
