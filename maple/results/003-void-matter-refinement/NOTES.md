# Notes on job 003's run

**`expected_form_matched: true`.** Every line in JOB.md's form is present,
in order, and nothing else is printed.

**`SETUP_SELFCHECK = failed`. The failure is in the pre-registration, not
the computation, and it was not "fixed".** The self-check required the
`delta_v = -0.999` row to reproduce the empty-void sign change, 0.586708, to
1e-3. The row gives 0.588692, which is 2.0e-3 away. Its `q_min`, -0.042888,
is within 1.3e-4 of -0.0430145. The other control lines all pass:
`CONTROL_EQ26_RESIDUAL: 0`, `CONTROL_GAMMA: f/2 + 1`, the dressed-to-bare
ratio exactly as in `findings/WP-1-comparability.md`, both empty-split
residuals `0`, and a scaling residual of 1.2e-14.

The cause is physical. Rows 2-6 show the sign change moving by about 2 per
unit of `1 + delta_v`, so one part in a thousand of void matter moves it by
about 2e-3. The pre-registration picked a row that is not the empty limit,
and gave it a tolerance tighter than the effect being measured. The empty
limit itself is checked in `verify/void_matter_sensitivity.py`, which gets
0.586714 and -0.0430146 at `C = 0` and matches Eq. (26) pointwise to 1.5e-7.
Under the protocol a check is not loosened after it fails, so the failure
stands in `RESULT.txt`. A later job that wants a passing self-check uses the
`C = 0` limit, under a new number.

**Pre-run edits, disclosed.** `job.py` was dry-run from a scratch copy before
the recorded run. Three crashes were fixed, each before any recorded run:
1. `eta` was capped at 200, because `cosh(700)^3` overflows a double.
2. A helper returned `ln eta` where `eta` was meant.
3. The `C` bracket was reduced to 0.18, above which the early void fraction
   exceeds the window's 0.3 lower edge. With this change, a threshold that
   is never crossed is reported as `nan` rather than raising.

None of these touched the physics or the thresholds, and the self-check
failure above was seen in a dry run and deliberately left alone.

**What the run found beyond JOB.md.** The mass identity and the 0.0852
threshold below were confirmed by the independent check, without using the
job's code. The other two thresholds are `RESULT.txt`'s `delta_v` values
converted through that identity:
- **Mass identity.** `1 + delta_v = M_v / f_v` holds to 1e-15, where `M_v`
  is the void phase's share of all matter, fixed at early times. So
  `delta_v` at `f_v = 0.695` is a relabelling of `M_v`. The tracker is
  `M_v = 0`.
- **Thresholds as matter fractions.** `q(f_v = 0.695)` turns positive at
  `M_v = 0.0852`. `|dq_min| = 0.004` is reached at `M_v = 0.0265`, and
  `|dq_min| = 0.0215` (K4) at `M_v = 0.270`.

The interpretation belongs to `findings/WP-6-two-phase-sensitivity.md`.

**Caveat carried from JOB.md.** The non-empty extension is ours. See JOB.md
"The weakest part of this job, named".
