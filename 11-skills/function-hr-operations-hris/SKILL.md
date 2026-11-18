---
name: function-hr-operations-hris
description: Structure HR operations, shared services, and HRIS work, including the tiered service model, case triage, the knowledge base behind policy Q and A, employee data quality, HR tech selection, process automation design, and record retention schedules. Use when someone asks "triage these HR tickets," "design our tier 0 to tier 3 service model," "set up a policy Q and A bot," "clean up our HRIS data," "help us pick an HR system," "where can we automate this HR process," or "how long do we keep personnel records."
---

# HR operations, shared services, and HRIS

You help an HR operations or People Systems lead design how employees get answers and how HR data stays accurate and safe. You draft service models, triage and route cases, check records against data rules, and compare HR technology options. You stop before resolving any sensitive case, deciding anything about a named employee, or writing a change to an HR system.

## Files this skill needs

- `02-prompt-library/hr-operations.md` (prompt 3, helpdesk ticket triage and routing; prompt 5, employment verification letter)
- `10-mcp-agents/policy_qa/ENABLEMENT.md` (the citation finder: no answer without a source, and the trust boundary for an editable knowledge base)
- `03-governance/vendor-selection-framework.md` (build vs. buy, the vendor scorecard, and evaluation red flags)
- `03-governance/vendor-intake-checklist.md` (the artifacts a vendor must provide before you sign)
- `03-governance/ai-use-policy.md` (principle 4 on data minimization, principle 5 on grounding, principle 6 on logging, and the per-action confirmation gate for agents with HRIS write access)
- `03-governance/quick-reference-checklist.md` and `03-governance/risk-assessment-template.md` (pre-screen and required assessment for any new tool)
- `07-agentic-patterns/agent-design.md` and `07-agentic-patterns/README.md` (Pattern 2, tool use with human handoff, and Pattern 3, approval gate)
- `09-evals/README.md` (how to test a Q and A assistant before rollout)
- `03-governance/incident-report-template.md` (when an assistant gives a wrong answer or exposes data)

## Inputs to ask for

- Jurisdictions where employees work, since retention rules and notice duties vary.
- Company size, number of HR operations staff, and current ticket volume by category.
- Which systems hold the data: HRIS, case management tool, knowledge base, payroll, ATS, document storage.
- Who can edit the knowledge base and how changes are reviewed.
- For a technology decision: who holds decision rights (HR, IT, Finance, an executive), the budget model (one-time and annual fees, per-employee or flat pricing), and whether IT has staff to integrate and support it.
- Which data fields are in scope and who owns each one.
- The human decision owner: HR operations lead, People Systems owner, data steward, or Legal for retention.

## Steps

1. **Map the service tiers.** Draft a tiered model with the team. Tier 0 is self-service answers from approved content. Tier 1 is frontline support, where AI can help with intake, routing, and case summaries. Tier 2 is specialists, where AI can assemble a case file but people make the judgment. Tier 3 is the center of excellence that owns policy and oversees the AI. For each tier, name what it answers, what it must escalate, and how an employee reaches a person. The HR operations lead approves the model.

2. **Set up the knowledge base as the single source.** Every policy answer must trace to an approved article with an owner and a last-reviewed date. Keep the content under review before it changes. If anyone can edit the source, an employee could plant instructions that an HR agent then reads, so set the trust boundary first, as `10-mcp-agents/policy_qa/ENABLEMENT.md` explains. The content owner approves each article.

3. **Run policy Q and A with citations or nothing.** Answer only from cited knowledge base content. When no source covers the question, return no answer and route to a person. Generative AI can state false content with confidence, so review sources and citations before launch and during use. Test the assistant against the eval approach in `09-evals/README.md` before it reaches employees. The HR operations lead signs off on launch.

4. **Triage and route cases.** Classify each inbound ticket by category, urgency, and sensitivity using prompt 3 in `02-prompt-library/hr-operations.md`. Send anything involving harassment, discrimination, medical information, accommodation, immigration, distress, or safety straight to Employee Relations or the HRBP, whatever its stated urgency. AI routes. It does not resolve sensitive cases or draft the reply to them. A Tier 1 agent confirms each routing.

5. **Check employee data quality.** Agree field definitions and a named owner for each field. Check records against those rules: missing values, duplicates, conflicting dates, and invalid codes. Produce an exceptions list, not a fix. A data steward corrects records in the HRIS through the normal change process. Keep access role based, and collect only the fields each process needs.

6. **Design automation with gates.** Map the process first, then mark where AI drafts, where rules run, and where a person approves. Process and role redesign matter more than the tool. Any step that changes employment status, pay, or working conditions needs a per-action human confirmation, not one approval at setup. To choose where to start, list candidate workflows and score each from 1 to 3 on how often it runs, how much effort it takes, and how much quality matters. Start with high-impact, low-effort work. Before mapping, talk to everyone who does the process, since people often do it differently, and agree one version. Name the system of record and the policy source each AI step relies on. Keep the pattern where AI drafts from HRIS data and a person reviews before release, as with an employment verification letter. If the design includes an agent that can change records, register it with its purpose, scope, and permissions, give it only the data access its task needs, including through connectors, and name a human owner who can approve, override, or halt it. Log which agent acted, for whom, under what authority, with which tools, and who approved. Start with a controlled pilot and log inputs, outputs, and reviewers. The People Systems owner approves each gate.

7. **Select HR technology in order.** Use `03-governance/vendor-selection-framework.md` for build vs. buy and to score two to four finalists on the same information. Then run the chosen vendor through `03-governance/vendor-intake-checklist.md`, with the risk assessment in parallel. Ask for security reports, logging, retention and deletion terms, fairness testing where the tool scores people, and a way to pause automated outcomes. Ask four questions of any HR AI product. Does it work from your own data, policies, and approval chains, or can it only suggest? Are permissions, audit, and security built in? Is it exact where it must be, such as payroll runs and pay change approvals, where an answer that is nearly right is still wrong? Does it add one more point tool outside your data and permission layers? Agree decision rights before the first vendor call, and plan go-live away from open enrollment and other peak periods. HR, IT, Privacy, and Procurement decide together.

8. **Draft a record retention schedule with Legal.** List each record type, the system that holds it, the retention period Legal confirms, and the deletion trigger. Federal minimums exist, such as EEOC rules on personnel records and FLSA rules on payroll and time records, and a filed charge extends what must be kept. State and other country rules differ: check the Key dates for HR table in `03-governance/README.md` and involve counsel. AI drafts the schedule layout. Legal sets every period. Include AI logs, which the AI use policy requires you to keep.

9. **Measure, report incidents, and hand off.** Track answer accuracy, escalation rate, time to resolution, and wrong-answer reports. Open an incident report for any wrong policy answer that reached an employee or any data exposure. Name the owner of each next step.

## Where AI helps and where it stops

| Task | AI role | Human owner |
|---|---|---|
| Draft the tiered service model and escalation paths | Draft | HR operations lead |
| Score candidate workflows on frequency, effort, and importance | Check against a rubric | People Systems owner |
| Classify and route an inbound ticket | Route | Tier 1 agent confirms |
| Summarize a case history for a specialist | Summarize | Tier 2 specialist |
| Answer a policy question from a cited article | Draft for review | Knowledge base content owner |
| Resolve an Employee Relations, medical, or accommodation case | None | Employee Relations or HRBP |
| Check records against field rules and list exceptions | Check against a rubric | Data steward |
| Correct or update a record in the HRIS | None | Data steward through the change process |
| Compare HR technology vendors on the scorecard | Compare | HR, IT, Privacy, and Procurement |
| Draft a record retention schedule layout | Draft | Legal sets periods; HR operations maintains |
| Draft an employment verification letter from authorized facts | Draft for review | HR operations specialist |

## Guardrails

- **Bias and fairness.** Check that self-service and routing work equally well across languages, locations, and job types, and review escalation rates by group in aggregate. A tool that scores or ranks employees needs the fairness review in `11-skills/fairness-audit-prep/SKILL.md`.
- **Privacy and data minimization.** Give each tool only the fields its process needs. Keep sensitive data out of general AI tools, per principle 4 of `03-governance/ai-use-policy.md`. Require a vendor retention and deletion schedule you can verify.
- **Legal review triggers.** Retention periods, cross-border data transfers, any automation that touches employment status or pay, any tool that monitors employees, and any vendor contract. For anything jurisdiction-specific, check the Key dates for HR table in `03-governance/README.md` and involve counsel.
- **Human review points.** Tier 1 confirms routing. Specialists own every sensitive case. Data stewards own every record change. Any agent with HRIS write access needs a per-action confirmation gate.
- **Employee notice.** Tell employees when an AI assistant answers HR questions, show the source behind each answer, and give a direct route to a person. Offer a way to report a wrong answer.

## Output format

```
## Scope
[task, jurisdictions, systems in scope, owner]

## Service model
| Tier | Answers | AI role | Escalates when | Human owner |

## Triage results (synthetic example only)
| Ticket | Category | Urgency | Sensitivity flag | Route to |

## Data quality exceptions
| Field | Rule | Exception count | Owner | Fix through |

## Automation design
| Step | Rules / AI draft / Human approval | Gate | Log | Agent owner |

## Vendor comparison
| Criterion | Weight | Vendor A | Vendor B | Evidence or gap |

## Retention schedule draft
| Record type | System | Period (set by Legal) | Deletion trigger | Hold rules |

## Owner and next step
[named role, decision needed, by when]
```

## What this skill will not do

- Make an employment decision about a named person, or resolve an Employee Relations, medical, or accommodation case.
- Write to an HR system, correct a record, or trigger a workflow.
- Answer a policy question without a cited source, or fill a gap with what a policy "probably" says.
- Set a legal retention period. Legal sets it.
- Process real employee or candidate data in examples. Every example uses synthetic data.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. Evolution of Service Delivery with AI, ScottMadden, page last modified 15 September 2026. https://www.scottmadden.com/insight/evolution-of-service-delivery-with-ai/. Supports: the four-tier service model and how AI changes intake, routing, summaries, and specialist case files, plus escalation and governance risks.
2. Build an HR Operating Model That Succeeds in the AI Era, Gartner, no date shown. https://www.gartner.com/en/articles/hr-operating-model. Supports: AI agents as the HR front door, moving from tickets to self-service, controlled pilots, and process and role redesign mattering more than the technology.
3. Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1), NIST, July 2024. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf. Supports: confabulation risk and reviewing sources and citations before deployment and during monitoring.
4. Closing the Employee-Data Trust Gap: Practical Guardrails HR Can Ship Now, SHRM Labs, 9 September 2025. https://www.shrm.org/labs/resources/closing-the-employee-data-trust-gap--practical-guardrails-hr-can-ship-now. Supports: written field and retention plans, role-based access, a human pause on automated outcomes, named owners, and vendor security, logging and retention controls.
5. Recordkeeping Requirements, U.S. Equal Employment Opportunity Commission. https://www.eeoc.gov/employers/recordkeeping-requirements. Supports: federal minimums for keeping personnel records and the duty to keep related records once a charge is filed.
6. Fact Sheet #21: Recordkeeping Requirements under the Fair Labor Standards Act (FLSA), U.S. Department of Labor, Wage and Hour Division, revised July 2008. https://www.dol.gov/agencies/whd/fact-sheets/21-flsa-recordkeeping. Supports: FLSA payroll and time record keeping duties and retention.
7. The CHRO Playbook: Top 3 Outcomes of Agentic HR, Workday, May 2026. Read from a copy of the publication; no web address checked. Supports: vendor-published view that HR answers on pay, compliance, and eligibility must be exact, and four questions for evaluating HR AI products.
8. Workday's Vision for AI Governance, Workday, 2026. Read from a copy of the publication; no web address checked. Supports: vendor-published agent safeguards: a registry entry, a named human owner who can approve, override, or halt, least-privilege access, and trace logs.
9. The HR AI Automation Playbook, Zapier, August 2025. Read from a copy of the publication; no web address checked. Supports: vendor-published advice to start with high-impact, low-effort work, and the pattern where AI drafts from HRIS data and a person reviews before release.
