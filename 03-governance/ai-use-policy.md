# HR AI use policy

**Status:** Template, adapt for your organization before adopting
**Version:** 1.0
**Last reviewed:** [DATE]
**Owner:** People Team / HR Technology
**Legal review required before publishing:** Yes

**Changelog:**

| Version | Date | Change |
|---|---|---|
| 1.0 | [DATE] | Initial policy |

---

## Purpose

This policy establishes principles and requirements for how the People Team uses artificial intelligence tools in HR processes. It applies to all AI-assisted workflows, including commercial AI tools, internally built agents, and AI features embedded in existing HR systems.

The goal is to enable responsible innovation: capturing the efficiency and experience benefits of AI while protecting employee rights, maintaining human accountability in employment decisions, and complying with applicable laws.

---

## Scope

This policy applies to:
- All members of the People Team using AI tools in their work
- All AI tools used in HR processes, regardless of vendor
- Any automated or AI-assisted workflow that touches employee data or influences employment decisions

---

## Jurisdiction

This policy states organization-wide principles. It does not replace jurisdiction-specific compliance work. For EU high-risk AI obligations, GDPR Article 22, UK automated decision-making rules, US state AI hiring laws, and Ontario's AI disclosure requirement, use the checklists and templates listed under [Cross-links](#cross-links) alongside this policy, not instead of it.

**Scope of this playbook.** The jurisdiction-specific content here covers the EU, US, UK, and Canada, because those are the markets with the most developed AI employment regulation as of this writing. It does not cover APAC, Latin America, the Middle East, or Africa. If you operate in those markets, treat the principles here as a starting frame and get local counsel before assuming any specific checklist applies. A genuinely global program needs jurisdiction coverage this playbook doesn't provide yet.

---

## Core principles

### 1. Humans make consequential employment decisions

AI may assist, inform, or accelerate HR work. It may not make or fully automate decisions that materially affect an employee's employment status, compensation, advancement, or working conditions without meaningful human review.

This includes: hiring decisions, performance ratings, promotions, terminations, PIPs, pay changes, and disciplinary actions.

"Human review" means a qualified HR professional or manager has reviewed the AI output, applied their judgment, and taken ownership of the decision.

**Agentic tools carry this principle further.** An AI agent that can plan and execute multi-step actions (writing to the HRIS, sending communications, triggering a workflow) must have an explicit confirmation gate before any action affecting employment status, compensation, advancement, or working conditions. A human approving the agent's plan once at setup does not satisfy "meaningful human review" for each individual action. See [Designing HR agents](../07-agentic-patterns/agent-design.md) for the scope and escalation design this requires.

### 2. Employees have a right to know

Employees will be informed when AI is used in processes that affect them, including recruiting, performance assessment, and L&D recommendations, through Privacy Notices and employee communications.

Employees may request human review of any AI-assisted decision that affects them. That request must be honored within [X] business days.

### 3. Fairness and bias prevention are active responsibilities

Before deploying any AI use case that scores, ranks, or filters employees or candidates, the People Team must:
- Document the intended use and decision criteria
- Assess potential for disparate impact across protected characteristics
- Establish a monitoring plan to detect bias post-deployment
- Define thresholds that trigger human review or tool suspension

AI tools used in hiring or performance management must be reviewed for adverse impact at least annually.

### 4. Data minimization and privacy

AI tools used in HR processes may only access the employee data necessary for their specific function. People Team members may not input sensitive personal data (health information, protected category data, immigration status) into AI tools unless the tool has been explicitly approved for that data type.

No employee data will be used to train external AI models without explicit consent and legal review.

### 5. Accuracy and grounding

AI-generated content used in HR communications, policies, or official documentation must be reviewed and verified by a human before distribution. Known hallucination risk areas, policy details, legal requirements, benefit specifics, must be verified against authoritative source systems before any AI-generated response is treated as final.

### 6. Auditability

All AI-assisted processes that influence employment decisions must be logged with sufficient detail to reconstruct the AI's input, output, and the human review that followed. Logs must be retained for [retention period, consult Legal].

---

## Prohibited uses

The following uses of AI in HR are prohibited without explicit approval from Legal, Privacy, and HR Leadership:

- **Autonomous hiring decisions**: rejecting candidates without human review of AI scoring
- **Behavioral surveillance**: using AI to monitor employee communications, productivity, or sentiment without disclosure and consent
- **Predictive health or disability inference**: using AI to infer medical conditions or disability status from work patterns
- **Automated termination**: any workflow that triggers or documents a termination without direct human initiation and review
- **Using personal data for purposes beyond original collection scope** without updated consent

---

## Approved tool categories

| Category | Approval status | Notes |
|---|---|---|
| Copilot writing assistants (drafting, summarizing) | Approved | Do not input sensitive personal data |
| AI Q&A for HR policy | Approved with monitoring | Responses must be grounded in authoritative source; escalation path required |
| Resume screening tools | Approved with conditions | Requires annual adverse impact review; human review of all shortlists |
| Survey sentiment analysis | Approved | Aggregate insights only; no individual scoring |
| Attrition risk models | Approved with conditions | HR leadership review required before any action taken on individual scores |
| Autonomous offer generation | Under review | Not approved until legal review complete |
| Performance rating automation | Not approved | Employment decision; requires human judgment |
| Agents with HRIS or system write access | Approved with conditions | Requires a per-action confirmation gate for any employment-affecting action, not just approval of the agent's overall plan; scope and escalation rules documented per [agent design guidance](../07-agentic-patterns/agent-design.md) |
| Compensation and pay equity analysis | Attorney-directed only | Do not run without employment counsel initiating the analysis; see [pay equity governance](pay-equity-governance.md) before touching any comp data |

---

## Governance process for new AI use cases

Before implementing a new AI use case in HR, complete the [Risk Assessment Template](risk-assessment-template.md). Use cases classified as medium or high risk require sign-off from:
- HR Leadership
- Legal / Employment Counsel
- Privacy / Data Protection
- People Systems

Timeline from intake to approval: target 4 weeks for low risk, 8 weeks for medium/high.

---

## Reporting concerns

Employees or People Team members who observe AI being used in a way that appears to violate this policy should report it to [HR Ethics channel / HR Leadership / EthicsPoint, configure for your org].

Reports will be reviewed within [X] business days. Retaliation for good-faith reporting is prohibited.

If the report describes an AI system doing something it shouldn't (wrong information, a disclosure, a biased output), open an [incident report](incident-report-template.md).

---

## Review cadence

This policy will be reviewed annually and updated when:
- New AI capabilities are deployed in HR systems
- Relevant regulations change (e.g., new state AI hiring laws, EEOC guidance)
- A significant incident or concern is identified

**On EEOC guidance specifically:** the EEOC withdrew its 2022 and 2023 AI technical assistance documents in early 2025, and an April 2025 executive order directs federal agencies to deprioritize disparate-impact enforcement. That's an enforcement-priority shift, not a change in the underlying law, Title VII disparate-impact liability is still codified and still enforceable through private litigation, and state and local laws (Illinois, Colorado, NYC, and others) impose independent obligations regardless of federal posture. Principle 3 and the fairness audit requirements in this policy apply exactly as written, don't scope them down because federal enforcement has quieted. See [US federal AI enforcement context](README.md#us-federal-ai-enforcement-context) for detail.

---

## Frameworks this policy draws on

This policy is structured around two frameworks rather than invented from scratch:

- **NIST AI Risk Management Framework 1.0** (January 2023): the four functions, Govern, Map, Measure, Manage, map loosely to this policy's structure. Governance process and non-negotiables (Govern), the use-case-specific risk assessment (Map), the fairness and bias monitoring plan (Measure), and the incident and escalation process (Manage).
- **ISO/IEC 42001**: the AI management system standard referenced in the [vendor intake checklist](vendor-intake-checklist.md) as evidence to request from vendors.

Neither framework is HR-specific. Both are general-purpose AI governance frameworks this policy adapts to employment use cases.

---

## Cross-links

- [EU AI Act intake template](eu-ai-act-intake-template.md): per-use-case classification for EU high-risk obligations.
- [Vendor intake checklist](vendor-intake-checklist.md): evidence required from vendors before adoption.
- [Deployer checklist](deployer-checklist.md): ongoing obligations once an EU high-risk system is deployed.
- [Risk assessment template](risk-assessment-template.md): the intake process referenced above.
- [Designing HR agents](../07-agentic-patterns/agent-design.md): scope, escalation, and oversight design for agentic tools.

---

*This is a template document. Adapt it for your organization's specific legal jurisdiction, existing policies, and tool stack before publishing. Have Employment Counsel review before distribution.*
