# HR AI transformation roadmap template

A phased roadmap framework for HR AI transformation programs. Adapt the phases, timelines, and milestones to your organization's size, maturity, and starting point.

**How to use this template:**
1. Assess your current state using the maturity scale below
2. Identify your target state for the next 12–18 months
3. Select the use cases from the [use case library](../01-use-cases/use-case-library.md) that match your phase
4. Build phase gate criteria specific to your org
5. Align with your CHRO and People Systems team before sharing more broadly

---

## HR AI maturity scale

Before planning where to go, be honest about where you are.

| Level | Description | Indicators |
|---|---|---|
| **0 — Unaware** | AI not yet in scope for HR | No AI tools in use; conversations are theoretical |
| **1 — Experimenting** | Individual HR team members using AI tools ad-hoc | Scattered Copilot use; no governance; no shared prompts |
| **2 — Piloting** | Deliberate pilots with defined success metrics | 1–3 use cases in controlled pilots; governance forming |
| **3 — Scaling** | Proven use cases deployed org-wide; enablement underway | Multiple live use cases; HR team trained; monitoring in place |
| **4 — Transforming** | AI embedded in HR operating model; continuous innovation | AI influence on HR strategy; feedback loops to improve models |
| **5 — Leading** | HR AI program is a competitive differentiator | External recognition; exporting practices to broader org |

**Honest starting point is essential.** Most large HR organizations are at Level 1 or 2. Plans built from an assumed Level 3 starting point fail.

---

## Phase 0: Foundation (months 1–2)

**Goal:** Establish the governance, infrastructure, and alignment needed to move fast safely.

**Key activities:**
- [ ] Assess current HR AI maturity (use scale above)
- [ ] Inventory AI tools already in use across the People Team (you likely have more than you think)
- [ ] Identify People Systems landscape — what HRIS, LMS, ATS, and analytics tools are in scope
- [ ] Establish an HR AI working group: HR Tech, HRBPs, HR Ops, Legal, Privacy
- [ ] Draft and ratify the [AI Use Policy](../03-governance/ai-use-policy.md)
- [ ] Define data governance basics: what data can be used, where, by whom
- [ ] Identify 2–3 executive sponsors

**Phase gate criteria to exit Phase 0:**
- AI use policy approved by HR Leadership and Legal
- Working group meeting cadence established
- Current-state HR AI inventory complete
- At least one Tier 1 use case identified and approved for piloting

**Common Phase 0 traps:**
- Spending too long here. 8 weeks maximum; governance can mature alongside pilots.
- Designing governance for a Level 4 org when you're at Level 1.
- Not involving Legal early enough.

---

## Phase 1: Quick wins (months 2–5)

**Goal:** Demonstrate measurable value with low-risk, high-visibility use cases. Build internal credibility and team confidence.

**Target use cases (choose 2–3):**
- New hire Q&A agent
- HR helpdesk triage
- Manager onboarding checklist generation
- Performance review draft assistance
- Job description optimization

**Key activities:**
- [ ] Select 2–3 use cases using the [prioritization matrix](../01-use-cases/prioritization-matrix.md)
- [ ] Complete [risk assessments](../03-governance/risk-assessment-template.md) for each
- [ ] Run pilot with a defined cohort (one team, one region, one use case at a time)
- [ ] Instrument success metrics before launching
- [ ] Train pilot participants using Module 1–2 of the [HR AI literacy curriculum](../04-enablement/hr-ai-literacy-curriculum.md)
- [ ] Run weekly retrospectives during pilot; document what's working and what isn't
- [ ] Prepare a results summary for HR Leadership after 4–6 weeks

**Phase gate criteria to exit Phase 1:**
- At least 2 pilots completed with documented results
- Measurable improvement on at least one metric per use case
- Pilot participants trained and able to use tools independently
- No material governance issues identified
- Executive sponsors briefed and supportive of Phase 2

**Success metrics to instrument:**

| Use case | Primary metric | Secondary metric |
|---|---|---|
| New hire Q&A | CSAT on new hire experience | Helpdesk ticket volume reduction |
| HR helpdesk triage | Response time (first reply) | Resolution rate without escalation |
| Manager onboarding checklist | Manager completion rate | New hire 30-day satisfaction score |
| Performance review draft | Manager time on review cycle | Review quality score (HRBP-rated) |

---

## Phase 2: Scale and enablement (months 5–10)

**Goal:** Expand proven use cases org-wide. Build HR team capability. Establish monitoring infrastructure.

**Key activities:**
- [ ] Roll out Phase 1 wins to all relevant HR users
- [ ] Deliver full [HR AI literacy curriculum](../04-enablement/hr-ai-literacy-curriculum.md) to all People Team members
- [ ] Identify and develop HR AI Champions — internal advocates in each HRBP region
- [ ] Add 3–5 medium-complexity use cases (recruiting pipeline, learning paths, calibration prep)
- [ ] Stand up monitoring dashboards for live use cases
- [ ] Conduct first fairness audit on any use cases touching employment decisions
- [ ] Begin building internal prompt library beyond the starter kit
- [ ] Quarterly business review: ROI report for HR Leadership and CFO

**Scaling checklist for each use case:**

Before rolling a pilot use case to org-wide deployment:
- [ ] Pilot results documented and reviewed
- [ ] Risk assessment updated with pilot learnings
- [ ] Training materials ready for all users
- [ ] Escalation path tested and staffed
- [ ] Monitoring dashboard live
- [ ] Rollback plan defined

**Phase gate criteria to exit Phase 2:**
- 80%+ of People Team trained through Module 1–3 of literacy curriculum
- 5+ use cases live in production with monitoring
- Quarterly fairness audit complete for all employment-decision-adjacent use cases
- HR AI Champions network active in all major regions/functions
- Positive ROI demonstrated on at least 3 use cases

---

## Phase 3: Advanced capability (months 10–18)

**Goal:** Move from assisting HR workflows to transforming them. Introduce agentic automation and predictive analytics.

**Target use cases:**
- Attrition risk modeling with HRBP workflow integration
- Workforce planning models
- Personalized learning path generation with LMS integration
- Agentic onboarding workflow automation
- Pay equity analysis

**Key activities:**
- [ ] Commission full attrition risk model (requires clean HRIS data — see [05 · Notebooks](../05-notebooks/README.md))
- [ ] Build agentic workflows for highest-volume HR processes
- [ ] Integrate AI recommendations into HRIS where technically feasible
- [ ] Establish HR AI as a function — dedicated headcount or formal role(s)
- [ ] Publish internal annual report on HR AI program outcomes
- [ ] Begin knowledge-sharing with broader organization (other business functions)

---

## KPI framework

Track these at the program level, regardless of individual use case metrics.

### Efficiency
| Metric | Baseline | Target |
|---|---|---|
| HR headcount ratio (employees per HR FTE) | [measure] | +15–20% efficiency |
| Average HR query resolution time | [measure] | −30% |
| Time to fill (recruiting) | [measure] | −20% |
| Onboarding completion rate (30-day checklist) | [measure] | +15pp |

### Quality
| Metric | Baseline | Target |
|---|---|---|
| New hire 90-day satisfaction (survey) | [measure] | +0.5 point |
| Manager performance review quality score | [measure] | +20% |
| HR helpdesk CSAT | [measure] | +10pp |
| Internal mobility rate | [measure] | +5pp |

### Capability
| Metric | Baseline | Target |
|---|---|---|
| % of HR team trained (AI literacy program) | 0% | 100% by Phase 2 end |
| Number of AI use cases live in production | 0 | 8+ by month 18 |
| Number of HR AI Champions | 0 | 1 per team or region |

### Governance
| Metric | Baseline | Target |
|---|---|---|
| % of live use cases with active monitoring | — | 100% |
| Fairness audits completed on schedule | — | 100% |
| Risk assessments completed before deployment | — | 100% |
| Governance issues identified (target: find and fix) | — | 0 unresolved >30 days |

---

## Roadmap on a page

```
Month:  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18
        ├──────────────┤
Phase 0: Foundation
                  ├───────────────────┤
Phase 1: Quick wins (pilots → scale)
                              ├──────────────────────┤
Phase 2: Scale + enablement
                                               ├────────────────────────┤
Phase 3: Advanced capability
```

---

## Checkpoint: questions to ask at each phase review

**Is our governance keeping pace with our ambition?**
Every new use case should flow through the risk assessment process. Speed is not a reason to skip it.

**Are our HR people actually using this?**
Tool deployment ≠ adoption. Track active usage, not just access.

**Is this making HR work better or just different?**
Measure outcomes, not outputs. Process automation that doesn't improve employee experience or HR quality is not transformation.

**What have we gotten wrong?**
Every phase should surface failures and near-misses. A program with no documented failures is a program not being honest.
