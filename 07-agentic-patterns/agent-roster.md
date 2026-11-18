# HR agent roster

Before an AI system does HR work, give it what a new hire gets: a manager, a written scope, access limited to the job, a check before day one, regular reviews, and a clean exit. The roster keeps one row per system so the People team can see what is running, who owns it, and what it is allowed to do.

[← Workflow patterns](README.md)

## Why HR should own the roster

People teams already run a lifecycle for every role: request, job description, hiring manager, access, onboarding checks, performance reviews, and offboarding. AI systems that do People work need the same steps, and the gaps look the same. A system with no owner is like a contractor with no manager. A system that still has access after its project ended is like a former employee with a working badge.

| People lifecycle step | Equivalent for an AI system | Where this playbook covers it |
|---|---|---|
| Headcount request | Use case and business case | [Intake template](../01-use-cases/intake-template.md) |
| Job description | Scope: what it does, never does, and when it hands off | [Scoping an HR AI system](agent-design.md) |
| Hiring manager | One accountable owner, by role | This page |
| Access provisioning | Only the data fields and tools the task needs | [Information rules](agent-design.md#information-rules) |
| Pre-start checks | Evaluation passed against criteria set in advance | [Evals](../09-evals/README.md) |
| Performance review | Re-run evaluation on any model, scope, or data change, plus sampled review | [Testing and evaluation](testing-and-evaluation.md) |
| Employee relations case | Incident report | [Incident report template](../03-governance/incident-report-template.md) |
| Offboarding | Retire: remove access, keep logs for the retention period, tell the people who used it | This page |

## What each row records

Copy [agent-roster.yaml](agent-roster.yaml) and keep one entry per system. A row with any required field blank is not ready to run.

| Field | What to write | Required |
|---|---|---|
| Name | What people call it | Yes |
| Owner | The role accountable for its output, not the team that built it | Yes |
| Purpose | The one task it exists for, in one sentence | Yes |
| Pattern | Which [workflow pattern](README.md) it follows, or rules only | Yes |
| Model | Model and version, or "none" if it runs on rules | Yes |
| Reads | The data it can reach. Name fields, not systems | Yes |
| Can do | Its tools or outputs | Yes |
| Never does | The actions it has no way to take | Yes |
| Hands off when | The triggers that send work to a person | Yes |
| Human checkpoint | Who reviews its output before anything changes for an employee or candidate | Yes |
| Evidence | Tests or evaluations it passed, and when | Yes |
| Logging | What each call records, and where | Yes |
| How to stop it | Who can switch it off, and how | Yes |
| Status | Proposed, pilot, live, paused, or retired | Yes |
| Next review | A date | Yes |
| Known gaps | What is not yet in place | If any |

## Rules

- **No owner, no system.** If the owner leaves or changes roles, the system pauses until a new owner accepts it.
- **Review on change, not only on schedule.** A new model or model version, a new data source, a wider scope, a new user group, or an incident each triggers a review before the change goes live. Otherwise review at least once a quarter.
- **Write down the gaps.** A row that says "not yet in place" is more useful than a row that implies a control exists.
- **Retire on purpose.** When a system is replaced or its pilot ends, remove its access, keep its logs for the retention period your policy sets, and tell the people who relied on it what replaces it.
- **The roster records decisions. It does not make them.** Whether a system may run is the owner's call, with the approvals your [AI use policy](../03-governance/ai-use-policy.md) requires.

## Example: this repository's own tools

[agent-roster.yaml](agent-roster.yaml) fills in the roster for the four [MCP tool packages](../10-mcp-agents/README.md) in this repository. The owners are example roles, since one maintainer runs this repository. Three things stand out when the rows are filled in honestly:

- **None of the four tools uses a model.** Each runs on rules, so its own row says "none". Any model that calls these tools needs its own row, with its own evidence.
- **Logging and a way to stop them are not built.** [Adoption monitoring](../10-mcp-agents/ADOPTION-MONITORING.md) describes what each call should log. The tools do not log yet, so those fields say "not yet in place".
- **Every row is a demonstration.** The tools run on synthetic data, so the status is "proposed", not "live".

## What this page does not do

- It does not replace a legal or risk review. Some systems in hiring and employment need specific notices, assessments, or records under law. Check the [Key dates for HR table](../03-governance/README.md) and talk to counsel.
- It does not track vendor products in detail. Use the [vendor intake checklist](../03-governance/vendor-intake-checklist.md) for those, then give each one a roster row.
