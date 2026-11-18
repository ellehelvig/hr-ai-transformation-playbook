# Worked example: HR AI governance

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Odile Farraday-Kim, VP People Operations and program owner at Harbor & Pine (1,400 staff in California, Illinois, NYC, Colorado, and Germany), writes: "Our CHRO wants an HR AI inventory and the first quarterly report by Friday. Here is what the team listed. Route each tool, and please approve the scheduling optimizer so support can use it in January."

| Tool | Use | Where | Oversight owner |
|---|---|---|---|
| ATS resume screening feature | Filters applicants | All US | Recruiting operations lead |
| Review writing assistant | Drafts review text | All | HRBP lead |
| HR helpdesk assistant (internal, read-only) | Answers policy questions with citations | All | HR operations lead |
| Shift scheduling optimizer | Assigns support shifts | Colorado, Germany | None named |
| Spreadsheet AI add-in (found in app catalog) | Merit increase modeling | California | None named |

## Output (abridged)

### Routing for this request

| Tool | Skill | Why | Owner of next step |
|---|---|---|---|
| ATS resume screening | `hr-ai-vendor-review`, `fairness-audit-prep` | Vendor tool that filters people; check NYC Local Law 144 coverage | Recruiting operations lead |
| Review writing assistant | `hr-ai-vendor-review`, `eu-ai-act-hr-classifier` | Feeds performance reviews of German staff | HRBP lead |
| HR helpdesk assistant | `hr-ai-use-case-intake` | Internal agent, no decisions about people | HR operations lead |
| Shift scheduling optimizer | `eu-ai-act-hr-classifier`, `fairness-audit-prep` | Allocates tasks to workers in Germany; owner UNRESOLVED, so held | Odile Farraday-Kim to name an owner |
| Spreadsheet AI add-in | Stop: employment counsel under `pay-equity-governance.md` | Touches pay | Employment counsel |

### Decision rights calls in this output

| Item | Agent role | Routed to |
|---|---|---|
| Inventory, routing, and report | Drafts for sign-off | Odile Farraday-Kim, then the CHRO |
| "Approve the scheduling optimizer for January" | Refuses and routes | Reviewers in the RACI, after an owner is named and launch conditions in section 8 are met |
| Merit modeling add-in | Refuses and routes | Employment counsel |

### Quarterly governance report (DRAFT)

| Measure | This quarter | Action |
|---|---|---|
| Inventory by tier | High 2, Medium 2, held 1 | Tier the add-in after counsel review |
| Inventory review currency | 1 of 5 entries current: 1 / 5 = 20% | Complete vendor reviews by next quarter |
| Fairness monitoring coverage | 0 of 2 tools that filter or allocate people have a monthly check: 0 / 2 = 0% | Start checks before any expansion |
| Time to pause | No breaches logged; baseline next quarter | ... |

### Audit trail

- Inputs used: team tool list and location counts (synthetic).
- Tools called: app catalog export (app name, user counts by department); ATS admin console (AI feature name, enabled status); `ask_governance_policy` (launch conditions). No employee records read.
- Items needing sign-off: charter and report (CHRO); routing (Odile Farraday-Kim); add-in (employment counsel).
- Open legal questions: NYC Local Law 144 coverage of the screening feature; EU AI Act, high-risk HR systems status of the optimizer; works council involvement in Germany.
