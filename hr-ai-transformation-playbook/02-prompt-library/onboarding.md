# Prompt library: onboarding

Production-tested prompts for onboarding workflows. Copy, adapt, and iterate — the `[BRACKETED]` fields are variables you fill in from your HRIS or manually.

Each prompt includes: what it does, sample output, and tuning notes.

---

## 1. Personalized onboarding plan

**What it does:** Generates a role-specific 30/60/90-day onboarding plan for a new hire, including priority learning goals, key relationships to build, and early win opportunities.

```
You are an experienced HR Business Partner creating a structured onboarding plan.

New hire details:
- Name: [FIRST NAME]
- Role: [JOB TITLE]
- Team: [TEAM NAME]
- Manager: [MANAGER NAME]
- Start date: [START DATE]
- Location/work arrangement: [REMOTE / HYBRID / ONSITE — LOCATION]
- Prior relevant experience: [1-2 SENTENCE SUMMARY]

Create a 30/60/90-day onboarding plan. For each phase include:
1. Top 3 learning priorities (what they need to understand)
2. Top 3 relationship-building priorities (who they need to know and why)
3. One concrete early win goal (something achievable in the timeframe that builds credibility)
4. Key metrics or signals that define success for this phase

Format as a structured plan, not a bulleted list. Be specific to the role and team context provided.
```

**Tuning notes:**
- Add team-specific context (current projects, team structure) for significantly better output
- For senior hires (Director+), emphasize stakeholder mapping over task learning
- Pair with manager's own 30/60/90 expectations for alignment check

---

## 2. New hire welcome message (from manager)

**What it does:** Drafts a personalized first-day welcome message for a manager to send to their new hire.

```
Draft a warm, direct welcome message from a manager to a new team member joining on [START DATE].

Manager context:
- Manager name: [NAME]
- Team: [TEAM NAME], [BRIEF TEAM DESCRIPTION — e.g., "a 6-person engineering team working on developer tools"]
- One thing the manager is most excited to work on with this person: [SPECIFIC THING]

New hire context:
- Name: [FIRST NAME]
- Role: [JOB TITLE]
- One thing from their background the manager found compelling: [SPECIFIC THING]

The message should:
- Open with a genuine, specific welcome (not "Welcome aboard!")
- Reference one concrete thing the new hire will be working on in their first week
- Tell them who to contact if they have questions before their start date
- Be 3–4 short paragraphs maximum
- Sound like a human manager, not HR communications
```

**Tuning notes:**
- Managers should review and add their own voice before sending
- This is a Copilot prompt — the draft should be a starting point, not a final output

---

## 3. Manager onboarding checklist

**What it does:** Generates a manager-facing checklist for preparing to onboard a new direct report.

```
Generate a manager onboarding checklist for [MANAGER NAME], who is preparing to onboard [NEW HIRE NAME] as a [JOB TITLE] starting [START DATE].

The checklist should cover three phases:
1. Before day one (actions the manager should complete before the new hire starts)
2. Week one (daily touchpoints, introductions, and context-setting)
3. First 30 days (ongoing check-ins, goal-setting, and early feedback)

For each item, include: the action, timing, and why it matters for new hire success.

Format as a checklist using task checkboxes (- [ ]).

Team context: [BRIEF TEAM AND ROLE CONTEXT]
```

**Sample output (truncated):**

```markdown
## Before day one

- [ ] Send a welcome message at least 3 days before start date — gives the new hire time to prepare questions
- [ ] Block 90 minutes on day one for an uninterrupted welcome conversation
- [ ] Send a team intro email so colleagues know who's joining and why the role matters
- [ ] Confirm equipment and access are provisioned (check with IT 5 days out)
- [ ] Identify a peer buddy and brief them on the new hire's background
...
```

---

## 4. Onboarding feedback synthesis

**What it does:** Synthesizes free-text responses from a 30-day new hire survey into a structured summary for the HR team.

```
You are an HR analyst synthesizing new hire onboarding survey responses.

Below are free-text responses from [N] employees who completed their 30-day onboarding survey. Survey question: "[SURVEY QUESTION TEXT]"

[PASTE SURVEY RESPONSES — one per line]

Synthesize these responses into:
1. Top 3 themes (what most people mentioned positively)
2. Top 3 concerns or gaps (what most people flagged as missing or difficult)
3. Outlier observations (notable responses that don't fit the main themes)
4. One recommended action for the People Team based on this data

Keep the synthesis factual and grounded in the responses provided. Do not invent themes not present in the data. Quote specific phrases (without attribution) to support each theme.
```

**Tuning notes:**
- Run this per cohort or per team for more actionable insights
- Minimum useful sample size: 5 responses. Below that, summarize manually.
- Always have a human review before sharing upward — AI can misread sarcasm or cultural context

---

## 5. Buddy program matching rationale

**What it does:** Given two employee profiles, drafts a personalized explanation of why they were matched as onboarding buddies.

```
Write a short, warm message explaining why [NEW HIRE NAME] and [BUDDY NAME] have been matched as onboarding buddies.

New hire: [ROLE], [1-2 SENTENCES ON BACKGROUND/INTERESTS]
Buddy: [ROLE], [1-2 SENTENCES ON BACKGROUND/INTERESTS]

Shared connections: [LIST ANY — overlapping experience, interests, location, team adjacency]

The message should:
- Be addressed to both people
- Explain 2–3 specific reasons this match makes sense
- Suggest one concrete topic for their first conversation
- Be 2 short paragraphs

Tone: friendly and collegial, not corporate.
```
