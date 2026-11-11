# WP-6: does the two-phase split survive refinement?

**Status:** complete for the refinement that can be computed from the model's
own ingredients. One extension is ours, not the literature's, and is named in
§5.
**Provisional on WP-0.** Run 02 has not run.
**Evidence:** `maple/results/003-void-matter-refinement/` (SymPy job; JOB.md
pre-registered at `2ed08ff` before `job.py` ran),
`verify/void_matter_sensitivity.py` (13/13, shares no code with the job),
`verify/maple_job_design_checks.py` (10/10, for §1).
**Kill criterion tested:** K4. **It does not fire.** §4.

**The short version.** Splitting the voids into phases with different
curvatures changes **nothing**, exactly: empty voids expand the same way
whatever their curvature constant. The refinement the model *is* sensitive to
is the one Run 01's T6 named second, density. Timescape's tracker requires
the voids to hold **no** matter. Real voids hold some. Let `M_v` be the share
of all matter that sits in the void phase. Then:

| `M_v` | `q_min` | shift | sign change at `f_v` | dressed `q` at `f_v = 0.695` |
|---|---|---|---|---|
| 0 (tracker) | -0.0430 | 0 | 0.587 | -0.036 |
| 0.0265 | | **0.004**, the published `q_0` uncertainty | | |
| 0.0695 (`delta_v = -0.90`) | -0.0342 | 0.0088 | 0.680 | -0.0066 |
| **0.0852** | | | | **0** |
| 0.270 | | **0.0215**, K4's threshold | | |

Pan et al. (arXiv:1103.4156) report that voids filling 62% of the SDSS DR7
volume contain about 7% of its bright galaxies `[LEAD]`, so `M_v ≈ 0.07` is
the right order. At that value:
- `q_min` moves by twice the published `q_0` uncertainty but by under half of
  K4's threshold;
- the void fraction at which apparent acceleration begins moves from 0.587
  to about 0.68;
- the dressed `q` at the model's own fitted `f_v0 = 0.695` goes from -0.036
  to -0.0066.

Present-day acceleration at the fitted `f_v0` disappears once voids hold more
than 8.5% of the matter.

---

## 1. Why job 001 could not answer this

`verify/maple_job_design_checks.py` shows that queued Maple job 001 has two
problems:
- **As written it cannot run.** `Omk_two` ends in `* fv / fv` and drops the
  factor `f_v`, so the root-find inside `q_two` has no solution for any
  `f_v` in (0, 1). This is D0.
- **With that factor restored, it is blind by construction.** `q_two(f_v, s)`
  is the published Eq. (26) evaluated at a re-mapped `f_v`. Re-mapping the
  argument of a function cannot change its minimum value, so
  `q_min(s) = q_min(0)` to 1e-10 for every `s`. This is D1. The job would
  have reported "`T6` is not load-bearing" whatever the physics.

Its JOB.md flagged the substitution as its weakest step, but expected it to
be merely crude. In fact the substitution removes exactly the quantity the
job set out to measure.

## 2. The machinery, and its control

`[COMPUTED]` job 003, item 1. The two phases are separately Friedmann in
volume-average time: flat walls holding matter, and negatively curved voids.
That is T6 together with "no backreaction within walls and within voids
separately", `[SOURCED]` arXiv:0909.0749 Sec. II as quoted in Run 01 T6. The
dressing uses the wall lapse of arXiv:0709.0732 Eq. (7). For empty voids, the
dressed `q` derived from these alone, symbolically, is **identical** to the
published Eq. (26): the residual is `0`. The derivation also yields
`gamma_bar = 1 + f_v/2` and the dressed-to-bare relation
`H/Hbar = (4f^2 + f + 4)/(2(2 + f))`, which `findings/WP-1-comparability.md`
uses independently. So the extension in §3-§4 is built on ingredients that
reproduce the published model exactly where the two overlap.

## 3. Curvature splitting is null, exactly

`[COMPUTED]` job 003, item 2. Take two empty void phases with arbitrary
curvature constants `k_1` and `k_2`. Both residuals, against Eq. (26) and
against the tracker's `Omega_k_bar`, are `0`. The reason is plain. An empty
region with negative curvature expands as `a ∝ t` (Milne) whatever the size
of its curvature constant, so two such regions have the same expansion rate
at every moment and act as one. The curvature constant only sets how a
region's scale factor is normalised. Job 001's question ("does a spread in
void curvature move the predictions?") has the answer **no, by an identity**,
and that counts *for* the model in the sense Run 01 meant.

## 4. Matter in the voids, and K4

`[COMPUTED]` job 003, items 3-5; `[CHECKED]` by `verify/void_matter_sensitivity.py`.

**One parameter, and it is measurable.** Each phase conserves its own matter.
At early times both phases have the same density, so the void phase's share
of all matter, `M_v`, is fixed from the start. At every later epoch
`1 + delta_v = M_v / f_v`, which holds to 1e-15. The family of non-empty
models therefore has exactly one parameter: job 003's scaling check gives a
residual of 1.2e-14. The tracker is `M_v = 0`. A rescaling would leave
`M_v` and `delta_v` related as above, so labelling by either is equivalent.

**The numbers are in the table above.** The `q` curve moves in a consistent
direction as voids hold more matter. The minimum becomes shallower, it occurs
later (at `f_v` 0.775, then 0.832 at `M_v = 0.07`), and the onset of apparent
acceleration moves to larger `f_v`.

**K4 does not fire.** K4 requires `q_min` to move by more than 0.0215, half
the effect. That needs `M_v ≈ 0.27`, with voids holding more than a quarter
of all matter at `delta_v ≈ -0.61`. The only void-content figure in this
repository, Pan et al.'s 7% of galaxies, is about a factor of four below
that. `[INFERENCE]`, premise named: the galaxy share is within a factor of a
few of the matter share.

**But T6 is load-bearing at a level the published uncertainties do not
show.** At `M_v ≈ 0.07`:
- **`q_min` moves by 0.0088.** The published `q_0` uncertainty is
  `+0.004/-0.000` (arXiv:1706.07236, via job 001's JOB.md), so the shift is
  twice that.
- **The onset of acceleration moves by 0.094 in `f_v`.** The published
  `f_v0` uncertainty is `+0.041/-0.051` (Run 01, T13), so this is about twice
  that as well.
- **The dressed `q` at the fitted `f_v0 = 0.695` drops from -0.036 to
  -0.0066.**

This is not a refit. A fit uses distances, not `q`, and refitting is WP-2,
which is out of scope. So none of these numbers is a corrected `f_v0`.
`[INFERENCE]`: they say that the published `f_v0` and `q_0`, with their
quoted errors, are conditional on `M_v = 0`. That condition is not among the
error budgets this repository has seen.

## 5. The weakest point, and what would settle it

**The extension is ours.** No timescape paper retrieved here computes
non-empty voids. A timescape author has a reasonable reply: the void phase
is *defined* as the empty part, and occupied underdense regions count as
wall. That reply is coherent but not free. It lowers the void volume
fraction the model must be compared with, and WP-4 already finds the
measured fraction (0.6228 on `main`; 0.6157 after the mask-index correction
on the unmerged PR #14) to be only a lower bound on `f_v0`. PR #14 also finds
that whether `A(H̄_dec) = 0.627` survives that bound depends on a one-pixel
mask convention. Under the reply, VoidFinder's voids would
overcount the void phase, and the lower bound would stop binding. So the
reply trades WP-6's sensitivity for WP-4's.

**What settles it is a number this repository can get: `M_v` for the same
VoidFinder voids WP-4 measured.** That means galaxy membership in the
`*_comoving_holes.txt` spheres, which needs the NSA galaxy positions. Those
are not in `data/001-sdss-dr7-voids/`, which holds only NSA IDs via the V2
membership files. V2's voids fill 90.8% of the volume (REVOLVER, WP-4) and do
not correspond to the void phase, so they cannot substitute. The step is
tractable and is the natural next cycle of WP-6.

A galaxy count measures galaxies, not matter. `[INFERENCE]`, premise named:
galaxy formation is suppressed in low-density regions, so the void share of
bright galaxies is more likely to understate the matter share than to
overstate it. If that premise holds, `M_v ≈ 0.07` is closer to a floor than
a ceiling, and the 0.0852 threshold sits 1.5 points above it.

---

## 6. Prior art (appended 2026-11-11)

A subagent literature search covered about 12 queries over arXiv, search
engines and ar5iv full texts. It did **not** run a direct NASA ADS full-text
query, and its quotes passed through a summariser, so every quote below is
`[LEAD]` until checked character by character against the source.

- **Already known.**
  - The tracker is "the walls expanding as an Einstein–de Sitter model … the
    voids as an empty Milne universe" (arXiv:1311.3787 Sec. 5.2). §2's
    control is therefore a consistency check, not a result.
  - The local Hubble extremes are `Hbar0` and `Hbar0 / h_r`
    (arXiv:1311.3787 Sec. 5.3; arXiv:1306.3208 fn. 7). This is cited, not
    claimed as new, in `findings/WP-8-prediction-spec.md` §1.
- **Formula known, characterisation not found.** `Omega_k_bar ≃
  9 f_v/(2+f_v)^2` appears in arXiv:1306.3208 App. A. The statement that it
  holds **iff** `Omega_k_v = 1` (WP-5 I2) was not found.
- **Not found anywhere.**
  - Timescape's lapse and dressing applied to voids that contain matter.
  - Any parametrisation of the model by the void mass fraction `M_v`.
  - Any computation of dressed `q` against void content, or a sign crossing
    near `M_v ≈ 0.085`.
  - Any sensitivity analysis of the two-phase ansatz.
- **Closest work.**
  - Wiegand & Buchert, arXiv:1002.3912: matter in the underdense region of a
    two-scale Buchert model, with no lapse.
  - Räsänen, astro-ph/0607626: varies void emptiness qualitatively, with no
    dressing.
  - Mattsson & Mattsson, arXiv:1012.4008: non-empty LTB voids, not
    timescape.
- **The tension this work addresses.**
  - Wiltshire's own lecture notes give voids `delta = -0.94 ± 0.02`
    (arXiv:1311.3787) while the phenomenology uses empty voids.
  - Galoppo & Mourier (arXiv:2511.17160) describe voids as "dust-sourced"
    but use the tracker.

**Before any novelty claim is made publicly, an ADS full-text query is
required**, e.g.
`full:"timescape" AND full:("void density" OR "non-empty voids")`.

---

## 7. The measured void matter share (appended 2026-11-11)

**Evidence:**
- `verify/wp6_void_galaxy_share.py` (6/6), using dataset 002 with cuts
  pre-registered at `78fa7a3` and cut 5a appended;
- `verify/wp6_bias_mapping.py` (5/5).

**Galaxy share, measured.** The sample is the `M_r < -20` volume-limited
SDSS DR7 sample (194,124 galaxies, `z < 0.114`), and the voids are the same
VoidFinder voids WP-4 measured at `f_v = 0.6228`. **6.09%** of the galaxies
lie strictly inside them (`delta_g = -0.902`). The figure is stable to 0.0005
across Planck 2018 / WMAP5 and both mask conventions, and flat to within
0.0006 as the interior margin goes from 1e-3 to 1e-1 h^-1 Mpc.

The registered cut 5 (`<= R`) gives 17.2%. That reproduces VAST's own
"~18% of the galaxies" (arXiv:2202.01226 Sec. 3.2), but only by counting the
hole-bounding galaxies. VAST's Sec. 2.1 identifies those as **wall**
galaxies: a sphere "is grown … until it is bounded by four galaxies", and
growth "explicitly stops once wall galaxies are encountered". So 6.09% is
the interior figure and 17.2% is an upper bracket. The interior figure
agrees with Pan et al. (7%, `[LEAD]`) and with Hoyle & Vogeley's galaxy
contrasts of -0.92 to -0.96.

**Matter share, under a sourced bias.** Zehavi et al. 2011 (arXiv:1005.2413,
ApJ 736, 59, HOD threshold table) give, for `M_r < -20`,
"`b_g × (σ8/0.8)` = 1.20 ± 0.01". At Planck's σ8 = 0.811 that is
`b = 1.184`.

With linear bias inside voids, `delta_m = delta_g / b`:
- **`M_v = 0.148`** at `b = 1.184`.
- The neighbouring thresholds bracket it: 0.130 at `b = 1.14` and 0.187 at
  `b = 1.29`.

Pollina et al. 2017 (arXiv:1610.06176, MNRAS 469, 787) find that the
tracer-matter relation around voids "is always linear", with a slope above
the large-scale bias for small voids. That points **higher**, not lower.
Benson et al. 2003 (astro-ph/0208257) find galaxies in voids more
underdense than the dark matter. The quotes and the subagent's verbatim
sources are in this repository's session record, so they are `[LEAD]` until
re-read.

**Named premise: linear bias holds at `delta_g ≈ -0.9`.** Pollina 2017's
text claims validity "for arbitrarily small values of r, as long as large
enough voids are considered", but warns that Poisson noise rises near void
centres. Whether the relation holds at this contrast is not shown in its
text. No source gives the matter share inside VoidFinder voids directly. That
would need VoidFinder run on an `M_r < -20` HOD mock, with the dark matter
counted inside the voids.

**What it does to the model** (job 003's model, figures from
`verify/wp6_bias_mapping.py`):

| inputs | `M_v` | `q_min` | share of the effect lost | `q` at `f_v0 = 0.695` | acceleration begins at `f_v` |
|---|---|---|---|---|---|
| empty voids (tracker) | 0 | -0.0430 | 0 | -0.036 | 0.587 |
| interior, no bias | 0.061 | -0.0351 | 18% | -0.010 | 0.672 |
| **interior, `b = 1.184`** | **0.148** | **-0.0280** | **35%** | **+0.027** | **0.745** |
| interior, `b = 1.29` | 0.187 | -0.0256 | 40% | +0.046 | 0.771 |
| surface-inclusive, `b = 1.184` | 0.242 | -0.0228 | 47% | +0.074 | 0.803 |

**K4.** K4 requires more than half the effect lost, which needs `M_v >
0.270`.
- With the interior share it needs `b > 1.59`. The sourced bias is 1.18-1.29,
  so **K4 does not fire**.
- With the surface-inclusive share it needs `b > 1.28`. That falls between
  Zehavi's `M_r < -20` and `-20.5` values, so under the upper-bracket
  convention K4 is **marginal**.

**What this establishes, at the strength the premises allow.** The empty-void
assumption behind every published timescape number is not a harmless
idealisation. At the void matter share that the measured galaxy content and
the measured galaxy bias imply:
- **The deepest apparent acceleration the model can produce is about a third
  weaker.**
- **Apparent acceleration starts only once voids fill 74.5% of the volume.**
  Every published fitted `f_v0` from 0.550 to 0.695 lies below that, so each
  describes a universe that would appear to be decelerating today. Run 01
  T13 lists those fits.
- **The model has to be refitted.** That is WP-2-class work, out of this
  loop's scope. Whether a refit, now required to reach `f_v0 ≳ 0.75`,
  still fits supernovae, and stays consistent with WP-4's measured void
  fraction (a lower bound of 0.62), is the question this result hands on.

**This is not the reformulation stop condition.** K4 is applied exactly as
written and does not fire. The finding reports a large sensitivity below the
kill threshold, which is what the plan's "counts against" limb for WP-6
describes, short of a kill.
