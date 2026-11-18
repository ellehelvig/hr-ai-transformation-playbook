# Worked example: change management

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Ines Calloway, HR Transformation Lead, writes: "On 2 March we pilot an AI case-drafting assistant in the HR service center, sponsored by the CHRO. The team got a new case system in January. Draft the change plan and agent FAQ. After week 2, list agents who skip the tool so managers can follow up."

| Group | Size |
|---|---|
| Service center agents, US | 22 |
| Service center agents, Germany (works council) | 8 |
| HRBPs | 30 |
| Managers who raise cases | 180 |

## Output (abridged)

```markdown
## The change
Yesterday: agents write every case reply from scratch.
Tomorrow: the assistant drafts from the case history; the agent edits
and sends.
Decision zones: reply drafting, human with AI, agent approves every
send; benefits and leave answers, human-led.

## Impact by group
- Agents, US and Germany: process, tools, critical behaviors. High.
  Skill needed: checking drafts against policy. Flag: works council.
- HRBPs: escalation volume. Medium.
- Managers: reply speed. Low.

## Communication plan (DRAFT, not sent)
Agents, from their team lead after the CHRO kickoff, two weeks before
go-live: what the assistant does, the data it reads, that it is not
used to rate anyone, and how to flag a bad draft.
FAQ checked with lint_jd_language: no flags.

## Adoption measures
- Sustained use at day 90: agents using it in 3 of 4 weeks / 30.
  Expand above 70% if quality holds.
- First-pass quality: sent drafts with no rework / all sent drafts.
  Pause below the pre-pilot rate.
Germany (8) is below the threshold of 10, so usage is reported for
all 30 agents together.

## Change load
Agents: case system (January), assistant (March). Proposal: start once case system tickets settle; the CHRO decides.

## Decision rights calls
- Agent FAQ: drafts for sign-off, to Ines Calloway and the CHRO.
- List agents who skip the tool: refuses and routes, to the change
  lead; offers group usage and reasons for non-use instead.

## Metrics tracked
- Sustained use rate: not yet measured, day 90
- First-pass quality rate: GAP
- Support access ratio: remote versus on-site agents, 30 days

## Audit trail
- Inputs used: groups above. GAP: pre-pilot quality rate.
- Tools called: HRIS (group counts by site); LMS (completion counts);
  ask_governance_policy (notice duties; cited ai-use-policy
  principle 2); lint_jd_language (FAQ text).
- Items needing sign-off: messages (change lead, CHRO); expand,
  pause, or stop (CHRO).
- Open legal questions: works council consultation; Key dates rows
  EU AI Act, transparency and EU AI Act, AI literacy (Article 4) for
  the German agents.
```
