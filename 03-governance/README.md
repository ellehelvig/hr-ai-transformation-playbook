# Governance

> **03 / GOVERN** · Translate principles, laws, and risk decisions into operating controls.

[← Prompt library](../02-prompt-library/README.md) · [Playbook home](../README.md) · [Next: Enablement →](../04-enablement/README.md)

---

**For:** HR, Legal, Privacy, and Compliance partners. **Start with:** [AI use policy](ai-use-policy.md), then the [one-page pre-screen](quick-reference-checklist.md).

Frameworks for responsible AI adoption in HR, structured around the NIST AI Risk Management Framework 1.0 (Govern, Map, Measure, Manage) and ISO/IEC 42001. None of this is legal advice. All documents should be reviewed by Legal and Privacy before adoption.

## Contents

| File | Purpose |
|---|---|
| [quick-reference-checklist.md](quick-reference-checklist.md) | One-page pre-screen on data privacy, employee consent, and bias mitigation. Start here, then go deep on the documents below. |
| [ai-use-policy.md](ai-use-policy.md) | Principles and requirements for HR AI use. Adapt for your organization. |
| [risk-assessment-template.md](risk-assessment-template.md) | Required before deploying any new HR AI use case. |
| [eu-ai-act-intake-template.md](eu-ai-act-intake-template.md) | Row-per-use-case intake for HR AI under the EU AI Act. Includes example cards. |
| [vendor-selection-framework.md](vendor-selection-framework.md) | Build vs. buy decision, and comparing vendors before you pick one to run through intake. |
| [vendor-intake-checklist.md](vendor-intake-checklist.md) | What HR AI vendors must hand over before you sign, renew, or deploy. |
| [deployer-checklist.md](deployer-checklist.md) | What your organization owes under Article 26 once you deploy. |
| [incident-report-template.md](incident-report-template.md) | Fill out when an HR AI system does something it shouldn't. Severity scale, root cause, corrective actions, and communication steps. |
| [pay-equity-governance.md](pay-equity-governance.md) | Compensation and pay equity are the single highest-exposure use case. Privilege considerations, approved/prohibited AI use, and the required sign-off gate. |

## Key dates for HR

**Last reviewed: 24 September 2026.** Review this table once a quarter. When a date changes, update it here, in the documents that repeat it, and in the [changelog](../CHANGELOG.md). Each source link goes to the official text.

### Already in force

| Law | What it means for HR | Since | Source |
|---|---|---|---|
| GDPR, Article 22 (EU) | People have the right not to be subject to a decision made solely by automated means that significantly affects them, such as an automated rejection. Keep a human in the decision. | 25 May 2018 | [Regulation (EU) 2016/679](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679) |
| NYC Local Law 144 | An automated tool used to screen candidates or employees for hiring or promotion needs a bias audit within the past year, published results, and advance notice to the people it assesses. | 5 July 2023 | [Local Law 144 of 2021](https://legistar.council.nyc.gov/LegislationDetail.aspx?GUID=B051915D-A9AC-451E-81F8-6596032FA3F9&ID=4344524) |
| New Jersey Law Against Discrimination | The existing anti-discrimination law covers AI tools. Buying the tool from a vendor, or not knowing how it works, is no defense. | Applies now (state guidance, January 2025) | [NJ Attorney General guidance](https://www.nj.gov/oag/newsreleases25/2025-0108_DCR-Guidance-on-Algorithmic-Discrimination.pdf) |
| EU AI Act, fines | Breaking the AI Act's transparency rules can be fined up to EUR 15 million or 3% of worldwide turnover, whichever is higher. For SMEs it is whichever is lower. | Fine rules since 2 August 2025 | [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689), Article 99 |
| California FEHA automated-decision system regulations | Using an automated-decision system that discriminates, directly or through disparate impact, violates the Fair Employment and Housing Act, including when the tool comes from a vendor. Keep automated-decision data for four years. | 1 October 2025 | [Civil Rights Council final text](https://calcivilrights.ca.gov/wp-content/uploads/sites/32/2025/06/Final-Text-regulations-automated-employment-decision-systems.pdf) |
| Texas TRAIGA (HB 149) | Bans using AI with the intent to discriminate. Disparate impact alone does not prove intent, and the Act's consumer protections exclude employment. | 1 January 2026 | [HB 149, enrolled](https://capitol.texas.gov/tlodocs/89R/billtext/html/HB00149F.HTM) |
| Illinois HB 3773 (Human Rights Act) | Using AI that has the effect of discriminating in recruiting, hiring, promotion, training selection, discipline, discharge, or other terms of employment is a civil rights violation. ZIP code may not stand in for a protected class. Employees and applicants must be told when AI is used. The state's notice rules were proposed in May 2026 and withdrawn in June 2026, so the notice details are still unsettled; the duty itself applies now. | 1 January 2026 | [Public Act 103-0804](https://www.ilga.gov/legislation/publicacts/fulltext.asp?Name=103-0804) |
| EU Pay Transparency Directive | Member states had to turn the Directive into national law by this date. Check the status in each country where you employ people. | 7 June 2026 deadline | [Directive (EU) 2023/970](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023L0970), Article 34 |
| EU AI Act, transparency | Tell people when they are talking to an AI system, and label AI-generated or manipulated content. Tools on the market before August 2026 have until 2 December 2026 to add machine-readable labels. | 2 August 2026 | [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689), Article 50 |

### Coming up

| Law | What it means for HR | From | Source |
|---|---|---|---|
| Connecticut Public Act 26-15 | Using an AI tool is no defense to a discrimination complaint. Evidence of bias testing, and how you acted on the results, can be weighed in your favor. | 1 October 2026 | [Public Act 26-15](https://www.cga.ct.gov/2026/ACT/PA/PDF/2026PA-00015-R00SB-00005-PA.PDF) |
| California CPPA automated decisionmaking rules | Employers covered by the CCPA that use automated decisionmaking technology for significant employment decisions, without meaningful human involvement, owe a pre-use notice, an opt-out right, and access rights. | 1 January 2027 | [California Privacy Protection Agency](https://cppa.ca.gov/announcements/2025/20250923.html) |
| Colorado SB 26-189 | Replaces the 2024 Colorado AI Act. Employees and Colorado applicants get notice when automated decision-making technology materially influences an employment decision, an explanation within 30 days of an adverse decision, and the right to request human review. Enforcement is stayed by a stipulated federal court order until rulemaking ends and the court rules on a constitutional challenge, so check the docket before treating it as live. | 1 January 2027 | [SB26-189](https://leg.colorado.gov/bills/sb26-189) |
| EU AI Act, high-risk HR systems | AI used in recruiting, promotion, termination, task allocation, or performance monitoring must meet the high-risk rules, including human oversight, logging, and telling workers. This is a fixed date, so don't plan around further delay. | 2 December 2027 | [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32026R1744) (the AI Omnibus) |
| EU AI Act, AI inside regulated products | A separate, later date for AI built into products such as machinery. Rarely an HR question. | 2 August 2028 | [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32026R1744) |

Other laws this playbook discusses, including the Illinois AI Video Interview Act, the UK, and Ontario, are covered in the documents above but are not yet in this table.

The European Commission's draft guidelines on which systems count as high-risk (published 19 May 2026, final text expected around the end of 2026) are the best current guide to the employment categories. They are draft and non-binding. See the [EU AI Act intake template](eu-ai-act-intake-template.md).

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
