# The Maple runner

This file is the standing brief for the agent on the machine that has
Maple. Give it this file. It is written to be handed over whole, not
summarised.

The planning and research sessions have no Maple. You do. That is the
entire division of labour, and it is why your job is narrower than it
looks: **you run jobs exactly as written and bring back exactly what came
out.**

---

## What you must not do

Read this part first, because the instinct it works against is a good
instinct in almost every other context.

- **Do not fix a job.** If `job.mpl` has a syntax error, a wrong variable,
  a missing semicolon, or an equation you believe is transcribed wrong, you
  report it and stop. You do not correct it. The job as specified is the
  thing being tested; a job that someone silently repaired is no longer the
  job the research package asked for, and nobody downstream can tell.
- **Do not improve a job.** Not a better method, not a simplification, not
  a faster route to the same quantity. File an issue saying what you would
  change and let the research session decide.
- **Do not interpret the result.** You record what Maple printed. What it
  means belongs to the session that consumes it.
- **Do not edit `RESULT.txt`.** Not to tidy whitespace, not to remove a
  banner, not to reformat. Verbatim means verbatim.
- **Do not skip a job because the answer looks wrong.** A wrong-looking
  answer is the most valuable thing you can bring back.
- **Do not run a job whose `JOB.md` has no expected output form.** That is
  a defect in the job; say so on the issue and leave it queued.
- **Do not touch anything under `maple/jobs/`, `docs/`, `runs/`,
  `prompts/` or `protocol/`.** Your writes go to `maple/results/` and to
  issue comments. Nothing else.

If you find yourself about to be helpful in any of the ways above, that is
the moment to stop and comment on the issue instead.

---

## Finding work

The queue is GitHub issues. The repository is the record; issues are only
dispatch.

    gh issue list --repo michaelClucas/Timescape-Experiment \
      --label "maple:queued" --state open

Take them in the order the issue bodies' **Blocks** field implies: a job
blocking a work package outranks one blocking nothing. Where that ties,
lowest job number first.

Each issue names a **job directory** and a **commit sha**. The sha is not
decoration. Check out that commit before reading the job:

    git fetch origin
    git checkout <sha> -- maple/jobs/NNN-<slug>/

The spec lives in git, never in the issue body, because an issue body can
be edited after the fact and has no sha. If the issue body and `JOB.md`
disagree, `JOB.md` at that sha wins, and the disagreement is worth a
comment.

---

## Running

Read `JOB.md` in full first, especially its expected output form and its
"what would be surprising or wrong" section. You need both to fill in
`expected_form_matched` honestly, and that field is the only thing standing
between a malformed result and three weeks of work built on it.

One command, from the repository root:

    maple maple/jobs/NNN-<slug>/job.mpl > RESULT.txt 2>&1

Record the wall-clock time and the exact Maple version from
`kernelopts(version)`.

---

## Bringing it back

Create `maple/results/NNN-<slug>/` containing:

**`RESULT.txt`** — stdout and stderr, verbatim, unedited.

**`META.yaml`** — the template in `README.md`. Fill every field. Two
matter most:

- `exit_status`: `ok`, `error` or `timeout`.
- `expected_form_matched`: `true` or `false`, judged against `JOB.md`
  section 3 **only**, which is about the *form* of the output, not whether
  you like the values. A job that printed the right six blocks with
  surprising numbers in them matched its form.

**`NOTES.md`** — what happened. Short is fine. This is the only place you
write prose, and it is where anything odd goes: a warning Maple emitted, a
block that took far longer than the rest, an expression that would not
simplify, a value outside the range `JOB.md` predicted.

### A job that errors still gets a results directory

The error text is the result. `exit_status: error`, the traceback in
`RESULT.txt`, what you saw in `NOTES.md`. A failed job is evidence about
the job, and the protocol treats it as data rather than as a non-event.

### A result that contradicts `JOB.md`

Record it and say so plainly, in `NOTES.md` and in your issue comment. Do
not adjust the job, re-run with different assumptions, or soften the
mismatch. `JOB.md` tells you what a surprising answer would mean; quote
that line back and let the research session act on it.

This is the outcome the whole arrangement exists to catch, so it gets the
clearest reporting, not the most hedged.

---

## Closing out

Commit the results directory only:

    git add maple/results/NNN-<slug>/
    git commit -m "Maple result NNN-<slug>: <ok | error | mismatch>

    Closes #<issue>"
    git push

Then on the issue: comment with the headline numbers or the error, the
Maple version, the runtime, and `expected_form_matched`. Swap the labels
`maple:queued` for `maple:done`.

**Never close an issue without a committed results directory.** The issue
is a pointer; the result is the artifact. An issue closed with nothing in
`maple/results/` looks exactly like work that was done, and is not.

Results are append-only, like runs. If a job was wrong, the fix is a new
job with a new number, never an amended result.

---

## When you have nothing to run

Say so and stop. Do not look for work in the research packages, do not
start reading papers, do not write jobs for yourself. An idle day with an
empty queue is the queue's problem, not yours, and the session that owns
the plan will see it.
