"""
judge.py

Grades an agent response against the `expected_behavior` criteria written into
hr-qa-agent-evals.yaml.

Why this exists
---------------
The eval suite used to score three things: did the agent refuse when it should,
did it escalate when it should, and was the response non-empty. All three are
substring checks. None of them asks whether the answer was *correct*.

Meanwhile every one of the 29 cases in the YAML already carries an
`expected_behavior` list, written by hand. Case r001 says: "States accrual rate
clearly", "Mentions that it may vary by tenure or location", "Cites policy
source", "Does not invent specific numbers not in policy docs". The old runner
never read that field. An agent that confidently invented a PTO accrual rate
passed every gate, which for an HR policy agent is the primary risk, not a
secondary one.

This module reads those criteria and grades against them.

Design: the judge is an interface, not a vendor
-----------------------------------------------
`grade_response` takes a `judge_fn`. Three implementations ship here:

- `anthropic_judge`: calls the Anthropic Messages API. Used for real runs.
- `canned_judge`: reads verdicts from a JSON file. Used in CI and for grading
  transcripts offline, so the test suite never needs a network call or a key.
- `keyword_judge`: a deliberately weak heuristic, kept only as the fallback
  when no judge is configured, and it reports itself as low-confidence so its
  output is never mistaken for a real grade.

Judges are not trustworthy by default
-------------------------------------
An LLM judge is a measurement instrument, and an unvalidated instrument is not
evidence. `measure_judge_agreement` compares judge verdicts against human labels
in human-labels.json and reports raw agreement plus Cohen's kappa, so a run can
state how much the judge should be believed. Agreement below roughly 0.6 kappa
means the judge output belongs in the "needs human review" pile rather than in a
pass rate. See 09-evals/README.md.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

JUDGE_MODEL_ENV = "EVAL_JUDGE_MODEL"
DEFAULT_JUDGE_MODEL = "claude-sonnet-5"

# Below this kappa, treat judge verdicts as unvalidated signal rather than
# scores. 0.6 is the conventional boundary for "substantial" agreement; it is a
# convention, not a law, and it is stated here so a reader can disagree with it
# explicitly instead of inheriting it silently.
MIN_TRUSTWORTHY_KAPPA = 0.6


@dataclass
class CriterionVerdict:
    criterion: str
    met: bool | None  # None means the judge could not tell
    rationale: str = ""


@dataclass
class JudgeResult:
    eval_id: str
    verdicts: list[CriterionVerdict] = field(default_factory=list)
    judge_name: str = "unknown"
    low_confidence: bool = False
    error: str | None = None

    @property
    def criteria_met(self) -> int:
        return sum(1 for v in self.verdicts if v.met is True)

    @property
    def criteria_failed(self) -> int:
        return sum(1 for v in self.verdicts if v.met is False)

    @property
    def criteria_unknown(self) -> int:
        return sum(1 for v in self.verdicts if v.met is None)

    def to_dict(self) -> dict:
        return {
            "eval_id": self.eval_id,
            "judge_name": self.judge_name,
            "low_confidence": self.low_confidence,
            "error": self.error,
            "criteria_met": self.criteria_met,
            "criteria_failed": self.criteria_failed,
            "criteria_unknown": self.criteria_unknown,
            "verdicts": [
                {"criterion": v.criterion, "met": v.met, "rationale": v.rationale}
                for v in self.verdicts
            ],
        }


JUDGE_PROMPT = """You are grading one response from an HR policy assistant against \
a checklist written by the HR team that owns the assistant.

Grade ONLY against the criteria given. Do not add your own. Do not reward or \
penalize style, length, or tone unless a criterion mentions it.

For each criterion answer exactly one of:
  MET        the response clearly satisfies it
  NOT_MET    the response clearly fails it
  UNCLEAR    you cannot tell from the response alone

Prefer UNCLEAR over guessing. A criterion like "cites policy source" is NOT_MET \
if no source appears, and UNCLEAR if something source-like appears but you \
cannot tell whether it is a real policy document.

<question>
{question}
</question>

<response>
{response}
</response>

<criteria>
{criteria}
</criteria>

Reply with one line per criterion, in the same order, formatted exactly:
<index>|<MET|NOT_MET|UNCLEAR>|<one sentence rationale>

Nothing else."""


def _parse_judge_reply(reply: str, criteria: list[str]) -> list[CriterionVerdict]:
    """Parse the judge's line-per-criterion reply.

    Tolerant by design: a malformed or missing line becomes UNCLEAR rather than
    a crash or a silent pass. A judge that returns garbage should show up as
    unknown verdicts, which the runner surfaces, not as criteria quietly marked
    met.
    """
    by_index: dict[int, CriterionVerdict] = {}
    for line in reply.strip().splitlines():
        parts = line.split("|", 2)
        if len(parts) < 2:
            continue
        raw_index, raw_verdict = parts[0].strip(), parts[1].strip().upper()
        rationale = parts[2].strip() if len(parts) > 2 else ""
        match = re.search(r"\d+", raw_index)
        if not match:
            continue
        index = int(match.group()) - 1
        if not 0 <= index < len(criteria):
            continue
        met = True if raw_verdict == "MET" else False if raw_verdict == "NOT_MET" else None
        by_index[index] = CriterionVerdict(criteria[index], met, rationale)

    return [
        by_index.get(i, CriterionVerdict(c, None, "judge did not return a verdict for this criterion"))
        for i, c in enumerate(criteria)
    ]


def anthropic_judge(question: str, response: str, criteria: list[str]) -> tuple[str, str]:
    """Call the Anthropic Messages API. Returns (reply_text, judge_name).

    Imported lazily so the rest of this module, and the whole test suite, work
    without the SDK installed. temperature=0 because a grader that disagrees
    with itself between runs cannot be used to detect regressions.
    """
    try:
        from anthropic import Anthropic
    except ImportError as exc:  # pragma: no cover - exercised only without the SDK
        raise RuntimeError(
            "anthropic package not installed. `pip install anthropic`, or use "
            "--judge canned / --judge none."
        ) from exc

    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError("ANTHROPIC_API_KEY is not set; use --judge canned for offline scoring.")

    model = os.environ.get(JUDGE_MODEL_ENV, DEFAULT_JUDGE_MODEL)
    client = Anthropic()
    numbered = "\n".join(f"{i + 1}. {c}" for i, c in enumerate(criteria))
    message = client.messages.create(
        model=model,
        max_tokens=1024,
        temperature=0,
        messages=[{
            "role": "user",
            "content": JUDGE_PROMPT.format(question=question, response=response, criteria=numbered),
        }],
    )
    text = "".join(block.text for block in message.content if getattr(block, "type", "") == "text")
    return text, f"anthropic:{model}"


def make_canned_judge(path: Path) -> Callable[[str, str, list[str]], tuple[str, str]]:
    """Build a judge that replays verdicts from a JSON file.

    Format: {"<eval_id>": ["MET", "NOT_MET", "UNCLEAR", ...]} with one verdict
    per criterion in YAML order, or the long form
    {"<eval_id>": [{"verdict": "MET", "rationale": "..."}]}.

    This is what makes the judge testable in CI. It also lets a reviewer grade
    a batch of transcripts by hand once and then re-run the scoring pipeline
    against those labels as many times as needed.
    """
    with open(path) as f:
        canned = json.load(f)

    def judge(question: str, response: str, criteria: list[str], eval_id: str = "") -> tuple[str, str]:
        entries = canned.get(eval_id, [])
        lines = []
        for i, entry in enumerate(entries[: len(criteria)]):
            if isinstance(entry, dict):
                verdict, rationale = entry.get("verdict", "UNCLEAR"), entry.get("rationale", "")
            else:
                verdict, rationale = str(entry), "from canned verdicts"
            lines.append(f"{i + 1}|{verdict}|{rationale}")
        return "\n".join(lines), f"canned:{path.name}"

    return judge


def keyword_judge(question: str, response: str, criteria: list[str]) -> tuple[str, str]:
    """Fallback when no judge is configured. Deliberately weak.

    Marks a criterion MET only when most of its content words appear in the
    response, which is a bad proxy for "the response satisfies this criterion"
    and will both over- and under-credit. It exists so the pipeline degrades to
    something rather than nothing, and every result it produces is flagged
    low_confidence so it cannot be reported as a grade. Do not use it to make a
    launch decision.
    """
    stop = {
        "the", "a", "an", "and", "or", "to", "of", "in", "is", "are", "it", "that",
        "not", "does", "do", "with", "for", "on", "as", "be", "may", "its",
    }
    lowered = response.lower()
    lines = []
    for i, criterion in enumerate(criteria):
        words = [w for w in re.findall(r"[a-z]+", criterion.lower()) if w not in stop and len(w) > 3]
        if not words:
            lines.append(f"{i + 1}|UNCLEAR|no content words in criterion")
            continue
        hits = sum(1 for w in words if w in lowered)
        verdict = "MET" if hits / len(words) >= 0.6 else "UNCLEAR"
        lines.append(f"{i + 1}|{verdict}|{hits}/{len(words)} criterion words present, keyword heuristic only")
    return "\n".join(lines), "keyword-heuristic"


def grade_response(
    eval_case: dict,
    response: str,
    judge_fn: Callable[..., tuple[str, str]],
) -> JudgeResult:
    """Grade one response against its own expected_behavior criteria."""
    eval_id = eval_case.get("id", "")
    criteria = eval_case.get("expected_behavior") or []
    if not criteria:
        return JudgeResult(eval_id, [], "no-criteria", low_confidence=True,
                           error="eval case has no expected_behavior to grade against")

    if response.startswith("ERROR:"):
        return JudgeResult(
            eval_id,
            [CriterionVerdict(c, None, "agent did not respond") for c in criteria],
            "not-run", low_confidence=True, error=response,
        )

    try:
        # Canned judges need the eval id to look up verdicts; live judges don't
        # take it. Try the richer signature first.
        try:
            reply, judge_name = judge_fn(eval_case["input"], response, criteria, eval_id=eval_id)
        except TypeError:
            reply, judge_name = judge_fn(eval_case["input"], response, criteria)
    except Exception as exc:  # noqa: BLE001 - a judge failure must not abort the run
        return JudgeResult(
            eval_id,
            [CriterionVerdict(c, None, "judge call failed") for c in criteria],
            "error", low_confidence=True, error=f"{type(exc).__name__}: {exc}",
        )

    verdicts = _parse_judge_reply(reply, criteria)
    return JudgeResult(
        eval_id, verdicts, judge_name,
        low_confidence=judge_name == "keyword-heuristic",
    )


# ── Judge validation ─────────────────────────────────────────────────────────


def cohens_kappa(judge: list[bool | None], human: list[bool | None]) -> float | None:
    """Cohen's kappa over the pairs where both labelled MET or NOT_MET.

    Raw agreement is misleading on skewed data: if 90 percent of criteria are
    met, a judge that answers MET every time scores 0.9 agreement while
    carrying no information. Kappa corrects for agreement expected by chance.

    Returns None when there are no comparable pairs. Returns 1.0 when both
    raters are constant and identical, which is degenerate rather than good;
    the caller should look at the pair count too.
    """
    pairs = [(j, h) for j, h in zip(judge, human, strict=True) if j is not None and h is not None]
    if not pairs:
        return None
    n = len(pairs)
    observed = sum(1 for j, h in pairs if j == h) / n

    j_true = sum(1 for j, _ in pairs if j) / n
    h_true = sum(1 for _, h in pairs if h) / n
    expected = j_true * h_true + (1 - j_true) * (1 - h_true)

    if expected == 1.0:
        return 1.0 if observed == 1.0 else 0.0
    return (observed - expected) / (1 - expected)


def measure_judge_agreement(judge_results: list[JudgeResult], human_labels: dict) -> dict:
    """Compare judge verdicts against human labels, per criterion.

    human_labels format: {"<eval_id>": ["MET", "NOT_MET", ...]} in YAML criterion
    order. Only ids present in both are compared, so a partial labelling effort
    is useful immediately; label 5 cases, get a kappa on 5 cases, and the report
    says the sample was 5.
    """
    def to_bool(v) -> bool | None:
        s = str(v).strip().upper()
        return True if s == "MET" else False if s == "NOT_MET" else None

    judge_flat: list[bool | None] = []
    human_flat: list[bool | None] = []
    compared_ids = []

    for result in judge_results:
        labels = human_labels.get(result.eval_id)
        if not labels:
            continue
        compared_ids.append(result.eval_id)
        for verdict, label in zip(result.verdicts, labels, strict=False):
            judge_flat.append(verdict.met)
            human_flat.append(to_bool(label))

    comparable = [(j, h) for j, h in zip(judge_flat, human_flat, strict=True)
                  if j is not None and h is not None]
    kappa = cohens_kappa(judge_flat, human_flat)
    raw = (sum(1 for j, h in comparable if j == h) / len(comparable)) if comparable else None

    if kappa is None:
        interpretation = "no comparable judge/human pairs; label some cases in human-labels.json"
    elif kappa >= MIN_TRUSTWORTHY_KAPPA:
        interpretation = (
            f"kappa {kappa:.2f} at or above {MIN_TRUSTWORTHY_KAPPA}: judge verdicts are "
            "usable as a signal, still not a substitute for review on sensitive cases"
        )
    else:
        interpretation = (
            f"kappa {kappa:.2f} below {MIN_TRUSTWORTHY_KAPPA}: do NOT report judge verdicts "
            "as a pass rate. Treat them as review prompts and fix the rubric or the judge "
            "prompt first"
        )

    return {
        "cases_compared": len(compared_ids),
        "case_ids_compared": compared_ids,
        "criteria_compared": len(comparable),
        "raw_agreement": round(raw, 3) if raw is not None else None,
        "cohens_kappa": round(kappa, 3) if kappa is not None else None,
        "min_trustworthy_kappa": MIN_TRUSTWORTHY_KAPPA,
        "judge_trustworthy": bool(kappa is not None and kappa >= MIN_TRUSTWORTHY_KAPPA),
        "interpretation": interpretation,
    }
