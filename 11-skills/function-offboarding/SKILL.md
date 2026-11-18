---
name: function-offboarding
description: Plans a voluntary or involuntary exit, or a group reduction, so legal flags, final pay, benefits notices, access removal, knowledge transfer and communication happen in the right order with a named owner each. Produces an exit intake record, legal flags for counsel, a dated timeline, an access removal plan, manager talking points, a knowledge transfer template, aggregate exit interview themes and an audit trail. Use whenever someone says build an offboarding checklist, someone resigned, plan a termination meeting, we are planning a layoff, pick who goes in the reduction, summarize our exit interviews, set up knowledge transfer, or draft the exit email to the team, and whenever an automated system touches discipline or termination.
---

# Offboarding

For an HRBP, HR operations lead or manager. It produces the exit plan, the drafts inside it and aggregate exit interview themes, so nothing is missed and the person is treated with respect. It stops before any decision about who leaves, any severance terms, any access change in a system, and any conversation with the departing person. Those stay with the manager, HR, IT and Security, and Legal.

## Files this skill needs

- `02-prompt-library/people-analytics.md` (prompt 3, exit interview theme synthesis across many departures)
- `03-governance/ai-use-policy.md` (principle 1 lists terminations as human decisions; principle 2 notice; principle 4 data; the prohibited use on automated termination)
- `03-governance/quick-reference-checklist.md` and `03-governance/risk-assessment-template.md` (before any offboarding or exit survey tool with AI features)
- `07-agentic-patterns/agent-design.md` (confirmation gates before any action that changes employment status)
- `11-skills/function-workforce-planning-org-design/SKILL.md` (redeployment and reskilling review before roles are removed)
- `11-skills/fairness-audit-prep/SKILL.md` (adverse impact method for a reduction)
- `03-governance/README.md` (Key dates for HR table)

## Inputs

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| Exit type | Yes | Ask the user | Resignation, retirement, contract end, involuntary for cause, not for cause, or group reduction |
| Work location (state or country) | Yes | HRIS, read-only: work location | Colorado |
| Last day and notice date | Yes | Ask the user | Notice 2 December, last day 16 December |
| Named owners: manager, HRBP, payroll, benefits administrator, IT and Security, Legal | Yes | HRIS, read-only: manager; ask the user for the rest | Owners by role |
| Systems that hold the person's data and access | Yes | Ask the user | HRIS, payroll, benefits administrator, identity tool, device management, exit survey |
| Confirmation that a named leader made the decision with HR and Legal | For involuntary exits and reductions | Ask the user | Decision record dated 25 November |
| Company size, and for a reduction the count at each site and over what period | For reductions | HRIS, read-only: headcount by site; ask the user for the affected count | 1,400 staff; 38 at one site |
| Whether a severance agreement or release is planned | Yes | Ask the user | Release for a group program |
| Ages of affected people | Only if Legal asks, for waiver disclosures | HRIS, read-only, released to Legal only | Not read by default |
| Exit interview comments | For step 8 only | Survey platform export, read-only: comment text, quarter, department, no names or IDs | 64 comments, Q3 |

If a required input is missing, ask once, then proceed with the gap labeled, for example "Location not confirmed: final pay rule not mapped."

## Tools and connectors

- **HRIS, read-only through an MCP connector or export.** Read job, department, manager, work location, hire date and exit type. Never read performance notes, health, leave or complaint records unless Legal directs it.
- **Payroll export, read-only.** Read pay frequency and work state only, so payroll can confirm the final pay rule. Not pay amounts.
- **Benefits administrator, read-only.** Read whether the person is enrolled in group health coverage, to trigger the COBRA steps. Not plan or claims detail.
- **Identity and device tools, read-only.** Read the list of accounts, groups, badges and assigned devices, to build the access plan.
- **Survey platform, read-only.** De-identified exit comments only.
- Never call a disable, revoke, terminate, update or send tool, even if the connector offers one. IT and Security act in their own systems.
- Log each tool call (tool, purpose, fields read) in the Audit trail.
- If a tool returns data on people outside the request, stop, do not use it, and ask.
- If an agent coordinates the exit as one workflow, it starts from one intake record and stops at the confirmation gates in `agent-design.md`. Any automated workflow that opens access removal tickets gets only the access that task needs, a named owner who can halt it, and a log of what it did and who approved each step.

## Steps

1. **Confirm the decision is made and owned.** For an involuntary exit or a reduction, confirm a named leader made the decision with HR and Legal, and that no AI tool selected the person or ranked people for selection. If anyone proposes using a model to pick who leaves, stop and route to Legal under the prohibited uses in `ai-use-policy.md`. If roles are being removed because AI or automation changed the work, confirm that redeployment and reskilling were reviewed first with `function-workforce-planning-org-design`. AI drafts nothing until this is confirmed. Sign-off: accountable leader and HRBP.

2. **Check group-layoff triggers and adverse impact early.** For a reduction, flag the federal WARN Act for Legal: it generally covers employers with 100 or more employees and requires 60 calendar days' notice before a covered plant closing or mass layoff, to affected workers, the state dislocated worker unit and local government. State laws can add duties. If a release is planned for a group exit program, flag the longer review period and the age and job title disclosures that waivers of age claims require. Before selections are final, draft a request for People Analytics to compare retention rates by group in the reduction pool, under counsel's direction, using the method in `fairness-audit-prep`. The four-fifths ratio is a screening flag under [29 CFR 1607.4(D)](https://www.govinfo.gov/content/pkg/CFR-2024-title29-vol4/pdf/CFR-2024-title29-vol4-sec1607-4.pdf), not a safe harbor or a verdict; small groups need a statistical test that People Analytics or counsel interprets. Sign-off: employment counsel.

3. **Build the timeline in the right order.** Start every exit from one intake record with the exit type, dates and owners, so each team works from the same facts at the same time. Steps that slip can leave access open, miss a notice, or damage the relationship. Draft a dated checklist with an owner per line: decision record, Legal review, access plan, the conversation, final pay, benefits notices, equipment return, knowledge transfer and announcement. Federal law does not require a final paycheck immediately, but some states do, so payroll confirms the state rule with the state labor department. Sign-off: HRBP.

4. **Plan access removal with IT and Security.** List every system, badge, device and shared credential, with who removes each and when. For an involuntary exit, set the timing with Security before the meeting. Include retrieving personal belongings and company equipment, and a reminder of confidentiality and intellectual property agreements. Sign-off: IT and Security own execution; AI never removes access.

5. **Prepare the conversation, not the verdict.** For an involuntary exit, draft manager talking points: the decision in the first sentences, what happens next, final pay and benefits timing, and who to contact. Keep it short and respectful, in private, and avoid anything that would embarrass the person. Do not draft reasons beyond what HR and Legal approved. If an automated system informed the decision, the person's explanation and any review route follow the Regulation map, and counsel approves the wording. Sign-off: the manager and HRBP hold the meeting; AI does not attend or speak for them.

6. **Line up benefits and release paperwork.** Draft the benefits notice checklist. Under COBRA, which generally covers group health plans of employers with 20 or more employees, the employer notifies the plan within 30 days of a termination, the plan sends an election notice within 14 days, and the person gets at least 60 days to elect. If a release covers age claims, a valid waiver must name the ADEA in plain language, advise the person in writing to consult a lawyer, allow at least 21 days to consider (45 for a group program), and allow 7 days to revoke. A release cannot stop someone from filing a charge with the EEOC. Sign-off: Legal drafts and approves all release terms.

7. **Plan knowledge transfer.** Draft a handover template: open work, recurring tasks and how they are done, key contacts and vendors, where files live, and what only this person knows. Prefer shadowing or a recorded walkthrough for know-how that is hard to write down. Map handed-over tasks to the skills the team will now need, so gaps feed workforce planning. For a voluntary exit, start on notice; for an involuntary exit, the manager decides what is safe and fair to ask. Sign-off: the manager assigns owners.

8. **Run the exit interview and analyze in aggregate.** HR offers an exit interview and tells the person how the data is used. Use prompt 3 only across many departures, never to analyze one person. Do not name people, and treat themes with few mentions as weak. Route any concentration around one manager to the HRBP for follow-up, not to a conclusion. Do not infer health, family or other sensitive reasons, and do not score tone or emotion in any recording or transcript. Sign-off: HRBP or People Analytics.

9. **Communicate and stay connected.** Draft the team announcement with only what the departing person and HR agreed to share. For a voluntary exit, draft an alumni invitation and a rehire eligibility note for HR to decide. Log which AI drafts were used so the process can be reconstructed. Sign-off: manager and HRBP.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Decide who leaves, or rank people for a reduction | Accountable leader, with HR and Legal | Refuses and routes |
| Read the exit fields listed under Tools and connectors and look up the Key dates rows for each work location | Not a decision | Does alone |
| Build the dated timeline of notice, final pay, COBRA and access deadlines from those inputs | Not a decision; the HRBP confirms dates | Does alone |
| Draft the dated offboarding checklist from the intake record | HRBP | Drafts for sign-off |
| Flag WARN, COBRA, release and final pay items for review | Employment counsel | Drafts for sign-off |
| Draft the request for an adverse impact check of a reduction pool | Counsel and People Analytics | Drafts for sign-off |
| Draft manager talking points for an exit conversation | Manager and HRBP | Drafts for sign-off |
| Draft the access removal plan by system | IT and Security | Drafts for sign-off |
| Remove access, close accounts or change a record in the HRIS | IT, Security, HR operations | Refuses and routes |
| Draft a knowledge transfer template | Manager | Drafts for sign-off |
| Summarize exit interview themes across many departures | HRBP or People Analytics | Drafts for sign-off |
| Analyze one person's exit interview or infer why they left | HRBP, in conversation | Refuses and routes |
| Set severance amounts or release terms | Legal and HR leadership | Refuses and routes |
| Draft the team announcement, alumni invitation and rehire eligibility note | Manager and HRBP; HR decides rehire eligibility | Drafts for sign-off |

### Refuse and route

- "Use performance and tenure data to pick the 40 people for the layoff": refuse; route to HR leadership and counsel with the selection criteria and the adverse impact request.
- "Which of these people will sue?" or a litigation risk score for a named person: refuse; route to employment counsel.
- "Why did Jordan really leave?" from one exit interview: refuse; route to the HRBP for a conversation, and offer aggregate themes.
- Score tone, stress or emotion in an exit interview recording or transcript: refuse; route to Legal.
- Disable accounts, send the termination email or update the HRIS: refuse; hand the plan to IT, Security and HR operations.
- Set severance or write final release language: refuse; route to Legal.
- Decide the final pay deadline or notice rules for a location: refuse to state; route to payroll, the state labor department and counsel.
- Use age, leave status, a recent complaint or another protected trait or activity as a selection criterion: refuse; route to counsel.
- Use real employee data in examples: refuse; use synthetic data.

## Guardrails

- **Fairness and adverse impact.** No model selects, scores or ranks people for termination or a reduction. People Analytics checks retention rates by group in a reduction pool before decisions are final, under counsel's direction. The European Commission's draft guidelines on classifying high-risk AI systems, which are consultation drafts and not binding, read termination broadly, including non-renewal of a contract. They also say a decision can count as AI-driven when a person signs off but relies heavily on the tool's output, so a human sign-off does not by itself make such a tool low risk. A plain reminder that a contract is ending is given as an example that can fall outside.
- **Explainability and notice.** The departing person hears the decision, next steps, pay and benefits timing and a contact for questions after they leave. Exit interview notice says the data is analyzed in aggregate and, if AI helps summarize it, says so, per principle 2.
- **Privacy and minimization.** Share the minimum with each owner. Keep the reason for an involuntary exit, health or leave details and severance terms out of AI tools not approved for them, per principle 4. Exit analysis never names individuals.
- **Dignity.** Deliver involuntary news privately and respectfully, with a clear contact afterward.
- **Legal review triggers.** Any involuntary exit; any group reduction; any release or severance agreement; any person on leave, with a pending complaint or who recently raised a concern; any state with a final pay deadline; any non-US worker; any automated system that informed discipline or termination.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| California SB 951 (Ch. 860, Stats. 2026) | A reduction at a California site may need a Cal/WARN notice and technology changed the work | Flags technology-displacement content for the notice to counsel |
| California SB 947 (Ch. 859, Stats. 2026) | An automated decision system informed discipline or termination of a California worker | Flags corroboration and post-use notice questions to counsel |
| Colorado SB 26-189 (ADMT Act) | Automated technology was used in a termination decision for a Colorado worker | Drafts notice, explanation and human review steps for counsel; the row says status is unverified |
| Illinois HB 3773 (Public Act 103-0804) | AI was used in a discharge decision for an Illinois worker | Flags the notice duty and the discrimination risk to counsel |
| EU AI Act, high-risk HR systems | A tool informs termination or contract non-renewal for a worker in Germany or another EU country | Routes to `eu-ai-act-hr-classifier` and counsel |

Counsel confirms scope and current status before you rely on any row.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| Offboarding on time | Exits in a month where every checklist line (access removed at the time Security set, final pay on the date payroll confirmed, benefits notice to the plan, equipment returned) closed by its due date, divided by all exits that month | Outcome: missed steps are where security, legal and relationship damage starts |
| Access removed by the set time | Accounts and badges in scope that were disabled by the time Security set, divided by all accounts and badges in scope, per month | Security outcome |
| Reduction pool retention rate ratio by group | Per reduction: (people in a group retained / people in that group in the pool), divided by the same rate for the highest-retention group; computed by People Analytics under counsel's direction before decisions are final; below 0.8 is a flag, not a finding | Fairness check before anyone is told |

## Output format

```markdown
## Exit context
[exit type, location, company size, owners, Legal involved Y/N, gaps labeled]

## Legal flags for counsel
| Item | Why it may apply | Owner | Status |

## Offboarding timeline
| Date | Step | Owner | Done |

## Access removal plan
| System or asset | Removal timing | Owner |

## Benefits and pay
[final pay rule to confirm with the state, COBRA steps and owner, release review]

## Knowledge transfer
| Area | What to hand over | Method | New owner |

## Communication drafts
[manager talking points, team announcement, alumni note, each marked draft for review]

## Exit interview themes (aggregate only)
[themes, sample size, confidence, routing]

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

A Harbor & Pine HRBP plans a 38-person reduction at a California site after a support workflow was automated, and is asked to "pick the list." See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They are written, not yet run against a model.

- `voluntary-resignation-checklist`: core request, a resignation plan from intake to alumni note.
- `colorado-exit-with-ai-flag-missing-date`: an involuntary exit in Colorado where a productivity tool fed the decision and the last day is missing.
- `select-layoff-list-by-model`: a request to rank named employees for a layoff and send termination emails, which the skill refuses and routes.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. Last Paycheck, US Department of Labor. https://www.dol.gov/general/topic/wages/lastpaycheck. Supports: no federal requirement to pay final wages immediately; some states require it; state labor department contacts.
2. An Employer's Guide to Group Health Continuation Coverage Under COBRA, US Department of Labor, Employee Benefits Security Administration. https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/an-employers-guide-to-group-health-continuation-coverage-under-cobra. Supports: 20-employee coverage rule; termination as a qualifying event; 30-day employer notice to the plan; 14-day election notice; 60-day election period.
3. Employment Law Guide: Notices for Plant Closings and Mass Layoffs, US Department of Labor. https://webapps.dol.gov/elaws/elg/layoffs.htm. Supports: WARN coverage of employers with 100 or more employees; 60 calendar days' notice; who must be notified; WARN does not preempt state law.
4. Q and A: Understanding Waivers of Discrimination Claims in Employee Severance Agreements, US Equal Employment Opportunity Commission, 15 July 2009. https://www.eeoc.gov/laws/guidance/qa-understanding-waivers-discrimination-claims-employee-severance-agreements. Supports: OWBPA waiver requirements, 21 and 45 day review, 7 day revocation, group disclosures, right to file an EEOC charge.
5. Human Resources' Role in Preventing Insider Threats, Cybersecurity and Infrastructure Security Agency, July 2024. https://www.cisa.gov/sites/default/files/2024-07/hrs-role-in-preventing-insider-threats-fact-sheet_07-29-2024_508.pdf. Supports: respectful termination notice; plan to retrieve belongings and end physical and digital access; exit interview; reviewing IP and nondisclosure agreements; procedure for informing staff.
6. Capture What Employees Know Before They Leave the Company, Jennifer Thomas, SHRM HR Magazine, 30 November 2023. https://www.shrm.org/topics-tools/news/hr-magazine/capture-what-employees-know-before-they-leave-the-company. Supports: knowledge capture as ongoing work; documenting explicit and tacit knowledge; shadowing and cross-training.
7. Making Exit Interviews Count, Everett Spain and Boris Groysberg, Harvard Business Review, April 2016. https://hbr.org/2016/04/making-exit-interviews-count. Supports: exit interviews can show what does and does not work; many programs fail on poor data quality and lack of agreed practice.
8. Why Companies Should Stay Connected with Ex-Employees, Geri Tucker, SHRM HR Magazine, 19 March 2018. https://www.shrm.org/mena/topics-tools/news/hr-magazine/companies-stay-connected-ex-employees. Supports: alumni programs, boomerang hiring, introducing alumni programs before exit.
9. The HR AI Automation Playbook, Zapier, August 2025. Read from a copy of the publication; no web address checked. Supports: vendor-published pattern of one intake record that starts every offboarding step, and the security, compliance, and relationship risks when steps slip.
10. Workday's Vision for AI Governance, Workday, 2026. Read from a copy of the publication; no web address checked. Supports: vendor-published safeguards for automated workflows: least-privilege access, a named human owner who can halt, and logs of actions and approvals.
11. Draft guidelines on the classification of high-risk AI systems, European Commission, 2026 consultation drafts (non-binding). Read from a copy of the publication; no web address checked. Supports: termination read to include non-renewal, heavy reliance on AI output counting even with a human sign-off, and a plain contract-end reminder as a possible exception. Draft guidance only.
