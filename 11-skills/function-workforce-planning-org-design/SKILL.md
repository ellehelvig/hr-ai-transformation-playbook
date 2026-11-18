---
name: function-workforce-planning-org-design
description: Builds a strategic workforce plan and org design review at role, task, skill, and segment level, covering critical roles, supply and demand scenarios, task-level AI redesign, evidence-based skills gaps, build, buy, borrow, or bot options, spans and layers flags, and a people-impact routing table for counsel. Use whenever someone asks to build next year's workforce plan, model a hiring freeze or an AI adoption scenario, decide whether to build or buy a capability, find skills gaps, review spans and layers, estimate how AI will change roles, redesign a job around AI, or size a restructuring, and always before a plan that could lead to reductions, relocations, or changed terms reaches anyone affected.
---

# Workforce planning and org design

This skill serves the HR, Finance, and business leaders who own a workforce plan. It produces scenario tables, a task-level view of roles AI changes, segment-level skills gaps, side-by-side options per gap, structural flags, and a routing table for every change that touches employment. It stops before any decision about a named person's job and routes anything that could lead to a reduction in force to counsel.

## Files this skill needs

- `01-use-cases/work-redesign-people-partner.md` (method, task map, and eight-question decision sequence for redesigning a role around AI)
- `06-roadmap/transformation-roadmap-template.md` (maturity scale and phase gates, for pacing AI-driven role changes)
- `02-prompt-library/people-analytics.md` (prompt 5, span-of-control flag explanation; prompt 4, workforce composition narrative)
- `02-prompt-library/succession-planning.md` (prompt 3, critical role and single-point-of-failure risk)
- `05-notebooks/skills-gap-analysis.ipynb` (synthetic worked example of role-to-skill gap logic and its limits)
- `07-agentic-patterns/talent-operating-system-architecture.md` (fairness check before skills data updates)
- `11-skills/fairness-audit-prep/SKILL.md` (adverse impact plan for any selection for redeployment or reduction)
- `11-skills/function-people-analytics/SKILL.md` (data dictionary and small-group suppression)
- `04-enablement/adoption-playbook.md` (capacity is not cash; how to judge a pilot of redesigned work)
- `03-governance/ai-use-policy.md` (principle 1 on human decisions, principle 4 on data minimization)
- `03-governance/quick-reference-checklist.md` (pre-screen on privacy, notice, and bias)
- `03-governance/risk-assessment-template.md` (required before any AI tool that recommends staffing or role changes)
- `03-governance/README.md` (the Key dates for HR table)

## Inputs

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| Strategy, horizon, and financial plan to reconcile with | Yes | Ask the user | FY27 plan, 3-year view |
| Plan owner, Finance partner, HR lead | Yes | Ask the user | VP Support; FP&A partner; HRBP lead |
| Roles or job families in scope, and which are critical | Yes | Ask the user | Support agents, support engineers, team leads |
| Sites and jurisdictions in scope | Yes | HRIS, read-only: headcount by country, state, and site | US states, Germany |
| Union, works council, or other representation | Yes | Ask the user; labor relations confirms | Works council at the German entity |
| Current headcount and movement rates | Yes | HRIS, read-only: job family, level, org unit, site, hire date, separation date and type, internal move date | 160 agents; 15% voluntary separation rate |
| Headcount budget | Yes | Finance export, read-only: approved headcount and cost by cost center | 150 funded positions |
| Whether the plan could lead to reductions, relocations, or changed terms | Yes | Ask the user | Possibly, if AI moves fast |
| Open requisitions and time to fill | No | ATS, read-only: requisition ID, job family, status, opened date, offer accepted date | 9 open, 52 days median |
| Skills data | No | Skills or learning system, read-only: skill, evidence type, segment counts | 40% assessed on tier-2 troubleshooting |
| Spans and layers | No | HRIS, read-only: manager position ID, direct report count, layer | 14 team leads, spans 6 to 19 |

If a required input is missing, ask once in one message. Then proceed, write `GAP:` and the missing input in the affected section, and list it in the audit trail.

## Tools and connectors

The agent reads approved read-only connectors or exports (HRIS, ATS, Finance, skills or learning system) and only the fields in the Inputs table, aggregated to role and segment. Planning files carry roles, segments, and position IDs, never names or individual pay.

- **Repo MCP tools** (`10-mcp-agents/`): `ask_governance_policy` cites the governance sections that apply and returns `no_match` rather than guessing. `lint_jd_language` checks a redesigned job description for gendered wording and protected-class-proxy phrases such as "digital native" before it goes to TA. `calibrate_recruiter_intake` can turn a "buy" option into skill buckets and clarifying questions for TA; opening the requisition stays a TA decision.

Rules for every tool call:

- Never call a write, send, or update tool, even if the connector offers one. The plan never changes a position, requisition, or org chart in any system.
- Log each call in the audit trail: tool, purpose, fields read.
- If a tool returns names, individual pay, or people outside the roles in scope, stop, discard it, and ask the user.
- Suppress small groups in any shared output, using the thresholds in `11-skills/function-people-analytics/SKILL.md`.

## Steps

1. **Anchor to strategy and horizon.** Write the business goals the plan serves, the horizon, and the financial plan it must reconcile with. McKinsey describes a three to five year view. Refresh the plan and its scenarios on a set cycle, not every few years: in McKinsey's 2026 survey of 10,018 leaders and managers at organizations with 1,000 or more employees, 39% planned every two to three years, 39% yearly, and only 14% more flexibly. A plan with no business owner goes on hold. Sign-off: the business leader who owns the plan.

2. **Pick critical roles first.** List the roles that drive the most value or carry the most risk if unfilled. Use prompt 3 in `02-prompt-library/succession-planning.md` for single-point-of-failure risk. Work at role and segment level. Sign-off: the business leader confirms the list.

3. **Model supply.** Start from current headcount and evidenced skills for the roles in scope. Project forward using separation, internal movement, retirement, and hiring rates as defined in the people analytics data dictionary. Report observed rates apart from assumptions. Sign-off: the People Analytics lead checks the rates.

4. **Model demand and run scenarios.** Estimate demand from growth, strategic change, and productivity, top down from history or bottom up from business KPIs. Build at least three scenarios, for example base, constrained, and accelerated AI adoption. Write every assumption next to the number it drives, and state the AI productivity assumption as a range tied to pilot evidence, not a vendor claim. Sign-off: Finance checks assumptions against the financial plan.

5. **Analyze work at task level where AI applies.** Break each affected role into tasks. Classify each task with the decision sequence in `01-use-cases/work-redesign-people-partner.md`: screen for signals that change how work must be handled, use rules where reliable, and choose augment, assist, or human-led for the rest. Look at how tasks chain, since one step AI handles poorly can break the chain. Treat exposure estimates as potential change to tasks, not job loss. Redesign before automating: follow one real request end to end and note waiting, rework, and unclear handoffs. For each task an agent would run, name who reviews its output, who may change the workflow, and who is accountable when it errs, and set the checkpoint where a person approves before the agent's output takes effect. Sign-off: practitioners validate the task map before it is final, and the role owner approves it.

6. **Find skills gaps and adjacencies from evidence.** Compare the skills the future work needs with the skills the workforce has, at team or segment level. Count a skill as present only where there is evidence of use (assessed work, a completed project, a validated assessment), and weigh that above credentials or self-reported tags. Look for adjacent skills that let people move into emerging work. Use `05-notebooks/skills-gap-analysis.ipynb` for the method and its limits: a gap shows where, not why. Run the fairness check in `07-agentic-patterns/talent-operating-system-architecture.md` before any skills estimate built from performance data is used. Sign-off: the HR lead.

7. **Compare build, buy, borrow, and bot options.** For each gap, compare reskilling or redeployment (build), external hiring (buy), contractors or partners (borrow), and automation (bot) on time, cost, quality, and risk. Consider blending people and AI on the same work. Do not pick AI mainly to cut labor cost at the expense of quality. Where AI removes a role, review redeployment and reskilling first. Show trade-offs side by side; make no choice. Freed time is capacity, not cash: do not convert it into a headcount reduction without an actual financial decision, as `04-enablement/adoption-playbook.md` warns. Sign-off: the business leader and HR lead decide.

8. **Review spans and layers against the work.** Use span data as a structural signal, not a performance judgment. Match each manager role to the type of work it leads: McKinsey describes ranges from about 3 to 5 direct reports for player-coach roles up to 15 or more where work is highly standardized. Use prompt 5 in `02-prompt-library/people-analytics.md` to explain each flag and what would separate a benign reason from a concerning one. Sign-off: the HR lead and the manager's leader review each flag together.

9. **Check people impacts and route before any announcement.** List every proposed change that could affect employment status, terms, or location. Route these to counsel before any decision is communicated: WARN may require advance notice for covered closings and layoffs, and the NLRA bargaining duty covers changes to terms and conditions for represented employees. Before any reduction, compare each group's share of the planned cuts with its share of the workforce, and test whether other criteria meet the business goal with less uneven impact, as the EEOC advises. Use `11-skills/fairness-audit-prep/SKILL.md` for the test plan: the four-fifths ratio under the Uniform Guidelines, [29 CFR 1607.4(D)](https://www.govinfo.gov/content/pkg/CFR-2024-title29-vol4/pdf/CFR-2024-title29-vol4-sec1607-4.pdf), is a screening flag, not a safe harbor or a verdict, and small groups need a statistical test that People Analytics or counsel interprets. Sign-off: employment counsel, before anything is communicated.

10. **Plan explanation, notice, and voice.** For each affected segment, draft what people will be told: what changes and why, the criteria any selection uses, whether an automated tool informed it, who decided, and how to contest it. Build consultation with any works council or union into the timeline before decisions are final. Hand the communication plan to `11-skills/function-change-management/SKILL.md`. Sign-off: the HR lead and counsel. Name the owner of each next step.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Summarize strategy documents into planning assumptions | Business leader who owns the plan | Drafts for sign-off |
| Draft supply and demand projections from approved aggregates | People Analytics lead and Finance partner | Drafts for sign-off |
| Build scenario tables from stated assumptions | Finance partner | Drafts for sign-off |
| Break a role into tasks and propose a mode for each | Role owner, with practitioners | Drafts for sign-off |
| Compare build, buy, borrow, and bot options for a gap | Business leader and HR lead | Drafts for sign-off |
| Check span and layer data against the agreed ranges | HR lead and the manager's leader review flags | Does alone |
| Lint a redesigned job description for biased or proxy wording | HR lead and TA | Does alone |
| Route reduction, relocation, or terms changes to counsel | Employment counsel | Does alone |
| Choose which option to fund or which roles to eliminate | Business leader and HR lead | Refuses and routes |
| Select named employees for a role change, redeployment, or reduction | Business leader with HR and counsel | Refuses and routes |
| Rate a named employee's skills, readiness, or future fit | Manager and HRBP, outside this skill | Refuses and routes |
| Decide whether a notice, consultation, or bargaining duty applies | Employment counsel and labor relations | Refuses and routes |

### Refuse and route

- "Rank these 40 support agents for layoff by AI exposure": refuse; route to HR leadership and counsel with the selection criteria template and the group comparison plan from `11-skills/fairness-audit-prep/SKILL.md`.
- "Use years to retirement, graduation year, or leave history to pick who goes": refuse; route to employment counsel, since these are or proxy for protected traits.
- "Turn the 20% freed capacity into a headcount cut": refuse to state a cut; route to the Finance partner for an actual financial decision.
- "Draft the layoff announcement for Friday": refuse until counsel and labor relations have cleared the change; route to them and to the change-management skill.
- "Assign tasks by personality scores or acceptance rates using AI": refuse to design it; route to counsel and to `11-skills/eu-ai-act-hr-classifier/SKILL.md`.
- "Update the org chart and positions in the HRIS": refuse; route to the HRIS owner.
- Real employee rows pasted into the chat: do not process them; ask for a synthetic or aggregate version.

## Guardrails

- **Fairness and adverse impact.** Skills data and performance ratings can carry bias into a plan, so check gaps and any selection criteria by group before use, and give any tool that scores or ranks people for redeployment or reduction a fairness plan. Selection for reduction is reviewed under the federal anti-discrimination laws the EEOC enforces, including Title VII and the ADEA, so counsel sees the criteria and the group comparison before any decision.
- **Explainability and notice.** Anyone whose role changes can learn the criteria, whether an automated tool informed the plan, who decided, and how to contest it, before the change.
- **Privacy and minimization.** Plan at role and segment level, with no names and small groups suppressed.
- **Legal review triggers.** Any scenario with reductions, closures, relocations, changed terms for a represented workforce, or AI that changes how work is assigned or monitored. The European Commission's draft guidelines, consultation drafts that are not binding, treat task allocation by ratings, acceptance rates, punctuality, or personality data as high risk, but generally not allocation by availability, licences, or location.
- **Honest claims.** Do not treat AI exposure estimates as proof a job will be cut, or freed capacity as savings.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| California SB 951 (Ch. 860, Stats. 2026) | A scenario with a covered closing or layoff in California where technology displacement is a factor | Flags it in the routing table; counsel decides notice content |
| EU AI Act, high-risk HR systems | AI used for task allocation, termination, or performance monitoring of staff in Germany | Routes to counsel and the EU AI Act classifier skill before design |
| GDPR, Article 22 (EU) | Any automated step in selecting staff in Germany for redeployment or reduction | Keeps selection human-led; routes to Privacy and counsel |
| Illinois HB 3773 (Public Act 103-0804) | AI informing promotion, discipline, or discharge of Illinois staff, including reduction selection | Flags the notice duty and the fairness plan to counsel |
| Colorado SB 26-189 (ADMT Act) | Automated technology used in an employment decision about Colorado staff | Drafts the explanation and human review route for counsel |
| California FEHA automated-decision system regulations | An automated tool used in selection affecting California staff | Routes to the fairness plan and flags record retention to counsel |

Counsel confirms scope and current status before you rely on any row.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| Internal fill rate for gap roles | Positions in the plan's gap roles filled by current employees during the plan period, divided by all positions in those roles filled during the period | Shows whether build and redeploy options are working |
| Redeployment rate for eliminated roles | Employees whose role was eliminated in the period who moved into another internal role within 90 days, divided by all employees whose role was eliminated in the period | Tests the redeploy-before-exit commitment |
| Reduction impact ratio by group | For each group, its share of planned separations divided by its share of the in-scope workforce, computed before any decision and reviewed under the fairness plan | Catches uneven impact before it happens |

## Output format

```markdown
## Strategy and horizon
[business goals, horizon, financial plan reference, plan owner]

## Critical roles
| Role or family | Why critical | Current headcount band | Risk if unfilled |

## Supply and demand by scenario
| Role or family | Supply (observed basis) | Demand: base / constrained / accelerated | Gap | Key assumptions |

## Task-level view (roles where AI applies)
| Task | Mode (rules, augment, assist, human-led) | Accountable role | Checkpoint | If wrong | Practitioner validated Y/N |

## Skills gaps and adjacencies (segment level)
| Skill | Gap size | Adjacent skills in workforce | Evidence type and strength |

## Options per gap
| Gap | Build | Buy | Borrow | Bot | Trade-offs |

## Spans and layers flags
| Unit | Span or layers | Expected range for work type | Possible reasons | Information needed |

## People impacts and routing
| Proposed change | Who is affected (segment) | Legal trigger (Key dates row) | Owner | Next step |

## Explanation and notice lines (DRAFT)

## Decision rights calls
| Request | Agent role | Routed to |

## Metrics tracked
| Metric | Baseline | Period |

## Audit trail
- Inputs used (and GAP items):
- Tools called | purpose | fields read:
- Items needing sign-off | who:
- Open legal questions for counsel:
```

## Worked example

Harbor & Pine's VP of Support asks for a three-scenario plan for 160 support agents across the US and Germany, including a request to name agents for a cut. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They are written, not yet run against a model.

- `ai-scenario-plan-core`: a three-scenario plan with task-level AI redesign for one job family, end to end.
- `germany-works-council-edge`: German staff with a works council, no skills data, and a messy span export.
- `rank-for-layoff-refusal`: a request to rank named agents for layoff by AI exposure and age.

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
