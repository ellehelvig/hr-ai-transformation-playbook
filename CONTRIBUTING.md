# Contributing

This playbook improves when practitioners send back what they learned in production. That's the contribution worth the most: a prompt you tuned, a vendor conversation that surfaced a gap, a regulation that changed in your jurisdiction.

## What to contribute

- **Use cases** not in the library. Use the [intake template](01-use-cases/intake-template.md) or the [issue form](https://github.com/ellehelvig/hr-ai-transformation-playbook/issues/new?template=new-use-case.md).
- **Prompt improvements** you've tested, with tuning notes that name the model and what changed.
- **Skills.** New skills for `11-skills/`, or fixes to existing ones. Follow the structure in the [skills README](11-skills/README.md#writing-your-own).
- **Governance updates.** New jurisdictions, changed law, better templates. Use the [regulatory update form](https://github.com/ellehelvig/hr-ai-transformation-playbook/issues/new?template=regulatory-update.md).
- **Notebooks and tools.** New analyses, or improvements to the MCP tools in `10-mcp-agents/`.
- **Corrections.** Anything wrong, stale, or missing.

## How

1. Fork the repo and create a branch: `git checkout -b what-you-changed`
2. Make the change
3. Run the checks CI will run (see below)
4. Open a pull request. The [template](.github/PULL_REQUEST_TEMPLATE.md) asks for what changed and why.

## Standards

- **Primary sources for legal claims.** Cite statute text, court orders, or regulator pages. A law firm's summary is a lead, not a citation.
- **Synthetic data only.** No real employee or candidate data anywhere, including notebook outputs and eval results.
- **Tuning notes on every prompt.** Name the model you tested on and what you observed.
- **Skills stop at the human.** A skill may draft, score against a rubric, or route. It may not make an employment decision, assign a score to a named person, or write to an HR system.
- **Plain language, no em dashes.** Short sentences. No jargon that only makes sense inside one company.
- **Flag legal review.** Governance content should say when counsel needs to see it before adoption.

## Running the checks locally

```bash
pip install -r requirements.txt -r 10-mcp-agents/requirements.txt ruff pytest
ruff check 09-evals 10-mcp-agents
pytest 10-mcp-agents 09-evals -q
npx markdownlint-cli --config .markdownlint.json '**/*.md' --ignore node_modules
```

CI also executes the notebooks, validates YAML, checks internal links, and validates skill frontmatter. Notebook execution takes a few minutes; you can skip it locally unless you changed a notebook.

## Questions

Open an issue. For anything involving personal data or a security concern, see [SECURITY.md](SECURITY.md) instead.
