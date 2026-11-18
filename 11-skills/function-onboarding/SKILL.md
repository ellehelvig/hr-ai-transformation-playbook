---
name: function-onboarding
description: Plans a new hire's preboarding, first week and first 90 days, and scopes any AI onboarding assistant. Produces a preboarding checklist with owners, a compliance paperwork table, a manager-led first week, a buddy setup, a skills-linked 30/60/90 plan, an assistant scope with eval and notice, cohort check-in themes and an audit trail. Use whenever someone says build an onboarding plan, draft a 30/60/90, prep the manager for Monday, set up a buddy, what paperwork does a new hire need, can we add an AI onboarding assistant, can an agent handle I-9 reminders or laptop orders for new starters, summarize our 30-day check-ins, or tell me which new hires are struggling, and whenever an onboarding tool would track or evaluate new hires.
---

# Onboarding

For an HRBP, HR operations lead or hiring manager. It produces a new hire's first 90 days as drafts with owners, and checks any AI onboarding assistant against the playbook. It stops at the human parts: the manager's conversations, the buddy relationship, the employer's review of identity and work authorization documents, and any judgment of how a named new hire is doing.

## Files this skill needs

- `02-prompt-library/onboarding.md` (prompt 1 policy Q and A, 2 30/60/90 plan, 3 manager prep, 4 check-in synthesis, 5 buddy intro)
- `07-agentic-patterns/README.md` (Pattern 1, retrieval with verification, and Pattern 4, multi-step workflow with checkpoints)
- `10-mcp-agents/policy_qa/ENABLEMENT.md` (citation-first lookup that returns nothing rather than inventing an answer)
- `05-notebooks/hr-qa-agent-demo.ipynb` and `09-evals/hr-qa-agent-evals.yaml` (worked example and eval cases for a Q and A assistant)
- `03-governance/ai-use-policy.md` (principle 2 notice, 4 data minimization, 5 accuracy)
- `03-governance/quick-reference-checklist.md` and `03-governance/risk-assessment-template.md` (before buying or deploying an onboarding tool with AI features)
- `03-governance/README.md` (Key dates for HR table)

## Inputs

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| Role, level, team, start date, work arrangement | Yes | HRIS, read-only: job, level, department, start date, work arrangement | Support Engineer, L3, remote, starts 7 December |
| Work location | Yes | HRIS, read-only: work location (state or country) | Illinois; Berlin |
| Manager, HR operations owner, buddy if named | Yes | HRIS, read-only: manager; ask the user for the others | Manager by role; buddy not yet named |
| Cohort size and start dates | No | HRIS, read-only: count of hires by start date | 9 starting the same week |
| Systems with new hire data and their AI features | Yes | Ask the user | HRIS, IT ticketing, learning platform, chat tool |
| Proposed AI assistant and its source documents | If an assistant is in scope | Ask the user | Handbook v4.2, IT guide v1.9 |
| Check-in survey comments | For step 8 only | Survey platform export, read-only: cohort, question, comment text with no names or IDs | 30-day survey, 9 responses |

If a required input is missing, ask for it once, in one short question at the top of your reply, then proceed with the gap labeled in the output, for example "Buddy not named: intro drafted with a placeholder."

## Tools and connectors

- **HRIS, read-only through an MCP connector or export.** Read only job, level, department, manager, work location, start date and work arrangement. Never read Social Security numbers, immigration documents, health data or accommodation records.
- **IT ticketing, read-only.** Read status, owner and due date of the new hire's equipment and account tickets, to show readiness gaps. Never open or close a ticket.
- **Learning platform, read-only.** Read the assigned onboarding module list. Completion data only in aggregate for the program review.
- **Survey platform, read-only.** Read de-identified comments for a cohort. Do not report a theme where the cohort is small enough that a comment identifies its author; People Analytics sets the minimum.
- **Repo MCP tool.** `ask_governance_policy` returns cited sections of this repo's `03-governance/` files, or nothing. Use it for the AI orientation content and as the reference pattern for a company policy assistant. Read `policy_qa/ENABLEMENT.md` first: an editable wiki as a corpus opens a prompt injection path.
- Never call a write, send, create-account or update tool, even if the connector offers one.
- Log each tool call (tool, purpose, fields read) in the Audit trail.
- If a tool returns data on people outside the request, stop, do not use it, and ask.
- If an agent coordinates preboarding across HRIS, IT and learning systems, follow Pattern 4: it reads status and drafts the next action, and the named owner acts in their own system. It does not continue past an unconfirmed checkpoint.

## By maturity stage

Stages follow the repo's maturity scale in [the roadmap template](../../06-roadmap/transformation-roadmap-template.md). Decision rights in this skill are the same at every stage.

| Stage | How to run it | Before moving up |
|---|---|---|
| Start (Levels 0 to 1) | Paste role, level, start date, location and handbook excerpts, with no names. Agent drafts the checklist and 30/60/90; HR operations checks every date and form. | Counsel confirms state and country forms. |
| Pilot (Level 2) | Read-only HRIS export per cohort: job, level, manager, location, start date, work arrangement. HR operations lead owns it and tracks day-one readiness. | Any assistant has a pass bar on `hr-qa-agent-evals.yaml`. |
| Scale (Level 3) | Logged reads of HRIS, IT ticket status and module lists, plus `ask_governance_policy`. Tracks assistant answer accuracy. AI notice reaches new hires before launch. | Policy owner confirms the monthly accuracy sample; Legal approves launch. |
| Embed (Levels 4 to 5) | A new hire record triggers the preboarding draft and manager prep guide. Managers still own plans and buddies; HR operations reviews I-9 documents. | Rerun the test cases in `evals/` when the skill or model changes. |

## Steps

1. **Map the four parts of onboarding.** Plan for compliance (forms and rules), clarification (role and expectations), culture (how work gets done here) and connection (relationships). New hires report that onboarding often leans too heavily on admin tasks and can feel isolating, so check the plan has real time with people, not only modules. Sign-off: HRBP.

2. **Draft the preboarding checklist.** Cover equipment, accounts, a welcome note and the first-day schedule, each with an owner and due date. List the federal paperwork owners: Form I-9 Section 1 by the new hire no later than the first day of employment, Section 2 by the employer within three business days of hire, and Form W-4 at the start of work. The HR operations owner reviews identity and work authorization documents; AI never does. Add state and country forms only after counsel confirms them. Sign-off: HR operations owner.

3. **Plan the first week with the manager at the center.** Use prompt 3 to draft a manager prep guide five days before the start date. Research ties active manager involvement to new hires feeling their onboarding succeeded, so the plan names the manager's first-day 1:1, first-week check-in questions and the people to meet. Pace the content: new hires often feel flooded when too much arrives at once.

   Add a short AI orientation: which AI tools are approved, the main rules in `ai-use-policy.md`, what never goes into a general AI tool, and how to check an AI answer before using it. Building this into onboarding sets the same baseline for every new hire from day one. Keep a record of who completed it. As an optional exercise, the new hire can write a short "how I work" note: AI turns their answers to a few questions into a first draft, and the new hire edits it, decides what to share, or skips it. That note is never used to assess them. Sign-off: the manager edits and owns the plan.

4. **Set up a buddy.** Use prompt 5 to draft the intro. Pick a buddy with enough tenure to know the unwritten rules, protect their time, and give them a short guide with a meeting rhythm for the first 90 days. More frequent buddy meetings have been linked to new hires saying the buddy helped them become productive. AI can draft the meeting series and reminders across time zones; the buddy confirms them. AI may suggest work-related criteria, such as function, location, time zone or shared tools, never a person. Sign-off: the manager chooses the buddy.

5. **Draft a skills-linked 30/60/90 plan.** Use prompt 2. Make each stage specific to the role: learning goals and introductions by 30 days, owned deliverables by 60, independent outcomes by 90. Link each learning goal to a skill in the role's skills profile, so development starts from the same skills language used later in growth conversations. Reaching full performance takes much longer than 90 days, so frame the plan as a start, not a probation scorecard. Sign-off: the manager and new hire agree it in the first week.

6. **Scope any AI onboarding assistant.** Allow it only to answer from approved, versioned policy documents, cite the source and version, and say "I don't know" and route to a person when nothing applies (Pattern 1 and the no-fabrication rule in `policy_qa/ENABLEMENT.md`). Generative models can state false content with confidence, so test with `09-evals/hr-qa-agent-evals.yaml` before launch and set a pass bar. Tell new hires they are talking to an AI and how to reach a person. Route pay, leave, accommodation, immigration and complaint questions to a named HR owner, never to the assistant's answer.

   For risk triage, the European Commission's draft guidelines on classifying high-risk AI systems, which are consultation drafts and not binding, give an onboarding Q and A bot as an example outside the employment high-risk uses. The same drafts treat monitoring or evaluating performance, including during probation, as a high-risk category of its own. If an assistant starts to track, score or report on a new hire's activity, stop and redo the risk assessment with counsel. Sign-off: HR operations owner of the policy corpus, with Legal for launch.

7. **Keep the human channel open.** Some new hires use AI to answer questions instead of asking a manager or colleague. Build in a standing question slot in each manager 1:1 and a buddy check-in. The assistant does not replace either. Sign-off: manager.

8. **Synthesize check-ins at the group level.** Use prompt 4 to summarize 30, 60 and 90 day comments across a cohort. Report themes and support needs, not a risk label for any person. Do not infer that anyone plans to leave, and do not score sentiment or emotion per person. Sign-off: HRBP reviews and routes manager-level items to the manager.

9. **Close the loop on the program.** Draft a short program review: what new hires found useful, where they waited on access or answers, what the assistant could not answer, and the metrics below. Sign-off: HR operations owns program changes.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Compute paperwork and checklist due dates from the start date | HR operations owner uses them | Does alone |
| Draft the preboarding and first-week checklist | HR operations owner | Drafts for sign-off |
| Review identity or work authorization documents for Form I-9 | HR operations owner | Refuses and routes |
| Draft the manager prep guide and first-week 1:1 questions | Hiring manager | Drafts for sign-off |
| Draft the 30/60/90 plan | Manager, agreed with the new hire | Drafts for sign-off |
| Choose a named buddy | Manager | Refuses and routes |
| Draft a "how I work" note from the new hire's own answers | New hire | Drafts for sign-off |
| Answer a policy question from approved documents, with citation | Policy corpus owner set the scope at launch | Does alone |
| Answer pay, leave, accommodation, immigration or complaint questions | Named HR case owner | Refuses and routes |
| Summarize cohort check-in comments into themes | HRBP | Drafts for sign-off |
| Judge how a named new hire is doing or whether they will stay | Manager | Refuses and routes |
| Create accounts, open tickets or send messages to a new hire | IT, HR operations, manager | Refuses and routes |

### Refuse and route

- "Which new hires in this cohort are struggling or likely to quit?": refuse; route to the HRBP with cohort-level themes and to each manager's 1:1.
- Check a new hire's passport or tell them which I-9 documents to bring: refuse; route to the HR operations owner. AI may remind people of deadlines only.
- Answer a leave, pay, benefits or accommodation question from memory: refuse; route to the named HR owner, or answer only from an approved, cited document.
- Pick the buddy, or tailor content by age, gender or another protected trait: refuse; route to the manager with work-related criteria.
- Track a new hire's logins, keystrokes or activity and report it to the manager: refuse; route to Legal and redo the risk assessment.
- Score sentiment or emotion in check-in comments per person: refuse; route to the HRBP for group-level themes.
- Send the welcome email, create accounts or enroll the new hire in courses: refuse; hand the draft to the owner.
- "Which state forms apply in Illinois?": do not state it; route to counsel and the Key dates table.
- Use real employee data in examples: refuse; use synthetic data.

## Guardrails

- **Fairness.** Buddy suggestions, plan templates and access to tools and training do not vary by protected characteristics. Check day-one readiness across work arrangements and locations, so remote hires are not left waiting. Onboarding selects no one; if a tool starts to score new hires, it is a different use case and goes to `fairness-audit-prep`.
- **Explainability and notice.** Tell new hires which steps use AI, that the assistant is an AI, what it cannot answer and how to reach a person, per principle 2. Every policy answer shows source and version so the new hire can check it.
- **Privacy and minimization.** The assistant gets only the documents and new hire fields it needs. Do not load immigration documents, Social Security numbers, health information or accommodation requests into an AI tool, per principle 4. Check-in analysis stays at cohort level.
- **Accuracy.** When no source applies, the assistant says so and routes. A person verifies any AI-written policy statement before it is sent, per principle 5.
- **Legal review triggers.** Any state or country onboarding form or notice; any assistant that answers benefits, leave or pay questions; any monitoring of new hire activity; any new hire in the EU.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| EU AI Act, transparency | New hires chat with an AI onboarding assistant | Puts "you are talking to an AI, here is how to reach a person" in the notice text and routes scope to counsel |
| EU AI Act, AI literacy (Article 4) | New hires in Germany or other EU countries will use AI systems at work | Builds AI orientation into week one and keeps an internal completion record; counsel checks the current Article 4 text |
| EU AI Act, high-risk HR systems | An onboarding tool begins to monitor or evaluate new hire performance, including in probation | Stops and routes to a new risk assessment and counsel |
| EU AI Act, emotion recognition at work (Article 5(1)(f)) | A proposed tool would infer new hires' emotions from check-ins, chat or video | Refuses and routes to Legal |

Counsel confirms scope and current status before you rely on any row. In your reply, name each rule as: see the Key dates row "exact row name" in `03-governance/README.md`. Stop there: do not write the row's dates, status or regulation numbers, even ones you read in the table or in Sources, because the table is the one place they are kept current.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| 90-day new hire retention | New hires who started in a quarter and are still employed 90 days after their start date, divided by all new hires who started that quarter | Outcome measure of early onboarding |
| Day-one readiness by work arrangement | New hires in a month with laptop, core accounts and I-9 Section 1 complete by the end of day one, divided by new hires starting that month; reported separately for on site, hybrid and remote | Shows whether every group starts equally equipped |
| Assistant answer accuracy | Sampled assistant answers in a month that cite a current approved source and that the policy owner confirms correct, divided by answers sampled that month; questions de-identified before review | Trust check on the assistant |

## Output format

```markdown
## New hire context
[role, level, start date, arrangement, location, owners, gaps labeled]

## Preboarding checklist
| Item | Owner | Due | Status |

## Compliance paperwork
| Form | Who completes | Deadline | Human reviewer |

## First week
[day-by-day plan, manager 1:1s, people to meet, buddy meetings, AI orientation]

## 30/60/90 plan
| Stage | Learning goals | Skill it builds | Deliverables | Check-in |

## AI onboarding assistant scope (if any)
- Source documents and versions:
- Topics it answers:
- Topics it routes, and to whom:
- Eval set and pass bar:
- Notice text to new hires:

## Decision rights applied
| Item | Agent role | Routed to |

## Metrics this plan tracks
[from the Metrics table]

## Audit trail
- Inputs used: [list; gaps labeled]
- Tools called and fields read: [tool, purpose, fields]
- Items needing sign-off: [item -> owner]
- Open legal questions: [Key dates row -> question for counsel]
```

## Worked example

A Harbor & Pine HR operations lead asks for a plan for a December cohort split across Illinois and Berlin, with a proposed onboarding chatbot. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They were run on 18 November 2026 with `claude-sonnet-5-5`, one fresh session per case, and graded in a separate pass; see [the results](../../09-evals/skill-eval-results-2026-11-18.md) for the method and its limits.

- `new-hire-plan-with-assistant`: core request, a full first-90-days plan with an assistant scope and sign-offs.
- `berlin-hire-missing-start-date`: a Germany-based hire with no start date and a policy corpus kept in an editable wiki.
- `flag-struggling-new-hires`: a request to label named new hires as struggling and check their documents, which the skill refuses and routes.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. Completing Section 1, Employee Information and Attestation, US Citizenship and Immigration Services. https://www.uscis.gov/i-9-central/completing-form-i-9/completing-section-1-employee-information-and-attestation. Supports: Section 1 no later than the first day of employment; Section 2 within three business days of hire; preparer and translator rules.
2. Hiring employees, Internal Revenue Service. https://www.irs.gov/businesses/small-businesses-self-employed/hiring-employees. Supports: verify identity and work authorization with Form I-9; collect name and SSN for Form W-2; ask new employees for a signed Form W-4 when they start.
3. 8 Practical Tips for Leaders for a Better Onboarding Process, Emily Wetherell and Bailey Nelson, Gallup, 12 August 2021. https://www.gallup.com/workplace/353096/practices-better-employee-onboarding.aspx. Supports: active manager involvement linked to successful onboarding; long time to full performance; peer connection and mentors.
4. Work Buddies Can Help New Employees Transition into Job, Organizational Culture, Kathy Gurchiek, SHRM, 18 August 2022. https://www.shrm.org/mena/topics-tools/news/organizational-employee-development/work-buddies-can-help-new-employees-transition-job-organizational-culture. Supports: buddy tenure and selection; protecting buddy time; structure and reminders; link between meeting frequency and perceived productivity.
5. Don't Underestimate the Importance of Good Onboarding, Arlene S. Hirsch, SHRM, 10 August 2017. https://www.shrm.org/mena/topics-tools/news/talent-acquisition/dont-underestimate-importance-good-onboarding. Supports: compliance, clarification, culture, and connection as the parts of onboarding; onboarding running past orientation; manager training and check-ins.
6. First Day Fog: Onboarding Benchmarking Report for 2025, BambooHR (vendor survey), March 2026. https://www.bamboohr.com/resources/guides/onboarding-benchmarking. Supports: too much admin focus; isolation; information overload; new hires using AI instead of asking a manager or colleague.
7. Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1), NIST, July 2024. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf. Supports: confabulation risk; disclosing AI use to users; feedback and recourse for users; verifying sources in outputs.
8. AI in the Workplace Playbook, SHRM, 2025. Read from a copy of the publication; no web address checked. Supports: building AI literacy training into onboarding for every new hire.
9. The HR AI Automation Playbook, Zapier, August 2025. Read from a copy of the publication; no web address checked. Supports: vendor-published examples of an AI-drafted "how I work" note that the new hire edits, onboarding scheduling across time zones, and buddy pairing on shared work criteria.
10. Draft guidelines on the classification of high-risk AI systems, European Commission, 2026 consultation drafts (non-binding). Read from a copy of the publication; no web address checked. Supports: onboarding Q and A bots given as an example outside the employment high-risk uses, and performance monitoring, including probation, treated as its own high-risk category. Draft guidance only.
