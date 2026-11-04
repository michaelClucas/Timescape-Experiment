# The claim ledger (scaffold, v0)

The scaffold for this experiment. Every empirical claim about timescape
gets one ledger entry with these fields. This replaces the loose
"timescape fits the data" with something that can be checked field by
field.

## Fields

### C1. Statement
The claim, in one sentence, quantitative where possible. "Timescape is
preferred by supernova data" is not a claim. "Bayesian model comparison on
Pantheon+ with cut z > 0.075 gives log evidence favouring timescape over
LCDM by X" is a claim.

### C2. Source
Primary source with a locator retrieved in this run. Author, year, arXiv
id or DOI, and the specific section, table, or figure.

### C3. Dataset
Which data, which release, which selection cuts, how many objects. Cuts
matter enormously here: timescape's distinctive signature is at low to
intermediate redshift, and a redshift cut is a modelling choice that can
be argued either way.

### C4. Analysis method
Likelihood, sampler, priors, nuisance-parameter treatment. For supernovae
specifically: how light-curve standardisation parameters are handled, and
whether they were refitted per cosmology or inherited from an LCDM-based
calibration. Inherited standardisation is a known route to circularity
and must be recorded explicitly.

### C5. Free parameters, both sides
A count for timescape and a count for the comparison model. Information
criteria and Bayes factors are meaningless without this, and it is often
omitted in summaries.

### C6. Comparison statistic
What was computed: Bayes factor, AIC, BIC, chi-squared per dof. Its value
and the stated interpretation scale. A Bayes factor described only as
"moderate" or "strong" with no number is not usable.

### C7. Systematics acknowledged
What the authors list as their own leading systematics.

### C8. Published responses
Replies, critiques, failed or successful replications, with locators. If
none exist, say so and give the paper's age, because a 2025 result with no
replies yet is a different evidential situation from a 2011 result with
none.

### C9. Status
One of: `supported`, `contested`, `superseded`, `untested`,
`unverified-in-this-run`.

### C10. What would change the status
The specific measurement or analysis that would move it. If nothing
foreseeable would, say that, because an unfalsifiable claim is a finding.

---

## Datasets the audit must cover

Each gets at least one ledger entry, or an explicit `untested`.

**Type Ia supernovae.** The headline evidence. Both the recent Pantheon+
analyses and the earlier work. Pay attention to C4 and C5 here above all;
the standardisation question is where this evidence is strongest or
weakest and summaries almost never say which.

**CMB acoustic peaks.** Timescape must reproduce the peak positions with a
different calibration of the sound horizon and a different
distance-redshift relation. This is a severe test and the audit should
establish how well it is actually met, with numbers, not whether it is
claimed to be met.

**BAO.** Same issue, plus the question of whether the BAO scale as
*measured* is model-independent or was extracted under LCDM assumptions.

**Local Hubble flow variance.** Timescape predicts specific variance and
possible anisotropy in the locally inferred expansion rate. This is a
distinctive prediction rather than a refit of existing data, so it carries
more weight than a good fit to supernovae. Find out what was predicted,
when, and what has been measured since.

**Hubble tension.** Whether timescape addresses the early-versus-late H0
discrepancy, and whether that is a derived consequence or an additional
fit.

**Structure growth and BBN.** Any viable alternative must not break these.
If the audit cannot establish that timescape is consistent with them,
record `unverified-in-this-run` rather than assuming it is fine.

---

## Rules

- A claim with no C2 locator is a `[LEAD]` and goes in the unverified
  list, not the ledger.
- C5 is not optional. If the parameter counts cannot be established, C6
  is recorded as uninterpretable.
- Never report C6 without C4 and C5 in the same entry.
- A paper's own abstract is not a source for C7 or C8.
- `supported` requires an independent analysis, not only the proponents'.
  If the only analyses are by the model's authors, the status is
  `contested` at best, regardless of how good the analysis is. This is not
  a judgement about the authors; it is what the word means.
