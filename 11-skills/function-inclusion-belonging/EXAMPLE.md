# Worked example: inclusion and belonging

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Tamsin Vale, inclusion programs lead, writes: "Please review three programs before next cycle. Emerging Leaders is open to L4 and above, but managers nominate with no written criteria. The Women in Engineering mentoring circle is open to women engineers only. The Code Path apprenticeship requires a CS degree. We have no federal contracts that I know of, but we hold one research grant. Here are last cycle's Emerging Leaders nominations, aggregated."

| Age band | Eligible | Nominated |
|---|---|---|
| Under 40 | 410 | 38 |
| 40 and over | 190 | 9 |
| Total | 600 | 47 |

## Output (abridged)

```markdown
## Scope
US (CA, IL, NYC, CO) and Germany; federal grant Y, contracts N (counsel to
confirm); 3 programs; owners: L&D lead, Engineering, TA; counsel named

## Program access review
| Program | As written | As practiced | Open to all eligible | Question for counsel |
| Emerging Leaders | L4+ | manager nomination, no criteria | Y as written, unclear in practice | Is unstructured nomination consistent with job-related selection? |
| Women in Engineering circle | women engineers | same | N | Membership limited by sex; see EEOC ERG examples |
| Code Path | CS degree | same | Y | Is the degree a documented job requirement? |

## Selection criteria
| Code Path | CS degree | Proposed: degree OR assessed coding task OR portfolio | ... |

## Adverse impact screen (aggregates only)
| Step | Group | Selected / eligible | Rate | Ratio to highest | Flag |
| Nomination | Under 40 | 38 / 410 | 9.3% | 1.00 | |
| Nomination | 40 and over | 9 / 190 | 4.7% | (9/190) / (38/410) = 0.51 | Below 0.80 |
Screening flag only (29 CFR 1607.4(D)), not a verdict. Group of 9 is small:
People Analytics runs a statistical test per fairness-audit-prep; counsel
interprets.

## Decision rights calls
| Request | Agent role | Routed to |
| Rewrite the Code Path posting with skills evidence | Drafts for sign-off | TA lead |
| Structured nomination criteria for Emerging Leaders | Drafts for sign-off | L&D lead and counsel |
| "Just tell us the mentoring circle is fine to keep" | Refuses and routes | Counsel, with the access review |

## Next step owner
Counsel: mentoring circle eligibility, grant certification (Key dates row
"US Executive Order 14173"). L&D lead: nomination criteria.

## Audit trail
Inputs used: program rules, aggregate nomination counts. Not provided:
written nomination criteria.
Tools called:
| LMS (read-only) | eligibility rules | program name, eligibility text |
| lint_jd_language | Code Path posting | posting text |
Needs sign-off: criteria (L&D lead, counsel), posting (TA lead)
Open legal questions: circle eligibility; grant certification; Germany
programs out of US guidance scope
```

Metrics this plan tracks: open-access program rate (1 of 3 open in practice today), accommodation first-response time, and selection steps with a screening flag (1 of 1 tested).
