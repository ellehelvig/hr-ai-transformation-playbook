---
name: function-learning-development
description: Produces learning needs analyses tied to a named performance gap, skills-based program designs, role-tiered AI literacy plans with a training record, quality checks on AI-generated learning content, four-level evaluation plans with baselines, and aggregate access checks, each with an audit trail, while program choices and any decision about a named person stay with a human. Use whenever someone says "what training do we need," "run a learning needs analysis," "design an AI literacy program," "build a learning path for this role," "check this AI-written course," "how do we evaluate this program," "set up Kirkpatrick levels," or "who should get into this program," and whenever a request would have AI select, certify or monitor named learners.
---

# Learning and development

This skill serves L&D leads, program owners and HR partners. It ties learning to a real performance gap, designs programs that build skills in the work, plans AI literacy by role, checks AI-drafted content before it ships, and plans evaluation. It stops before choosing who gets an opportunity, assessing a named person's skills, or certifying anyone: those calls belong to the manager, the program owner and, where access is contested, HR and Legal.

## Files this skill needs

- `02-prompt-library/learning-development.md` (prompts 1 to 6: gap analysis, learning path, coaching guide, evaluation plan, course rewrite, AI literacy outline)
- `04-enablement/hr-ai-literacy-curriculum.md` (four-module AI literacy program to adapt for HR staff)
- `04-enablement/workshop-facilitator-guide.md` (delivery notes for the curriculum)
- `04-enablement/adoption-playbook.md` (if the program supports rollout of an AI tool)
- `05-notebooks/skills-gap-analysis.ipynb` (competency-to-gap logic on synthetic data, with its governance notes)
- `03-governance/ai-use-policy.md` (principle 2 on notice for L&D recommendations, principles 4 and 5 on data and accuracy)
- `03-governance/risk-assessment-template.md` (if a tool recommends or restricts development by person)
- `11-skills/fairness-audit-prep/SKILL.md` (any tool that recommends, selects or ranks learners)
- `03-governance/README.md` (Key dates for HR table)

## Inputs

If a required input is missing, ask for it once, in one short question at the top of your reply, then proceed with the gap labeled `[GAP: what is missing]` in the output.

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| Performance gap the learning should close, in one sentence | Yes | Ask the user | "Support reps accept AI-drafted replies without checking policy" |
| Target result and how it is measured today | Yes | Ask the user | Reopened tickets per 1,000 closed |
| Audience: roles, levels, headcount, countries | Yes | HRIS, read-only: job, level, location (aggregate counts) | 310 support staff, 64 in Germany |
| Skills framework or taxonomy, with proficiency levels | If one exists | Skills platform, read-only: role skill profiles | "Policy judgment, level 3" |
| Current proficiency, aggregate by role | For a needs analysis | Skills platform or survey export, aggregate only | Median self-rating 3.4 of 5 |
| AI tools staff use, and for which tasks | For AI literacy | Ask the user | Drafting assistant in the ticket queue |
| Eligibility rules and aggregate nomination counts by group | For an access check | HRIS or LMS export, aggregate only | 120 eligible, 30 nominated |
| Decision owner | Yes | Ask the user | Program owner for design; manager for individual plans |

## Tools and connectors

Work through MCP connectors or exports, read-only, with the minimum fields:

- LMS: course list, enrollment and completion dates, assessment results aggregated by course or cohort.
- HRIS: job, level, location and manager as aggregate counts. No performance ratings, leave or health fields.
- Skills platform: role skill profiles and aggregate proficiency distributions, never named skill scores.
- Survey platform: aggregate program survey results with small groups suppressed.
- Repo MCP tools in `10-mcp-agents/`: `lint_jd_language` (in `resume_screen/`) flags gender-coded and protected-class-proxy wording in course text, scenarios and program descriptions; `ask_governance_policy` (in `policy_qa/`) cites the governance section behind a stop point.

Never call a write, send or update tool, even if the connector offers one: no enrollment, assignment, completion mark or learner message. Log each tool call (tool, purpose, fields read) in the output's audit trail. If a tool returns data on people outside the request, or named learner records, stop, do not use it, and ask.

## By maturity stage

Stages follow the repo's maturity scale in [the roadmap template](../../06-roadmap/transformation-roadmap-template.md). Decision rights in this skill are the same at every stage.

| Stage | How to run it | Before moving up |
|---|---|---|
| Start (Levels 0 to 1) | Paste the gap, role headcounts and LMS completion counts by cohort. An expert checks every drafted content item. | Program owner signs a needs analysis tied to a named gap. |
| Pilot (Level 2) | One read-only LMS export: course, cohort, completion dates, cohort assessment results. Metric: behavior transfer rate. | Baselines recorded; one program's content passes expert review. |
| Scale (Level 3) | Limited. Read-only LMS, HRIS counts, skills platform and `lint_jd_language`; tracks literacy record coverage. Recommending learning by person: not before a `fairness-audit-prep` review and learner notice. | HR and People Analytics review the access check. |
| Embed (Levels 4 to 5) | Limited. A submitted AI-drafted course triggers the content check for expert sign-off. Never enrolls, selects or certifies. | Rerun the test cases in `evals/` when the skill or model changes. |

## Steps

Run the work as a workflow with hard checkpoints the agent never passes alone: priority list confirmed (program owner), content signed (subject matter expert), access check reviewed (HR), evaluation plan locked before launch (program owner).

1. **Start from the performance gap.** Ask what work outcome must change and who owns it. A needs analysis not tied to organizational drivers turns into an annual tick-box exercise. Write the target result first, then work back to the behaviors and skills that produce it. If nobody can name the result, say the program is not ready to design. Sign-off: the business owner of the result.

2. **Run the needs analysis on aggregate data, against skills.** Use prompt 1 for a role, or the method in `skills-gap-analysis.ipynb` for a population. Map each gap to the organization's skills taxonomy, with proficiency levels written as observable behaviors. Compare required and current proficiency by role, not by person, and weight by business importance, not gap size alone. Self-ratings run high and low: ask for a second source, preferring skills evidence from work samples and observed tasks over course completions or credentials. Define the target skills and success measures before buying any content. Sign-off: the program owner confirms the priority list.

3. **Design for skills in context.** Build learning people apply in real work soon after: practice on live tasks, short stretch assignments, reflection and manager follow-up. Plan the manager's role up front; insufficient manager support is the most cited barrier in LinkedIn's 2025 survey of L&D professionals. Where AI tools are part of the job, design exercises that make learners check and reason about AI output, not accept it as given. In Microsoft's 2026 Work Trend Index survey of 20,000 knowledge workers who use AI, quality control of AI output was the top-ranked rising human skill, named by 50%. For AI upskilling, small peer groups practicing on real tasks, with an experienced user sharing their screen, often beat generic e-learning. Target tasks rather than whole jobs, give protected time to experiment within policy, and train managers first. The same report links four manager behaviors to stronger AI results: using AI visibly, setting quality standards for AI work, making room for experiments, and pushing for redesign of the work itself. Build manager enablement around those four. Sign-off: the L&D designer.

4. **Plan AI literacy by role and risk.** Use prompt 6 and `hr-ai-literacy-curriculum.md`. Set four tiers: all staff; regular AI users; staff who oversee AI in hiring, performance or pay; and builders or administrators. Cover what the AI systems in use do, their limits, the organization's policy, and the legal and ethical points for each tier's tasks. Responsible-use content covers data exposure, copyright, inaccurate output and how to review it, and who may use which tool with which data. Add prompt-writing practice and a shared prompt library. Address job security fears directly in the all-staff module. In SHRM's 2025 survey of U.S. workers, better training was the most named way to improve AI outcomes, so treat literacy as part of any AI rollout. If EU staff are in scope, see the Key dates row for EU AI Act, AI literacy (Article 4): the Commission says no certificate is required and suggests an internal record of training, and the article was amended in 2026, so counsel checks the current text. Sign-off: the L&D lead, with Legal for legal content.

5. **Check AI-generated content before it ships.** For any AI-drafted course, quiz, scenario or job aid, check factual claims against a named source (confabulation), policy and legal statements against the current internal source, examples for stereotypes or one-sided casting (run `lint_jd_language` on the text), uniform generic text, copied third-party material, and any real employee data. Flag AI-generated video, voice or images for labeling. Sign-off: a subject matter expert on accuracy, the program owner on fit.

6. **Lock the evaluation plan before launch.** Use prompt 4. Define measures for all four Kirkpatrick levels: reaction, learning, on-the-job behavior and results. For behavior and results, name the support and accountability in place after training, the data source, the baseline and when you will measure. Where rollout is staggered, use the later cohort as a comparison group for levels 3 and 4. Prefer measures tied to the step 1 gap over completion counts. Sign-off: the program owner.

7. **Check fair access and explain recommendations.** Before rollout, check eligibility, nomination and completion by group, in aggregate. Access to training is an employment practice covered by federal anti-discrimination law. Where nomination counts by group are available, compute the four-fifths ratio as a screening flag under the Uniform Guidelines, [29 CFR 1607.4(D)](https://www.govinfo.gov/content/pkg/CFR-2024-title29-vol4/pdf/CFR-2024-title29-vol4-sec1607-4.pdf), not a safe harbor or a verdict; small groups need a statistical test, and People Analytics or counsel interprets it, per `fairness-audit-prep`. If an AI tool recommends learning or stretch work by person, it needs `risk-assessment-template.md` and that fairness check, and each learner is told why an item was recommended, that AI made the suggestion, and how to ask a person instead. If anyone proposes AI proficiency as a performance or promotion criterion, check equal access to approved tools, training, practice time and accommodations first, and route it to HR and Legal. The European Commission's draft high-risk guidelines (not binding) treat training as inside the high-risk employment rules when its results feed promotion, pay or continued employment, and learner-only feedback as outside them. Keep learner-only feedback apart from evaluation unless counsel has reviewed the link. Sign-off: HR owns eligibility rules and exceptions.

8. **Report and hand off.** Report results at the program level and name the owner of the next decision: continue, change or stop the program.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Check AI-generated content against the quality rubric | Subject matter expert | Does alone |
| Summarize aggregate survey and assessment results by program | Program owner | Does alone |
| Learning needs analysis on aggregate role data | Program owner | Drafts for sign-off |
| Program outline, session plans and course description rewrite | L&D designer | Drafts for sign-off |
| AI literacy plan by role tier, with training record | L&D lead, Legal for legal content | Drafts for sign-off |
| Four-level evaluation plan with baselines | Program owner | Drafts for sign-off |
| Four-fifths screening flag on aggregate nomination counts | HR, with People Analytics | Drafts for sign-off |
| Learning path for a named employee | Manager and employee | Drafts for sign-off |
| Who gets into a program, stretch role or cohort | HR and manager | Refuses and routes |
| Skills rating or certification of a named employee | Manager or assessor | Refuses and routes |
| AI proficiency as a performance or promotion criterion | HR and Legal, after an access check | Refuses and routes |

### Refuse and route

- "Pick the top 20 for the leadership program from LMS scores": refuse; route to HR and the program owner with written eligibility criteria and an open nomination process.
- "Certify these people as AI literate" or "rate Sam's skills": refuse; route to the manager or a named assessor.
- "Turn on webcam attention or engagement tracking in virtual classes": refuse as emotion inference; route to the HR AI governance group and counsel.
- "Enroll everyone" or "assign this course in the LMS": refuse; the LMS administrator does it after the program owner approves.
- "Publish this AI-written course now": refuse until a subject matter expert signs off.
- "Tell us exactly what Article 4 requires of us": point to the Key dates row and route to counsel.
- "Use assessment scores to decide who is let go": refuse; route to HR leadership and counsel with the selection criteria template.

## Guardrails

- **Fairness and adverse impact.** Check nominations, access and completion by group in aggregate. Do not let a recommendation engine narrow who sees development options without a fairness test. Check AI-written content for stereotyped examples and uneven casting.
- **Explainability and notice.** Tell employees when AI recommends learning to them, per principle 2 of `ai-use-policy.md`, why the item was suggested, and how to ask a person instead. Say plainly when feedback is for the learner only.
- **Privacy and minimization.** Use aggregate or synthetic data for needs analysis and synthetic data in examples. Do not paste named skill ratings, performance ratings or learner records into a general AI tool. Learning records used for development do not flow into performance or promotion decisions unless employees were told.
- **Legal review triggers.** Mandatory or compliance training content; any legal or policy statement in course material; AI literacy duties for EU staff; tools that recommend or limit development by person; training tied to promotion eligibility. Title VII, the ADA and the ADEA apply to training access.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| EU AI Act, AI literacy (Article 4) | Germany staff operate or use AI systems at work | Drafts the role-tiered plan and an internal training record; counsel checks the amended text |
| EU AI Act, transparency | An AI tutor talks to learners, or course media is AI-generated | Flags disclosure and labeling for the program owner and counsel |
| EU AI Act, emotion recognition at work (Article 5(1)(f)) | Anyone proposes inferring learner attention or emotion from webcam, voice or text | Refuses and routes to the governance group |
| California AB 1883 (Ch. 853, Stats. 2026) | The same kind of proposal for California staff | Refuses and routes to counsel |
| EU AI Act, high-risk HR systems | Training results feed promotion, pay or continued employment for Germany staff | Keeps learner-only feedback apart; routes the link to `eu-ai-act-intake-template.md` and counsel |
| Illinois HB 3773 (Public Act 103-0804) | A learning recommender's output feeds promotion for Illinois staff | Flags notice and routes to counsel |

Counsel confirms scope and current status before you rely on any row. In your reply, name each rule as: see the Key dates row "exact row name" in `03-governance/README.md`. Stop there: do not write the row's dates, status or regulation numbers, even ones you read in the table or in Sources, because the table is the one place they are kept current.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| Behavior transfer rate | Completers whose step 1 behavior measure meets target at the 90-day check, divided by completers with a 90-day observation, per program cohort | Shows learning changed the work, not just attendance |
| Development access ratio by group | For each group, people nominated divided by people eligible, per program per half-year; each group's rate divided by the highest group's rate, with a statistical test for small groups | Screens who gets development for adverse impact |
| AI literacy record coverage | Staff with access to an approved AI system who hold a completed literacy record for their tier, divided by all staff with such access, at quarter end | Shows every AI user is trained and the record exists |

## Output format

```markdown
## Problem and owner
Performance gap: [one sentence]
Target result and measure: [what changes, how measured, baseline]
Decision owner: [role]

## Needs analysis (aggregate)
| Role | Skill (taxonomy) | Required | Current | Gap | Business weight | Evidence source |

## Program design
[audience, format, practice on real work, manager role, timeline]

## AI literacy plan (if in scope)
| Tier | Audience and headcount | AI systems used | Topics | Record kept |

## Content quality check
| Item | Facts sourced | Policy current | Bias check | Originality | Real data removed | AI media labeled | Reviewer |

## Evaluation plan
| Level | Measure | Data source | Baseline | Comparison group | When |

## Access check
[eligibility rules, aggregate nomination and completion by group, screening flag, owner]

## Decision rights calls
[what was drafted for sign-off, what was refused and routed, to whom]

## Audit trail
Inputs used: [list, with gaps labeled]
Tools called and fields read: [tool, purpose, fields]
Items needing sign-off: [item, owner]
Open legal questions: [question, Key dates row, counsel]

## Next step
[named role] decides [what]
```

## Worked example

An L&D lead at a fictional software company asks for an AI literacy plan for every employee, and also asks the agent to pick the 20 support reps with the highest quiz scores for a champion cohort. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They were run on 18 November 2026 with `claude-sonnet-5-5`, one fresh session per case, and graded in a separate pass; see [the results](../../09-evals/skill-eval-results-2026-11-18.md) for the method and its limits.

- `ai-literacy-plan-support-rollout`: core request; a tiered literacy and evaluation plan for an AI tool rollout.
- `needs-analysis-messy-self-ratings`: edge case; self-ratings only, blanks, and no stated performance gap.
- `webcam-engagement-cohort-selection`: red flag; webcam engagement scoring used to pick named people.

## Sources

Read on 18 November 2026. Practice sources inform the method. Legal points cite primary sources.

1. Learning needs analysis (factsheet), CIPD. https://prd.cipd.org/ae/knowledge/factsheets/learning-needs-factsheet. Supports: needs analysis tied to performance gaps and organizational drivers, risk of a tick-box annual exercise. Public preview only.
2. Kirkpatrick Four Levels Evaluation Certification Program, Bronze Level (brochure), Kirkpatrick Partners, August 2021. https://kirkpatrickpartners.com/wp-content/uploads/2024/03/KIRKPA_1.pdf. Supports: definitions of the four levels, results depending on a support and accountability package.
3. Workplace Learning Report 2025, LinkedIn Learning. https://learning.linkedin.com/content/dam/me/business/en-us/talent-solutions/resources/pdfs/linkedIn-workplace-learning-report-2025.pdf. Supports: insufficient manager support as the most cited barrier (survey of 937 L&D and HR professionals and 679 learners), need to link measures to business value.
4. Closing the experience gap, Deloitte Insights (Mallon, Cantrell, Forsythe), 24 March 2025. https://www.deloitte.com/us/en/insights/focus/human-capital-trends/2025/closing-the-experience-gap-through-talent-development.html. Supports: upskilling in context, micro-opportunities and reflection, managers sharing tacit knowledge, AI used to build judgment rather than accepted as given.
5. Press release on the report From Adoption to Empowerment: Shaping the AI-Driven Workforce of Tomorrow, SHRM, 8 July 2025. https://www.shrm.org/about/press-room/shrm-report-warns-of-widening-skills-gap-as-ai-adoption-reaches-. Supports: workers name better training as the top priority for improving AI outcomes, training satisfaction tied to how well AI fits business goals.
6. AI Literacy: Questions and Answers, European Commission, last updated 20 October 2026. https://digital-strategy.ec.europa.eu/en/faqs/ai-literacy-questions-answers. Supports: Article 4 duty on deployers to take measures, context and risk-based approach, no certificate required, internal record suggested, Article 4 amended by the Omnibus.
7. Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1), NIST, July 2024. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf. Supports: content check categories: confabulation, harmful bias and homogenization, intellectual property, data privacy.
8. Know Your Rights: Workplace Discrimination is Illegal, U.S. Equal Employment Opportunity Commission. https://eeoc.gov/know-your-rights-workplace-discrimination-illegal. Supports: Title VII, age and disability protections cover job training and promotion.
9. AI in the Workplace Playbook, SHRM, 2025. Read from a copy of the publication; no web address checked. Supports: role-based AI training in layers, responsible-use topics, prompt practice and shared prompt libraries, peer learning groups, training managers first, defining skills before buying content.
10. 2026 Work Trend Index Annual Report, Microsoft, May 2026. Read from a copy of the publication; no web address checked. Supports: quality control of AI output as the top-ranked rising human skill (50% of AI users surveyed), manager behaviors linked to stronger AI results.
11. Draft guidelines on the classification of high-risk AI systems, European Commission, consultation drafts (2026), non-binding. Read from a copy of the publication; no web address checked. Supports: draft view that training is in scope when results feed promotion, pay or continued employment, and learner-only feedback is not.
