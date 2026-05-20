# AI use case risk assessment template

Complete this template before deploying any new AI use case in HR. Submit to the HR Technology governance review process.

**Intake date:** [DATE]  
**Submitter:** [NAME, TITLE]  
**Target launch date:** [DATE]

---

## 1. Use case overview

**Name:**

**One-sentence description:**

**HR function(s) affected:**
- [ ] Talent Acquisition
- [ ] Onboarding
- [ ] Performance Management
- [ ] Learning & Development
- [ ] HR Operations / Employee Experience
- [ ] People Analytics
- [ ] Compensation & Benefits
- [ ] Employee Relations

**Estimated users:** [Number of HR team members using the tool] / [Number of employees affected by its outputs]

**Tool / vendor:** [Name, or "internally built"]

**AI approach:**
- [ ] Agent (autonomous multi-step task completion)
- [ ] Copilot (AI-assisted, human makes final decision)
- [ ] Automation (structured workflow with AI components)
- [ ] Analytics (AI-augmented data analysis)

---

## 2. Data inventory

### What employee data does this use case access or process?

| Data type | Source system | Sensitivity | Purpose |
|---|---|---|---|
| [e.g., Job title, tenure] | [HRIS] | Low | [Context for recommendations] |
| [e.g., Performance ratings] | [Performance system] | High | [Training signal] |
| [e.g., Survey responses] | [Survey tool] | High | [Sentiment analysis] |

### Does this use case process any of the following?

| Data type | Yes/No | Notes |
|---|---|---|
| Protected category data (race, gender, age, disability, religion, national origin) | | |
| Health or medical information | | |
| Financial or compensation data | | |
| Immigration status | | |
| Communications data (email, Slack, calendar) | | |
| Biometric or behavioral data | | |

**If any "Yes" above:** Stop and consult Privacy and Legal before proceeding.

### Data retention:
- Is employee data stored by the AI tool or vendor? [Yes / No]
- If yes, for how long? [Duration]
- Is data used to train the vendor's models? [Yes / No / Unknown]

---

## 3. Decision impact assessment

**Does this use case influence or produce outputs that affect any of the following?**

| Employment decision | Involved? | Human review step? |
|---|---|---|
| Candidate screening or ranking | | |
| Interview selection | | |
| Offer generation | | |
| Performance rating | | |
| Promotion or advancement recommendation | | |
| Compensation change | | |
| Learning path assignment | | |
| Termination or PIP | | |
| Leave approval | | |
| Disciplinary action | | |

**If any employment decision is involved:** Document the human review step explicitly. An AI use case may not autonomously execute any item in this list without a documented human review gate.

---

## 4. Fairness and bias assessment

**Describe how the AI produces its outputs:**
[Brief description of the model, scoring approach, or generation method]

**Which groups could be disadvantaged if the model performs unevenly?**
[List protected characteristics or demographic groups relevant to this use case]

**Pre-deployment fairness testing:**
- [ ] Tested for disparate impact across relevant demographic groups
- [ ] Reviewed training data for historical bias
- [ ] Established baseline demographic distribution of inputs and expected outputs
- [ ] Not yet assessed — testing required before approval

**Post-deployment monitoring plan:**
- Metric(s) to monitor: [e.g., offer rate by gender, screening pass rate by race]
- Monitoring frequency: [Monthly / Quarterly]
- Threshold that triggers review: [e.g., >5% disparity vs. baseline]
- Owner: [Name or role]

---

## 5. Transparency and employee notice

**Will employees know AI was used in this process?**
- [ ] Yes — Privacy Notice updated, employees informed via [channel]
- [ ] Yes — disclosed at point of use (e.g., in the tool interface)
- [ ] No — not applicable (AI is used only internally, no employee-facing output)
- [ ] Not yet — notice update required before launch

**Can employees request human review of AI outputs that affect them?**
- [ ] Yes — process is: [describe]
- [ ] N/A — this use case has no employee-facing output

---

## 6. Risk classification

Score the overall risk level:

| Factor | Low | Medium | High |
|---|---|---|---|
| Employment decisions affected | None | Advisory input | Direct decision |
| Data sensitivity | Aggregate / low-sensitivity | Personal, non-sensitive | Sensitive personal data |
| Employee visibility | Internal only | Affects employee experience | Affects employee status |
| Regulatory exposure | Minimal | Some (state AI laws, GDPR) | High (EEOC, CCPA, IL AIAA) |
| Autonomy level | Human-in-the-loop throughout | Human reviews AI output | AI acts autonomously |

**Overall risk rating:** [ ] Low  [ ] Medium  [ ] High

---

## 7. Approval

| Reviewer | Sign-off required | Approved | Date |
|---|---|---|---|
| HR Technology Lead | Always | | |
| HR Leadership | Medium + High | | |
| Legal / Employment Counsel | Medium + High | | |
| Privacy / Data Protection | If personal data involved | | |
| CISO / Security | If external vendor or new data access | | |

---

## 8. Launch conditions

Before this use case goes live:

- [ ] All required approvals obtained
- [ ] Data processing agreements signed (if vendor involved)
- [ ] Employee notice updated or confirmed not required
- [ ] Human review gates documented and tested
- [ ] Monitoring plan activated
- [ ] Escalation path documented and communicated to HR team
- [ ] Rollback plan defined: [describe how to disable the tool if issues arise]
