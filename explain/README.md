# Write-ups: the obligation and the rules

Any answer or partial answer this programme produces gets written up here
in language a late-highschooler could follow.

```
explain/
  NNN-<slug>.md     one per answer or partial answer
```

`NNN` matches the work package or run that produced the result, so a reader
can get from the prose back to the evidence.

## When one is written

At the point a work package reaches a conclusion, **including a negative
one**. A package that kills a branch gets a write-up: "here is what we
tested, here is what we found, here is why that closes this line" is
exactly the kind of result that otherwise disappears.

Not at the end of the programme. A write-up deferred to the end is a write-up
nobody can check against what was actually done, because by then the
reasoning has been reconstructed rather than recorded.

A write-up names the run or job its claims rest on, by directory. No claim
appears here that is not sourced there.

## The rules on the prose

**Explain the actual mechanism, in literal terms.** What the quantity is,
what it does, what changes when it changes. Literal description is almost
always possible and is almost always shorter than the alternative.

**No invented analogies.** In particular none of the fluent
comparison-to-everyday-objects register: no stretched rubber sheets of our
own devising, no ants on balloons, no bank accounts, no traffic. If an
analogy is not already standard in physics exposition, it does not go here.

**An analogy is permitted only when established physics exposition already
uses that specific one**, such as curved fabric for spacetime, and only
**after** the literal mechanism has been stated. The analogy is then a
second pass over something already explained, never the explanation itself.

**If a step cannot be explained literally, say so.** "We do not yet
understand this step well enough to explain what it means" is a permitted
sentence and an informative one. It is a finding about the state of the
work, and it is far more useful than fluent prose papering over a gap.
Reach for it rather than for an analogy.

**No false confidence.** Where the result is contested, the write-up says
it is contested and says by whom. Where a number comes from a fit rather
than a derivation, the write-up says it was fitted. The reading age of the
audience is not a reason to drop the uncertainty; it is a reason to state
the uncertainty in short words.

## Structure of a write-up

No fixed template, but each one answers, in order:

1. What question was being asked.
2. What was actually done. The dataset, the calculation, the fit.
3. What came out.
4. What it means, and what it does not mean.
5. What would change the answer.

Point 5 is the one that keeps the prose honest, and it is usually the
shortest.

## A test you can apply

Hand the write-up to someone who has not read the repository and ask them
to state what would have to be true for the conclusion to be wrong. If they
cannot, the write-up has explained a result without explaining the
reasoning, and it needs another pass.
