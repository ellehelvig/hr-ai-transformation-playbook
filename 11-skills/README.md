# 11. Skills

Six installable agent skills for HR teams, in the order to adopt them.

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

## Install

Copy a skill folder into wherever your agent loads skills from.

```bash
# Claude Code (project scope)
cp -r 11-skills/hr-ai-use-case-intake .claude/skills/

# Claude Code (user scope, every project)
cp -r 11-skills/hr-ai-use-case-intake ~/.claude/skills/

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

- [10 · MCP agents](../10-mcp-agents/README.md): the tools these skills can call when they need deterministic, tested logic (comp banding, policy Q&A)
- [09 · Evals](../09-evals/README.md): how to test a skill's outputs before rolling it out to a team
- [03 · Governance](../03-governance/README.md): the source documents every skill points back to
