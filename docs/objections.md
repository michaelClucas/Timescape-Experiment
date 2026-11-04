# Live objections (seed, v0)

These are unresolved in the published literature. The audit reports them
as unresolved, with both sides stated from primary sources. An output that
makes any of them read as settled is wrong regardless of which way it
settles them.

Each objection is paired with the derivation step it attacks (`D1`-`D8`
in `derivation-chain.md`).

---

## O1. Backreaction cannot be large enough (attacks D4)

Green and Wald constructed a framework for the effect of small-scale
inhomogeneity on large-scale dynamics and argued that backreaction takes
the form of an effective traceless stress, so it behaves like radiation
rather than like dark energy, and cannot produce acceleration.

Buchert and a large set of co-authors published a direct response arguing
that the framework's assumptions exclude the regime where backreaction
would be significant, so the result is a consequence of the setup rather
than a theorem about the universe.

Audit: this is the single highest-priority item. Required output:
- Both positions from primary sources, in their own terms.
- The precise assumption each side says is doing the work.
- Whether either side has conceded any point in later work.
- Whether the disagreement is mathematical (one of them is wrong) or
  about which idealisation applies to the real universe.
- A `[LEAD]`-tagged note on whether any third party has adjudicated.

Do not report a winner. If the literature has not resolved it, the output
says so, and that is the correct result.

## O2. The clock effect is a calibration convention, not physics (attacks D6)

The strongest form: differences in clock rates between regions are
statements about how one chooses to synchronise and calibrate, and a
quantity that depends on that choice is not an observable. On this
reading, the cumulative tens-of-percent difference is an artifact of a
particular identification between the inhomogeneous spacetime and its
FLRW template, not a physical effect.

The reply appeals to quasilocal gravitational energy and to the claimed
Cosmological Equivalence Principle, holding that the effect is physical
and in principle measurable.

Audit:
- State the Cosmological Equivalence Principle in Wiltshire's own words,
  with a locator. Is it an extra postulate or claimed to follow from GR?
- Identify the gauge-invariant content, if any. What would a measurement
  of the effect actually measure?
- Find the published critiques by name and state their argument.
- Establish whether anyone has proposed a test that distinguishes
  "physical clock effect" from "calibration convention".

If this objection holds, timescape fails even if O1 resolves entirely in
backreaction's favour. Those are independent.

## O3. Circularity in the supernova evidence (attacks D8)

Supernova standardisation parameters are typically calibrated within an
assumed cosmology. If a timescape analysis inherits standardisation
derived under LCDM, the comparison is not clean; if it refits them, the
parameter count changes and the model comparison must account for it.

Audit: establish what the published timescape supernova analyses actually
do here, per analysis. Quote the method section. This is checkable and is
the most consequential technical question about the headline evidence.

## O4. Prediction versus postdiction (attacks D7)

Whether the void fraction f_v is independently determined from structure
surveys and then *predicts* the observed distance-redshift relation, or is
fitted to the supernova data it is then said to explain.

Audit: find the independently measured void fraction and its uncertainty,
find the fitted value, and compare. If they agree within errors and the
measurement was not derived under an LCDM assumption, that is substantial
evidence and should be stated as such. If f_v is fitted, the model's
status is weaker than its presentations suggest.

## O5. LTB-style void models are already excluded (attacks the programme)

Large local void models were strongly constrained by kinetic
Sunyaev-Zel'dovich measurements and by other probes.

Audit: establish whether those constraints apply to timescape. Timescape
is not a single large local void, so the constraints may not transfer, but
the argument that they do not transfer has to be made explicitly rather
than assumed. Find out whether anyone has made it.

## O6. Severity of the CMB test (attacks D8)

Fitting the acoustic peak structure with a different sound-horizon
calibration and a different distance-redshift relation is a strong
constraint. Claimed consistency is not the same as demonstrated
consistency at the precision of current data.

Audit: find the actual numbers and the data release used. A fit to
pre-Planck data is not a current result.

---

## Objections not yet seeded

The audit should add any it finds. Candidates to check for:
structure growth, BBN consistency, the foliation dependence of scalar
averaging, whether the two-phase split is stable under refinement, and
anything raised in conference proceedings or comment papers that did not
get a journal reply.

## Seed warning

The objections above are reconstructed from background knowledge without
retrieval. Names, framings, and attributions may be wrong, and the
strongest published version of each objection is probably sharper than
the summary here. Treat all of it as `[LEAD]` and go to the sources.
