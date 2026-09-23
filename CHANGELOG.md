# Changelog

Notable changes to the playbook. Regulatory content is checked against primary sources; only material changes are logged here.

## 2.3.0 (2026-09-23)

Added

- **A clearer front page.** The README now leads with the playbook's point of view, a five-minute tour, and four stages (Decide, Govern, Build, Adopt and prove) that group the eleven sections. Every section opens with who it is for and where to start.
- **Key dates for HR** in the governance README: every key legal date in one table, in plain language, with a link to the official text and a "Last reviewed" date.
- **New Jersey** in the state law module and the risk assessment template. New Jersey has no AI hiring statute, but its Attorney General's January 2025 guidance says the Law Against Discrimination already covers algorithmic discrimination and that a vendor's tool is no defense.

Fixed

- **Images on the GitHub Pages site.** The banner and the ROI walkthrough lived in `.github/assets/`, which Jekyll does not publish, so both were broken on the site while working on GitHub. They now live in `assets/`.
- **EU AI Act penalties date.** Article 99 fines have applied since 2 August 2025, not 2 August 2026. Only Article 101, for general-purpose AI model providers, started in 2026.
- **EU AI Act wording.** Articles 26(11), 26(12), and 50 are no longer run together, the Article 6(3) exemptions match the Act, and the Article 50 grace period to 2 December 2026 is stated.
- **Notebooks.** The attrition model no longer uses age as an input and audits it instead. The skills gap analysis measures each skill only against the roles that need it. The Q&A demo no longer invents policy details.
- **Prioritization matrix example.** Three weighted scores and one tier were wrong. The example is now recomputed in CI.
- **Eval runner.** A correct refusal is no longer marked as a prompt-injection failure, and a self-harm case now expects crisis resources.
- **Overclaims** removed from the prompt library, curriculum, facilitator guide, and skills. The roadmap diagram matches the phase months.

Removed

- **The claims registry and weekly source-check workflow**, replaced by the Key dates table. They verified that quotes still appeared in statutes, which cost more to maintain than it gave an HR reader.
- **Four AI agent workflows** that depended on an API key that was never configured, so none of them ever ran successfully.

Changed

- **One color system across the portfolio.** The ROI dashboard, the GitHub Pages theme, and the README badges now use the portfolio's midnight, violet, and cyan palette in place of warm beige, Cayman's blue-green gradient, and mixed badge colors. Every text pair on the dashboard was checked in light and dark mode and meets WCAG AA. The walkthrough GIF is recaptured in dark mode.
- **Model cost tiers** price input and output separately, rechecked on 18 September 2026 against each provider's pricing page.

## 2.2.0 (2026-09-12)

Code review pass. The theme: three governance claims were stronger than what the code enforced, and one screening bug produced false negatives on qualified candidates.

Fixed

- **`resume_screen` dropped every short technical term.** The keyword extractor required 4+ characters with the regex `[a-zA-Z][a-zA-Z\-]+`, which silently deleted SQL, AWS, MCP, Go, R, C++, and .NET. A resume reading "built SQL pipelines on AWS" returned `no_evidence_found` against a JD requiring "experience with SQL and AWS", while the response note told the reader that meant the resume didn't mention it. A false negative on a qualified candidate is the worst output this tool can produce. Short and punctuated technical terms now bypass the length floor via `data/technical_terms.json`, with per-term regression assertions.
- **A requirement with no comparable terms is now `not_assessable_by_this_tool`, not `no_evidence_found`.** "5+ years of experience" reduces to zero keywords because every word is a stopword. Reporting that as missing evidence was misleading; the tool cannot measure it.
- **The comp historical-pay guardrail now refuses.** It previously appended a `BLOCKED-BY-POLICY` string to `flags` and returned the full band position, percentile included, so an agent ignoring one list element got the answer the policy forbids. The refusal path now returns no percentile, no band edges, and no label. `used_historical_pay_as_input` also lost its `False` default: a control that fires only when the caller volunteers incriminating input is not a control.
- **Percentile estimates outside p25 to p90 return null instead of an invented number.** The old code assumed a 1st percentile at `p25 * 0.7` and a 99th at `p90 * 1.25` and interpolated into those anchors. Both multipliers were made up, and the resulting figures get quoted to candidates.
- **`policy_qa` retrieval replaced with BM25 plus two measured relevance gates.** The old scorer summed raw keyword-overlap counts with no length normalization and no IDF, so long sections won on volume and "review" counted the same as "Annex". Two heuristics existed to patch the symptoms; the navigational-heading penalty is deleted, since BM25 handles the case it was working around. `no_match` previously fired only on zero word overlap, so "can I bring my dog to the office review?" returned three confident citations. Coverage is weighted by IDF rather than counting terms, so filler words cost nothing and an absent distinctive term is penalized heavily. Both thresholds carry their measurements in the source.
- **`non_empty_response` was computed and never read** by the summary or the gate, so a blank response scored as a clean pass. It is now a launch gate at genuinely empty, while short-but-present stays a review flag.
- **B023 late-binding closure** in `skills-gap-analysis.ipynb`: `lambda row: compute_gap(row, skill)` inside a loop. Correct only because `.apply()` runs immediately; now binds explicitly.
- **CI linted two directories, not the repo.** `ruff check 09-evals 10-mcp-agents` meant notebook cells were never checked: `ruff check .` found 8 findings locally while CI reported zero. Now `ruff check .`, and all 8 are fixed.
- `policy_qa` corpus parsing was re-read and re-parsed on every query; now cached on file mtimes, with a test that an edit still invalidates it. `comp_bands.json` gains schema and monotonicity validation with errors naming the row and key.

Added

- **`09-evals/judge.py`: grades responses against each case's `expected_behavior` criteria.** All 29 cases already carried hand-written criteria that nothing ever read, so an agent that confidently invented a PTO accrual rate passed every gate. Three judge implementations: Anthropic API, canned verdicts for offline and CI use, and a deliberately weak keyword fallback that always reports itself low-confidence.
- **Judge validation via Cohen's kappa against human labels** (`--human-labels`), because an unvalidated grader is not evidence. Kappa rather than raw agreement: on skewed data a judge answering MET every time scores 0.9 raw agreement and 0.0 kappa. Below 0.6 the run says in words that verdicts are review prompts, not scores. `JUDGE_CRITERIA_FAILED` is deliberately not a launch gate until the judge has a measured kappa.
- **Per-group expected calibration error** in the attrition notebook. The existing check compared each group's mean score to its observed rate, which is calibration-in-the-large and hides within-group miscalibration. The new cell demonstrates exactly that on the synthetic data: one group shows a 0.010 mean gap while carrying a 0.118 gap in a bin holding 84 people.
- `ENFORCED_GUARANTEES` and `KNOWN_LIMITATIONS` ship in every `resume_screen` response. The claim "never produces a score" was unenforceable, since the response carries counts a caller can divide, and a test asserting no field name matches `/score|rank/` passes while the guarantee fails. The enforceable subset is now verified behaviorally; what a schema cannot prevent, including the untested linguistic bias in keyword matching, is stated plainly in the payload.
- Corpus trust boundary documented in `policy_qa`, with an `excerpt_provenance` field in every response. Verbatim corpus text in an agent's context is safe when the corpus is reviewed markdown and is an injection path when it is a wiki employees can edit.

Changed

- Test count: 43 to 89.

## 2.1.0 (2026-09-12)

Added

- Connecticut Public Act 26-15 (SB 5), verified against the enrolled act text: the October 1, 2026 provisions (AI is not a defense under Conn. Gen. Stat. 46a-60, and the WARN notice AI disclosure to the Labor Department) and the October 1, 2027 developer and deployer duties, with the CUTPA enforcement posture and the absence of a private right of action (literacy curriculum, risk assessment template)
- Connecticut Section 8(c) developer duty-assumption as a procurement negotiating point (vendor intake checklist)
- European Commission draft Guidelines on Article 6 high-risk classification, published 19 May 2026, flagged as draft and non-binding (intake template, governance README)
- Article 50 transparency obligations and the Article 99 and 101 penalty provisions noted as enforceable since 2 August 2026, so the December 2027 date is not read as "nothing applies yet" (intake template, deployer checklist, governance README)

Changed

- California AB 1883 and SB 947 recorded as pending the Governor's signature with a September 30, 2026 deadline, not as enacted law. Several secondary sources report AB 1883 as signed on September 3, 2026; the leginfo bill history shows it was enrolled and presented to the Governor on September 10, 2026, with no chaptering action
- Model cost tiers in `07-agentic-patterns/agent-design.md` are now defined by role and price band instead of product name, with a dated price check, so the table does not go stale each time a lab ships a flagship
- Module 3 regulatory currency note moved from July 2026 to September 2026

## 2.0.0 (2026-09-04)

Added

- `11-skills`: six installable agent skills for HR teams, ranked in the order to adopt them, plus a human capability ladder that maps each skill to the practitioner skill it depends on
- Root README rewrite with role-based entry points and a "what makes this different" section backed by repo facts
- SECURITY.md, CODE_OF_CONDUCT.md, CITATION.cff, issue templates, PR template
- CI now runs the `10-mcp-agents` pytest suite and ruff, and validates skill package frontmatter
- Eval runner is now a real launch gate: exits 1 when a refusal, escalation, or reachability gate fails; accepts OpenAI, Anthropic, and plain JSON response shapes, not only SSE streams; `--responses-file` scores canned transcripts with no endpoint; 11 scorer tests run in CI
- Attrition notebook fairness audit extended from selection-rate parity to calibration by group and error-rate parity, with a small-group caution (the synthetic data shows exactly why: a 30-person group produces an unstable false negative rate)
- ROI calculator adds a realization rate and a one-time investment; payback formula now consistent between the dashboard, the business case template, and the framework (the template previously labeled a years figure as months)

Changed

- EDPB 2026 Coordinated Enforcement Framework described accurately as a general GDPR transparency action, not an AI-hiring audit (intake template, deployer checklist)
- Colorado: enforcement of SB 24-205 and SB 26-189 is stayed by a federal court pending xAI's challenge and AG rulemaking (risk assessment template, prioritization matrix)
- Texas: TRAIGA complaint portal is live; noted the statute's "consumer" definition excludes the employment context (risk assessment template)
- Illinois: added Public Act 104-0425 civil penalty tiers, verified against statutory text (literacy curriculum)
- Added *Mobley v. Workday* as the reference case for vendor liability, and the ICO's post-report consultation on ADM guidance
- Removed every em dash from the repo; fixed seven ruff findings in the MCP tools
- Eval scorer signals tightened: bare "human" no longer counts as an escalation (it matched "human resources"), and a refusal that names "system prompt" is no longer scored as compliance

## 1.x (2026)

- Working MCP server with four HR tools and a 32-test suite
- Executed notebooks: attrition risk with fairness audit, skills gap analysis, HR Q&A agent demo
- 29-case eval framework with launch-blocking gates
- Governance suite: AI use policy, risk assessment, EU AI Act intake, vendor selection and intake, deployer checklist, incident report, pay equity governance
- Prompt library across eight HR functions
- Literacy curriculum, facilitator guide, adoption playbook, 18-month roadmap, ROI dashboard
