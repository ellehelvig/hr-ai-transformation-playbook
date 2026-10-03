# GitHub portfolio health check

Keep the portfolio useful to People leaders, transformation teams, technical reviewers, and governance owners. Strengthen existing resources before adding a repository. This is a maintenance process, not a certification of security or legal compliance.

## Monthly operating review

| Review | Evidence to capture | Action when it fails |
|---|---|---|
| Security and privacy | Secret scan of current files and reachable history; GitHub alerts where available; synthetic-data review | Treat exposed credentials or inappropriate personal data as P0. Do not paste secrets in issues. Rotate credentials where needed; plan history remediation separately. |
| Dependencies and execution | Clean documented install, runtime entry-point import, relevant tests, current CI and dependency advisories | Distinguish advisory exposure from exploitability. Fix a narrow dependency set and validate runtime behavior. Passing unit tests alone does not prove the server imports. |
| Navigation | Internal files and anchors; external links and live demos | Repair confirmed broken links. Record access-blocked pages as unverified. |
| Documentation and claims | README compared with code, evaluation artifacts, tool counts and model boundaries | Label measured, estimated, illustrative, or hypothetical results. Keep historical evidence attached to the version that produced it. |
| Project hygiene | Open issues and PRs, status, descriptions, topics, branches and licenses | Resolve duplicates and clarify blockers. Recommend substantial deletion or consolidation before executing it. |

For this repository, run the checks in [CONTRIBUTING](../CONTRIBUTING.md#running-the-checks-locally) and inspect CI. Preserve the maintainer review requirement in [CLAUDE.md](../CLAUDE.md).

## Quarterly strategic review

1. Read the profile as a recruiter for 30 seconds. Does it communicate HR transformation, AI enablement, technical fluency, governance, and implementation?
2. Review the featured projects as an HR executive, engineering leader, and responsible AI reviewer. Can each locate business value, implementation evidence, limitations, and release gates?
3. Trace the portfolio through opportunity, prioritization, risk, work design, implementation, evaluation, adoption, and measurement. Identify the weakest evidence, not the most fashionable missing technology.
4. Recheck governance and regulatory statements against primary sources. Record review dates per claim; counsel must review applicability before organizational adoption. Do not advance a review date when sources were inaccessible.
5. Reclassify repositories as HERO, SUPPORTING, DEVELOP, ARCHIVE, PRIVATE, or DELETE CANDIDATE. Preserve private material; recommend consequential changes before execution.
6. Reassess hero selection and role alignment. Prefer two strong anchors over filling a quota with unfinished demos.

## After significant learning

For new knowledge in evaluations, MCP, RAG, agent architectures, AI security, governance, or operating models: identify an existing workflow that benefits; document the decision and tradeoff; implement only where useful; test; update the limitations and evidence. A new concept alone is not a reason for a new repository.

## Prioritization and review record

| Priority | Use when |
|---|---|
| P0 | Security, privacy, broken functionality, or a serious conceptual error |
| P1 | Credibility, misleading claims, incomplete evidence, or recruiter confusion |
| P2 | Reusable resources or validation that materially increase usefulness |
| P3 | Optional visual or editorial polish |

Record one row per improvement:

| Date | Repository / version | Finding and evidence | Priority | Impact | Effort | Recommended action | Owner | Status / validation |
|---|---|---|---|---|---|---|---|---|
| YYYY-MM-DD | Name / commit | Reproducible observation, no sensitive text | P0-P3 | High / medium / low | Hours or days | Concrete change | Accountable reviewer | Proposed / implemented / tested / validated |

Keep private security evidence outside public repositories. A review may pass a narrow check while the portfolio remains unready: unresolved release gates, missing practitioner evaluation, inaccessible security alerts, and unverified business metrics must remain visible in the review record.
