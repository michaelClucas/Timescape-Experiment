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
