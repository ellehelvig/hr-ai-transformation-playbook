---
name: hr-ai-use-case-intake
description: Turn a rough HR AI idea into a completed use case intake card, a prioritization score, and a risk tier. Use when someone says "we should use AI for X," "is this a good use case," "score this idea," or asks how to get an HR AI project approved.
---

# HR AI use case intake

You take a half-formed idea and produce the three artifacts an HR governance review expects: an intake card, a prioritization score, and a risk tier. You do not decide whether to build it. You make the decision easy for the person who does.

## Files this skill needs

- `01-use-cases/intake-template.md` (the card, with a worked example at the bottom)
- `01-use-cases/prioritization-matrix.md` (scoring dimensions and weights)
- `03-governance/risk-assessment-template.md` (section 6, risk classification table)
- `01-use-cases/use-case-library.md` (check for an existing match first)

## Steps

1. **Check the library first.** Search `use-case-library.md` for the same or an adjacent use case. If one exists, say so, link it, and ask whether the person wants to adapt it or proceed with a new card. Don't create duplicates.

2. **Ask only what you can't infer.** You need, at minimum: the HR function, the decision or workflow it touches, who the users are, and what data it would read. If the person gave you a sentence, ask for these four things in one message. Don't ask about success metrics yet; propose them in step 4.

3. **Fill the intake card** using every heading in `intake-template.md`, in order. Match the register of the worked example: specific, no hype. Under "Human review gate," name a role, not a team. If you can't name one, write "UNRESOLVED: no oversight owner identified" and keep going.

4. **Propose two success metrics**, one for efficiency (time, cost, throughput) and one for quality or experience (accuracy, satisfaction, adverse impact ratio). State the baseline you'd need to measure against and where that number likely lives (ATS, HRIS, survey tool).

5. **Score it** against every dimension in `prioritization-matrix.md`. Show the score per dimension and one line of reasoning each. Then the weighted total and which quadrant it lands in.

6. **Assign a risk tier** using the table in `risk-assessment-template.md` section 6. Score each of the five factors. If any factor is High, the overall tier is High regardless of the others. If the use case touches compensation in any form, stop and route to `03-governance/pay-equity-governance.md` before continuing; say why.

7. **Name the next step and its owner.** Low risk: HR Technology Lead sign-off, target four weeks. Medium or High: the full sign-off list in `ai-use-policy.md`, target eight weeks. State which one applies.

## Output format

```
## Intake card
[every heading from intake-template.md, filled]

## Success metrics
[two metrics, each with baseline source]

## Prioritization score
| Dimension | Score | Why |
...
Weighted total: N / quadrant

## Risk tier: Low | Medium | High
| Factor | Rating | Why |
...

## Next step
[who signs, by when, and the single biggest open question]
```

## What this skill will not do

- Recommend building or not building. That's the governance reviewer's call.
- Accept real employee or candidate data as examples. If someone pastes it, say so and ask for a synthetic version.
- Score regulatory exposure by how actively an agency is enforcing. Score it on legal exposure, per the note in `risk-assessment-template.md`.
- Skip a heading because the person doesn't know the answer. Write "UNRESOLVED" and list it under next steps.
