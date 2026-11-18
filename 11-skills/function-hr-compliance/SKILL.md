---
name: function-hr-compliance
description: Drafts an HR compliance calendar, poster list, and record retention schedule for every work location from regulator pages, checks policies and the handbook against a checklist, lists FLSA classification questions, inventories AI tools in HR decisions with their notice duties, and prepares internal audit sampling plans, with every legal conclusion routed to counsel. Use whenever someone says "build our compliance calendar," "which posters do we need," "how long do we keep I-9s," "review this handbook section," "is this role exempt," "prep for an internal HR audit," "we're hiring in a new state, what changes," "what changed this month," or "do we need a notice for our AI screening tool," and whenever a new location, a government inspection notice, or a new HR AI tool appears.
---

# HR compliance

This skill serves the HR compliance owner. It produces a footprint, a calendar, a poster list, a retention schedule, classification questions, a policy review, an AI notice check, an audit sampling plan, and a change log, each traced to a primary source. It does not decide whether the organization is compliant or how a law applies to a worker: counsel reviews every legal conclusion before anyone relies on it.

## Files this skill needs

- `03-governance/README.md` (the Key dates for HR table is the only place this skill takes AI-law dates from; also the US federal AI enforcement context)
- `03-governance/ai-use-policy.md` (principle 5 on verifying legal content against authoritative sources, principle 6 on logging)
- `03-governance/risk-assessment-template.md` (run it for any AI tool found in an HR decision)
- `03-governance/quick-reference-checklist.md` (pre-screen for any compliance or policy tool that uses AI)
- `03-governance/deployer-checklist.md` (only if EU workers are in scope and an AI system is deployed in HR)
- `02-prompt-library/hr-operations.md` (prompt 2, leave eligibility explanation, which routes individual cases to a person)
- `11-skills/fairness-audit-prep/SKILL.md` (any AI tool found that scores, ranks, or filters people)

## Inputs

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| Every work location, including remote employees' home locations | Yes | HRIS, read-only: work location, employment type, headcount by location | California 410, Illinois 220, NYC 180, Colorado 150, Germany 440 |
| Headcount by location and in total | Yes | HRIS, read-only: counts only | 1,400 total |
| Temporary and leased workers supervised day to day | Yes | Ask the user | 35 contractors in Denver |
| Federal contractor status and industry | Yes | Ask the user | Not a federal contractor; software |
| Systems holding records | Yes | Ask the user | HRIS, payroll, electronic I-9 system, OSHA log, policy repository |
| Union status and any collective bargaining agreement | Yes | Ask the user | None in the US; works council in Germany |
| AI tools in hiring, promotion, discipline, scheduling, or monitoring | For step 7 | Governance inventory, read-only: tool, use, locations | ATS resume screening feature |
| Compliance owner and reviewing counsel | Yes | Ask the user | HR compliance manager; outside employment counsel |

If a required input is missing, ask for it once, in one short question at the top of your reply. Then proceed with the gap labeled "Not provided: [input]" and mark every row that depends on it Unverified.

## Tools and connectors

An agent may read, never write. Use MCP connectors or exports with read-only scopes and these fields only:

- **HRIS:** work location, employment type, FLSA status flag, job code, and job title, as counts or role-level rows with no names.
- **Payroll export:** record types and counts, for the retention schedule.
- **I-9 system:** form counts by hire year and termination year. Never the documents.
- **OSHA log:** case counts by establishment and form status. Never case details.
- **Policy repository:** policy ID, owner, last review date, jurisdictions, text.
- **Regulator pages:** a read-only web fetch of the regulator's own page, recorded with the date read.
- **Repo MCP tool:** `policy_qa` (`ask_governance_policy`) returns cited passages from `03-governance/`, including the Key dates for HR table. If it returns `no_match: true`, report no source, not a guess.

Rules for every tool call:

- Never call a write, send, update, publish, or file tool, even if the connector offers one.
- Log each call in the Audit trail: tool, purpose, fields read.
- If a tool returns data on named people, document images, or fields outside this list, stop, do not use it, and ask the user.

## By maturity stage

Stages follow the repo's maturity scale in [the roadmap template](../../06-roadmap/transformation-roadmap-template.md). Decision rights in this skill are the same at every stage.

| Stage | How to run it | Before moving up |
|---|---|---|
| Start (Levels 0 to 1) | Paste headcount by location, worker types, record types, and dated regulator page excerpts. The compliance owner opens every source link. | Counsel approves the calendar; unsourced rows stay Unverified. |
| Pilot (Level 2) | One scheduled read-only HRIS export (work location, employment type, headcount). The compliance owner tracks verified calendar coverage and samples rows weekly. | Counsel's quarterly check reviews the monthly change log. |
| Scale (Level 3) | Read-only HRIS, policy repository, regulator page fetch, and `policy_qa`, calls logged; monthly change log on schedule. Track on-time completion and AI notice coverage. | Notice confirmed for every inventoried HR AI tool. |
| Embed (Levels 4 to 5) | A new work location, inventoried AI tool, or inspection notice triggers a draft update. Counsel approves every legal row and any privileged audit use. | Rerun the test cases in `evals/` when the skill or model changes. |

## Steps

1. **Map the footprint.** One row per work location: headcount, worker types (including temporary and leased workers the organization supervises day to day), union status, and the agencies that apply. OSHA expects the employer that supervises a temporary worker day to day to record that worker's injuries. Sign-off: compliance owner confirms the footprint before anything is built on it.

2. **Build the calendar from regulator pages only.** For each obligation record what it is, the regulator's page, the frequency, the due date as the regulator states it, the owner, and the evidence of completion. Example: OSHA requires notice within 8 hours of a work-related death and within 24 hours of an in-patient hospitalization, amputation, or loss of an eye, and lists an annual electronic submission window for covered establishments. Take every AI-law date from the Key dates for HR table and nowhere else. Mark any row without a primary-source link as Unverified. To check that no area is missing, walk this category list: payroll and year-end tax forms, benefit plan limits, health coverage reporting and continuation, leave, remote work expenses, workers' compensation, system access, personnel records, pay transparency, minimum wage, and agency reporting. Confirm completion of last year's required training and schedule next year's. A vendor checklist can suggest categories; dates still come from the regulator. Sign-off: counsel approves the calendar before it is shared.

3. **List required posters per location.** Run the U.S. Department of Labor's elaws Poster Advisor for federal posters, which differ by law and employer size. It covers federal requirements only, so add state and local posters from each state labor department. Recheck when a new law takes effect, since some required posters and model notices are released after the law passes. Sign-off: HR operations confirms posting, with a dated photo per location as evidence.

4. **Draft the retention schedule.** One row per record type, with its source. From the EEOC: keep personnel or employment records for one year (for an involuntary termination, one year from the termination date), and keep ADEA payroll records for three years. When a charge is filed, keep related records until final disposition. From USCIS: keep each Form I-9 for three years after the hire date or one year after employment ends, whichever is later, and be able to produce it within three business days of an inspection request. A legal hold overrides the schedule. Where a Key dates row sets a retention duty for automated-decision data, add a row and take the period from that row. Sign-off: counsel approves the schedule and every state-specific addition.

5. **Review FLSA classification as questions, not answers.** Compare each role's actual duties to the tests in DOL Fact Sheet 17A. Job titles do not determine exempt status. For the salary level, check DOL's overtime rulemaking FAQ on the day of review: when read, it said a federal court vacated the 2024 rule, DOL was enforcing the 2019 levels, and an appeal was pending. Add state law with counsel. Work at role level with no names. The output is a list of roles with open questions, never a classification. Sign-off: counsel and the compensation lead decide.

6. **Check policies and the handbook against a checklist.** For each policy record the owner, last review date, jurisdictions covered, and required content per jurisdiction. Check for rules that could reasonably tend to inhibit employees' Section 7 rights under the NLRA, such as limits on discussing pay, or on talking about a union during working time when other non-work talk is allowed. When a new law takes effect, list the policies, forms, postings, and notices it touches. Draft redline suggestions with the source for each. Sign-off: counsel approves any final text.

7. **Find AI in the HR stack and check notice and fairness.** List every tool that uses AI in hiring, promotion, discipline, scheduling, or monitoring. For each, pull obligations from the Key dates for HR table and the US federal AI enforcement context, then run `03-governance/risk-assessment-template.md`. Route any such tool used on EU staff to `eu-ai-act-hr-classifier` and counsel by name. Do not restate legal dates. Check that:
   - The AI use policy names hiring and employment decisions, and candidate notices are confirmed before any AI screening starts.
   - The notice says AI is in use, how it affects the decision, how to see and correct the data used, and how to reach a human reviewer. Counsel decides what a given law requires.
   - The vendor has answered how the tool works, how it is audited, and its record on bias. A vendor's assurance does not replace your own review, and a vendor that will not explain is a reason to stop.
   - Any tool that scores, ranks, or filters people has an adverse impact plan from `11-skills/fairness-audit-prep/SKILL.md`. The four-fifths ratio is a screening flag under the Uniform Guidelines, [29 CFR 1607.4(D)](https://www.govinfo.gov/content/pkg/CFR-2024-title29-vol4/pdf/CFR-2024-title29-vol4-sec1607-4.pdf), not a safe harbor or a verdict; small groups need a statistical test, and People Analytics or counsel interprets it. Bias audits cover age and disability as well as race and sex, and there is a route for accommodation requests.
   - Where EU work is in scope, freelancers and platform workers are listed too. The Commission's draft guidelines (non-binding) include them, and note that a use appearing as an example does not make it lawful.

   Sign-off: compliance owner, with counsel for every notice.

8. **Prepare the internal audit.** Draft a sampling plan: a sample of I-9s, the OSHA log and its summary, a dated photo of posters at each location, a sample of personnel files against the retention schedule, and a sample of exempt roles. Summarize the sample with counts and no conclusions. Sign-off: if counsel directs the audit, ask counsel before any AI tool sees audit material, and keep findings within the privilege counsel sets.

9. **Run the change log as an agentic workflow with checkpoints.** Monthly: the agent reads each regulator page behind the calendar and the Key dates for HR table, compares it to the last recorded read, and drafts a change log entry with the source and the calendar rows, policies, and posters affected. Checkpoint 1: the compliance owner confirms each entry before any row changes status. Checkpoint 2: counsel reviews the log each quarter. Some laws phase in over several years, so one review is not enough. Sign-off: compliance owner monthly; counsel quarterly.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Draft the footprint from location counts | Compliance owner | Drafts for sign-off |
| Draft calendar rows with regulator links | Compliance owner, approved by counsel | Drafts for sign-off |
| Mark a row Unverified when no primary source is linked | Fixed rule | Does alone |
| Draft the poster list per location | HR operations | Drafts for sign-off |
| Draft the retention schedule | Compliance owner and counsel | Drafts for sign-off |
| Compare role duties to FLSA exemption tests | Counsel and compensation lead | Drafts for sign-off |
| Classify a named worker as exempt or non-exempt | Counsel and compensation lead | Refuses and routes |
| Check a policy against the checklist and draft redlines | Counsel | Drafts for sign-off |
| Summarize audit sample results | Compliance owner | Drafts for sign-off |
| Draft a regulatory change log entry | Compliance owner, confirmed by counsel | Drafts for sign-off |
| Declare the organization compliant | Counsel | Refuses and routes |
| Publish a policy, post a notice, or file with an agency | Compliance owner | Refuses and routes |

### Refuse and route

- "Confirm we're compliant in Colorado": refuse; route to counsel with the calendar and its Unverified rows.
- "Is Dana Ruiz exempt?": refuse to classify a named person; route to counsel and the compensation lead with role-level duty questions.
- "Update the handbook in the policy repository" or "send the new notice to all staff": refuse to write or send; route the redline or notice draft to the compliance owner.
- "Paste these I-9s and medical files so you can check them": refuse; route to the compliance owner to supply counts and record types only.
- "What's the effective date of the new state AI law?" when it is not in the Key dates table: refuse to state one; route to counsel and to the table's maintainer.
- "Add a rule that staff may not discuss pay": refuse to draft it; route to counsel with the NLRA Section 7 source.
- "Run the privileged audit on these files": refuse until counsel confirms in writing that AI may see the material.
- A request to process real employee records in an example: refuse; ask for a synthetic version.

## Guardrails

- **Primary sources only.** Every legal statement links the regulator's own page, the statute, or a court order. A law firm alert or vendor checklist is a lead to follow, not a source.
- **No invented law.** `ai-use-policy.md` principle 5 names legal requirements as a known hallucination risk. Open and read every cited source before a row is marked Verified. Take AI-law dates only from the Key dates for HR table, and link the regulator's page for any other jurisdiction-specific date.
- **Fairness and adverse impact.** Any AI tool found in a selection decision needs an adverse impact plan before the calendar treats it as covered. A shift in federal enforcement emphasis does not remove state and private exposure; see the US federal AI enforcement context.
- **Explainability and notice.** Track delivery of postings and notices as calendar items with evidence, and check AI notices against the four contents in step 7.
- **Privacy and minimization.** Work from record types and counts, not records. Do not put I-9 documents, medical files, or OSHA case details into an AI tool not approved for that data.
- **Legal review triggers.** Any classification question, a new state or country, a change in federal contractor status, a government inspection notice, a handbook rule touching employee speech or pay discussion, and any AI tool in a decision about people.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| California FEHA automated-decision system regulations | An automated tool is used in hiring or employment for California staff | Adds an automated-decision data row to the retention schedule, period from the Key dates row |
| Illinois HB 3773 (Public Act 103-0804) | AI is used in hiring, promotion, discipline, or discharge for Illinois staff | Adds an employee notice row to the calendar with evidence of delivery |
| NYC Local Law 144 | A tool in NYC hiring or promotion may be a covered AEDT | Adds bias audit, public summary, and notice rows; counsel confirms coverage |
| Colorado SB 26-189 (ADMT Act) | Automated technology is used in an employment decision for Colorado staff | Adds notice and adverse-decision explanation rows, Unverified until counsel checks enforcement status |
| EU Pay Transparency Directive | Staff work in an EU country | Adds a row to check national law status in each country, owned by counsel |
| OFCCP final rule rescinding the EO 11246 regulations | The footprint shows federal contractor status | Marks contractor rows built on those regulations Unverified for counsel to recheck |

Counsel confirms scope and current status before you rely on any row. In your reply, name each rule as: see the Key dates row "exact row name" in `03-governance/README.md`. Stop there: do not write the row's dates, status or regulation numbers, even ones you read in the table or in Sources, because the table is the one place they are kept current.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| Verified calendar coverage | Calendar rows marked Verified (primary source opened and read, counsel approved) divided by all calendar rows, at month end | Shows how much of the calendar the organization can defend |
| On-time obligation completion | Obligations completed with evidence on or before the due date, divided by obligations due in the quarter | The outcome the calendar exists for |
| AI notice coverage | AI tools used in hiring, promotion, discipline, scheduling, or monitoring with a confirmed notice and human review route, divided by all such tools in the inventory, per quarter | Shows whether affected workers and candidates are told and can reach a person |

## Output format

```
## Footprint
| Location | Headcount | Worker types | Union Y/N | Agencies |
Gaps: Not provided: ...

## Compliance calendar
| Obligation | Source (regulator URL, date read) | Frequency | Due | Owner | Evidence | Status (Verified/Unverified) |

## Posters
| Location | Federal (Poster Advisor) | State and local | Last checked |

## Retention schedule
| Record type | Retention | Source | Legal hold Y/N | Owner |

## Classification questions for counsel
| Role (no names) | Duties summary | Test compared | Open question |

## Policy review
| Policy | Jurisdiction | Gap or question | Source | Counsel decision |

## AI tools in HR decisions
| Tool | Decision stage | Key dates rows | Notice confirmed | Adverse impact plan | Open question |

## Change log
| Date | Change | Source | Rows affected | Confirmed by |

## Decision rights calls in this output
| Item | Agent role | Routed to |

## Metrics
| Metric | Baseline | Owner |

## Audit trail
Inputs used:
Tools called (tool, purpose, fields read):
Items needing sign-off (item, owner):
Open legal questions:
```

## Worked example

Harbor & Pine, a fictional 1,400-person company, opens a Denver office and asks for a calendar update, posters, and a check of its AI resume screening feature. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They were run on 18 November 2026 with `claude-sonnet-5-5`, one fresh session per case, and graded in a separate pass; see [the results](../../09-evals/skill-eval-results-2026-11-18.md) for the method and its limits.

- `new-state-calendar-update`: adds a new location to the calendar, posters, and retention schedule.
- `ai-notice-check-missing-sources`: checks AI tool notices across US locations and Germany with vendor answers missing.
- `declare-exempt-and-compliant`: a request to classify named workers and declare compliance, to refuse and route.

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
10. AI in the Workplace Playbook, SHRM, 2025. Read from a copy of the publication; no web address checked. Supports: not relying on vendors for compliance, vendor questions on algorithm, audits, and bias record, bias audits that include age and disability, accommodations.
11. 2027 Compliance Checklist, Rippling, updated September 2026. Read from a copy of the publication; no web address checked. Supports (vendor-published; practice points only, not a legal source): year-end category list, training completion check, AI policy naming employment decisions, confirming candidate notices.
12. Draft guidelines on the classification of high-risk AI systems, European Commission, consultation drafts (non-binding). Read from a copy of the publication; no web address checked. Supports: freelancers and platform workers in scope of the employment use cases; an example listing does not make a use lawful. Draft guidance only; counsel confirms.
13. Workday's Vision for AI Governance, Workday, 2026. Read from a copy of the publication; no web address checked. Supports (vendor-published, one viewpoint): the contents checklist for an AI notice.
