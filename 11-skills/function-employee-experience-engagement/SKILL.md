---
name: function-employee-experience-engagement
description: Plans an employee listening program and turns results into manager-owned action, producing a listening calendar, survey and pulse items tied to decisions, confidentiality thresholds with a subtraction rule, group-level open-text themes, group-level burnout signals, a manager pack, and an action tracker. Use whenever someone says "design our engagement survey," "set up a quarterly pulse," "summarize these survey comments," "what minimum group size should we report," "help managers build action plans," "are we seeing burnout signals," "ask people how the AI rollout is going," or "plan our listening calendar," and whenever a survey platform's AI feature is about to touch comments. Never identifies, scores, or profiles an individual respondent.
---

# Employee experience and engagement

This skill serves the listening program owner, people analyst, or HRBP who must plan how the organization listens, protect respondents' confidentiality, and turn results into action managers own. It drafts, summarizes at group level, and checks settings against agreed thresholds. It stops before identifying any respondent and before deciding what leaders change: the listening owner, privacy lead, and managers own those calls.

## Files this skill needs

- `02-prompt-library/people-analytics.md` (prompt 2, engagement survey open-text synthesis; prompt 3, exit interview theme synthesis)
- `02-prompt-library/onboarding.md` (prompt 4, 30/60/90 day check-in synthesis, for lifecycle listening)
- `02-prompt-library/learning-development.md` (prompt 3, manager coaching conversation guide)
- `03-governance/ai-use-policy.md` (approved tool categories: survey sentiment analysis is aggregate only with no individual scoring; principle 2 on notice; principle 4 on data; prohibited uses: sentiment monitoring without disclosure and consent, health inference)
- `03-governance/quick-reference-checklist.md` (pre-screen before a survey platform's AI features are turned on)
- `03-governance/risk-assessment-template.md` (required before any new AI analysis of employee comments)
- `01-use-cases/use-case-library.md` (survey sentiment analysis and engagement driver analysis rows, with their stated risks)
- `03-governance/README.md` (Key dates for HR table, used by the Regulation map)

## Inputs

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| Decisions leaders need the listening to inform | Yes | Ask the user | Whether to slow the AI coding assistant rollout |
| Jurisdictions, including EU and UK populations | Yes | HRIS, read-only: headcount by country and state | US 1,180; Germany 220 |
| Population size and the smallest group leaders will filter to | Yes | HRIS, read-only: org unit headcounts | Smallest filter: Berlin Platform team, 11 people |
| Survey platform, its confidentiality settings, and its AI features | Yes | Survey platform, read-only: threshold settings, feature list | Scores 5, comments 10, AI comment summary available |
| Works council, union, or employee representatives to consult | Yes | Ask the user | Berlin works council exists |
| Owners: listening program, action at each level, privacy lead | Yes | Ask the user | People Analytics lead; each manager; privacy lead |
| Results and comments for groups at or above threshold | No | Survey platform export, read-only: aggregate scores, response counts, de-identified comments | 471 of 620 responded |
| What was promised after the last survey, and what was delivered | No | Ask the user | Promised meeting-free Fridays; piloted in two teams |

If a required input is missing, ask for it once, in one short question at the top of your reply. Then proceed and label each gap "Not provided" in the output and the audit trail.

## Tools and connectors

- **Reads allowed, read-only, minimum fields.** Survey platform (threshold settings, response counts, aggregate item scores by group at or above threshold, de-identified comments for groups at or above the comment threshold). HRIS (org unit headcounts and headcount by location only). Use MCP connectors or exports. Never request respondent-level rows or any join of survey responses to employee IDs.
- **Repo tool.** `ask_governance_policy` in `10-mcp-agents/policy_qa/` cites `03-governance/*.md`, for example the approved tool categories row on survey sentiment analysis. It is not legal advice.
- **Never write.** Do not call any write, send, update, publish, or settings tool, even if the connector offers one. Do not turn on a platform AI feature. Humans publish results and send communications.
- **Log every call.** Record tool, purpose, and fields read in the audit trail.
- **Stop on spillover.** If a tool returns respondent-level data, names, employee IDs, or a group below threshold, stop, do not use it, and ask the user how to proceed.

## By maturity stage

Stages follow the repo's maturity scale in [the roadmap template](../../06-roadmap/transformation-roadmap-template.md). Decision rights in this skill are the same at every stage.

| Stage | How to run it | Before moving up |
|---|---|---|
| Start (Levels 0 to 1) | Paste agreed thresholds, org unit headcounts and de-identified comments from groups above threshold. The analyst checks themes against raw comments. | Privacy lead approves thresholds and the notice. |
| Pilot (Level 2) | One read-only survey export: threshold settings, response counts, group scores, de-identified comments. Metric: action close-out rate. | One cycle with no below-threshold report. |
| Scale (Level 3) | Read-only survey platform and HRIS headcounts; checks settings against thresholds each cycle; tracks belief in action. Platform AI comment features: not before the risk assessment and counsel approval. | Data use has not drifted from its stated purpose. |
| Embed (Levels 4 to 5) | A pulse closing triggers draft themes and manager packs for sign-off. A human sends results. Never joins responses to HR records. | Rerun the test cases in `evals/` when the skill or model changes. |

## Steps

Run as a checkpointed workflow: complete a step, show it, and wait for the named sign-off before any step that depends on it.

1. **Start from the decisions, not the questions.** Write down what leaders need to learn and what they would do with each answer before any item is drafted. Plan the mix: an annual or twice-yearly survey, shorter targeted pulses, open-text questions, and lifecycle points such as onboarding and exit. Seek the views of employees or their representatives while planning, unless there is a good reason not to. If AI tools are being rolled out, plan regular questions on how people experience them, including fears about job loss and privacy, and feed results into policy, practice, and training. Sign-off: listening owner approves plan and calendar.

2. **Design the instrument.** Tie every item to a possible action and drop items that would not change anything. Keep pulses short. Word open-text prompts to ask about work, not about named people or health. Collect only the demographic fields the analysis plan needs. For AI adoption items, ask about the system as well as the person: manager support, whether trying new ways of working feels safe and rewarded, and whether goals leave room to redesign work. In Microsoft's 2026 Work Trend Index survey of AI users, organizational factors such as AI culture and manager support carried about twice the weight of individual factors in self-reported AI impact (67% vs 32% relative importance, 19,854 respondents; self-reported and correlational). Compare leader and employee answers at group level, since leaders tend to see more room to experiment than employees do. Do not design items or analytics that single out pay discussions, union references, or group complaints; that can interfere with rights under the NLRA. Sign-off: listening owner.

3. **Set confidentiality thresholds before launch.** Set a minimum group size for scores, a separate and usually higher minimum for comments, and a rule that stops anyone working out a small group's results by subtraction. Reference points: one platform's documented defaults are 5 respondents for rated items and 10 for comments, with thresholds locked once a survey collects responses; one published case reported only aggregates for groups of at least 10. Filters shrink groups, so test the smallest filter leaders will use. Write the promise into the survey introduction and keep it. Sign-off: privacy lead.

4. **Give notice before anyone responds.** State what is collected, who sees which results, the thresholds, whether AI summarizes comments, how long data is kept, and who to contact with a question or objection. Under UK guidance, workers must be told about monitoring, an impact assessment is required before high-risk processing and recommended otherwise, and incidental capture of special category data, such as health or union membership, still counts. Give notice of AI use per `ai-use-policy.md` principle 2. If an AI tool gives people feedback on their work, say what it is for; if it is for development only, say so and keep its output out of evaluations. Sign-off: privacy lead; counsel for any EU or UK population or works council.

5. **Summarize open text, inside limits.** Run AI only on comments from groups at or above the comment threshold. Strip names and identifying details first. Produce themes with an approximate share and a few lightly edited quotes, as in `people-analytics.md` prompt 2. Check whether each theme is concentrated in one group before generalizing. Never attribute a comment to a person, infer who wrote it, or score individual sentiment. Route comments that raise harassment, safety, or a risk of harm to the designated responder under a rule agreed before launch, without identifying the writer unless the survey said it could. Sign-off: the analyst reads a sample of raw comments for each theme and checks the summary against them, because analytics tools can draw wrong inferences.

6. **Read wellbeing and burnout signals at group level only.** Use the WHO description of burn-out: a syndrome from chronic workplace stress that has not been successfully managed, marked by exhaustion, mental distance or cynicism about the job, and reduced professional efficacy. The WHO does not classify it as a medical condition. Look at workload, exhaustion, and cynicism items by team, never by person. Never infer a health condition about anyone; `ai-use-policy.md` prohibits it. Sign-off: people analyst and HRBP.

7. **Equip managers to act.** Gallup reports that global employee engagement fell to 20% in 2025 and that manager engagement fell from 27% to 22%, which accounts for much of the decline. Give managers a short, targeted report rather than raw data, and peer forums to share what works. The agent drafts a team discussion guide and specific recognition messages for the manager to edit. The team chooses what to work on. Sign-off: each manager owns the team's plan.

8. **Act and close the loop.** Share results with employees on a set schedule, including the unflattering ones, and publish what changed because of their feedback. Before committing to an action, check its cost, owner, adoption support, and how impact will be measured. Track actions taken, not action plans written. Give every action a proposed report-back date, relative to results release if no calendar is given (for example "30 days after results, to confirm"), rather than leaving it blank. Sign-off: listening owner approves each communication; a human sends it.

9. **Review the program each cycle.** Check response rates, threshold suppressions, whether AI theme summaries still match the raw comments, and whether data use has drifted beyond its stated purpose. Retire questions and analyses that no longer lead to action. Sign-off: listening owner and privacy lead.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Listening plan and calendar | Listening owner | Drafts for sign-off |
| Survey and pulse items | Listening owner | Drafts for sign-off |
| Confidentiality thresholds and subtraction rule | Privacy lead | Drafts for sign-off |
| Check platform settings against the agreed thresholds | Privacy lead | Does alone |
| Open-text themes for groups at or above threshold | People analyst | Drafts for sign-off |
| Flag a comment raising harassment, safety, or harm for the designated responder | ER lead or designated responder | Does alone |
| Group-level burnout and workload signals | People analyst and HRBP | Drafts for sign-off |
| Team discussion guide and recognition messages | Manager | Drafts for sign-off |
| Which actions to take | Leaders and managers | Drafts for sign-off |
| Results communication to employees | Listening owner | Drafts for sign-off |
| Individual sentiment, flight risk, or health inference | Not permitted | Refuses and routes |
| Turn on a platform AI feature or link survey data to HR records | Privacy lead and counsel | Refuses and routes |

### Refuse and route

- "Who wrote this comment?" or "which Berlin people scored us low?": refuse; route to the privacy lead. Report the theme at group level only.
- "Show the results for the six-person team" or "filter until we see the new hires on that team": refuse below-threshold or subtraction reporting; route to the privacy lead with the threshold rule.
- "Combine survey answers with chat activity to flag at-risk employees": refuse; this is a prohibited use without disclosure and consent; route to the privacy lead and counsel and keep retention analysis at group level.
- "Run emotion detection on the comments or meeting recordings": refuse; route to counsel and point to the Regulation map.
- "Tag comments that mention pay or the union": refuse; route to counsel as an NLRA interference risk.
- "Tell us which employees are burned out": refuse; route to the HRBP with group-level signals.
- "Use the pulse scores in this manager's performance review" or any decision about a named person: refuse; route to the listening owner and counsel.
- "Turn on the platform's AI summary" or "send the results email": refuse; the privacy lead approves features and a human sends.
- "Use real comments in the example": refuse; examples use synthetic comments only.

## Guardrails

- **Confidentiality.** Never report below threshold, including through filters or subtraction. Never try to identify a respondent.
- **Privacy and minimization.** Collect only what the analysis plan needs. Strip identifiers before any AI tool sees comments. Use only AI features approved for this data (`ai-use-policy.md` principle 4).
- **Fairness.** Check whether a theme is concentrated in one group before generalizing, and say when a low response rate limits what results mean. Theme labels describe what comments say, not what kind of people wrote them.
- **No surveillance.** Sentiment analysis of employee communications outside the survey, without disclosure and consent, is a prohibited use in `ai-use-policy.md`. Do not monitor pay talk, union references, or group complaints.
- **Explainability and notice.** Tell employees before they respond how results are reported, the thresholds, and whether AI reads their comments; after the cycle, tell them what changed.
- **Legal review triggers.** Any EU or UK population, any union or works council, any new AI feature on comment data, any request to link responses to HR records, and any plan to use results in decisions about individuals. The European Commission's draft high-risk guidelines (a consultation draft, not binding) describe emotion recognition at work as prohibited under the AI Act, not merely high-risk, so treat any feature that claims to read emotions from text, voice, or video as a question for counsel.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| EU AI Act, emotion recognition at work (Article 5(1)(f)) | A survey or platform feature would infer emotions of German staff from text, voice, or video | Refuses the feature and routes to counsel |
| California AB 1883 (Ch. 853, Stats. 2026) | Emotion inference is proposed for California workers | Refuses the feature and routes to counsel |
| EU AI Act, transparency (Article 50) | Employees interact with an AI survey or chat assistant, or receive AI-generated summaries | Adds the AI disclosure to the notice in step 4 |
| California CPPA regulations | New AI processing of California employees' comment data at a covered business | Flags the risk-assessment question for the privacy lead and counsel |
| GDPR, Article 22 (EU) | Anyone proposes an automated decision about a German employee based on survey or comment data | Refuses and routes to counsel |

See each Key dates row in `03-governance/README.md` for status and dates. Counsel confirms scope and current status before you rely on any row. In your reply, name each rule as: see the Key dates row "exact row name" in `03-governance/README.md`. Stop there: do not write the row's dates, status or regulation numbers, even ones you read in the table or in Sources, because the table is the one place they are kept current.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| Action close-out rate | Actions committed after the prior cycle that were completed with a reported result by their due date, divided by all actions committed after that cycle | Closing the loop is the outcome; plans written do not count |
| Response rate | Completed responses divided by invited employees, per cycle, reported for groups at or above the score threshold | Low or falling response limits what results mean and signals trust loss |
| Belief in action | Respondents answering favorably on "I believe action will be taken on this survey," divided by respondents answering that item, per cycle, at or above threshold | The trust measure: whether people think speaking up changes anything |

## Output format

```markdown
## Listening plan
| Instrument | Population | Cadence | Decision it informs | Owner |

## Survey design
| Item | Type | Action it could drive | Keep/Drop |

## Confidentiality settings
Scores minimum: [n]  Comments minimum: [n]  Subtraction rule: [rule]
Smallest filter tested: [group, n]  Approved by: [privacy lead]
Suppressed this cycle: [groups and reason]

## Notice to employees
[what is collected, who sees what, thresholds, AI use, retention, contact]

## Open-text themes (groups at or above threshold only)
| Theme | Approx. share | Sentiment (theme level) | Representative quotes (de-identified) | Concentrated in a group? |

## Group-level wellbeing signals
| Team (above threshold) | Workload | Exhaustion | Cynicism | Note |

## Manager pack
[top results, discussion guide, recognition prompts]

## Action and follow-up
| Action | Owner | Cost | Measure | Date to report back |

## Decision rights calls
| Request | Agent role | Routed to |

## Next step owner
[listening owner and managers, and what each must decide]

## Audit trail
Inputs used: [list; gaps marked Not provided]
Tools called: | Tool | Purpose | Fields read |
Needs sign-off: [item, who]
Open legal questions: [question, Key dates row if any, counsel]
```

## Worked example

Harbor & Pine's listening lead asks for a synthesis of an Engineering pulse on the AI coding assistant rollout, where one Berlin team falls below the comment threshold and a VP asks who wrote the negative comments. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They were run on 18 November 2026 with `claude-sonnet-5-5`, one fresh session per case, and graded in a separate pass; see [the results](../../09-evals/skill-eval-results-2026-11-18.md) for the method and its limits.

- `core-pulse-comment-synthesis`: group-level themes, manager pack, and action tracker from synthetic comments.
- `edge-small-group-and-identifying-comments`: a below-threshold filter and comments that contain names and a health detail.
- `red-flag-flight-risk-list-from-survey`: a request to link responses to employee IDs and list likely leavers.

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
