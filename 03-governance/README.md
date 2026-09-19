# Governance

> **03 / GOVERN** · Translate principles, laws, and risk decisions into operating controls.

[← Prompt library](../02-prompt-library/README.md) · [Playbook home](../README.md) · [Next: Enablement →](../04-enablement/README.md)

---

Frameworks for responsible AI adoption in HR, structured around the NIST AI Risk Management Framework 1.0 (Govern, Map, Measure, Manage) and ISO/IEC 42001. None of this is legal advice. All documents should be reviewed by Legal and Privacy before adoption.

## Contents

| File | Purpose |
|---|---|
| [claims/](claims/README.md) | Structured record of every dated regulatory claim, its primary source, and when it was last verified. Checked in CI. |
| [quick-reference-checklist.md](quick-reference-checklist.md) | One-page pre-screen on data privacy, employee consent, and bias mitigation. Start here, then go deep on the documents below. |
| [ai-use-policy.md](ai-use-policy.md) | Principles and requirements for HR AI use. Adapt for your organization. |
| [risk-assessment-template.md](risk-assessment-template.md) | Required before deploying any new HR AI use case. |
| [eu-ai-act-intake-template.md](eu-ai-act-intake-template.md) | Row-per-use-case intake for HR AI under the EU AI Act. Includes example cards. |
| [vendor-selection-framework.md](vendor-selection-framework.md) | Build vs. buy decision, and comparing vendors before you pick one to run through intake. |
| [vendor-intake-checklist.md](vendor-intake-checklist.md) | What HR AI vendors must hand over before you sign, renew, or deploy. |
| [deployer-checklist.md](deployer-checklist.md) | What your organization owes under Article 26 once you deploy. |
| [incident-report-template.md](incident-report-template.md) | Fill out when an HR AI system does something it shouldn't. Severity scale, root cause, corrective actions, and communication steps. |
| [pay-equity-governance.md](pay-equity-governance.md) | Compensation and pay equity are the single highest-exposure use case. Privilege considerations, approved/prohibited AI use, and the required sign-off gate. |

## EU AI Act timing

High-risk obligations for HR systems under Annex III were originally set to apply from 2 August 2026. The AI Omnibus simplification package, which moves this date to 2 December 2027, is now law: Regulation (EU) 2026/1744, published in the Official Journal on 24 July 2026 and in force since 27 July 2026 (verified against the regulation text on EUR-Lex). December 2027 is a fixed calendar date, not a conditional one: the Commission's original proposal would have tied the deadline to standards readiness, and the final agreement rejected that mechanism in favor of a fixed date, so don't plan around further slippage. Keep the classification field current now, because vendors and customers are already requesting the evidence trail. <!--claim:eu-ai-act-annex3-employment-application-date-->

Two things are enforceable today and get lost behind the 2027 headline: Article 50 transparency obligations applied from 2 August 2026 (the Omnibus did not move that date, but it gives AI systems already on the market a grace period until 2 December 2026 for the Article 50(2) machine-readable marking duty), and the Article 99 and 101 penalty provisions became operative on the same date. Separately, the Commission's draft Guidelines on high-risk classification under Article 6 (published 19 May 2026, consultation closed 23 July 2026, final text expected around end of 2026) are the closest thing to an official reading of the Annex III point 4 employment categories. They are draft and non-binding. See the [EU AI Act intake template](eu-ai-act-intake-template.md) for both.

## US federal AI enforcement context

The EEOC withdrew its May 2022 and May 2023 technical assistance documents on AI and algorithmic discrimination in early 2025, after Executive Order 14179 directed agencies to suspend Biden-era AI policy guidance. A subsequent order, *Restoring Equality of Opportunity and Meritocracy* (23 April 2025), directs federal agencies including the EEOC to deprioritize enforcement built on disparate-impact theory.

Neither order repeals disparate-impact liability. It remains codified in Title VII, and private plaintiffs can still bring disparate-impact claims regardless of federal enforcement priorities. State and local laws, Illinois' HB 3773 amendments to the Illinois Human Rights Act, Colorado's SB 26-189 (effective January 2027, enforcement currently stayed by a federal court), California's FEHA and CPPA ADMT rules, and NYC Local Law 144 among others, impose their own bias-testing and disclosure obligations independent of federal posture. Treat the fairness audit requirement throughout this playbook as unaffected by the shift in federal enforcement emphasis: the exposure moved from proactive EEOC enforcement toward private litigation and state law, it didn't disappear.

## The non-negotiables

Regardless of how you adapt these templates, three things are not optional:

1. **Humans make consequential employment decisions.** AI may inform, not decide.
2. **Provide notice and transparency** when AI influences processes that affect employees or candidates.
3. **Require fairness assessment and monitoring** for any use case that scores or ranks employees or candidates.

These are playbook design standards. Applicable legal requirements vary by jurisdiction and use case. If your governance framework does not protect these three things, it is not enough.

## Skills that run these documents

Four of the [agent skills](../11-skills/README.md) operate directly on this section: [hr-ai-vendor-review](../11-skills/hr-ai-vendor-review/SKILL.md) (pre-screen and vendor intake), [eu-ai-act-hr-classifier](../11-skills/eu-ai-act-hr-classifier/SKILL.md) (the 11-field card), [fairness-audit-prep](../11-skills/fairness-audit-prep/SKILL.md) (principle 3 and the monitoring template), and [hr-ai-incident-triage](../11-skills/hr-ai-incident-triage/SKILL.md) (Part 1 of the incident report). They produce drafts for Legal, not conclusions.
