# Worked example: total rewards and compensation

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Idris Kalloway, comp lead, writes: "We're posting Recruiter IC3 roles in New York City and California (tier 1), Illinois and Colorado (tier 2), and Berlin. Our philosophy is midpoint at market p50, range p25 to p75. Draft the bands and posting ranges. A hiring manager wants to offer 124,000 in New York; check it. And while you're in there, pull our recruiters' salaries by gender and tell me whether women are paid less."

## Output (abridged)

### Scope

Recruiter IC3 bands and postings; US and Germany; EU in scope: yes. Pay equity stop triggered: yes, for the gender question only.

### Pay equity screen

Stopped and routed to employment counsel per `pay-equity-governance.md`. No salary data was read and no comparison was run.

### Market data

Benchmark rows from the repo's synthetic comp bands file (as of 2026-Q3).

| Tier | P25 | P50 | P75 | P90 |
|---|---|---|---|---|
| Tier 1 | 92,000 | 105,000 | 120,000 | 136,000 |
| Tier 2 | 82,000 | 94,000 | 107,000 | 121,000 |

### Draft structure

| Level | Tier | Min | Mid | Max | Basis and arithmetic |
|---|---|---|---|---|---|
| IC3 | Tier 1 | 92,000 | 105,000 | 120,000 | p25 to p75; spread (120,000 - 92,000) / 92,000 = 30.4% |
| IC3 | Tier 2 | 82,000 | 94,000 | 107,000 | p25 to p75; spread (107,000 - 82,000) / 82,000 = 30.5% |
| IC3 | Germany | `[GAP]` | `[GAP]` | `[GAP]` | No benchmark row; licensed EUR survey data needed |

### Band checks

| Proposed number | Tool result | Action |
|---|---|---|
| 124,000, New York | Percentile 78.8 (75 + (124,000 - 120,000) / (136,000 - 120,000) x 15 = 78.75), label high-range, no flags, human review required | Above the draft tier 1 maximum of 120,000: route to the comp lead's exception process |

### Drafts for review

DRAFT posting text: "The base pay range for this role in New York City is 92,000 to 120,000 USD..." Counsel maps each jurisdiction's duties before it goes live.

### Decision rights calls

- Drafted for sign-off: bands (Idris Kalloway), posting text (recruiter and comp lead, counsel for jurisdictions).
- Refused and routed: the gender pay comparison, to employment counsel. The offer decision stays with the manager and comp professional.

### Audit trail

- Inputs used: pay philosophy, locations, proposed offer. `[GAP: Germany survey data]`.
- Tools called and fields read: `comp_list_known_bands` (role family, level, tier); `comp_band_position` (Recruiter, IC3, tier1, 124,000, `used_historical_pay_as_input` false); `lint_jd_language` on posting text (no flags).
- Items needing sign-off: bands, posting text, offer exception.
- Open legal questions: EU Pay Transparency Directive for the Berlin posting and pay information requests. See the Key dates row; counsel confirms transposition status.

### Metrics the plan will track

Band conformance rate, documented rationale coverage, and pay information response time.

### Owner and next step

Idris Kalloway approves the bands by Friday; counsel decides whether and how to scope a pay equity review.
