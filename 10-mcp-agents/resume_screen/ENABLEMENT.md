# Bias-mitigated screening tool: handoff notes for a Recruiter or TA lead

## What it does

Takes a JD and a resume, pulls the requirements out of the JD, and for each
one tells you whether the resume has direct evidence, partial evidence, or
none, with the matching resume line shown so you can check it yourself.
Separately, it scans the JD's own wording for gendered-coded terms
("rockstar," "nurturing") and protected-class-proxy phrases ("culture fit,"
"digital native") so you can clean up the req before it goes live.

## What it will never do, and why that's not a limitation

It will never output a score, a percentage match, or a rank. This is
tested, not just documented (`test_output_never_contains_a_score_field`).
That's the entire point of the tool. A "78% match" number feels objective
and isn't, it's a hundred small judgment calls compressed into a figure
nobody can audit. This tool shows you the evidence instead and leaves the
judgment call with you.

**"No evidence found" means the resume doesn't mention it, not that the
candidate doesn't have it.** Resumes are marketing documents, not complete
inventories of someone's skills. Use gaps as interview questions, not
auto-rejection criteria. If you're screening out candidates based on this
tool's "no evidence" flags without a conversation, you've turned a
bias-mitigation tool into exactly the black-box screen it was built to
replace.

## How to extend it yourself

**Add or edit bias terms:** open `data/bias_terms.json`. Three lists:
`masculine_coded` and `feminine_coded` (research-backed gendered wording,
advisory severity, reword at your discretion) and `protected_class_proxy`
(phrases that stand in for a protected characteristic, flagged high
severity, these should almost always come out or get a Legal sign-off).
Add a term, run `pytest test_resume_screen.py`, done.

**Change how strict the evidence match is:** in `tool.py`,
`_evidence_for_requirement` uses a coverage threshold (currently 0.4, meaning
40% of a requirement's key terms need to show up somewhere in the resume) to
decide between "evidence_found" and "partial_evidence_unconfirmed." If
you're finding it too lenient or too strict for your JDs, that's the number
to tune, don't touch the scoring-key ban, that stays.

## If something looks wrong

- **It's missing an obvious requirement from the JD**: check
  `extract_requirements`. It looks for bulleted lines first; a JD written as
  dense paragraphs falls back to sentence-splitting, which is much less
  reliable. If your org's JDs aren't bulleted, that's worth fixing at the
  source (bulleted JDs are also just better JDs) before asking the tool to
  parse paragraphs better.
- **It's flagging a word you don't think is biased in context**: the
  masculine/feminine-coded lists are advisory on purpose, "competitive
  compensation" isn't the same claim as "we need a competitive person." Use
  judgment; the tool surfaces, you decide.
- **You want it to also read PDFs or Word docs**: out of scope here on
  purpose, this tool takes plain text so the matching logic stays
  inspectable. Add a conversion step upstream (in the calling agent, not
  this module) rather than growing file-format handling into the scoring
  logic.

## Where this plugs into governance

This is the mitigation for the "Resume screening and scoring" row in
`01-use-cases/use-case-library.md` (previously flagged "None yet"), and it
implements the fairness-and-bias-prevention principle in
`03-governance/ai-use-policy.md`. If you're asked to add a ranking feature
later: don't, without a real conversation with Legal and People Analytics
first. That's not me being precious about my own code, it's the actual
governance policy this tool is built to comply with.
