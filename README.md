# HR AI Transformation Playbook

A practitioner's field guide for HR and People teams building responsible,
high-impact AI programs, from use case discovery through deployment and upskilling.

[![CI](https://github.com/ellehelvig/hr-ai-transformation-playbook/actions/workflows/ci.yml/badge.svg)](https://github.com/ellehelvig/hr-ai-transformation-playbook/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## Why this exists

Most HR AI guidance falls into one of two traps: too theoretical to act on,
or too vendor-specific to generalize. This playbook is neither. It is a working
toolkit, prompts that run, notebooks that execute, governance checklists that
hold up to legal review, and a use case library grounded in measurable business
outcomes.

---

## If you have 5 minutes

Start with the **[live ROI dashboard](https://ellehelvig.github.io/hr-ai-transformation-playbook/08-roi-measurement/dashboard.html)**, a working mock-up of the monthly reporting format with a payback calculator you can run with your own numbers.

Then, three things worth reading:

- **[Attrition risk model](05-notebooks/attrition-risk-modeling.ipynb)**, a working model with a fairness audit built in, not bolted on after the fact. Shows the calibration and disparate-impact analysis a real HR model needs before a score reaches a manager.
- **[HR agent eval framework](09-evals/README.md)**, 29 structured test cases with a real pass/fail [rubric](09-evals/eval-rubric.md), including adversarial and information-disclosure gates that block launch, not just quality scores.
- **[Agentic pattern decision tree](07-agentic-patterns/README.md)**, five architecture patterns for HR agents, with the governance requirement built into each one instead of treated as a separate compliance layer.

---

## What's inside

| Section | What you get |
|---|---|
| [01 · Use cases](01-use-cases/README.md) | Library of 30+ vetted HR AI use cases, prioritization matrix, intake template |
| [02 · Prompt library](02-prompt-library/README.md) | Production-ready prompts across talent acquisition, onboarding, performance, learning and development, HR operations, people analytics, succession planning, and internal mobility |
| [03 · Governance](03-governance/README.md) | [AI use policy](03-governance/ai-use-policy.md), [risk assessment template](03-governance/risk-assessment-template.md), [EU AI Act intake template](03-governance/eu-ai-act-intake-template.md), [vendor selection](03-governance/vendor-selection-framework.md), [vendor intake](03-governance/vendor-intake-checklist.md), [deployer checklist](03-governance/deployer-checklist.md), [incident report template](03-governance/incident-report-template.md), [pay equity governance](03-governance/pay-equity-governance.md) |
| [04 · Enablement](04-enablement/README.md) | HR AI literacy curriculum, workshop facilitator guide, adoption playbook |
| [05 · Notebooks](05-notebooks/README.md) | Skills gap analysis, a fairness-audited attrition risk model, and a working HR Q&A agent demo |
| [06 · Roadmap](06-roadmap/README.md) | 18-month transformation roadmap template, KPI framework, phase gate criteria |
| [07 · Agentic patterns](07-agentic-patterns/README.md) | Architecture patterns, agent design guide, testing and evaluation framework, [talent operating system architecture](07-agentic-patterns/talent-operating-system-architecture.md) |
| [08 · ROI measurement](08-roi-measurement/README.md) | Business case templates, ROI calculation framework, reporting cadence, [live dashboard demo](https://ellehelvig.github.io/hr-ai-transformation-playbook/08-roi-measurement/dashboard.html) |
| [09 · Evals](09-evals/README.md) | 29 structured test cases, eval rubric, and automated eval runner script |
| [10 · MCP agents](10-mcp-agents/README.md) | Four working HR agent tools (comp banding, bias-mitigated resume screening, recruiter intake calibration, governance policy Q&A) on one MCP server, real code with a 32-test pytest suite, not prompts-only |

---

## Quick start

**I want to identify the right AI use cases for my team**
→ [01 · Use cases / prioritization-matrix.md](01-use-cases/prioritization-matrix.md)

**I want prompts I can use today**
→ [02 · Prompt library](02-prompt-library/README.md)

**I need prompts for HR ops, people analytics, succession, or internal mobility**
→ [02 · Prompt library / hr-operations.md](02-prompt-library/hr-operations.md), [people-analytics.md](02-prompt-library/people-analytics.md), [succession-planning.md](02-prompt-library/succession-planning.md), [internal-mobility.md](02-prompt-library/internal-mobility.md)

**I need a governance framework**
→ [03 · Governance / ai-use-policy.md](03-governance/ai-use-policy.md)

**I need to handle the EU AI Act for HR**
→ [03 · Governance / eu-ai-act-intake-template.md](03-governance/eu-ai-act-intake-template.md)

**I need to upskill my HR team**
→ [04 · Enablement / hr-ai-literacy-curriculum.md](04-enablement/hr-ai-literacy-curriculum.md)

**I want to build workforce analytics**
→ [05 · Notebooks](05-notebooks/README.md)

**I need to build a business case**
→ [08 · ROI measurement](08-roi-measurement/README.md)

**I want to design and test HR agents**
→ [07 · Agentic patterns](07-agentic-patterns/README.md)

**I need to wire a skills ontology into my HRIS and performance process**
→ [07 · Agentic patterns / talent-operating-system-architecture.md](07-agentic-patterns/talent-operating-system-architecture.md)

**I want a working MCP server I can actually run, not just prompt docs**
→ [10 · MCP agents](10-mcp-agents/README.md)

---

## Design principles

**Outcome-first.** Every use case, prompt, and model is anchored to a
measurable HR or business outcome. No technology for its own sake.

**Governance built in.** Responsible AI considerations are embedded in every
section, not bolted on at the end, structured around the NIST AI Risk
Management Framework 1.0 and ISO/IEC 42001, with federal and state
regulatory context kept current (see [governance](03-governance/README.md)).

**HRIS-agnostic.** Nothing here assumes a specific vendor. Integration patterns
are documented as adapters you wire to your own stack.

**Humans in the loop.** This playbook treats AI as a force multiplier for HR
professionals, not a replacement. Every automated workflow has a defined
escalation path to a human.

---

## The three non-negotiables

Regardless of which use cases you pursue:

1. **Humans make consequential employment decisions.** AI may inform, not decide.
2. **Employees have a right to know** when AI influences processes that affect them.
3. **Fairness audits** are required on any use case that scores or ranks employees
or candidates.

---

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

MIT — use freely, adapt for your organization, share improvements back.

> None of this is legal advice. All governance documents should be reviewed
> by Legal and Privacy before adoption.

---

Built by Elle Helvig · [LinkedIn](https://www.linkedin.com/in/ellehelvig/)
