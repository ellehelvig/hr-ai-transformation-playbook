# Flagship decision: extend the playbook before creating another repository

Recommendation for Elle's approval, 3 November 2026. No new flagship implementation has been built.

**Extend `hr-ai-transformation-playbook`, starting with the existing pilot-evidence work. Do not create a separate HR AI pilot evidence gate repository now.** A separate repository would repeat the same decision criteria and synthetic examples before the existing work has a reviewed, integrated path.

## Evidence reviewed

| Existing work | What is implemented or proposed | Boundary |
|---|---|---|
| [Playbook adoption plan](https://github.com/ellehelvig/hr-ai-transformation-playbook/blob/92b888be35eeeb9b972287ffca1f4244063f63f5/04-enablement/adoption-playbook.md) and [roadmap](https://github.com/ellehelvig/hr-ai-transformation-playbook/blob/92b888be35eeeb9b972287ffca1f4244063f63f5/06-roadmap/README.md) | Pilot criteria, roles, adoption work, and human decision rights | Reference guidance, not executable release authorization |
| [PR #51](https://github.com/ellehelvig/hr-ai-transformation-playbook/pull/51), head `5844555` | Read-only Copilot review prompt, grounded in the two source documents; dated development record with three synthetic cases | Draft advisory model output. The record is one author-designed rehearsal, not independent validation or technical enforcement |
| [PR #52](https://github.com/ellehelvig/hr-ai-transformation-playbook/pull/52), head `e9c508e` | Offline strict-schema checker for fictional evidence assertions, incident flags, and total effort; 72 added tests | Does not inspect evidence artifacts or verify approval. Valid pause/stop output exits zero. Every result withholds authorization |
| [Playbook evaluation framework](https://github.com/ellehelvig/hr-ai-transformation-playbook/tree/92b888be35eeeb9b972287ffca1f4244063f63f5/09-evals) | Evaluation cases, scorer/judge code, refusal/escalation checks, and a testable exit-code gate | Specific response-evaluation machinery, not a complete pilot decision system; recorded model/judge validation remains separate |
| [Resolve](https://github.com/ellehelvig/peopleops-resolution-agent/tree/074246e4e026e310e16616b11b44f3fe73cd5a59) | Executable synthetic request workflow, evaluation reports, simulated review, and independent-evaluation protocol | Known rules-only routing failures, self-reported identity, temporary storage, and production hold. It should supply evidence, not approve its own release |

Reviewed PR metadata, changed files, checker source, schema example, tests, and the prompt's development record. Independently reran PR #52's 72 tests and fictional example from its exact source snapshot. All 72 passed; the example returned `pause_for_evidence`, `authorization_granted: false`, identity/access and privacy gaps, and approximately -1.67 illustrative capacity hours. This verifies that example and those tests, not the truth of evidence assertions, independence of evaluation, or readiness for real HR use. PR #51's model rehearsal was not repeated.

Compass is not publicly accessible and Request Desk has no public repository in the accepted audit. Their decision fields remain unanswered. No private source was used to infer their features, and neither is required for this recommendation.

## Why an extension is the stronger next step

The proposed flagship and PRs #51/#52 serve the same HR leader: someone deciding whether evidence supports a pilot's next stage. They use the same adoption and roadmap criteria, preserve human decisions, separate efficiency from safety, and start with fictional data. Publishing another checklist or assertion checker would add a repository without adding a distinct capability.

The meaningful gap is **traceability from a stated criterion to inspectable evidence and a version-specific human review record**. PR #52 intentionally does not close that gap. Its advisory behavior should remain unchanged unless a separately reviewed specification says otherwise. Rename neither its exit code nor its `present` assertions into proof of an enforced deployment gate.

An extension keeps policy guidance, examples, tests, and limits together. Resolve can provide a documented synthetic evidence packet while retaining its production hold. This creates a clearer portfolio story: choose and redesign the work in the playbook, observe a workflow in Resolve, then review its evidence before proposing expansion.

## Proposed scope, only after approval

1. Define a small, versioned synthetic evidence-packet contract. Include criterion IDs, the tested source revision, dataset/method identifiers, provenance limits, and references to local artifacts. Validate malformed, absent, stale, and mismatched artifacts. An artifact hash establishes content identity, not truth or independence.
2. Add a separate evidence-packet validator and readable review report beside PR #52's advisory preflight. Keep its caller assertions visibly separate from inspected artifacts and observed test results. Missing or failed required evidence must be reported explicitly, without being offset by capacity estimates.
3. Record a proposed human disposition for the specific evidence version. If identity remains typed and storage local, label both as simulated and editable. Do not claim authenticated approval, tamper-proof audit trails, or deployment authorization. Any future enforceable release gate needs its own threat model and integration design.
4. Add fictional examples that produce pause, stop, and eligible-for-human-review reports, plus a Resolve example that preserves its known failures. Never let an example reach a production-approved state merely because familiar regression cases pass.
5. Publish a concise walkthrough and current screenshots in the playbook. Document what a reviewer must inspect and what the code cannot verify. Map any governance criteria to current primary sources when that specification is written. Do not label the result an independent NYC bias audit, EU compliance certification, or NIST certification.

No new authentication system, employee data integration, model calls, legal conclusion, or operational HR deployment belongs in this initial extension.

## Acceptance criteria for a later implementation proposal

- Existing PR behavior and tests remain intact or changes are explicitly justified.
- Missing, stale, contradictory, or revision-mismatched required evidence cannot yield a clean report.
- Known Resolve misses remain visible and the production hold is preserved.
- Every displayed outcome identifies its source revision, synthetic dataset/method, and limits.
- Human-review status cannot be confused with verified identity or authority to deploy.
- A fresh contributor can run the offline fictional examples and tests from documented commands.
- CI passes on the proposed head; claims and screenshots match that head.

## Reconsidering a standalone repository

Reconsider extraction only after a reusable contract serves at least two distinct workflows without depending on the playbook's internal layout, and the maintenance boundary is clear. This is a proposed design criterion, not a claim that two such integrations already exist. A new repository should follow demonstrated separation of purpose, not precede it.

## Approval requested

Approve an extension of the playbook in the narrow scope above, or request a different scope. PRs #51 and #52 remain unmerged proposals for Elle to review first. This decision does not approve or merge them. Implementation of the proposed extension is paused pending Elle's approval.
