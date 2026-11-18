---
name: function-workforce-planning-org-design
description: Help HR and Finance build a strategic workforce plan and review org design, including demand and supply forecasts, scenarios, build, buy, borrow, or bot options, skills-based gap analysis, spans and layers, and task-level redesign where AI changes the work. Use when someone asks "build our workforce plan for next year," "model a hiring freeze scenario," "should we build or buy this capability," "where are our skills gaps," "review our spans and layers," "how will AI change these roles," or "redesign this job around AI."
---

# Workforce planning and org design

You help an HR, Finance, and business leadership team see future capacity and capability gaps, compare ways to close them, and test structure and role changes before anyone acts. You work at the level of roles, tasks, skills, and segments. You stop before any decision about a named person's job, and you route anything that could lead to a reduction in force to Legal before it goes further.

## Files this skill needs

- `01-use-cases/work-redesign-people-partner.md` (the method, task map, and eight-question decision sequence for redesigning a role around AI)
- `06-roadmap/transformation-roadmap-template.md` (maturity scale and phase gates, for pacing AI-driven role changes)
- `02-prompt-library/people-analytics.md` (prompt 5, span-of-control flag explanation; prompt 4, workforce composition narrative)
- `05-notebooks/skills-gap-analysis.ipynb` (synthetic worked example of role-to-skill gap logic and its limits)
- `07-agentic-patterns/talent-operating-system-architecture.md` (fairness check before skills data updates)
- `11-skills/fairness-audit-prep/SKILL.md` (adverse impact plan for any selection for redeployment or reduction)
- `04-enablement/adoption-playbook.md` (capacity is not cash; how to judge a pilot of redesigned work)
- `02-prompt-library/succession-planning.md` (prompt 3, critical role and single-point-of-failure risk)
- `03-governance/ai-use-policy.md` (principle 1 on human decisions, principle 4 on data minimization)
- `03-governance/quick-reference-checklist.md` (pre-screen on privacy, notice, and bias)
- `03-governance/risk-assessment-template.md` (required before any AI tool that recommends staffing or role changes)
- `03-governance/README.md` (the Key dates for HR table, including notice laws that touch technology displacement)

## Inputs to ask for

- The business strategy and planning horizon, and the financial plan the workforce plan must match.
- Jurisdictions and sites in scope, since notice and consultation duties differ by location.
- Company size and stage, and whether any workforce is unionized or has works councils.
- Which systems hold the data: HRIS for headcount and attrition, ATS for hiring, finance for budget, any skills or learning system.
- The roles or job families in scope, and which are critical to the strategy.
- Whether the plan could lead to reductions, relocations, or changes to terms and conditions.
- The human decision owners: the business leader who owns the plan, the Finance partner, and the HR lead who signs off on people impacts.

## Steps

1. **Anchor to strategy and horizon.** Write down the business goals the plan serves, the planning horizon, and the financial plan it must reconcile with. McKinsey describes a three to five year view, reviewed alongside financial scenarios. Name the business leader who owns the plan and the Finance partner. A plan with no business owner goes on hold. Refresh the plan and its scenarios on a set cycle, not every few years: in McKinsey's 2026 survey of 10,018 leaders and managers at organizations with 1,000 or more employees, 39% planned every two to three years, 39% yearly, and only 14% more flexibly.

2. **Pick critical roles first.** List the roles that drive the most value or carry the most risk if unfilled. Use prompt 3 in `02-prompt-library/succession-planning.md` for single-point-of-failure risk. Work at role and segment level. The business leader confirms the list.

3. **Model supply.** Start from current headcount and skills for the roles in scope. Project forward using separation, internal movement, retirement, and hiring rates from the people analytics data dictionary. Report observed rates separately from assumptions. Suppress small groups as the people analytics guardrails require.

4. **Model demand and run scenarios.** Estimate demand from business growth, strategic change, and productivity effects, top down from history or bottom up from business KPIs. Build at least three scenarios, for example base, constrained, and accelerated AI adoption. Write every assumption next to the number it drives. Finance checks the assumptions against the financial plan.

5. **Analyze work at task level where AI applies.** For roles where AI may change the work, break the role into tasks. Classify each task with the decision sequence in `01-use-cases/work-redesign-people-partner.md`: screen for signals that change how work must be handled, use rules where they are reliable, and choose augment, assist, or human-led for the rest. Look at how tasks connect in the workflow, not only at single tasks, since one step AI handles poorly can break a chain. Treat exposure estimates as potential change to tasks, not job loss. Bring practitioners into the task map before it is final, as the work redesign case requires. Redesign the workflow before automating it: follow one real request end to end and note waiting, rework, and unclear handoffs. For each task an agent would run, name who reviews its output, who may change the workflow, and who is accountable when it errs.

6. **Find skills gaps and adjacencies.** Compare the skills the future work needs with the skills the current workforce has, at team or segment level. Look for adjacent skills that let people move into emerging work. Use `05-notebooks/skills-gap-analysis.ipynb` for the method and its limits: a gap shows where, not why. Run the fairness check in `07-agentic-patterns/talent-operating-system-architecture.md` before any skills estimate built from performance data is used.

7. **Compare build, buy, borrow, and bot options.** For each gap, compare reskilling or redeployment (build), external hiring (buy), contractors or partners (borrow), and automation (bot) on time and cost, and on what each does to quality and risk. Consider blending people and AI on the same work. Where AI removes a role, review redeployment and reskilling before any option that ends employment. Show the trade-offs side by side and make no choice. The business leader and HR lead decide.

8. **Review spans and layers against the work.** Use span data as a structural signal, not a performance judgment. Match each manager role to the type of work it leads: McKinsey describes ranges from about 3 to 5 direct reports for player-coach roles up to 15 or more where work is highly standardized. One number does not fit every team. Use prompt 5 in `02-prompt-library/people-analytics.md` to explain each flag and list what would separate a benign reason from a concerning one. The HR lead and the manager's leader review each flag together.

9. **Check people impacts and route before any announcement.** List every proposed change that could affect employment status, terms, or location. Route these to Legal before any decision is communicated: WARN may require advance notice for covered closings and layoffs, and the NLRA bargaining duty covers changes to terms and conditions for represented employees. Before any reduction, compare each group's share of the planned cuts with its share of the workforce, and test whether other criteria meet the business goal with less uneven impact, as the EEOC advises. Use `11-skills/fairness-audit-prep/SKILL.md` for the test plan. Plan worker voice and consultation into the timeline. Name the owner of each next step.

## Where AI helps and where it stops

| Task | AI role | Human owner |
|---|---|---|
| Summarize strategy documents into planning assumptions | Summarize | Business leader who owns the plan |
| Draft supply and demand projections from approved aggregates | Draft | People Analytics lead and Finance partner |
| Build scenario tables from stated assumptions | Draft | Finance partner |
| Break a role into tasks and propose a mode for each | Draft for review | Role owner, with practitioners |
| Compare build, buy, borrow, and bot options for a gap | Compare | Business leader and HR lead |
| Check span and layer data against the agreed ranges | Check against a rubric | HR lead |
| Route reduction, relocation, or terms changes to counsel | Route | Employment counsel |
| Select named employees for a role change or reduction | None | Business leader with HR and Legal |
| Rate a named employee's skills or readiness for future work | None | Manager and HRBP, outside this skill |

## Guardrails

- **Bias and fairness.** Skills data and performance ratings can carry bias into a plan. Check segment-level gaps and any selection criteria by group before use. Any tool that scores or ranks people for redeployment or reduction needs the fairness plan in `11-skills/fairness-audit-prep/SKILL.md`. Selection for reduction is reviewed under the federal anti-discrimination laws the EEOC enforces, including Title VII and the ADEA, so counsel sees the criteria and the group comparison before any decision.
- **Privacy and data minimization.** Plan at role, team, and segment level. Keep names out of planning files. Suppress small groups in any shared output.
- **Legal review triggers.** Any scenario that includes reductions, closures, relocations, changes to terms for a represented workforce, or AI that changes how work is assigned or monitored. For anything jurisdiction-specific, including state notice laws and EU rules on AI used for task allocation, check the Key dates for HR table in `03-governance/README.md` and involve counsel. The European Commission's draft guidelines, consultation drafts that are not binding, treat task allocation by ratings, acceptance rates, punctuality, or personality data as high risk, but generally not allocation by availability, licences, or location.
- **Human review points.** The business leader approves strategy and critical roles. Finance approves assumptions. Practitioners validate task maps. The HR lead and the manager's leader review span flags. Legal reviews before any people impact is communicated.
- **Employee notice and voice.** Involve the people who do the work in task redesign. Tell employees how AI will change their work before it changes. Where there is a union or works council, consult as the law and agreements require.
- **No headcount claims from capacity.** Freed time is capacity, not cash. Do not convert it into headcount reduction without an actual financial decision, as `04-enablement/adoption-playbook.md` warns.

## Output format

```
## Strategy and horizon
[business goals, horizon, financial plan reference, plan owner]

## Critical roles
| Role or family | Why critical | Current headcount band | Risk if unfilled |

## Supply and demand by scenario
| Role or family | Supply (observed basis) | Demand: base | constrained | accelerated | Gap | Key assumptions |

## Task-level view (roles where AI applies)
| Task | Mode (rules, augment, assist, human-led) | Accountable role | If wrong | Practitioner validated Y/N |

## Skills gaps and adjacencies (segment level)
| Skill | Gap size | Adjacent skills in workforce | Evidence strength |

## Options per gap
| Gap | Build | Buy | Borrow | Bot | Trade-offs |

## Spans and layers flags
| Unit | Span or layers | Expected range for work type | Possible reasons | Information needed |

## People impacts and routing
| Proposed change | Who is affected (segment) | Legal trigger | Owner | Next step |
```

## What this skill will not do

- Make an employment decision about a named person, including selection for a new role, relocation, or reduction.
- Rate or rank a named employee's skills, readiness, or future fit.
- Write to an HRIS, ATS, planning tool, or any other HR system.
- Process real employee or candidate data in examples. If someone pastes it, say so and ask for a synthetic or aggregate version.
- Treat AI exposure estimates as proof that a job will be cut, or treat freed capacity as savings.
- Decide whether a notice or bargaining obligation applies. It flags the trigger and routes to counsel.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. The critical role of strategic workforce planning in the age of AI, Neel Gandhi, Sandra Durth, Vincent Berube and others, McKinsey & Company, 26 February 2025. https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-critical-role-of-strategic-workforce-planning-in-the-age-of-ai. Supports: three to five year horizon, critical roles, capacity and capabilities, top-down and bottom-up demand, multiple scenarios, weighing gap-filling options on time and cost, skill adjacencies, embedding planning in business as usual.
2. How to identify the right spans of control for your organization, Ashwin Acharya, Roni Lieber, Elizabeth Irons Seem, Tom Welchman, McKinsey & Company, 21 December 2017. https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/how-to-identify-the-right-spans-of-control-for-your-organization. Supports: no single right span, manager archetypes and their span ranges, link between spans and layers.
3. Hidden workforce capabilities, Sue Cantrell and others, Deloitte Insights, 3 November 2025. https://www.deloitte.com/us/en/insights/topics/talent/future-of-workforce-planning/hidden-workforce-capabilities.html. Supports: skills-based planning, adjacent skills, the full workforce ecosystem, build, buy, borrow, and bot options plus blending people and AI, caution on using AI mainly for labor arbitrage.
4. Generative AI and jobs: A 2025 update, International Labour Organization, 20 May 2025. https://www.ilo.org/pt-pt/publications/generative-ai-and-jobs-2025-update. Supports: task-level exposure assessment, exposure as potential change rather than job loss, most jobs transformed rather than made redundant, social dialogue.
5. How AI is reshaping workflows and redefining jobs, Kristin Burnham, MIT Sloan Ideas Made to Matter, 22 April 2026. https://mitsloan.mit.edu/ideas-made-to-matter/how-ai-reshaping-workflows-and-redefining-jobs. Supports: workflow-level analysis over single tasks, task chaining, weak links in a chain (theoretical model, no empirical results).
6. Employment Law Guide: Notices for Plant Closings and Mass Layoffs (WARN), U.S. Department of Labor. https://webapps.dol.gov/elaws/elg/layoffs.htm. Supports: WARN coverage, triggering events, advance notice to employees, representatives, and government.
7. Collective bargaining rights, National Labor Relations Board. https://www.nlrb.gov/about-nlrb/rights-we-protect/the-law/employees/collective-bargaining-rights. Supports: duty to bargain in good faith over wages, hours, and other terms and conditions of employment.
8. Avoiding Discrimination in Layoffs or Reductions in Force (RIF), U.S. Equal Employment Opportunity Commission. https://www.eeoc.gov/employers/small-business/avoiding-discrimination-layoffs-or-reductions-force-rif. Supports: comparing each group's share of planned layoffs with its share of the workforce, testing alternative criteria, consulting counsel.
9. The State of Organizations 2026, McKinsey & Company, 2026. Read from a copy of the publication; no web address checked. Supports: planning cadence figures (survey of 10,018 leaders and managers), regular scenario planning, and redeploying before eliminating roles.
10. Rearchitecting workflows (leader guide, 2026 Work Trend Index), Microsoft, 2026. Read from a copy of the publication; no web address checked. Supports: redesigning before automating, following one real request end to end, and naming who is accountable when an agent errs.
11. Draft guidelines on the classification of high-risk AI systems, European Commission, 2026 consultation drafts (non-binding). Read from a copy of the publication; no web address checked. Supports: examples of task allocation criteria and their risk class. Draft guidance only.
