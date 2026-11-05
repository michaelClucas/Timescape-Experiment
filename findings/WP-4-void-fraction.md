# WP-4: is `f_v0` measuring what it claims?

**Status:** complete for what this dataset can settle. One part deliberately
not done and named in §7.
**Provisional on WP-0.** Run 02 has not run.
**Evidence:** `verify/wp4_inspect_inputs.py`, `verify/wp4_void_fraction.py`
(14/14), `verify/wp4_fv0_comparison.py` (11/11).
**Dataset:** VAST SDSS DR7 void catalogues v1.3.1,
`doi:10.5281/zenodo.11043278`, provenance in `data/001-sdss-dr7-voids/`.
**Kill criterion tested:** K5. **It does not fire, and it cannot fire on this
dataset.** §6.

**The short version.** The measured void fraction does not exclude the fitted
`f_v0`, so K5 does not fire. But WP-4's "counts against" clause has a second
limb, that the fitted spread is irreducible, and that limb holds decisively.
`f_v0` is not excluded by measurement; it is **unconstrained by measurement**,
and the model's own fits disagree with each other about it at nine times the
scatter their error bars allow. Objection O4 hardens, through the second limb
rather than the first.

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

## 6. Does K5 fire? No, and it cannot

K5: "WP-4 finds the measured void fraction excludes **every** fitted `f_v0`."

The measured interval across every verified variant is 0.448 to 0.626. Two
fitted values lie inside it: 0.550 and 0.557, the two CMB matching
prescriptions of arXiv:1410.3470 Table 2. So the condition "excludes every
fitted value" is not met and **K5 does not fire**.

It also could not have fired, for three independent reasons:

1. The measured quantity is a **lower bound** on `f_v0`, not an estimate (§4).
   A lower bound of 0.626 does not exclude a fitted 0.791; it is consistent
   with it.
2. The dominant systematic, the edge treatment at 17.5 points, is comparable
   to the entire fitted spread of 24 points. A measurement whose own
   systematic is most of the range in dispute cannot exclude anything in it.
3. K5's wording relies on an algorithm spread that this dataset cannot
   independently establish (§3).

**The branch does not stop.** `T13`'s evidential weight does not collapse by
this route.

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
