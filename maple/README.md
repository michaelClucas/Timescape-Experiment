# Maple as a daily batch service

Maple runs on a different machine, under a different account, with roughly
**one turnaround per day**. It is not a tool you call; it is a queue you
post to and read from tomorrow.

Everything downstream follows from that. A calculation that needs five
sequential Maple answers takes five days, and a work package that does not
say how many round trips it needs cannot be scheduled.

## The rule that matters

**No work package may block on more than one Maple round trip per day.**

A package needing several round trips states the number, and that number is
its minimum duration in days. Where a package can be restructured to send
three independent jobs at once instead of three sequential ones, it is, and
the plan says so.

## Layout

```
maple/
  README.md                  this file
  jobs/NNN-<slug>/
    JOB.md                   what is computed, why, the exact expected
                             output form, and what result would be
                             surprising or wrong
    job.mpl                  self-contained, no network, no interactive
                             input, one command to run
    inputs/                  any data the job needs, committed
  results/NNN-<slug>/
    RESULT.txt               verbatim Maple output, unedited
    META.yaml                Maple version, machine, date, operator, runtime
    NOTES.md                 the runner's notes, including any error
```

Numbers are allocated in order and never reused. A job and its result share
the directory name.

## Results are append-only

`RESULT.txt` is the verbatim output and is never edited, for the same reason
`runs/*/OUTPUT.md` is never edited: an edited result is not a data point. If
a job was wrong, file a new job. If the output needs interpretation, that
goes in `NOTES.md` or in the run that consumes it.

A job that errors still gets a `results/` directory, with the error in
`RESULT.txt` and what happened in `NOTES.md`. A failed job is evidence about
the job.

## A job is not ready to queue unless it states its expected output

This is the hard requirement, and it is not paperwork. With a day's latency
you cannot iterate your way to recognising a correct answer. If `JOB.md`
does not say what form the output will take and what values would be
surprising, then a wrong answer comes back looking exactly like a right one
and a day is gone.

`JOB.md` must contain:

1. **What is computed**, stated as an equation or a quantity, not a topic.
2. **Why**, naming the work package and the step `T1`-`T13` it bears on.
3. **The exact expected output form.** Not "a value for q" but "three lines,
   each `name = float`, in the order q0, f_v_signchange, q_min".
4. **What would be surprising or wrong.** A numeric range you expect, and
   what it means if the answer falls outside it.
5. **Independent check**, where one exists: how the result could be
   re-derived by another route, so a Maple bug or a transcription error is
   catchable.
6. **Equation provenance.** Every equation in `job.mpl` carries the arXiv
   identifier and equation number it came from, in a comment. An equation
   with no provenance is not allowed, because the most likely failure in
   this repository is a correct Maple run on a wrong transcription.

## Running a job

One command, from the repository root:

    maple maple/jobs/NNN-<slug>/job.mpl

The job prints its results to standard output in the format `JOB.md`
specifies, and nothing else. No plots, no `interface(prettyprint)` output
intended for a human reader, no prompts. The operator redirects stdout to
`maple/results/NNN-<slug>/RESULT.txt` verbatim.

Jobs must not use `with(plots)`, write files, or read anything outside
`inputs/`.

## META.yaml template

```yaml
job: NNN-<slug>
maple_version: ""      # exact, from kernelopts(version)
machine: ""            # which machine, since it is not the one planning
operator: ""
date: ""
runtime_seconds: null
command: "maple maple/jobs/NNN-<slug>/job.mpl"
exit_status: ""        # ok | error | timeout
expected_form_matched: null   # true | false, per JOB.md section 3
notes_file: NOTES.md
```

`expected_form_matched` is the field that makes the expected-output rule
real. A result whose form does not match what the job predicted is flagged
at the point of collection, not three weeks later.

## Transcription risk, stated plainly

The jobs in this directory were written from equations **quoted in**
`runs/01-audit-derivation-chain-2026-11-04/OUTPUT.md`, with that run's
citations, not from the papers directly. The audit quotes them with arXiv
identifiers and equation numbers, and its citation integrity was scored 2
of 3 with a complete-sweep check on locator existence but only sampled
checking of content.

So before any job is queued, its equations are checked against the cited
paper by someone reading the paper. This is a cheap check and it guards the
expensive thing: a day of Maple time spent correctly solving the wrong
system. The check is recorded in `JOB.md` under `Equation provenance`, with
who checked it and when.

Job `001` is designed so that a transcription error announces itself: it
reproduces published numbers, and a mismatch means our setup is wrong
rather than the model.
