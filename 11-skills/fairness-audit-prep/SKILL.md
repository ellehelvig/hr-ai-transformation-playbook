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
   - Selection rate by group and the four-fifths ratio (0.80 threshold, per the deployer checklist)
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

## What this skill will not do

- Run statistics on real employee or candidate data. It produces the plan; the org runs it with proper access controls.
- Declare a tool fair. A passing four-fifths ratio is a floor, not a verdict.
- Substitute a vendor's aggregate accuracy number for a group breakdown. That's red flag 6 in the vendor intake checklist.
- Touch compensation analysis outside an attorney-directed process.
