---
name: function-hr-operations-hris
description: Drafts the HR service delivery model (tier 0 to tier 3), ticket triage and routing rules, a cited policy Q and A setup, HRIS and skills data quality exception lists, gated automation designs for HR agents, HR technology comparisons, and record retention schedule layouts, all for human sign-off. Use whenever someone says "triage these HR tickets," "design our tier 0 to tier 3 model," "set up a policy Q and A bot," "clean up our HRIS data," "our skills data is a mess," "help us pick an HR system," "where can we automate this HR process," "can an agent update records," or "how long do we keep personnel records," and whenever an HR process is about to get an AI step or an agent with system access.
---

# HR operations, shared services, and HRIS

This skill serves an HR operations or People Systems lead. It produces service models, triage and routing rules, data quality exception lists, automation designs with approval gates, vendor comparisons, and retention schedule layouts. It stops before resolving a sensitive case, deciding anything about a named employee, or writing a change to any HR system.

## Files this skill needs

- `02-prompt-library/hr-operations.md` (prompt 3, helpdesk ticket triage and routing; prompt 5, employment verification letter)
- `10-mcp-agents/policy_qa/ENABLEMENT.md` (no answer without a source, and the trust boundary for an editable knowledge base)
- `03-governance/ai-use-policy.md` (principle 4 data minimization, principle 5 grounding, principle 6 logging, and the per-action confirmation gate for agents with HRIS write access)
- `03-governance/vendor-selection-framework.md` and `03-governance/vendor-intake-checklist.md` (build vs. buy, scorecard, red flags, vendor artifacts)
- `03-governance/quick-reference-checklist.md` and `03-governance/risk-assessment-template.md` (pre-screen and assessment for any new tool)
- `07-agentic-patterns/agent-design.md` (Pattern 2, tool use with human handoff; Pattern 3, approval gate)
- `09-evals/README.md` (testing a Q and A assistant before rollout)
- `03-governance/incident-report-template.md` (a wrong answer reached an employee, or data was exposed)
- `11-skills/fairness-audit-prep/SKILL.md` (any automation that decides eligibility or scores people)
- `03-governance/README.md` (the Key dates for HR table)

## Inputs

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| Task type | Yes | Ask the user | Triage design, Q and A launch, data cleanup, automation, vendor choice, retention |
| Jurisdictions where staff work | Yes | HRIS, read-only: work location, headcount by location | California 410, Illinois 220, NYC 180, Colorado 150, Germany 440 |
| Ticket volume by category | For triage and service model | Case system export, read-only: category, created date, channel, tier closed at | 2,900 tickets last quarter, 38% pay and payroll |
| Systems in scope and system of record per field | Yes | Ask the user | HRIS for job data, payroll for pay, case tool for tickets |
| Knowledge base editors and review process | For Q and A | Ask the user | 6 named editors, two-person review before publish |
| Field definitions and owner per field | For data quality | HRIS data dictionary export, read-only, or ask the user | Hire date owned by HR operations |
| Decision rights, budget model, IT support capacity | For vendor choice | Ask the user | HR, IT, Finance; per-employee pricing; 1 integration engineer |
| Human decision owner | Yes | Ask the user | People Systems owner |

If a required input is missing, ask for it once, in one short question at the top of your reply. Then proceed with the gap labeled "Not provided: [input]" in the output and in the audit trail.

## Tools and connectors

An agent may read, never write. Connect through MCP connectors or exports with read-only scopes, and request only these fields:

- **HRIS:** worker ID (pseudonymized), work location, job code, department, employment type, and the fields under a named data quality rule. No compensation, medical, or leave reason fields.
- **Case management system:** ticket ID, category, channel, created and closed dates, tier closed at, reopen flag. Ticket text only for the synthetic or sampled set the user names.
- **Knowledge base:** article ID, owner, last-reviewed date, body text.
- **Payroll export:** field names and record counts only, for retention and data quality mapping.
- **Repo MCP tool:** `policy_qa` (`ask_governance_policy`) finds cited passages in `03-governance/`. Use it as the reference pattern for a company Q and A assistant: it returns `no_match: true` instead of guessing, and its corpus is version-controlled. A company wiki anyone can edit breaks that trust boundary.

Rules for every tool call:

- Never call a write, send, update, approve, or workflow-trigger tool, even if the connector offers one.
- Log each call in the Audit trail: tool, purpose, fields read.
- If a tool returns data on people outside the request, or fields outside the list above, stop, do not use it, and ask the user.

## By maturity stage

Stages follow the repo's maturity scale in [the roadmap template](../../06-roadmap/transformation-roadmap-template.md). Decision rights in this skill are the same at every stage.

| Stage | How to run it | Before moving up |
|---|---|---|
| Start (Levels 0 to 1) | Paste a synthetic or sampled ticket set, the data dictionary, and knowledge base articles. Tier 1 confirms each route. | Q and A passes the pay, eligibility, and leave tests in `09-evals`. |
| Pilot (Level 2) | One read-only case system export (category, channel, dates, tier closed at, reopen flag). The HR operations lead owns it and tracks sensitive misroute rate. | Every misroute reviewed; routing rules signed off. |
| Scale (Level 3) | Read-only HRIS, case system, and knowledge base tools, calls logged; AI assistant notice live; weekly 50-ticket sample. Track cited answer accuracy and the self-service gap. | Eligibility or scoring automations pass `fairness-audit-prep`. |
| Embed (Levels 4 to 5) | A new ticket triggers routing; sensitive tickets go straight to Employee Relations. Data stewards make every HRIS change. | Rerun the test cases in `evals/` when the skill or model changes. |

## Steps

1. **Map the service tiers.** Tier 0 is self-service from approved content. Tier 1 is frontline support, where AI helps with intake, routing, and case summaries. Tier 2 is specialists, where AI assembles a case file and people judge. Tier 3 is the center of excellence that owns policy and oversees the AI. For each tier, name what it answers, what it must escalate, and how an employee reaches a person in one step. Sign-off: HR operations lead.

2. **Make the knowledge base the single source.** Every answer traces to an approved article with an owner and a last-reviewed date. Set the trust boundary before launch: if anyone can edit the source, an employee can plant instructions an HR agent will read (`10-mcp-agents/policy_qa/ENABLEMENT.md`). Keep the agent's other permissions narrow so an injected instruction has nothing worth doing. Sign-off: content owner per article.

3. **Run policy Q and A with citations or nothing.** Answer only from cited content. With no source, return no answer and route to a person. Generative AI can state false content with confidence, so review sources and citations before launch and during use. Test against `09-evals/README.md` with questions on pay, eligibility, and leave, where a nearly right answer is still wrong. Show the employee the source, say an AI assistant answered, and give a one-click route to report a wrong answer. Sign-off: HR operations lead approves launch.

4. **Triage and route as an agentic workflow with checkpoints.** Use prompt 3 in `02-prompt-library/hr-operations.md`. The flow is: read ticket, classify category and urgency, run the sensitivity check, then route. The sensitivity check is a hard stop: harassment, discrimination, medical information, accommodation, immigration, distress, or safety go straight to Employee Relations or the HRBP, whatever the stated urgency, and the agent drafts no reply. Checkpoint: a Tier 1 agent confirms each route during the pilot, then reviews a weekly 50-ticket sample after. Sign-off: Tier 1 agent per ticket; HR operations lead for the routing rules.

5. **Check employee data quality.** Agree a definition and a named owner per field. Check records against the rules: missing values, duplicates, conflicting dates, invalid codes. If the HRIS holds a skills taxonomy, add three rules: each skill maps to one taxonomy ID, each skill record carries an evidence source (assessment, project, manager validation) and a date, and self-tagged skills with no evidence are flagged, not deleted. Skills evidence can only beat credentials in talent decisions if the evidence is recorded. Output an exceptions list with counts, never a fix. Sign-off: data steward, who corrects records through the normal change process.

6. **Design automation with gates.** Score candidate workflows 1 to 3 on frequency, effort, and quality stakes; start with high-impact, low-effort work. Before mapping, interview everyone who runs the process, since people often do it differently, and agree one version. Then mark each step as rules, AI draft, or human approval, and name the system of record and policy source each AI step relies on. Keep the pattern where AI drafts from HRIS data and a person reviews before release, as with an employment verification letter. Any step that changes employment status, pay, or working conditions needs a per-action human confirmation, not one approval at setup. Process and role redesign matter more than the tool. Sign-off: People Systems owner per gate.

7. **Register any agent that can change records.** Record its purpose, scope, permissions, and the data and connectors it can reach, kept to what the task needs. Name a human owner who can approve, override, or halt it. Log which agent acted, for whom, under what authority, with which tools, and who approved. Pilot in one team and log inputs, outputs, and reviewers. Sign-off: People Systems owner, with the governance program owner.

8. **Check automated outcomes for adverse impact and explainability.** If an automation decides eligibility, approves or denies a request, or scores people, compare outcome rates by group in aggregate and route to `11-skills/fairness-audit-prep/SKILL.md`. The four-fifths ratio is a screening flag under the Uniform Guidelines, [29 CFR 1607.4(D)](https://www.govinfo.gov/content/pkg/CFR-2024-title29-vol4/pdf/CFR-2024-title29-vol4-sec1607-4.pdf), not a safe harbor or a verdict; small groups need a statistical test, and People Analytics or counsel interprets it. Write what the employee is told: the outcome, the rule or source used, the data relied on, and how to contest it with a named human reviewer. Sign-off: People Analytics for the check; counsel for any flag.

9. **Select HR technology in order.** Use `03-governance/vendor-selection-framework.md` to score two to four finalists on the same information, then run the chosen vendor through `03-governance/vendor-intake-checklist.md` with the risk assessment in parallel. Ask for security reports, logging, retention and deletion terms, fairness testing where the tool scores people, and a way to pause automated outcomes. Ask four questions of any HR AI product. Does it work from your own data, policies, and approval chains, or can it only suggest? Are permissions, audit, and security built in? Is it exact where it must be, such as payroll runs and pay change approvals? Does it add one more point tool outside your data and permission layers? Agree decision rights before the first vendor call, and plan go-live away from open enrollment. Sign-off: HR, IT, Privacy, and Procurement together.

10. **Draft a retention schedule layout with Legal.** One row per record type: system, retention period Legal confirms, deletion trigger, hold rules. Federal minimums exist, such as EEOC rules on personnel records and FLSA rules on payroll and time records, and a filed charge extends what must be kept. State and country rules differ, so counsel reviews each location. Add rows for AI logs, which the AI use policy requires, and for automated-decision data where a Key dates row applies. AI drafts the layout. Sign-off: Legal sets every period.

11. **Measure, report incidents, and hand off.** Track the metrics below. Open an incident report for any wrong policy answer that reached an employee or any data exposure. Name the owner of each next step.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Draft the tiered service model and escalation paths | HR operations lead | Drafts for sign-off |
| Score candidate workflows on frequency, effort, and stakes | People Systems owner | Drafts for sign-off |
| Classify and route a non-sensitive ticket | Tier 1 agent confirms | Drafts for sign-off |
| Send a ticket that hits the sensitivity check to Employee Relations or the HRBP | Fixed rule set by the HR operations lead | Does alone |
| Summarize a case history for a specialist | Tier 2 specialist | Drafts for sign-off |
| Answer a policy question from a cited article | Knowledge base content owner | Drafts for sign-off |
| Return "no source found" and route to a person | Fixed rule | Does alone |
| Resolve an Employee Relations, medical, or accommodation case | Employee Relations or HRBP | Refuses and routes |
| List records that break field rules | Data steward | Does alone |
| Correct or update a record in the HRIS | Data steward through the change process | Refuses and routes |
| Compare HR technology vendors on the scorecard | HR, IT, Privacy, and Procurement | Drafts for sign-off |
| Set a retention period | Legal | Refuses and routes |

### Refuse and route

- "Have the agent fix the duplicates in the HRIS" or any write to an HR system: refuse; route the exceptions list to the data steward for the change process. Do not design that change process, suggest merge values or batch approvals: the steward owns it.
- "Reply to this accommodation ticket": refuse to draft or resolve; route to Employee Relations or the HRBP with the ticket ID only.
- "Answer with what the policy probably says": refuse; return no answer and route to the content owner.
- "Give the agent standing approval to change job codes": refuse; route to the People Systems owner with the per-action confirmation gate in `03-governance/ai-use-policy.md`.
- "List the employees who file the most tickets": refuse; this monitors named people. Route to HR leadership and counsel.
- "How long must we keep these records in Germany?": refuse to set it; route to Legal with the schedule layout.
- A request to process real employee data in an example: refuse; ask for a synthetic version.

## Guardrails

- **Fairness and adverse impact.** Check that self-service and routing work equally well across languages, locations, and job types, and review escalation rates by group in aggregate. Any automation that decides eligibility or scores people goes through step 8 and `fairness-audit-prep`.
- **Explainability and notice.** Tell employees when an AI assistant answers HR questions, show the source behind each answer, and give a direct route to a person and a way to report a wrong answer. For an automated outcome, the employee sees the rule, the data used, and how to contest.
- **Privacy and minimization.** Give each tool only the fields its process needs, per principle 4 of `03-governance/ai-use-policy.md`. Keep sensitive data out of general AI tools. Require a vendor retention and deletion schedule you can verify.
- **Legal review triggers.** Retention periods, cross-border data transfers, any automation touching employment status or pay, any tool that monitors employees, any automated eligibility decision, and any vendor contract.
- **Human review points.** Tier 1 confirms routing. Specialists own every sensitive case. Data stewards own every record change. Any agent with HRIS write access needs a per-action confirmation gate.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| EU AI Act, transparency | An AI assistant answers HR questions from staff in the EU | Puts the "you are talking to an AI assistant" notice on the launch checklist; see the Key dates row |
| GDPR, Article 22 (EU) | An automation approves or denies a request for EU staff with no meaningful human involvement | Adds a human approval gate and flags the design for counsel |
| California FEHA automated-decision system regulations | An automated tool feeds an employment decision for California staff | Adds an automated-decision data row to the retention layout, period from the Key dates row |
| California CPPA regulations | HR data of California staff feeds automated processing | Flags risk-assessment and ADMT notice questions for Privacy and counsel |
| EU AI Act, high-risk HR systems | An automation allocates tasks to or monitors the performance of workers | Routes to `11-skills/eu-ai-act-hr-classifier/SKILL.md` before build |

Counsel confirms scope and current status before you rely on any row. In your reply, name each rule as: see the Key dates row "exact row name" in `03-governance/README.md`. Stop there: do not write the row's dates, status or regulation numbers, even ones you read in the table or in Sources, because the table is the one place they are kept current.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| Cited answer accuracy | Sampled Tier 0 answers the content owner rates correct and correctly cited, divided by all sampled Tier 0 answers, per month (fixed sample of at least 50) | A wrong pay or eligibility answer is a trust and legal problem, not a convenience problem |
| Sensitive misroute rate | Tickets reclassified into a sensitive category after first being routed to Tier 0 or Tier 1, divided by all tickets that end in a sensitive category, per month | Shows whether the hard stop in step 4 holds |
| Self-service resolution gap | Lowest group's Tier 0 resolution rate divided by the highest group's, across language, location, and job type groups, per quarter | Shows whether self-service works for frontline, non-English, and remote staff as well as for others |

## Output format

```
## Scope
Task, jurisdictions, systems in scope, owner, gaps ("Not provided: ...")

## Service model
| Tier | Answers | AI role | Escalates when | Route to a person | Human owner |

## Triage rules and results (synthetic or sampled only)
| Ticket | Category | Urgency | Sensitivity flag | Route to | Confirmed by |

## Data quality exceptions
| Field | Rule | Exception count | Owner | Fix through |

## Automation design
| Step | Rules / AI draft / Human approval | Gate | Log | Agent owner |
Adverse impact check needed (Y/N) and routed to:
Employee explanation and contest route:

## Vendor comparison
| Criterion | Weight | Vendor A | Vendor B | Evidence or gap |

## Retention schedule layout
| Record type | System | Period (set by Legal) | Deletion trigger | Hold rules |

## Decision rights calls in this output
| Item | Agent role | Routed to |

## Metrics
| Metric | Baseline | Owner |

## Audit trail
Inputs used:
Tools called (tool, purpose, fields read):
Items needing sign-off (item, owner):
Open legal questions:
```

## Worked example

Harbor & Pine, a fictional 1,400-person company, wants ticket triage rules and a policy Q and A launch plan across California, Illinois, NYC, Colorado, and Germany. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They were run on 18 November 2026 with `claude-sonnet-5-5`, one fresh session per case, and graded in a separate pass; see [the results](../../09-evals/skill-eval-results-2026-11-18.md) for the method and its limits.

- `triage-and-qa-launch`: designs routing rules and a cited Q and A launch end to end.
- `skills-data-cleanup-germany`: messy skills data and an assistant for German staff, with a field owner missing.
- `agent-writes-hris-records`: a request to let an agent fix records directly, which must be refused and routed.

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
