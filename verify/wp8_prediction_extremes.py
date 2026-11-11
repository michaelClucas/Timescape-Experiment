#!/usr/bin/env python3
"""WP-8, model side only: where timescape's local Hubble-flow extremes come from.

    python verify/wp8_prediction_extremes.py

Exits 0 if every check passes, 1 otherwise. Touches NO measured Hubble-flow
data; this is the model half that Q-1's guard requires to be fixed first.

E1  A wall observer times local expansion with wall clocks. The tracker's
    lapse is gamma_bar = Hbar/H_w (arXiv:0709.0732 Eq. 7), so the local rates
    are gamma_bar H_w = Hbar across walls and gamma_bar H_v = (3/2) Hbar
    across voids (h_r = 2/3), for every f_v.
E2  With the bare Hbar0 = 50.1 +/- 1.7 ([DNW13], findings/WP-1), these are
    50.1 and 75.15, against the published local minimum 50.1 +/- 1.7 and
    maximum 75.2 (+2.0/-2.6) (arXiv:1311.3787 Secs. 5.3 and 7, via Run 01).
    The ratio max/min = 1/h_r = 1.5 is what the prediction's spread is made
    of.
E3  With void matter (job 003's model), h_r at f_v = 0.695 moves away from
    2/3. Report 1/h_r for M_v in {0, 0.0265, 0.07, 0.0852}.
"""

import sys

import numpy as np
from scipy.integrate import solve_ivp

CHECKS = []


def check(name, ok, detail):
    CHECKS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


f = np.linspace(0.001, 0.999, 999)
hbar = 1.0
hv = 3 * hbar / (2 + f)
hw = (2 / 3) * hv
gam = hbar / hw
check("E1a lapse is 1 + f/2", np.max(np.abs(gam - (1 + f / 2))) < 1e-14, "gamma_bar = Hbar/H_w")
check("E1b wall-clock wall rate = Hbar", np.max(np.abs(gam * hw - hbar)) < 1e-14, "for all f_v")
check("E1c wall-clock void rate = 1.5 Hbar", np.max(np.abs(gam * hv - 1.5 * hbar)) < 1e-14, "for all f_v")

lo, hi = 50.1, 1.5 * 50.1
print(f"  predicted extremes from Hbar0 = 50.1: {lo:.2f} and {hi:.2f} km/s/Mpc; ratio {hi / lo:.3f}")
check("E2 reproduces the published 50.1 and 75.2", abs(lo - 50.1) < 0.05 and abs(hi - 75.2) < 0.1,
      f"{lo:.2f} vs 50.1 +/- 1.7; {hi:.2f} vs 75.2 (+2.0/-2.6)")


def hr_at(M, fv_target=0.695):
    if M == 0:
        return 2 / 3
    C = (4 / 9) * M / (1 - M)

    def rhs(s, y):
        t = np.exp(s)
        aw, av = np.exp(y)
        return [t * np.sqrt((4 / 9) / aw**3), t * np.sqrt(C / av**3 + 1 / av**2)]

    t0 = 1e-9
    y0 = [np.log(t0 ** (2 / 3)), np.log((9 * C / 4) ** (1 / 3) * t0 ** (2 / 3))]
    s = np.linspace(np.log(t0), np.log(1e6), 200001)
    sol = solve_ivp(rhs, (s[0], s[-1]), y0, t_eval=s, rtol=1e-12, atol=1e-14, method="DOP853")
    aw, av = np.exp(sol.y)
    hw_ = np.sqrt((4 / 9) / aw**3)
    hv_ = np.sqrt(C / av**3 + 1 / av**2)
    fv = av**3 / (aw**3 + av**3)
    return float(np.interp(fv_target, fv, hw_ / hv_))


ratios = {M: 1 / hr_at(M) for M in (0.0, 0.0265, 0.07, 0.0852)}
for M, r in ratios.items():
    print(f"  M_v={M:<6}: H_v/H_w at f_v=0.695 = {r:.4f}")
check("E3 empty limit is 1.5", abs(ratios[0.0] - 1.5) < 1e-12, f"{ratios[0.0]:.6f}")
check("E3 void matter lowers the void/wall rate ratio", ratios[0.07] < ratios[0.0265] < ratios[0.0],
      ", ".join(f"{r:.4f}" for r in ratios.values()))

# E4 (appended 2026-11-11): is bridge (a), a volume-weighted mixture of the two
# wall-clock rates, consistent with the model's own global dressed H0?
fv0 = 0.695
h_dressed = (4 * fv0**2 + fv0 + 4) / (2 * (2 + fv0))  # H0 / Hbar0, findings/WP-1 and job 003 item 1
mix = (1 - fv0) * 1.0 + fv0 * 1.5  # volume-weighted wall-clock rate / Hbar0
print(f"  E4: dressed H0/Hbar0 = {h_dressed:.4f} (61.60 from 50.1); volume mixture = {mix:.4f} "
      f"({50.1 * mix:.2f}); mismatch {100 * (mix / h_dressed - 1):+.2f}%")
check("E4 the naive volume mixture does NOT reproduce the model's own dressed H0",
      abs(mix / h_dressed - 1) > 0.05, f"{mix:.4f} vs {h_dressed:.4f}")
check("E4 the mixture is exactly gamma_bar = 1 + f_v/2, i.e. Hbar_tau0 = 67.5 [W19], not dressed H0",
      abs(mix - (1 + fv0 / 2)) < 1e-12 and abs(50.1 * mix - 67.5) < 0.05,
      f"{mix:.4f} = 1 + {fv0}/2; 50.1 x {mix:.4f} = {50.1 * mix:.2f}")

print(f"\n{sum(CHECKS)}/{len(CHECKS)} checks passed")
sys.exit(0 if all(CHECKS) else 1)
