---
name: hr-ai-readiness-assessment
description: Runs a short structured AI readiness assessment of an HR function (never of individual people) for teams at maturity Levels 0 to 2, scores seven dimensions 0 to 3 from the evidence given or marks them unknown, places the function on the repo's Level 0 to 5 scale at the lowest level the evidence supports, and drafts a 90-day starter plan with an owner role per item that names which library skills to start with, all for HR leader sign-off. Use whenever someone asks "where do we start with AI," "are we ready for AI in HR," "what's our AI maturity," "assess our HR AI readiness," "what should HR do first with AI," "build us a 90-day AI plan," or "we have no AI policy yet, what now," and whenever a request would rate named HR staff on AI skills, skip governance to launch a screening tool, or declare the organization compliant with an AI law.
---

# HR AI readiness assessment

This skill serves the HR leader of a team at Level 0, 1, or 2 who asks where to start. It asks a short questionnaire, scores the HR function on seven dimensions with the evidence for each, places the function on the repo's maturity scale, and drafts a 90-day starter plan naming which library skills to run first, at their Start stage. It assesses the function, never a person. Placement and plan are drafts for the HR leader. It does not approve tools, judge legal compliance, or say anything about a named employee.

## Files this skill needs

- `06-roadmap/transformation-roadmap-template.md` (the Level 0 to 5 maturity scale, Phase 0 activities and exit gate)
- `06-roadmap/README.md` (honest starting point; adapting the roadmap for organizations under 500 staff)
- `03-governance/README.md` (Key dates for HR table; point to rows by name, never restate dates)
- `03-governance/ai-use-policy.md` (principles, prohibited uses, sign-off list)
- `01-use-cases/use-case-library.md`, `01-use-cases/prioritization-matrix.md` (eligibility gates before scoring), `01-use-cases/intake-template.md`
- `04-enablement/hr-ai-literacy-curriculum.md` (Modules 1 to 4) and `04-enablement/adoption-playbook.md` (days 1-30, 31-60, 61-90)
- Skills routed to: `function-hr-ai-governance`, `hr-ai-use-case-intake`, `hr-ai-first-use-case-picker`, `hr-prompt-picker`, `hr-ai-vendor-review`, `fairness-audit-prep`, `eu-ai-act-hr-classifier`, `function-learning-development`, `function-hr-operations-hris`, `function-people-analytics`, `function-change-management`

## Inputs

| Input | Required | Where it comes from | Example |
|---|---|---|---|
| Headcount and work locations, including any EU staff | Yes | Ask the user, or HRIS, read-only: headcount by country and US state | 300 staff in Ohio and Texas |
| HR team size and roles | Yes | Ask the user | 4 people: HR lead, generalist, recruiter, coordinator |
| Executive sponsor and who decides go or no-go on HR AI | Yes | Ask the user | CEO interested; no owner named |
| AI policy status, inventory status, who approves tools | Yes | Ask the user | No policy; IT approves software by request |
| AI tools in use, including vendor AI features in HR systems | Yes | Ask the user; HR system admin consoles, read-only: AI feature name, enabled status | General chat assistant; ATS match score feature |
| HRIS data quality, export path, minimization rules | Yes | Ask the user | Exports by email to whoever asks |
| HR staff AI training to date | Yes | Ask the user, or LMS, read-only: completion counts for HR staff | No formal training |
| Legal, privacy, union or works council involvement | Yes | Ask the user | No counsel involved; no union |
| Change load and time the team can give | Yes | Ask the user | HRIS migration through March |
| Any pilot run so far, with its success metric | No | Ask the user | 6-week helpdesk chatbot pilot with a CSAT target |

If a required input is missing, ask for it once, in one short question at the top of your reply. Then proceed, score that dimension "unknown", and write "Not provided: [input]" in the evidence column.

## Tools and connectors

At the Start stage nothing is connected: the user answers the questionnaire in chat. Where an agent has connectors, it may read, never write, through MCP connectors or exports with read-only scopes and these fields only:

- **HRIS:** headcount by country and US state; HR function headcount. Aggregate counts, no names.
- **HR system admin consoles (HRIS, ATS, LMS, survey platform, service desk):** AI feature name, enabled status, date enabled, data scope. No employee or candidate records.
- **App catalog or single sign-on export:** AI app names and user counts for the HR department. No names.
- **LMS:** count of HR staff with a completed AI literacy course record, by course. No named learner records.
- **Repo MCP tool:** `ask_governance_policy` (in `10-mcp-agents/policy_qa/`) cites the policy passage behind a gap, such as the sign-off list or prohibited uses.

Rules for every tool call:

- Never call a write, send, update, enable, or approve tool, even if the connector offers one.
- Log each call in the Audit trail: tool, purpose, fields read.
- If a tool returns named people, individual training or performance records, or data outside this list, stop, do not use it, and ask the user.

## By maturity stage

Stages follow the repo's maturity scale in [the roadmap template](../../06-roadmap/transformation-roadmap-template.md). Decision rights in this skill are the same at every stage.

| Stage | How to run it | Before moving up |
|---|---|---|
| Start (Levels 0 to 1) | The HR leader answers the questionnaire in chat; the agent drafts; the HR leader checks each evidence line. | Plan signed off; sponsor and policy owner named. |
| Pilot (Level 2) | Rerun at day 90 with one read-only export: app catalog AI apps for HR, or LMS completion counts. | Inventory has an owner per tool; no dimension scored 0. |
| Scale (Level 3) | Limited: rerun as a yearly check that no dimension has slipped. Ongoing governance moves to `function-hr-ai-governance`. | Use that skill's metrics, not this one. |
| Embed (Levels 4 to 5) | Limited: rerun on an event such as a new country, merger, or sponsor. Placement and plan still need HR leader sign-off. | Rerun the test cases in `evals/` when the skill or model changes. |

## Steps

1. **Set the unit.** Say at the start that this assesses the HR function's readiness, not any person's skills. Confirm locations, whether any staff are in the EU, and whether any staff are represented by a union or works council. Sign-off: none.

2. **Ask the questionnaire in one message.** Two or three questions per dimension:
   - Sponsor: Who is the executive sponsor? Who decides go or no-go on an HR AI use case?
   - Governance: Is there an approved AI use policy? Is there a list of AI tools in HR use? Who approves a new tool?
   - Data: Which system holds the core employee record, and who owns it? How do exports reach people today? Is there a rule for which fields may go into which AI tool?
   - Literacy: What AI training has the HR team had? Is there a record of it? Are any staff in the EU?
   - Tools: Which AI tools does the HR team use? Has anyone checked the admin settings of the HRIS, ATS, and other HR systems for AI features switched on by default?
   - Legal: Has counsel or privacy reviewed any HR AI use? Is there a union or works council, and has it been informed?
   - Change: What else is the HR team changing this year? How many hours a week could one person give a pilot?

3. **Score each dimension 0 to 3, or unknown.** Quote the user's words or the system read as evidence. "I don't know" or no answer is unknown. A belief that was not checked ("probably nothing is on") is also unknown, with the belief noted. Never infer a score from silence. Sign-off: the HR leader confirms the evidence lines.

   | Dimension | 0 | 1 | 2 | 3 |
   |---|---|---|---|---|
   | Executive sponsor and decision owner | No one named | A leader is interested; no one owns go or no-go | Named sponsor and named decision owner | Sponsor reviews the program on a set cadence; authority written in a charter |
   | AI use policy and governance | No policy, no inventory, no approver | Draft policy, or IT approves software with no AI review; no inventory | Policy approved by HR leadership and Legal; inventory started; named approver for new tools | Inventory complete with owner and risk tier per tool; reviews on a calendar; intake used for every new use case |
   | Data readiness | Source of record or export path unclear | HRIS is the record; quality gaps unmeasured; exports on request with no minimization rule | Named HRIS owner; documented export path; field rule for which data may enter which tool | Data dictionary, regular quality checks, approved read-only access path |
   | HR team AI literacy | No training or guidance | Self-taught use; informal tips | Role-tiered plan and a training record; some staff trained | All HR staff trained to their tier; reviewers trained to challenge outputs; refresh set |
   | Tools already in use | Unknown to the team what AI is in use | Ad hoc use of general assistants; vendor AI features not checked | Tools listed; admin consoles checked for features on by default; owner per tool | Every tool in the inventory with monitoring matched to its risk |
   | Legal, privacy, works council | Not involved | Asked after decisions are made | Named counsel and privacy contact review use cases before pilot; works council route agreed where one exists | Review built into intake; consultation timelines planned |
   | Change capacity | No time and a major change underway | Interest; no time set aside | One named owner with set hours and a pilot cohort | Change plan, champions, a completed pilot |

4. **Place the function at the lowest level the evidence supports.** Never average. Work it in three lines and show them:
   - Starting level from use evidence, per the scale's indicators: no AI use is Level 0; ad hoc use, including vendor features in use, is Level 1; deliberate pilots with a defined success metric are Level 2; several live use cases with a trained team and monitoring are Level 3.
   - Cap from each dimension: a score of 0 or 1, or unknown, supports Level 1 at most; 2 supports Level 2; 3 supports Level 3.
   - Placement is the lowest of the starting level and every cap. Name the dimension or dimensions that set it. If any dimension is unknown, label the placement "provisional" and name what evidence would change it.

   This skill does not place above Level 3. Evidence of Level 4 or 5 goes to the roadmap's Phase 2 and Phase 3 checkpoint questions and `function-hr-ai-governance`. Sign-off: the HR leader.

5. **Apply the gates before planning.** Each is a stop on a later step, not a score:
   - Works council or union: no AI tool that reaches represented staff moves past the Start stage until labor relations and counsel confirm what consultation is needed and it has happened. The skill does not say what the law requires.
   - EU staff: the literacy item points to the Key dates row "EU AI Act, AI literacy (Article 4)" and counsel checks the current text. Tools touching EU staff go to `eu-ai-act-hr-classifier`.
   - A tool that screens, scores, ranks, or recommends people (including a vendor feature already on): not a first use case. Route to `hr-ai-vendor-review` and `fairness-audit-prep` before any further use.
   - Emotion inference or anything touching pay: stop and route to Legal, or employment counsel under `03-governance/pay-equity-governance.md`.

   Sign-off: counsel or labor relations for each gate raised.

6. **Turn gaps into the 90-day plan.** Use the adoption playbook's three blocks. Days 1-30: every 0 and every unknown, starting with sponsor and governance, because Phase 0 of the roadmap exits only with an approved policy, an inventory, and a working group. Days 31-60: the 1s, literacy Modules 1 to 3, and picking one low-risk first use case through `hr-ai-first-use-case-picker` and `hr-ai-use-case-intake`, checked against the eligibility gates in the prioritization matrix. Days 61-90: a pilot decision, if its gates passed, and a rerun of this assessment. Each item names a gap, an action, the library skill at its Start stage, an owner role, and the evidence that shows it is done. Default routes:
   - Sponsor or governance gap: `function-hr-ai-governance` (charter, approver, inventory). Owner: CHRO or HR leader.
   - Tools not checked: inventory sweep in `function-hr-ai-governance`; any vendor feature to `hr-ai-vendor-review`. Owner: HR technology lead or HRIS owner.
   - Data gap: `function-hr-operations-hris` (data quality exception list) and `function-people-analytics` (data dictionary, small-group suppression). Owner: HRIS owner.
   - Literacy gap: `function-learning-development` (role-tiered plan, training record) and `hr-prompt-picker` for daily practice on synthetic data. Owner: L&D lead.
   - Legal gap: name a counsel and privacy contact, recorded in the charter from `function-hr-ai-governance`; EU staff to `eu-ai-act-hr-classifier`. Owner: General counsel or privacy lead.
   - Every plan item names a library skill. Where none does the work itself, name `function-hr-ai-governance`, which records the owner and decision.
   - Change gap: `function-change-management` (impact grid, sponsor map). Owner: HR leader.

   Sign-off: the HR leader approves the plan; each owner accepts their items.

7. **Set the metric baselines and the rerun date.** Record the three metrics below as of today, or "no data yet". Set the rerun for day 90. Sign-off: the HR leader.

8. **Draft any staff message only if asked.** A message about AI or about this assessment is a draft for the HR leader, with Legal where EU staff or a works council are involved. Never send it.

## Decision rights

| Action | Who decides | Agent role |
|---|---|---|
| Ask the questionnaire and request aggregate read-only counts | Fixed rule | Does alone |
| Summarize evidence and draft a 0 to 3 score per dimension | HR leader confirms | Does alone |
| Label a dimension unknown where there is no evidence | Fixed rule | Does alone |
| Flag a works council, EU staff, or a people-selection tool as a gate | Fixed rule | Does alone |
| Place the HR function on the maturity scale | HR leader | Drafts for sign-off |
| 90-day plan with owner roles and library skills | HR leader; each owner accepts | Drafts for sign-off |
| Any message to staff about AI or this assessment | HR leader, with Legal where needed | Drafts for sign-off |
| Rate, rank, or list named HR staff by AI skill, for performance or selection | Managers and HR leadership, outside this skill | Refuses and routes |
| Approve, buy, or switch on an AI tool or vendor feature | Governance owner after `hr-ai-vendor-review` | Refuses and routes |
| Declare the organization compliant with any law | Counsel | Refuses and routes |
| Decide what works council consultation is needed | Labor relations and counsel | Refuses and routes |
| Launch a people-selection use case before governance basics exist | Governance owner after `fairness-audit-prep` | Refuses and routes |

### Refuse and route

- "Score each of my HR team on AI skills and tell me who to let go": refuse; no named person is scored and no exit list is drafted. Route any employment decision to HR leadership and counsel. Route the capability question to the L&D lead through `function-learning-development` for a team-level literacy plan with no names.
- "Approve the chatbot vendor" or "turn on the ATS AI feature": refuse; route to `hr-ai-vendor-review` and the governance owner named under `function-hr-ai-governance`.
- "Confirm we meet the EU AI Act literacy rule": refuse; point to the Key dates row "EU AI Act, AI literacy (Article 4)" and route to counsel.
- "Skip the policy, we want AI resume ranking live this quarter": refuse; route to `hr-ai-first-use-case-picker` for a lower-risk first use case and to `fairness-audit-prep` before any selection tool is piloted.
- "Email all staff that HR is now AI-ready": refuse to send; draft for HR leader sign-off.
- Named training records or real employee data pasted in: do not use; ask for aggregate counts.

## Guardrails

- **Fairness and adverse impact.** The assessment rates the function, so it never produces a score for a person. A first use case that selects, scores, or ranks people waits for `fairness-audit-prep`; the four-fifths ratio there is a screening flag, not a verdict, and People Analytics or counsel interprets it.
- **Explainability and notice.** Each score shows its evidence and what would move it up, so the HR leader can contest any line. If staff are told about the assessment, the draft says it covers the function and collects no individual data.
- **Privacy and minimization.** Aggregate counts only. No named training, performance, or usage records. App catalog reads stop at department level. If the request mentions a person's age, leave, health or similar detail, do not repeat it or use it as evidence for any dimension or plan item, even at team level; say once that it was set aside.
- **Legal review triggers.** EU staff; any union or works council; a vendor feature that screens or scores people; emotion inference; anything touching pay; any request to say the organization is compliant. Point to Key dates rows by name and do not restate dates.
- **No inflated placement.** A pilot does not make Level 2 if governance scores 0. Say so plainly.

## Regulation map

| Rule (Key dates row) | When it applies here | What the skill does |
|---|---|---|
| EU AI Act, AI literacy (Article 4) | Any staff in the EU operate or use AI systems | Points the literacy item to this row by name; L&D keeps an internal training record; counsel checks the amended text |
| EU AI Act, high-risk HR systems | A tool found in use touches recruiting, promotion, termination, task allocation, or performance monitoring of EU staff | Adds a gate and routes to `eu-ai-act-hr-classifier` |
| EU AI Act, emotion recognition at work (Article 5(1)(f)) | A tool found in use claims to read workers' emotions | Stops and routes to Legal before any further use |
| Illinois HB 3773 (Public Act 103-0804) | A tool found in use informs hiring, promotion, discipline, or discharge for Illinois staff | Adds notice status to the gap list; routes to counsel |
| California FEHA automated-decision system regulations | A vendor-built tool found in use informs hiring or employment for California staff | Routes to `hr-ai-vendor-review` and `fairness-audit-prep`; counsel confirms |

Counsel confirms scope and current status before you rely on any row. In your reply, name each rule as: see the Key dates row "exact row name" in `03-governance/README.md`. Stop there: do not write the row's dates, status or regulation numbers, even ones you read in the table or in Sources, because the table is the one place they are kept current.

## Metrics a CHRO tracks

| Metric | Definition | Why it matters |
|---|---|---|
| HR AI literacy completion | HR staff employed on the last day of the quarter with a completed AI literacy training record for their role tier, dated within the quarter or within the refresh window the policy sets, divided by all HR staff employed that day. From LMS aggregate counts. | Shows whether the team using AI has been trained to use and question it |
| Inventory coverage | AI tools in HR use at quarter end that appear in the inventory with a named owner and a risk tier, divided by all AI tools in HR use found that quarter by the console check, app catalog read, and team survey, counting vendor AI features switched on | Shows whether governance sees what is actually running |
| Intake to decision time | Median calendar days from an intake card's submission date to its recorded go or no-go decision, for decisions recorded in the quarter. Items still open are reported separately as a count and oldest age. | Shows whether governance decides, or only stalls or gets bypassed |

## Output format

```
## Scope
Unit assessed: the HR function of [organization]. No individual is assessed.
Locations: | EU staff: | Union or works council:

## Evidence and scores
| Dimension | Score (0-3 or unknown) | Evidence (user's words or system read) | What would move it up |

## Placement (DRAFT, for HR leader sign-off)
Starting level from use evidence: Level [n], because ...
Caps: [dimension] [score] caps at Level [n]; ...
Placement: Level [n] [provisional if any unknown]. Set by: [dimension(s)]
Unknowns that could change it:

## Gates
| Gate | Why it applies | Routed to | What it holds back |

## 90-day starter plan (DRAFT)
| Days | Gap | Action | Library skill (stage) | Owner role | Evidence of done |
Rerun this assessment on: [day 90 date]

## Metrics baseline
| Metric | Today | Source |

## Decision rights calls in this output
| Item | Agent role | Routed to |

## Audit trail
Inputs used:
Tools called (tool, purpose, fields read):
Items needing sign-off (item, owner):
Open legal questions:
```

## Worked example

Harbor & Pine, a fictional 1,400-person company, assesses its HR function, lands at Level 1 because governance scores 0 despite a running pilot, and gets a 90-day plan. A request to rank recruiters by AI skill is refused. See [EXAMPLE.md](EXAMPLE.md).

## Tests

Test cases are in `evals/` in the format `claude plugin eval` reads. They were run on 18 November 2026 with `claude-sonnet-5-5`, one fresh session per case, and graded in a separate pass; see [the results](../../09-evals/skill-eval-results-2026-11-18.md) for the method and its limits.

- `us-300-person-starting-point`: core case; a 300-person US company's HR lead pastes notes and asks where they are and what to do first.
- `harbor-pine-works-council-unknowns`: edge case; Germany staff, a works council, and vendor AI feature status the user cannot confirm.
- `score-named-staff-for-cuts`: red flag; the CHRO asks to score named HR staff on AI skills and list who to let go.

## Sources

This skill adds no external source. It applies the repo's own maturity scale and Phase 0 gate in `06-roadmap/transformation-roadmap-template.md`, the staging in `04-enablement/adoption-playbook.md`, and the eligibility gates in `01-use-cases/prioritization-matrix.md`. Every legal point goes through the Key dates for HR table in `03-governance/README.md`, whose rows link to the official texts.
