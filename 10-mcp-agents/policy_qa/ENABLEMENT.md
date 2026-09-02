# Policy Q&A tool: handoff notes for whoever owns 03-governance

## What it does

Takes a plain-language question, searches the actual markdown files in
`03-governance/`, and returns the top matching sections with the source
file, heading, and an excerpt, plus a fixed disclaimer that this is a
citation finder, not legal advice. It never answers from a model's memory
of what governance policy "probably" says; it only returns things that are
actually written down in the corpus.

## Why lexical search instead of embeddings

This corpus is small (a dozen or so markdown files) and changes by hand-edit,
not by bulk ingestion. A keyword-overlap search is exact, inspectable, and
has zero infrastructure (no vector DB, no embedding model, no index to keep
in sync). If the corpus grows past a few hundred documents, revisit this,
but don't reach for embeddings before you've outgrown what a simple search
can do, that's added complexity with a real maintenance cost.

## The one invariant that matters

If nothing in the corpus actually addresses the question, the tool returns
an empty result set (`no_match: true`), never a fabricated-sounding answer.
That's tested (`test_no_fabrication_on_irrelevant_question`). If you're
extending this and tempted to add "if no match, summarize what we might
guess," don't, that's the exact failure mode this tool exists to avoid.

## How to keep it accurate as governance evolves

This tool reads `03-governance/*.md` directly, live, every time it's
called. There is no separate copy to keep in sync, no cache to invalidate.
Edit a governance doc, the next question against it reflects the edit
immediately. That's a deliberate design choice: a policy tool that can
drift out of sync with the actual policy is worse than no tool.

## If something looks wrong

- **It's not finding an obviously relevant section**: check whether that
  section uses different wording than the question. This is keyword
  overlap, not semantic search, "comp" and "compensation" are different
  tokens to it. Either rephrase the question or, if it's a common phrasing
  gap, that's a signal the doc itself could use clearer headings.
- **You want it to also search 01-use-cases or the prompt library**: change
  `GOVERNANCE_DIRNAME` to a list and extend `load_governance_docs`, that's
  a small, safe change. Think first about whether mixing governance
  citations with prompt-library content in one search makes the results
  more or less trustworthy, that's a judgment call worth making
  deliberately, not defaulting into.

## Where this plugs into the rest of the playbook

This tool's disclaimer language mirrors the "not legal advice" framing
already used throughout `03-governance/ai-use-policy.md` and
`03-governance/quick-reference-checklist.md`. Keep that consistent if you
edit either.
