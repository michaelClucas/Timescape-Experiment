# Research plan: timescape and the dark energy measurements

**The question.** Does timescape in fact provide a rigorous, corroborated
explanation of the dark energy measurements? If not currently, can it be
extended to do so, and how?

**This plan assumes nothing about the answer.** Every work package below
states what result would count against the model and what would count for
it, before the work starts. A plan whose packages only make sense if the
model survives is biased, and so is one that only makes sense if it dies.
Where a package has an outcome I expect, I say which and why, so that a
surprise is visible as a surprise rather than absorbed.

Starting point: `runs/01-audit-derivation-chain-2026-11-04/`. Its findings
are **leads to test, not foundations to build on**. Run 02, the adversarial
pass, has not run; the audit's own self-review scores it 12/15 and names
five things it would attack first.

---

## 1. The question in decidable form

"Rigorous" and "corroborated" are separate questions with separate answers,
and collapsing them is the main way this subject gets discussed badly.

### 1.1 What Run 01 found, which this plan tests rather than assumes

The audit renumbered the derivation to thirteen steps `T1`-`T13` and found
the weight spread across **eight non-theorem steps, each individually
sufficient to break the conclusion, none well established**: `T5` (a closure
is required and is not derivable), `T6` (the two-phase ansatz), `T8` (the
fitted bare budget), `T9` (the Cosmological Equivalence Principle), `T10`
(the clock rate is physical, 35-38%), `T11` (the dressed/bare map), `T12`
(light propagation), `T13` (the fit). Only `T2` and `T4` are theorems, and
`T4` only conditionally on `T5`.

Three corrections in that audit reshape the question, and all three are
checkable:

1. **Backreaction is not timescape's mechanism.** In the fitted solution
   `Omega_Q_bar0 = -0.0293`, **negative**, with `|Omega_Q_bar| <= 0.042`
   always and no volume acceleration. The bare budget is dominated by
   average negative spatial curvature, `Omega_k_bar0 = 0.862`. So the
   Green-Wald dispute, which the seed treated as central, is about a
   quantity this model does not lean on.
2. **A weight-3 step was missing entirely: light propagation (`T12`).**
   Getting a distance-redshift relation out of scalar-averaged quantities
   is a separate move that both Buchert and Wiltshire say in print is not
   yet justified. Every supernova, CMB and BAO comparison runs through it.
3. **The void fraction `f_v0` is fitted, not independently determined, in
   every analysis retrieved**, with values spanning `0.550` to `0.791` and
   a further range `0.72`-`0.95`, "a spread far exceeding the quoted
   uncertainties".

I have independently confirmed the arithmetic underlying (1).
`verify/tracker_relations.py` reproduces all eleven published tracker
values from the equations of arXiv:0709.0732, including
`Omega_k_bar(0.695) = 0.861211` against the published `0.862` and
`Omega_Q_bar(0.695) = -0.0291855` against `-0.0293`. That confirms the
transcription, not the physics.

### 1.2 The decidable claims

| # | Claim | Settled by | Package |
|---|---|---|---|
| D1 | Timescape and LCDM are distinguishable by a joint supernova + BAO fit, and one loses | reanalysis of Pantheon+ and DESI BAO | WP-1, WP-2 |
| D2 | The published supernova evidence is or is not circular through LCDM-calibrated light-curve standardisation | refit Pantheon+ with `alpha`, `beta`, `M_B` free simultaneously with cosmology | WP-2 |
| D3 | The clock-rate postulate improves the fit at matched parameter count, or does not | ablation on identical data | WP-3 |
| D4 | The independently measured void fraction agrees with the fitted `f_v0`, or does not | void catalogues against the fitted values | WP-4 |
| D5 | The average negative curvature the model requires is or is not consistent with the curvature real voids have | Maple 002 plus void profile data | WP-5 |
| D6 | The predictions survive refinement of the two-phase split, or are artefacts of it | Maple 001, then 003 if needed | WP-6 |
| D7 | The model does or does not reproduce `Omega_b h^2` and `S_8` | compute them; neither exists in the literature | WP-7 |
| D8 | The predicted 17-22% local Hubble-flow variance is or is not observed | reanalysis against that specific prediction | WP-8 |
| D9 | The dressed metric does or does not give correct luminosity distances | ray tracing against the averaged model | WP-9 |

### 1.3 What no foreseeable data can settle

Stated up front so no package pretends otherwise.

- **Whether the Cosmological Equivalence Principle is true** (`T9`). It is
  a postulate, and Wiltshire says so in his own words; the audit confirms
  he nowhere claims it follows from general relativity. Only its
  consequences are testable, so "is the CEP correct" is not on this plan.
  Its consequences are, via D5 and D9.
- **Whether the clock effect is physical or a calibration convention**
  (objection O2). This is decidable only by constructing a gauge-invariant
  observable that distinguishes them, which is theory, not measurement. It
  is WP-9's secondary target and may have no answer. Run 01 also could not
  establish that any published gauge critique exists, and flags that as an
  absence it did not run the search to confirm.
- **Redshift drift**, the cleanest discriminator in the discrimination
  table (`-7.2e-10` for timescape against `-9.3e-10` for flat LCDM over ten
  years at `z = 4`). It needs roughly a twenty-year Lyman-alpha baseline
  with ELTs. Real, and not on any plan written now.
- **Whether the exact two-scale solution is unique among admissible
  closures.** `T5` says a closure must be added; nothing says which. This
  is a mathematics question, not a data question, and it is the one place
  Lean might eventually bite (see `lean/README.md`).
- **Whether `T3` matters.** It has weight 0: the model does not use
  metric-averaging non-commutativity. Dropped from the plan entirely, which
  is what a weight-0 finding is for.

---

## 2. Work packages

Costs are in agent-runs and wall-clock days, not money. "Maple RT" is
round trips at roughly one per day.

### Phase 0 - cheap, potentially terminal, and the protocol's own debt

#### WP-0. Run 02, the adversarial pass over the audit
**Establishes:** whether Run 01's findings survive attack. **Everything
below depends on the audit, and the audit is unverified.**
**Depends on:** nothing. **Datasets:** none. **Maple RT:** 0.
**Cost:** 1 agent-run, ~1 day.

Per `protocol/METHOD.md` and `prompts/02-adversary-v2.md`, on a fresh
context with inputs enforced by staging. The audit's self-review names its
own five weakest points, including the `T4` `THEOREM` tag and the claim
that no published gauge critique of the clock effect exists.

**Counts against the audit:** any fabricated locator caps it at 0 on axis 1
and it is discarded as research. **Counts for it:** a clean locator sweep,
as happened in the sibling repository.

This is first because it is cheap and because the alternative is building
nine packages on an unverified foundation.

#### WP-1. Replicate the two results that may already have decided this
**Establishes:** whether timescape is already refuted by published data.
**Depends on:** nothing. **Maple RT:** 0. **Cost:** 1 agent-run, ~2 days.

Run 01's discrimination table flags two entries as **arguably already
decided against timescape**, and notes the second "is not usually stated":

- **Supernova + BAO joint fit.** One independent analysis
  (arXiv:2406.05048, Table 7) reports tension between the two for
  timescape where flat LCDM has none.
- **Dressed `H_0`.** Timescape gives `60.98`-`61.7` km/s/Mpc against local
  determinations of `70`-`73.3` at `+/- 0.9`.

Retrieve both, establish exactly what was fitted and with how many
parameters on each side, and state the significance. For `H_0`, establish
whether the comparison is like-for-like: the dressed `H_0` is a different
quantity from a distance-ladder `H_0`, and whether that difference is
legitimate or a rescue is the crux.

**Counts against:** both confirmed as like-for-like and significant. Then
the question changes from "is timescape right" to "why does it fit
supernovae alone", and WP-5, WP-6 and WP-9 are cancelled.
**Counts for:** the `H_0` comparison turns out not to be like-for-like and
the joint-fit tension rests on an LCDM-derived BAO scale, in which case D1
reopens and WP-2 becomes decisive.
**Expected:** I do not know, and that is why this is package one.

### Phase 1 - the circularity question and the two Maple jobs

#### WP-2. Refit Pantheon+ from light curves, standardisation free
**Establishes:** D2, and D1 for supernovae alone. The thing Run 01 could
not settle from published method sections.
**Depends on:** WP-1 not having cancelled the programme. **Maple RT:** 0.
**Cost:** 2 agent-runs, ~4 days, meaningful compute.

**Dataset:** Pantheon+ (Scolnic et al. 2022; Brout et al. 2022). ~1550 SNe
after standard cuts, with the full covariance. Tens of MB. **Tractable,
and this is where the circularity bites hardest.** Recorded per
`data/README.md`, with field 7 (derivation under an assumed cosmology) the
point of the exercise.

Fit flat LCDM, timescape, and a Buchert scaling solution to the same data
with `alpha`, `beta` and `M_B` **free simultaneously with the cosmology**,
not inherited. Report parameter counts on every model and the evidence with
`emcee` or `dynesty`. Repeat at the published redshift cuts (`z_min` of
`0.033` and `0.075`) and report the sensitivity, because the cut is a
modelling choice.

**Counts against:** timescape loses at matched parameter count with free
standardisation. Its headline evidence is then gone on its own terms.
**Counts for:** timescape wins or ties with standardisation free, **and**
the published results turn out to have inherited LCDM standardisation. That
would mean the model has been under-credited rather than over-credited, and
it is a real possibility nobody has checked.

#### WP-3. The ablation nobody has run
**Establishes:** D3. What the clock-effect postulate actually buys.
**Depends on:** WP-2's pipeline. **Maple RT:** 0.
**Cost:** 1 agent-run, ~1 day on top of WP-2.

Run 01 found a **clean negative**: no paper fits the same supernova dataset
with and without the clock-rate postulate and reports the difference. The
closest is Desgrange, Heinesen & Buchert (arXiv:1902.07915, Table 2), which
fits both to JLA at matched parameter count and finds AIC
indistinguishable, but does not frame it as an ablation. The audit flags
that the AIC **sign convention** in that table is unconfirmed and that its
cleanest result depends on it; confirm it as part of this package.

Fit with the clock effect on and off, same data, same cuts, same parameter
count, report the difference.

**Counts against:** no improvement. The distinctive postulate is then
unnecessary for the supernova fit, and Occam removes `T9`, `T10`, `T11`
while leaving Buchert averaging intact.
**Counts for:** a clear improvement, which would be the first clean
quantitative case for the clock effect in the literature.
**Expected:** no improvement on supernovae, because Run 01's Part 4 already
found none at matched parameter count. What the clock effect buys is
off-supernovae: not needing volume acceleration. WP-5 tests that.

#### WP-4. Is `f_v0` measuring what it claims?
**Establishes:** D4, and hardens or dissolves objection O4.
**Depends on:** nothing. **Maple RT:** 0. **Cost:** 1 agent-run, ~2 days.

**Datasets:** SDSS DR7 void catalogue (Pan et al., arXiv:1103.4156: 1054
voids, 62% volume fraction, median effective radius 17 h^-1 Mpc) and a
modern DESI or SDSS catalogue. Small.

Compare the independently measured void volume fraction against the fitted
`f_v0` values, accounting for the fact that the measured fraction is
**strongly algorithm-dependent** across `VoidFinder`, `V2/VIDE` and
`V2/REVOLVER` (Douglass et al., arXiv:2202.01226; the audit retrieved the
reference but not its tables, so the spread is a `[LEAD]` to settle here).

Also: the same Pan et al. paper reports that observed void fractions are
**reproduced by LCDM mocks**, so the void filling factor is not by itself
discriminating. Establish whether the model's required `f_v0` is
distinguishable from LCDM's at all.

**Counts against:** the measured fraction, with algorithm spread, excludes
the fitted values, or the fitted spread `0.550`-`0.791` is irreducible.
Then the one parameter generating the whole effect is a free fitting
parameter wearing the name of an observable.
**Counts for:** the measured fraction brackets the fitted values within the
algorithm spread, which would convert `f_v0` from a fit into a measurement
and materially strengthen the model.

#### WP-5. The curvature requirement: the gap nobody has measured
**Establishes:** D5. The highest-value package in the plan.
**Depends on:** retrieving the fitted `f_vi` (a one-hour literature task,
prerequisite for Maple 002's numeric items). **Maple RT:** 1, plus 1 more
if the first result needs the rigorous rederivation.
**Cost:** 2 agent-runs, ~4 days including Maple latency.

Run 01's Part 4 isolated precisely what the clock effect does: it
**relocates the required large quantity** from `Q`, where realistic
estimates fall short by about a factor of five (Rasanen, arXiv:0801.2692:
`|Omega_Q|` below 0.04 against `>~ 0.2` needed), to `<R>`, where **no
comparable realistic estimate exists at all**.

That is the deepest unexamined thing about this model. The
backreaction-only route has a published number showing it fails. The
curvature route has never had the equivalent number computed.

Two halves:
- **Requirement side.** `maple/jobs/002-curvature-budget-requirement/`,
  cleared to queue once `f_vi` is retrieved. Inverts
  `Omega_k_bar = -k_v f_vi^(2/3) f_v^(1/3)/(abar^2 Hbar^2)` against the
  tracker's `Omega_k_bar0 = 9 f_v0/(2+f_v0)^2` to get the required void
  curvature, curvature radius, and implied void density contrast, with
  sensitivity to the `f_v0` spread.
- **Observation side.** Confront that requirement with measured void
  density profiles. Observed voids reach `delta < -0.85` at their edges.

**Counts against:** the requirement sits outside what real voids provide,
for instance needing `delta_v` below `-0.99` or a curvature radius far
below 10 Mpc. That is the curvature analogue of Rasanen's factor of five
and would be the strongest quantitative result available against the model.
**Counts for:** the requirement lands inside observed void properties.
Nobody has shown this, and it would be the first direct corroboration of
the mechanism rather than of the fit.
**Expected:** genuinely unknown, which is what makes it worth doing first
among the physics packages.

#### WP-6. Does the two-phase split survive refinement?
**Establishes:** D6, and closes one of the three escapes Run 01 identified.
**Depends on:** nothing. **Maple RT:** 1, plus 1 if rigorous rederivation
is triggered. **Cost:** 1 agent-run, ~2 days.

`maple/jobs/001-two-phase-sensitivity/`, cleared to queue. `T6` carries
weight 3 and **no sensitivity analysis exists**; Run 01's open question 10
asks exactly this. The job generalises to two void curvature scales with
spread `s` and reports how the sign-change `f_v` and `q_min` move.

The job's own `JOB.md` names its weakest step: `q_two` patches the
published Eq. (26) rather than rederiving it. A **large** `s` dependence is
therefore **not reportable** and triggers job 003, a rederivation from
Eqs. (4)-(7) with `M` phases. Cheap version first, deliberately.

**Counts against:** `|q_min(s=0.5) - q_min(0)| > 0.02`, roughly half the
whole effect. The published numbers would then be artefacts of an
unjustified choice.
**Counts for:** a shift under `0.004`, inside the published fit uncertainty
on `q_0`. `T6` would not be load-bearing, which removes a weakness rather
than adding a strength, and that counts.
**Expected:** `d q_min/d s = 0` at `s = 0` by a relabelling symmetry, with
the leading dependence at `O(s^2)`. A nonzero first derivative is a setup
error, not a finding.

### Phase 2 - the missing predictions and the conceded step

#### WP-7. Compute what the model does not have
**Establishes:** D7. **Depends on:** WP-2. **Maple RT:** 0-1.
**Cost:** 2 agent-runs, ~3 days.

Run 01 failed to establish two things the model must have:
- **`Omega_b h^2`.** Needed for any CMB or BBN comparison. Run 01's open
  question 6.
- **`S_8` / `sigma_8`.** The discrimination table records the timescape
  value as **not computed**: "the prediction does not exist".

Compute both from the model, using camb 2.0.5 (verified working, `r_drag =
146.989` Mpc) for the standard-model side. `classy` is **unavailable on
this platform** and is not used.

**Counts against:** the model cannot produce an `S_8`, or produces one far
from measurement. A cosmology that cannot predict structure growth is not a
complete cosmology, whatever it does for supernovae.
**Counts for:** an `S_8` consistent with measurement, which would be a new
prediction confirmed rather than a refit.

#### WP-8. The Hubble-flow variance prediction
**Establishes:** D8. **Depends on:** nothing. **Maple RT:** 0.
**Cost:** 1 agent-run, ~2 days.

Timescape predicts 17-22% variance in the locally inferred expansion rate
(minimum `50.1 +/- 1.7`, maximum `75.2 (+2.0/-2.6)` km/s/Mpc). The audit
notes the measured uniformity at 70-100 Mpc is "consistent with LCDM over
20-150 Mpc", that **the two results are not stated as the same quantity**,
and that **the reanalysis against the 17-22% prediction has never been
done**. Run 01's open question 3.

Do it: construct the predicted quantity and the measured quantity as the
same statistic, then compare.

**Counts against:** the measured variance excludes 17-22%. Unlike the fit
comparisons, this is a prediction the model makes and LCDM does not, so a
failure here is costly to the model.
**Counts for:** confirmation at the predicted level, which would be the
strongest positive result available anywhere in this plan.

#### WP-9. Light propagation: the step conceded to be unjustified
**Establishes:** D9, and the secondary target of O2. **Depends on:** WP-5,
WP-6. **Maple RT:** 2-3. **Cost:** 3 agent-runs, ~2 weeks.

`T12` carries weight 3, the seed omitted it, and **both Buchert and
Wiltshire say in print it is not justified**: "The averaged equations cannot
predict luminosity distances unless one considers averages on the
lightcone"; identifying the volume-average Hubble parameter with the
observed one "remains to be rigorously justified". Rasanen's analysis
(arXiv:0812.2872 Eq. 38) shows what it takes, under six conditions
including vanishing vorticity and small uncorrelated shear.

Check whether the dressed metric reproduces distances obtained by
propagating light through an inhomogeneous model with the same void
statistics.

**Counts against:** a discrepancy at the level of the effect, about 5% in
distance modulus. Every fit in the literature would then be comparing the
wrong quantity to the data.
**Counts for:** agreement to well under the effect, which would discharge
the step its own authors flag as unjustified. That would be a substantial
contribution independent of whether timescape is right.

This package is last in Phase 2 because it is the most expensive and
because WP-1 or WP-5 may cancel it.

### Phase 3 - protocol debt

#### WP-10. Run 03: apply the corrections
**Establishes:** the seed docs matching what Run 01 and Run 02 found.
**Depends on:** WP-0. **Maple RT:** 0. **Cost:** 1 agent-run, ~1 day.

Run 01 filed **35 seed corrections** and disagreed with the seed's `kind`
tag on 8 of 13 steps. `docs/derivation-chain.md` and `docs/objections.md`
are still the hand-written originals, and runs are append-only, so the
corrections need a run of their own. Also migrate `C-SN-5`, which
`protocol/validate.py` flags for quoting `ln B = -3.46` with null parameter
counts and no uninterpretable marking.

**This plan does not edit those files.** That is this package's job.

---

## 3. Kill criteria

A plan with no kill criteria cannot be run honestly. These stop the
programme or a branch of it.

| # | Trigger | Effect |
|---|---|---|
| K1 | WP-1 confirms both the joint-fit tension and the `H_0` discrepancy as like-for-like and significant, **and** WP-2 finds the supernova fit is not circular | **Programme stops.** The model loses on data it was supposed to explain, with its headline evidence sound. Cancel WP-5, WP-6, WP-9. Write up as a negative result. |
| K2 | WP-2 finds timescape loses at matched parameter count with standardisation free | **Branch stops**: the supernova case is dead. The curvature mechanism (WP-5) may still be interesting and continues. |
| K3 | WP-5 finds the required void curvature outside what observed voids provide | **Programme stops.** The mechanism fails quantitatively, as the backreaction-only route already does. This is the cleanest available kill. |
| K4 | WP-6, in its rigorous form, finds `q_min` moving by more than half the effect under refinement | **All quantitative claims stop.** Every published number, including every fitted `f_v0`, is an artefact of `T6`. The qualitative claim survives and would need rebuilding from scratch. |
| K5 | WP-4 finds the measured void fraction excludes every fitted `f_v0` | **Branch stops**: `f_v0` is a fitting parameter, not an observable, and `T13`'s evidential weight collapses. |
| K6 | WP-7 finds the model cannot produce an `S_8` at all | **Narrows the claim**: timescape is at most a distance-redshift model, not a cosmology. Extensions are then about structure growth, not about dark energy. |
| K7 | WP-0 finds a fabricated locator in Run 01 | **Phase 1 pauses.** The audit is discarded as research, and every package's premises are re-established before continuing. |

Two kill criteria are deliberately **not** here:

- "Timescape is a minority position" is not a kill criterion.
- "The CEP is an extra postulate" is not a kill criterion. Extra postulates
  are how physics works; `Lambda` is one. What matters is whether its
  consequences hold, which is D5 and D9.

### What would make this programme a success

Also stated, so success is not defined only as survival:

- **A clean negative** is a success. "The curvature requirement is a factor
  of N outside observed voids" is a publishable result and closes a
  twenty-year question.
- **Discharging `T12`** is a success independent of timescape, because the
  step is unjustified for the whole Buchert programme.
- **The first ablation** of the clock-rate postulate is a success whichever
  way it falls, because nobody has run it.
- **Resolving the `f_v0` spread** is a success, because a parameter quoted
  with uncertainties far smaller than its scatter across datasets is a
  problem for anyone's model.

---

## 4. The extension path, gated

**The gate is shut.** `protocol/EXTENSION-RULES.md` requires Run 01
reviewed at 2 or better on every rubric axis, Run 02 existing with its
findings addressed, and the extension targeting a **named weakness** cited
by step or claim id. Run 01 self-scores 2/3/2/3/2, so it clears the first
condition on its own scores; Run 02 has not run. **No extension work is
planned before WP-0 completes**, and nothing in Phase 1 or 2 is extension
work.

The user's question explicitly includes extension, so it is planned
properly rather than omitted. Any proposal takes the E1-E5 shape:

- **E1 target.** The step or claim id, and what is wrong with it, citing the
  run that established it. On current evidence the live candidates are
  `T5` (the closure is not derivable), `T12` (light propagation,
  conceded), and `T6` (if WP-6 finds sensitivity). Not `T3`: weight 0.
- **E2 modification.** Which equation changes, which assumption is dropped
  or added, how many new free parameters.
- **E3 what it preserves.** Which existing successes survive. An extension
  fixing the clock-effect objection and breaking the CMB fit has not
  helped.
- **E4 a discriminating prediction.** An observable differing from **both**
  base timescape and LCDM, with a magnitude and the precision needed.
- **E5 a falsifier.** The measurement that would kill it, and whether
  existing data already does.

Plus the honesty requirements: search before proposing, show the limiting
cases, and commit negative results.

**Where extensions would most plausibly go**, as a sequencing note and not
a proposal: `T5` is the principled target, because a closure derived rather
than assumed would convert several `SCHEME` steps into consequences and is
the only route that reduces the eight-step weight spread rather than
redistributing it. `T12` is the most tractable. Neither is proposed here.

---

## 5. What this plan does not cover

- **Whether the CEP is true**, and whether the clock effect is physical
  rather than conventional. Not decidable by data; see 1.3. WP-9 touches
  the second as a secondary target and may fail.
- **Redshift drift.** Decades away.
- **The Green-Wald dispute.** Deliberately dropped as a central concern,
  because Run 01 found timescape does not lean on large backreaction. It
  returns only if WP-0 overturns that finding. This is the plan's biggest
  departure from the seed framing and the thing to check first if the plan
  looks wrong.
- **`T3`.** Weight 0.
- **Galactic dynamics and the MOND-scale coincidence.** The implied
  `alpha_0 = 8.6e-11` m/s^2 sits close to the MOND scale, and Wiltshire
  says it "may be purely coincidental" and that no quantitative comparison
  is possible until finite infinity is modelled directly. Interesting, not
  dark energy, out of scope. Galoppo, Re & Wiltshire (arXiv:2408.00358) is
  the thread.
- **CMB from scratch.** Planck likelihoods are large and slow, and
  timescape has no `Omega_b h^2` established, so a full CMB reanalysis
  cannot be set up yet. WP-7 does the prerequisite; a CMB package comes
  after, or not at all. Listing it now as a work package would be pretending
  effort is free.
- **Lean formalisation.** No targets identified. See `lean/README.md`.
- **Editing the seed docs.** WP-10's job.
- **Anything about the observer problem.** The sibling repository.

---

## 6. Conventions, and what must match the sibling repository

Flagged for the overseer rather than settled unilaterally. `maple/` was
specified to me; the rest I chose and they should be aligned or renamed:

| Convention | Choice here |
|---|---|
| Write-ups | `explain/NNN-<slug>.md`, rules in `explain/README.md` |
| Lean | `lean/README.md` holds the trigger; no project until it fires |
| Dataset provenance | `data/NNN-<dataset>/` with `SOURCE.md`, `fetch.sh`, `MANIFEST.sha256`, `cuts.md` |
| Verified environment | `env/requirements.txt`, pinned to versions actually installed and run |
| Local verification | `verify/<topic>.py`, runnable, exit non-zero on failure |
| Work package ids | `WP-n`, numbered by phase |

### Verified tooling, recorded because a plan on untested tooling is worthless

Installed into a clean venv on **Python 3.14.7** and imported:
numpy 2.5.4, scipy 1.18.1, matplotlib 3.11.2, pandas 3.1.1, astropy 8.0.2,
sympy 1.14.0, emcee 3.1.6, corner 2.3.0, getdist 1.7.7, dynesty 3.1.0,
iminuit 2.33.0, camb 2.0.5, cobaya 3.6.2.

camb was **run**, not merely imported: `r_drag = 146.989` Mpc,
`theta_star = 1.04465`.

**`classy` is unavailable.** pip reports no distribution for any version on
this platform. camb substitutes for every use in this plan. No package here
depends on CLASS.

`verify/tracker_relations.py` passes 11 of 11 checks.

---

## 7. Sequencing summary

```
Phase 0 (parallel)    WP-0 Run 02 adversary        1 day
                      WP-1 already-decided check   2 days
                      -> K1, K7

Phase 1 (parallel)    WP-2 Pantheon+ refit         4 days
                      WP-4 f_v0 vs measurement     2 days
                      WP-5 curvature requirement   4 days  [Maple 002]
                      WP-6 two-phase sensitivity   2 days  [Maple 001]
                      -> K2, K3, K4, K5

Phase 2               WP-3 ablation                1 day   (after WP-2)
                      WP-7 Omega_b h^2 and S_8     3 days
                      WP-8 Hubble-flow variance    2 days
                      WP-9 light propagation       2 weeks
                      -> K6

Phase 3               WP-10 Run 03 corrections     1 day
                      gate check -> extensions
```

Maple jobs 001 and 002 are independent and go on the queue the same day, so
Phase 1 costs two Maple round trips in parallel rather than two in series.
No package blocks on more than one round trip per day.
