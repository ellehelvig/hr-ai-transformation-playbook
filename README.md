# HR AI Transformation Playbook

A working toolkit for HR and People teams putting AI into production responsibly: use cases, prompts, governance that survives legal review, executable notebooks, a tested MCP server, and installable agent skills.

[![CI](https://github.com/ellehelvig/hr-ai-transformation-playbook/actions/workflows/ci.yml/badge.svg)](https://github.com/ellehelvig/hr-ai-transformation-playbook/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)
[![Regulatory content verified weekly](https://img.shields.io/badge/regulatory%20content-verified%20weekly-blue.svg)](CHANGELOG.md)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## What makes this different

Most HR AI guidance is either too abstract to act on or too tied to one vendor to reuse. This repo is neither, and you can check that claim against the repo itself:

- **It runs.** Three notebooks execute in CI on every push. Four MCP tools ship with a 32-test suite. The 29-case eval runner exits non-zero when a refusal or escalation gate fails, so it can block a deploy, and its scorer has tests of its own.
- **Governance is verified, not vibes.** Every regulatory claim cites a primary source and is re-checked weekly against the statute, regulator page, or court docket. When something changes (the EU AI Omnibus, Colorado's rewrite, Illinois penalties), the docs change within days and the [changelog](CHANGELOG.md) says what moved.
- **Humans stay in the loop by construction.** The MCP tools have `human_review_required: true` with no code path that turns it off, and the resume screener's schema is tested to guarantee it can never emit a score.
- **It's vendor-agnostic.** Nothing assumes a specific HRIS, ATS, or model provider.

---

## Start here, by role

**HR leader deciding where to begin**
→ [Prioritization matrix](01-use-cases/prioritization-matrix.md), then the [18-month roadmap](06-roadmap/transformation-roadmap-template.md)

**HR professional who wants something useful today**
→ Install the [hr-prompt-picker](11-skills/hr-prompt-picker/SKILL.md) skill, or go straight to the [prompt library](02-prompt-library/README.md)

**Legal, Privacy, or Compliance partner**
→ [Governance suite](03-governance/README.md): start with the [AI use policy](03-governance/ai-use-policy.md) and the [one-page pre-screen](03-governance/quick-reference-checklist.md)

**Operating in the EU**
→ [EU AI Act intake template](03-governance/eu-ai-act-intake-template.md) and [deployer checklist](03-governance/deployer-checklist.md). Annex III employment obligations apply from 2 December 2027; GDPR Article 22 applies now.

**People analytics or data science**
→ [Attrition risk model with fairness audit](05-notebooks/attrition-risk-modeling.ipynb), then [fairness-audit-prep](11-skills/fairness-audit-prep/SKILL.md)

**Engineer building HR agents**
→ [Agentic pattern decision tree](07-agentic-patterns/README.md), the [MCP server](10-mcp-agents/README.md), and the [evals](09-evals/README.md)

**Procurement or vendor management**
→ [Vendor selection framework](03-governance/vendor-selection-framework.md), [vendor intake checklist](03-governance/vendor-intake-checklist.md), and the [hr-ai-vendor-review](11-skills/hr-ai-vendor-review/SKILL.md) skill

**Five minutes and a skeptical CFO**
→ The [live ROI dashboard](https://ellehelvig.github.io/hr-ai-transformation-playbook/08-roi-measurement/dashboard.html), a payback calculator you can run with your own numbers

---

## Skills HR should install first

New in 2.0: six agent skills that make an AI assistant follow this playbook's templates instead of improvising. Ranked by risk removed per hour of setup.

| # | Skill | One line |
|---|---|---|
| 1 | [hr-ai-use-case-intake](11-skills/hr-ai-use-case-intake/SKILL.md) | Idea in, completed intake card + prioritization score + risk tier out |
| 2 | [hr-prompt-picker](11-skills/hr-prompt-picker/SKILL.md) | Right prompt from the library, adapted, with verify-before-use attached |
| 3 | [hr-ai-vendor-review](11-skills/hr-ai-vendor-review/SKILL.md) | Vendor docs in, gap list + red flags + follow-up email out |
| 4 | [fairness-audit-prep](11-skills/fairness-audit-prep/SKILL.md) | Disparate impact test plan and monitoring template for anything that scores people |
| 5 | [eu-ai-act-hr-classifier](11-skills/eu-ai-act-hr-classifier/SKILL.md) | The 11-field Annex III card with Article 6(3) reasoning counsel can argue with |
| 6 | [hr-ai-incident-triage](11-skills/hr-ai-incident-triage/SKILL.md) | First-hour incident report, severity, containment, routing |

The [skills README](11-skills/README.md) also has a human capability ladder: the practitioner skill each agent skill depends on, and where in the curriculum to build it.

---

## What's inside

| Section | What you get |
|---|---|
| [01 · Use cases](01-use-cases/README.md) | 30+ vetted HR AI use cases with resources column, prioritization matrix, intake template with worked example |
| [02 · Prompt library](02-prompt-library/README.md) | Tested prompts with tuning notes across talent acquisition, onboarding, performance, L&D, HR operations, people analytics, succession, internal mobility |
| [03 · Governance](03-governance/README.md) | AI use policy, risk assessment, EU AI Act intake, vendor selection and intake, deployer checklist, incident report, pay equity governance, one-page pre-screen |
| [04 · Enablement](04-enablement/README.md) | 4-module literacy curriculum (with slides and PDF), facilitator guide, 90-day adoption playbook |
| [05 · Notebooks](05-notebooks/README.md) | Skills gap analysis, fairness-audited attrition model, HR Q&A agent demo. All synthetic data, all executed in CI |
| [06 · Roadmap](06-roadmap/README.md) | 18-month transformation roadmap, KPI framework, phase gates |
| [07 · Agentic patterns](07-agentic-patterns/README.md) | Five architecture patterns with governance built in, agent design guide, testing framework, talent operating system architecture |
| [08 · ROI measurement](08-roi-measurement/README.md) | Business case template, ROI framework, reporting cadence, live dashboard |
| [09 · Evals](09-evals/README.md) | 29 test cases, rubric with launch-blocking gates, automated runner |
| [10 · MCP agents](10-mcp-agents/README.md) | Four working tools on one MCP server: comp banding, bias-mitigated screening, recruiter intake, policy Q&A. 32 passing tests |
| [11 · Skills](11-skills/README.md) | Six installable agent skills, ranked adoption order, human capability ladder |

---

## The three non-negotiables

Whatever you build:

1. **Humans make consequential employment decisions.** AI informs; it does not decide.
2. **Employees have a right to know** when AI influences a process that affects them.
3. **Fairness audits are required** on anything that scores or ranks employees or candidates.

Every template, prompt, tool, and skill here is built to hold those lines. If you find one that doesn't, [open an issue](https://github.com/ellehelvig/hr-ai-transformation-playbook/issues/new/choose).

---

## Regulatory coverage and currency

Covers the EU (AI Act, GDPR Article 22), the US (Title VII, NYC Local Law 144, Illinois, Colorado, California, Texas), the UK (Data (Use and Access) Act 2025), and Canada (Ontario disclosure rule). Does not cover APAC, Latin America, the Middle East, or Africa; get local counsel there.

Claims are dated in the docs and verified weekly against primary sources. Material changes land in [CHANGELOG.md](CHANGELOG.md). If you spot something stale, use the [regulatory update issue template](https://github.com/ellehelvig/hr-ai-transformation-playbook/issues/new?template=regulatory-update.md) with a citation.

None of this is legal advice. Every governance document should be reviewed by Legal and Privacy before adoption.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Practitioner contributions with real-world tuning notes are the most valuable thing you can send.

## License

MIT. Use it, adapt it for your organization, send improvements back.

## Citation

If this playbook informs your work, cite it via [CITATION.cff](CITATION.cff) or link the repo.

---

Built and maintained by Elle Helvig · [LinkedIn](https://www.linkedin.com/in/ellehelvig/)
