# Standing loop: unattended research day

This is not a run prompt. It does not produce a numbered run under `runs/`.
It is the standing brief for a session that works this repository's research
plan for a whole day with nobody answering questions.

Read `docs/RESEARCH-PLAN.md` first. It is the authority on what the work is.
This file is the authority on how to proceed when you are alone.

---

## The one hard rule

**Nobody will answer you today.** A question that stops your work costs the
whole day. So you never stop to ask. Every block has a route around it,
written below. Take the route, record the block, keep working.

The corollary is the rule that matters more: **you never route around a
block by inventing the answer.** A blocked computation stays blocked and
gets filed. It does not get estimated, approximated in your head, or
replaced by a plausible number. A result you cannot compute today is worth
exactly nothing to this repository; a result you fabricated today is worth
less than nothing, because it will be built on.

---

## Standing constraints, from the overseer

These came with the research plan and do not change.

1. **Do not assume any conclusions.** This is an experiment, not an attempt
   to support timescape or to bury it. A clean negative is a success; so is
   a clean positive. Neither is the goal.
2. **Symbolic calculation happens in SymPy**, locally, in the repository's
   `.venv`. Changed 2026-11-10 by the overseer: no Maple licence is
   available and no free route to one exists. Before that date it read
   "Symbolic calculation happens in Maple, on another machine, one round trip
   per day". The queue's discipline survives the change of engine: a job's
   `JOB.md`, with its expected output form and its surprises, is committed
   **before** its `job.py` is run; the output is committed verbatim under
   `maple/results/`; and an independent numeric check that shares no code with
   SymPy is required. The directory keeps the name `maple/` so that existing
   references stay resolvable.
3. **Proofs are verified in Lean**, and only if a proof-shaped claim
   appears. Do not start a Lean project speculatively.
4. **Data-driven.** Reanalyse the raw public data. A number taken from a
   paper's abstract is a `[LEAD]`, not a result.
5. **Any answer gets a natural-language write-up** a late-highschooler can
   follow, under `explain/`. No AI-slop analogies. An analogy of the
   fabric-and-gravity kind is allowed where the mechanism genuinely needs
   one; a decorative comparison is not.

---

## The cycle

You work in cycles. One cycle is one slice of one work package, ending in a
commit. Repeat until a stop condition fires.

### Step 1. Sync and ingest

```
git fetch origin
git merge origin/main        # on your day branch
gh issue list --label "maple:done" --state all --limit 30
gh issue list --label "maple:queued"
gh issue list --label "maple:blocked"
```

Any `maple:done` issue whose results landed since your last cycle unblocks
the package that filed it. **Resuming blocked work takes priority over
starting new work**, because a returned Maple result is the scarcest thing
in this process: one per day per job, and the queue goes idle if you do not
consume it.

Read the result from `maple/results/NNN-<slug>/RESULT.txt`, not from the
issue comment. The comment is a notification; the committed file is the
record. If they disagree, the file wins and you note the disagreement.

### Step 2. Pick the work

**Your scope is five packages.** The research plan has eleven; the other
six are out of scope for this loop and the reasons are below. Work these,
in this order, taking the first that is unblocked and unfinished:

| | Package | Why it is in scope |
|---|---|---|
| 1 | **WP-1**, comparability check only | Cheap, potentially terminal. If the published joint-fit tension and the `H_0` discrepancy are already like-for-like and significant, K1 may fire before anything expensive starts. |
| 2 | **WP-6**, two-phase sensitivity | Maple job 001 is already queued. If `q_min` moves by more than half the effect under refinement, K4 fires and every quoted number in the programme is an artefact of `T6`. |
| 3 | **WP-4**, `f_v0` against measured void fractions | Public void catalogues, bounded computation. A fitted parameter quoted with uncertainties far tighter than its scatter across datasets is a problem whichever way this falls. |
| 4 | **WP-5**, the curvature requirement | Maple job 002 is already queued. The required void curvature against what observed voids provide. This is the highest-value item in the repository and the cleanest available kill (K3). |
| 5 | **WP-8**, Hubble-flow variance, **behind a pre-registration guard** | Added 2026-11-10 by the overseer's answer to Q-1 (option 3). WP-1 found the `H_0` question undecided by three routes, all ending at this prediction. **Guard:** first commit `findings/WP-8-prediction-spec.md` specifying the predicted statistic (quantity, scales, weighting, what counts against), touching no measured data; only a later commit may read data. If the statistic cannot be specified from the published model without new perturbation theory, WP-8 is blocked on WP-7 and stops. |

**WP-1 is the comparability check and nothing more.** Read the published
results, establish whether the comparisons are like-for-like at matched
parameter count, and report. **It must not slide into WP-2.** The moment you
find yourself fitting supernovae, you have left your scope.

### Out of scope, and why

Do not work these. If you believe one has become necessary, write it to
`OPEN-QUESTIONS.md` with the argument and carry on with what is in scope.

- **WP-0** (Run 02, the adversarial pass) and **WP-10** (Run 03). Both need
  a fresh context with staged inputs and no repository checkout. You hold a
  checkout, so you cannot run either honestly.
- **WP-2** (refit Pantheon+ from light curves, standardisation free). The
  question is real and the job is months of work for someone who already
  owns the SALT3 machinery. A reduced version will produce a number that
  looks like the real answer and is not one. **This is the single largest
  slop risk in this repository.**
- **WP-3** (the ablation). Depends on WP-2.
- **WP-7** (compute `Omega_b h^2` and `S_8`). Requires a perturbation theory
  timescape does not have. Building one is not a day's work and not yours.
- **WP-8** was here until 2026-11-10; Q-1's answer moved it into scope
  behind a guard. See package 5 above.
- **WP-9** (light propagation, the conceded step `T12`). This is the open
  problem of the whole Buchert averaging programme, budgeted in the plan at
  two weeks. It will not be solved here. If you produce something that looks
  like a solution to it, you have made an error; find it.

**When all five in-scope packages are finished or blocked, stop.** Do not
promote an out-of-scope package to fill the day. That instruction is the
main thing this scoping is for.

Every conclusion you reach is `provisional on WP-0`, including in the commit
message, because K7 can invalidate the audit's premises and work built on
them has to be findable if it does.

### Step 3. Do the work

Rules that apply to everything you produce:

- **Every number in prose comes from a committed, runnable script or from a
  Maple `RESULT.txt`.** Scripts go in `verify/<topic>.py`, exit non-zero on
  failure, and are run before you commit them. No exceptions, including for
  arithmetic you are confident about.
- **Every dataset gets `data/NNN-<dataset>/` with `SOURCE.md`, `fetch.sh`,
  `MANIFEST.sha256` and `cuts.md`** before any analysis touches it. The
  cuts file is written before you see the result, not after.
- **Confidence tags on every claim**: `[SOURCED]` means you fetched and read
  the source; `[LEAD]` means you have a pointer you did not verify;
  `[INFERENCE]` means you derived it and must name the premises;
  `[UNKNOWN]` means you do not know. A citation you did not fetch is never
  `[SOURCED]`. This is checked, and a fabricated locator is kill criterion
  K7 for a reason.
- **Use the repository's venv, not system Python.** `.venv/Scripts/python`
  on this machine; nothing is installed globally and `import numpy` from
  system Python fails. The venv is gitignored, so if it is missing rebuild
  it: `python -m venv .venv` then
  `.venv/Scripts/python -m pip install -r env/requirements.txt`. If you need
  a package that is not pinned, install it, verify the import actually
  works, and add it with the version you ran.
- **`classy` and `healpy` are unavailable on this platform** and
  `env/requirements.txt` records what was tried. camb substitutes for
  CLASS. Do not work around a missing package by writing your own; say the
  work does not run here.
- **Record the negative.** A fit that failed to converge, a dataset that
  turned out unusable, an approach you abandoned after an hour: all of it
  goes in the day log. A day's work that reports only what succeeded is a
  day's work nobody can trust.

### Step 4. Run the validator if you touched run output

```
python protocol/validate.py runs/<run-dir>/OUTPUT.json
```

**Never change a rule in `protocol/validate.py` to make a hit disappear.**
If you believe a rule is wrong, the finding is "rule N is wrong, here is
the hit it produced and why the run is right" — written into the day log
and left for the overseer. Two of that file's rules were in fact wrong on
their first run; that was established by examining the hits, not by
deleting the rules.

### Step 5. Commit

One commit per cycle, on the day branch, message naming the package:

```
WP-5: void curvature requirement, analytic bound before Maple 002
```

Push every cycle. An unpushed day is a lost day if the session dies.

**Assert the parent, every commit** (Q-3, option 3). Record
`git rev-parse HEAD` when you create or check out the branch, and again
after every push. Immediately after each commit, check that
`git rev-parse HEAD^` equals the recorded sha. If it does not, something
else moved your branch or your checkout. Stop and do not push. Log it.
Do not repair it with a force-push, an amend or a rebase.

**Isolation** (Q-3, option 2). If another session could be working in
this repository at the same time, work in your own `git worktree`. Use
the main checkout's `.venv` by absolute path, and copy `data/raw/` in and
verify it against the manifest. Never use `git stash`: the stash stack is
shared across worktrees. Relay generations run one at a time and are
exempt from this paragraph, but not from the parent assertion.

### Step 6. Log

Append to `logs/YYYY-MM-DD.md` — cycle number, package, what you did, what
you concluded, what blocked, what you filed. Append only; never rewrite an
earlier cycle's entry. If a later cycle overturns an earlier one, the later
entry says so.

Then go to step 1.

---

## Blocks, and the route around each

### Block: it needs a symbolic computation

**Since 2026-11-10 (constraint 2): write a SymPy job and run it yourself,
in two commits.** First commit `JOB.md`, which pre-registers the expected
form and what would be surprising. Then run `job.py`, and commit its verbatim
output and the independent check together. A job is never edited after its
`JOB.md` is committed; a corrected job gets a new number. The Maple procedure
below is kept for the record and for any job that genuinely needs Maple.

File a Maple job. This is the whole reason the queue exists.

1. Write `maple/jobs/NNN-<slug>/JOB.md` and `job.mpl`, following
   `maple/README.md`. `JOB.md` **must** state the expected output form. A
   job without one is refused by the runner, and rightly: at a day's
   latency a wrong answer that arrives looking like a right one costs a
   week.
2. Write `crosscheck.py` where a numerical check is possible. A Maple result
   with no independent check is one machine's word.
3. Commit and push. Note the sha.
4. Open the issue with the `maple-job` template, label `maple:queued`,
   naming the job directory and **that sha**. The spec never goes in the
   issue body.
5. Move to the next package. **Do not wait.** Do not estimate what Maple
   would have said. Do not substitute sympy for a job you have filed — a
   cross-check is a cross-check, not a result.

Ceiling: **three open `maple:queued` issues**. The runner does one pass a
day; a longer queue is a backlog pretending to be progress. At three, stop
filing and work something unblocked.

If a filed job's spec turns out wrong, **do not edit the job directory** —
the runner checks out a sha and your edit is invisible to it. Comment on the
issue saying the spec is wrong and why, label it `maple:blocked`, then file
a new numbered job directory and a new issue. You cannot close issues; the
runner closes them, and only with a committed results directory.

### Block: it needs a decision only the overseer can make

Write it to `OPEN-QUESTIONS.md`: the question, the options, the consequence
of each, and your recommendation. Then **take the reversible default** and
carry on, marking the output `provisional on Q-n`. A choice you can undo
tomorrow is not worth a day of idleness. A choice you cannot undo — deleting
data, rewriting history, changing a frozen prompt — is not a default and
you stop that branch instead.

### Block: it needs a paper you cannot fetch

Record the claim as `[LEAD]` with the locator and what you needed from it.
Do not infer the content from the title, the abstract, or what the citing
paper says it says. A `[LEAD]` is a perfectly respectable output; an
`[INFERENCE]` dressed as `[SOURCED]` is the failure mode this whole protocol
exists to catch.

### Block: it needs a proof

If a claim is proof-shaped — a statement that something follows necessarily,
not that it fits — write the statement precisely in `lean/README.md` under
the trigger, with the hypotheses explicit. Starting the Lean project is a
separate decision and not a default. Most of what looks proof-shaped in this
repository is a `SCHEME` or a `FIT` and the Lean trigger does not fire.

### Block: a kill criterion fired

Stop that branch. Do not keep working it in a different vocabulary.

K1-K7 are in `docs/RESEARCH-PLAN.md` §3. If one fires:

1. Write the evidence up immediately, in the clearest form you can, while
   you still have the context.
2. Say in the day log that it fired, which one, and on what evidence.
3. If it is a **programme** kill (K1, K3), stop the day there and leave the
   write-up as the day's output. Do not start another package to soften it.

A kill criterion firing is the plan working. K3 in particular — the required
void curvature falling outside what observed voids provide — would be the
cleanest result this repository can produce, and it is a success.

---

## What you must not do

- **Do not push to `main`** or merge your own PR. You work on
  `research/auto-YYYY-MM-DD`, one PR for the day, updated as you go.
- **Do not rewrite history.** No force-push, no amend of a pushed commit, no
  rebase of the day branch.
- **Do not edit anything under `runs/`.** Runs are append-only, including
  runs that are wrong. Corrections belong to a later run.
- **Do not edit `prompts/01-audit-derivation-chain.md` or
  `prompts/02-adversary.md`.** They are frozen; a run's `prompt_commit` has
  to stay resolvable and a one-character change breaks the sha.
- **Do not relax a protocol rule, a validator rule, or a kill criterion.**
  Argue against it in the log if you think it is wrong.
- **Do not close a Maple issue**, and do not write anything under
  `maple/results/`. That is the runner's half of the contract.
- **Do not start a second long-running agent** against this repository. One
  session, one branch, one day. Two writers on the same files produce a diff
  nobody can review.
- **Do not fill a day.** If you run out of legitimate work, stop. See below.

---

## Stop conditions

Stop and write the day up when any of these holds:

1. **Every in-scope package is finished or blocked** — blocked on a Maple
   round trip, on WP-0, or on a question in `OPEN-QUESTIONS.md` whose
   reversible default you have already taken as far as it goes. Five
   packages is the whole day's scope and finishing them early is a good
   outcome, not an idle one.
2. **A programme kill criterion fired** (K1 or K3).
3. **You have spent the day's budget**: roughly 12 cycles, or any single
   package past 3 cycles with nothing committed. A package that cannot
   produce a commit in three cycles is mis-specified; say so in the log and
   move on.
4. **You caught yourself reformulating.** If you are restating a question in
   new vocabulary because the old vocabulary gave an answer you did not
   want, that is the end of the day's useful work. Log it and stop.

On stopping, write `logs/YYYY-MM-DD-STATUS.md`:

- which packages advanced, and to what state
- which kill criteria were tested and what the evidence was
- every Maple issue filed, with its number and what it blocks
- every `OPEN-QUESTIONS.md` entry added, with the default you took
- what tomorrow's first cycle should pick up, and why
- **what you would have done differently with one question answered.** This
  is the most useful line in the file for the overseer.

Then update the day's PR body with that status and stop. Do not merge it.

---

## Write-ups

If the day produces an answer to one of the plan's decidable claims, it gets
`explain/NNN-<slug>.md` per `explain/README.md`, written for a
late-highschooler: what was asked, what was done, what came out, and what it
does and does not settle. Plain words for the mechanism. No analogy unless
the mechanism needs one, and then one that carries real structure rather than
atmosphere.

The write-up is not a summary of your work. It is an explanation of the
result to somebody who will never read your work.

---

## Why this prompt is shaped like this

Two failure modes have already happened in this repository and this file is
mostly about them.

A session with a full budget and good intentions produced a run that stated
a comparison statistic without the free-parameter counts the repository's own
rules require — a number that looks exactly like a result. Nothing caught it
until a checker was written. Hence: every number from a committed script,
and the validator runs before the commit.

And a session told not to read a file, while holding a checkout containing
it, cannot honestly claim it did not. Hence WP-0 is not yours, and hence the
Maple spec lives at a sha rather than in an editable issue body. Where the
protocol depends on what you will not do, it is weaker than where it depends
on what you cannot do.
