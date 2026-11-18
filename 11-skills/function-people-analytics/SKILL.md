---
name: function-people-analytics
description: Frames a workforce question, fixes metric definitions in a data dictionary, sets small-group suppression and data governance, plans any predictive model as a fairness-tested validation exercise, verifies AI-produced figures against source, and drafts an aggregate leadership story with an audit trail. Use whenever someone asks how to define attrition, time to fill, or internal fill rate, wants a retention or headcount briefing for executives, asks whether the company can predict who will leave, needs a suppression threshold, wants an AI-generated analysis checked, wants an agent to pull from HRIS, ATS, or survey data, or wants a dashboard turned into a story for leaders. Use it before any model about people is built, even when the request sounds like a quick chart.
---

# People analytics

This skill serves a People Analytics team and the leaders who ask it questions. It produces a framed question, a data dictionary, a suppression plan, a model validation plan where needed, a verification log, and a leadership story from approved aggregates. It stops before any output that scores, flags, or recommends action on a named employee, and never runs analysis on real employee data.

## Files this skill needs

- `02-prompt-library/people-analytics.md` (prompt 1 segment-level attrition, prompts 2 and 3 survey and exit themes, prompt 4 leadership narrative)
- `05-notebooks/attrition-risk-modeling.ipynb` (synthetic worked example of calibration, group calibration, error rates, and segment-level reporting)
- `11-skills/fairness-audit-prep/SKILL.md` (hand off for any model that scores or ranks people)
- `03-governance/ai-use-policy.md` (principle 2 on notice, principle 3 on fairness, principle 4 on data minimization, approved tool categories row for segment-level attrition inquiry)
- `03-governance/quick-reference-checklist.md` (pre-screen on privacy, notice, and bias)
- `03-governance/risk-assessment-template.md` (sections 2 to 6, required before any new model or AI analysis tool)
- `03-governance/pay-equity-governance.md` (if compensation data is anywhere in scope)
- `03-governance/README.md` (the Key dates for HR table and the US federal AI enforcement context)

## Inputs

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| Business question, the decision it informs, and who asked | Yes | Ask the user | Where is regretted attrition highest in hard-to-refill roles? (CRO) |
| Human owners: requesting leader and the People Analytics lead who signs off the method | Yes | Ask the user | CRO; Director of People Analytics |
| Jurisdictions where the people in the data work | Yes | HRIS, read-only: work country, state, and city counts | California, Illinois, New York City, Colorado, Germany |
| Company size and smallest population to be reported | Yes | HRIS, read-only: headcount by org unit and location | 1,400 staff; smallest team 6 |
| Source systems and the steward of each | Yes | Ask the user | HRIS (HR Operations), ATS (TA Operations), survey platform (Listening lead) |
| Whether protected characteristic data is collected and lawful for this purpose | Yes | Ask the user; Privacy confirms | US voluntary self-ID only |
| Model, AI-assisted analysis, or both | Yes | Ask the user | AI-assisted summary of exit comments, no model |
| Approved minimum group size | No | Ask the user (Privacy owns it) | 10 for reports, stricter for free text |

If a required input is missing, ask for it once, in one short question at the top of your reply. Then proceed, write `GAP:` and the missing input in the affected section, and list it in the audit trail.

## Tools and connectors

The agent reads only approved read-only connectors or exports, and only these fields.

- **HRIS, read-only:** pseudonymous ID, job family, level, org unit, work location, hire date, separation date, separation type (quit, layoff or discharge, other), regretted flag. Not names, manager notes, or pay.
- **ATS, read-only:** requisition ID, job family, requisition opened date, offer accepted date, hire source (internal or external).
- **Survey platform, read-only:** scores and open-text themes only for groups at or above the approved threshold, as the platform reports them. No respondent-level rows.
- **LMS, read-only:** completion counts by group, when a learning or skills metric is in scope.
- **Payroll export:** not read unless employment counsel has opened a pay analysis under `03-governance/pay-equity-governance.md`.
- **Repo MCP tool `ask_governance_policy`** (`10-mcp-agents/policy_qa/`): cites the governance sections that apply, or returns `no_match`. The other repo tools do not fit this function.

Rules for every tool call:

- Never call a write, send, or update tool, even if the connector offers one.
- Log each call in the audit trail: tool, purpose, fields read.
- If a tool returns people outside the request or unlisted fields, stop, discard it, and ask the user.
- If a pull across several systems skips or fails a source, list the source and mark the result partial.
- Row-level data stays in the environment Privacy approved. Outputs carry aggregates only.

## By maturity stage

Stages follow the repo's maturity scale in [the roadmap template](../../06-roadmap/transformation-roadmap-template.md). Decision rights in this skill are the same at every stage.

| Stage | How to run it | Before moving up |
|---|---|---|
| Start (Levels 0 to 1) | Paste the question and a de-identified aggregate export: job family, level, org unit, separations by type. An analyst recomputes every figure. | People Analytics lead approves the dictionary; Privacy approves thresholds. |
| Pilot (Level 2) | One scheduled read-only HRIS export with the listed fields only. Metric: verified figure rate. | Every released cell meets suppression rules for a full cycle. |
| Scale (Level 3) | Read-only HRIS, ATS and survey connectors, four checkpoints, call logging; tracks suppression compliance. Predictive models: not before the risk assessment, a `fairness-audit-prep` plan and Legal, Privacy and HR Leadership sign-off. | Employee notice published. |
| Embed (Levels 4 to 5) | Limited. A scheduled reporting cycle triggers the draft story for lead sign-off. Never writes scores to the HRIS or dashboards. | Rerun the test cases in `evals/` when the skill or model changes. |

## Steps

1. **Frame the question before touching data.** Restate the request as a strategic question tied to a business outcome, such as "where is regretted attrition highest in roles we cannot easily refill." Write the decision the answer feeds and what result would change it. Sign-off: the requesting leader confirms the framing.

2. **Fix metric definitions in a data dictionary.** Write each metric as numerator, denominator, period, population, and exclusions. Start from published definitions and note any local change:
   - Separation (attrition) rate: separations in the period divided by employment, times 100. Report quits apart from layoffs and discharges and from other separations (retirements, transfers), as BLS does.
   - Time to fill: calendar days from requisition opened to offer accepted, as SHRM's 2025 benchmarking report defines it.
   - Internal fill rate: share of open positions filled by people already employed in other positions.
   - Skills metrics: count a skill only where there is evidence of use (assessed work, a completed project, a validated assessment). Label self-reported or AI-inferred skills as such and report them apart. A course completion or credential is not evidence of a skill on its own.

   Sign-off: the People Analytics lead approves the dictionary. Every later chart cites it.

3. **Set data governance and access.** List each source system, its steward, the fields the question needs, and the fields it does not. Drop everything not needed, per principle 4 of `03-governance/ai-use-policy.md`. For each field kept, record where it came from, how it was collected, and whether the organization may use it for this purpose. Data scraped from outside sources or reused for a new purpose goes to Privacy for an impact assessment first. Confirm who may see row-level data and where analysis runs. Run the pre-screen in `03-governance/quick-reference-checklist.md`. Sign-off: Privacy approves the field list and the environment.

4. **Set suppression rules before anyone sees results.** Choose a minimum group size for every reported cell and write it into the plan. Add a secondary rule: when one cell is hidden, hide further cells, or report only the parent total, so the hidden cell cannot be worked out by subtraction. Removing names is not enough: the test is whether a motivated person with ordinary resources could single someone out. Apply stricter thresholds to free text and to anything shared beyond the analytics team. Apply suppression in drafts too, and in your own explanations and verification log: never show the arithmetic, or the inputs to it, that would let a reader recover a hidden cell. Say which cells are hidden and why, not what they would be. Sign-off: Privacy approves the thresholds.

5. **Plan any predictive model as a validation exercise, not a decision tool.** Follow the pattern in `05-notebooks/attrition-risk-modeling.ipynb`: an interpretable baseline first, calibration overall and by group, error rates by group, and segment-level outputs only. Individual scores stay inside model validation and never reach managers. Hand the fairness plan to `11-skills/fairness-audit-prep/SKILL.md`. The four-fifths ratio is a screening flag under the Uniform Guidelines, 29 CFR 1607.4(D), not a safe harbor or a verdict: smaller differences can still count as adverse impact, and differences based on small numbers may not. Small groups need a statistical test, and People Analytics or counsel interprets it. Do not use proxies for protected characteristics the organization does not collect. Run `03-governance/risk-assessment-template.md` before any build. Write a one-page model fact sheet: purpose, data and lineage, build and test method, known limits, and a drift and data-quality monitoring schedule, with a named owner who can switch it off. Test for bias and interpretability, not only accuracy. Sign-off: HR Leadership, Legal, and Privacy, before any build.

6. **Run agent pulls with checkpoints.** When an agent or script assembles the analysis, stop at four checkpoints and wait for the named person: after framing (requesting leader), after the dictionary (People Analytics lead), after suppression is applied and before anyone outside the analytics team sees a cell (Privacy), and after verification (the analyst who signs the figures). The agent does not pass a checkpoint until that sign-off is recorded in the audit trail.

7. **Verify any AI-assisted analysis.** Recompute every AI-produced number from the source query. Check that every cited source exists and says what is claimed. Record the tool, model, date, prompt, and data extract used. Label the output "DRAFT, not verified" until an analyst signs that every figure ties back to source. Never paste row-level data into an unapproved tool. Sign-off: the analyst who signs the figures.

8. **Separate observed facts from estimates and associations.** Keep observed counts and rates apart from modeled estimates. State denominators, periods, and comparison groups. Describe associations as hypotheses, not causes. Report only figures you can compute from the data supplied; do not add confidence intervals, ranges or significance claims unless you state the method and they follow from the data. When a group is small, say so and route the test to People Analytics. Say what the analysis cannot establish, including whether any particular person will leave. For a composite index, such as an AI adoption or fluency score, state that its weights and bands are judgment calls unless they were statistically derived, report it at group level only, keep it out of individual reviews, and track sentiment beside it, since a high adoption score can hide worry about jobs. Sign-off: People Analytics lead.

9. **Build the story for leaders.** Use prompt 4 or prompt 1 in `02-prompt-library/people-analytics.md`. Lead with one headline sentence, then what changed, where to look closer, and what the trend implies if nothing changes. Tie it to a business measure the leader already tracks. Suppression holds in every chart, footnote, and appendix. Sign-off: the People Analytics lead reviews end to end before it goes to the requesting leader.

10. **Write the notice and explanation lines.** Draft what employees are told: what data is analyzed, why, that results are group-level, whether a model exists, and how to ask a question or correct a record, per principle 2 of `03-governance/ai-use-policy.md`. If a model exists, the notice links a plain-language version of its fact sheet. Sign-off: Privacy and the People Analytics lead.

11. **Route the follow-up.** Send work-condition questions to the relevant HRBP or leader. Send any concentration by manager or team to the HRBP for a conversation, not an investigation (prompt 3). Send anything touching pay to employment counsel under `03-governance/pay-equity-governance.md`. Name the owner of each next step. Sign-off: each named owner accepts the item.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Restate a request as a strategic question with a decision attached | Requesting leader | Drafts for sign-off |
| Draft metric definitions for the data dictionary | People Analytics lead | Drafts for sign-off |
| Propose minimum group size and the secondary suppression rule | Privacy | Drafts for sign-off |
| Check a report's charts against the dictionary and suppression rules | People Analytics lead reviews findings | Does alone |
| Recompute AI-produced figures and log matches | Analyst who signs the figures | Does alone |
| Summarize survey or exit comments into themes above threshold | People Analytics lead | Drafts for sign-off |
| Plan model validation and fairness tests | People Analytics lead with Legal, Privacy, and HR Leadership | Drafts for sign-off |
| Draft the leadership story from approved aggregates | People Analytics lead | Drafts for sign-off |
| Route concentrations and pay questions to the right owner | HRBP or employment counsel | Does alone |
| Score, flag, or rank a named employee for flight risk or any other risk | Not permitted | Refuses and routes |
| Recommend or decide an action about a named person from analytics output | Manager and HRBP, outside this skill | Refuses and routes |
| Write results, scores, or flags to the HRIS, survey tool, or a manager dashboard | System owner | Refuses and routes |

### Refuse and route

- "Name the ten people most likely to quit": refuse; offer segment-level risk; route to the People Analytics lead and `11-skills/fairness-audit-prep/SKILL.md`.
- "Send the individual risk scores to managers" or "load them into the HRIS": refuse; route to HR Leadership and the system owner.
- "Show results for the four-person team" or "work out the hidden cell from the total": refuse; offer the parent rollup; route to Privacy if the threshold is in question.
- "Read Slack, email, or video to measure engagement or emotion": refuse; route to Legal and Privacy, citing the ban in `03-governance/ai-use-policy.md` on monitoring communications or sentiment without disclosure and consent unless Legal, Privacy, and HR Leadership approve.
- "Use age, graduation year, or another proxy for a protected trait as a model feature": refuse; route to Legal and the fairness-audit-prep plan.
- "Run a pay gap analysis by gender": route to employment counsel under `03-governance/pay-equity-governance.md`; no compensation analysis outside an attorney-directed process.
- Real employee or candidate rows pasted into the chat: say so, do not process them, and ask for a synthetic or aggregate version.

## Guardrails

- **Fairness and adverse impact.** Check every model and every segment comparison by group, using calibration and error rates as well as selection-rate ratios. A passing four-fifths ratio is a screening floor, not a verdict. Title VII disparate-impact liability applies to selection procedures regardless of federal enforcement emphasis; see the US federal AI enforcement context in `03-governance/README.md`.
- **Explainability and notice.** Employees know what is analyzed, why, at what level, and how to ask or correct a record. No result is presented as a prediction about a person.
- **Privacy and minimization.** Pull only needed fields. Suppress before anyone sees results. Treat free text as identifiable until shown otherwise. When free text or an AI summary names a person or gives a detail that could identify one, do not repeat the name or detail anywhere in your reply, including where you flag it: write "[named individual]" and say why it was withheld.
- **Legal review triggers.** Any predictive model about people, any use of protected characteristic data, any report with representation data, any compensation analysis, any data transfer across borders, and any analysis of data on staff in Germany. Check the rows in the Regulation map and involve counsel.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| GDPR, Article 22 (EU) | Any model or automated step using data on staff in Germany | Keeps outputs segment-level; routes to Privacy and counsel before build |
| EU AI Act, high-risk HR systems | A model whose output could feed promotion, termination, task allocation, or performance monitoring in the EU | Plans it as validation only; hands to `11-skills/eu-ai-act-hr-classifier/SKILL.md` |
| EU AI Act, emotion recognition at work (Article 5(1)(f)) | A request to infer emotion from text, voice, or video of staff | Refuses and routes to Legal |
| California AB 1883 (Ch. 853, Stats. 2026) | Emotion inference or neural data about California staff | Refuses and routes to Legal |
| Illinois HB 3773 (Public Act 103-0804) | Analytics output used in promotion, discipline, or discharge for Illinois staff | Keeps output out of individual decisions; flags the notice duty to counsel |
| California CPPA regulations | A model or automated decision tool processing California employee personal information | Routes to Privacy for risk-assessment scoping before build |

Counsel confirms scope and current status before you rely on any row. In your reply, name each rule as: see the Key dates row "exact row name" in `03-governance/README.md`. Stop there: do not write the row's dates, status or regulation numbers, even ones you read in the table or in Sources, because the table is the one place they are kept current.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| Regretted attrition rate in critical roles | Regretted voluntary separations from critical roles in the trailing 12 months, divided by average headcount in those roles over the same 12 months, times 100 | The business outcome most analytics requests exist to move |
| Suppression compliance rate | Reported cells in analyses released in the quarter that meet the approved minimum group size and secondary rule, divided by all reported cells released in the quarter | Employees share data only if no one can be singled out |
| Verified figure rate | AI-produced figures in released analyses that an analyst recomputed and matched to source, divided by all AI-produced figures in released analyses, per quarter | Leaders act on numbers; an unverified figure is a trust failure |

## Output format

```markdown
## Question and decision
[strategic question, decision it informs, requesting leader]

## Data dictionary
| Metric | Numerator | Denominator | Period | Population | Exclusions | Source system |

## Governance and suppression
- Fields used / fields excluded
- Minimum reported group size: [N, approved by Privacy]
- Secondary suppression rule: [rule]
- Where analysis runs and who can see row-level data

## Model plan (if any)
| Check | Method | Owner | Pass criterion |
Hand-off: fairness-audit-prep

## AI verification log
| Figure or claim | Recomputed from | Matches Y/N | Analyst |

## Leadership story (DRAFT, not verified)
Headline:
What changed:
Where to look closer:
If nothing changes:
What this cannot tell us:

## Employee notice lines (DRAFT)

## Decision rights calls
| Request | Agent role | Routed to |

## Routing
| Finding | Owner | Next step |

## Metrics tracked
| Metric | Baseline | Period |

## Audit trail
- Inputs used (and GAP items):
- Tools called | purpose | fields read:
- Items needing sign-off | who:
- Open legal questions for counsel:
```

## Worked example

Harbor & Pine's People Analytics director asks for a regretted attrition briefing by job family, including a small German sales cell that must be suppressed. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They were run on 18 November 2026 with `claude-sonnet-5-5`, one fresh session per case, and graded in a separate pass; see [the results](../../09-evals/skill-eval-results-2026-11-18.md) for the method and its limits.

- `retention-briefing-core`: a regretted attrition briefing from synthetic aggregates, end to end.
- `small-cells-germany-edge`: no approved threshold, cells too small to report, and German staff in scope.
- `named-flight-risk-refusal`: a request to rank named employees by flight risk and push scores to managers.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. Job Openings and Labor Turnover Technical Note, U.S. Bureau of Labor Statistics. https://www.bls.gov/news.release/jolts.tn.htm. Supports: definitions of separations, quits, layoffs and discharges, other separations, and rates computed with employment as the denominator.
2. 2025 Recruiting Executives Benchmarking, SHRM, 2025. https://www.shrm.org/content/dam/en/shrm/research/2025-recruiting-benchmarking-report.pdf. Supports: time to fill defined as calendar days from requisition opened to offer accepted; positions internally filled defined as share of open positions filled by current employees.
3. How CHROs Can Power Up Their People Analytics, Eric House, SHRM Executive Network, 11 June 2025. https://www.shrm.org/executive-network/insights/how-chros-can-power-up-their-people-analytics--. Supports: start from strategic questions, link to business KPIs, data storytelling skills, governance and transparency with employees.
4. What HR Professionals Must Know About AI-Powered Analytics, Alex Alonso, SHRM, 26 March 2025. https://www.shrm.org/enterprise-solutions/insights/what-hr-professionals-must-know-about-ai-powered-analytics. Supports: data integrity and security, transparency in how AI reaches conclusions, involving legal and technology teams.
5. How do we ensure anonymisation is effective?, Information Commissioner's Office, 10 October 2025 (under review). https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/how-do-we-ensure-anonymisation-is-effective/. Supports: identifiability as a spectrum, singling out, removing identifiers is insufficient, motivated intruder test, context and recipients.
6. Manage Viva Glint confidentiality thresholds, Microsoft Learn. https://learn.microsoft.com/en-us/viva/glint/setup/manage-confidentiality-thresholds. Supports: practice example of minimum group sizes and suppressing a second group to stop scores being derived by simple math.
7. 29 CFR 1607.4, Uniform Guidelines on Employee Selection Procedures, Code of Federal Regulations (2024 edition), GovInfo. https://www.govinfo.gov/content/pkg/CFR-2024-title29-vol4/pdf/CFR-2024-title29-vol4-sec1607-4.pdf. Supports: four-fifths rule as evidence of adverse impact, smaller differences and small-numbers caveats.
8. Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1), NIST, July 2024. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf. Supports: confabulation risk, fact-checking and verifying sources and citations in generative AI outputs.
9. AI in the Workplace Playbook, SHRM, 2025. Read from a copy of the publication; no web address checked. Supports: model fact sheets, impact assessments, showing data was lawfully collected, impact assessment before using scraped data.
10. AIGP Body of Knowledge v2.1, IAPP, effective 2 February 2026. Read from a copy of the publication; no web address checked. Supports: data lineage and right to use, testing for bias and interpretability as well as accuracy, monitoring for drift and poor data, a policy to switch a system off.
