# HR AI use case library

37 vetted use cases organized by HR function. Each entry includes the AI approach, effort/impact rating, key risks, and success metrics, plus a Resources column linking to a starter prompt, notebook, or governance document already in this playbook where one exists. Use this as a starting point, not every use case fits every organization.

**AI approach key:**
- **Agent**: autonomous multi-step task completion with tool use
- **Copilot**: AI assists a human who retains decision authority
- **Automation**: rule-based + AI for structured, repeatable workflows
- **Analytics**: AI-augmented data analysis and insight generation

---

## Talent acquisition

| Use case | AI approach | Business impact | Implementation effort | Key risk | Resources |
|---|---|---|---|---|---|
| Resume screening and scoring | Copilot | High | Medium | Bias amplification | *None yet* |
| Job description optimization | Copilot | Medium | Low | Over-standardization | [talent-acquisition.md, #1](../02-prompt-library/talent-acquisition.md) |
| Candidate sourcing from internal talent pools | Agent | High | Medium | Data freshness | [internal-mobility.md, #2](../02-prompt-library/internal-mobility.md) |
| Interview question generation by competency | Copilot | Medium | Low | Validity of competency mapping | [talent-acquisition.md, #2](../02-prompt-library/talent-acquisition.md) |
| Offer letter drafting | Automation | Medium | Low | Compliance with local law | *None yet* |
| Candidate disposition communications | Automation | Medium | Low | Tone consistency | [talent-acquisition.md, #3](../02-prompt-library/talent-acquisition.md) |
| Recruiter coaching on interview feedback quality | Copilot | High | Medium | Adoption resistance | [talent-acquisition.md, #4](../02-prompt-library/talent-acquisition.md) |
| Headcount forecasting from business plans | Analytics | High | High | Data quality in source systems | *None yet* |

### Spotlight: resume screening

**What it does:** AI scores inbound applications against a structured competency rubric, surfaces top candidates, and flags potential red flags for recruiter review, without making pass/fail decisions autonomously.

**What it does not do:** Reject candidates. Every disposition decision is made by a human recruiter.

**Metrics:**
- Time to first screen (target: ≤24 hrs from application)
- Recruiter review time per requisition
- Offer acceptance rate (proxy for quality-of-hire signal)
- Demographic parity across candidate pool scores (fairness audit)

---

## Onboarding

| Use case | AI approach | Business impact | Implementation effort | Key risk | Resources |
|---|---|---|---|---|---|
| Personalized onboarding plan generation | Agent | High | Medium | Role/team data quality | [onboarding.md, #2](../02-prompt-library/onboarding.md) |
| New hire Q&A assistant | Agent | High | Low | Policy accuracy, hallucination | [onboarding.md, #1](../02-prompt-library/onboarding.md); [hr-qa-agent-demo.ipynb](../05-notebooks/hr-qa-agent-demo.ipynb) |
| Onboarding task automation (IT provisioning triggers) | Automation | High | High | System integration complexity | [Pattern 5, agentic patterns](../07-agentic-patterns/README.md) |
| 30/60/90 day check-in synthesis | Analytics | Medium | Low | Survey fatigue | [onboarding.md, #4](../02-prompt-library/onboarding.md) |
| Manager onboarding prep guide | Copilot | High | Low | Template staleness | [onboarding.md, #3](../02-prompt-library/onboarding.md) |
| Buddy program matching | Analytics | Medium | Low | Thin data for new orgs | [onboarding.md, #5](../02-prompt-library/onboarding.md) |

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

| Use case | AI approach | Business impact | Implementation effort | Key risk | Resources |
|---|---|---|---|---|---|
| Performance review draft generation | Copilot | High | Low | Over-reliance, generic output | [performance.md, #1](../02-prompt-library/performance.md) |
| Calibration prep, manager briefing doc | Copilot | High | Medium | Data access permissions | [performance.md, #2](../02-prompt-library/performance.md) |
| Goal-setting quality scoring | Analytics | Medium | Medium | Subjectivity of scoring rubric | [performance.md, #3](../02-prompt-library/performance.md) |
| Mid-year feedback synthesis | Analytics | Medium | Low | Feedback recency bias | [performance.md, #5](../02-prompt-library/performance.md) |
| PIP documentation drafting | Copilot | High | Low | Legal exposure if misused | [performance.md, #4](../02-prompt-library/performance.md) |
| Succession planning gap analysis | Analytics | High | High | Data completeness | [succession-planning.md, #1 & #3](../02-prompt-library/succession-planning.md) |

### Spotlight: calibration prep

**What it does:** Generates a pre-calibration briefing doc for each manager: team performance distribution, flight-risk flags, compensation positioning, and prior-cycle outcomes. Delivered 48 hours before calibration sessions.

**What it does not do:** Make rating recommendations.

**Metrics:**
- Calibration session duration (target: reduce by 20%)
- Rating distribution spread vs. prior year
- Manager satisfaction with calibration prep

---

## Learning and development

| Use case | AI approach | Business impact | Implementation effort | Key risk | Resources |
|---|---|---|---|---|---|
| Skills gap identification by role | Analytics | High | High | Skills taxonomy maintenance | [learning-development.md, #1](../02-prompt-library/learning-development.md); [skills-gap-analysis.ipynb](../05-notebooks/skills-gap-analysis.ipynb) |
| Personalized learning path generation | Agent | High | Medium | LMS integration quality | [learning-development.md, #2](../02-prompt-library/learning-development.md) |
| Course content summarization | Copilot | Medium | Low | Copyright compliance | *None yet* |
| Compliance training completion prediction | Analytics | Medium | Low | Prediction accuracy floor | *None yet* |
| Manager effectiveness coaching | Copilot | High | Medium | Psychological safety concerns | [learning-development.md, #3](../02-prompt-library/learning-development.md) |
| Internal knowledge base Q&A | Agent | High | Medium | Knowledge freshness | [Pattern 3: RAG](../07-agentic-patterns/README.md); [hr-qa-agent-demo.ipynb](../05-notebooks/hr-qa-agent-demo.ipynb) |

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
| HR helpdesk triage and response | Agent | High | Medium | Policy accuracy | [hr-operations.md, #3](../02-prompt-library/hr-operations.md) |
| Benefits enrollment guidance | Copilot | High | Low | Benefits complexity, legal | [hr-operations.md, #1](../02-prompt-library/hr-operations.md) |
| Leave request processing | Automation | Medium | Medium | Leave law variation by jurisdiction | [hr-operations.md, #2](../02-prompt-library/hr-operations.md) |
| Employee survey sentiment analysis | Analytics | High | Low | Interpretation subjectivity | [people-analytics.md, #2](../02-prompt-library/people-analytics.md) |
| Exit interview theme synthesis | Analytics | High | Low | Sample size at small orgs | [people-analytics.md, #3](../02-prompt-library/people-analytics.md) |
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
