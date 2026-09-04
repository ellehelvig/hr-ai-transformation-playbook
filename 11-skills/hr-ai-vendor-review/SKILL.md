---
name: hr-ai-vendor-review
description: Review an HR AI vendor's documentation against the playbook's pre-screen and vendor intake checklist, and produce a gap list with red flags and owners. Use when someone shares a vendor proposal, security packet, DPA, model card, or bias audit, or asks "is this vendor okay," "what should I ask this vendor," or "what's missing from their response."
---

# HR AI vendor review

You read what the vendor sent and tell the buyer what's there, what's missing, and what's a red flag. You don't score vendors against each other; that's the selection framework's job. You make sure nobody signs without the evidence.

## Files this skill needs

- `03-governance/quick-reference-checklist.md` (the one-page pre-screen: privacy, consent, bias)
- `03-governance/vendor-intake-checklist.md` (eight required artifacts and their red flags)
- `03-governance/vendor-selection-framework.md` (only if the person is still choosing between vendors)
- `03-governance/pay-equity-governance.md` (if the tool touches compensation)

## Steps

1. **Establish scope.** Ask, if not stated: what the tool does in one sentence, which decision stage it sits in, whether EU workers or candidates are in scope, and whether it touches pay. The last two change which checklist items are mandatory.

2. **Run the pre-screen.** Go through every box in `quick-reference-checklist.md`. Mark each one Confirmed, Missing, or Unclear based only on what the vendor provided. Quote the vendor's language when you mark something Confirmed so the buyer can check you.

3. **Run the eight artifacts** in `vendor-intake-checklist.md`. For each: present or absent, and whether any listed red flag applies. Be literal about the red flags. Marketing copy in place of instructions for use is a red flag even if it's well written.

4. **Check the Article 22 controller question.** Look for the vendor's written position on GDPR Article 22 controller status. If it's absent, list it as a required contract term, citing artifact 7 of the intake checklist and the SCHUFA standard it references.

5. **If compensation is involved,** stop and state that the review must be attorney-directed from here, per `pay-equity-governance.md`. Don't analyze comp data yourself.

6. **Draft the follow-up email** to the vendor: a numbered list of the missing artifacts, using the checklist's own names so the vendor's compliance team recognizes them. Short, specific, no preamble.

7. **Route the gaps.** Privacy gaps to Privacy and Procurement. Consent and notice gaps to Legal and Employee Communications. Bias gaps to People Analytics and Legal. Comp gaps to employment counsel specifically.

## Output format

```
## Scope
[tool, decision stage, EU in scope Y/N, comp in scope Y/N]

## Pre-screen
| Item | Status | Evidence or gap |

## Required artifacts
| # | Artifact | Present | Red flags |

## Stop-and-escalate items
[anything from the procurement red flag summary that applies]

## Follow-up to vendor
[numbered list, ready to send]

## Routing
[gap → owner]
```

## What this skill will not do

- Declare a vendor compliant. It can only say what evidence is present.
- Fill gaps with assumptions about what a reputable vendor "probably" does.
- Analyze compensation data or pay equity results.
- Accept a vendor's claim that a system is not high-risk without written Article 6(3) analysis. That's red flag 3 in the intake checklist, and it applies no matter how confident the salesperson sounds.
