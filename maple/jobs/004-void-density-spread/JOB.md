# Job 004 - Is the void mass fraction enough, or does the spread of void densities matter?

**Engine: SymPy**, with SciPy integration. **Round trips: 0.** This file is
committed before `job.py` is written or run.
No scratch exploration of this job's quantities was done before it was
written. Its thresholds are K4's and job 001's, which predate 2026-11-10.

## What is computed

This is job 003's model (`maple/jobs/003-void-matter-refinement/JOB.md`),
with the void phase split into **two non-empty sub-phases** that hold equal
shares of the void matter, `M_1 = M_2 = M_v / 2`. Each sub-phase is open FRW,
`H_i^2 = C_i / a_i^3 + 1 / a_i^2`, with curvature strengths
`C_1 = C (1 + s)` and `C_2 = C (1 - s)`. The volume weights `w_i` are set so
that each sub-phase's early-time volume fraction equals its mass share
(equal density at early times, as in job 003). Walls are EdS. Dressing is
unchanged: `gamma = Hbar / H_w`, dressed `H = gamma Hbar - dgamma/dt`,
dressed `q = -1 - gamma (dH/dt) / H^2`.

A smaller `C_i` relative to the curvature means that sub-phase becomes
curvature-dominated sooner, i.e. it empties faster. So `s` is a spread of
emptiness at a fixed total void mass.

1. **Symbolic.** The dressed `q` for `N` phases as an explicit expression in
   the phases' `f_i`, `H_i` and `dH_i/dt`, with `dH_i/dt` taken from each
   phase's acceleration equation. Check symbolically that it reduces to job
   003's construction for `N = 2` (one wall, one void).
2. **Numeric.** At `M_v = 0.0695`, which is `delta_v = -0.90` at
   `f_v = 0.695` in job 003, and for `s` in `{0, 0.25, 0.5, 0.9}`: report
   `q_min`, the sign-change `f_v`, the dressed `q` at `f_v = 0.695`, and the
   two sub-phases' density contrasts at `f_v = 0.695`.

## Exact expected output form

```
SYMBOLIC_Q_REDUCES_TO_JOB003 = <true|false>
SPREAD s=<float> q_min=<float> fv_signchange=<float> q_at_fv0=<float> delta_1=<float> delta_2=<float>
  (four SPREAD lines, s = 0, 0.25, 0.5, 0.9)
MAX_ABS_DQMIN_OVER_S = <float>
SETUP_SELFCHECK = <ok|failed>
```

## What would be surprising or wrong

- **Control.** `s = 0` must reproduce job 003's `delta_v = -0.900000` row:
  `q_min = -0.034244`, sign change 0.680228, `q(0.695) = -0.006557`, within
  2e-4 on each. `SETUP_SELFCHECK` tests exactly this and the symbolic
  reduction, and nothing else.
- **Readings of `MAX_ABS_DQMIN_OVER_S`:**
  - below 0.004, the published `q_0` error: the spread does not matter at
    the level that matters, and `M_v` alone is an adequate label. WP-6's
    results are robust to it.
  - above 0.0215 (K4): the void density spread is load-bearing, and K4
    would fire for the density refinement whatever `M_v` is. That is a
    strong claim, and it is checked hard before it is reported.
  - in between: reportable as a second-order sensitivity.
- **Expected `delta_1` and `delta_2`:** they straddle job 003's -0.90, and
  the mass-weighted identity `sum_i f_i (1 + delta_i) = M_v` holds.

## Independent check

`verify/void_density_spread.py` uses each sub-phase's **parametric** open-FRW
solution, inverted for `t` numerically, and finite differences, whereas the
job uses ODE integration and analytic derivatives. It shares no code with the
job, and must reproduce every SPREAD line within 2e-4.

## The weakest part, named

As in job 003, the non-empty extension is ours. With two sub-phases there is
also a choice of **what is held fixed**: equal masses here. Equal initial
volumes, or a fixed volume-weighted mean `delta`, are other choices. Equal
masses is chosen because `M_v` is the quantity WP-6 found to be the label.
