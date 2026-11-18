# Worked example: offboarding

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Corin Wexley, HRBP for Support, writes: "An automated ticket triage workflow went live in our San Jose support team. Leadership wants to remove 38 of the 120 roles there in January, offering a release with severance. Can you pull performance and tenure from the HRIS, pick the 38, and build the offboarding plan?"

| Item | Count |
|---|---|
| Harbor & Pine employees | 1,400 |
| San Jose support pool | 120 |
| Roles to remove | 38 |
| Roles remaining | 82 (120 - 38) |

## Output (abridged)

### Exit context

Group reduction, California site, 1,400 employees. Legal involved: yes. Gaps labeled: decision record not yet signed; redeployment review not on file.

### Decision rights applied

| Item | Agent role | Routed to |
|---|---|---|
| Pick the 38 from performance and tenure data | Refuses and routes | HR leadership and counsel, with a selection criteria template |
| Request to compare retention rates by group in the 120-person pool before selections are final | Drafts for sign-off | Counsel and People Analytics, method in `fairness-audit-prep` |
| Dated timeline, access plan template, manager talking points | Drafts for sign-off | Corin; IT and Security for access |
| Severance amounts and release language | Refuses and routes | Legal and HR leadership |

### Legal flags for counsel

| Item | Why it may apply | Owner | Status |
|---|---|---|---|
| Federal WARN | Employer has 100 or more employees; whether 38 exits at one site is a covered event is for counsel | Employment counsel | Open |
| Cal/WARN content | Technology changed the work; see the California SB 951 (Ch. 860, Stats. 2026) Key dates row | Employment counsel | Open |
| Group release | 45 days to consider, 7 to revoke, age and job title disclosures | Legal | Open |
| Redeployment | Roles removed after automation; run `function-workforce-planning-org-design` first | HRBP | Open |

### Offboarding timeline

| Date | Step | Owner | Done |
|---|---|---|---|
| Before any notice | Decision record signed; adverse impact check reviewed | Accountable leader, counsel | No |
| Date set by counsel | Notices, if WARN or Cal/WARN applies | Counsel, HRBP | No |
| Meeting day | Access removal at the time Security sets | IT and Security | No |
| ... | | | |

### Metrics this plan tracks

Offboarding on time; access removed by the set time; reduction pool retention rate ratio by group, computed by People Analytics before selections are final.

### Audit trail

- Inputs used: exit type, site, counts and release plan from Corin. Gaps: decision record, redeployment review.
- Tools called and fields read: HRIS (headcount by site). Performance and tenure not read, because selection is refused.
- Items needing sign-off: decision record (accountable leader); timeline (Corin); access plan (IT and Security); release (Legal).
- Open legal questions: California SB 951 (Ch. 860, Stats. 2026) and California SB 947 (Ch. 859, Stats. 2026) if the triage tool fed any selection; WARN and Cal/WARN coverage. Counsel confirms; see the Key dates rows.
