---
name: function-inclusion-belonging
description: Designs and audits people programs and selection processes so they are open to all eligible employees, use job-related, skills-based criteria applied the same way to everyone, and are accessible to people with disabilities, producing a program access review, a criteria table, an accommodation path, plain-language rewrites, and questions for counsel. Use whenever someone says "review our ERG charter," "is our mentoring program open to everyone," "audit our hiring process for fairness," "make this job posting clearer and more inclusive," "set up an accommodation request process," "check this training content," "what changed for DEI programs," or "do we need to change this program for a federal contract," and whenever a program limits eligibility or a tool scores or ranks people. Routes every legal question to counsel and every decision about a named person to its owner.
---

# Inclusion, belonging and fair processes

This skill serves the inclusion lead, program owner, or HRBP who must show that each people program is open to all eligible employees, uses job-related criteria applied consistently, and is accessible. It compares programs with primary-source guidance, frames gaps as questions for counsel, and drafts fixes. It stops before any legal opinion and any decision about a named person: counsel and the program owner own those.

## Files this skill needs

- `03-governance/README.md` (Key dates for HR table, and the US federal AI enforcement context section on disparate impact)
- `03-governance/ai-use-policy.md` (principle 2 on notice, principle 3 on fairness, principle 4 on protected category data, and the prohibited use on inferring health or disability)
- `11-skills/fairness-audit-prep/SKILL.md` (whenever a process uses a tool that scores, ranks, filters, or recommends people, or selection rates are compared)
- `03-governance/risk-assessment-template.md` (section 4, fairness and bias assessment)
- `02-prompt-library/talent-acquisition.md` (prompt 1, job description review; prompt 2, interview question bank)
- `02-prompt-library/internal-mobility.md` (prompt 1, internal job posting; prompt 5, stretch assignment matching explanation)
- `02-prompt-library/hr-operations.md` (prompt 4, return-to-work synthesis, which routes accommodation requests to the formal process)

## Inputs

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| Jurisdictions in scope (US federal guidance does not describe other countries' law) | Yes | HRIS, read-only: headcount by country and state | California, Illinois, NYC, Colorado, Germany |
| Federal contractor, subcontractor, or federal funds recipient | Yes | Ask the user | No federal contracts; one research grant, counsel to confirm |
| Company size, because federal EEO coverage depends on headcount | Yes | HRIS, read-only: active headcount total | 1,400 |
| Program inventory, including past names | Yes | Ask the user, plus LMS and community platform, read-only: program name, written eligibility | "Emerging Leaders," formerly "Diverse Leaders" |
| How people are selected in practice | Yes | Ask the program owner | Manager nomination, no written criteria |
| Aggregate selection or enrollment counts by stage | No | ATS or LMS, read-only: counts by stage and group, no individual records | 47 of 600 eligible nominated |
| Owners: program, accommodation decisions, counsel | Yes | Ask the user | Program owner L&D lead; accommodation owner Benefits |

If a required input is missing, ask once in one message. Then proceed and label each gap "Not provided" in the output and the audit trail.

## Tools and connectors

- **Reads allowed, read-only, minimum fields.** ATS (stage names, selection criteria configuration, aggregate counts by stage). LMS (program eligibility rules, aggregate enrollment). Community or ERG platform (charter, membership rules, never member lists). Accommodation case tool (request dates and first-response dates only, never medical documents or diagnoses). HRIS (headcount by location). Use MCP connectors or exports.
- **Repo tools.** `lint_jd_language` in `10-mcp-agents/resume_screen/` flags gendered-coded wording and protected-class-proxy phrases in any posting or program text; its flags are prompts to rewrite, not verdicts. `ask_governance_policy` in `10-mcp-agents/policy_qa/` cites `03-governance/*.md`; it is not legal advice.
- **Never write.** Do not call any write, send, update, or publish tool, even if the connector offers one. Owners post and change programs.
- **Log every call.** Record tool, purpose, and fields read in the audit trail.
- **Stop on spillover.** If a tool returns individual demographic, health, or accommodation records, stop, do not use them, and ask the user how to proceed.

## Steps

Run as a checkpointed workflow: complete a step, show it, and wait for the named sign-off before any step that depends on it.

1. **Start from the current primary sources, stated neutrally.** Summarize what each source says, with its link, and nothing more. Executive Order 14173 revoked Executive Order 11246 and directs agencies to put two terms in federal contracts and grants: that compliance with federal anti-discrimination law is material to payment decisions under the False Claims Act, and a certification that the recipient does not operate DEI programs that violate those laws. OFCCP's final rule rescinds the regulations that implemented Executive Order 11246; read it in the Federal Register for its full scope. For both, see the Key dates rows "US Executive Order 14173" and "OFCCP final rule rescinding the EO 11246 regulations". The EEOC's technical assistance says DEI is not defined in Title VII and that an employment action motivated in whole or in part by a protected characteristic can be unlawful. In February 2026 the EEOC Chair sent a letter to large employers pointing them to that guidance. A July 2025 Attorney General memo for recipients of federal funding lists practices it treats as unlawful and gives non-binding best practices. Sign-off: counsel confirms which apply and whether any has changed since it was read.

2. **Inventory every program and practice.** Include programs under other names; the EEOC Chair's letter names "Inclusion & Diversity" and "Belonging" as examples. For each, record eligibility as written and as practiced: hiring and promotion steps, candidate slates, internships and fellowships, mentoring and sponsorship, leadership development, training, ERGs, and scholarships or awards. Sign-off: each program owner confirms their row.

3. **Check access to each program.** Is it open to all eligible employees regardless of protected characteristic? Does it limit membership or separate people by a protected characteristic, even with the same content or resources? The EEOC lists both as possible discrimination. Does any facially neutral criterion work as a stand-in for a protected characteristic? The Attorney General memo gives examples, such as diversity statements and geographic targeting chosen for demographic reasons. Is it announced where everyone can see it? Record each answer as a question for counsel, not a verdict. Sign-off: counsel.

4. **Make selection criteria job-related, skills-based, and consistent.** Tie each selection step to specific, measurable skills for the role, and accept evidence of the skill (work samples, portfolio, assessed tasks) in place of a credential unless the credential is a documented job requirement. Use structured interviews: the same questions in the same order, scored on one rating scale with shared standards. Tell candidates what each stage is, how it relates to the job, and how decisions are made. Document the job-related reason for every criterion. If AI skill or AI use is proposed as a criterion, first check that every group had equal access to approved tools, training, practice time, and accommodations. If any step uses a tool that scores, ranks, or filters people, run `fairness-audit-prep` before use, and ask the vendor how the tool works, how it is audited, and its record on bias; do not rely on the vendor for compliance. Sign-off: program owner and counsel approve the criteria.

5. **Check selection outcomes for adverse impact.** For any step that selects people (nomination, slate, interview advance, program admission), People Analytics compares selection rates by group using `fairness-audit-prep`, with counsel deciding first whether and how demographic data is analyzed. The four-fifths ratio is a screening flag under the Uniform Guidelines, [29 CFR 1607.4(D)](https://www.govinfo.gov/content/pkg/CFR-2024-title29-vol4/pdf/CFR-2024-title29-vol4-sec1607-4.pdf), not a safe harbor or a verdict; small groups need a statistical test that People Analytics or counsel interprets. Include age and disability in scope, not only race and sex. Report aggregates only. Sign-off: counsel reviews results before they go to leadership.

6. **Draft clear, accessible language.** Rewrite postings and program descriptions in plain words: essential functions, real requirements, who is eligible, how to apply, and how to request an accommodation. Run `lint_jd_language` and remove eligibility wording tied to a protected characteristic. A tool that only checks wording for clear, inclusive language is a lower-risk use: the European Commission's draft high-risk guidelines (a consultation draft, not binding) place inclusive-language checkers outside the high-risk employment rules, but not a tool that sets requirements or scores applicants. Sign-off: the posting or program owner approves the final text before it is posted.

7. **Set up the accommodation path.** Follow the EEOC's ADA guidance. A person can ask in plain words, without saying "reasonable accommodation" or naming the ADA; a representative can ask for them; the request need not be in writing. The request starts an interactive process; respond promptly. Ask for medical documentation only when the disability or need is not obvious, and only what shows the disability and the need. Applicants are entitled to accommodation in the application process. Before a conditional offer, an employer generally may not ask whether an applicant will need accommodation, with narrow exceptions. Requesting a disability or religious accommodation is protected activity. The agent drafts process documents and routes requests. Sign-off: the accommodation owner decides every request.

8. **Review training content.** Check materials for content that stereotypes, excludes, or assigns traits to people by protected characteristic. The EEOC says training can support a hostile environment claim depending on its design, content, and delivery, and that opposing a training can be protected activity when the employee has a fact-specific basis. Sign-off: content owner and counsel decide on flagged content.

9. **Explain, give notice, and hand off.** For every change, record the old rule, the new rule, the job-related reason, the source, and who approved it. For each selection process, draft the explanation people receive: stages, criteria, whether AI assisted any step, and how to request an accommodation or human review. Track each cycle: criteria applied the same way, program access, accommodation response times, and candidate feedback on fairness. Sign-off: each program owner.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Neutral summary of current federal guidance with links | Counsel | Drafts for sign-off |
| Program inventory and eligibility table | Program owners | Drafts for sign-off |
| Check program eligibility against the access checklist | Counsel | Drafts for sign-off |
| Run `lint_jd_language` on a posting and list the flags | Posting owner | Does alone |
| Posting or program description rewrite | Posting or program owner | Drafts for sign-off |
| Structured interview questions and rating scale | Hiring manager and TA lead | Drafts for sign-off |
| Route an accommodation request to the formal process | Accommodation owner | Does alone |
| Accommodation decision for a named person | Accommodation owner, with counsel where needed | Refuses and routes |
| Training content review | Content owner and counsel | Drafts for sign-off |
| Aggregate adverse impact results | People Analytics and counsel | Drafts for sign-off |
| Selection or eligibility decision about a named person | Decision owner | Refuses and routes |
| Whether a program is lawful, or signing a federal contract certification | Counsel | Refuses and routes |

### Refuse and route

- "Is our program legal?": refuse a legal opinion; route to counsel with the program access review.
- "Limit this mentoring circle to one gender" or "keep the ERG members-only by race": refuse to draft protected-characteristic eligibility; route to counsel and the program owner with the access questions.
- "Rank these candidates so the slate looks diverse" or "pick the nominees": refuse; route to the hiring manager or program owner with the job-related criteria table.
- "Use leave or badge data to find employees who probably have a disability": refuse; inferring health or disability is a prohibited use; route to the accommodation owner and privacy lead and offer an open accommodation notice instead.
- "Pull the ERG member list with demographics": refuse; route to the privacy lead and work from aggregate counts.
- "Write our position on the new DEI policy": refuse political commentary; offer a neutral, sourced summary for counsel.
- "Post the new requirements to the ATS": refuse; the posting owner publishes.
- "Use real employee data in the example": refuse; examples use synthetic data only.

## Guardrails

- **Neutral and sourced.** State what a primary source says, with its link. No political commentary, no characterizing the policy, no prediction of enforcement. Say where a source describes itself as non-binding.
- **Fairness and adverse impact.** Check explicit criteria and neutral proxies. Disparate impact claims remain possible; see the US federal AI enforcement context in `03-governance/README.md`.
- **Disability and health data.** Never infer disability or a health condition; it is a prohibited use in `ai-use-policy.md`. Medical documentation stays in the accommodation process and out of AI tools not approved for it.
- **Privacy and minimization.** Work from program rules and aggregate counts. Never paste individual demographic records into an AI tool.
- **Explainability and notice.** Tell employees and candidates when AI is used in a process that affects them (`ai-use-policy.md` principle 2), how each stage relates to the job, and how to request an accommodation and human review.
- **Legal review triggers.** Any program limited by a protected characteristic, any federal contract or funding certification, any demographic analysis, any accommodation dispute, and any non-US jurisdiction.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| US Executive Order 14173 | The organization holds federal contracts or grants | Flags the certification question for counsel; gives no view on compliance |
| OFCCP final rule rescinding the EO 11246 regulations | A federal contractor's affirmative action plan or program relies on the old regulations | Lists affected programs for counsel to review against the rule |
| NYC Local Law 144 | A covered automated tool is used in hiring or promotion for NYC roles | Routes to `fairness-audit-prep` and counsel before use |
| Illinois HB 3773 (Public Act 103-0804) | AI is used in hiring or promotion for Illinois roles | Adds an AI-use notice line to the explanation in step 9 for counsel to confirm |
| California FEHA automated-decision system regulations | An automated tool is used in hiring or employment for California roles | Requires the adverse impact check in step 5 before use |
| EU AI Act, high-risk HR systems | A tool sets requirements or scores applicants for German roles | Routes to `eu-ai-act-hr-classifier` and counsel |

See each Key dates row in `03-governance/README.md` for status and dates. Counsel confirms scope and current status before you rely on any row.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| Open-access program rate | Programs whose written and practiced eligibility are open to all eligible employees, divided by programs inventoried, at quarter end | The outcome this skill exists to produce |
| Accommodation first-response time | Median business days from request receipt to first interactive-process response, for requests received in the quarter | Shows whether the path works for the people who use it |
| Selection steps with a screening flag | Selection steps where any group's selection rate divided by the highest group's rate fell below 0.80 in the period, divided by selection steps tested, each flag then reviewed under `fairness-audit-prep` | The fairness signal leadership sees, with counsel interpreting each flag |

## Output format

```markdown
## Scope
[jurisdictions, federal contractor or funding Y/N, programs in scope, owners, counsel]

## Primary sources reviewed
| Source | What it says (neutral summary) | Link | Applies here? (counsel) |

## Program access review
| Program | Eligibility as written | As practiced | Open to all eligible Y/N | Possible proxy criteria | Question for counsel |

## Selection criteria
| Process step | Criterion | Skills evidence accepted | Job-related reason | Applied consistently? | Tool that scores or ranks Y/N |

## Adverse impact screen (aggregates only)
| Step | Group | Selected / eligible | Rate | Ratio to highest | Flag | Routed to |

## Accommodation path
[how to ask, who receives it, response time target, documentation rule, owner]

## Language changes
| Document | Current text | Proposed text | Reason | lint_jd_language flags |

## Decision rights calls
| Request | Agent role | Routed to |

## Next step owner
[program owner, accommodation owner, counsel, and what each must decide]

## Audit trail
Inputs used: [list; gaps marked Not provided]
Tools called: | Tool | Purpose | Fields read |
Needs sign-off: [item, who]
Open legal questions: [question, Key dates row if any, counsel]
```

## Worked example

Harbor & Pine's inclusion lead asks for a review of three development programs, one of which limits membership by sex and one of which shows a selection-rate flag by age band. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They are written, not yet run against a model.

- `core-program-access-review`: access review of three programs plus a posting rewrite.
- `edge-germany-and-unknown-contractor-status`: programs spanning the US and Germany with federal contractor status unknown.
- `red-flag-infer-disability-from-leave-data`: a request to flag employees who probably have a disability.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. Executive Order 14173, Ending Illegal Discrimination and Restoring Merit-Based Opportunity, Federal Register, published 31 January 2025. https://www.federalregister.gov/documents/2025/01/31/2025-02097/ending-illegal-discrimination-and-restoring-merit-based-opportunity. Supports: revocation of EO 11246, contract and grant terms, private sector direction.
2. OFCCP final rule rescinding the regulations implementing Executive Order 11246, Federal Register, document 2026-17114, effective 26 October 2026. https://www.federalregister.gov/documents/full_text/html/2026/08/21/2026-17114.html. Supports: rescission of the EO 11246 implementing regulations.
3. What You Should Know About DEI-Related Discrimination at Work, U.S. Equal Employment Opportunity Commission. https://www.eeoc.gov/wysk/what-you-should-know-about-dei-related-discrimination-work. Supports: DEI not defined in Title VII, examples including ERG limits and segregated training, training and hostile environment, retaliation for opposing training.
4. Reminder of Title VII Obligations Related to DEI Initiatives, U.S. Equal Employment Opportunity Commission, 26 February 2026. https://www.eeoc.gov/reminder-title-vii-obligations-related-dei-initiatives. Supports: letter to large employers, programs under other names, guidance described as non-binding.
5. Guidance for Recipients of Federal Funding Regarding Unlawful Discrimination, U.S. Department of Justice, Office of the Attorney General, 29 July 2025. https://www.justice.gov/ag/media/1409486/dl. Supports: proxy criteria examples, non-binding best practices on open access, skills-based criteria, documenting rationale.
6. Enforcement Guidance on Reasonable Accommodation and Undue Hardship under the ADA, U.S. Equal Employment Opportunity Commission. https://www.eeoc.gov/laws/guidance/enforcement-guidance-reasonable-accommodation-and-undue-hardship-under-ada. Supports: plain-language requests, interactive process, documentation limits, applicants, pre-offer inquiries.
7. Retaliation, U.S. Equal Employment Opportunity Commission. https://www.eeoc.gov/retaliation. Supports: accommodation requests as protected activity, coverage thresholds.
8. Structured Interviews, U.S. Office of Personnel Management. https://www.opm.gov/policy-data-oversight/assessment-and-selection/structured-interviews/. Supports: same questions, same order, one rating scale.
9. Fair selection: an evidence review, practice summary, CIPD, April 2023. https://www.cipd.org/globalassets/media/knowledge/knowledge-hub/evidence-reviews/2023-pdfs/fair-selection-evidence-practice-summary_tcm18-114569.pdf. Supports: job-related selection measures, explaining stages and decisions to candidates.
10. SHRM's BEAM Framework for Inclusion: Aligning Merit with Organizational Excellence, SHRM, 31 January 2025. https://shrm.org/topics-tools/news/inclusion-diversity/shrms-beam-framework-for-inclusion-aligning-merit-with-organizational-excellence. Supports: programs open to all, job-related qualifications, broad and accessible communication.
11. AI in the Workplace Playbook, SHRM, 2025. Read from a copy of the publication; no web address checked. Supports: questions to ask AI vendors, not relying on vendors for compliance, bias audits that include age and disability, providing accommodations.
12. Draft guidelines on the classification of high-risk AI systems, European Commission, consultation drafts (2026), non-binding. Read from a copy of the publication; no web address checked. Supports: draft examples placing inclusive-language checkers outside, and requirement-setting or applicant-scoring tools inside, the high-risk employment rules.
