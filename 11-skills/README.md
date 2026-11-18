# 11. Skills

> **11 / BUILD** · Package the playbook into repeatable, human-governed agent behaviors.

[← MCP tools](../10-mcp-agents/README.md) · [Playbook home](../README.md)

---

**For:** HR teams using an AI assistant such as Claude. **Start with:** [hr-ai-use-case-intake](hr-ai-use-case-intake/SKILL.md).

Two sets of installable agent skills. Six governance skills help you decide whether and how to use AI, in the order to adopt them. Seventeen HR function skills, listed further down, help you do the work in each part of HR with AI kept in its lane.

A skill is a folder with a `SKILL.md` file: instructions an AI agent loads when a task matches the skill's description. Install one and your assistant stops improvising and starts following this playbook's actual templates, checklists, and gates. The skills here don't call external services and don't make decisions. They structure the work so a human can make the decision faster, with the right evidence in front of them.

They run in Claude Code, Claude Cowork, and Claude.ai projects, and the format is plain markdown, so any agent framework that reads a system prompt can use them.

## Install these first

Ranked by how much risk each one removes per hour of setup. Start at the top.

| # | Skill | What it does | Why this order |
|---|---|---|---|
| 1 | [hr-ai-use-case-intake](hr-ai-use-case-intake/SKILL.md) | Turns a rough idea into a completed intake card, prioritization score, and risk tier | Every other skill assumes you know what you're building and how risky it is. This is the front door. |
| 2 | [hr-prompt-picker](hr-prompt-picker/SKILL.md) | Picks the right prompt from the library for a task, adapts it, and enforces verify-before-use | Highest daily usage, lowest risk. Gets the team practicing with guardrails before anything touches a decision. |
| 3 | [hr-ai-vendor-review](hr-ai-vendor-review/SKILL.md) | Runs a vendor's documentation against the pre-screen and intake checklist, outputs a gap list | Most HR AI arrives through procurement, not engineering. This is where bad tools get stopped. |
| 4 | [fairness-audit-prep](fairness-audit-prep/SKILL.md) | Sets up the disparate impact test plan and monitoring template for anything that scores or ranks people | Required by the playbook's third non-negotiable. Do it before go-live, not after a complaint. |
| 5 | [eu-ai-act-hr-classifier](eu-ai-act-hr-classifier/SKILL.md) | Produces the 11-field EU AI Act card with Annex III hook, Article 6(3) analysis, and GDPR Article 22 touchpoint | Only matters if you touch EU workers or candidates, but if you do, December 2027 is closer than it sounds. |
| 6 | [hr-ai-incident-triage](hr-ai-incident-triage/SKILL.md) | Fills the incident report, assigns severity, and routes to the right owner | You hope to never use it. Install it before you need it so the first incident is handled well. |

## HR function skills

One skill for each part of HR. Each one is built to be run by an agent, not just read:

- **Inputs and tools.** A table of required inputs and where each comes from, and which systems the agent may read through a connector, read-only, with the fields named.
- **Decision rights.** Every action the function involves is marked Does alone, Drafts for sign-off (with the named owner), or Refuses and routes (with where it goes).
- **Regulation map.** The rules that touch the function, each pointing to its row in the Key dates for HR table rather than restating dates.
- **Metrics.** Two or three measures a CHRO would track, defined precisely enough to compute.
- **Output template with an audit trail.** Inputs used, tools called and fields read, items awaiting sign-off, open legal questions.
- **A worked example** (`EXAMPLE.md`) on a fictional company with synthetic data.
- **Three test cases** (`evals/`): a core request, an edge case, and a red-flag request the skill must refuse. They use the folder layout that `claude plugin eval` reads, so they can be run with and without the skill. They are written, not yet run against a model.

Where a skill selects, scores, or ranks people, it sends the adverse impact check to [fairness-audit-prep](fairness-audit-prep/SKILL.md), which now includes a tested calculator for selection rates, impact ratios, and a Fisher exact test from aggregate counts. `09-evals/test_skill_packages.py` checks in CI that every function skill keeps these parts.

| Area | Skill | Use it for |
|---|---|---|
| Hiring and entry | [function-talent-acquisition](function-talent-acquisition/SKILL.md) | Intake, job descriptions, sourcing, structured interviews, screening risks, offers |
| Hiring and entry | [function-onboarding](function-onboarding/SKILL.md) | Preboarding, first week, 30/60/90 plans, I-9 and new hire paperwork |
| Growth | [function-performance-management](function-performance-management/SKILL.md) | Goals, check-ins, review drafts, calibration prep, improvement plans |
| Growth | [function-learning-development](function-learning-development/SKILL.md) | Needs analysis, skills-based programs, AI literacy, evaluation |
| Growth | [function-talent-review-succession](function-talent-review-succession/SKILL.md) | Talent reviews, succession, internal mobility, career paths |
| Rewards | [function-total-rewards-compensation](function-total-rewards-compensation/SKILL.md) | Job architecture, bands, market pricing, merit guides, posting ranges |
| Rewards | [function-benefits](function-benefits/SKILL.md) | Plan review, open enrollment, leave, COBRA and ERISA calendars, vendors |
| Operations | [function-hr-operations-hris](function-hr-operations-hris/SKILL.md) | Tiered service, case triage, knowledge base, data quality, HR tech |
| Operations | [function-hr-compliance](function-hr-compliance/SKILL.md) | Compliance calendar, postings, recordkeeping, handbook checks, audits |
| Workplace | [function-employee-relations](function-employee-relations/SKILL.md) | Intake, investigation plans, neutral evidence summaries, retaliation checks |
| Workplace | [function-inclusion-belonging](function-inclusion-belonging/SKILL.md) | Programs open to all, job-related criteria, accommodation path, process audits |
| Workplace | [function-employee-experience-engagement](function-employee-experience-engagement/SKILL.md) | Listening strategy, surveys, comment analysis within privacy limits, action plans |
| Strategy | [function-people-analytics](function-people-analytics/SKILL.md) | Question framing, metric definitions, suppression, model fairness checks |
| Strategy | [function-workforce-planning-org-design](function-workforce-planning-org-design/SKILL.md) | Demand and supply, scenarios, build, buy, borrow or bot, spans and layers |
| Strategy | [function-change-management](function-change-management/SKILL.md) | Impact assessment, sponsors, communication plans, adoption measures |
| Exit | [function-offboarding](function-offboarding/SKILL.md) | Exits and layoffs: final pay, notices, access removal, knowledge transfer |
| Governance | [function-hr-ai-governance](function-hr-ai-governance/SKILL.md) | Charter, roles, AI inventory, review cadence, routing to the six skills above |

Every function skill follows the same guardrails as the governance skills, listed below. Where a legal duty depends on jurisdiction, the skill points to the Key dates for HR table in [governance](../03-governance/README.md) and to counsel rather than restating dates.

## Install

Copy a skill folder into wherever your agent loads skills from.

```bash
# Claude Code (project scope)
cp -r 11-skills/hr-ai-use-case-intake .claude/skills/

# Claude Code (user scope, every project)
cp -r 11-skills/hr-ai-use-case-intake ~/.claude/skills/

# Several at once, for example every HR function skill
cp -r 11-skills/function-* .claude/skills/

# Cowork or Claude.ai: upload the folder in Settings > Skills, or paste SKILL.md into a project's instructions
```

Each skill references files in this repo by relative path (`03-governance/...`). If you install a skill outside a clone of this repo, either keep the referenced templates alongside it or update the paths. The skill will tell you which files it needs at the top.

## Human capability ladder

Skills don't replace practitioner judgment; they depend on it. This is the order to build the human side, with the module that teaches each rung and the skill that puts it to work.

| Rung | Practitioner skill | Learn it in | Then use |
|---|---|---|---|
| 1 | Write a specific prompt and verify the output before relying on it | [Literacy curriculum, Module 2](../04-enablement/hr-ai-literacy-curriculum.md#module-2-using-ai-in-your-daily-hr-work) | hr-prompt-picker |
| 2 | Describe a use case in terms of the decision it touches and the metric it moves | [Use case intake template](../01-use-cases/intake-template.md), [prioritization matrix](../01-use-cases/prioritization-matrix.md) | hr-ai-use-case-intake |
| 3 | Read a vendor's technical documentation and know what's missing | [Vendor selection framework](../03-governance/vendor-selection-framework.md), [vendor intake checklist](../03-governance/vendor-intake-checklist.md) | hr-ai-vendor-review |
| 4 | Run and interpret a four-fifths rule check and a calibration plot | [Attrition risk notebook](../05-notebooks/attrition-risk-modeling.ipynb), [Literacy curriculum, Module 3](../04-enablement/hr-ai-literacy-curriculum.md#module-3-governance-ethics-and-responsible-use) | fairness-audit-prep |
| 5 | Classify a system under Annex III and explain the Article 6(3) exemption test | [EU AI Act intake template](../03-governance/eu-ai-act-intake-template.md), [deployer checklist](../03-governance/deployer-checklist.md) | eu-ai-act-hr-classifier |
| 6 | Run a blameless postmortem and separate root cause from symptom | [Incident report template](../03-governance/incident-report-template.md) | hr-ai-incident-triage |

Someone at rung 2 can use skill 1 well. Someone at rung 0 will get a polished-looking intake card they can't defend in a governance review. Build the rung, then install the skill.

## Guardrails every skill shares

- No skill makes an employment decision, assigns a score to a person, or writes to an HR system.
- Every skill ends by naming the human who owns the next step.
- Every skill refuses real employee or candidate data in examples and says so.
- Every skill flags when the answer depends on jurisdiction and points to the governance doc rather than guessing.

## Writing your own

Copy the structure of any skill here: frontmatter with `name` and `description`, a "Files this skill needs" block, numbered steps, an output format, and a "What this skill will not do" section. Test it against a scenario the playbook already covers so you can compare against the expected result. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Cross-links

- [10 · MCP tools](../10-mcp-agents/README.md): the tools these skills can call when they need deterministic, tested logic (comp banding, policy Q&A)
- [09 · Evals](../09-evals/README.md): how to test a skill's outputs before rolling it out to a team
- [03 · Governance](../03-governance/README.md): the source documents every skill points back to
