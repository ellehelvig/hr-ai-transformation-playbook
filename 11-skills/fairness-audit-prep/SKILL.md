---
name: fairness-audit-prep
description: Set up the disparate impact test plan, thresholds, and monitoring template for any HR AI use case that scores, ranks, filters, or recommends people. Use when someone asks "how do we test this for bias," "what's a four-fifths check," "set up fairness monitoring," or before go-live on any scoring or ranking tool.
---

# Fairness audit prep

The playbook's third non-negotiable is that anything scoring or ranking employees or candidates gets a fairness audit. This skill builds the plan. It does not run the audit on real data; that happens in your analytics environment with the right access controls, and the results go through Legal.

## Files this skill needs

- `03-governance/ai-use-policy.md` (principle 3, the required elements)
- `03-governance/deployer-checklist.md` (monthly monitoring template, disparity ratio row)
- `05-notebooks/attrition-risk-modeling.ipynb` (worked example of calibration and disparate impact analysis on synthetic data)
- `03-governance/risk-assessment-template.md` (section 4, fairness and bias assessment)
- `03-governance/pay-equity-governance.md` (if compensation is anywhere in scope)

## Steps

1. **Define the decision and the outcome variable.** What does the tool output (a score, a rank, a pass/fail, a recommendation), and what real decision does it feed? Name the favorable outcome you'll measure selection rates against (advanced to interview, flagged for retention outreach, recommended for role).

2. **List the groups.** Which protected characteristics are relevant and lawfully available in each jurisdiction in scope? Note where the data isn't collected and what proxy risk that creates. Don't invent group labels the org doesn't have.

3. **Set the pre-deployment tests**, using the checklist in `risk-assessment-template.md` section 4:
   - Selection rate by group and the four-fifths ratio (0.80 threshold, per the deployer checklist). Compute it with `scripts/adverse_impact.py` rather than by hand: it takes aggregate counts per group (group, considered, selected), never individual records, and returns each group's selection rate, impact ratio against the highest-rate group, and a two-sided Fisher exact p-value. The 0.80 line is the screening flag in the Uniform Guidelines, [29 CFR 1607.4(D)](https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XIV/part-1607/section-1607.4), which also says sample size matters, hence the p-value. Run it in the plan on synthetic counts to show the method; the org runs it on real counts inside its own analytics environment.
   - Calibration by group: does a score of X mean the same thing for everyone? Point to the notebook for the method.
   - Training data review for historical bias, with a named owner
   - Baseline distribution of inputs so you can detect drift later

4. **Set thresholds that trigger action.** Pull from `ai-use-policy.md` principle 3. Be explicit: what number pauses the tool, what number triggers review, who can press pause without further approval.

5. **Fill the monthly monitoring template** from `deployer-checklist.md`: metric, threshold, owner, action if breached. Add an annual adverse impact review for hiring and performance tools, which the policy requires.

6. **Flag jurisdiction hooks.** If NYC, Illinois, Colorado, California, or the EU are in scope, name the specific obligation from the literacy curriculum's Module 3 and say whether the plan above satisfies it or needs more. Don't summarize the law; point to the doc.

7. **Compensation check.** If the tool influences pay in any way, state that the analysis must be initiated by employment counsel, per `pay-equity-governance.md`, and stop.

## Output format

```
## Decision and outcome
## Groups in scope (and gaps)
## Pre-deployment test plan
| Test | Method | Owner | Pass criterion |
## Thresholds and pause authority
## Monthly monitoring template
| Metric | Threshold | Owner | Action if breached |
## Jurisdiction hooks
## Open questions for Legal
```

## By maturity stage

Stages follow the repo's maturity scale in [the roadmap template](../../06-roadmap/transformation-roadmap-template.md). Decision rights are the same at every stage: the skill drafts the plan, People Analytics runs it on real counts, Legal reviews results.

| Stage | How to run it | Before moving up |
|---|---|---|
| Start (Levels 0 to 1) | Paste the use case card and which group fields each jurisdiction collects. Run `scripts/adverse_impact.py` on synthetic counts only. | People Analytics and Legal approved a plan and its pause owner. |
| Pilot (Level 2) | One read-only export: the intake register card and HRIS data dictionary (field names, no values). Log every run; review a weekly sample. | Every test and threshold row names an owner. |
| Scale (Level 3) | Limited to plan drafting: the agent reads the register and dictionary, never individual records. Track monitoring rows with no owner. | Test cases written in `evals/` (none yet). |
| Embed (Levels 4 to 5) | Limited to plan drafting, triggered when a scoring or ranking use case enters pilot. Pause authority stays with named people. | Rerun the test cases in `evals/` when the skill or model changes. |

## What this skill will not do

- Run statistics on real employee or candidate data. It produces the plan; the org runs it with proper access controls.
- Declare a tool fair. A passing four-fifths ratio is a floor, not a verdict.
- Substitute a vendor's aggregate accuracy number for a group breakdown. That's red flag 6 in the vendor intake checklist.
- Touch compensation analysis outside an attorney-directed process.
