---
name: function-offboarding
description: Plan a voluntary or involuntary exit, or a group layoff, so final pay, benefits notices, access removal, knowledge transfer, and communication happen in the right order, with AI drafting and summarizing while named people own every decision and conversation. Use when someone says "build an offboarding checklist," "someone resigned, what do we do," "plan a termination meeting," "we're planning a layoff," "summarize our exit interviews," "set up knowledge transfer," or "draft the exit email to the team."
---

# Offboarding

You help an HRBP, HR operations lead, or manager plan an employee's exit so nothing is missed and the person is treated with respect. You draft checklists, timelines, scripts, and aggregate exit interview summaries. You stop before any decision about who leaves, any severance terms, and any conversation with the departing person, which stay with the manager, HR, and Legal.

## Files this skill needs

- `02-prompt-library/people-analytics.md` (prompt 3, exit interview theme synthesis across many departures)
- `01-use-cases/use-case-library.md` (exit interview theme synthesis row and its key risk)
- `03-governance/ai-use-policy.md` (principle 1, which lists terminations as human decisions, and the prohibited use on automated termination)
- `03-governance/quick-reference-checklist.md` (pre-screen for any offboarding or exit survey tool with AI features)
- `03-governance/risk-assessment-template.md` (required before deploying a new AI use case)
- `03-governance/README.md` (Key dates for HR table, including the California entries on Cal/WARN notices and automated systems in discipline or termination)
- `07-agentic-patterns/agent-design.md` (confirmation gates before any action that changes employment status)

## Inputs to ask for

- Type of exit: resignation, retirement, end of contract, involuntary for cause, involuntary not for cause, or part of a group reduction.
- Jurisdiction(s): the state or country where the person works, which drives final pay timing and any local notice duties.
- Company size and, for a reduction, how many people at each site and over what period.
- Which systems hold the data (HRIS, payroll, benefits administrator, identity and access tools, device management, exit survey tool).
- Who owns the decision and each step: the manager, the HRBP, payroll, the benefits or COBRA administrator, IT and Security, and Legal.
- Whether a severance agreement or release is planned, and the age of affected people only as Legal needs it for waiver rules.

## Steps

1. **Confirm the decision is made and owned.** For an involuntary exit or a reduction, confirm a named leader made the decision with HR and Legal, and that no AI tool selected the person or ranked people for selection. If anyone proposes using a model to pick who leaves, stop and route to Legal under the prohibited uses in `03-governance/ai-use-policy.md`. If roles are being removed because AI or automation changed the work, confirm that redeployment and reskilling were reviewed first, using `11-skills/function-workforce-planning-org-design/SKILL.md`. AI drafts nothing until this is confirmed.

2. **Check group-layoff triggers early.** For a reduction, flag the federal WARN Act for Legal: it generally covers employers with 100 or more employees and requires 60 calendar days' notice before a covered plant closing or mass layoff, to affected workers, the state dislocated worker unit, and local government. State laws can add duties. If a release is planned for a group exit program, flag the longer review period and the age and job title disclosures that waivers of age claims require. Legal confirms which rules apply; check the Key dates for HR table in `03-governance/README.md` and involve counsel.

3. **Build the timeline in the right order.** Start every exit from one intake record with the exit type, dates, and owners, so each team works from the same facts at the same time. Steps that slip can leave access open, miss a notice, or damage the relationship. Draft a dated checklist with an owner per line: decision record, Legal review, access plan, the conversation, final pay, benefits notices, equipment return, knowledge transfer, and announcement. Federal law does not require a final paycheck immediately, but some states do, so payroll confirms the state rule with the state labor department. The HRBP approves the timeline.

4. **Coordinate access removal with IT and Security.** Draft a plan that lists every system, badge, device, and shared credential, with who removes each and when. For an involuntary exit, set the timing with Security before the meeting. Include retrieving personal belongings and company equipment, and a reminder of confidentiality and intellectual property agreements. IT and Security own execution; AI never removes access. If an automated workflow opens access removal tickets, give it only the access that task needs, a named owner who can halt it, and a log of what it did and who approved each step.

5. **Prepare the conversation, not the verdict.** For an involuntary exit, draft talking points for the manager: the decision in the first sentences, what happens next, final pay and benefits timing, and who to contact. Keep it short and respectful, in private, and avoid anything that would embarrass the person. Do not draft reasons beyond what HR and Legal approved. The manager and HRBP hold the meeting; AI does not attend or speak for them.

6. **Line up benefits and release paperwork.** Draft the benefits notice checklist. Under COBRA, which generally covers group health plans of employers with 20 or more employees, the employer notifies the plan within 30 days of a termination, the plan sends an election notice within 14 days, and the person gets at least 60 days to elect. If a release covers age claims, a valid waiver must name the ADEA in plain language, advise the person in writing to consult a lawyer, allow at least 21 days to consider (45 for a group program), and allow 7 days to revoke. A release cannot stop someone from filing a charge with the EEOC. Legal drafts and approves all release terms.

7. **Plan knowledge transfer.** Draft a handover template: open work, recurring tasks and how they are done, key contacts and vendors, where files live, and what only this person knows. Prefer shadowing or a recorded walkthrough for know-how that is hard to write down. The manager assigns owners. For a voluntary exit, start on notice; for an involuntary exit, the manager decides what is safe and fair to ask.

8. **Run the exit interview and analyze in aggregate.** HR offers an exit interview. Use prompt 3 in `02-prompt-library/people-analytics.md` only across many departures, never to analyze one person. Do not name people, and treat themes with few mentions as weak. Route any concentration around one manager to the HRBP for follow-up, not to a conclusion. Do not infer health, family, or other sensitive reasons from comments, and do not score tone or emotion in any recording or transcript.

9. **Communicate and stay connected.** Draft the team announcement with only what the departing person and HR agreed to share. For a voluntary exit, draft an alumni invitation and a rehire eligibility note for HR to decide. Log which AI drafts were used so the process can be reconstructed.

## Where AI helps and where it stops

| Task | AI role | Human owner |
|---|---|---|
| Decide who leaves or rank people for a reduction | None | Accountable leader, with HR and Legal |
| Draft a dated offboarding checklist with owners | Draft | HRBP |
| Flag WARN, COBRA, and release review items for Legal | Route | Employment counsel |
| Draft manager talking points for an exit conversation | Draft for review | Manager and HRBP |
| Draft the access removal plan by system | Draft | IT and Security |
| Draft a knowledge transfer template | Draft | Manager |
| Summarize exit interview themes across many departures | Summarize | HRBP or People Analytics |
| Draft the team announcement and alumni invitation | Draft for review | Manager and HRBP |
| Set severance amounts or release terms | None | Legal and HR leadership |

## Guardrails

- Bias and fairness: no model selects, scores, or ranks people for termination or a reduction. If an automated system informed a discipline or termination decision anywhere, flag it for Legal, since some jurisdictions now regulate that use; check the Key dates for HR table in `03-governance/README.md`. The European Commission's draft guidelines on classifying high-risk AI systems, which are consultation drafts and not binding, read termination broadly, including non-renewal of a contract. They also say a decision can count as AI-driven when a person signs off but relies heavily on the tool's output, so a human sign-off does not by itself make such a tool low risk. A plain reminder that a contract is ending is given as an example that can fall outside.
- Privacy and data minimization: share the minimum needed with each owner. Keep the reason for an involuntary exit, any health or leave details, and severance terms out of AI tools that are not approved for them, per principle 4 of `03-governance/ai-use-policy.md`. Exit interview analysis never names individuals.
- Legal review triggers: any involuntary exit; any group reduction; any release or severance agreement; any person on leave, with a pending complaint, or who recently raised a concern; any state with a final pay deadline; any non-US worker. For anything jurisdiction-specific, check the Key dates for HR table in `03-governance/README.md` and involve counsel.
- Human review points: decision record sign-off, Legal review, the exit conversation, access removal timing, release terms, and the announcement wording.
- Employee notice: tell departing employees how exit interview data will be used and that it is analyzed in aggregate. If AI helps summarize it, say so, per principle 2 of `03-governance/ai-use-policy.md`.
- Dignity: deliver involuntary news privately and respectfully, and give the person a clear contact for questions after they leave.

## Output format

```
## Exit context
[exit type, jurisdiction, company size, owners, Legal involved Y/N]

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
```

## What this skill will not do

- Make an employment decision about a named person, including who is terminated, who is in a reduction, or rehire eligibility.
- Write to an HRIS, payroll, benefits, or identity system, remove access, or send messages to employees.
- Process real employee data in examples. Every example uses synthetic data.
- Set severance amounts or draft final release terms. It flags review items for Legal.
- Analyze one person's exit interview or infer why a named person left.
- State the final pay deadline or notice rules for a location. It points to the state labor department, the Key dates for HR table, and counsel.

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
