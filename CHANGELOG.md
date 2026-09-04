# Changelog

Notable changes to the playbook. Regulatory content is re-verified weekly against primary sources; only material changes are logged here.

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
