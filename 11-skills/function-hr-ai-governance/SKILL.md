---
name: function-hr-ai-governance
description: Drafts and runs an HR AI governance program, including the charter, RACI, AI and agent inventory, routing of each tool to the right playbook skill (intake, prompt picker, vendor review, fairness audit prep, EU AI Act classifier, incident triage), review calendar, and quarterly leadership report, all for human approval. Use whenever someone says "set up AI governance for HR," "who should sit on our AI committee," "build an inventory of the AI tools we use," "we found shadow AI," "how often should we review our HR AI tools," "what's the RACI for HR AI," "which review does this tool need," "can we turn on this vendor's new AI feature," "register our HR agents," or "prepare the quarterly AI governance report," and whenever a new HR AI tool, agent, or vendor feature appears.
---

# HR AI governance program

This skill serves the HR leader who owns AI risk and the program owner who runs the cadence. It produces a charter, a RACI, an inventory, a routing table, a review calendar, and a quarterly report, and it is the router: for each tool or request it names the playbook skill that does the detailed work. It drafts for human approval. It does not approve a use case, settle a legal classification, or decide anything about a named person.

## Files this skill needs

- `03-governance/README.md` (the three non-negotiables, the Key dates for HR table, US federal enforcement context)
- `03-governance/ai-use-policy.md` (principles, prohibited uses, approved tool categories, sign-off list, review cadence)
- `03-governance/deployer-checklist.md` (monitoring cadence, pause criteria, logs, worker notice, monthly monitoring template)
- `03-governance/risk-assessment-template.md` (sections 5 to 8: notice, risk classification, approval, launch conditions)
- `03-governance/quick-reference-checklist.md` (pre-screen and the routing of gaps to owners)
- `03-governance/incident-report-template.md` (severity scale)
- `03-governance/pay-equity-governance.md` (the attorney-directed stop for anything touching pay)
- `06-roadmap/transformation-roadmap-template.md` (Phase 0 inventory and working group; governance KPIs)
- `07-agentic-patterns/agent-design.md` (per-action confirmation gates for agents with write access)
- `10-mcp-agents/ADOPTION-MONITORING.md` (override rate as the adoption and review signal)
- `11-skills/hr-ai-use-case-intake/SKILL.md`, `11-skills/hr-prompt-picker/SKILL.md`, `11-skills/hr-ai-vendor-review/SKILL.md`, `11-skills/fairness-audit-prep/SKILL.md`, `11-skills/eu-ai-act-hr-classifier/SKILL.md`, `11-skills/hr-ai-incident-triage/SKILL.md`

## Inputs

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| Jurisdictions of employees and candidates, including EU workers | Yes | HRIS, read-only: work location counts; ATS, read-only: requisition locations | California, Illinois, NYC, Colorado, Germany |
| Size and roadmap maturity level | Yes | Ask the user | 1,400 staff; level 2 |
| Systems that hold or embed AI | Yes | Admin consoles and app catalog exports, read-only | HRIS, ATS, LMS, survey tool, service desk, writing assistants, internal agents |
| Existing enterprise AI committee, privacy, or risk function | Yes | Ask the user | Enterprise AI council, monthly |
| HR AI touching pay, hiring, performance, or termination | Yes | Ask the user | ATS screening feature |
| Accountable executive, program owner, oversight owner per tool | Yes | Ask the user | CHRO; HR technology lead; recruiting operations lead |

If a required input is missing, ask once in one message. Then proceed with the gap labeled "Not provided: [input]", and write "UNRESOLVED" where an owner cannot be named.

## Tools and connectors

An agent may read, never write. Connect through MCP connectors or exports with read-only scopes and these fields only:

- **HR system admin consoles (HRIS, ATS, LMS, survey platform, service desk):** AI feature name, enabled status, data scopes, release notes date. No employee or candidate records.
- **App catalog or single sign-on export:** app name and user counts by department, to find unapproved AI use. No names.
- **Procurement export:** vendor, contract renewal date, and the log export, incident notification, and Article 22 controller allocation clauses.
- **LMS:** AI literacy training completion counts by role.
- **Incident log:** incident ID, tool, severity, status.
- **Repo MCP tools:** `policy_qa` (`ask_governance_policy`) cites governance passages. The other tools on that server (`comp_banding`, `resume_screen`, `recruiter_intake`) are themselves inventory entries; inventory them like any other tool.

Rules for every tool call:

- Never call a write, send, update, configure, enable, or approve tool, even if the connector offers one.
- Log each call in the Audit trail: tool, purpose, fields read.
- If a tool returns data on named people, or fields outside this list, stop, do not use it, and ask the user.

## Steps

1. **Write the charter.** Adapt `03-governance/ai-use-policy.md` and state the three non-negotiables from `03-governance/README.md`. Name the executive who takes responsibility for HR AI risk decisions, as GOVERN 2.3 of the NIST AI RMF describes. Map the program to the NIST AI RMF functions (Govern, Map, Measure, Manage), which are voluntary and currently being revised, and to ISO/IEC 42001, the AI management system standard the policy cites. Neither is a certification of the program. Do not skip the named executive: in McKinsey's 2026 survey of 10,018 leaders and managers at organizations with 1,000 or more employees, 1 in 6 organizations had no clear C-level owner for AI adoption. Join an existing enterprise AI committee rather than duplicate it. Sign-off: HR Leadership and Legal.

2. **Set roles and a RACI.** Form a group with HR, Legal, Privacy, IT and Security, compliance, and business leadership, so governance does not sit in HR alone. Document roles and lines of communication for mapping, measuring, and managing risk, as GOVERN 2.1 asks. Start from the sign-off list in `03-governance/ai-use-policy.md` and section 7 of `03-governance/risk-assessment-template.md`. Every tool gets one named oversight owner by role, with authority to pause it without further approval, per section 3 of `03-governance/deployer-checklist.md`. Where no one can be named, write "UNRESOLVED" and hold the tool. Sign-off: program owner.

3. **Build the inventory as an agentic sweep with checkpoints.** List every AI system in HR use: features embedded in existing HR systems, vendor tools, general assistants, and internal agents, as Phase 0 of the roadmap asks. The agent reads admin consoles and the app catalog, drafts entries, and asks each HR team what they use, since unapproved use will not show up in procurement records. Checkpoint: the program owner confirms each new entry before it gets a tier. Record every column of the inventory table in the Output format, including what affected people are told and how they contest. For any agent that can read or change HR records, add: identity, scope, and permissions; the named human who can approve, override, or halt it; the data and connections it can reach, including MCP servers and other agents, kept to the minimum; where its trace log lives (who it acted for, with which tools, who approved); and who may change its workflow. GOVERN 1.6 calls for inventory mechanisms resourced to risk priorities. Sign-off: program owner keeps it current.

4. **Route each entry to the right skill.** Apply the routes below; a tool can need more than one. Each skill drafts for its named owner. To set the tier, ask how consequential the context is and how much the output weighs on the decision. If it scores, ranks, labels, recommends, or filters people, treat it as higher risk. The European Commission's draft classification guidelines (non-binding) add that a human sign-off does not lower the tier, a pipeline of agents is judged as a whole, and repurposing a general chatbot for screening may bring provider duties; route that last case to `eu-ai-act-hr-classifier` and counsel.
   - New idea or unassessed tool: the pre-screen in `03-governance/quick-reference-checklist.md`, then `hr-ai-use-case-intake` for the intake card and risk tier.
   - Bought from or embedded by a vendor: `hr-ai-vendor-review` for the evidence gap list.
   - Scores, ranks, filters, or recommends people: `fairness-audit-prep` before go-live. The four-fifths ratio is a screening flag under the Uniform Guidelines, [29 CFR 1607.4(D)](https://www.govinfo.gov/content/pkg/CFR-2024-title29-vol4/pdf/CFR-2024-title29-vol4-sec1607-4.pdf), not a safe harbor or a verdict; small groups need a statistical test, and People Analytics or counsel interprets it.
   - Touches EU workers or candidates: `eu-ai-act-hr-classifier` for the 11-field card.
   - Infers emotions of workers: stop and route to Legal before any pilot.
   - Day-to-day drafting with library prompts: `hr-prompt-picker`.
   - Something went wrong: `hr-ai-incident-triage`, at once.
   - Touches pay in any way: stop and route to employment counsel under `03-governance/pay-equity-governance.md`.
   - Agent that can write to an HR system: confirm a per-action confirmation gate per `07-agentic-patterns/agent-design.md`.

   Sign-off: program owner confirms the routes.

5. **Gate approval.** Use the risk tier from intake and the approval table in section 7 of `03-governance/risk-assessment-template.md`. Low risk needs the HR Technology Lead. Medium and High need the full sign-off list in the policy. No tool goes live until the launch conditions in section 8 are met: employee notice, tested human review gates, an activated monitoring plan, and a rollback plan. Before launch, write down answers to three questions: who is accountable when the tool is wrong, how will we know it still works next quarter, and can we explain and defend a decision it informed, including what the affected person is told and how they contest. Prefer a pilot in one team before wider rollout. Sign-off: the reviewers named in the RACI.

6. **Set the review cadence.** Per tool, scaled to risk tier: weekly override review, monthly fairness check, and quarterly calibration, as the deployer checklist sets out. Read the override rate both ways, per `10-mcp-agents/ADOPTION-MONITORING.md`: frequent overrides with no reason mean the tool is tolerated, not adopted, and an override rate near zero on a tool that scores people is a flag for rubber-stamping. Program level: quarterly committee review of the inventory, monitoring results, and new use cases; at least annual adverse impact review for hiring and performance tools; annual policy review. Event triggers force an early review: a vendor model update, new data, a new jurisdiction, a change in intended use, or an incident. Sign-off: program owner.

7. **Manage third parties.** Re-run `hr-ai-vendor-review` at renewal and whenever a vendor reports a material model or feature change, including a new AI feature switched on by default. Track contract terms such as log export, incident notification, and Article 22 controller allocation as inventory fields. GOVERN 6 of the NIST AI RMF asks for policies covering third-party AI risk. Sign-off: program owner with Procurement.

8. **Plan pause, incidents, and retirement.** Record pause criteria and who can pause each tool. Route incidents to `hr-ai-incident-triage` and share incidents with the people affected, as MANAGE 4.3 describes. Retire a tool safely: access revoked, logs preserved under the retention rule, notices updated, inventory entry closed, as GOVERN 1.7 asks. Sign-off: oversight owner per tool.

9. **Track AI literacy by role.** Record training completion for each role that operates or reviews an HR AI tool, with reviewers trained to challenge an output, not only use it. Sign-off: program owner.

10. **Report to leadership.** Each quarter, draft a one-page report for the executive: inventory count by risk tier, reviews overdue, monitoring breaches and actions, incidents by severity, open legal questions, and literacy training completion. Use the governance KPIs in `06-roadmap/transformation-roadmap-template.md`, where monitoring, fairness audits, and pre-deployment risk assessments are requirements, not targets. Recommend policy updates when adoption lags, risks rise, or laws change. Sign-off: the executive.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Draft the charter from the policy template | Accountable executive, with Legal | Drafts for sign-off |
| Draft the RACI from the policy sign-off list | Program owner | Drafts for sign-off |
| Combine team answers and console reads into an inventory draft | Program owner | Drafts for sign-off |
| Pick the playbook skill or skills each tool needs | Program owner | Drafts for sign-off |
| Flag an entry missing an owner, review, or notice | Fixed rule | Does alone |
| Flag overdue reviews on the calendar | Fixed rule | Does alone |
| Draft the quarterly governance report | Accountable executive | Drafts for sign-off |
| Approve a use case or a tool for launch | Reviewers named in the RACI | Refuses and routes |
| Pause or resume a tool | The tool's oversight owner | Refuses and routes |
| Enable a vendor AI feature or change a tool's configuration | Oversight owner after review | Refuses and routes |
| Decide whether a legal classification or regulatory notification applies | Legal | Refuses and routes |
| Decide anything about a named employee or candidate | The accountable HR decision owner, outside this skill | Refuses and routes |

### Refuse and route

- "Approve the ATS screening feature so we can launch Monday": refuse; route to the reviewers in the RACI with the intake card and launch conditions.
- "Confirm this tool is not high-risk under the EU AI Act": refuse; route to `eu-ai-act-hr-classifier` and counsel.
- "Rank our managers by how well they use AI": refuse; this scores named people. Route to HR leadership.
- "Turn on the meeting tool's sentiment and mood scoring for engagement": refuse; it infers emotions at work. Route to Legal before any pilot.
- "Skip the fairness audit, the EEOC isn't pursuing disparate impact": refuse; the audit stays required. Route to Legal with the US federal AI enforcement context.
- "Can the comp team use AI to set raises?": stop; route to employment counsel under `03-governance/pay-equity-governance.md`.
- "Switch the vendor's new AI feature on" or "email all staff the new policy": refuse to configure or send; route to the oversight owner with a draft notice.
- Real employee or candidate data pasted into the request: refuse to process it; ask for a synthetic version.

## Guardrails

- **Fairness and adverse impact.** Every tool that scores, ranks, filters, or recommends people goes to `fairness-audit-prep` before launch and stays on the monitoring calendar. A shift in federal enforcement emphasis does not reduce this requirement; see the US federal AI enforcement context in `03-governance/README.md`.
- **Explainability and notice.** Confirm each tool's notice and human review route before launch, per principle 2 of `03-governance/ai-use-policy.md` and section 5 of `03-governance/risk-assessment-template.md`. Publish a plain-language description of the program and how to raise a concern.
- **Privacy and minimization.** The inventory records which data each tool uses, not the data. Keep sensitive categories out of tools not approved for them, per principle 4. Privacy is in the RACI for every tool that processes personal data.
- **Legal review triggers.** Any Medium or High tier tool, any tool touching EU workers or candidates, any tool used in hiring, promotion, discipline, or termination, any pay-related use, any emotion inference, any agent with write access, and any incident at the top two severity levels. Link to the Key dates for HR table; do not restate legal dates in program documents.
- **No paper program.** A policy without an owner, an inventory, and a calendar is not governance. If any of the three is missing, say so first.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| EU AI Act, high-risk HR systems | A tool is used in recruiting, promotion, termination, task allocation, or performance monitoring of EU workers | Routes to `eu-ai-act-hr-classifier`; adds oversight, logging, and notice fields |
| EU AI Act, emotion recognition at work (Article 5(1)(f)) | A tool infers the emotions of workers | Flags it as a prohibited-use question and routes to Legal before any pilot |
| EU AI Act, AI literacy (Article 4) | Staff operate or use AI systems | Tracks completion by role in an internal training record |
| NYC Local Law 144 | A tool may be a covered AEDT in NYC hiring or promotion | Adds bias audit date and notice status as inventory fields; counsel confirms coverage |
| Colorado SB 26-189 (ADMT Act) | Automated technology is used in an employment decision for Colorado staff | Adds notice and adverse-decision explanation fields; counsel checks status |
| California FEHA automated-decision system regulations | An automated tool is used in hiring or employment for California staff | Treats vendor-built tools as the employer's risk; keeps automated-decision data per the Key dates row |

Counsel confirms scope and current status before you rely on any row.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| Inventory review currency | Live inventory entries with every required review complete and the next review date not past, divided by all live entries, at quarter end | Shows whether the program is running or on paper |
| Fairness monitoring coverage | Live tools that score, rank, filter, or recommend people with a monthly fairness check completed in each month of the quarter, divided by all such live tools | Tracks the third non-negotiable directly |
| Time to pause | Median hours from a monitoring breach or top-two-severity incident being logged to the tool being paused or a documented decision not to pause, per quarter | Shows whether pause authority works in practice |

## Output format

```
## Charter (DRAFT)
Scope, non-negotiables, frameworks mapped, accountable executive

## RACI
| Activity | Responsible | Accountable | Consulted | Informed |

## AI inventory
| Tool | Purpose and decision stage | Vendor or internal | Data used | Jurisdictions | Oversight owner | Risk tier | Reviews required (skill) | Review status | Monitoring in place | Notice and contest route | Next review | Lifecycle status |
Agents: | Agent | Scope and permissions | Halt owner | Connections | Trace log location |

## Routing for this request
| Tool or request | Skill | Why | Owner of next step |

## Review calendar
| Cadence | Activity | Tools in scope | Owner |
Event triggers:

## Quarterly governance report (DRAFT)
| Measure | This quarter | Prior quarter | Action |
Recommended policy changes:

## Decision rights calls in this output
| Item | Agent role | Routed to |

## Audit trail
Inputs used:
Tools called (tool, purpose, fields read):
Items needing sign-off (item, owner):
Open legal questions:
```

## Worked example

Harbor & Pine, a fictional 1,400-person company, builds its first HR AI inventory, routes five tools, and drafts its quarterly report. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They are written, not yet run against a model.

- `inventory-and-routing`: builds an inventory, routes each tool, and sets the calendar end to end.
- `vendor-feature-on-by-default`: a vendor AI feature switched on for US and German staff with no oversight owner.
- `approve-and-emotion-scoring`: a request to approve a launch and enable mood scoring of staff, to refuse and route.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. AI RMF Core, NIST AI Resource Center. https://airc.nist.gov/airmf-resources/airmf/5-sec-core/. Supports: the four functions; GOVERN 1.5 periodic review, 1.6 inventory, 1.7 decommissioning, 2.1 roles and responsibilities, 2.3 executive accountability, 6 third-party risk; MAP 3.5 human oversight; MEASURE 2.11 fairness; MANAGE 4.3 incident communication.
2. AI Risk Management Framework, NIST. https://www.nist.gov/itl/ai-risk-management-framework. Supports: AI RMF 1.0 released January 2023 for voluntary use, Generative AI Profile released July 2024, framework currently being revised.
3. Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1), NIST, July 2024. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf. Supports: generative AI risks such as confabulation and data privacy that inventory entries for general assistants should record.
4. OPM AI Compliance Plan (under OMB M-25-21), U.S. Office of Personnel Management, September 2025. https://www.opm.gov/ai/references/opm-ai-compliance-plan.pdf. Supports: practice example of a governance board meeting at least quarterly, a central AI use case inventory and its fields, quarterly inventory review, impact assessments, waivers, and decommissioning with inventory update.
5. HR Leaders: You Have Implemented an AI Policy. Now What?, David G. Epstein, SHRM, 28 October 2026. https://www.shrm.org/mena/topics-tools/employment-law-compliance/hr-leaders-you-have-implemented-ai-policy-now-what. Supports: cross-functional committee, governance not only in HR, at least quarterly checks, periodic audits, shadow AI, vendor capability changes, updating the policy.
6. Artificial intelligence, International Organization for Standardization. https://www.iso.org/sectors/it-technologies/ai. Supports: ISO publishes standards for AI management systems, AI risk management guidance, and AI system impact assessment.
7. Workday's Vision for AI Governance, Workday, 2026. Read from a copy of the publication; no web address checked. Supports (vendor-published, one viewpoint): the decision-weight triage test and agent inventory fields.
8. Draft guidelines on the classification of high-risk AI systems, European Commission, consultation drafts (non-binding). Read from a copy of the publication; no web address checked. Supports: the scoring and ranking signal, sign-off not lowering the tier, pipelines judged as a whole, and repurposing a general tool. Draft guidance only; counsel confirms.
9. The State of Organizations 2026, McKinsey & Company, 2026. Read from a copy of the publication; no web address checked. Supports: the 1 in 6 figure on C-level AI ownership.
