# Job 002 - What void curvature does the model actually require?

**Round trips: 1.** Independent of job 001; both can be queued the same day.

## What is computed

The tracker fixes the bare curvature budget as a function of the void
fraction alone:

    Omega_k_bar0 = 9 f_v0 / (2 + f_v0)^2

At the fitted `f_v0 = 0.695` this is `0.861`, which is where the Run 01
audit found the model's energy budget actually sits. But `Omega_k_bar` is
*defined* in terms of a physical void curvature,

    Omega_k_bar = -k_v f_vi^(2/3) f_v^(1/3) / (abar^2 Hbar^2)

so the tracker's value is a **requirement** on `k_v`. This job inverts it.

1. `k_v` required, symbolically, as a function of `f_v0`, `f_vi` and
   `Hbar_0`, from equating the tracker `Omega_k_bar0` to the definition.
2. The same in physical units at `f_v0 = 0.695` and `Hbar_0 = 61.7`
   km/s/Mpc: `k_v` in Mpc^-2, and the implied curvature radius
   `R_curv = |k_v|^(-1/2)` in Mpc.
3. The implied present mean void density contrast `delta_v`, from the void
   phase's own Friedmann-like equation with that curvature and the tracker's
   Milne-like void scaling `a_v ~ t`.
4. The sensitivity `d R_curv / d f_v0` and `d R_curv / d f_vi` at those
   values, so the spread in published `f_v0` can be propagated.
5. `R_curv` at the extremes of the published `f_v0` spread, `0.550` and
   `0.791`.

## Why

Work package **WP-5**, bearing on steps `T8` and `T6`, and it is the
highest-value calculation in the programme.

Run 01's Part 4 isolated what the clock-effect postulate buys, and the
answer was precise: it **relocates the required large quantity** from
`Q`, where the best realistic estimates fall short by about a factor of
five (Rasanen, arXiv:0801.2692 Sec. 4.3: `|Omega_Q|` below 0.04 against
`>~ 0.2` needed), to `<R>`, where the audit states that **no comparable
realistic estimate exists at all**.

That gap is the single most important unexamined thing about timescape. The
backreaction-only route has a published number showing it comes up short.
The curvature route has never had the equivalent number computed. This job
computes the requirement side of it, so WP-5 can then confront it with
measured void profiles.

## Exact expected output form

```
KV_REQUIRED_SYMBOLIC: <expression in fv0, fvi, Hbar0>
kv_required_Mpc^-2 = <float>
R_curv_Mpc = <float>
delta_v_implied = <float>
dR_curv_d_fv0_Mpc = <float>
dR_curv_d_fvi_Mpc = <float>
R_curv_at_fv0_0550_Mpc = <float>
R_curv_at_fv0_0791_Mpc = <float>
SETUP_SELFCHECK = <ok|failed>
```

## What would be surprising or wrong

This job computes a requirement, so there is no published value to match
and the control is dimensional and limiting rather than numerical.

Expectations, stated before the result:

- `R_curv` of order the void size. SDSS DR7 voids have median effective
  radius `17 h^-1 Mpc` and the largest just over `30 h^-1 Mpc`
  (arXiv:1103.4156, abstract). A required curvature radius in the range
  roughly `10`-`100` Mpc is unremarkable and means the requirement is
  plausibly met by real voids.
- `R_curv` **much smaller** than `10` Mpc would mean the model needs voids
  far more strongly curved than any observed, which is the curvature
  analogue of Rasanen's factor of five and would be a serious quantitative
  problem for the model.
- `R_curv` **much larger** than the Hubble radius, about `4300` Mpc at this
  `Hbar_0`, would mean the curvature is effectively negligible and cannot
  carry `Omega_k_bar0 = 0.861`, which would indicate a setup error rather
  than a finding, because the tracker's own budget says it does.
- `delta_v_implied` must lie in `(-1, 0)`. A value below `-1` is
  unphysical and means the setup is wrong. Observed voids reach
  `delta < -0.85` at their edges (arXiv:1103.4156), so a requirement near
  `-0.9` is consistent with observation and a requirement near `-0.99`
  is not.
- The `f_v0` sensitivity matters because the published fitted values span
  `0.550` to `0.791` and beyond, "a spread far exceeding the quoted
  uncertainties" per Run 01's `T13`. If `R_curv` varies by more than a
  factor of two across that spread, then the requirement is not even
  well defined until the `f_v0` discrepancy is resolved, and that
  reordering of the work is itself the result.

`SETUP_SELFCHECK` verifies that substituting the computed `k_v` back into
the definition returns `Omega_k_bar0 = 9 f_v0/(2 + f_v0)^2` to ten digits,
and that the `f_v0 -> 0` limit sends `k_v -> 0`. If it fails, ignore the
other lines.

## Independent check

1. **Dimensional, by hand.** `Omega_k_bar` is dimensionless, so
   `k_v f_vi^(2/3) f_v^(1/3)` must carry dimensions of `abar^2 Hbar^2`,
   i.e. inverse length squared with `abar` dimensionless. Checking the
   units of the returned `k_v` catches the most likely error for free.
2. **Numeric, locally.** `verify/curvature_requirement.py`, to be written
   against this `JOB.md` before the result returns, recomputes items 2-5
   with scipy and shares no code with Maple.
3. **Cross-check against the model's own fitted output.** The fitted
   solution reports `Omega_k_bar0 = 0.862 (+0.024/-0.032)`
   (arXiv:1311.3787 Table 1), and `verify/tracker_relations.py` already
   reproduces `0.861211` from the tracker formula. So the left-hand side of
   the inversion is independently confirmed; only the inversion itself and
   the unit conversion are new.

## Equation provenance

All from Wiltshire, arXiv:0709.0732, PRL 99:251101 (2007), retrieved from
the paper's full text:

- `Omega_k_bar = -k_v f_vi^(2/3) f_v^(1/3) / (abar^2 Hbar^2)`, definition
  stated before Eq. (4). `k_v < 0`, so `Omega_k_bar > 0`.
- Tracker `Omega_k_bar0 = 9 f_v0/(2 + f_v0)^2`, tracker parameter values.
- Tracker void scaling `a_v = a_v0 t`, Milne-like, stated with `h_r = 2/3`.
- `f_v^(1/3) abar = f_vi^(1/3) a_v`, stated with the partition.

Supporting values: `f_v0 = 0.695`, `Omega_k_bar0 = 0.862 (+0.024/-0.032)`,
`Hbar_0` from arXiv:1311.3787 Table 1; dressed `H_0 = 60.98`-`61.7`
km/s/Mpc from Run 01's discrimination table. The published `f_v0` spread
`0.550`-`0.791` from Run 01 `T13`.

**Checked against the paper: YES**, same retrieval and the same
transcription that `verify/tracker_relations.py` validates on eleven
published values.

`f_vi`, the void fraction at last scattering, is **not** fixed by the
above and must be taken from the fitted solution. Run 01 does not record
it. The job therefore reports `k_v` symbolically in `f_vi` as well as
numerically at a stated assumed value, and the assumption is flagged in the
output rather than buried: **retrieving the fitted `f_vi` from
arXiv:1311.3787 is a prerequisite for item 2 to mean anything**, and it is
listed in WP-5 as a one-hour literature task to be done before queueing.

**This job is cleared to queue once `f_vi` is retrieved.** Items 1, 4 and 5
do not depend on it and are valid regardless.
