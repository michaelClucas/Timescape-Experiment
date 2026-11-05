# WP-4: is `f_v0` measuring what it claims?

**Status:** complete for what this dataset can settle. One part deliberately
not done and named in §7.
**§6 was corrected on 2026-11-05 and §10 is why.** A later session settled the
threshold question §4 has to argue around (§10.1-10.2) and found that §6
applied an interval test to a one-sided bound (§10.3). §6 now carries the
corrected test and §6.0 records what it got wrong. §4's `[INFERENCE]` premise
is no longer unverified; §10.2 supports it twice.

**Read §11 and §12 before §3.** A third session of 2026-11-05, running in
parallel with the one that corrected §6, checked §3's attribution of the
1.5-point pipeline-vs-published gap to the survey mask, which had never been
checked. §11 confirms it and turns it into a ±1.5-point systematic that §3 and
§5 do not carry. **§12 then found a sourced defect in
`verify/wp4_void_fraction.py`'s own mask indexing**, worth −0.710 points: every
measured fraction in §3, §5, §6, §10 and §11 is high by that amount, and §12.3
carries the corrected values. The script was deliberately left unaltered; see
§12.6 and `OPEN-QUESTIONS.md` Q-4. **The corrected bound does not change which
fitted values §6 and §10.3 exclude**, which §12.4 checks.
**Provisional on WP-0.** Run 02 has not run.
**Evidence:** `verify/wp4_inspect_inputs.py`, `verify/wp4_void_fraction.py`
(14/14), `verify/wp4_fv0_comparison.py` (13/13, two checks added by the
2026-11-05 correction to §6; this line still read 11/11 after that change),
`verify/wp4_critical_threshold.py` (14/14, for §10),
`verify/wp4_mask_resolution.py` (16/16, for §11),
`verify/wp4_vast_mask_convention.py` (10/10, for §12).
**Dataset:** VAST SDSS DR7 void catalogues v1.3.1,
`doi:10.5281/zenodo.11043278`, provenance in `data/001-sdss-dr7-voids/`.
**Kill criterion tested:** K5. **It does not fire.** §6.

**The short version.** The measurement bounds `f_v0` from below only. The
strongest bound, 0.6228, excludes two of the ten fitted values and leaves
eight consistent with it, so K5's "every fitted value" is not met and the
branch does not stop. That exclusion is conditional on the 17.5-point edge
systematic: under the other edge treatment the bound excludes nothing.

The more durable result is WP-4's second "counts against" limb, that the fitted
spread is irreducible. It holds decisively: arXiv:1410.3470 fits one Planck
dataset three ways and gets 0.627, 0.550 and 0.557 with ±0.016 errors,
`chi2/dof = 9.14`. And the two prescriptions the void bound excludes are the
same two whose dressed `H_0` falls below timescape's own admissible floor
(§10.4) — two independent routes rejecting the same two of three. Objection O4
hardens, through the second limb rather than through K5.

---

## 1. What was asked

D4 in `docs/RESEARCH-PLAN.md`: does the independently measured void fraction
agree with the fitted `f_v0`, or not?

## 2. Every number is LCDM-conditioned, per cut 8

The catalogues are supplied in comoving Cartesian coordinates derived under a
FLRW distance-redshift relation that timescape does not share
(`data/001-sdss-dr7-voids/SOURCE.md` field 7). Every fraction below carries
that label. §5 quantifies what it costs, which turns out to be less than
field 7 feared, for a reason specific to this dataset.

## 3. The measured void fraction

Computed, not quoted. The method is the catalogue paper's own: rasterise the
union of all ~40,000 VoidFinder hole spheres onto a 1 h⁻¹ Mpc grid and count
cells also inside the masked survey volume. Cut 6 forbids summing sphere
volumes; the union is rasterised so overlaps count once.

| | Planck2018 | WMAP5 |
|---|---|---|
| **edge voids included** | **62.28%** | **62.63%** |
| edge flag 0 only | 44.82% | 44.86% |
| edge flag != 1 | 45.86% | 45.72% |
| published, arXiv:2202.01226 Table 6 | 60.8% | 61.1% |

Agreement with the published value to about 1.5 points, high in both
cosmologies, attributable to the 1-degree mask resolution.

**V2/VIDE and V2/REVOLVER are not reproducible from the published files.**
Summing `(4/3)π r_eff³` gives 73.7% and 80.7% (Planck2018) against published
68.1% and 90.8%. The discrepancy runs **opposite ways** for the two pruning
methods, so no single systematic explains it. `radius` is confirmed to be the
effective radius from the void volume, since the tabulated triaxial semi-axes
satisfy `a1 a2 a3 = radius³` to machine precision in all 1049 V2 voids. The
partial explanation is that arXiv:2202.01226 Sec. 3.2 zeroes the volume of any
Voronoi cell extending outside the survey, so `r_eff` is not the spatial
extent; rebuilding the extent needs the tessellation, which needs galaxy
positions this dataset does not contain. That explanation predicts a
one-directional shortfall and the observed discrepancy is not one-directional,
so it is **recorded as unexplained**.

That matters for K5's wording, which leans on "the measured fraction, with
algorithm spread". The algorithm spread is exactly what this dataset cannot
independently establish.

**A note on the source.** arXiv:2202.01226 Table 6's note says "Edge voids are
excluded from all properties except Nvoid". The published 60.8% matches the
edge-**included** 62.3%, not the edge-excluded 44.8%, and Sec. 4.2 describes a
grid-particle count with no edge filter. So the volume column does not exclude
edge voids despite the note. Anyone reading Table 6 at face value gets this
wrong.

## 4. The two quantities are not the same quantity

`SOURCE.md` section 6 requires this step before any comparison, and it is the
substance of WP-4.

**Timescape's `f_v0`** is the present-epoch volume fraction of the void phase
in a two-phase Buchert average, and the phase boundary is a **critical-density
criterion**. `[SOURCED]` arXiv:1306.3208 p. 2: bound systems "necessarily form
in regions where the density is greater than critical" and are embedded within
regions bounded by a "finite infinity surface". `[SOURCED]` arXiv:1009.5855
Sec. 2: "we and all the objects we observe are necessarily in regions of
greater than critical density, which are contained within walls". So walls are
the above-critical volume and voids are everything else.

**VoidFinder's voids** are regions grown from cells empty of wall galaxies.
`[SOURCED]` arXiv:2202.01226 Sec. 3.1: field galaxies are removed by a
third-nearest-neighbour cut, the rest are gridded, "a sphere is then grown
from each empty cell in the grid until it is bounded by four galaxies", and a
void is the union of a maximal sphere of radius at least 10 h⁻¹ Mpc with
overlapping smaller spheres. **There is no density threshold in that definition
at all.**

**V2's voids** are watershed basins pruned by a zone-linking density (VIDE) or
by taking zones above the median zone volume (REVOLVER). `[SOURCED]`
arXiv:2202.01226 Sec. 4.2 on its own catalogues: "many galaxies in overdense
regions are incorrectly classified as void galaxies by V2" and "V2 is not
ideal for isolating the void environment". So V2/REVOLVER's 90.8%, the largest
of the three and the one that would most help a high fitted `f_v0`, is not a
measurement of underdense volume on its own authors' account.

**The direction of the mismatch, which is what makes the comparison usable at
all.** A region containing no wall galaxies is, on any reasonable bias model,
below the critical density. The converse fails: much below-critical volume
contains galaxies. So the VoidFinder void set is contained in the
below-critical set, and **the measured 62.3% is a lower bound on the quantity
`f_v0` names**, not an estimate of it. `[INFERENCE]`; premise: that galaxy
absence implies sub-critical density. The premise can fail where dark matter is
above critical and galaxy formation is suppressed, so the bound is not a
theorem. It is one-sided in the stated direction either way.

## 5. The error budget, and a correction to `SOURCE.md` field 7

| Term | Size |
|---|---|
| **survey-edge treatment** (cut 4) | **17.46 points** |
| FLRW conditioning, timescape against Planck2018 (estimated) | ~2.01 points |
| cosmology within FLRW (cut 3) | 0.35 points |
| this pipeline against the published value | 1.48 points |

The FLRW-conditioning estimate is the one worth explaining, because field 7
treats it as the headline problem.

`f_v` is a **ratio of volumes**, so a uniform rescaling of all distances
cancels exactly. What survives is the change in the **shape** of `D_C(z)`
across `0 < z < 0.114`, which to leading order is set by `q_0`. The dataset
supplies a measured sensitivity to a known change in `q_0`: Planck2018
(`q_0 = -0.528`) against WMAP5 (`q_0 = -0.613`) is `Δq_0 = 0.086` and moves the
answer by 0.35 points. Timescape's dressed `q_0` at `f_v0 = 0.695` is `-0.036`,
so `Δq_0 = 0.492` against Planck2018, a factor 5.7 larger. Scaling gives ~2.0
points. `[INFERENCE]`; premises: linearity in `Δq_0` over this range, and `q_0`
capturing the leading shape difference at `z < 0.114`. It is an extrapolation
by a factor of 5.7 and is quoted as an estimate, not a result.

**So the circularity `SOURCE.md` field 7 identified is real and is about eight
times smaller than the survey-edge systematic.** Field 7 was right in principle
and the effect is small *for this dataset*, because the survey is shallow and
`f_v` is a ratio. That is a correction to the error budget, not to the
reasoning: on a deep survey the term would not be small.

## 6. Does K5 fire? No. (Corrected 2026-11-05; see §6.0)

### 6.0 What this section got wrong, and who caught it

**The first version of this section applied an interval test to a one-sided
quantity, which is invalid.** It said: the measured interval is 0.448 to 0.626,
two fitted values (0.550 and 0.557) "lie inside it", so K5's condition is not
met.

But §4 establishes that the measurement is a **lower bound** on `f_v0`, not an
interval containing it. If 0.6228 is a lower bound, then `f_v0 = 0.550` and
`0.557` lie **below a lower bound** and are **excluded by it**. They are not
"inside the measured interval" in any sense that bears on K5. The two values
cited as sparing K5 are the two the bound actually excludes.

Caught by the parallel session of 2026-11-05, which argued it in §10.3 and
pinned it as a check in `verify/wp4_critical_threshold.py` so it cannot
silently vanish. **§10.3 is the authority on why the old test was wrong**; this
section is the corrected test. The verdict is unchanged; the argument for it
was broken and is now sound.

### 6.1 The corrected test

K5: "WP-4 finds the measured void fraction excludes **every** fitted `f_v0`."

The measurement bounds `f_v0` from below only, so the test is: does the bound
sit above every fitted value?

Both cosmologies reported apart, per cut 3, never averaged.

| Bound | Value | Fitted values below it | K5 condition |
|---|---|---|---|
| edge-included, WMAP5 (strongest) | 0.6263 | 0.550, 0.557 | not met |
| edge-included, Planck2018 | 0.6228 | 0.550, 0.557 | not met |
| edge-excluded, Planck2018 | 0.4482 | none | not met |
| edge-excluded, WMAP5 (weakest) | 0.4486 | none | not met |

The two cosmologies agree on which fits are excluded, so the choice between
them does not matter here; the edge treatment does.

**Eight of the ten fitted values sit at or above the strongest measured lower
bound**, so they are consistent with it and "every fitted value" is not met.
**K5 does not fire. The branch does not stop** and `T13`'s evidential weight
does not collapse by this route.

### 6.2 The exclusion that is real, and what it is conditional on

The bound does exclude two fits, which the first version of this section denied.
Three qualifications, all of which matter more than the exclusion:

1. **It is entirely conditional on the dominant systematic.** Edge-included,
   the bound excludes 0.550 and 0.557. Edge-excluded, it excludes nothing. The
   two variants disagree about whether any fit is excluded, and the gap between
   them is the 17.5-point edge treatment §5 names as dominant.
2. **The third low fit is not distinguished from the bound.** `0.627`, the
   `A(H̄_dec)` prescription, clears the bound by `0.0042`. That is smaller than
   the `0.0148` by which this pipeline disagrees with arXiv:2202.01226's own
   published fraction. Not excluded, and not resolved either.
3. **A lower bound cannot touch the high fits at all.** 0.72, 0.76, 0.791 and
   0.95 are consistent with any bound at or below them, so the bulk of the
   fitted spread is untested by this measurement in principle, not just in
   practice.

K5's wording also relies on an algorithm spread this dataset cannot
independently establish (§3), which is a fourth reason the criterion could not
have been decided here either way.

### 6.3 Two routes converge on the same two prescriptions

The two fits the edge-included bound excludes are the same two whose dressed
`H_0` falls below timescape's own admissible floor of 57. **§10.4 has the
table and the argument.** That convergence is the strongest thing in this
package, and it is a sharper statement than §8's: the model's three CMB
prescriptions are not merely mutually inconsistent with each other, two of the
three are independently disfavoured.

## 7. What was not done, and the decision behind it

`data/001-sdss-dr7-voids/cuts.md` leaves one question open deliberately:
whether the volume fraction is recomputed under the timescape
distance-redshift relation from the catalogue's angles and redshifts.

**Decision: not done, and it would not be enough on its own.** The reason is
not budget. Recomputing volumes under a different distance-redshift relation
requires **re-running the void finders**, because the void identification
itself depends on the comoving positions: VoidFinder grows spheres in the
gridded wall-galaxy distribution and V2 tessellates it. Converting the supplied
void radii to a timescape distance scale would move the voids without moving
the galaxies, which is not the same calculation and would produce a number
that looks like the answer and is not one.

Re-running the finders is tractable, since VAST is public, but it needs the NSA
galaxy catalogue, which is not in this dataset, and it is a work package rather
than a cycle. What is delivered instead is §5's estimate of what the
conditioning is worth, ~2 points, which bounds the thing field 7 asked about
without pretending to have removed it. `cuts.md` requires that the
LCDM-conditioned number not be presented as a clean comparison if the
recomputation is skipped; it is not, here or in the write-up.

No change was made to `cuts.md`. Nothing it decided in advance was relaxed.

## 8. The actual result: the second limb

WP-4's "counts against" clause reads: "the measured fraction, with algorithm
spread, excludes the fitted values, **or the fitted spread 0.550-0.791 is
irreducible**." The first limb fails. The second holds.

**`f_v0` is fitted in every analysis retrieved, and the fits do not agree.**

| `f_v0` | Uncertainty | What was fitted | Source |
|---|---|---|---|
| 0.76 | +0.12/-0.09 | CMB sound horizon + BAO + SNe | arXiv:0709.2535 |
| 0.95 | +0.03/-0.04 | Union2, "out of the box" | arXiv:1009.5855 Table 1 |
| 0.72 | ±0.05 | SDSS-II, "out of the box" | arXiv:1009.5855 Table 1 |
| 0.695 | +0.041/-0.051 | Planck acoustic scales | arXiv:1306.3208 |
| 0.627 | +0.014/-0.012 | CMB, matching `A(H̄_dec)` | arXiv:1410.3470 Table 2 |
| 0.550 | +0.017/-0.015 | CMB, matching `W(k = 0)` | arXiv:1410.3470 Table 2 |
| 0.557 | +0.017/-0.015 | CMB, matching `W(k ≠ 0)` | arXiv:1410.3470 Table 2 |
| 0.791 | +0.039/-0.034 | DES-SN5YRcut | arXiv:2406.05048 Table 6 |
| 0.665 | +0.008/-0.009 | DES-SN5YRcut + BAO | arXiv:2406.05048 Table 6 |
| 0.675 | point estimate | Pantheon+ 1690, MLE | arXiv:2311.01438 Fig. 8 |

The sharpest evidence is **internal to one paper**. arXiv:1410.3470 Table 2
fits the same Planck data three times, differing only in how the timescape
geometry is matched to the CMB, and gets 0.627, 0.550 and 0.557 with errors of
±0.016. Weighted about their mean, `χ² /dof = 9.14` on 2 degrees of freedom;
the widest pair is 3.7σ apart. Three descriptions of one universe from one
dataset by one set of authors.

Across the whole literature the spread 0.550 to 0.791 is **15 times** the
±0.016 the tightest fits quote, and the full range reaches 0.95. A parameter
whose fitted value moves by that much with the fitting prescription is a
fitting parameter wearing the name of an observable, which is exactly the shape
of objection O4.

**This is not the same as K5 firing**, and the difference matters. K5 would
have meant "observation contradicts the model". What is established is weaker
and more awkward: observation does not currently constrain this parameter at
all, and the model's own determinations of it are mutually inconsistent.

## 9. Carried to other packages

- **To WP-1.** arXiv:1410.3470 Table 2 also gives the dressed `H_0` for each
  matching prescription: 60.984 (`A`), 56.148 (`W k=0`), 56.774 (`W k≠0`). Two
  consequences. First, this sources the `60.98` that
  `findings/WP-1-comparability.md` §4.4 had to mark `[UNKNOWN]`. Second, and
  more pointedly, **two of the three prescriptions fall below timescape's own
  admissible floor** of `57 < H_0 < 68` from arXiv:1009.5855 Sec. 2. WP-1
  compared one dressed value against the distance ladder; the prescription
  spread within the CMB fit is itself 4.8 km/s/Mpc, comparable to the width of
  the admissible band. WP-1's conclusion is unchanged, since its finding was
  that the `H_0` row is non-discriminating, and this makes it less
  discriminating rather than more.
- **To WP-5.** The curvature requirement inverts a relation containing `f_v0`
  and `f_vi`. The sensitivity to the `f_v0` spread that Maple job 002 was asked
  to report is therefore sensitivity over 0.550 to 0.791 at least, and the
  spread is not reducible by measurement. WP-5's answer will carry that spread
  whatever Maple returns.
- **To WP-10.** Two corrections to seed and run outputs, not made here because
  runs are append-only: the `H_0` row of Run 01's discrimination table (from
  WP-1), and the `f_v0` provenance now that `0.550` and `60.98` are sourced to
  arXiv:1410.3470 Table 2 rather than arXiv:1306.3208 Table 1 as Run 01's
  ledger states.
- **A new dataset would be needed** to improve this: a deep survey, where the
  edge systematic is proportionally smaller and the FLRW-conditioning term is
  not negligible, with the void finders re-run under both distance-redshift
  relations. That is a work package, not a cycle, and it is not in the current
  plan.

---

# Addendum, 2026-11-05 (second session): the threshold, and a correction to §6

**Added by a later session of the same date, on branch
`research/auto-2026-11-05-day2`.** Appended rather than merged into the
sections above, so that what was concluded when stays readable. §4 and §6 are
unchanged in place; **§6's test is wrong and §10.3 below says how.**

**Evidence:** `verify/wp4_critical_threshold.py` (14/14).
**Still provisional on WP-0.**

## 10.1 There is no numerical threshold, and there cannot be one

`logs/2026-11-05-STATUS.md` §7 named the one question that would have changed
yesterday most: *is `f_v0` the volume fraction below the critical density or
below some other threshold, and is the threshold published as a number or an
equation?* It has an answer, and the answer is negative for a reason stronger
than absence.

`[SOURCED]` arXiv:0712.3984 §5, "Finite infinity and the true critical
density". Its Eq. (7) is a **denial**:

> `rho_cr != 3 H_av^2 / (8 pi G)`

"In the standard FLRW cosmology the critical density is proportional to the
square of the Hubble parameter. However, in an inhomogeneous cosmology this is
no longer true, [Eq. 7], as the average Hubble parameter, `H_av`, is related to
the spatial scale of averaging and the clock chosen."

The relation sign took two routes: `pdftotext` dropped the glyph and rendered
it `=`, the `ar5iv` HTML gives `!=`. It is settled from inside the PDF
independently of both, by the same section's later "as long as we evolve the
average geometry purely by the Friedmann equation, **with equality in (7)**",
which only parses if (7) as printed is not an equality.

Finite infinity is then defined **kinematically**, `[SOURCED]`, same section:
"finite infinity is defined in terms of a scale over which the average
expansion, including virialized, collapsing and marginally expanding regions is
zero, `[theta]_fi = 0`, while being positive outside. Then `rho_cr = rho_fi`."

So the wall/void demarcation is a condition on the **average expansion** -
local, scale-dependent and clock-dependent - and the model explicitly rejects
the one formula that would turn it into a density. There is no threshold number
to find. A later session should not go looking for one.

This does not weaken §4. It explains why §4 had to argue about the *direction*
of the mismatch rather than its size: the size has no definition in the model.

## 10.2 The premise §4 could not check

§4's `[INFERENCE]` premise was: a region containing no wall galaxies is below
the critical density. It is now supported twice, by routes that fail
independently.

**Route 1, the model's own observational identification.** `[SOURCED]`
arXiv:0909.0749 §II: bound structures formed from "over-critical
perturbations" are enclosed "within regions which are spatially flat on
average, and marginally expanding at the boundary. These boundaries are called
finite infinity regions"; "The walls constitute the union of such finite
infinity regions"; and "Observationally they would correspond to all extended
structures that contain galaxy clusters, namely **sheets, filaments and
knots**."

That is the structure VoidFinder's wall galaxies trace, and it is timescape's
own statement of how its wall phase is to be recognised in a galaxy survey. The
premise §4 had to infer is in substance asserted by the model's author as the
intended correspondence. What remains `[INFERENCE]` is narrower and more
tractable: whether VoidFinder's third-nearest-neighbour cut implements that
correspondence well. That is a question about an algorithm, not about physics.

**Route 2, the failure condition quantified.** Under the FLRW-style reading
that §10.1's Eq. (7) denies - the only reading in which the threshold is a
number at all, and therefore the only one in which the premise can fail
numerically - a matter-only region reaches critical density at
`1 + delta_m = 1 / Omega_M`:

| reading | `Omega_M` | threshold `1 + delta_m` |
|---|---|---|
| Planck2018, flat LCDM | 0.3150 | 3.175 |
| WMAP5, flat LCDM | 0.2580 | 3.876 |
| timescape dressed, `f_v0 = 0.550` | 0.5737 | **1.743** |
| timescape dressed, `f_v0 = 0.695` | 0.4110 | 2.433 |
| timescape dressed, `f_v0 = 0.950` | 0.0738 | 13.559 |

The dressed relation is `Omega_M0 = (1/2)(1 - f_v0)(2 + f_v0)`, `[SOURCED]`
arXiv:0909.0749 Fig. 3 caption, which prints it with the value 0.33 at
`f_v0 = 0.762`. The script independently checks that composing that paper's
Eq. (27), `Omega_M = gamma_w^3 Omega_M_bar`, with the tracker relations already
verified in `verify/tracker_relations.py` reproduces the closed form to
`2.2e-16` across `f` in `(0.01, 0.99)`.

So in the most permissive case available, a VoidFinder void must reach **1.74
times the mean matter density** to be above critical. That is a wall-level
overdensity inside a region selected for containing no wall galaxies, and it
needs galaxies to anti-correlate with matter on 10-30 h^-1 Mpc scales.
`[INFERENCE]`; premise named: linear bias `b > 0` on those scales.

**The radial density profiles were not obtained, and cannot be.** `[SOURCED]`
arXiv:2202.01226 §4.4 defines the stacked profile in Eq. (5) as
`delta(r) = n(r)/n_bar - 1`, a **galaxy number** density contrast, and
publishes it only as Figures 5 and 6. There is no table of profile values in
the paper, and both figures are raster JPEGs at 148 ppi, so there are no vector
coordinates to recover. Reading values off them by eye would produce numbers
indistinguishable in form from data, so it was not done. `[LEAD]`: whether the
VAST project publishes the profile data separately was not checked.

## 10.3 §6 applies the bound in one direction only, and that is wrong

**This is a correction to §6 of this finding, not an extension of it.**

§6 and `verify/wp4_fv0_comparison.py` test whether each fitted `f_v0` falls
inside the measured **interval** `[0.448, 0.626]`, find that `0.550` and
`0.557` do, and conclude `f_v0` is "unconstrained by measurement". But §4
establishes the measured fraction as a **lower bound** on `f_v0`, and a lower
bound excludes every value **below** it. Interval membership is the wrong test:
the interval's low end is the edge-*excluded* variant, which is a weaker bound
on the same quantity, not a second measurement of it. Taking the minimum over
variants is the right conservative choice for the bound's validity, and it
licenses nothing whatever about fitted values below the maximum.

Applying the bound in the direction it actually cuts:

| bound | excludes |
|---|---|
| 0.6228 (Planck2018, edge included) | `f_v0 = 0.550`, `0.557` |
| 0.6263 (WMAP5, edge included) | `f_v0 = 0.550`, `0.557` |
| 0.4482 (Planck2018, edge excluded) | nothing |
| 0.4486 (WMAP5, edge excluded) | nothing |

So the exclusion is **real and entirely conditional on the edge treatment**,
which §5 had already identified as the dominant systematic at 17.5 points. The
edge-included variant is the one matching the catalogue paper's own published
60.8%, per §3. Both halves are asserted in
`verify/wp4_critical_threshold.py` so neither can quietly vanish.

`f_v0 = 0.627`, the third low fit, clears the edge-included bound by `+0.0042`
- smaller than the `0.0148` by which this pipeline disagrees with the published
fraction, and far inside the 0.175 edge systematic. It is not excluded, and it
is not distinguished from the bound either.

**K5 still does not fire**, and §6's conclusion is unchanged: eight of the ten
fitted values sit at or above the strongest available bound, so "excludes every
fitted `f_v0`" is not met. What changes is the reason. §6 says the measurement
constrains nothing; it in fact excludes the bottom of the fitted range,
conditional on the systematic that dominates it. §8's second limb is unaffected
and still carries the package.

## 10.4 Where two routes converge

The two prescriptions the bound excludes, `0.550` and `0.557`, are the same two
of arXiv:1410.3470 Table 2's three whose dressed `H_0` - 56.148 and 56.774 -
falls below timescape's own admissible floor of 57 from arXiv:1009.5855 §2, as
§9 records.

| prescription | `f_v0` | dressed `H_0` | below the bound? | below the `H_0` floor? |
|---|---|---|---|---|
| `A(H_bar_dec)` | 0.627 | 60.984 | no (by 0.004) | no |
| `W(k = 0)` | 0.550 | 56.148 | **yes** | **yes** |
| `W(k != 0)` | 0.557 | 56.774 | **yes** | **yes** |

Two independent routes, one from measured void volumes and one from the model's
own admissible `H_0` band, reject the same two of three CMB matching
prescriptions. `[INFERENCE]`; the premises are §4's lower-bound reading and the
edge-included variant. It does not establish that `A(H_bar_dec)` is right - it
survives the bound by less than this pipeline's own error - but it does mean
only one of arXiv:1410.3470's three prescriptions is simultaneously consistent
with the measured void volume and with timescape's own `H_0` floor.

## 10.5 What timescape says fills the gap, and what it would take to measure it

`[SOURCED]` arXiv:0909.0749 §II: "Voids of a characteristic diameter 30h^-1
Mpc are observed to fill 40-50% of the universe at the present epoch", citing
Hoyle & Vogeley, ApJ 566, 641 - **not fetched**, so 40-50% is `[SOURCED]` as a
claim about what arXiv:0909.0749 says and `[LEAD]` as a claim about Hoyle &
Vogeley. The passage continues: "In addition there are numerous minivoids ...
Together voids of all sizes appear to dominate the volume of the present epoch
universe, the exact volume fraction depending on the empirical definition of a
void in terms of some particular negative density contrast."

Three consequences.

1. **That 40-50% overlaps this pipeline's measured 44.8-62.6%.** Timescape is
   not working from a different measurement of the large-void fraction than
   §3's.
2. **Timescape's own reconciliation of `f_v0 ~ 0.7` with a catalogued 40-50%
   runs through minivoids** - and arXiv:2202.01226's 10 h^-1 Mpc minimum radius
   excludes that population by construction. So §4's lower-bound reading is
   confirmed a third time, by a route needing no bias assumption and no density
   threshold: the catalogue cannot see a population the model requires. This
   also retires the cut-7 question for this comparison. No radius cut was
   applied, `cuts.md` is unmodified, and a radius cut would only push the
   measured fraction further below a floor.
3. **The gap is quantifiable.** Against the edge-included 0.6228:

   | fitted `f_v0` | minivoid volume fraction required |
   |---|---|
   | 0.627 | +0.004 |
   | 0.695 | **+0.072** |
   | 0.760 | +0.137 |
   | 0.791 | **+0.168** |

   The Planck acoustic-scale fit needs 7.2 points of the present horizon volume
   in voids this catalogue cannot see. The DES-SN5YR fit needs 16.8, which is
   27% of the measured large-void volume over again.

**So the measurement that would constrain `f_v0` is the minivoid volume
fraction, and there is no number for it anywhere in this dataset.** That is a
sharper statement of what §9's "a new dataset would be needed" was reaching
for: not merely a deeper survey, but a survey resolving voids below 10 h^-1 Mpc,
with its own volume fraction computed the same way. It is a work package.

---

# Addendum, 2026-11-05 (third session, day 3): §3's attribution, checked at last

**Added by a third session of the same calendar date, on branch
`research/auto-2026-11-05-day3`.** Appended, like §10, rather than merged into
the sections above. **§3's final sentence is corrected in substance here**: its
claim turns out to be right, and it was never checked by the session that wrote
it or by the one that followed.

**Evidence:** `verify/wp4_mask_resolution.py` (16/16). The six earlier scripts
were all re-run at `96fe08e` first and all pass unchanged.
**Still provisional on WP-0.**

## 11.1 The sentence under test, and why it was worth a cycle

§3 reads: "Agreement with the published value to about 1.5 points, high in both
cosmologies, attributable to the 1-degree mask resolution." The attribution was
an assertion. `logs/2026-11-05-STATUS.md` records that the first session did
not verify it, and the second session did not either.

It mattered because of §10.3. `f_v0 = 0.627` clears the edge-included measured
lower bound of 0.6228 by `+0.0042`, and this unverified 0.0148 is **three and a
half times that margin**. Whether the bound excludes two of arXiv:1410.3470
Table 2's three CMB matching prescriptions or all three rested on a systematic
nobody had looked at.

## 11.2 The mask convention moves the answer by 3.1 points, twice the gap

The survey mask is a `(360, 180)` boolean sky grid at 1 degree. A spatial cell
counts as inside the survey when the pixel containing its direction is set. At
`r = 332 h⁻¹ Mpc` one degree subtends `5.80 h⁻¹ Mpc`, so the footprint has a
boundary layer several cells thick whose position the mask fixes only to within
a pixel. Eroding and dilating the mask by one pixel brackets that: any finer
mask of the same footprint, and any convention differing from cell-centre
lookup by under a pixel, lies between them.

| variant | Planck2018 | WMAP5 |
|---|---|---|
| eroded 1 px | 63.52% | 63.85% |
| coarse 2°, all-pixels-set | 63.24% | 63.58% |
| **baseline 1°, as committed in §3** | **62.28%** | **62.63%** |
| coarse 2°, any-pixel-set | 60.94% | 61.28% |
| dilated 1 px | 60.45% | 60.79% |
| **published, arXiv:2202.01226 Table 6** | **60.8%** | **61.1%** |

**The span is 3.07 points (Planck2018) and 3.06 (WMAP5), against a gap of 1.48
and 1.53.** The mask term covers the gap twice over, and **the published value
falls inside the span in both cosmologies**. §3's attribution is confirmed in
magnitude.

`[LEAD]`, not `[SOURCED]`: a convention one pixel more inclusive than
cell-centre lookup reproduces Table 6 to within 0.35 points, but
arXiv:2202.01226's mask code was not read, so this does not establish that the
published pipeline used such a convention. What is established is that the two
pipelines are consistent once the footprint convention is treated as unknown to
one pixel, which it is.

## 11.3 Why the ratio does not cancel, which is a correction to this session

`f_v` is `(void cells inside the survey) / (survey cells)`, so a mask change
moves numerator and denominator together. **This session predicted, in writing
and before running anything, that the ratio would cancel most of the change,
that the whole bracket would come to "well under 0.5 points", and therefore
that §3's attribution would be refuted. That was wrong by a factor of six.**
Per protocol rule 6 the expectation is corrected and recorded, not the
tolerance widened; the script's docstring carries the failed prediction and
`logs/2026-11-05-day3.md` cycle 3 records it as a negative.

The cancellation argument is right in form and wrong in magnitude, for a reason
the argument names and this session then failed to evaluate. What survives the
cancellation is the difference between the void fraction of the boundary layer
and that of the bulk, and here that difference is enormous:

| layer | cells | void fraction | survey as a whole |
|---|---|---|---|
| added by dilation | +1,149,733 | **17.0%** | 62.3% |
| removed by erosion | −1,101,788 | **32.9%** | 62.3% |

The VoidFinder sphere union stops at the footprint edge; the mask does not. So
dilation appends a nearly void-free shell to the denominator and almost nothing
to the numerator, and 57% of an 8.6% volume change survives into the ratio.

## 11.4 Three other candidates, all negligible

Tested in the same script so that the mask conclusion is not one hypothesis
examined alone:

| term | size |
|---|---|
| **mask footprint convention, ±1 px** | **3.06 points, two-sided** |
| WMAP5's radial limit: its own 334.007 against the pickle's 332.386 | 0.490 points |
| denominator: rasterised cell count against analytic cone volume | 0.022 points |
| spatial grid, 1 → 2 h⁻¹ Mpc | 0.012 points |

The three together come to 0.524 points, under half the gap. The denominator
definition was this session's other pre-run favourite, on the argument that it
touches only the denominator and so has no cancellation to rely on; the two
volumes agree to 0.035% and it is the smaller lever by a factor of 140. Also
recorded as a wrong expectation. The grid result confirms the 1 h⁻¹ Mpc
rasterisation is converged, which arXiv:2202.01226 §4.2's stated grid size
implied but nobody had checked. A 0.5 h⁻¹ Mpc run was not done: 8× the cells is
about 1.2 GB of boolean grids and the 1→2 trend bounds it.

## 11.5 What it costs §10.3 and §10.4, which is nothing

§4 establishes the measured fraction as a **lower bound** on `f_v0`. The
conservative reading of a newly quantified two-sided systematic on a lower
bound is its **lowest** value, which is the dilated mask.

| Planck2018 edge-included bound on `f_v0` | value |
|---|---|
| conservative (dilated) | **0.6045** |
| as committed in §3 and §10.3 (baseline) | 0.6228 |
| aggressive (eroded) | 0.6352 |

| arXiv:1410.3470 Table 2 | `f_v0` | vs conservative | vs baseline | vs aggressive |
|---|---|---|---|---|
| `A(H̄_dec)` | 0.627 | +0.0225 | +0.0042 | **excluded** |
| `W(k ≠ 0)` | 0.557 | **excluded** | **excluded** | **excluded** |
| `W(k = 0)` | 0.550 | **excluded** | **excluded** | **excluded** |

**§10.3's and §10.4's conclusion survives, and is better supported than when it
rested on the baseline mask alone.** `0.550` and `0.557` are excluded under
every mask variant, sitting `0.0545` and `0.0475` below even the conservative
bound. Exactly two of three prescriptions are excluded, which is what §10.3 and
§10.4 say.

**What changes is the standing of the third.** §10.3 flagged `0.627`'s
`+0.0042` margin as thinner than the pipeline's own disagreement with the
published value and therefore not to be trusted. That is now sharp rather than
vague: under the conservative bound the margin is `0.0225`, five times what
§10.3 had, but under the aggressive bound `0.627` is itself excluded by
`0.0082`. So **whether arXiv:1410.3470's `A(H̄_dec)` prescription survives the
measured bound is set by a one-pixel footprint convention in a survey mask.**
Not excluded on the conservative reading, which is the one §4's bound licenses;
not safe either.

K5 is unaffected and still does not fire. §8's second limb, which is what
carries the package, is untouched.

## 11.6 What this closes, and the one thing it does not

`logs/2026-11-05-day2-STATUS.md` listed the unexplained 1.5-point gap as the
weakest load-bearing joint in WP-4. **It is closed.** The gap is a
footprint-convention effect of a size the convention can produce, in both
cosmologies, in the right direction, and it is not evidence of an error in
either pipeline. It leaves `[UNKNOWN]` and becomes a quantified systematic of
±1.5 points which every future quotation of the measured fraction should carry.

The error budget of §5 gains a row, larger than three of its four existing
ones:

| term | size |
|---|---|
| survey-edge treatment (cut 4) | 17.46 points |
| **mask footprint convention (§11.2)** | **3.06 points** |
| FLRW conditioning, estimated | ~2.01 points |
| cosmology within FLRW (cut 3) | 0.35 points |
| ~~this pipeline against the published value: 1.48 points~~ | now a consequence of the mask row, not an independent term |

**What it does not close.** The footprint convention arXiv:2202.01226 actually
used is still unread, so the measured fraction cannot be pinned inside the
3.06-point band; it can only be bracketed. Reading VAST's mask code would do
it, and that is a cycle rather than a package, but it needs a code repository
rather than a paper and was not attempted today. `[LEAD]`.

---

# Addendum, 2026-11-05 (third session, day 3, after the overseer's instruction): the convention, and a defect it exposed

**Added by the same session as §11, after it had stopped and the overseer
instructed it to read VAST's mask code.** §11.6 left that as the one `[LEAD]`
worth a cycle and argued it was not worth opening a day for. The overseer said
to do it.

**Evidence:** `verify/wp4_vast_mask_convention.py` (10/10).
**Still provisional on WP-0.**

**The short version.** The convention is now `[SOURCED]`, and reading it found
a **defect in this repository's own pipeline** rather than in the published one.
`verify/wp4_void_fraction.py` indexes the mask's declination axis with an
expression VAST does not use, which costs 0.710 points. Correcting it halves
the residual against arXiv:2202.01226 Table 6. It does **not** settle whether
`f_v0 = 0.627` is excluded, because the ±1-pixel pixelation systematic of §11 is
independent of the index expression and survives it.

## 12.1 The convention, sourced

VAST (Void Analysis Software Toolkit), which produced both the catalogues and
`NSA_main_mask.pickle`, is public at `github.com/DESI-UR/VAST`. Read at commit
`24e66e1`, the repository head on 2026-11-05, and **every claim below
re-checked at commit `133cfcf` of 2022-02-10**, contemporaneous with
arXiv:2202.01226's submission. The relevant lines are identical at both.

**The mask is built** in `python/vast/voidfinder/multizmask.py`, with
`dec_offset = -90` at line 15. `generate_mask` scales the galaxy angles and
truncates (line 166):

```python
scaled_converted_ang = (mask_resolution*ang).astype(int)
```

then sets each unique scaled pair (line 192):

```python
mask[row[0], row[1] - mask_resolution*dec_offset] = True
```

**The mask is read** in `python/vast/voidfinder/voidfinder_functions.py`, where
`not_in_mask` ends (line 249):

```python
return not survey_mask_ra_dec[int(n*ra), int(n*dec) - n*dec_offset]
```

So the declination index is `int(n·dec) + 90n` in both places, with truncation
**toward zero** applied after scaling and before the offset. VAST is internally
consistent: the array is written and read with the same expression.
`[SOURCED]`.

## 12.2 This pipeline uses a different expression, and it is wrong for this file

`verify/wp4_void_fraction.py`'s `in_mask` computes
`((dec + 90.0) * res).astype(np.int64)`, applying the offset **before** the
truncation. For `dec ≥ 0` the two agree, since `int(dec) + 90 = int(dec + 90)`.
For `dec < 0` they differ by exactly one pixel, because truncating toward zero
rounds a negative number **up**:

| `dec` | this pipeline | VAST | |
|---|---|---|---|
| −11.0 | 79 | 79 | same |
| −10.5 | 79 | **80** | differ |
| −5.3 | 84 | **85** | differ |
| −0.4 | 89 | **90** | differ |
| 0.0 | 90 | 90 | same |
| +5.3 | 95 | 95 | same |
| +70.0 | 160 | 160 | same |

VAST's pixel 85 covers `dec ∈ (−6, −5]`; this pipeline's covers
`dec ∈ [−5, −4)`. **209 of the footprint's 9133 set pixels (2.3%) are
southern**, and the SDSS DR7 main sample reaches to about `dec = −11`.

**An array must be read with the convention it was written with.** The pickle
was written by `generate_mask`, so VAST's expression is correct for this file
and this pipeline's is a **defect, not a variant**. It is also a *shift* rather
than an erosion or a dilation, so it is a different operation from anything
§11 varied and is not bracketed by §11's erode-dilate pair.

**Why nothing caught it.** `verify/wp4_void_fraction.py` validates its mask
convention by confirming that 1.0000 of 1163 VoidFinder void centres fall
inside the mask against 0.1660 under the transposed convention. That
distinguishes transposed from not. It cannot distinguish a one-pixel
declination shift, because both expressions put essentially every void centre
inside a 9133-pixel footprint. The check was correct about what it tested and
silent about this. **It is the third time in three days that a committed check
passed while the thing it was taken to establish was wrong**, after §10.3's
one-sided bound and §11.3's expectation.

## 12.3 The corrected numbers

| | Planck2018 | WMAP5 |
|---|---|---|
| as committed in §3 (offset-before index) | 62.280% | 62.628% |
| **corrected (VAST index)** | **61.570%** | **61.923%** |
| shift | −0.710 | −0.705 |
| survey cells | +475,266 (+1.75%) | +478,563 (+1.73%) |
| published, arXiv:2202.01226 Table 6 | 60.8% | 61.1% |
| residual, as committed | +1.480 | +1.528 |
| **residual, corrected** | **+0.770** | **+0.823** |

The shift has the same sign and nearly the same size in both cosmologies, as a
convention difference should and as noise would not. It is 0.71 points against
§11's 3.07-point pixelation span, so the ordering §11 predicted holds: a
partial-footprint shift is smaller than a whole-boundary bracket.

**Correcting the index roughly halves the disagreement with the published
value.** §11's conclusion is unaffected — the remaining +0.77 is still well
inside the ±1.5-point pixelation systematic, and the published value still lies
inside the bracket — but the two pipelines now agree better than §11 left them.

## 12.4 What it does to the exclusion, which is less than it looks

§11.5's bound table, recomputed about the corrected centre. The ±1-pixel
pixelation systematic is a property of the 1-degree mask and is independent of
the index expression, so it is re-applied rather than discarded:

| Planck2018 edge-included bound on `f_v0` | value |
|---|---|
| as committed (offset-before index) | 0.6228 |
| **corrected (VAST index)** | **0.6157** |
| corrected, less half the ±1 px span | 0.6003 ← conservative |
| corrected, plus half that span | 0.6311 ← aggressive |

| arXiv:1410.3470 Table 2 | `f_v0` | vs corrected | vs conservative | vs aggressive |
|---|---|---|---|---|
| `A(H̄_dec)` | 0.627 | +0.0113 | +0.0267 | **excluded** |
| `W(k ≠ 0)` | 0.557 | **excluded** | **excluded** | **excluded** |
| `W(k = 0)` | 0.550 | **excluded** | **excluded** | **excluded** |

**`0.550` and `0.557` remain excluded**, now 0.0503 and 0.0433 below even the
conservative corrected bound. That exclusion has survived the edge treatment,
the one-pixel footprint bracket and an index correction, and is the most robust
result WP-4 has produced.

**`0.627` is still not settled.** It sits between the conservative 0.6003 and
the aggressive 0.6311, so the correction moved the centre without resolving the
question. **Reading the code closed the `[LEAD]` in the sense it was asked —
the convention is `[SOURCED]` — and did not settle the question it was asked in
order to settle**, because the term that straddles 0.627 is the 1-degree
pixelation, not the index expression, and pixelation is a property of the
supplied mask that no amount of code-reading removes.

K5 is unaffected and still does not fire. §8's second limb is untouched.

## 12.5 The negative: Table 6's own volume code is not in VAST

The obvious candidate for "what computed Table 6" is
`python/vast/catalog/void_overlap.py`, which places a 1 h⁻¹ Mpc grid with
`np.arange` and filters it through `MaskChecker.not_in_mask`, together with
`python/vast/catalog/void_catalog.py`, whose `get_single_overlap` is documented
"Calculates the void volume fraction of a void catalog".

**Both first appear in commit `04233d7`, dated 2025-02-06 — three years after
arXiv:2202.01226 was submitted.** At `133cfcf` the repository contains no
grid-based volume-fraction code at all: searching the paper-era tree for
`np.arange(x_min`, `grid_points` and `test particle` returns nothing. So that
module did not produce Table 6.

It is also not a candidate on its merits, because it defaults to
`edge_buffer=30`, cutting every grid point within 30 h⁻¹ Mpc of the survey
border out of **both** numerator and denominator. That is a far larger
intervention than anything considered in §11 or here, and it is not what
arXiv:2202.01226 §4.2 describes.

**So the denominator convention remains `[UNKNOWN]` and cannot be settled from
VAST's repository.** §11.4 established it is worth only 0.022 points as a
rasterised-against-analytic choice, so this is a small residual ignorance, but
it is ignorance and not a result.

## 12.6 What is now open

One thing, and it is a decision rather than a measurement.
`verify/wp4_void_fraction.py` has a sourced defect worth 0.71 points, and its
numbers are quoted in §3, §5, §6, §10.3, §10.4, §11 and two `explain/`
write-ups. **Nothing in that file was altered.** Its 14 checks and its output
stand as committed so that every finding quoting them stays resolvable, a
correction notice was appended to its docstring, and this section carries the
corrected numbers. Whether the script should instead be corrected in place, and
every dependent number updated, is **`OPEN-QUESTIONS.md` Q-4**, with the
reversible default being what was done here.
