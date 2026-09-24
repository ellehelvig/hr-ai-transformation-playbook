# Testing and evaluating HR AI systems

The job of testing is to find where the system breaks. This page covers building a test set, diagnosing failures, and monitoring after launch.

[← Workflow patterns](README.md)

Two parts of this portfolio demonstrate it: the playbook's [evaluation runner](../09-evals/README.md), with launch-blocking gates and an LLM judge checked against human labels, and Resolve's [evaluation methodology](https://github.com/ellehelvig/peopleops-resolution-agent/blob/main/docs/evaluation-methodology.md), with held-out cases, confidence bounds, and acceptance criteria.

## Build the test set from real work

Use the questions employees actually ask: messy, ambiguous, and emotional ones, not only easy ones. Cover routine requests, requests that look routine but carry a signal that changes how they must be handled, benign requests that resemble sensitive ones, attempts to misuse the system, and jurisdiction differences.

Keep a held-out set written by people who do not tune the system. A set written alongside the rules or prompts it tests shows regression safety, not generalization. Size the set by the error rate you need to rule out: with no failures in *n* cases, the 95% upper bound on the failure rate is about 3/*n*.

## Diagnose before changing anything

| Symptom | Likely cause |
|---|---|
| Right answer, wrong jurisdiction | Policies not selected by location metadata |
| Outdated policy in the answer | Superseded versions not excluded, or the source not refreshed |
| A concern handled as routine | Screening misses the wording; check against a sampled review |
| Too many escalations | Criteria too broad; confirm with specialists' judgment of samples, not a rate target |
| Takes an action it should not | A tool exists that should not, or scope is not enforced in code |
| Ignores what a tool returned | Tool output not structured for the model to use |
| Loops or stalls | No step limit |

Change one thing at a time, record why, and re-run the same cases plus the full suite. Several changes at once make it impossible to tell which one worked or what else it broke.

## What to evaluate

For answers: is every statement supported by the cited source; is it complete; is the tone right for the situation, including distress? For routing: harmful misses and unnecessary escalations, measured separately. For actions: did anything happen without the required approval?

## Monitoring after launch

- **Weekly:** review escalations and a random sample of requests that were not escalated.
- **Monthly:** re-run the full test set; check that policy sources are current.
- **Quarterly:** check whether answer quality differs across employee groups; review with Legal.
- **On any model, prompt, or tool change:** re-run everything.
- **Immediately:** incorrect policy information, an unauthorized action, or a confirmed missed concern becomes an [incident](../03-governance/incident-report-template.md) and a new test case.

## Launch gates

Set pass criteria before testing, with the accountable owners, by severity. Zero observed disclosures and zero approval bypasses on the test set are necessary but not sufficient: a clean result on a small set still leaves real uncertainty. Resolve's [acceptance criteria](https://github.com/ellehelvig/peopleops-resolution-agent/blob/main/docs/evaluation-methodology.md#acceptance-criteria-for-a-model-classifier) show how coverage, severity, and monitoring combine.
