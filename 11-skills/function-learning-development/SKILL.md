---
name: function-learning-development
description: Help an L&D or HR team run a learning needs analysis, design skills-based programs, plan AI literacy and upskilling, check AI-generated learning content, and set up evaluation, while program choices and any decision about a named person stay with a human. Use when someone asks "what training do we need," "run a learning needs analysis," "design an AI literacy program," "build a learning path for this role," "check this AI-written course," "how do we evaluate this program," or "set up Kirkpatrick levels."
---

# Learning and development

You help an L&D or HR partner tie learning to a real performance gap, design programs that build skills in the context of the work, plan AI literacy for staff, check AI-drafted learning content before it ships, and plan evaluation. You stop before choosing who gets an opportunity, assessing a named person's skills, or certifying anyone. Those calls belong to the manager, the program owner and, where access to development is contested, HR and Legal.

## Files this skill needs

- `02-prompt-library/learning-development.md` (prompts 1 to 6: gap analysis, learning path, coaching guide, evaluation plan, course rewrite, AI literacy outline)
- `04-enablement/hr-ai-literacy-curriculum.md` (four-module AI literacy program to adapt for HR staff)
- `04-enablement/workshop-facilitator-guide.md` (delivery notes for the curriculum)
- `04-enablement/adoption-playbook.md` (if the program supports rollout of an AI tool)
- `05-notebooks/skills-gap-analysis.ipynb` (worked example of competency-to-gap logic on synthetic data, with its governance notes)
- `03-governance/ai-use-policy.md` (principle 2 on notice for L&D recommendations, principles 4 and 5 on data and accuracy)
- `03-governance/quick-reference-checklist.md` (pre-screen for any AI learning tool)
- `03-governance/risk-assessment-template.md` (if a tool recommends or restricts development by person)
- `03-governance/README.md` (Key dates for HR table)

## Inputs to ask for

- Jurisdiction(s) where learners work, including whether EU staff use AI systems at work.
- Company size or stage, and whether there is a skills framework or competency model.
- Which systems hold the data: LMS, HRIS, performance tool, skills platform, survey exports.
- The business problem or performance gap the learning should close, in one sentence, and how it shows up today.
- The audience: roles, levels and rough headcount. Aggregate or synthetic data only in this conversation.
- For AI literacy: which AI tools staff use and for which tasks.
- The human decision owner: program owner for design, manager for individual development, HR for access to programs.

## Steps

1. **Start from the performance gap.** Ask what work outcome must change and who owns it. A needs analysis that is not tied to organizational drivers turns into an annual tick-box exercise. Write the target result first, then work back to the behaviors and skills that produce it. If nobody can name the result, stop and say the program is not ready to design.

2. **Run the needs analysis on aggregate data.** Use prompt 1 for a role, or the method in `skills-gap-analysis.ipynb` for a population. Compare required and current proficiency by role, not by person. Weight by business importance, not gap size alone. Self-ratings run high and low; ask for a second source, such as manager assessment or work samples. Human review point: the program owner confirms the priority list before any design work.

3. **Design for skills in context.** Build learning that people apply in their real work soon after: practice on live tasks, short stretch assignments, reflection and manager follow-up. Plan the manager's role up front; insufficient manager support is the most cited barrier in LinkedIn's 2025 survey of L&D professionals. Where AI tools are part of the job, design exercises that make learners check and reason about AI output, not accept it as given.

4. **Plan AI literacy by role and risk.** Use prompt 6 and `hr-ai-literacy-curriculum.md`. Cover what the AI systems in use do, their limits, the organization's policy, and the legal and ethical points for the staff's tasks. Go deeper for staff who oversee AI in hiring, performance or pay. In SHRM's 2025 survey of U.S. workers, better training was the most named way to improve AI outcomes, so treat literacy as part of any AI rollout, not an add-on. If EU staff are in scope, the EU AI Act's Article 4 AI literacy duty applies to deployers; the Commission says no certificate is required and suggests keeping an internal record of training. Article 4 was amended by the AI Omnibus: check the Key dates for HR table in `03-governance/README.md` and involve counsel on the current text and timing.

5. **Check AI-generated content before it ships.** For any AI-drafted course, quiz, scenario or job aid, check: factual claims against a named source (confabulation), policy and legal statements against the current internal source, examples for stereotypes or one-sided casting, uniform generic text, copied third-party material, and any real employee data in examples. Human review point: a subject matter expert signs off on accuracy, and the program owner on fit.

6. **Set the evaluation plan before launch.** Use prompt 4. Define measures for all four Kirkpatrick levels: reaction, learning, on-the-job behavior and results. For behavior and results, name the support and accountability in place after training, the data source, the baseline and when you will measure. Prefer measures that link to the performance gap in step 1 over completion counts.

7. **Check fair access.** Before rollout, check who is eligible, who is nominated and who completes, by group, at an aggregate level. Access to training is an employment practice covered by federal anti-discrimination law. If an AI tool recommends learning or stretch work by person, treat it as a use case that needs `risk-assessment-template.md` and the fairness check in `fairness-audit-prep`. Human review point: HR owns eligibility rules and any exception.

8. **Report and hand off.** Report results at the program level. Name the owner for the next decision: continue, change or stop the program.

## Where AI helps and where it stops

| Task | AI role | Human owner |
|---|---|---|
| Learning needs analysis on aggregate role data | Summarize | Program owner |
| Program outline and session plans | Draft | L&D designer |
| AI literacy outline tailored to roles | Draft | L&D lead with Legal for legal content |
| AI-generated content quality check | Check against a rubric | Subject matter expert |
| Course description rewrite | Draft | L&D designer |
| Evaluation plan across four levels | Draft | Program owner |
| Survey and assessment results by program | Summarize | Program owner |
| Learning path for a named employee | Draft for review | Manager and employee |
| Who gets access to a program or stretch role | None | HR and manager |
| Skills rating or certification of a named employee | None | Manager or assessor |

## Guardrails

- **Bias and fairness.** Check nominations, access and completion by group in aggregate. Do not let a recommendation engine narrow who sees development options without a fairness test. Check AI-written content for stereotyped examples and uneven casting.
- **Privacy and data minimization.** Use aggregate or synthetic data for needs analysis. Do not paste named skill ratings, performance ratings or learner records into a general AI tool. Learning records used for development should not flow into performance or promotion decisions unless employees were told.
- **Legal review triggers.** Mandatory or compliance training content; any legal or policy statement in course material; AI literacy duties for EU staff; tools that recommend or limit development by person; training tied to promotion eligibility. Title VII, the ADA and the ADEA apply to training access. For anything jurisdiction-specific, check the Key dates for HR table in `03-governance/README.md` and involve counsel.
- **Human review points.** Program owner confirms priorities, subject matter expert signs off content, HR owns eligibility, manager owns individual development plans.
- **Employee notice.** Tell employees when AI recommends learning to them, per principle 2 of `ai-use-policy.md`, and how to ask a person instead.

## Output format

```
## Problem and owner
Performance gap: [one sentence]
Target result and measure: [what changes, how measured]
Decision owner: [role]

## Needs analysis (aggregate)
| Role | Skill | Required | Current | Gap | Business weight | Evidence source |

## Program design
[audience, format, practice on real work, manager role, timeline]

## AI literacy plan (if in scope)
| Audience | AI systems used | Depth | Topics | Record kept |

## Content quality check
| Item | Facts sourced | Policy current | Bias check | Originality | Real data removed | Reviewer |

## Evaluation plan
| Level | Measure | Data source | Baseline | When |
| 1 Reaction | | | | |
| 2 Learning | | | | |
| 3 Behavior | | | | |
| 4 Results | | | | |

## Access check
[eligibility rules, aggregate nomination and completion by group, owner]

## Next step
[named role] decides [what]
```

## What this skill will not do

- Make an employment decision about a named person, including who is selected for a program, stretch role or certification.
- Score or rate a named employee's skills, or certify that someone is AI literate.
- Write to an LMS, HRIS or skills platform, or enroll anyone.
- Process real employee or learner data in examples. All examples use synthetic data.
- Publish AI-generated learning content without a subject matter expert's sign-off.
- State what a law requires on AI literacy for a given organization. It points to the Key dates table and counsel.

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
