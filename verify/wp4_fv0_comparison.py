#!/usr/bin/env python3
"""WP-4b: the fitted f_v0 against the measured void fraction, and K5.

    .venv/Scripts/python verify/wp4_fv0_comparison.py

Exits 0 if every check passes, 1 otherwise. Runs in under a second.

`verify/wp4_void_fraction.py` computed the measured void volume fraction. This
script does the comparison `data/001-sdss-dr7-voids/SOURCE.md` section 6
insists on: it establishes how far apart the two quantities are before putting
any number next to any other number, assembles the error budget, and evaluates
kill criterion K5.

The headline is in main()'s closing summary and it is not the one the plan
expected. K5 as worded does not fire and cannot fire on this dataset. The
second limb of WP-4's own "counts against" clause - that the fitted spread is
irreducible - does hold, and is demonstrated here from a primary source.

Sources, all fetched and read in full text:

  [LNW08] Leith, Ng & Wiltshire, arXiv:0709.2535, ApJ 672 (2008) L91.
  [SW11]  Smale & Wiltshire, arXiv:1009.5855, MNRAS 413 (2011) 367,
          Sec. 2 (walls are above critical density), Tables 1-3.
  [DNW13] Duley, Nazer & Wiltshire, arXiv:1306.3208, parameter table and
          p. 2 (finite infinity encloses greater-than-critical density).
  [NW15]  Nazer & Wiltshire, arXiv:1410.3470, Phys. Rev. D 91, 043004 (2015),
          Table 2: three CMB matching prescriptions, f_v0 and dressed H_0.
  [DES]   Camilleri et al. (DES), arXiv:2406.05048, MNRAS 533 (2024) 2615,
          Tables 5/6.
  [DVB23] Douglass, Veyrat & BenZvi, arXiv:2202.01226, ApJS 265, 7 (2023),
          Sec. 3.1 (the VoidFinder criterion), Sec. 4.2 and Table 6.

Measured values are from verify/wp4_void_fraction.py in this repository, run
on VAST v1.3.1, doi:10.5281/zenodo.11043278.
"""

import sys

import numpy as np

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((bool(ok), name, detail))


def close(name, got, want, tol, detail=""):
    CHECKS.append((abs(got - want) <= tol, name,
                   "got %.4g, want %.4g +/- %.3g. %s" % (got, want, tol, detail)))


# ---------------------------------------------------------------------------
# Part A. The fitted f_v0 landscape
# ---------------------------------------------------------------------------
#
# (value, +err, -err, source, what was fitted). A None error means the source
# gives a point estimate with no uncertainty.

FITTED = [
    (0.76, 0.12, 0.09, "arXiv:0709.2535 abstract", "CMB sound horizon + BAO + SNe"),
    (0.95, 0.03, 0.04, "arXiv:1009.5855 Table 1", "Union2, 'out of the box'"),
    (0.72, 0.05, 0.05, "arXiv:1009.5855 Table 1", "SDSS-II, 'out of the box'"),
    (0.695, 0.041, 0.051, "arXiv:1306.3208 table", "Planck acoustic scales"),
    (0.627, 0.014, 0.012, "arXiv:1410.3470 Table 2", "CMB, matching A(H_bar_dec)"),
    (0.550, 0.017, 0.015, "arXiv:1410.3470 Table 2", "CMB, matching W(k = 0)"),
    (0.557, 0.017, 0.015, "arXiv:1410.3470 Table 2", "CMB, matching W(k != 0)"),
    (0.791, 0.039, 0.034, "arXiv:2406.05048 Table 6", "DES-SN5YRcut"),
    (0.665, 0.008, 0.009, "arXiv:2406.05048 Table 6", "DES-SN5YRcut + BAO"),
    (0.675, None, None, "arXiv:2311.01438 Fig. 8", "Pantheon+ 1690, MLE"),
]

# The three [NW15] prescriptions are the sharpest case available: one paper,
# one dataset, one set of authors, three ways of matching the timescape
# geometry to the CMB, all describing the same universe. Their spread against
# their own quoted errors is a direct test of whether f_v0 is a measurement.
NW15 = [(0.627, 0.013), (0.550, 0.016), (0.557, 0.016)]

# [NW15] Table 2 also gives the dressed H_0 for each prescription. This is a
# WP-1 input, recorded here because it is the same table and because WP-1
# marked the value 60.98 [UNKNOWN] for want of a source. It has one.
NW15_H0 = [("A(H_bar_dec)", 60.984), ("W(k = 0)", 56.148), ("W(k != 0)", 56.774)]
SW11_ADMISSIBLE = (57.0, 68.0)   # [SW11] Sec. 2


# ---------------------------------------------------------------------------
# Part B. The measured void fraction, from verify/wp4_void_fraction.py
# ---------------------------------------------------------------------------

MEASURED = {
    ("VoidFinder", "Planck2018", "edge included"): 62.28,
    ("VoidFinder", "WMAP5", "edge included"): 62.63,
    ("VoidFinder", "Planck2018", "edge excluded"): 44.82,
    ("VoidFinder", "WMAP5", "edge excluded"): 44.86,
}
PUBLISHED_VF = {"Planck2018": 60.8, "WMAP5": 61.1}   # [DVB23] Table 6

# Deceleration parameters, for the FLRW-conditioning estimate in Part C.
OMEGA_M = {"Planck2018": 0.315, "WMAP5": 0.258}      # [DVB23] Sec. 2.1


def q0_flat_lcdm(omega_m):
    """q_0 = Omega_M/2 - Omega_Lambda for flat LCDM."""
    return 1.5 * omega_m - 1.0


def q_dressed(f):
    """Dressed deceleration parameter, tracker. arXiv:0709.0732 Eq. (26).

    Transcription identical to verify/tracker_relations.py, which checks it
    against eleven published values.
    """
    return -(1 - f) * (8 * f**3 + 39 * f**2 - 12 * f - 8) / (4 + f + 4 * f**2) ** 2


def main():
    print("=" * 78)
    print("WP-4b: fitted f_v0 against the measured void fraction, and K5")
    print("=" * 78)
    print()

    # -- A1. The landscape --------------------------------------------------
    print("-" * 78)
    print("A. What `f_v0` has actually been fitted to, and to what")
    print("-" * 78)
    print("%-8s %-18s %-34s %s" % ("f_v0", "uncertainty", "what was fitted", "source"))
    for v, ep, em, src, what in FITTED:
        unc = "point estimate" if ep is None else "+%.3f / -%.3f" % (ep, em)
        print("%-8.3f %-18s %-34s %s" % (v, unc, what, src))
    vals = np.array([f[0] for f in FITTED])
    print()
    print("range %.3f to %.3f, a spread of %.3f" % (vals.min(), vals.max(),
                                                    vals.max() - vals.min()))
    close("the fitted f_v0 range matches the plan's 0.550-0.95",
          vals.min(), 0.550, 1e-9, "lowest is the [NW15] W(k=0) prescription")
    close("the fitted f_v0 upper end", vals.max(), 0.95, 1e-9,
          "[SW11] Union2 'out of the box', which [SW11] itself calls "
          "an unreasonably high best fit")

    # -- A2. Are the fits mutually consistent? ------------------------------
    print()
    print("The sharpest internal test: [NW15] Table 2 fits the SAME CMB data")
    print("three ways, by matching prescription, in one paper.")
    v = np.array([x[0] for x in NW15])
    s = np.array([x[1] for x in NW15])
    w = 1.0 / s**2
    mean = (w * v).sum() / w.sum()
    chi2 = (w * (v - mean) ** 2).sum()
    dof = len(v) - 1
    print("  values %s with errors %s" % (list(v), list(s)))
    print("  weighted mean %.4f, chi2 = %.2f on %d dof, chi2/dof = %.2f"
          % (mean, chi2, dof, chi2 / dof))
    worst = (v.max() - v.min()) / np.sqrt(s[v.argmax()] ** 2 + s[v.argmin()] ** 2)
    print("  widest pair: %.3f against %.3f is %.2f sigma apart"
          % (v.max(), v.min(), worst))
    check("the three [NW15] prescriptions are mutually inconsistent",
          chi2 / dof > 3.0,
          "chi2/dof = %.2f on %d dof; three descriptions of one universe from "
          "one dataset" % (chi2 / dof, dof))
    close("widest [NW15] pair separation in sigma", worst, 3.75, 0.1,
          "0.627 against 0.550")

    # The same table's dressed H_0, carried back to WP-1.
    print()
    print("  Same table, dressed H_0 by prescription, against [SW11]'s own")
    print("  admissible band %.0f < H_0 < %.0f:" % SW11_ADMISSIBLE)
    below = []
    for name, h0 in NW15_H0:
        flag = "BELOW the floor" if h0 < SW11_ADMISSIBLE[0] else "inside"
        if h0 < SW11_ADMISSIBLE[0]:
            below.append(name)
        print("    %-14s H_0 = %.3f   %s" % (name, h0, flag))
    check("WP-1's unsourced 60.98 now has a source",
          abs(NW15_H0[0][1] - 60.98) < 0.01,
          "[NW15] Table 2, matching A(H_bar_dec), best fit 60.984; WP-1 "
          "recorded this value [UNKNOWN]")
    check("two of three CMB prescriptions fall below timescape's own H_0 floor",
          len(below) == 2,
          "%s give %.1f and %.1f, under the %.0f floor of [SW11] Sec. 2"
          % (" and ".join(below), NW15_H0[1][1], NW15_H0[2][1],
             SW11_ADMISSIBLE[0]))

    # -- B. The definitional gap -------------------------------------------
    print()
    print("-" * 78)
    print("B. The two quantities, and why they are not the same one")
    print("-" * 78)
    print("""
  TIMESCAPE's f_v0 is the present-epoch volume fraction of the void phase in
  a two-phase Buchert average. The phase boundary is a density criterion.
  [DNW13] p. 2: bound systems "necessarily form in regions where the density
  is greater than critical" and are embedded in regions bounded by a "finite
  infinity surface". [SW11] Sec. 2: "we and all the objects we observe are
  necessarily in regions of greater than critical density, which are
  contained within walls". So the wall phase is the above-critical-density
  volume and the void phase is the rest. The boundary sits at the critical
  density, not at some deep underdensity.

  VOIDFINDER's voids are regions grown from cells empty of wall galaxies.
  [DVB23] Sec. 3.1: field galaxies are removed by a third-nearest-neighbour
  cut, the rest are gridded, "a sphere is then grown from each empty cell in
  the grid until it is bounded by four galaxies", and a void is the union of
  one maximal sphere of radius at least 10 h^-1 Mpc plus overlapping smaller
  spheres. There is no density threshold in that definition at all; the
  criterion is the absence of wall galaxies.

  V2's voids are watershed basins in a Voronoi tessellation, pruned either by
  a zone-linking density (VIDE) or by taking zones above the median zone
  volume (REVOLVER). [DVB23] says of these: "many galaxies in overdense
  regions are incorrectly classified as void galaxies by V2" and "V2 is not
  ideal for isolating the void environment". A volume fraction from
  V2/REVOLVER is therefore not a measurement of underdense volume on its own
  authors' account, which matters because it is the largest of the three.

  THE DIRECTION OF THE MISMATCH. A region containing no wall galaxies is, on
  any reasonable bias model, below the critical density. The converse fails:
  plenty of below-critical volume contains galaxies. So the VoidFinder region
  set is contained in the below-critical region set, and the VoidFinder
  fraction is a LOWER BOUND on the quantity f_v0 names. It is not an estimate
  of it, and it cannot be an upper bound.
""")

    # -- C. The error budget ------------------------------------------------
    print("-" * 78)
    print("C. The error budget on the measured number")
    print("-" * 78)
    edge = (MEASURED[("VoidFinder", "Planck2018", "edge included")]
            - MEASURED[("VoidFinder", "Planck2018", "edge excluded")])
    cosmo = abs(MEASURED[("VoidFinder", "WMAP5", "edge included")]
                - MEASURED[("VoidFinder", "Planck2018", "edge included")])
    lit = abs(MEASURED[("VoidFinder", "Planck2018", "edge included")]
              - PUBLISHED_VF["Planck2018"])

    # The FLRW-conditioning term. f_v is a ratio of volumes, so a uniform
    # rescaling of all distances cancels exactly; what survives is the change
    # in the SHAPE of D_C(z) across the survey, which to leading order is set
    # by q_0. The two supplied cosmologies give a measured sensitivity to a
    # known change in q_0, and timescape's q_0 differs from flat LCDM's by a
    # known amount, so the measured sensitivity can be scaled.
    dq_flrw = abs(q0_flat_lcdm(OMEGA_M["WMAP5"]) - q0_flat_lcdm(OMEGA_M["Planck2018"]))
    q_ts = q_dressed(0.695)
    dq_ts = abs(q_ts - q0_flat_lcdm(OMEGA_M["Planck2018"]))
    scale = dq_ts / dq_flrw
    est_flrw = cosmo * scale
    print("  edge treatment (cut 4)                      %6.2f points"
          % edge)
    print("  cosmology within FLRW (cut 3)               %6.2f points" % cosmo)
    print("  this pipeline against [DVB23] Table 6       %6.2f points" % lit)
    print()
    print("  The FLRW-conditioning term, SOURCE.md field 7's worry:")
    print("    f_v is a ratio of volumes, so a uniform distance rescaling")
    print("    cancels exactly. What survives is the shape of D_C(z) across")
    print("    0 < z < 0.114, set to leading order by q_0.")
    print("    q_0 flat LCDM, Omega_M = %.3f : %+.4f" % (
        OMEGA_M["Planck2018"], q0_flat_lcdm(OMEGA_M["Planck2018"])))
    print("    q_0 flat LCDM, Omega_M = %.3f : %+.4f" % (
        OMEGA_M["WMAP5"], q0_flat_lcdm(OMEGA_M["WMAP5"])))
    print("    q_0 timescape dressed, f_v0 = 0.695       : %+.4f" % q_ts)
    print("    measured: d q_0 = %.4f moves f_v by %.2f points" % (dq_flrw, cosmo))
    print("    needed:   d q_0 = %.4f, a factor %.2f larger" % (dq_ts, scale))
    print("    scaled estimate                           %6.2f points" % est_flrw)
    close("the FLRW-conditioning term, scaled from the measured sensitivity",
          est_flrw, 2.0, 0.3,
          "[INFERENCE]; premises: f_v sensitivity is linear in d q_0 over "
          "this range, and q_0 captures the leading shape difference at "
          "z < 0.114. An extrapolation by a factor of %.1f." % scale)
    check("the edge systematic dominates the whole budget",
          edge > 5 * max(cosmo, lit, est_flrw),
          "%.2f points against a next-largest of %.2f"
          % (edge, max(cosmo, lit, est_flrw)))
    print()
    print("  So the dominant uncertainty on the measured void fraction is")
    print("  neither the assumed cosmology nor the FLRW conditioning. It is")
    print("  the treatment of voids clipped by the survey boundary, at %.1f"
          % edge)
    print("  points, roughly %.0f times the FLRW-conditioning estimate."
          % (edge / est_flrw))
    print("  SOURCE.md field 7 was right that the conditioning is real. It")
    print("  turns out to be small for THIS dataset, because the survey is")
    print("  shallow and f_v is a ratio.")
    print()
    print("  Not in the budget, because it cannot be put there: the")
    print("  algorithm spread. Two of the three finders' published fractions")
    print("  are not reproducible from the published files (see")
    print("  verify/wp4_void_fraction.py), so the spread K5's wording leans")
    print("  on is not independently established by this dataset.")

    # -- D. K5 --------------------------------------------------------------
    print()
    print("-" * 78)
    print("D. Kill criterion K5")
    print("-" * 78)
    print("  K5: 'WP-4 finds the measured void fraction excludes every")
    print("  fitted f_v0.' Effect: branch stops, f_v0 is a fitting parameter")
    print("  and T13's evidential weight collapses.")
    print()
    # CORRECTED 2026-11-05. The first version of this block tested whether each
    # fitted value fell INSIDE the measured interval [lo, hi] and reported the
    # two that did as evidence K5's condition was not met. That is invalid:
    # Part B establishes the measurement as a LOWER BOUND on f_v0, not an
    # interval containing it, and a lower bound excludes every value BELOW it.
    # So the two values the old test counted as "inside" are the two the bound
    # actually excludes. Caught by verify/wp4_critical_threshold.py and argued
    # in findings/WP-4-void-fraction.md Sec. 10.3. The verdict is unchanged;
    # the test is now the right one.
    lo = min(MEASURED.values()) / 100.0
    hi = max(MEASURED.values()) / 100.0
    print("  the measurement is one-sided: it bounds f_v0 from BELOW only.")
    print("  So the test is whether the bound sits above every fitted value.")
    print()
    print("  %-34s %8s %8s" % ("bound", "value", "fits below it"))
    for label, bound in (("edge-included (strongest)", hi),
                         ("edge-excluded (weakest)", lo)):
        below = [f[0] for f in FITTED if f[0] < bound]
        print("  %-34s %8.4f %8d   %s" % (
            label, bound, len(below),
            ", ".join("%.3f" % b for b in below) if below else "none"))
    excluded_strong = [f for f in FITTED if f[0] < hi]
    excluded_weak = [f for f in FITTED if f[0] < lo]
    consistent = [f for f in FITTED if f[0] >= hi]
    print()
    check("K5 does not fire: the bound does not sit above every fitted value",
          len(consistent) > 0,
          "%d of %d fitted values sit at or above the strongest bound %.4f, "
          "so they are consistent with it and K5's 'every' is not met"
          % (len(consistent), len(FITTED), hi))
    check("the strongest bound does exclude two fits, which the old test denied",
          len(excluded_strong) == 2,
          "%s lie below the edge-included bound %.4f and are excluded by it; "
          "the superseded interval test called these two 'inside the measured "
          "interval', which is the wrong test for a one-sided quantity"
          % (" and ".join("%.3f" % f[0] for f in excluded_strong), hi))
    check("and the weakest bound excludes nothing, so the exclusion is conditional",
          len(excluded_weak) == 0,
          "no fitted value lies below the edge-excluded bound %.4f, so whether "
          "any fit is excluded is set entirely by the %.1f-point edge "
          "systematic" % (lo, 100 * (hi - lo)))
    check("a lower bound cannot touch the high fits in principle",
          all(f[0] > hi for f in FITTED if f[0] >= 0.72),
          "every fit at or above 0.72 clears the strongest bound, so the bulk "
          "of the fitted spread is untested by this measurement by "
          "construction, not merely in practice")

    # The second limb of the plan's "counts against" clause.
    print()
    print("  WP-4's 'counts against' clause has a second limb: 'or the fitted")
    print("  spread 0.550-0.791 is irreducible'. That limb holds.")
    close("the fitted spread against the typical quoted uncertainty",
          (0.791 - 0.550) / 0.016, 15.06, 0.1,
          "the 0.550-0.791 spread is this many times the ~0.016 error the "
          "tightest CMB fits quote")

    print()
    print("=" * 78)
    print("WHAT WP-4 ESTABLISHES")
    print("=" * 78)
    print("""
 1. The measured VoidFinder void volume fraction in SDSS DR7 is
    62.3% (Planck2018) or 62.6% (WMAP5) with edge voids included, and
    44.8% with them excluded. LCDM-conditioned, per cut 8.

 2. That number is a LOWER BOUND on the quantity f_v0 names, not an
    estimate of it. VoidFinder voids are regions empty of wall galaxies;
    timescape's void phase is all volume below the true critical density,
    which is a strictly larger set. That threshold is kinematic and has no
    published numerical value - see verify/wp4_critical_threshold.py and
    findings/WP-4-void-fraction.md Sec. 10.1.

 3. K5 DOES NOT FIRE. Eight of the ten fitted values sit at or above the
    strongest bound, so K5's 'every fitted value' is not met and the branch
    does not stop. The bound DOES exclude 0.550 and 0.557 under the
    edge-included measurement and nothing under the edge-excluded one, so
    that exclusion is conditional on the dominant systematic.

 4. The dominant systematic is the survey-edge treatment at 17.5 points,
    not the FLRW conditioning, which is about 2 points. That reorders
    SOURCE.md field 7's error budget: the circularity is real but small
    for a survey this shallow, because f_v is a ratio of volumes.

 5. The real result is the other limb. f_v0 is not a measurement. The
    sharpest evidence is internal: [NW15] Table 2 fits one CMB dataset
    three ways and gets 0.627, 0.550 and 0.557 with errors of 0.016,
    chi2/dof far above 1. Across all analyses the spread is 0.550 to 0.95,
    about fifteen times the tightest quoted error. A parameter whose fitted
    value moves by fifteen sigma with the fitting prescription is a fitting
    parameter.

 6. So objection O4 hardens, but not through K5. Measurement constrains
    f_v0 only from below, weakly, and conditionally on the edge treatment;
    the model's own fits do not agree with each other on it.

 7. And the two prescriptions the bound excludes are the same two whose
    dressed H_0 falls below timescape's own admissible floor of 57. Two
    independent routes reject the same two of [NW15]'s three. See
    findings/WP-4-void-fraction.md Sec. 10.4.
""")

    width = max(len(c[1]) for c in CHECKS)
    failed = 0
    for ok, name, detail in CHECKS:
        if not ok:
            failed += 1
        print("%s  %-*s %s" % ("PASS" if ok else "FAIL", width, name, detail))
    print()
    if failed:
        print("FAIL: %d of %d checks failed. No WP-4b conclusion is quotable."
              % (failed, len(CHECKS)))
        return 1
    print("PASS: %d of %d checks." % (len(CHECKS), len(CHECKS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
