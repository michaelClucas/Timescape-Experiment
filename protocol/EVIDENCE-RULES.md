# Evidence rules

Binding on every agent run in this repository. Violations invalidate a run
as research.

## 1. Citations

- Usable only if retrieved in this run, or given a locator precise enough
  to check: DOI, arXiv id, or journal volume and page.
- Author plus year is a **lead**, tagged `[LEAD]`. Never promote a lead to
  a citation by inference. A plausible arXiv number is worse than none,
  because it is built to survive review.
- Cite the specific section, equation, table, or figure when the claim is
  specific. "They show this in the paper" is not usable for a numeric
  claim.
- Attribute to the source where the claim was made, not to a review
  describing it, unless the review is what you are citing.

## 2. Confidence tags

Every substantive claim carries exactly one:

- `[SOURCED]` retrieved a primary source in this run that states it.
- `[LEAD]` believed from background knowledge; locator unverified.
- `[INFERENCE]` the run's own reasoning from sourced material. Name the
  premises.
- `[UNKNOWN]` could not establish. Say what would settle it.

`[INFERENCE]` is welcome. Disguising it as `[SOURCED]` is the failure this
document exists to prevent.

## 3. Kind before quality

Before judging whether a step is well supported, say what kind of claim it
is: theorem, scheme, postulate, fit, or interpretation. Most confusion in
this literature comes from a `SCHEME` or a `POSTULATE` being discussed as
though it were a `THEOREM`, by advocates and critics alike.

When unsure of the kind, say so. An honest "I could not tell whether the
Cosmological Equivalence Principle is an additional postulate or a
consequence of GR, and here is why that is unclear" is a better result
than a confident wrong tag.

## 4. Numbers or nothing

- A model comparison is reported with the statistic, its value, the
  dataset and cuts, the priors, and the free-parameter count on **both**
  sides. Any of those missing, say which.
- Never report a Bayes factor or information criterion by its verbal
  label alone.
- "Fits the data well" is not a claim. Give chi-squared per dof, or the
  evidence, or say the number was not available.
- A fit to a superseded data release is reported with the release named.

## 5. Live disputes stay live

Where the literature is unresolved, the output says unresolved and states
both positions in their proponents' own terms. This binds in both
directions: reporting timescape as refuted is as much a failure as
reporting it as established.

If you notice yourself writing a sentence that would satisfy both sides of
a real disagreement, delete it. Smoothing is the characteristic failure of
fluent summarisation and it destroys the only thing this repository is
trying to produce.

## 6. Proponent framing is not neutral framing

Timescape has one dominant proponent and a modest literature. Background
knowledge about it is therefore likely to carry that proponent's framing,
including which objections are treated as serious. Treat your own prior
sense of what is settled as unreliable, and go to the critics directly
rather than to proponents' characterisations of them.

The same applies in reverse to the incumbent model. Do not import the
standard-cosmology default that an alternative must be wrong.

## 7. Independence

A result is `supported` only when someone outside the proposing group has
reproduced or confirmed it. Otherwise it is `contested` at best. This is
not a judgement about anyone's competence; it is what independent
confirmation means, and in a small field it is frequently absent. When it
is absent, say so plainly rather than treating author-count as a proxy.
