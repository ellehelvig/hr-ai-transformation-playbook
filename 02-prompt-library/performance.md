# Prompt library: performance management

Prompts for performance review cycles, calibration, goal-setting, and feedback. All prompts are designed with a human-in-the-loop — AI assists the manager or HR professional, it does not make rating decisions.

---

## 1. Performance review draft (manager → direct report)

**What it does:** Helps managers draft a structured, evidence-based performance review narrative.

```
You are helping a manager write a performance review for one of their direct reports.

Employee: [NAME], [JOB TITLE], [TENURE IN ROLE]
Review period: [DATE RANGE]
Proposed rating: [RATING] (on a scale of: Exceeds / Meets / Developing / Underperforming)

Manager's notes on performance (bullet points fine — these are raw inputs):
[PASTE MANAGER'S NOTES]

Key accomplishments to highlight:
[LIST 2-4]

Areas for development:
[LIST 1-2]

Draft a performance review narrative that:
1. Opens with a 2-sentence summary of the employee's overall contribution this period
2. Covers accomplishments with specific, observable evidence (not vague praise)
3. Acknowledges 1–2 development areas constructively — focused on future growth, not criticism
4. Closes with a forward-looking statement about the next review period

Length: 300–400 words. Use clear paragraphs, not bullets.
Tone: Professional, direct, and growth-oriented. Avoid generic phrases like "goes above and beyond" or "valued team member."
```

**Tuning notes:**
- The quality of output is directly proportional to the quality of manager notes
- Coach managers to provide specific examples, not adjectives
- Flag reviews where the draft sounds inconsistent with the proposed rating — this often signals the manager hasn't gathered enough evidence

---

## 2. Self-assessment prompt (employee-facing)

**What it does:** Helps employees structure a strong self-assessment. Can be shared directly with employees as a prompt to use themselves.

```
Help me write a strong self-assessment for my performance review.

My role: [JOB TITLE]
Review period: [DATE RANGE]
Key projects and accomplishments (bullet points):
[LIST YOUR WORK]

What I want to communicate about my impact:
[1-2 SENTENCES]

Areas I'm actively developing:
[1-2 AREAS]

Write a self-assessment that:
1. Opens with my most significant contribution this period and its business impact
2. Covers 3-4 accomplishments with specifics — metrics, outcomes, or scope where possible
3. Is honest about development areas without underselling my progress
4. Closes with what I want to focus on in the next period

Length: 250–350 words. Write in first person. Avoid filler phrases.
My tone preference: [DIRECT AND CONFIDENT / COLLABORATIVE AND REFLECTIVE / OTHER]
```

---

## 3. Calibration prep briefing

**What it does:** Generates a pre-calibration briefing doc for a manager to review before entering a calibration session.

```
Generate a calibration prep briefing for a manager preparing to calibrate their team's performance ratings.

Manager: [NAME]
Team size: [N people]
Calibration session: [DATE], [DURATION]

Team ratings summary (provide as a list):
[EMPLOYEE NAME — PROPOSED RATING — TENURE — KEY CONTEXT]
e.g.:
- Jordan M. — Exceeds — 2.5 years — Led migration project
- Sam K. — Meets — 8 months — New to role, strong ramp
- Alex R. — Developing — 1 year — Struggled with delivery in H2

Generate a briefing that includes:
1. A summary of the team's proposed rating distribution vs. expected curve
2. The 2–3 employees where calibration pushback is most likely, and suggested talking points
3. Employees at risk of rating inflation or deflation — flag with reasoning
4. One data point or example the manager should have ready for each employee
5. A 2-sentence opening statement the manager could use to anchor their team's performance story

Format clearly. This will be read in the 20 minutes before the session.
```

---

## 4. Goal quality scoring and rewrite

**What it does:** Reviews an employee's goals and rewrites vague ones to be specific, measurable, and time-bound.

```
Review the following employee goals and score each one on clarity, measurability, and achievability (1–5 each). Then rewrite any goal scoring below 4 on measurability into a stronger version using SMART criteria.

Employee role: [JOB TITLE]
Review period: [DATE RANGE]

Goals:
1. [GOAL TEXT]
2. [GOAL TEXT]
3. [GOAL TEXT]

For each goal provide:
- Scores: Clarity [X/5], Measurability [X/5], Achievability [X/5]
- One-line diagnosis of the weakness (if any)
- Rewritten version (if measurability < 4)

Keep rewrites ambitious but achievable. Don't change the intent of the goal — only sharpen how it's expressed.
```

---

## 5. PIP documentation framework

**What it does:** Helps HR and managers draft a structured PIP with clear expectations, timeline, and support commitments. Use only after legal and HR review.

> ⚠️ Always involve your Employment Counsel and HRBP before initiating a PIP. This prompt generates a draft framework only — it is not legal advice and does not replace HR review.

```
Draft a Performance Improvement Plan framework for the following situation.

Employee: [ROLE, TENURE — do not include name in this draft]
Manager: [TITLE]
HRBP: [TITLE]
PIP duration: [30 / 60 / 90 days]
Primary performance concern: [1-2 SENTENCES — be specific and behavioral, not characterological]

Specific performance gaps (with examples):
[LIST 2-4 OBSERVABLE GAPS WITH DATES/EXAMPLES WHERE POSSIBLE]

Prior feedback given (dates and method):
[LIST]

Draft a PIP framework that includes:
1. Clear statement of performance expectations (what "success" looks like at PIP end)
2. Specific, measurable milestones at the midpoint and end of the PIP period
3. Support commitments from the manager and HR (check-ins, coaching, resources)
4. Consequences section — what happens if expectations are or are not met
5. Employee acknowledgment section

Tone: Constructive and factual. Avoid punitive language. Focus on behavior and outcomes, not personality.
```
