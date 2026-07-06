# Prompt library: talent acquisition

Prompts for recruiting and hiring workflows. Job descriptions, interview prep, candidate communications, sourcing outreach, and recruiter feedback coaching. Every prompt is designed to augment recruiters and hiring managers, not replace human judgment on disposition decisions.

---

## 1. Job description optimization

**What it does:** Rewrites a job description for clarity, inclusivity, and candidate appeal. Use before posting any role, especially for technical or senior positions where the JD often drifts into jargon.

```
You are an experienced talent acquisition partner reviewing a job description before it gets posted. Your goal is to make this JD clearer, more compelling, and more inclusive without losing accuracy.

Current job description:
[PASTE FULL JD]

Role context:
- Level: [IC / Manager / Director / VP / C-suite]
- Function: [Engineering / Product / Sales / etc.]
- Team size and reporting structure: [BRIEF]
- Why this role exists right now: [1-2 sentences]
- Top 3 things this person will accomplish in their first year: [LIST]

Produce a revised job description that:

1. Opens with what the person will do, not what the company is. The first paragraph should answer "why would I want this job?"
2. Reorganizes responsibilities into 4-6 outcomes, not a long list of tasks
3. Distinguishes requirements (non-negotiable) from preferences (nice to have). Be honest. Most "requirements" are actually preferences.
4. Removes language that screens out qualified candidates from underrepresented backgrounds (gendered terms, "rockstar," excessive years of experience requirements, degree requirements when not actually required)
5. Includes salary range or salary band if the original had one. Do not invent one.
6. Ends with a concrete next step.

Do not:
- Use the words "rockstar," "ninja," "guru," "passionate," "self-starter," "wear many hats," "fast-paced," "synergy," "world-class"
- Pad with company boilerplate that does not relate to the role
- Add years-of-experience requirements that were not in the original
- Promise things you cannot verify (unlimited PTO without policy backing, etc.)

Flag any sections that need verification with the hiring manager before posting.
```

---

## 2. Interview question bank for a competency

**What it does:** Generates a structured set of interview questions for evaluating a specific competency. Used by recruiters when prepping interview loops, or by hiring managers building structured interviews.

```
Generate an interview question bank for evaluating a single competency.

Competency: [NAME, e.g., "cross-functional collaboration"]
Role context: [TITLE, LEVEL]
Interview format: [Phone screen / Onsite panel / Final round]
Time available for this competency in the interview: [15-30-45 minutes]
What "strong" looks like for this competency at this level: [2-3 sentences from the competency framework]

Produce:

1. **Opening question** that gets the candidate sharing a real example without prompting (one question)
2. **Probe questions** to go deeper on the example (3-5 questions). Aim for STAR follow-ups: situation, task, action, result.
3. **Counter-example question** that tests whether the candidate has learned from failure
4. **Hypothetical** scenario tied to the actual role (one question, role-specific)
5. **What to listen for** as evidence of strong performance vs. weak performance (4-5 bullets each)
6. **Common candidate trap responses** that sound good but are actually red flags

Calibrate question difficulty to the role level. A senior role gets more complex hypotheticals; an early-career role gets more skills-focused probes.

Do not:
- Ask brainteasers or puzzle questions
- Include questions that test class background (favorite books, dinner party guests, etc.)
- Ask anything that could be interpreted as discriminatory
```

---

## 3. Candidate disposition communication (decline)

**What it does:** Drafts a warm, specific rejection message after a candidate has interviewed. Use after the recruiter and hiring manager have agreed on the decision. Never use to deliver a decision the candidate has not been told about through the appropriate channel.

```
Draft a candidate disposition message declining to move forward after interviews.

Candidate context:
- Stage they reached: [Phone screen / First round / Final round / Offer declined by company]
- Number of interviews completed: [N]
- Time invested: [Total hours including assessments]
- Strongest area in their candidacy: [1 specific thing]
- Reason for the decision (internal, not for sharing): [BRIEF]

Tone target: warm, specific, respectful. The candidate spent real time. Treat them like a person, not a transaction.

The message should:

1. Lead with the decision in the first sentence. Do not bury it.
2. Acknowledge what was genuinely strong in their candidacy. Be specific. "Your background in X stood out" not "we were impressed."
3. Be honest about why without being legally risky. Stay close to "we moved forward with someone whose background was a closer match for [specific requirement]."
4. Leave the door open if appropriate (future roles, reconnecting in 6-12 months). Only if true.
5. Close with one concrete next step or resource (LinkedIn connection, talent community, specific future role posting)

Keep it to 4-5 sentences. Long rejection messages read as guilty, not kind.

Do not:
- Use the words "unfortunately" (overused, signals bad news before they read it), "regret," "decision was difficult"
- Promise future consideration if you do not mean it
- Give performance feedback without the candidate asking (it creates legal risk and most candidates do not want it from a rejection)
- Use generic templates that any company could send
```

---

## 4. Recruiter coaching on interview feedback quality

**What it does:** Reviews an interviewer's written feedback after an interview and provides coaching on quality. Used by recruiters or HRBPs to improve interview feedback discipline.

```
Review the following interview feedback and provide structured coaching to the interviewer.

Interview context:
- Role: [TITLE, LEVEL]
- Interview type: [Phone screen / Technical / Behavioral / Final]
- Competency the interviewer was evaluating: [NAME]
- Candidate disposition recommendation by interviewer: [Advance / Reject / Strong yes / Lean yes / Lean no / Strong no]

Feedback as written by interviewer:
[PASTE FEEDBACK]

Evaluate the feedback against these criteria:

1. **Evidence-based.** Does the feedback cite specific examples from the interview, or is it impressionistic? "Strong communicator" is impressionistic. "Walked through trade-offs of three database choices and chose the right one for the scenario" is evidence.

2. **Tied to the competency.** Does the feedback actually evaluate what the interviewer was assigned to evaluate, or did they drift into general impressions?

3. **Distinguishes performance from preference.** Are there judgments embedded that are about cultural fit or interviewer preference rather than role requirements?

4. **Calibrated to the level.** Does the bar applied match the role level, or is the interviewer over-indexing on senior-level expectations for a mid-level role (or vice versa)?

5. **Bias check.** Are there phrases that could indicate affinity bias, halo effect, or stereotype-driven assessment? Quote them directly.

Produce coaching that includes:
- One specific strength of this feedback
- 2-3 specific areas to improve, with concrete rewrite suggestions
- A "would this hold up in a calibration discussion?" verdict
- One question to ask the interviewer to surface their underlying reasoning

Be direct. Soft coaching on interview quality produces weak interviewers and bad hires.
```

---

## 5. Sourcing outreach message

**What it does:** Drafts a personalized cold outreach message to a passive candidate. Use after a sourcer or recruiter has actually reviewed the candidate's profile. Never send to a list.

```
Draft a personalized outreach message to a passive candidate for a specific role.

Candidate context:
- Name: [NAME]
- Current role and company: [TITLE at COMPANY]
- Specific aspect of their background that makes them relevant: [BE SPECIFIC, e.g., "led X migration at Y company in 2024"]
- Mutual connections, if any: [LIST, or "none"]

Role context:
- Title: [TITLE]
- Why this candidate specifically (not just the role): [1-2 sentences]
- What is different about this role from their current one: [1-2 sentences]
- Compensation band, if you can share: [RANGE, or "competitive with current"]
- Location and arrangement: [REMOTE / hybrid in CITY / in-office in CITY]

The message should:

1. Open with the specific reason you reached out to them. Not "your impressive background." A real reason, named.
2. Connect that reason to what is interesting about the role for them specifically.
3. Be honest about the ask. You want a conversation, not a commitment.
4. Make it easy to say no. Decent passive candidates get many messages a week.
5. End with one concrete next step (15-minute intro call within the next 2 weeks).

Length: 4-6 sentences. Anything longer and they will not read it.

Do not:
- Open with "I came across your profile and was impressed"
- Use the words "rockstar," "passionate," "exciting opportunity," "world-class team," "disrupting"
- Promise specifics you cannot deliver (compensation numbers without authorization, role scope without manager confirmation)
- Send to a candidate the company has already declined within the past 12 months (always check ATS first)
- Use a template. If this message could have been sent to 50 other candidates, do not send it.
```
