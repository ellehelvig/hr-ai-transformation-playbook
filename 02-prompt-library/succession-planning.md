# Prompt library: succession planning

Prompts for succession planning workflows, readiness narratives, slate calibration prep, critical role risk assessment, and development planning. Every prompt here supports the succession committee's judgment, none of them rank, score, or select a successor. That decision stays with the people who own it.

---

## 1. Successor readiness narrative

**What it does:** Turns structured readiness inputs, competency ratings, experience, and development history, into a readiness narrative for a succession review, without ranking candidates against each other.

```
You are drafting a successor readiness narrative for a succession planning review. You are synthesizing inputs the committee will discuss, not ranking or selecting a successor.

Candidate context:
- Current role: [TITLE, LEVEL, TENURE]
- Target role: [TITLE they are being considered for]
- Readiness horizon, as assessed by manager/HRBP: [Ready now / Ready in 1-2 years / Ready in 3+ years / Development needed]

Structured inputs:
- Competency ratings against target role requirements: [LIST: competency, current level, required level]
- Relevant experience: [LIST specific projects, roles, or exposure relevant to the target role]
- Development actions completed to date: [LIST]
- Most recent performance rating and trend: [RATING, TREND OVER LAST 2-3 CYCLES]
- Stated career interest in this path, from the employee if known: [YES / NO / UNCLEAR]

Generate a readiness narrative with:
1. **Readiness summary**: one paragraph stating the horizon and the primary basis for it
2. **Strengths for this target role**: evidence-based, tied to the competency ratings and experience above
3. **Gaps to close**: specific, tied to the competency ratings, not generic ("needs more experience")
4. **Recommended development actions** for the next 6-12 months, specific and assignable
5. **Flag if stated career interest is unknown**: a readiness assessment without confirmed interest is incomplete, note this explicitly

Do not:
- Compare this candidate to other candidates for the same role, that comparison happens in the committee discussion, not in this narrative
- State a readiness horizon more confident than the underlying evidence supports
- Assume career interest, if it is not confirmed, say so
```

---

## 2. Succession slate calibration prep

**What it does:** Prepares a briefing for a succession review meeting, the same discipline as the [performance calibration prep briefing](performance.md), applied to a succession slate.

```
Generate a succession review briefing doc for the following critical role.

Role context:
- Role: [TITLE]
- Incumbent: [NAME, TITLE], planned departure timeline if known: [TIMELINE, OR "no known departure, proactive planning"]
- Why this role is in scope for succession planning: [Business criticality / Incumbent retirement horizon / Flight risk / Regulatory requirement]

Candidate slate, structured input per candidate:
[LIST: name/role, readiness horizon, top strength, top gap, stated interest]

Generate a briefing with:
1. **Slate summary table**: one line per candidate (readiness horizon, strength, gap, interest)
2. **Slate health check**: is there at least one "ready now" candidate? Is the slate diverse in background and path, or does it concentrate risk in one team or pipeline? Is there any role with zero viable internal candidates, a single point of failure worth flagging to leadership regardless of what this review decides
3. **Discussion questions** the committee should work through for this slate, not yes/no questions, questions that surface disagreement
4. **Development investment priorities**: if the slate skews toward "ready in 3+ years" across the board, that is itself a finding worth surfacing
5. **What this review should NOT do**: finalize a successor decision in the room without the incumbent's timeline being confirmed, or treat this as a promotion decision rather than a planning exercise

Do not:
- Rank the candidates numerically, present the slate for discussion, not a leaderboard
- Recommend a specific successor, that is the committee's decision informed by this briefing
```

---

## 3. Critical role and single-point-of-failure risk assessment

**What it does:** Flags roles where departure risk and thin succession coverage create organizational exposure, to prioritize succession investment. Does not evaluate any individual's performance.

```
You are assessing organizational risk from critical roles with thin succession coverage. Your output prioritizes where to invest succession planning effort, it does not evaluate any individual's performance.

Roles under review:
[LIST: role title, incumbent tenure in role, business criticality (why this role matters), current succession depth (0 = no identified successor, 1 = one candidate identified, 2+ = multiple), incumbent flight risk signal if known]

For each role, assess:
1. **Risk level**: [High / Medium / Low], based on the combination of criticality, succession depth, and flight risk, not any single factor alone
2. **What "high risk" means specifically for this role**: what breaks or slows down if this person left with no notice
3. **Time to readiness gap**: if the identified successor(s) are not "ready now," how long is the exposure window
4. **Recommended action**: accelerate a specific successor's development, broaden the slate, or consider an external contingency option, only where warranted

Produce a summary ranking roles by risk level, with the highest-risk, thinnest-coverage roles first.

Do not:
- Treat succession depth of zero as a reflection on the incumbent, it is a planning gap, not a performance issue
- Speculate about why a role has no identified successor without input from the business leader who owns it
- Recommend an external hire as contingency without input from the hiring manager and TA on feasibility
```

---

## 4. Successor development plan

**What it does:** Generates a targeted development plan to close the specific gaps identified in a readiness assessment, for a named successor candidate.

```
Create a development plan to close the readiness gap for a succession candidate.

Candidate context:
- Current role: [TITLE, LEVEL]
- Target role: [TITLE]
- Readiness horizon: [FROM READINESS ASSESSMENT]
- Specific gaps identified: [LIST, FROM READINESS NARRATIVE OR COMMITTEE DISCUSSION]
- Candidate's stated development preferences: [Stretch assignment / Formal training / Mentoring / Lateral move / Mix]

Generate a development plan with:
1. For each gap: one specific development action (stretch project, exposure opportunity, formal program, mentor pairing), not a generic training recommendation
2. A realistic timeline tied to the readiness horizon, if the horizon is "1-2 years," the plan should show what closes in year 1 versus year 2
3. **Exposure opportunities**: specific ways to give this candidate visibility to the decision-makers involved in the eventual succession decision, without making the outcome look predetermined to peers
4. **Checkpoints**: when and how readiness will be reassessed, not just when the plan ends
5. **Manager's role**: what the current manager needs to actively enable, not block, for this plan to work

Do not:
- Promise the target role as an outcome, this is a development plan, not a commitment
- Recommend removing the candidate from their current responsibilities in a way that would be obvious to their team
```

---

## 5. Succession review talking points for leadership

**What it does:** Prepares talking points for an HR leader presenting succession slate status to executive leadership or the board.

```
Prepare executive talking points summarizing succession planning status for leadership or board review.

Scope: [Executive team / Function: SPECIFY / Org-wide critical roles]
Roles covered: [N] roles reviewed this cycle
Data provided:
- Roles with a "ready now" successor: [N of TOTAL]
- Roles with zero identified successor: [N of TOTAL]
- Roles where the incumbent's departure timeline is known and near-term, within 12 months: [N]
- Notable changes since the last review cycle: [LIST]

Generate talking points with:
1. **Headline status**: one sentence a board member would remember
2. **Where coverage is strong**: 1-2 specific examples, brief
3. **Where coverage is thin**: the roles with zero or weak succession depth, framed as investment priorities, not failures
4. **What's being done about the gaps**: tie back to development plans in motion, not just a list of problems
5. **One ask of leadership**, if there is one: budget for an external contingency search, executive sponsorship for a stretch assignment, a faster decision on a near-term departure

Tone: confident and specific. Boards and executives lose confidence in a succession program that sounds like a compliance exercise rather than active talent management.

Do not:
- Name specific successor candidates in a leadership-wide or board presentation unless your organization's governance explicitly allows naming individuals at that level
- Overstate readiness to make the numbers look better than the underlying assessments support
```
