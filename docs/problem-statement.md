# What this experiment is about

## The observation

Type Ia supernovae at redshift z ~ 0.5 are dimmer than a decelerating,
matter-dominated FLRW universe predicts. Fitted within FLRW, the data
require a component with negative pressure making up roughly 70% of the
energy budget. That component is called dark energy, and in the standard
model it is a cosmological constant.

The inference has a step in it that is easy to miss: the data constrain
the *distance-redshift relation*. Converting that into "the expansion is
accelerating" requires assuming the geometry is FLRW, that is,
homogeneous and isotropic, at the scales being probed.

## The timescape alternative

The late universe is not homogeneous. Roughly 60% of the present volume
is in voids of tens of megaparsecs; galaxies sit in walls and filaments
threading between them. General relativity is nonlinear, so the average
of the true inhomogeneous geometry is not the FLRW solution with the
average density. This is the **averaging problem**, and it is prior to
any particular alternative model.

Timescape (Wiltshire) proposes that once inhomogeneity is averaged
correctly, the apparent acceleration is a *calibration artifact* rather
than a dynamical effect. Its distinctive ingredient is a claimed
difference in clock rates: quasilocal gravitational energy gradients make
clocks in voids run faster than clocks in bound structures, cumulatively
by tens of percent over cosmic history. Observers live in walls. Using
wall time to interpret light that has traversed mostly void volume
produces an apparent acceleration with no dark energy present.

The model is not merely interpretive. It makes a different
distance-redshift relation, different CMB and BAO calibrations, and a
specific prediction about variance in the local Hubble flow. It can be
wrong, which is why it is worth auditing.

## Why an LLM experiment

The repository description sets the target: whether language-model agents
can work out how to explain dark energy via timescape and its extensions.

That is a harder brief than it sounds, and the failure mode is specific.
Timescape is a chain of inferences. Some links are standard general
relativity, some are a particular averaging scheme, some are a contested
interpretation of quasilocal energy, and some are parameter fits. An
agent that produces a fluent summary treating all of those as equally
secure has produced nothing. The thing worth extracting is *which link
carries the weight and how well supported it is*.

So the first runs do not extend the model. They audit it.

## The audit targets

**A1. The derivation chain.** From "the universe is inhomogeneous" to
"the apparent acceleration is an artifact", what are the discrete steps?
For each: is it a theorem, a modelling choice, a physical postulate, or a
fit? See `derivation-chain.md`.

**A2. Evidential status.** For each empirical claim, what data, what
analysis, what systematics, what model-comparison statistic, and what did
the critics say in reply. See `claim-ledger.md`.

**A3. Live objections.** The backreaction-magnitude dispute is unresolved
in the literature, not settled in either direction. The same goes for
whether the clock effect is physical or a gauge artifact. These get
reported as open with both sides stated. See `objections.md`.

**A4. Rivals.** Timescape is one of several inhomogeneous-cosmology
responses and competes with modified gravity and with plain LCDM. An
audit that does not say what else could produce the same signature is
incomplete. See `rival-approaches.md`.

## The extension question, deferred

Extensions are the stated long-run goal and are gated behind the audit.
A proposed extension that is not anchored to a specific identified
weakness in the chain is speculation with equations attached. See
`../protocol/EXTENSION-RULES.md`.

## Non-goals

- Advocating for timescape, or against it.
- Producing a verdict on whether dark energy exists.
- Treating the number of citations a position has as evidence for it.
- Any output that reads as settled where the literature is not.
