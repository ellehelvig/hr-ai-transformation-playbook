# Compensation and pay equity AI governance

**Status:** Do not adopt as written. Requires employment counsel review before any use.
**Legal review required before publishing:** Yes, employment counsel specifically, not general Legal or Privacy.
**Last reviewed:** August 2026. Pay transparency and privilege law changes by jurisdiction and by year, confirm current status before relying on anything below.

> This is the highest legal-exposure document in this playbook. Everything here is general, research-grounded orientation, not a substitute for advice from a lawyer who knows your jurisdictions, your data, and your litigation history. The privilege and affirmative-defense mechanics described below are jurisdiction-specific, change over time, and often only work if structured correctly before an analysis begins. Getting this wrong doesn't just mean an outdated document, it can mean a comp disparity finding becomes discoverable evidence against your organization. Do not treat any part of this file as cleared for use until employment counsel has reviewed it.

Compensation is the single highest-exposure use case in the [use case library](../01-use-cases/use-case-library.md). This document exists because that library flags "legal exposure if mishandled" on pay equity analysis, and nothing else in this playbook said what to do about it. Read this before running any AI tool, prompt, or model against compensation data, and read the warning above again after you do.

---

## Why comp is different from other HR AI use cases

Every other use case in this playbook creates risk if it goes wrong. Comp AI creates risk just by existing, in two ways other use cases don't:

1. **The analysis itself can become evidence.** A pay equity analysis that finds a disparity is discoverable in litigation unless it was structured to be privileged from the start. Running an AI tool over comp data without counsel involvement can create a permanent, discoverable record of a disparity your organization then failed to fix.

2. **Historical compensation data can carry past discrimination.** A model trained on or benchmarked against past pay decisions may reproduce or amplify that bias. This is a risk to test, not an inevitable outcome of every model. Examine labels, proxy features, group errors, and reviewer behavior. A suggested pay figure may also anchor human judgment; a review requirement alone does not demonstrate that bias has been corrected. See the [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework).

---

## The privilege question

**Common misconception:** that a "pay equity audit" is automatically privileged or confidential. It generally is not.

- **Self-critical analysis privilege** exists in a limited form in some jurisdictions but is not universally recognized and is frequently rejected by federal courts. Do not rely on it as your primary protection.
- **Attorney-client privilege and work product protection** are the more reliable path, but only if outside or employment counsel directs the analysis from the start: counsel engages the analyst (internal or vendor), frames the legal question, and controls the findings. An AI-assisted pay analysis run by HR or People Analytics on their own initiative, with counsel looped in only if something looks bad, will generally not be privileged.
- **Massachusetts and Oregon** are examples of states that give a good-faith self-evaluation an affirmative defense under their equal pay statutes (not the same thing as privilege, but a real protection if you can show the evaluation was genuine and progress was made). Check your specific state; this is not uniform.

**What this means operationally:** any AI-assisted compensation or pay equity analysis that could surface a disparity must be initiated under attorney direction, not run first and shown to counsel after. Design the governance gate (below) around this, not around the standard risk assessment process.

---

## Jurisdiction by jurisdiction (verify before relying on this)

**US state pay transparency laws.** Before using AI to draft a posting, have counsel map the actual duties for each jurisdiction the posting reaches. Distinguish salary-range disclosure in advertisements from disclosure on request, salary-history restrictions, and protections for discussing pay. Record employer thresholds, geographic and remote-work scope, required benefits information, and effective dates with a current statute or regulator link. Do not use an undifferentiated state count as a compliance checklist. Apply the resulting requirements to the [talent acquisition prompt library](../02-prompt-library/talent-acquisition.md).

**California SB 1162 pay data reporting, amended by SB 464.** Employers with 100+ employees (including labor-contracted workers) must file an annual pay data report; the deadline moved to the second Wednesday of May. Reports must be filed per establishment, not consolidated. SB 464 (not SB 1162 itself) adds mandatory civil penalties and requires separating demographic data from personnel files, both effective January 1, 2026. Starting with the 2026 reporting cycle (due May 2027), SB 464 requires classifying workers using the 23-category SOC system instead of the 10 EEO-1 categories, a significant reclassification effort if you're using AI to help map job titles to categories.

**EU Pay Transparency Directive (2023/970).** Article 34 set a [7 June 2026 transposition deadline](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023L0970). Confirm each member state's implementing law, employer coverage, and phased duties before applying it to a specific organization. Missing transposition does not automatically make every provision directly enforceable against a private employer. Direct effect of a directive is conditional and generally vertical, against the state or a qualifying public body, rather than horizontal against another private party. Ask local counsel to assess the relevant provision and employer. See the [EU explanation of direct effect](https://eur-lex.europa.eu/EN/legal-content/summary/the-direct-effect-of-european-union-law.html).

**This list is not exhaustive.** Confirm current requirements for every jurisdiction where you have employees before deploying any comp-related AI use case.

---

## Approved and prohibited AI use in compensation

This extends the [AI use policy's](ai-use-policy.md) approved tool categories with comp-specific rules.

| Use | Status | Conditions |
|---|---|---|
| Market benchmarking data synthesis (aggregate, no individual employee data) | Approved | Standard vendor DPA; no individual-level output |
| Compensation band/range drafting assistance | Approved with conditions | Human comp professional finalizes; verify against current state disclosure law before posting |
| Explaining an existing comp decision in plain language to an employee | Approved with conditions | Must be grounded in the actual decision rationale, not generated to sound plausible |
| Pay equity or disparate impact analysis | **Attorney-directed only** | Must be initiated by outside or employment counsel per the privilege section above. Never run as a standalone HR Analytics project first. |
| Individual pay recommendation generation (new hire offer, merit increase, adjustment) | Approved with conditions | Advisory only; comp professional makes and owns the final number; see the [AI use policy's](ai-use-policy.md) human review principle |
| Autonomous compensation changes (any AI system that can write a pay change to the HRIS without human confirmation) | **Prohibited** | No exceptions. See the [AI use policy's](ai-use-policy.md) agentic confirmation gate requirement. |
| Using employee compensation history to train or fine-tune a model | Not approved | Historical pay data reflects historical bias; do not let a model learn from it as ground truth without a bias review that counsel has signed off on |

---

## Required governance gate

Standard use cases go through the [risk assessment template](risk-assessment-template.md). Comp and pay equity use cases require the same template plus:

- [ ] Employment counsel (not just internal Legal generally) has reviewed and directed the analysis design before any AI tool touches compensation data
- [ ] A determination has been made and documented on whether the analysis is being conducted under privilege, and if so, the steps taken to preserve it (counsel engagement letter, restricted distribution, marked privileged and confidential)
- [ ] Current pay transparency and reporting obligations have been confirmed for every jurisdiction where affected employees are located
- [ ] A plan exists for what happens if the analysis finds a disparity, before the analysis runs, not after. "We'll figure it out if we find something" is not a plan and undermines any good-faith defense
- [ ] Output is restricted to the people who need it for remediation, not broadly shared with managers or embedded in dashboards

A comp or pay equity use case that can't check every box above is not ready, regardless of how promising the model is.

---

## Cross-links

- [AI use policy](ai-use-policy.md): the human-review and approved-tool-category framework this extends.
- [Risk assessment template](risk-assessment-template.md): required baseline; comp use cases add the gate above on top of it.
- [Use case library](../01-use-cases/use-case-library.md): where "pay equity analysis" is listed under People analytics.
- [Incident report template](incident-report-template.md): use if an AI tool touching comp data does something it shouldn't, this is an automatic Sev 1 or Sev 2.
