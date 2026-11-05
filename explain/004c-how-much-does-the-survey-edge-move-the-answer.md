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
