# Worked example: employee relations

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Marlo Fenwick, HRBP for Engineering, writes: "A Chicago senior engineer says their manager made age comments, then pulled them off the launch project. The manager now wants to start a PIP. I'm investigating; the VP of Engineering decides any outcome; counsel isn't directing yet. Nobody is in a union. Please triage and plan."

| Date | Event (role labels) |
|---|---|
| 20 Oct | Respondent B: "you're too old to pick up the new stack" (per Complainant A) |
| 3 Nov | Complainant A asks two coworkers in team chat whether their pay changed after releveling |
| 10 Nov | Respondent B moves Complainant A off the launch project |
| 12 Nov | Complainant A raises the age comments with Marlo |
| 14 Nov | Respondent B asks HR to start a PIP for Complainant A |

## Output (abridged)

```markdown
## Case summary
ER-2026-114, possible age discrimination and retaliation, urgency high,
Illinois, union N, investigator Marlo Fenwick, decision owner VP Engineering,
counsel directing N

## Protected activity flags
| Complainant A | Pay question raised with coworkers (possible concerted activity) | 3 Nov | team chat export |
| Complainant A | Complaint of age discrimination | 12 Nov | HRBP intake note |

## Investigation plan
Scope in: age comments (20 Oct, others reported); project removal (10 Nov)
Scope out: releveling pay question, logged for the comp team
Witnesses: Coworker 1 and Coworker 2 (chat), then Respondent B
...

## Retaliation check
| Proposed action | Affects | Protected activity and date | Days between | Route to counsel |
| Project removal (done) | Complainant A | Pay question, 3 Nov | 7 | Y |
| PIP (proposed) | Complainant A | Complaint, 12 Nov | 2 | Y, hold until counsel reviews |

## Decision rights calls
| Request | Agent role | Routed to |
| Investigation plan and interview guides | Drafts for sign-off | Marlo Fenwick |
| Draft the PIP for Complainant A now | Refuses and routes | ER lead and counsel, with this check |
| "Is the manager's account believable?" | Refuses and routes | Investigator, with the evidence matrix |

## Next step owner
Counsel: whether the 3 Nov chat is concerted activity and whether to hold the PIP.

## Audit trail
Inputs used: concern as raised, locations, headcount 1,400, union flag,
owners. Not provided: list of approved AI tools for ER data.
Tools called:
| HRIS (read-only) | locations, union flag | work location, bargaining unit flag |
| HRIS (read-only) | recent changes | project assignment for A and B, last 90 days |
Needs sign-off: triage (ER lead), plan and guides (Marlo Fenwick),
retaliation check (ER lead, counsel)
Open legal questions: concerted activity status; if any automated tool
informs discipline, see Key dates row Illinois HB 3773 (Public Act 103-0804)
```

Metrics this matter feeds: median days to close (intake 12 Nov), post-close retaliation concern rate, and AI draft correction rate on the evidence matrix.
