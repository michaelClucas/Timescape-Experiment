#!/usr/bin/env python3
"""Show, without Maple, what queued Maple jobs 001 and 002 can and cannot measure.

    python verify/maple_job_design_checks.py

Exits 0 if every check passes, 1 otherwise. It reproduces each job's own
formulas as written in maple/jobs/00N-*/job.mpl at the sha the issues name,
and checks four properties of the jobs' design. None of this says anything
about timescape. It says what the two jobs would have returned had a runner
existed, and why those returns would not have answered WP-6 or WP-5.

D0  Job 001 as written cannot run. Omk_two ends in "* fv / fv", which
    cancels, so it returns 9/(2+fv)^2 * g(s) and drops the factor fv that
    Omega_k_bar = 9 fv/(2+fv)^2 carries. q_two then asks fsolve for x with
    Omk_pub(x) = Omk_pub(fv)/fv > 1, and Omk_pub < 1 on (0, 1): no root for
    any fv, so every line built on q_two errors or returns unevaluated.
D1  With the factor restored, job 001's q_two(fv, s) is q_pub evaluated at a re-mapped fv. A re-mapping
    of the argument cannot change a function's minimum value, so q_min(s) is
    q_min(0) by construction for every s. The job would report "T6 is not
    load-bearing" whatever the physics. It also breaks its own symmetry
    expectation in the other observable: the sign-change fv moves at O(s^2).
D2  Job 002's R_curv = |k_v|^(-1/2) depends on the arbitrary normalisation
    of a_v through f_vi: R_curv is proportional to f_vi^(+1/3) exactly. The
    normalisation-free quantity is the void's present Gaussian curvature
    K_v = k_v / a_v0^2, with a_v0 = (f_v0 / f_vi)^(1/3) abar_0 from the
    partition f_v^(1/3) abar = f_vi^(1/3) a_v (arXiv:0709.0732).
D3  Job 002 sets Hbar0 to the DRESSED 61.7 km/s/Mpc. The definition it
    inverts uses the BARE Hbar, which findings/WP-1-comparability.md gives
    as 50.1 +/- 1.7 km/s/Mpc at f_v0 = 0.695 ([DNW13]).
D4  Job 002's delta_v_implied returns a value outside (-1, 0), the range its
    own JOB.md says means "the setup is wrong".
"""

import sys

import numpy as np
from scipy.optimize import brentq, minimize_scalar

CHECKS = []


def check(name, ok, detail):
    CHECKS.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


# --- Job 001 formulas, transcribed from maple/jobs/001-two-phase-sensitivity/job.mpl
def q_pub(f):
    return -(1 - f) * (8 * f**3 + 39 * f**2 - 12 * f - 8) / (4 + f + 4 * f**2) ** 2


def omk_pub(f):
    return 9 * f / (2 + f) ** 2


def omk_two_as_written(fv, s, c_resp=1.0):
    """Transcribed literally, including the trailing '* fv / fv'."""
    f1 = (fv / 2) * (1 + c_resp * s)
    f2 = (fv / 2) * (1 - c_resp * s)
    h = 0.5 ** (2 / 3)
    return (9 / (2 + fv) ** 2) * (
        ((1 + s) * h * f1 ** (1 / 3) + (1 - s) * h * f2 ** (1 / 3))
        / (h * (fv / 2) ** (1 / 3) * 2)
    ) * fv / fv


def omk_two(fv, s, c_resp=1.0):
    """The evident intent: the same, times fv, so s = 0 returns omk_pub(fv)."""
    f1 = (fv / 2) * (1 + c_resp * s)
    f2 = (fv / 2) * (1 - c_resp * s)
    h = 0.5 ** (2 / 3)
    return (9 / (2 + fv) ** 2) * (
        ((1 + s) * h * f1 ** (1 / 3) + (1 - s) * h * f2 ** (1 / 3))
        / (h * (fv / 2) ** (1 / 3) * 2)
    ) * fv


def q_two(fv, s):
    target = omk_two(fv, s)
    if target >= omk_pub(0.999):
        return np.nan  # job's fsolve range has no root here
    x = brentq(lambda x: omk_pub(x) - target, 0.001, 0.999)
    return q_pub(x)


def qmin_of(fun, lo=0.5, hi=0.95):
    fs = np.linspace(lo, hi, 20001)
    qs = np.array([fun(f) for f in fs])
    i = np.nanargmin(qs)
    r = minimize_scalar(fun, bounds=(fs[max(i - 1, 0)], fs[min(i + 1, len(fs) - 1)]),
                        method="bounded", options={"xatol": 1e-12})
    return r.fun


grid = np.linspace(0.01, 0.99, 99)
need = np.array([omk_two_as_written(f, s) / omk_pub(f) * omk_pub(f) for f in grid for s in (0.0, 0.5)])
check("D0 job 001 as written has no root for q_two", bool(np.all(need > 1.0)),
      f"target Omk_pub(x) ranges {need.min():.4f}..{need.max():.4f}, all above max Omk_pub = 1 on (0,1)")
check("D0 the intended form reduces to the control at s=0",
      max(abs(omk_two(f, 0.0) - omk_pub(f)) for f in grid) < 1e-12, "omk_two(fv, 0) == omk_pub(fv)")

q0 = qmin_of(q_pub)
for s in (0.1, 0.25, 0.5):
    qs = qmin_of(lambda f: q_two(f, s))
    check(f"D1 q_min invariant at s={s}", abs(qs - q0) < 1e-9,
          f"q_min(s)={qs:.10f}, q_min(0)={q0:.10f}")

fs0 = brentq(q_pub, 0.3, 0.9)
fsh = brentq(lambda f: q_two(f, 0.5), 0.3, 0.8)
check("D1 sign-change fv does move", abs(fsh - fs0) > 1e-3,
      f"s=0: {fs0:.6f}, s=0.5: {fsh:.6f} - so the job's two observables disagree "
      f"on whether T6 matters, and only the one it calls 'the interesting number' is blind")

# --- Job 002 formulas, transcribed from maple/jobs/002-curvature-budget-requirement/job.mpl
C_KMS = 299792.458


def kv_req(fv0, fvi, hbar_kms):
    hb = hbar_kms / C_KMS  # 1/Mpc, as the job does it
    return -omk_pub(fv0) * hb**2 / (fvi ** (2 / 3) * fv0 ** (1 / 3))


def r_curv(fv0, fvi, hbar_kms):
    return 1 / np.sqrt(abs(kv_req(fv0, fvi, hbar_kms)))


r1 = r_curv(0.695, 1e-5, 61.7)
r2 = r_curv(0.695, 8e-5, 61.7)
check("D2 R_curv scales as f_vi^(+1/3)", abs(r2 / r1 - 8 ** (1 / 3)) < 1e-12,
      f"R(1e-5)={r1:.4f} Mpc, R(8e-5)={r2:.4f} Mpc, ratio {r2 / r1:.12f} vs 2")

phys = []
for fvi in (1e-6, 1e-5, 1e-4):
    a_v0 = (0.695 / fvi) ** (1 / 3)
    K = kv_req(0.695, fvi, 61.7) / a_v0**2
    phys.append(1 / np.sqrt(abs(K)))
check("D2 physical radius |K_v|^(-1/2) is f_vi-free", np.ptp(phys) < 1e-6 * phys[0],
      f"{phys[0]:.6f} Mpc for f_vi in 1e-6..1e-4 (with the job's wrong Hbar0)")

hbar_bare = 50.1  # findings/WP-1-comparability.md, [DNW13]
gam = 1 + 0.695 / 2
dressed_from_bare = (4 * 0.695**2 + 0.695 + 4) * hbar_bare / (2 * (2 + 0.695))
check("D3 61.7 is the dressed value, not the bare one",
      abs(dressed_from_bare - 61.7) < 0.2 and abs(hbar_bare - 61.7) > 10,
      f"bare 50.1 -> dressed {dressed_from_bare:.2f} (WP-1 relation); job uses 61.7 as bare")

OmM = 4 * (1 - 0.695) / (2 + 0.695) ** 2
x = (1 - omk_pub(0.695)) / OmM
delta_job = x / 0.695 - 1
check("D4 job 002 delta_v_implied leaves (-1, 0)", not (-1 < delta_job < 0),
      f"delta_v_implied = {delta_job:+.6f}")

print(f"\n{sum(CHECKS)}/{len(CHECKS)} checks passed")
sys.exit(0 if all(CHECKS) else 1)
