# HR AI business case template

Use this structure for any HR AI investment proposal. Pair it with the [ROI calculation framework](README.md#roi-calculation-framework) for the numbers behind the payback calculation, and the [use case library](../01-use-cases/use-case-library.md) if you haven't picked a use case yet.

---

## [Use case name]

**Problem statement**
What is painful, slow, or inconsistent today? Who feels it? What does it cost?

*Example: New hire onboarding Q&A is handled manually by HR Ops. Average response time is 4 hours. Each HR Ops team member spends approximately 6 hours/week answering repetitive questions from the same 40-question set. The result: HR capacity constrained on low-value work, new hires waiting for answers during their most critical first weeks.*

**Proposed solution**
One sentence: what will the AI do?

*Example: Deploy a RAG-based Q&A agent trained on onboarding policies and FAQs, available 24/7, escalating to HR Ops for complex or sensitive questions.*

**Investment required**
Be specific. Include build time, ongoing model costs, maintenance, and enablement.

| Cost item | Estimate | Basis |
|---|---|---|
| Build (engineer time) | [X hours × rate] | [Complexity estimate] |
| Ongoing model API costs | [$/month] | [Volume estimate × token cost] |
| Knowledge base maintenance | [X hours/month] | [Policy update frequency] |
| Enablement (training HR team) | [X hours] | [Team size × session time] |
| **Total Year 1** | **$X** | |
| **Total Year 2+** | **$X/year** | |

**Expected outcomes**

| Metric | Baseline | Target | Measurement method |
|---|---|---|---|
| HR Ops time on Q&A | 6 hrs/week/person | <1 hr/week/person | Time tracking or self-report |
| New hire question response time | 4 hrs avg | <5 min | Ticket system timestamp |
| New hire 30-day CSAT | [baseline] | +0.5 points | Onboarding survey |
| HR helpdesk ticket volume | [baseline] | -40% for FAQ categories | Ticket system |

**Payback calculation**

```
Annual HR time saved: 5 hrs/week × 3 HR Ops staff × 48 weeks = 720 hrs
Value of HR time: 720 hrs × $[blended hourly rate] = $[X]
Annual cost: $[model costs + maintenance]
Net annual value: $[X - costs]
Payback period: [Investment ÷ net annual value] months
```

**Risks and mitigations**

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Policy hallucination | Medium | High | RAG grounding + citation requirement + human review of edge cases |
| Low adoption | Medium | High | Manager champions + embedded in existing workflow |
| Policy staleness | High | Medium | Designated knowledge base owner + update SLA |
| Employee trust concerns | Low | Medium | Transparency communication + easy human escalation |

**Go/no-go criteria**
What must be true for this to succeed? State these before you start.

*Example: Clean policy documentation available in structured format; HRBP team committed to reviewing escalations within 2 hours; IT approval for API integration.*

---

## Cross-links

- [ROI measurement](README.md): the outcome categories, ROI formulas, and reporting cadence this business case feeds into.
- [Use case library](../01-use-cases/use-case-library.md): where the use case in this template should come from.
- [Risk assessment template](../03-governance/risk-assessment-template.md): required before any use case in this template goes from proposal to pilot.
