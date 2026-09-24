# HR AI use case library

37 vetted use cases organized by HR function. Each entry includes the AI approach, effort/impact rating, key risks, and success metrics, plus a Resources column linking to a starter prompt, notebook, or governance document already in this playbook where one exists. Use this as a starting point, not every use case fits every organization.

**AI approach key:**
- **Rules**: deterministic logic or conventional software. No model.
- **Augment**: AI produces work that a person reviews, edits, and owns.
- **Assist**: AI provides information, analysis, options, classification, or recommendations; a person decides.
- **Human-led**: the substantive judgment stays with a person; technology may support administrative steps.
- **Analytics**: structured reporting, measurement, or statistical analysis. "AI-assisted" marks where a model reads free text.

Where a use case combines modes, the row says so. **Agent** is reserved for a model that plans and carries out several steps through tools with limited human review between them. No use case here currently meets that definition; see the [work redesign case study](work-redesign-people-partner.md) for why autonomy has to be earned through evidence.

---

## Talent acquisition

| Use case | AI approach | Business impact | Implementation effort | Key risk | Resources |
|---|---|---|---|---|---|
| Resume screening and scoring | Assist | High | Medium | Bias amplification | *None yet* |
| Job description optimization | Augment | Medium | Low | Over-standardization | [talent-acquisition.md, #1](../02-prompt-library/talent-acquisition.md) |
| Candidate sourcing from internal talent pools | Assist | High | Medium | Data freshness | [internal-mobility.md, #2](../02-prompt-library/internal-mobility.md) |
| Interview question generation by competency | Augment | Medium | Low | Validity of competency mapping | [talent-acquisition.md, #2](../02-prompt-library/talent-acquisition.md) |
| Offer letter drafting | Rules | Medium | Low | Compliance with local law | *None yet* |
| Candidate disposition communications | Rules + Augment | Medium | Low | Tone consistency | [talent-acquisition.md, #3](../02-prompt-library/talent-acquisition.md) |
| Recruiter coaching on interview feedback quality | Assist | High | Medium | Adoption resistance | [talent-acquisition.md, #4](../02-prompt-library/talent-acquisition.md) |
| Headcount forecasting from business plans | Analytics | High | High | Data quality in source systems | *None yet* |

### Spotlight: resume screening

**What it does:** AI scores inbound applications against a structured competency rubric, surfaces top candidates, and flags potential red flags for recruiter review, without making pass/fail decisions autonomously.

**What it does not do:** Reject candidates. Every disposition decision is made by a human recruiter.

**Metrics:**
- Time to first screen (target: [Set after baseline])
- Recruiter review time per requisition
- Offer acceptance rate (proxy for quality-of-hire signal)
- Demographic parity across candidate pool scores (fairness audit)

---

## Onboarding

| Use case | AI approach | Business impact | Implementation effort | Key risk | Resources |
|---|---|---|---|---|---|
| Personalized onboarding plan generation | Augment | High | Medium | Role/team data quality | [onboarding.md, #2](../02-prompt-library/onboarding.md) |
| New hire Q&A assistant | Assist | High | Low | Policy accuracy, hallucination | [onboarding.md, #1](../02-prompt-library/onboarding.md); [hr-qa-agent-demo.ipynb](../05-notebooks/hr-qa-agent-demo.ipynb) |
| Onboarding task automation (IT provisioning triggers) | Rules | High | High | System integration complexity | [Pattern 4, workflow patterns](../07-agentic-patterns/README.md#pattern-4-multi-step-workflow-with-checkpoints) |
| 30/60/90 day check-in synthesis | Analytics (AI-assisted) | Medium | Low | Survey fatigue | [onboarding.md, #4](../02-prompt-library/onboarding.md) |
| Manager onboarding prep guide | Augment | High | Low | Template staleness | [onboarding.md, #3](../02-prompt-library/onboarding.md) |
| Buddy program matching | Analytics | Medium | Low | Thin data for new orgs | [onboarding.md, #5](../02-prompt-library/onboarding.md) |

### Spotlight: new hire Q&A assistant

**What it does:** Answers policy, benefit, and process questions from new hires, citing the policy it relies on. Screens every question for signals that change how it must be handled and routes those, and anything it cannot answer from a cited source, to the right HR contact. Sending answers without human review is a later step for informational questions only, earned through evaluation.

**What it does not do:** Make benefit elections on behalf of employees or interpret individual circumstances.

**Metrics** (worth measuring; targets are set by the organization after a baseline):
- Correct resolution by request type
- Appropriate escalation: harmful misses found in a sampled review of non-escalated questions, and escalations specialists judged unnecessary
- Grounded answer quality: sampled check that answers match the cited policy
- Employee effort: repeat contacts about the same question
- Time to the right answer or the right person
- CSAT on new hire experience (30-day survey)
- Time-to-productivity (manager-rated)
- Question volume by type, observed rather than targeted

---

## Performance management

| Use case | AI approach | Business impact | Implementation effort | Key risk | Resources |
|---|---|---|---|---|---|
| Performance review draft generation | Augment | High | Low | Over-reliance, generic output | [performance.md, #1](../02-prompt-library/performance.md) |
| Calibration prep, manager briefing doc | Augment | High | Medium | Data access permissions | [performance.md, #2](../02-prompt-library/performance.md) |
| Goal-setting quality scoring | Assist | Medium | Medium | Subjectivity of scoring rubric | [performance.md, #3](../02-prompt-library/performance.md) |
| Mid-year feedback synthesis | Augment | Medium | Low | Feedback recency bias | [performance.md, #5](../02-prompt-library/performance.md) |
| PIP documentation drafting | Augment; decision human-led | High | Low | Legal exposure if misused | [performance.md, #4](../02-prompt-library/performance.md) |
| Succession planning gap analysis | Analytics | High | High | Data completeness | [succession-planning.md, #1 & #3](../02-prompt-library/succession-planning.md) |

### Spotlight: calibration prep

**What it does:** Generates a pre-calibration briefing doc for each manager: team performance distribution, flight-risk flags, compensation positioning, and prior-cycle outcomes. Delivered 48 hours before calibration sessions.

**What it does not do:** Make rating recommendations.

**Metrics:**
- Calibration session duration (target: [Set after baseline])
- Rating distribution spread vs. prior year
- Manager satisfaction with calibration prep

---

## Learning and development

| Use case | AI approach | Business impact | Implementation effort | Key risk | Resources |
|---|---|---|---|---|---|
| Skills gap identification by role | Analytics | High | High | Skills taxonomy maintenance | [learning-development.md, #1](../02-prompt-library/learning-development.md); [skills-gap-analysis.ipynb](../05-notebooks/skills-gap-analysis.ipynb) |
| Personalized learning path generation | Assist | High | Medium | LMS integration quality | [learning-development.md, #2](../02-prompt-library/learning-development.md) |
| Course content summarization | Augment | Medium | Low | Copyright compliance | *None yet* |
| Compliance training completion prediction | Analytics | Medium | Low | Prediction accuracy floor | *None yet* |
| Manager effectiveness coaching | Assist | High | Medium | Psychological safety concerns | [learning-development.md, #3](../02-prompt-library/learning-development.md) |
| Internal knowledge base Q&A | Assist | High | Medium | Knowledge freshness | [Pattern 1: retrieval with verification](../07-agentic-patterns/README.md#pattern-1-retrieval-with-verification); [hr-qa-agent-demo.ipynb](../05-notebooks/hr-qa-agent-demo.ipynb) |

### Spotlight: personalized learning paths

**What it does:** Analyzes an employee's role, skills data, career goals (from performance system), and team context to recommend a 90-day learning path from available LMS content, external resources, and mentoring.

**What it does not do:** Mandate learning, all recommendations are advisory.

**Metrics:**
- LMS course completion rate (baseline vs. personalized)
- Skills assessment score changes at 90 days
- Internal mobility rate for employees who completed recommended paths
- Manager-rated skill improvement at next review cycle

---

## HR operations and employee experience

| Use case | AI approach | Business impact | Implementation effort | Key risk | Resources |
|---|---|---|---|---|---|
| HR helpdesk triage and response | Mixed: rules, assist, augment; human-led for sensitive requests | High | Medium | Missed Employee Relations, legal, or health signals in routine-looking requests; policy accuracy | [hr-operations.md, #3](../02-prompt-library/hr-operations.md), [work redesign case study](work-redesign-people-partner.md) |
| Benefits enrollment guidance | Assist | High | Low | Benefits complexity, legal | [hr-operations.md, #1](../02-prompt-library/hr-operations.md) |
| Leave request processing | Rules; a person decides | Medium | Medium | Leave law variation by jurisdiction | [hr-operations.md, #2](../02-prompt-library/hr-operations.md) |
| Employee survey sentiment analysis | Analytics (AI-assisted) | High | Low | Interpretation subjectivity | [people-analytics.md, #2](../02-prompt-library/people-analytics.md) |
| Exit interview theme synthesis | Analytics (AI-assisted) | High | Low | Sample size at small orgs | [people-analytics.md, #3](../02-prompt-library/people-analytics.md) |
| Org design modeling | Analytics | High | High | Political sensitivity | [people-analytics.md, #5](../02-prompt-library/people-analytics.md) |

---

## People analytics

| Use case | AI approach | Business impact | Implementation effort | Key risk | Resources |
|---|---|---|---|---|---|
| Attrition risk scoring | Analytics | High | High | Data staleness, fairness | [attrition-risk-modeling.ipynb](../05-notebooks/attrition-risk-modeling.ipynb); [people-analytics.md, #1](../02-prompt-library/people-analytics.md) |
| Workforce planning models | Analytics | High | High | Forecast uncertainty | *None yet* |
| Pay equity analysis | Analytics | High | Medium | Legal exposure if mishandled | [pay-equity-governance.md](../03-governance/pay-equity-governance.md) |
| Engagement driver analysis | Analytics | High | Medium | Correlation ≠ causation | [people-analytics.md, #2](../02-prompt-library/people-analytics.md) |
| Headcount vs. revenue ratio benchmarking | Analytics | Medium | Low | Benchmark selection bias | *None yet* |

---

## Notes on this library

- **Resources column**: links to a prompt, notebook, or governance document already in this playbook that gets you started on that use case today. "*None yet*" means there's no starter resource in this repo yet, build your own or [contribute one](../CONTRIBUTING.md). A resource link is a starting point, not a finished, deployed solution, every use case still needs its own [risk assessment](../03-governance/risk-assessment-template.md) before deployment regardless of what's linked here.
- **Pay equity analysis, and any use case that touches compensation data**, has governance requirements beyond the standard risk assessment. See [pay equity governance](../03-governance/pay-equity-governance.md) before scoping this one.
- **Effort ratings** assume an organization with reasonably clean HRIS data and a dedicated HR tech team. Without that, add one level to every effort estimate.
- **Impact ratings** are for a 1,000+ employee organization. Smaller orgs may see lower absolute impact but faster time to value.
- Use the [prioritization matrix](prioritization-matrix.md) to score and rank these for your specific context.
- Submit new use cases via the [intake template](intake-template.md).
