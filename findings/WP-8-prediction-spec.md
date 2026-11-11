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

---

## 5. Step 1 done, 2026-11-11: what the measurement computes, and why bridge (a) fails here

Only the methods of arXiv:2510.19945 were read. The fetch was instructed to
return no results, values or conclusions, and none were seen.

**The statistic** (their Eqs. 5, 11, 17-20):
- `Delta H_s = H_s^CMB - H_s^LG`, the difference between the Hubble constant
  fitted in the CMB rest frame and in the Local Group rest frame;
- computed in concentric radial shells 30 Mpc wide, from 20-40 Mpc out to
  about 150 Mpc;
- using Pantheon+SH0ES SNe Ia at `0.008 <= z < 0.04`, with `M_B` fixed and
  the full covariance;
- the LCDM expectation comes from Monte Carlo resampling and random boosts,
  not N-body.

The statistic is the one introduced by arXiv:1201.5371 (Wiltshire et al.).

**Why §1's prediction cannot yet be put into this statistic.** `Delta H_s`
measures how the shell-averaged expansion depends on the choice of boost.
Under timescape it is driven by where the voids and walls lie **in each
direction** around the Local Group within about 150 Mpc, because that
geometry decides how a direction-dependent non-kinematic expansion projects
onto the dipole. §1 gives the two rates. Bridge (a) needs their full-sky
geometry, and dataset 001 covers only the SDSS DR7 northern footprint.
Arranging the two rates over the missing sky by assumption would be choosing
a geometry, which is exactly the improvisation the guard forbids.

**Status: WP-8 is blocked at bridge (a).** It is not blocked on WP-7; what
it needs is data, not new theory. What would unblock it is a full-sky void
catalogue within about 150 Mpc of the Local Group, as a new dataset with its
own SOURCE.md and cuts.md. Q-6 raises that choice. Steps 2 and 3 do not run
until Q-6 is answered or a default is taken. No Hubble-flow numbers have been
read.

---

## 6. 2026-11-11: dataset found; bridge (a) fails for a deeper reason; WP-8 stops

**Q-6's dataset exists.** A subagent search identified the Manticore-Local
VIDE void catalogue (arXiv:2507.06866, A&A 705, A160):
- full sky, to about 200 h^-1 Mpc;
- a posterior-combined void-membership grid (`Voronoi_cloud_all_voids_N64.npy`,
  64^3 cells of 7.4 h^-1 Mpc);
- LCDM with `Omega_m = 0.306`, from 2M++ via BORG.

The anti-halo catalogue of Stopyra et al. (arXiv:2311.12926, Zenodo 10160612,
CC-BY-4.0) would serve as the robustness check, though it shares the 2M++
input. None of this was downloaded, for the reason below.

**Bridge (a) is not well defined inside the model.** `[COMPUTED]` E4 in
`verify/wp8_prediction_extremes.py`. The volume-weighted mixture of the two
wall-clock rates at `f_v0 = 0.695` is `1.3475 Hbar0 = 67.51`. That is exactly
`gamma_bar = 1 + f_v/2`, i.e. Wiltshire's `Hbar_tau0 = 67.5` [W19], and **not**
the dressed `H0 = 61.6` that the model's own distance-redshift relation
gives. The 9.6% gap is the `-d gamma_bar / dt` term in the dressed Hubble
rate: the change of the lapse along the light path.

Which of these rates low-redshift supernova distances sample in a 20-150 Mpc
shell, and how that varies with direction, is therefore set by how light
crosses walls and voids. That is step T12, the conceded step, and it is
**WP-9, out of scope** (`prompts/standing-loop.md`). A void map does not
supply it. Choosing a rule would be inventing T12's answer.

**WP-8 stops here, blocked on WP-9.** This is Q-1's guard working as
intended: the predicted statistic cannot be specified without new theory,
which this time is light propagation rather than WP-7's perturbations. No
Hubble-flow numbers were read at any point. The model-side facts in §1 stand
and are scripted.
