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

**Answer:** (overseer, pending)

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

**Answer:** (overseer, pending)

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

**Answer:** (overseer, pending)

### Note appended 2026-11-05 by the third session (day 3), cycle 1

**Not an answer. Evidence on this question from a session that did not choose
it.** Q-3's text above stands unedited.

**Option 2 is already in place, and it works.** This session was handed a
`git worktree` at `.claude/worktrees/timescape-experiment-day-3-65745f` by the
harness rather than the main checkout. Nobody asked for it. Across the whole
session `git reflog` shows only this session's own operations: no stray
`checkout: moving from ... to verify-check`, which the second session recorded
three times in one day.

Why it works: a worktree has its own `HEAD` file and its own working tree, so
another process checking out branches in the main checkout cannot move this
session's `HEAD` or overwrite its files. That is exactly the failure Q-3
describes - a commit landing on local `main` with the previous session's files
absent from its tree.

**Two limits, so that option 2 is not oversold.**

1. **The ref store is shared.** `.git/refs` is common to all worktrees, so
   another process can still create, move or delete branches, `main` and this
   session's day branch included. What it cannot do is move a checked-out
   `HEAD` or write to another worktree's files.
2. **The stash stack is shared**, so `git stash` is unsafe across worktrees and
   can pop another session's work. No stash was used today. A temporary commit
   is the route if one is ever needed, and that is worth a line in
   `prompts/standing-loop.md`.

**Two costs, both small and both paid today.** The worktree has no `.venv` and
no `data/raw/`, since both are gitignored. The main checkout's interpreter was
used by absolute path (a venv is not tied to a working directory, so it is the
same interpreter the previous two sessions ran), and the 17 catalogue files
were copied in and re-verified against the committed manifest: all 17 `OK`
after stripping carriage returns. Nothing was moved or deleted and the manifest
was not edited.

**Recommendation, amending the second session's by one clause.** Still **3 plus
4**, and additionally **2 written into `prompts/standing-loop.md` rather than
left to the harness**, with the venv and data steps named so the next session
does not have to work them out. Option 3's parent assertion is still wanted,
because it catches the shared-ref-store case that a worktree does not.

---

## Q-4. Should `verify/wp4_void_fraction.py` be corrected in place, or left with a correction notice?

**Raised:** 2026-11-05, third session, cycle 5, WP-4
**Blocks:** nothing is unresolvable because of this. The corrected numbers
exist and are committed in `verify/wp4_vast_mask_convention.py` and
`findings/WP-4-void-fraction.md` §12.3. What it blocks is whether a reader who
runs the repository's own scripts gets the right number or the wrong one with a
pointer.

**The argument.** `verify/wp4_void_fraction.py` indexes the survey mask's
declination axis as `((dec + 90) * res)` truncated. [VAST], which wrote
`NSA_main_mask.pickle`, builds and reads it as `int(res*dec) - res*dec_offset`
with `dec_offset = -90` (`multizmask.py` lines 15, 166, 192;
`voidfinder_functions.py` line 249; identical at commit `133cfcf` of 2022-02-10
and at `24e66e1`). Truncation toward zero applied after scaling and before the
offset differs by one pixel wherever `dec < 0`, which is 2.3% of this
footprint. **An array must be read with the convention it was written with, so
this is a defect and not a variant.** `[SOURCED]`.

Correcting it moves the VoidFinder edge-included fraction from 62.280% to
61.570% (Planck2018) and 62.628% to 61.923% (WMAP5), by **-0.710 and -0.705
points**, and halves the residual against arXiv:2202.01226 Table 6. It does
not change any conclusion: `f_v0 = 0.550` and `0.557` stay excluded and `0.627`
stays undecided, for the reasons in §12.4.

The difficulty is reach. Those numbers are quoted in §3, §5, §6, §10.3, §10.4
and §11 of the finding, in
`explain/004c-how-much-does-the-survey-edge-move-the-answer.md`, and in two day
logs and three status files. (`explain/004-is-the-void-fraction-measured.md`
was checked when the answer was applied and quotes no measured fraction, only
fitted values, so the reach is one write-up rather than two.) `verify/wp4_fv0_comparison.py` and
`verify/wp4_critical_threshold.py` both hard-code 0.6228 as the bound and would
have to change with it, which means re-running and re-expecting 25 checks
across two scripts.

**Options:**

1. **Leave the script, append the correction.** What was done. The docstring
   carries a correction notice naming the corrected values and the script that
   produces them; §12 carries them in the finding; the 14 checks and the
   output stand exactly as committed, so every number quoted anywhere in the
   repository stays resolvable to the script that produced it. Cost: a reader
   who runs `verify/wp4_void_fraction.py` and does not read its docstring gets
   62.280% with no warning in the output itself.
2. **Correct the script in place, and every dependent number with it.** The
   repository then reports the right number everywhere. Cost: it is a rewrite
   of the evidence base for a conclusion, not an append, and it breaks the
   repository's one strong convention - `SOURCE.md` §9, finding §10, §11 and
   §12 all append-and-date rather than overwrite. Done carelessly it would also
   leave three status files and two day logs quoting numbers no script
   produces, which is the failure mode the convention exists to prevent.
3. **Correct the script in place and leave a frozen copy** as
   `verify/legacy/wp4_void_fraction_preindexfix.py`, so quoted numbers stay
   resolvable while the live script is right. Costs a file and a line of
   explanation; it is the option that satisfies both the append-only
   convention and the "scripts are the evidence" rule, because nothing is
   deleted and the live script is correct.
4. **Add the correction as a second code path inside the script**, reporting
   both conventions side by side with the VAST one marked correct. Cheapest to
   verify, and the output then carries its own warning. Costs a slightly
   confusing script and does not settle which number the finding quotes.

**Default taken:** option 1, leave it and append. Reversible: nothing was
deleted, the corrected numbers are committed in a second script and in §12.3,
and options 2, 3 and 4 can all be done later from exactly this state. It was
also the only option available without rewriting an evidence file an hour after
the overseer had read the findings that rest on it, which is not a thing an
unattended session should do on its own authority.

**Recommendation: option 3.** The live script should produce the right number,
because "every number in prose comes from a committed, runnable script" is
weakened if running the script gives a different number from the prose; and a
frozen copy keeps every already-quoted number resolvable, which is what the
append-only convention is actually protecting. Option 1 is stable but leaves a
known-wrong script as the repository's headline measurement. Option 2 should
not be taken without option 3's frozen copy.

**A note on sequencing, if option 2 or 3 is chosen.** `wp4_fv0_comparison.py`
and `wp4_critical_threshold.py` hard-code the 0.6228 bound. Their expected
values must be **corrected, not loosened** - the bound becomes 0.6157 and
`0.627`'s margin becomes +0.0113 - and the check that currently reads "0.627
survives the bound by less than the pipeline's own error" needs rewording,
since §12 reduces that error. Rule 6 applies to that edit as much as to a new
one.

**Answer:** (overseer, 2026-11-05) **Option 3.** Correct
`verify/wp4_void_fraction.py` in place and keep a frozen copy. Instructed
directly, in the same session that raised the question.

**Applied, same session, cycle 7.** What was done:

- `verify/legacy/wp4_void_fraction_preindexfix.py` is the pre-fix script frozen
  exactly as it stood at `db47115`, still runnable and still passing its own
  14 checks, so every number quoted in `findings/WP-4-void-fraction.md` §3, §5,
  §6, §10 and §11, in `explain/004c-...`, and in the three 2026-11-05 status files stays resolvable
  to the script that produced it. `explain/004-...` was checked and quotes no
  measured fraction, only fitted values. Only its `RAW` data path changed, by one directory level, because it
  moved into `verify/legacy/`.
- `verify/wp4_void_fraction.py` now uses [VAST]'s index,
  `int(res*dec) - res*DEC_OFFSET` with `DEC_OFFSET = -90`. Its own
  void-centre convention check now prints what the superseded index would have
  given, so it states its own blind spot instead of implying it has none.
- `verify/wp4_fv0_comparison.py` and `verify/wp4_critical_threshold.py` have
  their measured values corrected, with the sequencing note's warning
  observed: **the expectations were corrected, never loosened.** One check in
  `wp4_critical_threshold.py` had to be **rewritten rather than retuned**,
  because the correction reversed the ordering it asserted - see below.
- `verify/wp4_mask_resolution.py`'s baseline is corrected and its mask
  variants re-measured rather than rescaled.
- `verify/wp4_vast_mask_convention.py` is repurposed from proposing the
  correction to being its **regression test**: it asserts that the live script
  implements the sourced expression and that the frozen copy reproduces the
  superseded numbers, so the 0.71-point difference stays demonstrable and a
  later "simplification" back to the old form fails a check.
- `findings/WP-4-void-fraction.md` §13 carries the corrected canonical numbers
  and the header points at it. §3, §5, §6, §10 and §11 are **left standing**
  with their superseded figures, per the append-and-date convention, and §13
  says plainly that they are superseded and by how much.

**The one substantive consequence, which was not anticipated when Q-4 was
raised.** The correction **reversed** an ordering that `wp4_critical_threshold.py`
asserted. Before it, `f_v0 = 0.627` cleared the edge-included bound by `0.0042`
while this pipeline disagreed with [DVB23] Table 6 by `0.0148`, so the check
read "0.627 survives the bound by less than the pipeline's own error". After
it, the margin is `0.0113` and the residual is `0.0077`: **0.627 now clears the
bound by more than the pipeline's residual.** The old claim is false and the
check was rewritten to assert the true one. It changes no verdict - 0.627 is
still undecided, because the +-1-pixel pixelation bracket still straddles it -
but it does mean the specific worry §10.3 raised about that margin is answered,
and answered in the direction that makes the margin more trustworthy rather
than less.

**No exclusion verdict changed**, which is asserted as a check in
`verify/wp4_vast_mask_convention.py` rather than claimed here: every [NW15]
prescription falls on the same side of the superseded bound and the corrected
one.

### Second note appended 2026-11-05 by the third session (day 3), cycle 6

**Q-3's option 4 — "find out what `verify-check` was" — now has an answer, and
it was obtained by accident rather than by investigation.** Q-3's text and the
first appended note both stand unedited.

**What happened.** This session finished its work, wrote its status file and
updated its PR body. On a final check of repository state, `main` had moved
from `96fe08e` to `ce5fcaa` and this session's PR #14 had become
`CONFLICTING`. The cause was not corruption: **PR #13, "WP-4: correct the K5
test, which applied an interval test to a one-sided bound", had been merged
into `main` at 2026-11-05T21:05:54Z**, two minutes after this session branched.
Its own body says it was "Caught by the parallel session of 2026-11-05".

So **a second session was running against this repository at the same time as
this one**, legitimately, doing good work. `git worktree list` confirms the
shape of it:

```
C:/Users/mluca/Documents/Timescape-Experiment            ce5fcaa [main]
C:/.../.claude/worktrees/timescape-experiment-day-3-...  561444e [research/auto-2026-11-05-day3]
C:/Users/mluca/Documents/Timescape-Experiment-run01      f4dfea0 [run-01-audit]  prunable
```

**This explains the day-2 reflog entries exactly.** The second session of
2026-11-05 was working in the **main checkout**, and so was a concurrent
session. One of them ran `git checkout verify-check` and then
`git checkout main` in that shared tree, between two of the other's commits.
Nothing was corrupting anything; two sessions were sharing one working tree,
which is precisely what `prompts/standing-loop.md` forbids and what Q-3
suspected without being able to confirm. The branch no longer exists anywhere
(`git branch -a --list "*verify-check*"` is empty), which is consistent with a
short-lived scratch branch in a shared tree.

**So Q-3 resolves, and the answer is the unexciting one.** The second writer
was another Claude session, not a stray process, not a hook, not a tool
misfiring. The failure mode is real, the diagnosis is confirmed, and **option 2
is the fix** — as this session's first note recorded from the other side, having
been handed a worktree and finding its reflog clean.

**What this changes in the recommendation.** The first note recommended "3 plus
4, plus 2 written into `prompts/standing-loop.md`". That stands, with option 4
struck as **answered**:

- **Option 2 is now evidenced on both sides**: a session in the main checkout
  gets its HEAD moved under it, and a session in a worktree does not. It should
  be in the prompt.
- **Option 3's parent assertion is still wanted**, and cycle 6 is a second
  argument for it: the shared ref store let `main` advance under this session,
  which a worktree does not prevent. It did no harm here because the session
  never committed to `main` and checked its parent every cycle, but the
  mechanism that bit day 2 is still live.
- **Option 4 is closed.** No overseer hour is needed to find out what
  `verify-check` was.

**One thing this session cannot determine, stated rather than guessed.** Every
commit, PR and merge in this repository is authored and merged by the single
account `michaelClucas`, so `gh pr view --json mergedBy` cannot distinguish a
merge the overseer performed from one a session performed. #12 and #13 are
indistinguishable by that field, and the overseer's instruction to merge #12 is
known only from this session's prompt. **Whether #13's merge was instructed is
therefore `[UNKNOWN]` to this session**, and no inference is drawn from it.
Recording it because `prompts/standing-loop.md`'s "do not merge your own PR"
rule is unenforceable and unauditable while every actor shares one identity,
which is a separate and smaller problem than Q-3 but has the same shape: the
protocol depends on what a session will not do rather than on what it cannot.

**What this session did about the conflict.** Merged `origin/main` into the day
branch — which is `prompts/standing-loop.md` cycle step 1, not a deviation —
resolved the single conflict (the finding's header block, where both sessions
had added a reader's note), kept **both** sessions' text, and re-ran all eight
`verify/` scripts on the merged tree. No force-push, no amend, no rebase.
`main` was not pushed to and this session's PR was not merged.
