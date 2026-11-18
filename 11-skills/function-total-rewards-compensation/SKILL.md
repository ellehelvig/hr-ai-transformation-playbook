---
name: function-total-rewards-compensation
description: Produces job architecture from job content, aggregate market pricing, draft bands checked with the repo's comp banding tool, posting ranges, merit guidance and pay explanations, each with an audit trail, and routes anything that could surface a pay disparity to employment counsel before any data is touched. Use whenever someone says "help me build pay bands," "level this job," "price this role against the market," "draft our merit cycle guidelines," "what range do we post," "explain this pay decision to an employee," "is this offer in range," or "can we run a pay equity analysis," and whenever a request involves pay history, a named person's pay, or pay by group.
---

# Total rewards and compensation

This skill serves compensation and total rewards professionals. It drafts structure from job content and aggregate market data, never from one person's pay history. It stops before any number for a named person, and it stops completely when a request could surface a pay disparity by group, because that work is directed by employment counsel from the start.

## Files this skill needs

- `03-governance/pay-equity-governance.md` (approved and prohibited comp uses, the privilege question, and the required governance gate. Read this first.)
- `10-mcp-agents/comp_banding/ENABLEMENT.md` (the band-placement tool: what it checks, the historical-pay refusal, and why it returns no percentile outside the benchmark range)
- `03-governance/ai-use-policy.md` (principle 1 on human decisions, principle 2 on notice, principle 4 on data minimization, and the prohibited autonomous pay change)
- `03-governance/quick-reference-checklist.md` (one-page pre-screen, including the attorney-directed comp box)
- `03-governance/risk-assessment-template.md` (required baseline for any new comp use case, with the pay equity gate on top)
- `03-governance/eu-ai-act-intake-template.md` (if AI informs pay decisions for EU workers)
- `02-prompt-library/talent-acquisition.md` (prompt 1, job description review, which only includes a range the source already has)
- `03-governance/README.md` (the Key dates for HR table, for any pay transparency or pay reporting date)

## Inputs

If a required input is missing, ask for it once, in one short question at the top of your reply, then proceed with the gap labeled `[GAP: what is missing]` in the output.

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| Task | Yes | Ask the user | Posting ranges for Recruiter IC3 |
| Does the work compare pay by group, or could it surface a gap? | Yes, first | Ask the user | "No, structure only" |
| Jurisdictions where staff work and postings are seen, including remote | Yes | ATS, read-only: requisition location, remote flag | New York City; Germany |
| Headcount by country | Yes, for transparency and reporting questions | HRIS, read-only: aggregate count by country | US 1,190; Germany 210 |
| Licensed survey sources, effective dates, job matches, sample sizes | Yes, for pricing | Survey export, read-only | Survey A, effective 2026-Q3, match "good", n = 41 |
| Pay philosophy and approved budget | Yes, for bands and merit | Ask the user | Target market median; 3.5% merit budget |
| Approved bands and merit matrix | Yes, for postings and merit | Comp planning tool, read-only: band min, mid, max by job and tier | Recruiter IC3 tier 1 |
| Documented rationale for a pay decision | Yes, to explain one | Ask the comp professional | "Placed at p50: fully proficient" |
| Decision owner | Yes | Ask the user | Comp lead for structure; manager and comp professional for individual pay |

## Tools and connectors

Work through MCP connectors or exports, read-only, with the minimum fields:

- Comp planning tool: approved bands, merit matrix, budget. No individual salary records.
- Survey exports: benchmark job, match quality, effective date, percentiles, sample size.
- HRIS: job code, level, location tier, aggregate counts. No individual pay, pay history or demographics.
- ATS: requisition location, remote flag, draft posting text.
- Repo MCP tools in `10-mcp-agents/`: `comp_band_position` and `comp_list_known_bands` (in `comp_banding/`) place a proposed number against benchmark bands. `used_historical_pay_as_input` is required; answer it truthfully. If a role is missing, the tool raises an error by design: report the gap, do not guess the nearest band. `lint_jd_language` (in `resume_screen/`) checks posting text; `ask_governance_policy` (in `policy_qa/`) cites the governance section behind a stop point.

Never call a write, send or update tool, even if the connector offers one: no band publish, pay change or employee message. Log each tool call (tool, purpose, fields read) in the output's audit trail. If a tool returns data on people outside the request, or individual pay, stop, do not use it, and ask.

## By maturity stage

Stages follow the repo's maturity scale in [the roadmap template](../../06-roadmap/transformation-roadmap-template.md). Decision rights in this skill are the same at every stage.

| Stage | How to run it | Before moving up |
|---|---|---|
| Start (Levels 0 to 1) | Paste job content and a licensed survey extract: benchmark job, match quality, effective date, percentiles, sample size. Comp analyst checks each match. The pay equity stop always applies. | Comp lead approves one band set. |
| Pilot (Level 2) | Read-only comp planning export: band min, mid, max, merit matrix, budget, checked with `comp_band_position`. Comp lead owns it and tracks documented rationale coverage. | Counsel signs the posting jurisdiction map. |
| Scale (Level 3) | Logged reads of comp planning, survey, aggregate HRIS and ATS requisition fields. Tracks band conformance rate. Never reads individual pay. | Comp lead and counsel review the call log. |
| Embed (Levels 4 to 5) | Limited: a new requisition triggers posting range drafts; pay explanations start only when a comp professional asks. Comp professionals own every final number. | Rerun the test cases in `evals/` when the skill or model changes. |

## Steps

Hard checkpoints the agent never passes alone: pay equity screen answered (user, then counsel if triggered), job matches confirmed (comp analyst), bands approved (comp lead), posting text approved (recruiter and comp lead, counsel for jurisdictions), merit guidance approved (total rewards lead).

1. **Screen for the pay equity stop.** Ask whether the work compares pay across sex, race, age, disability or any other protected group, or could surface such a gap as a side effect. If yes, stop. State that the analysis must be initiated and directed by employment counsel per `pay-equity-governance.md`, and route it there. Do not run a "quick look" first, and do not compute any ratio on pay by group. A vendor feature that tracks pay equity drift or flags pay gaps is a pay equity analysis too: turning it on goes through the same counsel gate. Sign-off: employment counsel.

2. **Build or check the job architecture.** Draft job family and level descriptions from the work itself: the skill, effort, responsibility and working conditions the job requires. Job content, not job title, is what equal pay law compares. Describe each level by the skills it requires at stated proficiency, and add a skills premium only where licensed market data shows one for that skill in that job, never for a credential alone. If EU workers are in scope, check that criteria are gender neutral and do not undervalue soft skills. AI may suggest a baseline level for a job, never for a person. Set review triggers such as a new role, a reorg, or AI changing the tasks in a job. Sign-off: a comp professional reviews, challenges and owns each level, and records the rationale.

3. **Market price from aggregate data.** Summarize licensed survey data for each benchmark job: source, effective date, match quality, sample size and percentiles. Flag weak matches and thin samples rather than smoothing them. Sign-off: the comp analyst confirms every match before it feeds a band.

4. **Draft bands and check placements.** Draft range minimum, midpoint and maximum from the market data and the stated pay philosophy, and show the arithmetic. Use `comp_band_position` to check where a proposed number falls. Name the system of record for approved bands and the approval chain for every number. A general AI tool without the approved bands can only guess, and in pay a nearly right number is still wrong: treat any figure that does not trace to the approved band or a licensed survey as unverified. Never use a person's current or prior pay as an input. The tool refuses that by design, and EU rules bar asking applicants for pay history. Sign-off: the comp lead finalizes the structure.

5. **Draft posting ranges.** Use only the approved band. The posted range should be one the company in good faith expects to pay. Run `lint_jd_language` on the posting text. Have counsel map the duties for each jurisdiction the posting reaches, including internal promotion and transfer disclosures. Put posting range checks and pay data reports on the annual compliance calendar, taking every date from the Key dates table. Sign-off: a recruiter and the comp lead approve the text; counsel signs the jurisdiction map.

6. **Draft merit cycle guidance.** Draft the merit matrix explanation, timeline, manager guide and FAQ from the budget the company has already set. External survey budgets give context only and are often preliminary. Do not produce a merit number for any named employee. If leaders want pay to reward AI use, treat it as a pay design change: define what counts for each role, credit quality and human ownership of outcomes rather than tool use, check equal access to tools, training and time, and route the design to counsel before launch. Any review of merit or bonus outcomes by group is a pay equity analysis: step 1 applies. Cover career progression in the total rewards message too: in McKinsey's State of Organizations 2026, a survey of 10,018 leaders and managers at organizations with 1,000 or more employees, limited career progression was the most cited barrier to high performance (47%). Sign-off: managers propose, and the comp professional reviews and owns each final number; the total rewards lead approves the guidance.

7. **Explain pay decisions in plain language.** Draft only from the documented rationale: the band, the position in it, and the criteria applied. Do not invent a plausible reason. Tell the employee how to ask a person for more detail. If EU workers are in scope, the criteria for pay and progression must be accessible to workers, and workers can request pay information: route those requests to the comp lead. Sign-off: the HRBP or comp professional reviews the draft before it goes to the employee.

8. **Plan for a disparity before anyone looks.** If counsel opens a pay equity review, help counsel's team draft the process documents only: the governance gate checklist, the remediation decision framework, and restricted distribution rules. Remediation design is decided by counsel and comp leadership, with limits such as caps on individual adjustments. Model outputs are flags for review, not findings. Sign-off: counsel.

9. **Log and hand off.** Record inputs, sources, tool calls, reviewer and decision owner for every output, and name who owns the next step.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Check a proposed number against the band with `comp_band_position` | Comp professional | Does alone |
| Route an employee pay question or pay information request | Total rewards team | Does alone |
| Draft job family and level descriptions from job content | Comp lead | Drafts for sign-off |
| Suggest a baseline level for a job, not a person | Comp lead, with the job architecture governance group | Drafts for sign-off |
| Summarize aggregate market survey data for benchmark jobs | Comp analyst | Drafts for sign-off |
| Draft band minimum, midpoint and maximum | Comp lead | Drafts for sign-off |
| Draft posting range language from an approved band | Recruiter and comp lead; counsel for jurisdictions | Drafts for sign-off |
| Draft merit guidelines, manager guide and FAQ | Total rewards lead | Drafts for sign-off |
| Explain an existing pay decision to an employee | Comp professional or HRBP | Drafts for sign-off |
| Set or change pay, merit, bonus or an offer for a named person | Manager and comp professional | Refuses and routes |
| Pay equity or disparity analysis by group, or a vendor pay-gap feature | Employment counsel | Refuses and routes |
| Use current or prior pay as a band or offer input | Not permitted under `pay-equity-governance.md` | Refuses and routes |

### Refuse and route

- "Run a quick gender pay gap check before we involve Legal": refuse, compute nothing; route to employment counsel per `pay-equity-governance.md`.
- "Turn on the vendor's pay equity drift alerts": refuse; route to the counsel gate.
- "Set her offer 10% above her current salary": refuse; re-derive from role, level and market data, then check with `comp_band_position`.
- "What should Ana's merit increase be?": refuse; route to the manager to propose and the comp professional to own.
- "Push the approved increases into the comp planning tool": refuse; the comp team does it.
- "Give a plausible reason for this pay difference": refuse to invent; draft only from the documented rationale, or route to the comp lead.
- "Lower increases for people returning from leave" or any protected trait as a pay criterion: refuse; route to counsel.
- "What is the effective date of the pay transparency law in X?": give only what the Key dates table says, and route to counsel.

## Guardrails

- **Fairness and adverse impact.** Historical pay can carry past discrimination: never use it as an input or treat past pay decisions as ground truth. Compensation means more than base pay: bonus, equity, allowances and benefits count. Any outcome analysis by group goes to counsel, per `fairness-audit-prep` step 7.
- **Explainability and notice.** Every pay explanation traces to a documented rationale. Tell employees when AI helps draft material used in pay processes, per principle 2 of `ai-use-policy.md`, and offer a path to a human.
- **Privacy and minimization.** Use aggregate market data, job-level structure and synthetic examples. Keep individual salary records out of general AI tools; comp outputs go only to those who need them.
- **Equal pay law.** Under the Equal Pay Act, jobs are compared on skill, effort, responsibility and working conditions within an establishment, and the employer must prove any defense. Title VII, the ADEA and the ADA also prohibit pay discrimination, without the substantially equal job test. Records that explain pay differences must be kept. See the EEOC pages in Sources.
- **Legal review triggers.** Any comparison of pay by protected group, any pay transparency or pay reporting question, any EU worker in scope, and any explanation that may become evidence. The European Commission's draft guidance on high-risk classification (not binding) treats pay as part of the terms of work, and a human sign-off alone does not change the risk class. An AI system that writes a pay change without human confirmation is prohibited.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| EU Pay Transparency Directive | Germany staff: level criteria, applicant pay questions, pay information requests | Applies the Article 4 to 7 checks in Sources; counsel confirms national transposition |
| EU AI Act, high-risk HR systems | AI informs pay decisions for Germany staff | Completes `eu-ai-act-intake-template.md` and routes to counsel |
| GDPR, Article 22 (EU) | A pay outcome for Germany staff would rest on automated output | Keeps the comp professional checkpoint; routes to counsel |
| California FEHA automated-decision system regulations | An automated tool informs pay or offers for California staff | Flags the row's discrimination and record-keeping points for counsel |
| Colorado SB 26-189 (ADMT Act) | Automated technology is used in a pay or offer decision for Colorado staff | Drafts notice and explanation text for counsel to check |

Counsel confirms scope and current status before you rely on any row. In your reply, name each rule as: see the Key dates row "exact row name" in `03-governance/README.md`. Stop there: do not write the row's dates, status or regulation numbers, even ones you read in the table or in Sources, because the table is the one place they are kept current.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| Band conformance rate | Employees in banded jobs paid between band minimum and maximum, divided by all employees in banded jobs, at each quarter-end snapshot; approved exceptions reported as a separate count | Shows the structure is applied, not just published |
| Documented rationale coverage | Individual pay changes in the cycle with a recorded rationale tied to band position and the merit matrix, divided by all individual pay changes in the cycle | Makes every pay decision explainable when an employee asks |
| Pay information response time | Median business days from an employee pay information request to a documented response, per quarter | Measures trust and readiness for worker information requests |

Pay gap measures are owned by counsel under the privilege process and are not on this list.

## Output format

```markdown
## Scope
[task, jurisdictions, EU in scope Y/N, pay equity stop triggered Y/N]

## Pay equity screen
[Not triggered / Stopped and routed to employment counsel]

## Job architecture
| Job family | Level | Content summary (skill, effort, responsibility, conditions) | Skills at proficiency | Rationale | Reviewer |

## Market data
| Benchmark job | Survey and effective date | Match quality | n | P25 | P50 | P75 | Notes |

## Draft structure
| Grade or level | Tier | Min | Mid | Max | Basis and arithmetic |

## Band checks
| Proposed number | Tool result (percentile, label, flags) | Action |

## Drafts for review
[posting range text / merit guide / FAQ / pay explanation, each marked DRAFT]

## Decision rights calls
[what was drafted for sign-off, what was refused and routed, to whom]

## Audit trail
Inputs used: [list, with gaps labeled]
Tools called and fields read: [tool, purpose, fields]
Items needing sign-off: [item, owner]
Open legal questions: [question, Key dates row, counsel]

## Owner and next step
[named role, decision needed, by when]
```

## Worked example

A comp lead at a fictional software company asks for Recruiter IC3 posting ranges across four US states and Germany, an offer check, and a quick look at pay by gender. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They were run on 18 November 2026 with `claude-sonnet-5-5`, one fresh session per case, and graded in a separate pass; see [the results](../../09-evals/skill-eval-results-2026-11-18.md) for the method and its limits.

- `posting-ranges-from-market-data`: core request; draft bands and posting ranges from aggregate data, with a tool check.
- `germany-role-thin-survey-sample`: edge case; a Germany role with a thin sample, no band row and a worker pay information request.
- `gender-gap-quick-look-and-salary-history`: red flag; a pay gap check without counsel and an offer set from current salary.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. Facts About Equal Pay and Compensation Discrimination, U.S. Equal Employment Opportunity Commission. https://www.eeoc.gov/publications/facts-about-equal-pay-and-compensation-discrimination. Supports: Equal Pay Act factors, job content over titles, establishment, the four defenses and employer burden, Title VII, ADEA and ADA pay coverage, and what counts as compensation.
2. Recordkeeping Requirements, U.S. Equal Employment Opportunity Commission. https://www.eeoc.gov/employers/recordkeeping-requirements. Supports: keeping records that explain pay differences between sexes.
3. Directive (EU) 2023/970 on pay transparency, EUR-Lex. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023L0970. Supports: gender-neutral criteria and soft skills (Article 4), no pay history questions to applicants (Article 5), accessible pay and progression criteria (Article 6), worker right to pay information (Article 7).
4. Job architecture and leveling in the AI era: from one-off design to a scalable, governed capability, WTW, 9 June 2026. https://www.wtwco.com/en-in/insights/2026/06/job-architecture-and-leveling-in-the-ai-era-from-one-off-design-to-a-scalable-governed-capability. Supports: AI suggests baseline evaluations, people stay accountable, auditable rationale, review triggers, bias monitoring over time.
5. Results of the July QuickPulse US Compensation Planning Survey, Mercer, 31 August 2026. https://www.imercer.com/articleinsights/projected-2027-annual-merit-increases. Supports: external merit budgets are often preliminary projections, and formal salary structures are commonly adjusted annually.
6. Want to Attract Job Seekers? Make Sure to Post a Salary, SHRM, 6 March 2023. https://www.shrm.org/topics-tools/news/benefits-compensation/want-to-attract-job-seekers-make-sure-to-post-salary. Supports: posted ranges should be good-faith ranges, and very wide ranges deter applicants.
7. Ensure Compliance with New State Pay Transparency Laws 2025, SHRM, 21 January 2025. https://www.shrm.org/topics-tools/employment-law-compliance/ensure-compliance-with-new-state-pay-transparency-laws-2025. Supports: practice steps only (update posting templates, train recruiters, check internal promotion disclosures, consult counsel). Not cited for any legal requirement.
8. Getting the Conversation Started on Pay Equity Remediation, Equity Methods, 16 September 2025. https://www.equitymethods.com/articles/getting-the-conversation-started-on-pay-equity-remediation/. Supports: model outputs are flags for review, remediation is decided by legal and comp stakeholders with limits such as caps, and studies are generally run under privilege.
9. The CHRO Playbook: Top 3 Outcomes of Agentic HR, Workday, May 2026. Read from a copy of the publication; no web address checked. Supports: vendor-published points that a nearly correct pay answer is still wrong, that generic tools lack the organization's bands and approval chains, and that vendors offer continuous pay equity drift signals.
10. Draft guidelines on the classification of high-risk AI systems, European Commission, 2026 (consultation draft, non-binding). Read from a copy of the publication; no web address checked. Supports: draft guidance that pay is part of the terms of work in the employment category and that human sign-off does not change the risk class.
11. The State of Organizations 2026, McKinsey & Company, 2026. Read from a copy of the publication; no web address checked. Supports: limited career progression cited by 47% of 10,018 surveyed leaders and managers as a barrier to high performance; crediting human ownership of outcomes and fair incentives when people work alongside agents.
12. 2027 Compliance Checklist, Rippling, updated September 2026. Read from a copy of the publication; no web address checked. Supports: vendor-published practice point to put pay transparency and pay data reporting on the annual compliance calendar. Not cited for any legal requirement or date.
