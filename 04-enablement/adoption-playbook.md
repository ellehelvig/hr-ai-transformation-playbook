# AI adoption playbook

Training builds skill. Adoption is a separate problem — most HR AI programs fail not because people can't use the tools, but because nothing in the surrounding system makes using them the path of least resistance. This playbook covers the change management work that has to happen alongside (not after) the [literacy curriculum](hr-ai-literacy-curriculum.md).

---

## Why enablement alone doesn't produce adoption

A team can complete every module of the literacy curriculum and still not use AI in their daily work six months later. The usual reasons:

- **No time was actually freed up.** If AI use is additive to an already-full workload instead of replacing a slower manual step, it gets deprioritized the first busy week.
- **No one modeled it.** If the HRBP's manager doesn't visibly use AI tools, "this is optional" is the message received, regardless of what training said.
- **The first bad output wasn't recoverable.** One early hallucination or wrong policy citation, without a quick way to report and learn from it, teaches the team "don't trust this" faster than ten good outputs teach "trust this."
- **Success wasn't visible.** If wins aren't shared, adoption stays individual and fragile instead of becoming a team norm.

Design against all four, not just the training gap.

---

## Stakeholder map

| Stakeholder | What they need from the program | What they can block |
|---|---|---|
| CHRO / HR leadership | Clear business case, risk posture they can defend upward | Budget, executive air cover |
| People managers | Confidence their team won't create legal exposure | Whether their team actually uses it day to day |
| HRBPs / practitioners | Tools that save real time, not extra process | Grassroots adoption or quiet non-use |
| Legal / Privacy | Governance framework they trust | Approval to deploy any use case touching employee data |
| IT / Security | Vendor and data security assurance | Technical access to tools |
| Employees (as end users, for agent-facing use cases) | Transparency, a human escalation path | Trust in the program if handled badly once |

Map your specific organization's version of this table before launch. The most common failure is treating HRBPs as the only stakeholder and skipping people managers, who control whether adoption becomes a team habit or an individual side project.

---

## A 90-day adoption roadmap

**Days 1-30 — Foundation**
- Deliver Module 1-2 of the literacy curriculum to a pilot group (one function or team, not the whole org)
- Identify 2-3 use cases from the [use case library](../01-use-cases/use-case-library.md) that solve a real, currently-annoying problem for the pilot group specifically
- Set up a lightweight feedback channel (a Slack channel, a shared doc) for "this worked" / "this didn't" reports

**Days 31-60 — Proof**
- Pilot group uses the 2-3 use cases in real work, not a sandbox
- Weekly 15-minute check-in: what worked, what broke, what would make this easier
- Document one concrete before/after example with a real time or quality metric — this becomes the story you tell everyone else

**Days 61-90 — Expansion**
- Share the pilot's concrete results with the next cohort before training them — proof beats persuasion
- Deliver Module 3-4 to the pilot group; deliver the full curriculum to the next cohort
- Identify one person per team as a peer resource (not a formal role, just "who do I ask when I'm stuck") — this scales faster than routing every question to the program owner

Do not attempt to roll out to the entire HR function simultaneously. A visible, credible pilot is worth more than a wide, shallow launch.

---

## Adoption metrics that actually mean something

Avoid vanity metrics (training completion, login counts). Track:

| Metric | What it tells you |
|---|---|
| % of pilot group using a tool 2+ weeks after training | Whether training converted to habit |
| Time saved per use case (self-reported, spot-checked) | Whether the value story is real |
| Escalation rate on agent-facing use cases | Whether governance boundaries are working as designed |
| Ratio of "this worked" to "this didn't" feedback reports | Early warning on trust erosion |
| Requests for new use cases from the field | The clearest signal that adoption is becoming pull, not push |

Review these monthly for the first two quarters, then fold into your standard [ROI reporting cadence](../08-roi-measurement/README.md).

---

## Handling the first public failure

Every program has one: a wrong answer, a bad draft that went out unedited, a hallucinated policy detail an employee caught. How this is handled in the first 90 days sets the trust ceiling for the next two years.

1. Acknowledge it specifically and quickly — don't let it circulate without a response from the program owner
2. Explain what went wrong in plain language (which verification step was skipped, not just "the AI made a mistake")
3. Fix the actual gap (a missing verify-before-use step, a prompt issue, a scope boundary) and say what changed
4. Do not respond by restricting the whole program if the failure was isolated — a proportionate fix builds more trust than an overcorrection

A well-handled failure in month one often does more for long-term adoption than an unbroken string of quiet successes, because it proves the governance actually works.

---

## Manager enablement (the most skipped step)

People managers who don't use AI themselves become adoption bottlenecks even if they don't intend to. Before wide rollout:

- Brief managers separately, ahead of their teams, on what's coming and why
- Give managers one visible use case they can model themselves (e.g., using a prompt from the [performance prompt library](../02-prompt-library/performance.md) for their own review drafting)
- Ask managers directly what would make them comfortable modeling this — don't assume the barrier is the same as their team's barrier

---

## Signs adoption is becoming self-sustaining

- Use case requests come from the field, unprompted
- People ask "is there a prompt for this" before asking "can someone help me with this"
- Feedback shifts from "does this work" to "can we make this better"
- A manager mentions using a tool in a context you didn't train them on — it's been generalized, not just followed by rote

At that point, shift program effort from adoption to [scaling and measurement](../08-roi-measurement/README.md).
