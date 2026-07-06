# Prompt library: performance management

Prompts for performance conversations, documentation, and calibration. These are drafting and preparation aids for managers and HRBPs — the manager remains the author and decision-maker on every output. Nothing here should be sent to an employee without manager review and edit.

**Before deploying in a live performance cycle:** route the use case through the [risk assessment template](../03-governance/risk-assessment-template.md). Performance ratings and PIPs are consequential employment decisions — AI may inform documentation, never determine the rating or outcome.

---

## 1. Performance review draft from manager notes

**What it does:** Turns a manager's informal notes and examples into a structured, well-written performance review draft the manager then edits and owns.

```
Draft a performance review section from the following manager notes. Do not add examples or claims that aren't in the notes.

Employee: [ROLE, LEVEL, REVIEW PERIOD]
Rating category being written: [e.g., "Collaboration" / "Technical Execution" / "Ownership"]
Manager's raw notes and examples: [PASTE — bullet points, fragments, whatever the manager has]

Produce a review section that:
1. Opens with a clear, specific statement of performance in this category
2. Uses only the examples and evidence provided — do not invent specifics
3. Is behavioral and specific ("shipped X, which reduced Y") not vague ("great team player")
4. If the notes suggest a growth area, states it directly and constructively, not buried in praise
5. Matches a professional, direct tone — not effusive, not clinical

Flag any place where the notes are too thin to support a strong claim, so the manager knows to add detail rather than let the AI fill the gap.
```

---

## 2. Calibration prep — evidence organizer

**What it does:** Organizes a manager's supporting evidence for a proposed rating ahead of a calibration meeting, so the manager can defend the rating with specifics rather than generalities.

```
Organize this manager's evidence to support their proposed rating ahead of calibration.

Employee: [ROLE, LEVEL]
Proposed rating: [RATING]
Manager's supporting notes: [PASTE]
Rating rubric/definitions for this level: [PASTE OR SUMMARIZE]

Produce:
1. The 3 strongest pieces of evidence supporting the proposed rating, mapped to specific rubric criteria
2. Any rubric criteria the notes don't clearly address — flag as a gap the manager should be ready to speak to
3. One question a calibration peer is likely to push back with, and how the manager could respond using the evidence provided
4. A one-paragraph summary the manager can use to open their case in calibration

This is a preparation aid. The rating decision and its defense in calibration remain the manager's.
```

---

## 3. Performance improvement plan (PIP) documentation support

**What it does:** Helps a manager or HRBP structure PIP documentation clearly and fairly, with specific, verifiable performance gaps rather than vague characterizations.

```
Help draft PIP documentation from the following inputs. This will be reviewed by HR and Legal before use — flag anything that needs their input.

Employee: [ROLE, LEVEL, TENURE]
Performance gaps (manager's description): [PASTE SPECIFIC EXAMPLES WITH DATES WHERE POSSIBLE]
Prior feedback already given: [WHEN AND HOW — e.g., "verbal feedback in 1:1s on 3/2 and 4/10, written warning on 5/1"]
Expected improvement: [SPECIFIC, MEASURABLE STANDARD]
Timeline: [LENGTH OF PIP]
Support being offered: [COACHING, TRAINING, CHECK-IN CADENCE]

Structure the documentation with:
1. Specific, dated examples of the performance gap (not characterizations like "bad attitude" — behaviors and outcomes only)
2. Clear statement of the expected standard, measurable and specific
3. Timeline and check-in schedule
4. Support and resources being provided
5. Clear statement of consequence if improvement standard is not met

Flag explicitly: any place where the manager's input is a characterization rather than a specific, dated example, since HR and Legal will need it converted to fact before this can be issued.
```

**Governance note:** PIP documentation must be reviewed by HR (and typically Legal) before issuance. This prompt produces a draft for that review, not a final document.

---

## 4. 1:1 development conversation prep from performance data

**What it does:** Prepares a manager for an ongoing 1:1 focused on performance trajectory, using recent context so the manager walks in ready rather than improvising.

```
Prepare talking points for a manager's 1:1 focused on performance trajectory.

Employee: [ROLE, TENURE, CURRENT PERFORMANCE STANDING]
Recent context: [RECENT WINS, RECENT MISSES, ANY FEEDBACK ALREADY GIVEN]
Purpose of this specific 1:1: [e.g., mid-cycle check-in / addressing a recent miss / recognizing recent improvement]

Generate:
1. An opening line that's honest about the purpose without being alarming or falsely casual
2. 2-3 specific things to acknowledge (positive or constructive) tied to actual recent examples
3. 1 question to understand the employee's own view before the manager states theirs
4. A clear statement of what "on track" looks like from here, if relevant
5. What NOT to say (common manager missteps for this type of conversation — over-promising, vague reassurance, burying the real message)

Tone: direct, respectful, no corporate hedging.
```

---

## 5. Cross-team calibration consistency check

**What it does:** Flags cases where similar performance evidence produced different ratings across managers, for an HR calibration lead to investigate — never auto-adjusts a rating.

```
Review these anonymized rating packets for consistency. Flag discrepancies only — do not suggest a "correct" rating.

Packets (role, level, key evidence summary, rating given): [PASTE MULTIPLE PACKETS]

Flag:
1. Any pair of packets with similar evidence but notably different ratings
2. Any packet where the rating seems inconsistent with its own stated evidence (rating higher or lower than the evidence would suggest under the rubric)
3. Any pattern across a specific manager, team, or demographic grouping worth a second look — flag for human investigation, do not draw conclusions about cause

This is a flag-for-review tool for the calibration lead. Every flagged case requires human investigation before any rating changes.
```

---

## 6. Manager self-check before a difficult performance conversation

**What it does:** Gives a manager a structured self-check before a hard conversation, surfacing gaps in their own preparation rather than scripting the conversation for them.

```
I'm about to have a difficult performance conversation. Help me check my preparation before I go in.

Situation: [BRIEF DESCRIPTION]
What I plan to say: [MANAGER'S OWN SUMMARY]
Desired outcome: [WHAT SHOULD THE EMPLOYEE UNDERSTAND OR COMMIT TO]

Check my preparation against these questions and flag any gaps:
1. Do I have specific, dated examples, or am I relying on impressions?
2. Has this person heard any of this feedback before? If not, why is a formal conversation the first time?
3. Am I prepared for the employee to disagree or push back — do I have a plan beyond repeating myself?
4. Is there a clear next step and timeline, or does this conversation end without one?
5. Am I bringing any assumption about this employee's intent (vs. their impact) into this conversation?

Answer honestly based on what I've given you — tell me where my prep is thin, don't just reassure me.
```
