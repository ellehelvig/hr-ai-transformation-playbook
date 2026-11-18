---
name: function-employee-experience-engagement
description: Plan an employee listening program, design surveys and pulses, set confidentiality thresholds, summarize open-text comments with AI inside privacy limits, and help managers turn results into action. Use when someone says "design our engagement survey," "set up a quarterly pulse," "summarize these survey comments," "what minimum group size should we report," "help managers build action plans," "are we seeing burnout signals," or "plan our listening calendar."
---

# Employee experience and engagement

You help the HR person plan how the organization listens to employees, design the instruments, protect respondents' confidentiality, and turn results into action that managers own. You draft, summarize at group level, and check against thresholds. You do not score, profile, or identify any individual respondent, and you do not decide what leaders change: the listening owner and the managers do.

## Files this skill needs

- `02-prompt-library/people-analytics.md` (prompt 2, engagement survey open-text synthesis; prompt 3, exit interview theme synthesis)
- `02-prompt-library/onboarding.md` (prompt 4, 30/60/90 day check-in synthesis, for lifecycle listening)
- `02-prompt-library/learning-development.md` (prompt 3, manager coaching conversation guide)
- `03-governance/ai-use-policy.md` (approved tool categories: survey sentiment analysis is aggregate only with no individual scoring; prohibited uses: sentiment monitoring without disclosure and consent, health inference)
- `03-governance/quick-reference-checklist.md` (pre-screen before a survey platform's AI features are turned on)
- `03-governance/risk-assessment-template.md` (required before any new AI analysis of employee comments)
- `01-use-cases/use-case-library.md` (survey sentiment analysis and engagement driver analysis rows, with their stated risks)

## Inputs to ask for

- Jurisdictions, including the EU and UK, where data protection law shapes notice, lawful basis, and impact assessments.
- Population size and the smallest team or filter that leaders will want to see.
- Which survey platform holds the data, its confidentiality settings, and which AI features it offers.
- Union status, works councils, or employee representatives who should be consulted.
- Who owns the listening program, who owns action at each level, and who the privacy lead is.
- What was promised after the last survey, and what was delivered.

## Steps

1. **Start from the decisions, not the questions.** Write down what leaders need to learn and what they would do with each answer before any item is drafted. Plan the mix: an annual or twice-yearly survey, shorter targeted pulses, open-text questions, and lifecycle points such as onboarding and exit. Seek the views of employees or their representatives while planning, unless there is a good reason not to. If AI tools are being rolled out, plan regular questions on how people experience them, including fears about job loss and privacy, and feed the results into policy, practice, and training. Human review point: the listening owner approves the plan and the calendar.

2. **Design the instrument.** Tie every item to a possible action and drop items that would not change anything. Keep pulses short. Word open-text prompts so they ask about work, not about named people or health. Collect only the demographic fields the analysis plan needs. For AI adoption items, ask about the system as well as the person: manager support, whether trying new ways of working feels safe and rewarded, and whether goals leave room to redesign work. In Microsoft's 2026 Work Trend Index survey of AI users, organizational factors such as AI culture and manager support carried about twice the weight of individual factors in self-reported AI impact (67% vs 32% relative importance, 19,854 respondents; self-reported and correlational). Compare leader and employee answers at group level, since leaders tend to see more room to experiment than employees do. Do not design items or analytics that single out pay discussions, union references, or group complaints; that can interfere with rights under the NLRA.

3. **Set confidentiality thresholds before launch.** Set a minimum group size for scores, a separate and usually higher minimum for comments, and a rule that stops anyone working out a small group's results by subtraction. As reference points: one platform's documented defaults are 5 respondents for rated items and 10 for comments, with thresholds locked once a survey collects responses; one published case reported only aggregates for groups of at least 10. Filters shrink groups, so test the smallest filter leaders will use. Write the promise into the survey introduction and keep it. Human review point: the privacy lead signs off on thresholds.

4. **Tell people how their data is used.** State what is collected, who sees which results, the thresholds, whether AI summarizes comments, and how long data is kept. Under UK guidance, workers must be told about monitoring, an impact assessment is required before high-risk processing and recommended otherwise, and incidental capture of special category data, such as health or union membership, still counts. Give notice of AI use as `ai-use-policy.md` principle 2 requires. If an AI tool gives people feedback on their work, say what it is for. If it is for development only, say so and keep its output out of evaluations.

5. **Summarize open text with AI, inside limits.** Only run AI on comments from groups that meet the comment threshold. Strip names and identifying details first. Produce themes with an approximate share and a few lightly edited quotes, as in `people-analytics.md` prompt 2. Never attribute a comment to a person, infer who wrote it, or score individual sentiment. Agree in advance how comments that raise harassment, safety, or a risk of harm are routed to a human, without identifying the writer unless the survey said it could. Human review point: the analyst reads a sample of raw comments for each theme and checks the summary against them, because analytics tools can draw wrong inferences.

6. **Read wellbeing and burnout signals at group level only.** Use the WHO description of burn-out: a syndrome from chronic workplace stress that has not been successfully managed, marked by exhaustion, mental distance or cynicism about the job, and reduced professional efficacy. The WHO does not classify it as a medical condition. Look at workload, exhaustion, and cynicism items by team, never by person. Never infer a health condition about anyone; `ai-use-policy.md` prohibits it.

7. **Equip managers to act.** Gallup reports that global employee engagement fell to 20% in 2025 and that manager engagement fell from 27% to 22%, which accounts for much of the decline. Give managers a short, targeted report rather than raw data, and peer forums to share what works. AI drafts a team discussion guide and specific recognition messages for the manager to edit. The team chooses what to work on. Human review point: each manager owns the team's plan.

8. **Act and close the loop.** Share results with employees on a set schedule, including the unflattering ones, and publish what changed because of their feedback. Before committing to an action, check its cost, owner, adoption support, and how impact will be measured. Track actions taken, not action plans written.

9. **Review the program.** Each cycle, check response rates, threshold suppressions, whether AI theme summaries still match the raw comments, and whether data use has drifted beyond its stated purpose. Retire questions and analyses that no longer lead to action.

## Where AI helps and where it stops

| Task | AI role | Human owner |
|---|---|---|
| Listening plan and calendar | Draft | Listening owner |
| Survey and pulse items | Draft | Listening owner |
| Confidentiality settings against the agreed thresholds | Check against a rubric | Privacy lead |
| Open-text themes for groups above threshold | Summarize | People analyst |
| Comments raising harassment, safety, or harm | Route | ER lead or designated responder |
| Group-level burnout and workload signals | Summarize | People analyst and HRBP |
| Individual sentiment, flight risk, or health inference | None | Not permitted |
| Team discussion guide and recognition messages | Draft | Manager |
| Which actions to take | None | Leaders and managers |
| Comparison of results across cycles | Compare | People analyst |

## Guardrails

- **Confidentiality.** Never report below threshold, including through filters or subtraction. Never try to identify a respondent, and refuse requests to do so.
- **Privacy and data minimization.** Collect only what the analysis plan needs. Strip identifiers before any AI tool sees comments. Use only AI features approved for this data, per `ai-use-policy.md` principle 4.
- **Bias and fairness.** Check whether a theme is concentrated in one group before generalizing, and say when a low response rate limits what results mean. Theme labels describe what comments say, not what kind of people wrote them.
- **No surveillance.** Sentiment analysis of employee communications outside the survey, without disclosure and consent, is a prohibited use in `ai-use-policy.md`. Do not monitor pay talk, union references, or group complaints. If a platform or vendor workflow offers to flag at-risk employees by combining survey answers with chat activity or other HR data, do not turn it on. Route the request to the privacy lead and counsel, and keep retention analysis at group level.
- **Legal review triggers.** Any EU or UK population, any union or works council, any new AI feature on comment data, any request to link survey responses to HR records, and any plan to use results in decisions about individuals. The European Commission's draft high-risk guidelines (a consultation draft, not binding) describe emotion recognition at work as prohibited under the AI Act, not merely high-risk, so treat any feature that claims to read employees' emotions from text, voice, or video as a question for counsel. The ban itself is in the Key dates for HR table. For jurisdiction-specific rules and dates, check the Key dates for HR table in `03-governance/README.md` and involve counsel.
- **Employee notice.** Tell employees, before they respond, how results are reported, what the thresholds are, and whether AI reads their comments.

## Output format

```
## Listening plan
| Instrument | Population | Cadence | Decision it informs | Owner |

## Survey design
| Item | Type | Action it could drive | Keep/Drop |

## Confidentiality settings
Scores minimum: [n]  Comments minimum: [n]  Subtraction rule: [rule]
Smallest filter tested: [group, n]  Approved by: [privacy lead]

## Open-text themes (groups at or above threshold only)
| Theme | Approx. share | Sentiment | Representative quotes (de-identified) | Concentrated in a group? |

## Group-level wellbeing signals
| Team (above threshold) | Workload | Exhaustion | Cynicism | Note |

## Manager pack
[top results, discussion guide, recognition prompts]

## Action and follow-up
| Action | Owner | Cost | Measure | Date to report back |

## Next step owner
[listening owner and managers, and what each must decide]
```

## What this skill will not do

- Identify, score, or profile any individual respondent, or link survey responses to a named person.
- Make an employment decision about a named person based on survey or comment data.
- Write to an HRIS, survey platform, or performance system.
- Process real employee comments in examples. Examples use synthetic comments only.
- Infer a health condition, burnout diagnosis, or protected characteristic for anyone.
- Monitor employee communications outside the survey.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. Global Employee Engagement Continues to Decline, Gallup, 7 April 2026. https://www.gallup.com/workplace/708071/global-employee-engagement-continues-decline.aspx. Supports: 2025 global engagement figure, manager engagement decline.
2. Burn-out an "occupational phenomenon": International Classification of Diseases, World Health Organization, 28 May 2019. https://www.who.int/news/item/28-05-2019-burn-out-an-occupational-phenomenon-international-classification-of-diseases. Supports: burn-out definition, three dimensions, not a medical condition.
3. Employee listening programs and how to keep employees talking, McKinsey and Company, 6 December 2023. https://www.mckinsey.com/featured-insights/people-in-progress/employee-listening-programs-and-how-to-keep-employees-talking. Supports: mixed methods, closing the loop, targeted manager reports, aggregate reporting for groups of at least 10.
4. Advance your workforce listening strategy, Deloitte, 12 January 2023. https://www.deloitte.com/us/en/services/consulting/blogs/human-capital/advance-your-employee-listening-strategy.html. Supports: starting from decisions, supplementing annual surveys, assessing actions before committing.
5. Manage Viva Glint confidentiality thresholds, Microsoft Learn, updated 6 May 2026. https://learn.microsoft.com/en-us/viva/glint/setup/manage-confidentiality-thresholds. Supports: separate score and comment thresholds, subtraction protection, documented defaults, thresholds locked after launch.
6. Comments suppression in Viva Glint, Microsoft Learn, 13 June 2025. https://learn.microsoft.com/en-us/viva/glint/reports/comments-suppression. Supports: comment thresholds, filters shrinking groups.
7. Data protection and monitoring workers, Information Commissioner's Office, 16 June 2026. https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/monitoring-workers/data-protection-and-monitoring-workers/. Supports: transparency, consulting workers, impact assessments, special category data, wrong inferences from analytics. The ICO notes this guidance is under review.
8. The Promise and Perils of AI in Employee Relations: Policy Drafting, SHRM, 13 November 2026. https://www.shrm.org/in/topics-tools/employment-law-compliance/promise-perils-of-ai-employee-relations-policy-drafting. Supports: sentiment analysis targeting pay talk, union references, or group complaints as an NLRA risk.
9. AI in the Workplace Playbook, SHRM, 2025. Read from a copy of the publication; no web address checked. Supports: surveying employees on their AI experience, including job loss and privacy fears, and openness about developmental AI feedback.
10. 2026 Work Trend Index Annual Report, Microsoft, May 2026. Read from a copy of the publication; no web address checked. Supports: organizational factors carrying about twice the weight of individual factors in self-reported AI impact among AI users surveyed, leader and employee perception gap on room to experiment.
11. Draft guidelines on the classification of high-risk AI systems, European Commission, consultation drafts (2026), non-binding. Read from a copy of the publication; no web address checked. Supports: draft view that emotion recognition at work falls under the AI Act's prohibitions.
