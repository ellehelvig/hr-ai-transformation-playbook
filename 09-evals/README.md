# HR agent eval framework

Evals are structured test cases that verify an agent behaves correctly across a range of inputs, including edge cases, adversarial inputs, and emotionally sensitive scenarios. Running evals before deployment and after any change is what separates a reliable production agent from a demo.

This directory contains an eval set for the HR Q&A agent, plus a framework for writing your own. The same approach works for testing an [agent skill](../11-skills/README.md) before a team adopts it: write cases for the scenarios the skill's source template already covers, and compare the skill's output to the worked example.

---

## Files

| File | Contents |
|---|---|
| [hr-qa-agent-evals.yaml](hr-qa-agent-evals.yaml) | 29 test cases for the HR policy Q&A agent |
| [eval-rubric.md](eval-rubric.md) | Scoring rubric for human evaluation of agent responses |
| [run-evals.py](run-evals.py) | Script to run evals against a live agent endpoint |
| [evals-summary-example.txt](evals-summary-example.txt) | Example output from a pilot run. Shows what the runner produces, including a real flagged case |
| [evals-results-example.json](evals-results-example.json) | Full structured results behind the example summary above |
| [test_run_evals.py](test_run_evals.py) | Tests for the scorer and the exit-code gate; run with `pytest 09-evals -q` |

---

## How evals work

Each eval case defines:
- **input**: what the user sends to the agent
- **expected_behavior**: what a correct response looks like (not exact text, but criteria)
- **should_escalate**: whether this input should trigger human handoff
- **should_refuse**: whether this input should be declined
- **category**: type of test (routine, edge-case, adversarial, sensitive)
- **notes**: why this case exists and what failure looks like

Evals are not unit tests, they don't check for exact string matches. They check for behavioral correctness, which requires a combination of automated checks and human spot-review.

---

## Running evals

```bash
pip install -r ../requirements.txt

# Run against a local agent
python run-evals.py --endpoint http://localhost:3000 --evals hr-qa-agent-evals.yaml

# Run against a deployed agent, adversarial cases only
python run-evals.py --endpoint https://your-agent.example --evals hr-qa-agent-evals.yaml --category adversarial

# Score canned responses with no endpoint (CI, regression checks, grading
# transcripts exported from another tool). JSON mapping eval id -> response.
python run-evals.py --responses-file responses.json --evals hr-qa-agent-evals.yaml

# Output: evals-results-[timestamp].json and evals-summary-[timestamp].txt
```

**Exit code is the gate.** The runner exits 1 if any case fails a refusal gate, an escalation gate, or the agent was unreachable, so you can wire it into a deploy pipeline and let it block the release. Quality flags like `response_very_short` don't fail the build; they mark the case for human review. Pass `--no-fail-on-gates` if you only want the report.

**Endpoint contract.** The runner POSTs `{"messages": [{"role": "user", "content": ...}]}` and reads back OpenAI-style SSE streams, OpenAI chat-completion JSON, Anthropic Messages JSON, or any JSON object with a top-level `response`, `content`, `output`, `text`, or `answer` string. Plain text bodies work too. If your agent speaks something else, adapt `extract_text()` in the runner; it's one function.

Review results in `evals-results-*.json`. Cases marked `requires_human_review: true` need manual inspection, automated scoring cannot reliably evaluate tone, emotional appropriateness, or nuanced escalation decisions.

**The scorer has its own tests.** `pytest 09-evals -q` runs 11 tests that pin the behaviors that make this a gate rather than a vibes check: a correct refusal that says "I can't share my system prompt" is not marked as compliance, an answer that merely says "human resources" doesn't count as an escalation, and the shipped reference responses pass every gate while the recorded a003 failure trips it. CI runs these on every push.

---

## Grading correctness, not just safety

The runner's built-in scorer checks three things: did the agent refuse when it should, did it escalate when it should, and did it return content at all. All three are substring checks. None asks whether the answer was **right**.

That was a real hole. Every case in the YAML carries an `expected_behavior` list, written by hand. Case `r001` asks for "Cites policy source" and "Does not invent specific numbers not in policy docs". Nothing read that field, so an agent that confidently invented a PTO accrual rate passed every gate. For an HR policy agent, a wrong policy answer delivered fluently is the primary risk, not a secondary one.

`judge.py` grades responses against those criteria.

```bash
# Real run, needs ANTHROPIC_API_KEY
python run-evals.py --endpoint http://localhost:3000 --evals hr-qa-agent-evals.yaml --judge anthropic

# Offline: replay canned verdicts, and measure agreement with human labels
python run-evals.py --responses-file responses.json --evals hr-qa-agent-evals.yaml \
  --judge canned --judge-verdicts judge-verdicts-example.json \
  --human-labels human-labels-example.json
```

### The judge is an instrument, and an unvalidated instrument is not evidence

An LLM grading another LLM is a measurement, and a measurement nobody has checked is a number with a confidence interval of unknown width. Anyone can bolt an LLM judge onto an eval suite in an afternoon and report a pass rate; the part that makes it worth anything is being able to say how far the grader agrees with a person.

Pass `--human-labels` and the run reports raw agreement plus **Cohen's kappa** against your own labels. Kappa rather than raw agreement, because raw agreement lies on skewed data: when 90 percent of criteria are met, a judge that answers MET every time scores 0.9 agreement while carrying zero information. Kappa corrects for chance and scores that judge at 0.0.

Below kappa 0.6 the run says so in words, and judge verdicts should be read as review prompts rather than scores. Fix the rubric or the judge prompt before reporting a pass rate off them.

You do not need to label all 29 cases. Label a sample, get a kappa on that sample, and the report states the sample size. Start where a wrong grade costs most, which here means the `sensitive` and `adversarial` categories.

### What gates a deploy and what does not

| Signal | Blocks deploy? | Why |
|---|---|---|
| `FAILED_REFUSAL` | Yes | Agent complied with an adversarial input |
| `FAILED_ESCALATION` | Yes | Agent did not route a case that needed a human |
| `FAILED_EMPTY_RESPONSE` | Yes | No reading of an empty response where the agent did its job |
| `agent_error` | Yes | Unreachable agent |
| `JUDGE_CRITERIA_FAILED` | **No** | The judge has no measured kappa yet |
| `response_very_short` | No | A character count cannot tell terse-but-correct from incomplete |

`JUDGE_CRITERIA_FAILED` is deliberately not a gate. Blocking a deploy on an unvalidated grader is how a pipeline starts failing for reasons nobody can defend, which is how teams learn to ignore it. Once you have a kappa you trust, add `--fail-on-untrustworthy-judge` to CI so the judge itself is monitored for drift.

### Known limits

- One sample per case. These agents are stochastic and the suite does not yet measure run-to-run variance, so a single pass is weaker evidence than it looks. Run the set more than once before a launch decision.
- Refusal and escalation detection is still substring matching against a fixed phrase list, so a refusal worded outside that list reads as a failure. The scorer's own accuracy has not been measured against human labels the way the judge's now can be. That is the next gap to close.

---

## Writing new eval cases

Add cases to the YAML file following the existing format. Guidelines:

- Cover your highest-volume query types first
- Include at least 3 adversarial cases per agent
- Every escalation trigger in your system prompt should have at least 2 eval cases
- Update evals whenever you update the system prompt or knowledge base
- Minimum eval set size before production: 25 cases

---

## Eval cadence

| Trigger | Run evals? |
|---|---|
| Before initial deployment | Yes, full set |
| System prompt change | Yes, full set |
| Knowledge base update | Yes, cases relevant to changed content |
| Model version change | Yes, full set |
| Weekly production monitoring | Yes, random sample of 10 cases |
| After any escalation incident | Yes, add case covering the incident scenario |
