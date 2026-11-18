# Worked example: HR AI first use case picker

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Marisol Quennell-Abe, VP People at Harbor & Pine (1,400 staff in four US states and Germany; Level 1; works council at the German entity), writes: "Seven ideas, room for two pilots. Priorities: the policy question backlog and hiring 40 engineers. Which first? Our HR technology lead owns governance."

## Output (abridged)

### First-pilot screen

- Passed: the four scored ideas below, and exit interview themes.
- Not a first pilot: resume ranking (ranks people) and a flight-risk score per engineer (scores people). Route: `fairness-audit-prep` and the governance owner; later only with an audit.
- Exit interview themes: eligibility hold (privacy review missing), not scored.

### Scoring table (prioritization matrix)

| Idea | Strat | Impact | Time | Data | Feas | Weighted | Tier | Risk | Reversible |
|---|---|---|---|---|---|---|---|---|---|
| Policy Q and A drafting | 4 | 4 | 4 | 4 | 4 | 4.00 | 1 | Medium | Yes |
| JD rewriting | 3 | 3 | 3 | 5 | 5 | 3.67 | 2 | Low | Yes |
| Manager onboarding guide | 4 | 3 | 2 | 4 | 5 | 3.61 | 2 | Low | Yes |
| Interview questions | 3 | 3 | 2 | 4 | 5 | 3.33 | 2 | Low | Yes |

JD rewriting: (3 x 0.25 + 3 x 0.20 + 3 x 0.15 + 5 x 0.15 + 5 x 0.15) / 0.90 = 3.30 / 0.90 = 3.67. Time scores are assumptions until measured.

### Recommended first pilots

**Pilot 1: policy Q and A drafting, HR reviews before sending.** The only Tier 1 idea.

- Success metric: median minutes per answered question, review and rework included, weekly, with every sent answer matching its cited policy on a sampled check; target [Set after baseline].
- Baseline: two weeks of manual handling, same question types.
- Phase gate, six weeks after launch: change against baseline, reviewers through literacy Modules 1 to 2, no material governance issue, sponsor briefed.
- Human sign-off point: an HR operations specialist approves every draft; the HR operations lead can pause.
- Hand-off: run `hr-ai-use-case-intake` for the full card and risk tier.

**Pilot 2: JD rewriting.** Top of Tier 2, Low risk, no integration, starter prompt in the library. Pay range text stays untouched. ...

### Decision rights calls

- Picks, metrics, gates: Drafts for sign-off, to Marisol Quennell-Abe and the HR technology lead.
- Resume ranking, flight-risk score: Refuses and routes, as above.

### Metrics this plan tracks

Pilots meeting their metric at the gate: first reading at the gate. Intake before launch: 0 of 2 cards signed today.

### Audit trail

- Inputs used: seven ideas, headcount by location, priorities (synthetic).
- Tools called: `ask_governance_policy` (approved tool categories). No employee records read.
- Items needing sign-off: picks, metrics, gates (VP People, HR technology lead).
- Open legal questions: works council consultation before Pilot 1 handles German staff questions; the EU AI Act, transparency (Article 50) row if drafts ever reach staff unreviewed.
