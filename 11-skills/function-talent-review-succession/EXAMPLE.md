# Worked example: talent review and succession

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Imogen Starling, Talent Lead, writes: "The Director of Platform Engineering role is critical and the holder retires next year. Prep the succession review. Our three internal candidates are Bram Ellery, Tova Lindqvist and Kasimir Oduro; rank them so the committee can move fast. People Analytics sent last cycle's engineering counts for people rated Exceeds on performance:"

| Group | Rated Exceeds | Placed in top potential band | Rate |
|---|---|---|---|
| Men | 40 | 16 | 40.0% |
| Women | 25 | 6 | 24.0% |

## Output (abridged)

### Scope and owner

Task: succession slate. Decision owner: succession committee, chaired by the CHRO. Gaps: no written definition of potential; career interest unknown for Kasimir.

### Critical roles

| Role | Business impact | Replacement risk | Named successors or pool | Confirmed by |
|---|---|---|---|---|
| Director of Platform Engineering | Owns uptime for all customer products | Holder retiring; no external bench | Named successors plus a platform leadership pool | Leadership team (pending) |

### Narratives (drafts for committee)

Bram Ellery: led the 2026 storage migration (observed by two peer directors); readiness stated as "ready with development in budget ownership"; career interest confirmed. ...

Kasimir Oduro: ... Career interest not recorded; the manager asks before the committee meets.

No narrative compares candidates.

### Bias checks (aggregate)

| Check | Result | Route to |
|---|---|---|
| Potential vs performance by group | Women 6 / 25 = 24.0%; men 16 / 40 = 40.0%; ratio 24.0 / 40.0 = 0.60, below 0.8 | People Analytics and Legal: a flag under 29 CFR 1607.4(D), not a finding; groups this small need a statistical test |
| Skills data source and recency | Two of three profiles self-reported, last updated 2023 | Skills taxonomy owner |

### Decision rights applied

| Item | Agent role | Routed to |
|---|---|---|
| Readiness narratives for each candidate | Drafts for sign-off | Succession committee |
| Rank Bram, Tova and Kasimir | Refuses and routes | Succession committee, which compares in the meeting |
| Behavioral anchors for potential | Drafts for sign-off | Talent review group |

### Metrics this plan tracks

Critical role internal fill rate; top-potential rate ratio by group within performance level, each cycle; development action follow-through.

### Next step

Succession committee decides the slate at its December meeting.

### Audit trail

- Inputs used: role data, three candidates' supplied evidence, aggregate counts from People Analytics. Gaps: potential definition, one career interest.
- Tools called and fields read: HRIS (job, level, time in role); skills platform (skill, evidence source, last updated). No health, leave or family fields read.
- Items needing sign-off: critical role (leadership team); narratives (committee); anchors (talent review group).
- Open legal questions: Illinois HB 3773 (Public Act 103-0804) and EU AI Act, high-risk HR systems if a matching tool is added later. Counsel confirms; see the Key dates rows.
