# Recruiter intake tool: handoff notes for a recruiter or TA lead

## What it does

Takes a raw hiring-manager intake (job title, must-haves, nice-to-haves,
trainable skills, disqualifiers, a day-in-the-life note) and turns it into
three things: skill buckets, a working Boolean search string, and a list of
clarifying questions for whatever the intake left vague or missing.

## Why the clarifying questions matter as much as the Boolean string

Every question the tool asks maps to a specific way intakes go wrong in
practice: too many "must haves" (more than ~6) usually means some are
actually nice-to-haves, quietly shrinking your candidate pool for no real
reason. No disqualifiers listed means you'll improvise different bars for
different candidates. No day-in-the-life means whoever's doing the sourcing
outreach is guessing at what the role actually feels like. These aren't
generic form-validation nags, they're the specific failure modes that make
a calibration call take twice as long as it should.

## How the Boolean string is built, and the one rule to protect

Must-haves get ANDed together; nice-to-haves get OR'd into their own
optional block. That's deliberate: if a nice-to-have gets ANDed in like a
must-have, you've just told the search engine to reject anyone missing an
optional skill, which is the single most common way a Boolean string
quietly over-filters. If you're extending this tool, keep that separation,
don't let "just AND everything together" creep back in because it looked
simpler.

## How to extend it

**Add a skill and its synonyms:** `data/skill_synonyms.json`, canonical
skill name as the key, list of search-string variants as the value. Unknown
skills still work without expansion, so adding synonyms is purely additive,
never required for the tool to function.

**Add a new clarifying-question rule:** in `tool.py`,
`generate_clarifying_questions`. Each rule should map to a real failure
you've actually seen in a calibration call, not a hypothetical, that's what
keeps this list useful instead of naggy.

## If something looks wrong

- **Boolean string looks off for a skill you know has more search-term
  variants**: add them to the synonyms file, that's the whole fix, no code
  change needed.
- **Too many/too few clarifying questions**: the thresholds (6 must-haves,
  etc.) are guesses calibrated for a small AI/People-tech team. Tune them
  in `tool.py` to match what your own intake calls actually look like.
- **You want it to also draft the outreach message**: intentionally out of
  scope. Drafting a sourcing message needs real judgment about a real
  market and a real candidate pool, that stays with the calling agent and
  the recruiter, not hardcoded into a structuring tool.

## Where this plugs into the rest of the playbook

This is a different intake than `01-use-cases/intake-template.md` (that one
is for proposing new AI use cases to the governance board). This tool is
about a specific req getting calibrated for sourcing. If it's confusing
that both are called "intake," that's worth flagging back to me, naming
things clearly is part of the job.
