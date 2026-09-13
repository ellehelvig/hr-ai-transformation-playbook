# Regulatory claims registry

Every dated or status-bearing legal claim in this repo gets a record here, one file per
claim. The record names the primary source, and where possible pins a verbatim quote from
it. `scripts/verify_claim_sources.py` then checks the registry mechanically.

The point is to make the repo's currency claim testable instead of asserted. A citation
that cannot be checked by a script is a promise. A citation with a quote that CI fetches
and compares is evidence.

## Why a registry and not just prose

Claims written only as prose cannot be diffed against a statute, carry no record of when
they were last checked, and give a reader no way to audit the repo. A structured record
fixes all three.

## Schema

| Field | Required | Notes |
|---|---|---|
| `id` | yes | Matches the filename. Stable, never reused. |
| `jurisdiction` | yes | `EU`, `UK`, `CA-ON`, `US-TX`, `US-NY-NYC`, and so on. |
| `topic` | yes | Short human label. |
| `statement` | yes | The claim as the repo makes it. One claim per record. |
| `status` | yes | One of: `in-force`, `enacted-not-yet-effective`, `pending`, `stayed`, `repealed`, `superseded`, `vacated`, `withdrawn`, `draft-guidance`. |
| `effective` | no | ISO date the specific obligation applies, not the act's general entry into force. |
| `primary_source.url` | yes | Must be https and must be a primary source. |
| `primary_source.citation` | yes | Statute, enrolled bill, rule, regulator page, or docket entry. |
| `primary_source.quote` | no | Verbatim text from the source. Once present, CI checks it. |
| `primary_source.retrieved` | with quote | ISO date the quote was taken. |
| `primary_source.archived` | no | Snapshot URL, so the audit trail survives link rot. |
| `asserted_in` | yes | Repo files that state this claim. Checked for existence. |
| `last_verified` | yes | ISO date a human opened the source and confirmed it, or `never`. |
| `verified_by` | yes | Who did that, or `unverified`. |
| `review_interval_days` | yes | How long before this claim goes stale. |
| `notes` | no | What is still unresolved about this record. |

## What the checks do

Offline, on every push:

- schema, unique ids, filename matches id, `asserted_in` files exist
- dates parse, `last_verified` is not in the future
- a claim past its `review_interval_days` fails the build
- no em dashes
- prints how many claims are anchored to a quote and how many a human has verified

Online, on a schedule rather than on every push, so a government website being down never
blocks a merge:

- fetches every `primary_source.url`
- asserts the `quote` still appears in it, after normalizing whitespace and quote marks
- a quote that no longer matches means either the source moved or the quote is wrong, and
  both need a human before anything resting on that claim is merged

## Adding or updating a claim

1. One claim per record. If a sentence in the docs makes two claims, it needs two records.
2. Cite the primary source. A law firm alert is a lead, never the citation.
3. Use the per-section applicability date for the obligation described, not the act's
   general entry into force.
4. State status precisely. A pending bill is never described as law.
5. Set `last_verified` only when you have personally opened the source and read it.

## Current state

This registry is new and incomplete. Claims found in `03-governance` that do not yet have
a record are listed in [BACKLOG.md](BACKLOG.md) with the file and line where they appear,
so nothing is silently dropped. The gap is meant to be visible and to shrink.
