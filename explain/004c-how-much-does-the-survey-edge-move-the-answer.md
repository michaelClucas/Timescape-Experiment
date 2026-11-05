# How much does the edge of the survey move the answer?

Third write-up for work package WP-4. The first two are
`explain/004-is-the-void-fraction-measured.md`, which explains what the void
fraction is and why it was measured, and
`explain/004b-what-counts-as-a-void-in-timescape.md`, which explains what
counts as a void in the first place. You do not have to have read either.

Evidence: `verify/wp4_mask_resolution.py`, 16 of 16 checks pass. The result it
revises is in `findings/WP-4-void-fraction.md` §3 and §11.

---

## 1. What was being asked

Earlier work in this repository measured what fraction of the volume of a
patch of sky is inside a void — a big empty region between the sheets and
filaments of galaxies. It got **62.3%**. The astronomers who published the void
catalogue got **60.8%** from the same data.

A 1.5-point difference sounds small, and for most purposes it would be. Here it
was not, for a specific reason. The theory being tested (timescape) has a number
in it called `f_v0`, the fraction of the universe's volume that is void. The
theory does not predict `f_v0`; it is fitted to data, and different ways of
fitting give different answers. One of those fitted answers is **0.627**, and
the measurement says `f_v0` must be **at least 0.6228**. So that fit survived
by 0.004 — and the unexplained 1.5-point disagreement between the two
pipelines was **three and a half times larger than the margin that survival
depended on**.

A note from the first session had guessed where the 1.5 points came from: the
survey's **mask**. Nobody had checked the guess. That is what was checked.

## 2. What a mask is, and what was actually done

A galaxy survey does not look at the whole sky. It looks at an irregular patch,
and the shape of that patch is recorded as a **mask**: a grid covering the
whole sky, one cell per square degree, with each cell marked "looked here" or
"did not look here". There are 64,800 cells and 9,133 of them are marked.

To work out how much of the surveyed volume is void, you fill the surveyed
region with a grid of points one megaparsec apart, ask of each point "is this
inside the survey?" and "is this inside a void?", and divide the second count
by the first.

The question "is this inside the survey?" is answered by looking up the mask
cell that the point's direction falls in. **And a square degree is not small.**
At the far edge of this survey, 332 megaparsecs out, one degree of sky is 5.8
megaparsecs across. So the mask does not say exactly where the survey's edge
is. It says where the edge is to within one cell, and one cell is about six
grid points wide.

So: take the mask and **shrink** it by one cell all the way round. Then take it
and **grow** it by one cell all the way round. The real edge, whatever
convention the published pipeline used to find it, is somewhere between those
two. Recompute the void fraction for each, and you have bracketed how much the
answer can move on the strength of the mask alone.

Two other things were varied at the same time, to be sure the mask was not just
the one thing that happened to get tested: the depth the survey is cut off at,
and whether the surveyed volume is counted as grid points or calculated as a
cone. Both turned out not to matter. The spacing of the grid itself was also
doubled, to confirm one megaparsec is fine enough; it is.

## 3. What came out

| mask | void fraction |
|---|---|
| shrunk by one cell | 63.5% |
| as used before | 62.3% |
| grown by one cell | 60.5% |
| **what the astronomers published** | **60.8%** |

**The answer moves by 3.1 points between the two brackets — twice the gap that
needed explaining.** And the published 60.8% sits inside the bracket.

So the two measurements were never in conflict. They are the same measurement
with the survey's edge drawn in slightly different places, and that choice is
worth about one and a half points in either direction.

The other three things varied came to half a point between them, so the mask
really is the term that does it, rather than merely being a term that could.

**One honest limit.** This shows that a slightly more generous edge reproduces
the published number. It does **not** show that the published pipeline drew its
edge that way, because the code the astronomers used was not read. So the
measurement now has a known uncertainty of about ±1.5 points, and no way yet to
narrow it inside that band.

## 4. Why the edge matters so much, which was a surprise

The void fraction is a **ratio**: void volume over surveyed volume. Growing the
mask adds volume to the bottom of the fraction, but the added volume also gets
searched for voids, so it adds to the top too. Those two effects pull against
each other, and the obvious guess is that they mostly cancel.

**That guess was written down in advance in this repository, by the session
that did this work, and it was wrong by a factor of six.** It is recorded as
such, because recording wrong predictions is what makes the right ones worth
anything.

Here is why it fails. The voids were found by growing spheres through the
galaxy data, and those spheres **stop at the edge of the survey**, because
beyond the edge there is no data to grow through. The mask does not stop there:
grown by one cell, it claims a shell of space that the void-finding never
reached into. So that shell is counted as surveyed volume while being almost
empty of voids. Measured: the shell added by growing the mask is **17% void**,
against **62%** for the survey as a whole.

A nearly void-free shell added to the bottom of the fraction and not to the top
drags the ratio down. 57% of the volume change survives into the ratio instead
of cancelling.

## 5. What it means for the theory being tested

The measured fraction is a **floor**, not an estimate: it says `f_v0` must be at
least this big, not that it equals this. (The reason is in
`explain/004b-what-counts-as-a-void-in-timescape.md`: the voids the catalogue
can see are a subset of the volume the theory calls void.) When a floor has a
newly measured uncertainty, the honest floor to use is the **lowest** value in
the range, because that is the one you can defend.

The lowest value is **0.6045**. Against it:

| one paper's three ways of fitting `f_v0` | value | ruled out? |
|---|---|---|
| matching `A(H̄_dec)` | 0.627 | no, by 0.023 |
| matching `W(k ≠ 0)` | 0.557 | **yes** |
| matching `W(k = 0)` | 0.550 | **yes** |

**The conclusion reached before this check is unchanged, and now rests on
firmer ground.** Two of the three are ruled out, and they are ruled out no
matter where in the bracket you put the survey's edge — they are 0.05 below
even the most generous floor. That was the result at risk, and it held.

What did change is how the third one stands. Before, 0.627 survived by 0.004,
which was less than the disagreement nobody had explained. Now it survives by
0.023 against the defensible floor — but against the *strictest* floor in the
bracket, 0.6352, it would be ruled out too. So: **whether that third way of
fitting the theory survives the measurement depends on where you draw the edge
of a survey, to within one degree of sky.** It is not ruled out. It is not safe
either.

Worth saying plainly: those three numbers are three ways **one paper** fits
**one dataset**, and they disagree with each other by far more than the error
bars they each quote. That, rather than anything here, is the main problem WP-4
found with `f_v0`, and this check does not touch it.

## 6. What would change the answer

- **Reading the code the published pipeline used** to decide whether a point is
  inside the survey. That would replace the ±1.5-point bracket with a single
  number and would settle whether 0.627 is ruled out. It is a small job, but it
  needs the software, not the paper, and was not done here.
- **A survey with a smaller edge-to-volume ratio.** All of this is an edge
  effect, and a deeper or wider survey has proportionally less edge.
- **Finding out that the floor is not a floor.** The whole chain above rests on
  the voids the catalogue sees being a subset of what the theory means by void.
  That argument is in `findings/WP-4-void-fraction.md` §4 and §10.2, and if it
  is wrong, none of the exclusions above follow.

Everything here is also conditional on something larger that has not happened
yet: an independent adversarial audit of the reasoning this whole repository
rests on, filed as WP-0. Until that runs, this is marked **provisional**.

---

# Added later the same day: the code was read, and it found a mistake of ours

Section 3 above says the published pipeline's own code "was not read", and
section 6 said reading it would settle whether `f_v0 = 0.627` is ruled out.
**It has now been read.** Evidence: `verify/wp4_vast_mask_convention.py`, 10 of
10 checks pass. Details in `findings/WP-4-void-fraction.md` §12.

## What the code says

The software is called VAST, it is public, and it both **wrote** the mask file
we have been using and **reads** it when finding voids. The two places where it
writes and reads the mask use the same line of arithmetic to turn a declination
into a row number of the mask grid. We used different arithmetic.

The difference sounds like nothing and is not. Both versions take a
declination, scale it, and chop off the fractional part to get a whole-number
row. Ours adds 90 **before** chopping; VAST adds 90 **after**. For declinations
north of the equator the two give the same row. For declinations south of it
they are **one row apart**, because chopping the fractional part off a negative
number moves it *up* while chopping it off a positive number moves it *down*.

About 2% of this survey's patch of sky is south of the equator, reaching about
11 degrees down.

**A grid has to be read the same way it was written**, or you are reading the
wrong row. The file was written VAST's way. So this is not two defensible
conventions; **ours was simply wrong for this file.**

## What it changes

| | Planck2018 | WMAP5 |
|---|---|---|
| what we had been reporting | 62.28% | 62.63% |
| **corrected** | **61.57%** | **61.92%** |
| the astronomers' published value | 60.8% | 61.1% |

So we were overstating the void fraction by about 0.71 points, and correcting it
**halves** the remaining disagreement with the published number, from about 1.5
points to about 0.8. Everything section 3 above says still holds: the published
value is still inside the ±1.5-point bracket, and the two measurements were
never in conflict. They now agree better than this write-up first said.

## Why none of our checks caught it

The script that computes the void fraction does check its mask convention. It
confirms that all 1,163 void centres land inside the surveyed patch, and that
only 17% of them do if you swap the two axes. That test catches a swapped
mask. It cannot catch a mask read one row off, because moving the whole patch
by one degree still leaves essentially every void centre inside it.

The check was right about what it tested and silent about this. That is the
third time in three days that a passing check turned out not to establish the
thing it was being relied on for — and all three were caught by writing down,
in advance, what the answer ought to be, and then being wrong.

## What it does to the conclusion, which is less than you would hope

Recomputing section 5's table with the corrected floor:

| one paper's three ways of fitting `f_v0` | value | ruled out? |
|---|---|---|
| matching `A(H̄_dec)` | 0.627 | **still undecided** |
| matching `W(k ≠ 0)` | 0.557 | **yes** |
| matching `W(k = 0)` | 0.550 | **yes** |

The two that were ruled out are **still** ruled out, and by a wider margin than
before relative to nothing having changed in their favour. That result has now
survived three separate attempts to break it.

But **0.627 is still undecided**, and this is the honest and slightly
disappointing part. Reading the code was supposed to replace the ±1.5-point
bracket with one number and settle it. It did not, because the bracket does not
come from the arithmetic we got wrong. It comes from the mask being stored at
one-degree resolution in the first place, which is a property of the file and
not of anyone's code. Fixing our arithmetic moved the centre of the bracket;
the bracket is the same width, and 0.627 is still inside it.

**So: a real mistake found and fixed, the agreement with the published work
improved, and the question it was all meant to settle still open.** That is a
normal outcome and worth stating plainly rather than dressing up.

## One more thing that was looked for and is not there

The actual code that produced the published volume fractions **is not in VAST
at the date of the paper.** The module that does exactly this calculation —
place a grid, keep the points inside the survey, count how many are in voids —
was added to VAST in February 2025, three years after the paper was submitted.
At the paper's own date the software contains no such code at all. It also, in
its 2025 form, throws away every grid point within 30 megaparsecs of the survey
border, which is not what the paper describes doing.

So how the published denominator was defined is still unknown, and cannot be
found out from this software. It is worth about 0.02 points, so it changes
nothing — but "we do not know" is the accurate answer and it is better than a
guess.
