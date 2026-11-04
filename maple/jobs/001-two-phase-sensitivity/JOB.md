# Job 001 - Does the two-phase split survive refinement?

**Round trips: 1.** Independent of job 002; both can be queued the same day.

## What is computed

The timescape ansatz uses **one** void curvature scale (`T6`). This job
generalises to `M` void phases with distinct curvatures and derives how the
observable predictions move.

1. The `M`-phase bare backreaction `Omega_Q_bar`, symbolically, and
   confirmation that it reduces to
   `-f_v_dot^2 / (9 f_v (1 - f_v) H_bar^2)` when `M = 1`.
2. The `M`-phase bare curvature `Omega_k_bar`.
3. For `M = 2` void phases of equal volume with curvatures
   `k_v (1 + s)` and `k_v (1 - s)`, the dressed deceleration parameter
   `q(f_v; s)`, and from it:
   - the `f_v` at which `q` changes sign, as a function of `s`;
   - `q_min`, the most negative `q`, as a function of `s`.
4. `d q_min / d s` and `d f_v_signchange / d s` at `s = 0`.
5. Those two quantities at `s = 0.5`, a 50% curvature spread.

## Why

Work package **WP-6**, bearing on step `T6`, which carries weight 3 and
which the Run 01 audit marks `no` under "secure", with the note that **no
sensitivity analysis exists**. Open question 10 of that run asks exactly
this and leaves it unanswered.

The question matters because of the structure Run 01 found. The weight sits
on eight non-theorem steps, and the audit's own account of why the model is
hard to refute is that "any failure can be absorbed by a different closure
(T5), a finer phase decomposition (T6), or a better light-propagation
treatment (T12), none of which is pinned down." This job removes one of
those three escapes, in whichever direction it falls.

**Both outcomes are results, and neither is the one we want.** If the
predictions are insensitive to `s`, then `T6` is not a weakness and the
two-phase ansatz is doing less work than its `SCHEME` tag suggests: that
counts *for* the model. If they move substantially, then the published
numbers are an artefact of a choice nobody has justified, and every fitted
`f_v0` in the literature inherits that: that counts *against* it.

## Exact expected output form

Exactly these lines on stdout, in this order, nothing else. Symbolic lines
print a Maple expression on one line; numeric lines print `name = float`
with at least six significant figures.

```
OMEGA_Q_M_PHASE: <expression in f[i], fdot[i], Hbar>
OMEGA_Q_REDUCES_TO_PUBLISHED = <true|false>
OMEGA_K_M_PHASE: <expression in k[i], f[i], abar, Hbar>
Q_TWO_VOID_PHASE: <expression in f_v and s>
f_v_signchange_at_s0 = <float>
q_min_at_s0 = <float>
d_f_v_signchange_d_s_at_0 = <float>
d_q_min_d_s_at_0 = <float>
f_v_signchange_at_s_half = <float>
q_min_at_s_half = <float>
SETUP_SELFCHECK = <ok|failed>
```

## What would be surprising or wrong

The `s = 0` line is the control and is **not** a new result. It must
reproduce the published single-phase values:

| Quantity | Required at `s = 0` | Source |
|---|---|---|
| `f_v_signchange_at_s0` | `0.5867` | arXiv:0709.0732, after Eq. (26) |
| `q_min_at_s0` | `-0.043` | same |
| `OMEGA_Q_REDUCES_TO_PUBLISHED` | `true` | arXiv:0709.0732, definition before Eq. (4) |

**If the `s = 0` line does not reproduce those, the generalisation is wrong
and every other line is void.** `verify/tracker_relations.py` passes all 11
of its checks on this transcription, so a failure here is in the `M`-phase
generalisation, not in the base equations.

For the new results, stated before seeing them:

- `d q_min / d s` at `s = 0` is expected to be **zero**, on the symmetry
  argument that `s -> -s` relabels the two phases and must leave `q`
  unchanged, so `q_min` is even in `s`. A nonzero first derivative would
  mean the generalisation breaks that symmetry and is a setup error, not a
  finding.
- The leading dependence is therefore expected at `O(s^2)`, and the
  interesting number is `q_min_at_s_half`.
- `|q_min_at_s_half - q_min_at_s0| < 0.004` would put the shift inside the
  published fit uncertainty on `q_0` (`-0.043 +0.004/-0.000`,
  arXiv:1706.07236) and means `T6` is not load-bearing at this level.
- A shift larger than `0.02`, roughly half the whole effect, means the
  two-phase choice substantially sets the answer.
- `q_min` becoming positive at `s = 0.5` would mean the apparent
  acceleration vanishes under refinement. That would be a strong result
  against the model and must be checked hard before being reported, because
  it is also what a sign error looks like.

`SETUP_SELFCHECK` covers the `M = 1` reduction and the
Einstein-de Sitter limit `f_v -> 0`, where `q_bar -> 1/2`,
`Omega_M_bar -> 1`, `Omega_Q_bar -> 0`. If it reports `failed`, ignore
every other line.

## Independent check

1. **Numeric, locally.** `verify/two_phase_sensitivity.py`, to be written
   against this job's `JOB.md` before the result returns, integrates the
   same `M = 2` system numerically with scipy and shares no code with
   Maple. Written in advance deliberately, so it cannot be tuned to agree
   with whatever Maple returns.
2. **Analytic, by hand.** `d q_min / d s = 0` at `s = 0` follows from the
   relabelling symmetry above. That is checkable without either tool and is
   the cheapest guard against a broken generalisation.
3. **Limit.** As `s -> 1` one void phase becomes flat and the system should
   reduce to a two-phase model with the void fraction halved. Printing that
   limit is not required for this job but is the natural follow-up if the
   `s` dependence turns out to be large.

## Equation provenance

Base equations from Wiltshire, "Exact solution to the averaging problem in
cosmology", arXiv:0709.0732, Phys. Rev. Lett. 99:251101 (2007):

- Volume partition, stated inline before Eq. (1):
  `abar^3 = f_vi a_v^3 + f_wi a_w^3`, `f_wi = 1 - f_vi`.
- Budget, Eq. (5): `Omega_M_bar + Omega_k_bar + Omega_Q_bar = 1`.
- Definitions before Eq. (4): `Omega_M_bar = 8 pi G rho_M0 abar_0^3 / (3 Hbar^2 abar^3)`,
  `Omega_k_bar = -k_v f_vi^(2/3) f_v^(1/3) / (abar^2 Hbar^2)`,
  `Omega_Q_bar = -f_v_dot^2 / (9 f_v (1 - f_v) Hbar^2)`.
- Bare expansion rate, Eq. (4): `Hbar = f_v H_v + f_w H_w`.
- Integrability, Eq. (6).
- Lapse, Eq. (7): `gamma_bar = 1 + h_r^(-1)(1 - h_r) f_v`; tracker
  `h_r = 2/3`, so `gamma_bar = 1 + f_v/2`.
- Tracker values: `Omega_M_bar0 = 4(1 - f_v0)/(2 + f_v0)^2`,
  `Omega_k_bar0 = 9 f_v0/(2 + f_v0)^2`.
- Dressed `q`, Eq. (26):
  `q = -(1 - f_v)(8 f_v^3 + 39 f_v^2 - 12 f_v - 8)/(4 + f_v + 4 f_v^2)^2`.
- Bare `q`, after Eq. (26): `q_bar = 2(1 - f_v)^2/(2 + f_v)^2`.

**Checked against the paper: YES.** Retrieved from the full text of
arXiv:0709.0732 and independently verified: `verify/tracker_relations.py`
reproduces all eleven published values from these equations, including the
`q` sign change at `0.586708` against the published `0.5867`, `q_min =
-0.0430145` against `-0.043`, `Omega_Q_bar(0.695) = -0.0291855` against
`-0.0293`, and `Omega_k_bar(0.695) = 0.861211` against `0.862`.

The `M`-phase generalisation is **ours**, not the paper's, and is the part
of this job that can be wrong. It is guarded by the `s = 0` control line
rather than by review.

## The weakest part of this job, named

`q_two` in `job.mpl` does **not** rederive the dressed `q`. It scales
`Omega_k_bar` for the two-void-phase case and then re-evaluates the
published Eq. (26) at the `f_v` carrying the same curvature. That is a
substitution, not a derivation, and Eq. (26) is not simply a function of
`Omega_k_bar`: it comes out of the full lapse algebra, so the substitution
is valid only to the extent that the curvature is what carries the `f_v`
dependence there.

This is stated here rather than hidden because it bounds what the result
can mean:

- If the job returns a **small** `s` dependence, the conclusion is weak but
  usable: the crude substitution finds no sensitivity, which makes a real
  sensitivity less likely without establishing its absence.
- If the job returns a **large** `s` dependence, the result is **not
  reportable** as a finding about timescape. It must be re-run as job 003,
  rederiving `q` from Eqs. (4)-(7) with `M` phases from the start, because a
  large shift is exactly what an invalid substitution also produces.

Either way one round trip is spent well: the cheap version either
discharges the question or tells us the expensive version is worth a day.
Doing it in this order is deliberate.

**This job is cleared to queue, with the caveat above recorded in its
`RESULT` notes when it returns.**
