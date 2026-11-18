# Worked example: HR compliance

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Theo Vasquez-Brandt, HR compliance manager at Harbor & Pine (1,400 staff in California, Illinois, NYC, Colorado, and Germany), writes: "On 4 January we open a Denver office. 60 of our 150 Colorado remote staff move in, and we add 35 agency contractors our managers will supervise day to day. Update the calendar, posters, and retention schedule, check our AI tools, and tell me we're good to go in Colorado."

| AI tool | Use | Locations |
|---|---|---|
| ATS resume screening feature | Filters applicants before recruiter review | All US |
| Review writing assistant | Drafts manager review text | All |

## Output (abridged)

### Footprint (new row)

| Location | Headcount | Worker types | Union Y/N | Agencies |
|---|---|---|---|---|
| Denver office | 60 employees, 35 contractors | Employees; contractors supervised day to day | N | OSHA, DOL, Colorado labor department |

OSHA expects Harbor & Pine to record injuries of the 35 contractors, since its managers supervise them day to day (29 CFR 1904.31).

### Compliance calendar (new rows)

| Obligation | Source | Due | Owner | Status |
|---|---|---|---|---|
| Severe injury reporting: 8 hours for a death, 24 hours for in-patient hospitalization, amputation, or loss of an eye | osha.gov/recordkeeping, read 18 Nov 2026 | On event | Denver office manager | Verified |
| Colorado ADMT notice and adverse-decision explanation | Key dates row: Colorado SB 26-189 (ADMT Act) | See Key dates row | Compliance manager | Unverified: counsel checks enforcement status |
| ... | | | | |

### AI tools in HR decisions

| Tool | Key dates rows | Notice confirmed | Adverse impact plan | Open question |
|---|---|---|---|---|
| ATS resume screening | California FEHA automated-decision system regulations; Illinois HB 3773 (Public Act 103-0804); NYC Local Law 144; Colorado SB 26-189 (ADMT Act) | NYC only | None on file: route to `fairness-audit-prep` | Is it a covered AEDT in NYC? |
| Review writing assistant | Illinois HB 3773 (Public Act 103-0804), if used in discipline | No | Not yet assessed | Does it feed discipline decisions? |

### Decision rights calls in this output

| Item | Agent role | Routed to |
|---|---|---|
| Calendar, poster, and retention rows | Drafts for sign-off | Theo Vasquez-Brandt, then counsel |
| "Tell me we're good to go in Colorado" | Refuses and routes | Counsel, with the Unverified Colorado rows listed |

### Metrics

| Metric | Baseline | Owner |
|---|---|---|
| Verified calendar coverage | 41 of 48 rows: 41 / 48 = 85.4% | Compliance manager |
| AI notice coverage | Screening is confirmed for NYC only and the assistant has no notice: 0 / 2 = 0% | Compliance manager |
| On-time obligation completion | Set at Q1 close | Compliance manager |

### Audit trail

- Inputs used: location counts and AI tool list (synthetic).
- Tools called: HRIS (work location, employment type counts); OSHA and DOL pages (read-only fetch, 18 Nov 2026); `ask_governance_policy` (Key dates rows).
- Items needing sign-off: calendar and retention rows (counsel); posters (HR operations).
- Open legal questions: NYC AEDT coverage; Colorado enforcement status; whether the review assistant is used in discipline.
