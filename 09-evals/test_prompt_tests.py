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
