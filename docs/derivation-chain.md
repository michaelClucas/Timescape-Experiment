# The derivation chain (seed, v0)

Timescape is a sequence of steps from an uncontroversial premise to a
strong conclusion. The audit's job is to find which steps carry the weight.

Every step below is tagged with what *kind* of claim it is. The seed tags
are a guess and the audit is expected to correct them.

- `THEOREM` follows from general relativity with no extra assumption.
- `SCHEME` a modelling choice: a specific averaging procedure, a specific
  decomposition. Other defensible choices exist.
- `POSTULATE` a physical assumption added to the theory.
- `FIT` a parameter determined from data rather than derived.
- `INTERPRETATION` a statement about what an existing formal result means.

---

### D1. The late universe is inhomogeneous at scales relevant to observation
`THEOREM` / observational.
Voids of order tens of Mpc occupy the majority of present volume; galaxies
occupy walls and filaments. Not in dispute. What *is* in dispute is the
scale of statistical homogeneity and whether it is reached within the
survey volume.

Audit: what is the current best estimate of the homogeneity scale, and
does timescape require it to be larger than the standard value?

### D2. Averaging an inhomogeneous solution does not commute with the field equations
`THEOREM`.
The Einstein tensor of an averaged metric is not the average of the
Einstein tensors. Known as the fitting problem (Ellis) and the averaging
problem. Not in dispute as a formal statement.

Audit: state it precisely. The dispute is entirely about magnitude, not
existence, and conflating the two is the most common error in both
directions.

### D3. The Buchert formalism gives averaged evolution equations with backreaction terms
`SCHEME`.
Scalar averaging over a spatial domain yields Friedmann-like equations
with an extra kinematical backreaction term Q built from variance of the
expansion rate and shear.

Audit: this is a *scheme*, with known limitations (foliation dependence,
restriction to scalars, domain dependence). Record what it assumes and
what alternatives exist. Also record what Q's sign and magnitude are
*allowed* to be, separately from what timescape needs them to be.

### D4. Backreaction can be large enough to matter
`INTERPRETATION` / disputed.
This is the first genuinely contested link, and it is contested in the
formal literature, not just in interpretation. Green and Wald developed a
framework arguing that backreaction from small-scale inhomogeneity cannot
mimic dark energy; Buchert and a large group of co-authors published a
direct rebuttal arguing the framework's assumptions exclude the relevant
regime by construction.

Audit: this is the highest-priority item in the run. State both positions
from primary sources, state precisely what each assumes, and say what the
disagreement actually turns on. Do not report a winner. If the dispute is
unresolved in the literature, the output says it is unresolved.

### D5. A two-phase (wall / void) decomposition is the right coarse-graining
`SCHEME`.
Timescape splits the domain into a wall fraction and a void fraction with
volume fraction f_v, each with its own expansion history.

Audit: what fixes the two-phase split rather than a continuum of
densities? Is the result sensitive to that choice?

### D6. Clocks in voids and clocks in walls run at measurably different rates
`POSTULATE` / the distinctive claim.
Wiltshire argues that quasilocal gravitational energy gradients produce a
cumulative difference in clock rates between void centres and bound
structures, of order tens of percent today. This is supported by a
proposed "Cosmological Equivalence Principle" and a particular treatment
of quasilocal energy.

Audit, in priority order:
1. What exactly is the Cosmological Equivalence Principle, in Wiltshire's
   own statement of it, and is it an additional postulate or claimed to
   follow from standard GR?
2. What is the quantitative claim, with its current best value and its
   uncertainty?
3. Is the effect gauge-invariant? The strongest form of the objection is
   that a clock-rate difference between regions is a statement about
   calibration conventions rather than about physics. State the objection
   as its proponents state it and state the reply.
4. Is there a laboratory or solar-system regime where the principle makes
   a check-able statement, or is it only defined cosmologically?

This step is where the model lives or dies. D4 can be granted in full and
timescape still fails if D6 does not hold.

### D7. Wall observers inferring FLRW from their own clocks see apparent acceleration
`INTERPRETATION` + `SCHEME`.
The "dressed" versus "bare" parameter distinction: dressed parameters are
what a wall observer infers under the (false, in this model) assumption of
FLRW. Apparent acceleration appears in dressed parameters with no
acceleration in bare ones.

Audit: is the apparent acceleration a *derived consequence* of D1-D6 with
the observed f_v, or does it require f_v to be fitted to the supernova
data it then explains? The answer determines whether timescape predicts
or postdicts the acceleration, and the two have very different
evidential weight.

### D8. The model fits the data at least as well as LCDM
`FIT` / empirical.
Supernova distance-redshift, CMB acoustic peaks, BAO, and local Hubble
flow variance.

Audit: this is `claim-ledger.md`. Per dataset: which analysis, how many
free parameters on each side, what statistic was used for comparison,
what priors, what systematics, and what the published responses say. A
Bayesian preference computed with different parameter counts on the two
models is not a like-for-like comparison and must be reported with the
counts.

---

## How to use this chain

The deliverable is not a verdict on the chain. It is a table saying, for
each link: what kind of claim it is, what supports it, what the strongest
objection is, and how much of the conclusion collapses if it fails.

The last column is the one that matters. A chain where one `POSTULATE`
carries everything is a different research situation from one where the
weight is spread across six `THEOREM` steps, and the published discussion
rarely makes clear which this is.

## Seed warning

The step decomposition above is a hand-written guess. The real derivation
may have more steps, fewer steps, or a different order, and the `kind`
tags are likely wrong in places. Correcting the chain is a legitimate and
valuable output of the audit. Attributions here are `[LEAD]` only; see
`../protocol/EVIDENCE-RULES.md`.
