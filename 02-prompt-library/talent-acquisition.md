# Prompt library: talent acquisition

Prompts for recruiting and hiring workflows — job posting drafts, screening support, interview prep, and offer communication. Every prompt here augments recruiter and hiring manager judgment; none is designed to make a hiring decision on its own.

**Before using any of these in a live hiring process:** route the use case through the [risk assessment template](../03-governance/risk-assessment-template.md). Hiring is one of the highest-scrutiny areas for AI use — several jurisdictions (NYC Local Law 144, Illinois AI Video Interview Act, EU AI Act Annex III) impose specific disclosure or audit requirements on AI used in employment decisions.

---

## 1. Inclusive job posting rewrite

**What it does:** Rewrites a job posting to remove biased or exclusionary language and improve candidate pool diversity without changing the actual requirements.

```
Rewrite this job posting to be more inclusive, while keeping every substantive requirement unchanged.

Current posting:
[PASTE JOB POSTING]

Rewrite so that:
1. Gendered or exclusionary language is replaced with neutral alternatives (e.g., "ninja," "rockstar," "he/she")
2. Requirements are separated into "must-have" and "nice-to-have" — research shows women and underrepresented candidates self-select out when everything reads as required
3. Years-of-experience requirements are only listed if genuinely necessary, not as a proxy for skill
4. The tone is direct and specific, not full of buzzwords ("fast-paced," "wear many hats," "work hard play hard")
5. Physical or schedule requirements are stated only if they are actual bona fide job requirements

Do not remove or soften any requirement that reflects a real business need. Flag anything you're unsure whether to keep.
```

---

## 2. Structured screening question generator

**What it does:** Generates consistent, job-related screening questions tied to the actual requirements of a role, to reduce interviewer variability and improve legal defensibility.

```
Generate a structured phone screen guide for the following role.

Role: [TITLE]
Level: [LEVEL]
Must-have requirements: [LIST]
Key responsibilities: [LIST 3-5]

Generate:
1. 5 screening questions directly tied to must-have requirements (no generic "tell me about yourself" filler)
2. For each question, what a strong answer sounds like and what a weak answer sounds like
3. 1 question to assess motivation/fit for this specific role (not generic culture fit)
4. 2 questions the recruiter should NOT ask (list common legally risky questions for this role type — e.g., asking about caregiving responsibilities, age-adjacent questions, salary history where prohibited by law)

Keep questions job-related and consistent across candidates — that consistency is what makes screening defensible.
```

---

## 3. Resume screening — evidence extraction (not scoring)

**What it does:** Extracts evidence of stated requirements from a resume for a recruiter to review. Deliberately does not produce a pass/fail score or ranking — that judgment stays with the recruiter.

```
Extract evidence from this resume relevant to the role requirements below. Do not score, rank, or recommend a decision.

Role requirements:
[LIST MUST-HAVE REQUIREMENTS]

Resume:
[PASTE RESUME TEXT]

For each requirement, output:
- Requirement
- Evidence found (direct quote or clear paraphrase from the resume)
- Evidence strength: Clear / Partial / Not found
- Note anything ambiguous that a recruiter should verify in screening

Do not infer protected characteristics (age, gender, disability, family status, etc.) from any resume content, even indirectly (e.g., graduation year as an age proxy). Do not penalize employment gaps without evidence they reflect a performance issue.
```

**Governance note:** This prompt is intentionally scoped to evidence extraction, not scoring. Any use case that ranks or scores candidates requires a fairness audit under the [risk assessment template](../03-governance/risk-assessment-template.md) and, for EU-based roles, classification under the [EU AI Act intake template](../03-governance/eu-ai-act-intake-template.md).

---

## 4. Interview panel debrief synthesis

**What it does:** Synthesizes multiple interviewers' independent notes into a structured summary for the hiring decision meeting, without collapsing dissenting views into false consensus.

```
Synthesize the following interview panel notes into a debrief summary. Preserve disagreement — do not average it away.

Candidate: [NAME/ID]
Role: [TITLE]

Interviewer notes:
[PASTE EACH INTERVIEWER'S NOTES, LABELED BY INTERVIEWER AND STAGE]

Produce:
1. Areas of clear agreement across interviewers (with which requirement each relates to)
2. Areas of disagreement — state both views and who held them, don't resolve the disagreement yourself
3. Any requirement no interviewer actually assessed (a coverage gap, not a candidate weakness)
4. Open questions the hiring team should discuss before deciding

Do not produce an overall recommendation or score. That is the hiring team's decision, made in the debrief meeting.
```

---

## 5. Candidate rejection message (individualized, not template-flat)

**What it does:** Drafts a rejection message that feels specific to the candidate rather than a form letter, without over-explaining or creating legal exposure.

```
Draft a candidate rejection message.

Candidate: [NAME]
Role applied for: [TITLE]
Stage reached: [e.g., phone screen / panel interview / final round]
One genuine, specific positive to include: [SOMETHING TRUE ABOUT THIS CANDIDATE'S BACKGROUND OR PERFORMANCE]

Requirements:
1. Warm but honest — do not imply they were closer to an offer than they were
2. Include the one specific positive naturally, not as generic praise
3. Do not give a specific reason for rejection beyond "we moved forward with a candidate whose experience more closely matched what we need for this role right now" — do not compare to other candidates or detail deficiencies
4. Invite them to apply for future roles only if genuinely true for this candidate
5. 4-5 sentences maximum

Never include specifics that could be read as discriminatory reasoning (age, health, family status, accent, name-based assumptions) even if unintentionally implied.
```

---

## 6. Offer stage — internal equity check prompt

**What it does:** Helps a recruiter or comp partner sanity-check a proposed offer against internal equity before it goes out, flagging discrepancies for human review rather than auto-adjusting anything.

```
Review this proposed offer for internal equity concerns. Flag issues only — do not recommend a specific number.

Proposed offer: [LEVEL, BASE, BONUS TARGET, EQUITY IF APPLICABLE]
Candidate background: [YEARS EXPERIENCE, RELEVANT SKILLS, CURRENT COMP IF KNOWN]
Comparable current employees at this level (anonymized): [PASTE RANGE OR TABLE — LEVEL, TENURE, CURRENT COMP]

Flag:
1. Whether the proposed offer falls outside the range of comparable current employees at the same level, and by how much
2. Whether the gap (if any) is explainable by a legitimate factor (specialized skill, market scarcity, location) or looks unexplained
3. Any pattern worth a second look (e.g., consistently lower offers for a particular candidate profile) — flag for human review, do not draw a conclusion about intent

This is a flagging tool for a human comp partner, not a compensation decision system. Never output a "corrected" offer amount.
```
