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
