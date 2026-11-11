#!/usr/bin/env python3
"""WP-6: from the measured void GALAXY share to the void MATTER share, under linear bias.

    python verify/wp6_bias_mapping.py

Exits 0 if every check passes, 1 otherwise.

Input: verify/wp6_void_galaxy_share.py, cut 5a, Planck 2018, VAST mask
convention: M_v,gal = 11824 / 194124 of the M_r < -20 volume-limited
sample, inside VoidFinder voids that fill f_v,meas = 0.6228 of the volume
(WP-4).

Premise, named and NOT established here: linear bias inside voids,
delta_gal = b * delta_matter. Then delta_m = delta_g / b and
M_v = f_v,meas (1 + delta_m). The bias value and whether linearity holds at
delta ~ -0.9 are sourced separately (findings/WP-6, the bias section). This
script only maps b to M_v and to the dressed-q quantities of job 003's model
(separately Friedmann phases; the integration is the same as
verify/void_matter_sensitivity.py's).
"""

import sys

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

N_VOID, N_TOT, FV_MEAS, FV0 = 11824, 194124, 0.6228, 0.695
M_GAL = N_VOID / N_TOT
DELTA_G = M_GAL / FV_MEAS - 1
CHECKS = []


def check(name, ok, detail):
    CHECKS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


def m_of_b(b):
    return FV_MEAS * (1 + DELTA_G / b)


def model(M, n=200001):
    """q_min and dressed q at f_v = 0.695 for void matter share M."""
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
    return float(q[m].min()), float(np.interp(FV0, fv[m], q[m]))


print(f"  measured: M_v,gal = {M_GAL:.4f}, delta_g = {DELTA_G:+.4f}")
check("input matches wp6_void_galaxy_share.py headline", abs(M_GAL - 0.0609) < 5e-5 and abs(DELTA_G + 0.9022) < 5e-5,
      f"{M_GAL:.4f}, {DELTA_G:+.4f}")

qmin0 = model(1e-12)[0]
rows = []
for b in (1.0, 1.05, 1.1, 1.2, 1.3, 1.5):
    M = m_of_b(b)
    qm, q0 = model(M)
    rows.append((b, M, qm, q0))
    print(f"  b={b:<5} delta_m={DELTA_G / b:+.4f} M_v={M:.4f} q_min={qm:+.5f} (shift {qm - qmin0:+.5f}) "
          f"q(f_v=0.695)={q0:+.5f}")

b_zero = brentq(lambda b: m_of_b(b) - 0.0852, 1.0, 3.0)
b_k4 = brentq(lambda b: m_of_b(b) - 0.270, 1.0, 20.0)
print(f"  q(f_v0) = 0 needs M_v = 0.0852, i.e. b > {b_zero:.4f}; K4 (M_v = 0.270) needs b > {b_k4:.3f}")
check("b = 1 reproduces the galaxy share itself", abs(rows[0][1] - M_GAL) < 1e-12, f"{rows[0][1]:.4f}")
check("q(f_v0) = 0 threshold in b lies just above 1", 1.0 < b_zero < 1.1, f"b* = {b_zero:.4f}")

print(f"\n{sum(CHECKS)}/{len(CHECKS)} checks passed")
sys.exit(0 if all(CHECKS) else 1)
