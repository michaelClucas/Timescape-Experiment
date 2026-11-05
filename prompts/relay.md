# The relay: continuous research with no day boundary

This file replaces the *day* in `prompts/standing-loop.md` and nothing else.
The standing loop is still the operating brief: the cycle, the scope, the
overseer's standing constraints, the route around every block, what you must
not do. Read it first and follow it. This file changes four things:

1. There is no day. You work until you hand over, and your successor picks up
   where you stopped.
2. There is one branch, `research/relay`, and one PR. Not one per day.
3. The day log becomes `relay/STATE.md`, an append-only baton file.
4. When you are near the end of your context, you start your successor
   yourself. Nobody pastes a prompt. Nobody waits for morning.

Everything in `prompts/standing-loop.md` that this file does not name stays
exactly as written, and where the two appear to conflict the standing loop
wins, except on those four points.

---

## The rule this whole design rests on

**The repository is the memory. The handover is a pointer, not a container.**

You cannot pass your context to your successor. Whatever you know and have
not committed is lost at the handover, and a long prose handover does not
rescue it — it launders it, because your successor will read your summary of
your reasoning and treat it as evidence it has not seen.

So the test for every cycle is not "did I learn something" but "is what I
learned in a file, with a script that reproduces its numbers". A generation
that learned a great deal and committed little has produced nothing, however
good its handover reads.

This is why `relay/STATE.md` has a line that must say `Nothing`. If it does
not, you are trying to carry knowledge across the boundary in prose, and the
fix is to go and commit it, not to write the handover better.

---

## Generation 0: what to do if `relay/STATE.md` does not exist

You are generation 1. Create the branch and the baton:

```
git fetch origin
git checkout -B research/relay origin/main
mkdir -p relay
```

Write `relay/STATE.md` with the header below and your first block at the end
of your first cycle. Open the PR on your first push, title
`Relay: continuous research on research/relay`, and leave it open forever.
Do not merge it; the overseer merges.

```markdown
# Relay state

Append-only. One block per generation, newest last. A block is a pointer to
committed work, never a substitute for it.

Generation cap: 10. Current branch: `research/relay`.
```

---

## Step 0 of every generation, before any work

Four checks, in this order. They cost one cycle at most and they prevent the
three failures that have already happened in this repository.

**1. Is there a stop order?**

```
test -f relay/STOP && echo STOP
```

If `relay/STOP` exists, append a final block to `relay/STATE.md` saying you
stopped on the overseer's order, commit, push, and **start no successor**.
Check this again at the top of every cycle, not only here — the overseer may
write it while you are working.

**2. Has the branch been merged while the relay ran?**

```
git fetch origin
git log --oneline -3 origin/main
git log --oneline -3 origin/research/relay
```

If `relay/STATE.md` on `origin/main` already contains your predecessor's
block, the overseer merged the PR. Squash-merging has silently dropped
commits in this repository three times, so handle it explicitly:

```
git checkout -B research/relay origin/main
```

and open a fresh PR on your first push. **Do not cherry-pick, do not
force-push, do not rebuild.** If `origin/main` does not contain your
predecessor's block, stay on `origin/research/relay` and extend it.

**3. Read the baton, and only the tail of it.**

The last two blocks of `relay/STATE.md`, not the whole file. The newest tells
you what to do; the one before it tells you whether the newest generation's
plan survived contact, which is the cheapest way to notice a plan that keeps
getting restated and never executed.

Then read, in this order: `prompts/standing-loop.md`, `docs/RESEARCH-PLAN.md`,
and only the `findings/` files the newest block names. Not all of them.

**4. Has Maple returned anything?**

```
gh issue list --label "maple:done"
```

As the standing loop's step 1 says: a returned job outranks everything else,
because something downstream has been waiting on it. Read
`maple/results/NNN-<slug>/RESULT.txt`, not the issue comment.

---

## Then work the cycle exactly as the standing loop describes it

Pick the work, do the work, run the validator, commit, log. One commit per
cycle, pushed every cycle. The scope table in `prompts/standing-loop.md` is
unchanged and the out-of-scope packages are still out of scope — the relay
gives you more time, not more licence. A package the standing loop refuses by
name stays refused for every generation.

The log entry goes in `relay/STATE.md`'s current block as you go, or in
`logs/relay.md` if you prefer a running log; either way it is append-only and
a later entry that overturns an earlier one says which.

---

## When to hand over, and when to stop instead

**The relay hands over for one reason only: you are running out of context
and there is work left.** Every other reason to stop is a reason to stop
without a successor, because in every other case a successor would read your
handover, find the same wall, and either stop immediately or invent work to
fill the time. Inventing work to fill time is the exact failure this
repository exists to avoid, and a relay is a machine for doing it
indefinitely if this table is not respected.

| What happened | Successor? |
| --- | --- |
| Context running out, work left in scope | **Yes.** Hand over. |
| Every in-scope package finished or blocked on Maple, on WP-0, or on an answered-default question | **No.** Stop. The relay is done until the overseer acts. |
| A programme kill criterion fired (K1, K3) | **No.** Stop. |
| You caught yourself reformulating | **No.** Stop, and say so in the block. |
| `relay/STOP` exists | **No.** Stop. |
| You are generation 10 | **No.** Stop. |
| You have committed nothing this generation | **No.** Stop. |

Two of those deserve their reasons spelled out.

**Reformulating is a hard stop, not a handover.** If you are restating a
question in new vocabulary because the old vocabulary gave an answer you did
not want, your successor cannot detect that — it will inherit the new
vocabulary from your handover as though it were the question. Across
generations this compounds into a programme that has drifted off its own
plan with every step documented. Stop, and write down what you caught
yourself doing.

**A generation that committed nothing does not get a successor.** Eight
cycles with no commit is a stuck state, and passing a stuck state down the
chain burns the overseer's budget reproducing it. Stop and say what the wall
was.

A *branch* kill criterion firing is different from a programme one: it closes
a package, you write it up, and you carry on with the rest of the scope. Only
K1 and K3 stop the relay.

---

## How to tell you are running out of context

You cannot read a token counter. Three signals, and the first one means you
are already late:

1. **You are reading a summary of your own earlier work in this session.**
   The conversation was compacted. Detail you had is gone. Finish the current
   cycle, hand over, and say in your block that you compacted — your
   successor should distrust anything in your block that no committed file
   supports.
2. **You have completed about 8 cycles.** Hand over pre-emptively. Two
   sessions in this repository ran 4 and 7 cycles without compacting, so 8 is
   near the practical edge. This is the signal you should normally act on.
3. **You are re-reading files you already read, or you cannot recall a number
   you computed without re-running the script.** Hand over at the end of the
   cycle.

Handing over early is nearly free: the successor reads four files and is
working within a cycle. Handing over late costs the chain a generation's
worth of detail with no sign that anything was lost.

---

## The handover, in order

**1. Commit and push everything.** Working tree clean. If something is not
ready to commit, it is not ready to hand over; finish it or drop it and say
you dropped it.

**2. Append your block to `relay/STATE.md`.** This template, filled, at most
60 lines. Longer than that means you are writing prose instead of pointing at
files.

```markdown
## Generation N

**Cycles:** n. **Handed over because:** <context budget | compacted | ...>
**Branch at start:** <sha>. **At end:** <sha>.
**Commits:** <one line each: sha and subject>

### State of every in-scope package
| Package | State | Blocked on |
| --- | --- | --- |

### What the next generation should do first, and why
<one paragraph. Name the file it starts from. Concrete enough to act on
without asking a question.>

### What I established that is not in a committed file
Nothing.

### What I got wrong this generation
<every correction I made to my own earlier numbers or claims, with the cycle.
If this says "none", say so and treat it as a warning sign rather than a
clean record: both sessions that ran before this relay found several.>

### Numbers the next generation must not take on trust
<each number, and the script that reproduces it. A number with no script
does not belong in a commit, let alone in a handover.>

### Open questions whose defaults I took
<Q-n, the default, and what is provisional on it>
```

If the line under "not in a committed file" is not `Nothing`, stop writing
the handover and go commit it.

**3. Commit the block and push.** Update the PR body to the two newest
blocks.

**4. Start your successor.** One session, `context: fresh`,
`use_worktree: false` (the relay needs `.venv`, which is gitignored and would
not exist in a worktree), `cwd` this repository. Name it `ts-relay-gen<N+1>`.

Send exactly this brief, with only the generation number changed. **Do not
improve it, do not add today's findings to it, do not summarise your work in
it.** The brief is fixed so that drift cannot accumulate through it; the state
travels in the file, where it is version-controlled and the overseer can read
it.

> You are generation `<N+1>` of the Timescape-Experiment relay, working in
> `C:\Users\mluca\Documents\Timescape-Experiment`.
>
> Read `prompts/relay.md` and follow it. Step 0 is the first thing you do;
> it tells you what else to read and in what order. Your predecessor's
> handover is the last block of `relay/STATE.md`.
>
> Use `.venv/Scripts/python`. Work on `research/relay` unless step 0's merge
> check tells you otherwise. Commit every cycle, push every cycle, merge
> nothing.

**5. Stop.** Do not keep working after starting your successor, do not report
results to the overseer beyond your block, and do not wait for the successor.
Two generations working the same branch at the same time will overwrite each
other's commits.

---

## What the overseer does, and does not, have to do

Nothing, for the relay to continue. That is the point.

Three things are still only theirs: merging the PR, answering
`OPEN-QUESTIONS.md`, and running Maple. Each generation's block should make
clear what the chain is waiting on, because the relay's throughput is
eventually set by those three and by nothing the agents can do.

To halt the chain: `touch relay/STOP` and commit it, or stop the running
session. To raise the cap: edit the number in `relay/STATE.md`'s header and in
this file's table.
