# Worked example: employee experience and engagement

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Jory Ambleside, listening program lead, writes: "Our November Engineering pulse on the AI coding assistant rollout just closed. Leadership wants to decide whether to slow the rollout. Please synthesize the comments, build a manager pack, and draft the action tracker. Also, the VP of Platform asked which Berlin people wrote the negative comments. Thresholds are 5 for scores and 10 for comments."

| Group | Invited | Responded | Comments |
|---|---|---|---|
| Engineering, all | 620 | 471 | 220 |
| of which Berlin Platform team | 11 | 8 | 6 |

## Output (abridged)

```markdown
## Confidentiality settings
Scores minimum: 5  Comments minimum: 10  Subtraction rule: no filter pair
that differs by fewer than 10 respondents
Smallest filter tested: Berlin Platform team, 8 respondents
Suppressed this cycle: Berlin Platform comments (8 < 10). Its 6 comments
are excluded from AI summary; scores shown (8 >= 5).

## Open-text themes (groups at or above threshold only)
Base: 220 - 6 = 214 comments
| Theme | Approx. share | Sentiment | Quote (de-identified) | Concentrated? |
| Workload rose during rollout | 77 / 214 = 36% | negative | "Review time doubled" | No |
| Unclear rules on what code the assistant may see | 47 / 214 = 22% | negative | "Nobody said if client code is allowed" | Yes, Platform |
| Manager made time to practice | 34 / 214 = 16% | positive | "Our lead blocked Friday mornings" | No |
...

## Manager pack
Discussion guide: "What would make the assistant save you time, not add it?"
...

## Action and follow-up
| Action | Owner | Cost | Measure | Report back |
| Publish code-access rules for the assistant | CTO office | low | theme share next pulse | 15 Jan |

## Decision rights calls
| Request | Agent role | Routed to |
| Themes and manager pack | Drafts for sign-off | People analyst, managers |
| "Which Berlin people wrote the negative comments?" | Refuses and routes | Privacy lead; VP gets team-level themes only |
| "Slow the rollout?" | Drafts for sign-off | Leadership decides, with options above |

## Audit trail
Inputs used: decision to inform, thresholds, response counts, de-identified
comments. Not provided: works council consultation status for Berlin.
Tools called:
| Survey platform (read-only) | thresholds, counts | threshold settings, response counts |
| Survey platform (read-only) | comments | de-identified comments, groups >= 10 |
Needs sign-off: themes (people analyst checks raw sample), results
communication (Jory Ambleside)
Open legal questions: works council consultation for Berlin; any platform
feature that reads emotions, see Key dates row EU AI Act, emotion
recognition at work (Article 5(1)(f))
```

## Metrics this plan tracks

- Response rate: 471 / 620 = 76.0% this cycle.
- Action close-out rate: 3 of 5 actions from the last cycle completed with a reported result = 60%.
- Belief in action: 212 of 463 respondents to that item answered favorably = 45.8%.
