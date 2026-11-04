# Extension rules

The repository's stated goal includes extensions to the timescape model.
This document gates them. Extension runs are locked until Run 01 is
complete and reviewed, and Run 02 has attacked it.

The reason for the gate is specific. Proposing modifications to a
cosmological model is the single easiest thing for a language model to do
badly: the output is fluent, carries equations, cites real concepts, and
is unfalsifiable at a glance. Extensions produced before the audit cannot
be distinguished from that failure mode, and committing them to the
repository would poison every later run that reads it.

## Entry condition

An extension run may start only when all hold:

1. Run 01 exists, is reviewed, and scores at least 2 on every rubric axis
   in `METHOD.md`.
2. Run 02 (adversarial) exists and its findings are addressed.
3. The extension targets a **specific identified weakness** named in the
   Run 01 or Run 02 output, cited by its step id or claim id.

An extension not anchored to a named weakness is rejected without review.

## What a proposed extension must come with

All five. A proposal missing any of them is not evaluated.

**E1. The target.** Which derivation step (`D1`-`D8`) or ledger claim it
addresses, and what is wrong with the current treatment, citing the run
that established it.

**E2. The modification.** Stated precisely enough to be wrong. Which
equation changes, which assumption is dropped or added, what new free
parameters are introduced and how many.

**E3. What it preserves.** Which of the existing successes survive. An
extension that fixes the clock-effect objection and breaks the CMB fit has
not helped, and the proposal must say which it is or say that this was
not checked.

**E4. A discriminating prediction.** At least one observable where the
extension differs from both base timescape and LCDM, with a magnitude and
the precision needed to see it. "Could in principle be tested" is not a
prediction.

**E5. A falsifier.** The specific measurement that would kill it, and
whether existing data already does. If the extension cannot be killed by
any foreseeable measurement, say so, and it is logged as a formal
exploration rather than a physical proposal. That is a legitimate category
and should not be disguised as the other one.

## Honesty requirements

- An extension that reproduces an existing proposal in the literature is
  not an extension. Search before proposing, and say what you searched.
- Dimensional consistency and limiting cases are checked and the check is
  shown. An equation that does not reduce correctly in a known limit is
  reported as broken, not presented with the limit unmentioned.
- If the agent cannot carry out a derivation it proposes, it says so and
  states what would need to be computed. An asserted result with no
  derivation is tagged `[INFERENCE]` at best.
- Negative results are committed. An extension that was tried and fails
  on E3 or E4 is more useful to this repository than one that was quietly
  dropped, and the runs directory is append-only partly to make that cost
  nothing.

## Review

Extensions are reviewed against E1-E5 before any assessment of whether
they are interesting. A proposal that is interesting and fails E4 is
still rejected.
