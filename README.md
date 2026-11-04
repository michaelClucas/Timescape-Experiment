# Timescape Experiment

A research experiment testing whether LLM agents can work out how to
explain dark energy via the timescape model, and extend it.

Supernovae at intermediate redshift are dimmer than a decelerating FLRW
universe predicts. Read through a homogeneous model, that means dark
energy. Timescape proposes that the late universe is inhomogeneous enough
that the homogeneous reading is wrong, and that the apparent acceleration
is a calibration artifact arising from a difference in clock rates between
voids and the bound structures observers live in.

The model might be right. The point of this repository is that you cannot
tell from the summaries, because timescape is a chain of inferences in
which some links are theorems of general relativity, some are modelling
choices, one is a contested physical postulate, and some are parameter
fits, and the presentations rarely separate them.

So the first runs do not extend the model. They audit it.

## Status

Scaffolding only. No runs yet. Extensions are locked.

## Layout

| Path | What it is |
| --- | --- |
| `docs/problem-statement.md` | The observation, the proposal, and what the audit targets |
| `docs/derivation-chain.md` | Steps D1-D8 from inhomogeneity to apparent acceleration, each tagged by kind |
| `docs/claim-ledger.md` | The scaffold: fields C1-C10 for every empirical claim |
| `docs/objections.md` | Live objections O1-O6, paired with the step each attacks |
| `docs/rival-approaches.md` | What else could produce the same signature |
| `protocol/METHOD.md` | Run structure, controls, review rubric |
| `protocol/EVIDENCE-RULES.md` | Citation, confidence, and numeric-reporting rules |
| `protocol/EXTENSION-RULES.md` | Gate on extension runs, and what a proposal must contain |
| `protocol/output-schema.md` | Structured output contract |
| `prompts/` | Committed, versioned agent prompts |
| `runs/` | One append-only directory per agent run |
| `sources/bibliography.md` | Unverified seed bibliography and fabrication probe |

## How a run works

1. Pick a prompt from `prompts/`. Prepend `prompts/00-system-researcher.md`.
2. Give the agent the seed docs the prompt lists, and nothing else.
3. Create `runs/<NN>-<slug>-<date>/`, fill `META.yaml`, save the output
   verbatim as `OUTPUT.md` and `OUTPUT.json`.
4. Write `REVIEW.md` against the rubric in `protocol/METHOD.md`.
5. Never edit a committed output.

Run 01 should be replicated on at least two models, plus one seed-withheld
control, before anything is built on it.

## The two things being measured

The research target is where the weight sits in the derivation chain. The
method target is whether an agent can tell a theorem from a postulate from
a fit in a literature that blurs them. The second is the sharper test:
fluent summarisation of timescape is easy, and the summaries are nearly
useless.

## Design commitments

- **Extensions are gated.** Proposing modifications to a cosmological
  model is the easiest thing for a language model to do badly, because the
  output is fluent, carries equations, and is unfalsifiable at a glance.
  Nothing is proposed until the audit says which link is weak. See
  `protocol/EXTENSION-RULES.md`.
- **Live disputes stay live.** The backreaction-magnitude dispute and the
  gauge status of the clock effect are open. Reporting timescape as
  refuted is as much a failure as reporting it as established.
- **Numbers or nothing.** No comparison statistic without the dataset,
  cuts, priors, and free-parameter counts on both sides.
- **Independent confirmation means independent.** A result confirmed only
  within the proposing group is `contested`, whatever its quality.
- **Append-only runs.** An edited output is not a data point.
- **Negative results get committed.** An extension that fails is more
  useful here than one quietly dropped.

## Related

Companion experiment on the cosmological-scale observer problem:
[The-Observer-Problem](https://github.com/michaelClucas/The-Observer-Problem).
Same protocol design, different target.

## Contributing

See `CONTRIBUTING.md`. Corrections to `docs/derivation-chain.md`,
especially wrong `kind` tags, are the most useful thing to send.
