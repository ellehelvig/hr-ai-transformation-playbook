"""Run prompt library templates on a real model and grade them against their own rules.

    python 09-evals/prompt_tests.py --list           # check fixtures against the library, offline
    python 09-evals/prompt_tests.py --run            # needs ANTHROPIC_API_KEY and `pip install anthropic`

Each fixture in prompt-fixtures.yaml fills one template's placeholders with
synthetic inputs, usually planting a trap the template says to avoid, such as
health context in calibration notes or an age reference in PIP evidence. The
filled prompt runs on the model under test, and the judge in judge.py grades
the output against the fixture's criteria.

The prompt text is read from 02-prompt-library at run time, so a test always
runs the template as currently written. Results record the model, the date,
and a hash of each filled prompt.

What a result means: one synthetic input, one run, graded by an LLM judge whose
agreement with human labels has not been measured. That is a smoke test, not a
benchmark. A prompt counts as tested only after a person reads the output and
records the model, date, and any change next to the prompt, as CLAUDE.md asks.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).parent
ROOT = HERE.parent
LIBRARY = ROOT / "02-prompt-library"
FIXTURES = HERE / "prompt-fixtures.yaml"
RESULTS = HERE / "prompt-test-results.json"
MODEL_ENV = "PROMPT_TEST_MODEL"
DEFAULT_MODEL = "claude-opus-5-5"

SECTION = re.compile(r"^## (\d+)\. (.+)$", re.MULTILINE)
FENCE = re.compile(r"^```\n(.*?)^```$", re.MULTILINE | re.DOTALL)


def load_library() -> dict[str, dict]:
    """Return {"<file stem>-<n>": {"title", "prompt"}} for every numbered prompt."""
    prompts = {}
    for path in sorted(LIBRARY.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        sections = list(SECTION.finditer(text))
        for i, match in enumerate(sections):
            end = sections[i + 1].start() if i + 1 < len(sections) else len(text)
            block = FENCE.search(text, match.end(), end)
            if block:
                prompts[f"{path.stem}-{match.group(1)}"] = {"title": match.group(2).strip(), "prompt": block.group(1)}
    return prompts


def fill(prompt: str, fills: dict) -> str:
    """Replace placeholders. A list value fills repeated placeholders in order."""
    for placeholder, value in fills.items():
        count = prompt.count(placeholder)
        if count == 0:
            raise ValueError(f"placeholder not in prompt: {placeholder}")
        if isinstance(value, list):
            if len(value) != count:
                raise ValueError(f"{placeholder} appears {count} times but {len(value)} values were given")
            for item in value:
                prompt = prompt.replace(placeholder, str(item).strip(), 1)
        else:
            prompt = prompt.replace(placeholder, str(value).strip())
    return prompt


def load_cases() -> list[dict]:
    library = load_library()
    cases = []
    for fixture in yaml.safe_load(FIXTURES.read_text(encoding="utf-8")):
        if fixture["prompt"] not in library:
            raise ValueError(f"unknown prompt id: {fixture['prompt']}")
        filled = fill(library[fixture["prompt"]]["prompt"], fixture["fills"])
        cases.append({"id": fixture["prompt"], "title": library[fixture["prompt"]]["title"], "trap": fixture["trap"],
                      "input": filled, "expected_behavior": fixture["criteria"],
                      "sha256": hashlib.sha256(filled.encode()).hexdigest()[:16]})
    return cases


def run_model(prompt: str, model: str) -> str:
    """Run one filled prompt. Returns the text, or a string starting with ERROR:."""
    import anthropic

    client = anthropic.Anthropic()
    try:
        response = client.beta.messages.create(
            model=model, max_tokens=16000, betas=["server-side-fallback-2026-07-01"], fallbacks="default",
            output_config={"effort": "medium"}, messages=[{"role": "user", "content": prompt}],
        )
    except anthropic.APIError as exc:
        return f"ERROR: {type(exc).__name__}: {exc}"
    if response.stop_reason != "end_turn":
        return f"ERROR: stop reason {response.stop_reason}"
    return "".join(block.text for block in response.content if block.type == "text")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--list", action="store_true", help="validate fixtures and list coverage, offline")
    parser.add_argument("--run", action="store_true", help="run every fixture on the model and grade it")
    args = parser.parse_args()

    library, cases = load_library(), load_cases()
    if not args.run:
        covered = {c["id"] for c in cases}
        print(f"{len(cases)} fixtures cover {len(covered)} of {len(library)} library prompts.")
        for prompt_id in sorted(library):
            status = "fixture   " if prompt_id in covered else "no fixture"
            print(f"  {status}  {prompt_id}  {library[prompt_id]['title']}")
        return 0

    sys.path.insert(0, str(HERE))
    import judge

    model = os.environ.get(MODEL_ENV, DEFAULT_MODEL)
    results = []
    for case in cases:
        output = run_model(case["input"], model)
        graded = judge.grade_response(case, output, judge.anthropic_judge)
        results.append({"id": case["id"], "title": case["title"], "trap": case["trap"],
                        "prompt_sha256": case["sha256"], "output": output, "grading": graded.to_dict()})
        print(f"{case['id']:28} met={graded.criteria_met} not_met={graded.criteria_failed} "
              f"unclear={graded.criteria_unknown}  {'(error)' if graded.error else ''}")

    output_path = Path(os.environ.get("PROMPT_TEST_RESULTS", RESULTS))
    output_path.write_text(json.dumps({
        "model": model, "judge_model": os.environ.get(judge.JUDGE_MODEL_ENV, judge.DEFAULT_JUDGE_MODEL),
        "run_at": datetime.now(timezone.utc).isoformat(),
        "note": ("One synthetic input per prompt, one run, graded by an unvalidated LLM judge. "
                 "Smoke test, not a benchmark."),
        "results": results,
    }, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
