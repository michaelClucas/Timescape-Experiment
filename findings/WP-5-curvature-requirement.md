# WP-5: the curvature requirement

**Status:** the requirement side is complete. The observation side is
reduced to one measurable quantity, which is shared with WP-6 and not yet
measured (§4).
**Provisional on WP-0.** Run 02 has not run.
**Evidence:** `verify/wp5_curvature_requirement.py` (6/6),
`verify/maple_job_design_checks.py` (10/10, D2-D4 for §1),
`maple/results/003-void-matter-refinement/` (for §3).
**Kill criterion tested:** K3. **It does not fire.** §3.

**The short version.** The tracker's curvature budget,
`Omega_k_bar0 = 9 f_v0/(2 + f_v0)^2 = 0.861`, is not a free requirement on the
voids. It holds if and only if the voids are exactly empty and pure
curvature, a Milne expansion. In physical terms that means a curvature radius
equal to the voids' own Hubble radius, **5.38 Gpc**. That figure varies by
only 9.45% across the whole published `f_v0` spread.

Voids that hold a realistic share of the matter still supply 98.4% of this
curvature, so on curvature the model is safe. Run 01 named curvature as the
place where "no realistic estimate exists". That estimate exists now, and it
comes out in the model's favour.

The cost appears elsewhere. The same void matter that barely touches the
curvature moves the model's deceleration by twice its quoted uncertainty
(WP-6). WP-5 and WP-6 turn out to be one question: **what share of the
matter sits in the voids?**

---

## 1. Why job 002 could not answer this

`verify/maple_job_design_checks.py` D2-D4 shows three problems with job 002:
- **The output is not a physical quantity.** Its `R_curv = |k_v|^(-1/2)` is
  built from the comoving constant `k_v`, whose size depends on how the void
  scale factor is normalised. It scales as `f_vi^(+1/3)`, so the
  normalisation choice changes the answer.
- **It uses the wrong Hubble rate.** It inverts a definition written in the
  bare `Hbar`, but plugs in the dressed `H_0 = 61.7`. The bare value is
  `50.1 ± 1.7` ([DNW13], via WP-1).
- **Its density contrast is out of range.** `delta_v_implied` comes out at
  +0.189, outside the range (-1, 0) that job 002's own JOB.md calls
  physical.

Job 002's JOB.md expected `R_curv` to be "of order the void size",
10-100 Mpc. That expectation compared a curvature radius with a region's
size, and the two are not commensurable. A region of any size can have any
curvature radius.

## 2. The requirement

`[COMPUTED]` I1-I3.

**I1, the identity.** Start from the paper's own definition and partition
(arXiv:0709.0732: the definition before Eq. 4, and
`f_v^(1/3) abar = f_vi^(1/3) a_v`). Then

    Omega_k_bar = f_v * Omega_k_v * (H_v / Hbar)^2

where `Omega_k_v = -k_v / (a_v^2 H_v^2)` is the void phase's own curvature
parameter. This form is free of normalisation: neither `f_vi` nor the scale
of `a_v` appears.

**I2, the requirement.** With the tracker's `h_r = 2/3`,
`H_v / Hbar = 3/(2 + f_v)`. The published `Omega_k_bar` then holds **if and
only if `Omega_k_v = 1`** (to 8e-16 across `f_v` in 0.001-0.999). In a
phase with no cosmological constant, `Omega_k_v = 1` means
`Omega_m_v = 0`: the voids are empty.

**I3, the required radius.** `R_v = c/H_v`.

| `f_v0` | `R_v` |
|---|---|
| 0.695, `Hbar0 = 50.1` | **5375.5 Mpc** |
| 0.695, `Hbar0` from 48.4 to 51.8 | 5199-5564 Mpc |
| 0.550 | 5086 Mpc |
| 0.791 | 5567 Mpc |

The radius varies by a factor of 1.095 across the `f_v0` spread. Job 002's
JOB.md said a factor above 2 would make the requirement ill-defined until
the `f_v0` discrepancy was resolved. That did not happen.

## 3. What voids with matter provide, and K3

`[COMPUTED]` I4, in job 003's model: separately Friedmann phases, whose
empty limit reproduces Eq. (26) exactly (WP-6 §2).

| void share of matter `M_v` | `Omega_k_v` supplied at `f_v = 0.695` | `R_v` / required |
|---|---|---|
| 0 | 1 | 1 |
| 0.0265 | 0.9946 | 1.003 |
| 0.07 | **0.9845** | 1.008 |
| 0.0852 | 0.9806 | 1.010 |
| 0.270 | 0.9121 | 1.047 |

**K3 does not fire.** K3 asks whether the required curvature lies outside
what real voids provide. Two caveats bound that answer:
- **This is not an independent observation of void curvature.** In the
  model, a void's curvature follows from its density and its expansion rate,
  and no survey measures void curvature directly. The defensible statement is
  that a void phase holding 7% of the matter falls short of the required
  curvature by 1.55%.
- **The comparison scale is narrow.** That shortfall is inside the fitted
  `Omega_k_bar0` uncertainty of `+0.024/-0.032` on 0.862 (arXiv:1311.3787,
  via job 002's JOB.md). But that uncertainty is conditional on the tracker,
  so this comparison is indicative only.

`[INFERENCE]`: the part of the requirement that is not automatic is the
expansion rate, `H_v / H_w = 3/2`. Given empty voids that expand at that
rate, the curvature follows. **So K3's content passes to the Hubble-flow
variance, WP-8, which is now in scope behind its pre-registration guard.**
This does not reframe K3 in order to avoid an answer. K3 has been answered:
on curvature, the requirement is met. The note only says where the model's
remaining exposure lies.

## 4. The one measurement both packages need

Two things depend on `M_v`, the share of matter in the void phase:
- the 1.55% curvature shortfall here;
- WP-6's shifts in the deceleration (8.5% removes present acceleration at
  the fitted `f_v0`).

The repository has `M_v` only as a `[LEAD]`, Pan et al.'s abstract figure of
about 7% of bright galaxies. Measuring it for the VoidFinder voids WP-4
used needs NSA galaxy positions cross-matched to the hole spheres; see
`findings/WP-6-two-phase-sensitivity.md` §5.
