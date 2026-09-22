# Regulatory claims registry

> **GOVERNANCE / EVIDENCE** · Trace dated legal claims to primary sources and scheduled checks.

[← Governance](../README.md) · [Playbook home](../../README.md)

---

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

## Linking a claim to the prose that makes it

A date in a record is only useful if the documents asserting it say the same thing. Prose
cites a record with an HTML comment, which renders as nothing:

```markdown
Obligations for high-risk AI systems in employment apply from 2 December 2027.
<!--claim:eu-ai-act-annex3-employment-application-date-->
```

Without the marker, a date lives in the registry and is separately retyped in up to six
documents with nothing connecting the copies. Change one, forget the others, and the build
stays green while the repo contradicts itself. A silently wrong effective date is the worst
defect this repo can ship, because a reader acts on it.

With the marker, four things become mechanical:

- a marker naming an id that does not exist is a dangling citation and fails
- a marker in a file the record does not list in `asserted_in` fails, so the registry always
  knows every place its claim is made
- a file in `asserted_in` with no marker fails, catching prose that dropped the claim
- **the drift gate**: for a claim with an `effective` date, the marker's own paragraph has to
  state that date. Change the date in the record and every paragraph still showing the old
  one fails by name until it is fixed

The date may be written `2 December 2027`, `December 2, 2027`, `December 2027`, or
`2027-12-02`. Month and year without the day is accepted deliberately: prose legitimately
says "December 2027", and the drift worth catching is a wholly different date, not an
off-by-one day.

The last three rules apply only to claims that already carry at least one marker. Adoption is
per record. A claim with no marker anywhere is counted as an unmarked gap and printed on every
run, not failed, so the scheme can be taken up one record at a time and the gap shrinks
visibly.

## What the checks do

Offline, on every push:

- schema, unique ids, filename matches id, `asserted_in` files exist
- dates parse, `last_verified` is not in the future
- a claim past its `review_interval_days` fails the build
- marker rules and the drift gate, for every claim that carries a marker
- no em dashes
- prints how many claims are anchored to a quote, verified by a human, and linked by a marker

Online, on a schedule rather than on every push, so a government website being down never
blocks a merge:

- fetches every `primary_source.url`
- asserts the `quote` still appears in it, after normalizing whitespace and quote marks
- a quote that no longer matches means either the source moved or the quote is wrong, and
  both need a human before anything resting on that claim is merged
- a source that answers with a bot challenge, a status other than 200, or an empty page
  fails as "could not fetch", not as a wrong quote. EUR-Lex does this to every script, so
  EU records point at the Publications Office copy of the same Official Journal text and
  keep the EUR-Lex link in `notes`

## PDF sources

Most US state legislatures publish enacted acts as PDF only. Connecticut does, and so do
Colorado, Illinois and Texas, so a registry that could only check HTML would leave most of
the US backlog permanently unverifiable.

The checker detects a PDF by its magic bytes rather than a `.pdf` suffix, since legislature
sites serve PDFs from extensionless and query-string URLs, and extracts text with
pdfminer.six. Two quirks of statute PDFs are handled, both discovered on the real
Connecticut act:

- **Running headers land mid-sentence.** Extraction drops the page header and footer into
  whatever sentence spans the page break, so a quote crossing a boundary can never match.
  Short lines that repeat at the top or bottom of most pages are stripped first. Position
  and length both matter: without them, a repeated line of real statutory text gets stripped
  too.
- **Hyphens vanish at line breaks.** "employment-related" comes out as "employmentrelated"
  wherever the phrase happened to wrap. Comparison is therefore hyphen-insensitive on both
  sides. This cannot tell "re-creation" from "recreation", which is an acceptable trade for
  matching a sentence of statutory text.

Both are heuristics, and both fail in the safe direction: a quote that does not match is
reported to a human rather than passed. A scanned, image-only PDF produces no text and says
so, which means anchoring a different primary source rather than that one.

`scripts/test_verify_claim_sources.py` pins all of this against PDF fixtures generated in
the test run, so the logic is testable without fetching a government website.

Quoting from a PDF is still weaker evidence than a human reading it. The quote proves the
words are in the document; `last_verified` is what records that a person read them in
context. Extraction alone never sets `last_verified`.

## Adding or updating a claim

1. One claim per record. If a sentence in the docs makes two claims, it needs two records.
2. Cite the primary source. A law firm alert is a lead, never the citation.
3. Use the per-section applicability date for the obligation described, not the act's
   general entry into force.
4. State status precisely. A pending bill is never described as law.
5. Set `last_verified` only when you have personally opened the source and read it.
6. Add a `<!--claim:id-->` marker in every file listed in `asserted_in`, in the paragraph
   that states the claim.

## The unverified deadline

`last_verified: never` used to skip the staleness check entirely. Since every record says
`never`, the control the registry advertises ran on nothing while appearing to work. A field
nobody fills in is not a control.

Failing the build on all of them at once would block every merge, so the gate is dated rather
than absent: `UNVERIFIED_DEADLINE` in `scripts/verify_claim_sources.py` is **31 December
2026**. Until then, unverified records are counted and printed on every run. After it, they
fail the build.

The deadline is the commitment. Move it only with a reason worth writing down.

## Current state

This registry is new and incomplete. Claims found in `03-governance` that do not yet have
a record are listed in [BACKLOG.md](BACKLOG.md) with the file and line where they appear,
so nothing is silently dropped. The gap is meant to be visible and to shrink.
