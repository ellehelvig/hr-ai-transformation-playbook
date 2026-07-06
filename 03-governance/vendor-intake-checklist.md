# Vendor Intake Checklist

What an HR AI vendor must hand over before you sign, renew, or deploy. Use this for any tool that scores, ranks, recommends, screens, summarizes, or otherwise influences decisions about workers or candidates in the EU.

Not legal advice. Pair with Legal, Privacy, and Procurement review.

## How to use

- Send this list to the vendor with the intake template request.
- Track responses per item. Missing items are negotiation points, not afterthoughts.
- Re-run on every major model version change.

## Required artifacts

### 1. Instructions for use (Article 13)

The vendor must provide written instructions covering:

- Intended purpose, including the specific HR use cases the system is meant for and the ones it is not.
- Level of accuracy, robustness, and cybersecurity the system is designed to meet, with the metrics used.
- Known and foreseeable circumstances that may lead to risks to health, safety, or fundamental rights.
- Known limitations, including performance differences across populations the system was tested on.
- Human oversight measures the deployer must implement, including how to interpret outputs.
- Computational and hardware requirements, expected lifetime, and maintenance expectations.
- Any input data specifications the deployer must meet for the system to work as intended.

Red flag: vendor provides marketing material instead of instructions for use, or instructions are not version-locked to the model.

### 2. Technical documentation summary (Annex IV)

You do not need the full technical file. You need a summary that lets you and your auditors verify the system is what the vendor claims.

- General description: intended purpose, version, provider, date of placement on market.
- Design choices, including system architecture and what the system was optimized for.
- Training, validation, and test data: where it came from, how it was selected, labeled, cleaned.
- Validation and testing procedures, including bias metrics and performance across demographic groups where applicable.
- Risk management measures and residual risks.
- Post-market monitoring plan.

Red flag: vendor refuses to share any part of the technical documentation summary, even under NDA.

### 3. Conformity assessment status

For high-risk systems, the vendor must complete a conformity assessment before placing on the market.

- Has the vendor declared the system high-risk under Annex III?
- Which conformity assessment procedure applies (internal control under Annex VI, or notified body under Annex VII)?
- Date of the EU declaration of conformity, and the version it covers.
- CE marking status.
- If the system is not declared high-risk, on what basis (Article 6(3) exemption analysis, or category does not apply).

Red flag: vendor claims the system is not high-risk without written analysis, or the declaration of conformity is for a different version than what you are buying.

### 4. Logging posture

The deployer needs logs to meet Article 26(6). The vendor must enable them.

- What events are logged by default.
- What additional events can be enabled.
- Where logs are stored (vendor cloud, customer cloud, both).
- Retention defaults and configurable range. Minimum six months for deployer logs.
- Export format and API for compliance and audit.
- Access controls and audit trail on the logs themselves.

Red flag: logs are not exportable, retention is hard-capped below six months, or logs are aggregated in a way that prevents per-decision review.

### 5. Human oversight guidance

The vendor must explain how a human is meant to oversee the system in practice. Generic "humans can override" language is not enough.

- What the human reviewer sees in the UI: score, confidence, top features, comparable cases, recommendation.
- What the human can do: accept, override, request explanation, escalate, disable for a case or req.
- How the system flags low-confidence or anomalous outputs.
- What training the vendor recommends for oversight roles.
- How overrides are captured and fed back into monitoring.

Red flag: oversight is described as a checkbox in the UI with no supporting context.

### 6. Fairness and accuracy evidence

- Performance metrics on the populations the system is intended for.
- Bias testing methodology and results, broken down by relevant protected groups (age, gender, disability where lawful and available).
- How the vendor monitors for drift after deployment.
- Procedure for handling fairness incidents reported by deployers.

Red flag: vendor reports aggregate accuracy only, refuses to break down performance, or has no drift monitoring.

### 7. Deployer support commitments

- Support for the deployer obligations under Article 26, including templates for worker notice and oversight role descriptions.
- Notification SLA when the model version changes, instructions for use change, or incidents occur.
- Right to audit, or independent attestations the vendor will provide (SOC 2, ISO 42001 where available, fairness audits).
- Co-operation on regulator inquiries.
- Termination assistance, including data return and log preservation.

Red flag: vendor disclaims all responsibility for supporting deployer compliance, or treats compliance support as a premium tier.

### 8. Incident reporting

- Definition of a reportable incident in the vendor's contract.
- Notification timeline. Match or improve on AI Act and GDPR timelines.
- Reporting channel and required content.
- Right of the deployer to verify root cause analysis.

Red flag: incident definition is narrower than the AI Act post-market monitoring concept, or the vendor only commits to "commercially reasonable" notification.

## Procurement red flag summary

Any of the following means stop and escalate before signing:

- No version-locked instructions for use.
- No technical documentation summary, even under NDA.
- No declaration of conformity for high-risk use cases.
- Logs that cannot be exported or are capped below six months.
- Oversight described only as a UI checkbox.
- No bias testing or no breakdown by population.
- No support for Article 26 deployer obligations.
- Incident definition narrower than AI Act post-market monitoring.

## Cross-links

- [EU AI Act intake template](eu-ai-act-intake-template.md): the per-use-case card that this checklist feeds.
- [Deployer checklist](deployer-checklist.md): what your organization owes once the vendor evidence is in hand.
- [Risk assessment template](risk-assessment-template.md): the broader fairness and incident process.
