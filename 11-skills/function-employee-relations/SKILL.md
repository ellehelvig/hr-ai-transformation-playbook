---
name: function-employee-relations
description: Organizes an employee relations matter from intake to a documented, human-made outcome, producing a triage record, protected-activity flags, an investigation plan, role-specific interview guides, a quoted evidence matrix and chronology, a findings memo shell, and a retaliation check on any follow-up action. Use whenever someone says "I got a complaint about a manager," "help me plan this investigation," "draft interview questions for the witnesses," "summarize these interview notes," "could this be protected concerted activity," "how do I avoid retaliation here," "can we move the complainant off the project," or "help me coach this manager," and whenever a grievance, hotline report, or exit-interview allegation needs structure. Stops before credibility, findings, and discipline, which stay with the investigator and decision owner.
---

# Employee relations and workplace investigations

This skill serves the ER lead, HRBP, or investigator who must move a concern from intake to a documented outcome. It triages, plans, drafts interview guides, and organizes evidence so the investigator can see agreement, conflict, and gaps at a glance. It stops before credibility, findings, and discipline: the investigator and the decision owner make those calls, with counsel where needed.

## Files this skill needs

- `02-prompt-library/hr-operations.md` (prompt 3, helpdesk triage, whose sensitivity flag routes protected topics straight to Employee Relations)
- `02-prompt-library/performance.md` (prompt 4, PIP documentation draft, only if the matter becomes a performance plan after the investigation closes)
- `03-governance/ai-use-policy.md` (principle 1 on human decisions and agent confirmation gates, principle 2 on notice, principle 4 on data minimization, principle 6 on logging, and the prohibited uses list)
- `03-governance/quick-reference-checklist.md` (pre-screen before any case management tool or AI feature touches ER data)
- `03-governance/risk-assessment-template.md` (required before an AI tool is added to the ER workflow)
- `03-governance/README.md` (Key dates for HR table, used by the Regulation map)
- `11-skills/fairness-audit-prep/SKILL.md` (only if discipline outcomes are compared across groups)

## Inputs

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| The concern as raised, in the reporter's words | Yes | Ask the user | "My manager said I'm too old to learn the new stack" |
| How it arrived | Yes | Ask the user | Verbal to HRBP, hotline, exit interview, observed by a manager |
| Work location of complainant, respondent, and key witnesses | Yes | HRIS, read-only: work location only | Chicago, Illinois; Berlin, Germany |
| Headcount, because federal EEO coverage depends on it | Yes | HRIS, read-only: active headcount total | 1,400 |
| Union or collective agreement coverage | Yes | HRIS, read-only: bargaining unit flag | Not represented |
| Investigator, decision owner, and whether counsel directs the work | Yes | Ask the user | HRBP investigates; VP Engineering decides; counsel not directing |
| Case system and AI tools approved for ER data | Yes | Ask the user | ER case tool approved; general chat assistant not approved |
| Recent actions touching the people involved | No | HRIS, read-only: job, manager, and project changes in the last 90 days for the named people only | Project reassignment one week after a pay question |
| Time pressure | No | Ask the user | Key witness leaves in 10 days |

If a required input is missing, ask once in one message. Then proceed and label each gap "Not provided" in the output and the audit trail.

## Tools and connectors

- **Reads allowed, read-only, minimum fields.** ER case system (case ID, category, intake date, role labels, prior case IDs for the same people). HRIS (work location, bargaining unit flag, manager, job and project changes for the named people only). Documents the investigator exports (notes, messages, policies). Use MCP connectors or exports; never request broad table pulls.
- **Repo tool.** `ask_governance_policy` in `10-mcp-agents/policy_qa/` returns cited sections of `03-governance/*.md`, for example the prohibited uses list. It is a citation finder, not legal advice; treat `no_match` as no answer.
- **Never write.** Do not call any write, send, update, close, or notify tool, even if the connector offers one. The investigator records outcomes and a human sends every letter.
- **Log every call.** Record tool, purpose, and fields read in the audit trail.
- **Stop on spillover.** If a tool returns data about people outside the case, stop, do not use it, and ask the user how to proceed.

## Steps

Run as a checkpointed workflow: the agent completes one step, shows the output, and waits for the named sign-off before any step that depends on it. Approval of the plan at the start does not count as approval of later steps (`ai-use-policy.md` principle 1).

1. **Triage at intake.** Record the concern as raised, in the reporter's words. Do not require a written complaint before acting. Classify it: possible discrimination or harassment, retaliation, safety, policy breach, interpersonal conflict, or group concern about pay or working conditions. Treat gossip or a "personality clash" as a possible sign of something deeper until checked. Flag urgency and interim measures to consider. Propose who investigates: a low-level issue may suit a manager with HR guidance; a serious allegation or a senior respondent may call for an independent external investigator so the process is seen as impartial. If the concern includes a disability or religious accommodation request, route that request to the accommodation owner the same day so it is not lost inside the case. Sign-off: ER lead confirms category, urgency, interim measures, and investigator.

2. **Flag protected activity.** Under EEOC guidance, protected activity includes complaining about discrimination, answering questions in an investigation, requesting a disability or religious accommodation, and asking about pay to uncover wage discrimination. Under the NLRA, acting with coworkers on pay or working conditions is protected concerted activity. If anyone is union-represented, note their right to request a representative in an investigatory interview that may lead to discipline. Record each flag with its date and source. Every later action is checked against these flags. Sign-off: ER lead; counsel for any concerted activity or union question.

3. **Draft the investigation plan.** Scope in and scope out. Core witnesses first; add others only if interviews show they hold relevant information. Documents and data to preserve. An out-of-scope log for new concerns, handled separately. A target timeline, because prompt action matters. Sign-off: investigator approves the plan and owns any change to scope.

4. **Draft interview guides.** Open, non-leading questions by role. Complainant: what happened, who was involved, who saw it, and where secondhand information came from. Witnesses: what they saw directly and what they heard from others. Respondent: whether the events happened, their account, and context, with a full chance to respond. Add a short confidentiality and non-retaliation script for counsel to check. Record an interview only with the interviewee's consent. If the complaint reads as AI-drafted and legal-sounding, add an opening question that confirms the core concerns in the employee's own words. The investigator runs every interview; AI is not in the room. Sign-off: investigator.

5. **Build the evidence matrix and chronology.** For each allegation: what each person said (quoted), what documents show, and where accounts agree, conflict, or leave gaps. Mark every inference as an inference. Draft a dated chronology with each entry tied to its source. No credibility ratings and no view on whether an allegation is supported. Sign-off: investigator checks every line against the original notes, because AI tools can fill gaps with content that is not in the source.

6. **Structure the findings memo; do not write findings.** Draft the shell: allegations, evidence considered, credibility assessment, findings, rationale. Leave the last three blank. After the investigator writes them, check that every finding cites evidence and no allegation lacks a finding. Before close, list how comparable matters were handled so policy is applied consistently. If the organization compares discipline outcomes across groups, People Analytics runs it with `fairness-audit-prep`: the four-fifths ratio is a screening flag under the Uniform Guidelines, [29 CFR 1607.4(D)](https://www.govinfo.gov/content/pkg/CFR-2024-title29-vol4/pdf/CFR-2024-title29-vol4-sec1607-4.pdf), not a safe harbor or a verdict, and small groups need a statistical test that People Analytics or counsel interprets. Sign-off: investigator owns findings; decision owner owns any outcome.

7. **Run a retaliation check on every proposed follow-up action.** Before any action affecting the complainant, a witness, or the respondent, compare it with the EEOC's examples of adverse action: reprimands or unjustifiably low reviews, transfers to less desirable roles, increased scrutiny, and schedule changes that make work harder. Show the number of days between each protected activity and the proposed action. Route any overlap to counsel before the action happens. Sign-off: ER lead and counsel.

8. **Draft manager coaching notes.** Base them on the EEOC's prevention steps: make clear that retaliation is prohibited, reassure people who raised concerns, act promptly on new concerns, make sure managers know their duty to stop retaliation, and enforce policy consistently. Coach the conversation, not the outcome. Sign-off: HRBP edits and delivers.

9. **Close, explain, and log.** Draft closing letters to complainant and respondent: factual, plain, every name, date, and placeholder checked. State what each person is told about the outcome, how to raise a process concern or a new retaliation concern, and who reviews it. If any AI tool assisted a step affecting either person, include notice per `ai-use-policy.md` principle 2. Counsel reviews any letter that confirms discipline; a human sends it. Log the outcome, who decided, and what AI assisted with (principle 6). Plan a check-in with the complainant after close. Apply the retention schedule and any legal hold counsel sets. Sign-off: investigator and, for discipline, counsel.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Classify a concern and flag urgency | ER lead | Drafts for sign-off |
| Route an accommodation request found inside a complaint | Accommodation owner | Does alone |
| Protected activity flags with dates and sources | ER lead; counsel for concerted activity | Drafts for sign-off |
| Investigation plan, scope, and witness order | Investigator | Drafts for sign-off |
| Interview guides by role | Investigator | Drafts for sign-off |
| Quoted evidence matrix and chronology | Investigator | Drafts for sign-off |
| Check a findings memo for uncited findings | Investigator | Does alone |
| Credibility assessment and findings | Investigator, with counsel where directed | Refuses and routes |
| Discipline or corrective action for a named person | Decision owner, with HR and counsel | Refuses and routes |
| Retaliation check on a proposed action | ER lead and counsel | Drafts for sign-off |
| Manager coaching notes | HRBP | Drafts for sign-off |
| Send closing letters or update the case record | Investigator | Refuses and routes |

### Refuse and route

- "Tell me who is lying" or "rate each witness's credibility": refuse; route to the investigator with the evidence matrix showing conflicts and gaps.
- "Recommend whether to fire the respondent": refuse; route to the decision owner, HR, and counsel with the findings memo shell.
- "Run sentiment, emotion, or truthfulness analysis on the interview recordings or chat logs": refuse; route to counsel and point to the Regulation map.
- "Flag anyone talking about pay or the union in chat": refuse; route to counsel as an NLRA interference risk.
- "Draft a PIP for the complainant while the case is open": refuse; route to the ER lead and counsel with the retaliation check.
- "Tell the employee they are not protected" or "is this conduct unlawful": refuse; route to counsel.
- "Update the case record," "send the closing letters," or "interview the witness for me": refuse; the investigator acts in the system and runs every interview.
- "Use the real case notes as the training example": refuse; examples use synthetic cases only.

## Guardrails

- **Confidentiality and minimization.** Use only a tool approved for ER data. Replace names with role labels (Complainant A, Witness 2) before drafting. Keep health details, immigration status, and other sensitive data out of any tool not approved for it (`ai-use-policy.md` principle 4).
- **Confidentiality instructions.** Under the NLRA, an employer may not keep work rules that reasonably tend to inhibit employees from exercising their Section 7 rights. Counsel reviews any instruction not to discuss an investigation.
- **No monitoring of protected activity.** Do not use AI to flag pay discussions, union references, or group complaints; that monitoring can interfere with NLRA rights.
- **Fairness in language and outcomes.** Describe conduct, not character. Remove "aggressive," "emotional," or "difficult" unless quoted. Compare with similar matters before close; see step 6 for any group comparison.
- **No emotion or truth reading.** Do not score sentiment, emotion, tone, or truthfulness in recordings, messages, or statements. See the Regulation map.
- **Privilege.** If counsel directs the investigation, ask counsel before using any AI tool; AI-generated documents can raise privilege questions.
- **Reliance still counts.** A manager who signs a decision that leans heavily on an AI output has still used AI in that decision. The European Commission's draft classification guidelines (non-binding) take the same view and also count a failure to act, such as not promoting someone. Treat both as legal review triggers.
- **Explainability and notice.** Each party learns the outcome they are entitled to know, how to contest the process, and whether AI assisted any step that affected them.
- **Legal review triggers.** Possible retaliation, a union or concerted activity question, a threatened or filed charge, any non-US party, privilege, and any discipline that relies on an automated tool.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| California SB 947 (Ch. 859, Stats. 2026) | An automated decision system informs discipline or termination of a California worker | Flags the reliance in the retaliation check and routes to counsel before action |
| Illinois HB 3773 (Public Act 103-0804) | AI is used in discipline or discharge of an Illinois employee | Records AI's role in the audit trail and adds the notice question for counsel |
| Colorado SB 26-189 (ADMT Act) | Automated technology is used in an employment decision about a Colorado employee | Drafts the explanation and human review path in the closing letter for counsel |
| EU AI Act, emotion recognition at work (Article 5(1)(f)) | Anyone proposes emotion inference on interviews or messages involving German staff | Refuses and routes to counsel |
| California AB 1883 (Ch. 853, Stats. 2026) | Emotion inference is proposed for California workers | Refuses and routes to counsel |
| GDPR, Article 22 (EU) | A decision about a German employee would rest on automated processing | Flags meaningful human involvement as a question for counsel |

See each Key dates row in `03-governance/README.md` for status and dates. Counsel confirms scope and current status before you rely on any row.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| Median days to close | For cases closed in the quarter, median calendar days from intake date to documented close date | Prompt action is part of a fair process and limits harm |
| Post-close retaliation concern rate | Cases where the complainant or a witness raised a retaliation concern within 180 days after close, divided by cases closed in the same quarter | Shows whether people can raise concerns safely; the trust measure |
| AI draft correction rate | Evidence matrix lines the investigator corrected or removed, divided by lines the agent drafted, per quarter | Shows whether AI summaries stay faithful to the notes |

## Output format

```markdown
## Case summary
[case ID, category, urgency, jurisdictions, union Y/N, investigator, decision owner, counsel directing Y/N]

## Protected activity flags
| Person (role label) | Activity | Date | Source |

## Investigation plan
Scope in: [allegations]
Scope out: [logged separately]
Witnesses: [role labels, order]
Evidence to preserve: [list]
Target timeline: [dates]

## Interview guides
[by role, open questions, confidentiality and non-retaliation script for counsel]

## Evidence matrix
| Allegation | Source | What it says (quote) | Agrees with | Conflicts with | Gap |

## Chronology
| Date | Event | Source |

## Findings memo shell
[allegations, evidence considered; credibility, findings and rationale left blank for the investigator]

## Retaliation check
| Proposed action | Affects | Protected activity and date | Days between | Route to counsel Y/N |

## Decision rights calls
| Request | Agent role | Routed to |

## Next step owner
[role, and the decision they own]

## Audit trail
Inputs used: [list; gaps marked Not provided]
Tools called: | Tool | Purpose | Fields read |
Needs sign-off: [item, who]
Open legal questions: [question, Key dates row if any, counsel]
```

## Worked example

A Harbor & Pine HRBP brings an age-related complaint from an Illinois engineer who was moved off a project a week after raising a pay question with coworkers. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They are written, not yet run against a model.

- `core-age-complaint-investigation-plan`: triage, protected activity flags, plan, guides, and retaliation check for a standard complaint.
- `edge-cross-border-missing-decision-owner`: a respondent in Germany and no named decision owner; tests gap labeling and routing.
- `red-flag-credibility-and-termination`: a request to judge who is lying, recommend termination, and update the case record.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. How to Conduct Bulletproof HR Investigations in 2025, SHRM, 30 July 2025. https://www.shrm.org/topics-tools/employment-law-compliance/how-to-conduct-bulletproof-hr-investigations-2025. Supports: prompt response, not requiring written complaints, gray-area signals, interview roles, follow-up after close.
2. Take Time to Plan Out Your Workplace Investigation Interviews, SHRM, 2 November 2022. https://www.shrm.org/in/topics-tools/employment-law-compliance/take-time-to-plan-workplace-investigation-interviews. Supports: core witnesses first, out-of-scope log, question areas by role, recording only with consent.
3. The Promise and Perils of AI in Employee Relations: Policy Drafting, SHRM, 13 November 2026. https://www.shrm.org/in/topics-tools/employment-law-compliance/promise-perils-of-ai-employee-relations-policy-drafting. Supports: AI tasks in ER, accountable human owns adverse decisions, NLRA monitoring risk, privilege concerns.
4. Strategies for managing the use of AI in employee disputes, International Bar Association, 21 April 2026. https://www.ibanet.org/strategies-for-managing-the-use-of-AI-in-employee-disputes. Supports: AI filling gaps with invented content, handling AI-drafted complaints by confirming concerns verbally.
5. Retaliation, U.S. Equal Employment Opportunity Commission. https://www.eeoc.gov/retaliation. Supports: protected activity examples, adverse action examples, coverage thresholds.
6. What is retaliation and how can I prevent it?, U.S. Equal Employment Opportunity Commission. https://www.eeoc.gov/employers/small-business/8-what-retaliation-and-how-can-i-prevent-it. Supports: the prevention steps used in manager coaching.
7. Concerted Activity, National Labor Relations Board. https://www.nlrb.gov/about-nlrb/rights-we-protect/the-law/employees/concerted-activity. Supports: definition and examples of protected concerted activity.
8. Interfering with employee rights (Section 7 and 8(a)(1)), National Labor Relations Board. https://www.nlrb.gov/about-nlrb/rights-we-protect/the-law/interfering-with-employee-rights-section-7-8a1. Supports: work rules that reasonably tend to inhibit Section 7 rights.
9. Weingarten Rights, National Labor Relations Board. https://www.nlrb.gov/about-nlrb/rights-we-protect/your-rights/weingarten-rights. Supports: union-represented employees' right to request a representative in investigatory interviews.
10. The Human Readiness Operating System, Wowledge, January 2026. Read from a copy of the publication; no web address checked. Supports (vendor-published white paper): independent external investigators for formal investigations, manager handling of low-level issues with guidance, AI assembling a case chronology.
11. The HR AI Automation Playbook, Zapier, August 2025. Read from a copy of the publication; no web address checked. Supports (vendor-published): routing accommodation requests to the right team so none are missed.
12. Draft guidelines on the classification of high-risk AI systems, European Commission, consultation drafts (non-binding). Read from a copy of the publication; no web address checked. Supports: a decision counts as AI-assisted when a human relies heavily on the output, and omissions count. Draft guidance only; counsel confirms.
