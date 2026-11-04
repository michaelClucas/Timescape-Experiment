#!/usr/bin/env python3
"""Reproduce the published timescape tracker numbers from the paper's equations.

    python verify/tracker_relations.py

Exits 0 if every check passes, 1 otherwise. Runs in under a second.

Why this exists: before any Maple job builds on these relations, we need to
know our transcription of them is right. Every number below is published, so
this script discovers nothing. It de-risks everything downstream, and it is
the independent numeric route against which Maple jobs 001 and 002 are
checked, sharing no code with them.

All equations from Wiltshire, "Exact solution to the averaging problem in
cosmology", arXiv:0709.0732, Phys. Rev. Lett. 99:251101 (2007), with the
equation numbers given per function. Verified against the paper's full text,
not against a secondary quotation.
"""

import sys

import numpy as np
from scipy.optimize import brentq, minimize_scalar


def q_dressed(f):
    """Dressed deceleration parameter, wall observers. arXiv:0709.0732 Eq. (26)."""
    return -(1 - f) * (8 * f**3 + 39 * f**2 - 12 * f - 8) / (4 + f + 4 * f**2) ** 2


def q_bare(f):
    """Volume-average deceleration parameter. arXiv:0709.0732, after Eq. (26)."""
    return 2 * (1 - f) ** 2 / (2 + f) ** 2


def omega_m_bare(f):
    """Bare matter density, tracker. arXiv:0709.0732, tracker parameter values."""
    return 4 * (1 - f) / (2 + f) ** 2


def omega_k_bare(f):
    """Bare curvature density, tracker. arXiv:0709.0732, tracker parameter values."""
    return 9 * f / (2 + f) ** 2


def omega_q_bare(f):
    """Bare backreaction, from the budget Omega_M + Omega_k + Omega_Q = 1, Eq. (5)."""
    return 1 - omega_m_bare(f) - omega_k_bare(f)


def gamma_lapse(f):
    """Relative lapse, tracker (h_r = 2/3). arXiv:0709.0732 Eq. (7), after Eq. (19)."""
    return 1 + f / 2


CHECKS = []


def check(name, got, want, tol, source):
    ok = abs(got - want) <= tol
    CHECKS.append((ok, name, got, want, tol, source))
    return ok


def main():
    # 1. Dressed q changes sign at f_v = 0.5867
    check("f_v at dressed q sign change",
          brentq(q_dressed, 0.3, 0.9), 0.5867, 5e-5,
          "arXiv:0709.0732, after Eq. (26)")

    # 2-3. Apparent acceleration is largest at f_v = 0.7736, where q = -0.043
    m = minimize_scalar(q_dressed, bounds=(0.5, 0.99), method="bounded")
    check("f_v at dressed q minimum", m.x, 0.7736, 5e-4,
          "arXiv:0709.0732, after Eq. (26)")
    check("dressed q minimum", m.fun, -0.043, 5e-4,
          "arXiv:0709.0732, after Eq. (26); fitted q_0 = -0.043 "
          "(+0.004/-0.000), arXiv:1706.07236 abstract")

    # 4. Bare q_bar is positive at all times: no volume acceleration.
    f = np.linspace(1e-9, 1 - 1e-9, 2_000_001)
    qb_min = q_bare(f).min()
    CHECKS.append((bool(qb_min > 0), "q_bar > 0 everywhere on (0,1)", qb_min, 0.0,
                   0.0, "arXiv:1311.3787 Sec. 5.3, no volume acceleration"))

    # 5-6. The fitted bare budget at f_v0 = 0.695.
    check("Omega_Q_bar at f_v0 = 0.695", omega_q_bare(0.695), -0.0293, 2e-4,
          "arXiv:1311.3787 Table 1")
    check("Omega_k_bar at f_v0 = 0.695", omega_k_bare(0.695), 0.862, 1e-3,
          "arXiv:1311.3787 Table 1")

    # 7. |Omega_Q_bar| <= 0.042 at all times.
    mq = minimize_scalar(omega_q_bare, bounds=(0.01, 0.99), method="bounded")
    CHECKS.append((bool(abs(mq.fun) <= 0.042), "|Omega_Q_bar| <= 0.042 on (0,1)",
                   abs(mq.fun), 0.042, 0.0, "arXiv:1311.3787 Sec. 5.3"))

    # 8. Einstein-de Sitter limit as f_v -> 0: q_bar -> 1/2, Omega_M -> 1,
    #    Omega_Q -> 0. Not a published claim; a consistency requirement.
    check("q_bar -> 1/2 as f_v -> 0", q_bare(1e-12), 0.5, 1e-9, "EdS limit")
    check("Omega_M_bar -> 1 as f_v -> 0", omega_m_bare(1e-12), 1.0, 1e-9, "EdS limit")
    check("Omega_Q_bar -> 0 as f_v -> 0", omega_q_bare(1e-12), 0.0, 1e-9, "EdS limit")

    # 9. Lapse at the fitted void fraction. The 35-38% figure in the
    #    literature is the cumulative wall/volume clock-rate difference.
    check("gamma_lapse at f_v0 = 0.695", gamma_lapse(0.695), 1.3475, 1e-4,
          "arXiv:0709.0732 Eq. (7) with h_r = 2/3")

    width = max(len(c[1]) for c in CHECKS)
    failed = 0
    for ok, name, got, want, tol, source in CHECKS:
        if not ok:
            failed += 1
        print("%s  %-*s got %-14s want %-10s  [%s]"
              % ("PASS" if ok else "FAIL", width, name,
                 "%.6g" % got, "%.6g" % want, source))

    print()
    if failed:
        print("FAIL: %d of %d checks failed. Do not queue Maple jobs 001 or 002 "
              "until this passes: they use these relations." % (failed, len(CHECKS)))
        return 1
    print("PASS: %d of %d checks. The transcription of arXiv:0709.0732 used by "
          "Maple jobs 001 and 002 reproduces every published value." % (len(CHECKS), len(CHECKS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
