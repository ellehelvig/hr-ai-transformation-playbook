# 11. Skills

> **11 / BUILD** · Package the playbook into repeatable, human-governed agent behaviors.

[← MCP tools](../10-mcp-agents/README.md) · [Playbook home](../README.md)

---

**For:** HR teams using an AI assistant such as Claude, at any stage of AI maturity. **Start with:** [hr-ai-readiness-assessment](hr-ai-readiness-assessment/SKILL.md) if you are new to AI in HR, or [hr-ai-use-case-intake](hr-ai-use-case-intake/SKILL.md) if you have an idea in hand.

Twenty-five installable agent skills in three sets. Two starter skills help a team new to AI find its stage and pick a safe first pilot. Six governance skills help you decide whether and how to use AI, in the order to adopt them. Seventeen HR function skills, listed further down, help you do the work in each part of HR with AI kept in its lane.

A skill is a folder with a `SKILL.md` file: instructions an AI agent loads when a task matches the skill's description. Install one and your assistant stops improvising and starts following this playbook's actual templates, checklists, and gates. The skills here don't call external services and don't make decisions. They structure the work so a human can make the decision faster, with the right evidence in front of them.

They run in Claude Code, Claude Cowork, and Claude.ai projects, and the format is plain markdown, so any agent framework that reads a system prompt can use them.

## Find your stage first

The library is useful at every stage of AI maturity, from a team that has never used AI to one running agents inside its HR systems. Stages follow the Level 0 to 5 scale in the [roadmap template](../06-roadmap/transformation-roadmap-template.md):

| Stage | Levels | How a skill runs |
|---|---|---|
| Start | 0 to 1 | No integrations. Paste de-identified inputs or a spreadsheet export into a chat with the skill loaded. A person checks every output. |
| Pilot | 2 | One read-only connector or scheduled export, a named owner, one success metric, and the audit trail filled on every run. |
| Scale | 3 | A connected agent with read-only tools, call logging, the skill's metrics tracked, and scheduled adverse impact checks where people are selected, scored or ranked. |
| Embed | 4 to 5 | The skill runs inside the workflow, triggered by a system event, still drafting for sign-off. Its test cases are rerun whenever the skill or the model changes. |

Decision rights never loosen as maturity rises. A higher stage changes how inputs arrive and how often a skill runs, never who decides. Every skill has a "By maturity stage" section that says how to run it at each stage and what must be true before moving up.

**New to AI in HR?** Two starter skills are built for Levels 0 to 2:

- [hr-ai-readiness-assessment](hr-ai-readiness-assessment/SKILL.md): scores the HR function, never a person, on seven readiness dimensions with evidence, places it on the scale at the lowest level the evidence supports, and drafts a 90-day plan that names which skills to start with.
- [hr-ai-first-use-case-picker](hr-ai-first-use-case-picker/SKILL.md): screens out first pilots that select, score or rank people, scores the rest with the [prioritization matrix](../01-use-cases/prioritization-matrix.md), and recommends one or two first pilots with a success metric and phase gate.

Where each skill fits. "Limited" means only part of the skill runs at that stage; its "By maturity stage" section says which part and what gate comes first.

| Skill | Start | Pilot | Scale | Embed |
|---|---|---|---|---|
| [hr-ai-readiness-assessment](hr-ai-readiness-assessment/SKILL.md) | Yes | Yes | Limited | Limited |
| [hr-ai-first-use-case-picker](hr-ai-first-use-case-picker/SKILL.md) | Yes | Yes | Limited | Limited |
| [hr-ai-use-case-intake](hr-ai-use-case-intake/SKILL.md) | Yes | Yes | Yes | Yes |
| [hr-prompt-picker](hr-prompt-picker/SKILL.md) | Yes | Yes | Yes | Limited |
| [hr-ai-vendor-review](hr-ai-vendor-review/SKILL.md) | Yes | Yes | Yes | Yes |
| [fairness-audit-prep](fairness-audit-prep/SKILL.md) | Yes | Yes | Limited | Limited |
| [eu-ai-act-hr-classifier](eu-ai-act-hr-classifier/SKILL.md) | Yes | Yes | Yes | Yes |
| [hr-ai-incident-triage](hr-ai-incident-triage/SKILL.md) | Yes | Yes | Yes | Yes |
| [function-hr-ai-governance](function-hr-ai-governance/SKILL.md) | Yes | Yes | Yes | Yes |
| [function-talent-acquisition](function-talent-acquisition/SKILL.md) | Yes | Yes | Limited | Limited |
| [function-onboarding](function-onboarding/SKILL.md) | Yes | Yes | Yes | Yes |
| [function-performance-management](function-performance-management/SKILL.md) | Yes | Yes | Yes | Limited |
| [function-learning-development](function-learning-development/SKILL.md) | Yes | Yes | Limited | Limited |
| [function-talent-review-succession](function-talent-review-succession/SKILL.md) | Yes | Yes | Limited | Limited |
| [function-total-rewards-compensation](function-total-rewards-compensation/SKILL.md) | Yes | Yes | Yes | Limited |
| [function-benefits](function-benefits/SKILL.md) | Yes | Yes | Yes | Yes |
| [function-hr-operations-hris](function-hr-operations-hris/SKILL.md) | Yes | Yes | Yes | Yes |
| [function-hr-compliance](function-hr-compliance/SKILL.md) | Yes | Yes | Yes | Yes |
| [function-employee-relations](function-employee-relations/SKILL.md) | Yes | Yes | Yes | Limited |
| [function-inclusion-belonging](function-inclusion-belonging/SKILL.md) | Yes | Yes | Yes | Limited |
| [function-employee-experience-engagement](function-employee-experience-engagement/SKILL.md) | Yes | Yes | Yes | Yes |
| [function-people-analytics](function-people-analytics/SKILL.md) | Yes | Yes | Yes | Limited |
| [function-workforce-planning-org-design](function-workforce-planning-org-design/SKILL.md) | Yes | Yes | Limited | Limited |
| [function-change-management](function-change-management/SKILL.md) | Yes | Yes | Yes | Yes |
| [function-offboarding](function-offboarding/SKILL.md) | Yes | Yes | Limited | Limited |

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
- **Three test cases** (`evals/`): a core request, an edge case, and a red-flag request the skill must refuse. They use the folder layout that `claude plugin eval` reads. All 57 cases, including the two starter skills', were run on 18 November 2026 with `claude-sonnet-5-5` and graded in a separate pass, and the skills were fixed where they failed. A trigger test checked that each skill loads for the right requests and not for near misses. See [the results](../09-evals/skill-eval-results-2026-11-18.md), including what one model and self-grading can and cannot show.

Where a skill selects, scores, or ranks people, it sends the adverse impact check to [fairness-audit-prep](fairness-audit-prep/SKILL.md), which now includes a tested calculator for selection rates, impact ratios, and a Fisher exact test from aggregate counts. `09-evals/test_skill_packages.py` checks in CI that every function and starter skill keeps these parts, and that every skill has a maturity stage section.

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
