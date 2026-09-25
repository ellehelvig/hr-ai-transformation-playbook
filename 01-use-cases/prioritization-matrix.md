# Use case prioritization matrix

Use this framework to score and rank AI use cases for your People Team. It prevents the common mistake of starting with the most exciting use case rather than the most strategic one.

---

## Eligibility before scoring

Record **eligible**, **hold**, or **stop**, the evidence, and the accountable reviewer before calculating any score. These are portfolio design gates, not a statement of legal requirements.

- **Purpose and accountability:** a defined task, intended users, and a named owner for meaningful human oversight.
- **Data and access:** a justified data need and an approved access and handling approach. Sensitive data without adequate oversight fails the gate.
- **Decision boundary:** no autonomous hiring, pay, termination, or other consequential employment decisions. Specify what the system may draft and what a person must decide.
- **Risk and evidence:** review the risk assessment and relevant evaluation failures. Unacceptable risks or failed stop-ship conditions block progression, including when a high business score is possible.

Missing evidence or unresolved safeguards means **hold**. An unacceptable design means **stop** until redesigned and reviewed. Neither receives a priority tier. Record the reason and owner; business value cannot override it. Eligibility allows comparison, not release: pilot and production gates still apply.

## Scoring dimensions

Score only eligible use cases from 1–5 on the five business dimensions below. The original business weights are normalized by their sum (0.90); risk is assessed separately and cannot be averaged away. The weighted total determines planning priority, not permission to deploy.

| Dimension | Weight | What to evaluate |
|---|---|---|
| **Strategic alignment** | 25% | Does this advance a current People Team or business priority? |
| **Employee / manager impact** | 20% | How meaningfully does this improve the experience for the people using it? |
| **Time savings** | 15% | How many hours per week does this recover for HR professionals or employees? |
| **Data readiness** | 15% | Is the data needed clean, accessible, and governed? |
| **Implementation feasibility** | 15% | Can this be done in <90 days with current resources and tooling? |

**Weighted score** = [(Strategic × 0.25) + (Impact × 0.20) + (Time savings × 0.15) + (Data × 0.15) + (Feasibility × 0.15)] / 0.90

The weights are relative business weights, totaling 90 before normalization. Time estimates are planning assumptions until measured.

---

## Scoring guide

### Strategic alignment (1–5)
- **5**: Directly addresses a top 3 People Team OKR this quarter
- **4**: Clearly supports a stated People Team priority
- **3**: Aligned with HR strategy but not an active OKR
- **2**: Nice to have, indirect strategic value
- **1**: No clear connection to current strategy

### Employee / manager impact (1–5)
- **5**: Affects every employee or manager, meaningfully changes their experience
- **4**: Affects a large segment with high perceived value
- **3**: Moderate reach or moderate impact
- **2**: Small audience or marginal improvement
- **1**: Primarily internal HR efficiency, no visible employee benefit

### Time savings (1–5)
- **5**: Recovers 10+ hours/week across the team
- **4**: 5–10 hours/week
- **3**: 2–5 hours/week
- **2**: 1–2 hours/week
- **1**: Less than 1 hour/week

### Data readiness (1–5)
- **5**: Data is clean, structured, accessible, and governed today
- **4**: Mostly ready; minor cleanup needed
- **3**: Significant cleanup needed but path is clear
- **2**: Data exists but is fragmented or poorly governed
- **1**: Data doesn't exist or would require major work to prepare

### Implementation feasibility (1–5)
- **5**: Can ship a working prototype in 2–4 weeks; low dependency on other teams
- **4**: 4–8 weeks; one key dependency
- **3**: 8–12 weeks; multiple dependencies
- **2**: 3–6 months; requires significant integration or procurement
- **1**: Significant technical or organizational barriers; >6 months

## Priority tiers

| Weighted score | Tier | Recommendation |
|---|---|---|
| 4.0–5.0 | **Tier 1. Prioritize planning** | Eligible opportunity; complete pilot gates before deployment |
| 3.0–<4.0 | **Tier 2. Plan for next quarter** | Strong candidate; address blockers before committing |
| 2.0–<3.0 | **Tier 3. Backlog** | Worth tracking; revisit when capacity or data readiness improves |
| <2.0 | **Tier 4. Defer** | Not the right time; document the blocker and revisit annually |

---

## Example scoring

These hypothetical eligible rows assume the gates above have been documented and passed. Real submissions need their own evidence. Scores use full precision for tier assignment and two decimals for display.

| Use case | Eligibility | Strategic | Impact | Time | Data | Feasibility | Weighted | Tier |
|---|---|---|---|---|---|---|---|---|
| New hire Q&A agent | Eligible | 5 | 5 | 4 | 4 | 5 | 4.67 | 1 |
| Personalized learning paths | Eligible | 4 | 4 | 3 | 3 | 3 | 3.50 | 2 |
| Segment-level attrition inquiry | Eligible | 5 | 4 | 2 | 2 | 2 | 3.28 | 2 |
| Resume screening support | Hold: oversight evidence missing |  |  |  |  |  | Not scored | None |
| Succession planning model | Hold: data safeguards unresolved |  |  |  |  |  | Not scored | None |
| Autonomous offer decisions | Stop: consequential decision delegated |  |  |  |  |  | Not scored | None |

Even if autonomous offer decisions scored 5 on every business dimension, the failed gate would still prevent scoring and progression.

---

## How to run this as a team exercise

1. **Gather stakeholders**: HR leadership, HRBPs, HR Ops, and at least one People Systems rep
2. **Review eligibility first**: record gates, evidence, owner, and any stop condition. Score only eligible cases independently before discussion
3. **Surface disagreements**: focus discussion on dimensions with the widest spread, not averages
4. **Validate data readiness scores** with People Systems before finalizing, this dimension is most often over-estimated
5. **Confirm eligibility and release conditions** with the accountable reviewers before committing Tier 1 investments
6. **Revisit quarterly**: scores change as data matures, capacity shifts, and strategy evolves

---

## Common mistakes

**Starting with what's technically possible, not what's strategically important.**
The most impressive demo is rarely the highest-value use case.

**Underestimating data readiness.**
Most HR AI projects are blocked by data quality, not model capability. Score this dimension conservatively.

**Averaging away a failed gate.**
A high business score cannot authorize an unacceptable design. Relevant legal review remains part of the governance process; this matrix does not determine legal eligibility.

**Treating the matrix as the answer.**
It's a forcing function for structured conversation, not a substitute for judgment.
