# Is the void fraction a measurement or a fitted number?

*What this rests on: `findings/WP-4-void-fraction.md`, with the calculations in
`verify/wp4_void_fraction.py` and `verify/wp4_fv0_comparison.py`. The data are
the VAST void catalogues for SDSS DR7, `doi:10.5281/zenodo.11043278`, with
provenance in `data/001-sdss-dr7-voids/`.*

## 1. What was being asked

The timescape model explains why distant supernovae look dimmer than a simple
expanding universe predicts, without using dark energy. Its explanation runs
through one number: **the void fraction**, written `f_v0`. That is the
proportion of the universe's present volume that sits in near-empty regions
rather than in the sheets and filaments where galaxies live. In the model's
fits, `f_v0` is around 0.7, meaning about 70% of space is void.

That number is doing almost all the work. The model's whole effect comes from
clocks running at slightly different rates in empty regions than in dense ones,
and how much that matters depends on how much of space is empty. So a fair
question is: **is 0.7 something we have measured, or is it a knob that was
turned until the supernova data fitted?**

If it is measured, the model is making a real prediction and getting it right.
If it is a knob, the model is describing the data rather than explaining it.

## 2. What was actually done

Two separate pieces of work.

**First, measure how much of space is void.** Astronomers have catalogues of
voids found in real galaxy surveys. We used three of them, all built from the
same survey, the Sloan Digital Sky Survey's seventh data release, out to a
distance where light has been travelling about 1.5 billion years. The three
catalogues use three different computer algorithms to decide what counts as a
void.

We did not take the published percentages. We downloaded the catalogues and
computed the fraction ourselves, by filling the surveyed region with test
points one megaparsec apart (a megaparsec is about three million light years)
and counting what proportion of them fall inside a void. That is roughly 27
million test points. Doing it ourselves matters, because it turned up two
things the published tables do not say, both in section 4 below.

**Second, collect every value of `f_v0` the model has ever been fitted to**, and
see whether they agree with each other and with the measurement. Ten values,
from eight papers, all read in full rather than quoted from abstracts.

## 3. What came out

**The measurement.** Using the algorithm whose result we could reproduce,
voids fill **62% of the surveyed volume**. If you throw away voids that touch
the edge of the survey, where we cannot see the whole void, the figure drops to
**45%**.

That 62-versus-45 gap is not a detail. It is the single largest uncertainty in
the whole measurement, far bigger than the uncertainty from assuming a
particular expansion history, and nobody had published the 45% figure.

**The fitted values.** Ten of them, ranging from **0.550 to 0.95**.

The sharpest comparison is inside a single paper. Nazer and Wiltshire (2015)
fitted the model to one dataset, the cosmic microwave background, three times
over. The three attempts differ only in a technical choice about how to connect
the model's geometry to what the microwave background measures. They got
**0.627, 0.550 and 0.557**, and each came with a stated uncertainty of about
**±0.016**.

Those three numbers are meant to describe the same universe, from the same
data, by the same authors. They disagree with each other by about five times
their own stated uncertainties. Across the whole literature the spread is
roughly **fifteen times** the smallest quoted uncertainty.

## 4. What it means

**`f_v0` is not currently a measured quantity.** It is a fitted one, and the
fits do not agree with each other. That is the answer to the question asked.

It is worth being precise about what this does and does not show, because there
is a stronger claim available that the evidence does **not** support.

The stronger claim would be: *the measurement contradicts the model*. It does
not. The research plan had written down in advance that if the measured void
fraction ruled out every fitted value, that would stop this line of work. It
does not rule them out. Two of the fitted values, 0.550 and 0.557, sit inside
the measured range, and the rest sit above it in a way the measurement cannot
object to, for a reason explained next.

**Why the measurement cannot object.** The model and the void catalogues are
not counting the same thing.

Timescape divides space by **density**. A region is "wall" if its density is
above a particular critical value, and "void" if below. That is the definition
in the model's own papers.

A void-finding algorithm divides space by **where the galaxies are**. The
algorithm we reproduced grows spheres outward from empty patches until each
sphere runs into four galaxies, and calls the result a void. There is no
density threshold in that procedure at all.

These give different answers, and crucially they differ in a known direction. A
region with no galaxies in it is, barring unusual circumstances, below the
critical density. But the reverse is not true: plenty of below-critical space
has galaxies in it. So the regions the algorithm finds are a **subset** of the
regions the model calls void.

That makes the 62% figure a **floor**, not an estimate. The true fraction of
space below critical density is at least 62%, and could be considerably more.
A floor of 62% has nothing to say against a fitted value of 0.791. It is
consistent with it, and with 0.9, and with 0.95.

**Two things we found by doing the arithmetic rather than reading the tables.**

The published catalogue paper states that voids clipped by the survey edge are
excluded from the properties it tabulates. For the volume percentage, they are
not: our edge-included 62% matches the published figure and our edge-excluded
45% does not. Anyone taking the published number at face value will think the
edge problem has been handled when it has not.

And for two of the three algorithms, we could not reproduce the published
volume fraction at all. We get 74% where the paper says 68%, and 81% where it
says 91% — too high in one case and too low in the other, so it is not one
mistake pointing one way. We can explain part of it: those catalogues report a
void's size as a radius derived from a volume, and that volume is set to zero
for cells touching the survey boundary, so the radius understates the real
extent. But that explanation would make both of our figures too low, and one
of them is too high. **We do not know what the rest of the discrepancy is**,
and reconstructing it would need the galaxy positions, which are not part of
the published dataset. We have recorded it as unexplained rather than guessing.

That last point has a consequence. The plan expected to use the disagreement
*between* the three algorithms as the measurement's uncertainty. That
disagreement is precisely what this dataset does not let us establish
independently.

**A worry that turned out smaller than expected.** Before any of this was
computed, we wrote down a concern: the void catalogues give positions in
coordinates that were calculated by assuming a particular expanding-universe
model, and it is not timescape's model. Using them to test timescape risks
circular reasoning.

The concern is sound, and it turns out to cost about **2 percentage points**
here, against the 17 points from the edge problem. The reason is that the void
fraction is a **ratio** of two volumes. If you stretch every distance in the
universe by the same factor, both volumes stretch equally and the ratio does
not change at all. What does change the ratio is the way distances get
stretched *differently* at different depths, and across a survey this shallow
that effect is small. On a deeper survey it would not be.

So the circularity is real, is quantified, and is not what limits this answer.

## 5. What would change the answer

**A measurement that counts the same thing the model counts.** Someone would
have to measure the fraction of volume below the critical density, rather than
the fraction occupied by algorithmically identified voids. That needs a density
field, not a void catalogue. If that fraction came out at, say, 0.62 ± 0.02, it
would exclude most of the fitted range and this would become a very different
result.

**Re-running the void finders under timescape's own distance relation.** We
did not do this, and the reason is worth stating because it is not laziness.
The algorithms decide what is a void using the galaxy positions. Changing the
distance relation moves the positions, so the voids have to be found again
from scratch. Converting the published void sizes to a new distance scale would
move the voids without moving the galaxies, which is a different calculation
and would give a number that looks like an answer and is not one. Doing it
properly needs the underlying galaxy catalogue and is a piece of work in its
own right.

**A deep survey.** The edge problem shrinks as the surveyed volume grows,
because a smaller share of voids touch the boundary. That is the single
cheapest way to turn the 17-point uncertainty into something small.

**And the thing that would change the conclusion most.** If the model's own
fits were made to agree with each other, `f_v0` would start to look like a
parameter with a value. At the moment three fits to one dataset, differing only
in a technical matching choice, give three answers that are incompatible on
their own error bars. Until that is resolved, no measurement can usefully be
compared against "the" fitted value, because there is not one.
