# Synthetic pilot review contract, version 1

[Quickstart and limits](README.md)

All files are UTF-8 JSON, with duplicate keys, non-finite constants, nesting deeper than 32, and individual files over 256 KiB rejected. There are at most four artifact references. IDs are lowercase letters/digits/hyphens, start with a letter, and are at most 64 characters. Source revisions are 40 lowercase hexadecimal characters; SHA-256 fields are 64. An identifier's shape does not prove provenance or remove personal information.

## Packet

Required keys: `schema_version: 1`, `data_kind: synthetic`, `packet_id`, `workflow_id`, `source_revision`, and `artifacts`. Unknown keys are rejected.

Each artifact reference has exactly `criterion_id`, `path`, `sha256`, `format`, `dataset_id`, `method_id`, and `observed_on`. Paths are normalized relative JSON paths inside the packet directory. Absolute paths, traversal, URLs, Windows drive paths, and symlinks are rejected. Artifacts must be regular files; on supported platforms the reader also rejects final symlinks at open time. This does not create a secure filesystem sandbox against concurrent changes.

Allowed criteria: `routing`, `privacy`, `review_controls`, `reviewer_capacity`. Duplicate criteria and paths are rejected. Missing criteria produce findings, never an implicit pass.

Optional keys:

- `assertions`: any subset of `privacy_review`, `identity_access_review`, `technical_review`, each `present`, `missing`, or `unknown`. These states are shown as caller assertions only and cannot produce verified approval.
- `reported_incidents`: a list containing `cross_user_exposure` and/or `approval_bypass`, without duplicates. These caller reports require stop consideration even without artifact support. They are not a claim that this tool observed an incident.

## Artifact

Required keys: `schema_version: 1`, `data_kind: synthetic`, `criterion_id`, `workflow_id`, `source_revision`, `dataset_id`, `method_id`, `observed_on`, `format`, and `results`. Unknown keys are rejected. Bindings must match the packet/reference. Each reference hashes the entire artifact file. Observation dates use `YYYY-MM-DD` and must not be in the future relative to the review date.

Under `checks-v1`, `results` has the following exact shape for each criterion:

| Criterion | Required results | Passing observation |
|---|---|---|
| `routing` | `regression` and `paraphrases`, each containing integer `passed`/`total`; integer `specialist_misses` | Both nonempty suites pass every case; no specialist misses |
| `privacy` | Integer `tested_cases`, `cross_user_exposures` | Nonempty test set; zero recorded exposures |
| `review_controls` | Integer `tested_cases`, `approval_bypasses` | Nonempty test set; zero recorded bypasses |
| `reviewer_capacity` | Integer `case_count`; numeric `required_review_minutes`, `available_review_minutes` | Nonempty workload; positive required effort; available effort meets required effort |

Counts are integers from zero through 1,000,000, excluding booleans. Denominators must be positive. Passed counts cannot exceed totals; specialist misses cannot exceed failed paraphrase cases; incident counts cannot exceed tested cases. Minutes must be finite, nonnegative, and at most 1,000,000,000. Zero required human-review effort is invalid. Capacity is not savings or a headcount estimate.

`resolve-rules-v1` is allowed only for routing. Its `results` is the preserved Resolve suite 1.0.0 report. The adapter reconciles baseline counts/rate/category totals/failures, paraphrase case count, passed flags, and miss-type summaries. A passed case cannot contradict its expected routing status. The report's timezone-aware generation date must match `observed_on`. The adapter does not independently establish that each expected outcome is correct or every passed flag is truthful.

## Policy and outcomes

Policy ID: `synthetic-pilot-review-v1`. Maximum observation age: 30 calendar days, inclusive. This is a demonstration threshold, not a legal deadline. Packets cannot change required criteria or thresholds.

- `stop`: a valid artifact records an exposure/bypass, or the caller reports either incident. Staleness does not clear an inspected incident. An unreadable or mismatched file is not interpreted as trustworthy incident evidence; it remains a blocker.
- `pause`: any required artifact is missing, invalid, stale, future-dated, inconsistent, or failing.
- `eligible_for_human_review`: all required artifacts satisfy this demonstration contract. Operational approvals remain unverified; production hold stays true.

Every report includes packet identity, review date, policy ID, source revision, hashes, bindings, findings, caller assertions, a digest, `authorization_granted: false`, and `production_hold: true`. Digests bind serialized report content; they are not signatures or independently trusted timestamps. Changing the chosen review date changes the digest. The optional date argument is operator-supplied, not a trusted clock.

## CLI and review records

`review` exits `0` only for eligible-for-human-review, `1` for pause/stop with a report, and `2` for invalid or unreadable packet input. Invalid artifacts inside a valid packet produce pause findings, not a traceback. Formats are `markdown`, `json`, and `html`. Standard error never repeats raw rejected file contents. Standard output contains validated IDs, relative paths, bindings, and extracted typed observations, so synthetic labeling is not a substitute for safe inputs.

`record` accepts `reviewer-00` through `reviewer-99` as fictional IDs and a proposed disposition. It can be more conservative but cannot clear blockers. It returns a JSON record to standard output; it does not create a file itself.

`verify-record` recomputes current findings and requires an exact match to the record's packet hash, review digest, date, policy, source revision, schema, and explicit limits. Undeclared fields and false identity/authorization claims fail matching. Both record commands exit `0` for successful creation/consistency checking, including a stop record, and `2` for invalid input or mismatch. Their exit codes never grant release permission.

The record is local, editable, unsigned, and based on a typed fictional identity. It cannot prove who reviewed anything, prevent coordinated replacement, enforce authorization, or protect an audit trail. Surrounding tooling must not treat any command's exit code as HR deployment approval.
