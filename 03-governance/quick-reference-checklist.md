# Quick-reference checklist: vendor privacy, employee consent, bias mitigation

A one-page pre-screen for the three questions that come up in almost every HR AI vendor or deployment conversation: is employee data protected, do employees know AI is involved, and has bias been checked for. This checklist does not replace the documents it links to, it's a fast way to see what's missing before you go deep on any one of them. Not legal advice; the underlying documents carry the real detail and the required Legal/Privacy review.

Use this at the start of a vendor conversation or use case intake, before the [risk assessment template](risk-assessment-template.md) and [vendor intake checklist](vendor-intake-checklist.md), not instead of them.

---

## Data privacy

- [ ] Vendor has a standard DPA in place, or one is in negotiation → [vendor intake checklist, artifact 2](vendor-intake-checklist.md#2-technical-documentation-summary-annex-iv)
- [ ] Data residency and sub-processor list confirmed → [vendor selection framework, scorecard](vendor-selection-framework.md#step-2-vendor-comparison-scorecard)
- [ ] No sensitive personal data (health, protected category, immigration status) will be input without explicit tool approval → [AI use policy, principle 4](ai-use-policy.md#4-data-minimization-and-privacy)
- [ ] Logging posture confirmed: what's logged, where it's stored, retention ≥ 6 months, exportable → [vendor intake checklist, artifact 4](vendor-intake-checklist.md#4-logging-posture)
- [ ] No employee data used to train external models without explicit consent and legal review → [AI use policy, principle 4](ai-use-policy.md#4-data-minimization-and-privacy)

## Employee consent and notice

- [ ] Affected employees will be told AI is used in this process, and how → [AI use policy, principle 2](ai-use-policy.md#2-employees-have-a-right-to-know)
- [ ] A path exists for an employee to request human review, with a defined response time → [AI use policy, principle 2](ai-use-policy.md#2-employees-have-a-right-to-know)
- [ ] Behavioral surveillance, sentiment monitoring, or health/disability inference is not in scope without disclosure and consent → [AI use policy, prohibited uses](ai-use-policy.md#prohibited-uses)
- [ ] If this touches compensation, the analysis is attorney-directed from the start, not run first and shown to counsel after → [pay equity governance, the privilege question](pay-equity-governance.md#the-privilege-question)
- [ ] EU deployment: worker notice obligations under Article 26 are covered → [deployer checklist](deployer-checklist.md)

## Bias mitigation

- [ ] Use case has been assessed for disparate impact potential before deployment → [AI use policy, principle 3](ai-use-policy.md#3-fairness-and-bias-prevention-are-active-responsibilities)
- [ ] Vendor has provided bias testing methodology and results, broken down by protected group where lawful and available → [vendor intake checklist, artifact 6](vendor-intake-checklist.md#6-fairness-and-accuracy-evidence)
- [ ] A monitoring plan exists to detect bias post-deployment, with a defined review cadence (hiring and performance tools: at least annually) → [AI use policy, principle 3](ai-use-policy.md#3-fairness-and-bias-prevention-are-active-responsibilities)
- [ ] Thresholds are defined for when a bias finding triggers human review or tool suspension → [AI use policy, principle 3](ai-use-policy.md#3-fairness-and-bias-prevention-are-active-responsibilities)
- [ ] If skill or performance scoring is involved, the fairness check on any calibration-to-skill-graph feedback loop is in place → [talent operating system architecture, fairness check](../07-agentic-patterns/talent-operating-system-architecture.md#fairness-check-before-any-skill-graph-update)

---

## If any box is unchecked

An unchecked box is not automatically a blocker, it's a flag for what to resolve before this use case or vendor goes further. Route data privacy gaps to Privacy and Procurement, consent gaps to Legal and Employee Communications, and bias gaps to People Analytics and Legal. Comp-related gaps route to employment counsel specifically, not general Legal, see [pay equity governance](pay-equity-governance.md) for why that distinction matters.

## Cross-links

- [AI use policy](ai-use-policy.md): the source of truth for the principles this checklist points back to.
- [Vendor intake checklist](vendor-intake-checklist.md): the full evidence-gathering process for privacy and bias documentation.
- [Risk assessment template](risk-assessment-template.md): required before deploying any new HR AI use case.
- [Pay equity governance](pay-equity-governance.md): required reading before this checklist is sufficient for anything comp-related.
- [Deployer checklist](deployer-checklist.md): ongoing EU obligations once a high-risk system is live.
