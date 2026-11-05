# Has timescape already lost, on data we already have?

*What this rests on: `findings/WP-1-comparability.md`, with the arithmetic in
`verify/wp1_comparability.py`. Every source named was fetched and read in full.*

## 1. What was being asked

Two published results are sometimes treated as having already settled the
question against timescape, the model that tries to explain the supernova
observations without dark energy.

The first is a **joint fit**: take the supernova data and the baryon acoustic
oscillation data (a standard length scale imprinted on the distribution of
galaxies) and fit both at once. One independent analysis, by the Dark Energy
Survey, reports that timescape cannot fit both together, where the standard
model can.

The second is the **Hubble constant**, the present expansion rate of the
universe. Timescape's value is about 61 or 62 kilometres per second per
megaparsec. Measurements using nearby stars as a distance ladder give about 73,
with a stated uncertainty of about 1. That looks like a flat contradiction.

The question asked here was deliberately narrow: **are these comparisons fair?**
Not "is timescape right". A comparison can be against a model and still be
unfair, if the two numbers being compared are not the same quantity, or if one
side was allowed more adjustable parameters than the other.

## 2. What was actually done

No new fitting. This was a check on comparability, which means reading what was
actually fitted, counting the adjustable parameters on each side, and
reproducing the published comparison statistics from the published raw numbers
to confirm the counting.

Six papers were downloaded and read in full text. Two would not render as web
pages and were read by extracting the text from the PDFs.

## 3. What came out

### The joint fit is fair, and timescape loses it

The usual way a model comparison goes wrong is that one model is given more
knobs to turn. A model with more knobs fits better automatically, so comparing
raw fit quality is meaningless unless the knob count is equal or the extra
knobs are penalised.

Here the counts are equal. The Dark Energy Survey fitted timescape with **one**
adjustable cosmological parameter, the void fraction, and the standard model
with **one**, the matter density. Both had the Hubble constant treated the same
way, as a nuisance to be averaged over.

We confirmed that by arithmetic rather than by taking the paper's word. The
paper states its own formula for the comparison statistic, which combines fit
quality with a penalty for each parameter. Plugging the paper's published fit
qualities into the paper's published formula, with a zero difference in
parameter count, reproduces the paper's published comparison numbers. If one
model had had one extra parameter, the result would have been off by twice the
rounding error in the published table, so this check genuinely distinguishes
the two cases.

With that settled, the result stands: on supernovae **plus** the acoustic
scale, the comparison favours the standard model by a margin conventionally
described as very strong.

And the interesting part is not either number but the **flip between them**. On
supernovae alone, timescape is slightly preferred. Add one acoustic-scale
measurement to the same supernovae, and it becomes strongly disfavoured. The
whole result lives in that change, not in either fit by itself.

Two things belong alongside it. The timescape comparison uses only one external
measurement, not the full external dataset the paper's other fifteen models
were tested against, because the two models handle spatial curvature
differently. And the Dark Energy Survey itself names the weakest link in its
own pipeline: the step that corrects for observational biases is calibrated
using simulations of the standard model, and the paper says this step "holds
the biggest potential for harbouring cosmological assumptions that could
influence the cosmological results". Whether that matters is a separate piece
of work that nobody has completed.

### The Hubble constant comparison is not fair, and also not a rescue

This one is more interesting, because both the obvious readings are wrong.

**First: timescape does not have one Hubble constant. It has three.** They are
different physical quantities, not different estimates of one quantity:

- **50.1** — the rate averaged over the whole volume, measured on clocks in the
  voids
- **61.7** — the rate as inferred by observers like us, sitting inside dense
  regions, with our own clocks
- **67.5** — the volume-averaged rate converted onto our clocks

Those span 35%. We verified the relations connecting them, reproducing each
published value from the others, including from two different papers that
share no numbers in common. The published comparison picks the middle one, 61.7,
and sets it against the distance ladder, without establishing that 61.7 is what
a distance ladder measures. That is the comparability question, and it is not
established.

There is a direct warning sign. The model's own authors say that **67.5**, not
61.7, is the number that matches what the microwave background gives for the
standard model's Hubble constant. So the model already assigns different
quantities to different kinds of measurement, which means the one assigned to a
distance ladder cannot just be assumed.

**Second: the model's own stated rule excludes the distance-ladder
measurement.** Smale and Wiltshire, writing on timescape's supernova tests,
say the Hubble constant should be determined "only on scales significantly
larger than the scale of statistical homogeneity, z > 0.033, by methods which
do not depend on calibrations below that scale". The distance ladder is
calibrated using stars in galaxies much nearer than that limit. So by the
model's own criterion, this is not the right measurement to compare against.

**Third, and this is the part that stops it being a rescue: the authors do not
treat the gap as harmless.** The same section says that values of 57 to 68
"would be admissible in the TS scenario, but values as large as the recent H_0
= 74.2 ± 3.6 ... would represent a severe challenge to the model." The current
distance-ladder value, 73.04 ± 1.04, sits **4.85 of its own uncertainties
above** the model's own ceiling of 68.

**Fourth: and yet the escape route is numerically the right size.** The reason
the model excludes nearby calibrations is that it predicts the apparent
expansion rate should be **higher** when measured nearby, by up to **17%** at
roughly the distance where the ladder is anchored, falling back to the global
value further out.

The gap that needs explaining is 73.04 against 61.6, which is **18.6%**. The
predicted enhancement is up to 17%. Apply the full 17% and you get 72.07
against a measured 73.04 ± 1.04 — a remaining gap of **0.93**, under one
uncertainty.

## 4. What it means

**Neither comparison has settled this, and for different reasons.**

The joint fit is a fair comparison and timescape loses it, but it is a fit
comparison resting on a pipeline whose own authors flag a possible
standard-model assumption in it.

The Hubble constant comparison is **not a comparison of the same quantity**, so
the apparent 18% contradiction is not a contradiction. But the escape is not
free either: it works by invoking a specific prediction, that the nearby
expansion rate is enhanced by 17-22%, and that prediction has a size which
happens to match the discrepancy almost exactly.

When a discrepancy and the effect invoked to explain it are the same size, the
measurement cannot tell you which is happening. The Hubble constant question
therefore does not resolve here. It **turns into a different question**: is the
predicted nearby variation in expansion rate actually observed, at the
predicted level? That calculation has never been done. It is the obvious next
piece of work and it is not part of this session's remit.

**So the research programme does not stop.** The plan had written down in
advance a condition that would have stopped it: both comparisons confirmed as
fair and significant, *and* the supernova evidence shown not to be circular.
Neither half holds. The Hubble constant comparison is not fair, and the
circularity question is open with the available evidence running against it.

One honest note on the 17% figure. It is the predicted peak enhancement at a
particular distance, and a distance ladder is not a measurement of the
expansion rate at one distance — it is a calibration of supernova brightness
using nearby galaxies, applied to supernovae much further out. Lining those two
things up properly is exactly the work that has not been done. What is
established here is only that the two effects are the same size, which is
enough to show the comparison cannot decide anything, and not enough to say
which way it would fall.

## 5. What would change the answer

**Doing the expansion-rate variation calculation.** Construct the predicted
quantity and the measured quantity as the same statistic and compare them. If
the measured nearby variation is much smaller than 17%, the escape route closes
and the Hubble constant objection returns with real force, because the model
would then be left with a 4.85-uncertainty excursion past its own stated
ceiling.

**Checking the one measurement the model itself endorsed.** Smale and Wiltshire
named strong gravitational lensing time delays as a method that does satisfy
their criterion, since it is not calibrated by nearby stars. They cited a value
of about 62, comfortably inside their admissible band. That was 2010. Modern
time-delay measurements appear to have moved substantially higher. We did not
verify those papers, so this is recorded as a lead rather than a result, but it
is the sharpest available follow-up: **if the one method the model named as fair
no longer gives a value in its admissible band, the 17% escape does not help,
because that method is not calibrated nearby.**

**Refitting the supernovae without the standard-model bias corrections**, with
the brightness-standardisation parameters free at the same time as the
cosmology. That is what would settle whether the joint fit's supernova half is
circular. It is a substantial piece of work and no published analysis has done
it.
