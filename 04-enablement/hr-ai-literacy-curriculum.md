# HR AI literacy curriculum

A 4-module learning program for HR professionals at all experience levels. Designed to be delivered as a facilitated series over 4–6 weeks, or adapted for self-paced completion.

**Total time:** ~8 hours across all modules  
**Format:** Workshop + async reading + hands-on practice  
**Audience:** All People Team members  
**Prerequisite:** None

---

## Program overview

| Module | Title | Duration | Format |
|---|---|---|---|
| 1 | How AI works — what HR professionals actually need to know | 90 min | Workshop |
| 2 | Using AI in your daily HR work | 2 hours | Workshop + lab |
| 3 | Governance, ethics, and responsible use | 90 min | Workshop |
| 4 | Building and scaling AI use cases | 2 hours | Workshop + project |

---

## Module 1: How AI works — what HR professionals actually need to know

**Learning objectives:**
- Explain the difference between traditional automation and generative AI
- Describe why AI "hallucinates" and how to mitigate it in HR contexts
- Identify which HR tasks are good candidates for AI assistance and which are not

**Session outline (90 minutes):**

| Time | Activity |
|---|---|
| 0:00–0:10 | Opening: What do you already believe about AI? (quick poll + discussion) |
| 0:10–0:30 | Concept: How LLMs work — without the jargon (facilitator presentation) |
| 0:30–0:45 | Concept: Hallucination, confidence, and why AI makes things up |
| 0:45–1:05 | Exercise: Spot the hallucination (participants identify errors in AI-generated HR content) |
| 1:05–1:20 | Discussion: Where should HR use AI? Where should we be cautious? |
| 1:20–1:30 | Wrap-up + homework: Try one AI tool before next session |

**Key concepts to cover:**

*What LLMs actually are:*
Large language models predict the next most likely word given context. They don't "know" things the way a database knows things — they pattern-match against training data. This is why they can sound authoritative while being wrong.

*The spectrum from rule-based to agentic:*
```
Rule-based automation → AI Copilot → AI Agent
(deterministic)         (assisted)    (autonomous)
```
Most HR AI today sits in the middle. True agentic AI — where the model takes multi-step actions autonomously — is emerging and brings new governance requirements.

*Prompt quality drives output quality:*
The single highest-leverage skill for HR professionals using AI is prompt construction. Vague prompts produce generic output. Specific, well-structured prompts with good context produce usable output.

**Pre-reading (assign before session):**
- [Your organization's AI use policy](../03-governance/ai-use-policy.md)
- One-page primer on generative AI for non-technical audiences (create or source)

---

## Module 2: Using AI in your daily HR work

**Learning objectives:**
- Write effective prompts for HR use cases
- Use the prompt library for at least 3 HR workflows
- Identify when to use AI, when to verify AI output, and when not to use it

**Session outline (2 hours including lab):**

| Time | Activity |
|---|---|
| 0:00–0:15 | Share-back from Module 1 homework — what did you try, what happened? |
| 0:15–0:45 | Prompt engineering for HR: the four elements of a good prompt |
| 0:45–1:10 | Live demo: Onboarding plan, performance review draft, policy Q&A |
| 1:10–1:50 | Hands-on lab: Each participant works through 2 prompts from the library using their own real work |
| 1:50–2:00 | Debrief: What surprised you? What didn't work? |

**The four elements of an effective HR prompt:**

1. **Role** — Tell the AI who it is. "You are an experienced HRBP..." produces better output than just asking a question.

2. **Context** — Provide the specific details the AI needs. Role, tenure, team size, situation. Don't make the AI guess.

3. **Task** — State clearly what you want it to produce. One output per prompt. "Draft a..." is clearer than "Help me with..."

4. **Constraints** — Define length, tone, format, and what to avoid. "300 words, no bullet points, avoid generic phrases" significantly improves output quality.

**Lab instructions:**

Participants choose 2 prompts from the library that are relevant to their current work:
1. Run the prompt with a real (or realistic) example from their work
2. Evaluate the output: What's useful? What's wrong or missing? What would you change before using it?
3. Iterate: Modify the prompt once based on what you learned and run it again
4. Note: What changed between run 1 and run 2?

**The verify-before-use rule:**

Introduce and reinforce this heuristic:
- Policy details → always verify against source system before sharing
- Legal requirements → always verify with Legal before relying on
- Factual claims → spot-check against a known source
- Tone and content → always read before sending; AI doesn't know your audience

---

## Module 3: Governance, ethics, and responsible use

**Learning objectives:**
- Apply the organization's AI use policy to real HR scenarios
- Identify the key legal risk areas in HR AI (bias, privacy, employment law)
- Complete a basic risk assessment for a new use case

**Session outline (90 minutes):**

| Time | Activity |
|---|---|
| 0:00–0:15 | Case study: Three HR AI failures and what we can learn (discussion) |
| 0:15–0:40 | Framework: What makes AI use in HR risky? Legal and ethical dimensions |
| 0:40–1:00 | Scenario practice: Is this use case okay? (small groups, 4 scenarios) |
| 1:00–1:20 | Walk-through: The risk assessment template |
| 1:20–1:30 | Q&A + open discussion |

**Key legal risk areas to cover:**

*Bias and disparate impact:*
AI trained on historical HR data can encode and amplify past discrimination. An AI that learned from 10 years of hiring decisions at a company where 80% of engineering hires were male will score resumes accordingly. Annual adverse impact testing is not optional — it's legally and ethically required.

*Illinois AI Video Interview Act, NYC Local Law 144, and emerging state laws:*
Several jurisdictions now require disclosure, impact assessments, or consent for AI use in hiring. The regulatory landscape is shifting quickly. Use cases involving hiring must be reviewed against current state law.

*GDPR and CCPA:*
Employees in covered jurisdictions have rights regarding automated decision-making. Know which of your employees are covered and how your AI use cases interact with their rights.

*The "AI as a manager" trap:*
AI that monitors, evaluates, or scores employees without their knowledge — even for legitimate purposes — creates legal and trust exposure. Transparency is not just ethical, it's protective.

**Scenario practice cards:**

Print or share these four scenarios. Groups of 3–4 discuss: Is this use appropriate? What are the risks? What would you change?

> **Scenario A:** An AI tool automatically rejects resumes with gaps of more than 6 months without showing them to a recruiter.

> **Scenario B:** An HRBP uses an AI writing assistant to draft a PIP for an employee, then reviews and edits it before sharing with the manager.

> **Scenario C:** People Analytics builds an attrition risk model that scores all employees monthly and shares the scores directly with managers.

> **Scenario D:** An AI chatbot answers benefits questions for employees. It sometimes gives incorrect information but flags that users should confirm with HR.

---

## Module 4: Building and scaling AI use cases

**Learning objectives:**
- Apply the prioritization matrix to identify your team's highest-value AI use cases
- Define a use case with clear success metrics and governance requirements
- Draft a basic implementation plan for a low-complexity use case

**Session outline (2 hours):**

| Time | Activity |
|---|---|
| 0:00–0:15 | Opening: What does "scaling AI in HR" actually mean? |
| 0:15–0:45 | Framework: From idea to deployment — the use case lifecycle |
| 0:45–1:15 | Team exercise: Prioritization matrix applied to your team's top 5 ideas |
| 1:15–1:45 | Small group: Draft a one-page use case spec for your top-ranked idea |
| 1:45–2:00 | Gallery walk + feedback |

**Use case lifecycle:**

```
Discover → Prioritize → Design → Pilot → Evaluate → Scale
   ↑                                          |
   └──────────────── iterate ─────────────────┘
```

- **Discover:** What problem are we solving? Who feels it most?
- **Prioritize:** Use the matrix. Don't skip this.
- **Design:** Define inputs, outputs, human review gates, success metrics, and fallback
- **Pilot:** Small scope, high observation. 4–8 weeks.
- **Evaluate:** Did it work? For whom? What didn't?
- **Scale:** Expand with the lessons from pilot baked in

**One-page use case spec template:**

Participants complete this for their team's top-ranked use case:

```
Use case name:
Problem it solves (1 sentence):
Who benefits and how:
AI approach (Agent / Copilot / Automation / Analytics):
Data needed:
Human review gate:
Success metric(s):
What could go wrong:
Governance requirements (from risk assessment):
First step to move forward:
```

---

## Assessment and certification

Participants who complete all four modules and the hands-on components receive a **HR AI Practitioner** acknowledgment from the People Team.

Optional extension: Participants who complete a full use case spec and present it to the HR Technology team are recognized as **HR AI Champions** — an informal internal designation that supports peer enablement.

---

## Facilitator notes

- Module 3 generates the most discussion and sometimes the most resistance. Budget flex time.
- The hands-on lab in Module 2 is the highest-value session — don't let it get cut for time.
- Adapt the case studies and scenarios in Module 3 to your organization's actual context. Generic examples land less well than ones that feel real.
- Keep an AI skeptic on the facilitation team if possible. The best discussions happen when the room has range.
