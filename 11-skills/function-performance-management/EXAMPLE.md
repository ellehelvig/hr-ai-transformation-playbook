# Worked example: performance management

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Rowan Pell, HRBP for Platform Engineering (84 people across California, Illinois, New York City, Colorado and Germany), writes: "Mid-year calibration is on 4 December. Ratings are developmental at mid-year and do not feed pay. Build me a calibration briefing, check the proposed ratings below for bias, and flag the bottom five so we can start PIPs in December."

| Group (People Analytics export, aggregate) | People | Proposed "Exceeds" |
|---|---|---|
| Women | 30 | 6 |
| Men | 54 | 16 |
| Total | 84 | 22 |

## Output (abridged)

### Task and owner

Calibration prep, mid-year cycle, no pay link. Decision owner: calibration lead, Inez Marlowe.

### Draft

DRAFT calibration briefing for Inez Marlowe:

- Rating definitions agreed before any name is discussed. "Exceeds" means two or more goals delivered above the stated measure, each backed by a dated ledger item.
- Individual discussion for proposed "Exceeds" (22) and "Below" (7): 29 people at 6 minutes each is 174 minutes, split over two sessions.
- Watch for a pull to the middle rating and for the strongest advocate winning over the strongest evidence.

...

### Checks run

| Check | Result | Action |
|---|---|---|
| Four-fifths screening flag | Women 6 / 30 = 20.0%. Men 16 / 54 = 29.6%. Ratio 20.0 / 29.6 = 0.68, below 0.80 | Screening flag only, not a finding. Groups this small need a statistical test; People Analytics runs it and interprets with counsel before 4 December, per `fairness-audit-prep` |
| Evidence covers full period | 3 managers' notes cover only October | Ask those managers to complete their ledgers |

### Decision rights calls

- Drafted for sign-off: the briefing (Inez Marlowe) and the screening flag (People Analytics).
- Refused and routed: "flag the bottom five." The agent does not rank or select named people. Routed to the calibration lead with the rating definitions. A PIP starts only after the manager and HRBP decide one is warranted and confirm no accommodation, leave or complaint is open.

### Audit trail

- Inputs used: aggregate counts above; rating scale; cycle dates. `[GAP: rating definitions not yet agreed]`.
- Tools called and fields read: People Analytics export (group, count, proposed rating level, aggregate only); `ask_governance_policy` (question on PIP sign-off; cited `ai-use-policy.md` principle 1).
- Items needing sign-off: briefing (calibration lead); flag interpretation (People Analytics).
- Open legal questions: Illinois HB 3773 (Public Act 103-0804) and EU AI Act, high-risk HR systems if any scoring tool is added later. See the Key dates rows; counsel confirms.

### Metrics the plan will track

- Evidence traceability rate for AI-assisted drafts this cycle.
- Top-rating selection ratio by group after calibration.
- Rating review request rate.

### Next step

Inez Marlowe decides the agenda; People Analytics reports on the flag by 2 December.
