# Open questions for the overseer

Questions an unattended session could not answer and did not stop for.

Append an entry, take the reversible default, mark the affected output
`provisional on Q-n`, and carry on. The overseer answers these between
days. **Append-only**: an answered question is marked answered in place,
with the answer and the date, never deleted.

```
## Q-n. <the question in one line>

**Raised:** YYYY-MM-DD, cycle N, WP-x
**Blocks:** what is provisional until this is answered
**Options:** each with its consequence
**Default taken:** which, and why it is reversible
**Answer:** (overseer, YYYY-MM-DD)
```

An entry whose default is **not** reversible does not belong here. Those
are stop conditions: the session halts that branch and says so in the day
log, because taking an irreversible default on nobody's authority is worse
than losing a day.

---

<!-- entries below, newest last -->

## Q-1. Should WP-8 be promoted into the standing loop's scope?

**Raised:** 2026-11-05, cycle 1, WP-1
**Blocks:** nothing is provisional on this; it is a scoping decision about
what tomorrow works. WP-1's conclusion stands either way.
**The argument.** `prompts/standing-loop.md` scopes the loop to WP-1, WP-6,
WP-4 and WP-5, and WP-8 is not among them. WP-1 found that the dressed `H_0`
objection does not decide anything on its own, because the discrepancy to be
explained (18.6%) and the local enhancement timescape predicts (up to 17%) are
the same size, leaving a residual of 0.93 sigma. Cycle 4 then found that the
one alternative method timescape itself endorsed, strong-lens time delays,
spans its admissible ceiling depending on a lensing systematic. So the `H_0`
question has failed to decide by three routes, and every route ends at the same
place: the Hubble-flow variance prediction, which is WP-8, and which
`docs/RESEARCH-PLAN.md` records as never having been done by anyone.

WP-8 depends on nothing, needs no Maple round trip, and is costed at 1
agent-run. It is the only package that can settle what WP-1 could not.

**Options:**
1. **Leave WP-8 out of scope.** The `H_0` question stays open indefinitely.
   Costs nothing today; the loop's scope stays as written, which is itself
   worth something, since the scoping exists to stop packages being promoted
   to fill a day.
2. **Promote WP-8 into the loop's scope for subsequent days.** The `H_0`
   question becomes answerable. Risk: WP-8 requires constructing the predicted
   and measured quantities as the same statistic, and getting that wrong
   produces a number that looks like the answer. It has the same shape of slop
   risk the prompt flags for WP-2, though smaller.
3. **Promote it with a stated guard**: WP-8 may be worked only after the
   predicted statistic has been specified in writing and committed, before any
   measured data is touched, in the way `cuts.md` binds a dataset.

**Default taken:** option 1, leave it out of scope. Reversible: the overseer
can add it to the prompt's scope table at any time and nothing done today
needs redoing. I did not work WP-8 and did not promote it to fill the day,
which is what the prompt's scoping section is for. Recommendation is option 3.

**Answer:** (overseer, 2026-11-10; decided by relay generation 1 on the overseer's explicit instruction to answer Q-1 to Q-3) **Option 3.** WP-8 is promoted into the
standing loop's scope as package 5, behind a pre-registration guard. Before
any measured data is touched, the predicted statistic is specified in
`findings/WP-8-prediction-spec.md` and committed on its own: what quantity is
computed from the model, at which scales, with which weighting, and what
measured outcome would count against the model. Measured data may be read
only in a later commit. `prompts/standing-loop.md` previously said WP-8
"depends on WP-7's machinery", while `docs/RESEARCH-PLAN.md` says it depends
on nothing. The guard settles that conflict without assuming either side. If
the predicted statistic cannot be specified from the published model without
new perturbation theory, then the WP-7 dependency is real: WP-8 stops,
blocked, and is not approximated. Scope table updated in
`prompts/standing-loop.md`.

---

## Q-2. Is the void-finder re-run under the timescape distance relation worth commissioning?

**Raised:** 2026-11-05, cycle 3, WP-4
**Blocks:** `findings/WP-4-void-fraction.md` §5 and §7, and the write-up
`explain/004-is-the-void-fraction-measured.md`, are provisional on this being
left undone. Nothing is wrong if it stays undone; the result is simply
one-sided in a stated direction.
**The argument.** `data/001-sdss-dr7-voids/cuts.md` deliberately left open
whether the void volume fraction is recomputed under the timescape
distance-redshift relation rather than the supplied LCDM comoving coordinates,
and assigned the decision to the work package. WP-4 decided **not** to, for a
reason that is not budget: the void finders identify voids *using* the comoving
galaxy positions, so changing the distance relation means re-running the
finders, not converting the published radii. Converting the radii would move
the voids without moving the galaxies and would produce a number that looks
like the answer.

WP-4 instead estimated what the conditioning is worth, ~2 percentage points,
by scaling the measured Planck2018-against-WMAP5 sensitivity by the ratio of
`Δq_0`. That is an extrapolation by a factor of 5.7 and is labelled as an
estimate.

The re-run is tractable: VAST is public and the finders are the published
code. It needs the NSA galaxy catalogue, which is not part of this dataset, and
a timescape distance-redshift relation implemented and checked. It is a work
package, not a cycle.

**Options:**
1. **Leave it.** WP-4's answer stands with the ~2-point estimate and the
   one-sided bound. Cheap. The LCDM conditioning stays an estimate rather than
   a removed systematic.
2. **Commission it as a new work package.** Removes the conditioning properly
   and would also let the V2 fractions be recomputed from the tessellation,
   which would close the unexplained discrepancy in §3 of that finding. Costs
   roughly a WP-2-sized effort for a term WP-4 estimates at 2 points against a
   17-point edge systematic.
3. **Commission a cheaper version**: re-run only VoidFinder, only under the
   timescape relation, on the existing survey, to check the ~2-point estimate
   rather than to improve the measurement.

**Default taken:** option 1, leave it, with the conditioning quantified as an
estimate and the measured number labelled LCDM-conditioned everywhere per cut
8. Reversible: the dataset, the cuts file and the scripts are committed, so
the re-run can be done later and compared against today's numbers directly.
Recommendation is option 1 unless a deep-survey void dataset enters the plan,
in which case option 2 should be folded into that work rather than done on
SDSS DR7, where the edge systematic dominates anyway.

**Answer:** (overseer, 2026-11-10; decided by relay generation 1 on the overseer's explicit instruction to answer Q-1 to Q-3) **Option 1.** Leave it, as recommended. WP-4's
answer stands with the LCDM conditioning given as an estimate, labelled as
such. If a deep-survey void dataset enters the plan, fold option 2 into that
work instead of doing it on SDSS DR7.

---

## Q-3. Does the standing loop need an isolated checkout?

**Raised:** 2026-11-05, second session, cycle 3
**Blocks:** nothing scientific. It blocks confidence in the process, which is
worse, because the failure mode is silent.
**The argument.** `prompts/standing-loop.md` says "One session, one branch,
one day. Two writers on the same files produce a diff nobody can review", and
forbids starting a second agent. That rule assumes the session controls the
working tree. **It does not.** This session's `git reflog` records
`checkout: moving from research/auto-2026-11-05-day2 to verify-check` and then
`verify-check to main` between two of its own commits, for a branch it never
created and which no longer exists. The result was that a cycle's commit landed
on local `main` with every file from the previous session absent from its tree.

It was caught by reading `git log --oneline -2` and noticing the parent commit
was wrong. **Nothing in the protocol would have caught it.**
`protocol/validate.py` checks run output, and this touched none.
`verify/` scripts check numbers, and the numbers were right - they were simply
committed on top of the wrong base. A session that did not happen to print the
commit graph would have pushed a branch that looks complete and silently drops
what it builds on.

The repair used no forbidden operation: no force-push, no amend, no rebase, and
`main` was never pushed to. Details in `logs/2026-11-05-day2.md` cycle 3.

**Options:**
1. **Leave it.** Rely on each session noticing. Costs nothing now. The failure
   is silent, intermittent, and produces output that passes every existing
   check, so "rely on noticing" is the option that already failed once today.
2. **Give each unattended session its own `git worktree`.** One command at
   session start, one at teardown. Another process checking out branches in the
   main tree then cannot move this session's HEAD. Does not fix the underlying
   cause and does not need to.
3. **Add a base-commit assertion to the loop.** Have each session record its
   expected parent sha at branch creation and assert `git rev-parse HEAD^`
   against it before every commit. Catches the symptom mechanically rather
   than relying on attention. Cheap, and it is the kind of check this
   repository already prefers: `prompts/standing-loop.md`'s closing section
   says that where the protocol depends on what a session will not do, it is
   weaker than where it depends on what it cannot do.
4. **Find out what `verify-check` was.** Not something an unattended session
   can do, and the thing actually worth the overseer's time.

**Default taken:** option 1 by necessity for the remainder of this session,
with the mitigation that every cycle was pushed immediately rather than at
day's end, so nothing lived only in a tree something else was moving.
Reversible: options 2 and 3 are both changes to `prompts/standing-loop.md` and
neither invalidates anything committed today. **Recommendation is 3 plus 4** -
3 because it makes the failure loud instead of silent, and 4 because a second
writer in this checkout is a bigger problem than anything in the research plan.
This should be read alongside the Maple access problem: that one stalls work,
this one corrupts it.

**Answer:** (overseer, 2026-11-10; decided by relay generation 1 on the overseer's explicit instruction to answer Q-1 to Q-3) **Options 2 and 3.** Option 4 was answered by
the third session (PR #14, commit `db47115`): the second writer was a
concurrent Claude session in the main checkout.
Option 3 applies to every session: assert the parent before each commit (see
`prompts/standing-loop.md` Step 5).
Option 2 applies to any session that could run at the same time as another:
use its own `git worktree`, use the main checkout's `.venv` by absolute path,
and never use `git stash`, because the stash stack is shared.
Relay generations run strictly one at a time, so `prompts/relay.md`'s
`use_worktree: false` stands for them, and they still make option 3's
assertion. Both prompt changes were made in `prompts/standing-loop.md`.

---

## Q-5. Is timescape's void phase the VoidFinder voids, or only their empty part?

**Raised:** 2026-11-11, relay generation 1, WP-6
**Blocks:** how two findings are read:
- `findings/WP-6-two-phase-sensitivity.md` §4-§5 (how large the void
  mass fraction `M_v` is taken to be);
- the direction in which `findings/WP-4-void-fraction.md`'s lower bound
  binds.

No number changes. What changes is which of the two packages carries the
exposure.

**The argument.** The tracker requires empty voids
(`verify/wp5_curvature_requirement.py` I2). Real voids hold matter, and with
`M_v ≈ 0.07` the deceleration shifts by about twice its quoted error
(`verify/void_matter_sensitivity.py`). A timescape author can define the
void phase as only the truly empty regions, with occupied underdense regions
counted as wall. That makes `M_v ≈ 0` by definition, but the void volume
fraction observations can be compared with then falls below VoidFinder's
0.62, and WP-4's lower bound stops binding.

**Options:**
1. **Void phase = VoidFinder voids**, as WP-4 assumed. Then `M_v` is the
   measured void share of matter, and WP-6's shifts apply.
2. **Void phase = the empty part only.** Then WP-6's shifts vanish, and the
   measured void fraction becomes an overestimate of the void phase rather
   than a lower bound. WP-4's §6 conclusions would need restating.
3. **Report both** in each finding, and leave the choice to whatever paper
   states the model's own operational definition. Run 01 found none
   (`findings/WP-4-void-fraction.md` §9 quotes Wiltshire on recognising the
   wall phase in a survey).

**Default taken:** option 1, for consistency with WP-4, with option 2's
consequence stated in WP-6 §5. Reversible: no script depends on the choice,
only the prose that reads the scripts. Recommendation is option 3.

**Answer:** (overseer, pending)

---

## Q-6. Should WP-8 acquire a full-sky local void catalogue?

**Raised:** 2026-11-11, relay generation 1, WP-8
**Blocks:** WP-8 steps 2-3 (`findings/WP-8-prediction-spec.md` §5).
**The argument.** The measured statistic, `Delta H_s` in arXiv:2510.19945,
is a CMB-minus-LG frame difference in radial shells out to about 150 Mpc.
Timescape's prediction for it depends on the full-sky void and wall geometry
around the Local Group. The repository's only void data, VAST SDSS DR7,
covers the northern SDSS footprint.

**Options:**
1. **Leave WP-8 blocked.** It costs nothing, and the `H_0` question stays
   open.
2. **Acquire a full-sky local void catalogue**, for example one built on the
   2MASS Redshift Survey, as dataset 003, and build bridge (a) on it. This
   is a dataset package, with the same pre-registration as datasets 001 and
   002.
3. **Use the published Szekeres model of the local structure**
   (arXiv:1512.07364) as the geometry. Run 01 notes that it is not timescape,
   so this would test a different model's geometry with timescape's rates,
   and the result would need that caveat on every line.

**Default taken:** option 1. It is reversible: nothing has been computed
that depends on the choice, and no Hubble-flow numbers have been read, so
any option can still be taken cleanly. Recommendation is option 2.

**Answer:** (overseer, pending)
