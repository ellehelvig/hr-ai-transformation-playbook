# Use case prioritization matrix

Use this framework to score and rank AI use cases for your People Team. Use it to make assumptions and disagreements visible before committing resources.

**Reference decision tool, not a validated risk model.** All weights, scoring anchors, and priority thresholds are illustrative judgment aids. They do not establish legal eligibility or permission to deploy.

[Redesign the selected work](work-redesign-people-partner.md) → [Plan its pilot](../04-enablement/adoption-playbook.md)

---

## Eligibility before scoring

Record **eligible**, **hold**, or **stop**, the evidence, and the accountable reviewer before calculating any score. These are portfolio design gates, not a statement of legal requirements.

- **Purpose and accountability:** a defined task, intended users, and a named owner for meaningful human oversight.
- **Data and access:** a justified data need and an approved access and handling approach. Sensitive data without adequate oversight fails the gate.
- **Decision boundary:** no autonomous hiring, pay, termination, or other consequential employment decisions. Specify what the system may draft and what a person must decide.
- **Risk and evidence:** review the risk assessment and relevant evaluation failures. Unacceptable risks or failed stop-ship conditions block progression, including when a high business score is possible.

Missing evidence or unresolved safeguards means **hold**. An unacceptable design means **stop** until redesigned and reviewed. Neither receives a priority tier. Record the reason and owner; business value cannot override it. Eligibility allows comparison, not release: pilot and production gates still apply.

## Decision record to complete before scoring

| Question | Evidence to record | Decision owner |
|---|---|---|
| Value and alternatives | Problem, affected users, baseline, and why ordinary automation or process repair is insufficient | Business sponsor |
| Readiness and feasibility | Approved source versions, minimum data, access, dependencies, operating capacity | HR systems / IT |
| Employee impact | Who may benefit or be harmed, human-channel access, accessibility, employee feedback method | HR owner with employee input |
| Ownership and permissions | Sponsor, operator, reviewer authority, allowed actions, incident owner, review date, retirement owner | HR operations |
| Evaluation | Rubric, independent-case provenance where required, failures that stop work, reviewer capacity | HR specialists and technical partner |
| Adoption | Manager routine, practice time, support route, change in responsibilities, reasons for non-use | Enablement owner |

A blank or unknown gate remains **hold**. Copy this record with the [intake](intake-template.md), retain the supporting evidence, and record who accepted each gate.

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

## Completed fictional example: People Partner policy-drafting support

**Illustrative decision record. No pilot has been run.** Fictional owner: HR service delivery lead. Sponsor: Head of People. Review date: 10 October 2026. Next review: before any scope change.

- **Problem/value:** routine policy lookup competes with sensitive case handling. Baseline handling and review time are unknown; time saving is a hypothesis.
- **Smallest scope:** synthetic rehearsal of policy retrieval and draft review. Ordinary rules retrieve approved fictional policy; a person owns the final reply. Compare against improving search without AI.
- **Data/readiness:** fictional request and fictional eligibility fields only. No real records or employer documents. Policy owner verifies the source version. Technical partner must confirm an approved offline or sandbox path before rehearsal.
- **Employee impact:** no employee-facing answer during rehearsal. Invite practitioners and accessibility feedback before designing an employee pilot. Offer a human route in the target design.
- **Ownership/actions:** operator owns routing and incident handling; policy owner owns content; specialist owns sensitive matters. No approval, denial, HRIS write, diagnosis, or investigation is delegated.
- **Evaluation:** measure policy correctness, hidden-risk misses, false refusal, specialist load, and total reviewer time. New assistant-authored cases are development cases. Resolve's known failures do not satisfy the independent-evaluation gate.
- **Adoption:** proposed weekly practice on fictional cases, a manager briefing, and a route for reviewers to challenge drafts without penalty.
- **Decision:** **HOLD for employee-facing use**, because identity-bound access, independent evaluation, baseline, and operating approvals are missing. **Not scored; no priority tier.** A synthetic rehearsal may be planned separately after its narrower data/tool gates are documented. A hypothetical high value score cannot change the hold.
- **Next action:** HR owner takes this record into the [work redesign](work-redesign-people-partner.md), then the [pilot plan](../04-enablement/adoption-playbook.md). Record evidence and re-review before changing the decision.

This is a completed example of a useful decision to pause, not a simulated claim of approval.

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
Data quality can block an otherwise plausible use case. Record the evidence behind this score.

**Averaging away a failed gate.**
A high business score cannot authorize an unacceptable design. Relevant legal review remains part of the governance process; this matrix does not determine legal eligibility.

**Treating the matrix as the answer.**
It's a forcing function for structured conversation, not a substitute for judgment.
