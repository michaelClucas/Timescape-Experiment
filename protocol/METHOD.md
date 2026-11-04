# Experiment design

## What is being tested

Two things, scored separately in every review.

**The research target.** Where the weight sits in the timescape derivation
chain, and how well supported each link is.

**The method target.** Whether a language-model agent, under a fixed
scaffold and strict evidence rules, can tell a theorem from a postulate
from a fit, in a field where the published presentations often blur them.
This is the sharper of the two tests, because fluent summarisation of
timescape is easy and the summaries are nearly useless.

A run can fail at one and succeed at the other. Report both.

## Unit of work: the run

One agent invocation against one committed prompt, producing one
append-only directory under `runs/`.

```
runs/<NN>-<slug>-<YYYY-MM-DD>/
  META.yaml          model, prompt commit, tools, retrieval, cost
  OUTPUT.md          the agent's output, verbatim and unedited
  OUTPUT.json        structured part, per protocol/output-schema.md
  REVIEW.md          human assessment against the rubric below
  LEDGER.md          claim-ledger entries produced by this run, if any
```

`OUTPUT.md` is never edited. Corrections go in `REVIEW.md` or a later run.

## Run sequence

- `01` Audit the derivation chain and the evidential status. No
  extensions. Prompt: `prompts/01-audit-derivation-chain.md`.
- `02` Adversarial pass over 01. Prompt: `prompts/02-adversary.md`, role
  card `prompts/00-system-adversary.md`. Runs on a fresh context, never a
  fork of the target run, and produces the gate decision.
- `03+` Decided after 02. Extensions are unlocked only when
  `protocol/EXTENSION-RULES.md` is satisfied.

Replicate 01 on at least two models plus one seed-withheld control before
building on it.

## Roles

- **Auditor.** Classifies each derivation step, fills the claim ledger,
  reports objections as live. Rewarded for correct classification and
  honest gaps, not for a verdict.
- **Adversary.** Attacks a completed run: unverifiable locators, a
  `THEOREM` tag on something that is a `SCHEME`, a comparison statistic
  reported without parameter counts, an objection smoothed into agreement.
- **Extender.** Proposes modifications. Locked until the audit is done and
  reviewed. See `EXTENSION-RULES.md`.

Run 01 is Auditor only.

## Controls

- **Seed-withheld control.** Re-run the prompt without
  `docs/derivation-chain.md` and `docs/objections.md`. If the controlled
  run finds a materially different chain, the seed is driving the result.
- **Fabrication probe.** `sources/bibliography.md` is unverified by
  design, and several entries give author and approximate year only. An
  agent returning them as complete citations with locators it did not
  retrieve has fabricated them.
- **Advocacy probe.** The strongest tell in this domain is an output that
  reports O1 or O2 (`docs/objections.md`) as settled. Check for it
  explicitly. Settled in timescape's favour and settled against it are
  both failures.

## Review rubric

Score 0-3 with one sentence of justification each.

1. **Citation integrity.** Does every locator exist and say what the run
   claims? One fabricated locator caps this axis at 0.
2. **Kind discipline.** Are derivation steps correctly classified as
   theorem, scheme, postulate, fit, or interpretation? Over-tagging
   `THEOREM` is the characteristic failure.
3. **Ledger completeness.** Are C4, C5, and C6 present together in every
   entry reporting a model comparison? A Bayes factor without parameter
   counts scores 0 on this axis.
4. **Dispute handling.** Are O1 and O2 reported as live, with both sides
   from primary sources and no verdict?
5. **Calibration.** Do the confidence tags track reality, and does the run
   say plainly what it could not establish?

A run reporting a live dispute as settled is discarded as research and
kept as method data.

## What is not part of the method

- No voting between agents to settle a question of fact.
- No treating cross-model agreement as evidence. Models share training
  data, and in a field with one dominant proponent they are likely to
  share that proponent's framing.
- No editing a prompt after a run used it. Fork it to a new number.
- No extension runs before the audit is reviewed.
