---
name: function-talent-acquisition
description: Builds a structured, skills-based hiring process from intake to offer, with AI drafting and checking at each stage and a named human owning every candidate decision. Produces a job analysis, inclusive job description, structured interview and scorecard, AI-use-by-stage map with fairness audit status, identity check plan, candidate notice, offer checklist and audit trail. Use whenever someone says run an intake for this req, rewrite this job description, build a structured interview and scorecard, can we use AI to screen resumes, rank these applicants, we think a candidate used a deepfake, draft the offer stage checklist, or how do we explain our AI use to candidates, and whenever a hiring tool would score, rank or filter people.
---

# Talent acquisition

For a recruiter, TA lead or hiring manager. It produces a structured, skills-based hiring plan and the drafts inside it. It stops wherever a person is advanced, rejected, scored, ranked or offered a job: those calls belong to the recruiter and hiring manager, with Legal where the steps say so.

## Files this skill needs

- `02-prompt-library/talent-acquisition.md` (prompt 1 job description, 2 question bank, 3 decline message, 4 feedback coaching, 5 sourcing outreach)
- `10-mcp-agents/recruiter_intake/ENABLEMENT.md` and `10-mcp-agents/resume_screen/ENABLEMENT.md`
- `11-skills/fairness-audit-prep/SKILL.md` (before any tool that scores, ranks or filters candidates goes live)
- `11-skills/hr-ai-vendor-review/SKILL.md` (if the AI arrives inside an ATS, sourcing or assessment product)
- `11-skills/eu-ai-act-hr-classifier/SKILL.md` (if EU candidates are in scope)
- `03-governance/ai-use-policy.md` (principle 1 human decisions, 2 notice, 4 data, 6 logging, and the prohibited uses list)
- `03-governance/risk-assessment-template.md` and `03-governance/quick-reference-checklist.md`
- `03-governance/deployer-checklist.md` (workplace emotion recognition flag)
- `03-governance/README.md` (Key dates for HR table)

## Inputs

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| Role title, level, team, req approved and budgeted | Yes | ATS, read-only: req ID, title, level, approval status | Senior Data Engineer, L5, approved |
| Work location and where candidates may live | Yes | Ask the user | Remote US, open to Chicago and Berlin |
| Hiring manager and process-owning recruiter | Yes | ATS, read-only: req owner fields | Named by role on the req |
| Must-haves, nice-to-haves, trainable skills, disqualifiers | Yes | Ask the user | Six must-haves, two trainable |
| Systems that hold candidate data and which use AI features | Yes | Ask the user | ATS with ranking add-on, scheduling tool |
| Whether any tool scores, ranks or filters, and its fairness audit status | Yes | Ask the user | Vendor ranking, no audit on file |
| Company size, federal contractor status, union or works council | No | Ask the user | 1,400 staff, works council in Germany |
| Stage counts for a past req, for monitoring | No | ATS export, read-only: stage, counts, self-identified group fields in aggregate only | 412 applied, 60 screened in |

If a required input is missing, ask for it once, in one short question at the top of your reply, then proceed with the gap labeled in the output, for example "Jurisdiction not confirmed: notice duties not mapped."

## Tools and connectors

- **Repo MCP tools.** `calibrate_recruiter_intake` turns an intake into skill buckets, a Boolean string and clarifying questions. `lint_jd_language` flags coded and proxy wording in a job description. `screen_resume_against_jd` maps evidence per requirement with no score or rank and returns `human_review_required: true`. Read each tool's `ENABLEMENT.md` before calling it.
- **ATS, read-only through an MCP connector or export.** Read the minimum: req fields, stage names, stage counts. Read a named candidate's resume text only when the user asks for an evidence map on that candidate.
- **Scheduling and assessment tools.** Read configuration only (which steps use AI, what is recorded), never recordings.
- Never call a write, send, move-stage, disposition or update tool, even if the connector offers one. Hand drafts to the recruiter.
- Log each tool call (tool, purpose, fields read) in the Audit trail.
- If a tool returns data on candidates or reqs outside the request, stop, do not use it, and ask.
- If an agent runs intake, job description and outreach as one workflow, it pauses at each sign-off below and does not continue past an unsigned checkpoint.

## By maturity stage

Stages follow the repo's maturity scale in [the roadmap template](../../06-roadmap/transformation-roadmap-template.md). Decision rights in this skill are the same at every stage.

| Stage | How to run it | Before moving up |
|---|---|---|
| Start (Levels 0 to 1) | Paste intake notes, the job description and past stage counts, never resumes. Agent drafts the job analysis, posting and interview plan; the recruiter checks each. | Hiring manager signs one plan; counsel reviews the candidate notice. |
| Pilot (Level 2) | Read-only ATS export: req ID, level, approval status, req owner, stage counts. TA lead owns it and tracks human review request resolution. | Notice live; People Analytics computes selection rate ratios. |
| Scale (Level 3) | Limited: logged ATS reads, `calibrate_recruiter_intake`, `lint_jd_language`. `screen_resume_against_jd` not before an adverse impact check on last cycle's screen-outs passes People Analytics review. | Quarterly ratios reviewed by People Analytics and Legal. |
| Embed (Levels 4 to 5) | Limited: an approved req triggers intake and posting drafts; evidence maps run only when a recruiter asks. Recruiters and hiring managers decide every candidate. | Rerun the test cases in `evals/` when the skill or model changes. |

## Steps

1. **Run a skills-based job analysis.** Call `calibrate_recruiter_intake` to sort the list into must-haves, nice-to-haves, trainable skills and disqualifiers. Tie every must-have to a task. Ask which must-haves a strong learner could build after hire, since hiring for capacity to learn can outperform hiring only for current proficiency. Replace a degree or certificate with the skill it stands for unless the hiring manager ties the credential itself to a task. More than six must-haves usually hides nice-to-haves. Sign-off: hiring manager.

2. **Draft an inclusive job description.** Use prompt 1, then run `lint_jd_language`. Remove preferences dressed up as requirements and language that signals a preference for a protected group, such as "recent graduates." Mark every pay range, benefit or work arrangement claim for the hiring manager to verify. Keep requirements human-set: in the European Commission's draft, non-binding guidance, a tool that sets requirements or scores CVs is high risk, while one that drafts from a person's requirements may not be. Sign-off: recruiter approves the posting.

3. **Plan sourcing and outreach.** Draft the Boolean string from the intake and personal outreach with prompt 5. Check that sourcing does not rely only on referrals from a homogeneous team, which can exclude groups by effect. A sourcer reads each profile before any message goes out. Never send to a list. Sign-off: sourcer, per message.

4. **Build the structured interview and scorecard.** Pick four to six competencies from the job analysis. Draft the same questions, in the same order, for every candidate, with prompt 2. Mix past-behavior and situational questions, write neutral probes in advance, and give each rating level a written example answer the interviewers agree. Plan accessible formats and say how to request accommodation. Interviewers rate on their own before any group discussion.

   Where skills matter more than credentials, add a realistic work sample; it is harder to inflate with AI than a certificate. Tell candidates in advance whether they may use AI in it. If they may, assess how they check and correct its output, and confirm authorship with follow-up questions in a live round. Route proctoring tools, such as webcam monitoring or browser lockdown, to Privacy and Legal first, and offer another format on request. Sign-off: hiring manager and panel.

5. **Set what screening AI may do.** Default to the evidence-only pattern: `screen_resume_against_jd` shows where a resume does or does not show evidence, with no score or rank. "No evidence found" means the resume does not mention it; use it as an interview question, never an auto-reject. Research on embedding models used for resume retrieval found strong preferences tied to names associated with race and gender, so treat any tool that ranks resumes as high risk. Quick test: if the output scores, ranks, recommends or filters people, assume high risk. The Commission's draft guidance agrees, says a human sign-off does not lower the risk class, and says an employer that builds screening on a general-purpose chatbot may take on provider duties. These are draft points for counsel. If anyone proposes scoring, ranking or auto-rejecting, stop: run `risk-assessment-template.md` and `fairness-audit-prep` first and route to Legal and People Analytics. Sign-off: a recruiter reviews every screen-out.

6. **Add identity checks without profiling.** Candidate fraud now includes AI face-swapping in video interviews and reused contact details across applications. Apply the same steps to every candidate at a stage: a live identity check at a set stage, at least one in-person or live interaction where practical, a duplicate contact detail check in the ATS, and an audit of staffing partners. Do not draft rules that flag people by accent, schooling country or name. Sign-off: Security, with the recruiter, owns any suspected case.

7. **Tell candidates how AI is used, and how to contest it.** Draft a short notice: which steps use AI, what a person reviews, what candidate AI use is acceptable, how to request an accommodation or human review, and who answers. Candidates report low trust that AI will judge them fairly, so use plain language. A declined candidate who asks is told the job-related requirements and the stage, never a model output. Check notice duties in the Regulation map. Sign-off: recruiter, with counsel on wording.

8. **Prepare the offer stage.** Draft the offer checklist: approved pay inside the posted range, conditional offer language and background check steps. If a consumer report is used, the checklist includes a standalone disclosure and written authorization before the check, and a pre-adverse action notice with a copy of the report before any decision based on it. Medical questions wait until after a conditional offer. Sign-off: hiring manager approves the offer; HR and Legal approve any withdrawal.

9. **Close the loop and monitor.** Draft decline messages with prompt 3 only after a person has decided. Use prompt 4 to coach interviewers on evidence-based feedback. Log which AI outputs were used at each stage, per principle 6, so the process can be reconstructed. Each quarter, ask People Analytics for stage selection rates by group (see Metrics). Sign-off: TA lead.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Sort the intake into skill buckets and clarifying questions | Hiring manager | Drafts for sign-off |
| Run the job description wording check and list flags | Recruiter acts on the flags | Does alone |
| Publish a job posting | Recruiter | Drafts for sign-off |
| Send sourcing outreach to a named person | Sourcer | Drafts for sign-off |
| Write interview questions and rating anchors | Hiring manager and panel | Drafts for sign-off |
| Map resume evidence per requirement, with no score | Recruiter | Drafts for sign-off |
| Check interviewer notes for impressionistic or biased language | Recruiter or HRBP | Drafts for sign-off |
| Advance, reject, score or rank a named candidate | Recruiter and hiring manager | Refuses and routes |
| Turn on a scoring, ranking or auto-reject feature | Legal and People Analytics, after a fairness audit | Refuses and routes |
| Decide a named candidate is fraudulent | Security, with the recruiter | Refuses and routes |
| Draft a decline message after the decision | Recruiter | Drafts for sign-off |
| Draft offer letter text from approved terms | Hiring manager with HR; any withdrawal by HR and Legal | Drafts for sign-off |

### Refuse and route

- "Rank these applicants" or "give each a fit score": refuse; return the evidence map for the recruiter, and route any scoring tool to `fairness-audit-prep`, People Analytics and Legal.
- "Auto-reject anyone without X": refuse; route to the recruiter, with the gap as an interview question.
- Read emotion, enthusiasm or honesty from interview video or voice, or judge culture fit from social media: refuse; route to Legal with `deployer-checklist.md`.
- Flag candidates as fraud risks by accent, schooling country or name: refuse; route to Security with the stage-based identity plan.
- Use age, "recent graduates" or any protected trait, or a proxy for one, as a criterion: refuse; route to the recruiter and Legal.
- Move a candidate's stage, disposition them, or message candidates: refuse; hand the draft to the recruiter.
- Ask for a photo before an offer is accepted, or a medical question before a conditional offer: refuse; route to HR and Legal.
- "What does the law require in New York City?": do not state it; point to the Key dates row and counsel.
- Use real candidate data in examples: refuse; use synthetic data.

## Guardrails

- **Fairness and adverse impact.** No tool scores, ranks or filters candidates until a fairness plan exists from `fairness-audit-prep`. Every procedure that screens people out must be job related; if it excludes a protected group, look for an equally effective option with less adverse impact. A vendor's validation helps but does not move the employer's responsibility. The four-fifths ratio is a screening flag under [29 CFR 1607.4(D)](https://www.govinfo.gov/content/pkg/CFR-2024-title29-vol4/pdf/CFR-2024-title29-vol4-sec1607-4.pdf), not a safe harbor or a verdict; small groups need a statistical test that People Analytics or counsel interprets.
- **Explainability and notice.** Per principle 2, candidates learn which steps use AI and how to request human review; explanations cite job-related requirements, never a model score.
- **Accessibility.** Offer accommodation for every test, assessment and interview format, and say how to ask in the notice.
- **Privacy and minimization.** Collect only what judges qualifications. No photo before an offer is accepted. Do not paste candidate data into an AI tool not approved for it, per principle 4. An agent reading candidate email reads only messages since its last run and keeps sender, subject and a one-line summary.
- **Inference about people.** SHRM's playbook lists interview sentiment analysis and social media culture fit judgments as emerging practices, not recommended ones, and `deployer-checklist.md` flags workplace emotion recognition as broadly prohibited in the EU. Both are refused above.
- **Legal review triggers.** Any scoring or ranking tool; candidates in the EU, New York City, Illinois, California, Colorado or another covered location; background checks; offer withdrawals; proctoring tools.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| NYC Local Law 144 | A tool that scores, ranks or filters is used for a New York City role | Flags it as a possible covered AEDT, asks for bias audit and notice status, routes to counsel |
| Illinois HB 3773 (Public Act 103-0804) | AI is used in hiring decisions for an Illinois role | Adds Illinois to the notice draft and the fairness check list, routes to counsel |
| California FEHA automated-decision system regulations | An automated tool is used in hiring for a California role | Flags the vendor-built tool and records retention questions, routes to counsel |
| Colorado SB 26-189 (ADMT Act) | Automated technology is used in a hiring decision for a Colorado role | Drafts notice, explanation and human review steps for counsel; the row says status is unverified |
| EU AI Act, high-risk HR systems | A tool is used in recruiting for a role in Germany or another EU country | Routes to `eu-ai-act-hr-classifier` and the EU AI Act intake template |
| GDPR, Article 22 (EU) | A rejection of an EU candidate would be solely automated | Refuses auto-reject and routes the design to counsel |

Counsel confirms scope and current status before you rely on any row. In your reply, name each rule as: see the Key dates row "exact row name" in `03-governance/README.md`. Stop there: do not write the row's dates, status or regulation numbers, even ones you read in the table or in Sources, because the table is the one place they are kept current.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| First-year retention of hires | Hires who started in a quarter and are still employed 12 months after their start date, divided by all hires who started that quarter | Outcome check that structured, skills-based selection picks people who stay |
| Stage selection rate ratio by group | Per stage and quarter: (candidates in a group advanced / candidates in that group who entered the stage), divided by the same rate for the highest-rate group; ratios below 0.8 go to People Analytics as a flag, not a finding | Earliest fairness signal for any screen, human or AI |
| Human review request resolution | Candidate requests for human review or accommodation closed within the recruiter-set response time in a quarter, divided by requests received that quarter | Shows the contest route in the notice works |

## Output format

```markdown
## Role and scope
[title, level, locations, systems, decision owners, gaps labeled]

## Job analysis
| Requirement | Type (must / nice / trainable / disqualifier) | Task it supports | Skill evidence accepted | Confirmed by |

## Job description draft
[draft text]
[wording flags; items for the hiring manager to verify]

## Structured interview plan
| Competency | Questions | Probes | Rating anchors (low / mid / high) | Interviewer |
[work sample, candidate AI use rule, accommodation route]

## AI use by stage
| Stage | Tool | AI role | Human review point | Fairness audit status |

## Identity steps
[same steps for every candidate at each stage, with owner]

## Candidate notice draft
[plain-language text, including how to request human review]

## Offer stage checklist
[approvals, background check notices]

## Decision rights applied
| Item | Agent role | Routed to |

## Metrics this plan tracks
[from the Metrics table]

## Audit trail
- Inputs used: [list; gaps labeled]
- Tools called and fields read: [tool, purpose, fields]
- Items needing sign-off: [item -> owner]
- Open legal questions: [Key dates row -> question for counsel]
```

## Worked example

A Harbor & Pine recruiter asks for a plan for a data engineer role open to Chicago, Denver and Berlin candidates, where the ATS ranking add-on has no audit on file. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They were run on 18 November 2026 with `claude-sonnet-5-5`, one fresh session per case, and graded in a separate pass; see [the results](../../09-evals/skill-eval-results-2026-11-18.md) for the method and its limits.

- `structured-plan-for-new-req`: core request, intake through offer checklist with sign-offs.
- `cross-border-req-missing-audit`: Illinois, Colorado and Germany candidates, a ranking add-on with no audit, and missing hiring manager input.
- `rank-applicants-and-auto-reject`: a request to score, rank and auto-reject named applicants, which the skill refuses and routes.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. Employment Tests and Selection Procedures, US Equal Employment Opportunity Commission, 1 December 2007. https://eeoc.gov/laws/guidance/employment-tests-and-selection-procedures. Supports: Title VII, ADA, and ADEA apply to tests; disparate impact framework; job relatedness; less discriminatory alternatives; vendor validation does not shift responsibility; test accommodations.
2. Prohibited Employment Policies/Practices, US Equal Employment Opportunity Commission. https://www.eeoc.gov/prohibited-employment-policiespractices. Supports: job ads showing a preference such as "recent college graduates"; word-of-mouth recruiting risk; limiting pre-employment inquiries; no photo before an offer is accepted; no pre-offer disability inquiries.
3. Structured Interviews, US Office of Personnel Management. https://WWW.OPM.GOV/policy-data-oversight/assessment-and-selection/structured-interviews/structured-interviews.pdf. Supports: job analysis first; four to six competencies; same questions in the same order; behavioral and situational questions; planned neutral probes; rating levels with example answers; individual rating before consensus; accessible setting.
4. Gartner Survey Shows Just 26% of Job Applicants Trust AI Will Fairly Evaluate Them, Gartner, 31 July 2025. https://www.gartner.com/en/newsroom/press-releases/2025-07-31-gartner-survey-shows-just-26-percent-of-job-applicants-trust-ai-will-fairly-evaluate-them. Supports: low candidate trust in AI evaluation; candidate use of AI in applications; interview fraud; setting clear expectations on acceptable AI use; system-level validation over individual surveillance.
5. Gartner HR Survey Reveals Hiring for Promise Instead of Proficiency is More Effective and Efficient for Closing Skills Gaps, Gartner, March 2025. https://www.gartner.com/en/newsroom/press-releases/2025-03-11-closing-skills-gaps-at-scale. Supports: separating trainable skills from must-haves in the intake.
6. Gender, Race, and Intersectional Bias in Resume Screening via Language Model Retrieval, Kyra Wilson and Aylin Caliskan, arXiv, 29 July 2024. https://arxiv.org/html/2407.20371v1. Supports: embedding models used to rank resumes showed preferences tied to names associated with race and gender.
7. North Korean IT Workers Conducting Data Extortion (I-012325-PSA), FBI Internet Crime Complaint Center, 23 January 2025. https://www.ic3.gov/PSA/2025/PSA250123. Supports: face-swapping in video interviews; reused phone numbers and email addresses; identity checks at hiring and onboarding; auditing staffing firms; in-person steps where possible.
8. Background Checks: What Employers Need to Know, US Federal Trade Commission and EEOC. https://www.ftc.gov/business-guidance/resources/background-checks-what-employers-need-know. Supports: FCRA standalone disclosure and written authorization; pre-adverse action notice with report copy and summary of rights; adverse action notice; same standards for everyone; no medical questions before a conditional offer.
9. AI in the Workplace Playbook: A Practical Guide for Human-First AI Strategy in the Modern Workplace, SHRM, 2025. Read from a copy of the publication; no web address checked. Supports: scenario-based assessments; interview sentiment analysis and social media culture-fit judgments named as emerging practices; humans keep final hiring decisions.
10. Draft guidelines on the classification of high-risk AI systems, European Commission, 2026 (consultation draft, non-binding). Read from a copy of the publication; no web address checked. Supports: draft guidance that tools which score, rank, recommend, or filter candidates, or set job requirements, are high risk; human sign-off does not change the class; repurposing general-purpose tools may shift provider duties.
11. How to Hire the Best Engineers in the AI Era, CoderPad, no date shown. Read from a copy of the publication; no web address checked. Supports: vendor-published practice points on work samples, assessing candidate AI use, confirming authorship, and privacy questions raised by proctoring.
