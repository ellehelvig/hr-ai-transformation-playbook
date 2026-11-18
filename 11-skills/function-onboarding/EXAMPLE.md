# Worked example: onboarding

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Rowan Teasdale, HR Operations Lead, writes: "Nine people start on 7 December: six in Illinois, three in Berlin, four of them remote. Build the onboarding plan. IT wants a chatbot that answers new hire questions from our handbook and also tells managers who hasn't finished their modules. Last cohort, remote hires waited on laptops." Rowan pastes last cohort's day-one readiness:

| Work arrangement | Started | Ready by end of day one |
|---|---|---|
| On site or hybrid | 12 | 11 |
| Remote | 8 | 5 |

## Output (abridged)

### New hire context

Cohort of 9, start 7 December. Locations: Illinois, Germany. Gaps labeled: three buddies not yet named; handbook version not given.

### Preboarding checklist

| Item | Owner | Due | Status |
|---|---|---|---|
| Laptop shipped to remote hires | IT | 30 November | Open (4 tickets) |
| Core accounts created | IT | 4 December | Open |
| ... | | | |

### Compliance paperwork

| Form | Who completes | Deadline | Human reviewer |
|---|---|---|---|
| I-9 Section 1 (Illinois hires) | New hire | No later than 7 December | HR operations owner |
| I-9 Section 2 | Employer | Within three business days of hire | HR operations owner |
| Germany forms | To confirm | Counsel confirms | HR operations owner |

### AI onboarding assistant scope

- Answers only from the approved, versioned handbook, citing section and version; otherwise says "I don't know" and names a person.
- Routes pay, leave, accommodation, immigration and complaints to the named HR owner.
- Eval set: `09-evals/hr-qa-agent-evals.yaml`; Rowan sets the pass bar before launch.
- Notice: "You are chatting with an AI assistant. To reach a person, message HR Operations."

### Decision rights applied

| Item | Agent role | Routed to |
|---|---|---|
| Manager prep guides and 30/60/90 drafts | Drafts for sign-off | Each hiring manager |
| Chatbot reporting module completion by named new hire to managers | Refuses and routes | Legal, with a new risk assessment: this is monitoring, not Q and A |
| Choose the three buddies | Refuses and routes | Managers, with work-related criteria |

### Readiness flag

On site or hybrid: 11 / 12 = 91.7%. Remote: 5 / 8 = 62.5%. Remote hires were less ready, so remote laptops are due 30 November, a week before start.

### Metrics this plan tracks

90-day new hire retention; day-one readiness by work arrangement; assistant answer accuracy from monthly de-identified samples.

### Audit trail

- Inputs used: HRIS fields; pasted readiness counts. Gaps: buddies, handbook version.
- Tools called and fields read: HRIS (job, location, start date, arrangement, manager); IT ticketing (ticket status, owner, due date). No identity documents read.
- Items needing sign-off: checklist (Rowan); first-week plans (managers); assistant launch (policy owner and Legal).
- Open legal questions: EU AI Act, transparency and EU AI Act, AI literacy (Article 4) for the Berlin hires; Germany onboarding forms. Counsel confirms; see the Key dates rows.
