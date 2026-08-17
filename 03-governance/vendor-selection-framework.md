# Build vs. buy and vendor selection framework

Use this before the [vendor intake checklist](vendor-intake-checklist.md), not instead of it. That checklist assumes you've already picked a vendor and are getting ready to sign. This framework is for the stage before that: deciding whether to build at all, and if not, which vendor to run through intake.

Not legal advice. Pair with Legal and Procurement, especially on contract terms and data ownership.

---

## Step 1: Build vs. buy

Most HR AI use cases should be bought, not built. The exceptions are narrower than most HR Tech teams assume.

| Factor | Favors build | Favors buy |
|---|---|---|
| **Uniqueness of the need** | No vendor solves this well; it's specific to your org's process or data | A mature vendor category already exists (ATS scoring, HR chatbots, comp benchmarking) |
| **Internal AI/ML capability** | You have engineers who can own model development and maintenance long-term | HR Tech is 1-3 people with no dedicated ML capacity |
| **Time to value** | You can tolerate 6+ months to a working v1 | You need something live in weeks, not quarters |
| **Data sensitivity** | Keeping data in-house is a hard requirement (rare, but real for some comp and health-adjacent use cases) | Standard vendor DPA and security review is sufficient |
| **Differentiation value** | This is a genuine competitive differentiator for how you do HR | This is table-stakes HR infrastructure everyone needs |
| **Total cost of ownership** | You've actually costed engineering time, monitoring, retraining, and governance overhead, not just the initial build | Vendor pricing is transparent and predictable at your scale |
| **Maintenance burden** | You have a named owner for the model's entire lifecycle, not just the launch | You'd rather pay for someone else to own model drift, retraining, and support |

**Default assumption:** build only if you scored "favors build" on uniqueness of need AND internal capability. Everything else is a secondary consideration. Teams that build because of data sensitivity or differentiation ambition alone, without the capability to back it up, are the most common source of abandoned internal AI tools.

**A note on the notebooks in this playbook:** the [attrition risk model](../05-notebooks/attrition-risk-modeling.md) and [HR Q&A agent](../05-notebooks/hr-qa-agent-demo.md) demos are working sketches meant to show you what a well-governed build looks like, not a recommendation to build these specific things in-house. Most orgs are better served buying an attrition or Q&A product and applying this playbook's governance to it.

---

## Step 2: Vendor comparison scorecard

If you're buying, compare 2-4 real vendors before you pick one to run through the [intake checklist](vendor-intake-checklist.md). Score each 1-5.

| Criterion | Weight | What to evaluate |
|---|---|---|
| **Capability fit** | 25% | Does it solve your actual use case, not an adjacent one the sales deck implied? |
| **Governance readiness** | 25% | Can they answer the [vendor intake checklist](vendor-intake-checklist.md) categories today, or will you be waiting months for documentation? |
| **Security and data posture** | 20% | SOC 2, data residency options, DPA terms, sub-processor list |
| **Integration complexity** | 10% | Does it work with your actual HRIS/ATS/LMS, or does the demo only show a clean sandbox? |
| **Pricing transparency and scalability** | 10% | Is pricing predictable as you scale usage, or does it have hidden per-seat/per-call cliffs? |
| **References in an HR context specifically** | 10% | Not general enterprise AI references, HR-specific customers you can actually call |

**Weighted score** = sum of (criterion score × weight). Score every finalist independently before comparing, same anti-anchoring principle as the [use case prioritization matrix](../01-use-cases/prioritization-matrix.md).

---

## Red flags at the evaluation stage

Catch these before you've invested in a full intake process with a vendor who was never going to pass it:

- Won't run a demo or pilot against your own (de-identified or synthetic) data, only their curated demo data
- No references you can call who are HR buyers specifically, only general enterprise logos
- Pricing requires a call to understand, and the call doesn't produce a real number
- Vague or evasive answers about whether the system would be classified high-risk under the EU AI Act, or claims "AI Act doesn't apply to us" without an Article 6(3) exemption analysis
- Roadmap promises (compliance features, integrations) substitute for what the product does today
- Sales team can't connect you with the people who'll actually support your deployment (implementation, support, security contacts)

Any of these doesn't automatically disqualify a vendor, but it means slow down and verify before starting the formal intake.

---

## Cross-links

- [Vendor intake checklist](vendor-intake-checklist.md): the deep evidence-gathering process once you've picked a finalist.
- [Use case library](../01-use-cases/use-case-library.md): where the use case being solved should come from.
- [Prioritization matrix](../01-use-cases/prioritization-matrix.md): the scoring discipline this framework borrows.
- [Risk assessment template](risk-assessment-template.md): run in parallel with vendor evaluation, not after a vendor is chosen.
