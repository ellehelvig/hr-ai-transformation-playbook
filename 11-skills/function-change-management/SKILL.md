---
name: function-change-management
description: Plans the people side of an organizational change at group level, producing a yesterday and tomorrow description with human and AI decision zones, an impact grid by group, a sponsor and stakeholder map, draft communications and manager talking points, a resistance diagnosis, adoption measures with expand, pause, or stop triggers, and a change-load view, with AI rollouts as the common case. Use whenever someone asks for a change plan for a rollout or reorg, who is impacted and how much, a stakeholder map or sponsor roles, change comms or an FAQ, why people are not adopting a tool, how to measure adoption, whether teams have change fatigue, or which change model is proven, and before any message about a change to pay, terms, reporting lines, or location goes out.
---

# Change management

This skill serves the sponsor, change lead, and HR lead running a change. It produces a before and after description, an impact grid, a sponsor map, draft messages, a resistance watch, adoption measures, and a change-load view, all at group level. It stops before any judgment about a named person, never sends a message, and routes changes to terms of employment to counsel.

## Files this skill needs

- `04-enablement/adoption-playbook.md` (roles table, staged plan, measures for the whole task, expand, pause, or stop criteria)
- `04-enablement/workshop-facilitator-guide.md` (common resistance patterns and how to respond)
- `04-enablement/hr-ai-literacy-curriculum.md` (Module 3 surfaces concerns about AI; the training side of an AI rollout)
- `01-use-cases/work-redesign-people-partner.md` (before and after table; how the work and the manager's role change when AI enters a workflow)
- `02-prompt-library/people-analytics.md` (prompt 2, survey open-text synthesis, for pulse checks)
- `03-governance/ai-use-policy.md` (principle 2, employees have a right to know; the rule on monitoring communications or sentiment)
- `03-governance/risk-assessment-template.md` (section 5, transparency and employee notice)
- `03-governance/quick-reference-checklist.md` (pre-screen on notice and consent)
- `03-governance/README.md` (the Key dates for HR table)

## Inputs

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| What is changing, and the start date or phase | Yes | Ask the user | AI case-drafting assistant, pilot from 2 March |
| Primary sponsor, change lead, and HR lead | Yes | Ask the user | CHRO; HR transformation lead; HRBP lead |
| Affected groups and their sizes | Yes | HRIS, read-only: org unit, job family, site, work arrangement (remote, part-time, frontline) counts | 30 service center agents, 180 managers |
| Sites, jurisdictions, and any union or works council | Yes | HRIS, read-only: headcount by country, state, site; ask labor relations | US states, Germany (works council) |
| Whether AI is involved, what it does, and what data it uses | Yes | Ask the user; vendor documentation | Drafts replies from case history |
| Other changes hitting the same groups in the period | Yes | Ask the user | New case system in Q1 |
| Channels and feedback routes | No | Ask the user | Team meetings, intranet, pulse survey |
| Adoption and usage data | No | Tool usage export, read-only: active users and task counts by group, weekly | 21 of 30 agents active in week 4 |
| Training completion | No | LMS, read-only: completion counts by group | 26 of 30 completed |
| Pulse results | No | Survey platform, read-only: scores and themes for groups at or above threshold | Trust item 3.4 of 5 |

If a required input is missing, ask for it once, in one short question at the top of your reply. Then proceed, write `GAP:` and the missing input in the affected section, and list it in the audit trail.

## Tools and connectors

The agent reads approved read-only connectors or exports (HRIS, tool usage export, LMS, survey platform) and only the fields in the Inputs table, aggregated by group. No names, per-person usage logs, or respondent-level rows.

- **Email, chat, and intranet connectors:** not used to send, post, or schedule anything. Drafts are returned to the change lead.
- **Repo MCP tools** (`10-mcp-agents/`): `ask_governance_policy` cites the notice and monitoring rules in `03-governance/` and returns `no_match` rather than guessing. `lint_jd_language` checks messages, FAQs, and talking points for gendered wording and protected-class-proxy phrases such as "digital native".

Rules for every tool call:

- Never call a write, send, post, or update tool, even if the connector offers one.
- Log each call in the audit trail: tool, purpose, fields read.
- If a tool returns per-person usage, message content, or people outside the affected groups, stop, discard it, and ask the user.
- Report survey and usage data at group level with small groups suppressed.

## By maturity stage

Stages follow the repo's maturity scale in [the roadmap template](../../06-roadmap/transformation-roadmap-template.md). Decision rights in this skill are the same at every stage.

| Stage | How to run it | Before moving up |
|---|---|---|
| Start (Levels 0 to 1) | Paste the change, affected group counts by site and work arrangement, and other changes in the period. The change lead checks each draft; a person sends. | Sponsor confirms the before and after description. |
| Pilot (Level 2) | One weekly read-only usage export: active users and task counts by group, pilot unit only. Metric: sustained use rate at day 90. | Sponsor records the expand, pause or stop decision. |
| Scale (Level 3) | Read-only HRIS, usage, LMS and survey connectors; tracks support access ratio, small groups suppressed. Messaging connectors never send. AI notice reaches every group before go-live. | Remote, part-time and frontline access reviewed. |
| Embed (Levels 4 to 5) | A new rollout entering the portfolio triggers the load view and drafts. The sponsor still decides; the change lead sends. | Rerun the test cases in `evals/` when the skill or model changes. |

## Steps

1. **Describe yesterday and tomorrow.** Write how the work is done today and how it will be done after the change, in plain terms. For AI, use the before and after table in `01-use-cases/work-redesign-people-partner.md`. Follow one real request end to end and ask the people closest to the work where it is harder than it should be. Redesign before you automate: combine handoffs, cut steps that do not change the outcome, and agree standard inputs and a definition of done. Then mark each step human-led, human with AI support, or run by AI within set limits, and name the checkpoint where a person reviews the output before it takes effect. Sign-off: the primary sponsor confirms the description.

2. **Assess impact by group.** For each affected group, check processes, systems, tools, job roles, critical behaviors, mindsets, reporting structure, performance reviews, compensation, and location. Rate the degree of impact per group. Check whether the change moves work onto managers (coaching, approvals, questions) and what time and guidance come with it. List the skills the new way of working needs per group. Any impact on compensation, reporting lines, or location goes to the HR lead and counsel before plans go further. Give every affected group a degree of impact, external groups such as customers included; where evidence is thin, give a provisional degree and say what would confirm it. Sign-off: the change lead.

3. **Map stakeholders and set sponsor roles.** List the primary sponsor, other sponsors whose areas are affected, people managers, HR, IT, Privacy, employee representatives, and the affected groups. The primary sponsor authorizes the change and is accountable for its results. Prosci's research describes the sponsor's job as active and visible participation, building a coalition of other leaders, and communicating directly. Name any role no one holds. Before launch, check that senior leaders tell the same story: in Microsoft's 2026 Work Trend Index survey of 20,000 knowledge workers who use AI, only 26% said their leadership was clearly and consistently aligned on AI. A change with no active sponsor goes on hold, as `04-enablement/adoption-playbook.md` says of any missing owner. Sign-off: the primary sponsor.

4. **Use a change model as a lens, not a guarantee.** ADKAR (Awareness, Desire, Knowledge, Ability, Reinforcement) from Prosci helps find where an individual's progress is blocked. Kotter's eight steps give a leader-led sequence. Both are structured checklists. A 2012 literature review of Kotter's model found support for most steps but no formal study of the whole model, and Prosci's own comparison of models is written by the firm that sells ADKAR. Say this when a leader asks which model is "proven."

5. **Bring workers in early.** Invite the people who do the work to help define the problem, shape the design, test training, and plan the transition. MIT researchers who studied AI adoption recommend worker input at each of those stages. Where employees are represented, the employer must bargain in good faith over changes to wages, hours, and other terms and conditions, so route those changes to counsel and labor relations before announcing them. Where there is a works council, plan its consultation into the timeline before decisions are final. Sign-off: the change lead, with labor relations where employees are represented.

6. **Draft the communication plan.** For each group, set the message, sender, channel, timing, and feedback route. Employees want the business reason from a senior leader and the personal impact from their own manager, so brief managers before their teams. Describe AI changes at task level, not whole jobs. If AI is part of the change, every group's message says what the AI does, what data it uses, who reviews its output, what it will not be used for (for example, rating individual performance), and how to ask for a human or raise a concern, per principle 2 of `03-governance/ai-use-policy.md` and section 5 of `03-governance/risk-assessment-template.md`. Run each draft through `lint_jd_language`. Sign-off: the change lead and sponsor approve every message, and a person sends it.

7. **Build skills in the flow of work.** Pair any training with practice on real tasks, and count a skill as built when people show it on the job, not when a course is completed. Make training reach every group, including remote, part-time, and frontline workers and people who need accessible formats. Sign-off: the HR lead, with L&D.

8. **Diagnose resistance as information.** When adoption stalls, find the earliest unmet ADKAR element in the affected group, then use the patterns in `04-enablement/workshop-facilitator-guide.md`. Treat concerns about workload, job security, or poor outputs as evidence about the design. Record reasons for non-use without pressuring people to accept poor outputs, as the adoption playbook requires. Sign-off: the change lead.

9. **Measure adoption across the whole task, with checkpoints.** Start with a volunteer-led pilot in one unit and pace the rollout to what people can absorb. Set review points, for example at about 30, 60, and 90 days: first what people do and what blocks them, then what is working and where support is missing, then whether to embed, redesign, or retire the change. Set measures, periods, and denominators before launch. Pair sustained use with output quality, reasons for non-use, and review and rework time, per the measures table in `04-enablement/adoption-playbook.md`. Training completion alone does not show adoption. Expand only when outcomes, trust, and fair access hold or improve. Usage data never feeds an individual's performance review. Sign-off: the sponsor decides to expand, pause, or stop from this evidence.

10. **Check change load and fatigue.** List every change hitting each group in the same period. Gartner's 2025 research found that 45% of employees said they achieved the change goals their organization set, and 39% of surveyed leaders said change is a major source of stress for their teams. Where one group carries several high-impact changes, propose sequencing or pausing one, and build practice into normal work rather than adding top-down guidance. Sign-off: the sponsor and HR lead decide. Name the owner of each next step.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Draft the yesterday and tomorrow description and propose human-led, shared, and AI-run steps | Primary sponsor, with the people who do the work | Drafts for sign-off |
| Build the impact grid by group | Change lead | Drafts for sign-off |
| Draft the stakeholder map and sponsor role list | Change lead | Drafts for sign-off |
| Draft messages, FAQs, and manager talking points | Change lead and sponsor | Drafts for sign-off |
| Summarize pulse and feedback themes at group level | Change lead | Drafts for sign-off |
| Check the plan against the impact grid and notice requirements, and lint drafts | HR lead reviews findings | Does alone |
| Combine all changes hitting each group into a load view | HR lead reviews it | Does alone |
| Route changes to pay, terms, reporting lines, or location to counsel | Employment counsel and labor relations | Does alone |
| Send, post, or schedule any message | Change lead, after sponsor approval | Refuses and routes |
| Label a named employee as resistant or rate their readiness | Not permitted | Refuses and routes |
| Use adoption or usage data in an individual's review | Not permitted | Refuses and routes |
| Decide to expand, pause, or stop the change | Primary sponsor | Refuses and routes |

### Refuse and route

- "List the agents who haven't used the tool so managers can talk to them about their attitude": refuse; offer group-level usage and reasons for non-use; route to the change lead.
- "Run sentiment analysis on Slack or Teams to find the resisters": refuse; route to Legal, Privacy, and HR Leadership, since `03-governance/ai-use-policy.md` bars monitoring communications or sentiment without disclosure and consent unless they approve.
- "Send this to all staff now" or "post it to the intranet": refuse to send; return the draft to the change lead and sponsor.
- "Announce the new reporting lines or pay structure before Legal sees it": refuse; route to counsel and labor relations, and to the works council timeline where one exists.
- "Make tool usage a performance goal": refuse; route to the HR lead and performance management owner.
- "Tell staff ADKAR is proven to get 90% adoption": refuse the claim; offer the honest description from step 4.
- Real employee data pasted into the chat: do not process it; ask for a synthetic or group-level version.

## Guardrails

- **Fairness and access.** Check that training and support reach every affected group. If the change introduces AI that selects, scores, or ranks people, route it to `11-skills/fairness-audit-prep/SKILL.md`, where the four-fifths ratio under [29 CFR 1607.4(D)](https://www.govinfo.gov/content/pkg/CFR-2024-title29-vol4/pdf/CFR-2024-title29-vol4-sec1607-4.pdf) is a screening flag, not a verdict. Never use adoption data to rate a named person.
- **Explainability and notice.** Tell people before the change affects them what AI does, what it will not be used for, and how to reach a person.
- **Privacy and minimization.** Use group-level data with small groups suppressed. Never monitor individual sentiment or communications.
- **Legal review triggers.** Any change to pay, hours, terms and conditions, reporting lines, location, or job content for represented employees, any reduction in roles, and any new AI that monitors or evaluates workers. Check the rows in the Regulation map and involve counsel.
- **Honest claims.** Do not promise outcomes a change model cannot guarantee, and do not convert freed time into savings without a real financial change.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| EU AI Act, high-risk HR systems | Rollout of AI for task allocation, performance monitoring, or similar uses affecting staff in Germany | Flags worker information duties to counsel; plans works council timing |
| EU AI Act, transparency | Staff will talk to an AI assistant, or messages include AI-generated content | Drafts the line telling people they are dealing with AI, for counsel to confirm |
| EU AI Act, emotion recognition at work (Article 5(1)(f)) | A request to read staff emotions to track resistance | Refuses and routes to Legal |
| California AB 1883 (Ch. 853, Stats. 2026) | Emotion inference or neural data about California staff | Refuses and routes to Legal |
| Illinois HB 3773 (Public Act 103-0804) | The rolled-out AI is used in hiring, promotion, discipline, or discharge affecting Illinois staff | Adds the notice to the communication plan for counsel review |
| EU AI Act, AI literacy (Article 4) | Staff in Germany will operate or use the new AI system | Routes the training plan to L&D and counsel to check the current text |

Counsel confirms scope and current status before you rely on any row. In your reply, name each rule as: see the Key dates row "exact row name" in `03-governance/README.md`. Stop there: do not write the row's dates, status or regulation numbers, even ones you read in the table or in Sources, because the table is the one place they are kept current.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| Sustained use rate at day 90 | People in the target group who completed the defined task the new way in at least 3 of the 4 weeks before day 90, divided by people in the target group whose role includes that task | Shows the change took hold, not just launched |
| First-pass quality rate | Tasks completed the new way in the month that passed the agreed quality check without rework, divided by all tasks completed the new way in the month | Use without quality is not adoption |
| Support access ratio | Lowest group's rate of completing role-based training or a support session within 30 days of go-live, divided by the highest group's rate, across remote, part-time, frontline, and other groups | Catches groups left behind before they fall behind |

## Output format

```markdown
## The change
Yesterday:
Tomorrow:
Start date or phase:
Primary sponsor:
Decision zones: [step, human-led / human with AI / AI-run, checkpoint]

## Impact by group
| Group | Aspects affected | Degree (low, medium, high) | Skills needed | Legal or HR flag |

## Stakeholders and roles
| Stakeholder | Role in the change | What they must do | Gap Y/N |

## Communication plan (DRAFT, not sent)
| Group | Message | Sender | Channel | Timing | Feedback route |
AI notice lines: what it does, data used, who reviews, what it is not used for, how to reach a person

## Resistance watch
| Group | Earliest unmet ADKAR element | Evidence | Response | Owner |

## Adoption measures
| Measure | Definition and denominator | Cadence | Owner | Expand, pause, or stop trigger |

## Change load
| Group | Concurrent changes | Combined impact | Proposal |

## Decision rights calls
| Request | Agent role | Routed to |

## Routing
| Item | Owner | Next step |

## Audit trail
- Inputs used (and GAP items):
- Tools called | purpose | fields read:
- Items needing sign-off | who:
- Open legal questions for counsel:
```

## Worked example

Harbor & Pine's HR transformation lead plans the rollout of an AI case-drafting assistant to its HR service center in the US and Germany, including a request to flag agents who skip the tool. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They were run on 18 November 2026 with `claude-sonnet-5-5`, one fresh session per case, and graded in a separate pass; see [the results](../../09-evals/skill-eval-results-2026-11-18.md) for the method and its limits.

- `ai-assistant-rollout-core`: a full change plan for an AI assistant rollout to one function.
- `cross-border-no-sponsor-edge`: a US and Germany rollout with no named sponsor and a messy usage export.
- `sentiment-resisters-refusal`: a request to scan chat for resisters and email them directly.

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
9. AI in the Workplace Playbook, SHRM, 2025. Read from a copy of the publication; no web address checked. Supports: pilots with early adopters, middle managers as change champions, pacing change to what people can absorb, framing AI at task level.
10. 2026 Work Trend Index Annual Report, Microsoft, May 2026. Read from a copy of the publication; no web address checked. Supports: 26% of AI users surveyed report clear, consistent leadership alignment on AI.
11. Rearchitecting workflows: a leader's guide, Microsoft, 2026 (Work Trend Index leader guide). Read from a copy of the publication; no web address checked. Supports: following one real request end to end, redesign before automating, human-led, shared, and AI-run decision zones with checkpoints.
12. The Human Readiness Operating System, Wowledge, January 2026. Read from a copy of the publication; no web address checked. Supports: vendor-published white paper; checking whether change shifts work onto managers, expanding a pilot only when outcomes, trust, and equity improve.
