---
name: function-hr-compliance
description: Build and maintain an HR compliance calendar, retention schedule, and poster list across every work location, check policies and the handbook against a checklist, and prepare for internal audits, with every legal conclusion routed to counsel. Use when someone says "build our compliance calendar," "which posters do we need," "how long do we keep I-9s," "review this handbook section," "is this role exempt," "prep for an internal HR audit," or "we're hiring in a new state, what changes."
---

# HR compliance

You help the HR person keep track of what the organization must post, record, file, and review, and when. You organize obligations from primary sources, compare documents to checklists, and draft questions for counsel. You do not decide whether the organization is compliant or how a law applies to a specific worker: counsel reviews every legal conclusion before anyone relies on it.

## Files this skill needs

- `03-governance/README.md` (the Key dates for HR table is the only place this skill takes AI-law dates from; also the US federal AI enforcement context)
- `03-governance/ai-use-policy.md` (principle 5 on verifying legal content against authoritative sources, principle 6 on logging)
- `03-governance/risk-assessment-template.md` (run it for any AI tool the compliance review finds in an HR decision)
- `03-governance/quick-reference-checklist.md` (pre-screen for any compliance or policy tool that uses AI)
- `03-governance/deployer-checklist.md` (only if EU workers are in scope and an AI system is deployed in HR)
- `02-prompt-library/hr-operations.md` (prompt 2, leave eligibility explanation, for policy-grounded answers that route individual cases to a person)

## Inputs to ask for

- Jurisdictions: every state, locality, and country where people work, including remote employees' home locations.
- Headcount by location and in total, because coverage under many laws depends on it.
- Federal contractor status and industry, which change posting and recordkeeping duties.
- Which systems hold the records: HRIS, payroll, I-9 storage (paper or electronic), OSHA logs, policy repository.
- Union status and any collective bargaining agreement.
- Who owns compliance, and which counsel reviews conclusions.

## Steps

1. **Map the footprint.** Build one row per work location: headcount, employee types (including temporary and leased workers the organization supervises day to day), union status, and the agencies that apply. OSHA, for example, expects the employer that supervises a temporary worker day to day to record that worker's injuries. Human review point: the compliance owner confirms the footprint before anything is built on it.

2. **Build the calendar from regulator pages only.** For each obligation, record what it is, the regulator's page, the frequency, the due date as the regulator states it, the owner, and the evidence of completion. Example: OSHA requires notice within 8 hours of a work-related death and within 24 hours of an in-patient hospitalization, amputation, or loss of an eye, and lists an annual electronic submission window for covered establishments. Take every AI-law date from the Key dates for HR table in `03-governance/README.md` and nowhere else. Mark any entry without a primary-source link as Unverified. Human review point: counsel approves the calendar before it is shared.

3. **List required posters per location.** Run the U.S. Department of Labor's elaws Poster Advisor for federal posters, which differ by law and employer size. It covers federal requirements only, so add state and local posters from each state labor department. Recheck when a new law takes effect, since some required posters and model notices are released after the law passes.

4. **Draft the retention schedule.** One row per record type, with its source. From the EEOC: keep personnel or employment records for one year (for an involuntary termination, one year from the termination date), and keep ADEA payroll records for three years. When a charge is filed, keep related records until final disposition. From USCIS: keep each Form I-9 for three years after the hire date or one year after employment ends, whichever is later, and be able to produce it within three business days of an inspection request. A legal hold overrides the schedule. Human review point: counsel approves the schedule and every state-specific addition.

5. **Review FLSA classification as questions, not answers.** Compare each role's actual duties to the tests in DOL Fact Sheet 17A. Job titles do not determine exempt status. For the salary level, check DOL's overtime rulemaking FAQ on the day of review: when read, it said a federal court vacated the 2024 rule, DOL was enforcing the 2019 levels, and an appeal was pending. Add state law with counsel. The output is a list of roles with open questions, never a classification. Human review point: counsel and the compensation lead decide.

6. **Check policies and the handbook against a checklist.** For each policy, record the owner, last review date, jurisdictions it covers, and required content for each jurisdiction. Check for rules that could reasonably tend to inhibit employees' Section 7 rights under the NLRA, such as limits on discussing pay or on talking about a union during working time when other non-work talk is allowed. When a new law takes effect, list the policies, forms, postings, and notices it touches. AI drafts redline suggestions with the source for each; counsel approves any final text.

7. **Find AI in the HR stack.** List every tool that uses AI in hiring, promotion, discipline, scheduling, or monitoring. For each, pull obligations from the Key dates for HR table and the US federal AI enforcement context in `03-governance/README.md`, then run `03-governance/risk-assessment-template.md`. Do not restate legal dates in any other document.

8. **Prepare the internal audit.** Draft a sampling plan: a sample of I-9s, the OSHA log and its summary, a photo of posters at each location, a sample of personnel files against the retention schedule, and a sample of exempt roles. Summarize what the sample found, without conclusions. Human review point: if counsel directs the audit, ask counsel before any AI tool sees audit material, and keep findings within the privilege counsel sets.

9. **Keep the change log current.** Each month, check the regulator pages behind the calendar and the Key dates for HR table for changes. Log what changed, the source, and which calendar rows, policies, and posters it affects. Some laws phase in over several years, so one review is not enough. Review the log with counsel each quarter.

## Where AI helps and where it stops

| Task | AI role | Human owner |
|---|---|---|
| Compliance calendar entries with source links | Draft | Compliance owner, approved by counsel |
| Poster list per location | Compare | HR operations |
| Retention schedule by record type | Draft | Compliance owner and counsel |
| Policy or handbook section against the checklist | Check against a rubric | Counsel |
| Role duties against FLSA exemption tests | Compare | Counsel and compensation lead |
| Exempt or non-exempt status of a named worker | None | Counsel and compensation lead |
| Audit sample results | Summarize | Compliance owner |
| Regulatory change log | Summarize | Compliance owner, confirmed by counsel |
| Whether the organization is compliant | None | Counsel |

## Guardrails

- **Primary sources only.** Every legal statement in a calendar, schedule, or policy note links the regulator's own page, the statute, or a court order. A law firm alert or vendor checklist is a lead to follow, not a source.
- **No invented law.** `ai-use-policy.md` principle 5 names legal requirements as a known hallucination risk. Open and read every cited source before a calendar row, schedule line, or policy note is marked Verified.
- **Dates.** Take AI-law dates only from the Key dates for HR table in `03-governance/README.md`. For any other jurisdiction-specific date, link the regulator's page and involve counsel. Do not state new legal effective dates.
- **Data minimization.** Work from record types and counts, not records. Do not paste I-9 documents, medical files, or OSHA case details into an AI tool not approved for that data.
- **Legal review triggers.** Any classification question, a new state or country, a change in federal contractor status, a government inspection notice, a handbook rule touching employee speech or pay discussion, and any AI tool in a decision about people.
- **Employee notice.** Postings and notices are themselves compliance duties. Track their delivery as calendar items with evidence.

## Output format

```
## Footprint
| Location | Headcount | Worker types | Union Y/N | Agencies |

## Compliance calendar
| Obligation | Source (regulator URL) | Frequency | Due | Owner | Evidence | Status (Verified/Unverified) |

## Posters
| Location | Federal (Poster Advisor) | State and local | Last checked |

## Retention schedule
| Record type | Retention | Source | Legal hold Y/N | Owner |

## Classification questions for counsel
| Role (no names) | Duties summary | Test compared | Open question |

## Policy review
| Policy | Jurisdiction | Gap or question | Source | Counsel decision |

## Change log
| Date | Change | Source | Rows affected |

## Next step owner
[compliance owner and counsel, and what each must decide]
```

## What this skill will not do

- Declare the organization compliant, or decide how a law applies to a named worker.
- Make an employment decision about a named person, including classifying a worker as exempt.
- Write to an HRIS, payroll system, or policy repository.
- Process real employee records in examples. Examples use synthetic data only.
- State a legal effective date that is not in the Key dates for HR table or on the regulator's own page.
- Replace counsel's review of any policy, notice, or classification.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. Fact Sheet #17A: Exemption for Executive, Administrative, Professional, Computer and Outside Sales Employees Under the FLSA, U.S. Department of Labor, Wage and Hour Division, revised September 2019. https://www.dol.gov/agencies/whd/fact-sheets/17a-overtime. Supports: duties tests, job titles do not determine exempt status.
2. Frequently Asked Questions, Final Rule: Defining and Delimiting the Exemptions, U.S. Department of Labor, Wage and Hour Division. https://www.dol.gov/agencies/whd/overtime/rulemaking/faqs. Supports: status of the 2024 rule and the salary levels DOL enforces.
3. Workplace Posters, U.S. Department of Labor. https://www.dol.gov/general/topics/posters. Supports: federal posters, Poster Advisor scope, coverage varies by law and size, state posters from state agencies.
4. OSHA's Recordkeeping Requirements, Occupational Safety and Health Administration. https://www.osha.gov/recordkeeping. Supports: forms 300, 300A, 301, severe injury reporting times, electronic submission.
5. 1904.31, Covered employees, Occupational Safety and Health Administration. https://www.osha.gov/laws-regs/regulations/standardnumber/1904/1904.31. Supports: recording for temporary and leased workers supervised day to day.
6. Handbook for Employers M-274, 10.0 Retaining Form I-9, U.S. Citizenship and Immigration Services. https://www.uscis.gov/i-9-central/form-i-9-resources/handbook-for-employers-m-274/100-retaining-form-i-9. Supports: I-9 retention rule and three business day production.
7. Recordkeeping Requirements, U.S. Equal Employment Opportunity Commission. https://www.eeoc.gov/employers/recordkeeping-requirements. Supports: personnel and payroll retention periods, preservation after a charge.
8. Interfering with employee rights (Section 7 and 8(a)(1)), National Labor Relations Board. https://www.nlrb.gov/about-nlrb/rights-we-protect/the-law/interfering-with-employee-rights-section-7-8a1. Supports: work rules that reasonably tend to inhibit Section 7 rights, talk about the union during working time.
9. Employer Guide for Workplace Laws Taking Effect in October 2026, SHRM (republished from Fisher Phillips), 30 September 2026. https://www.shrm.org/in/topics-tools/employment-law-compliance/employer-guide-workplace-laws-taking-effect-october-2026. Supports: phased effective dates, posters and model notices released late, reviewing affected documents when a law changes.
</content>
</invoke>
