# WP-8 pre-registration: the predicted Hubble-flow statistic

**This file exists because of Q-1's guard.** It is committed before any
measured Hubble-flow data is read. No number from arXiv:2510.19945,
arXiv:1201.5371 or any distance catalogue has been read in writing it,
beyond what Run 01 already quotes in prose.
**Provisional on WP-0.**
**Evidence for the model side:** `verify/wp8_prediction_extremes.py` (6/6).

## 1. What the model fixes, now

`[COMPUTED]` E1-E3. A wall observer, which is what we are, times expansion
with wall clocks. In the tracker, for every `f_v`:

- across wall regions the measured rate is `gamma_bar H_w = Hbar`;
- across void regions it is `gamma_bar H_v = Hbar / h_r = (3/2) Hbar`.

With the bare `Hbar0 = 50.1 ± 1.7` these are 50.10 and 75.15 km/s/Mpc. The
published local extremes are 50.1 ± 1.7 and 75.2 (+2.0/-2.6)
(arXiv:1311.3787, via Run 01). So **the published prediction is two numbers,
`Hbar0` and `Hbar0 / h_r`, and its spread is the single parameter
`1/h_r = 1.5`**.

This is the quantity WP-5 passed on (`findings/WP-5-curvature-requirement.md`
§3): given empty voids, `h_r = 2/3` is what makes the curvature budget come
out, and it is not measured anywhere in this repository.

With void matter (job 003's model), the void-to-wall rate ratio at
`f_v = 0.695` is:

| `M_v` | 0 | 0.0265 | 0.07 | 0.0852 |
|---|---|---|---|---|
| ratio | 1.5000 | 1.4810 | 1.4575 | 1.4499 |

**Pre-registered prediction: wall-clock local expansion rates in void-dominated
and wall-dominated regions differ by a factor of 1.45-1.50.** The range covers
void matter from none up to WP-6's 8.5% threshold.

## 2. What the model does not fix, and the WP-7 exit

The model gives the two extremes. It does not say how a measured shell or
direction **mixes** them. That mixing depends on how much of the volume, or
of the sight-line, out to distance `R` lies in voids around the Local Group.

There are two possible bridges:

- **(a) Empirical geometry.** Take the void fraction around the observer as
  a function of `R` and direction from a void catalogue, and form the
  volume-weighted mixture of the two rates. That uses data, but not the
  Hubble-flow data being tested, so it is allowed under the guard. Its
  weakness is that dataset 001 (SDSS DR7 VoidFinder) is incomplete at small
  distances and covers only the SDSS footprint.
- **(b) A model of the variation within each phase.** This needs
  perturbation theory that timescape does not have.

**If (a) cannot be made to work and (b) is needed, WP-8 is blocked on WP-7,
which is out of scope, and it stops there** (Q-1's answer).

## 3. The order of the next commits, fixed now

1. **Read the methods sections only** of arXiv:2510.19945 (Shao & Bengaly)
   and arXiv:1201.5371 (Wiltshire et al.), to learn what statistic each
   computes:
   - shells or directions;
   - the weighting;
   - which frame;
   - which distance indicator.

   Write that down with the bridge (a) construction that maps §1's two rates
   into **the same statistic**, and commit. Results sections and tables are
   not read in this step.
2. **Compute the predicted statistic**, as a curve against scale with its
   spread from §1's 1.45-1.50 range and bridge (a)'s geometric uncertainty,
   and commit with its script.
3. **Only then read the measured values** and compare.

## 4. What would count against the model, fixed now

- **Against.** The measured statistic, on scales where bridge (a) says the
  sight-lines are void-dominated, excludes a void-to-wall rate contrast of
  1.45 at the measurement's own stated confidence. This is D8's "counts
  against" (`docs/RESEARCH-PLAN.md` WP-8), made specific.
- **For.** The measured statistic requires a contrast within 1.45-1.50,
  **and** excludes the contrast a LCDM void outflow gives at the same
  density contrast. The linear-theory form of the latter,
  `delta_H / H ≈ -f(Omega) delta / 3`, is computed in step 2, with its
  premise named, not quoted here.
- **Neither.** The data cannot distinguish 1.45-1.50 from the LCDM outflow.
  That is a reportable null and does not license reformulating the
  statistic.
