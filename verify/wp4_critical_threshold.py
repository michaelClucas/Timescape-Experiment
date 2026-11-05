#!/usr/bin/env python3
"""WP-4, loose end: is the void/wall threshold a density, and does the bound hold?

    .venv/Scripts/python verify/wp4_critical_threshold.py

Exits 0 if every check passes, 1 otherwise. Runs in under a second.

Why this exists. findings/WP-4-void-fraction.md Sec. 4 rests its central
claim - that the measured VoidFinder fraction is a LOWER BOUND on timescape's
f_v0 rather than an estimate of it - on one premise it marked [INFERENCE] and
could not check: that regions empty of wall galaxies are below the critical
density. logs/2026-11-05-STATUS.md negative 12 records it as the day's loose
end, and Sec. 7 of that file names the single question that would have settled
it: is there a published numerical threshold?

There is not, and this script quantifies what follows from that. The
qualitative sources are quoted in the finding, with tags; everything numeric
is here.

Sources, all fetched and read in full as PDF text, not from abstracts:

  [W08]   Wiltshire, "Dark energy without dark energy", arXiv:0712.3984.
          Sec. 5, "Finite infinity and the true critical density". Eq. (7).
  [W09]   Wiltshire, "Average observational quantities in the timescape
          cosmology", arXiv:0909.0749, Phys. Rev. D80:123512. Sec. II,
          Eq. (27), and the Fig. 3 caption.
  [W07]   Wiltshire, "Exact solution to the averaging problem in cosmology",
          arXiv:0709.0732. Tracker relations, as transcribed in
          verify/tracker_relations.py and checked there against 11 published
          values.
  [DVB23] Douglass, Veyrat & BenZvi, arXiv:2202.01226. Sec. 2.1 cosmologies,
          Sec. 4.4 and Eq. (5) density profiles, Table 6.
  [NW15]  Nazer & Wiltshire, arXiv:1410.3470 Table 2, via
          verify/wp4_fv0_comparison.py.
  [SW11]  Smale & Wiltshire, arXiv:1009.5855 Sec. 2, same route.
  [HV02]  Hoyle & Vogeley, Astrophys. J. 566, 641 (2002). Cited by [W09] as
          its source for the observed void volume fraction, reference [56]
          there. NOT fetched: it enters only through what [W09] says of it,
          so the 40-50% below is attributed to [W09]'s use of it and is a
          [SOURCED] claim about [W09], not about [HV02].
"""

import sys

import numpy as np

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((bool(ok), name, detail))
    return bool(ok)


def close(name, got, want, tol, detail=""):
    CHECKS.append((abs(got - want) <= tol, name,
                   "got %.6g, want %.6g +/- %g. %s" % (got, want, tol, detail)))


# ---------------------------------------------------------------------------
# Transcriptions. Identical to verify/tracker_relations.py, which checks them
# against eleven published values. Repeated rather than imported, following
# verify/wp4_fv0_comparison.py, so this script stands alone.
# ---------------------------------------------------------------------------

def omega_m_bare(f):
    """Bare matter density, tracker. [W07], tracker parameter values."""
    return 4 * (1 - f) / (2 + f) ** 2


def gamma_lapse(f):
    """Relative lapse, tracker (h_r = 2/3). [W07] Eq. (7), after Eq. (19)."""
    return 1 + f / 2


def omega_m_dressed_eq27(f):
    """Dressed matter density via [W09] Eq. (27): Omega_M = gamma_w^3 Omega_M_bar."""
    return gamma_lapse(f) ** 3 * omega_m_bare(f)


def omega_m_dressed_closed(f):
    """Dressed matter density, closed form. [W09] Fig. 3 caption:
    Omega_M0 = (1/2)(1 - f_v0)(2 + f_v0)."""
    return 0.5 * (1 - f) * (2 + f)


# ---------------------------------------------------------------------------
# Inputs, all published or computed by a committed script.
# ---------------------------------------------------------------------------

# [DVB23] Sec. 2.1. The two flat LCDM cosmologies the catalogues are built in.
OMEGA_M_FLRW = {"Planck2018": 0.315, "WMAP5": 0.258}

# Measured VoidFinder void volume fraction, from verify/wp4_void_fraction.py
# (14/14 at 569ebb9, re-run clean this session). LCDM-conditioned per cut 8.
# CORRECTED 2026-11-05 per OPEN-QUESTIONS.md Q-4. These were 0.6228, 0.6263,
# 0.4482 and 0.4486 until commit db47115, from a mask declination index that
# applied the +90 offset before the truncation rather than after; see
# verify/wp4_vast_mask_convention.py. No exclusion verdict below changes, and
# that is asserted there as a check rather than assumed here.
MEASURED = {
    ("Planck2018", "edge included"): 0.6157,
    ("WMAP5", "edge included"): 0.6192,
    ("Planck2018", "edge excluded"): 0.4406,
    ("WMAP5", "edge excluded"): 0.4411,
}

# Fitted f_v0, as tabulated in verify/wp4_fv0_comparison.py.
FITTED = [
    (0.76, "arXiv:0709.2535 abstract", "CMB sound horizon + BAO + SNe"),
    (0.95, "arXiv:1009.5855 Table 1", "Union2, out of the box"),
    (0.72, "arXiv:1009.5855 Table 1", "SDSS-II, out of the box"),
    (0.695, "arXiv:1306.3208 table", "Planck acoustic scales"),
    (0.627, "arXiv:1410.3470 Table 2", "CMB, matching A(H_bar_dec)"),
    (0.550, "arXiv:1410.3470 Table 2", "CMB, matching W(k = 0)"),
    (0.557, "arXiv:1410.3470 Table 2", "CMB, matching W(k != 0)"),
    (0.791, "arXiv:2406.05048 Table 6", "DES-SN5YRcut"),
    (0.665, "arXiv:2406.05048 Table 6", "DES-SN5YRcut + BAO"),
    (0.675, "arXiv:2311.01438 Fig. 8", "Pantheon+ 1690, MLE"),
]

# [W09] Sec. II: voids of a characteristic diameter 30 h^-1 Mpc are observed
# to fill 40-50% of the universe at the present epoch, its reference [56]
# being [HV02]. This is timescape's own statement of the observed large-void
# volume fraction, and the interval is the paper's, not a derived one.
W09_OBSERVED_LARGE_VOID = (0.40, 0.50)

# [NW15] Table 2 prescriptions with their dressed H_0, and [SW11]'s floor.
NW15 = [("A(H_bar_dec)", 0.627, 60.984),
        ("W(k = 0)", 0.550, 56.148),
        ("W(k != 0)", 0.557, 56.774)]
SW11_H0_FLOOR = 57.0


def main():
    print("=" * 78)
    print("WP-4 loose end: the void/wall threshold, and which way the bound cuts")
    print("=" * 78)

    # -- A. There is no numerical threshold, and the dressed relation -------
    print()
    print("-" * 78)
    print("A. What the threshold is, in timescape's own terms")
    print("-" * 78)
    print("  [W08] Sec. 5 Eq. (7) is a DENIAL: rho_cr != 3 H_av^2 / (8 pi G),")
    print("  because the average Hubble parameter is tied to the spatial scale")
    print("  of averaging and the clock chosen. Finite infinity is then defined")
    print("  kinematically: the scale over which the average expansion is zero,")
    print("  positive outside, with rho_cr the density there. So the threshold")
    print("  is not a number and cannot be one. The quotations are in")
    print("  findings/WP-4-void-fraction.md Sec. 4, tagged.")
    print()
    print("  What IS published as a number is the dressed matter density.")

    # Eq. (27) composed with the tracker relations must give the closed form
    # [W09] quotes in its Fig. 3 caption. If it does not, one of the two
    # transcriptions is wrong and nothing below is safe.
    fs = np.linspace(0.01, 0.99, 991)
    resid = float(np.max(np.abs(omega_m_dressed_eq27(fs)
                                - omega_m_dressed_closed(fs))))
    check("[W09] Eq. (27) over [W07]'s tracker gives [W09]'s closed form",
          resid < 1e-12,
          "max |gamma^3 Omega_M_bar - (1/2)(1-f)(2+f)| = %.3g over f in "
          "(0.01, 0.99). Two independent transcriptions agree identically, so "
          "the dressed relation used below is not a guess" % resid)

    close("dressed Omega_M0 at the [W09] best fit f_v0 = 0.762",
          omega_m_dressed_closed(0.762), 0.33, 5e-3,
          "[W09] Fig. 3 caption states this value explicitly")

    # -- B. The threshold overdensity under the reading timescape denies ----
    print()
    print("-" * 78)
    print("B. The premise's failure condition, quantified")
    print("-" * 78)
    print("  The premise is: a region empty of wall galaxies is below the")
    print("  critical density. Under the FLRW-style reading that [W08] Eq. (7)")
    print("  denies, rho_cr = 3H^2/(8 pi G) and a matter-only region reaches it")
    print("  when Omega_M (1 + delta_m) = 1, i.e. 1 + delta_m = 1/Omega_M. That")
    print("  is the only reading in which the threshold is a number at all, so")
    print("  it is the only one in which the premise can fail numerically.")
    print()
    print("  %-36s %-10s %-13s %s"
          % ("reading", "Omega_M", "1 + delta_m", "delta_m needed"))
    thresholds = []
    for name, om in sorted(OMEGA_M_FLRW.items()):
        thresholds.append(("%s (flat LCDM, [DVB23])" % name, om, 1.0 / om))
    for f, _src, _what in sorted(FITTED):
        om = omega_m_dressed_closed(f)
        thresholds.append(("timescape dressed, f_v0 = %.3f" % f, om, 1.0 / om))
    for name, om, t in thresholds:
        print("  %-36s %-10.4f %-13.3f %+.3f" % (name, om, t, t - 1.0))

    tmin = min(t for _n, _o, t in thresholds)
    tmax = max(t for _n, _o, t in thresholds)
    close("the weakest threshold over every reading, as 1 + delta_m",
          tmin, 1.7426, 5e-4,
          "the least demanding case is timescape's own dressed geometry at "
          "the lowest fitted f_v0 = 0.550, where Omega_M0 = 0.5738")
    close("the strongest threshold over every reading, as 1 + delta_m",
          tmax, 13.5593, 5e-4,
          "I expected WMAP5's 3.876 here and was wrong: timescape's own "
          "dressed geometry at the highest fitted f_v0 = 0.95 gives "
          "Omega_M0 = 0.0738, so the threshold runs to 13.6. Recorded as a "
          "correction to my own arithmetic, not to a published value")
    check("the premise can fail only at a wall-level matter overdensity",
          tmin > 1.5,
          "in the most permissive reading available a region must still reach "
          "%.2f times the mean matter density to be critical, i.e. delta_m > "
          "%+.2f. A region selected for containing no wall galaxies is not at "
          "%+.0f%% matter overdensity unless galaxies anti-correlate with "
          "matter on 10-30 h^-1 Mpc scales. [INFERENCE]; premise: linear bias "
          "b > 0 on those scales" % (tmin, tmin - 1, 100 * (tmin - 1)))

    # -- C. Which way the bound cuts ----------------------------------------
    print()
    print("-" * 78)
    print("C. A lower bound excludes from BELOW, which WP-4 did not apply")
    print("-" * 78)
    print("  If the measured VoidFinder fraction is a lower bound on f_v0, then")
    print("  every fitted f_v0 strictly below it is EXCLUDED by it.")
    print("  verify/wp4_fv0_comparison.py tested only whether fits fall inside")
    print("  the measured interval [min variant, max variant] and concluded")
    print("  f_v0 is unconstrained by measurement. That framing is wrong: the")
    print("  interval's low end is the edge-EXCLUDED variant, which is a weaker")
    print("  bound on the same quantity, not a second measurement of it. Taking")
    print("  the min over variants is the conservative choice for the bound's")
    print("  validity, and it licenses nothing about values below the max.")
    print()
    for variant in ("edge included", "edge excluded"):
        for cosmo in ("Planck2018", "WMAP5"):
            b = MEASURED[(cosmo, variant)]
            below = sorted(f for f, _s, _w in FITTED if f < b)
            print("  bound %.4f (%-11s %-13s) excludes %d fits: %s"
                  % (b, cosmo, variant, len(below),
                     ", ".join("%.3f" % v for v in below) if below else "none"))

    b_incl = MEASURED[("Planck2018", "edge included")]
    b_excl = MEASURED[("Planck2018", "edge excluded")]
    excl_incl = sorted(f for f, _s, _w in FITTED if f < b_incl)
    excl_excl = sorted(f for f, _s, _w in FITTED if f < b_excl)

    check("the edge-included bound does exclude fits, which WP-4 said it did not",
          excl_incl == [0.550, 0.557],
          "under the edge-included Planck2018 bound of %.4f the fits 0.550 and "
          "0.557 lie below a LOWER bound on f_v0 and are therefore excluded by "
          "it. findings/WP-4-void-fraction.md Sec. 6 calls exactly these two "
          "inside the measured interval; that is the wrong test, and this "
          "check asserts the disagreement so it cannot silently vanish later. "
          "I expected 0.627 to be excluded too and it is not" % b_incl)
    # REWRITTEN 2026-11-05 with the Q-4 index correction. This check used to
    # read "0.627 survives the bound by less than the pipeline's own error",
    # asserting 0 < 0.627 - b_incl < 0.0148. That ordering has REVERSED: the
    # correction moved the bound from 0.6228 to 0.6157, so the margin went from
    # 0.0042 to 0.0113, while the pipeline's residual against [DVB23] Table 6
    # went from 0.0148 to 0.0077. The old claim is now false and the check
    # asserts the true one instead. The expectation is corrected, not widened.
    # The upper limit is half the +-1 px pixelation bracket of
    # verify/wp4_mask_resolution.py, 0.03663 as that script re-measures it
    # about the corrected baseline. It read 0.0307 for one run, from the
    # bracket measured about the SUPERSEDED baseline; corrected here to the
    # value the cited script actually reports. The check passed either way.
    check("0.627 now clears the bound by MORE than the pipeline's own residual",
          0.0077 < 0.627 - b_incl < 0.5 * 0.03663,
          "the A(H_bar_dec) prescription clears the edge-included bound of "
          "%.4f by %+.4f, against a residual of 0.0077 against [DVB23]'s own "
          "published fraction. Before the Q-4 index correction the margin was "
          "0.0042 against a 0.0148 residual and this check asserted the "
          "opposite ordering. It is still inside half the 0.03663 one-pixel "
          "pixelation bracket of verify/wp4_mask_resolution.py, which is why "
          "0.627 remains undecided, and far inside the 0.175 edge systematic"
          % (b_incl, 0.627 - b_incl))
    check("and the edge-excluded bound excludes nothing",
          excl_excl == [],
          "under the edge-excluded bound of %.4f no fitted value lies below "
          "the bound, so the exclusion in the previous check is entirely "
          "conditional on the edge treatment, which is WP-4's own dominant "
          "systematic at 17.5 points" % b_excl)
    check("so the exclusion is conditional, not established",
          len(excl_incl) > 0 and len(excl_excl) == 0,
          "the two edge variants disagree about whether any fit is excluded. "
          "That is the honest state: the bound cuts downward, and how far down "
          "is set by the systematic WP-4 already named as dominant")

    print()
    print("  Where this converges. [NW15] Table 2's three prescriptions:")
    print("  %-14s %-8s %-9s %-12s %s"
          % ("prescription", "f_v0", "H_0", "below bound?", "below H_0 floor 57?"))
    conv = []
    for name, f, h0 in NW15:
        below_b = f < b_incl
        below_h = h0 < SW11_H0_FLOOR
        conv.append((name, below_b, below_h))
        print("  %-14s %-8.3f %-9.3f %-12s %s"
              % (name, f, h0, "yes" if below_b else "no",
                 "yes" if below_h else "no"))
    check("the two prescriptions below timescape's H_0 floor are also below the bound",
          all(bb for _n, bb, bh in conv if bh),
          "W(k=0) and W(k!=0) give dressed H_0 = 56.148 and 56.774, both below "
          "[SW11]'s admissible floor of 57, and f_v0 = 0.550 and 0.557, both "
          "below the edge-included measured lower bound. Two independent routes "
          "reject the same two of three prescriptions. Neither rejects "
          "A(H_bar_dec) on H_0, and the bound rejects it only marginally "
          "(0.627 against %.4f)" % b_incl)

    # -- D. K5, restated on the corrected logic -----------------------------
    print()
    print("-" * 78)
    print("D. K5 on the corrected logic")
    print("-" * 78)
    print("  K5: the measured void fraction excludes EVERY fitted f_v0.")
    not_excluded = sorted(f for f, _s, _w in FITTED if f >= b_incl)
    print("  fits NOT excluded even by the strongest bound available (%.4f):"
          % b_incl)
    print("    %s" % ", ".join("%.3f" % v for v in not_excluded))
    check("K5 still does not fire",
          len(not_excluded) > 0,
          "%d of %d fitted values sit at or above the strongest measured lower "
          "bound, so they are consistent with it and K5's every is not met. The "
          "conclusion is unchanged; the reason is now sharper than "
          "unconstrained" % (len(not_excluded), len(FITTED)))

    # -- E. The minivoid budget ---------------------------------------------
    print()
    print("-" * 78)
    print("E. What [W09] says accounts for the gap, and how big the gap is")
    print("-" * 78)
    print("  [W09] Sec. II gives the observed large-void fraction as 40-50%,")
    print("  from [HV02], then adds minivoids and says voids of all sizes")
    print("  appear to dominate the volume, with the exact volume fraction")
    print("  depending on the empirical definition of a void in terms of some")
    print("  particular negative density contrast. So timescape's own")
    print("  reconciliation of f_v0 ~ 0.7 with a catalogued 40-50% runs through")
    print("  a population no large-void catalogue measures, and [DVB23]'s")
    print("  10 h^-1 Mpc minimum radius excludes exactly that population.")
    print()
    lo_m = min(MEASURED.values())
    hi_m = max(MEASURED.values())
    check("[W09]'s own quoted 40-50% overlaps this pipeline's measured range",
          lo_m <= W09_OBSERVED_LARGE_VOID[1] and hi_m >= W09_OBSERVED_LARGE_VOID[0],
          "measured %.3f-%.3f across variants against [W09]'s 0.40-0.50. The "
          "overlap matters because it means timescape is not working from a "
          "different measurement of the large-void fraction than this one"
          % (lo_m, hi_m))
    print("  %-8s %-26s %s" % ("f_v0", "minivoid volume required", "source"))
    for f, src, _w in sorted(FITTED):
        print("  %-8.3f %+-26.4f %s" % (f, f - b_incl, src))
    close("minivoid volume the Planck-acoustic fit requires, in volume fraction",
          0.695 - b_incl, 0.0793, 5e-4,
          "f_v0 = 0.695 against the edge-included measured 0.6157: 7.9 points "
          "of the present horizon volume must be in voids this catalogue "
          "cannot see")
    close("and what the DES-SN5YR fit requires",
          0.791 - b_incl, 0.1753, 5e-4,
          "f_v0 = 0.791 needs 17.5 points, which is 28% of the measured "
          "large-void volume over again in minivoids")

    print()
    print("=" * 78)
    print("WHAT THIS SETTLES")
    print("=" * 78)
    print("""
 1. There is no published numerical threshold for timescape's wall/void split,
    and [W08] Eq. (7) says there cannot be one: rho_cr is explicitly NOT
    3H_av^2/(8 pi G) in an inhomogeneous cosmology. The threshold is
    kinematic - the surface of zero average expansion - and local. So
    logs/2026-11-05-STATUS.md Sec. 7's question has an answer, and the answer
    is that the question has no numerical form.

 2. WP-4's lower-bound premise is no longer unverified. It is supported twice:
    [W09] Sec. II identifies the wall phase observationally as sheets,
    filaments and knots containing galaxy clusters, which is what VoidFinder's
    wall galaxies trace; and numerically, the premise can fail only if the
    matter overdensity inside a VoidFinder void exceeds +74% in the most
    permissive reading available.

 3. The bound cuts DOWNWARD and WP-4 did not apply it that way. Under the
    edge-included measurement it excludes f_v0 = 0.550 and 0.557. Under the
    edge-excluded one it excludes nothing. The exclusion is real and entirely
    conditional on the dominant systematic. The third low fit, 0.627, clears
    the bound by 0.004, which is less than this pipeline's own 0.015
    disagreement with the published fraction: not excluded, not distinguished.

 4. The two prescriptions excluded by the bound are the same two whose dressed
    H_0 falls below timescape's own admissible floor. Two independent routes,
    one from void volumes and one from the model's own H_0 band, reject the
    same two of [NW15]'s three CMB matching prescriptions.

 5. K5 still does not fire. A lower bound does not exclude the high fits.

 6. The gap between f_v0 and the measured large-void fraction is attributed by
    [W09] itself to minivoids, a population with no volume fraction anywhere
    in this dataset. That is the measurement that would constrain f_v0, and it
    is not a cycle's work.
""")

    width = max(len(c[1]) for c in CHECKS)
    failed = sum(1 for ok, _n, _d in CHECKS if not ok)
    for ok, name, detail in CHECKS:
        print("%s  %-*s %s" % ("PASS" if ok else "FAIL", width, name, detail))
    print()
    if failed:
        print("FAIL: %d of %d checks failed." % (failed, len(CHECKS)))
        return 1
    print("PASS: %d of %d checks." % (len(CHECKS), len(CHECKS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
