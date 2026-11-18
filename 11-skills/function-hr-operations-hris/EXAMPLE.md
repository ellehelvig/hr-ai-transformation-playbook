# Worked example: HR operations and HRIS

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Marisol Tenney, HR operations lead at Harbor & Pine (1,400 staff in California, Illinois, NYC, Colorado, and Germany), writes: "We closed 2,900 tickets last quarter. I want triage rules and a plan to launch a policy Q and A assistant in January for US and German staff. Also, can the bot just update home addresses in the HRIS and close those tickets itself?"

| Category | Tickets | Share |
|---|---|---|
| Pay and payroll | 1,102 | 38% |
| Leave | 580 | 20% |
| Benefits | 435 | 15% |
| Job data changes | 348 | 12% |
| Ended in a sensitive category | 145 | 5% |
| Other | 290 | 10% |
| Total | 2,900 | 100% |

## Output (abridged)

### Scope

Triage rules and Q and A launch plan. Five locations. HRIS, case tool, knowledge base. Owner: Marisol Tenney. Not provided: who reviews knowledge base edits.

### Triage rules

| Step | Rule | Confirmed by |
|---|---|---|
| Sensitivity check | Harassment, discrimination, medical, accommodation, immigration, distress, safety: send to Employee Relations, no AI reply | Fixed rule |
| Classify | Category and urgency per prompt 3 | Tier 1 agent, every ticket in pilot |
| Route | Pay and payroll to payroll team; leave to leave specialist | Tier 1 agent |

### Q and A launch plan

- Answers only from articles with an owner and a last-reviewed date; "no source found" routes to a person.
- German staff see an "AI assistant" notice and the cited article (see the Key dates row EU AI Act, transparency).
- Eval set: 40 questions on pay, leave, and benefits per `09-evals/README.md` before launch.
- ...

### Decision rights calls in this output

| Item | Agent role | Routed to |
|---|---|---|
| Triage rules and launch plan | Drafts for sign-off | Marisol Tenney |
| Bot updates home addresses and closes tickets | Refuses and routes | People Systems owner: design a per-action confirmation gate, then the data steward makes changes through the change process |
| Who may edit the knowledge base | Refuses and routes | Marisol Tenney to name reviewers before launch |

### Metrics

| Metric | Baseline | Owner |
|---|---|---|
| Sensitive misroute rate | 12 of the 145 sensitive tickets were first routed to Tier 1: 12 / 145 = 8.3% | HR operations lead |
| Cited answer accuracy | Set in pilot month, sample of 50 | Content owners |
| Self-service resolution gap (German vs. English speakers) | Set in pilot month | HR operations lead |

### Audit trail

- Inputs used: ticket counts by category (synthetic), location headcounts.
- Tools called: case system export (category counts, tier closed at, reopen flag); HRIS (work location counts). No ticket text read.
- Items needing sign-off: triage rules (Marisol Tenney); launch (Marisol Tenney); address-change gate (People Systems owner).
- Open legal questions: whether the German works council must be consulted before launch; cross-border transfer of German ticket data to the US case tool. Both to counsel.
