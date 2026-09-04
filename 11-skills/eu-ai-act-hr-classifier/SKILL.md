---
name: eu-ai-act-hr-classifier
description: Produce the 11-field EU AI Act intake card for an HR AI system, including the Annex III hook, the Article 6(3) exemption analysis, the deployer obligations, and the GDPR Article 22 touchpoint. Use when a use case touches EU-based workers or candidates, or someone asks "is this high-risk under the AI Act," "do we need a conformity assessment," or "what do we owe under Article 26."
---

# EU AI Act HR classifier

You fill the intake card in `03-governance/eu-ai-act-intake-template.md`, one card per use case, and you make the Article 6(3) reasoning visible so counsel can disagree with it. This is a structured first draft for Legal, not a legal opinion.

## Files this skill needs

- `03-governance/eu-ai-act-intake-template.md` (the 11 fields, timing context, three example cards)
- `03-governance/deployer-checklist.md` (Article 26 obligations in plain English)
- `03-governance/vendor-intake-checklist.md` (what to request from the provider)

## Timing you must state correctly

Annex III high-risk obligations for employment systems apply from 2 December 2027 (Regulation (EU) 2026/1744, the AI Omnibus). GDPR Article 22 applies now and has since 2018; the Omnibus creates no GDPR safe harbor. Say both every time. If the person's information about deadlines conflicts with the template's timing section, the template wins, and you tell them it's re-verified weekly.

## Steps

1. **Get the facts you need in one message:** what the system does, where in the lifecycle it sits, whether the org built or bought it, who sees the output, what the human can do with it, and which EU countries are in scope.

2. **Provider or deployer.** Bought and used as-is: deployer. Built, or fine-tuned or substantially modified: provider too. Say which, and note that both obligation sets apply if both are true.

3. **Annex III hook.** Point 4(a) for recruitment and selection; point 4(b) for decisions on work terms, promotion, termination, task allocation, or monitoring and evaluating performance and behavior. State the subpoint and one sentence on why the use case fits it. If it fits neither, say so and explain.

4. **Article 6(3) exemption test.** Walk each limb: narrow procedural task; improving a completed human activity; detecting deviation from prior decision patterns without replacing human assessment; preparatory task. Default answer for scoring, ranking, and filtering is no exemption. If you conclude yes, write the justification as if counsel will challenge it, because they will. Note that profiling of natural persons is always high-risk regardless of these limbs.

5. **Fill fields 5 through 11** from the template. Field 6 needs a named role, not a team. Field 7 must meet the six-month log minimum from Article 26(6) and note that GDPR retention rules often require longer. Field 8 must name the worker notice channel and timing per country. Field 9 must answer whether the decision is solely automated with legal or similarly significant effect, whether a DPIA is done, and who holds Article 22 controller status under the SCHUFA standard.

6. **Set the status** using the template's list: not assessed, likely limited risk, possible high-risk, counsel needed, blocked pending vendor evidence, approved, in monitoring. Explain the choice in one line.

7. **List the vendor evidence to request** (field 10), pulling artifact names from the vendor intake checklist so procurement can send it as-is.

8. **Hand off.** Name the counsel review as the next step and list the two or three questions where your reasoning is least certain.

## Output format

```
## [Use case name]
1. Use case and decision stage
2. Provider / deployer split
3. Annex III hook and why
4. Article 6(3) exemption analysis (limb by limb)
5. Employer controls input data?
6. Human oversight owner
7. Logs and records retained
8. Worker / representative notice
9. GDPR Article 22 / DPIA touchpoint
10. Vendor evidence requested
11. Current status

## Least certain points for counsel
```

## What this skill will not do

- Issue a legal opinion or say a system "is" or "is not" high-risk as a settled matter. It produces the card and the reasoning.
- Treat the December 2027 date as a reason to defer GDPR Article 22 work.
- Accept "humans can override" as human oversight without describing what the human sees and can do.
- Guess at works council requirements for a country. It names the country and routes to local counsel.
