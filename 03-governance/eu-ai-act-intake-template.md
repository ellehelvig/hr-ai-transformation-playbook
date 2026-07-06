# EU AI Act Intake Template

A row-per-use-case intake for HR AI systems. Fill one card before you adopt, build, or renew any HR AI tool that may touch EU-based workers or candidates.

This is not legal advice. Use it to structure the conversation with Legal, Privacy, and your vendor. Outputs should be reviewed by counsel before relying on them.

## Timing context

The EU AI Act is in force. Obligations for high-risk AI systems in employment (Annex III, point 4) were originally set to apply from 2 August 2026. The AI Omnibus simplification package, which moves this date to 2 December 2027, is now formally adopted: Parliament passed its final vote on 16 June 2026 and the Council gave final sign-off on 29 June 2026. The package is pending publication in the Official Journal and enters into force shortly after. Embedded high-risk AI under Annex I (regulated products) gets a separate deferral, to 2 August 2028. Keep the classification field current now, because vendors and customers are already requesting the evidence trail.

Other AI Act obligations (prohibited practices, GP-AI, transparency) follow their own timelines and are not affected by the same deferral.

## The 11 fields

Every use case gets a card with these fields. Skipping a field is itself a finding.

1. **Use case and decision stage.** What the system does, and where in the employee or candidate lifecycle it sits (sourcing, screening, interview, offer, onboarding, performance, comp, promotion, internal mobility, retention, separation).
2. **Provider / deployer split.** Are you the provider (you built it or substantially modified it) or the deployer (you bought or licensed it)? Both sets of obligations apply if you did both.
3. **Candidate Annex III hook and why.** Which Annex III category likely applies. For HR, the relevant ones are point 4(a) recruitment and selection, and point 4(b) decisions affecting work conditions, promotion, termination, task allocation, performance, or behavior monitoring. State the specific subpoint and why your use case fits.
4. **Article 6(3) exemption question.** Does the system qualify for the narrow exemption (preparatory task, narrow procedural task, detecting deviation from prior decision patterns, or no material influence on outcome)? Default assumption: most HR scoring and ranking use cases do not qualify. Justify any "yes" answer.
5. **Employer controls input data?** Yes / partial / no. If the vendor controls input data or training data, the deployer still owns oversight and worker notice obligations but loses some practical control over fairness.
6. **Human oversight owner.** Named role, not a team. Who reviews outputs, who can override, who is on the hook if the system causes harm. If no individual can be named, the use case is not ready to deploy.
7. **Logs and records retained.** What gets logged, where, for how long. Article 26(6) sets a six-month minimum for deployer-side logs unless other law requires longer (GDPR retention rules often do).
8. **Worker / representative notice needed.** Article 26(7) requires informing workers and their representatives before deploying a high-risk system in the workplace. Note the channel, timing, and what the notice will say.
9. **GDPR Article 22 / DPIA touchpoint.** Is there solely automated decision-making with legal or similarly significant effect? If yes, Article 22 protections apply on top of AI Act duties. Has a DPIA been completed or scheduled?
10. **Vendor evidence requested.** Specific artifacts asked for: instructions for use, technical documentation summary, conformity assessment status, logging posture, oversight guidance, fairness testing results, incident reporting commitments.
11. **Current status.** One of: not assessed, likely limited risk, possible high-risk, counsel needed, blocked pending vendor evidence, approved, in monitoring.

## Summary view

A short rollup table for leadership and audit. Keep it current.

| Use case | Lifecycle stage | Provider / deployer | Annex III hook | Status |
|---|---|---|---|---|
| Resume screening AI | Sourcing / screening | Deployer | 4(a) recruitment | Possible high-risk |
| Interview scheduling bot | Sourcing / screening | Deployer | None (procedural) | Likely limited risk |
| Internal mobility recommender | Internal mobility | Deployer | 4(b) promotion / task allocation | Possible high-risk |
| Attrition risk model (HRBP-facing) | Retention | Provider + deployer | 4(b) work conditions | Counsel needed |
| Performance review summarizer | Performance | Deployer | 4(b) performance evaluation | Counsel needed |

## Example cards

### Resume screening AI

1. **Use case and decision stage.** Vendor-licensed model scores inbound applications against job requirements. Recruiter sees ranked list. Used at first-pass screening for tech and ops roles in EU markets.
2. **Provider / deployer split.** Deployer only. No fine-tuning or substantial modification.
3. **Candidate Annex III hook and why.** Annex III point 4(a). System is used to filter and rank candidates, which directly influences who progresses to recruiter review.
4. **Article 6(3) exemption question.** No. Scoring materially influences the screening decision even with recruiter override available, because volume forces reliance on the ranking.
5. **Employer controls input data?** Partial. Job descriptions and screening criteria are ours. Training data and model weights are the vendor's.
6. **Human oversight owner.** Senior Recruiting Operations Manager. Reviews calibration monthly, can disable scoring for any req, owns appeal process.
7. **Logs and records retained.** Per-candidate score, model version, recruiter override, timestamp. Retained 24 months in vendor SaaS plus our ATS audit log. Exceeds 6-month minimum.
8. **Worker / representative notice needed.** Yes for candidates (privacy notice updated, AI use disclosed in job posting footer). Works council notified 45 days before go-live in DE and FR markets.
9. **GDPR Article 22 / DPIA touchpoint.** Not solely automated (recruiter reviews top ranked list). DPIA completed and signed by DPO.
10. **Vendor evidence requested.** Instructions for use, bias audit summary, logging architecture diagram, conformity assessment status, SOC 2, DPA, incident notification SLA.
11. **Current status.** Possible high-risk. Blocked pending vendor conformity assessment documentation.

### Interview scheduling bot

1. **Use case and decision stage.** Chatbot finds mutual availability between candidate and interviewer panel. No assessment, no ranking.
2. **Provider / deployer split.** Deployer only.
3. **Candidate Annex III hook and why.** None. System performs a narrow procedural task and does not influence selection.
4. **Article 6(3) exemption question.** Yes, narrow procedural task per Article 6(3)(a). Document the analysis.
5. **Employer controls input data?** Yes.
6. **Human oversight owner.** Recruiting Coordinator Manager.
7. **Logs and records retained.** Scheduling logs only, 12 months.
8. **Worker / representative notice needed.** Standard candidate privacy notice covers it.
9. **GDPR Article 22 / DPIA touchpoint.** No automated decision-making. DPIA not required.
10. **Vendor evidence requested.** DPA, SOC 2, instructions for use.
11. **Current status.** Likely limited risk. Approved.

### Internal mobility recommender

1. **Use case and decision stage.** ML model surfaces internal candidates to hiring managers for open EU roles based on skills, tenure, and performance signals.
2. **Provider / deployer split.** Both. Vendor model, fine-tuned on our employee data.
3. **Candidate Annex III hook and why.** Annex III point 4(b). Recommendations materially affect access to promotion and task allocation.
4. **Article 6(3) exemption question.** No. Recommendations shape opportunity access and are not narrow procedural.
5. **Employer controls input data?** Yes for employee features. Vendor for base model.
6. **Human oversight owner.** VP Talent.
7. **Logs and records retained.** Recommendations shown to each manager, manager actions, employee opt-out status. 24 months.
8. **Worker / representative notice needed.** Yes. Works council consultation underway in DE, FR, IT, NL.
9. **GDPR Article 22 / DPIA touchpoint.** Not solely automated. DPIA in progress.
10. **Vendor evidence requested.** Fairness audit across protected groups (age, gender), model card, conformity assessment plan, logging posture.
11. **Current status.** Possible high-risk. In monitoring, with quarterly fairness review.

## How to use this template

- Copy the 11-field block per use case. Keep the cards in version control.
- Update the summary table monthly.
- Review every card when: vendor changes model version, you add a new EU jurisdiction, you change the decision stage, regulatory guidance changes.
- Audit findings live as comments on the card, not in a separate tracker.

## Cross-links

- [Vendor intake checklist](vendor-intake-checklist.md): what the vendor must hand over before you complete a card.
- [Deployer checklist](deployer-checklist.md): what your organization owes once you deploy.
- [Risk assessment template](risk-assessment-template.md): the broader fairness, accuracy, and incident process. Run alongside this intake.
- [AI use policy](ai-use-policy.md): the organizational frame these checklists sit inside.
