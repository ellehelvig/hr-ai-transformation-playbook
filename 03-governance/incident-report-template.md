# AI incident report and postmortem template

Use this when an HR AI system does something it shouldn't have: a wrong policy citation, a disclosure it shouldn't have made, a biased or incorrectly escalated output, an unauthorized action, or anything an employee or manager flags as wrong. Fill out Part 1 immediately. Fill out Part 2 within the timeline set by your severity rating.

Not legal advice. Severity 1–2 incidents should involve Legal and Privacy before any external communication.

---

## Part 1: Incident report (fill out immediately, within hours)

**Date/time detected:**
**Reported by:**
**System or use case involved:** (link to its entry in the [use case library](../01-use-cases/use-case-library.md) or risk assessment)
**Detected via:** (employee report / HRBP spot-check / automated monitoring / eval regression / other)

**What happened.** Facts only, no blame, no speculation about cause yet:

**Who was affected, and how many:**

**Immediate action taken:** (paused the system / disabled a feature / no action yet, still assessing)

**Notification status:**
- [ ] Affected employee(s) informed
- [ ] Manager/HRBP informed
- [ ] Vendor notified (if third-party system)
- [ ] Legal/Privacy notified
- [ ] Regulatory notification assessed (see [deployer checklist §10](deployer-checklist.md) and [vendor checklist §8](vendor-intake-checklist.md))

---

## Severity scale

| Severity | Definition | Postmortem due |
|---|---|---|
| **Sev 1** | Disclosed sensitive personal data, made or influenced an unreviewed employment decision, or a systemic bias/fairness failure | 24 hours, Legal + Privacy + HR Leadership involved from detection |
| **Sev 2** | Incorrect information given on a consequential topic (leave, pay, legal rights), or a single employee harmed | 3 business days |
| **Sev 3** | Incorrect but low-stakes information, tone failure, or a near-miss caught before reaching an employee | 5 business days |
| **Sev 4** | Minor, no employee impact, caught in routine monitoring | Log only, no formal postmortem required |

A score of 1 on the [eval rubric's](../09-evals/eval-rubric.md) information safety dimension is automatically Sev 1.

---

## Part 2: Postmortem

**Timeline of events.** From first occurrence to resolution, with timestamps:

**Root cause.** Not "the AI made a mistake." Which layer failed? Cross-reference the failure patterns in [testing-and-evaluation.md](../07-agentic-patterns/testing-and-evaluation.md):

- [ ] System prompt / scope definition
- [ ] Knowledge base (stale, missing, or wrong content)
- [ ] Tool design or tool output parsing
- [ ] Escalation trigger too narrow or too broad
- [ ] Model version change
- [ ] Human review gate skipped or rubber-stamped
- [ ] Other:

**What worked.** How was this caught? What part of detection or response worked as designed?

**What didn't.** Where did the process fail or lag?

**Fix implemented:**

**Regression coverage added.** New case(s) added to the eval set per the [eval framework](../09-evals/README.md) so this exact failure is caught before it recurs:

**Corrective actions:**

| Action | Owner | Due date | Status |
|---|---|---|---|
| | | | |

---

## Part 3: Communication

**Internal.** Follow the four steps in [handling the first public failure](../04-enablement/adoption-playbook.md#handling-the-first-public-failure): acknowledge specifically and quickly, explain what went wrong in plain language, fix the actual gap, say what changed. Do not restrict the whole program over an isolated failure.

**Employee-facing** (if the incident directly affected one or more employees):

**Regulatory** (if applicable, assess against AI Act Article 73, GDPR breach notification, and any state-law incident definitions in your [risk assessment](risk-assessment-template.md)):

---

## Worked example

**What happened:** The new hire Q&A agent told an employee they had unlimited PTO carryover into the next calendar year. The actual policy caps carryover at 5 days. Employee flagged it after checking with their HRBP.

**Severity:** Sev 2 (incorrect information on a consequential topic, single employee, caught before financial harm).

**Root cause:** Knowledge base gap. The PTO policy document in the RAG store was the prior year's version; the carryover cap was added in a policy update that hadn't been re-indexed.

**Fix:** Re-indexed the policy store, added a monthly freshness check owned by HR Ops (see [Pattern 3 governance requirement](../07-agentic-patterns/agent-design.md)).

**Regression coverage:** Added eval case checking PTO carryover cap citation against the current policy version.

**Corrective action:** Knowledge base owner now gets an automated alert on any policy doc change; re-index SLA set at 48 hours. Owner: HR Ops lead. Closed within 5 business days.

---

## Cross-links

- [AI use policy](ai-use-policy.md): the reporting-concerns process this template feeds.
- [Deployer checklist](deployer-checklist.md): regulatory reporting obligations for high-risk EU systems.
- [Testing and evaluation](../07-agentic-patterns/testing-and-evaluation.md): failure pattern diagnosis and the signal loop this template plugs into.
- [Eval framework](../09-evals/README.md): where regression coverage for a fixed incident belongs.
- [Adoption playbook](../04-enablement/adoption-playbook.md): the trust-and-communication side of handling a failure.
