#!/usr/bin/env python3
"""WP-1: is either published comparison against timescape like-for-like?

    .venv/Scripts/python verify/wp1_comparability.py

Exits 0 if every check passes, 1 otherwise. Runs in under a second.

WP-1 in docs/RESEARCH-PLAN.md is a comparability check and nothing more. Two
published results are flagged in Run 01's discrimination table as "arguably
already decided against timescape":

  (a) the supernova + BAO joint fit of Camilleri et al. (DES), arXiv:2406.05048
  (b) the dressed H_0 of 61.7 km/s/Mpc against local determinations of 70-73

This script establishes what is arithmetically checkable about each. It does
not fit anything. Fitting supernovae is WP-2 and out of scope for the standing
loop.

Every target value below is from a source that was fetched and read, with the
locator on the check. Nothing here is taken from an abstract or a citing paper.

Sources, all retrieved in full text:

  [DES]   Camilleri et al. (DES Collaboration), "The Dark Energy Survey
          Supernova Program: Investigating Beyond-LCDM", arXiv:2406.05048,
          MNRAS 533 (2024) 2615, DOI 10.1093/mnras/stae1988.
          Tables 5/6 (parameters), Table 7 (model comparison), Sec. 7.8
          (timescape setup), Eq. (49) (dressed/bare Hubble relation).
  [SW11]  Smale & Wiltshire, "Supernova tests of the timescape cosmology",
          arXiv:1009.5855, MNRAS 413 (2011) 367. Sec. 2 (the 17% local
          enhancement, the admissible H_0 band, the SH0ES remark),
          Eq. (17) (bare from dressed).
  [DNW13] Duley, Nazer & Wiltshire, "Timescape cosmology with radiation
          fluid", arXiv:1306.3208. Parameter table: f_v0, gamma_bar_0,
          H_bar_0.
  [W19]   Wiltshire, "Comment on 'Hubble flow variations as a test for
          inhomogeneous cosmology'", arXiv:1812.01586, A&A 624 (2019) A12.
          Secs. 2-3: H_bar_0, gamma_bar_0, dressed H_0, H_bar_tau_0.
  [LNW08] Leith, Ng & Wiltshire, "Gravitational energy as dark energy",
          arXiv:0709.2535, ApJ 672 (2008) L91. Abstract: dressed H_0, f_v0,
          bare H_0.
  [R22]   Riess et al. (SH0ES), arXiv:2112.04510, ApJL 934 (2022) L7,
          DOI 10.3847/2041-8213/ac5c5b. Abstract: H_0 = 73.04 +/- 1.04.
"""

import sys

CHECKS = []


def check(name, got, want, tol, source, note=""):
    CHECKS.append((abs(got - want) <= tol, name, got, want, tol, source, note))


# ---------------------------------------------------------------------------
# Part A. The DES joint fit: is the model comparison at matched parameter count?
# ---------------------------------------------------------------------------
#
# [DES] Sec. 7.8 states the timescape model has one free cosmological
# parameter, the void fraction f_v0, with H_0 marginalised as a nuisance
# parameter. Flat-LCDM as fitted there has one free cosmological parameter,
# Omega_m, with the same nuisance treatment. So k_timescape = k_LCDM.
#
# [DES] defines AIC = 2k - 2 ln L_max and chi2 = -2 ln L_max, and Table 7
# reports half-Delta-AIC. Therefore
#
#     half-Delta-AIC = (1/2) * [ 2*Delta_k + Delta_chi2 ]
#
# and at Delta_k = 0 this is just half the chi-squared difference. If the
# published half-Delta-AIC is recovered from the published chi2 values with
# Delta_k = 0, the parameter counts are confirmed matched *arithmetically*,
# independently of the prose. That is the check Run 01's own C5 rule demands
# and the one its supernova table could not supply for most rows.
#
# Table 7, DES-SN5YRcut rows ([DES] Table 7, verbatim):
#     Flat-LCDM   DES-SN5YRcut                 half-dAIC  0.0   dlnS  0.0    chi2 1616
#     Timescape   DES-SN5YRcut                 half-dAIC -1.7   dlnS -1.72   chi2 1612
#     Flat-LCDM   DES-SN5YRcut + BAO-theta*perp half-dAIC  0.0   dlnS  0.0    chi2 1624
#     Timescape   DES-SN5YRcut + BAO-theta*perp half-dAIC  6.3   dlnS  6.17   chi2 1637
#
# chi2 is tabulated to the nearest integer, so Delta_chi2 carries +/- 1 and
# half-Delta-AIC carries +/- 0.5. The tolerance below is that rounding, not a
# fudge: a parameter-count mismatch of one would move half-Delta-AIC by 1.0,
# twice the tolerance, so the check still discriminates.

CHI2_SN_LCDM, CHI2_SN_TS = 1616.0, 1612.0
CHI2_SNBAO_LCDM, CHI2_SNBAO_TS = 1624.0, 1637.0

K_TS = 1          # [DES] Sec. 7.8: "the only free parameter of the Timescape model"
K_LCDM = 1        # [DES] Tables 5/6: Omega_m, with H_0 a nuisance parameter on both


def half_delta_aic(chi2_model, chi2_ref, k_model, k_ref):
    """half-Delta-AIC from [DES]'s own definitions AIC = 2k - 2 ln L, chi2 = -2 ln L."""
    return 0.5 * (2 * (k_model - k_ref) + (chi2_model - chi2_ref))


check("DES SNe-only half-dAIC from chi2 at matched k",
      half_delta_aic(CHI2_SN_TS, CHI2_SN_LCDM, K_TS, K_LCDM), -1.7, 0.5,
      "arXiv:2406.05048 Table 7",
      "recovers the published -1.7; confirms k_TS = k_LCDM")

check("DES SNe+BAO half-dAIC from chi2 at matched k",
      half_delta_aic(CHI2_SNBAO_TS, CHI2_SNBAO_LCDM, K_TS, K_LCDM), 6.3, 0.5,
      "arXiv:2406.05048 Table 7",
      "recovers the published +6.3; confirms k_TS = k_LCDM")

# A mismatch of one parameter would NOT reproduce the table. Recorded as a
# check so the discrimination is visible rather than asserted.
_mismatch = half_delta_aic(CHI2_SNBAO_TS, CHI2_SNBAO_LCDM, K_TS + 1, K_LCDM)
check("a one-parameter mismatch would be excluded",
      abs(_mismatch - 6.3), 1.0, 0.5,
      "arithmetic on arXiv:2406.05048 Table 7",
      "k_TS = 2 would give %.1f, off by 1.0 = twice the rounding" % _mismatch)

# Significance of the joint-fit result. At Delta_k = 0, Delta_AIC = Delta_chi2,
# so the AIC difference carries no parameter-count penalty either way and the
# whole of it is fit quality.
DELTA_AIC_SNBAO = 2 * 6.3
check("DES SNe+BAO Delta_AIC favouring flat-LCDM",
      DELTA_AIC_SNBAO, 12.6, 1e-9,
      "arXiv:2406.05048 Table 7",
      "2 x half-dAIC; >10 is conventionally 'very strong' on the AIC scale")

# And the sign flip between the two rows is the whole result: timescape is
# weakly preferred on supernovae alone and strongly disfavoured once the BAO
# angular measurement is added. Both rows at the same k.
check("sign flip on adding BAO is larger than either row alone",
      (6.3 - (-1.7)), 8.0, 1e-9,
      "arXiv:2406.05048 Table 7",
      "half-dAIC moves 8.0 on adding BAO-theta*perp")

# The fitted f_v0 moves with the data combination by far more than its own
# quoted uncertainty. [DES] Table 6: 0.791 (+0.039/-0.034) on SNe alone,
# 0.665 (+0.008/-0.009) with BAO. This is a WP-4/K5 input, recorded here
# because it is the same table.
FV0_DES_SN, FV0_DES_SN_ERRLO = 0.791, 0.034
FV0_DES_SNBAO, FV0_DES_SNBAO_ERRHI = 0.665, 0.008
_shift = FV0_DES_SN - FV0_DES_SNBAO
_combined_err = (FV0_DES_SN_ERRLO**2 + FV0_DES_SNBAO_ERRHI**2) ** 0.5
check("DES f_v0 shift on adding BAO, in units of its own error",
      _shift / _combined_err, 3.59, 0.02,
      "arXiv:2406.05048 Table 6",
      "0.791 -> 0.665 is %.3f, i.e. %.2f sigma on the quoted errors"
      % (_shift, _shift / _combined_err))

# ---------------------------------------------------------------------------
# Part B. The dressed/bare Hubble relation, and which quantity is which
# ---------------------------------------------------------------------------
#
# Timescape has three distinct H_0-like quantities and the discrimination
# table compares only one of them to the distance ladder. Pinning the relation
# between them is a prerequisite for asking whether that comparison is
# like-for-like.
#
# [SW11] Eq. (17):  H_bar_0 = 2(2 + f_v0) H_0 / (4 f_v0^2 + f_v0 + 4)
# [DES]  Eq. (49):  H_0 = (4 f_v0^2 + f_v0 + 4) H_bar_0 / [2(2 + f_v0)]
#
# These are the same relation, written both ways, in two independent papers.


def dressed_from_bare(f, h_bar):
    """Dressed H_0 from bare H_bar_0, tracker solution. [SW11] Eq. (17), [DES] Eq. (49)."""
    return (4 * f**2 + f + 4) * h_bar / (2 * (2 + f))


def bare_from_dressed(f, h_dressed):
    """Inverse of the above. [SW11] Eq. (17) as written."""
    return 2 * (2 + f) * h_dressed / (4 * f**2 + f + 4)


# Round trip, so a sign or transcription error cannot hide.
check("dressed/bare relation inverts exactly",
      bare_from_dressed(0.695, dressed_from_bare(0.695, 50.1)), 50.1, 1e-9,
      "arXiv:1009.5855 Eq. (17); arXiv:2406.05048 Eq. (49)")

# [DNW13] parameter table: f_v0 = 0.695 (+0.041/-0.051),
# gamma_bar_0 = 1.348 (+0.021/-0.025), H_bar_0 = 50.1 +/- 1.7 km/s/Mpc.
# [W19] Sec. 2 quotes the same fit and gives dressed H_0 = 61.7 +/- 3.0.
FV0_CMB = 0.695
H_BAR_0 = 50.1
GAMMA_BAR_0 = 1.348

check("dressed H_0 from the CMB-fitted bare H_0",
      dressed_from_bare(FV0_CMB, H_BAR_0), 61.7, 0.15,
      "arXiv:1306.3208 table; arXiv:1812.01586 Sec. 2",
      "50.1 at f_v0 = 0.695 gives %.2f against the published 61.7"
      % dressed_from_bare(FV0_CMB, H_BAR_0))

# Independent confirmation at a different f_v0 and a different paper: [LNW08]
# fit supernovae and report dressed H_0 = 61.7 (+1.2/-1.1), f_v0 = 0.76
# (+0.12/-0.09), bare H_0 = 48.2 (+2.0/-2.4). The same relation must carry
# 61.7 to 48.2 at f_v0 = 0.76, which is a genuinely separate test of the
# transcription because neither number is shared with the CMB fit.
check("bare H_0 from the SNe-fitted dressed H_0",
      bare_from_dressed(0.76, 61.7), 48.2, 0.1,
      "arXiv:0709.2535 abstract",
      "61.7 at f_v0 = 0.76 gives %.2f against the published 48.2"
      % bare_from_dressed(0.76, 61.7))

# The third quantity. [W19] Sec. 2: H_bar_tau_0 = gamma_bar_0 * H_bar_0, the
# volume-average expansion rate measured on wall clocks, which [W19] states
# matches the FLRW Hubble constant inferred from the same CMB data.
check("H_bar_tau_0 = gamma_bar_0 * H_bar_0",
      GAMMA_BAR_0 * H_BAR_0, 67.5, 0.1,
      "arXiv:1812.01586 Sec. 2",
      "1.348 x 50.1 = %.2f against the published 67.5" % (GAMMA_BAR_0 * H_BAR_0))

# gamma_bar_0 is NOT the dressed/bare ratio. The two differ by 10%, which is
# the whole reason the H_0 row needs a comparability check: "the timescape
# Hubble constant" names three numbers spanning 50.1 to 67.5.
_ratio = dressed_from_bare(FV0_CMB, H_BAR_0) / H_BAR_0
check("dressed/bare ratio differs from the lapse gamma_bar_0",
      GAMMA_BAR_0 - _ratio, 0.1185, 0.002,
      "arXiv:1306.3208 table; arXiv:1812.01586 Sec. 2",
      "gamma_bar_0 = 1.348 but H_0/H_bar_0 = %.4f" % _ratio)

check("the three timescape H_0-like quantities span 35%",
      (GAMMA_BAR_0 * H_BAR_0) / H_BAR_0 - 1.0, 0.348, 1e-9,
      "arXiv:1812.01586 Sec. 2",
      "bare 50.1, dressed 61.7, H_bar_tau_0 67.5")

# ---------------------------------------------------------------------------
# Part C. Is the H_0 comparison like-for-like, on timescape's own criterion?
# ---------------------------------------------------------------------------
#
# [SW11] Sec. 2 states the admissible band and the challenge in its own words:
#   "values of 57 < H_0 < 68 km sec-1 Mpc-1 would be admissible in the TS
#    scenario, but values as large as the recent H_0 = 74.2 +/- 3.6 km sec-1
#    Mpc-1 determined by the SH0ES survey (Riess et al. 2009) would represent
#    a severe challenge to the model."
#
# [SW11] Sec. 2 also states the comparability criterion:
#   "Ideally the global average Hubble constant should be determined only on
#    scales significantly larger than the scale of statistical homogeneity,
#    z > 0.033, by methods which do not depend on calibrations below that
#    scale."
#
# and the quantitative escape:
#   "The Hubble 'constant' inferred in this manner should peak at the dominant
#    void scale 30/h Mpc, i.e. at z ~ 0.01, with a maximum value up to 17%
#    greater than the global average and then steadily decrease to near the
#    global average value when the scale of statistical homogeneity is
#    reached."
#
# [R22] gives H_0 = 73.04 +/- 1.04 from Cepheid-calibrated SNe Ia, with the
# calibrating SNe at z < 0.01 - i.e. below the z = 0.033 scale [SW11] excludes,
# and at the scale where [SW11] predicts the largest enhancement.

H0_SHOES, H0_SHOES_ERR = 73.04, 1.04
TS_ADMISSIBLE_CEILING = 68.0        # [SW11] Sec. 2
LOCAL_ENHANCEMENT_MAX = 0.17        # [SW11] Sec. 2

# C1. Taken at face value, against timescape's own stated ceiling, SH0ES is
# excluded by a wide margin. This is the strongest form of the H_0 objection
# and it is the authors' own criterion, not an outside one.
check("SH0ES above timescape's own admissible ceiling, in SH0ES sigma",
      (H0_SHOES - TS_ADMISSIBLE_CEILING) / H0_SHOES_ERR, 4.85, 0.01,
      "arXiv:1009.5855 Sec. 2; arXiv:2112.04510 abstract",
      "73.04 vs the 68 ceiling is %.2f sigma on the SH0ES error alone"
      % ((H0_SHOES - TS_ADMISSIBLE_CEILING) / H0_SHOES_ERR))

# C2. Against the dressed value specifically, which is what the
# discrimination table compares.
_dressed = dressed_from_bare(FV0_CMB, H_BAR_0)
check("SH0ES / dressed H_0 ratio",
      H0_SHOES / _dressed, 1.1857, 0.002,
      "arXiv:1306.3208 table; arXiv:2112.04510 abstract",
      "73.04 / %.2f = %.4f, an 18.6%% excess" % (_dressed, H0_SHOES / _dressed))

# C3. And here is why the comparison is not decisive. The excess that has to
# be explained is 18.6%; the enhancement timescape predicts at the scale where
# the ladder is calibrated is "up to 17%". Those are the same size. The H_0
# row therefore cannot discriminate on its own: it collapses into the
# Hubble-flow-variance question, which is WP-8 and which nobody has done.
_required = H0_SHOES / _dressed - 1.0
check("required excess is within 2 points of the predicted maximum",
      _required - LOCAL_ENHANCEMENT_MAX, 0.0157, 0.002,
      "arXiv:1009.5855 Sec. 2; arXiv:2112.04510 abstract",
      "needs %.1f%%, predicts up to %.0f%%" % (100 * _required, 100 * LOCAL_ENHANCEMENT_MAX))

# C4. The predicted local value, if the full 17% applied at the calibration
# scale. Stated so the gap that remains is explicit and small.
_predicted_local = _dressed * (1 + LOCAL_ENHANCEMENT_MAX)
check("dressed H_0 boosted by the full predicted 17%",
      _predicted_local, 72.1, 0.15,
      "arXiv:1009.5855 Sec. 2; arXiv:1306.3208 table",
      "%.2f against the measured 73.04 +/- 1.04, a gap of %.2f sigma"
      % (_predicted_local, (H0_SHOES - _predicted_local) / H0_SHOES_ERR))

# C5. That residual gap, stated as a number so it is not glossed. Under 1
# sigma means the H_0 objection is not settled either way by this arithmetic:
# it means the comparison requires the WP-8 calculation to decide.
check("residual gap after the full predicted boost, in SH0ES sigma",
      (H0_SHOES - _predicted_local) / H0_SHOES_ERR, 0.93, 0.02,
      "arXiv:1009.5855 Sec. 2; arXiv:2112.04510 abstract",
      "under 1 sigma: not a kill and not a rescue, a referral to WP-8")


# ---------------------------------------------------------------------------
# A discrepancy found between two published statements of the same equation
# ---------------------------------------------------------------------------
#
# [DNW13] p. 9 writes the dressed/bare relation as
#     H_0 = (4 f_v0^2 + 4 f_v0 + 4) H_bar_0 / [2(2 + f_v0)]
# with 4 f_v0 in the middle term, where [SW11] Eq. (17) and [DES] Eq. (49)
# both have f_v0. The forms are not equivalent and only one reproduces the
# same paper's own published dressed H_0 of 61.7 from its own H_bar_0 of 50.1.
# Recorded as a check so the resolution is arithmetic rather than asserted.
# This is a transcription question about the literature, not a result.

def dressed_from_bare_dnw_asprinted(f, h_bar):
    """The middle term as it appears in the [DNW13] text: 4 f_v0, not f_v0."""
    return (4 * f**2 + 4 * f + 4) * h_bar / (2 * (2 + f))


check("the [SW11]/[DES] form reproduces 61.7, as published",
      dressed_from_bare(FV0_CMB, H_BAR_0), 61.7, 0.15,
      "arXiv:1009.5855 Eq. (17); arXiv:2406.05048 Eq. (49)")

check("the as-printed [DNW13] middle term does not",
      dressed_from_bare_dnw_asprinted(FV0_CMB, H_BAR_0), 80.98, 0.1,
      "arXiv:1306.3208 p. 9",
      "gives %.2f, not 61.7: either a typo in that line or a PDF extraction "
      "artefact. The f_v0 form is the one used everywhere downstream."
      % dressed_from_bare_dnw_asprinted(FV0_CMB, H_BAR_0))


# ---------------------------------------------------------------------------
# Part D. The one method timescape itself named as like-for-like
# ---------------------------------------------------------------------------
#
# Added in cycle 4 of 2026-11-05, closing the follow-up this script's first
# version left open. [SW11] Sec. 2 does not only exclude the distance ladder;
# it names a method it regards as satisfying its own criterion, because it is
# not calibrated below z = 0.033: strong-lens time delays. [SW11] cites a
# then-current value of H_0 = 62 (+6/-4) from Courbin et al. (2010), which sits
# comfortably inside its admissible band of 57 to 68.
#
# That comparator has since moved, and the modern values were fetched rather
# than left as leads:
#
#   [W20]  Wong et al., "H0LiCOW XIII. A 2.4% measurement of H_0 from lensed
#          quasars", arXiv:1907.04869, MNRAS 498 (2020) 1420,
#          DOI 10.1093/mnras/stz3094. Six lensed quasars, flat LCDM, deflector
#          mass profile fixed to a parametric form (power law, or stars plus
#          halo). H_0 = 73.3 (+1.7/-1.8). The abstract states the method is
#          "completely independent of both the supernovae and CMB analyses".
#   [B20]  Birrer et al., "TDCOSMO IV: Hierarchical time-delay cosmography",
#          arXiv:2007.02941, A&A 643 (2020) A165,
#          DOI 10.1051/0004-6361/202038861. Replaces the fixed parametric
#          profile with flexible mass models, so the mass-sheet degeneracy is
#          constrained hierarchically by stellar kinematics instead of by the
#          parametric choice. TDCOSMO only, 7 lenses: 74.5 (+5.6/-6.1).
#          TDCOSMO + 33 SLACS lenses, hierarchical: 67.4 (+4.1/-3.2).

TIME_DELAY = [
    # label, H_0, +err, -err, source, what fixes the mass profile
    ("Courbin et al. 2010, as cited by [SW11]", 62.0, 6.0, 4.0,
     "arXiv:1009.5855 Sec. 2", "single lens HE 0435-1223"),
    ("H0LiCOW XIII, 6 lenses", 73.3, 1.7, 1.8,
     "arXiv:1907.04869 abstract", "parametric: power law or stars+halo"),
    ("TDCOSMO only, 7 lenses", 74.5, 5.6, 6.1,
     "arXiv:2007.02941 abstract", "flexible, kinematics-constrained"),
    ("TDCOSMO + SLACS, hierarchical", 67.4, 4.1, 3.2,
     "arXiv:2007.02941 abstract", "flexible, kinematics-constrained"),
]

TS_FLOOR, TS_CEILING = 57.0, 68.0   # [SW11] Sec. 2


def sigma_above_ceiling(h0, err_lo):
    """How far above timescape's own admissible ceiling, in the measurement's
    own lower uncertainty. Negative means inside the band."""
    return (h0 - TS_CEILING) / err_lo


for _label, _h0, _ep, _em, _src, _prof in TIME_DELAY:
    _s = sigma_above_ceiling(_h0, _em)
    _inside = TS_FLOOR <= _h0 <= TS_CEILING
    CHECKS.append((
        True,
        "time-delay H_0: %s" % _label,
        _h0, _h0, 0.0, _src,
        "%.1f (+%.1f/-%.1f), %s; %s the %.0f-%.0f band%s"
        % (_h0, _ep, _em, _prof,
           "INSIDE" if _inside else "OUTSIDE", TS_FLOOR, TS_CEILING,
           "" if _inside else " by %.2f sigma" % _s)))

# The value [SW11] relied on is inside the band; the tightest modern value from
# the same method is outside it at 3 sigma.
check("the comparator [SW11] cited is inside its own admissible band",
      62.0, 62.0, 1e-9, "arXiv:1009.5855 Sec. 2",
      "57 <= 62 <= 68, which is why [SW11] could point to it")
check("H0LiCOW XIII is outside the band, in its own sigma",
      sigma_above_ceiling(73.3, 1.8), 2.94, 0.02,
      "arXiv:1907.04869; arXiv:1009.5855 Sec. 2",
      "the tightest modern value from the method timescape endorsed")

# But the method's own answer is not stable. Relaxing the mass-profile
# assumption moves it by more than the gap to the ceiling, and the
# hierarchical value lands back inside the band. So the endorsed method does
# not settle the question either, and the reason has nothing to do with
# timescape.
_spread = 74.5 - 67.4
check("relaxing the lens mass profile moves H_0 by more than the gap to the ceiling",
      _spread, 7.1, 1e-9,
      "arXiv:2007.02941 abstract",
      "74.5 against 67.4 within one paper, versus a %.1f gap from the "
      "ceiling to H0LiCOW" % (73.3 - TS_CEILING))
check("the hierarchical time-delay value is inside the admissible band",
      67.4, 67.4, 1e-9, "arXiv:2007.02941 abstract",
      "57 <= 67.4 <= 68, at the very top of it")

# And the caveat that stops this being a clean result either way: every
# time-delay H_0 above is inferred assuming flat LCDM. A time-delay distance
# becomes an H_0 only through a distance-redshift relation, so these values are
# calibration-independent but NOT model-independent. Using them against
# timescape needs the inference redone with timescape's relation.
CHECKS.append((True, "time-delay values are calibration- but not model-independent",
               0.0, 0.0, 0.0, "arXiv:1907.04869; arXiv:2007.02941",
               "all assume flat LCDM in converting time-delay distance to "
               "H_0; a timescape comparison needs the inference redone"))


def main():
    width = max(len(c[1]) for c in CHECKS)
    failed = 0
    for ok, name, got, want, tol, source, note in CHECKS:
        if not ok:
            failed += 1
        print("%s  %-*s got %-12s want %-10s  [%s]"
              % ("PASS" if ok else "FAIL", width, name,
                 "%.6g" % got, "%.6g" % want, source))
        if note:
            print("      %s" % note)

    print()
    if failed:
        print("FAIL: %d of %d checks failed. No WP-1 conclusion is quotable "
              "until this passes." % (failed, len(CHECKS)))
        return 1
    print("PASS: %d of %d checks." % (len(CHECKS), len(CHECKS)))
    print()
    print("What this establishes, and only this:")
    print(" 1. The DES joint-fit comparison IS at matched parameter count")
    print("    (k = 1 each), confirmed arithmetically from the published chi2")
    print("    and the paper's own AIC definition, and Delta_AIC = 12.6")
    print("    against timescape once BAO is added.")
    print(" 2. The H_0 comparison is NOT like-for-like on timescape's own")
    print("    stated criterion: SH0ES is Cepheid-calibrated at z < 0.01,")
    print("    below the z = 0.033 scale [SW11] requires, and that is the")
    print("    scale at which [SW11] predicts up to 17% enhancement.")
    print(" 3. The excess needing explanation (18.6%) and the predicted")
    print("    enhancement (17%) are the same size, so the H_0 row cannot")
    print("    decide anything by itself. It refers to WP-8.")
    print()
    print(" 4. The one method timescape named as like-for-like, strong-lens")
    print("    time delays, now gives 67.4 to 74.5 depending on how the lens")
    print("    mass profile is treated. The tightest value is 2.9 sigma above")
    print("    timescape's own ceiling; the hierarchical value is just inside")
    print("    it. So the endorsed method does not settle it either, for a")
    print("    reason internal to lensing. And all of these assume flat LCDM")
    print("    in the inference, so none is model-independent.")
    print()
    print("K1 does not fire. Its first limb requires BOTH comparisons")
    print("like-for-like; the H_0 one is not. Its second limb requires WP-2,")
    print("which is out of scope for the standing loop and unstarted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
