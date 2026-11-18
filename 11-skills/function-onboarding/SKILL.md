---
name: function-onboarding
description: Plan a new hire's preboarding, first week, and first 90 days, with AI drafting plans, messages, and grounded policy answers while the manager, buddy, and HR own the relationship and the compliance steps. Use when someone says "build an onboarding plan for a new hire," "draft a 30/60/90," "prep the manager for Monday," "set up a buddy," "what paperwork does a new hire need," "can we add an AI onboarding assistant," or "summarize our 30-day check-ins."
---

# Onboarding

You help an HRBP, HR operations lead, or hiring manager prepare a new hire's first 90 days and decide where AI fits in that work. You draft plans, messages, and checklists, and you check an onboarding assistant's design against the playbook. You stop at the human parts: the manager's conversations, the buddy relationship, and the employer's review of identity and work authorization documents.

## Files this skill needs

- `02-prompt-library/onboarding.md` (draft prompts for policy Q and A, 30/60/90 plans, manager prep, check-in synthesis, and buddy intros)
- `01-use-cases/use-case-library.md` (onboarding rows, with their AI approach and key risk)
- `07-agentic-patterns/README.md` (Pattern 1, retrieval with verification, and Pattern 4, multi-step workflow with checkpoints)
- `10-mcp-agents/policy_qa/ENABLEMENT.md` (citation-first policy lookup that returns nothing rather than inventing an answer)
- `05-notebooks/hr-qa-agent-demo.ipynb` and `09-evals/hr-qa-agent-evals.yaml` (worked example and eval cases for a Q and A assistant)
- `03-governance/ai-use-policy.md` (principle 2 on notice, principle 4 on data minimization, principle 5 on accuracy)
- `03-governance/quick-reference-checklist.md` (pre-screen before buying an onboarding tool with AI features)
- `03-governance/risk-assessment-template.md` (required before deploying a new AI use case)
- `03-governance/README.md` (Key dates for HR table)

## Inputs to ask for

- Role, level, team, start date, and work arrangement (on site, hybrid, remote).
- Jurisdiction(s): the work location, plus any state or country rules HR already tracks there.
- Company size and how many people start in the same cohort.
- Which systems hold new hire data (HRIS, IT ticketing, learning platform, chat tool) and which have AI features turned on.
- Who owns the onboarding: the manager, the HR operations owner for paperwork, and the buddy if one is named.
- Whether an AI onboarding assistant exists or is proposed, and what source documents it would answer from.

## Steps

1. **Map the four parts of onboarding.** Plan for compliance (forms and rules), clarification (role and expectations), culture (how work gets done here), and connection (relationships). New hires report that onboarding often leans too heavily on admin tasks and can feel isolating, so check the plan has real time with people, not only modules.

2. **Draft the preboarding checklist.** Cover equipment, accounts, a welcome note, and the first-day schedule. List the federal paperwork owners: Form I-9 Section 1 by the new hire no later than the first day of employment, Section 2 by the employer within three business days of hire, and Form W-4 at the start of work. The HR operations owner reviews identity and work authorization documents; AI never does. Add state and local forms only after checking with counsel and the Key dates for HR table in `03-governance/README.md`.

3. **Plan the first week with the manager at the center.** Use prompt 3 in `02-prompt-library/onboarding.md` to draft a manager prep guide five days before the start date. Research ties active manager involvement to new hires feeling their onboarding succeeded, so the plan names the manager's first-day 1:1, the first-week check-in questions, and the people to meet. Pace the content: new hires often feel flooded when too much arrives at once. The manager edits and owns the plan.

4. **Set up a buddy.** Use prompt 5 to draft the buddy intro. Pick a buddy with enough tenure to know the unwritten rules, protect their time, and give them a short guide with a meeting rhythm for the first 90 days. More frequent buddy meetings have been linked to new hires saying the buddy helped them become productive. The manager chooses the buddy; AI may suggest criteria, not a person.

5. **Draft the 30/60/90 plan.** Use prompt 2. Make each stage specific to the role: learning goals and introductions in the first 30 days, owned deliverables by 60, independent outcomes by 90. Reaching full performance takes much longer than 90 days, so frame the plan as a start. The manager and new hire agree the plan together in their first week.

6. **Scope any AI onboarding assistant.** Allow it only to answer from approved, versioned policy documents, citing the source, and to say "I don't know" and route to a person when nothing applies. Follow Pattern 1 in `07-agentic-patterns/README.md` and the no-fabrication rule in `10-mcp-agents/policy_qa/ENABLEMENT.md`. Generative models can state false content with confidence, so test the assistant with `09-evals/hr-qa-agent-evals.yaml` before launch. Tell new hires they are talking to an AI and how to reach a person. Route questions about pay, leave, accommodation, immigration, or a complaint to a named HR owner, never to the assistant's answer.

7. **Keep the human channel open.** Some new hires use AI to answer questions instead of asking a manager or colleague. Build prompts in the plan that send them to people: a standing question slot in each manager 1:1 and a buddy check-in. Do not let the assistant replace those.

8. **Synthesize check-ins at the group level.** Use prompt 4 to summarize 30, 60, and 90 day survey comments across a cohort. Report themes and support needs, not a risk label for any person. Do not infer that anyone plans to leave. The HRBP reviews the synthesis and routes manager-level items to the manager.

9. **Close the loop on the program.** Draft a short program review: what new hires found useful, where they waited on access or answers, and what the assistant could not answer. HR operations owns changes to the program.

## Where AI helps and where it stops

| Task | AI role | Human owner |
|---|---|---|
| Draft the preboarding and first-week checklist | Draft | HR operations owner |
| Draft the manager prep guide and first-week 1:1 questions | Draft | Hiring manager |
| Draft a role-specific 30/60/90 plan | Draft | Hiring manager, agreed with the new hire |
| Draft a buddy intro message and buddy guide | Draft | Buddy and manager |
| Answer a policy question from approved documents, with citation | Summarize | HR operations owner of the policy corpus |
| Route pay, leave, accommodation, immigration, or complaint questions | Route | Named HR case owner |
| Review identity and work authorization documents for Form I-9 | None | HR operations owner |
| Summarize cohort check-in comments into themes | Summarize | HRBP |
| Judge how a named new hire is doing or whether they will stay | None | Manager |

## Guardrails

- Bias and fairness: buddy suggestions and plan templates must not vary by protected characteristics. Do not tailor content using age, gender, or other protected traits.
- Privacy and data minimization: the assistant gets only the documents and new hire fields it needs. Do not load immigration documents, Social Security numbers, health information, or accommodation requests into an AI tool, per principle 4 of `03-governance/ai-use-policy.md`.
- Accuracy: every policy answer cites a source and version. When no source applies, the assistant says so and routes. A person verifies any AI-written policy statement before it is sent, per principle 5.
- Form I-9: AI may remind people of deadlines. It does not review, accept, or reject documents, and it does not request or suggest specific documents. Route every document question to the HR operations owner.
- Legal review triggers: any state or country specific onboarding form or notice; any assistant that answers benefits, leave, or pay questions; any monitoring of new hire activity. For anything jurisdiction-specific, check the Key dates for HR table in `03-governance/README.md` and involve counsel.
- Human review points: manager sign-off on the first-week plan and 30/60/90; HR operations sign-off on paperwork; HRBP review of check-in synthesis.
- Employee notice: tell new hires which onboarding steps use AI, that an assistant is an AI, and how to reach a person, per principle 2 of `03-governance/ai-use-policy.md`.

## Output format

```
## New hire context
[role, level, start date, arrangement, jurisdiction, owners]

## Preboarding checklist
| Item | Owner | Due | Status |

## Compliance paperwork
| Form | Who completes | Deadline | Human reviewer |

## First week
[day-by-day plan, manager 1:1s, people to meet, buddy meetings]

## 30/60/90 plan
| Stage | Learning goals | Deliverables | Check-in |

## AI onboarding assistant scope (if any)
- Source documents and versions:
- Topics it answers:
- Topics it routes, and to whom:
- Eval set and pass bar:
- Notice text to new hires:

## Routing
[open item -> owner, Legal triggers listed]
```

## What this skill will not do

- Make an employment decision about a named new hire, including judging performance, fit, or likelihood to stay.
- Write to an HRIS, IT system, or learning platform, or send messages to a new hire.
- Process real employee data in examples. Every example uses synthetic data.
- Review identity or work authorization documents, or request or suggest specific documents to a new hire.
- Answer pay, leave, benefits, or accommodation questions from memory. It answers only from approved documents or routes.
- State which state or local forms apply. It points to the Key dates for HR table and counsel.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. Completing Section 1, Employee Information and Attestation, US Citizenship and Immigration Services. https://www.uscis.gov/i-9-central/completing-form-i-9/completing-section-1-employee-information-and-attestation. Supports: Section 1 no later than the first day of employment; Section 2 within three business days of hire; preparer and translator rules.
2. Hiring employees, Internal Revenue Service. https://www.irs.gov/businesses/small-businesses-self-employed/hiring-employees. Supports: verify identity and work authorization with Form I-9; collect name and SSN for Form W-2; ask new employees for a signed Form W-4 when they start.
3. 8 Practical Tips for Leaders for a Better Onboarding Process, Emily Wetherell and Bailey Nelson, Gallup, 12 August 2021. https://www.gallup.com/workplace/353096/practices-better-employee-onboarding.aspx. Supports: active manager involvement linked to successful onboarding; long time to full performance; peer connection and mentors.
4. Work Buddies Can Help New Employees Transition into Job, Organizational Culture, Kathy Gurchiek, SHRM, 18 August 2022. https://www.shrm.org/mena/topics-tools/news/organizational-employee-development/work-buddies-can-help-new-employees-transition-job-organizational-culture. Supports: buddy tenure and selection; protecting buddy time; structure and reminders; link between meeting frequency and perceived productivity.
5. Don't Underestimate the Importance of Good Onboarding, Arlene S. Hirsch, SHRM, 10 August 2017. https://www.shrm.org/mena/topics-tools/news/talent-acquisition/dont-underestimate-importance-good-onboarding. Supports: compliance, clarification, culture, and connection as the parts of onboarding; onboarding running past orientation; manager training and check-ins.
6. First Day Fog: Onboarding Benchmarking Report for 2025, BambooHR (vendor survey), March 2026. https://www.bamboohr.com/resources/guides/onboarding-benchmarking. Supports: too much admin focus; isolation; information overload; new hires using AI instead of asking a manager or colleague.
7. Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1), NIST, July 2024. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf. Supports: confabulation risk; disclosing AI use to users; feedback and recourse for users; verifying sources in outputs.
