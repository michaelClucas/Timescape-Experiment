#!/usr/bin/env python3
"""WP-4d: VAST's own mask convention, read from VAST's source, applied here.

    .venv/Scripts/python verify/wp4_vast_mask_convention.py

Exits 0 if every check passes, 1 otherwise. Takes a few minutes.

## What this closes

`verify/wp4_mask_resolution.py` established that the survey mask's footprint
convention is worth +-1.5 points on the measured void volume fraction, and that
whether arXiv:1410.3470 Table 2's `A(H_bar_dec)` fit at `f_v0 = 0.627` is
excluded by the measured lower bound turns on it. It left the convention itself
as a `[LEAD]`, because [DVB23]'s mask code had not been read.

**It has now been read.** The convention is `[SOURCED]` below, and it differs
from the one `verify/wp4_void_fraction.py` uses.

## The source, with locators

VAST (Void Analysis Software Toolkit), the software that produced both the
catalogues and the mask pickle in `data/raw/001-sdss-dr7-voids`, is public at
`github.com/DESI-UR/VAST`. Read at commit `24e66e1`, the repository head on
2026-11-05. Every claim below was also checked at commit `133cfcf`
(2022-02-10), which is contemporaneous with [DVB23]'s submission, and is
**unchanged between the two**.

**The mask is built** in `python/vast/voidfinder/multizmask.py`. With
`dec_offset = -90` at line 15, `generate_mask` scales the galaxy angles and
truncates (line 166):

    scaled_converted_ang = (mask_resolution*ang).astype(int)

and then sets, for each unique scaled pair (line 192):

    mask[row[0], row[1] - mask_resolution*dec_offset] = True

**The mask is read** in `python/vast/voidfinder/voidfinder_functions.py`, where
`not_in_mask` ends (line 249):

    return not survey_mask_ra_dec[int(n*ra), int(n*dec) - n*dec_offset]

So in both places the declination index is

    int(n * dec) + 90 * n

and `.astype(int)` and `int()` both truncate **toward zero**. VAST is
internally consistent: the array is built and read with the same expression.

**`verify/wp4_void_fraction.py` uses a different expression.** Its `in_mask`
computes

    ((dec + 90.0) * res).astype(np.int64)

which truncates **downward in declination**, because the offset is applied
before the truncation rather than after.

## Why that is not a cosmetic difference

For `dec >= 0` the two agree: `int(dec) + 90 == int(dec + 90)`.

For `dec < 0` they differ by exactly one pixel, because truncation toward zero
rounds a negative number **up**. At `res = 1`:

    dec = -5.3   VAST: int(-5.3) + 90 = 85     this pipeline: int(84.7) = 84

VAST's pixel 85 covers `dec in (-6, -5]`; this pipeline's pixel 85 covers
`dec in [-5, -4)`. So over the whole southern part of the footprint the two
conventions read the mask one degree apart in declination, and the SDSS DR7
main sample reaches to about `dec = -11`.

**This is a shift, not an erosion or a dilation**, so it is a different
operation from anything `verify/wp4_mask_resolution.py` varied, and it is not
bracketed by that script's erode-dilate pair in any guaranteed way. It is
applied to part of the footprint only.

**Why the existing validation did not catch it.**
`verify/wp4_void_fraction.py` checks the mask convention by confirming that
1.0000 of 1163 VoidFinder void centres fall inside the mask under
`[ra, dec+90]` against 0.1660 under the transposed convention. That test
distinguishes transposed from not. It cannot distinguish a one-pixel
declination shift, because both conventions put essentially every void centre
inside a 9133-pixel footprint. The check was right about what it tested and
silent about this.

## What is varied here, and what is not

Only the declination index. VAST's right-ascension index is `int(n*ra)` on an
RA already folded into `[0, 360)`, which is what this pipeline's
`(ra * res).astype(int)` computes, so RA is already identical.

Two measure-zero differences in VAST's `not_in_mask` are **not** implemented,
and are recorded rather than silently dropped. VAST reconstructs RA with
`arctan` plus a quadrant fix-up whose condition is `coords[0] < 0 and
coords[1] != 0`, so a point on the negative x-axis exactly gets `ra = 0`
instead of 180; and VAST returns "outside" for `r == 0` exactly. Each affects
a set of grid cells of measure zero on a 1 h^-1 Mpc grid (at most a line and a
point), against the ~27 million survey cells, so neither can move a percentage
to three decimals.

## Expectation, stated before running

Rule 6 applies, and the last script in this series had my prediction wrong by a
factor of six. So, stated plainly and in advance: **I do not have a prediction
for the sign.** The shifted band is at `dec < 0`, which is one edge of the
footprint, and whether shifting the lookup into or out of the surveyed region
there raises or lowers `f_v` depends on where the voids happen to sit in that
band. I expect the magnitude to be **smaller than the 3.06-point erode-dilate
span**, because only part of the footprint is affected rather than all of its
boundary, and **larger than 0.05 points**, because the affected band is a real
fraction of the survey. Those two bounds are what the checks test.

## The negative this script also records

**The code that computed [DVB23] Table 6's volume column is not in VAST at the
paper's date.** `python/vast/catalog/void_overlap.py`, which places a 1 h^-1
Mpc grid with `np.arange` and filters it through `MaskChecker.not_in_mask`, and
`python/vast/catalog/void_catalog.py`, whose `get_single_overlap` is
documented "Calculates the void volume fraction of a void catalog", **both
first appear in commit `04233d7`, dated 2025-02-06** - three years after
[DVB23] was submitted. At `133cfcf` the repository contains no grid-based
volume-fraction code at all.

That module also defaults to `edge_buffer=30`, cutting grid points within
30 h^-1 Mpc of the survey border out of **both** numerator and denominator,
which is a far larger intervention than anything considered here. Whatever
produced Table 6, it was not that code.

**So the denominator convention remains `[UNKNOWN]` and cannot be settled from
this repository.** What is settled is the mask indexing, which is what the
`[LEAD]` in `findings/WP-4-void-fraction.md` §11.6 actually asked about.

Sources:

  [VAST]  github.com/DESI-UR/VAST, read at commit 24e66e1 and checked at
          133cfcf (2022-02-10). Files and lines cited above.
  [DVB23] Douglass, Veyrat & BenZvi, arXiv:2202.01226, ApJS 265, 7 (2023).
  [NW15]  Nazer & Wiltshire, arXiv:1410.3470, Phys. Rev. D 91, 063519 (2015),
          Table 2.
  Dataset: doi:10.5281/zenodo.11043278, version 1.3.1.
"""

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import wp4_void_fraction as vf        # noqa: E402

Z_MAX = vf.Z_MAX
OMEGA_M = vf.OMEGA_M

# findings/WP-4-void-fraction.md §3 and §11.2, from wp4_void_fraction.py and
# wp4_mask_resolution.py at 266c701.
BASELINE = {"Planck2018": 62.280, "WMAP5": 62.628}
PUBLISHED = {"Planck2018": 60.8, "WMAP5": 61.1}
ERODED = {"Planck2018": 63.517, "WMAP5": 63.853}
DILATED = {"Planck2018": 60.446, "WMAP5": 60.794}

NW15 = {"A(H_bar_dec)": 0.627, "W(k = 0)": 0.550, "W(k != 0)": 0.557}

DEC_OFFSET = -90      # [VAST] multizmask.py line 15, voidfinder_functions.py line 21

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((bool(ok), name, detail))


def close(name, got, want, tol, detail=""):
    CHECKS.append((abs(got - want) <= tol, name,
                   "got %.4g, want %.4g +/- %.3g. %s" % (got, want, tol, detail)))


def in_mask_vast(mask, res, ra, dec):
    """[VAST]'s own index expression: int(n*dec) - n*dec_offset.

    Truncation toward zero, applied after scaling and before the offset, which
    is what `int()` in voidfinder_functions.py line 249 and `.astype(int)` in
    multizmask.py line 166 both do. Contrast vf.in_mask, which offsets first.
    """
    i = np.clip((ra * res).astype(np.int64), 0, mask.shape[0] - 1)
    j = np.clip((dec * res).astype(np.int64) - int(res * DEC_OFFSET),
                0, mask.shape[1] - 1)
    return mask[i, j]


def main():
    print("=" * 78)
    print("WP-4d: [VAST]'s own mask index convention, applied to this pipeline")
    print("=" * 78)
    print("EVERY FRACTION BELOW IS LCDM-CONDITIONED, per cut 8. The numerator")
    print("is the VoidFinder edge-included sphere union throughout.")
    print()

    mask, res, r_min, r_pickle = vf.load_mask()
    r_of = {c: vf.comoving_distance(Z_MAX, OMEGA_M[c]) for c in OMEGA_M}

    # --- the two conventions, on the declination axis alone -----------------
    print("-" * 78)
    print("THE TWO INDEX EXPRESSIONS, on a declination grid")
    print("-" * 78)
    print("  %8s %12s %12s %6s" % ("dec", "this pipeline", "[VAST]", "same?"))
    disagree_demo = 0
    for dec in (-11.0, -10.5, -5.3, -0.4, 0.0, 0.4, 5.3, 40.7, 70.0):
        a = int((dec + 90.0) * res)
        b = int(dec * res) - int(res * DEC_OFFSET)
        if a != b:
            disagree_demo += 1
        print("  %8.1f %12d %12d %6s" % (dec, a, b, "yes" if a == b else "NO"))
    check("the two conventions agree for dec >= 0 and differ for dec < 0",
          disagree_demo > 0
          and all(int((d + 90.0) * res) == int(d * res) - int(res * DEC_OFFSET)
                  for d in (0.0, 0.4, 5.3, 40.7, 70.0))
          and all(int((d + 90.0) * res) != int(d * res) - int(res * DEC_OFFSET)
                  for d in (-10.5, -5.3, -0.4)),
          "truncation toward zero rounds a negative declination up, so the "
          "offset-after form reads one pixel north of the offset-before form "
          "wherever dec < 0 and is not an integer")
    print()

    # How much of the footprint is affected at all. The southern rows are the
    # only ones where the conventions differ, so if the survey had no southern
    # sky this whole question would be empty; it is checked, not assumed.
    south = mask[:, :90].sum()
    print("mask pixels set: %d total, %d at dec < 0 (%.1f%%)"
          % (mask.sum(), south, 100.0 * south / mask.sum()))
    check("a real part of the footprint lies at dec < 0",
          south > 0.02 * mask.sum(),
          "%d of %d set pixels (%.1f%%) are southern, so the convention "
          "difference acts on a real fraction of the survey rather than on a "
          "corner of it" % (south, mask.sum(), 100.0 * south / mask.sum()))
    print()

    # --- recompute ----------------------------------------------------------
    results = {}
    for cosmo in ("Planck2018", "WMAP5"):
        r_max = r_of[cosmo]
        print("-" * 78)
        print("COSMOLOGY: %s   r_max = %.3f h^-1 Mpc   grid = 1.0"
              % (cosmo, r_max))
        print("-" * 78)
        vf.GRID = 1.0
        axes = vf.grid_box(mask, res, r_max)
        holes = vf.read_table(os.path.join(
            vf.RAW, "VoidFinder-nsa_v1_0_1_%s_comoving_holes.txt" % cosmo))
        union = vf.rasterise_union(axes, holes["x"], holes["y"], holes["z"],
                                   holes["radius"])

        row = {}
        for label, fn in (("this pipeline", vf.in_mask),
                          ("[VAST] convention", in_mask_vast)):
            saved = vf.in_mask
            vf.in_mask = fn        # survey_cells calls the module-level name
            try:
                surv, n_survey = vf.survey_cells(mask, res, axes, r_min, r_max)
                n_void = vf.count_in(union, surv)
            finally:
                vf.in_mask = saved
            row[label] = {"f_v": 100.0 * n_void / n_survey,
                          "n_survey": n_survey, "n_void": n_void}
            print("  %-20s f_v = %7.3f %%   survey cells %d"
                  % (label, row[label]["f_v"], n_survey))
        results[cosmo] = row

        d = row["[VAST] convention"]["f_v"] - row["this pipeline"]["f_v"]
        dn = (row["[VAST] convention"]["n_survey"]
              - row["this pipeline"]["n_survey"])
        print("  shift: %+.3f points on f_v, %+d survey cells (%+.3f%%)"
              % (d, dn, 100.0 * dn / row["this pipeline"]["n_survey"]))
        print("  vs published %.1f : this pipeline %+.3f, [VAST] %+.3f"
              % (PUBLISHED[cosmo],
                 row["this pipeline"]["f_v"] - PUBLISHED[cosmo],
                 row["[VAST] convention"]["f_v"] - PUBLISHED[cosmo]))
        print()

        close("%s baseline still reproduces the committed pipeline" % cosmo,
              row["this pipeline"]["f_v"], BASELINE[cosmo], 0.01,
              "if this fails, nothing below is about the same quantity")

    # --- the size of the effect --------------------------------------------
    print("=" * 78)
    print("THE SIZE OF THE EFFECT, against the bounds stated in advance")
    print("=" * 78)
    shifts = {c: results[c]["[VAST] convention"]["f_v"]
              - results[c]["this pipeline"]["f_v"] for c in results}
    span = {c: ERODED[c] - DILATED[c] for c in results}
    for c in sorted(results):
        print("  %-11s convention shift %+.3f points; erode-dilate span %.3f"
              % (c, shifts[c], span[c]))
    worst = max(abs(v) for v in shifts.values())
    check("the shift is smaller than the erode-dilate span, as predicted",
          worst < min(span.values()),
          "largest shift %.3f points against the narrowest span %.3f. Only "
          "part of the footprint is affected, so this was the expected "
          "ordering" % (worst, min(span.values())))
    check("and it is larger than 0.05 points, as predicted",
          worst > 0.05,
          "largest shift %.3f points, so the convention difference is not "
          "negligible and the measured fraction does depend on which of the "
          "two expressions is used" % worst)
    check("the shift has the same sign in both cosmologies",
          len({np.sign(v) for v in shifts.values()}) == 1,
          "shifts %+.3f (Planck2018) and %+.3f (WMAP5). A systematic that "
          "flipped sign between two nearly identical survey depths would "
          "indicate noise rather than a convention"
          % (shifts["Planck2018"], shifts["WMAP5"]))

    # --- which convention is the right one to use here ---------------------
    print()
    print("=" * 78)
    print("WHICH EXPRESSION THIS PIPELINE SHOULD USE")
    print("=" * 78)
    print("  The mask pickle in data/raw/ was WRITTEN by [VAST]'s")
    print("  generate_mask, using int(n*dec) - n*dec_offset (multizmask.py")
    print("  line 166 and 192). An array must be read with the convention it")
    print("  was written with, so [VAST]'s is correct for this file and this")
    print("  pipeline's offset-before form is a defect, not a variant.")
    print()
    check("the [VAST] convention is the one the stored array was written with",
          True,
          "multizmask.py builds the array at [int(n*ra), int(n*dec) - "
          "n*dec_offset] and voidfinder_functions.py reads it at the same "
          "index; both are unchanged between 133cfcf (2022-02-10) and "
          "24e66e1. [SOURCED]. So the corrected measured fraction is the "
          "[VAST]-convention row, and this pipeline's committed numbers carry "
          "a %.3f-point indexing defect" % worst)

    # --- what it does to the exclusion -------------------------------------
    print("=" * 78)
    print("WHAT IT DOES TO THE EXCLUSION (finding 10.3, 10.4, 11.5)")
    print("=" * 78)
    corrected = results["Planck2018"]["[VAST] convention"]["f_v"] / 100.0
    committed = results["Planck2018"]["this pipeline"]["f_v"] / 100.0
    # The mask-resolution systematic is a property of the 1-degree pixelation
    # and survives the index correction, so it is re-applied about the
    # corrected centre rather than discarded.
    half = 0.5 * span["Planck2018"] / 100.0
    cons = corrected - half
    aggr = corrected + half
    print("  Planck2018 edge-included bound on f_v0:")
    print("    as committed (offset-before index)   %.4f" % committed)
    print("    corrected ([VAST] index)             %.4f" % corrected)
    print("    corrected, less half the +-1 px span %.4f  <- conservative"
          % cons)
    print("    corrected, plus half that span       %.4f  <- aggressive"
          % aggr)
    print()
    print("  %-14s %7s %14s %14s %14s"
          % ("[NW15] prescr.", "f_v0", "vs corrected", "vs conserv.",
             "vs aggr."))
    for name, f in sorted(NW15.items(), key=lambda kv: -kv[1]):
        cells = []
        for b in (corrected, cons, aggr):
            cells.append("excluded" if f < b else "+%.4f" % (f - b))
        print("  %-14s %7.3f %14s %14s %14s"
              % (name, f, cells[0], cells[1], cells[2]))

    low_two = [f for n, f in NW15.items() if n != "A(H_bar_dec)"]
    check("0.550 and 0.557 remain excluded under the corrected index",
          all(f < cons for f in low_two),
          "both lie below even the conservative corrected bound of %.4f, by "
          "%.4f and %.4f. The exclusion of two of [NW15]'s three "
          "prescriptions has now survived the edge treatment, the one-pixel "
          "footprint bracket and an index correction, and is the most robust "
          "thing WP-4 has" % (cons, cons - 0.550, cons - 0.557))
    settled = (0.627 < cons) or (0.627 > aggr)
    check("whether 0.627 is excluded is STILL not settled by this",
          not settled,
          "0.627 sits between the conservative %.4f and aggressive %.4f "
          "corrected bounds, so the index correction moves the centre without "
          "resolving the question. The +-1 px pixelation systematic of "
          "wp4_mask_resolution.py is independent of the index expression and "
          "survives it, and it is the term that straddles 0.627" % (cons, aggr))
    print()
    print("  So the [LEAD] in findings/WP-4-void-fraction.md 11.6 is closed in")
    print("  the sense it was asked - the convention is now [SOURCED] - and")
    print("  the question it was asked IN ORDER to settle is not. Reading the")
    print("  code found a defect worth %.3f points and left the %.2f-point"
          % (worst, span["Planck2018"]))
    print("  pixelation systematic exactly where it was.")

    print()
    width = max(len(c[1]) for c in CHECKS)
    failed = 0
    for ok, name, detail in CHECKS:
        if not ok:
            failed += 1
        print("%s  %-*s %s" % ("PASS" if ok else "FAIL", width, name, detail))
    print()
    if failed:
        print("FAIL: %d of %d checks failed. No number here is quotable."
              % (failed, len(CHECKS)))
        return 1
    print("PASS: %d of %d checks." % (len(CHECKS), len(CHECKS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
