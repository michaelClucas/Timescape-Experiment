# Notes on job 004's run

**Form matched; `SETUP_SELFCHECK = ok`.** The symbolic N-phase dressed `q`
reduces exactly to Eq. (26) for one wall and one empty void phase. The
`s = 0` row reproduces job 003's `delta_v = -0.90` row to the printed
digits for `q_min` and `q(0.695)`. The sign change, 0.680245, sits 1.7e-5
from job 003's 0.680228, which is within the 2e-4 tolerance; the figure in
job 004 matches verify/void_matter_sensitivity.py's own 0.680245.

**Result in one line.** With 7% of the matter in voids, splitting the voids
into two sub-phases of very different emptiness moves `q_min` by at most
0.0012. That is under the 0.004 published `q_0` error, and far under K4's
0.0215. The extreme case has sub-phases at `delta = -0.36` and `-0.95`. So
the void **mass fraction** `M_v` is an adequate single label for the
density refinement, and job 003 / WP-6's results do not depend on assuming
uniform void density. The dressed `q` at `f_v = 0.695` moves more, from
-0.0066 to -0.0115 at `s = 0.9`, and in the direction of **more** apparent
acceleration.

**Pre-run edits.** Before the first dry run, three lines were removed: a
duplicated weight assignment, an unused variable, and a redundant alias.
The dry run and the recorded run printed identical output. No physics or
threshold was changed after any output was seen.

**Independent check: a correction to the check, not the job.** The first
version of `verify/void_density_spread.py` failed 0/4, with `q_min`
scattered by about 3e-3. The cause was numerical. Dressed `q` needs the third
derivative of `a(t)`, and a third finite difference at `dl = 5.8e-5`
amplifies 1e-15 rounding to about 5e-3. The script's density contrasts
already matched to 1e-6, which isolated the fault to the derivatives. With
`dl = 1.2e-3` (rounding about 1e-6, truncation about 1e-6) all four rows
match, with `q` to 1e-6. The reason is recorded in the script's comment.
