---
name: function-performance-management
description: Produces goal checks, review drafts traced line by line to a manager's dated evidence, calibration briefings, four-fifths screening flags on aggregate rating counts, employee-facing explanations and PIP drafts, each with an audit trail, while every rating and decision stays with a named human. Use whenever someone says "help me write this performance review," "turn my notes into a review draft," "prep me for calibration," "check these goals," "summarize mid-year feedback," "draft a PIP," "check our ratings for bias," or "can we use AI in our review cycle," and whenever a request would have AI rate, rank, monitor or read emotion from a named employee.
---

# Performance management

This skill serves HR business partners, calibration leads and people managers. It drafts and checks performance work from the manager's own evidence. It stops before any rating, calibration outcome, PIP decision or pay link: those belong to the manager, the calibration group, the HRBP and, where needed, counsel.

## Files this skill needs

- `02-prompt-library/performance.md` (prompts 1 to 5: review draft, calibration prep, goal feedback, PIP draft, mid-year synthesis)
- `03-governance/ai-use-policy.md` (principle 1 names performance ratings and PIPs as human decisions; principles 2, 4, 5 and 6 on notice, data, accuracy and logging)
- `03-governance/quick-reference-checklist.md` (pre-screen before any tool touches review data)
- `03-governance/risk-assessment-template.md` (sections 3 to 5 if a tool will score, summarize or flag employees)
- `03-governance/README.md` (Key dates for HR table)
- `11-skills/fairness-audit-prep/SKILL.md` (any tool or analysis that produces ratings, rankings or rating analytics)
- `03-governance/pay-equity-governance.md` (only if ratings feed pay)

## Inputs

If a required input is missing, ask for it once, in one short question at the top of your reply, then proceed with the gap labeled `[GAP: what is missing]` in the output.

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| Task | Yes | Ask the user | Year-end review draft |
| Work location of each person in scope | Yes | HRIS, read-only: work location, country | Illinois; Germany |
| Cycle design: ratings or not, self-ratings or not, pay or promotion link this cycle | Yes | Ask the user | 4-point scale, no self-rating, no pay link at mid-year |
| Manager's evidence in dated bullets across the whole period | Yes, for drafts | Ask the user (the manager supplies it) | "14 Mar: shipped billing migration two weeks early" |
| Agreed goals for the period | Yes, for drafts and goal checks | Performance system, read-only: goal text, dates, status | 4 goals, Q1 to Q4 |
| Decision owner | Yes | Ask the user | Manager, for the rating |
| Open accommodation, leave or complaint (yes or no only) | Yes, before any PIP | Ask the HRBP | "Yes, accommodation request open" |
| Aggregate proposed rating counts by group | Only for a distribution screen | People Analytics export, aggregate only | Proposed "Exceeds" by sex, two groups |
| AI tool in use and whether approved for review data | Yes | Ask the user | Approved enterprise assistant |

## Tools and connectors

Work through MCP connectors or exports, read-only, with the minimum fields:

- Performance system: goal text and dates, check-in dates, the manager's own notes for the people in the request.
- HRIS: job, level, manager, work location. No leave, health or demographic fields.
- People Analytics export: aggregate counts by group, never row-level demographics.
- Repo MCP tools in `10-mcp-agents/`: `lint_jd_language` (in `resume_screen/`) flags gender-coded and protected-class-proxy wording in any HR text, including a review draft; `ask_governance_policy` (in `policy_qa/`) cites the governance section behind a stop point.

Never call a write, send or update tool, even if the connector offers one: no rating entry, no status change, no message to an employee. Log each tool call (tool, purpose, fields read) in the output's audit trail. If a tool returns data on people outside the request, stop, do not use it, and ask.

## By maturity stage

Stages follow the repo's maturity scale in [the roadmap template](../../06-roadmap/transformation-roadmap-template.md). Decision rights in this skill are the same at every stage.

| Stage | How to run it | Before moving up |
|---|---|---|
| Start (Levels 0 to 1) | Manager pastes dated evidence, goal text and cycle design, with no leave or health details. Agent drafts from the ledger; the manager checks each `[UNTRACED]` mark. | HRBP reviews sample drafts for recency skew. |
| Pilot (Level 2) | Read-only performance system export: goal text, dates, check-in dates, the manager's notes. HRBP lead owns it and tracks evidence traceability rate. | Employee notice on AI assistance is live. |
| Scale (Level 3) | Logged reads of performance system and HRIS job fields, plus `lint_jd_language`. People Analytics tracks top-rating selection ratio by group. Scoring tools need `fairness-audit-prep` first. | Last cycle's ratio reviewed by People Analytics with counsel. |
| Embed (Levels 4 to 5) | Limited: cycle events trigger goal checks, drafts and calibration briefings. PIP drafts start only when the HRBP asks. Managers sign reviews; calibration groups decide. | Rerun the test cases in `evals/` when the skill or model changes. |

## Steps

Run the work as a workflow with hard checkpoints. The agent never passes a checkpoint on its own: evidence ledger confirmed (manager), draft signed (manager), rating flags interpreted (People Analytics), PIP cleared (HRBP and Legal).

1. **Set the cycle shape.** Confirm what the cycle produces and when. Current practice mixes frequent feedback that feeds the formal review, midyear calibration and regular check-ins so year-end outcomes hold no surprises; some firms keep ratings but drop self-ratings. Record this organization's choice. If leadership wants the cycle to encourage new ways of working, raise whether goals credit attempts to redesign work, not only results: in Microsoft's 2026 Work Trend Index, only 13% of AI users surveyed said they are rewarded for reinvention when results are not met. Do not recommend dropping ratings or changing pay links. Sign-off: HR leadership.

2. **Check goals against a rubric.** Use prompt 3 in `performance.md`. Check each goal for a clear outcome, a measure, a date and a link to team goals. Where work is shared with AI agents, check that each goal names an outcome and quality bar a person owns, not the volume of AI output; separate outcomes owned from activities done. If the organization has a skills taxonomy, tag each goal with the skills it exercises, so skills evidence builds from delivered work rather than course completions or credentials. Report gaps per goal; never silently rewrite an agreed goal. Sign-off: employee and manager.

3. **Build the evidence ledger before drafting.** Ask the manager for dated examples for each accomplishment and development area across the whole period. Record each item's date, source (observed work, delivered output, stakeholder feedback the manager supplied) and goal. Invite the employee's own evidence through the manager so the record is not one-sided. If most items come from the last quarter of the period, flag a possible recency skew and ask the manager for earlier examples: a draft cannot fix thin evidence. Sign-off: the manager confirms the ledger is complete.

4. **Draft the review from the ledger only.** Use prompt 1. The manager states the proposed rating; you do not suggest one. Every claim in the draft must trace to a ledger item; mark any sentence you could not trace `[UNTRACED]`. Remove generic praise and hedging. Keep to this pattern: in the European Commission's non-binding draft guidance on high-risk classification, a writing assistant that polishes a manager's finished write-up and flags biased wording, with the manager re-checking, may fall outside high risk, while a tool that monitors or evaluates performance is high risk even when the manager formally decides but relies heavily on its output. Every sentence traces to a dated ledger item: do not compute new figures (such as a percentage change from two numbers), and do not add weight words the manager did not use, such as "high-impact" or "costly". A summary that leans toward a rating is a suggested rating. Sign-off: the manager reads, edits and signs the final text, and decides whether to disclose AI assistance under local policy.

5. **Run a language and bias check.** Check for invented facts, personality statements instead of behavior, and words that apply different standards to different people; run `lint_jd_language` on the text. Where the manager has several drafts at the same proposed rating, flag any draft that rests on fewer or vaguer ledger items, without comparing or ordering the people. Check that AI use itself is not rated unless the organization has defined it as a job requirement for that role; rewarding tool use alone can reward speed over quality. Sign-off: the manager, then the HRBP for flagged items.

6. **Prepare calibration, do not run it.** Use prompt 2 to build a briefing from data the manager may already see. Before names are discussed, help the calibration lead write down what each rating level means and which evidence counts. Flag known risks: a pull toward the middle rating, narrower standards applied to women and people from under-represented groups, and outcomes that reward the strongest advocate rather than the strongest work. Allow enough time per person. If People Analytics supplies aggregate proposed-rating counts by group, compute the four-fifths ratio as a screening flag under the Uniform Guidelines, [29 CFR 1607.4(D)](https://www.govinfo.gov/content/pkg/CFR-2024-title29-vol4/pdf/CFR-2024-title29-vol4-sec1607-4.pdf), not a safe harbor or a verdict. Small groups need a statistical test, and People Analytics or counsel interprets the result; follow `fairness-audit-prep`. If ratings feed pay this cycle, the analysis goes to counsel first under `pay-equity-governance.md`. Sign-off: the calibration group decides outcomes; you may draft a neutral summary of what was decided and why.

7. **Explain the outcome and open a route to contest it.** Draft a short employee-facing summary: who decided the rating, the ledger items behind it, what AI did (drafting and language checks only), and how to ask for human review. The manager must be able to explain the outcome without the tool. Sign-off: the manager delivers it; the HRBP owns the review route.

8. **Treat a PIP as a support process.** Use prompt 4 only after the manager and HRBP have decided a PIP is warranted. The draft states the expected standard, observed gaps with dates, specific support, check-in dates and a firm end date. If the employee has raised a disability or asked for an accommodation, stop drafting and route to the HRBP: EEOC guidance allows a PIP to be paused while an accommodation request is processed, the request starts the interactive process even when it comes after a poor review, and accommodation information stays confidential. Sign-off: HRBP and Legal review before anyone shares the PIP.

9. **Log and name the next owner.** For any AI-assisted step that touched a rating or PIP, record input, output and reviewer, per principle 6 of `ai-use-policy.md`, and name who decides next.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Check goals against the rubric and list gaps | Employee and manager | Does alone |
| Build the evidence ledger from notes the manager supplied | Manager | Does alone |
| Scan a draft for vague, personality-based or coded language | Manager, then HRBP | Does alone |
| Summarize mid-year feedback from supplied notes | Manager | Drafts for sign-off |
| Write the review narrative from the ledger | Manager | Drafts for sign-off |
| Build the calibration briefing and rating definitions | Calibration lead | Drafts for sign-off |
| Four-fifths screening flag on aggregate rating counts | People Analytics, with counsel | Drafts for sign-off |
| Employee-facing explanation and contest route | Manager and HRBP | Drafts for sign-off |
| Write a PIP after the decision is made | HRBP and Legal | Drafts for sign-off |
| Propose or change a rating for a named employee | Manager | Refuses and routes |
| Calibration outcome, ranking or forced distribution of named people | Calibration group | Refuses and routes |
| Respond to an accommodation, leave or complaint raised in a review or PIP | HRBP and accommodation owner | Refuses and routes |

### Refuse and route

- "What rating should Jordan get?": refuse; route to the manager with the evidence ledger and the agreed rating definitions.
- "Rank my team" or "who is our bottom 10%": refuse; route to the calibration lead with the rating definitions. If the ranking is for a layoff, route to HR leadership and counsel with the selection criteria template.
- "Score performance from Slack, email, keystrokes or meeting tone": refuse as monitoring and possible emotion inference; route to the HR AI governance group and counsel.
- "Keep drafting the PIP" after a disability, accommodation request, leave, pregnancy or complaint is raised: stop; route to the HRBP.
- "Enter the ratings" or "send the review to the employee": refuse; the manager does it in the performance system.
- "Use AI usage counts as a performance measure": refuse until leadership defines it for the role and an access check is done; route to HR and Legal.
- "Check whether ratings drove pay gaps": refuse; route to employment counsel per `pay-equity-governance.md`.

## Guardrails

- **Fairness and adverse impact.** Ratings feed pay, promotion and potential decisions. Any tool that produces ratings, rating suggestions or rating analytics goes through `fairness-audit-prep` before use. Keep performance and potential separate. Before AI fluency becomes a criterion, check equal access to approved tools, training and time, plan accommodations, and route it to Legal.
- **Explainability and notice.** Tell employees when AI assists in performance assessment, per principle 2 of `ai-use-policy.md`, and how to ask for human review. Keep performance uses in scope of the AI governance group's bias audits. A developmental-only tool says so and stays out of ratings. A one-time tool approval is not review of each output.
- **Privacy and minimization.** Use only the evidence the task needs, and synthetic data in examples. Keep health details, accommodation records, leave history and protected-category data out of general AI tools and out of review text.
- **Legal review triggers.** Any PIP; any review where the employee has raised a disability, leave, pregnancy, complaint or protected activity; any rating that will drive termination, discipline or pay; any tool that scores or monitors performance. Federal laws in play include Title VII, the ADA and the ADEA (see the EEOC pages in Sources).

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| Illinois HB 3773 (Public Act 103-0804) | AI output feeds promotion, discipline or discharge for Illinois staff | Flags it, drafts notice text for HR review, routes to counsel |
| California SB 947 (Ch. 859, Stats. 2026) | An automated system informs discipline or termination for California staff, including a PIP that may end in exit | Stops at the PIP checkpoint and routes to counsel |
| Colorado SB 26-189 (ADMT Act) | Automated technology is used in an employment decision about Colorado staff | Drafts the explanation and human-review route for counsel to check |
| EU AI Act, high-risk HR systems | A tool monitors or evaluates performance of Germany staff | Keeps AI to drafting and language checks; routes any scoring tool to `eu-ai-act-intake-template.md` |
| EU AI Act, emotion recognition at work (Article 5(1)(f)) | Anyone proposes reading emotion or sentiment from messages, calls or video | Refuses and routes to the governance group |
| GDPR, Article 22 (EU) | A rating or PIP for Germany staff would rest on automated output | Holds the manager checkpoint and routes the meaningful-involvement question to counsel |

Counsel confirms scope and current status before you rely on any row. In your reply, name each rule as: see the Key dates row "exact row name" in `03-governance/README.md`. Stop there: do not write the row's dates, status or regulation numbers, even ones you read in the table or in Sources, because the table is the one place they are kept current.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| Evidence traceability rate | AI-assisted review drafts signed with zero `[UNTRACED]` sentences, divided by all AI-assisted drafts signed, per cycle | Shows reviews rest on evidence, not generated text |
| Top-rating selection ratio by group | For each group, people rated in the top level divided by people rated in that group, after calibration, per cycle; each group's rate divided by the highest group's rate, with a statistical test for small groups | Screens for adverse impact before ratings drive pay or promotion |
| Rating review request rate | Employees who asked for human review of an AI-assisted step or contested a rating, divided by employees whose review used AI, per cycle | Shows whether the contest route is known and used |

## Output format

```markdown
## Task and owner
[goals / review draft / calibration prep / PIP / cycle design]
Decision owner: [role]

## Evidence ledger
| Date | Item | Source | Goal | Skill tag |
[gaps in the period and recency flag]

## Draft
[goal check, review text, briefing, explanation or PIP draft, marked DRAFT]
[UNTRACED] on any sentence not tied to a ledger item

## Checks run
| Check | Result | Action for the manager |
| Evidence covers full period | | |
| Vague, personality or coded language | | |
| Different evidence standards across drafts | | |
| Accommodation, leave or complaint raised | | |
| Four-fifths screening flag (aggregate only) | | |

## Decision rights calls
[what was drafted for sign-off, what was refused and routed, to whom]

## Audit trail
Inputs used: [list, with gaps labeled]
Tools called and fields read: [tool, purpose, fields]
Items needing sign-off: [item, owner]
Open legal questions: [question, Key dates row, counsel]

## Next step
[named role] decides [what]
```

## Worked example

An HRBP at a fictional software company asks for a mid-year calibration briefing and a bias screen, and also asks the agent to flag the bottom five for PIPs. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They were run on 18 November 2026 with `claude-sonnet-5-5`, one fresh session per case, and graded in a separate pass; see [the results](../../09-evals/skill-eval-results-2026-11-18.md) for the method and its limits.

- `review-draft-from-manager-notes`: core request; a traced review draft with no suggested rating.
- `recency-only-evidence-germany`: edge case; thin, undated evidence for a Germany employee.
- `rank-team-by-message-sentiment`: red flag; ranking named people and reading sentiment from messages.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. HR Leaders Must Evolve Pay for Performance in the Age of AI, Gartner, 22 April 2026. https://www.gartner.com/en/newsroom/press-releases/2026-4-22-hr-leaders-must-evolve-pay-for-performance-in-the-age-of-ai. Supports: AI supports judgment and managers stay accountable, guardrails against inconsistent or biased AI-assisted reviews, separate performance from potential, decisions must be explainable.
2. Gartner Identifies Four Trends Talent Management Leaders Should Prepare for in 2026, Gartner, 29 October 2025. https://gartner.com/en/newsroom/press-releases/2025-10-29-gartner-identifies-four-trends-talent-management-leaders-should-prepare-for-in-2026. Supports: managers use AI in performance management without formal training, need for approved tools and bias guidance, PIPs with prescriptive steps, clear goals and firm deadlines.
3. The Current State of Performance Management (working group summary), Cornell ILR School, CAHRS, 8 May 2025. https://www.ilr.cornell.edu/sites/default/files-d8/2025-05/the-current-state-of-performance-management_final.pdf. Supports: frequent feedback feeding formal reviews, ratings without self-ratings, midyear calibration and quarterly check-ins, AI cannot replace manager conversations, SMART goal checks. Qualitative, ten companies.
4. What HR Leaders Need to Know About Performance Calibration, Korn Ferry, 1 May 2024. https://www.kornferry.com/insights/featured-topics/employee-experience/hr-leaders-and-performance-calibration. Supports: define criteria up front, allow enough time, centrality and tightrope bias, advocacy rewarded over performance.
5. How HR Is Using Generative AI in Performance Management, SHRM (Dave Zielinski), 8 August 2023. https://www.shrm.org/in/topics-tools/news/technology/how-hr-using-generative-ai-performance-management. Supports: drafting reviews from manager notes, risks of inaccurate and biased output, human ownership and disclosure of AI use.
6. Is It Time to Measure AI Use During Performance Reviews?, SHRM (Olivia Gebreamlak), 8 December 2025. https://www.shrm.org/topics-tools/news/is-time-to-measure-ai-use-performance-reviews. Supports: risks of rating AI use, emphasis on judgment and quality over volume.
7. Applying Performance and Conduct Standards to Employees with Disabilities, U.S. Equal Employment Opportunity Commission. https://www.eeoc.gov/laws/guidance/applying-performance-and-conduct-standards-employees-disabilities. Supports: same standards for all, PIP may be postponed while an accommodation request is processed, a late request still starts the interactive process, accommodation not withdrawn as punishment, confidentiality.
8. Know Your Rights: Workplace Discrimination is Illegal, U.S. Equal Employment Opportunity Commission. https://eeoc.gov/know-your-rights-workplace-discrimination-illegal. Supports: Title VII, age and disability protections apply to all aspects of employment, including promotion and discharge, and retaliation is prohibited.
9. AI in the Workplace Playbook: A Practical Guide for Human-First AI Strategy in the Modern Workplace, SHRM, 2025. Read from a copy of the publication; no web address checked. Supports: performance evaluations in the scope of AI ethics guidance and bias audits; transparency about AI feedback and its developmental purpose.
10. 2026 Work Trend Index Annual Report, Microsoft, May 2026. Read from a copy of the publication; no web address checked. Supports: only 13% of surveyed AI users (Feb to Apr 2026) say they are rewarded for reinvention when results are not met; AI in performance evaluation as part of organizational readiness.
11. Role redesign: a leader's guide to helping your people thrive in the AI era, Microsoft, 2026. Read from a copy of the publication; no web address checked. Supports: separating outcomes owned from activities when goals change with AI.
12. The State of Organizations 2026, McKinsey & Company, 2026. Read from a copy of the publication; no web address checked. Supports: crediting both human contribution and agent output with clear human ownership of outcomes; linking individual goals to organizational goals.
13. Draft guidelines on the classification of high-risk AI systems, European Commission, 2026 (consultation draft, non-binding). Read from a copy of the publication; no web address checked. Supports: draft examples of performance monitoring as high risk, reliance on AI output counting toward a decision, and a writing assistant that polishes a manager's finished text as a possible exemption.
