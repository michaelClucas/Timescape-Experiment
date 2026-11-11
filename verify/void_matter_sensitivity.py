#!/usr/bin/env python3
"""Independent numeric check of job 003 (void matter as the density refinement of T6).

    python verify/void_matter_sensitivity.py

Exits 0 if every check passes, 1 otherwise. Shares no code with SymPy or with
maple/jobs/003-void-matter-refinement/job.py. It integrates each phase's
Friedmann equation with scipy's solve_ivp, builds the volume average, the
wall lapse and the dressed Hubble rate from the integrated arrays, and takes
every derivative by finite differences in ln t. It does not use the job's
parametric open-FRW solution, its lambdified expressions, or its
root-finding over C. Each case's C comes from the mass identity alone.

Model (job 003 JOB.md): walls flat EdS, H_w^2 = (4/9)/a_w^3; voids open
FRW, H_v^2 = C/a_v^3 + 1/a_v^2; volume abar^3 = a_w^3 + a_v^3 (R = 1);
gamma = Hbar/H_w (arXiv:0709.0732 Eq. 7); dressed H = gamma Hbar - dgamma/dt;
dressed q = -1 - gamma (dH/dt)/H^2.

Mass identity, checked here rather than assumed: each phase conserves its
own matter, and at early times both phases have the same density. So the
void phase's share of all matter is M_v = f_v,early = (9C/4)/(1 + 9C/4), and
at any later epoch 1 + delta_v = M_v / f_v exactly.
"""

import sys

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

RESULT = {  # maple/results/003-void-matter-refinement/RESULT.txt, VOIDMATTER rows
    -0.999: (-0.042888, 0.588692, -0.035603),
    -0.990: (-0.041826, 0.601682, -0.032626),
    -0.950: (-0.037980, 0.642279, -0.020855),
    -0.900: (-0.034244, 0.680228, -0.006557),
    -0.850: (-0.031203, 0.711450, +0.008064),
    -0.800: (-0.028633, 0.738427, +0.023315),
}
FV0 = 0.695
CHECKS = []


def check(name, ok, detail):
    CHECKS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


def run(C, t0=1e-9, t1=1e6, n=400001):
    """Integrate both phases in y = ln a against s = ln t; return arrays."""
    def rhs(s, y):
        t = np.exp(s)
        aw, av = np.exp(y)
        hw = np.sqrt((4 / 9) / aw**3)
        hv = np.sqrt(C / av**3 + 1 / av**2)
        return [t * hw, t * hv]

    # early-time matter-dominated series: a = (9 C_i / 4)^(1/3) t^(2/3)
    av0 = (9 * C / 4) ** (1 / 3) * t0 ** (2 / 3) if C > 0 else t0
    y0 = [np.log(t0 ** (2 / 3)), np.log(av0)]
    s = np.linspace(np.log(t0), np.log(t1), n)
    sol = solve_ivp(rhs, (s[0], s[-1]), y0, t_eval=s, rtol=1e-12, atol=1e-14, method="DOP853")
    t = np.exp(s)
    aw, av = np.exp(sol.y)
    hw = np.sqrt((4 / 9) / aw**3)
    hv = np.sqrt(C / av**3 + 1 / av**2)
    fv = av**3 / (aw**3 + av**3)
    hb = fv * hv + (1 - fv) * hw
    g = hb / hw
    ds = s[1] - s[0]
    H = g * hb - np.gradient(g, ds) / t
    q = -1 - g * (np.gradient(H, ds) / t) / H**2
    rv, rw = C / av**3, (4 / 9) / aw**3
    dv = rv / (fv * rv + (1 - fv) * rw) - 1
    return fv, q, dv


def stats(fv, q):
    m = (fv > 0.3) & (fv < 0.999)
    F, Q = fv[m], q[m]
    i = int(np.argmin(Q))
    sc = np.where(np.diff(np.sign(Q)) != 0)[0]
    fs = np.interp(0.0, [Q[sc[0]], Q[sc[0] + 1]], [F[sc[0]], F[sc[0] + 1]]) if len(sc) else np.nan
    q0 = np.interp(FV0, F, Q)
    return Q[i], fs, q0


def c_from_mass(M):
    return (4 / 9) * M / (1 - M)


# 1. empty-void limit reproduces Eq. (26)
fv, q, _ = run(0.0)
eq26 = -(1 - fv) * (8 * fv**3 + 39 * fv**2 - 12 * fv - 8) / (4 + fv + 4 * fv**2) ** 2
m = (fv > 0.05) & (fv < 0.995)
check("empty voids reproduce Eq. (26) pointwise", np.max(np.abs(q[m] - eq26[m])) < 1e-6,
      f"max |q - Eq26| = {np.max(np.abs(q[m] - eq26[m])):.2e}")
qm, fs, q0 = stats(fv, q)
check("empty q_min = -0.0430145 (published -0.043)", abs(qm + 0.0430145) < 1e-5, f"{qm:.7f}")
check("empty sign change = 0.586708 (published 0.5867)", abs(fs - 0.586708) < 1e-5, f"{fs:.6f}")

# 2. mass identity
for M in (0.01, 0.07, 0.2):
    fv, q, dv = run(c_from_mass(M))
    m = (fv > 0.3) & (fv < 0.99)
    err = np.max(np.abs((1 + dv[m]) - M / fv[m]))
    check(f"mass identity 1+delta_v = M_v/f_v at M_v={M}", err < 1e-8, f"max error {err:.2e}")

# 3. each job-003 row, with C set from the mass identity only
for delta, (qm_j, fs_j, q0_j) in RESULT.items():
    M = FV0 * (1 + delta)
    fv, q, dv = run(c_from_mass(M))
    qm, fs, q0 = stats(fv, q)
    d_here = np.interp(FV0, fv[(fv > 0.3) & (fv < 0.999)], dv[(fv > 0.3) & (fv < 0.999)])
    ok = abs(qm - qm_j) < 2e-4 and abs(fs - fs_j) < 2e-4 and abs(q0 - q0_j) < 2e-4 and abs(d_here - delta) < 1e-6
    check(f"job 003 row delta_v={delta:+.3f}", ok,
          f"q_min {qm:+.6f} vs {qm_j:+.6f}; sign {fs:.6f} vs {fs_j:.6f}; q(fv0) {q0:+.6f} vs {q0_j:+.6f}")

# 4. the threshold where the dressed q at f_v = 0.695 changes sign
def q0_of_delta(d):
    fv, q, _ = run(c_from_mass(FV0 * (1 + d)), n=200001)
    return stats(fv, q)[2]


dz = brentq(q0_of_delta, -0.95, -0.80, xtol=1e-6)
check("q(f_v=0.695) = 0 at delta_v = -0.877361 (job 003)", abs(dz + 0.877361) < 5e-4, f"{dz:+.6f}")
print(f"  -> void mass fraction at that threshold: M_v = {FV0 * (1 + dz):.4f}")

print(f"\n{sum(CHECKS)}/{len(CHECKS)} checks passed")
sys.exit(0 if all(CHECKS) else 1)
