# Operating these agents as a product, not shipping and walking away

Building the tool is the easy half. This is the part that's easy to skip
and is exactly the part a "figure it out, own the outcome" role actually
needs: what it means to monitor adoption, diagnose failures, and turn
skeptics into sponsors once something is live, not just at launch.

## What "adopted" actually means for each tool

Adoption isn't call volume. A tool that gets called constantly but whose
output is ignored or overridden every time isn't adopted, it's tolerated.
The signal that matters is the override rate: how often does a human's
final decision diverge from what the tool surfaced?

| Tool | Adoption signal | Failure signal |
|---|---|---|
| Comp banding | % of banding conversations where the analyst references the tool's output in their final rationale | Override rate on the band_label with no documented reason; repeated `BLOCKED-BY-POLICY` flags on the same req (someone's routing around it, not reading it) |
| Resume screening | % of screens where the recruiter's stated decision cites specific evidence lines from the tool, not a gut call | High `no_evidence_found` rate on requirements that ARE actually in most resumes (signals the requirement extraction is mis-parsing that JD's format) |
| Recruiter intake | % of generated Boolean strings used with zero or one edit before a live search | Repeated manual rewrites of the same clause (signals a missing synonym entry, an easy fix, see `recruiter_intake/ENABLEMENT.md`) |
| Policy Q&A | % of governance questions in Slack/email that get answered with a citation from this tool instead of "let me check with someone" | `no_match: true` rate trending up over time (signals the corpus has a real gap, not just a phrasing mismatch) |

## Logging, without touching people data unnecessarily

Every call should log: timestamp, tool name, a hash (not the raw text) of
the input, the output's structured fields (band_label, evidence counts,
question count, result count) and latency. It should NOT log raw resume
text, raw JD text, or raw compensation figures into a general-purpose
analytics log, that data doesn't need to leave the calling context to
answer "is this tool working," and logging it anyway is exactly the kind
of unnecessary people-data handling this playbook's governance section
argues against. If a specific failure needs the raw input to debug, pull
it from the original conversation, don't duplicate it into a log store by
default.

## Failure triage, by severity

- **A tool returns wrong information that could affect a real decision**
  (e.g., comp banding matches the wrong benchmark row): treat as a Sev 2
  per `03-governance/incident-report-template.md`, fix within 3 business
  days, and check whether other in-flight decisions used the same bad
  match.
- **A tool silently under- or over-triggers a guardrail** (e.g., the
  historical-pay block doesn't fire when it should): treat as Sev 1, this
  is exactly the systemic-fairness-failure category that policy defines as
  24-hour, Legal + Privacy + HR Leadership.
- **A tool is technically correct but nobody's using it**: not an
  incident, a product problem. Go find out why (see below) before writing
  more code.

## Turning skeptics into sponsors

The realistic failure mode for a tool like this isn't a bug, it's a
comp analyst or recruiter who tried it once, didn't trust the output, and
quietly went back to doing it by hand. The fix for that isn't a better
demo, it's:

1. **Co-build, don't hand off.** Each `ENABLEMENT.md` in this folder is
   written as if I were sitting with that SME while they made their first
   edit to the tool. The goal of the first real use isn't "the tool worked,"
   it's "they changed something in it themselves and it still worked."
   That's the moment a tool stops being someone else's system.
2. **Show your work, always.** Every tool returns evidence (matched terms,
   band edges, cited sections), never a bare verdict. A skeptical SME can
   check the tool's reasoning against their own read of the resume or the
   policy doc in under a minute. Tools that hide their reasoning don't earn
   trust just because they're usually right.
3. **Track override rate as a conversation starter, not a scoreboard.** A
   high override rate isn't proof the tool is bad, it might mean the SME
   knows something the tool structurally can't (a candidate's off-resume
   context, an unwritten team norm). The point of tracking it is to go ask
   which one it is, then either fix the tool or write down the norm.
4. **Retire what doesn't get adopted.** If a tool's usage doesn't grow past
   its pilot group after a real push, that's a finding, not a failure to
   hide. Better to document why (wrong workflow fit, missing integration,
   trust gap that co-building didn't close) and redirect effort than to
   keep maintaining something nobody asked for a second time.

## Pilot-to-scale gate

Each tool should have one SME pilot partner before any broader rollout.
Graduation criteria: the SME has made at least one real edit to their
tool's data file unassisted, the override rate has a documented
explanation for its current level (not just a number), and there's a named
owner for triaging failures who isn't the person who built it, that last
one matters, a tool that only its author can debug isn't actually handed
off yet.
