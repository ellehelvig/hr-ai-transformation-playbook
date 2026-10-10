# Pilot and adoption plan: make the new work worth doing

**Proposed plan with a fictional People Partner example. No pilot, adoption result, or business benefit has been observed.**

[Select the use case](../01-use-cases/prioritization-matrix.md) → [Redesign the work](../01-use-cases/work-redesign-people-partner.md) → **Judge the pilot**

A pilot should answer whether the redesigned work is useful, dependable within its scope, and workable for the people who own it. Training completion alone cannot answer that. This plan starts with synthetic rehearsal and keeps employee-facing use on hold until its own gates pass.

## Pilot charter to adapt

**Fictional scope:** People Partner policy lookup and draft review for remote-work questions. Ordinary rules retrieve approved fictional policy. AI drafting is a proposed option to compare, not an implemented feature of Resolve's default demo. Sensitive context goes to a person. No employment decision or HRIS write is automated.

**Decision today:** synthetic rehearsal only after its tool/data approvals. Resolve is not approved for employee-facing use. Trusted identity, protected records, independent evaluation, and operating ownership remain prerequisites.

| Role | Responsibility before and during a pilot |
|---|---|
| Sponsor: Head of People | Authorize scope and resources; decide expand/pause/stop with accountable partners |
| Operator: HR service delivery lead | Own daily handling, capacity, version record, incidents, and retirement of the workflow |
| Policy owner and People Partners | Verify policy, review outputs, record edits and exceptions, retain decision authority |
| Employee Relations / accommodations / Legal | Set specialist boundaries and severity criteria; own sensitive substantive decisions and legal review |
| HR systems / IT / Security | Verify permitted tools, identity-bound access, technical failures, integration limits, and rollback |
| Privacy | Approve minimum data, provider handling, retention, access to evidence, and small-group reporting |
| Enablement owner and managers | Protect practice time, explain changed responsibilities, support challenge and non-use feedback |
| Employees or representatives | Review clarity, accessibility, human-channel choice, and concerns before employee-facing design is approved |

These are role assignments to make, not people who have already participated. Record actual named owners privately before work begins. No accountable owner means hold.

## A staged plan, with no automatic expansion

### Days 1-30: understand and rehearse

Map the manual process with practitioners, including exceptions and invisible review work. Confirm an approved tool and synthetic data scope. Deliver literacy Modules 1-3, including governance and data handling, before practice. See the [curriculum](hr-ai-literacy-curriculum.md) and [facilitator guide](workshop-facilitator-guide.md).

Measure a human-only synthetic baseline on the same scope and rubric planned for comparison. Treat it as rehearsal evidence, not an operational employee baseline. Before any later real-work pilot, establish a separately authorized operational baseline in the approved environment. Never put employer data in this repository.

Have reviewers practice three fictional requests: a routine policy question, an ambiguous request, and a sensitive disclosure hidden inside a routine topic. Require source checking, an override, and a specialist referral. These are assistant-authored learning examples, not independent evaluation cases. Ask managers to rehearse explaining why a person needs more information without asking for unnecessary health details.

### Days 31-60: compare the work

Compare manual handling, rules-only support, and any separately approved assisted option. Use the same case scope and independently labeled evaluation set where required. Separate development cases from unseen evaluation. Record versions, errors, disagreement, handling time, review time, and rework. Include accessibility and an easy route to a human in practitioner walkthroughs.

Run a weekly 15-minute practice and feedback session. Managers protect review time and ask which step became easier or harder. The operator records reasons for non-use and false escalation without pressuring people to accept poor outputs. Employee participation is a design input, not a claim that trust has been earned.

Remain in synthetic rehearsal if an access, privacy, evaluation, or ownership gate is unresolved. A date on this plan is not permission to process employee data.

### Days 61-90: decide, then prepare the next cohort

The sponsor reviews the evidence with HR, specialists, IT/Security, and Privacy. Complete the curriculum, including Module 4, before a new cohort starts real-work use. Expand only the tested task, data scope, and version after its gates pass. Share both failures and useful findings. Record a pause or stop with the same care as an expansion.

## Measure the entire task

Set periods, denominators, severity tolerances, and reviewer-capacity limits before evaluation. No numerical success threshold is validated by this template.

| Measure | Baseline / comparison | Cadence and owner |
|---|---|---|
| Correct policy and useful output | Reviewed cases meeting the predefined rubric / all reviewed cases; report critical defects separately | Weekly, policy owner |
| Missed specialist concerns | Review failures individually; sample non-escalated cases as well as escalations | Weekly during pilot, specialist owner |
| Unnecessary escalation and false refusal | Report each separately with specialist minutes and delays | Weekly, operator |
| Total handling effort | Intake + retrieval/drafting + review + rework + escalation effort per comparable case | Weekly, operator |
| Employee experience | Correct-owner time, repeat contacts, abandonment, accessibility concerns, human-channel availability | Weekly, HR owner; use approved aggregate feedback |
| Sustained use | Repeat users / eligible participants with access; pair with quality and reasons for non-use | Weekly cohort review, enablement owner |
| Operating cost | Implementation, learning, software, evaluation, maintenance, incident handling | At each decision, sponsor and finance partner |

Use within-scope comparison and report case-mix differences. Synthetic performance is not field fairness, employee satisfaction, or independent validation.

## A transparent value calculation

**Illustrative assumptions only, not a target or observed saving:** 100 cases in one month. Manual effort is 20 minutes per case. Proposed assisted effort is 8 minutes preparation + 7 review + 3 rework, or 18 minutes total. Net case-handling capacity is `100 × (20 - 18) / 60 = 3.33 hours`.

If review instead takes 10 minutes, total effort becomes 21 minutes and the same volume **adds 1.67 hours**. This sensitivity shows why review burden matters. Add proposed setup of 12 hours, learning of 4 hours, and ongoing evaluation/maintenance of 2 hours for month one: `3.33 - 12 - 4 - 2 = -14.67 net hours` before software cost. In later months at the original assumptions, `3.33 - 2 = 1.33 net hours`, with software and any new incident cost still to account for.

Capacity is not cash. Do not convert it into headcount reduction or claim realized savings without an actual financial change. If a monetary business case is later approved, disclose the hourly-cost assumption, period, usage, and all costs: `ROI = (monetized benefit - total cost) / total cost`. Keep avoided spending distinct from redeployed time; do not count labor cost twice. Quality and safety gates apply even when projected ROI is positive.

## Expand, pause, or stop

- **Expand:** agreed quality and employee-access criteria pass; reviewer capacity is adequate; independent evaluation and access/privacy gates pass; owners approve the specific version and scope. Evidence supports only that expansion.
- **Pause:** missing baseline, uncertain source quality, excessive review/rework, unexplained non-use, absent owner, or unverified control. Keep manual handling available and resolve the gap.
- **Stop affected processing:** cross-user exposure, unapproved sensitive data, bypassed approval, or a confirmed critical routing miss. Contain access, notify the incident owner, and preserve evidence in the approved environment. Missing critical evidence cannot be offset by speed or adoption.

After a failure, explain what is known, investigate the actual cause, and choose containment based on severity and reach. Do not assume the user skipped a verification step. Restart requires a recorded corrective action, fresh evidence, and the relevant owner's approval. Use the [incident template](../03-governance/incident-report-template.md).

Review again when the model, prompt, policy, permissions, provider, or intended use changes. Retire the workflow if the need disappears or operating capacity cannot sustain it. Preserve decisions and approved evidence under the organization's retention rules.

## Research basis and maintenance

Microsoft's [2026 Work Trend Index](https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization), published 5 May 2026 and accessed 10 October 2026, informs the emphasis on managers and organizational readiness. Its survey associations are not causal proof of business impact. NIST's [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), released January 2023 and accessed 10 October 2026, informs ongoing evaluation and risk ownership. It is voluntary guidance, not certification. The schedule, calculations, and gates above are proposed design judgments.

Maintain one charter, one measurement record, and one decision log. Review weekly during the pilot and at material changes. The stopping point is an evidence-backed expand, pause, or stop decision, not a larger collection of templates.
