#!/usr/bin/env python3
"""Independent check of job 004 (spread of void densities at fixed void mass).

    python verify/void_density_spread.py

Exits 0 if every check passes, 1 otherwise. Shares no code with
maple/jobs/004-void-density-spread/job.py. The job integrates ODEs and uses
analytic derivatives. This script uses each void sub-phase's exact
parametric open-FRW solution,
    a = (C/2)(cosh eta - 1),  t = (C/2)(sinh eta - eta)   (K = 1),
inverted for eta at each t by Newton iteration, with EdS walls a_w = t^(2/3).
Every derivative is a finite difference in ln t.
"""

import sys

import numpy as np

RESULT = {  # maple/results/004-void-density-spread/RESULT.txt
    0.00: (-0.034244, 0.680245, -0.006557, -0.900000, -0.900000),
    0.25: (-0.034279, 0.679732, -0.006767, -0.870280, -0.918640),
    0.50: (-0.034409, 0.678017, -0.007485, -0.814907, -0.931494),
    0.90: (-0.035403, 0.668369, -0.011454, -0.363173, -0.945740),
}
FV0, MV = 0.695, 0.0695
CHECKS = []


def check(name, ok, detail):
    CHECKS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


def eta_of_t(t, C):
    """Solve (C/2)(sinh eta - eta) = t for eta, vectorised Newton."""
    eta = np.cbrt(12 * t / C)  # small-eta start: sinh e - e ~ e^3/6
    big = eta > 3
    eta[big] = np.log(4 * t[big] / C + 1)  # large-eta start
    for _ in range(60):
        s = np.where(eta < 1e-2, eta**3 / 6 + eta**5 / 120, np.sinh(eta) - eta)
        g = (C / 2) * s - t
        gp = (C / 2) * (np.cosh(eta) - 1)
        eta = eta - g / gp
    return eta


def run(s):
    C = (4 / 9) * MV / (1 - MV)
    Cv = np.array([C * (1 + s), C * (1 - s)])
    # Step size matters: dressed q needs the THIRD derivative of a(t), and a
    # third finite difference amplifies rounding (~1e-15) by dl^-3. At 400001
    # points (dl = 5.8e-5) that is ~5e-3 of noise and the minimum lands on a
    # spike (first version of this script, 0/4). 20001 points (dl = 1.2e-3)
    # gives ~1e-6 noise and ~1e-6 truncation error.
    lt = np.linspace(np.log(1e-4), np.log(1e6), 20001)
    t = np.exp(lt)
    aw = t ** (2 / 3)
    av = np.array([(c / 2) * (np.cosh(eta_of_t(t, c)) - 1) for c in Cv])
    # early volume share equals mass share: w_i (9 C_i/4) = (MV/2)/(1-MV), wall weight 1
    w = ((MV / 2) / (1 - MV)) / ((9 / 4) * Cv)
    V = aw**3 + (w[:, None] * av**3).sum(axis=0)
    fi = w[:, None] * av**3 / V
    fv = fi.sum(axis=0)
    dl = lt[1] - lt[0]
    Hw = np.gradient(np.log(aw), dl) / t
    Hv = np.array([np.gradient(np.log(a), dl) / t for a in av])
    Hb = (1 - fv) * Hw + (fi * Hv).sum(axis=0)
    g = Hb / Hw
    Hd = g * Hb - np.gradient(g, dl) / t
    q = -1 - g * (np.gradient(Hd, dl) / t) / Hd**2
    rho_w, rho_v = (4 / 9) / aw**3, Cv[:, None] / av**3
    rbar = (1 - fv) * rho_w + (fi * rho_v).sum(axis=0)
    delta = rho_v / rbar - 1
    m = (fv > 0.3) & (fv < 0.999)
    F, Q = fv[m], q[m]
    i = int(np.argmin(Q))
    sc = np.where(np.diff(np.sign(Q)) != 0)[0]
    fs = np.interp(0.0, [Q[sc[0]], Q[sc[0] + 1]], [F[sc[0]], F[sc[0] + 1]])
    return (Q[i], fs, np.interp(FV0, F, Q), np.interp(FV0, F, delta[0][m]), np.interp(FV0, F, delta[1][m]))


for s, want in RESULT.items():
    got = run(s)
    ok = all(abs(a - b) < 2e-4 for a, b in zip(got, want))
    check(f"job 004 SPREAD s={s:.2f}", ok,
          "q_min {:+.6f}/{:+.6f} sign {:.6f}/{:.6f} q0 {:+.6f}/{:+.6f} d1 {:+.6f}/{:+.6f} d2 {:+.6f}/{:+.6f}".format(
              *[x for pair in zip(got, want) for x in pair]))

print(f"\n{sum(CHECKS)}/{len(CHECKS)} checks passed")
sys.exit(0 if all(CHECKS) else 1)
