# Local verification

One runnable script per topic: `verify/<topic>.py`. `tracker_relations.py`
is the existing one; it passes 11 of 11 checks, including `gamma_lapse`
1.3475 and `f_v` 0.586708 at the dressed deceleration sign change.

Rules, and they are not negotiable:

- **Every number that appears in prose anywhere in this repository comes
  from a script here, or from a Maple `RESULT.txt`.** Including arithmetic
  you are confident about.
- A script **exits non-zero on failure** and prints what failed.
- A script is **run before it is committed**, and its output goes in the
  day log.
- A script takes no hidden state: no edited constants between runs, no
  commented-out branches that were used to get the committed number.

A Maple result with a `crosscheck.py` is worth considerably more than one
without, because otherwise it is one machine's word.

This is the check that would have caught Run 01's one real violation: a
comparison statistic quoted without the free-parameter counts the claim
ledger's C5 requires. `protocol/validate.py` now catches that class; this
directory catches the arithmetic.

## Scripts added 2026-11-10/11 (relay generation 1)

- `maple_job_design_checks.py` (10/10): what queued Maple jobs 001 and 002
  could and could not measure. No claim about timescape.
- `void_matter_sensitivity.py` (16/16): the independent check on
  `maple/results/003-void-matter-refinement/`. It uses solve_ivp and shares no
  code with the SymPy job, and it also produces the figures quoted in
  `findings/WP-6-two-phase-sensitivity.md` and `explain/006`.
- `wp5_curvature_requirement.py` (7/7): the normalisation-free curvature
  requirement and the figures quoted in
  `findings/WP-5-curvature-requirement.md`.
