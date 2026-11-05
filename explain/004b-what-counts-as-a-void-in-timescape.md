# What counts as a void, and why that decides whether the measurement bites

**Work package:** WP-4, second write-up. Numbered `004b` because `NNN` tracks
the work package and `explain/004-is-the-void-fraction-measured.md` already
holds `004`; this answers a different question inside the same package.

**Evidence:** `verify/wp4_critical_threshold.py` (14 of 14 checks pass),
`verify/wp4_void_fraction.py` (14 of 14), and the sources quoted in
`findings/WP-4-void-fraction.md` §10.

**Provisional on WP-0.** The adversarial re-run of this programme's audit has
not happened, and it could still undercut the premises everything here starts
from.

---

## The question

The timescape model has one number doing most of the work: `f_v0`, the fraction
of space taken up by voids today. Published fits put it between about 0.55 and
0.95, so the model needs most of space to be void.

`explain/004-is-the-void-fraction-measured.md` asked whether that number
matches what surveys actually measure. The answer was that the measured
fraction is a **floor**, not an estimate: the catalogue counts a smaller set of
regions than the model means by "void", so the real void fraction is at least
as big as the measurement, and could be bigger.

That argument had a hole in it. It assumed that a region a galaxy survey calls
a void really is below the model's density threshold. Nobody had checked. This
write-up is about checking it, and about what turned up instead.

## Two different definitions of "void"

**What the survey does.** The VoidFinder algorithm looks at where galaxies are.
It throws out isolated galaxies, keeps the ones sitting in dense structure, and
then grows spheres into the empty gaps between them. A void is a big empty
sphere plus the smaller spheres overlapping it. There is no density number
anywhere in that procedure. It is entirely a statement about where galaxies are
not.

**What the model does.** Timescape splits space into two kinds of region. One
kind contains everything gravitationally bound: galaxies, clusters, the
filaments and sheets they sit in. The other kind is everything else. The
boundary between them is where the model's "critical density" sits.

So the comparison has a gap in the middle: the survey counts empty space, the
model counts space below a density. To know whether the first is a subset of
the second, you need to know what the density threshold is.

## The threshold is not a number, and it cannot be one

This is the main finding, and it was unexpected.

In the standard cosmological model the critical density is a specific quantity
computed from the expansion rate: `3H^2/8(pi)G`, where `H` is how fast space is
expanding. It is one number for the whole universe at a given time.

Timescape says that formula does not apply. Wiltshire's arXiv:0712.3984, the
paper that introduces the relevant machinery, writes the relation out as a
**negation**: the critical density is *not* equal to `3H^2/8(pi)G` once the
universe is lumpy, "as the average Hubble parameter is related to the spatial
scale of averaging and the clock chosen". In plain terms: in this model there
is no single expansion rate to put into the formula, because the answer depends
on how big a region you average over and whose clock you use.

What the model puts in its place is a condition on motion rather than on
density. The boundary of a bound region is drawn where the **average expansion
is zero** - the surface at which matter is, on average, neither flying apart
nor falling together. Inside that surface things are collapsing or settled;
outside it, space is expanding. The density at that surface is then *defined* to
be the critical density, and it can differ from place to place.

So the question "what density separates wall from void in timescape?" has no
numerical answer. It is not that nobody has published one. It is that the model
does not have the kind of quantity that could be published. This matters
practically: a previous session recorded finding that number as the single thing
that would have most improved its work, and the answer is that the search cannot
succeed.

## So does the original argument survive?

Yes, by two routes that do not depend on each other.

**First, the model says how to recognise its own walls.** Wiltshire's
arXiv:0909.0749 describes the bound regions and then says, directly, that
"observationally they would correspond to all extended structures that contain
galaxy clusters, namely sheets, filaments and knots". That is the same
structure VoidFinder uses to define its walls. The step that was an unchecked
assumption is close to being the model's own instruction for how to map itself
onto a galaxy survey. What is left uncertain is narrower: whether VoidFinder
implements that mapping accurately. That is a question about a piece of
software, which is a much easier thing to be uncertain about than a question
about physics.

**Second, the assumption is hard to break numerically.** Suppose you insist on
the standard formula anyway, the one timescape rejects. Then a region reaches
critical density when its matter density is `1/(Omega_M)` times the average,
where `Omega_M` is the fraction of the critical density that matter supplies.
Across every version of this calculation - the two standard cosmologies the
catalogue was built in, and timescape's own numbers at every published `f_v0` -
the smallest answer is **1.74 times the average density**. In most cases it is
over 3.

That is the size of overdensity you find in a wall, not a void. For the
assumption to fail, a region chosen specifically for having no galaxies in it
would have to contain 74% more matter than average. That would require galaxies
to avoid matter, on scales of tens of millions of light years, which is the
opposite of what every measurement of galaxy clustering finds. It is not
impossible in principle and it is not proven false here; it is simply a long way
from what is observed.

## A mistake in the earlier work, and what it changes

Checking the above turned up an error in the previous session's reasoning, so it
is recorded here rather than quietly fixed.

If the measured fraction is a **floor** on `f_v0`, then any fitted value
*below* that floor is ruled out. The earlier work never applied the floor that
way. It asked only whether each fitted value fell inside the range of numbers
the measurement produced, and concluded that the measurement constrains nothing.

Applying the floor properly: the measured fraction is 62.3% when voids clipped
by the edge of the survey are counted, and 44.8% when they are not. Under the
first number, two published fits - `f_v0 = 0.550` and `0.557` - sit below the
floor and are ruled out. Under the second, nothing is ruled out.

So the measurement does bite, and exactly how hard depends on how you handle
voids at the survey boundary - which the earlier work had already identified as
the biggest source of error in the whole calculation. That is an honest result
and a frustrating one: the conclusion turns on the one thing least well
determined.

There is a detail worth stating plainly. The two fits ruled out are the same
two that fail a completely separate test: their implied expansion rates, 56.1
and 56.8, fall below the floor of 57 that timescape's own authors set as the
lowest admissible value. Two unrelated routes reject the same two of the three
options in that paper. The third one, `f_v0 = 0.627`, clears the void-volume
floor by 0.004 - less than the error in our own calculation - so it is neither
ruled out nor confirmed.

## What would actually settle it

The same paper by Wiltshire says where the missing volume is supposed to be.
Large voids, it reports, are observed to fill 40-50% of space, and that range
overlaps what we measured. It then adds that there are many **minivoids** as
well, and that voids of all sizes together dominate the volume.

That is the gap. The catalogue we used requires a void to be at least 10
h^-1 Mpc across, so it cannot see minivoids at all. Against our measured 62.3%,
the fit `f_v0 = 0.695` needs another 7.2% of all space in voids too small for
this catalogue, and the fit `f_v0 = 0.791` needs another 16.8%.

So the number that would decide whether `f_v0` is measurable is the volume
fraction of minivoids, computed the same way as the large-void fraction. No such
number exists in this dataset, and getting one means a deeper survey and a
separate piece of work.

## What this does and does not settle

**Settles.** Timescape has no numerical density threshold for its wall/void
split, by design rather than by omission. The earlier claim that the measured
void fraction is a floor on `f_v0` stands, and is now supported by the model's
own description of how to identify its walls. The floor rules out the two
lowest published fits, if voids at the survey edge are counted.

**Does not settle.** Whether `f_v0` is a real measurable property of the
universe. Kill criterion K5 asked whether measurement contradicts *every*
published fit, and it does not: eight of the ten survive the strongest floor
available. And the exclusion that does happen is conditional on a choice about
survey boundaries that nobody has resolved.

**Not attempted.** The survey's measured density profiles would have let us
check the assumption directly instead of arguing about it. They are published
only as pictures - low-resolution images with no accompanying numbers - so they
could not be used. Reading values off a graph by eye and presenting them as
measurements is the kind of thing this project is set up to prevent, so it was
not done.
