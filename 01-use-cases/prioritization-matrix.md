# Use case prioritization matrix

Use this framework to score and rank AI use cases for your People Team. It prevents the common mistake of starting with the most exciting use case rather than the most strategic one.

---

## Scoring dimensions

Score each use case from 1–5 on six dimensions. The weighted total determines priority tier.

| Dimension | Weight | What to evaluate |
|---|---|---|
| **Strategic alignment** | 25% | Does this advance a current People Team or business priority? |
| **Employee / manager impact** | 20% | How meaningfully does this improve the experience for the people using it? |
| **Time savings** | 15% | How many hours per week does this recover for HR professionals or employees? |
| **Data readiness** | 15% | Is the data needed clean, accessible, and governed? |
| **Implementation feasibility** | 15% | Can this be done in <90 days with current resources and tooling? |
| **Risk level (inverse)** | 10% | Score 5 = low risk, 1 = high risk. Be honest. |

**Weighted score** = (Strategic × 0.25) + (Impact × 0.20) + (Time savings × 0.15) + (Data × 0.15) + (Feasibility × 0.15) + (Risk inverse × 0.10)

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

### Risk level, score inversely (1–5)
- **5**: Low risk: no sensitive employee data, no employment decisions, easy to audit
- **4**: Low-medium: uses some personal data, decisions are advisory only
- **3**: Medium: touches employment decisions or sensitive data; requires legal review
- **2**: Medium-high: automated decisions, potential for bias, regulatory exposure
- **1**: High: autonomous decisions on hiring, compensation, termination, or sensitive data without human review

---

## Priority tiers

| Weighted score | Tier | Recommendation |
|---|---|---|
| 4.0–5.0 | **Tier 1. Start now** | High-confidence investment; prioritize in next planning cycle |
| 3.0–3.9 | **Tier 2. Plan for next quarter** | Strong candidate; address blockers before committing |
| 2.0–2.9 | **Tier 3. Backlog** | Worth tracking; revisit when capacity or data readiness improves |
| <2.0 | **Tier 4. Defer** | Not the right time; document the blocker and revisit annually |

---

## Example scoring

| Use case | Strategic | Impact | Time | Data | Feasibility | Risk⁻¹ | **Weighted** | Tier |
|---|---|---|---|---|---|---|---|---|
| New hire Q&A agent | 5 | 5 | 4 | 4 | 5 | 4 | **4.60** | 1 |
| Personalized learning paths | 4 | 4 | 3 | 3 | 3 | 4 | **3.55** | 2 |
| Attrition risk scoring | 5 | 4 | 2 | 2 | 2 | 3 | **3.25** | 2 |
| Resume screening AI | 3 | 3 | 3 | 4 | 3 | 2 | **3.00** | 2 |
| Succession planning model | 4 | 5 | 2 | 1 | 1 | 3 | **2.85** | 3 |
| Autonomous offer decisions | 2 | 2 | 3 | 3 | 2 | 1 | **2.05** | 4 |

---

## How to run this as a team exercise

1. **Gather stakeholders**: HR leadership, HRBPs, HR Ops, and at least one People Systems rep
2. **Score independently first**: each person scores all use cases before discussion; prevents anchoring
3. **Surface disagreements**: focus discussion on dimensions with the widest spread, not averages
4. **Validate data readiness scores** with People Systems before finalizing, this dimension is most often over-estimated
5. **Pressure-test risk scores** with Legal or your Privacy team before committing Tier 1 investments
6. **Revisit quarterly**: scores change as data matures, capacity shifts, and strategy evolves

---

## Common mistakes

**Starting with what's technically possible, not what's strategically important.**
The most impressive demo is rarely the highest-value use case.

**Underestimating data readiness.**
Most HR AI projects are blocked by data quality, not model capability. Score this dimension conservatively.

**Skipping the risk inverse score.**
Regulatory exposure in HR AI (EEOC guidance, GDPR, CCPA, NYC Local Law 144, Illinois AI Video Interview Act, Colorado AI Act) can kill a project months in. Score it first, not last.

*Specific regulations listed are current as of July 2026. Note Colorado: SB 189 (signed May 14, 2026) delayed the Colorado AI Act's effective date to January 1, 2027, and narrowed it substantially, dropping the duty of care and the deployer risk-management-program and impact-assessment requirements in favor of a disclosure/transparency-only regime. Weight it accordingly if scoring risk today. The landscape evolves rapidly, confirm current law for your jurisdiction(s) when assigning risk scores.*

**Treating the matrix as the answer.**
It's a forcing function for structured conversation, not a substitute for judgment.
