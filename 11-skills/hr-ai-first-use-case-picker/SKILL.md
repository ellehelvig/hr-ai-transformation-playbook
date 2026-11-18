---
name: hr-ai-first-use-case-picker
description: Screens a list of candidate HR AI ideas, scores the ones that pass with the playbook's prioritization matrix, and recommends one or two first pilots for an HR team at maturity Levels 0 to 2, each with a one-line success metric, the phase gate that ends the pilot, the human sign-off point, and a hand-off to hr-ai-use-case-intake. Shows the full scoring table so the team can disagree, and screens out ideas that select, score or rank people or infer emotion as first pilots. Use whenever someone says "where should HR start with AI," "which AI idea should we pilot first," "pick our first AI pilot," "we have a list of AI ideas, which one first," "what is a safe first AI project for HR," "we only have spreadsheets, what can we try," or "the CEO wants our first AI project to pick who to lay off," and whenever an HR team with no live AI pilot has more ideas than capacity.
---

# HR AI first use case picker

This skill serves the HR leader and governance owner of a team about to run its first one to three AI pilots (Levels 0 to 2 on the maturity scale). It produces a screened candidate list, a scoring table built on the playbook's prioritization matrix, and one or two recommended first pilots, each with a success metric, a phase gate, a human sign-off point, and a hand-off to `hr-ai-use-case-intake`. It drafts for sign-off. It does not write the full intake card for one idea (that is `hr-ai-use-case-intake`), assess the whole function's maturity (that is `hr-ai-readiness-assessment`), approve a launch, or decide anything about a named person.

## Files this skill needs

- `01-use-cases/prioritization-matrix.md` (eligibility gates, the five scoring dimensions, weights, formula, priority tiers)
- `01-use-cases/use-case-library.md` (candidate ideas when the user has none; AI approach, effort, key risk, starter resources; the note on effort without clean HRIS data)
- `01-use-cases/intake-template.md` (the fields the hand-off pre-fills)
- `06-roadmap/transformation-roadmap-template.md` (maturity scale, Phase 1 target use cases, Phase 1 exit gate, success metrics to instrument)
- `04-enablement/adoption-playbook.md` (30, 60, 90 day pilot stages; expand, pause, or stop criteria; measuring the entire task)
- `03-governance/ai-use-policy.md` (prohibited uses, approved tool categories)
- `03-governance/risk-assessment-template.md` (sections 6 to 8: risk factors, approvals, launch conditions)
- `03-governance/pay-equity-governance.md` (the stop for anything touching pay)
- `03-governance/README.md` (the Key dates for HR table)
- `11-skills/hr-ai-use-case-intake/SKILL.md`, `11-skills/fairness-audit-prep/SKILL.md`, `11-skills/hr-ai-vendor-review/SKILL.md`, `11-skills/eu-ai-act-hr-classifier/SKILL.md`

## Inputs

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| Candidate ideas, one line each | No: if none, draw from the library | Ask the user | Policy Q and A drafting; JD rewriting; resume ranking |
| Maturity level on the roadmap scale | Yes | Ask the user, or the output of `hr-ai-readiness-assessment` | Level 1: scattered assistant use, no shared prompts |
| Headcount by country and US state | Yes | Ask the user, or HRIS, read-only: headcount by work location | 1,400: California, Illinois, NYC, Colorado, Germany |
| Systems in use and whether data is in an HRIS or spreadsheets | Yes | Ask the user | HRIS, ATS, LMS; or spreadsheets only |
| HR team size and hours free for a pilot | Yes | Ask the user | 6 people, about 4 hours a week each |
| Current People Team priorities or OKRs | Yes | Ask the user | Cut policy question backlog; hire 40 engineers |
| Approved AI tools and any AI already in use | No | Ask the user, or the AI inventory export, read-only | Company assistant approved for drafting |
| Works council, union, or employee representatives | Yes where staff are outside the US | Ask the user | Works council at the German entity; or none known |
| HR leader and governance owner who sign off | Yes | Ask the user | VP People; HR technology lead |

If a required input is missing, ask for it once, in one short question at the top of your reply. Then proceed with the gap labeled "Not provided: [input]" in the output and in the audit trail. If the maturity level is unknown, take the user's self-report against the roadmap scale, label it self-reported, and suggest `hr-ai-readiness-assessment` for a fuller view.

## Tools and connectors

An agent may read, never write. This skill needs no employee or candidate records. Connect through MCP connectors or exports with read-only scopes, and request only these fields:

- **HRIS:** headcount by country and US state. No names, IDs, or job data.
- **AI inventory export (from `function-hr-ai-governance`):** tool, use, owner, lifecycle status, so a pick does not duplicate a live pilot.
- **Service desk or case system export:** ticket counts by category for the last full quarter, to support the time savings score. No ticket text.
- **LMS:** AI literacy completion counts by HR role, for the phase gate's training line.
- **Repo MCP tool:** `policy_qa` (`ask_governance_policy`) cites `03-governance/` passages, such as the approved tool categories, when the skill explains a screen. It is also the reference pattern for a policy Q and A pilot: it returns no match rather than guessing.

Rules for every tool call:

- Never call a write, send, update, configure, enable, or purchase tool, even if the connector offers one.
- Log each call in the Audit trail: tool, purpose, fields read.
- If a tool returns data on named people, or fields outside this list, stop, do not use it, and ask the user.

## By maturity stage

Stages follow the repo's maturity scale in [the roadmap template](../../06-roadmap/transformation-roadmap-template.md). Decision rights in this skill are the same at every stage, and the first-pilot screen never loosens.

| Stage | How to run it | Before moving up |
|---|---|---|
| Start (Levels 0 to 1) | No connectors. Paste the ideas, or none, plus headcount by country, systems, and team hours. The HR leader checks every score. | Picks signed, and each has a signed intake card and risk tier from `hr-ai-use-case-intake`. |
| Pilot (Level 2) | Add one read-only export: the AI inventory (tool, use, owner, status), so picks do not duplicate a live pilot. | The first pilot reached its phase gate, metric recorded as met or missed. |
| Scale (Level 3) | Limited: first pilots for a team or region still at Level 1 to 2, or a new HR area. Tracks pilots meeting their metric. | Both CHRO metrics reported for two quarters. |
| Embed (Levels 4 to 5) | Limited: runs on the intake queue export when the quarterly prioritization review opens, still drafting for sign-off. | Rerun the test cases in `evals/` when the skill or model changes. |

## Steps

1. **Confirm the starting point.** Record the inputs. At Level 3 or above, point to the roadmap's Phase 2 for function-wide sequencing. Plan one pilot at Level 0 and up to two at Levels 1 to 2: the roadmap runs one team, one region, one use case at a time. The agent does this alone.

2. **Build the candidate list.** Use the user's ideas, merging duplicates. If they gave none, draw six to eight `use-case-library.md` rows that are Augment or Assist, Low effort, tied to a stated priority, and ideally with a starter resource. Without clean HRIS data or an HR tech team, the library says to add one level to every effort estimate, so favor ideas with no system integration: drafting from documents the team already holds. Mark each row's source. The agent does this alone.

3. **Apply the first-pilot screen.** This screen is the skill's own rule and is stricter than the matrix. An idea cannot be a first pilot if it:
   - selects, scores, ranks, filters, or matches people, including resume screening or ranking, layoff or redundancy selection, performance rating suggestions, flight-risk or attrition scores for individuals, promotion or succession picks, and allocating tasks to or monitoring individual workers;
   - infers emotion, mood, or sentiment of identifiable workers, from text, voice, or video;
   - touches pay in any form (stop and route to employment counsel under `pay-equity-governance.md`);
   - is a prohibited use or "Not approved" in `ai-use-policy.md`.

   Screened ideas are not scored. Each gets "Not a first pilot" and what it needs first. People-selection ideas go to `fairness-audit-prep` and the governance owner; they can come later as decision support with an audit plan, a named human decision owner, notice, and counsel review. Emotion inference goes to Legal. The agent does this alone and explains each call.

4. **Draft the eligibility call.** Record the four matrix gates for each idea that passed (purpose and accountability, data and access, decision boundary, risk and evidence) and call it eligible, hold, or stop with the evidence. A gate the user's facts support but no reviewer has accepted reads "eligible, to confirm in intake". Missing evidence is hold; an unacceptable design is stop. Neither gets a score. Sign-off: the accountable reviewer per gate, in the intake.

5. **Score with the matrix, and show the work.** Score each eligible idea 1 to 5 against the matrix anchors for strategic alignment, employee or manager impact, time savings, data readiness, and implementation feasibility. Compute (Strategic x 0.25 + Impact x 0.20 + Time x 0.15 + Data x 0.15 + Feasibility x 0.15) / 0.90 to two decimals and assign the matrix tier. Give one line of reasoning per score, and label time savings as assumptions until measured. Add three columns beside the score, never averaged into it, since the matrix assesses risk separately:
   - **Risk tier preview:** Low, Medium, or High from section 6 of `risk-assessment-template.md`, with this skill's conservative rule that any High factor makes the idea High. `hr-ai-use-case-intake` sets the real tier.
   - **Reversible:** can the team switch the pilot off and return to manual work the same day (yes, partly, no).
   - **Integration needed:** none, export, or connector.

   Invite the user to change any score, and recompute. The agent does this alone.

6. **Pick one or two first pilots.** Take the highest tier first. Within a tier, prefer in order: Low risk preview, reversible, no integration, a library starter resource, a baseline measurable in two weeks. State why each pick beat the next-best idea. Sign-off: HR leader with the governance owner.

7. **Draft the pilot frame for each pick.**
   - **Success metric:** one line with numerator, denominator, period, and baseline source; target "[Set after baseline]". Pair efficiency with a quality check, per the adoption playbook's "Measure the entire task".
   - **Phase gate:** the roadmap's Phase 1 exit criteria fitted to this pilot: change on the metric against baseline, participants through literacy Modules 1 to 2, no material governance issue, sponsor briefed. Propose a date about six weeks after launch (the roadmap's 4 to 6 week results summary) and apply the adoption playbook's expand, pause, or stop criteria there.
   - **Human sign-off point:** the step where a named role reviews each output before it reaches anyone, and who can pause the pilot.
   - **Scope:** one team, one task, synthetic rehearsal first per the adoption playbook's days 1 to 30.
   - **Hand-off:** "Next: run `hr-ai-use-case-intake` for the full intake card and risk tier," pre-filling name, description, AI approach, data, human review gate, and metric. No pilot launches before that card is signed.

   Sign-off: HR leader for the metric and gate; governance owner for the hand-off.

8. **Flag the gates outside HR's control.** For staff outside the US, ask whether a works council or employee representatives exist. For any pilot that touches staff data or could monitor staff, list consultation as an open question for counsel and labor relations, settled before launch. Add the Regulation map rows that apply; route any purchase to `hr-ai-vendor-review`. Sign-off: governance owner.

9. **Assemble the output.** Fill the Output format, including "Not now, and when" and the Audit trail. Sign-off: HR leader and governance owner; nothing launches from this output.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| List candidate ideas, from the user or the library | Fixed rule | Does alone |
| Apply the first-pilot screen and explain each call | Fixed rule | Does alone |
| Score eligible ideas with the matrix and explain each score | Fixed rule; the HR leader may change any score | Does alone |
| Draft the eligibility call per matrix gate | Accountable reviewer per gate | Drafts for sign-off |
| Recommend one or two first pilots | HR leader with the governance owner | Drafts for sign-off |
| Draft each pilot's success metric and baseline method | HR leader as sponsor | Drafts for sign-off |
| Draft each pilot's phase gate and gate date | HR leader and governance owner | Drafts for sign-off |
| Name the human sign-off point and pause owner | HR leader with the pilot operator | Drafts for sign-off |
| Start a first pilot that selects, scores, or ranks people or infers emotion | Governance owner, after `fairness-audit-prep` and counsel | Refuses and routes |
| Buy, switch on, or configure a vendor AI tool | Oversight owner after `hr-ai-vendor-review` | Refuses and routes |
| Declare a use case compliant or not high-risk | Counsel, with `eu-ai-act-hr-classifier` for EU staff | Refuses and routes |
| Launch a pilot | Reviewers in section 7 of `risk-assessment-template.md`, after intake | Refuses and routes |

### Refuse and route

- "Make our first AI pilot pick who to lay off next quarter": refuse; route to the governance owner, HR leadership, and counsel, with `fairness-audit-prep` before any people-selection tool is considered. Selection stays human; any later AI role is decision support under audit. Offer a low-risk first pilot instead.
- "Start with resume screening or ranking": refuse as a first pilot; route to `fairness-audit-prep` and the governance owner. It can come later with an audit plan and a human reviewer of every shortlist. Offer JD rewriting or interview questions instead.
- "Have AI suggest performance ratings" or "score flight risk for each engineer": refuse as a first pilot; route to the governance owner and `fairness-audit-prep`. The policy lists performance rating automation as not approved.
- "Read team mood from meeting audio" or "score sentiment per employee": refuse; route to Legal before any pilot.
- "Buy the vendor's AI module and turn it on": refuse to buy or configure; route to `hr-ai-vendor-review`.
- "Confirm this pilot is compliant" or "tell us it is not high-risk": refuse; route to counsel and `eu-ai-act-hr-classifier`.
- "Use AI to set raises" as a first pilot: stop; route to employment counsel under `pay-equity-governance.md`.
- Real employee or candidate data pasted into the request: refuse to process it; ask for a synthetic or de-identified version.

## Guardrails

- **Fairness and adverse impact.** No first pilot selects, scores, ranks, or matches people. When such an idea comes back later, it goes through `fairness-audit-prep` before go-live; the four-fifths ratio there is a screening flag under 29 CFR 1607.4(D), not a verdict.
- **Explainability and notice.** Each pick names who reviews outputs and what staff are told. An employee-facing pilot needs notice and a human route before launch, per section 5 and section 8 of `risk-assessment-template.md`.
- **Privacy and minimization.** Rehearse on synthetic data first. Prefer pilots that draft from documents the team already holds over pilots that read employee records. Never paste real employee data into a tool the policy has not approved for it.
- **No fabricated numbers.** Scores are judgments with stated reasons. Time savings, adoption, and ROI are planning assumptions until measured; never cite a benchmark or survey figure from memory.
- **Legal review triggers.** Staff outside the US, any works council or union, any employee-facing assistant, any idea touching pay, any idea the screen removed that the sponsor wants to revisit. Point to the Key dates for HR table; do not restate dates.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| EU AI Act, emotion recognition at work (Article 5(1)(f)) | An idea infers emotions of workers | Screens it out and routes to Legal before any pilot |
| EU AI Act, high-risk HR systems | An idea would be used in recruiting, promotion, termination, task allocation, or performance monitoring of EU workers | Screens it out as a first pilot; routes to `eu-ai-act-hr-classifier` when it comes back |
| EU AI Act, transparency (Article 50) | A pick puts an AI assistant in front of EU staff | Adds telling people they are talking to AI to the pilot's launch conditions |
| EU AI Act, AI literacy (Article 4) | Pilot participants operate or use the AI tool | Adds literacy training completion to the phase gate |
| NYC Local Law 144 | A screened hiring or promotion idea returns later for NYC roles | Notes bias audit and notice as preconditions; counsel confirms coverage |

Counsel confirms scope and current status before you rely on any row. In your reply, name each rule as: see the Key dates row "exact row name" in `03-governance/README.md`. Stop there: do not write the row's dates, status or regulation numbers, even ones you read in the table or in Sources, because the table is the one place they are kept current.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| Pilots meeting their metric at the gate | Pilots whose success metric met the sponsor's post-baseline target on or before the phase gate date, divided by all pilots whose gate date fell in the half-year | Shows whether first picks deliver, not just launch |
| Intake before launch | Pilots launched in the quarter with a completed intake card and a signed risk tier dated before launch, divided by all pilots launched in the quarter | Shows whether governance runs ahead of pilots |
| HR hours redirected per month | In the pilot workflow, (mean minutes per task before minus mean minutes per task after, both on a defined sample of the same task type, review and rework included) times monthly task volume, divided by 60; reported as observed | Shows capacity actually freed, which is capacity, not cash |

## Output format

```
## First pilot pick (DRAFT for [HR leader] and [governance owner])
Maturity level: [n], self-reported or from hr-ai-readiness-assessment
Scope: headcount by country, systems, HR team hours, priorities
Gaps: Not provided: ...

## Candidates and first-pilot screen
| # | Idea | Source (user or library row) | Screen: pass or not a first pilot | Why | Route |

## Eligibility (matrix gates)
| Idea | Purpose and accountability | Data and access | Decision boundary | Risk and evidence | Call |

## Scoring table (prioritization matrix)
| Idea | Strategic | Impact | Time | Data | Feasibility | Weighted | Tier | Risk tier preview | Reversible | Integration |
Arithmetic per row:
One-line reason per score:
Change any score and the table is recomputed.

## Recommended first pilots
### Pilot 1: [name]
Why this one, and why not the next-best idea:
Success metric:
Baseline: what, where, over what period
Phase gate (proposed date):
Human sign-off point and pause owner:
Scope:
Open gates (works council, notice, literacy, vendor review):
Hand-off: run hr-ai-use-case-intake for the full intake card and risk tier. Pre-filled: ...

## Not now, and when
| Idea | Why not first | What it needs first | Route |

## Decision rights calls in this output
| Item | Agent role | Routed to |

## Metrics this plan tracks
| Metric | Baseline source | First reading |

## Audit trail
Inputs used:
Tools called (tool, purpose, fields read):
Items needing sign-off (item, owner):
Open legal questions:
```

## Worked example

Harbor & Pine, a fictional company at Level 1, brings seven ideas; the skill screens out two that score or rank people, holds one, scores four, and recommends two first pilots. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They were run on 18 November 2026 with `claude-sonnet-5-5`, one fresh session per case, and graded in a separate pass; see [the results](../../09-evals/skill-eval-results-2026-11-18.md) for the method and its limits.

- `eight-ideas-pick-first`: eight mixed-risk ideas; screen, score with the matrix, and pick first pilots end to end.
- `no-ideas-spreadsheets-germany`: no ideas, a 90-person company with staff in Germany and only spreadsheets; draw from the library, favor no-integration pilots, flag the works council.
- `ceo-layoff-first-pilot`: the CEO wants the first pilot to pick who to lay off; refuse and route.

## Sources

No external source was added for this skill. The method rests on these repo documents, each read on 18 November 2026:

1. `01-use-cases/prioritization-matrix.md`. Supports: eligibility gates, the five dimensions, weights, formula, and tiers.
2. `01-use-cases/use-case-library.md`. Supports: candidate ideas, AI approach, effort and risk ratings, and the effort note for teams without clean HRIS data.
3. `06-roadmap/transformation-roadmap-template.md`. Supports: the maturity scale, Phase 1 target use cases, exit gate, and 4 to 6 week results summary.
4. `04-enablement/adoption-playbook.md`. Supports: staged rehearsal, measuring the entire task, and expand, pause, or stop.
5. `03-governance/ai-use-policy.md`. Supports: prohibited uses and approved tool categories.
