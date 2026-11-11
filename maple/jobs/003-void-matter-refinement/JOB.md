# Job 003 - Does the two-phase result survive voids that are not empty?

**Engine: SymPy** (`prompts/standing-loop.md` constraint 2, from 2026-11-10).
**Round trips: 0.** Run locally. This file is committed **before** `job.py`
is run. `job.py` must not be edited after its first run; a corrected job gets
a new number.

**Disclosure, so that this pre-registration is not oversold.** Before this
file was written, scratch exploration in the session that wrote it already
showed approximate values for item 4 (roughly: `q_min` moves by about 0.012
and `q(0.695)` turns positive at `delta_v = -0.85`). What this file fixes in
advance is therefore **definitions and thresholds, not ignorance of the
numbers**. Every threshold below was set before 2026-11-10 by
`maple/jobs/001-two-phase-sensitivity/JOB.md` and by K4 in
`docs/RESEARCH-PLAN.md`; none is chosen here.

## What is computed

The model is the timescape two-phase bare dynamics with each phase
separately Friedmann in volume-average time `t`. That is Run 01's T6: no
backreaction within walls or within voids separately, [SOURCED]
arXiv:0909.0749 Sec. II, as quoted in Run 01 T6. Walls are spatially flat
and hold matter: `H_w^2 = C_w / a_w^3`. Voids are negatively curved:
`H_v^2 = C_v / a_v^3 + K / a_v^2` with `K > 0`. Dressing
is by the wall lapse, Eq. (7) of arXiv:0709.0732: `gamma_bar = Hbar / H_w`,
`d tau = dt / gamma_bar`, dressed `a = abar / gamma_bar`. Hence dressed
`H = gamma_bar Hbar - d gamma_bar / dt` and dressed
`q = -1 - gamma_bar (dH/dt) / H^2`.

1. **Control.** With empty voids (`C_v = 0`, so `a_v` is proportional to `t`)
   and walls `a_w` proportional to `t^(2/3)`, derive the dressed `q` as a
   function of `f_v` symbolically and subtract the published Eq. (26). Also
   print `gamma_bar(f_v)` and the dressed-to-bare Hubble ratio `H / Hbar`.
2. **Curvature split, empty voids.** Two empty void phases with arbitrary
   curvatures `k_1`, `k_2`, so that `a_i = sqrt(-k_i) t`. Derive `q(f_v)`
   and `Omega_k_bar(f_v)` and subtract the single-phase tracker forms. This
   is the refinement job 001 intended.
3. **Scaling symmetry.** The `q(f_v)` curve is unchanged under
   `(C_v, R) -> (lambda C_v, lambda R)`, where `R = f_wi / f_vi` times the
   normalisations. So the non-empty family has one parameter. Check it
   numerically at `lambda = 10`.
4. **Non-empty voids.** Open-FRW voids, `a_v = (C_v/2)(cosh eta - 1)` and
   `t = (C_v/2)(sinh eta - eta)` with `K = 1`, against EdS walls with
   `C_w = 4/9`. Label each member of the family by `delta_v`, the void
   phase's mean matter density contrast relative to the volume average at
   the epoch `f_v = 0.695` (the fitted `f_v0`, arXiv:1311.3787). For
   `delta_v` in `{-0.999, -0.99, -0.95, -0.90, -0.85, -0.80}` report
   `q_min`, the `f_v` at which it occurs, the sign-change `f_v`, and the
   dressed `q` at `f_v = 0.695`.
5. **Thresholds.** The `delta_v` at which `|q_min - q_min(empty)|` reaches
   `0.004` and `0.0215`, and the `delta_v` at which `q(f_v = 0.695) = 0`.

## Why

WP-6 (D6) and step T6. Run 01's T6 entry: what fixes two phases "rather than
a continuum of densities: nothing, by Wiltshire's own account", and "no
quantitative sensitivity analysis". Job 001 tried to supply one by splitting
the void curvature. Item 2 tests that refinement directly. Item 4 tests the
other refinement Run 01 names, density. Real voids are underdense, not
empty: arXiv:1103.4156's abstract gives `delta < -0.85` at void edges, and
7% of galaxies in voids that fill 62% of the volume.

## Exact expected output form

```
CONTROL_EQ26_RESIDUAL: <sympy expression>
CONTROL_GAMMA: <sympy expression in f>
CONTROL_H_DRESSED_OVER_BARE: <sympy expression in f>
EMPTY_SPLIT_Q_RESIDUAL: <sympy expression>
EMPTY_SPLIT_OMK_RESIDUAL: <sympy expression>
SCALING_MAX_ABS_DQ = <float>
VOIDMATTER delta_v=<float> Omega_m_v=<float> q_min=<float> fv_at_qmin=<float> fv_signchange=<float> q_at_fv0=<float>
  (six VOIDMATTER lines, in the delta_v order above)
DELTA_V_AT_DQMIN_0p004 = <float>
DELTA_V_AT_DQMIN_0p0215 = <float>
DELTA_V_AT_Q_FV0_ZERO = <float>
SETUP_SELFCHECK = <ok|failed>
```

## What would be surprising or wrong

- **Control.** `CONTROL_EQ26_RESIDUAL` must be `0`, `CONTROL_GAMMA` must be
  `f/2 + 1`, and `CONTROL_H_DRESSED_OVER_BARE` must equal
  `(4f^2 + f + 4) / (2(2 + f))`, the relation
  `findings/WP-1-comparability.md` uses to reproduce the dressed 61.60 from
  the bare 50.1. **If any of these fails, the dressing algebra is wrong and
  every other line is void.**
- **Item 2.** The residuals are expected to be `0`: empty voids are Milne
  whatever their curvature constant, so splitting them changes nothing. A
  nonzero residual is a setup error.
- **Item 3.** `SCALING_MAX_ABS_DQ` is expected to be at rounding level. If it
  is not, the family has two parameters, and item 4's labelling by
  `delta_v` alone is invalid.
- **Item 4.** The `delta_v = -0.999` row must reproduce the control,
  `q_min = -0.0430` and sign change `0.5867`, to about `1e-3`.
- **K4** (`docs/RESEARCH-PLAN.md`) fires if, under refinement, `q_min` moves
  by more than half the effect: `|dq_min| > 0.0215` at a `delta_v` that real
  voids have. `|dq_min| < 0.004` is inside the published `q_0` uncertainty
  (job 001 JOB.md). Whether real voids have such a `delta_v` is decided in
  WP-5/WP-6's findings against data, not here.
- A **positive** `q` at `f_v = 0.695` means no apparent acceleration at the
  fitted void fraction. That is also what a sign error looks like, so it is
  not reportable unless the independent check below reproduces it.

## Independent check

`verify/void_matter_sensitivity.py` shares no code with SymPy. It integrates
the phase Friedmann equations with `scipy.integrate.solve_ivp` in `t`, builds
`Hbar`, `gamma_bar` and the dressed `H` from the integrated arrays, and takes
the derivatives by finite differences. It must reproduce item 1's
`q_min` and sign change, and item 4's rows to `1e-3`.

## The weakest part of this job, named

Wiltshire's phenomenology uses the tracker, and **this job extends it** by
putting matter in the voids. The extension uses the model's own ingredients:
the T6 split, Eq. (7)'s lapse, and separately Friedmann phases per
arXiv:0909.0749. The control shows that these ingredients reproduce Eq. (26)
exactly when the voids are empty. But no timescape paper retrieved here
computes the non-empty case, so the extension is **ours**. A timescape author
could reasonably answer that the void phase is meant to be **defined** as
the empty part, with the underdense-but-occupied regions counted as wall. If
so, the measured `f_v` falls and WP-4's lower bound has to be re-read, so
that answer moves the problem rather than removing it.
