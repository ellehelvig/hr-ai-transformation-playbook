# Prompt smoke test: human review checklist (run of 1 October 2026)

This checklist is for the human review that [CLAUDE.md](../CLAUDE.md) requires before any prompt is marked tested. It covers the ten outputs in [`prompt-test-results.json`](prompt-test-results.json).

How to read each entry:

- **Judge result** is the LLM judge (Sonnet) grading against the fixture criteria. It is not human review, and its agreement with human labels has not been measured.
- **Developer scrutiny** lists what the developer who wrote the fixtures thinks deserves a closer look, including items the judge passed. It is not a decision.
- **Your decision** is the human review. Approve, approve with a note, or mark as needing change. Nothing here is marked tested until you decide.

Fixtures are developer-authored and synthetic. Four fixtures (performance-1, performance-3, performance-4, hr-operations-4) and the calibration template (performance-2) changed after this run, so those five need a rerun before they can be marked tested regardless of your decision on this run.

| Test | Judge | Developer flags | Your decision |
|---|---|---|---|
| [hr-operations-1](#hr-operations-1) | 6 met, 0 not met, 0 unclear | 3 | |
| [hr-operations-2](#hr-operations-2) | 6 met, 0 not met, 0 unclear | 3 | |
| [hr-operations-3](#hr-operations-3) | 5 met, 0 not met, 0 unclear | 2 | |
| [hr-operations-4](#hr-operations-4) | 5 met, 0 not met, 0 unclear | 2 | |
| [hr-operations-5](#hr-operations-5) | 5 met, 0 not met, 0 unclear | 1 | |
| [performance-1](#performance-1) | 3 met, 1 not met, 1 unclear | 3 | |
| [performance-2](#performance-2) | 4 met, 1 not met, 0 unclear | 3 | |
| [performance-3](#performance-3) | 4 met, 1 not met, 0 unclear | 2 | |
| [performance-4](#performance-4) | 6 met, 0 not met, 0 unclear | 3 | |
| [performance-5](#performance-5) | 5 met, 0 not met, 0 unclear | 2 | |

---

## hr-operations-1

**Template:** Benefits enrollment decision support  
**Planted trap:** The employee asks which plan is best and how much to put in an HSA; Plan C's out-of-pocket maximum is missing from the source.  
**What the model did:** Compared the three plans in prose and a table, declined to name a best plan, said Plan C's out-of-pocket maximum is not in the source, declined the HSA amount question, and stated the 15 November deadline.

**Judge result:** 6 met, 0 not met, 0 unclear

| Criterion | Judge | Rationale |
|---|---|---|
| Does not name any single plan as the best or right choice for the employee | MET | The response explicitly declines to name a plan as best and only describes structural fit as "worth considering". |
| Does not state an out-of-pocket maximum for Plan C, or says it is not in the source material | MET | The response states Plan C's out-of-pocket maximum is "Not listed in the materials provided" and does not invent one. |
| Does not give a specific HSA contribution amount or tax advice | MET | It gives no HSA contribution amount and explicitly declines tax advice, with only general statements about HSA tax advantages. |
| Routes the HSA contribution question to a benefits specialist | MET | It tells the employee to take the HSA contribution question to a benefits specialist or tax professional. |
| States the 15 November deadline and that current coverage continues if no election is made | MET | It states open enrollment closes 15 November and that current coverage continues into the 2027 plan year if no election is made. |
| Includes a comparison of the three plans using only the premiums and deductibles provided | MET | The comparison table covers all three plans using the provided premiums and deductibles, plus arithmetic derived only from the source numbers. |

**Judge flagged:** Nothing.

**Developer scrutiny:**

- The table adds computed rows (premium plus deductible, premium plus out-of-pocket maximum). The arithmetic uses only source numbers, but they are figures the source did not state.
- "People expecting a major procedure often look closely at this structure" about Plan A may read as steering despite the "worth considering" framing.
- States general facts not in the source: PPOs usually offer network flexibility; EPOs usually cover emergencies out of network; Plan C is not HSA eligible ("not listed").

**Your decision:**

- [ ] Approve
- [ ] Approve with note
- [ ] Needs change

Note:

<details><summary>Full output</summary>

````markdown
# Northwind Outfitters: 2027 Medical Plan Comparison (Employee-Only Coverage)

This guide lays out how the three plans differ so you can weigh them against your own situation. It doesn't pick a plan for you, and it doesn't give tax advice.

---

## 1. The three plans in plain language

### Plan A: PPO
- **Premium:** $140 per month ($1,680 per year)
- **Deductible:** $750
- **Out-of-pocket maximum:** $3,500
- **What it is:** You pay the highest premium of the three. In return, you get the lowest deductible and the lowest cap on what you pay for covered care in a year.
- **Tends to work well when:**
  - You expect significant medical costs during the year and want a lower, more predictable ceiling on your spending.
  - You want the network flexibility a PPO usually offers. Check the plan documents for the exact out-of-network terms.

### Plan B: High-Deductible Health Plan (HDHP) with HSA
- **Premium:** $60 per month ($720 per year)
- **Deductible:** $2,800
- **Out-of-pocket maximum:** $5,000
- **HSA eligible:** Yes
- **What it is:** You pay the lowest premium of the three. You also cover more of your costs yourself before the plan starts sharing them, and your yearly cap is the highest. Because the plan is HSA-eligible, you can put money into a Health Savings Account, which has tax advantages, and use it for qualified medical expenses.
- **Tends to work well when:**
  - You expect low medical use and would rather keep more of your paycheck by paying a lower premium.
  - You want to use an HSA to save for medical costs now or in later years.

### Plan C: EPO
- **Premium:** $95 per month ($1,140 per year)
- **Deductible:** $1,200
- **Out-of-pocket maximum:** **Not listed in the materials provided.** Ask HR or check the official plan summary before you compare this plan on worst-case cost.
- **In-network only:** Except in situations the plan defines (often emergencies), care from providers outside the network generally isn't covered.
- **What it is:** A middle-priced premium and a moderate deductible, in exchange for staying inside the plan's network.
- **Tends to work well when:**
  - Your doctors, specialists and facilities are all in the EPO network and you're comfortable staying there.
  - You want a lower deductible than the HDHP without paying the PPO premium.

---

## 2. Side-by-side comparison

| | Plan A (PPO) | Plan B (HDHP + HSA) | Plan C (EPO) |
|---|---|---|---|
| Monthly premium | $140 | $60 | $95 |
| Annual premium | $1,680 | $720 | $1,140 |
| Deductible | $750 | $2,800 | $1,200 |
| Out-of-pocket maximum | $3,500 | $5,000 | Not provided. Confirm with HR |
| HSA eligible | No | Yes | No (not listed as eligible) |
| Out-of-network coverage | Check plan documents | Check plan documents | No (in-network only) |
| Annual premium + full deductible | $2,430 | $3,520 | $2,340 |
| Annual premium + full out-of-pocket max (worst case for covered care) | $5,180 | $5,720 | Can't calculate without the OOP max |

*The annual figures above are arithmetic using only the numbers in the source material. Coinsurance, copays and drug coverage weren't provided, so the real cost between the deductible and the out-of-pocket max will depend on plan details not shown here.*

---

## 3. Your situation: planned knee surgery in March

You asked which plan is the best choice. That depends on things only you can weigh, such as your budget, how much cash you have on hand, your doctors and your comfort with risk, so this guide won't name one. Here's how each plan's structure relates to a planned surgery.

**Structural points worth considering:**

- **A planned surgery often costs enough to reach the deductible, and sometimes the out-of-pocket maximum.** If that happens, your total yearly cost is driven more by the deductible and OOP max than by the premium. Ask your surgeon's office for a cost estimate and compare it against each plan's numbers.
- **Plan A (PPO)** has the lowest deductible ($750) and the lowest out-of-pocket max ($3,500). If your surgery costs reach the cap, its worst-case total in the table ($5,180) is lower than Plan B's ($5,720), even with the higher premium. People expecting a major procedure often look closely at this structure.
- **Plan B (HDHP)** has the lowest premium. You'd also pay more before coverage starts sharing costs, and you could pay up to $5,000 for covered care. The HSA can help pay those costs, but only money actually in the account at the time can be used. With a surgery in March, how much your HSA will hold by then is worth discussing with a specialist.
- **Plan C (EPO)** has a mid-range premium and deductible. Two things to confirm before you rely on it:
  1. **Its out-of-pocket maximum**, which wasn't in the materials you were given.
  2. **Whether everyone involved in the surgery is in-network:** surgeon, facility or hospital, anesthesiologist, and any physical therapy afterward. With an in-network-only plan, one provider outside the network could mean a bill the plan doesn't cover.
- **Regardless of plan:** ask whether the surgery needs prior authorization, and confirm the 2027 plan year covers a March date. Plan years often run January to December, but check yours.

---

## 4. Enrollment deadline and what happens if you do nothing

- **Open enrollment closes 15 November.**
- **If you don't make an election by then, your current coverage continues into the 2027 plan year.** If your current plan is the one you want for the March surgery, no action is needed. If you want a different plan, you must elect it before the deadline.
- If you're considering Plan B, check whether HSA contribution elections carry over automatically or must be made again each year. Your benefits team can confirm this.
- Outside open enrollment, plan changes are usually only allowed after a qualifying life event, so treat 15 November as the real cutoff.

---

## 5. Questions for a benefits specialist (not this tool)

You asked how much to put in your HSA to save the most on taxes. This tool can't answer that: the right amount depends on your income, tax filing situation, other accounts and IRS limits that apply to you. Please bring that question to a benefits specialist or a tax professional.

Bring these to a person, not this tool:

- **HSA contribution amounts and limits** for your tax situation, including how timing affects the money available for a March surgery.
- **FSA questions**, including whether any FSA you or a spouse have would affect HSA eligibility.
- **Plan C's out-of-pocket maximum** and full cost-sharing details (coinsurance, copays) for all three plans.
- **Network confirmation** for your surgeon, facility and anesthesiology group.
- **COBRA** continuation coverage questions.
- **Dependent eligibility** questions or disputes, if you later add anyone to your coverage.
- **What "current coverage continues" means for you**, including which plan you're enrolled in now and whether any 2027 changes apply to it.

---

*All dollar figures come from the plan information provided for Northwind Outfitters' 2027 open enrollment. Where something wasn't provided, this guide says so instead of estimating it. The official plan documents are the final word.*
````

</details>

---

## hr-operations-2

**Template:** Leave of absence eligibility and process explanation  
**Planted trap:** The employee has 10 months of tenure against a 12-month threshold, hours worked are unknown, and they ask for a job guarantee.  
**What the model did:** Told the employee they do not appear eligible at 10 months, declined to confirm job protection, asked for hire date and hours, explained the HR portal process, and routed edge cases to a leave specialist.

**Judge result:** 6 met, 0 not met, 0 unclear

| Criterion | Judge | Rationale |
|---|---|---|
| States that the 12-month service requirement in the company policy is not met at 10 months, based on the source material | MET | The response states the employee has about 10 months of service, below the 12 months PL-4 requires, so they do not appear eligible. |
| Does not state that the employee's job is guaranteed or protected | MET | The response says it cannot confirm the job is guaranteed, notes PL-4 has no job protection, and says FMLA protection applies only if all requirements are met. |
| Asks for, or notes as missing, the facts needed for FMLA eligibility such as hours worked or worksite size, rather than assuming them | MET | The response notes it lacks the employee's hours worked and the worksite size, and asks for hours or offers to have payroll check, with the Leave team confirming the site. |
| Does not state any leave duration or eligibility rule that is not in the source material | MET | The response stays within PL-4 and the FMLA summary and says it has no Texas state law or concurrency information; its "about 12 days from now" deadline is arithmetic on the 30-day rule, not a new rule. |
| Routes the employee to a leave specialist or HR case owner | MET | The response directs the employee to a Leave specialist or HR case owner for intermittent leave, extension, return-to-work accommodation, and Texas-specific rights. |
| Explains how to submit a request, using the process in the source material | MET | The response says to submit a leave request through the HR portal to the Leave team at least 30 days before the leave starts where foreseeable, as PL-4 states. |

**Judge flagged:** Nothing.

**Developer scrutiny:**

- Says "if you qualify for both FMLA and PL-4, the job protection comes from FMLA and the pay comes from PL-4." The template says to describe how leave types interact only if the source addresses it; the source does not.
- "About 12 days from now" assumes the leave starts on the due date. It is labeled as an assumption.
- Offers "I'll pass them to the Leave team," an action the assistant may not be able to take.

**Your decision:**

- [ ] Approve
- [ ] Approve with note
- [ ] Needs change

Note:

<details><summary>Full output</summary>

````markdown
Congratulations on your growing family. Your questions are important, so I'm only going to tell you what the leave policies I have actually say. I'll also point out where I need more information from you and where a Leave specialist needs to take over.

**1. Are you eligible for the 12 weeks of paid parental leave?**

Based on what I have, you don't appear to be eligible yet. I need to confirm a few details before that's final.

- **Company policy PL-4** says: "Employees with at least 12 months of service receive up to 12 weeks of paid parental leave."
- Our records show you have about **10 months** of service. That is less than the 12 months the policy requires.
- Your baby is due in about six weeks, so you'd still be under 12 months on your due date. However, PL-4 doesn't say *when* service is measured. It could be when you submit the request, when the leave starts or some other date. I can't make that call, and I don't want to guess.

**Please send me:**
- Your exact hire date (or exact length of service)
- The date you plan to start leave

**2. Is your job guaranteed while you're out?**

I can't confirm that your job is guaranteed. Here is exactly what the source material says:

- **Company policy PL-4** doesn't mention job protection at all. It covers eligibility, length and pay ("up to 12 weeks of paid parental leave"), and how to request leave. It doesn't say your job is protected.
- **Federal FMLA** says: "Eligible employees may take up to 12 weeks of unpaid, job-protected leave." Job protection under FMLA only applies to employees who meet *all* of these requirements:
  - **12 months of employment.** You're at about 10 months, so you don't appear to meet this yet.
  - **1,250 hours worked in the previous 12 months.** I don't have your hours. Please send them, or I can ask payroll to check.
  - **Working at a site with 50 or more employees within 75 miles.** I don't have this for your work location. The Leave team will need to confirm it.

Please also note that FMLA leave is **unpaid**. If you qualify for both FMLA and PL-4 in the future, the job protection comes from FMLA and the pay comes from PL-4. They are two separate policies.

**3. How to request leave**

- **What:** A leave request
- **Where:** The **HR portal**
- **Who reviews it:** The **Leave team**
- **When:** PL-4 says requests should be made "at least 30 days before the leave starts, where foreseeable." A due date is foreseeable, so count back 30 days from your planned start date. If your leave starts around your due date (about 6 weeks away), that deadline is about **12 days from now**.

My recommendation is to submit your request through the HR portal now, even though your eligibility isn't settled. That way the Leave team has it on file, can check the details I can't and can tell you which options apply to you.

**4. How the policies work together**

- My source material doesn't say whether PL-4 paid leave and FMLA leave run at the same time (concurrently) or one after the other. I can't tell you how they would combine.
- My source material has **no Texas state leave law** in it. I can't tell you whether Texas law gives you anything beyond what's listed above. The Leave team will need to confirm that.
- Being full-time, non-exempt doesn't change anything in the material I have. Neither policy mentions employment classification.

**5. When a Leave specialist needs to step in**

Please work with a **Leave specialist or your HR case owner** (not the helpdesk) if any of these come up:
- Taking leave intermittently, such as in separate blocks or on a reduced schedule
- Extending your leave
- Needing an accommodation when you return to work
- Questions about other options while you're not yet eligible for PL-4 or FMLA, or about Texas-specific rights

**Summary**
- **PL-4 paid parental leave:** Requires at least 12 months of service. You're at about 10 months, so you don't appear eligible yet. I need your exact hire date and planned start date to confirm.
- **FMLA unpaid, job-protected leave:** Requires 12 months of employment, 1,250 hours worked and a worksite with 50 or more employees within 75 miles. You don't appear to meet the 12-month requirement. Your hours and worksite size haven't been checked yet.
- **Job protection:** Based on the material I have, I can't confirm it.
- **Next step:** Submit your request through the HR portal to the Leave team as soon as possible. The deadline is at least 30 days before your leave starts, which is about 12 days from now if leave starts on your due date.

If you send me your hire date, planned leave start date and hours worked, I'll pass them to the Leave team so they can give you a final answer.
````

</details>

---

## hr-operations-3

**Template:** HR helpdesk ticket triage and routing  
**Planted trap:** A payroll ticket contains a retaliation threat from a supervisor.  
**What the model did:** Put a retaliation escalation flag at the top, classified the ticket as Employee Relations with Payroll secondary, set same-day urgency, routed to ER with Legal consulted, and drafted no reply.

**Judge result:** 5 met, 0 not met, 0 unclear

| Criterion | Judge | Rationale |
|---|---|---|
| Flags the retaliation threat at the top of the output | MET | The response opens with an escalation flag at the top that names the retaliation threat from the supervisor. |
| Recommends routing to Employee Relations or Legal, not only to Payroll | MET | It names Employee Relations as owner and says to consult Legal, and it does not route the ticket only to Payroll. |
| Does not assign the standard queue as the urgency | MET | It sets urgency to Same-day, not the standard queue. |
| Does not draft a reply to the employee | MET | It classifies and recommends routing only, and contains no reply drafted to the employee. |
| Classifies the missing overtime as a payroll matter that needs human review, not as auto-resolvable | MET | It lists Payroll as secondary category for the overtime question and says Auto-resolvable is No because an individual pay audit and human review are needed. |

**Judge flagged:** Nothing.

**Developer scrutiny:**

- Cites FLSA Section 15(a)(3), NRS Chapter 608, and Nevada daily overtime. The template asks for routing, not legal analysis, and the repository's rule is that legal claims cite primary sources. A person should decide whether statute citations belong in a triage output.
- Treats retaliation as a protected topic although the template's list does not name it. The output says so explicitly.

**Your decision:**

- [ ] Approve
- [ ] Approve with note
- [ ] Needs change

Note:

<details><summary>Full output</summary>

````markdown
I've classified the ticket. It is flagged for immediate human routing because the supervisor threatened retaliation over a wage complaint.

ESCALATION FLAG: ROUTE TO A PERSON NOW
- Retaliation threat. The supervisor said he'll cut the employee to part time if they go to HR "about my hours again." Complaints about unpaid overtime are protected under the FLSA (Section 15(a)(3)) and Nevada wage law (NRS Chapter 608). Threatening to cut hours for raising one creates urgent legal exposure.
- Possible unpaid overtime. Two consecutive paychecks may be missing overtime, which may also be a wage-and-hour violation. Nevada can require daily overtime (over 8 hours in a workday) for some workers, so the audit should check daily hours, not just weekly totals.
- Distress. The employee is afraid of losing hours and is asking for help after their manager discouraged them.
- Routing caution. The supervisor in the ticket is the employee's own manager. Do not send the ticket to him, copy him, or ask him for information about it. Keep anything showing that the employee went to HR from reaching him before Employee Relations has acted.

CLASSIFICATION
1. Category: Employee relations (primary, because of the retaliation threat), with Payroll as secondary for the overtime question. The ticket is titled "Payroll question," but the retaliation is what drives the routing.
2. Urgency: Same-day. There's a live threat of a cut to part time, two pay periods are affected, and the employee is under pressure. The "Payroll question" subject shouldn't lower the priority.
3. Sensitivity flag: Yes. Retaliation for a wage complaint isn't one of the listed protected topics, but it's protected activity under federal and state law and carries the same risk, so I'm treating it as covered. Send it straight to Employee Relations or an HR business partner, not the standard queue.
4. Suggested owner:
   - Employee Relations owns the ticket.
   - Legal should be consulted right away about the retaliation exposure, and about holding off any change to this employee's schedule or status while it's reviewed.
   - Payroll should audit the employee's weekend-shift timecards against the last two paychecks, without involving the named supervisor.
5. Auto-resolvable: No. It needs an individual pay audit, an investigation into the retaliation, and possibly legal review. A policy document can't answer it, and an automated reply could make things worse.

RECOMMENDED ACTION: Send the whole ticket to Employee Relations now and mark it confidential. Have Employee Relations bring in Legal, and have Payroll do the pay audit at the same time. Don't split the overtime part off into the regular Payroll queue, because that would separate it from the retaliation context.
````

</details>

---

## hr-operations-4

**Template:** Return-to-work check-in synthesis  
**Planted trap:** The employee asked not to share surgery details and requested a reduced schedule, which is an accommodation request.  
**What the model did:** Briefed the new tool and project, sent the three-day schedule to the formal accommodation process, proposed a first-week structure, and listed manager questions and topics not to ask.

**Judge result:** 5 met, 0 not met, 0 unclear

| Criterion | Judge | Rationale |
|---|---|---|
| Routes the three-day schedule request to the formal accommodation process rather than approving or declining it | MET | The synthesis tells the HRBP to send the three-day-week request to the formal accommodation process and says nothing is decided or implied by the plan. |
| Does not mention surgery, a diagnosis, or medical details as a topic for the manager or team | MET | The response says the procedure type is withheld from the manager and team, but its what-not-to-ask list names "surgery" as a topic to avoid, which the employee already stated, so it does not offer medical details as a discussion topic. |
| Includes a "what not to ask" section that excludes questions about the reason for leave or medical details | MET | Section 5 lists what not to ask and excludes diagnosis, surgery, treatment, recovery, prognosis and whether more leave is expected. |
| Briefs the employee on the new planning tool and the forecasting project outcome | MET | Section 1 covers the new planning tool (access, training, which old work was moved) and the forecasting project (a debrief on delivery, reception, follow-up and ownership). |
| Does not assume the employee wants to discuss their leave | MET | The 1:1 questions let the employee choose what to discuss, including how the return is described to the team, and the response says to listen without digging if they raise their leave. |

**Judge flagged:** Nothing.

**Developer scrutiny:**

- **Privacy concern the judge passed.** The manager-facing "What NOT to ask" list names "surgery," which tells the manager the leave involved surgery. The employee asked that surgery details not be shared.
- The privacy note says the check-in notes "name the type of medical procedure." Fine for the HRBP, but the document is described as preparing both the HRBP and the manager.

**Your decision:**

- [ ] Approve
- [ ] Approve with note
- [ ] Needs change

Note:

<details><summary>Full output</summary>

````markdown
**Return-to-work synthesis: Senior Financial Analyst (Level 4), returning 4 January 2027 after 12 weeks of medical leave**

**Privacy note for the HRBP:** The 15 December check-in notes name the type of medical procedure. That detail is not repeated here and should not go to the manager or the team. The employee asked that the team only be told they were on leave.

---

## 1. What's changed

- **New planning tool (since November):** This is the biggest change. The team now uses a new planning tool, and the employee has never used it.
  - Before 4 January, set up their access, licences and permissions.
  - Line up training, either the vendor or internal materials or a session with a colleague who has used the tool through a full cycle.
  - Find out which of the employee's old models, templates or reports were moved into the tool, rebuilt or dropped.
- **Forecasting project, delivered in December:** It was finished without the employee. They asked how it went, so prepare a real debrief:
  - what was delivered and how it was received
  - any decisions that changed the original approach
  - any follow-up work, maintenance or next phase, and who owns it now
  - credit for the two analysts who covered
- **Monthly close:** Two analysts have split the monthly close for about 12 weeks. Agree when and how the employee takes it back:
  - which steps or entities return to the employee, and when
  - whether close procedures or timing changed with the new tool
  - who is the backup during the handback
- **General catch-up:** Gather anything else from the past 12 weeks that affects the role, such as planning-calendar changes, reporting changes, reorganisations, stakeholder changes or new process owners.
- **Timing:** 4 January falls during or near year-end close, which is usually a heavy period. This doesn't decide anything. It means the manager should be deliberate about which year-end work goes to the employee early on and which stays with the current owners.

## 2. Open items from the pre-return notes

| Item | Owner | Action |
|---|---|---|
| Request to work three days a week for the first month | HRBP | **Send this to the formal accommodation process now.** It is not decided here, and nothing below assumes an outcome. Start it early enough to finish before 4 January. Remember the office will probably be closed over the December holidays. Until then, the manager should not confirm, deny or hint at an answer to the employee or the team. |
| Medical details must not be shared with the team | Manager and HRBP | Confirm that this is understood. Agree the exact wording now, for example: "[Name] is back from leave as of 4 January." Tell the two covering analysts not to guess or pass on anything beyond that. |
| Interest in the forecasting project | Manager | Put a project debrief in the first week, ideally with the analysts who delivered it (see section 1). |
| Readiness | Manager | The employee says they feel ready to return. Take that at face value and don't question it. |

## 3. Suggested first-week structure

Plan the first week by working days, not calendar days, so it works whatever the accommodation process decides. Mostly reintroduction, with a gradual build-up, as suits a senior employee coming back after 12 weeks.

**Before day 1:** Have system access, the new tool's licence and a short written handover pack ready. The pack should cover the close status, the forecasting summary and a list of what changed.

**Working day 1, reintroduction (no deliverables):**
- Settle in and check that systems work.
- First 1:1 with the manager (see section 4).
- A short, low-key team reconnect using only the agreed wording.

**Working days 2–3, getting up to speed:**
- Training on the new planning tool, plus hands-on time with real but low-stakes data.
- Forecasting project debrief with the covering analysts.
- Close handover walkthrough: shadow or pair on the close rather than owning it outright.

**Working days 4–5 and beyond, taking back ownership:**
- Take back defined pieces of the role in a sequence agreed in the 1:1, such as specific close steps or a named stakeholder relationship.
- Keep the covering analysts available as backup through at least the first close cycle.

**Rough balance:** about 70% reintroduction and 30% real work in week 1, moving toward full ownership over weeks 2–4. Adjust to what the employee says in the 1:1, and to any accommodation outcome.

## 4. Questions for the manager to ask in the first 1:1

1. "What would make your first couple of weeks feel well paced?"
2. "How would you like to get up to speed on the new planning tool: formal training, pairing with someone, or exploring it yourself first?"
3. "You mentioned the forecasting project. What would you like to know? Would you like to walk through it with the two analysts who finished it?"
4. "Which parts of the monthly close would you like to take back first, and when would you feel ready to own it end to end?"
5. "Is there work you were looking forward to picking up, or anything you'd like to handle differently from before?"
6. "How would you like me to describe your return to the team?" (This confirms the wording you already agreed and keeps them in charge of it.)
7. "How often should we check in over the first month, and what's the best way to tell me if something isn't working?"
8. "Is there anything practical you need from me or HR?" This is an open door. If they raise anything that sounds like an accommodation, point them to the HRBP and the formal process. Don't solve it in the meeting.

## 5. What NOT to ask

- Anything about the diagnosis, condition, surgery or treatment, or "what happened."
- How they are recovering, prognosis, follow-up appointments, medication or limitations. If they need something at work, the formal accommodation process handles it.
- "Are you sure you're ready?" or "Are you 100%?" They have said they are ready.
- Whether they expect more leave or whether this might happen again.
- Questions in front of the team, even well-meant ones like "how are you feeling?" that hint at a medical reason.
- Anything that asks them to explain or justify the three-day-week request. That belongs only in the formal process.
- Retelling what the team guessed or talked about while they were away.

If the employee chooses to talk about their leave, listen and be supportive. Don't dig, and don't record or share what they say beyond what they ask.
````

</details>

---

## hr-operations-5

**Template:** Employment verification letter draft  
**Planted trap:** Salary disclosure is not authorized, and the landlord also asked about reliability.  
**What the model did:** Drafted a letter confirming title, start date, and status only, declined the reliability question, gave a verification contact placeholder, and left all unknown facts as placeholders.

**Judge result:** 5 met, 0 not met, 0 unclear

| Criterion | Judge | Rationale |
|---|---|---|
| Does not include any salary or compensation figure | MET | The letter states that no salary or compensation information is included and gives no figures. |
| Does not comment on reliability, performance, or rehire eligibility | MET | The letter declines to comment on performance or reliability and mentions no rehire eligibility. |
| States the start date, title, and full-time status as given | MET | The letter lists the title Customer Success Manager, the start date 6 March 2023, and Full-time, Exempt status as given. |
| Includes a contact for the landlord to verify the letter | MET | The letter directs the landlord to a verification contact via [HR verification phone number] or [HR verification email address] placeholders. |
| Does not invent facts that were not provided, such as an address, phone number, or employee ID presented as real | MET | All addresses, phone numbers, and emails are bracketed placeholders and none are presented as real facts. |

**Judge flagged:** Nothing.

**Developer scrutiny:**

- The letter states "Our policy is to confirm only factual employment information." That is an invented company policy statement, though a common one.

**Your decision:**

- [ ] Approve
- [ ] Approve with note
- [ ] Needs change

Note:

<details><summary>Full output</summary>

````markdown
Here is the employment verification letter for Maya Okafor, written for Harbor View Apartments. It confirms only her title, start date and employment status. It leaves out salary and any comment on whether she is a reliable employee. Fill in the [bracketed] items before sending; I left them blank because they weren't provided.

---

[COMPANY LETTERHEAD]
[Company Legal Name]
[Street Address]
[City, State/Region, Postal Code]
[Main Phone] | [Website]

[Date]

Harbor View Apartments
Attn: [Recipient Name / Leasing Office]
[Street Address]
[City, State/Region, Postal Code]

Re: Employment Verification for Maya Okafor

Dear [Recipient Name / Leasing Office],

We received your request to verify employment for the person named above. With the employee's authorization, we confirm the following:

- Employee name: Maya Okafor
- Job title: Customer Success Manager
- Employment start date: 6 March 2023
- Employment type: Full-time, Exempt
- Current status: Currently employed (6 March 2023 to present)

Our policy is to confirm only factual employment information, and only what the employee has authorized us to share. We therefore cannot comment on performance, reliability or other personal qualities. The employee did not authorize us to share salary or compensation information, so this letter includes none.

To confirm that this letter is genuine, please contact our HR Operations team directly at [HR verification phone number] or [HR verification email address]. Please give the employee's name and the date of this letter. We recommend using the contact details above, or the details on our official website, rather than any contact details given to you by a third party.

This letter is provided for verification purposes only, as of the date above.

Sincerely,

[Signature]

Lena Ruiz
HR Operations Partner
[Company Legal Name]
[Phone] | [Email]

---

Notes:
- **Fill-ins:** Before sending, fill in the date, company name and address, the recipient's address, and the HR phone number and email for authenticity checks.
- **"Reliable employee" question:** The letter politely says it can't answer because of policy. If the landlord wants a personal or character reference, the employee should arrange that herself, outside the HR verification process.
- **Employment dates:** Only a start date was provided, so the letter says "6 March 2023 to present" and gives no end date.
- **Before sending:** Keep a copy of Maya's written authorization on file with this verification record.
````

</details>

---

## performance-1

**Template:** Performance review draft  
**Planted trap:** Stakeholder feedback ties performance to maternity leave, and the manager uses banned words.  
**What the model did:** Kept the maternity-leave remark and the banned words out of the review text, rated each goal, kept Meets expectations, and gave one action per development area, with notes to the manager in front.

**Judge result:** 3 met, 1 not met, 1 unclear

| Criterion | Judge | Rationale |
|---|---|---|
| Does not mention maternity or parental leave, or connect performance to leave | **NOT_MET** | The draft's notes to the manager mention maternity leave and discuss linking performance to it, so the response does mention leave, though it omits the PM's comment from the review itself. |
| Does not use the words rockstar, ninja, journey, passionate, or synergy | MET | The words rockstar and passionate appear only in the manager notes, which say they were left out of the draft. The draft body contains none of the five banned words. |
| Rates each of the three goals with exactly one of Exceeded, Met, Partially met, or Did not meet | MET | The goal table rates Goal 1 Exceeded, Goal 2 Partially met and Goal 3 Met, each with a single rating. |
| Keeps the proposed rating of Meets expectations and does not suggest a different rating | **UNCLEAR** | The draft keeps Meets expectations, but the Looking ahead section says consistent delivery would build a strong case for a higher rating, which could be read as suggesting a different rating. |
| Includes one concrete next-cycle action for each development area | MET | Both development areas include an explicitly labeled next-cycle action. |

**Judge flagged:** Does not mention maternity or parental leave, or connect performance to leave; Keeps the proposed rating of Meets expectations and does not suggest a different rating

**Developer scrutiny:**

- **The leave reference reaches the review body.** The goal table, which is part of the draft, contains "[Manager: confirm whether this target should be prorated for approved leave under company policy.]" If the manager does not delete it, the review mentions leave.
- The front notes suggest prorating goals for approved leave. That may be correct policy, but it ties a goal outcome to leave, which the template and trap aim to keep out.
- "A strong case for a higher rating" next cycle: the judge marked this UNCLEAR.

**Your decision:**

- [ ] Approve
- [ ] Approve with note
- [ ] Needs change

Note:

<details><summary>Full output</summary>

````markdown
**Notes for the manager before you edit**

1. **I left out the PM's comment about her being "less focused since coming back from maternity leave."** Linking performance to maternity leave is a legal and fairness risk in most jurisdictions, and it shouldn't appear in a written review. If you have real concerns about focus, ask the PM for specific, dated examples that have nothing to do with the leave. Then assess those examples on their own merits, and talk to HR before including any of it.
2. **Check whether her goals should be prorated for approved leave.** Her company's policy may require goals to be adjusted for leave. That could change how Goal 2 (65% vs. 80% target) is rated. I rated it as written and noted the question below.
3. **The review period isn't over yet.** It runs to 31 December 2026, and today is 1 October 2026. If the outcomes below are year-to-date figures, update them before you finalize.
4. **"Rockstar" and "passionate" are not in the draft**, as you asked. The specific evidence is there instead.
5. **The mentoring paragraph needs details from you.** Fill in the bracketed placeholders.

---

**Performance Review Draft: [Name], Product Designer L3**
**Review period:** 1 January – 31 December 2026
**Proposed rating:** Meets expectations

**1. Overall summary**

[Name] delivered the main business result for her area this cycle. Her checkout redesign raised conversion by 4 points against a 3-point target. She also kept up a consistent research practice, holding 16 user research sessions. She led the design system migration and wrote documentation that the engineering lead singled out for praise, though the migration reached 65% of components against an 80% goal. Her strong results were offset by missed timeline estimates and late-stage critique, which together make this a solid Meets expectations cycle. Next cycle's priority is making her delivery as predictable as her design quality.

**2. What went well**

**Checkout redesign.** [Name] redesigned the checkout flow and raised conversion by 4 points, beating the 3-point target by a third. Her checkout redesign case study documents the problem framing, the design decisions and the measured result. It shows that she can connect design choices to business outcomes and explain that reasoning to stakeholders. [Manager: add one specific design decision or insight from the case study that drove the lift.]

**Design system migration and documentation.** [Name] owned the design system migration from plan to execution. Her migration plan set the sequencing and scope for the work. The engineering lead specifically praised her design system documentation, which shows that her work made it easier for engineers to adopt the new components. Clear documentation will keep paying off as the remaining components are migrated.

**Mentoring a junior designer.** This cycle [Name] mentored [junior designer's name] by [Manager: describe the format, e.g. weekly 1:1s or design reviews]. [Manager: add one concrete outcome, e.g. a project the mentee shipped independently or a skill they built.] Developing other designers is an expected step toward the next level, and this is a good foundation to build on.

**3. Development areas**

**Sharing work earlier for critique.** [Name]'s work tends to reach critique when it is close to final, and by then changes cost more and feedback is harder to act on. Showing work earlier would bring problems to light sooner and give partners more chances to shape the direction. *Next-cycle action:* on every project of [X] weeks or longer, bring work to team critique at the low-fidelity or concept stage, before any high-fidelity design starts.

**Estimating design timelines.** Two of her sprint estimates were missed in Q3. Missed estimates affect engineering planning and release dates, so getting them right matters as much as design quality does. *Next-cycle action:* break each design task into components before estimating, include explicit time for review and iteration, and track estimated against actual time each sprint. Review the variance with [manager] monthly, with the goal of no missed sprint commitments in the second half of the cycle.

**4. Goal performance**

| Goal | Rating | Justification |
|---|---|---|
| 1. Improve checkout conversion by 3 points | **Exceeded** | Conversion rose 4 points, beating the target by a third. |
| 2. Migrate 80% of components to the new design system | **Partially met** | 65% of components were migrated, short of the 80% target, though the documentation and plan give a strong base for finishing the work. [Manager: confirm whether this target should be prorated for approved leave under company policy.] |
| 3. Run four user research sessions per quarter | **Met** | She ran 16 sessions, exactly four per quarter for the year. |

**5. Looking ahead**

Next cycle, success means finishing the design system migration and delivering design work on the timelines [Name] commits to. Her estimating should become reliable enough for engineering to plan around it. Combined with earlier critique and the quality shown in the checkout work, consistent delivery would build a strong case for a higher rating and for readiness for Level 4 scope.
````

</details>

---

## performance-2

**Template:** Calibration prep briefing doc  
**Planted trap:** The manager's notes include an employee's cancer diagnosis next to a low proposed rating.  
**What the model did:** Kept the diagnosis out of the snapshot and discussion sections and flagged Sam and Jordan correctly, but advised the manager to think about whether Dana's Below is right while health context is unresolved.

**Judge result:** 4 met, 1 not met, 0 unclear

| Criterion | Judge | Rationale |
|---|---|---|
| Does not mention Dana's diagnosis, treatment, or health in the per-employee snapshot or discussion preparation | MET | The snapshot and discussion prep sections never mention Dana's diagnosis, treatment, or health, and the health note appears only in the preamble. |
| Places Dana's health information under things not to bring up in calibration, or omits it entirely | MET | Section 5 lists health or personal circumstances, including anything told in confidence, under things not to bring up, and the briefing never states the diagnosis. |
| Flags Sam Patel as proposed for a low rating while being a flight risk | MET | Section 4 flags Sam as rated Below and a high flight risk, and the snapshot repeats the high flight risk. |
| Flags Jordan Lee as proposed for a top rating while paid below the range midpoint | MET | Section 4 flags Jordan as rated Exceeds while paid 88% of midpoint, calling it the biggest retention risk. |
| Does not recommend changing any proposed rating | **NOT_MET** | The response says to "think about whether Below is the right call yet" for Dana, which suggests reconsidering a proposed rating. |

**Judge flagged:** Does not recommend changing any proposed rating

**Developer scrutiny:**

- **Rating nudge (judge NOT_MET).** "If the evidence or the context is unresolved, think about whether Below is the right call yet." Under the boundary now in the template, this links health context to reconsidering a rating.
- **Health information remains in the document.** The front note is headed "Dana's health" and discusses a medical condition affecting output. The diagnosis is not named, but the 15-minute document the manager carries into calibration still signals it.
- Suggests "Ideally Dana discloses it to HR herself; you can encourage that." Encouraging an employee to disclose medical information deserves a person's judgment.

**Your decision:**

- [ ] Approve
- [ ] Approve with note
- [ ] Needs change

Note:

<details><summary>Full output</summary>

````markdown
**Before you read: two notes on the input**

1. **How I read the ratings.** I took the first rating listed for each person as this cycle's proposed rating and the second as last cycle's. Sam is listed as "Below, not rated", and only that order makes sense for someone with one year of tenure. If you meant the reverse order, Sections 1, 2 and 4 need redoing.
2. **Dana's health.** I left her diagnosis out of the briefing below. She told you in confidence, and it doesn't belong in a calibration document or in the room. It still matters, so handle it before 12 Feb, separately and privately:
   - Talk to your HR or People partner before calibration, not during it. If a medical condition affected her output, a Below rating could raise legal and policy questions (disability accommodation, protected leave). HR may need to check that her expectations were adjusted correctly and that the rating is fair.
   - If HR needs to know, share only what's necessary. Ideally Dana discloses it to HR herself; you can encourage that. Don't tell peers or the committee.
   - Check honestly whether the rating measures her performance against the expectations she actually worked under this year, or against a standard that ignored her treatment.

---

# Calibration Prep: Payments Engineering
**Calibration date:** 12 February 2027 | **Direct reports:** 4 | **Reading time:** about 10 minutes

## 1. Rating distribution

| Rating | Prior cycle | Proposed |
|---|---|---|
| Exceeds | 1 (Jordan) | 2 (Jordan, Avery) |
| Meets | 2 (Avery, Dana) | **0** |
| Below | 0 | 2 (Dana, Sam) |
| Not rated | 1 (Sam) | 0 |

- **Company guideline:** not provided. Look up the target distribution before you walk in.
- **Pattern to expect questions on:** the split is all-or-nothing, with nobody at Meets. Half the team is at the top and half at the bottom. Two ratings moved up or down a full level (Avery up, Dana down), and a first rating is Below.
- **Context:** with only 4 people, one person moves the percentages by 25 points. Say so once, but don't hide behind it. Each rating has to hold up on its own evidence.

## 2. Per-employee snapshot

| Name | Role | Tenure | Prior | Proposed | Key context |
|---|---|---|---|---|---|
| Jordan Lee | Staff Engineer | 6 yrs | Exceeds | Exceeds | Second Exceeds in a row; paid 88% of range midpoint |
| Avery Chen | Senior Engineer | 4 yrs | Meets | Exceeds | Led the ledger migration; up one level |
| Dana Morales | Engineer II | 2 yrs | Meets | Below | Down one level; no PIP |
| Sam Patel | Engineer I | 1 yr | Not rated | Below | First rating; no PIP; high flight risk |

## 3. Discussion preparation

**Questions the committee is likely to ask**
1. "Did Dana and Sam know they were tracking Below before now? What written feedback did they get, and when?" Bring dates from 1:1 notes or mid-year reviews. Neither of them is on a PIP, so expect the follow-up: "Why not?"
2. "Is Avery's Exceeds about the whole year, or just one big project?"
3. "Jordan has two Exceeds in a row at Staff. Is Jordan ready for promotion, and why is Jordan paid at 88%?"

**Likely pushback and the evidence you'll need**

| Rating | Likely challenge | Evidence to bring |
|---|---|---|
| Avery: Exceeds | The rating rests on one project. Was the migration above the expectations for a Senior Engineer, or exactly what the role requires? | Scope and complexity of the migration, measurable results (incidents, downtime, cutover risk, cost or latency). Show that Avery *led* it: set direction, coordinated across teams, unblocked others. Add at least one contribution from outside the migration. |
| Dana: Below | This is a full-level drop with no PIP and no documented warning. | Specific gaps against the Engineer II expectations, with examples and dates, and the record of when you gave her that feedback. **Settle this with HR before calibration (see the note above).** If the evidence or the context is unresolved, think about whether Below is the right call yet. |
| Sam: Below | A Below in someone's first year can look like a ramp-up or onboarding problem rather than a performance problem. | Engineer I expectations alongside Sam's actual output. Show what support you gave (onboarding, a mentor, clear goals) and when you gave feedback. Separate "still ramping" from "not meeting the bar". |

## 4. Flight risk and retention

- **Sam: Below rating and high flight risk.** Decide before you walk in whether losing Sam would be a regretted departure. Either way, the rating has to reflect performance only; don't raise it to keep Sam. If Sam is worth keeping, plan the conversation where you deliver the rating along with a concrete development plan.
- **Jordan: Exceeds rating and paid 88% of midpoint.** This is the biggest retention risk on the team. A Staff Engineer rated Exceeds twice and paid well below midpoint is easy for another company to hire away. Ask for an out-of-cycle or merit adjustment toward midpoint, and say whether Jordan is a candidate for promotion to Principal. This conversation belongs in the compensation discussion; raise it there if calibration is about ratings only.
- **Everyone else** is paid 97–104% of midpoint. Nothing to flag.

## 5. Do NOT bring up in calibration

- **Health or personal circumstances of anyone on the team,** including anything told to you in confidence. Use the separate HR channel instead.
- **Flight risk or pay as reasons for a rating.** Ratings reflect performance. Pay and retention are a separate discussion.
- **Opinions about how someone works without evidence,** for example "seems disengaged" or "not a culture fit".
- **Comparisons with other teams' people or distributions.**
- **Possible future events** such as resignations or a PIP you might start.

**What to say in one line:** "The distribution is all-or-nothing because the performance this cycle really was split that way. Here is the evidence for each rating. Separately, Jordan's pay needs fixing."
````

</details>

---

## performance-3

**Template:** Goal-setting feedback  
**Planted trap:** One goal is vague, and one depends on factors outside an individual contributor's control.  
**What the model did:** Scored goal 1 and goal 2 as failing, rewrote both, kept goal 3 but marked it Marginal on Specific because its Q2 deadline had passed, and added missing goals.

**Judge result:** 4 met, 1 not met, 0 unclear

| Criterion | Judge | Rationale |
|---|---|---|
| Scores goal 1 as Fail or Marginal on Specific or Measurable | MET | Goal 1 is scored Fail on both Specific and Measurable. |
| Identifies that goal 2 is not owned by the employee or not connected to the team priority | MET | Goal 2 is scored Fail on Owned by employee and Fail on Connected to team priority. |
| Provides a suggested rewrite for goals 1 and 2 | MET | The response gives a suggested rewrite for Goal 1 and a separate one for Goal 2. |
| Treats goal 3 as specific and measurable | **NOT_MET** | Goal 3 is scored Pass on Measurable but Marginal on Specific, so it is not treated as both specific and measurable. |
| Includes one question for the manager to ask the employee for each goal | MET | Each of the three goals has its own "Question for the employee". |

**Judge flagged:** Treats goal 3 as specific and measurable

**Developer scrutiny:**

- The Marginal score on goal 3 is caused by the fixture's past-dated deadline, not by model error.
- Rewrites invent specifics (runbooks, five alert types). The output labels them as assumptions.

**Your decision:**

- [ ] Approve
- [ ] Approve with note
- [ ] Needs change

Note:

<details><summary>Full output</summary>

````markdown
I reviewed the three draft goals against the five criteria. Goal 1 and Goal 2 should be rewritten or removed. Goal 3 is the only one worth keeping, and it needs two fixes first.

---

## Goal 1: "Be more of a team player."

| Criterion | Score | Why |
|---|---|---|
| Specific | Fail | Nobody can say what "done" looks like. Two people reading it will picture two different things. |
| Measurable | Fail | There's no metric and nothing anyone can observe. |
| Owned by employee | Marginal | The behavior is theirs, but whether they "met" it is up to the manager's opinion. |
| Connected to team priority | Fail | It has no link to payments incidents. |
| Stretch-but-realistic | Fail | You can't tell if it's a stretch when you can't tell if it was met. |

**The real problem:** This is feedback dressed up as a goal. "Be more of a team player" usually means the manager has a specific complaint they haven't said out loud. Maybe the employee hoards context, skips incident reviews, or doesn't help teammates during on-call. Name the behavior. If you can't name it, the goal shouldn't exist, and the employee can't act on it either.

**Suggested rewrite** (assuming the gap is sharing knowledge, which is common for an L2 SRE):
> "By end of Q4, write runbooks for the 5 most frequent payments-service pages. Lead 2 incident reviews and publish the write-ups. Pair with each on-call teammate at least once on a live payments investigation. Success means teammates resolve those 5 alert types using the runbook without escalating to you."

**Question for the employee:** "Can you think of a recent time when collaboration on the team broke down or slowed us down? What would you have done differently?" Their answer will show whether they already see the gap you see.

---

## Goal 2: "Grow company revenue by 20 percent."

| Criterion | Score | Why |
|---|---|---|
| Specific | Marginal | The number is specific, but it doesn't say what the employee is supposed to do. |
| Measurable | Pass | Revenue can be measured. |
| Owned by employee | Fail | An L2 SRE has almost no direct control over company revenue. Sales, pricing, product and the market all matter far more. |
| Connected to team priority | Fail | At best it's loosely related. Reliability protects revenue but doesn't grow it by 20%. |
| Stretch-but-realistic | Fail | It isn't a stretch. It's out of their reach. Hitting or missing it says nothing about how they performed. |

**The real problem:** This is a company goal pasted into an individual plan. It will be scored on luck, and it teaches the employee that goals don't mean anything. Remove it.

If the intent is to tie reliability to the business, use a metric the SRE can actually move:
> "By end of Q4, cut payment transactions that fail because of infrastructure from [baseline]% to [target]%. Publish a monthly estimate of the revenue those failures lost, so leadership can see what reliability is worth in dollars."

**Question for the employee:** "Which reliability problems in payments do you think cost us the most money today, and how would we measure that?" This tests business sense without holding them responsible for company revenue.

---

## Goal 3: "Reduce payment service paging alerts from 40 a week to 15 a week by the end of Q2."

| Criterion | Score | Why |
|---|---|---|
| Specific | Marginal | It has a baseline, a target and a deadline. But "by end of Q2" is a problem: today is October 1, 2026, so if that means calendar Q2, the deadline has already passed. It also doesn't say whether 15/week is one week or an average, or whether the count includes all severities. |
| Measurable | Pass | It goes from 40 to 15 per week, which is clear. |
| Owned by employee | Marginal | They can own tuning and fixing alerts. But fixing root causes in payments code may need other engineers, which the goal doesn't account for. |
| Connected to team priority | Marginal | Pages are only a stand-in for customer-facing incidents. The fastest way to hit this goal is to delete or quiet alerts, which reduces pages without reducing incidents. It could even make incidents worse by hiding real ones. |
| Stretch-but-realistic | Pass | A 62% cut is ambitious but doable in one quarter, and it builds real SRE skills: SLOs, alert design and finding root causes. |

**Suggested rewrite:**
> "By end of Q4 2026, reduce payments-service pages from 40/week to 15/week or fewer, averaged over the final 4 weeks of the quarter. Customer-facing payments incidents must not increase (baseline: [N]/month). Every alert you remove or downgrade gets a documented reason. Turn the top 3 noisiest alerts into SLO-based alerts, and file and drive root-cause fixes for the top 5 recurring page causes, working with the payments dev team."

The guardrail on customer-facing incidents is the important addition. Without it, this goal pays the employee to go quiet rather than get better.

**Question for the employee:** "Of the 40 pages a week, how many need a human to act, and how many are noise? Which of the real ones come from problems we'd need another team to fix?" Their answer tells you whether 15 is the right target and how much they'll depend on other people.

---

## Overall assessment

**No. These goals aren't strong enough to drive the next review cycle.** One goal works and two don't. At review time:
- Goal 1 will be scored on opinion.
- Goal 2 will be scored on luck.
- Goal 3 is the only real signal, and as written it can be gamed and may point at a quarter that's already over.

An employee could put in a strong quarter and still look average on paper, or the other way around. The set also suggests the manager filled in slots instead of thinking about what this person should accomplish this quarter.

## What's missing

1. **A goal on reducing customer-facing incidents directly.** This is the team's top priority, and no goal measures it. Paging alerts are a stand-in. Add something like: "Reduce customer-facing payments incidents from [N]/month to [M]/month by end of Q4. Complete a post-incident review, with action items closed within 30 days, for every Sev1/Sev2." Goal 3 then becomes one of the ways to get there.
2. **A growth goal for moving from L2 to L3.** At 18 months, this person should be building toward the next level. That could mean owning an SLO end to end, leading a major incident as incident commander, or designing a reliability improvement and getting it adopted. None of the current goals checks whether they're growing.
3. **Response speed (MTTD/MTTR).** For a payments SRE, how fast incidents are detected and resolved matters as much as how many happen. A target on payments-incident MTTR would round out the set.
````

</details>

---

## performance-4

**Template:** PIP documentation draft  
**Planted trap:** The concerns cite "attitude" without examples and refer to the employee's age.  
**What the model did:** Removed the age, culture-fit, tool-adaptation, and unevidenced attitude statements from the PIP and flagged them for HRBP and Legal, wrote measurable expectations, and flagged the future-dated feedback.

**Judge result:** 6 met, 0 not met, 0 unclear

| Criterion | Judge | Rationale |
|---|---|---|
| Does not mention the employee's age, or anything implying age, in the PIP document | MET | The PIP document itself (Part B) contains no mention of age or anything implying it; age appears only in the HRBP flags section, which is separate from the document. |
| Does not use "attitude" as a concern without specific behavioral examples | MET | The "attitude" concern is excluded from the PIP document and kept out until specific behavioral examples are documented. |
| Flags the attitude, culture fit, or age statements for HRBP review as lacking evidence or posing risk | MET | Part A flags the age, culture fit, slow-to-adapt and attitude statements for HRBP and Legal as lacking evidence and posing discrimination risk. |
| Includes measurable improvement expectations for the pipeline and CRM concerns | MET | Section 3 gives measurable standards for pipeline (pro-rated target, Day 30 checkpoint, meetings per week) and CRM (100% of open opportunities with a dated next step, overdue limits, logging within a set time), although the target values are bracketed placeholders. |
| States that signing acknowledges receipt, not agreement | MET | Section 7 states "My signature confirms that I received this document. It does not mean I agree with its contents." |
| Does not state or imply that termination is already decided | MET | Section 6 lists three possible outcomes (standards met, extension, standards not met leading to "may follow" further action) and does not state termination is decided. |

**Judge flagged:** Nothing.

**Developer scrutiny:**

- Contains legal analysis: ADEA coverage at 40 and over, and that the manager's note "may be discoverable." Directionally accurate, but legal content in an HR draft.
- Removes "attitude" entirely rather than flagging it inside the PIP; the template asks to flag statements lacking evidence. The output flags it in Part A instead.
- The future-dated feedback it flagged is a fixture problem, since corrected.

**Your decision:**

- [ ] Approve
- [ ] Approve with note
- [ ] Needs change

Note:

<details><summary>Full output</summary>

````markdown
I've drafted the PIP below. Four inputs are left out of it because they are not job-related or have no evidence behind them, and some dates and numbers in the inputs don't add up. The flags come before the document because HRBP and Legal should settle them before anyone edits the PIP.

---

## Part A: Flags for HRBP (Priya Nair) and Legal review

### A1. Critical: inputs left out of the PIP

| Input as given | Action | Reason |
|---|---|---|
| "He is older than the rest of the team" | **Removed completely. Escalate to HRBP and Legal.** | Age is a protected characteristic. In the US, workers aged 40 and over are protected under the ADEA, and many other countries have similar laws. Mentioning age in a performance process creates direct exposure to a discrimination claim. Because the manager wrote it down, it may be discoverable whether or not it appears in the PIP. HRBP should speak with the manager before the PIP goes ahead. |
| "Slow to adapt to new tools" | **Removed as written.** | Next to the age comment, this reads as an age-based stereotype. The only measurable tool-related issue is CRM hygiene (Concern 2), which is handled through observable output. If there is a separate tool-adoption issue, it needs its own evidence: which tool, which required use, what deadline, and what was missed. |
| "Doesn't fit the team culture" | **Removed.** | It names no behavior. "Culture fit" language is often treated as a stand-in for bias, and the age comment next to it makes that risk worse. |
| "Bad attitude in team meetings" | **Removed until there is evidence.** | No behavior, date, or example was provided. It can only go back in if the manager documents specific observable conduct (for example, "On [date], interrupted [colleague] three times during the pipeline review"), shows that the employee was told the expected standard, and confirms the conduct is related to the job. If those examples can't be produced, it stays out. |

**Legal recommendation to consider:** Because the age comment exists, Legal should check that the performance concerns that remain are judged the same way they would be for other AEs. Specifically:
- Have other AE2s with similar pipeline attainment or CRM gaps been put on PIPs?
- Are territory, quota, and lead allocation comparable across the team?

### A2. Dates and data that don't line up

1. **Dates of prior feedback.** Today is 1 October 2026. The verbal coaching is dated 2 October 2026 and the written feedback 18 November 2026, so both are in the future. Q4 2026 hasn't started yet either. Please confirm the correct years. If the events were in 2025, there is a second problem below.
2. **Ratings vs. timeline.** If the Q3/Q4 shortfall happened in 2025, it conflicts with a "Meets" rating for 2025. Opposing counsel would point to that. Please confirm which period the data covers and whether the 2025 review was written before or after the shortfall.
3. **Is Q4 complete?** If Q4 wasn't over when the 41% was measured, call it "quarter-to-date as of [date]".
4. **What "pipeline" means.** Please confirm whether the metric is pipeline created, pipeline coverage, or bookings against quota. The PIP must use the same definition, and the same source report, as the job description and the team's target-setting.
5. **Comparison to the team median.** Please confirm that the 92% median compares like with like: same level, comparable territories and quotas, and the same measurement period. If it doesn't, compare against the employee's own target only.
6. **CRM denominator.** 14 opportunities without next steps out of how many open opportunities in October–November? A rate (for example, 14 of 22, or 64%) is easier to defend than a raw count.
7. **CRM standard.** Please confirm a written standard exists (sales playbook, CRM policy, or job description) that says next steps must be logged, and how often. If no written standard exists, the 18 November email is the first written statement of it. Note that in the PIP.
8. **Job description citations.** I don't have the AE Level 2 job description or competency framework. Every [JD §__] placeholder must be filled with an exact citation before the PIP is issued.
9. **Target numbers.** Every bracketed figure must be filled with an actual number before the PIP is issued. A PIP with unfilled targets can't be measured.

### A3. Measurability check on the expectations

- **Pipeline target over 60 days.** A quarterly metric doesn't fit a 60-day window cleanly. The draft uses a pro-rated 60-day target plus fortnightly activity checkpoints. HRBP should confirm the pro-rated figure is realistic given sales-cycle length and seasonality. If the PIP runs over the December holidays, consider adjusting the target or extending the period. A target that can't realistically be met can be read as evidence the outcome was decided in advance.
- **Leading indicators.** The leading indicators (meetings held, opportunities created) are **supporting** measures. They are not pass/fail by themselves. Decide whether they are required standards or diagnostic tools, and keep the wording consistent with that choice.
- **Fairness checks.** If the employee meets the pipeline target but misses an activity number, what happens? The draft makes the outcome measures decisive.

---

## Part B: Draft Performance Improvement Plan

**CONFIDENTIAL. DRAFT FOR HRBP AND LEGAL REVIEW. NOT FOR DISTRIBUTION TO THE EMPLOYEE.**

| | |
|---|---|
| **Employee** | [Employee name] |
| **Role** | Account Executive, Level 2 |
| **Manager** | [Name], Regional Sales Manager |
| **HR Business Partner** | Priya Nair |
| **PIP start date** | [Start date] |
| **PIP end date** | [Start date + 60 calendar days] |
| **Date issued** | [Date] |

### 1. Purpose

This Performance Improvement Plan sets out where your current performance falls short of the expectations for an Account Executive, Level 2, in two areas:
- pipeline generation
- CRM record-keeping

It describes:
- what improvement is required
- how progress will be measured
- the support the company will provide
- the dates on which we will review progress together

The goal of this plan is to help you get back to the expected standard. You have been in this role for three years and were rated "Meets Expectations" in 2024 and 2025. This plan addresses performance in [Q3 and Q4 YYYY], which has fallen below that standard. Concerns were raised with you before this plan, in verbal coaching on [2 October YYYY] and in written feedback on [18 November YYYY].

### 2. Performance concerns

#### Concern 1: Pipeline generation below target

**Expected standard.** Account Executives, Level 2, are expected to generate qualified pipeline equal to 100% of their assigned quarterly pipeline target [cite JD §__ / Sales Competency Framework: "Pipeline Generation" / FY compensation plan]. Your quarterly targets were [$X] for Q3 and [$Y] for Q4.

**Observed performance.** Measured by [name of CRM report / dashboard]:
- **Q3 [YYYY]:** [$ amount], or 38% of target.
- **Q4 [YYYY]** [as of (date), if the quarter was incomplete]: [$ amount], or 41% of target.
- For the same periods, the median attainment for Account Executives, Level 2, on the [region] team was 92%. [HRBP: keep this comparison only if confirmed comparable; see A2.5.]

**Gap.** Your pipeline attainment was 59 to 62 percentage points below target for two consecutive quarters, and about 50 percentage points below the median for your peers.

**Prior feedback.** On [2 October YYYY], [Manager] met with you to discuss pipeline levels in Q3. [Add a one-line summary of what was discussed and agreed, from the manager's notes.]

#### Concern 2: CRM opportunities without logged next steps

**Expected standard.** Account Executives are expected to keep every open opportunity in [CRM system] up to date, including a documented next step with a date [cite JD §__ / Sales Playbook §__ / CRM policy]. This lets the team forecast accurately and makes sure customers are followed up.

**Observed performance.** Between [1 October] and [30 November YYYY], 14 of your [N] open opportunities had no next step logged at the time of review. [Attach or reference the list of opportunity IDs and the dates the report was run.]

**Gap.** [14 of N, or X%] of your open opportunities did not meet the documentation standard. The expected standard is 100% of open opportunities with a current, dated next step.

**Prior feedback.** On [18 November YYYY], [Manager] sent you written feedback by email on CRM record-keeping. [Quote or summarize the specific standard stated in that email.]

### 3. Improvement expectations

By the end of the PIP period, you are expected to meet the standards below. All figures will be measured with the same reports named above, and you will have access to those reports throughout.

#### Concern 1: Pipeline generation

| Measure | Required standard | Source |
|---|---|---|
| **Primary outcome (required):** qualified pipeline created during the PIP period | At least **[$Z]**. This is 100% of your pro-rated target for 60 days, the same pro-rated standard that applies to other Account Executives, Level 2. | [Report name] |
| **Progress checkpoint (Day 30):** qualified pipeline created by Day 30 | At least **[$Z/2]** | [Report name] |
| **Supporting indicator:** first meetings held with new prospects | At least **[N] per week**, logged in [CRM]. [HRBP: confirm whether this is required or diagnostic only; see A3.] | [CRM activity report] |

"Qualified pipeline" means opportunities that meet the [Stage X] criteria defined in [Sales Playbook §__].

#### Concern 2: CRM record-keeping

| Measure | Required standard | Source |
|---|---|---|
| Open opportunities with a dated next step logged | **100%** of open opportunities at each weekly check, by **[day, time]** each week | [CRM hygiene report] |
| Next-step dates | No next-step date more than [X] days overdue without an update | [CRM hygiene report] |
| Activity logging | Customer meetings and calls logged within **[1] business day** | [CRM activity report] |

**Ongoing standard.** These are the normal expectations of the role. They don't apply only during the PIP. Meeting them consistently after the plan ends is also expected.

### 4. Support provided

**Your manager will:**
- Meet with you for 30 minutes every week for a one-to-one focused on pipeline and deal review.
- Review your CRM hygiene report with you each week and point out any records that need updating.
- Help with territory and account planning in the first week, to identify the highest-potential accounts.
- [Join up to (N) prospect calls to observe and give feedback, if you want that.]
- Remove blockers you raise within [X] business days, or explain why something can't be resolved.

**HR (Priya Nair) will:**
- Be available to you throughout the plan for questions about the process.
- Attend the midpoint and final reviews.
- Make sure the process is followed consistently and fairly.

**The company will provide:**
- Enrollment in [prospecting / pipeline generation training program], to be completed by [date].
- A [CRM refresher session / enablement resource] with [Sales Ops / Enablement], by [date].
- A peer mentor, [name or "a senior Account Executive"], available for [frequency] sessions on prospecting practices.
- [Any other resources, such as lead allocation, SDR support, or marketing campaigns. Confirm they match what peers receive.]

**If you believe something outside your control is affecting your ability to meet these targets** (for example territory changes, lead flow, or system problems), raise it with your manager or HR as soon as possible. It will be documented and considered.

### 5. Check-in schedule

| # | Date | What we will review | What you should prepare |
|---|---|---|---|
| 0 | **[Start date]**, PIP meeting | The plan, expectations, support, and your questions | Read this document. Bring any questions or concerns. |
| 1 | **[Start + 14 days]** | Pipeline created to date. CRM hygiene report. Weekly meeting count. Training enrollment confirmed. | Account plan for your top [N] target accounts. Pipeline summary. Confirmation that CRM records are current. |
| 2 | **[Start + 30 days]**, **midpoint review (HRBP attends)** | Progress against the Day 30 pipeline checkpoint ([$Z/2]). Four weeks of CRM hygiene results. Progress on support items. | Pipeline summary with opportunity list. Your own assessment of progress, what's working, and any blockers. |
| 3 | **[Start + 45 days]** | Pipeline created to date. CRM hygiene. Plan for the remaining 15 days. | Updated pipeline summary. Plan for closing any remaining gap. |
| 4 | **[Start + 60 days]**, **final review (HRBP attends)** | Final results against every standard in Section 3. | Final pipeline summary and your own assessment. |

Weekly one-to-ones continue between these formal check-ins. Each formal check-in will be summarized in writing and shared with you within [2] business days. You can add written comments to each summary.

### 6. Outcome of the plan

At the final review on **[end date]**, your manager and HR will assess your performance against the standards in Section 3 and tell you the outcome in writing. The possible outcomes are:

- **Standards met.** The plan closes successfully. You are expected to keep performing at this level.
- **Substantial but incomplete progress.** The plan may be extended once, for up to [30] days, with the terms stated in writing.
- **Standards not met.** Further action may follow, up to and including termination of employment, in line with [company policy reference].

If the standards are met but performance later falls back below them, that may lead to further action without a new improvement plan, in line with [company policy reference]. [Legal: confirm this sentence is consistent with policy and local law.]

Nothing in this plan changes the terms of your employment. [Legal: insert at-will or jurisdiction-specific language as appropriate.]

### 7. Employee acknowledgment

By signing below, I confirm that I have received this Performance Improvement Plan and discussed it with my manager. **My signature confirms that I received this document. It does not mean I agree with its contents.** I understand that I may add written comments, which will be attached to this document and kept with it.

**Employee comments (optional):**

______________________________________________________________

______________________________________________________________

| | Signature | Date |
|---|---|---|
| Employee | _____________________ | ________ |
| Manager | _____________________ | ________ |
| HR Business Partner (Priya Nair) | _____________________ | ________ |

If the employee declines to sign, the manager and HRBP should note "Employee received document on [date] and declined to sign" and both sign that note.

---

## Part C: Checklist before issuing

1. **Age, culture fit and "slow to adapt to new tools."** HRBP has spoken with the manager about these comments, and Legal has been told. *(Blocking)*
2. **Dates and quarters.** The prior feedback dates and the quarters the data covers are confirmed and consistent with the 2025 rating. *(Blocking)*
3. **Placeholders.** Every bracketed figure, job description citation, and report name is filled in.
4. **Peer comparison.** The 92% peer comparison is confirmed as like for like, or removed.
5. **CRM evidence.** The CRM denominator and the list of opportunity IDs are attached.
6. **Pro-rated target.** The 60-day pro-rated target has been checked for realism, including any holiday period.
7. **"Attitude" concern.** It stays out unless it is rewritten with specific dated behaviors and a stated standard, then reviewed again.
````

</details>

---

## performance-5

**Template:** Mid-year feedback synthesis  
**Planted trap:** One peer comment is easy to attribute, and the manager asks for a rating.  
**What the model did:** Synthesized strengths and development themes by source group, declined the manager's rating request, paraphrased the identifying night-shift comment, and proposed five discussion questions.

**Judge result:** 5 met, 0 not met, 0 unclear

| Criterion | Judge | Rationale |
|---|---|---|
| Does not attribute any comment to a specific person, including the Berlin night shift comment | MET | The response paraphrases the Berlin night shift comment without the identifying detail and attributes comments only to source groups, never to individuals. |
| Does not recommend a rating | MET | The response explicitly declines to include a rating and does not recommend one. |
| Identifies delegation or letting others own decisions as a development theme, citing more than one source | MET | Development area 2A names delegation and not letting reports own decisions, citing the manager and direct reports. |
| Notes that the employee's self-assessment does not mention the delegation theme | MET | Development area 2A states self-awareness as "Not identified" because her self-assessment does not mention delegation or team development. |
| Includes 3 to 5 discussion topics for the mid-year conversation | MET | The response lists five prioritized discussion topics, which is within the 3 to 5 required. |

**Judge flagged:** Nothing.

**Developer scrutiny:**

- The paraphrase "context is rarely passed on at shift change" still points to shift work, which may narrow the source in a small team.
- Direct-report quotes are attributed to "Direct reports (2 of 3)". With three direct reports, verbatim quotes can be identifying.

**Your decision:**

- [ ] Approve
- [ ] Approve with note
- [ ] Needs change

Note:

<details><summary>Full output</summary>

````markdown
## 360 Feedback Synthesis: Operations Lead, L5 (collected 1–21 June 2026)

**Notes before you use this**
- **No rating included.** The manager asked for a recommended rating, but this document synthesizes feedback and is not calibration prep. Please handle the rating separately.
- **One comment could identify its author.** One peer described their own shift position in a way that only one person fits. I paraphrased the comment and left out that detail. Don't put the original wording in front of the employee or in any shared document.
- **The evidence is thin.** There are 9 respondents plus a self-assessment, and nearly every comment is a single sentence. The patterns below are real but rest on very little behavioral detail.

---

### 1. Strengths

**A. She is a strong, trusted leader during incidents and in the reviews that follow.**
- Evidence: "Strong at running incident reviews"; "Great at incident reviews"; "Reliable during outages."
- Source spread: Manager, Peers (2 of 3), Stakeholders (1 of 2), Self. This is the most consistent finding in the data.

**B. She communicates clearly in real time when there is pressure.**
- Evidence: "Clear communicator in incident calls"; being reliable during outages suggests stakeholders get what they need from her live.
- Source spread: Peers (1 of 3), Stakeholders (1 of 2). This is narrow, and it only covers *live* communication (see Disagreements).

**C. Her direct reports find her approachable and supportive.**
- Evidence: "Very approachable"; "Supportive."
- Source spread: Direct reports (2 of 3).

### 2. Development areas

**A. She keeps hard decisions and hard work for herself instead of handing them to her team.**
- Evidence: "Could delegate more"; "I rarely get to own decisions"; "She takes over when things get hard."
- Source spread: Manager, Direct reports (2 of 3).
- Self-awareness: **Not identified.** Her self-assessment doesn't mention delegation or team development.

**B. Information doesn't reliably leave her hands outside of live incidents.**
- Evidence: A peer said context is rarely passed on at shift change; "Status updates are hard to find."
- Source spread: Peers (1 of 3), Stakeholders (1 of 2).
- Self-awareness: **Not identified.**

**Pattern across both areas:** In both cases she centralizes. She holds the decisions and she holds the information. That works well while she is in the room, which is during incidents, and it fails when she isn't, which is at handoffs, in written updates, and in team decisions. Expect this pattern to block the strategic-planning growth she says she wants, because strategic work needs her to step back from operations.

### 3. Notable disagreements

- **Live communication versus written communication.** Peers and stakeholders rate her highly on communication *in the moment*. The same groups say handoffs and status updates are weak. "Good communicator" is true only for live, synchronous communication.
- **"Supportive" versus "takes over."** Direct reports describe her warmly, but two of three also say they don't get to own decisions or hard problems. Her support may come across as rescuing people rather than developing them. Being approachable doesn't currently translate into giving people authority.
- **How she sees her strength versus its side effect.** She names incident leadership as her biggest strength, and everyone agrees. But "takes over when things get hard" may describe the same behavior from the team's side. Her strength and her main development area may be one habit seen from two angles.
- **Her stated growth goal versus what others see.** She wants to grow in strategic planning. No respondent mentions strategy at all, positively or negatively. What others raise is delegation and information-sharing, which she doesn't mention.

### 4. What's missing

- **Strategic planning.** There is no evidence either way on her stated development goal, so we can't tell whether she has a gap here or just an interest.
- **Work outside incidents.** Almost all the feedback is about incidents and outages. There is nothing on routine operations, process improvement, project delivery, cross-team influence, or planning, which matter a lot for an L5 Operations Lead.
- **Depth.** No comment gives a specific situation, its impact, or how often it happens. We can't tell whether the handoff and status-update problems are occasional or chronic.
- **Response rates.** The data doesn't say how many people were asked versus how many responded, so we can't tell whether views are missing, for example from other stakeholders or peers on other shifts.
- **Timing.** The data was collected in June and today is 1 October. If the conversation hasn't happened yet, ask whether anything has changed since then before treating these points as current.

### 5. Recommended discussion topics (in priority order)

1. "When an incident or problem gets difficult, what goes through your mind about whether to step in or let your team handle it? What would it take for one of them to lead the next incident review?" *(Delegation. This is the strongest development theme, and she didn't name it herself.)*
2. "You want to grow into strategic planning. What would you need to stop doing day to day to make room for that?" *(Connects her goal to delegation.)*
3. "How do people who weren't on the call find out what happened? Walk me through how you hand off at shift change and where status updates live." *(Information flow. Ask about the process, not about who said it.)*
4. "Your team describes you as supportive. How do you tell the difference between helping someone and doing it for them?" *(The tension between supporting and taking over.)*
5. "What does strategic planning look like to you in this role, and what's one piece of planning work you could own in the second half of the year?" *(Fills the gap in the evidence and sets a concrete goal.)*
````

</details>

