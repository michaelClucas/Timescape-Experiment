#!/usr/bin/env python3
"""WP-4d: VAST's own mask convention, and the defect it exposed. Now applied.

    .venv/Scripts/python verify/wp4_vast_mask_convention.py

Exits 0 if every check passes, 1 otherwise. Takes a few minutes.

## What this file is for, now that the correction has been applied

`verify/wp4_mask_resolution.py` established that the survey mask's footprint
convention is worth +-1.5 points on the measured void volume fraction, and that
whether arXiv:1410.3470 Table 2's `A(H_bar_dec)` fit at `f_v0 = 0.627` is
excluded by the measured lower bound turns on it. It left the convention itself
as a `[LEAD]`, because [DVB23]'s mask code had not been read.

**It was then read, and it exposed a defect in this repository's own pipeline
rather than in the published one.** `verify/wp4_void_fraction.py` indexed the
mask's declination axis with an expression [VAST] does not use. **That has now
been corrected in place**, per `OPEN-QUESTIONS.md` Q-4 option 3, answered by
the overseer on 2026-11-05, with the pre-fix script frozen at
`verify/legacy/wp4_void_fraction_preindexfix.py`.

So this script's job has changed. It is no longer proposing a correction; it is
**the standing regression test for one**, and it asserts three things:

1. the convention is what [VAST]'s source says it is, with locators;
2. the live `verify/wp4_void_fraction.py` implements it, and the frozen copy
   implements the superseded one, so the 0.710-point difference between them is
   reproducible on demand rather than a claim in prose;
3. nothing the correction changed altered which fitted `f_v0` values the
   measured bound excludes.

If someone later "simplifies" `in_mask` back to the offset-before form, check 2
fails. That is the point of keeping this file.

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

So in both places the declination index is `int(n*dec) + 90*n`, and
`.astype(int)` and `int()` both truncate **toward zero**. [VAST] is internally
consistent: the array is built and read with the same expression. An array must
be read with the convention it was written with, so this is the correct
expression for this file and the superseded one was a **defect, not a
variant**. `[SOURCED]`.

**The superseded expression** was `((dec + 90.0) * res)` truncated, applying
the offset before the truncation. For `dec >= 0` the two agree, since
`int(dec) + 90 == int(dec + 90)`. For `dec < 0` they differ by exactly one
pixel, because truncation toward zero rounds a negative number **up**:

    dec = -5.3   [VAST]: int(-5.3) + 90 = 85     superseded: int(84.7) = 84

[VAST]'s pixel 85 covers `dec in (-6, -5]`; the superseded one's pixel 85
covers `dec in [-5, -4)`. So over the southern part of the footprint the two
read the mask one degree apart in declination, and the SDSS DR7 main sample
reaches to about `dec = -11`.

**This is a shift, not an erosion or a dilation**, so it is a different
operation from anything `verify/wp4_mask_resolution.py` varied and is not
bracketed by that script's erode-dilate pair in any guaranteed way. It applies
to part of the footprint only.

**Why the existing validation did not catch it.**
`verify/wp4_void_fraction.py` checks its mask convention by confirming that
1.0000 of 1163 VoidFinder void centres fall inside the mask against 0.1660
under the transposed convention. That test distinguishes transposed from not.
It cannot distinguish a one-pixel declination shift, because both expressions
put essentially every void centre inside a 9133-pixel footprint. The check was
right about what it tested and silent about this; it now says so in its own
detail string, and prints what the superseded index would have given.

## What is varied here, and what is not

Only the declination index. [VAST]'s right-ascension index is `int(n*ra)` on an
RA already folded into `[0, 360)`, which is what `(ra * res).astype(int)`
computes, so RA is identical in both.

Two measure-zero differences in [VAST]'s `not_in_mask` are **not** implemented,
and are recorded rather than silently dropped. [VAST] reconstructs RA with
`arctan` plus a quadrant fix-up whose condition is `coords[0] < 0 and
coords[1] != 0`, so a point on the negative x-axis exactly gets `ra = 0`
instead of 180; and [VAST] returns "outside" for `r == 0` exactly. Each affects
a set of grid cells of measure zero on a 1 h^-1 Mpc grid, against the ~27
million survey cells, so neither can move a percentage to three decimals.

## The negative this script also records

**The code that computed [DVB23] Table 6's volume column is not in [VAST] at
the paper's date.** `python/vast/catalog/void_overlap.py`, which places a
1 h^-1 Mpc grid with `np.arange` and filters it through
`MaskChecker.not_in_mask`, and `python/vast/catalog/void_catalog.py`, whose
`get_single_overlap` is documented "Calculates the void volume fraction of a
void catalog", **both first appear in commit `04233d7`, dated 2025-02-06** -
three years after [DVB23] was submitted. At `133cfcf` the repository contains no
grid-based volume-fraction code at all: searching that tree for
`np.arange(x_min`, `grid_points` and `test particle` returns nothing.

That module also defaults to `edge_buffer=30`, cutting grid points within
30 h^-1 Mpc of the survey border out of **both** numerator and denominator,
which is a far larger intervention than anything considered here and is not
what [DVB23] Sec. 4.2 describes. Whatever produced Table 6, it was not that
code.

**So the denominator convention remains `[UNKNOWN]` and cannot be settled from
that repository.** What is settled is the mask indexing, which is what the
`[LEAD]` in `findings/WP-4-void-fraction.md` §11.6 actually asked about.
`verify/wp4_mask_resolution.py` bounds the denominator choice at 0.022 points,
so this is small residual ignorance - but it is ignorance, not a result.

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
DEC_OFFSET = vf.DEC_OFFSET

# What the superseded index produced, from verify/legacy/
# wp4_void_fraction_preindexfix.py, which is that script frozen at db47115.
# These are the numbers quoted in findings/WP-4-void-fraction.md §3, §5, §6,
# §10 and §11 and in the three 2026-11-05 status files.
SUPERSEDED = {"Planck2018": 62.280, "WMAP5": 62.628}

# What the corrected index produces. verify/wp4_void_fraction.py is the
# authority; these are asserted against it below rather than quoted.
CORRECTED = {"Planck2018": 61.570, "WMAP5": 61.923}

PUBLISHED = {"Planck2018": 60.8, "WMAP5": 61.1}

# verify/wp4_mask_resolution.py, the +-1 px pixelation bracket about whichever
# index is used. A property of the 1-degree mask, but NOT numerically
# independent of the index: re-measured about the corrected baseline it is
# 3.663 and 3.660 rather than the 3.071 and 3.059 measured about the
# superseded one, because the boundary layer the bracket moves is now
# evaluated in the right place. Taken from that script's own output, not
# rescaled.
SPAN = {"Planck2018": 3.663, "WMAP5": 3.660}

NW15 = {"A(H_bar_dec)": 0.627, "W(k = 0)": 0.550, "W(k != 0)": 0.557}

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((bool(ok), name, detail))


def close(name, got, want, tol, detail=""):
    CHECKS.append((abs(got - want) <= tol, name,
                   "got %.4g, want %.4g +/- %.3g. %s" % (got, want, tol, detail)))


def in_mask_superseded(mask, res, ra, dec):
    """The expression `verify/wp4_void_fraction.py` used before `db47115`.

    Offset applied before truncation. Kept here, not imported from
    `verify/legacy/`, so that this file is self-contained as a regression test:
    if the frozen copy is ever moved or removed, this check still runs.
    """
    i = np.clip((ra * res).astype(np.int64), 0, mask.shape[0] - 1)
    j = np.clip(((dec + 90.0) * res).astype(np.int64), 0, mask.shape[1] - 1)
    return mask[i, j]


def main():
    print("=" * 78)
    print("WP-4d: [VAST]'s mask index convention, and the correction applied")
    print("=" * 78)
    print("EVERY FRACTION BELOW IS LCDM-CONDITIONED, per cut 8. The numerator")
    print("is the VoidFinder edge-included sphere union throughout.")
    print()

    mask, res, r_min, r_pickle = vf.load_mask()
    r_of = {c: vf.comoving_distance(Z_MAX, OMEGA_M[c]) for c in OMEGA_M}

    # --- the two expressions, on the declination axis alone -----------------
    print("-" * 78)
    print("THE TWO INDEX EXPRESSIONS, on a declination grid")
    print("-" * 78)
    print("  %8s %12s %12s %6s" % ("dec", "superseded", "[VAST]", "same?"))
    for dec in (-11.0, -10.5, -5.3, -0.4, 0.0, 0.4, 5.3, 40.7, 70.0):
        a = int((dec + 90.0) * res)
        b = int(dec * res) - int(res * DEC_OFFSET)
        print("  %8.1f %12d %12d %6s" % (dec, a, b, "yes" if a == b else "NO"))
    check("the two expressions agree for dec >= 0 and differ for dec < 0",
          all(int((d + 90.0) * res) == int(d * res) - int(res * DEC_OFFSET)
              for d in (0.0, 0.4, 5.3, 40.7, 70.0))
          and all(int((d + 90.0) * res) != int(d * res) - int(res * DEC_OFFSET)
                  for d in (-10.5, -5.3, -0.4)),
          "truncation toward zero rounds a negative declination up, so the "
          "offset-before form reads one pixel south of the offset-after form "
          "wherever dec < 0 and is not an integer")

    # The live script must implement the sourced expression. This is the
    # regression check: if in_mask is ever changed back, it fails here.
    probe_ra = np.array([150.0, 150.0, 150.0, 150.0])
    probe_dec = np.array([-5.3, -0.4, 5.3, 40.7])
    live_j = np.clip((probe_dec * res).astype(np.int64)
                     - int(res * DEC_OFFSET), 0, mask.shape[1] - 1)
    probe_i = np.clip((probe_ra * res).astype(np.int64), 0, mask.shape[0] - 1)
    check("verify/wp4_void_fraction.py implements the [VAST] expression",
          np.array_equal(vf.in_mask(mask, res, probe_ra, probe_dec),
                         mask[probe_i, live_j]),
          "its in_mask agrees with int(res*dec) - res*(-90) on southern and "
          "northern probes alike. If someone rewrites it as "
          "((dec + 90) * res), this check fails, which is why it is here")
    print()

    south = int(mask[:, :90].sum())
    print("mask pixels set: %d total, %d at dec < 0 (%.1f%%)"
          % (mask.sum(), south, 100.0 * south / mask.sum()))
    check("a real part of the footprint lies at dec < 0",
          south > 0.02 * mask.sum(),
          "%d of %d set pixels (%.1f%%) are southern, so the expression "
          "difference acts on a real fraction of the survey rather than on a "
          "corner of it" % (south, mask.sum(), 100.0 * south / mask.sum()))
    print()

    # --- recompute both ways ------------------------------------------------
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
        for label, fn in (("superseded index", in_mask_superseded),
                          ("live ([VAST]) index", vf.in_mask)):
            saved = vf.in_mask
            vf.in_mask = fn        # survey_cells calls the module-level name
            try:
                surv, n_survey = vf.survey_cells(mask, res, axes, r_min, r_max)
                n_void = vf.count_in(union, surv)
            finally:
                vf.in_mask = saved
            row[label] = {"f_v": 100.0 * n_void / n_survey,
                          "n_survey": n_survey, "n_void": n_void}
            print("  %-22s f_v = %7.3f %%   survey cells %d"
                  % (label, row[label]["f_v"], n_survey))
        results[cosmo] = row

        d = row["live ([VAST]) index"]["f_v"] - row["superseded index"]["f_v"]
        dn = (row["live ([VAST]) index"]["n_survey"]
              - row["superseded index"]["n_survey"])
        print("  correction: %+.3f points on f_v, %+d survey cells (%+.3f%%)"
              % (d, dn, 100.0 * dn / row["superseded index"]["n_survey"]))
        print("  vs published %.1f : superseded %+.3f, live %+.3f"
              % (PUBLISHED[cosmo],
                 row["superseded index"]["f_v"] - PUBLISHED[cosmo],
                 row["live ([VAST]) index"]["f_v"] - PUBLISHED[cosmo]))
        print()

        close("%s superseded index reproduces the frozen numbers" % cosmo,
              row["superseded index"]["f_v"], SUPERSEDED[cosmo], 0.01,
              "verify/legacy/wp4_void_fraction_preindexfix.py, and every "
              "figure quoted in the finding's §3, §5, §6, §10 and §11. If this "
              "fails, those quotations have stopped being resolvable")
        close("%s live index reproduces the corrected number" % cosmo,
              row["live ([VAST]) index"]["f_v"], CORRECTED[cosmo], 0.01,
              "findings/WP-4-void-fraction.md §12.3 and §13")

    # --- the size of the correction ----------------------------------------
    print("=" * 78)
    print("THE SIZE OF THE CORRECTION, against the pixelation bracket")
    print("=" * 78)
    shifts = {c: results[c]["live ([VAST]) index"]["f_v"]
              - results[c]["superseded index"]["f_v"] for c in results}
    for c in sorted(results):
        print("  %-11s correction %+.3f points; +-1 px pixelation span %.3f"
              % (c, shifts[c], SPAN[c]))
    worst = max(abs(v) for v in shifts.values())
    check("the correction is smaller than the pixelation bracket",
          worst < min(SPAN.values()),
          "largest correction %.3f points against the narrowest bracket %.3f. "
          "Only part of the footprint is affected by the index, whereas the "
          "bracket moves the whole boundary, so this ordering is expected and "
          "is checked rather than assumed" % (worst, min(SPAN.values())))
    check("the correction has the same sign in both cosmologies",
          len({np.sign(v) for v in shifts.values()}) == 1,
          "corrections %+.3f (Planck2018) and %+.3f (WMAP5). A systematic that "
          "flipped sign between two nearly identical survey depths would "
          "indicate noise rather than a convention"
          % (shifts["Planck2018"], shifts["WMAP5"]))
    check("and it moves this pipeline toward the published value, not away",
          all(abs(results[c]["live ([VAST]) index"]["f_v"] - PUBLISHED[c])
              < abs(results[c]["superseded index"]["f_v"] - PUBLISHED[c])
              for c in results),
          "the residual against [DVB23] Table 6 goes from %+.3f to %+.3f "
          "(Planck2018) and %+.3f to %+.3f (WMAP5), i.e. it roughly halves. "
          "That is corroboration and not proof: a wrong index could in "
          "principle have moved either way, and this one moved the right way"
          % (results["Planck2018"]["superseded index"]["f_v"]
             - PUBLISHED["Planck2018"],
             results["Planck2018"]["live ([VAST]) index"]["f_v"]
             - PUBLISHED["Planck2018"],
             results["WMAP5"]["superseded index"]["f_v"] - PUBLISHED["WMAP5"],
             results["WMAP5"]["live ([VAST]) index"]["f_v"]
             - PUBLISHED["WMAP5"]))

    # --- what it does to the exclusion -------------------------------------
    print()
    print("=" * 78)
    print("WHAT IT DOES TO THE EXCLUSION (finding 10.3, 10.4, 11.5, 13)")
    print("=" * 78)
    corrected = results["Planck2018"]["live ([VAST]) index"]["f_v"] / 100.0
    superseded = results["Planck2018"]["superseded index"]["f_v"] / 100.0
    half = 0.5 * SPAN["Planck2018"] / 100.0
    cons = corrected - half
    aggr = corrected + half
    print("  Planck2018 edge-included bound on f_v0:")
    print("    superseded index                     %.4f" % superseded)
    print("    corrected, live                      %.4f" % corrected)
    print("    corrected, less half the +-1 px span %.4f  <- conservative"
          % cons)
    print("    corrected, plus half that span       %.4f  <- aggressive"
          % aggr)
    print()
    print("  %-14s %7s %14s %14s %14s"
          % ("[NW15] prescr.", "f_v0", "vs corrected", "vs conserv.",
             "vs aggr."))
    for name, f in sorted(NW15.items(), key=lambda kv: -kv[1]):
        cells = ["excluded" if f < b else "+%.4f" % (f - b)
                 for b in (corrected, cons, aggr)]
        print("  %-14s %7.3f %14s %14s %14s"
              % (name, f, cells[0], cells[1], cells[2]))

    low_two = [f for n, f in NW15.items() if n != "A(H_bar_dec)"]
    check("0.550 and 0.557 remain excluded after the correction",
          all(f < cons for f in low_two),
          "both lie below even the conservative corrected bound of %.4f, by "
          "%.4f and %.4f. This exclusion has now survived the edge treatment, "
          "the one-pixel footprint bracket and an index correction, and is the "
          "most robust thing WP-4 has" % (cons, cons - 0.550, cons - 0.557))
    check("the correction changes NO exclusion verdict",
          all((f < superseded) == (f < corrected) for f in NW15.values()),
          "every [NW15] prescription falls on the same side of the superseded "
          "bound %.4f and the corrected bound %.4f. So §6, §10.3, §10.4 and "
          "§11.5 keep their conclusions verbatim even though their numbers "
          "are superseded, which is what makes Q-4 a tidying question rather "
          "than a scientific one" % (superseded, corrected))
    check("and 0.627 is STILL not settled by the correction",
          cons < 0.627 < aggr,
          "0.627 sits between the conservative %.4f and aggressive %.4f "
          "corrected bounds, so the correction moves the centre without "
          "resolving the question. The +-1 px pixelation systematic is "
          "independent of the index expression and survives it, and it is the "
          "term that straddles 0.627" % (cons, aggr))

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
