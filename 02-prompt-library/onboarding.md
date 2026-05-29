# Prompt library: onboarding

Prompts for onboarding workflows, new hire Q&A, personalized onboarding plans, manager preparation, and check-in synthesis. Designed to support HR Operations and HR Business Partners, not replace human relationship-building with new hires.

---

## 1. New hire policy Q&A response

**What it does:** Generates an accurate, warm, citation-backed response to a common new hire policy question. Use as a Copilot-style assist when drafting HR helpdesk replies, or as the response generator inside an RAG-based agent.

```
You are an HR helpdesk specialist responding to a new hire question. Your goal is to give a clear, accurate answer the employee can act on, not to recite the entire policy.

Company context:
- Company: [COMPANY NAME]
- Employee's location: [COUNTRY / STATE]
- Employee start date: [DATE]
- Time since start date: [X days]

Policy source material:
[PASTE THE RELEVANT POLICY SECTION. DO NOT INVENT POLICY DETAILS]

Employee question:
[PASTE QUESTION]

Generate a response that:
1. Answers the question in the first sentence
2. Cites the policy section name and version, so the employee can verify
3. Flags any next steps the employee needs to take, with deadlines if relevant
4. Routes to a human contact (HRBP, HR Ops) if the question involves individual circumstances or jurisdiction-specific rules
5. Keeps tone warm but direct, new hires are nervous, not stupid

Do not:
- Invent policy details not in the source material above
- Use the words "kindly", "please feel free", "as per", "I hope this helps"
- Recite the full policy when a 2-sentence answer will do
```

---

## 2. Personalized onboarding plan

**What it does:** Generates a 30/60/90 day onboarding plan tailored to a specific role, team, and start context. Used by managers or HRBPs to prepare for a new hire's first 90 days.

```
Create a personalized 30/60/90 day onboarding plan for the following new hire.

New hire context:
- Role: [JOB TITLE, LEVEL]
- Team: [TEAM NAME, SIZE]
- Manager: [TITLE]
- Office / remote / hybrid: [ARRANGEMENT]
- Prior experience level: [Early career / Mid-career / Senior]
- Joining context: [Backfill / Net new headcount / Cross-functional move]

Team context:
- Top 3 team priorities this quarter: [LIST]
- Key stakeholders new hire should meet in first 30 days: [LIST 3-5]
- Tools / systems new hire needs access to on Day 1: [LIST]

Generate a 30/60/90 day plan with:

Days 1–30 (Foundation):
- 3 specific learning objectives
- 5 named stakeholder intro meetings
- 1 small early win they can ship by Day 30
- Manager 1:1 cadence and topics

Days 31–60 (Contribution):
- 3 deliverables they should own end-to-end
- Cross-functional projects to shadow or contribute to
- 30-day check-in topics

Days 61–90 (Ownership):
- 2 outcomes they should be driving independently
- Stakeholder feedback to gather and synthesize
- 90-day review prep

Keep it specific to the role and team, generic onboarding plans get ignored.
```

---

## 3. Manager onboarding prep guide

**What it does:** Prepares a manager for a new hire's first week. Generated 5 days before the start date so the manager has time to act on it.

```
You are preparing a manager for a new hire who starts in 5 days. Generate a one-page prep guide.

New hire context:
- Name: [NAME]
- Role: [TITLE]
- Start date: [DATE]
- Prior role / company: [BACKGROUND]
- Reason they were hired (paraphrased from hiring summary): [WHY]

Manager context:
- Manager's tenure with team: [DURATION]
- Last new hire onboarded by this manager: [DATE, OR "First direct hire"]

Generate a prep guide with:

1. **Day 1 plan (hour by hour for first half-day):** Welcome message, 1:1, lunch plan, account setup time, intros
2. **First week 1:1 topics:** 4–5 specific questions to ask, not generic "how's it going"
3. **What to set up before Day 1:** Calendar invites, Slack intros, doc access, first project brief
4. **What NOT to do in the first 2 weeks:** Common manager mistakes (overloading, vague feedback, skipping 1:1s, not introducing them to skip-level)
5. **30-day success criteria:** What "going well" looks like at the 30-day mark

Keep it practical. The manager has 15 minutes to read this, make every line earn its place.
```

---

## 4. 30/60/90 day check-in synthesis

**What it does:** Synthesizes free-text new hire check-in responses into actionable insights for HRBPs and managers. Useful for spotting onboarding issues before they become attrition.

```
You are analyzing new hire check-in survey responses. Identify themes and risks, do not just summarize.

Survey questions and responses:
[PASTE THE 30/60/90 SURVEY RESPONSES. FREE TEXT FIELDS]

New hire context:
- Cohort: [START MONTH]
- Cohort size: [N new hires]
- Department or function: [DEPT]

Produce a synthesis with:

1. **Top 3 themes** that appear across multiple responses (not just one person's complaint)
2. **Risk signals** for individual new hires, flag anyone whose responses suggest disengagement, confusion, or early attrition risk. Quote the specific language that triggered the flag.
3. **What's working**: themes worth reinforcing or replicating
4. **Recommended actions** for HRBP and manager follow-up, broken out by:
   - Things the HRBP should address centrally (process gaps, missing resources)
   - Things individual managers should address with their direct report
5. **What's missing from the data**: questions that should have been asked but weren't

Be direct about risks. Soft framing of attrition signals helps no one.
```

---

## 5. Buddy program introduction message

**What it does:** Generates a personalized intro message from a buddy to a new hire, before their start date.

```
Write a short, warm intro message from a peer buddy to a new hire who hasn't started yet.

Buddy context:
- Buddy's role: [TITLE]
- Buddy's tenure: [DURATION]
- Why this buddy was matched: [SIMILAR ROLE / SAME TEAM / SIMILAR BACKGROUND]

New hire context:
- Name: [NAME]
- Role they're starting: [TITLE]
- Start date: [DATE]

The message should:
- Be 4–6 sentences, conversational, sent via email or Slack
- Introduce the buddy and their role
- Offer one specific thing the buddy will help with in the first week (not generic "let me know if you have questions")
- Suggest a coffee chat in the first week with a proposed time window
- End with a single concrete next step

Do not:
- Use corporate onboarding language ("excited to support your journey")
- Promise to be available "24/7"
- Write more than 6 sentences
```
