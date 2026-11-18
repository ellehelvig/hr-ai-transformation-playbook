# Worked example: benefits

Harbor & Pine is a fictional company. All data here is synthetic.

## Request

Noor Abernathy, benefits lead, writes: "Draft the 2027 open enrollment email and FAQ comparing our two medical plans for US staff. The 2027 SBCs are attached. Enrollment closes 20 November. Also, use the carrier's claims extract to find employees likely to be pregnant next year so we can send them the maternity guide directly."

| 2027 plan, employee-only (from the SBCs) | PPO | HDHP with HSA |
|---|---|---|
| Premium per paycheck (26 paychecks) | 68 | 22 |
| Deductible | 500 | 1,800 |
| Out-of-pocket maximum | 3,000 | 4,000 |
| Employer HSA contribution | None | 750 |

## Output (abridged)

### Scope

2027 open enrollment; US staff only (1,190); Germany staff (210) are not on these plans. Health information present: yes, in the second request.

### Sensitivity screen

Routed: the claims request asks the agent to infer pregnancy from health plan data. Stopped before any claims data was read.

### Source documents used

| Document | Plan year | Section cited |
|---|---|---|
| PPO SBC | 2027 | Important questions; premium page |
| HDHP SBC | 2027 | Important questions; HSA page |

### Draft

DRAFT email: "Open enrollment runs until 20 November. If you take no action, your current medical election carries over... An AI assistant helped draft this email; reply to reach a benefits specialist."

DRAFT comparison (no plan is named as best):

| Annual figure | PPO | HDHP with HSA |
|---|---|---|
| Premiums | 68 x 26 = 1,768 | 22 x 26 = 572 |
| Premiums plus out-of-pocket maximum | 1,768 + 3,000 = 4,768 | 572 + 4,000 = 4,572 |
| Same, after employer HSA contribution | 4,768 | 4,572 - 750 = 3,822 |

...

### Routed items

| Question or issue | Routed to | Why |
|---|---|---|
| Find likely pregnant employees from claims | Privacy owner and counsel | Health inference is prohibited by `ai-use-policy.md`; plan records stay separate from employment records |

### Decision rights calls

- Drafted for sign-off: email, FAQ and comparison (Noor Abernathy).
- Refused and routed: the claims inference. Offered instead: an opt-in note in the email telling all eligible staff where the maternity guide is.

### Audit trail

- Inputs used: 2027 SBCs, enrollment deadline, US headcount. `[GAP: 2027 SPD not supplied; FAQ answers on dependents marked for the specialist]`.
- Tools called and fields read: plan document repository (2027 SBCs); benefits platform (2026 active elections by preferred language, aggregate).
- Items needing sign-off: email, FAQ, Spanish version.
- Open legal questions: California CPPA regulations if an enrollment assistant processes California staff data. See the Key dates row; counsel confirms.

### Metrics the plan will track

Active election rate by group. Last year: English-preferred 951 / 1,102 = 86.3%; Spanish-preferred 61 / 88 = 69.3%; overall 1,012 / 1,190 = 85.0%. The 17-point gap is why a Spanish version is drafted. Also cited-answer accuracy for the enrollment FAQ.

### Owner and next step

Noor Abernathy approves the email and FAQ; the privacy owner answers on the maternity guide.
