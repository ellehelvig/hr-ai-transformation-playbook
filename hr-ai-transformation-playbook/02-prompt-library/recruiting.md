# Prompt library: recruiting and talent acquisition

Production-ready prompts for recruiting workflows. All prompts involving candidate evaluation are designed as Copilot tools — AI informs the recruiter's judgment, it does not make screening or selection decisions.

---

## 1. Job description review and optimization

**What it does:** Reviews a job description for clarity, bias risk, and keyword effectiveness, then rewrites it.

```
Review this job description and provide:
1. Bias risk flags — language that may discourage qualified candidates (gendered language, credential inflation, culture-fit vagueness, unnecessary requirements)
2. Clarity score (1–5) with specific issues
3. Missing information candidates need to decide whether to apply
4. A rewritten version that addresses your findings

Job description:
[PASTE JD]

Company context: [INDUSTRY, SIZE, STAGE]
Audience: [WHO YOU'RE TRYING TO REACH]
Must-keep requirements: [LIST ANY NON-NEGOTIABLES]
```

---

## 2. Interview question bank by competency

**What it does:** Generates a structured interview question bank mapped to defined competencies.

```
Generate a structured interview question bank for a [JOB TITLE] role.

Competencies to assess:
1. [COMPETENCY 1 — e.g., Technical problem solving]
2. [COMPETENCY 2 — e.g., Cross-functional collaboration]
3. [COMPETENCY 3 — e.g., Navigating ambiguity]

For each competency, provide:
- 2 behavioral questions (past behavior: "Tell me about a time...")
- 1 situational question (hypothetical: "Imagine you...")
- What a strong answer demonstrates (2-3 bullet points)
- One follow-up probe

Format as a ready-to-use interview guide. Questions should be open-ended and avoid leading the candidate.
```

---

## 3. Candidate debrief synthesis

**What it does:** Synthesizes free-text interview feedback from multiple interviewers into a structured summary for the hiring team.

```
Synthesize interview feedback from [N] interviewers for a [JOB TITLE] candidate.

Interview feedback (one per interviewer — summarize each in your own words before pasting):
Interviewer 1 ([ROLE]): [FEEDBACK]
Interviewer 2 ([ROLE]): [FEEDBACK]
Interviewer 3 ([ROLE]): [FEEDBACK]

Generate a debrief summary that includes:
1. Consensus strengths (mentioned by 2+ interviewers)
2. Consensus concerns (mentioned by 2+ interviewers)
3. Split opinions (where interviewers significantly disagreed)
4. Open questions that were not resolved by the interview process
5. Recommended next step: [Hire / No hire / Additional interview] — flag if interviewers are split

Do not fabricate impressions not present in the feedback. Flag gaps where evidence is thin.
```

**Tuning notes:** The recruiter must review this summary before the debrief meeting — AI can miss tone, context, and interpersonal dynamics that a human picks up immediately.

---

## 4. Offer letter draft

**What it does:** Drafts a customized offer letter from structured inputs.

> ⚠️ Always have Legal and HR review offer letters before sending. Compensation, title, and equity details must be verified against HR systems.

```
Draft an offer letter for the following new hire.

Company: [NAME]
Candidate: [FIRST NAME] (use first name only in draft — personalize before sending)
Role: [JOB TITLE]
Department: [DEPARTMENT]
Manager: [MANAGER NAME, TITLE]
Start date: [DATE]
Work arrangement: [REMOTE / HYBRID / ONSITE — LOCATION]
Compensation: [BASE SALARY] annually, paid [FREQUENCY]
Bonus: [DESCRIPTION OR "N/A"]
Equity: [DESCRIPTION OR "N/A"]
Benefits: [SUMMARY OR "Standard benefits package per our benefits guide"]
Offer expiration: [DATE]

Draft a warm, professional offer letter that:
- Opens with genuine enthusiasm about this specific candidate (reference the role they're being hired for)
- Clearly states all compensation components
- References next steps (signing, background check, onboarding information)
- Is written in [FORMAL / CONVERSATIONAL] tone
- Is 3–4 paragraphs

[PASTE ANY COMPANY-SPECIFIC LANGUAGE REQUIRED]
```
