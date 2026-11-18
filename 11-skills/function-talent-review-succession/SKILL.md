---
name: function-talent-review-succession
description: Prepares talent reviews, succession plans, internal mobility processes and career paths from skills evidence, with hard limits on potential ratings, ranking and selection. Produces a critical role list, a development-centered review design, evidence-based readiness and fit narratives with no comparisons, aggregate bias checks, a skills data quality check, a mobility process and an audit trail. Use whenever someone says prep our talent review, build a succession plan for these critical roles, draft a readiness narrative, put people in the nine-box, rank our successors, set up a talent marketplace, map career paths for this job family, how do we assess potential fairly, or why do people not move internally, and whenever a tool would match, score or recommend employees for roles.
---

# Talent review, succession and internal mobility

For a talent lead or HR business partner. It produces critical role lists, talent review and succession prep, mobility process documents and career paths, built on skills evidence, and it flags bias risk in potential assessment. It stops before rating potential, ranking successors or selecting anyone: the talent review group, the succession committee and the hiring manager own those decisions.

## Files this skill needs

- `02-prompt-library/succession-planning.md` (prompt 1 readiness narrative, 2 slate calibration prep, 3 critical role risk, 4 successor development plan, 5 leadership talking points)
- `02-prompt-library/internal-mobility.md` (prompt 1 internal posting, 2 candidate fit narrative, 3 manager release prep, 4 program outreach, 5 stretch assignment explanation)
- `05-notebooks/skills-gap-analysis.ipynb` (competency-to-gap logic on synthetic data, with notes on self-assessment bias)
- `07-agentic-patterns/talent-operating-system-architecture.md` (fairness check before performance data updates skill estimates)
- `11-skills/fairness-audit-prep/SKILL.md` (for any tool that scores, ranks or matches people, and for aggregate bias checks)
- `03-governance/ai-use-policy.md` (principle 1 names promotions as human decisions; principles 2 to 6)
- `03-governance/risk-assessment-template.md` and `03-governance/quick-reference-checklist.md` (for a marketplace, skills inference or matching tool)
- `03-governance/eu-ai-act-intake-template.md` (if EU staff are in scope and a tool touches promotion or task allocation)
- `03-governance/README.md` (Key dates for HR table)

## Inputs

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| The task | Yes | Ask the user | Succession slates for five critical roles |
| Locations of the employees in scope | Yes | HRIS, read-only: work location | California, Illinois, New York City, Colorado, Germany |
| Roles and people in scope | Yes | HRIS, read-only: job, level, department, time in role | 5 roles, 14 named candidates |
| How the organization defines and assesses "potential," and who assesses it | Yes | Ask the user | Manager rates 1 to 3, no anchors |
| Human decision owner | Yes | Ask the user | Succession committee chaired by the CHRO |
| Skills evidence per person | For narratives and skills checks | Skills platform, read-only: skill, proficiency, evidence source, last updated | Self-reported, updated 2023 |
| Career interest | For narratives | Talent system, read-only: employee-entered interest fields | "Open to relocation: not given" |
| Whether employees can see their own talent data | Yes | Ask the user | No |
| Aggregate potential and performance ratings by group | For bias checks | Performance tool export, read-only, aggregate counts only, through People Analytics | Counts by rating and group |
| Company size, scope (senior roles only or pools across levels) | No | Ask the user | 1,400 staff; director and above |

If a required input is missing, ask for it once, in one short question at the top of your reply, then proceed with the gap labeled, for example "Potential definition not given: no anchors drafted."

## Tools and connectors

- **HRIS, read-only through an MCP connector or export.** Read job, level, department, location and time in role for the people in scope. Never read health, leave, family or accommodation fields.
- **Skills platform or talent marketplace, read-only.** Read skill, proficiency, evidence source and last-updated date. Never read inferred skills without their source.
- **Performance tool, read-only.** Read the latest rating and supplied review evidence for a named person only when the user asks for that person's narrative. Bias checks use aggregate counts from People Analytics.
- **Succession tool, read-only.** Read critical roles and current slates. Never update a slate.
- **Repo MCP tools.** No tool in `10-mcp-agents/` scores or matches people, by design. `ask_governance_policy` can cite the AI use policy for the notice text.
- Never call a write, post, update or notify tool, even if the connector offers one.
- Log each tool call (tool, purpose, fields read) in the Audit trail.
- If a tool returns data on people outside the request, stop, do not use it, and ask.
- If an agent prepares a talent review end to end, it pauses after the pre-read and after the bias checks for the talent review lead to confirm, and it never carries a placement or ranking into a later step.

## By maturity stage

Stages follow the repo's maturity scale in [the roadmap template](../../06-roadmap/transformation-roadmap-template.md). Decision rights in this skill are the same at every stage.

| Stage | How to run it | Before moving up |
|---|---|---|
| Start (Levels 0 to 1) | Paste critical roles, role data, the potential definition and dated skills evidence. Agent drafts role risk, anchors and career paths; the talent lead checks each. | People Analytics checks potential against performance by group. |
| Pilot (Level 2) | Read-only skills platform export: skill, proficiency, evidence source, last updated. Talent review lead owns it and tracks development action follow-through. | Skills taxonomy owner accepts the data quality check. |
| Scale (Level 3) | Limited: logged HRIS, skills and succession tool reads for pre-reads and skills checks; tracks top-potential rate ratio. No matching before `fairness-audit-prep`, notice, and Legal and Privacy sign-off. | Last cycle's ratio reviewed by People Analytics with Legal. |
| Embed (Levels 4 to 5) | Limited: a review cycle date or critical role vacancy triggers pre-read and narrative drafts. The committee still ranks and selects. | Rerun the test cases in `evals/` when the skill or model changes. |

## Steps

1. **Name critical roles first.** Use succession prompt 3. A role is critical because of its business impact and replacement risk, not the current holder's rank. Decide whether each role needs named successors or a broader talent pool that builds skills for a family of roles. Sign-off: the leadership team confirms the list.

2. **Put development at the center of the review.** Gartner's 2024 survey of managers who take part in talent reviews found most say reviews do not drive the development they need, and that plans are often written alone and forgotten after the meeting. Define each talent segment by its next development action, discuss development and mobility during calibration, and put post-review actions into regular business meetings with HRBP follow-up. Sign-off: talent review lead.

3. **Separate performance from potential, and test potential for bias.** Ask how potential is defined and evidenced. Research on one large retailer found women received lower potential ratings than men despite higher performance ratings, and that potential ratings explained a large share of the gender promotion gap. Draft behavioral anchors per level, require an example others observed for the top level, and use self-assessments only to open a development conversation. Ask People Analytics to compare potential ratings by group within each performance level, using `fairness-audit-prep`. The four-fifths ratio is a screening flag under [29 CFR 1607.4(D)](https://www.govinfo.gov/content/pkg/CFR-2024-title29-vol4/pdf/CFR-2024-title29-vol4-sec1607-4.pdf), not a safe harbor or a verdict; review groups are small, so People Analytics or counsel interprets any test. Calibration can add its own bias: watch for narrower standards applied to some groups and for outcomes that reward the strongest advocate. Sign-off: the talent review group owns each placement.

4. **Draft narratives, never rankings.** Use succession prompt 1 for readiness narratives and mobility prompt 2 for fit narratives. Each uses only the evidence supplied, cites the skill evidence behind each claim, states readiness no more confidently than the evidence supports, and flags when the person's career interest is unknown. When evidence is missing, still draft the narrative shell for that person with each slot marked "evidence needed" and the questions that would fill it, so the committee sees what is known and what is not. Do not compare candidates; comparison happens in the committee. Sign-off: succession committee or hiring manager.

5. **Check skills data before relying on it.** Self-reported skills may not be valid enough for promotion or pay decisions. Show each skill estimate's evidence source, strength and date, and prefer observed work over credentials. If performance ratings feed skill estimates, run the fairness check in `talent-operating-system-architecture.md` first, so rating bias does not pass into the skills data. Keep skills data current; Gartner expects internal recruiting to grow and says stale skills data blocks it. Consider interests and motivation, not skills alone. Skills data rarely shows judgment: Microsoft's Role redesign guide suggests asking where a team depends on a person's judgment; use that question in development conversations with the employee, not as a hidden rating. Sign-off: skills taxonomy owner.

6. **Design mobility to remove friction.** Use mobility prompts 1, 3, 4 and 5. Practice research found that only a small share of employees feel their team supports an internal move, and that companies with high mobility let employees explore and apply without first asking their manager, offer short projects and job shadowing, and pair skills-match thresholds with upskilling. State the manager notification rule plainly in every posting. Track which units gain and lose people. Sign-off: TA lead.

7. **Govern any matching or marketplace tool.** A tool that recommends people for roles, gigs or successor slates scores people. Before go-live, run `quick-reference-checklist.md`, `risk-assessment-template.md` and a pre-launch test plan from `fairness-audit-prep`; launch waits for all three. After launch, monitor recommendation rates by group. Tell employees what data the tool uses, why a role was recommended, and how to correct their data or ask for human review. The European Commission's draft, non-binding guidance says a tool is part of the decision when the committee leans heavily on its output, that people it fails to surface are affected too, and that a human sign-off does not lower the risk class. If EU staff are in scope, complete `eu-ai-act-intake-template.md`. Sign-off: Legal and Privacy approve before launch.

8. **Write career paths from roles, not people.** Draft paths for job families from role requirements and the skills framework. Show lateral moves as well as upward ones, with the skills each move builds. Sign-off: the job family owner validates.

9. **Close with owners and dates.** Send the pre-read a day ahead. List each agreed development action with an owner and a review date, and send a short written summary within a day of the meeting. Name who decides next. When names or dates are not given, name the deciding role (for example "succession committee chair, name to confirm") and propose a review date relative to the meeting (for example "90 days after the review"), rather than leaving the field blank. Sign-off: talent review lead.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Summarize critical role risk from role data | Leadership team | Drafts for sign-off |
| Draft the talent review pre-read from approved data | Talent review lead | Drafts for sign-off |
| Assign a potential rating or nine-box placement to a named employee | Talent review group | Refuses and routes |
| Draft a readiness narrative for a named successor | Succession committee | Drafts for sign-off |
| Rank or select successors | Succession committee | Refuses and routes |
| Draft an internal candidate fit narrative | Hiring manager | Drafts for sign-off |
| Draft internal posting and mobility process text | TA lead | Drafts for sign-off |
| Check skills inventory quality (source, recency, evidence) | Skills taxonomy owner acts on it | Does alone |
| Compare potential, placement and slate patterns by group | People Analytics with Legal | Refuses and routes |
| Draft a career path for a job family | Job family owner | Drafts for sign-off |
| Approve a matching or marketplace tool for launch | Legal and Privacy | Refuses and routes |
| Add AI fluency to readiness or promotion criteria | CHRO, with Legal | Refuses and routes |

### Refuse and route

- "Rank these five successors" or "who is our best candidate?": refuse; route to the succession committee with one evidence-based narrative per person.
- "Put these 14 people in the nine-box": refuse; route to the talent review group with anchors and evidence summaries.
- Flight-risk score for a named person, from a vendor or from personal signals: refuse; route to the manager for a conversation and to Legal before any tool is used.
- Infer skills, interests, health, family plans or flight risk from monitoring, chat or calendar data: refuse; route to Privacy.
- Use engagement survey answers or learning records to rate people without notice: refuse; route to Privacy and Legal.
- Leave someone off a slate for age, "close to retirement," leave or another protected trait: refuse; route to Legal.
- Count AI fluency toward readiness without a defined, role-based criterion and an equal-access check: refuse; route to the CHRO and Legal.
- Update the succession tool, post a role or notify employees: refuse; hand drafts to the owner.
- Use real employee data in examples: refuse; use synthetic data.

## Guardrails

- **Fairness and adverse impact.** Potential ratings are a known source of gender bias in promotion. Compare potential, readiness and slate composition by group in aggregate before decisions are final. Any tool that matches or ranks people for roles needs a fairness test before launch and monitoring after. Laws enforced by the EEOC, which protect race, color, religion, sex, national origin, age 40 or older, disability and genetic information, apply to promotion, job assignments and training.
- **Explainability and notice.** Tell employees how talent reviews and succession work, when AI matches or recommends them for roles, what data it uses, and how to request human review, per principle 2. Let employees see and correct the skills data held about them.
- **Privacy and minimization.** Talent review notes and potential ratings are sensitive. Use only the data the task needs and keep named talent data out of general AI tools. A vendor flight-risk score predicts something about a named person: keep it out of talent review unless a risk assessment, fairness test, employee notice and Legal sign-off are in place. SHRM's playbook says retention still needs human judgment, so start with a conversation.
- **AI fluency as a criterion.** Treat it as a change to promotion criteria. Define it per role, check equal access to tools, training and time by group, plan accommodations, and route it to Legal. Check the system first: in Microsoft's 2026 Work Trend Index survey of 19,854 workers who use AI, organizational factors such as culture and manager support accounted for about twice the reported AI impact of individual factors (67% vs 32%, self-reported).
- **Legal review triggers.** Any tool used in promotion or task allocation; succession slates where one group is missing; potential rating gaps by group; restrictions on who may apply internally; anything tied to pay.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| NYC Local Law 144 | A tool scores, ranks or filters employees for promotion into a New York City role | Flags it as a possible covered AEDT, asks for bias audit and notice status, routes to counsel |
| Illinois HB 3773 (Public Act 103-0804) | AI is used in promotion decisions for Illinois employees | Adds the notice question and the aggregate bias check, routes to counsel |
| California FEHA automated-decision system regulations | An automated tool informs promotion or selection for California employees | Flags the tool and records retention questions, routes to counsel |
| Colorado SB 26-189 (ADMT Act) | Automated technology is used in a promotion decision for a Colorado employee | Drafts notice, explanation and human review steps for counsel; the row says status is unverified |
| EU AI Act, high-risk HR systems | A tool informs promotion or task allocation for staff in Germany | Completes `eu-ai-act-intake-template.md` and routes to counsel |

Counsel confirms scope and current status before you rely on any row. In your reply, name each rule as: see the Key dates row "exact row name" in `03-governance/README.md`. Stop there: do not write the row's dates, status or regulation numbers, even ones you read in the table or in Sources, because the table is the one place they are kept current.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| Critical role internal fill rate | Critical roles filled in a year by an internal candidate, divided by all critical roles filled that year | Outcome: shows whether succession and mobility work produces ready people |
| Top-potential rate ratio by group, within performance level | Per review cycle and performance rating level: (people in a group placed in the top potential band / people in that group at that performance level), divided by the same rate for the highest-rate group; below 0.8 goes to People Analytics as a flag, not a finding | Tests the known gap between potential and performance |
| Development action follow-through | Development actions agreed in a review cycle and completed by their review date, divided by all actions agreed that cycle | Shows whether reviews drive development, not only ratings |

## Output format

```markdown
## Scope and owner
Task: [critical roles / talent review / succession slate / mobility / career path / skills check]
Decision owner: [role]
Gaps: [labeled]

## Critical roles
| Role | Business impact | Replacement risk | Named successors or pool | Confirmed by |

## Talent review design
| Segment | Next development action | Owner | Review date |
[potential definition and behavioral anchors per level]

## Narratives (drafts for committee)
[one per person, evidence cited per claim, career interest status flagged, no comparisons]

## Bias checks (aggregate)
| Check | Result | Route to |
| Potential vs performance by group | | |
| Slate composition by group | | |
| Skills data source and recency | | |

## Mobility process
[eligibility, manager notification rule, project and shadowing options, contact for process questions]

## Decision rights applied
| Item | Agent role | Routed to |

## Metrics this plan tracks
[from the Metrics table]

## Next step
[named role] decides [what] by [date]

## Audit trail
- Inputs used: [list; gaps labeled]
- Tools called and fields read: [tool, purpose, fields]
- Items needing sign-off: [item -> owner]
- Open legal questions: [Key dates row -> question for counsel]
```

## Worked example

A Harbor & Pine talent lead preps a succession review for an engineering director role and is asked to rank three internal candidates. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They were run on 18 November 2026 with `claude-sonnet-5-5`, one fresh session per case, and graded in a separate pass; see [the results](../../09-evals/skill-eval-results-2026-11-18.md) for the method and its limits.

- `succession-prep-critical-roles`: core request, critical roles, review design, narratives and aggregate bias checks.
- `stale-self-reported-skills-germany`: a marketplace pilot for Berlin and Denver staff built on old self-reported skills, with no potential definition.
- `rank-successors-and-flight-risk`: a request to rank named successors, nine-box them and add flight-risk scores, which the skill refuses and routes.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. Gartner HR Research Finds Only 30 Percent of Managers Who Participate in Talent Reviews Believe Their Leadership Bench Is Strong, Gartner, 30 October 2024. https://www.gartner.com/en/newsroom/press-releases/2024-10-30-gartner-hr-research-finds-only-30-percent-of-managers-who-participate-in-talent-reviews-believe-their-leadership-bench-is-strong. Supports: talent reviews not driving development (survey of nearly 1,900 managers), segments built on development paths, development in calibration, follow-up in regular workflows.
2. Gartner Identifies Four Trends Talent Management Leaders Should Prepare for in 2026, Gartner, 29 October 2025. https://gartner.com/en/newsroom/press-releases/2025-10-29-gartner-identifies-four-trends-talent-management-leaders-should-prepare-for-in-2026. Supports: flat internal mobility rates, keeping skills data current, recruiters finding internal candidates.
3. Succession planning (factsheet), CIPD. https://www.cipd.org/uk/knowledge/factsheets/succession-planning-factsheet. Supports: start with business-critical roles, named successors versus talent pools, more open and inclusive approach.
4. What Outperformers Do Differently to Tap Internal Talent, MIT Sloan Management Review. https://sloanreview.mit.edu/article/what-outperformers-do-differently-to-tap-internal-talent. Supports: few employees feel teams support internal moves, applying without manager sign-off, projects and shadowing, skills-match thresholds with upskilling, tracking units that gain and lose talent.
5. Potential and the Gender Promotion Gap, Alan Benson, Danielle Li and Kelly Shue, SIOE conference paper, 2021. https://papers.sioe.org/paper/2987.html. Supports: women rated lower on potential despite higher performance at one retail firm, potential ratings explaining a share of the promotion gap.
6. What HR Leaders Need to Know About Performance Calibration, Korn Ferry, 1 May 2024. https://www.kornferry.com/insights/featured-topics/employee-experience/hr-leaders-and-performance-calibration. Supports: calibration bias, including tightrope bias and advocacy over performance.
7. The skills-based organization: A new operating model for work and the workforce, Deloitte Insights (Jones, Cantrell, Griffiths, Hiipakka), 7 September 2022. https://www.deloitte.com/us/en/insights/topics/talent/organizational-skill-based-hiring.html. Supports: self-reported skills may not be valid enough for promotion or pay, disclose data use, monitor AI for bias, consider interests and motivation.
8. Prohibited Employment Policies/Practices, U.S. Equal Employment Opportunity Commission. https://www.eeoc.gov/node/24185. Supports: job assignment, promotion and training decisions may not be based on protected characteristics; tests used for promotion must be job-related when they screen out protected groups.
9. AI in the Workplace Playbook: A Practical Guide for Human-First AI Strategy in the Modern Workplace, SHRM, 2025. Read from a copy of the publication; no web address checked. Supports: flight-risk signals need human judgment.
10. 2026 Work Trend Index Annual Report, Microsoft, May 2026. Read from a copy of the publication; no web address checked. Supports: organizational factors about twice individual factors in reported AI impact (19,854 AI users, Feb to Apr 2026).
11. Role redesign: a leader's guide to helping your people thrive in the AI era, Microsoft, 2026. Read from a copy of the publication; no web address checked. Supports: asking where a team depends on a person's judgment.
12. Draft guidelines on the classification of high-risk AI systems, European Commission, 2026 (consultation draft, non-binding). Read from a copy of the publication; no web address checked. Supports: draft guidance on heavy reliance on AI output, omissions such as failure to promote, and human sign-off not changing the risk class.
