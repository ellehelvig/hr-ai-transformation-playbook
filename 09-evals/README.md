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
