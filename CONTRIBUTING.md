# Contributing

## Most useful contributions

1. **Corrections to `docs/derivation-chain.md`.** It was written by hand
   without retrieval. A wrong `kind` tag is the highest-value correction
   in the repository, because the whole audit hangs on telling theorems
   from postulates.
2. **Corrections to `docs/objections.md`.** If an objection is stated in a
   weaker form than its author actually made it, that is a bug. Send the
   stronger version with the source.
3. **Verified citations** for anything in `sources/bibliography.md`. Add
   the DOI or arXiv id and move the entry to Verified.
4. **Ledger entries.** A single well-sourced `docs/claim-ledger.md` entry
   with C4, C5, and C6 filled from a paper's method section is worth more
   than a broad survey.
5. **Replication runs.** Run an existing prompt on a different model and
   commit the result. Highest value per effort, and needs no domain
   expertise.

## Rules

- **Never edit a committed `OUTPUT.md` or `OUTPUT.json`.** Runs are
  append-only. Corrections go in `REVIEW.md` or a later run.
- **Never edit a prompt a run has used.** Fork it to a new number.
- **Follow `protocol/EVIDENCE-RULES.md`** in prose contributions too. Tag
  claims, cite primary sources, report numbers with their parameter
  counts.
- **No extension proposals** until the gate in
  `protocol/EXTENSION-RULES.md` opens, and then only with E1-E5 filled.
  Proposals arriving before that are closed without review, which is not a
  comment on their quality.
- **One concern per PR.**

## On advocacy

This repository is not a timescape advocacy project and not a debunking
project. PRs that argue for a verdict on whether timescape is correct will
be closed. PRs that sharpen an objection, or that strengthen a reply to
one, are both welcome, including from people who think the model is
obviously right or obviously wrong.

## Submitting a run

Include `META.yaml` with the exact model id and the git sha of the prompt
as used, both paths where a run used an overlay. A run whose prompt cannot
be reconstructed from the repository is not a data point and will be
closed.

Run the validator and record its result in your `REVIEW.md`:

    python protocol/validate.py runs/<run>/OUTPUT.json

A deliberate violation is acceptable when the contract gives you no honest
way to comply; say so in `REVIEW.md` and leave it visible. An undeclared
one will be found, because the check is mechanical. If you judge a rule
wrong rather than your run, say that instead and argue it.

For an adversary run, stage the permitted inputs in their own directory and
give the agent no repository checkout. A withholding that depends on the
agent choosing not to read a file it holds is not a withholding. Record
what was staged in an `INPUTS.md` beside the run.

Record cost in `META.yaml` notes. Cost per usable finding is part of what
the method experiment measures.

## Disagreement

Open an issue, not a PR, for disputes about the derivation chain, the
ledger fields, or the extension gate. Those shape every future run.
