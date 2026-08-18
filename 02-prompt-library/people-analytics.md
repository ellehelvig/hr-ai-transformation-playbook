# Prompt library: people analytics

Prompts for translating workforce data into decision-ready narrative for HR leaders, HRBPs, and managers. These prompts explain and synthesize, they do not score, rank, or decide. Anything that generates a risk score or model output belongs upstream of these prompts, see the [attrition risk model](../05-notebooks/attrition-risk-modeling.ipynb) for a worked example of a properly governed model these prompts can sit downstream of.

---

## 1. Attrition risk score explanation

**What it does:** Translates a model's attrition risk score and contributing factors into a plain-language narrative an HRBP or manager can act on, without disclosing model mechanics or making a retention decision.

```
You are explaining an attrition risk score to an HRBP who will use it to decide whether and how to intervene. You are not deciding whether to intervene, and the model's contributing factors are signals about patterns across the workforce, not proven facts about why this specific person might leave.

Employee context:
- Role: [TITLE, LEVEL]
- Tenure: [DURATION]
- Risk score: [SCORE / TIER, e.g., "High, 78th percentile"]
- Contributing factors from the model, feature importances or SHAP-style output: [LIST, e.g., "no promotion in 24 months (+), below-market pay percentile (+), high manager tenure with team (-)"]
- Manager's most recent qualitative note on this employee, if any: [PASTE, OR "none"]

Generate a briefing that:
1. States the risk tier and what percentile or threshold it represents
2. Translates each contributing factor into plain language, avoids restating model jargon
3. Distinguishes factors the organization can influence (pay, promotion timing, manager relationship) from factors it generally cannot (tenure, external market conditions)
4. Suggests 2-3 conversation starters for the manager or HRBP, framed as questions to ask, not conclusions to state
5. States the limits of this score explicitly: it is a probability based on patterns across the workforce, not a prediction about this individual, and should never be shared with the employee or referenced in a performance conversation

Do not:
- State the risk score as a certainty ("this employee will leave")
- Recommend a specific retention action (counteroffer, promotion) without human judgment on context
- Suggest sharing the score or its contributing factors directly with the employee
```

---

## 2. Engagement survey open-text synthesis

**What it does:** Synthesizes free-text engagement survey comments into themes for leadership reporting, with an equity check built in rather than added after the fact.

```
You are synthesizing open-text engagement survey comments into themes for leadership. Identify patterns, do not just summarize or repeat comments.

Survey context:
- Survey: [NAME, e.g., "Q3 Engagement Pulse"]
- Population: [TEAM / DEPARTMENT / ORG-WIDE]
- Response count: [N] out of [TOTAL] invited ([RESPONSE RATE]%)
- Question(s) the comments are responding to: [PASTE QUESTION TEXT]

Open-text responses:
[PASTE RESPONSES. KEEP ANONYMIZED, DO NOT INCLUDE NAMES]

Produce a synthesis with:
1. **Top themes** (4-5 max), each with a theme statement, approximate share of comments mentioning it, and 2-3 representative quotes, anonymized, lightly edited only to remove identifying detail
2. **Sentiment distribution** across the themes: predominantly positive, mixed, or predominantly negative
3. **Equity check**: if demographic or team breakdowns are available, note whether any theme is concentrated in a specific group rather than spread evenly, this often changes what the finding means
4. **What's actionable now** versus **what needs more data** before leadership acts on it
5. **Response rate caveat**: note if the response rate is too low to generalize, and to which population these themes can and cannot be extrapolated

Do not:
- Attribute a comment to an identifiable individual, even by inference
- Overstate confidence when the sample is small or skewed
- Editorialize sentiment as more positive or negative than the actual comments support
```

---

## 3. Exit interview theme synthesis

**What it does:** Synthesizes exit interview data across multiple departures into retention themes. Aggregate analysis, not a review of any one person's decision to leave.

```
You are synthesizing exit interview data across multiple departures to identify retention themes. This is aggregate analysis, not a review of any one person's decision to leave.

Cohort context:
- Time period: [DATES]
- Department or team: [SCOPE]
- Number of exit interviews included: [N]
- Total departures in this period: [N], note if not all departures were interviewed, and why

Exit interview data, structured and/or free text:
[PASTE EXIT INTERVIEW RESPONSES, REASONS FOR LEAVING, ANY STRUCTURED RATINGS]

Produce a synthesis with:
1. **Top reasons for leaving**, ranked by frequency, with the caveat that stated reasons and actual reasons often differ. Note where a stated reason (e.g., "better opportunity") likely masks an unstated one (e.g., manager relationship) based on patterns in the comments
2. **Comparison to the prior period**: are themes shifting, stable, or new
3. **Concentration check**: are departures and their reasons concentrated in a specific team, manager, or level? This is often more useful than the org-wide theme
4. **Regrettable versus non-regrettable framing**: if performance or fit data is available, note how themes differ between regrettable and non-regrettable departures, do not conflate them
5. **Recommended next steps**, split into what HR can act on centrally versus what needs to go to a specific manager or leader

Do not:
- Name individual departed employees in the synthesis
- Present a low-sample theme (fewer than 3-4 mentions) with the same confidence as a well-supported one
- Recommend a specific manager be investigated based solely on this synthesis, flag the concentration and route to the appropriate HRBP for follow-up
```

---

## 4. Workforce composition narrative for leadership reporting

**What it does:** Turns headcount and workforce composition data into a narrative leadership update.

```
You are drafting the workforce composition section of a leadership update. Turn the data below into a narrative a CHRO could present, not a data dump.

Reporting period: [QUARTER/MONTH]
Comparison period: [PRIOR QUARTER/MONTH, OR "same period last year"]

Data provided:
- Headcount by function/department: [PASTE OR TABLE]
- Hires and departures this period: [NUMBERS]
- Span of control / manager ratios: [DATA, IF AVAILABLE]
- Representation metrics, if your organization tracks and is legally permitted to report them: [DATA, OR "not included"]

Generate a narrative with:
1. **Headline**: the one sentence a leader would remember from this section
2. **What changed and why**, tying headcount movement to business context (planned growth, restructuring, seasonal pattern), not just the numbers
3. **Where to look closer**: any function or team with a notable outlier (rapid growth, high attrition, span of control outside typical range)
4. **Forward look**: what the current trajectory implies for the next period if nothing changes
5. Keep numbers precise but the narrative in plain language, a leader reading this on their phone should get the point in the first two sentences

Do not:
- Present representation data without confirming it is legally permissible to report in the relevant jurisdictions
- Round numbers in a way that changes the story
- Bury a significant outlier in a footnote
```

---

## 5. Manager span-of-control and org health flag explanation

**What it does:** Explains an org-design or span-of-control flag in plain language for an HR leader reviewing structural health, not a performance judgment on the flagged manager.

```
You are explaining an org health flag to an HR leader reviewing team structures. Your job is to make clear what the flag means and why it was raised, not to recommend a specific org change.

Flag context:
- Team or manager flagged: [MANAGER TITLE, TEAM NAME]
- Flag type: [Span of control outside range / Layer depth outside range / High manager-to-IC ratio in a specialized function / Other: SPECIFY]
- Threshold that triggered the flag: [e.g., "span of 14, threshold is 8-10 for this function"]
- Context that might explain it: [e.g., "recent reorg", "team includes several senior ICs who need less oversight", or "not yet known"]

Generate an explanation that:
1. States what the flag means in plain terms, and why the threshold exists (what typically goes wrong at this span or depth)
2. Lists plausible explanations, both benign (a genuinely capable team needing less oversight) and concerning (a manager stretched too thin, a layer that should not exist)
3. Suggests what additional information would distinguish benign from concerning before anyone acts on this
4. Frames this as a prompt for a conversation with the manager and their leader, not a verdict

Do not:
- Recommend a specific structural change (add a layer, split the team) without more context than a single flag provides
- Imply the flagged manager is underperforming, a span-of-control flag is a structural signal, not a performance judgment
```
