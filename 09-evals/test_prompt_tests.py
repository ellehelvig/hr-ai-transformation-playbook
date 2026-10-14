"""Offline checks for the prompt library smoke tests and the live judge request."""

from __future__ import annotations

import json
import re
import sys
import types
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

import judge  # noqa: E402
import prompt_tests  # noqa: E402

PLACEHOLDER = re.compile(r"\[[^\]\n]+\]")


def test_library_parses_every_numbered_prompt():
    library = prompt_tests.load_library()
    assert len(library) >= 40
    assert all(entry["prompt"].strip() for entry in library.values())


def test_every_fixture_fills_its_template():
    cases = prompt_tests.load_cases()
    assert cases
    for case in cases:
        assert case["trap"] and case["expected_behavior"], case["id"]
        # Anything left in brackets must be an option list the model chooses from, not a missing input.
        for leftover in PLACEHOLDER.findall(case["input"]):
            assert " / " in leftover, f"{case['id']}: unfilled placeholder {leftover}"


def test_fixtures_are_synthetic():
    text = prompt_tests.FIXTURES.read_text(encoding="utf-8")
    assert chr(0x2014) not in text  # the house style bans em dashes
    assert "fictional" in text.lower()


def test_fill_rejects_missing_and_miscounted_placeholders():
    with pytest.raises(ValueError):
        prompt_tests.fill("Hello [NAME]", {"[TITLE]": "x"})
    with pytest.raises(ValueError):
        prompt_tests.fill("[X] and [X]", {"[X]": ["one"]})
    assert prompt_tests.fill("[X] and [X]", {"[X]": ["one", "two"]}) == "one and two"


def test_live_judge_request_sends_no_sampling_parameters(monkeypatch):
    """Current Claude models reject non-default temperature with a 400."""
    sent = {}

    class FakeMessages:
        def create(self, **kwargs):
            sent.update(kwargs)
            return types.SimpleNamespace(content=[types.SimpleNamespace(type="text", text="1|MET|ok")])

    fake = types.ModuleType("anthropic")
    fake.Anthropic = lambda: types.SimpleNamespace(messages=FakeMessages())
    monkeypatch.setitem(sys.modules, "anthropic", fake)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    monkeypatch.delenv(judge.JUDGE_MODEL_ENV, raising=False)

    reply, name = judge.anthropic_judge("q", "r", ["c"])
    assert reply == "1|MET|ok"
    assert name == "anthropic:claude-sonnet-5-5"
    assert not {"temperature", "top_p", "top_k"} & sent.keys()


def test_run_path_end_to_end_with_a_fake_sdk(monkeypatch, tmp_path):
    """Exercise --run without a network call, so the first real run does not fail on plumbing."""
    sent = []

    class Beta:
        def create(self, **kwargs):
            sent.append(kwargs)
            return types.SimpleNamespace(stop_reason="end_turn", content=[
                types.SimpleNamespace(type="thinking", thinking=""), types.SimpleNamespace(type="text", text="DRAFT")])

    class Messages:
        def create(self, **kwargs):
            return types.SimpleNamespace(content=[types.SimpleNamespace(type="text", text="1|MET|ok\n2|NOT_MET|no")])

    fake = types.ModuleType("anthropic")
    fake.APIError = type("APIError", (Exception,), {})
    fake.Anthropic = lambda: types.SimpleNamespace(beta=types.SimpleNamespace(messages=Beta()), messages=Messages())
    monkeypatch.setitem(sys.modules, "anthropic", fake)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    out = tmp_path / "results.json"
    monkeypatch.setenv("PROMPT_TEST_RESULTS", str(out))
    monkeypatch.setattr(sys, "argv", ["prompt_tests.py", "--run"])

    assert prompt_tests.main() == 0
    data = json.loads(out.read_text())
    assert len(data["results"]) == len(prompt_tests.load_cases())
    first = data["results"][0]
    assert first["output"] == "DRAFT"
    assert first["grading"]["criteria_met"] == 1
    assert all(call["fallbacks"] == "default" and "temperature" not in call for call in sent)


def test_claude_cli_strips_api_key_and_disables_tools(monkeypatch):
    calls = []

    def run(cmd, **kwargs):
        calls.append((cmd, kwargs))
        return types.SimpleNamespace(returncode=0, stdout=json.dumps({"is_error": False, "result": "1|MET|ok"}))

    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-should-not-pass")
    assert judge.run_claude_cli("hello", "claude-sonnet-5-5", run=run) == "1|MET|ok"
    cmd, kwargs = calls[0]
    assert cmd[cmd.index("--tools") + 1] == ""
    assert "--system-prompt" in cmd
    assert "ANTHROPIC_API_KEY" not in kwargs["env"]
    assert kwargs["input"] == "hello"


@pytest.mark.parametrize("stdout,code", [("not json", 0), (json.dumps({"is_error": True}), 0), ("", 1)])
def test_claude_cli_failures_raise(stdout, code):
    def run(cmd, **kwargs):
        return types.SimpleNamespace(returncode=code, stdout=stdout)

    with pytest.raises(RuntimeError):
        judge.run_claude_cli("hello", "m", run=run)


def test_existing_evidence_is_rejected_before_model_use(monkeypatch, tmp_path):
    out = tmp_path / "historical.json"
    out.write_text("historical evidence\n")
    monkeypatch.setattr(prompt_tests, "run_model", lambda *_: pytest.fail("must not call model"))
    monkeypatch.setattr(sys, "argv", ["prompt_tests.py", "--run", "--output", str(out)])
    with pytest.raises(SystemExit) as exc:
        prompt_tests.main()
    assert exc.value.code == 2
    assert out.read_text() == "historical evidence\n"


def test_targeted_rerun_excludes_unselected_cases(monkeypatch, tmp_path):
    calls = []
    selected = "performance-2"
    out = tmp_path / "rerun.json"
    monkeypatch.setattr(prompt_tests, "run_model", lambda prompt, _: calls.append(prompt) or "draft")
    monkeypatch.setattr(judge, "grade_response", lambda *args: types.SimpleNamespace(
        criteria_met=0, criteria_failed=0, criteria_unknown=1, error=None, judge_name="fake",
        to_dict=lambda: {"criteria_unknown": 1}))
    monkeypatch.setattr(sys, "argv", ["prompt_tests.py", "--run", "--case", selected, "--output", str(out)])
    assert prompt_tests.main() == 0
    assert len(calls) == 1
    assert [r["id"] for r in json.loads(out.read_text())["results"]] == [selected]


def test_unknown_rerun_case_fails_before_model_use(monkeypatch):
    monkeypatch.setattr(prompt_tests, "run_model", lambda *_: pytest.fail("must not call model"))
    monkeypatch.setattr(sys, "argv", ["prompt_tests.py", "--run", "--case", "missing-fixture"])
    with pytest.raises(SystemExit) as exc:
        prompt_tests.main()
    assert exc.value.code == 2


def test_model_failure_records_evidence_and_fails_the_run(monkeypatch, tmp_path):
    out = tmp_path / "failed-run.json"
    monkeypatch.setattr(prompt_tests, "run_model", lambda *_: "ERROR: synthetic provider failure")
    monkeypatch.setattr(judge, "anthropic_judge", lambda *_: pytest.fail("must not grade a failed model call"))
    monkeypatch.setattr(sys, "argv", ["prompt_tests.py", "--run", "--case", "performance-2", "--output", str(out)])
    assert prompt_tests.main() == 1
    data = json.loads(out.read_text())
    record = data["results"][0]
    assert record["grading"]["error"] and record["output"] is None
    assert record["execution"]["model_call"]["status"] == "failed"
    assert record["execution"]["judge_call"]["status"] == "skipped"
    assert data["execution_summary"]["model_calls_succeeded"] == 0
    assert "not evidence about model quality" in data["evaluation_status"]


AUTH_ENVELOPE = json.dumps({"type": "result", "is_error": True, "stop_reason": "stop_sequence",
                            "result": "Failed to authenticate: OAuth session expired and could not be refreshed"})


def fake_cli(stdout, returncode):
    """Run the real envelope parsing against a canned CLI reply, with no subprocess."""
    real = judge.run_claude_cli_detailed
    reply = types.SimpleNamespace(returncode=returncode, stdout=stdout)
    return lambda prompt, model: real(prompt, model, run=lambda *a, **k: reply)


def test_cli_authentication_failure_is_classified_not_graded(monkeypatch, tmp_path):
    """An expired sign-in produces infrastructure evidence, never a model output or a criterion verdict."""
    out = tmp_path / "auth-blocked.json"
    monkeypatch.setattr(judge, "run_claude_cli_detailed", fake_cli(AUTH_ENVELOPE, 1))
    monkeypatch.setattr(judge, "claude_code_judge", lambda *_: pytest.fail("must not grade a failed model call"))
    monkeypatch.setattr(sys, "argv", ["prompt_tests.py", "--run", "--backend", "claude-code",
                                      "--case", "performance-2", "--case", "hr-operations-4", "--output", str(out)])
    assert prompt_tests.main() == 1
    data = json.loads(out.read_text())
    assert data["execution_summary"]["model_call_failures"] == {"authentication": 1}
    for record in data["results"]:
        call = record["execution"]["model_call"]
        assert (call["status"], call["failure_kind"], call["exit_code"]) == ("failed", "authentication", 1)
        assert record["output"] is None
        assert record["grading"]["criteria_met"] == record["grading"]["criteria_failed"] == 0


def test_cli_success_records_serving_model(monkeypatch, tmp_path):
    envelope = json.dumps({"is_error": False, "result": "DRAFT", "modelUsage": {"claude-opus-5-5": {}}})
    out = tmp_path / "ok.json"
    monkeypatch.setattr(judge, "run_claude_cli_detailed", fake_cli(envelope, 0))
    monkeypatch.setattr(judge, "claude_code_judge", lambda *_, **kwargs: ("1|MET|ok", "claude-code:test"))
    monkeypatch.setattr(sys, "argv", ["prompt_tests.py", "--run", "--backend", "claude-code",
                                      "--case", "performance-2", "--output", str(out)])
    prompt_tests.main()
    record = json.loads(out.read_text())["results"][0]
    assert record["output"] == "DRAFT"
    assert record["execution"]["model_call"]["serving_models"] == ["claude-opus-5-5"]
    assert record["execution"]["judge_call"]["status"] == "success"


@pytest.mark.parametrize("message,kind", [
    ("Failed to authenticate: OAuth session expired", "authentication"),
    ("Invalid API key", "authentication"),
    ("Usage limit reached", "rate_limit"),
    ("Connection reset by peer", "transport"),
    ("Request timed out", "transport"),
    ("Something unexpected", "cli_error"),
])
def test_failure_classification(message, kind):
    assert judge.classify_failure(message) == kind


def test_error_messages_are_redacted_before_they_become_evidence():
    cleaned = judge.safe_message("bad key sk-ant-api03-abcdefghijklmnop and Bearer abc.def " + "x" * 40)
    assert "sk-ant" not in cleaned and "abc.def" not in cleaned and "x" * 40 not in cleaned
    assert len(judge.safe_message("y " * 500)) <= 200


def test_api_failures_are_classified():
    record = prompt_tests.api_call_record("ERROR: AuthenticationError: invalid x-api-key", "m")
    assert record["failure_kind"] == "authentication"
    assert prompt_tests.api_call_record("ERROR: APIConnectionError: reset", "m")["failure_kind"] == "transport"
    assert prompt_tests.api_call_record("ERROR: stop reason max_tokens", "m")["failure_kind"] == "incomplete_output"
    assert prompt_tests.api_call_record("draft", "m")["status"] == "success"


def test_failed_judge_retains_evidence_and_stops_before_next_fixture(monkeypatch, tmp_path):
    calls = []

    def cli(prompt, model):
        calls.append(model)
        return {"ok": len(calls) == 1, "text": "DRAFT" if len(calls) == 1 else None,
                "exit_code": 0 if len(calls) == 1 else 1,
                "failure_kind": None if len(calls) == 1 else "authentication",
                "failure_message": None if len(calls) == 1 else "OAuth expired",
                "serving_models": [model] if len(calls) == 1 else []}

    out = tmp_path / "judge-failed.json"
    monkeypatch.setattr(judge, "run_claude_cli_detailed", cli)
    monkeypatch.setattr(sys, "argv", ["prompt_tests.py", "--run", "--backend", "claude-code",
                                      "--case", "performance-2", "--case", "performance-3", "--output", str(out)])
    assert prompt_tests.main() == 1
    data = json.loads(out.read_text())
    assert len(calls) == 2
    assert data["results"][0]["output"] == "DRAFT"
    assert data["results"][0]["execution"]["judge_call"]["failure_kind"] == "authentication"
    assert data["execution_summary"]["completed_evaluations"] == 0
    assert data["unattempted_cases"] == ["performance-3"]


def test_raw_judge_reply_and_both_serving_models_are_preserved(monkeypatch, tmp_path):
    case = next(c for c in prompt_tests.load_cases() if c["id"] == "performance-2")
    reply = "\n".join(f"{i+1}|UNCLEAR|synthetic parser test" for i in range(len(case["expected_behavior"])))
    calls = []

    def cli(prompt, model):
        calls.append(model)
        return {"ok": True, "text": "DRAFT" if len(calls) == 1 else reply, "exit_code": 0,
                "failure_kind": None, "failure_message": None, "serving_models": ["served-" + model]}

    out = tmp_path / "provenance.json"
    monkeypatch.setattr(judge, "run_claude_cli_detailed", cli)
    monkeypatch.setattr(sys, "argv", ["prompt_tests.py", "--run", "--backend", "claude-code",
                                      "--case", "performance-2", "--output", str(out)])
    assert prompt_tests.main() == 0
    data = json.loads(out.read_text())
    record = data["results"][0]
    assert record["judge_output"] == reply
    for kind in ("model_call", "judge_call"):
        execution = record["execution"][kind]
        assert execution["serving_models"] == ["served-" + execution["requested_model"]]
    assert data["execution_summary"]["completed_evaluations"] == 1


def test_unreadable_judge_is_not_a_completed_evaluation(monkeypatch, tmp_path):
    calls = []

    def cli(prompt, model):
        calls.append(model)
        return {"ok": True, "text": "DRAFT" if len(calls) == 1 else "no verdict lines", "exit_code": 0,
                "failure_kind": None, "failure_message": None, "serving_models": [model]}

    out = tmp_path / "unreadable.json"
    monkeypatch.setattr(judge, "run_claude_cli_detailed", cli)
    monkeypatch.setattr(sys, "argv", ["prompt_tests.py", "--run", "--backend", "claude-code",
                                      "--case", "performance-2", "--output", str(out)])
    assert prompt_tests.main() == 1
    data = json.loads(out.read_text())
    assert data["results"][0]["judge_output"] == "no verdict lines"
    assert data["execution_summary"]["completed_evaluations"] == 0
    assert data["execution_summary"]["judge_call_failures"] == {"unparseable_output": 1}


@pytest.mark.parametrize("text,stop", [("", "end_turn"), ("partial", "max_tokens")])
def test_empty_or_truncated_cli_output_is_not_success(text, stop):
    outcome = judge.run_claude_cli_detailed("p", "m", run=lambda *a, **k: types.SimpleNamespace(
        returncode=0, stdout=json.dumps({"is_error": False, "result": text, "stop_reason": stop})))
    assert outcome["ok"] is False
    assert outcome["failure_kind"] == "incomplete_output"
