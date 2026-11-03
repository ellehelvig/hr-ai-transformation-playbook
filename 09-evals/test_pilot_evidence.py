"""Boundary and advisory-only behavior checks using fictional pilot inputs."""

import copy
import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
from pilot_evidence import BASE_EVIDENCE, MAX_BYTES, ROLLOUT_EVIDENCE, assess, load_input  # noqa: E402


@pytest.fixture
def payload():
    return json.loads(Path(__file__).with_name("pilot-evidence-example.json").read_text())


def test_missing_reviews_pause_despite_all_other_assertions(payload):
    result = assess(payload)
    assert result["advisory_status"] == "pause_for_evidence"
    assert result["evidence_gaps"] == ["identity_access_review", "privacy_review"]
    assert result["illustrative_net_capacity_hours"] == pytest.approx(-100 / 60)
    assert result["authorization_granted"] is False


@pytest.mark.parametrize("incident", ["cross_user_exposure", "approval_bypass"])
def test_incidents_override_large_capacity_and_missing_evidence(payload, incident):
    payload["incidents"][incident] = "reported"
    payload["effort"]["baseline_minutes"] = 1000
    result = assess(payload)
    assert result["advisory_status"] == "stop_affected_processing"
    assert result["reported_incidents"] == [incident]
    assert result["human_review_required"] is True
    assert result["authorization_granted"] is False


@pytest.mark.parametrize("stage", ["rehearsal", "rollout_review"])
def test_all_present_assertions_only_reach_human_review(payload, stage):
    payload["stage"] = stage
    payload["evidence"] = dict.fromkeys(BASE_EVIDENCE + ROLLOUT_EVIDENCE, "present")
    result = assess(payload)
    assert result["advisory_status"] == "human_review"
    assert result["human_review_required"] is True
    assert result["authorization_granted"] is False


def test_rehearsal_has_separate_required_evidence(payload):
    payload["stage"] = "rehearsal"
    assert assess(payload)["evidence_gaps"] == []


def test_omitted_evidence_and_incidents_are_not_passes(payload):
    del payload["evidence"]
    del payload["incidents"]
    result = assess(payload)
    assert result["evidence_gaps"] == list(BASE_EVIDENCE + ROLLOUT_EVIDENCE)
    assert result["unresolved_incidents"] == ["cross_user_exposure", "approval_bypass"]
    assert result["advisory_status"] == "pause_for_evidence"


@pytest.mark.parametrize("case_count,baseline,expected", [(100, 23, 100 / 30), (0, 20, 0), (100, 21, 0)])
def test_capacity_counts_all_assisted_components(payload, case_count, baseline, expected):
    payload["effort"]["case_count"] = case_count
    payload["effort"]["baseline_minutes"] = baseline
    assert assess(payload)["illustrative_net_capacity_hours"] == pytest.approx(expected)


def test_missing_effort_is_unknown_and_does_not_change_evidence_status(payload):
    del payload["effort"]
    assert assess(payload)["illustrative_net_capacity_hours"] is None
    assert assess(payload)["advisory_status"] == "pause_for_evidence"


@pytest.mark.parametrize("field", ["baseline_minutes", "preparation_minutes", "review_minutes",
                                  "rework_minutes", "escalation_minutes"])
@pytest.mark.parametrize("value", [True, -1, float("nan"), float("inf"), "2", None])
def test_invalid_effort_is_rejected(payload, field, value):
    payload["effort"][field] = value
    with pytest.raises(ValueError):
        assess(payload)


@pytest.mark.parametrize("count", [True, -1, 2.5, "100", 10**400])
def test_invalid_case_counts(payload, count):
    payload["effort"]["case_count"] = count
    with pytest.raises(ValueError):
        assess(payload)


@pytest.mark.parametrize("value", [1e308, 10**308])
def test_sum_overflow_is_rejected_even_with_zero_cases(payload, value):
    payload["effort"]["case_count"] = 0
    payload["effort"]["review_minutes"] = value
    payload["effort"]["rework_minutes"] = value
    with pytest.raises(ValueError):
        assess(payload)


@pytest.mark.parametrize("section", [None, "evidence", "incidents", "effort"])
def test_unknown_fields_are_rejected_without_echo(payload, section):
    target = payload if section is None else payload[section]
    target["fictional_person"] = "PRIVATE_SENTINEL"
    with pytest.raises(ValueError) as error:
        assess(payload)
    assert "PRIVATE_SENTINEL" not in str(error.value)


@pytest.mark.parametrize("key,value", [("schema_version", True), ("schema_version", 2),
                                       ("stage", "approved"), ("data_kind", "real")])
def test_invalid_envelope(payload, key, value):
    payload[key] = value
    with pytest.raises(ValueError):
        assess(payload)


@pytest.mark.parametrize("section,key,value", [("evidence", "privacy_review", True),
                                               ("incidents", "approval_bypass", False),
                                               ("evidence", "baseline", "approved")])
def test_states_are_strict(payload, section, key, value):
    payload[section][key] = value
    with pytest.raises(ValueError):
        assess(payload)


@pytest.mark.parametrize("section", ["evidence", "incidents", "effort"])
def test_null_sections_are_rejected(payload, section):
    payload[section] = None
    with pytest.raises(ValueError):
        assess(payload)


def test_partial_effort_rejected(payload):
    del payload["effort"]["rework_minutes"]
    with pytest.raises(ValueError):
        assess(payload)


def test_assess_does_not_mutate_input(payload):
    original = copy.deepcopy(payload)
    assess(payload)
    assert payload == original


@pytest.mark.parametrize("raw", ['{"evidence":{"baseline":"missing","baseline":"present"}}',
                                 '{"schema_version":1,"schema_version":1}', '[', '\u0000'])
def test_malformed_or_duplicate_json(tmp_path, raw):
    path = tmp_path / "input.json"
    path.write_text(raw)
    with pytest.raises(ValueError):
        load_input(path)


def test_size_limit(tmp_path):
    path = tmp_path / "input.json"
    path.write_bytes(b" " * (MAX_BYTES + 1))
    with pytest.raises(ValueError):
        load_input(path)


def test_deeply_nested_non_object_input_is_rejected(tmp_path):
    path = tmp_path / "input.json"
    path.write_text("[" * 2000 + "0" + "]" * 2000)
    with pytest.raises(ValueError):
        assess(load_input(path))


def test_cli_has_no_writes_and_does_not_echo_invalid_content(tmp_path):
    path = tmp_path / "input.json"
    path.write_text('{"fictional_person":"PRIVATE_SENTINEL"}')
    before = path.read_bytes()
    result = subprocess.run([sys.executable, str(Path(__file__).with_name("pilot_evidence.py")), str(path)],
                            capture_output=True, text=True, check=False)
    assert result.returncode == 2
    assert result.stdout == ""
    assert "PRIVATE_SENTINEL" not in result.stderr
    assert path.read_bytes() == before


def test_cli_example_emits_advisory_json():
    result = subprocess.run([sys.executable, str(Path(__file__).with_name("pilot_evidence.py")),
                             str(Path(__file__).with_name("pilot-evidence-example.json"))],
                            capture_output=True, text=True, check=True)
    assert json.loads(result.stdout)["authorization_granted"] is False
