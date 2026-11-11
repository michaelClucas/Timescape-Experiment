#!/usr/bin/env python3
"""WP-6: from the measured void GALAXY share to the void MATTER share, under linear bias.

    python verify/wp6_bias_mapping.py

Exits 0 if every check passes, 1 otherwise.

Inputs, from verify/wp6_void_galaxy_share.py (Planck 2018, VAST mask
convention), inside VoidFinder voids filling f_v,meas = 0.6228 (WP-4), for
the M_r < -20 volume-limited sample:
  interior (cut 5a)            11824 / 194124 = 0.0609   <- headline
  surface-inclusive (cut 5)    33342 / 194124 = 0.1718   <- upper bracket
The surface-inclusive count includes the four WALL galaxies that bound each
VoidFinder sphere (arXiv:2202.01226 Sec. 2.1: a sphere "is grown ... until
it is bounded by four galaxies", and "the void-growing step in VoidFinder
explicitly stops once wall galaxies are encountered"). It reproduces VAST's
quoted "~18% of the galaxies" (Sec. 3.2) and is NOT the void interior.

Bias, sourced (verbatim quotes in findings/WP-6, the bias section):
  Zehavi et al. 2011 (arXiv:1005.2413, ApJ 736, 59), HOD table:
  b_g(M_r<-20) x (sigma_8/0.8) = 1.20 +/- 0.01; neighbours 1.14 (-19.5), 1.29 (-20.5).
  At Planck sigma_8 = 0.811: b = 1.20 x 0.8/0.811 = 1.184.
  Pollina et al. 2017 (arXiv:1610.06176): the tracer-matter relation around
  voids is linear, with slope above the large-scale bias for small voids.
  Scaling by their small-void factor gives ~1.4-1.5. That transfer is
  SPECULATIVE (different finder, tracer density and void sizes).

Premise, named: delta_gal = b * delta_matter inside voids. Pollina 2017 does
not show in its text that this holds at delta_g ~ -0.9.
"""

import sys

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

FV_MEAS, FV0, N_TOT = 0.6228, 0.695, 194124
SHARES = {"interior": 11824 / N_TOT, "surface-incl": 33342 / N_TOT}
BIAS = [("none", 1.0), ("Zehavi -19.5", 1.14), ("Zehavi -20 @Planck s8", 1.20 * 0.8 / 0.811),
        ("Zehavi -20", 1.20), ("Zehavi -20.5", 1.29), ("Pollina-scaled lo (spec.)", 1.4),
        ("Pollina-scaled hi (spec.)", 1.5)]
EFFECT = 0.0430145  # |q_min| of the tracker
CHECKS = []


def check(name, ok, detail):
    CHECKS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


def m_of(share, b):
    return FV_MEAS * (1 + (share / FV_MEAS - 1) / b)


def model(M, n=200001):
    """q_min, dressed q at f_v = 0.695, and the f_v of q's sign change, for void matter share M."""
    C = (4 / 9) * M / (1 - M)

    def rhs(s, y):
        t = np.exp(s)
        aw, av = np.exp(y)
        return [t * np.sqrt((4 / 9) / aw**3), t * np.sqrt(C / av**3 + 1 / av**2)]

    t0 = 1e-9
    y0 = [np.log(t0 ** (2 / 3)), np.log((9 * C / 4) ** (1 / 3) * t0 ** (2 / 3))]
    s = np.linspace(np.log(t0), np.log(1e6), n)
    sol = solve_ivp(rhs, (s[0], s[-1]), y0, t_eval=s, rtol=1e-12, atol=1e-14, method="DOP853")
    t = np.exp(s)
    aw, av = np.exp(sol.y)
    hw, hv = np.sqrt((4 / 9) / aw**3), np.sqrt(C / av**3 + 1 / av**2)
    fv = av**3 / (aw**3 + av**3)
    hb = fv * hv + (1 - fv) * hw
    g = hb / hw
    ds = s[1] - s[0]
    H = g * hb - np.gradient(g, ds) / t
    q = -1 - g * (np.gradient(H, ds) / t) / H**2
    m = (fv > 0.3) & (fv < 0.999)
    F, Q = fv[m], q[m]
    sc = np.where(np.diff(np.sign(Q)) != 0)[0]
    fs = float(np.interp(0.0, [Q[sc[0]], Q[sc[0] + 1]], [F[sc[0]], F[sc[0] + 1]])) if len(sc) else float("nan")
    return float(Q.min()), float(np.interp(FV0, F, Q)), fs


qmin0 = model(1e-12)[0]
check("tracker limit", abs(qmin0 + EFFECT) < 2e-6, f"q_min = {qmin0:.7f}")

table = {}
for share_name, share in SHARES.items():
    dg = share / FV_MEAS - 1
    print(f"\n  galaxy share [{share_name}] = {share:.4f}, delta_g = {dg:+.4f}")
    for label, b in BIAS:
        M = m_of(share, b)
        qm, q0, fs = model(M)
        table[(share_name, label)] = (b, M, qm, q0, fs)
        print(f"    b={b:.3f} {label:26s} M_v={M:.4f} q_min={qm:+.5f} shift={qm - qmin0:+.5f} "
              f"({100 * (qm - qmin0) / EFFECT:4.1f}% of the effect) q(0.695)={q0:+.5f} onset f_v={fs:.4f}")
    b_zero = brentq(lambda b: m_of(share, b) - 0.0852, 0.5, 5.0)
    b_k4 = brentq(lambda b: m_of(share, b) - 0.270, 0.5, 20.0)
    print(f"    q(0.695) = 0 needs b > {b_zero:.4f}; K4 (M_v = 0.270) needs b > {b_k4:.4f}")
    table[(share_name, "thresholds")] = (b_zero, b_k4)

bz_i, bk_i = table[("interior", "thresholds")]
bz_s, bk_s = table[("surface-incl", "thresholds")]
check("interior: q(f_v0)=0 threshold b* just above 1", 1.0 < bz_i < 1.1, f"b* = {bz_i:.4f}")
check("interior: K4 threshold b = 1.593", abs(bk_i - 1.593) < 2e-3, f"{bk_i:.4f}")
row = table[("interior", "Zehavi -20 @Planck s8")]
check("headline (interior, b=1.184): M_v, q(0.695), shift", 0.14 < row[1] < 0.16 and row[3] > 0 and 0.01 < row[2] - qmin0 < 0.02,
      f"M_v={row[1]:.4f}, q(0.695)={row[3]:+.4f}, q_min shift={row[2] - qmin0:+.4f}, onset f_v={row[4]:.4f}")
check("surface-inclusive K4 threshold lies between the Zehavi -20 and -20.5 biases", 1.20 < bk_s < 1.29, f"b = {bk_s:.4f}")

print(f"\n{sum(CHECKS)}/{len(CHECKS)} checks passed")
sys.exit(0 if all(CHECKS) else 1)
