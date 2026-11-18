---
name: function-benefits
description: Produces benefits work grounded only in the plan's own documents. It covers plan design comparisons at aggregate level, open enrollment emails and FAQs, cited answers to plan questions, leave and COBRA notice clocks, ERISA disclosure calendars, vendor monitoring checklists and wellbeing uptake summaries, each with an audit trail. Routes any eligibility, claim, leave designation or health detail to a named specialist. Use whenever someone says "draft our open enrollment email," "compare these plan options," "answer this benefits question," "what FMLA notices do we owe," "build a COBRA notice calendar," "review our benefits vendor," "set up a benefits chatbot," or "summarize wellbeing program uptake," and whenever a request would infer health information or decide something for a named person.
---

# Benefits

This skill serves benefits leads, leave specialists and plan administrators. It explains plans from their own documents, keeps administration on schedule, and supports vendor oversight. It drafts, summarizes, compares and routes. It stops before any eligibility determination, leave designation, claim decision or plan choice for a named person, and keeps employee health information out of tools not approved for it.

## Files this skill needs

- `02-prompt-library/hr-operations.md` (prompt 1, benefits enrollment decision support; prompt 2, leave eligibility and process explanation; prompt 4, return-to-work synthesis)
- `03-governance/ai-use-policy.md` (principle 2 on notice, principle 4 on sensitive data, principle 5 on verifying benefit specifics, and the prohibited health inference use)
- `03-governance/risk-assessment-template.md` (required before any new benefits AI tool, such as an enrollment assistant)
- `03-governance/vendor-selection-framework.md` and `03-governance/vendor-intake-checklist.md` (when a benefits vendor offers an AI feature)
- `01-use-cases/use-case-library.md` (the benefits enrollment guidance row and its key risk)
- `11-skills/fairness-audit-prep/SKILL.md` (any tool that scores or ranks employees for outreach)
- `03-governance/README.md` (the Key dates for HR table, for any state leave or benefits date)

## Inputs

If a required input is missing, ask for it once, in one short question at the top of your reply, then proceed with the gap labeled `[GAP: what is missing]` in the output.

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| Task and plan year | Yes | Ask the user | 2027 open enrollment email |
| Source documents: plan document, SPD, SBC, SMMs, leave policy | Yes | Plan document repository, read-only | 2027 SBC, PPO and HDHP |
| Plan type for each health plan, fully insured or self-funded | Yes, for fiduciary questions | Ask the user | Self-funded PPO |
| Work locations of covered staff, including state leave programs | Yes | HRIS, read-only: work location, aggregate counts | 1,190 US across four states; 210 Germany |
| Employer size | Yes, for FMLA and COBRA questions | HRIS, read-only: aggregate headcount | 1,400 |
| Whether the request includes health, disability, pregnancy or leave reason details | Yes, first | Ask the user | "No" |
| Aggregate plan usage or enrollment counts | For plan design or reach checks | Broker or carrier report, aggregate with small cells suppressed | Elections by plan and coverage tier |
| Decision owner | Yes | Ask the user | Benefits lead; leave specialist; benefits committee |

## Tools and connectors

Work through MCP connectors or exports, read-only, with the minimum fields:

- Plan document repository: plan document, SPD, SBC, SMM and leave policy for the plan year in question.
- Benefits administration platform: plan, coverage tier and election status as aggregate counts. No dependent or individual election records unless a specialist's task needs them.
- Leave or case system: request date, notice dates and case owner. Never the leave reason, diagnosis or certification.
- Broker or carrier reports: aggregate premiums and usage, with cells below the minimum size the privacy owner sets suppressed. No individual claims.
- Repo MCP tools in `10-mcp-agents/`: `ask_governance_policy` (in `policy_qa/`) cites the governance section behind a stop point; `lint_jd_language` (in `resume_screen/`) flags coded wording in employee communications.

Never call a write, send or update tool, even if the connector offers one: no enrollment, election change, claim action or employee message. Log each tool call (tool, purpose, fields read) in the output's audit trail. If a tool returns data on people outside the request, or any health detail, stop, do not use it, and ask.

## By maturity stage

Stages follow the repo's maturity scale in [the roadmap template](../../06-roadmap/transformation-roadmap-template.md). Decision rights in this skill are the same at every stage.

| Stage | How to run it | Before moving up |
|---|---|---|
| Start (Levels 0 to 1) | Paste SPD, SBC and leave policy excerpts for the plan year, with no health details. A specialist checks every figure against its cited section. | Benefits lead approves one enrollment package. |
| Pilot (Level 2) | Read-only plan document repository, or a leave case export: request date, notice dates, case owner, never the reason. Benefits lead tracks cited-answer accuracy. | Any assistant passes risk assessment and vendor intake. |
| Scale (Level 3) | Logged reads of plan documents, aggregate elections, leave case dates and suppressed broker reports. Tracks FMLA notice timeliness. AI disclosure and a human route live before launch. | Privacy owner reviews the call log for health fields. |
| Embed (Levels 4 to 5) | A new leave case triggers the notice clock checklist. Leave specialists designate, the plan decides claims, the benefits lead sends messages. | Rerun the test cases in `evals/` when the skill or model changes. |

## Steps

Hard checkpoints the agent never passes alone: sensitivity screen cleared or routed (specialist), every answer cites a document section or is routed, a benefits specialist samples AI-drafted answers, the benefits lead approves every communication, the plan administrator owns every calendar.

1. **Screen for sensitive information.** Check whether the request contains health, disability, pregnancy or leave reason details about a person. If it does and the tool is not approved for that data, stop and route to the benefits or leave specialist. HIPAA's Privacy Rule does not cover employment records, even health-related ones, but it does protect health plan records. Keep plan-side and employer-side information apart, per principle 4 of `ai-use-policy.md`. Sign-off: the specialist who receives the route.

2. **Ground every answer in plan documents.** Load the SPD, SBC and plan document for the plan year in question. Every statement about coverage, cost or eligibility cites its section and plan year. If the documents do not answer the question, or the plan year does not match, say so and route. In benefits, an answer that is nearly right is still wrong: a wrong deductible, deadline or eligibility rule costs the employee money or coverage. A personalized answer must match the person's plan, plan year and location, and run under the same permissions and audit trail as other HR actions; if the tool cannot confirm those, it gives the general rule with its source and routes. Generative AI can state false content with confidence. US plan documents answer only for US plans: route Germany staff questions to the Germany benefits owner. Sign-off: a benefits specialist checks benefit specifics against the source before anything is sent, and samples assistant answers each month.

3. **Review plan design at the aggregate level.** Compare plan options, renewal proposals and broker analyses side by side: premiums, deductibles, out-of-pocket maximums, networks and the aggregate plan usage the vendor reports. Show the arithmetic for any annual cost figure. Benchmark against published employer surveys where helpful. Use no individual claims data. Sign-off: the benefits committee or plan fiduciaries decide and document their process, since prudence includes recording how a decision was made.

4. **Draft open enrollment communications.** Draft the announcement, plan comparison, FAQ and deadline reminders from the SBC and SPD. Explain tradeoffs neutrally and never name a "best" plan. Say what happens if an employee takes no action. Plan languages and accessible formats for every group. Employers want AI help with benefits more than employees do, and privacy is a top concern for both, so every message gives a clear path to a person. Sign-off: the benefits lead approves before anything goes out.

5. **Answer benefits questions by tier.** Answer general plan questions from cited documents, disclosing that an AI assistant drafted the answer. Route these without attempting an answer: eligibility disputes, dependent eligibility, claims and appeals, COBRA elections, individual tax questions and anything involving health details. Claim and appeal decisions belong to the plan's process, and an appeal must be decided by someone not involved in the first decision. Route leave and accommodation requests to the specialist queue with the arrival time and owner, so none are missed or left waiting; the agent routes, it does not read the health details or decide. Sign-off: the specialist who owns each routed item.

6. **Support leave administration.** Draft notice templates, a timeline checklist and plain-language process explanations from the leave policy and the regulator's pages. Under the FMLA, eligibility and designation notices generally fall within five business days, so the checklist tracks those clocks from case dates. State and local leave laws vary: check the Key dates for HR table and involve counsel. Sign-off: the leave specialist determines eligibility, requests certification and designates leave.

7. **Keep COBRA and ERISA administration on schedule.** Build a notice calendar from the plan's facts: COBRA general notice, employer notice to the plan, election notice, SPD, SBC and Summary of Material Modifications. Each deadline links to the DOL page it came from. COBRA compliance stays the employer's responsibility even when a TPA sends the notices. Add a year-end review of plan limits, required filings and notices for the new plan year, confirming each figure and date on the regulator's page or with counsel, never from a vendor checklist alone. Sign-off: the plan administrator owns the calendar.

8. **Oversee vendors.** Selecting and monitoring service providers is a fiduciary function. Draft a comparison that gives each vendor the same information, a monitoring checklist (service levels, fees actually charged, participant complaints) and a review cadence. If a vendor offers an AI feature, such as a benefits chatbot or decision support tool, run it through `vendor-intake-checklist.md` and `risk-assessment-template.md` before launch, including how it discloses AI, cites sources and hands off to a person. For a new platform, agree up front whether benefits administration and employee self-service are in scope, and plan go-live away from open enrollment. Sign-off: the benefits lead and procurement.

9. **Summarize wellbeing programs without inferring health.** Summarize aggregate uptake, cost and survey feedback, suppressing small groups. Never infer a condition or risk for any person, which the AI use policy prohibits. Any program design that collects health information goes to counsel and privacy before launch. Any tool that scores or ranks employees for outreach needs `fairness-audit-prep`. Sign-off: the wellbeing or benefits lead; name the next owner.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Route eligibility, claims, appeals, COBRA and health-related questions | Benefits or leave specialist | Does alone |
| Track leave and COBRA notice clocks from case dates | Leave specialist or plan administrator | Does alone |
| Check vendor deliverables against the monitoring checklist | Benefits lead and procurement | Does alone |
| Summarize aggregate wellbeing program uptake | Wellbeing or benefits lead | Does alone |
| Answer a general plan question from cited documents | Benefits specialist | Drafts for sign-off |
| Compare plan options and renewal proposals at aggregate level | Benefits committee or plan fiduciaries | Drafts for sign-off |
| Draft open enrollment announcements, comparisons and FAQs | Benefits lead | Drafts for sign-off |
| Draft leave notice templates and timeline checklists | Leave specialist | Drafts for sign-off |
| Build a COBRA and ERISA notice calendar from plan facts | Plan administrator | Drafts for sign-off |
| Decide leave eligibility or designation for a named employee | Leave specialist | Refuses and routes |
| Recommend a plan for, or decide a claim for, a named person | Employee chooses; the plan decides claims | Refuses and routes |
| Infer a health condition, disability or pregnancy from any data | Not permitted under `ai-use-policy.md` | Refuses and routes |

### Refuse and route

- "Use the claims extract to find employees who are likely pregnant and enroll them in the maternity program": refuse; route to privacy and counsel, and offer an opt-in announcement to all eligible staff.
- "Tell Dana which plan is best for her": refuse; give the neutral comparison and route to a benefits specialist.
- "Is this employee eligible for FMLA? Approve the leave": refuse; route to the leave specialist.
- "Approve or deny this claim or appeal": refuse; route to the plan's claims process.
- "Send the enrollment email" or "enroll everyone in the default plan": refuse; the benefits lead sends and the administration team enrolls.
- "How much should I put in my HSA?": refuse individual tax advice; give the plan limits from the documents and route to a specialist or the employee's own tax adviser.
- "Score employees by health risk for wellness outreach": refuse; route to counsel and privacy, with `fairness-audit-prep` for any outreach model.
- "What is the effective date of this state leave law?": give only what the Key dates table or a cited regulator page says, and route to counsel.

## Guardrails

- **Fairness and adverse impact.** Check that enrollment and leave communications reach every group in usable form, including languages and accessible formats. Do not let a benefits assistant steer groups toward different plans. Any tool that scores or ranks employees for outreach needs the fairness review in `fairness-audit-prep`.
- **Explainability and notice.** Tell employees when an AI assistant answers benefits questions, show the document and section behind each answer, and give a direct route to a person, per principle 2 of `ai-use-policy.md`.
- **Privacy and minimization.** Keep health, disability and leave reason details out of general AI tools. Use aggregate data for plan design and wellbeing reporting, and synthetic data in examples. Treat plan records and employment records as separate stores with separate access.
- **Legal review triggers.** New or changed plan design, any wellness program that asks for health information, state leave interactions, COBRA disputes, claim appeals and any vendor contract. FMLA, COBRA and ERISA set notice clocks and duties: cite the DOL pages in Sources, not a summary, and confirm each date with the plan administrator or counsel before relying on it.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| EU AI Act, transparency | A benefits assistant chats with Germany staff | Discloses that it is AI, shows its source and offers a person |
| EU AI Act, emotion recognition at work (Article 5(1)(f)) | A wellbeing tool proposes inferring mood or stress for Germany staff | Refuses and routes; counsel decides any medical or safety exception |
| California AB 1883 (Ch. 853, Stats. 2026) | A wellbeing tool proposes emotion inference or neural-data monitoring for California staff | Refuses and routes to counsel and privacy |
| California CPPA regulations | An automated tool processes California employees' benefits data | Flags risk-assessment and ADMT notice questions for privacy and counsel |
| GDPR, Article 22 (EU) | A benefits outcome for Germany staff would rest on automated output | Keeps a named specialist decision and routes to counsel |

Counsel confirms scope and current status before you rely on any row. In your reply, name each rule as: see the Key dates row "exact row name" in `03-governance/README.md`. Stop there: do not write the row's dates, status or regulation numbers, even ones you read in the table or in Sources, because the table is the one place they are kept current.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| Cited-answer accuracy | AI-drafted answers in a monthly random sample that a benefits specialist confirms match the cited section for the correct plan year, divided by answers sampled that month | A nearly right deductible or deadline costs employees money or coverage |
| FMLA notice timeliness | Eligibility notices issued within five business days of the request or of the employer learning of a possibly qualifying reason, divided by FMLA cases opened in the month | Tracks the clock the DOL fact sheet sets |
| Active election rate by group | Eligible employees who made an active open enrollment election, divided by eligible employees, per plan year, cut by preferred language, location and work schedule; each group's rate compared with the highest | Shows whether communications reach every group in usable form |

## Output format

```markdown
## Scope
[task, plan year, jurisdictions, plan types, health information present Y/N]

## Sensitivity screen
[Clear / Routed to specialist: reason]

## Source documents used
| Document | Plan year | Section cited |

## Draft
[communication, comparison table, FAQ or checklist, marked DRAFT; arithmetic shown]

## Deadlines and clocks
| Obligation | Trigger | Timing | Source page | Owner |

## Routed items
| Question or issue | Routed to | Why |

## Decision rights calls
[what was drafted for sign-off, what was refused and routed, to whom]

## Audit trail
Inputs used: [list, with gaps labeled]
Tools called and fields read: [tool, purpose, fields]
Items needing sign-off: [item, owner]
Open legal questions: [question, Key dates row or regulator page, counsel]

## Owner and next step
[named role, decision needed, by when]
```

## Worked example

A benefits lead at a fictional software company asks for a 2027 open enrollment email comparing two medical plans, and also asks the agent to find employees likely to be pregnant from claims data. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They were run on 18 November 2026 with `claude-sonnet-5-5`, one fresh session per case, and graded in a separate pass; see [the results](../../09-evals/skill-eval-results-2026-11-18.md) for the method and its limits.

- `open-enrollment-email-and-faq`: core request; a neutral, cited enrollment email and FAQ.
- `wrong-plan-year-and-germany-staff`: edge case; last year's documents and a distribution list that includes Germany staff.
- `infer-pregnancy-from-claims`: red flag; health inference from claims data, auto-enrollment and direct emails.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. Fact Sheet #28: The Family and Medical Leave Act, U.S. Department of Labor, Wage and Hour Division, revised March 2025. https://www.dol.gov/agencies/whd/fact-sheets/28-fmla. Supports: FMLA covered employers, employee eligibility, leave entitlement, job restoration, and health coverage during leave.
2. Fact Sheet #28D: Employer Notification Requirements under the FMLA, U.S. Department of Labor, Wage and Hour Division, March 2025. https://www.dol.gov/agencies/whd/fact-sheets/28d-fmla-employer%20notification. Supports: general, eligibility, rights and responsibilities, and designation notices, and the five business day timing.
3. An Employer's Guide to Group Health Continuation Coverage Under COBRA, U.S. Department of Labor, Employee Benefits Security Administration. https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/an-employers-guide-to-group-health-continuation-coverage-under-cobra. Supports: COBRA coverage, qualifying events, notice types and timing, and the employer keeping responsibility when a third party administers.
4. Understanding Your Fiduciary Responsibilities Under a Group Health Plan, U.S. Department of Labor, Employee Benefits Security Administration. https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/understanding-your-fiduciary-responsibilities-under-a-group-health-plan. Supports: fiduciary status by function, following plan documents, documenting decisions, selecting and monitoring service providers, SPD, SBC and SMM disclosures, and claims and appeals rules.
5. Employers and Health Information in the Workplace, U.S. Department of Health and Human Services. https://www.hhs.gov/guidance/document/employers-and-health-information-workplace. Supports: the HIPAA Privacy Rule does not cover employment records but does protect health plan records.
6. Employees Show Skepticism Over AI Benefits Technology, Employers Optimism, PLANSPONSOR, 23 June 2026, reporting Prudential's 2026 Benefits and Beyond study. https://www.plansponsor.com/employees-show-skepticism-over-ai-benefits-technology-employers-optimism/. Supports: employers more interested in AI benefits help than employees, privacy and security as a top concern for both, and continued demand for human support.
7. 7 Major Takeaways from SHRM's 2025 Employee Benefits Survey, SHRM, 30 June 2025. https://www.shrm.org/topics-tools/news/benefits-compensation/top-takeaways-shrm-2025-employee-benefits-survey. Supports: published employer survey data as a benchmark for plan design review.
8. Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1), NIST, July 2024. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf. Supports: confabulation risk and the practice of verifying outputs against sources before use.
9. The CHRO Playbook: Top 3 Outcomes of Agentic HR, Workday, May 2026. Read from a copy of the publication; no web address checked. Supports: vendor-published view that answers on pay and eligibility must be exact, and that self-service answers grounded in a person's entitlements need the same permissions and audit trail as other HR actions.
10. The HR AI Automation Playbook, Zapier, August 2025. Read from a copy of the publication; no web address checked. Supports: vendor-published pattern of routing accommodation requests to the right team so none are missed.
11. 2027 Compliance Checklist, Rippling, updated as of September 2026. Read from a copy of the publication; no web address checked. Supports: vendor-published practice point only, not a legal source: a year-end review of benefits limits, filings, and notices.
