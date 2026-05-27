# Prompt library: performance management

Prompts for performance management workflows — review drafts, calibration prep, goal-setting feedback, PIP documentation, and mid-cycle synthesis. All prompts assume a human manager retains decision authority on ratings, advancement, and disciplinary action.

---

## 1. Performance review draft

**What it does:** Generates a first-draft performance review based on structured manager input and recent work artifacts. The manager edits, validates, and owns the final version.

```
You are drafting a performance review for a manager to edit and finalize. You are not making the rating decision — the manager is.

Employee context:
- Role: [TITLE, LEVEL]
- Tenure in role: [DURATION]
- Review period: [DATES]
- Proposed rating (manager's call): [RATING]

Inputs from the manager:
- Top 3 accomplishments this cycle: [LIST]
- Top 2 development areas: [LIST]
- Specific examples or artifacts: [PASTE OR REFERENCE]
- Stakeholder feedback received: [SUMMARY]

Goals set at start of cycle:
[PASTE GOALS AND OUTCOMES]

Write a review draft with the following sections:

1. **Overall summary** (3-4 sentences capturing the cycle, anchored to the proposed rating)
2. **What went well** — 3 paragraphs, each tied to a specific accomplishment with evidence
3. **Development areas** — 2 paragraphs, framed as growth opportunities, with one concrete next-cycle action each
4. **Goal performance** — explicit rating per goal: Exceeded / Met / Partially met / Did not meet, with one-sentence justification
5. **Looking ahead** — 2–3 sentences on what success looks like next cycle

Tone: specific, evidence-based, direct but respectful. Avoid:
- Vague praise ("great team player", "passionate")
- Hedge phrases ("could perhaps consider", "may want to think about")
- The words "rockstar", "ninja", "journey", "passionate", "synergy"
- Generic statements that could apply to any employee at any company
```

---

## 2. Calibration prep briefing doc

**What it does:** Generates a pre-calibration briefing for a people manager, 48 hours before their calibration session. Synthesizes team performance distribution, flight-risk flags, comp positioning, and prior-cycle context into a single document.

```
Generate a calibration prep briefing doc for the following manager.

Manager context:
- Manager: [TITLE]
- Team size: [N direct reports]
- Calibration date: [DATE]

Team data (provided as structured input):
- Proposed ratings by employee: [LIST: name, role, tenure, proposed rating, prior cycle rating]
- Flight risk signals from People Analytics (if available): [LIST or "none"]
- Compensation positioning vs. range midpoint: [LIST or "not provided"]
- Notable inflection points this cycle (promotions, role changes, PIPs): [LIST]

Generate a briefing doc with:

1. **Rating distribution summary**
   - Proposed distribution vs. prior cycle
   - Distribution vs. company guideline (if provided)
   - Flag any pattern that would warrant calibration discussion (rating compression, no top ratings, no bottom ratings)

2. **Per-employee snapshot** (one line each)
   - Name | Role | Tenure | Prior rating | Proposed rating | Key context

3. **Discussion preparation**
   - 2–3 questions the calibration committee is likely to ask this manager
   - 2–3 areas where this manager's ratings may receive pushback, and the evidence to support them

4. **Flight risk / retention concerns**
   - Anyone proposed for a low rating who is also a flight risk
   - Anyone proposed for a top rating who is underpaid vs. range

5. **Things to NOT bring up in calibration**
   - Anything not directly supporting the rating decision (personal life context, manager opinions on workstyle without evidence, comparison to other teams)

The manager has 15 minutes to read this before walking into calibration. Be ruthless about what makes the cut.
```

---

## 3. Goal-setting feedback

**What it does:** Reviews a manager's draft goals for a direct report and identifies quality issues before the goals are finalized.

```
Review the following goals drafted by a manager for an employee. Provide structured feedback on quality.

Employee context:
- Role: [TITLE, LEVEL]
- Tenure: [DURATION]
- Team's top priority this quarter: [PRIORITY]

Draft goals:
[PASTE 3–5 GOALS AS WRITTEN BY THE MANAGER]

For each goal, evaluate it against these criteria:

1. **Specific** — Is it clear what "done" looks like? Could two people read this and agree on what success means?
2. **Measurable** — Is there a metric or observable outcome? Not "improve" but "improve X from Y to Z."
3. **Owned by the employee** — Can the employee actually drive the outcome, or is it dependent on factors outside their control?
4. **Connected to team priority** — Does this goal advance the team's top priority? If not, why is it a goal?
5. **Stretch-but-realistic** — Will the employee learn or grow by hitting this? Is it achievable in the timeframe?

For each goal, return:
- The goal as written
- Score on each criterion (Pass / Fail / Marginal)
- Suggested rewrite if any criterion is Fail or Marginal
- One question the manager should ask the employee before finalizing

End with:
- **Overall assessment** — Are these goals collectively strong enough to drive the next review cycle?
- **What's missing** — Is there a goal that should exist for this role but doesn't?

Be direct. Soft feedback on weak goals produces weak goals.
```

---

## 4. PIP documentation draft

**What it does:** Generates a first-draft Performance Improvement Plan based on manager and HRBP input. The HRBP and Legal review and finalize before any conversation with the employee.

```
WARNING: This is a draft for HRBP and Legal review. Do not share with the employee until reviewed.

You are drafting a Performance Improvement Plan. Be precise. Vague language creates legal exposure and confuses the employee.

Inputs:
- Employee role: [TITLE, LEVEL]
- Tenure: [DURATION]
- Prior performance ratings: [LIST]
- Specific performance concerns (observed, with examples): [LIST CONCERNS AND EVIDENCE]
- Prior feedback given (verbal coaching, written feedback, prior PIP): [DOCUMENT WHAT AND WHEN]
- PIP duration: [TYPICALLY 30, 60, OR 90 DAYS]
- Manager: [TITLE]
- HRBP: [NAME]

Generate a PIP document with:

1. **Purpose statement** — Plain language: why this PIP is being issued. State the gap between current performance and role expectations.

2. **Performance concerns** — For each concern:
   - The expected standard (cite job description or competency framework)
   - The observed performance (specific examples with dates)
   - The gap between the two
   - Avoid generalizations. Every statement should be defensible in writing.

3. **Improvement expectations** — Specific, observable, measurable improvements required. Tied to each concern listed above. Include the standard ("at the level of others in this role") not just direction ("improve").

4. **Support provided** — What the manager, HRBP, and organization will do to support improvement (coaching cadence, training, mentoring, removal of blockers).

5. **Check-in schedule** — Specific dates for each check-in over the PIP period, what will be reviewed, and what the employee should prepare.

6. **Consequences** — Clear, factual statement of what happens if improvement targets are not met by the end of the PIP period.

7. **Employee acknowledgment section** — Space for employee signature and date, with language clarifying that signature acknowledges receipt, not agreement.

Tone: direct, factual, professional. Never:
- Use the word "attitude" without specific behavioral examples
- Cite "team dynamics" without naming the specific behavior
- Reference protected characteristics or anything that could imply discrimination
- Use language that suggests the outcome is predetermined

Flag for HRBP review:
- Any statement that lacks specific evidence
- Any expectation that isn't clearly measurable
- Any language that could be read as targeting the person rather than the performance
```

---

## 5. Mid-year feedback synthesis

**What it does:** Synthesizes 360-degree feedback collected mid-cycle into a structured summary the employee and manager can use in their mid-year conversation.

```
You are synthesizing 360 feedback for an employee's mid-year review conversation. Your goal is to surface patterns, not to repeat every comment.

Employee context:
- Role: [TITLE, LEVEL]
- Tenure: [DURATION]
- Feedback collection period: [DATES]

Feedback received:
- Manager feedback: [PASTE]
- Peer feedback (N=[X]): [PASTE]
- Direct report feedback if applicable (N=[X]): [PASTE]
- Stakeholder feedback (N=[X]): [PASTE]
- Self-assessment: [PASTE]

Produce a synthesis with:

1. **Themes — strengths** (3 max)
   - Each theme stated in one sentence
   - Evidence: 2–3 specific examples or quotes (anonymized)
   - Source spread: which feedback sources mentioned this strength

2. **Themes — development areas** (2-3 max)
   - Each theme stated in one sentence
   - Evidence: 2–3 specific examples or quotes (anonymized)
   - Source spread: which feedback sources raised this
   - Self-awareness check: did the employee identify this in their self-assessment?

3. **Notable disagreements** — where different sources see the employee differently. These often matter more than the agreement.

4. **What's missing** — patterns that would be useful but the data doesn't support, or sources that didn't respond.

5. **Recommended discussion topics for the mid-year conversation** (3–5 questions, prioritized)

Do not:
- Attribute specific comments to specific people, even when easy to infer
- Soften patterns to make them more palatable
- Recommend a rating — this is feedback synthesis, not calibration prep
```
