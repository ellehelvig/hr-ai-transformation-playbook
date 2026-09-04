# Security

This repo contains templates, prompts, notebooks on synthetic data, and a small MCP server. None of it should ever hold real employee data. If you find something that does, or a way the code could leak or mishandle data, please report it.

## Reporting

Email ellehelvig@gmail.com with "hr-ai-playbook security" in the subject. Include what you found, where, and how to reproduce it. You'll get a reply within 5 business days.

Please don't open a public issue for anything that involves personal data or a live exploit path.

## What counts

- Real personal or employee data anywhere in the repo, including notebook outputs and eval results
- A prompt or tool that could be used to extract system instructions or another user's data
- Dependency vulnerabilities in `requirements.txt` or `10-mcp-agents/requirements.txt`
- Injection paths in the MCP tools (`10-mcp-agents/*/tool.py`)

## What doesn't

- Governance content you disagree with. Open an issue or PR instead.
- Regulatory claims that have gone stale. The docs are re-checked weekly against primary sources, but if you spot something, open an issue with the citation.

## Scope note

The MCP server is a reference implementation. It runs locally, makes no external API calls, and has no authentication layer because it is not meant to be exposed on a network. If you deploy it anywhere shared, that's on you to secure.
