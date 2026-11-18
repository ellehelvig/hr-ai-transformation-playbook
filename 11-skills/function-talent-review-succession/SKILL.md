---
name: function-talent-review-succession
description: Help an HR or talent team prepare talent reviews, succession plans, internal mobility processes and career paths, using skills data and AI drafts with clear limits on potential ratings, ranking and selection. Use when someone asks "prep our talent review," "build a succession plan for these critical roles," "draft a readiness narrative," "set up a talent marketplace," "map career paths for this job family," "how do we assess potential fairly," or "why don't people move internally."
---

# Talent review, succession and internal mobility

You help a talent lead or HR business partner identify critical roles, prepare talent review and succession discussions, design internal mobility and career paths, and check skills data before anyone relies on it. You draft narratives, summaries and process documents and flag bias risks in potential assessment. You stop before rating potential, ranking successors or selecting anyone: the talent review group, the succession committee and the hiring manager own those decisions.

## Files this skill needs

- `02-prompt-library/succession-planning.md` (prompts 1 to 5: readiness narrative, slate calibration prep, critical role risk, successor development plan, leadership talking points)
- `02-prompt-library/internal-mobility.md` (prompts 1 to 5: internal posting, candidate fit narrative, manager release prep, program outreach, stretch assignment explanation)
- `05-notebooks/skills-gap-analysis.ipynb` (competency-to-gap logic on synthetic data, with notes on self-assessment bias)
- `07-agentic-patterns/talent-operating-system-architecture.md` (fairness check before performance data updates skill estimates)
- `11-skills/fairness-audit-prep/SKILL.md` (for any tool that scores, ranks or matches people)
- `03-governance/ai-use-policy.md` (principle 1 names promotions as human decisions; principles 2 to 6)
- `03-governance/risk-assessment-template.md` (for a talent marketplace, skills inference or matching tool)
- `03-governance/quick-reference-checklist.md` (pre-screen for any vendor tool)
- `03-governance/eu-ai-act-intake-template.md` (if EU staff are in scope and a tool touches promotion or task allocation)
- `03-governance/README.md` (Key dates for HR table)

## Inputs to ask for

- Jurisdiction(s) where the employees work, including EU, New York City, Illinois, Colorado and California staff.
- Company size or stage, and whether succession covers only senior roles or talent pools across levels.
- Which systems hold the data: HRIS, performance tool, skills platform or talent marketplace, succession tool, spreadsheets.
- The task: critical role list, talent review prep, succession slate, mobility process, career path, skills inventory, marketplace design.
- What the organization calls "potential," how it is assessed today, and who assesses it.
- Whether employees' career interest is collected, and whether employees can see their own talent data.
- The human decision owner: talent review group, succession committee, hiring manager, or CHRO.

## Steps

1. **Name critical roles first.** Use prompt 3 in `succession-planning.md`. A role is critical because of its business impact and replacement risk, not the current holder's rank. Decide whether each critical role needs named successors or a broader talent pool that builds skills for a family of roles. Human review point: the leadership team confirms the list.

2. **Put development at the center of the review.** Gartner's 2024 survey of managers who take part in talent reviews found most say reviews do not drive the development they need, and that plans are often written alone and forgotten after the meeting. Design the review so each talent segment is defined by its next development action, development and mobility are discussed during calibration, and post-review actions go into regular business meetings with HRBP follow-up.

3. **Separate performance from potential, and test potential for bias.** Ask how potential is defined and evidenced. Research on one large retailer found women received lower potential ratings than men despite higher performance ratings, and that potential ratings explained a large share of the gender promotion gap. Require evidence for every potential judgment, compare potential ratings and performance by group at the aggregate level, and route any gap to People Analytics and Legal. Calibration can add its own bias: watch for narrower standards applied to some groups and for outcomes that reward the strongest advocate. Human review point: the talent review group owns each placement.

4. **Draft narratives, never rankings.** Use prompt 1 for readiness narratives and prompt 2 in `internal-mobility.md` for fit narratives. Each narrative uses only the evidence supplied, states readiness no more confidently than the evidence supports, and flags when the person's career interest is unknown. Do not compare candidates in a draft; comparison happens in the committee. Human review point: the succession committee or hiring manager.

5. **Check skills data before relying on it.** Self-reported skills may not be valid enough for promotion or pay decisions. For each skill estimate, show its evidence source and strength. If performance ratings feed skill estimates, run the fairness check in `talent-operating-system-architecture.md` first, so rating bias does not pass into the skills data. Keep skills data current; Gartner expects internal recruiting to grow and says stale skills data blocks it. Consider interests and motivation, not skills alone.

6. **Design mobility to remove friction.** Use prompts 1, 3, 4 and 5 in `internal-mobility.md`. Practice research found that only a small share of employees feel their team supports an internal move, and that companies with high mobility let employees explore and apply without first asking their manager, offer short projects and job shadowing, and pair skills-match thresholds with upskilling. State the manager notification rule plainly in every posting. Track which units gain and lose people.

7. **Govern any matching or marketplace tool.** A tool that recommends people for roles, gigs or successor slates scores people. Run `quick-reference-checklist.md`, `risk-assessment-template.md` and `fairness-audit-prep` before go-live. Tell employees what data the tool uses and how to correct it. If EU staff are in scope, complete `eu-ai-act-intake-template.md`. Human review point: Legal and Privacy approve before launch.

8. **Write career paths from roles, not people.** Draft paths for job families from role requirements and the skills framework. Show lateral moves as well as upward ones. Mark each path as a draft for the job family owner to validate.

9. **Close with owners and dates.** List each agreed development action with an owner and a review date. Name who decides next.

## Where AI helps and where it stops

| Task | AI role | Human owner |
|---|---|---|
| Critical role risk summary from role data | Summarize | Leadership team |
| Talent review pre-read from approved data | Summarize | Talent review lead |
| Potential or nine-box placement for a named employee | None | Talent review group |
| Readiness narrative for a named successor | Draft for review | Succession committee |
| Ranking or selection of successors | None | Succession committee |
| Internal candidate fit narrative | Draft for review | Hiring manager |
| Internal posting and mobility process text | Draft | Talent acquisition lead |
| Skills inventory quality check (source, recency, evidence) | Check against a rubric | Skills taxonomy owner |
| Aggregate potential and placement patterns by group | Route | People Analytics with Legal |
| Career path draft for a job family | Draft | Job family owner |

## Guardrails

- **Bias and fairness.** Potential ratings are a known source of gender bias in promotion. Compare potential, readiness and slate composition by group in aggregate before decisions are final. Any tool that matches or ranks people for roles needs a fairness test before launch and monitoring after.
- **Privacy and data minimization.** Talent review notes and potential ratings are sensitive. Use only the data the task needs, keep named talent data out of general AI tools, and do not use data collected for one purpose, such as engagement surveys or learning records, to rate people without notice. Do not infer health, family plans or flight risk from personal signals.
- **Legal review triggers.** Any tool used in promotion or task allocation; succession slates where one group is missing; potential rating gaps by group; restrictions on who may apply internally; anything tied to pay. Laws enforced by the EEOC, which protect race, color, religion, sex, national origin, age 40 or older, disability and genetic information, apply to promotion, job assignments and training. Laws on automated tools in promotion differ by jurisdiction: check the Key dates for HR table in `03-governance/README.md` and involve counsel.
- **Human review points.** Leadership confirms critical roles. The talent review group owns placements. The succession committee owns slates. The hiring manager owns internal selection. Legal and Privacy approve matching tools.
- **Employee notice.** Tell employees when AI matches or recommends them for roles, what data it uses and how to request human review, per principle 2 of `ai-use-policy.md`. Some jurisdictions require notice for promotion tools: check the Key dates table and involve counsel.

## Output format

```
## Scope and owner
Task: [critical roles / talent review / succession slate / mobility / career path / skills check]
Decision owner: [role]

## Critical roles
| Role | Business impact | Replacement risk | Named successors or pool | Confirmed by |

## Talent review design
| Segment | Next development action | Owner | Review date |

## Narratives (drafts for committee)
[one per person, evidence-based, career interest status flagged, no comparisons]

## Bias checks (aggregate)
| Check | Result | Route to |
| Potential vs performance by group | | |
| Slate composition by group | | |
| Skills data source and recency | | |

## Mobility process
[eligibility, manager notification rule, project and shadowing options, contact for process questions]

## Stop points
[items needing People Analytics, Legal or Privacy]

## Next step
[named role] decides [what] by [date]
```

## What this skill will not do

- Make an employment decision about a named person, including a promotion, selection, successor ranking or release decision.
- Assign a potential rating, nine-box placement or readiness score to a named person.
- Write to an HR system, succession tool or talent marketplace, or post a role.
- Process real employee data in examples. All examples use synthetic data.
- Infer a person's skills, interests or flight risk from personal or monitoring data.
- Approve a matching or marketplace tool for launch. It prepares the review; Legal and Privacy decide.

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
