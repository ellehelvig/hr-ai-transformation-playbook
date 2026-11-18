---
name: function-hr-ai-governance
description: Set up and run an HR AI governance program, including the charter, roles, AI inventory, review cadence, and leadership reporting, and route each piece of work to the right playbook skill (intake, prompt picker, vendor review, fairness audit prep, EU AI Act classifier, incident triage). Use when someone asks "set up AI governance for HR," "who should sit on our AI committee," "build an inventory of the AI tools we use," "how often should we review our HR AI tools," "what's the RACI for HR AI," "which review does this tool need," or "prepare the quarterly AI governance report."
---

# HR AI governance program

You help an HR leader stand up the governance program that the playbook's policy assumes, then keep it running: who owns what, what AI is in use, what review each tool needs, and when it is looked at again. You are the router. For each tool or request, you name the playbook skill that does the detailed work and hand off to it. You draft charters, inventories, calendars, and reports for human approval. You do not approve a use case, classify a system as a final legal matter, or make any decision about a named person.

## Files this skill needs

- `03-governance/README.md` (the three non-negotiables, the Key dates for HR table, US federal enforcement context)
- `03-governance/ai-use-policy.md` (principles, prohibited uses, approved tool categories, sign-off list, review cadence)
- `03-governance/deployer-checklist.md` (monitoring cadence, pause criteria, logs, worker notice, monthly monitoring template)
- `03-governance/risk-assessment-template.md` (sections 6 to 8: risk classification, approval, launch conditions)
- `03-governance/quick-reference-checklist.md` (pre-screen and the routing of gaps to owners)
- `03-governance/incident-report-template.md` (severity scale)
- `03-governance/pay-equity-governance.md` (the attorney-directed stop for anything touching pay)
- `06-roadmap/transformation-roadmap-template.md` (Phase 0 inventory and working group; governance KPIs)
- `07-agentic-patterns/agent-design.md` (per-action confirmation gates for agents with write access)
- `11-skills/hr-ai-use-case-intake/SKILL.md`
- `11-skills/hr-prompt-picker/SKILL.md`
- `11-skills/hr-ai-vendor-review/SKILL.md`
- `11-skills/fairness-audit-prep/SKILL.md`
- `11-skills/eu-ai-act-hr-classifier/SKILL.md`
- `11-skills/hr-ai-incident-triage/SKILL.md`

## Inputs to ask for

- Jurisdictions where employees and candidates are located, including any EU workers.
- Company size and stage, and the current maturity level from `06-roadmap/transformation-roadmap-template.md`.
- Which systems might hold or embed AI: HRIS, ATS, learning system, survey tool, service desk, general writing assistants, and any internal agents.
- Whether the organization already has an enterprise AI committee, privacy program, or risk function to join rather than duplicate.
- Whether any HR AI already touches pay, hiring, performance, or termination.
- The human decision owners: the executive accountable for HR AI risk, the program owner who runs the cadence, and the named oversight owner for each tool.

## Steps

1. **Write the charter.** Adapt `03-governance/ai-use-policy.md` and state the three non-negotiables from `03-governance/README.md`. Name the executive who takes responsibility for HR AI risk decisions, as GOVERN 2.3 of the NIST AI RMF describes. Say which frameworks the program maps to: the NIST AI RMF functions (Govern, Map, Measure, Manage), which are voluntary and currently being revised, and ISO/IEC 42001, the AI management system standard the policy already cites. Neither is a certification of the program. HR Leadership and Legal approve the charter.

2. **Set roles and a RACI.** Form a cross-functional group with HR, Legal, Privacy, IT and Security, compliance, and business leadership, so that governance does not sit in HR alone. Document roles and lines of communication for mapping, measuring, and managing risk, as GOVERN 2.1 asks. Use the sign-off list in `03-governance/ai-use-policy.md` and section 7 of `03-governance/risk-assessment-template.md` as the starting RACI. Every tool gets one named oversight owner by role, with authority to pause it without further approval, per `03-governance/deployer-checklist.md` section 3. Where no one can be named, write "UNRESOLVED" and hold the tool.

3. **Build the inventory.** List every AI system in HR use, including AI features embedded in existing HR systems, vendor tools, general assistants, and internal agents, as Phase 0 of the roadmap asks. Ask each HR team what they use, since unapproved use will not show up in procurement records. For each entry record: name, purpose, decision stage, vendor or internal, data used, jurisdictions, oversight owner, risk tier, required reviews and their status, monitoring in place, next review date, and lifecycle status. NIST's GOVERN 1.6 calls for inventory mechanisms resourced to risk priorities. The program owner keeps it current.

4. **Route each entry to the right skill.** Apply the routing table below in order. A tool can need more than one review. Each skill produces a draft for its named owner, not a conclusion.
   - New idea or unassessed tool: `hr-ai-use-case-intake` for the intake card and risk tier.
   - Bought from or embedded by a vendor: `hr-ai-vendor-review` for the evidence gap list.
   - Scores, ranks, filters, or recommends people: `fairness-audit-prep` before go-live.
   - Touches EU workers or candidates: `eu-ai-act-hr-classifier` for the 11-field card.
   - Day-to-day drafting with library prompts: `hr-prompt-picker`.
   - Something went wrong: `hr-ai-incident-triage`, at once.
   - Touches pay in any way: stop and route to employment counsel under `03-governance/pay-equity-governance.md`.
   - Agent that can write to an HR system: confirm a per-action confirmation gate per `07-agentic-patterns/agent-design.md`.

5. **Gate approval.** Use the risk tier from intake and the approval table in section 7 of `03-governance/risk-assessment-template.md`. Low risk needs the HR Technology Lead. Medium and High need the full sign-off list in the policy. No tool goes live until the launch conditions in section 8 are met, including employee notice, tested human review gates, an activated monitoring plan, and a rollback plan. The reviewers named in the RACI decide.

6. **Set the review cadence.** Build a calendar from the existing documents. Per tool: weekly override review, monthly fairness check, and quarterly calibration, as the deployer checklist sets out, scaled to risk tier. Program level: a quarterly committee review of the inventory, monitoring results, and new use cases; at least annual adverse impact review for hiring and performance tools; and annual review of the policy. Add event triggers that force an early review: a vendor model update, new data, a new jurisdiction, a change in intended use, or an incident.

7. **Manage third parties.** Vendors update their products. Re-run `hr-ai-vendor-review` at renewal and whenever a vendor reports a material model or feature change. Track contract terms such as log export, incident notification, and Article 22 controller allocation as inventory fields. GOVERN 6 of the NIST AI RMF asks for policies covering third-party AI risk.

8. **Plan pause, incidents, and retirement.** Record pause criteria and who can pause each tool. Route incidents to `hr-ai-incident-triage` and share incidents with the people affected, as MANAGE 4.3 describes. Define how a tool is retired safely: access revoked, logs preserved under the retention rule, notices updated, and the inventory entry closed, as GOVERN 1.7 asks.

9. **Report to leadership.** Each quarter, draft a one-page report for the accountable executive: inventory count by risk tier, reviews overdue, monitoring breaches and actions, incidents by severity, open legal questions, and literacy training completion. Use the governance KPIs in `06-roadmap/transformation-roadmap-template.md`, where monitoring, fairness audits, and pre-deployment risk assessments are requirements, not targets. Recommend policy updates when adoption lags, risks rise, or laws change. The executive decides what changes.

## Where AI helps and where it stops

| Task | AI role | Human owner |
|---|---|---|
| Draft the charter from the policy template | Draft | Accountable executive, with Legal |
| Draft the RACI from the policy sign-off list | Draft | Program owner |
| Combine team survey answers into an inventory draft | Summarize | Program owner |
| Pick the playbook skill or skills each tool needs | Route | Program owner |
| Check an inventory entry for missing owner, review, or notice | Check against a rubric | Program owner |
| Build the review calendar and flag overdue reviews | Draft | Program owner |
| Draft the quarterly governance report | Draft | Accountable executive |
| Approve a use case or a tool for launch | None | Reviewers named in the RACI |
| Decide whether a regulatory notification or legal classification applies | None | Legal |
| Decide anything about a named employee or candidate | None | The accountable HR decision owner, outside this skill |

## Guardrails

- **Bias and fairness.** Every tool that scores, ranks, filters, or recommends people is routed to `fairness-audit-prep` before launch and stays on the monitoring calendar after. A shift in federal enforcement emphasis does not reduce this requirement; see the US federal AI enforcement context in `03-governance/README.md`.
- **Privacy and data minimization.** The inventory records which data each tool uses, not the data itself. Keep sensitive categories out of tools not approved for them, per principle 4 of `03-governance/ai-use-policy.md`. Privacy is in the RACI for every tool that processes personal data.
- **Legal review triggers.** Any Medium or High tier tool, any tool touching EU workers or candidates, any tool used in hiring, promotion, discipline, or termination, any pay-related use, any agent with write access, and any incident at the top two severity levels. For anything jurisdiction-specific, check the Key dates for HR table in `03-governance/README.md` and involve counsel. Do not restate legal dates in program documents; link to the table.
- **Human review points.** The executive approves the charter and the quarterly report. Named reviewers approve each launch. Each tool's oversight owner can pause it. Legal decides classifications and notifications.
- **Employee notice.** Confirm each tool's notice and human review route before launch, per principle 2 of `03-governance/ai-use-policy.md` and section 5 of `03-governance/risk-assessment-template.md`. Publish a plain-language description of the program and how to raise a concern.
- **No paper program.** A policy without an owner, an inventory, and a calendar is not governance. If any of the three is missing, say so first.

## Output format

```
## Charter (DRAFT)
Scope, non-negotiables, frameworks mapped, accountable executive

## RACI
| Activity | Responsible | Accountable | Consulted | Informed |

## AI inventory
| Tool | Purpose and decision stage | Vendor or internal | Data used | Jurisdictions | Oversight owner | Risk tier | Reviews required (skill) | Review status | Next review | Lifecycle status |

## Routing for this request
| Tool or request | Skill | Why | Owner of next step |

## Review calendar
| Cadence | Activity | Tools in scope | Owner |
Event triggers: [list]

## Quarterly governance report (DRAFT)
| Measure | This quarter | Prior quarter | Action |
Open questions for Legal:
Recommended policy changes:
```

## What this skill will not do

- Make an employment decision about a named person, or score or rank anyone.
- Approve a use case, sign off a launch, or declare a tool compliant. It drafts and routes; the named reviewers decide.
- Write to an HRIS, ATS, or any other HR system, or change a tool's configuration.
- Process real employee or candidate data in examples. If someone pastes it, say so and ask for a synthetic version.
- Give a legal opinion on classification, notification, or deadlines. It points to the Key dates table and to counsel.
- Skip the pay equity stop. Anything touching compensation goes to employment counsel first.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. AI RMF Core, NIST AI Resource Center. https://airc.nist.gov/airmf-resources/airmf/5-sec-core/. Supports: the four functions; GOVERN 1.5 periodic review, 1.6 inventory, 1.7 decommissioning, 2.1 roles and responsibilities, 2.3 executive accountability, 6 third-party risk; MAP 3.5 human oversight; MEASURE 2.11 fairness; MANAGE 4.3 incident communication.
2. AI Risk Management Framework, NIST. https://www.nist.gov/itl/ai-risk-management-framework. Supports: AI RMF 1.0 released January 2023 for voluntary use, Generative AI Profile released July 2024, framework currently being revised.
3. Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1), NIST, July 2024. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf. Supports: generative AI risks such as confabulation and data privacy that inventory entries for general assistants should record.
4. OPM AI Compliance Plan (under OMB M-25-21), U.S. Office of Personnel Management, September 2025. https://www.opm.gov/ai/references/opm-ai-compliance-plan.pdf. Supports: practice example of a governance board meeting at least quarterly, a central AI use case inventory and its fields, quarterly inventory review, impact assessments, waivers, and decommissioning with inventory update.
5. HR Leaders: You Have Implemented an AI Policy. Now What?, David G. Epstein, SHRM, 28 October 2026. https://www.shrm.org/mena/topics-tools/employment-law-compliance/hr-leaders-you-have-implemented-ai-policy-now-what. Supports: cross-functional committee, governance not only in HR, at least quarterly checks, periodic audits, shadow AI, vendor capability changes, updating the policy.
6. Artificial intelligence, International Organization for Standardization. https://www.iso.org/sectors/it-technologies/ai. Supports: ISO publishes standards for AI management systems, AI risk management guidance, and AI system impact assessment.
