# Reproduce the validation environment

This setup is for contributors running the tools, evaluations, and repository
checks. The templates can be read without installing Python packages.

The requirement files declare supported dependency ranges. `requirements-lock.txt`
records exact direct and transitive versions resolved for Python 3.11 and later.
CI installs that file so each run uses the same reviewed environment.

## Install

From the repository root, with Python 3.11 or later:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-lock.txt
python -m pip check
python -m pytest 10-mcp-agents 09-evals -q
python -m ruff check .
python scripts/verify_claims.py
```

On Windows, activate with `.venv\Scripts\Activate.ps1` in PowerShell.
Notebooks may need `jupyter` for an interactive editor; it is not required for
the notebook execution checks in CI. Live model calls require separate provider
setup and can incur costs. Never put API credentials in committed files.

## Refresh dependencies

Install [uv](https://docs.astral.sh/uv/) and run from the repository root:

```bash
uv pip compile requirements-dev.in --python-version 3.11 --universal --no-header \
  --upgrade --output-file requirements-lock.txt
```

Install the regenerated lock in a fresh environment and run the checks above.
Confirm notebook execution in CI before merging. Commit the range changes and
lock together. The MCP SDK remains below version 2 because this server uses
the version 1 FastMCP interface; a major migration needs its own review.

Do not update `pydantic-core` independently of `pydantic`: the parent package
requires an exact core version. Regenerate the complete lock with compatible
parent versions rather than hand-editing transitive pins. `pip check` verifies
installed package contracts; the server import check separately verifies the
interface the application actually uses.

The lock does not prove that packages are vulnerability-free. Security updates
still need review and validation. Optional model SDKs installed for live runs
are separate from this offline environment.
