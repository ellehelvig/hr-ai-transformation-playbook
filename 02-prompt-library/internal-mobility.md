# Prompt library: internal mobility

Prompts for internal mobility workflows, internal job postings, candidate fit narratives, manager release conversations, and program outreach. Internal mobility carries the same fairness and transparency obligations as external hiring, and it carries an additional one external hiring doesn't: the current manager relationship. Every prompt here is built with that in mind.

---

## 1. Internal job posting optimization

**What it does:** Adapts job description optimization for an internal posting. Internal postings need different framing than external ones, readers already work here and need to know what applying actually means for their current role and manager relationship.

```
You are optimizing an internal job posting. Internal postings need different framing than external ones: readers already work here, and they need to know what applying actually means for their current role and manager relationship.

Current internal posting draft:
[PASTE DRAFT]

Role context:
- Level: [IC / Manager / Director]
- Function: [DEPT]
- Why this role is open: [Backfill / New role / Reorg]
- Minimum tenure in current role to be eligible to apply, per policy: [X months, OR "no minimum"]
- Manager notification requirement: [Must notify current manager before applying / Notification happens automatically at a certain stage / No notification required until offer stage]

Produce a revised posting that:
1. States the role and impact clearly, the same clarity bar as an external posting
2. States the internal mobility process explicitly: eligibility requirements, whether and when the current manager is notified, and typical timeline
3. Is honest about what "being considered" means, internal candidates are not guaranteed the role over external candidates unless your policy states otherwise, do not imply a guarantee that does not exist
4. Notes what happens to their current role or team if they are selected (notice period, transition expectations)
5. Ends with a clear next step and a contact for process questions, distinct from the hiring manager, so people can ask process questions without signaling interest to their current manager prematurely

Do not:
- Imply internal candidates get preferential treatment if your policy does not actually guarantee that
- Omit the manager notification process, uncertainty about this is the single biggest reason employees don't apply internally
```

---

## 2. Internal candidate fit narrative

**What it does:** Compares an internal candidate's skills and experience against an open role's requirements, for the hiring manager's consideration. Supports evaluation, does not make the selection decision.

```
You are preparing an internal candidate fit narrative for a hiring manager. This supports their evaluation, it does not make the selection decision.

Candidate context:
- Current role and tenure: [TITLE, DURATION]
- Skills and experience relevant to the target role: [LIST, IDEALLY FROM SKILLS PROFILE OR PERFORMANCE HISTORY, NOT ASSUMED]
- Recent performance history: [RATINGS/TREND OVER LAST 2-3 CYCLES]
- Stated reason for interest in this role: [PASTE, IF PROVIDED]

Target role requirements:
[PASTE ROLE REQUIREMENTS OR COMPETENCY FRAMEWORK]

Generate a fit narrative with:
1. **Alignment**: where the candidate's demonstrated skills and experience map directly to role requirements, with evidence
2. **Gaps**: where the candidate does not yet meet a requirement, stated factually, not softened
3. **Transferable strengths**: capabilities from their current role that are relevant even if not an exact match to the listed requirements
4. **Questions for the interview**: 2-3 questions that would help the hiring manager assess the gaps identified above
5. **What this narrative does not tell you**: this is based on available data, not a full interview evaluation, treat it as a starting point

Do not:
- Score or rank this candidate numerically against other candidates
- Recommend hiring or not hiring, that is the hiring manager's decision after their own evaluation
- Infer skills not evidenced in the source material just because the role requires them
```

---

## 3. Manager release conversation prep

**What it does:** Prepares an HRBP or hiring manager for the conversation with a current manager whose direct report is moving to a new internal role, a common friction point in internal mobility programs.

```
You are preparing an HRBP or hiring manager for a release conversation with a current manager whose direct report is moving to a new internal role. This conversation often has real emotional and operational weight for the current manager, prepare for that.

Context:
- Employee moving: [ROLE, TENURE ON CURRENT TEAM]
- New role: [TITLE, TEAM]
- Stage of process: [Offer extended, not yet accepted / Offer accepted, transition being planned]
- Current manager's likely concern: [Team coverage gap / Timing (mid-project) / Not previously informed of employee's interest / Other: SPECIFY, IF KNOWN]
- Company's internal mobility policy on notice period and transition timeline: [PASTE RELEVANT POLICY TERMS]

Generate a conversation prep guide with:
1. **How to open**: acknowledging the impact on the current manager and team, not just announcing the outcome
2. **What the current manager can and cannot influence at this stage**: be honest about what's already decided versus what's still negotiable (transition timeline, backfill support)
3. **Anticipated pushback** and how to respond to each, grounded in the policy terms provided, not improvised commitments
4. **What support the organization will provide** for the transition (backfill process, interim coverage, knowledge transfer plan)
5. **What NOT to promise**: commitments about backfill timing or team headcount that the HRBP or hiring manager cannot actually guarantee

Do not:
- Frame the departing employee's move as something the current manager should have prevented
- Promise a backfill timeline that has not actually been approved
- Suggest the current manager can reverse a decision that internal mobility policy states is the employee's to make once an offer is accepted
```

---

## 4. Internal mobility program outreach message

**What it does:** Drafts an outreach message inviting an eligible employee to consider an internal mobility opportunity, a rotation, stretch assignment, or open role. An invitation, not a summons.

```
Draft an outreach message inviting an employee to consider an internal mobility opportunity.

Employee context:
- Current role: [TITLE, TEAM]
- Why they're being invited: [SPECIFIC REASON, e.g., "skills profile matches the data analytics stretch program", "manager nominated them", "tenure milestone triggers eligibility"]

Opportunity context:
- Type: [Open role / Stretch assignment / Rotation program / Mentoring program]
- Name and brief description: [DETAILS]
- Time commitment: [e.g., "10% time for 3 months" or "full transition"]
- Application or expression-of-interest process: [BRIEF]
- Deadline, if any: [DATE]

The message should:
1. Open with the specific reason they're being invited, not a generic "we think you'd be a great fit"
2. Be clear this is an invitation to consider, not an expectation or a signal that their current role is at risk
3. State what happens next if they're interested, and that "not now" carries no penalty
4. Note whether their current manager will be informed, and when, per the mobility policy
5. Keep it to 5-6 sentences

Do not:
- Use language implying the employee must respond or is obligated to apply
- Suggest declining reflects poorly on them, opt-in participation only works if opting out is genuinely safe
- Promise a specific timeline or outcome the program cannot guarantee
```

---

## 5. Skills-based stretch assignment matching explanation

**What it does:** Explains why a stretch assignment or gig was suggested for an employee based on their skills profile, making the confidence level behind the match visible rather than treating it as a guarantee.

```
You are explaining a stretch assignment recommendation that was generated from a skills-matching system. Your job is to make the "why" transparent to the employee and their manager, not to guarantee the match is right.

Employee context:
- Current role: [TITLE]
- Skills profile highlights relevant to this match: [LIST TOP MATCHING SKILLS, WITH CONFIDENCE LEVEL IF AVAILABLE, e.g., "Data visualization (confirmed via 2 completed projects, high confidence)"]

Assignment context:
- Assignment: [NAME, BRIEF DESCRIPTION]
- Skills the assignment requires: [LIST]
- Match score or ranking, if provided: [SCORE, OR "not scored, qualitative match"]

Generate an explanation that:
1. States which of the employee's skills drove this match, and the confidence level behind each, a skill inferred from one self-assessment is weaker evidence than one confirmed across multiple sources
2. Notes any gap between the employee's current skill level and what the assignment ideally wants, framed as a growth opportunity, not a disqualifier
3. Explains this is a suggested match, not an assignment, the employee and their manager still decide
4. Flags if the match relied heavily on low-confidence signals, and recommends a manager conversation to validate before proceeding

Do not:
- Present the match score as a guarantee of success in the assignment
- Hide or omit the confidence level, an employee acting on a low-confidence match should know that
```

---

## Cross-links

- [Talent operating system architecture](../07-agentic-patterns/talent-operating-system-architecture.md): the skills ontology and confidence-scoring system prompt 5 above assumes as its data source.
- [Skills gap analysis notebook](../05-notebooks/skills-gap-analysis.md): where the underlying skill proficiency data in these prompts typically originates.
