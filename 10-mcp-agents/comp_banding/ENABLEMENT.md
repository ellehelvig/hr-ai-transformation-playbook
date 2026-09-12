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
p90) and figures out where the proposed pay falls on that line.

Outside that range it returns **no percentile at all** (`percentile_estimate`
is null) and gives you `band_label` of "below-range" or "above-range" plus a
flag telling you to route it through the exception process. An earlier version
did report a number out there, by assuming a 1st percentile at 70 percent of
p25 and a 99th at 125 percent of p90 and interpolating into those. Both
multipliers were made up. The benchmark table has four points in it, and
"8th percentile" computed from an invented fifth point is a number you would
have repeated to a candidate in good faith. "Below p25, outside the benchmark
range" is just as actionable and it is true.

If you need real precision at the tails, add p10 and p95 columns to
`comp_bands.json` from your survey data and extend the interpolation points.
Getting more data is the fix; assuming a shape for data you don't have is not.

## The historical-pay guardrail

`used_historical_pay_as_input` is a **required** argument. You cannot call the
tool without answering it.

Answer True if the proposed number came, in any part, from the person's
current or prior salary. You will get a refusal: no percentile, no band edges,
no label. Nothing to quote. Re-derive the number from role, level, and market
data, then call again.

Two earlier versions of this were weaker, and both are worth knowing about if
you are building something similar:

- The argument used to default to False. That meant the guardrail only fired
  when the calling agent volunteered that it had used prohibited input. A
  control that depends on the caller incriminating itself is not a control.
- It used to add a "BLOCKED-BY-POLICY" note to the `flags` list and then return
  the full band position anyway. An agent that read the percentile and ignored
  one list element got exactly the answer the policy forbids.

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
