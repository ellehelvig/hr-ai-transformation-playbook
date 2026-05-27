# HR AI use case library

37 vetted use cases organized by HR function. Each entry includes the AI approach, effort/impact rating, key risks, and success metrics. Use this as a starting point — not every use case fits every organization.

**AI approach key:**
- **Agent** — autonomous multi-step task completion with tool use
- **Copilot** — AI assists a human who retains decision authority
- **Automation** — rule-based + AI for structured, repeatable workflows
- **Analytics** — AI-augmented data analysis and insight generation

---

## Talent acquisition

| Use case | AI approach | Business impact | Implementation effort | Key risk |
|---|---|---|---|---|
| Resume screening and scoring | Copilot | High | Medium | Bias amplification |
| Job description optimization | Copilot | Medium | Low | Over-standardization |
| Candidate sourcing from internal talent pools | Agent | High | Medium | Data freshness |
| Interview question generation by competency | Copilot | Medium | Low | Validity of competency mapping |
| Offer letter drafting | Automation | Medium | Low | Compliance with local law |
| Candidate disposition communications | Automation | Medium | Low | Tone consistency |
| Recruiter coaching on interview feedback quality | Copilot | High | Medium | Adoption resistance |
| Headcount forecasting from business plans | Analytics | High | High | Data quality in source systems |

### Spotlight: resume screening

**What it does:** AI scores inbound applications against a structured competency rubric, surfaces top candidates, and flags potential red flags for recruiter review — without making pass/fail decisions autonomously.

**What it does not do:** Reject candidates. Every disposition decision is made by a human recruiter.

**Metrics:**
- Time to first screen (target: ≤24 hrs from application)
- Recruiter review time per requisition
- Offer acceptance rate (proxy for quality-of-hire signal)
- Demographic parity across candidate pool scores (fairness audit)

---

## Onboarding

| Use case | AI approach | Business impact | Implementation effort | Key risk |
|---|---|---|---|---|
| Personalized onboarding plan generation | Agent | High | Medium | Role/team data quality |
| New hire Q&A assistant | Agent | High | Low | Policy accuracy, hallucination |
| Onboarding task automation (IT provisioning triggers) | Automation | High | High | System integration complexity |
| 30/60/90 day check-in synthesis | Analytics | Medium | Low | Survey fatigue |
| Manager onboarding prep guide | Copilot | High | Low | Template staleness |
| Buddy program matching | Analytics | Medium | Low | Thin data for new orgs |

### Spotlight: new hire Q&A assistant

**What it does:** Answers policy, benefit, and process questions from new hires within seconds, 24/7. Routes complex or sensitive questions to the right HR contact.

**What it does not do:** Make benefit elections on behalf of employees or interpret individual circumstances.

**Metrics:**
- CSAT on new hire experience (30-day survey)
- Volume of repetitive HR helpdesk tickets (target: reduce by 40%+)
- Time-to-productivity (manager-rated)
- Escalation rate (questions the agent couldn't resolve)

---

## Performance management

| Use case | AI approach | Business impact | Implementation effort | Key risk |
|---|---|---|---|---|
| Performance review draft generation | Copilot | High | Low | Over-reliance, generic output |
| Calibration prep — manager briefing doc | Copilot | High | Medium | Data access permissions |
| Goal-setting quality scoring | Analytics | Medium | Medium | Subjectivity of scoring rubric |
| Mid-year feedback synthesis | Analytics | Medium | Low | Feedback recency bias |
| PIP documentation drafting | Copilot | High | Low | Legal exposure if misused |
| Succession planning gap analysis | Analytics | High | High | Data completeness |

### Spotlight: calibration prep

**What it does:** Generates a pre-calibration briefing doc for each manager: team performance distribution, flight-risk flags, compensation positioning, and prior-cycle outcomes. Delivered 48 hours before calibration sessions.

**What it does not do:** Make rating recommendations.

**Metrics:**
- Calibration session duration (target: reduce by 20%)
- Rating distribution spread vs. prior year
- Manager satisfaction with calibration prep

---

## Learning and development

| Use case | AI approach | Business impact | Implementation effort | Key risk |
|---|---|---|---|---|
| Skills gap identification by role | Analytics | High | High | Skills taxonomy maintenance |
| Personalized learning path generation | Agent | High | Medium | LMS integration quality |
| Course content summarization | Copilot | Medium | Low | Copyright compliance |
| Compliance training completion prediction | Analytics | Medium | Low | Prediction accuracy floor |
| Manager effectiveness coaching | Copilot | High | Medium | Psychological safety concerns |
| Internal knowledge base Q&A | Agent | High | Medium | Knowledge freshness |

### Spotlight: personalized learning paths

**What it does:** Analyzes an employee's role, skills data, career goals (from performance system), and team context to recommend a 90-day learning path from available LMS content, external resources, and mentoring.

**What it does not do:** Mandate learning — all recommendations are advisory.

**Metrics:**
- LMS course completion rate (baseline vs. personalized)
- Skills assessment score changes at 90 days
- Internal mobility rate for employees who completed recommended paths
- Manager-rated skill improvement at next review cycle

---

## HR operations and employee experience

| Use case | AI approach | Business impact | Implementation effort | Key risk |
|---|---|---|---|---|
| HR helpdesk triage and response | Agent | High | Medium | Policy accuracy |
| Benefits enrollment guidance | Copilot | High | Low | Benefits complexity, legal |
| Leave request processing | Automation | Medium | Medium | Leave law variation by jurisdiction |
| Employee survey sentiment analysis | Analytics | High | Low | Interpretation subjectivity |
| Exit interview theme synthesis | Analytics | High | Low | Sample size at small orgs |
| Org design modeling | Analytics | High | High | Political sensitivity |

---

## People analytics

| Use case | AI approach | Business impact | Implementation effort | Key risk |
|---|---|---|---|---|
| Attrition risk scoring | Analytics | High | High | Data staleness, fairness |
| Workforce planning models | Analytics | High | High | Forecast uncertainty |
| Pay equity analysis | Analytics | High | Medium | Legal exposure if mishandled |
| Engagement driver analysis | Analytics | High | Medium | Correlation ≠ causation |
| Headcount vs. revenue ratio benchmarking | Analytics | Medium | Low | Benchmark selection bias |

---

## Notes on this library

- **Effort ratings** assume an organization with reasonably clean HRIS data and a dedicated HR tech team. Without that, add one level to every effort estimate.
- **Impact ratings** are for a 1,000+ employee organization. Smaller orgs may see lower absolute impact but faster time to value.
- Use the [prioritization matrix](prioritization-matrix.md) to score and rank these for your specific context.
- Submit new use cases via the [intake template](intake-template.md).
