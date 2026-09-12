"""
Tests for the LLM-judge layer.

These run with no network and no API key. The judge is a pluggable callable
precisely so that its parsing, its failure modes, and its validation math can be
tested deterministically; a grading pipeline you can only exercise by spending
money on API calls is a pipeline nobody exercises.

Run:  pytest 09-evals -q
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

HERE = Path(__file__).parent
_spec = importlib.util.spec_from_file_location("eval_judge_under_test", HERE / "judge.py")
judge = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = judge
_spec.loader.exec_module(judge)

CASE = {
    "id": "r001",
    "category": "routine",
    "input": "How many vacation days do I get per year?",
    "expected_behavior": [
        "States accrual rate clearly",
        "Mentions that it may vary by tenure or location",
        "Cites policy source",
    ],
}


def _fixed_judge(reply: str, name: str = "test-judge"):
    def judge_fn(question, response, criteria):
        return reply, name
    return judge_fn


# ── Reply parsing ────────────────────────────────────────────────────────────


def test_parses_well_formed_verdicts():
    reply = "1|MET|states 15 days\n2|NOT_MET|no mention of tenure\n3|UNCLEAR|source is vague"
    result = judge.grade_response(CASE, "15 days per year.", _fixed_judge(reply))
    assert [v.met for v in result.verdicts] == [True, False, None]
    assert result.criteria_met == 1
    assert result.criteria_failed == 1
    assert result.criteria_unknown == 1
    assert result.verdicts[1].rationale == "no mention of tenure"


def test_missing_verdict_lines_become_unclear_not_met():
    """A judge that returns fewer lines than criteria must not leave the
    remaining criteria looking satisfied. Silent passes are the failure mode
    that makes a grading pipeline worse than no pipeline."""
    result = judge.grade_response(CASE, "15 days.", _fixed_judge("1|MET|ok"))
    assert [v.met for v in result.verdicts] == [True, None, None]
    assert "did not return a verdict" in result.verdicts[2].rationale


def test_garbage_reply_yields_all_unknown_not_a_crash():
    result = judge.grade_response(CASE, "15 days.", _fixed_judge("I'm sorry, I can't do that."))
    assert all(v.met is None for v in result.verdicts)
    assert result.criteria_met == 0


def test_out_of_range_and_unordered_indices_are_handled():
    reply = "3|MET|third\n1|NOT_MET|first\n9|MET|no such criterion"
    result = judge.grade_response(CASE, "x" * 50, _fixed_judge(reply))
    assert [v.met for v in result.verdicts] == [False, None, True]


def test_judge_exception_is_captured_not_propagated():
    """One judge failure must not abort a 29-case run."""
    def exploding(question, response, criteria):
        raise RuntimeError("rate limited")

    result = judge.grade_response(CASE, "15 days.", exploding)
    assert result.error is not None
    assert "rate limited" in result.error
    assert all(v.met is None for v in result.verdicts)
    assert result.low_confidence is True


def test_unreachable_agent_is_not_graded_as_failure():
    """An agent that never answered should not be recorded as failing its
    criteria; that would conflate an outage with a quality regression."""
    result = judge.grade_response(CASE, "ERROR: Could not connect to agent endpoint", _fixed_judge("1|MET|x"))
    assert result.judge_name == "not-run"
    assert result.criteria_failed == 0
    assert all(v.met is None for v in result.verdicts)


def test_case_without_expected_behavior_is_flagged():
    result = judge.grade_response({"id": "z001", "input": "hi"}, "hello there friend", _fixed_judge("1|MET|x"))
    assert result.error is not None
    assert result.low_confidence is True


# ── Canned judge ─────────────────────────────────────────────────────────────


def test_canned_judge_replays_verdicts(tmp_path):
    path = tmp_path / "verdicts.json"
    path.write_text(json.dumps({"r001": ["MET", "NOT_MET", "UNCLEAR"]}))
    fn = judge.make_canned_judge(path)
    result = judge.grade_response(CASE, "15 days.", fn)
    assert [v.met for v in result.verdicts] == [True, False, None]
    assert result.judge_name == "canned:verdicts.json"


def test_canned_judge_unknown_id_yields_unknowns(tmp_path):
    path = tmp_path / "verdicts.json"
    path.write_text(json.dumps({"other": ["MET"]}))
    result = judge.grade_response(CASE, "15 days.", judge.make_canned_judge(path))
    assert all(v.met is None for v in result.verdicts)


# ── Keyword fallback must announce its own weakness ──────────────────────────


def test_keyword_judge_is_always_low_confidence():
    """The fallback exists so the pipeline degrades rather than dies. It must
    never be mistakable for a real grade."""
    result = judge.grade_response(CASE, "You accrue 15 days, varying by tenure and location.", judge.keyword_judge)
    assert result.low_confidence is True
    assert result.judge_name == "keyword-heuristic"


def test_keyword_judge_never_returns_not_met():
    """It cannot distinguish "fails the criterion" from "worded differently",
    so it only ever says MET or UNCLEAR. Claiming NOT_MET would be asserting
    something it has no basis for."""
    for response in ("totally unrelated text about parking", "15 days accrual by tenure and location, see policy"):
        result = judge.grade_response(CASE, response, judge.keyword_judge)
        assert result.criteria_failed == 0


# ── Judge validation math ────────────────────────────────────────────────────


def test_kappa_is_one_for_perfect_non_degenerate_agreement():
    assert judge.cohens_kappa([True, False, True, False], [True, False, True, False]) == 1.0


def test_kappa_is_zero_for_chance_level_agreement():
    """The property that makes kappa worth using: a rater that always says MET
    gets high raw agreement on skewed data and near-zero kappa."""
    human = [True] * 9 + [False]
    always_met = [True] * 10
    kappa = judge.cohens_kappa(always_met, human)
    raw = sum(1 for a, b in zip(always_met, human, strict=True) if a == b) / 10
    assert raw == 0.9
    assert kappa == 0.0


def test_kappa_ignores_unlabeled_pairs():
    assert judge.cohens_kappa([True, None, False], [True, False, False]) == 1.0


def test_kappa_none_when_nothing_comparable():
    assert judge.cohens_kappa([None, None], [True, False]) is None


def test_agreement_report_calls_out_an_untrustworthy_judge():
    """The headline behavior: a judge that disagrees with humans must produce a
    report saying so in words, not just a number a reader might skim past."""
    results = [
        judge.JudgeResult("r001", [
            judge.CriterionVerdict("a", True), judge.CriterionVerdict("b", True),
            judge.CriterionVerdict("c", True), judge.CriterionVerdict("d", True),
        ])
    ]
    report = judge.measure_judge_agreement(results, {"r001": ["NOT_MET", "NOT_MET", "MET", "NOT_MET"]})
    assert report["judge_trustworthy"] is False
    assert "do NOT report judge verdicts as a pass rate" in report["interpretation"]
    assert report["cases_compared"] == 1
    assert report["criteria_compared"] == 4


def test_agreement_report_handles_no_labels():
    report = judge.measure_judge_agreement([], {})
    assert report["cohens_kappa"] is None
    assert report["judge_trustworthy"] is False
    assert "label some cases" in report["interpretation"]


def test_agreement_report_partial_labeling_is_usable():
    """Labeling 2 of 29 cases must produce a kappa on 2 cases, and say so,
    rather than requiring a complete labeling effort before giving any signal."""
    results = [
        judge.JudgeResult("r001", [judge.CriterionVerdict("a", True), judge.CriterionVerdict("b", False)]),
        judge.JudgeResult("r002", [judge.CriterionVerdict("a", True), judge.CriterionVerdict("b", False)]),
        judge.JudgeResult("r003", [judge.CriterionVerdict("a", True)]),
    ]
    report = judge.measure_judge_agreement(results, {"r001": ["MET", "NOT_MET"], "r002": ["MET", "NOT_MET"]})
    assert report["cases_compared"] == 2
    assert report["case_ids_compared"] == ["r001", "r002"]
    assert report["cohens_kappa"] == 1.0


# ── The criteria in the real eval file must be gradeable ─────────────────────


def test_every_eval_case_has_gradeable_criteria():
    """The gap this whole module closes: all 29 cases carried hand-written
    expected_behavior criteria that nothing ever read. If a case loses its
    criteria, or gains an empty list, grading silently skips it."""
    data = yaml.safe_load((HERE / "hr-qa-agent-evals.yaml").read_text())
    for case in data["evals"]:
        criteria = case.get("expected_behavior")
        assert criteria, f"{case['id']} has no expected_behavior to grade against"
        assert all(isinstance(c, str) and c.strip() for c in criteria), case["id"]


def test_example_verdict_and_label_files_match_the_yaml():
    """The shipped example files must stay consistent with the eval file, or the
    documented command in judge-verdicts-example.json silently mis-grades."""
    data = yaml.safe_load((HERE / "hr-qa-agent-evals.yaml").read_text())
    criteria_by_id = {c["id"]: len(c["expected_behavior"]) for c in data["evals"]}

    for filename in ("judge-verdicts-example.json", "human-labels-example.json"):
        payload = json.loads((HERE / filename).read_text())
        for key, entries in payload.items():
            if key.startswith("_"):
                continue
            assert key in criteria_by_id, f"{filename} references unknown eval id {key}"
            assert len(entries) == criteria_by_id[key], (
                f"{filename}[{key}] has {len(entries)} verdicts but the YAML defines "
                f"{criteria_by_id[key]} criteria"
            )


@pytest.mark.parametrize("verdict", ["MET", "NOT_MET", "UNCLEAR"])
def test_only_documented_verdicts_appear_in_example_files(verdict):
    for filename in ("judge-verdicts-example.json", "human-labels-example.json"):
        payload = json.loads((HERE / filename).read_text())
        for key, entries in payload.items():
            if key.startswith("_"):
                continue
            for entry in entries:
                value = entry["verdict"] if isinstance(entry, dict) else entry
                assert value in {"MET", "NOT_MET", "UNCLEAR"}, f"{filename}[{key}]: {value}"
