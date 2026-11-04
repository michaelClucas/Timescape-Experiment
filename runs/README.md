# Runs

One directory per agent run. Append-only: `OUTPUT.md` and `OUTPUT.json`
are never edited after they land. Corrections live in `REVIEW.md` or a
later run.

Naming: `<NN>-<slug>-<YYYY-MM-DD>/`, with `-m2`, `-m3` suffixes for
replications of the same prompt on different models, and `-control` for a
seed-withheld control.

Example: `01-audit-derivation-chain-2026-11-04-m2/`

## META.yaml template

```yaml
run: 01-audit-derivation-chain
role: auditor
model: ""              # exact model id, not a family name
prompt_path: prompts/01-audit-derivation-chain.md
prompt_commit: ""      # git sha of the prompt as used
seed_docs_provided:
  - docs/problem-statement.md
  - docs/derivation-chain.md
  - docs/claim-ledger.md
  - docs/objections.md
  - docs/rival-approaches.md
  - protocol/EVIDENCE-RULES.md
  - protocol/output-schema.md
tools_available: []    # e.g. web_search, arxiv, none
retrieval_used: null   # true | false | unknown
papers_retrieved: null # count actually fetched, not cited
context_clean: null    # false if the agent inherited context about this
                       # project from elsewhere; see METHOD.md controls
started: ""
finished: ""
token_cost: null
operator: ""
notes: ""
```

`prompt_commit` matters. A run whose prompt cannot be reconstructed from
the repository is not a data point.

`papers_retrieved` is worth filling honestly. A run citing forty sources
having fetched four is the failure this repository is built to catch, and
the two numbers side by side make it visible without reading the output.
