# HR AI ROI measurement

HR AI programs fail to scale for one of two reasons: they can't show value, or they can't show it in terms leadership cares about. This section provides a framework for measuring and communicating the business impact of HR AI investments.

**[Live dashboard demo](https://ellehelvig.github.io/hr-ai-transformation-playbook/08-roi-measurement/dashboard.html)**, a working mock-up of the monthly reporting format below, plus a payback calculator that runs the formula from the business case template on your own numbers.

---

## The measurement problem in HR AI

Most HR AI programs are measured on the wrong things. They track outputs (prompts used, tickets deflected, hours saved) without connecting them to outcomes (quality of hire, retention, manager effectiveness, employee experience).

The result is a program that looks active but can't defend its budget in a business review.

The framework here is built around outcomes, not outputs, with output metrics as leading indicators, not endpoints.

---

## Contents

| File | Purpose |
|---|---|
| [business-case-template.md](business-case-template.md) | Fillable template for any HR AI investment proposal: problem statement, cost, expected outcomes, payback, risks, go/no-go criteria |
| [dashboard.html](https://ellehelvig.github.io/hr-ai-transformation-playbook/08-roi-measurement/dashboard.html) | Live interactive dashboard mock-up and ROI payback calculator |

---

## The four outcome categories

Every HR AI use case should map to at least one of these:

**Efficiency**: HR professionals and employees get time back. Work that took hours takes minutes.

**Quality**: HR decisions, communications, and processes are more consistent and better informed.

**Experience**: Employees and managers feel more supported, get answers faster, trust HR more.

**Capability**: The HR team can do things it couldn't do before: predictive analytics, personalized development, proactive retention interventions.

---

## Business case template

Use the [business case template](business-case-template.md) for any HR AI investment proposal: problem statement, investment required, expected outcomes, payback calculation, risks and mitigations, and go/no-go criteria before you start.

---

## ROI calculation framework

### Efficiency ROI (time saved)

```
Annual hours saved = (time_before - time_after) × frequency × people_affected × 48 weeks
Value of hours saved = annual_hours_saved × blended_hourly_cost
Net ROI = value_of_hours_saved - annual_cost
ROI% = (net_ROI / annual_cost) × 100
```

**Common efficiency benchmarks for HR AI:**

| Use case | Typical time saving | Source |
|---|---|---|
| Performance review draft | 45–90 min per review | Manager time studies |
| HR helpdesk Q&A deflection | 3–5 min per ticket | Ticket handling time |
| Onboarding plan generation | 60–120 min per new hire | HR Ops time studies |
| Job description writing | 30–60 min per JD | Recruiter surveys |
| Exit interview synthesis | 4–6 hrs per cohort | People Analytics estimate |

*Note: Always validate benchmarks with your own baseline measurement before building a business case.*

### Quality ROI (error reduction and consistency)

Harder to quantify but often larger in impact than efficiency. Use proxy metrics:

- **Consistency score**: % of documents meeting quality rubric before vs. after AI assistance
- **Error rate**: Factual errors in HR communications, policy misquotes, process mistakes
- **Manager feedback quality**: Calibration team ratings on review drafts
- **Offer acceptance rate**: Proxy for quality of candidate communication

### Experience ROI (employee and manager sentiment)

- **New hire CSAT**: 30/60/90-day survey scores
- **HR satisfaction score**: Annual engagement survey HR effectiveness question
- **Manager confidence**: "I feel supported by HR" pulse score
- **Response time**: Time from question to answer for HR queries

### Capability ROI (things you couldn't do before)

This is the hardest to quantify and the most strategically important. Document it qualitatively:

- *Before:* Could not predict attrition risk; found out when employees resigned
- *After:* Identifying at-risk employees 60–90 days before potential departure; enabling proactive retention conversations
- *Value:* Cost of turnover avoided (typically 50–200% of annual salary per role)

---

## Reporting cadence and format

### For HR leadership (monthly, 1 page)

Focus on: outcomes achieved, KPIs vs. targets, issues flagged, next month priorities.

```
HR AI Program, [Month] Update

USE CASES LIVE: [N]
────────────────────────────────
Onboarding Q&A Agent
  Response time:     3 min avg    (target: <5 min) ✓
  CSAT:             4.3/5.0      (target: >4.0)   ✓
  Escalation rate:  12%          (target: 5–20%)  ✓
  Helpdesk deflection: 380 tickets (↑18% vs last month)

Performance Review Assistant
  Manager adoption:  67%          (target: 80%)   ⚠
  Review quality:    4.1/5.0      (target: >4.0)  ✓
  Time per review:   35 min       (baseline: 90)  ✓

ISSUES:
  [1] Manager adoption below target, enablement session scheduled for [date]

NEXT MONTH:
  [1] Launch L&D recommendation pilot with Engineering team
  [2] Complete fairness audit on attrition risk model
```

### For CHRO/CFO (quarterly, 3–5 slides)

Focus on: cumulative ROI, strategic impact, investment vs. return, roadmap.

Key numbers to always include:
- Total HR hours recovered (and their dollar value)
- Employee experience improvement (CSAT change)
- Use cases live vs. planned
- Year-to-date cost vs. budget
- Cumulative net value delivered

### For the HR team (real-time, in their tools)

Don't make HR professionals go to a separate dashboard to see how their AI tools are performing. Surface key metrics in Slack, in their HRIS, or in a lightweight weekly digest.

---

## What not to measure

**Prompt volume.** Number of prompts run is an output metric with no relationship to value. A team that uses 1,000 prompts to do genuinely useful work is more valuable than one that uses 10,000 prompts on low-value tasks.

**Model accuracy in isolation.** A model that's 95% accurate on a use case that doesn't matter has delivered no value. Accuracy only means something relative to the decision it supports.

**Cost savings vs. theoretical baseline.** "We saved $500K compared to hiring 5 more HR people" is not a real saving unless you were actually going to hire those people. Only count savings against real alternatives.

**Vanity adoption metrics.** "100% of HR team members have accessed the tool" means nothing if they used it once and stopped. Measure active weekly users and whether they're using it for high-value tasks.

---

## Building the feedback loop

Every metric you track should have an owner, a review cadence, and a response protocol. A metric nobody acts on is just noise.

| Metric | Owner | Review cadence | Response if off-target |
|---|---|---|---|
| Agent accuracy | HR Tech | Weekly | Investigate and update knowledge base or prompt |
| Escalation rate | HRBP team | Weekly | If >25%: retrain; if <5%: audit for under-escalation |
| Employee CSAT | HR Ops | Monthly | If <3.8: pause and investigate; if <4.0: improvement sprint |
| Fairness scores | People Analytics | Quarterly | If flagged: immediate halt of use case pending review |
| Cost per task | HR Finance | Monthly | If >2× target: review model choice and prompt efficiency |
