# Synthetic pilot evidence preflight

This offline Python tool makes missing evidence visible before a person reviews
an HR AI pilot. It implements a small subset of the
[adoption playbook](../04-enablement/adoption-playbook.md) and
[roadmap](../06-roadmap/README.md). It does not verify evidence, enforce access,
authorize rollout, or make employment decisions. It is not a model evaluation.

## Run the example

From the repository root, using Python 3.12 or later:

```bash
python 09-evals/pilot_evidence.py 09-evals/pilot-evidence-example.json
pytest 09-evals/test_pilot_evidence.py -q
```

The fictional example pauses for missing identity/access and Privacy reviews.
Its 100 cases take 20 baseline minutes each. Assisted effort includes preparation
(5), human review (10), rework (4), and escalation (2): 21 minutes per case.
Illustrative net capacity is approximately **-1.67 hours**. A faster draft does
not establish lower total effort. Setup, training, and evaluation costs remain
outside this calculation. There is no financial or headcount conclusion.

## Input contract

Use only fictional input. No employee, candidate, employer, career, or contact
information belongs here. The JSON schema has no free-text fields. Unknown keys,
duplicate keys, invalid states, partial effort records, and files over 64 KiB
are rejected. A `synthetic` label is a caller assertion, not a privacy filter.
Do not load sensitive files to test rejection.

| Field | Accepted values |
|---|---|
| `schema_version` | Integer `1` |
| `data_kind` | `synthetic` |
| `stage` | `rehearsal` or `rollout_review`; both use fictional data |
| `evidence` | Optional object; each documented key is `present`, `missing`, or `unknown` |
| `incidents` | Optional object; `cross_user_exposure` and `approval_bypass` are `clear`, `reported`, or `unknown` |
| `effort` | Optional object; all components below are required when supplied |

Required evidence keys are `tool_data_scope`, `operator_owner`, `baseline`,
`independent_evaluation`, `reviewer_capacity`, `human_channel`, and
`incident_owner`. The rollout review also requires `identity_access_review`,
`privacy_review`, and `technical_review`. An omitted evidence key is a gap.
`present` records the caller's assertion, without inspecting an artifact or
verifying an approval. These keys are not a complete operational checklist.

Effort fields are `case_count` (nonnegative integer), `baseline_minutes`,
`preparation_minutes`, `review_minutes`, `rework_minutes`, and
`escalation_minutes`. Minutes are average effort per case. Values must be finite
and nonnegative; booleans are rejected. Negative net capacity is preserved.
Missing effort yields `null`, not zero. Effort does not determine evidence status.

## Read the result

| Advisory status | Meaning |
|---|---|
| `stop_affected_processing` | A caller reported exposure or approval bypass. A human must review containment and response. |
| `pause_for_evidence` | A required evidence assertion is absent or an incident status is unresolved. |
| `human_review` | Required assertions are present and incidents asserted clear. A person must still inspect evidence and decide. |

Every result has `human_review_required: true` and `authorization_granted: false`.
Reported incidents take precedence over efficiency and other evidence gaps.
Invalid input exits `2` without a result. Valid advisory output exits `0`, even
when it says stop or pause. **Do not use exit `0` as a deployment gate.**

The tool reads one local file and prints a result. It makes no network calls,
edits no files, and writes to no HR system. This is not a protected audit log.
Output fields do not repeat caller-supplied free text. Terminal history, local
file permissions, and any surrounding AI service remain outside its controls.

## Copilot practice, not completed activity

Use the fictional example to practice in your own signed-in Copilot session:

1. Ask panel chat to explain why the example pauses despite positive draft speed.
2. Ask a second review to find a case where the schema could fail or mislead a user.
3. Reproduce the concern locally, then review any proposed change before accepting it.
4. Review the diff, run tests, and ask Copilot to summarize the actual change.

For a tool-free CLI review after normal GitHub authentication:

```bash
copilot --disable-builtin-mcps --available-tools= --sync-session=off \
  -p 'List boundary tests for an advisory synthetic pilot evidence checker. Never grant rollout approval. Reject invalid numeric inputs. Preserve negative net capacity. No tools or files.'
```

The CLI command is an exercise, not a recorded model-review result. The code
and its deterministic tests were prepared with Codex. These exercises are not
evidence of independent validation. Record the actual model, date, finding,
accepted change, and verification only after doing an exercise.
