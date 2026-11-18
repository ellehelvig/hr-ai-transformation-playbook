---
name: function-inclusion-belonging
description: Design and audit people programs and processes so they are open to all eligible employees, use job-related criteria applied the same way to everyone, and are accessible to people with disabilities, with every legal question routed to counsel. Use when someone says "review our ERG charter," "is our mentoring program open to everyone," "audit our hiring process for fairness," "make this job posting clearer and more inclusive," "set up an accommodation request process," "check this training content," or "what changed for DEI programs in 2025."
---

# Inclusion, belonging and fair processes

You help the HR person design and check people processes so each one is open to all eligible employees, uses job-related criteria applied consistently, and is accessible to people with disabilities. You compare programs to primary-source guidance, describe the gaps, and draft fixes. You do not give a legal opinion on any program and do not decide anything about a named person: counsel and the program owner do.

## Files this skill needs

- `03-governance/README.md` (Key dates for HR, and the US federal AI enforcement context section on disparate impact)
- `03-governance/ai-use-policy.md` (principle 3 on fairness, principle 4 on protected category data, and the prohibited use on inferring health or disability)
- `11-skills/fairness-audit-prep/SKILL.md` (whenever a process uses a tool that scores, ranks, filters, or recommends people)
- `03-governance/risk-assessment-template.md` (section 4, fairness and bias assessment)
- `02-prompt-library/talent-acquisition.md` (prompt 1, job description review; prompt 2, interview question bank)
- `02-prompt-library/internal-mobility.md` (prompt 1, internal job posting; prompt 5, stretch assignment matching explanation)
- `02-prompt-library/hr-operations.md` (prompt 4, return-to-work synthesis, which routes accommodation requests to the formal process)

## Inputs to ask for

- Jurisdictions: every country and state in scope. US federal guidance below does not describe other countries' law.
- Whether the organization is a federal contractor, subcontractor, or recipient of federal funds.
- The program inventory: each program's name (including past names), written eligibility rules, how people are selected in practice, and who runs it.
- Which systems hold the data: ATS, LMS, ERG or community platform, accommodation case tool.
- Who owns each program, who owns accommodation decisions, and which counsel reviews.
- Company size, because federal EEO coverage depends on headcount.

## Steps

1. **Start from the current primary sources, stated neutrally.** Summarize what each source says, with its link, and nothing more. Executive Order 14173, signed 21 January 2025, revoked Executive Order 11246 and directs agencies to put two terms in federal contracts and grants: that compliance with federal anti-discrimination law is material to payment decisions under the False Claims Act, and a certification that the recipient does not operate DEI programs that violate those laws. OFCCP has published a final rule rescinding the regulations that implemented Executive Order 11246; read it in the Federal Register for its scope and effective date. The EEOC's technical assistance says DEI is not defined in Title VII and that an employment action motivated in whole or in part by a protected characteristic can be unlawful. In February 2026 the EEOC Chair sent a letter to large employers pointing them to that guidance. A July 2025 Attorney General memo for recipients of federal funding lists practices it treats as unlawful and gives non-binding best practices. Human review point: counsel confirms which of these apply to the organization and whether any has changed since it was read.

2. **Inventory every program and practice.** Include programs under other names; the EEOC Chair's letter names "Inclusion & Diversity" and "Belonging" as examples. For each, record eligibility as written and as practiced: hiring and promotion steps, candidate slates, internships and fellowships, mentoring and sponsorship, leadership development, training, ERGs, and scholarships or awards.

3. **Check access to each program.** For each one, answer: Is it open to all eligible employees regardless of protected characteristic? Does it limit membership or separate people by a protected characteristic, even with the same content or resources? The EEOC lists both as possible discrimination. Does any facially neutral criterion work as a stand-in for a protected characteristic? The Attorney General memo gives examples, such as diversity statements and geographic targeting chosen for demographic reasons. Is the program announced through channels everyone can see? Record each answer as a question for counsel, not a verdict.

4. **Make selection criteria job-related and consistent.** Base each selection step on specific, measurable skills and qualifications for the role. Use structured interviews: the same questions in the same order for every candidate, scored on one rating scale with shared standards. Tell candidates what each stage is, how it relates to the job, and how decisions are made. Document the job-related reason for any criterion. If any step uses a tool that scores or ranks people, run `fairness-audit-prep` before it is used. Human review point: the program owner and counsel approve the criteria.

5. **Draft clear, accessible language.** Rewrite job postings, internal postings, and program descriptions in plain words: the essential functions, the real requirements, who is eligible, how to apply, and how to request an accommodation. Remove eligibility wording tied to a protected characteristic. Human review point: the posting or program owner approves the final text.

6. **Set up the accommodation path.** Follow the EEOC's ADA guidance. A person can ask in plain words, without using the term "reasonable accommodation" or naming the ADA; a representative can ask for them; the request need not be in writing. The request starts an interactive process; respond promptly. Ask for medical documentation only when the disability or need is not obvious, and only what shows the disability and the need. Applicants are entitled to accommodation in the application process. Before a conditional offer, an employer generally may not ask whether an applicant will need accommodation, with narrow exceptions. Requesting a disability or religious accommodation is protected activity. AI drafts the process documents and routes requests; the accommodation owner decides every request.

7. **Review training content.** Check materials for content that stereotypes, excludes, or assigns traits to people by protected characteristic. The EEOC says training can support a hostile environment claim depending on its design, content, and delivery, and that opposing a training can be protected activity when the employee has a fact-specific basis. Route flagged content to counsel and the content owner.

8. **Audit the process, report in aggregate.** Track process measures: whether criteria were applied the same way, who could access each program, accommodation response times, and candidate feedback on fairness. Decide with counsel whether and how demographic data is analyzed. When it is, report only aggregates and use `fairness-audit-prep` for the method. Human review point: counsel reviews results before they go to leadership.

9. **Document and hand off.** For every change, record the old rule, the new rule, the job-related reason, the source, and who approved it. Name the program owner for each program.

## Where AI helps and where it stops

| Task | AI role | Human owner |
|---|---|---|
| Neutral summary of current federal guidance with links | Summarize | Counsel |
| Program inventory and eligibility table | Draft | Program owners |
| Program eligibility against the access checklist | Check against a rubric | Counsel |
| Job posting or program description rewrite | Draft | Posting or program owner |
| Structured interview questions and rating scale | Draft | Hiring manager and TA lead |
| Accommodation request intake | Route | Accommodation owner |
| Accommodation decision for a named person | None | Accommodation owner, with counsel where needed |
| Training content review | Check against a rubric | Content owner and counsel |
| Aggregate process audit results | Summarize | Program owner, reviewed by counsel |
| Selection or eligibility decision about a named person | None | Decision owner |

## Guardrails

- **Neutral and sourced.** State what a primary source says, with its link. No political commentary, no characterizing the policy, and no prediction of enforcement. Agency technical assistance can be non-binding; say so where the source says so.
- **Bias and fairness.** Check both explicit criteria and neutral criteria that may act as proxies. Disparate impact claims remain possible; see the US federal AI enforcement context in `03-governance/README.md` and run `fairness-audit-prep` for any scoring or ranking tool.
- **Disability and health data.** Never infer disability or a health condition from any data; it is a prohibited use in `ai-use-policy.md`. Medical documentation stays in the accommodation process and out of AI tools not approved for it.
- **Data minimization.** Work from program rules and aggregate counts. Do not paste individual demographic records into an AI tool.
- **Legal review triggers.** Any program limited by a protected characteristic, any federal contract or funding certification, any demographic analysis, any accommodation dispute, and any non-US jurisdiction. For jurisdiction-specific dates, check the Key dates for HR table in `03-governance/README.md` and involve counsel.
- **Employee notice.** Tell employees when AI is used in a process that affects them, per `ai-use-policy.md` principle 2, and publish how to request an accommodation in every process.

## Output format

```
## Scope
[jurisdictions, federal contractor or funding Y/N, programs in scope, counsel]

## Primary sources reviewed
| Source | What it says (neutral summary) | Link | Applies here? (counsel) |

## Program access review
| Program | Eligibility as written | As practiced | Open to all eligible Y/N | Possible proxy criteria | Question for counsel |

## Selection criteria
| Process step | Criterion | Job-related reason | Applied consistently? | Tool that scores or ranks Y/N |

## Accommodation path
[how to ask, who receives it, response time target, documentation rule, owner]

## Language changes
| Document | Current text | Proposed text | Reason |

## Next step owner
[program owner, accommodation owner, counsel, and what each must decide]
```

## What this skill will not do

- Give a legal opinion on whether a program is lawful.
- Make an employment decision about a named person, including any accommodation, selection, or eligibility decision.
- Write to an ATS, LMS, HRIS, or accommodation case system.
- Process real employee or candidate data in examples. Examples use synthetic data only.
- Infer anyone's disability, health condition, or protected characteristic.
- Offer political commentary on the policy changes it summarizes.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. Executive Order 14173, Ending Illegal Discrimination and Restoring Merit-Based Opportunity, Federal Register, published 31 January 2025. https://www.federalregister.gov/documents/2025/01/31/2025-02097/ending-illegal-discrimination-and-restoring-merit-based-opportunity. Supports: revocation of EO 11246, contract and grant terms, private sector direction.
2. OFCCP final rule rescinding the regulations implementing Executive Order 11246, Federal Register, document 2026-17114. https://www.federalregister.gov/documents/full_text/html/2026/08/21/2026-17114.html. Supports: rescission of the EO 11246 implementing regulations.
3. What You Should Know About DEI-Related Discrimination at Work, U.S. Equal Employment Opportunity Commission. https://www.eeoc.gov/wysk/what-you-should-know-about-dei-related-discrimination-work. Supports: DEI not defined in Title VII, examples including ERG limits and segregated training, training and hostile environment, retaliation for opposing training.
4. Reminder of Title VII Obligations Related to DEI Initiatives, U.S. Equal Employment Opportunity Commission, 26 February 2026. https://www.eeoc.gov/reminder-title-vii-obligations-related-dei-initiatives. Supports: letter to large employers, programs under other names, guidance described as non-binding.
5. Guidance for Recipients of Federal Funding Regarding Unlawful Discrimination, U.S. Department of Justice, Office of the Attorney General, 29 July 2025. https://www.justice.gov/ag/media/1409486/dl. Supports: proxy criteria examples, non-binding best practices on open access, skills-based criteria, documenting rationale.
6. Enforcement Guidance on Reasonable Accommodation and Undue Hardship under the ADA, U.S. Equal Employment Opportunity Commission. https://www.eeoc.gov/laws/guidance/enforcement-guidance-reasonable-accommodation-and-undue-hardship-under-ada. Supports: plain-language requests, interactive process, documentation limits, applicants, pre-offer inquiries.
7. Retaliation, U.S. Equal Employment Opportunity Commission. https://www.eeoc.gov/retaliation. Supports: accommodation requests as protected activity, coverage thresholds.
8. Structured Interviews, U.S. Office of Personnel Management. https://www.opm.gov/policy-data-oversight/assessment-and-selection/structured-interviews/. Supports: same questions, same order, one rating scale.
9. Fair selection: an evidence review, practice summary, CIPD, April 2023. https://www.cipd.org/globalassets/media/knowledge/knowledge-hub/evidence-reviews/2023-pdfs/fair-selection-evidence-practice-summary_tcm18-114569.pdf. Supports: job-related selection measures, explaining stages and decisions to candidates.
10. SHRM's BEAM Framework for Inclusion: Aligning Merit with Organizational Excellence, SHRM, 31 January 2025. https://shrm.org/topics-tools/news/inclusion-diversity/shrms-beam-framework-for-inclusion-aligning-merit-with-organizational-excellence. Supports: programs open to all, job-related qualifications, broad and accessible communication.
</content>
</invoke>
