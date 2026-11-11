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
