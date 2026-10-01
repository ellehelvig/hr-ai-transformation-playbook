# Performance data in talent systems

Skills data increasingly drives learning recommendations, internal mobility, and workforce planning. When performance ratings feed skill estimates, the bias in the ratings moves with them.

[← Workflow patterns](README.md)

Performance ratings carry whatever inconsistency, recency effect, or disparate treatment exists in the performance process. Feeding them into skill proficiency estimates can launder that bias into a system that looks like infrastructure rather than a rating, but still scores people and still shapes who gets development and opportunity.

## Fairness check before any skill graph update

Before performance-derived data updates anyone's skill estimates:

1. Test whether the update shifts estimates differently across protected groups.
2. If it does, block the update and route it to People Analytics for review.
3. Version every update with its source and date, so the organization can answer "what did we believe about this person's skills, and why did it change?"

Treat any such update as a use case that needs a [risk assessment](../03-governance/risk-assessment-template.md).

## Principles

- Skills data informs placement, promotion, and investment decisions. It never makes them.
- Show how strong the evidence is behind each estimate; a single self-assessment is not the same as corroborated evidence.
- Name one owner for the skills taxonomy, usually Talent or People Analytics.

## Status

Proposed. Nothing in this repository implements a skills graph. The [skills gap analysis notebook](../05-notebooks/skills-gap-analysis.ipynb) is the closest working example of competency-to-gap logic.
