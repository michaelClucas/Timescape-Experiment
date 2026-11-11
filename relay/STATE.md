# Relay state

Append-only. One block per generation, newest last. A block is a pointer to
committed work, never a substitute for it.

Generation cap: 10. Current branch: `research/relay`.

## Generation 1

**Cycles:** 1. **Stopped because:** standing-loop stop condition 1 — every
in-scope package is finished or blocked on Maple. **No successor started.**
**Branch at start:** `ce5fcaa` (= `origin/main`). **At end:** the commit that
adds this block.
**Commits:** one — this block. No research output; there was no unblocked
in-scope work to produce any.

### Step 0 results (2026-11-10)
- `relay/STOP`: absent. `research/relay` did not exist; created from
  `origin/main` per relay.md "Generation 0".
- `gh issue list --label maple:done`: empty. `maple/results/` does not exist.
- Maple #7 (job 001, WP-6) and #8 (job 002, WP-5): `maple:queued`, zero
  comments, last updated 2026-11-05T00:01Z. Five days, no runner activity.

### State of every in-scope package
| Package | State | Blocked on |
| --- | --- | --- |
| WP-1 comparability | Complete. `findings/WP-1-comparability.md` | — |
| WP-6 two-phase sensitivity | Blocked, not started | Maple 001, issue #7 |
| WP-4 `f_v0` vs measured | Complete. `findings/WP-4-void-fraction.md` (main); §11 mask check on unmerged PR #14 | — |
| WP-5 curvature requirement | Blocked, not started | Maple 002, issue #8 |

Cross-check: `logs/2026-11-05-day3-STATUS.md` on `origin/research/auto-2026-11-05-day3`
(PR #14, unmerged) reached the same table and stopped on the same condition.
Nothing has moved since.

### What the chain is waiting on (overseer actions only)
1. **A Maple runner for #7 and #8.** The only thing that unblocks in-scope
   work. Day 3's status records the runner lacks push access to the repo.
2. **Merging PR #15** (`prompts/relay`). `prompts/relay.md` is not on `main`,
   so it is not on this branch either; a successor branching here per
   relay.md would not find the file it is told to read.
3. Merging or closing PRs #14 and #10, and answering Q-1..Q-3 in
   `OPEN-QUESTIONS.md` (Q-4 is answered on #14's branch only).

No out-of-scope package was promoted to fill the time. Q-1 (promote WP-8)
remains the overseer's decision.

### What the next generation should do first, and why
There is no next generation until the overseer acts. Restart the relay only
after a `maple:done` label appears on #7 or #8; that generation starts from
`maple/results/001-two-phase-sensitivity/RESULT.txt` (WP-6, K4) or
`maple/results/002-curvature-budget-requirement/RESULT.txt` (WP-5, K3).

### What I established that is not in a committed file
Nothing.

### What I got wrong this generation
None. This is a warning sign only to the extent that I did no research: the
generation did nothing but check the blockers.

### Numbers the next generation must not take on trust
None produced. No verify/ script was run or changed this generation.

### Open questions whose defaults I took
None.

## Generation 1, continued: paused on the overseer's order (2026-11-11)

The overseer overrode the stop above. They answered Q-1..Q-3, chose SymPy
over Maple, and ordered work to continue. This block is the resume point,
not a handover: **the same session resumes**, and no successor was started.

**Commits since the block above:** `53ad28f` (Q-1..Q-3 answered, standing
loop updated), `ea84deb` (SymPy engine; jobs 001/002 shown defective),
`2ed08ff` (job 003 pre-registered), `6693e60` (job 003 result + independent
check), `3e4be5f` (WP-5 script), and the pause commit that adds this block
(findings WP-5/WP-6, explain/006, derived-figure checks).

### State
| Package | State | Next |
| --- | --- | --- |
| WP-1, WP-4 | Complete (unchanged) | - |
| WP-6 | Finding written; K4 does not fire | Measure `M_v` (below) |
| WP-5 | Finding written; K3 does not fire | Same measurement |
| WP-8 | In scope since Q-1; not started | Pre-registration spec first |

### Resume here, in this order
1. `findings/WP-5-curvature-requirement.md` quotes "9.5%" (line 17) and
   "1.6%" (lines 102, 119) as hand arithmetic. Add both to
   `verify/wp5_curvature_requirement.py` before relying on them. Rule:
   `verify/README.md`.
2. List the four new scripts in `verify/README.md`.
3. Add Q-5 to `OPEN-QUESTIONS.md`: is the void phase VoidFinder's voids, or
   only their empty part? Default: VoidFinder's voids, as WP-4 assumed.
   Reversible. See WP-6 §5.
4. Measure `M_v` for VoidFinder voids. This needs NSA galaxy positions
   cross-matched to `*_comoving_holes.txt`, and the NSA catalogue is not in
   the repo yet. It is a new dataset, so it gets a `data/002-*/SOURCE.md`
   and a `cuts.md` written before any analysis.
5. WP-8: commit `findings/WP-8-prediction-spec.md` before touching data
   (Q-1 guard).
6. Comment on Maple issues #7/#8, pointing to
   `verify/maple_job_design_checks.py`. Do not close them.

### What I established that is not in a committed file
Nothing.

### What I got wrong this generation
- `ea84deb` cycle: first wrote `R_curv ∝ f_vi^(-1/3)`. It is `+1/3`; the
  check caught it before commit.
- Job 003 JOB.md: the self-check tolerance on the `delta_v=-0.999` row was
  tighter than the effect. It was left as `failed` and is explained in
  NOTES.md.
- WP-6 finding draft: quoted a sign-change shift of 0.093. The script gives
  0.0935, so it now reads 0.094. Also dropped an unscripted "82%".

### Numbers the next session must not take on trust
`M_v` thresholds 0.0852, 0.0265 and 0.270, and the shifts 0.0088 and 0.094:
`verify/void_matter_sensitivity.py` (16/16). `R_v` = 5375.5 Mpc and
`Omega_k_v` = 0.9845: `verify/wp5_curvature_requirement.py` (6/6). Pan et
al.'s 7% is a `[LEAD]` from an abstract, not a measurement.

## Generation 1, continued again: checkpoint (2026-11-11)

**Cycles this stretch:** about 12, far past the relay's handover point of
about 8. **Not compacted.** This block is written as a handover so that the
next session, whether it is this one resumed or generation 2, starts clean.
**Branch at start of stretch:** `5edb707`. **At end:** the commit adding this
block.

**Overseer instructions this stretch:**
- "Continue";
- "You have permission to do everything, just keep this research going
  until you make a publishable breakthrough";
- "feel free to run as many subagents as you think you'll need".

**Commits (subjects abbreviated):**
- `efcb45f` WP-5 figures scripted, Q-5 raised
- `78fa7a3` dataset 002 (NSA) SOURCE/cuts pre-registered
- `f797d10` WP-8 pre-registration spec
- `2df78ce` WP-8 step 1, Q-6 raised
- `1442d1e` Q-6 answered (option 2)
- `5d7baaa` job 004 pre-registered
- `e620417` job 004 result: density spread negligible at fixed `M_v`
- `b3cda92` measured void galaxy share 0.0609, cut 5a appended
- `29ecc5e` bias-to-`M_v` mapping
- `ac1d320` WP-8 stops, blocked on WP-9 (T12)
- `ac93a1c` WP-6 prior art
- `86e7770` WP-6 §7, measured `M_v`
- `c434aba` §7.1, headline corrected to a bias bracket

### State of every in-scope package
| Package | State | Blocked on |
| --- | --- | --- |
| WP-1, WP-4 | Complete | - |
| WP-5 | Complete on curvature (K3 does not fire) | - |
| WP-6 | Measured, K4 does not fire; result bracketed by `b_void` in [1.0, 1.3] | An HOD-mock measurement of `b_void` |
| WP-8 | Stopped | WP-9 (T12, light propagation), out of scope |

### What the next session should do first, and why
Settle `b_void`, the one number WP-6's sign question hangs on
(`findings/WP-6-two-phase-sensitivity.md` §7.1).

The route:
1. Take a public N-body box with halos and a dark-matter particle subsample.
2. Populate it with Zehavi 2011's `M_r < -20` HOD.
3. Run VAST VoidFinder on the mock galaxies.
4. Count both mock galaxies (cut 5a) and dark-matter particles strictly
   inside the holes.

The ratio of the two gives `b_void` directly, with no linear-bias premise.
Pre-register it as dataset 003 or job 005 (SOURCE/cuts or JOB.md first)
before touching any simulation output. Expected cost: a simulation download
of 1-10 GB, and a VoidFinder run of tens of minutes.

### What I established that is not in a committed file
Nothing.

### What I got wrong this stretch
- **Cut 5 as registered** counted hole-surface wall galaxies, giving 0.172.
  Caught by a margin diagnostic; cut 5a appended. Both are reported.
- **§7's headline**, `q(0.695) = +0.027`, rested on a single bias value.
  Corrected in §7.1 to a bracket after Sutter 2014.
- **The first version of `verify/void_density_spread.py`** had a
  third-derivative noise problem, fixed with the reason documented.
- **WP-8 §1 presented `Hbar0` and `Hbar0/h_r` as structure** without noting
  that it is already published (arXiv:1311.3787 Sec. 5.3). Cited in WP-6 §6.

### Numbers the next session must not take on trust
| Number | Script |
| --- | --- |
| Galaxy share 0.0609 / 0.1718 | `verify/wp6_void_galaxy_share.py` (6/6) |
| `M_v` and `q` rows against `b` | `verify/wp6_bias_mapping.py` (5/5) |
| Job 004's density-spread result | `verify/void_density_spread.py` (4/4) |
| WP-8 E4, 67.51 vs 61.60 | `verify/wp8_prediction_extremes.py` (8/8) |

Bias values and literature quotes come from subagents reading arXiv LaTeX
sources. They are `[LEAD]` until re-read.

### Open questions whose defaults I took
- Q-5 (void phase = VoidFinder voids): option 1.
- Q-6: answered as option 2 by the overseer instruction.
