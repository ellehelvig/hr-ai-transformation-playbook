# Worked example: talent acquisition

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Dana Fernwood, Senior Recruiter, writes: "We're opening a Senior Data Engineer req open to Chicago, Denver and Berlin. The hiring manager wants a CS degree and eight must-haves. Can we turn on the ATS add-on that ranks applicants? Last time the resume screen looked lopsided. Build the plan." Dana attaches last quarter's aggregate screen-stage counts:

| Self-identified group | Entered screen | Advanced | Rate |
|---|---|---|---|
| Women | 80 | 14 | 17.5% |
| Men | 120 | 30 | 25.0% |

## Output (abridged)

### Role and scope

Senior Data Engineer, L5. Locations: Illinois, Colorado, Germany. Gap labeled: works council status in Germany not confirmed.

### Job analysis

| Requirement | Type | Task it supports | Skill evidence accepted | Confirmed by |
|---|---|---|---|---|
| Builds batch and streaming pipelines | Must | Owns ingestion for billing data | Work sample or shipped project | Hiring manager (pending) |
| Orchestration tool experience | Trainable | Schedules jobs | Learnable in first 60 days | Hiring manager (pending) |
| CS degree | Removed | No task tied to the credential | Skills evidence above | Hiring manager (pending) |
| ... | | | | |

Eight must-haves reduced to five; three moved to nice-to-have or trainable.

### AI use by stage

| Stage | Tool | AI role | Human review point | Fairness audit status |
|---|---|---|---|---|
| Job description | `lint_jd_language` | Flags wording | Recruiter | Not needed |
| Resume screen | `screen_resume_against_jd` | Evidence map, no score | Recruiter reviews every screen-out | Not needed |
| Resume screen | ATS ranking add-on | Ranks applicants | Not approved | None on file: blocked |

### Decision rights applied

| Item | Agent role | Routed to |
|---|---|---|
| Job description and interview kit | Drafts for sign-off | Dana, then hiring manager |
| Turn on the ranking add-on | Refuses and routes | People Analytics and Legal, with `fairness-audit-prep` |
| State Colorado notice duties | Refuses and routes | Counsel, via the Key dates row |

### Screen-stage flag

Women's rate 14 / 80 = 17.5%. Men's rate 30 / 120 = 25.0%. Ratio 17.5 / 25.0 = 0.70, below 0.8. A screening flag under 29 CFR 1607.4(D), not a finding. With 44 advanced in total, People Analytics runs a statistical test and interprets it.

### Metrics this plan tracks

First-year retention of hires; stage selection rate ratio by group, each quarter; human review request resolution.

### Audit trail

- Inputs used: req fields, hiring manager list, aggregate screen counts. Gap: works council status.
- Tools called and fields read: `calibrate_recruiter_intake` (intake text); `lint_jd_language` (draft text); ATS export (stage, counts, self-identified group in aggregate). No candidate names read.
- Items needing sign-off: must-have list (hiring manager); posting (Dana); interview kit (panel).
- Open legal questions: Illinois HB 3773 (Public Act 103-0804), Colorado SB 26-189 (ADMT Act), EU AI Act, high-risk HR systems: counsel confirms scope; see the Key dates rows.
