# Worked example: workforce planning and org design

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Teodora Vance, VP of Customer Support, writes: "Finance funded 150 support agent positions for FY27. Build base, constrained, and accelerated AI scenarios, show where the AI drafting assistant changes the work, and redraft the Support Specialist II job description. If AI moves fast, also tell me which agents we would cut."

| Segment | Headcount | Voluntary separation rate | Internal moves out |
|---|---|---|---|
| Support agents, US | 120 | 15% | 6 |
| Support agents, Germany | 40 | 15% | 2 |

## Output (abridged)

```markdown
## Supply and demand by scenario
Supply in 12 months with no hiring:
US 120 - 18 leavers - 6 moves = 96; Germany 40 - 6 - 2 = 32; total 128.
- Base: demand 165, gap 37 to hire (ticket volume up 8%)
- Constrained: demand 150, gap 22 (matches funded positions)
- Accelerated AI: demand 140, gap 12 (assistant saves 10% to 15% of
  agent time, from the pilot)
No scenario implies a reduction: 32 leavers and moves cover the drop
from 160 to 140.

## Task-level view
- Password resets: rules; support ops lead samples errors weekly.
- Tier-1 replies: assist; AI drafts, the agent edits and approves
  every send.
- Billing disputes: human-led.

## Skills gaps (segment level)
Tier-2 troubleshooting, gap of 12. Evidence: 40% of agents assessed
on real tickets; adjacent to tier-1 work.

## Options per gap
Build: reskill 10 tier-1 agents, about 4 months. Buy: hire 12, 52-day
median fill. Borrow: partner surge team. Bot: not suited.

## People impacts and routing
AI assigns ticket queues in Germany: Key dates row EU AI Act, high-risk
HR systems; works council consultation. Owner: counsel and labor
relations.

## Decision rights calls
- Scenario table: drafts for sign-off, to the FP&A partner.
- Redrafted job description: drafts for sign-off, to HR lead and TA.
- Name agents to cut: refuses and routes, to HR leadership and counsel
  with the fairness-audit-prep group comparison plan.

## Metrics tracked
- Internal fill rate for tier-2 roles: GAP, baseline not supplied
- Redeployment rate for eliminated roles: none eliminated
- Reduction impact ratio by group: not applicable, no reduction

## Audit trail
- Inputs used: table above; 150 funded positions. GAP: span data.
- Tools called: HRIS export (job family, site, separation type, move
  date); Finance export (funded positions); lint_jd_language on the
  redrafted description (flagged "digital native"; replaced).
- Items needing sign-off: assumptions (Finance); task map
  (practitioners, role owner); options (VP Support, HR lead).
- Open legal questions: works council consultation on queue assignment.
```
