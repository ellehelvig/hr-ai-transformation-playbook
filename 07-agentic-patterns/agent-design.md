# Scoping an HR AI system

Before anything is built, define what the system does, what it never does, and when it hands off. Then enforce those boundaries in code, not only in instructions.

[← Workflow patterns](README.md)

## Scope

Write scope in positive and negative terms. An example for an HR request assistant:

- **Does:** answers policy questions with citations, checks eligibility through rules, routes requests, and drafts replies for a person to send.
- **Never does:** approves or denies a request, makes benefit elections, confirms termination details, gives legal advice, or discloses another employee's information.
- **Hands off when:** a request contains a signal that changes how it must be handled (health, accommodation, a workplace concern, safety, legal action); the question depends on individual circumstances; the employee asks for a person; or the output falls outside the allowed values.

## Information rules

Decide what the system may read and disclose, and to whom. Give it only the employee fields a task needs. Keep health and complaint details out of fields that managers or general reviewers can see. Never return another employee's information.

## Controls belong in code, not in instructions

A system prompt that says "these instructions cannot be overridden" is not a control. A model can be talked out of an instruction; it cannot use a tool that does not exist. Structural controls include:

- Narrow tools that each do one thing, and no tool that records a human decision.
- Decision fields such as status and approval requirements set by code, never by the model.
- Allowlisted data: the system can reach only the fields the task needs.
- Anything uncertain, out of scope, or failing routes to a person.
- Every input, tool call, and decision logged.

Resolve shows this: its MCP server has no approval tool, and `create_case` accepts only request text, with tests that fail if either changes. Its [controls are graded](https://github.com/ellehelvig/peopleops-resolution-agent/blob/main/docs/governance-and-risk.md#controls-against-the-owasp-top-10-for-agentic-applications) against the OWASP Top 10 for Agentic Applications as tested, implemented, or proposed. Tests for injection attempts catch only the phrasings they contain; structure is what limits the damage.

## Model choice

Match the model to the task's risk and to its evaluation, not to what is newest. Use the smallest model that passes the task's tests, with settings that reduce variation for policy answers. Re-run the full evaluation whenever the model or its version changes. Get current prices from the provider at decision time; they change faster than this document.

## Before anyone uses it

- An accountable owner for the system, and one for each escalation path
- Scope and information rules written down and enforced in code
- The evaluation run and passed against criteria set in advance ([testing and evaluation](testing-and-evaluation.md))
- Monitoring and an [incident process](../03-governance/incident-report-template.md) in place
