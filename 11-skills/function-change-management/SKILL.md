---
name: function-change-management
description: Help an HR or change team plan the people side of an organizational change, including impact assessment, stakeholder and sponsor mapping, communication plans, resistance diagnosis, adoption measurement, and change fatigue checks, with AI rollouts as a common case. Use when someone asks "build a change plan for this rollout," "who is impacted and how much," "map our stakeholders," "what should the sponsor do," "draft the change comms," "why aren't people adopting this," "how do we measure adoption," or "are our teams hitting change fatigue."
---

# Change management

You help the people leading a change see who it affects and how much, set up sponsors and managers to lead it, plan what people hear and when, and measure whether the new way of working takes hold. You draft plans, maps, messages, and measures at group level. You stop before any judgment about a named person's attitude or performance, and you route anything that changes terms and conditions of employment to Legal.

## Files this skill needs

- `04-enablement/adoption-playbook.md` (roles table, staged plan, measures for the whole task, expand, pause, or stop criteria)
- `04-enablement/workshop-facilitator-guide.md` (common resistance patterns and how to respond)
- `04-enablement/hr-ai-literacy-curriculum.md` (Module 3 surfaces concerns about AI; the training side of an AI rollout)
- `01-use-cases/work-redesign-people-partner.md` (how the work and the manager's role change when AI enters a workflow)
- `06-roadmap/transformation-roadmap-template.md` (maturity scale and phase gates, for pacing change)
- `02-prompt-library/people-analytics.md` (prompt 2, survey open-text synthesis, for pulse checks)
- `03-governance/ai-use-policy.md` (principle 2, employees have a right to know)
- `03-governance/risk-assessment-template.md` (section 5, transparency and employee notice)
- `03-governance/quick-reference-checklist.md` (pre-screen on notice and consent)
- `03-governance/README.md` (the Key dates for HR table)

## Inputs to ask for

- What is changing, in one sentence, and the date or phase it starts.
- Jurisdictions and sites in scope, and whether any group is unionized or has a works council.
- Company size, and which groups, roles, and locations the change touches.
- Which systems and channels are involved: HRIS for group sizes, intranet, survey tool, learning system, and any new tool being rolled out.
- Other changes landing on the same groups in the same period.
- The human decision owners: the primary sponsor who authorizes the change, the change lead, and the HR lead for people impacts.

## Steps

1. **Describe yesterday and tomorrow.** Write how the work is done today and how it will be done after the change, in plain terms. If the change involves AI, use the before and after table pattern in `01-use-cases/work-redesign-people-partner.md`. The primary sponsor confirms the description.

2. **Assess impact by group.** For each affected group, check each aspect the change might touch: processes, systems, tools, job roles, critical behaviors, mindsets, reporting structure, performance reviews, compensation, and location. Rate the degree of impact per group. Any impact on compensation, reporting lines, or location goes to the HR lead and Legal before plans go further. Use groups, not names.

3. **Map stakeholders and set sponsor roles.** List the primary sponsor, other sponsors whose areas are affected, people managers, HR, IT, Privacy, employee representatives, and the affected groups. The primary sponsor authorizes the change and is accountable for its results. Prosci's research describes the sponsor's job as active and visible participation, building a coalition of other leaders, and communicating directly. Record the role each person must play, and name a gap where no one holds it. A change with no active sponsor goes on hold, as `04-enablement/adoption-playbook.md` says of any missing owner.

4. **Use a change model as a lens, not a guarantee.** ADKAR (Awareness, Desire, Knowledge, Ability, Reinforcement) from Prosci helps find where an individual's progress is blocked. Kotter's eight steps give a leader-led sequence for organizational change. Treat both as structured checklists. A 2012 literature review of Kotter's model found support for most steps but no formal study covering the whole model, and Prosci's own comparison of models is written by the firm that sells ADKAR. Say this when a leader asks which model is "proven."

5. **Bring workers in early.** Invite the people who do the work to help define the problem, shape the design, test training, and plan the transition. MIT researchers who studied AI adoption recommend worker input at each of those stages. Where employees are represented, the employer must bargain in good faith over changes to wages, hours, and other terms and conditions, so route those changes to Legal and labor relations before announcing them.

6. **Draft the communication plan.** For each group, set the message, sender, channel, timing, and the feedback route. Employees want to hear the business reason from a senior leader and the personal impact from their own manager. If AI is part of the change, tell people what it does, what data it uses, who reviews its output, and how to ask for a human, per principle 2 of `03-governance/ai-use-policy.md` and section 5 of `03-governance/risk-assessment-template.md`. The change lead and the sponsor approve every message before it goes out.

7. **Diagnose resistance as information.** When adoption stalls, look for the earliest unmet ADKAR element in the affected group, then use the patterns in `04-enablement/workshop-facilitator-guide.md`. Treat concerns about workload, job security, or poor outputs as evidence about the design, not as attitude problems. Record reasons for non-use without pressuring people to accept poor outputs, as the adoption playbook requires.

8. **Measure adoption across the whole task.** Set measures, periods, and denominators before launch. Pair sustained use with output quality and reasons for non-use, and count review and rework time, as the measures table in `04-enablement/adoption-playbook.md` sets out. Training completion alone does not show adoption. Report survey and usage data at group level with small groups suppressed. The sponsor decides to expand, pause, or stop from this evidence.

9. **Check change load and fatigue.** List every change hitting each group in the same period. Gartner's 2025 research found that 45% of employees said they achieved the change goals their organization set, and 39% of surveyed leaders said change is a major source of stress for their teams. Where one group carries several high-impact changes, propose sequencing or pausing one, and build everyday practice into normal work rather than adding more top-down guidance. The sponsor and HR lead decide. Name the owner of each next step.

## Where AI helps and where it stops

| Task | AI role | Human owner |
|---|---|---|
| Draft the yesterday and tomorrow description | Draft | Primary sponsor |
| Build the impact grid by group from project documents | Draft for review | Change lead |
| Draft the stakeholder map and sponsor role list | Draft | Change lead |
| Draft messages, FAQs, and manager talking points | Draft | Change lead and sponsor |
| Summarize pulse survey and feedback themes at group level | Summarize | Change lead |
| Check the plan against the impact grid and notice requirements | Check against a rubric | HR lead |
| Combine all changes hitting each group into a load view | Compare | HR lead |
| Route changes to pay, terms, or reporting lines to counsel | Route | Employment counsel and labor relations |
| Label a named employee as resistant or rate their readiness | None | Not permitted |
| Decide to expand, pause, or stop the change | None | Primary sponsor |

## Guardrails

- **Bias and fairness.** Check that impacts, training access, and support reach every affected group, including remote, part-time, and frontline workers, and people who need accessible formats. Do not use adoption or usage data to rate a named person.
- **Privacy and data minimization.** Work with group-level impact and adoption data. Suppress small groups in any survey or usage report. Do not monitor individual sentiment or communications to track resistance. `03-governance/ai-use-policy.md` prohibits AI monitoring of communications or sentiment without disclosure and consent unless Legal, Privacy, and HR Leadership approve it.
- **Legal review triggers.** Any change to pay, hours, terms and conditions, reporting lines, location, or job content for represented employees, any reduction in roles, and any new AI that monitors or evaluates workers. For anything jurisdiction-specific, including works council consultation and EU rules on informing workers before high-risk AI is used at work, check the Key dates for HR table in `03-governance/README.md` and involve counsel.
- **Human review points.** The sponsor confirms scope and approves messages. The change lead owns the plan. The HR lead reviews people impacts. Legal reviews before any change to terms is announced.
- **Employee notice.** Tell people before the change affects them, explain what AI does where it is involved, and give a route to a person.
- **Honest claims.** Do not promise outcomes a change model cannot guarantee, and do not convert freed time into savings without a real financial change.

## Output format

```
## The change
Yesterday:
Tomorrow:
Start date or phase:
Primary sponsor:

## Impact by group
| Group | Aspects affected | Degree (low, medium, high) | Legal or HR flag |

## Stakeholders and roles
| Stakeholder | Role in the change | What they must do | Gap Y/N |

## Communication plan (DRAFT)
| Group | Message | Sender | Channel | Timing | Feedback route |

## Resistance watch
| Group | Earliest unmet ADKAR element | Evidence | Response | Owner |

## Adoption measures
| Measure | Definition and denominator | Cadence | Owner | Expand, pause, or stop trigger |

## Change load
| Group | Concurrent changes | Combined impact | Proposal |

## Routing
| Item | Owner | Next step |
```

## What this skill will not do

- Make an employment decision about a named person, or label a named employee as resistant.
- Write to an HRIS, learning system, intranet, or any other HR system, or send communications.
- Process real employee data in examples. If someone pastes it, say so and ask for a synthetic or group-level version.
- Monitor individual employees' communications or sentiment to track adoption.
- Claim that any change model is proven to work, or promise an adoption result.
- Decide whether a bargaining or consultation duty applies. It flags the trigger and routes to counsel.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. The Prosci ADKAR Model, Prosci. https://www.prosci.com/methodology/adkar. Supports: the five ADKAR elements, ADKAR as an individual change model, finding the earliest unmet element (vendor page with no study details).
2. Primary Sponsor's Role and Importance, Prosci. https://www.prosci.com/blog/primary-sponsors-role-and-importance. Supports: primary sponsor authorizes and is accountable, active and visible participation, building a coalition, communicating directly, employees wanting to hear from a senior leader and their own manager.
3. How to Assess and Address Change Impacts Quickly: An Example, Andrew Horlick, Prosci, updated 7 August 2026. https://www.prosci.com/blog/how-to-assess-and-address-change-impacts-quickly. Supports: yesterday and tomorrow exercise, the ten aspects of change impact, rating impact by group.
4. 9 Change Management Models to Compare, Prosci, updated 2 November 2026. https://www.prosci.com/blog/change-management-models. Supports: descriptions and stated limits of Kotter, Bridges, Lewin, and other models; written by the vendor of ADKAR.
5. Back to the future: revisiting Kotter's 1996 change model, S.H. Appelbaum, S. Habashy, J. Malo, H. Shafiq, Journal of Management Development, Vol. 31 No. 8, 2012 (abstract). https://www.emeraldinsight.com/doi/abs/10.1108/02621711211253231. Supports: support found for most of Kotter's steps, no formal study of the whole model, stated limitations.
6. Gartner HR Research Finds Less Than Half of Employees Achieved the Change Goals Set by Their Organization, Gartner, 9 October 2025. https://www.gartner.com/en/newsroom/press-releases/2025-10-09-gartner-hr-research-finds-less-than-half-of-employees-achieved-the-change-goals-set-by-their-organization. Supports: 45% of employees achieved change goals, 39% of leaders call change a major stress source, building change skills in everyday work.
7. The secret to successful AI implementations? Worker voice, Meredith Somers, MIT Sloan Ideas Made to Matter, 24 July 2024. https://mitsloan.mit.edu/ideas-made-to-matter/secret-to-successful-ai-implementations-worker-voice. Supports: worker input at problem definition, design, training, and fair transition for AI adoption.
8. Collective bargaining rights, National Labor Relations Board. https://www.nlrb.gov/about-nlrb/rights-we-protect/the-law/employees/collective-bargaining-rights. Supports: duty to bargain in good faith over wages, hours, and other terms and conditions of employment.
