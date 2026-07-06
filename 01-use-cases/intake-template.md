# Use case intake template

Submit a new use case for review. Fill in all fields, open a pull request, and a maintainer will review within 2 weeks.

---

## Use case name

## One-sentence description

## HR function
(Talent Acquisition / Onboarding / Performance / L&D / HR Ops / People Analytics / Other)

## Problem it solves
What is painful, slow, or inconsistent today without this use case?

## Who benefits
Who uses it, and what is their experience improved?

## AI approach
(Agent / Copilot / Automation / Analytics)

## Data required
What data does this use case need? Where does it come from?

## Human review gate
Where does a human review AI output before it affects an employee?

## Proposed success metric(s)

## Known risks or governance considerations

## Have you tested this?
(Yes, describe / No, why are you proposing it?)

## Contact
Name and email for follow-up questions

---

## Worked example: filled-in intake submission

Below is a real-world example of how to fill out this template. Use it as a reference for the level of detail expected when submitting your own.

### Use case name
Exit interview theme synthesis

### One-sentence description
AI-augmented synthesis of free-text exit interview responses to surface departure themes, retention risks, and manager-specific patterns for HR leadership.

### HR function
People Analytics

### Problem it solves
Exit interview data sits unanalyzed because HR Ops doesn't have time to read every response. Patterns surface only when People Analytics runs the quarterly review, by which point the people who could have acted on the signal have moved on. Manager-specific concentration of exits takes 6+ months to identify.

### Who benefits
HR leadership and HRBPs get monthly attrition theme reports instead of quarterly. Specific managers receive aggregated feedback about patterns in their team's exits within 30 days. People Analytics frees up ~20 hours/quarter previously spent on manual synthesis.

### AI approach
Analytics. Copilot-style. AI generates the theme synthesis; HRBP reviews and validates before it reaches leadership or managers.

### Data required
- Exit interview free-text responses (from existing survey tool)
- Employee tenure, role, team, location, manager (from HRIS, joined on employee ID)
- Voluntary vs. involuntary departure flag
- Data accessed only post-departure, no active employee data needed

### Human review gate
HRBP reviews and validates synthesis before delivery to leadership or managers. Manager-specific reports require HRBP sign-off. Themes flagged as "potential systemic issue" route to People Analytics for deeper investigation before action.

### Proposed success metric(s)
- Time-to-insight on attrition patterns: 90 days → 30 days
- HRBP time spent on exit data synthesis: −75%
- Manager-specific intervention rate (managers who receive a flagged report and act within 30 days): target 60%+
- HRBP-rated accuracy of AI synthesis: target ≥4.0/5.0

### Known risks or governance considerations
- Risk of identifying individuals through small-sample exits, mitigation: minimum 5 exits per cohort for any team-specific report
- Risk of reinforcing manager bias if synthesis isn't validated, mitigation: HRBP review required before any manager-specific delivery
- Risk of suppressing critical feedback that's uncomfortable for leadership, mitigation: include verbatim quotes alongside synthesis
- No PII or compensation data accessed by AI tool
- Exit interview data subject to existing retention policy; AI synthesis stored with same controls

### Have you tested this?
Yes, manual prototype run on Q1 2026 exit data (n=47). HRBP rated 5 of 6 themes as accurate; one was a false pattern from a 3-exit cohort, which is what surfaced the need for minimum-sample thresholds.

### Contact
[Your name, your email]
