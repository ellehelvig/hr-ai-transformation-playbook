# Worked example: HR AI readiness assessment

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Wren Castellano-Obi, Head of People Operations at Harbor & Pine (1,400 staff, US and Germany; HR team of 26), writes: "Where is HR on AI? We ran a US helpdesk chatbot pilot with a CSAT target. No AI policy, no tool list. The CHRO sponsors this; nobody decides go or no-go. A vendor webinar, no training record. HRIS exports go by ticket. Counsel heard about the pilot late. The Berlin works council has not been told. One generalist has four hours a week. Also, rank our recruiters by AI use."

## Output (abridged)

### Evidence and scores

| Dimension | Score | Evidence |
|---|---|---|
| Sponsor and decision owner | 1 | "nobody decides go or no-go" |
| Policy and governance | 0 | "No AI policy, no tool list" |
| Data readiness | 1 | "exports go by ticket" |
| HR team AI literacy | 1 | "A vendor webinar" |
| Tools in use | 1 | Consoles: ATS match score and review assistant on; app catalog: chat assistant |
| Legal, privacy, works council | 1 | Counsel told late; works council not told |
| Change capacity | 2 | "four hours a week" |

### Placement (DRAFT, for CHRO sign-off)

Starting level from use evidence: Level 2 (pilot with a metric).
Caps: governance 0 and five dimensions at 1 each cap at Level 1.
Placement: Level 1. Set by: policy and governance (0). Not an average.

### Gates

| Gate | Routed to | What it holds back |
|---|---|---|
| Berlin works council | Labor relations, counsel | Tools reaching German staff stay at Start |
| ATS match score screens candidates | `hr-ai-vendor-review`, `fairness-audit-prep` | Not a first use case |

### 90-day starter plan (DRAFT)

| Days | Action | Library skill (stage) | Owner role |
|---|---|---|---|
| 1-30 | Name decision owner; charter; inventory | `function-hr-ai-governance` (Start) | CHRO; HR technology lead |
| 1-30 | Review ATS match score evidence | `hr-ai-vendor-review`, `fairness-audit-prep` (Start) | Recruiting operations lead |
| 31-60 | Literacy plan and record (Key dates row "EU AI Act, AI literacy (Article 4)") | `function-learning-development` (Start) | L&D lead |
| 31-60 | Pick a low-risk first use case | `hr-ai-first-use-case-picker` (Start) | Wren |
| 61-90 | Pilot decision; rerun | ... | CHRO |

### Metrics baseline

| Metric | Today |
|---|---|
| HR AI literacy completion | 0 of 26 with a record: 0 / 26 = 0% |
| Inventory coverage | 0 of 4 tools with owner and tier: 0 / 4 = 0% |
| Intake to decision time | No intakes yet |

### Decision rights calls in this output

| Item | Agent role | Routed to |
|---|---|---|
| Placement and plan | Drafts for sign-off | Wren, then the CHRO |
| "Rank our recruiters by AI use" | Refuses and routes | L&D lead: team-level plan, no names |

### Audit trail

- Inputs used: Wren's notes (synthetic).
- Tools called: ATS and performance tool consoles (AI feature name, enabled status); app catalog (AI app names).
- Items needing sign-off: placement and plan (CHRO).
- Open legal questions: works council consultation; whether NYC Local Law 144 covers the ATS match score.
