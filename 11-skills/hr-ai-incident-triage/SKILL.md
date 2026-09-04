---
name: hr-ai-incident-triage
description: Fill Part 1 of the HR AI incident report, assign severity, identify immediate containment, and route to the right owners. Use when an AI tool in an HR process did something wrong (bad output reached an employee, data was disclosed, a biased pattern was spotted, an agent took an action it shouldn't have), or someone says "the AI messed up" or "do we need to report this."
---

# HR AI incident triage

Speed and accuracy in the first hour. You get the facts down, size the problem, and get it to the people who own the next step. The postmortem comes later and is a separate conversation.

## Files this skill needs

- `03-governance/incident-report-template.md` (Part 1 fields, severity scale, worked example)
- `03-governance/ai-use-policy.md` (reporting concerns section, prohibited uses)
- `03-governance/deployer-checklist.md` (section 10, serious incident reporting; section 3, pause criteria)
- `03-governance/risk-assessment-template.md` (state law incident definitions in the regulatory note)

## Steps

1. **Get the timeline first.** What happened, when it was noticed, who noticed it, whether it's still happening. If it's still happening, go to step 2 before anything else.

2. **Containment.** Check the pause criteria in `deployer-checklist.md` section 3. If any applies, say plainly: "This meets the pause criteria. The oversight owner for this tool can pause it without further approval." Name the owner if the use case card is available. Don't wait for severity to be assigned.

3. **Fill Part 1** of the incident report, every field, in the order the template gives. Where a fact is unknown, write "UNKNOWN as of [time]" rather than leaving it blank or guessing.

4. **Assign severity** using the template's scale. Show which criteria were met. If the incident involves any of the prohibited uses in `ai-use-policy.md` (autonomous hiring decision, undisclosed surveillance, health or disability inference, automated termination), it's at least the second-highest tier regardless of impact size.

5. **Regulatory triggers.** Check, without concluding: does this look like a serious incident under AI Act Article 73 (EU high-risk system)? A GDPR personal data breach (72-hour clock)? A state law trigger listed in the risk assessment template? For each, write "possible" or "unlikely" and one line of why. Legal decides.

6. **Route.** Oversight owner (containment). Legal and Privacy (regulatory clocks). Employee Communications if an employee was affected and needs to hear from a human. Vendor, if the root cause may be on their side, with the notification SLA from the contract. HR Leadership if severity is in the top two tiers.

7. **Schedule the postmortem** and name who runs it. Point to Part 2 of the template. Remind that it's blameless and that the incident report is the org's record regardless of what the vendor commits to.

## Output format

```
## Status: CONTAINED | ONGOING
[if ongoing: pause criteria met Y/N, who can pause]

## Part 1: Incident report
[every field from the template]

## Severity: [tier]
[criteria met]

## Regulatory triggers
| Trigger | Possible / Unlikely | Why |

## Routing
| Owner | Action | By when |

## Postmortem
[owner, date, link to Part 2]
```

## What this skill will not do

- Decide whether a regulatory notification is required. It flags the possibility and the clock; Legal decides.
- Assign blame to a person. Root cause comes from the postmortem, not the triage.
- Communicate with the affected employee directly. It drafts nothing for them; Employee Communications and the person's HRBP handle that.
- Downgrade severity because the impact was small if a prohibited use was involved.
