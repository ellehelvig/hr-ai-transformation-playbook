# HR agent eval framework

Evals are structured test cases that verify an agent behaves correctly across a range of inputs — including edge cases, adversarial inputs, and emotionally sensitive scenarios. Running evals before deployment and after any change is what separates a reliable production agent from a demo.

This directory contains eval sets for the HR Q&A agent and onboarding agent, plus a framework for writing your own.

---

## Files

| File | Contents |
|---|---|
| [hr-qa-agent-evals.yaml](hr-qa-agent-evals.yaml) | 30 test cases for the HR policy Q&A agent |
| [eval-rubric.md](eval-rubric.md) | Scoring rubric for human evaluation of agent responses |
| [run-evals.py](run-evals.py) | Script to run evals against a live agent endpoint |

---

## How evals work

Each eval case defines:
- **input** — what the user sends to the agent
- **expected_behavior** — what a correct response looks like (not exact text, but criteria)
- **should_escalate** — whether this input should trigger human handoff
- **should_refuse** — whether this input should be declined
- **category** — type of test (routine, edge-case, adversarial, sensitive)
- **notes** — why this case exists and what failure looks like

Evals are not unit tests — they don't check for exact string matches. They check for behavioral correctness, which requires a combination of automated checks and human spot-review.

---

## Running evals

```bash
pip install anthropic pyyaml requests

# Run against local agent
python run-evals.py --endpoint http://localhost:3000 --evals hr-qa-agent-evals.yaml

# Run against deployed agent
python run-evals.py --endpoint https://your-agent.railway.app --evals hr-qa-agent-evals.yaml

# Output: evals-results-[timestamp].json
```

Review results in `evals-results-*.json`. Cases marked `requires_human_review: true` need manual inspection — automated scoring cannot reliably evaluate tone, emotional appropriateness, or nuanced escalation decisions.

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
| Before initial deployment | Yes — full set |
| System prompt change | Yes — full set |
| Knowledge base update | Yes — cases relevant to changed content |
| Model version change | Yes — full set |
| Weekly production monitoring | Yes — random sample of 10 cases |
| After any escalation incident | Yes — add case covering the incident scenario |
