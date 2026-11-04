# Lean: the trigger, not a programme

There is no Lean infrastructure here, deliberately, and this file is the
convention for when to create some.

## Why nothing is set up

mathlib has limited differential geometry and **no general relativity**.
Formalising the Buchert averaging derivations would be a multi-year project
in its own right, not a work package, and it would dominate this programme
while answering none of its questions. The averaging and light-propagation
steps are therefore **not Lean targets**, and this plan does not pretend
otherwise.

Setting up a toolchain for proofs that have not been identified yet is
worse than not setting one up: it creates an obligation to use it.

## The trigger

A claim goes to Lean when it is **proof-shaped**:

1. It has **explicit hypotheses** that can be stated without reference to a
   measurement, a fitted parameter, or a modelling choice.
2. Its conclusion **follows by proof rather than by measurement**. If
   replacing a number changes whether it holds, it is not proof-shaped.
3. It is **load-bearing**: some result in this repository depends on it, so
   a formal check buys something.

All three, not two. Most claims in this repository fail (2), because the
chain is held up by schemes, postulates and fits rather than theorems: of
the thirteen steps Run 01 identified, only `T2` and `T4` are theorems, and
`T4` only conditionally.

## What would actually qualify

Candidates, none of which has been established to exist yet:

- The Buchert integrability condition as an identity, given the averaged
  equations as hypotheses. `T2` is an exact identity and the integrability
  condition is a corollary, so this is the closest thing to a real target.
- Measure-theoretic or combinatorial claims about counting, regularisation
  or limits, if any arise.
- Inequality arguments: that a bound follows from stated assumptions, for
  instance the claim that volume acceleration is bounded above by the
  variance of the expansion rate.
- Consistency: that a closure choice is or is not compatible with the
  integrability condition. Maple job 001 computes a residual for this
  numerically; a proof that no closure of a given family can satisfy it
  would be proof-shaped and strong.

## When the trigger fires

Create `lean/` as a Lake project at that point, with:

```
lean/
  lakefile.toml
  lean-toolchain          pinned, recorded in the run that needed it
  TimescapeExperiment/
    NNN_<slug>.lean       one file per formalised claim
    NNN_<slug>.md         what is proved, its hypotheses, and which run or
                          step depends on it
```

The `.md` states, in prose, **what the hypotheses mean physically** and
what the theorem does *not* say. A formalised theorem whose hypotheses
nobody can interpret is a liability: it looks like certainty and carries
none.

Record the toolchain version and the mathlib commit in the consuming run's
`META.yaml`, for the same reason `prompt_commit` is recorded.

## What Lean does not buy here

A Lean proof says a conclusion follows from its hypotheses. It says nothing
about whether the hypotheses hold of the universe. In a programme whose
weight sits on eight non-theorem steps, that is a narrow kind of
reassurance, and it must not be reported as though it were broader.
