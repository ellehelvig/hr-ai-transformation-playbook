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

That invariant used to be weaker than it sounded. `no_match` only fired when a
question shared literally no words with the corpus, so "can I bring my dog to
the office review?" came back with three confident citations, top-ranked being
the README's US federal enforcement section, matched on the word "bring". A
citation finder that cites on a coincidence is worse than one that says it found
nothing, because the agent reading the result cannot tell the two apart.

Two gates now have to clear before anything is returned: a BM25 relevance score
and an IDF-weighted share of the question's terms. Both numbers are measured
against this corpus, with the measurements written into the constants at the top
of `tool.py`. If you change the corpus size substantially, re-measure them; IDF
is a corpus statistic and the thresholds do not port.

## Before you point this at your company wiki

The tool returns up to 600 characters of corpus text verbatim into the calling
agent's context. That is fine here, where the corpus is version-controlled
markdown that goes through pull request.

It stops being fine the moment the corpus is something its own readers can edit:
a policy wiki, a shared drive, an open Confluence space. Any employee who can
edit a page can then write instructions into it and have them delivered straight
into an HR agent's context. That is prompt injection with a direct payoff, since
the agent on the other end can often reach comp data and employee records.

There is no filter for this, and adding one would be theater; you cannot
reliably distinguish instructions from prose. The control is the trust boundary:
keep the corpus reviewed, and keep the agent's other tool permissions narrow
enough that an injected instruction has nothing worth doing. Every response
carries an `excerpt_provenance` field saying this, so the consuming agent knows
what it is holding.

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
