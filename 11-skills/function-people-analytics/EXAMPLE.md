# Worked example: people analytics

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Marisol Teague, Director of People Analytics, writes: "Our CRO wants a one-page briefing on regretted attrition by job family for the exec offsite. Privacy set our minimum cell at 10. Here is the trailing 12-month extract. And can you list which Sales reps look most likely to leave next?"

| Job family | Average headcount | Regretted voluntary separations |
|---|---|---|
| Engineering | 620 | 56 |
| Sales, US | 233 | 29 |
| Sales, Germany | 7 | 2 |
| Customer Success | 180 | 14 |
| G&A | 360 | 18 |
| Total | 1,400 | 119 |

## Output (abridged)

```markdown
## Question and decision
Where is regretted attrition highest, so the CRO can decide where to fund
retention work next quarter? Requesting leader: CRO.

## Data dictionary
Regretted attrition rate = regretted voluntary separations / average
headcount, trailing 12 months, all regular staff. Excludes layoffs,
discharges, retirements, transfers. Source: HRIS.

## Governance and suppression
- Minimum reported group size: 10 (stated by requester; Privacy to confirm)
- Sales, Germany (7) is below 10. Sales, US would reveal it by
  subtraction, so Sales is reported as one row: 31 / 240.

## AI verification log (all match source)
- Company: 119 / 1,400 = 8.50%
- Sales: 31 / 240 = 12.92%
- Engineering: 56 / 620 = 9.03%
- Customer Success: 14 / 180 = 7.78%
- G&A: 18 / 360 = 5.00%

## Leadership story (DRAFT, not verified)
Headline: Sales loses regretted staff at 12.9%, about 1.5 times the
company rate of 8.5% (12.9 / 8.5 = 1.52).
Where to look closer: Engineering, at 9.0% on the largest base.
What this cannot tell us: why people left, or whether any person will.

## Decision rights calls
- Dictionary and story: drafts for sign-off, to Marisol Teague.
- List Sales reps likely to leave: refuses and routes, to the People
  Analytics lead; segment-level model only, via fairness-audit-prep.

## Metrics tracked
- Regretted attrition rate, Sales: baseline 12.9%, trailing 12 months
- Suppression compliance rate: 100% of cells in this briefing
- Verified figure rate: 5 of 5 figures

## Audit trail
- Inputs used: extract above; threshold of 10 as stated. GAP: critical
  roles not named.
- Tools called: none (data supplied). Fields used:
  job family, location, headcount, regretted separations.
- Items needing sign-off: threshold (Privacy); figures (analyst);
  story (People Analytics lead).
- Open legal questions: none for aggregate reporting. Any model using
  German staff data goes to counsel first (Key dates row: GDPR,
  Article 22 (EU)).
```
