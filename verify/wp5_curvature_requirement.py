#!/usr/bin/env python3
"""WP-5: the void curvature timescape requires, in normalisation-free terms.

    python verify/wp5_curvature_requirement.py

Exits 0 if every check passes, 1 otherwise. Replaces what queued Maple job
002 was meant to compute. verify/maple_job_design_checks.py D2-D4 shows why
job 002 cannot answer the question: its k_v carries the arbitrary
normalisation of a_v, and it used the dressed H_0 where the bare one belongs.

I1  Identity. From Omega_k_bar = -k_v f_vi^(2/3) f_v^(1/3) / (abar^2 Hbar^2)
    and the partition f_v^(1/3) abar = f_vi^(1/3) a_v (arXiv:0709.0732,
    definition before Eq. 4, and the partition at Eq. 1):
        Omega_k_bar = f_v * Omega_k_v * (H_v / Hbar)^2
    with Omega_k_v = -k_v / (a_v^2 H_v^2), the void phase's own curvature
    parameter. Checked numerically for random inputs.
I2  Tracker. h_r = H_w/H_v = 2/3 (arXiv:0709.0732 Eq. 7 with tracker h_r)
    gives H_v/Hbar = 3/(2+f_v). Substituting this in I1 reproduces the
    published Omega_k_bar = 9 f_v/(2+f_v)^2 if and only if Omega_k_v = 1.
    So the requirement is that the voids are exactly empty and pure curvature:
    Milne.
I3  Physical curvature radius required, R_v = c / (H_v sqrt(Omega_k_v)),
    with the bare Hbar_0 = 50.1 +/- 1.7 km/s/Mpc ([DNW13], via
    findings/WP-1-comparability.md) at the published f_v0 = 0.695
    (+0.041/-0.051) and at the spread 0.550 and 0.791 (Run 01 T13).
I4  Curvature provided by voids holding a fraction M_v of all matter, in the
    job-003 model (separately Friedmann phases, EdS walls, open voids):
    Omega_k_v = 1 - Omega_m_v at f_v = 0.695, by direct integration.
"""

import sys

import numpy as np
from scipy.integrate import solve_ivp

C_KMS = 299792.458
CHECKS = []


def check(name, ok, detail):
    CHECKS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


# I1
rng = np.random.default_rng(1)
worst = 0.0
for _ in range(1000):
    kv = -rng.uniform(1e-6, 1e2)
    fvi, fv = sorted(rng.uniform(1e-6, 0.99, 2))
    abar, Hbar, Hv = rng.uniform(0.1, 10, 3)
    av = abar * (fv / fvi) ** (1 / 3)  # partition
    lhs = -kv * fvi ** (2 / 3) * fv ** (1 / 3) / (abar**2 * Hbar**2)
    omk_v = -kv / (av**2 * Hv**2)
    rhs = fv * omk_v * (Hv / Hbar) ** 2
    worst = max(worst, abs(lhs - rhs) / abs(lhs))
check("I1 Omega_k_bar = f_v Omega_k_v (H_v/Hbar)^2", worst < 1e-12, f"max relative error {worst:.1e} over 1000 draws")

# I2
f = np.linspace(0.001, 0.999, 999)
hv_over_hbar = 1 / (f + (1 - f) * (2 / 3))  # Hbar = f H_v + (1-f) H_w, H_w = (2/3) H_v
check("I2a tracker H_v/Hbar = 3/(2+f)", np.max(np.abs(hv_over_hbar - 3 / (2 + f))) < 1e-14, "Eq. 4 with h_r = 2/3")
omk_needed_v = (9 * f / (2 + f) ** 2) / (f * hv_over_hbar**2)
check("I2b tracker Omega_k_bar requires Omega_k_v = 1 exactly", np.max(np.abs(omk_needed_v - 1)) < 1e-12,
      f"max |Omega_k_v - 1| = {np.max(np.abs(omk_needed_v - 1)):.1e} for f_v in (0.001, 0.999)")


# I3
def r_required(fv0, hbar0):
    hv = 3 * hbar0 / (2 + fv0)
    return C_KMS / hv  # Mpc, Omega_k_v = 1


r0 = r_required(0.695, 50.1)
rs = {fv: r_required(fv, 50.1) for fv in (0.550, 0.644, 0.736, 0.791)}
rh = [r_required(0.695, h) for h in (48.4, 51.8)]
print(f"  R_v required at f_v0=0.695, Hbar0=50.1: {r0:.1f} Mpc "
      f"(Hbar0 48.4..51.8: {min(rh):.1f}..{max(rh):.1f}; "
      + ", ".join(f"f_v0={k}: {v:.1f}" for k, v in rs.items()) + ")")
check("I3 required radius is the void Hubble radius, 5.0-5.6 Gpc across the published range",
      all(5000 < r < 5600 for r in [r0, *rh, *rs.values()]) and abs(r0 - 5375.0) < 2,
      f"{r0:.1f} Mpc; factor across the f_v0 spread {rs[0.791] / rs[0.550]:.3f}, not the 2 that would make "
      f"the requirement ill-defined (job 002 JOB.md)")


# I4
def omega_m_v_at(M, fv_target=0.695):
    if M == 0:
        return 0.0  # empty voids: no matter, Omega_m_v = 0 identically
    C = (4 / 9) * M / (1 - M)

    def rhs(s, y):
        t = np.exp(s)
        aw, av = np.exp(y)
        return [t * np.sqrt((4 / 9) / aw**3), t * np.sqrt(C / av**3 + 1 / av**2)]

    t0 = 1e-9
    y0 = [np.log(t0 ** (2 / 3)), np.log((9 * C / 4) ** (1 / 3) * t0 ** (2 / 3))]
    sol = solve_ivp(rhs, (np.log(t0), np.log(1e6)), y0, rtol=1e-12, atol=1e-14, dense_output=True, method="DOP853")
    s = np.linspace(np.log(t0), np.log(1e6), 200001)
    aw, av = np.exp(sol.sol(s))
    fv = av**3 / (aw**3 + av**3)
    om = (C / av**3) / (C / av**3 + 1 / av**2)
    return float(np.interp(fv_target, fv, om))


rows = {M: omega_m_v_at(M) for M in (0.0, 0.0265, 0.07, 0.0852, 0.270)}
for M, om in rows.items():
    print(f"  M_v={M:<6} Omega_m_v(f_v=0.695)={om:.6f}  Omega_k_v provided={1 - om:.6f}  "
          f"R_v/R_required={1 / np.sqrt(1 - om):.5f}")
check("I4a matches job 003's Omega_m_v at delta_v=-0.90 (M_v=0.0695)",
      abs(omega_m_v_at(0.695 * 0.10) - 0.015424) < 2e-5, f"{omega_m_v_at(0.0695):.6f} vs RESULT 0.015424")
check("I4b at the observed-order M_v = 0.07, voids supply >98% of the required curvature",
      1 - rows[0.07] > 0.98, f"Omega_k_v = {1 - rows[0.07]:.4f}")

print(f"\n{sum(CHECKS)}/{len(CHECKS)} checks passed")
sys.exit(0 if all(CHECKS) else 1)
