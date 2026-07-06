# Testing and evaluating HR agents

Deploying an agent is not the end of the work, it's the beginning of a continuous improvement loop. HR agents interact with employees at moments that matter: policy questions, leave requests, onboarding, performance conversations. Getting it wrong has real consequences.

---

## The signal loop: how you test, learn, and improve

Your job as an operator is not to prove your agent works. Your job is to find where it breaks. Failures in testing are data. Failures in production are incidents.

### Step 1: Run it against real scenarios
Execute the agent against real or representative inputs. Don't cherry-pick easy ones. Use the actual questions employees ask, messy, ambiguous, edge-case questions. Pull from your HR helpdesk ticket history if you have it.

Build a test set before you launch. Minimum 20 scenarios covering:
- Common queries (high volume, routine)
- Edge cases (ambiguous, out-of-scope, emotionally charged)
- Adversarial inputs (attempts to get the agent to do something it shouldn't)
- Jurisdiction-specific queries (if your workforce is multi-country)

### Step 2: Read the signal
Look under the hood, not just at the final output. What tools did the agent call? What did it retrieve from your knowledge base? How did it reason step by step?

For RAG-based HR agents: did it retrieve the right policy chunks? Did it retrieve outdated versions? For tool-using agents: did it call the right tool, with the right parameters? Did it interpret the result correctly?

A correct final answer that was reached through bad reasoning is a fragile correct answer.

### Step 3: Diagnose before touching anything
Was the failure in the system prompt instructions? The knowledge base? The temperature setting? The model choice? The tool design?

Identify the root cause before making any changes. The most common mistake in agent debugging is making multiple changes at once, then you can't tell what actually fixed the problem.

Common HR agent failure patterns and their root causes:

| Symptom | Likely root cause |
|---|---|
| Agent gives correct answer but wrong jurisdiction | Policy doc store not segmented by geography |
| Agent escalates too aggressively | Escalation triggers in system prompt too broad |
| Agent gives outdated policy information | RAG knowledge base not refreshed after policy update |
| Agent refuses reasonable requests | Scope definition too restrictive |
| Agent takes action it shouldn't | Scope definition missing explicit prohibitions |
| Agent ignores tool output and answers from training data | Tool result not clearly formatted for the model to parse |
| Agent loops or stalls | No loop detection or step limit defined |

### Step 4: Adjust one variable
Make one targeted change. Document it. Describe what you changed, why, and what you expect to happen.

Shotgun edits, changing the system prompt, temperature, and knowledge base at the same time, make it impossible to know what fixed the problem. You'll face the same failure again and have no idea why.

### Step 5: Retest the same scenario
Did it improve? Did the change cause a regression somewhere else? Loop until the signal is clean.

For HR agents, "clean signal" means: correct answer, correct tone, correct escalation behavior, no information disclosure violations, consistent across multiple runs.

---

## The 4-question evaluation rubric

For every HR agent response you evaluate, ask these four questions. They replace the instinct of "that feels right" with a repeatable standard.

### 1. Factually correct?
Hallucination check. Did the agent make something up? Cross-reference against your policy knowledge base. For HR specifically: did it state the right number of leave days? The right eligibility criteria? The right process steps?

Trust but verify, every time, not just during testing. Build a spot-check process into your ongoing monitoring.

### 2. Complete?
Did it answer every part of the request? Is it appropriately thorough, not too verbose, not too thin? An employee who asks "what do I need to do to start parental leave?" needs the full process, not just "contact HR."

Completeness failures are often harder to catch than factual failures because the output sounds fine on a quick read.

### 3. Tone appropriate?
Does the emotional register match the situation? An employee asking about bereavement leave needs warmth and directness, not a clinical policy recitation. A manager asking about a PIP process needs precision, not hedging.

Tone is situational, not fixed. Your evaluation rubric should reflect the range of emotional contexts HR agents encounter, including distress, frustration, and confusion.

### 4. On brand?
Does this sound like your organization? Does it match your HR team's voice, your company's values, your culture? Would your CHRO be proud of this response?

Brand failures are the ones employees notice and remember. A factually correct but tone-deaf response damages trust in the entire HR AI program.

---

## Ongoing monitoring for production HR agents

Testing before launch is necessary but not sufficient. HR policies change, employee needs evolve, and model behavior can drift. Build monitoring in from day one.

**Weekly:**
- Review escalation logs: what are agents handing off to humans, and why?
- Spot-check 10 random conversations from each agent
- Check for any employee complaints or feedback flagged to HR

**Monthly:**
- Run the full test set against the live agent, has anything degraded?
- Review CSAT scores or satisfaction signals if collected
- Audit for any information disclosure incidents
- Check knowledge base currency: have any policies changed that aren't reflected?

**Quarterly:**
- Fairness audit: are different employee groups getting meaningfully different quality responses?
- Full escalation rate analysis by topic and team
- Policy alignment review with HR Legal
- Consider whether the model version in use is still appropriate or if an upgrade is warranted

**Trigger-based (act immediately):**
- Employee reports receiving incorrect policy information
- Agent takes an unauthorized action in a connected HR system
- Unusual spike in escalation rate (may signal a new type of query the agent can't handle)
- Policy update that affects any in-scope topic

---

## What good looks like: a quality benchmark for HR agents

Use this as your acceptance criteria before launching any HR agent to employees.

| Criterion | Target |
|---|---|
| Factual accuracy on policy questions (test set) | ≥95% |
| Appropriate escalation rate | 5–20% (below 5% = under-escalating; above 20% = over-escalating or undertrained) |
| Employee CSAT on agent interactions | ≥4.0/5.0 |
| Response completeness (human-rated spot check) | ≥90% |
| Tone appropriateness (human-rated spot check) | ≥90% |
| Zero information disclosure incidents | Required, not a percentage |
| Injection resistance (adversarial test set) | 100%, no exceptions |

No agent should go to production without passing the information disclosure and injection resistance criteria. Everything else is a target; those two are gates.
