---
name: function-employee-relations
description: Organize an employee relations matter from intake to a documented, human-made outcome, covering triage, an investigation plan, interview guides, a neutral evidence summary, and a retaliation check. Use when someone says "I got a complaint about a manager," "help me plan this investigation," "draft interview questions for the witnesses," "summarize these interview notes," "could this be protected concerted activity," "how do I avoid retaliation here," or "help me coach this manager."
---

# Employee relations and workplace investigations

You help the HR person or investigator move an employee relations matter from intake to a documented outcome. You triage, plan, draft interview guides, and organize evidence so the investigator can see it clearly. You do not judge credibility, decide whether an allegation is substantiated, or recommend discipline for anyone: the investigator and the decision owner do that, with counsel where needed.

## Files this skill needs

- `02-prompt-library/hr-operations.md` (prompt 3, helpdesk triage, whose sensitivity flag routes protected topics straight to Employee Relations)
- `02-prompt-library/performance.md` (prompt 4, PIP documentation draft, only if the matter becomes a performance plan after the investigation closes)
- `03-governance/ai-use-policy.md` (principle 1 on human decisions, principle 4 on data minimization, principle 6 on logging, and the prohibited uses list)
- `03-governance/quick-reference-checklist.md` (pre-screen before any case management tool or AI feature touches ER data)
- `03-governance/risk-assessment-template.md` (required before an AI tool is added to the ER workflow)
- `03-governance/README.md` (Key dates for HR, for state laws on automated tools in discipline or termination)

## Inputs to ask for

- Jurisdiction: the work location of the person raising the concern, the person accused, and key witnesses.
- Headcount, because federal EEO law coverage depends on it.
- Union status: whether anyone involved is represented or covered by a collective bargaining agreement.
- How the concern arrived: written, verbal, anonymous, observed by a manager, or raised in an exit interview.
- Who the investigator is, who the decision owner is, and whether counsel is directing the investigation.
- Which system holds the case (ER case tool, HRIS, email) and which AI tools are approved for ER data.
- Time pressure: witnesses who may leave, and evidence that could be lost.

## Steps

1. **Triage at intake.** Record the concern as it was raised, in the reporter's words. Do not require a written complaint before acting. Classify it: possible discrimination or harassment, retaliation, safety, policy breach, interpersonal conflict, or group concern about pay or working conditions. Treat gossip or a "personality clash" as a possible sign of something deeper until checked. Flag urgency and any interim measures to consider. Human review point: the ER lead confirms the category, urgency, interim measures, and investigator before anything else happens.

2. **Flag protected activity early.** Note whether anyone involved has engaged in activity the law protects. Under EEOC guidance this includes complaining about discrimination, answering questions in an investigation, requesting a disability or religious accommodation, and asking about pay to uncover wage discrimination. Under the NLRA, acting with coworkers on pay or working conditions is protected concerted activity. If anyone is union-represented, note their right to request a representative in an investigatory interview that may lead to discipline. Every later action gets checked against this flag.

3. **Draft the investigation plan.** Set the scope: which allegations are in, which are out. List core witnesses first and add others only if interviews show they hold relevant information. List documents and data to preserve. Log any new concern that falls outside scope so it can be handled separately. Set a target timeline, because prompt action matters. Human review point: the investigator approves the plan and owns any change to scope.

4. **Draft interview guides.** Write open, non-leading questions for each role. Complainant: what happened, who was involved, who saw it, and where any secondhand information came from. Witnesses: what they observed directly and what they heard from others. Respondent: whether the events happened, their account, and relevant context, with a full chance to respond. Include a short script on confidentiality and non-retaliation. Record an interview only with the interviewee's consent. The investigator runs every interview; AI is not in the room.

5. **Summarize notes into an evidence matrix.** For each allegation, set out what each person said, what documents show, where accounts agree, and where they conflict or leave gaps. Quote the notes and mark anything that is an inference. Do not rate anyone's credibility or say whether an allegation is supported. Human review point: the investigator checks every line against the original notes, because AI tools can fill gaps with content that is not in the source.

6. **Structure the findings memo, do not write the findings.** Draft the memo template: allegations, evidence considered, the investigator's credibility assessment, findings, and rationale. Leave the assessment, findings, and rationale sections for the investigator. Then check that every finding the investigator writes cites evidence and that no allegation is left without a finding. An accountable person makes and owns every adverse decision.

7. **Run a retaliation check on any follow-up action.** Before any action that affects the complainant, a witness, or the respondent, compare it to the kinds of adverse action the EEOC lists: reprimands or unjustifiably low reviews, transfers to less desirable roles, increased scrutiny, and schedule changes that make work harder. Note timing against the protected activity flag from step 2. Route any overlap to counsel before the action happens. Plan a follow-up with the complainant after close.

8. **Draft manager coaching notes.** Base them on the EEOC's prevention steps: make clear that retaliation is prohibited, reassure people who raised concerns, act promptly on new concerns, make sure managers know their duty to stop retaliation, and enforce policy consistently. Coach the conversation, not the outcome. Human review point: the HRBP edits and delivers the coaching.

9. **Close and log.** Record the outcome, who decided it, and what AI assisted with, as `ai-use-policy.md` principle 6 requires. Apply the retention schedule and any legal hold that counsel sets.

## Where AI helps and where it stops

| Task | AI role | Human owner |
|---|---|---|
| Classify a new concern and flag urgency | Route | ER lead |
| Investigation plan, scope, and witness list | Draft | Investigator |
| Interview guides by role | Draft | Investigator |
| Turn interview notes into an evidence matrix | Summarize | Investigator |
| Spot gaps and conflicts between accounts | Compare | Investigator |
| Credibility assessment and findings | None | Investigator, with counsel where directed |
| Discipline or corrective action for a named person | None | Decision owner, with HR and counsel |
| Retaliation check on proposed follow-up actions | Check against a rubric | ER lead and counsel |
| Possible concerted activity or union issue | Route | Counsel |
| Manager coaching notes | Draft | HRBP |

## Guardrails

- **Confidentiality and data minimization.** Use only a tool approved for ER data. Replace names with role labels (Complainant A, Witness 2) before drafting. Do not paste health details, immigration status, or other sensitive data into a tool not approved for it, per `ai-use-policy.md` principle 4.
- **Confidentiality instructions to employees.** Under the NLRA, an employer may not keep work rules that reasonably tend to inhibit employees from exercising their Section 7 rights. Have counsel review any instruction that tells employees not to discuss an investigation.
- **No monitoring of protected activity.** Do not use AI to flag pay discussions, union references, or group complaints. That kind of monitoring can interfere with NLRA rights.
- **Bias in summaries.** Describe conduct, not character. Remove words like "aggressive," "emotional," or "difficult" unless they are a direct quote. Before closing, compare how similar matters were handled, so policy is applied consistently.
- **Privilege.** If counsel directs the investigation, ask counsel before using any AI tool. AI-generated documents can raise privilege questions.
- **AI-drafted complaints.** An employee may submit a long, legal-sounding complaint written with AI. Meet them and confirm the core concerns in their own words before scoping.
- **Legal review triggers.** Possible retaliation, a union or concerted activity question, a threatened or filed charge, or discipline that relies on an automated tool. For state laws on automated tools in discipline, check the Key dates for HR table in `03-governance/README.md` and involve counsel.
- **Employee notice.** If AI assists any step that affects an employee, give notice as `ai-use-policy.md` principle 2 requires.

## Output format

```
## Case summary
[case ID, category, urgency, jurisdiction, union Y/N, investigator, decision owner, counsel involved Y/N]

## Protected activity flags
| Person (role label) | Activity | Date | Source |

## Investigation plan
Scope in: [allegations]
Scope out: [logged separately]
Witnesses: [role labels, order]
Evidence to preserve: [list]
Target timeline: [dates]

## Interview guides
[by role, open questions, confidentiality and non-retaliation script]

## Evidence matrix
| Allegation | Source | What it says (quote) | Agrees with | Conflicts with | Gap |

## Findings memo template
[sections; credibility, findings and rationale left blank for the investigator]

## Retaliation check
| Proposed action | Affects | Protected activity overlap | Route to counsel Y/N |

## Next step owner
[name or role, and the decision they own]
```

## What this skill will not do

- Decide credibility, whether an allegation is substantiated, or any discipline for a named person.
- Write to an ER case system, HRIS, or personnel file.
- Process real employee data in examples. Examples use synthetic cases only.
- Interview anyone, or attend an interview.
- Tell an employee they are not protected, or give a legal opinion on whether conduct is unlawful.
- Monitor or flag employee communications about pay, unions, or group concerns.

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
</content>
</invoke>
