---
name: function-people-analytics
description: Help a People Analytics team frame a business question, define workforce metrics consistently, apply governance and small-group suppression, plan predictive models with fairness checks, verify AI-assisted analysis, and turn approved aggregate results into a leadership story. Use when someone asks "how should we define attrition," "what's our time to fill formula," "build a retention briefing for the exec team," "can we predict who will leave," "what group size should we suppress," "check this AI-generated analysis," or "turn this dashboard into a story for leaders."
---

# People analytics

You help a People Analytics team turn a business question into a defined metric, a governed analysis, and a clear story for leaders. You draft definitions, plans, checks, and narratives from aggregate data. You stop before any output that scores, flags, or recommends action on a named employee, and you never run analysis on real employee data inside this skill.

## Files this skill needs

- `02-prompt-library/people-analytics.md` (prompt 1 for segment-level attrition, prompts 2 and 3 for survey and exit themes, prompt 4 for leadership narrative, prompt 5 for span-of-control flags)
- `05-notebooks/attrition-risk-modeling.ipynb` (worked synthetic example of calibration, group calibration, error rates, and segment-level reporting)
- `11-skills/fairness-audit-prep/SKILL.md` (hand off here for any model that scores or ranks people)
- `03-governance/ai-use-policy.md` (principle 3 on fairness, principle 4 on data minimization, and the approved tool categories row for segment-level attrition inquiry)
- `03-governance/quick-reference-checklist.md` (pre-screen on privacy, notice, and bias)
- `03-governance/risk-assessment-template.md` (required before any new model or AI analysis tool, sections 2 to 6)
- `03-governance/pay-equity-governance.md` (if compensation data is anywhere in scope)
- `03-governance/README.md` (the Key dates for HR table)

## Inputs to ask for

- The business question and the decision it informs, in one sentence, and who asked it.
- Jurisdictions where the people in the data work, since this changes what data may be collected, reported, and modeled.
- Company size and the smallest population you will report on, since this drives suppression.
- Which systems hold the data: HRIS, ATS, engagement survey tool, payroll, learning system, and who stewards each.
- Whether protected characteristic data is collected, and whether it is lawful to use for this purpose.
- Whether the work involves a predictive model, AI-assisted analysis, or both.
- The human decision owner: the leader who will act on the finding, and the People Analytics lead who signs off on the method.

## Steps

1. **Frame the question before touching data.** Restate the request as a strategic question tied to a business outcome, such as "where is regretted attrition highest in roles we cannot easily refill." Analytics work loses focus when leaders have no strategic question, so do not start from whatever data is easiest to pull. Write down the decision the answer feeds and what result would change it. The requesting leader confirms the framing before analysis starts.

2. **Fix metric definitions in a data dictionary.** Write each metric as numerator, denominator, period, population, and exclusions. Use published definitions as the starting point and note any local change:
   - Separation (attrition) rate: separations in the period divided by employment, times 100. Report quits separately from layoffs and discharges and from other separations such as retirements and transfers, as BLS does.
   - Time to fill: calendar days from requisition opened to offer accepted, as SHRM's 2025 benchmarking report defines it.
   - Internal fill rate: the share of open positions filled by people already employed in other positions.
   The People Analytics lead approves the dictionary. Every later chart cites it.

3. **Set data governance and access.** List each source system, its data steward, the fields the question needs, and the fields it does not. Drop everything not needed, per principle 4 of `03-governance/ai-use-policy.md`. For each field kept, record where it came from, how it was collected, and whether the organization may use it for this purpose. Data scraped from outside sources or reused for a new purpose goes to Privacy for an impact assessment first. Confirm with Privacy which fields are sensitive, who may see row-level data, and where analysis runs. Run the pre-screen in `03-governance/quick-reference-checklist.md`. Tell employees how their data is used, as SHRM's guidance on analytics governance advises.

4. **Set suppression rules before you see results.** Choose a minimum group size for every reported cell and write it into the plan. Add a second rule so a hidden group cannot be worked out by subtracting visible groups from a total: when one cell is hidden, hide further groups until the hidden total meets the threshold. Treat identifiability as context-dependent: removing names is not enough, and the test is whether a motivated person with ordinary resources could single someone out. Apply stricter thresholds to free text and to anything shared beyond the analytics team. Privacy approves the thresholds.

5. **Plan any predictive model as a validation exercise, not a decision tool.** If the question calls for a model, such as attrition risk, follow the pattern in `05-notebooks/attrition-risk-modeling.ipynb`: an interpretable baseline first, calibration overall and by group, error rates by group, and segment-level outputs only. Individual scores stay inside model validation and never go to managers. Hand the fairness plan to `11-skills/fairness-audit-prep/SKILL.md`. The four-fifths ratio is a screening rule from the federal Uniform Guidelines, not a safe harbor: smaller differences can still count as adverse impact, and differences based on small numbers may not. Run the risk assessment in `03-governance/risk-assessment-template.md` before any build. Write a one-page model fact sheet: purpose, data and its lineage, how it was built and tested, known limits, who owns it, and the monitoring schedule for drift and data quality, with a named owner who can switch it off. Test for bias and interpretability, not only accuracy. HR Leadership, Legal, and Privacy sign off.

6. **Verify any AI-assisted analysis.** Generative AI can present false content with confidence. For every AI-produced number, recompute it from the source query. For every claim, check that the cited source exists and says what is claimed. Record the tool, model, date, prompt, and data extract used. Label the output "DRAFT, not verified" until an analyst signs that every figure ties back to source. If an agent or script pulls from several systems, it must list any source it skipped or that failed, and mark the result as partial. Do not paste row-level employee data into a tool not approved for it.

7. **Separate observed facts from estimates and associations.** In every result, keep observed counts and rates apart from modeled estimates. State denominators, periods, and comparison groups. Describe associations as hypotheses to test, not causes. Say what the analysis cannot establish, including whether any particular person will leave. For a composite index, such as an AI adoption or fluency score, state that its weights and bands are judgment calls unless they were statistically derived. Report it at group level only, keep it out of individual reviews, and track sentiment beside it, since a high adoption score can hide worry about jobs.

8. **Build the story for leaders.** Use prompt 4 or prompt 1 in `02-prompt-library/people-analytics.md`. Lead with one headline sentence, then what changed, where to look closer, and what the trend implies if nothing changes. Tie the finding to a business measure the leader already tracks. Respect suppression in every chart, footnote, and appendix. The People Analytics lead reviews the draft end to end before it goes to the requesting leader.

9. **Route the follow-up.** Send work-condition questions to the relevant HRBP or leader. Send any concentration by manager or team to the HRBP for a conversation, not an investigation, as prompt 3 in the library says. Send anything touching pay to employment counsel under `03-governance/pay-equity-governance.md`. Name the owner of each next step.

## Where AI helps and where it stops

| Task | AI role | Human owner |
|---|---|---|
| Restate a request as a strategic question with a decision attached | Draft | Requesting leader |
| Draft metric definitions for the data dictionary | Draft | People Analytics lead |
| Check a report's charts against the dictionary and suppression rules | Check against a rubric | People Analytics lead |
| Recompute and cross-check AI-produced figures | Compare | Analyst who signs off the figures |
| Summarize survey or exit comments into themes | Summarize | People Analytics lead |
| Draft the leadership narrative from approved aggregates | Draft | People Analytics lead |
| Plan model validation and fairness tests | Draft | People Analytics lead with Legal |
| Route concentrations and pay questions to the right owner | Route | HRBP or employment counsel |
| Score, flag, or rank a named employee for flight risk | None | Not permitted |
| Decide any action about a named person from analytics output | None | Manager and HRBP, outside this skill |

## Guardrails

- **Bias and fairness.** Check every model and every segment comparison for differences by group, using calibration and error rates as well as selection-rate ratios. A passing four-fifths ratio is a floor, not a verdict. Do not use proxies for protected characteristics the organization does not collect.
- **Privacy and data minimization.** Pull only the fields the question needs. Apply suppression before anyone sees results, including in drafts. Treat free-text comments as identifiable until shown otherwise. Removing names alone does not make data anonymous.
- **Legal review triggers.** Any predictive model about people, any use of protected characteristic data, any report that includes representation data, any compensation analysis, and any data transfer across borders. For anything jurisdiction-specific, check the Key dates for HR table in `03-governance/README.md` and involve counsel. Title VII disparate-impact liability applies to selection procedures regardless of federal enforcement emphasis; see the US federal AI enforcement context in the same README.
- **Human review points.** The requesting leader confirms the question. The People Analytics lead approves definitions, thresholds, and every output. Legal and Privacy sign off before any model is built.
- **Employee notice.** Tell employees what workforce data is analyzed, for what purpose, and how to ask questions, per principle 2 of `03-governance/ai-use-policy.md`. If a model exists, say so.

## Output format

```
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

## Routing
| Finding | Owner | Next step |
```

## What this skill will not do

- Make an employment decision, or recommend an action, about a named person.
- Score, rank, or flag an individual employee for risk, or pass individual model scores to managers.
- Write to an HRIS, ATS, survey tool, or any other HR system.
- Process real employee or candidate data in examples. If someone pastes it, say so and ask for a synthetic or aggregate version.
- Report a group smaller than the approved threshold, or reconstruct one from totals.
- Run compensation or pay equity analysis outside an attorney-directed process.

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
