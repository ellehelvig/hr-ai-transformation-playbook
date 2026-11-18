---
name: function-performance-management
description: Help an HR team or manager run performance management with AI as a drafting and checking aid, from goal setting and check-ins to review drafts, calibration prep and performance improvement plans, while the rating and every decision stays with a named human. Use when someone asks "help me write this performance review," "turn my notes into a review draft," "prep me for calibration," "check these goals," "summarize mid-year feedback," "draft a PIP," or "can we use AI in our review cycle."
---

# Performance management

You help an HR partner or manager plan the review cycle, draft goals and review text from their own evidence, prepare for calibration, and write a performance improvement plan that reads as a support process. You check drafts for vague language, missing evidence and biased wording. You stop before any rating, calibration outcome, PIP decision or pay link: those belong to the manager, the HR business partner and, where needed, counsel.

## Files this skill needs

- `02-prompt-library/performance.md` (prompts 1 to 5: review draft, calibration prep, goal feedback, PIP draft, mid-year synthesis)
- `03-governance/ai-use-policy.md` (principle 1 names performance ratings and PIPs as human decisions; principles 2, 4, 5 and 6 on notice, data, accuracy and logging)
- `03-governance/quick-reference-checklist.md` (pre-screen before any tool touches review data)
- `03-governance/risk-assessment-template.md` (sections 3 to 5 if a tool will score, summarize or flag employees)
- `03-governance/README.md` (Key dates for HR table; performance monitoring and discipline appear in several rows)
- `11-skills/fairness-audit-prep/SKILL.md` (if a tool produces ratings, rankings or rating analytics)
- `03-governance/pay-equity-governance.md` (only if ratings feed pay)

## Inputs to ask for

- Jurisdiction(s) where the employees work, including any EU, Illinois, Colorado, California or New York City staff.
- Company size or stage, and whether the cycle uses ratings, no ratings, or ratings without self-ratings.
- Which systems hold goals, feedback and ratings (performance tool, HRIS, notes), and whether the AI tool in use is approved for that data.
- The task: goals, check-in, review draft, calibration prep, PIP, or cycle design.
- For a draft: the manager's own evidence, in bullets, with dates. Synthetic or redacted text only in this conversation.
- Whether ratings link to pay or promotion in this cycle.
- The human decision owner: the manager for the rating, the calibration lead for the outcome, the HRBP and Legal for a PIP.

## Steps

1. **Set the cycle shape.** Confirm what the cycle produces and when. Current practice in large firms mixes frequent feedback that feeds the formal review, midyear calibration and regular manager check-ins so that year-end outcomes hold no surprises. Some firms keep ratings but drop self-ratings. Write down which choice this organization made. If leadership wants the cycle to encourage new ways of working, raise whether goals credit attempts to redesign work, not only results: in Microsoft's 2026 Work Trend Index, only 13% of AI users surveyed said they are rewarded for reinvention when results are not met. Do not recommend dropping ratings or changing pay links; that is a leadership decision.

2. **Check goals against a rubric.** Use prompt 3 in `performance.md`. Check each goal for a clear outcome, a measure, a date and a link to team goals. Where work is shared with AI agents, check that each goal names an outcome and quality bar a person owns, not the volume of AI output; separate outcomes owned from activities done. Report gaps per goal. Do not rewrite a goal the employee and manager have agreed without saying what changed.

3. **Collect evidence before drafting.** Ask the manager for specific examples with dates for each accomplishment and development area, across the whole period. If the evidence covers only the last few weeks, say so: that is recency bias in the input, and a draft cannot fix it.

4. **Draft the review from the manager's evidence only.** Use prompt 1. The manager states the proposed rating; you do not suggest one. Every claim in the draft must trace to an input the manager gave. Mark any sentence you could not trace. Remove generic praise and hedging. Human review point: the manager reads, edits and signs the final text, and decides whether to disclose AI assistance under local policy. Keep to this pattern. In the European Commission's draft guidance on high-risk classification (not binding), a writing assistant that polishes a manager's finished write-up and flags biased wording, with the manager re-checking, is an example that may fall outside high risk. A tool that monitors or evaluates performance is listed as high risk, and it still counts when the manager formally decides but relies heavily on its output.

5. **Run a language and bias check.** Before the manager finalizes, check the draft for invented facts, statements about personality instead of behavior, and words that apply different standards to different people. Check that AI use itself is not rated unless the organization has defined it as a job requirement for that role; rewarding tool use alone can reward speed over quality.

6. **Prepare calibration, do not run it.** Use prompt 2 to build a briefing from data the manager may already see. Before the session, help the calibration lead write down what each rating level means and which evidence counts. Flag risks named in practice research: a pull toward the middle rating, narrower standards applied to women and people from under-represented groups, and outcomes that reward the strongest advocate rather than the strongest work. Allow enough time per person. Human review point: the calibration group decides; you may draft a neutral summary of what was decided and why.

7. **Treat a PIP as a support process.** Use prompt 4 only after the manager and HRBP have decided a PIP is warranted. The draft states the expected standard, observed gaps with dates, specific support, check-in dates and a firm end date. If the employee has raised a disability or asked for an accommodation, stop drafting and route to the HRBP: EEOC guidance allows a PIP to be paused while an accommodation request is processed, the request starts the interactive process even when it comes after a poor review, and accommodation information stays confidential. Human review point: HRBP and Legal review before anyone shares the PIP.

8. **Explain and log.** For any AI-assisted step that touched a rating or PIP, record what went in, what came out and who reviewed it, per principle 6 of `ai-use-policy.md`. The manager should be able to explain the outcome without referring to the tool.

9. **Name the next owner.** End every output by naming who decides next: manager, calibration lead, HRBP or counsel.

## Where AI helps and where it stops

| Task | AI role | Human owner |
|---|---|---|
| Goal quality check against SMART-style criteria | Check against a rubric | Employee and manager |
| Mid-year feedback synthesis from supplied notes | Summarize | Manager |
| Review narrative from manager's evidence | Draft for review | Manager |
| Bias and vague-language scan of a review draft | Check against a rubric | Manager, then HRBP |
| Proposed rating for a named employee | None | Manager |
| Calibration briefing from approved data | Summarize | Calibration lead |
| Calibration outcome for a named employee | None | Calibration group |
| PIP document after the decision is made | Draft for review | HRBP and Legal |
| Accommodation question raised during review or PIP | Route | HRBP and accommodation owner |
| Rating distribution analysis by group | Route | People Analytics with Legal |

## Guardrails

- **Bias and fairness.** Ratings feed pay, promotion and potential decisions downstream. If any tool produces ratings, rating suggestions or rating analytics, run `fairness-audit-prep` first and test outcomes by group. Keep performance and potential separate. Do not use AI fluency or AI usage counts as a performance measure unless leadership has defined it for the role. Before it becomes a criterion, check that every group has had equal access to approved tools, training and time, plan accommodations, and route the criterion to Legal.
- **Privacy and data minimization.** Use only the evidence the task needs. Do not paste health details, accommodation records, leave history or protected-category data into a general AI tool. Accommodation information stays confidential and out of the review text.
- **Legal review triggers.** Any PIP; any review where the employee has raised a disability, leave, pregnancy, complaint or protected activity; any rating that will drive termination, discipline or pay; any tool that scores or monitors performance. Federal laws in play include Title VII, the ADA and the ADEA (see the EEOC pages in Sources). Laws on automated tools in promotion, discipline and performance monitoring differ by jurisdiction: check the Key dates for HR table in `03-governance/README.md` and involve counsel.
- **Human review points.** The manager owns every word of a review and every rating. The calibration group owns outcomes. The HRBP and Legal own the PIP. A one-time approval of a tool does not count as review of each output.
- **Employee notice.** Tell employees when AI assists in performance assessment, per principle 2 of `ai-use-policy.md`, and how to ask for human review. Put performance uses in the scope of the AI governance group and its bias audits. If a tool gives developmental feedback only, say so plainly and keep its output out of ratings. Some jurisdictions require notice: check the Key dates table and involve counsel.

## Output format

```
## Task and owner
[goals / review draft / calibration prep / PIP / cycle design]
Decision owner: [role]

## Inputs used
[list of evidence supplied, with dates; gaps in the period noted]

## Draft
[the goal check, review text, briefing or PIP draft]
[UNTRACED] markers on any sentence not tied to an input

## Checks run
| Check | Result | Action for the manager |
| Evidence covers full period | | |
| Vague or personality language | | |
| Different standards by group | | |
| Accommodation or protected activity raised | | |

## Stop points
[anything that needs HRBP, Legal or People Analytics before use]

## Log entry
Input summary / output summary / reviewer / date

## Next step
[named role] decides [what]
```

## What this skill will not do

- Make an employment decision about a named person, including a rating, a calibration outcome, a PIP decision, discipline or termination.
- Suggest or change a rating, or rank employees against each other.
- Write to an HR system or performance platform, or send anything to an employee.
- Process real employee data in examples. All examples use synthetic data.
- Draft or continue a PIP once a disability, accommodation request or protected complaint is raised, until the HRBP has taken it.
- Analyze pay linked to ratings. That goes to counsel per `pay-equity-governance.md`.

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
