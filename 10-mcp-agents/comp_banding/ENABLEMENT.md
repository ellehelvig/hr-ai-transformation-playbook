# Comp banding tool: handoff notes for a Compensation Analyst

This is the doc you'd get if I were pairing with you directly, per the JD's
"transfer your technical craft so they can independently maintain and evolve
their own tools." Goal: after reading this, you can update the benchmark data
and extend the tool without needing an engineer in the room.

## What it does

Given a role family, level, location tier, and a proposed base pay, it tells
you where that number falls against benchmark bands (p25/p50/p75/p90), and
raises specific flags: below-range, above-p90, or "this number came from
someone's pay history, which policy doesn't allow as a banding input."

## What it deliberately does not do

It doesn't recommend a number. It doesn't approve anything. It always comes
back with `human_review_required: true`, and there is no way to turn that
off from the outside, that's intentional, not a bug to route around.

## The one thing to understand before you touch this

The benchmark data lives in `data/comp_bands.json`, in plain JSON, not
buried in a database or a notebook. That's the whole point: you should be
able to open that file, add a row for a role family we don't cover yet, and
re-run the tests, without asking anyone.

To add a role:

1. Open `data/comp_bands.json`.
2. Copy an existing row, e.g.:
   ```json
   {"role_family": "Recruiter", "level": "IC3", "location_tier": "tier1", "p25": 92000, "p50": 105000, "p75": 120000, "p90": 136000}
   ```
3. Change the values to your new role/level/tier and real survey numbers.
4. Run `pytest test_comp_banding.py` from this folder. If it's green, you're done.

**Replace the sample data before this touches anything real.** Everything in
that file right now is synthetic, made up for this demo, not sourced from
any real survey or real employee pay. There's a `_disclaimer` field at the
top of the JSON as a reminder.

## How the percentile math works, in plain terms

The tool draws a line between your known benchmark points (p25, p50, p75,
p90) and figures out where the proposed pay falls on that line. If pay is
below p25 or above p90, it doesn't try to extrapolate very far past those
points, it just says "below-range" or "above-range" and tells you to route
it through the exception process instead of trusting a number the tool
invented past the edge of real data.

## If something looks wrong

- **Wrong band assignment**: check the JSON row for that role first. 90% of
  "the tool is broken" reports are a stale or mistyped benchmark row, not a
  code bug.
- **A role is missing entirely**: the tool raises an error by design instead
  of guessing the closest match. Add the row (see above) rather than asking
  for a "fuzzy match" feature, a fuzzy match on comp bands is how you end up
  quietly underpaying someone in a role that's adjacent but not the same.
- **You want it to also handle bonus/equity, not just base**: that's a real
  next step, not in scope here. Talk to me before extending the schema so
  the flags logic (retention risk, exception routing) gets extended
  consistently rather than per-field.

## Where this plugs into governance

This tool implements one specific rule from
`03-governance/pay-equity-governance.md`: don't use historical pay as a
banding input. If you're adding new flags, check that file first, most
"should the tool block this?" questions already have an answer written down
there.
