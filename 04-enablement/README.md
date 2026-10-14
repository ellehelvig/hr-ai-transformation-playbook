# Enablement

> **04 / ADOPT AND PROVE** · Build the capability, trust, and feedback loops that make adoption durable.

[← Governance](../03-governance/README.md) · [Playbook home](../README.md) · [Next: Notebooks →](../05-notebooks/README.md)

---

**For:** HR leaders and L&D teams building AI fluency. **Start with:** [HR AI literacy curriculum](hr-ai-literacy-curriculum.md).

Training and adoption resources to build AI fluency across the People Team. Without this layer, even the best AI tools end up unused, misused, or used only by the early adopters who would have figured them out anyway.

## Contents

| File | Purpose |
|---|---|
| [hr-ai-literacy-curriculum.md](hr-ai-literacy-curriculum.md) | 4-module program for all People Team members (about 7 hours of sessions plus async work) |
| [HR-AI-Literacy-Curriculum.pdf](HR-AI-Literacy-Curriculum.pdf) | Visual presentation deck (23 slides), readable in any browser |
| [HR-AI-Literacy-Curriculum.pptx](HR-AI-Literacy-Curriculum.pptx) | Editable PowerPoint version for adaptation to your organization |
| [workshop-facilitator-guide.md](workshop-facilitator-guide.md) | Logistics, pacing, resistance handling, and format adaptations for anyone facilitating the curriculum |
| [adoption-playbook.md](adoption-playbook.md) | The change management work that happens alongside training, stakeholder map, 90-day rollout plan, adoption metrics, and handling the first public failure |

## Download status

The PDF and editable PowerPoint were synchronized to the 13 October 2026 curriculum snapshot. All 23 slides and PDF pages were rendered and reviewed. Session hours, synthetic lab boundaries, approach taxonomy, proposed recognition, pilot ownership and review gates are aligned. The slides summarize the material; PowerPoint notes retain the complete curriculum source and its hash. Legal delivery still requires current primary-source and counsel review.

Use synthetic examples in approved tools. Do not upload real employee, candidate, compensation, or employer-confidential content for a training exercise. Removing names alone does not establish anonymity.

## Why enablement is the bottleneck

Most HR AI programs over-invest in tooling and under-invest in capability. The result: shiny pilots that don't scale because the HR professionals who'd benefit either don't know the tools exist, don't trust them, or don't know how to use them well.

This curriculum is the counterweight. It is built on three assumptions:

1. **HR professionals don't need to understand the math.** They need to understand the failure modes, hallucination, bias, scope drift, well enough to spot them.
2. **Practice should resemble HR workflows.** Use synthetic scenarios in Module 2 and test whether the lab improves participants' judgment and verification habits.
3. **AI resistance is rational until people experience the lift.** Module 3 surfaces concerns instead of suppressing them. The best discussions happen when the room has range.

## Delivery guidance

The curriculum is designed for facilitator-led delivery but can be adapted for self-paced use. Specific notes:

- **Cadence:** Suggested cadence: one module per week over 4 weeks, with async practice. Compare completion and learning against your own baseline; no comparative completion evidence is supplied here.
- **Audience mix:** Don't separate HR Tech from HRBPs from HR Ops. The discussion is richer with the full mix.
- **Module 2 lab:** Reserve time for participants to work through synthetic HR scenarios using organization-approved tools. Review provider data handling and tool settings before delivery.
- **Module 3 case studies:** Adapt synthetic examples to familiar workflows. Do not use identifiable employee cases or confidential company documents.
- **Facilitator pairing:** Where possible, pair an AI-enthusiastic facilitator with an AI-skeptical one. The conversation that produces, not the lecture, is what people remember.

## Measuring program success

Track these against a baseline measured before launch:

- **Tool adoption**: % of People Team actively using approved AI tools weekly (target: [Set after baseline])
- **Self-rated confidence**: pre/post survey on "I can use AI tools in my HR work effectively" (target: [Set after baseline])
- **Quality of prompt use**: sample of prompts scored against the four-elements rubric from Module 2
- **Escalation appropriateness**: for any AI agent the team uses, are HR professionals correctly identifying when to override or escalate?

If completion is high but adoption is low, the gap is usually trust or workflow integration, not skill. Don't add more training, investigate the friction.

For maintenance, run `python scripts/verify_curriculum_exports.py` from the repository root. A source change requires updating and visually reviewing both downloads before recording a new manifest. The hash check detects drift; it does not establish semantic accuracy or native PowerPoint rendering.
