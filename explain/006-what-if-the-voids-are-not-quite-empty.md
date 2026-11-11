# What if the voids are not quite empty?

**Rests on:** `maple/results/003-void-matter-refinement/`,
`verify/void_matter_sensitivity.py`, `verify/wp5_curvature_requirement.py`,
`verify/maple_job_design_checks.py`. Findings:
`findings/WP-6-two-phase-sensitivity.md`, `findings/WP-5-curvature-requirement.md`.
**Provisional on WP-0.**

## The question

Timescape explains the apparent acceleration of the universe without dark
energy. It splits space into two kinds of region:
- **walls**, which hold the galaxies and expand slowly;
- **voids**, which expand faster.

Clocks in walls and clocks in voids run at slightly different rates.
Astronomers live in walls, so they measure the universe with wall clocks, and
the difference makes the expansion look as if it is speeding up. How strong
that effect is depends on how much of the volume is void, a number called
`f_v`. The model's fits put it at about 0.70 today.

The model's equations treat the voids as **completely empty**. Real voids are
not empty; they are just very thin. So we asked two things. Does the answer
change if the voids hold some matter? And does the model's account of void
curvature survive?

## What was done

First, the model's published formula for the apparent deceleration was
rebuilt from its basic ingredients. Those ingredients are each kind of region
expanding according to ordinary gravity for its own contents, and the clock
correction the model specifies. The rebuilt formula matched the published
one exactly, symbol for symbol. That check matters: it means that what
follows is built from the model's own parts, not from something else.

Then the voids were given a small share of the matter. A region that loses
matter to its surroundings early on never gets it back, so the voids' share
of all matter, called `M_v`, is fixed from the start. Everything else follows
from it. The calculation was done twice, by two separate programs that share
no code, and they agree to at least four decimal places.

## What came out

**Splitting the voids into kinds with different curvature changes nothing.**
An empty region expands at the same rate whatever its curvature, so two empty
regions with different curvatures behave as one. This was the question an
earlier job tried to ask, and the answer is an exact "no difference".

**Putting matter in the voids changes the answer a lot.** The quantity that
says whether expansion looks accelerated is the deceleration parameter `q`.
A negative `q` means apparent acceleration. At the model's fitted void
fraction, `q` is -0.036 with empty voids. Here is how it changes:

| voids hold this share of all matter | `q` at the fitted void fraction |
|---|---|
| none | -0.036 |
| 7% | -0.007 |
| 8.5% | 0 (no apparent acceleration) |

A large survey of nearby voids found they contain about 7% of the bright
galaxies, so 7% is roughly where the real universe sits.

**The curvature holds up.** The model needs the voids to be curved in a
particular amount. That amount is exactly what an empty region expanding at
the voids' rate has, so the requirement is simply that the voids are empty.
Voids holding 7% of the matter still have 98.4% of the curvature needed. On
this point the model passes.

## What this does and does not settle

**It does not kill the model.** The threshold this programme set in advance
for "the result is an artefact of the two-region picture" is a shift of
0.0215 in the minimum of `q`. Reaching it would need voids to hold 27% of the
matter, far more than observed.

**It does show that the empty-void assumption matters.** Two of the model's
published numbers are conditional on the voids being empty:
- **the void fraction**, whose error bar is about ±0.05; the point at which
  apparent acceleration begins moves by about 0.09;
- **today's `q`**, whose error bar is 0.004; its minimum moves by about
  0.009.

Neither error bar includes this effect, and in both cases the shift is about
twice the quoted error.

**It is not a new fit.** Working out what the model's best-fit numbers would
be with matter in the voids means refitting supernova data, which is a much
larger job and outside this programme's current scope.

**Two things remain open.** The first is the exact share of matter in the
voids that the model is compared against. We have it only as a figure quoted
from a paper's summary, and it counts galaxies rather than all matter. Doing
better requires matching galaxy positions to the void catalogue this
repository already uses. The second is a reply a timescape author could
reasonably make: the "voids" in the model are only the truly empty parts.
That reply works, but it shrinks the void fraction that observations can be
compared with, and that comparison is already tight.
