# CLAUDE.md

Shared contract for every Claude session and every automated agent working in this
repository. Read this before changing anything.

## What this repo is

An open-source toolkit for HR and People teams putting AI into production
responsibly. It is published, cited, and used by practitioners who make real
employment decisions about real people. A wrong claim here is not a cosmetic bug,
it is a liability for whoever acts on it. Accuracy outranks completeness, and
completeness outranks speed.

One maintainer reviews everything. Keep proposals small enough for one person to
review carefully.

## Writing style

- No em dashes anywhere. This includes Markdown, Python docstrings and comments,
  notebook cells, YAML, JSON, and escaped em dash sequences (U+2014) inside
  notebook JSON. Use a comma, a colon, or two sentences.
- Short sentences. Plain language. No jargon that only makes sense inside one
  company.
- Avoid "leverage", "utilize", "seamless", "robust", "transformative".
- No inflated claims. If the repo asserts something, the repo should be able to
  prove it.

## Legal and regulatory claims

This is the highest-risk content in the repo. The rules are strict on purpose.

- Primary sources only. Statute text, the enrolled bill, the regulator's own
  page, a court order or docket entry. A law firm alert or vendor blog is a lead
  worth following, never a citation.
- Secondary sources get dates wrong routinely. Check the bill history for the
  actual signing or enactment date instead of trusting a summary.
- Phased statutes carry per-section applicability dates. Cite the date for the
  specific obligation being described, not the date the act as a whole enters
  into force.
- State status precisely: enacted, signed, pending, in committee, stayed,
  vacated, superseded. Never describe a pending bill as law.
- Governance content should say when counsel needs to see it before adoption.

## Standing content rules

- Synthetic data only. No real employee or candidate data anywhere, including
  test fixtures, notebook outputs, and eval results.
- Every prompt carries tuning notes naming the model tested and what changed.
- Skills stop at the human. A skill may draft, score against a rubric, or route.
  It may not make an employment decision, assign a score to a named person, or
  write to an HR system.
- Notebooks are executed outputs, not source. Do not hand-edit notebook JSON.

## Repository map

| Path | Contents |
|---|---|
| `01-use-cases` | Vetted HR AI use cases, prioritization matrix, intake template |
| `02-prompt-library` | Tested prompts with tuning notes, by HR function |
| `03-governance` | Policy, risk assessment, EU AI Act intake, vendor and deployer checklists |
| `04-enablement` | Literacy curriculum, facilitator guide, adoption playbook |
| `05-notebooks` | Executable analyses, all synthetic data, all executed in CI |
| `06-roadmap` | Transformation roadmap, KPI framework, phase gates |
| `07-agentic-patterns` | Architecture patterns, agent design, testing framework |
| `08-roi-measurement` | Business case, ROI framework, live dashboard |
| `09-evals` | Eval cases, rubric with launch-blocking gates, runner and judge |
| `10-mcp-agents` | Working MCP server: comp banding, screening, intake, policy Q and A |
| `11-skills` | Installable agent skills |

## CI gates

Everything in `.github/workflows/ci.yml` must pass before merge. It currently runs:

- `ruff check .` repo-wide, which includes notebook cells. Rule selection is
  pinned in `ruff.toml` so a newer ruff cannot silently change what is enforced.
- `pytest 09-evals -q` and `pytest 10-mcp-agents -q`
- YAML parse of every `.yaml` and `.yml`
- `python -m py_compile 09-evals/run-evals.py`
- Skill package validation: every `11-skills/*/SKILL.md` needs `name` and
  `description` in its frontmatter
- Notebook execution under nbclient
- markdownlint against `.markdownlint.json`, which sets `"default": false` and
  enables only MD001 (heading increment), MD009 (trailing spaces), and MD010
  (hard tabs). Nothing else is enforced, so do not chase blank-line rules.
- Internal Markdown link check
- `python scripts/verify_claims.py`, which recomputes every count the README states
  from the tree and scans all text files for em dashes. If you change a count, a
  section, a test, or a skill, run this before you push.

Notebook execution takes several minutes. Skip it locally unless a notebook
changed.

## Rules for automated agents

- Never push to `main`. Open a pull request from a branch prefixed `bot/`.
- One concern per pull request. A regulatory correction and a README count fix
  are two pull requests.
- Every factual change carries its source in the pull request body. A claim
  without a primary-source link does not merge.
- Do not edit released version entries in `CHANGELOG.md`. Add to an
  `## [Unreleased]` section instead.
- Do not touch `LICENSE`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, or `CITATION.cff`.
- If a check fails and the fix is not obvious, say so in the pull request body
  rather than guessing at it.
- Propose, do not decide. The maintainer merges.
