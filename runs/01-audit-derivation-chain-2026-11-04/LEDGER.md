# Claim ledger, run 01

Entries in the `C1`-`C10` field format of `docs/claim-ledger.md`. The same
content is in `OUTPUT.json` under `ledger`; this file is the readable
rendering. `OUTPUT.md` Part 2 is authoritative where they differ.

Ids are `C-SN-n`, `C-CMB-n` and so on rather than `C1`, `C2`, because the
schema's example ids collide with the field names `C1`-`C10`. Noted in
`REVIEW.md`.

**Status note applying to every entry.** `EVIDENCE-RULES.md` Sec. 7:
`supported` requires confirmation from outside the proposing group. Three
outside analyses exist, all go against the model, and each has a
proponent reply disputing the setup with no counter-reply. So no entry
reaches `supported`, and `contested` is the ceiling. That is a statement
about the state of the record, not about who is right.

---

## C-SN-1. Dam, Heinesen & Wiltshire 2017, JLA

- **C1 Statement.** Bayesian comparison of timescape against flat LCDM on
  JLA supernovae at `z_min = 0.033` gives `ln B = 0.085 +/- 0.01`
  favouring timescape, with 9 free parameters on each side; at
  `z_min = 0.024`, `ln B = 0.600 +/- 0.007`.
- **C2 Source.** Dam, Heinesen & Wiltshire, arXiv:1706.07236, MNRAS 472
  (2017) 835-851, Sec. 4.1.1 and Table 3.
- **C3 Dataset.** JLA (Betoule et al. 2014), 740 SNe Ia. Minimum-redshift
  cut scanned progressively over `0.01 <= z_min <= 0.1`; headline values
  at 0.033 and 0.024. N surviving each cut is **not tabulated** in the
  paper. The homogeneity-scale justification is stated: "an average
  expansion law only holds on scales greater than the statistical
  homogeneity scale (SHS) >~70-120 h^-1 Mpc ... a CMB rest frame redshift
  of order z ~ 0.023-0.04" (Sec. 4.1.1).
- **C4 Analysis method.** March / Nielsen-Guffanti-Sarkar Bayesian
  hierarchical likelihood (Eq. 5). **Standardisation refitted, not
  inherited.** Verbatim, Sec. 4.1: "The 9 parameters {Omega_M0, alpha,
  x_1,0, sigma_x1,0, beta, c_0, sigma_c0, M_B,0, sigma_M_B,0} are then
  fit for each model". Worked from JLA's SALT2 outputs `m_B*`, `x1`, `c`,
  not from precomputed distance moduli. No host-mass step. JLA's own bias
  corrections **not applied**. JLA's tabulated CMB-frame redshifts **not
  used**, because, Appendix B: "these values also already include a
  correction, z^pec_em, for the peculiar velocity field ... of galaxies up
  to z=0.071, implicitly assuming the FLRW model"; their own boost applied
  using Fixsen et al. 371 km/s toward (l,b) = (264.14, 48.26). Priors,
  Table 1, all uniform or log-uniform: `f_v0` in [0.500, 0.799],
  `Omega_M0` in [0.143, 0.487], `alpha` in [0,1], `beta` in [0,4],
  `M_B,0` in [-20.3, -18.3], the three widths log-uniform in [-5,2].
  `H_0` fixed, degenerate with `M_B,0`. **Sampler not stated.**
- **C5 Free parameters.** Timescape **9**, flat LCDM **9**, stated by the
  paper (Table 3 column `k`; the empty universe has 8 "since
  Omega_M0 = 0"). The only entry in this ledger with matched counts
  stated by the authors for a Bayes factor.
- **C6 Comparison statistic.** `ln B_2 = ln(E_TS/E_model)`, positive
  favours timescape. Value `0.085 +/- 0.01` at `z_min = 0.033`,
  `0.600 +/- 0.007` at 0.024. Scale: Jeffreys / Kass & Raftery (1995) and
  Trotta (2008); the paper's own reading is "are statistically
  indistinguishable". `BIC = k ln N - 2 ln L` also reported.
- **C7 Systematics, the authors' own.** (i) "the empirical nature of
  light-curve fitting may mask effects due to the underlying expansion
  history if this deviates from the FLRW geometry" (Sec. 2). (ii) 0.1%
  differences in `d_L` "lead to order 1% corrections to cosmological
  parameters, which we have confirmed in our analysis" (Appendix B).
  (iii) "Malmquist type biases may not be completely corrected for in the
  JLA catalogue" (Sec. 2). (iv) "there is a marked 30% jump in c_0 as
  z_min is varied from 0.01 up to z ~= 0.033", and "there is clear
  evidence for some systematic effect at precisely the scale where we
  expect it" (Sec. 4.1.1).
- **C8 Published responses.** None found. Paper age at this run: 9 years.
- **C9 Status.** `contested`.
- **C10 What would change it.** An independent reanalysis; none exists.
  Note the paper's own result is "indistinguishable", so what would move
  the model's standing is a discriminating measurement, not a better
  supernova fit.

---

## C-SN-2. Lane, Seifert, Ridden-Harper & Wiltshire 2025, Pantheon+

- **C1 Statement.** `ln B` swings from `+2.93` (P+1690, `z_min = 0`,
  favouring timescape) to `-2.82` (P+1690, `z_min = 0.04`, favouring
  LCDM); bootstrapped P+580 gives `+1.02 +/- 0.04`; beyond `z = 0.075`
  the full sample gives `ln B ~ 0`; and the integrated P+1690 result
  "marginally favour[s] LCDM" with **no number given**.
- **C2 Source.** arXiv:2311.01438, MNRAS 536 (2025) 1752, DOI
  10.1093/mnras/stae2437, Secs. 4.7.1, 4.7.3 and Fig. 11. The `ln B`
  values are in a figure and in running text, **not in a table**.
- **C3 Dataset.** Pantheon+. P+1690 = 1690 observations / 1535 unique
  SNe, after dropping 15 "supernovae that have non-positive semi-definite
  statistical 3x3 covariance matrices". P+580 = the Pantheon+/JLA common
  subsample, 580 unique SNe / 635 observations. Also JLA580, JLA740, a
  P+1690 reduced-z sample, 50 random `N = 1000` subsamples, a size scan
  at `N = 580`-1375, and cuts at `z_min = 0.01, 0.033, 0.05, 0.075, 0.1`.
  **Discrepancy worth recording:** this paper and Seifert et al. both
  start from 1708 observations where Scolnic et al. report 1701 SNe after
  cuts (arXiv:2112.03863, Table 2); the seven-event difference is not
  explained in either timescape paper.
- **C4 Analysis method.** Nested sampling, nine parameters, `n_live =
  1000`; one cosmological parameter per model (`f_v0` versus
  `Omega_M0`); `H_0` a nuisance parameter. **Standardisation refitted**:
  `alpha` and `beta` varied with priors (Table 3), and Scolnic et al.'s
  values explicitly rejected - "Since Scolnic et al. (2022) calculate
  their nominal fit with wwCDM ... we do not use these values".
  **Pantheon+ bias corrections discarded**, verbatim: they "are not
  accounted for, as they introduce a bias towards the standard cosmology
  based on the FLRW metric". Malmquist and peculiar-velocity corrections
  also dropped; the Pantheon+ redshift treatment rejected because it
  "implicitly assumes the standard cosmological model based on the FLRW
  metric and Newtonian N-body simulations". Covariance matrix constructed
  to be as cosmology-independent as possible.
- **C5 Free parameters.** Timescape **9**, flat LCDM **9** (nine sampled
  parameters, one cosmological each, `H_0` and `M_B` among the nuisance
  set). The paper does not print a single consolidated list; this count
  is from its sampler statement and Table 3.
- **C6 Comparison statistic.** `ln B`, positive favours timescape. Scale
  cited: Kass & Raftery - `|ln B| < 1` no preference, 1-3 positive, 3-5
  strong, above 5 very strong. **The headline is cut-dependent and the
  sign flips on the same sample**, which is the finding.
- **C7 Systematics, the authors' own.** "Without the standard
  corrections, biases such as the Malmquist bias are present in our
  analysis" (Sec. 5) - the direct cost of avoiding the circularity. The
  `beta` parameter "does not converge for varying sample size". The
  Nielsen et al. framework "has some flaws in its formulation"; "The
  assumption of imposing Gaussianity may emphasise different
  characteristics of the distribution". SALT2 systematics "have to be
  investigated further before being incorporated into the algorithm".
  "more SNe Ia at high redshifts are required to be calibrated in a
  cosmology-independent manner". And the summary judgement: "As yet, we
  are not able to rule out the timescape" - non-exclusion, not
  confirmation, although the abstract says "we find evidence that the
  timescape cosmology may provide a better overall fit" than LCDM.
- **C8 Published responses.** No comment, reply, erratum or independent
  reanalysis. INSPIRE lists 26 citing records (recid 2717911), none of
  them such. The nearest independent work is the DES fit, C-SN-4. Paper
  age: 3 years from preprint, about 2 from publication.
- **C9 Status.** `contested`.
- **C10 What would change it.** An analysis that both avoids LCDM-derived
  bias corrections and corrects for selection bias. **No published
  analysis does both**, and every `ln B` here is conditional on which
  bias one chooses to carry.

---

## C-SN-3. Seifert, Lane, Galoppo, Ridden-Harper & Wiltshire 2025, Pantheon+ - the headline claim

- **C1 Statement.** `ln B > 5` favouring timescape on the full Pantheon+
  sample, and `ln B > 1` for `z_min >= 0.075`, with `f_v0 = 0.737 +/-
  0.029` against flat LCDM `Omega_M0 = 0.377 +/- 0.021`; "moderate to no
  significant preference" for `0.023 <= z_min < 0.054`.
- **C2 Source.** arXiv:2412.15143, MNRAS Lett. 537 (2025) L55, DOI
  10.1093/mnrasl/slae112, abstract, Sec. 3, Figs. 1-2. **The values are
  in figures, not a table.**
- **C3 Dataset.** The same P+1690 base as C-SN-2, with three `z_min`
  regimes as above.
- **C4 Analysis method.** "We use the Tripp equation for supernova
  standardisation alone", with `x1`, `c` and `m_B` taken directly from
  Pantheon+ and **per-supernova priors** - "directly seeding the priors
  of x1 and c with the inferred values from the SALT2 fitting algorithm",
  so the paper "does not assume any particular statistical distribution
  for x1 and c". Peculiar-velocity corrections omitted; Malmquist and
  other metric-dependent corrections not included. Host-mass step tested
  and excluded (`Delta BIC = -7.90` at `z_min = 0`, `Delta Omega_M0 ~
  0.0016`): "our final results are stated without galaxy host
  corrections". `H_0` fixed as a nuisance parameter for both models.
  **The authors attribute the large shift in evidence relative to Lane et
  al. to "the lifting of the Gaussian assumption"** - a change in the
  supernova population model, not the cosmology.
- **C5 Free parameters.** **Cannot be established.** The paper says
  "nine parameters" in one place and "only requiring five parameters" in
  another, and Table 1 lists eight rows. The three are unreconciled.
- **C6 Comparison statistic.** `ln B > 5`, positive favouring timescape,
  Kass & Raftery scale; also `Delta BIC = -13.39` against LCDM with
  curvature and `-11.70` against `wwCDM`, relative to timescape (Sec. 4).
  **Recorded as uninterpretable under ledger rule C5**, because C5 could
  not be established. Note also that the paper's own text says "the
  evidence in favour of timescape remains small but modest", which does
  not match the abstract's "very strong evidence".
- **C7 Systematics, the authors' own.** "it may, however, potentially
  overlook astrophysical systematics inherent in the SALT2 light curve
  procedure". "The largest systematic error in the Pantheon++ analysis is
  the standardisation of the heterogeneous mix". "matter model
  calibrations in the early universe must also be revisited". The
  discrepancy between full-sample and subsample results is said to
  "suggest the need for further analysis on how the redshift distribution
  of supernovae" affects the result.
- **C8 Published responses.** None. INSPIRE lists 21 citing records
  (recid 2861436); none is a comment, reply or independent reanalysis of
  the timescape supernova result. Paper age: about 23 months from
  preprint. Under C8 that is a different evidential situation from a
  claim with critiques, and should be read neither as acceptance nor as
  rejection. A promised follow-up on non-Gaussian distributions, flagged
  "in prep." in both this paper and Lane et al., has not appeared.
- **C9 Status.** `contested`.
- **C10 What would change it.** A stated and reconciled parameter count.
  That alone would move the headline statistic from uninterpretable to
  interpretable, and it is a question for the authors, not a new
  analysis.

---

## C-SN-4. Camilleri et al. (DES Collaboration) 2024, DES-SN5YR - the only independent fit to a modern sample

- **C1 Statement.** Timescape is weakly preferred over flat LCDM on
  DES-SN5YR alone (`half-Delta-AIC = -1.7`, `Delta ln S = -1.72`) and
  disfavoured once the angular BAO measurement is added
  (`half-Delta-AIC = +6.3`, `Delta ln S = +6.17`), with "a strong tension
  between the DES-SN5YR with BAO-theta*-perp datasets when fitting the
  Timescape model" - reported for none of the other 14 non-standard
  models tested.
- **C2 Source.** arXiv:2406.05048, MNRAS 533 (2024) 2615, DOI
  10.1093/mnras/stae1988, Sec. 7.8, Tables 5 and 7, Sec. 8.3. The volume
  and page come from citing papers rather than the journal page; the DOI
  is retrieved.
- **C3 Dataset.** DES-SN5YR, 1635 DES SNe plus 194 low-z. The "DES-SN5YR
  cut" adopts `z_min = 0.033` after Dam et al.: "We re-run the entire
  pipeline with this cut, which reduces our low-z sample by 68 SNe". CMB
  rest-frame redshifts excluding peculiar-velocity corrections. The CMB-R
  summary statistic is dropped for timescape and only `BAO-theta*-perp`
  is used (eBOSS-based: SDSS MGS, BOSS, eBOSS LRG, ELG, QSO, Lyman-alpha,
  plus a Planck-derived acoustic scale). Flat LCDM re-run with identical
  modifications.
- **C4 Analysis method.** Timescape tracker solution, Eqs. 44-50, with
  `Omega_m = (1/2)(1-f_v0)(2+f_v0)` derived from the single fitted
  parameter `f_v0`; `H_0` a nuisance parameter. **Standardisation
  inherited**, via the DES BBC pipeline, and the authors say so:
  "The simulations used for bias corrections within the baseline analysis
  are performed using a reference cosmology of Flat-LCDM with parameters
  (Omega_m, w)_ref = (0.315, -1.0)" and "The bias correction step thus
  holds the biggest potential for harbouring cosmological assumptions
  that could influence the cosmological results" (Sec. 2.3.2). They
  validate it: 25 realisations of simulated flat `wCDM` data analysed
  under six BBC reference cosmologies, concluding the pipeline "is able
  to return a Hubble diagram that represents the true distance versus
  redshift relation to within 1 sigma even given a reference cosmology
  that is ~10 sigma from the truth" (Sec. 4). **That validation is
  entirely within FLRW.** They also cite Marriner et al. that the
  `alpha`/`beta` fit "is decoupled from the choice of fiducial cosmology
  if the number of redshift bins is sufficiently large" (20 log-spaced
  bins).
- **C5 Free parameters.** Timescape **1** (`f_v0`), flat LCDM **1**
  (`Omega_m`), with `AIC = 2k - 2 ln L^max`. Matched. Whether `H_0`
  enters `k` is not stated.
- **C6 Comparison statistic.** `half-Delta-AIC` and `Delta ln S`
  (Suspiciousness) relative to flat LCDM. Sign convention verbatim: "A
  more negative half-Delta-AIC and Delta ln S value indicates a stronger
  preference over Flat-LCDM." Values: `-1.7` and `-1.72` on supernovae
  alone (chi-squared 1612 against 1616 for flat LCDM); `+6.3` and `+6.17`
  with BAO (chi-squared 1637 against 1624). Scale cited: Trotta (2008),
  `Delta > 1, > 2.5, > 5` for weak, moderate and strong evidence against
  the model with the higher value.
- **C7 Systematics, the authors' own.** The bias-correction reference
  cosmology, named as the biggest risk and validated only within FLRW.
  The BBC fiducial `(H_0, Omega_m) = (70, 0.3)`, which they note "may
  cause confusion within the community regarding a potential cosmology
  dependence". Fig. 9 excludes timescape from the best-fit overlays
  because "it was fit against a modified Hubble diagram".
- **C8 Published responses.** The timescape group has replied in print:
  "the BAO analysis of Camilleri et al. 2024 assumes purely geometric
  adjustments to the standard FLRW pipeline, using a LCDM calibration of
  the BAO drag epoch, which is not the case in timescape"
  (arXiv:2412.15143, Sec. 1); and "this result is encouraging for the
  timescape scenario as it suggests it may be falsifiable if its
  methodology is not fully implemented" (arXiv:2311.01438, fn. 22). No
  counter-reply from DES.
- **C9 Status.** `contested`.
- **C10 What would change it.** A timescape-native BAO drag-epoch
  calibration, which does not exist (C-BAO-1). Until one does, neither
  the DES result nor the timescape group's rejection of it can be
  adjudicated. **This is the pivotal missing analysis in the whole
  record.**

---

## C-SN-5. Smale & Wiltshire 2011, ten compilations

- **C1 Statement.** Across ten supernova compilations the
  timescape-versus-flat-LCDM Bayes factor ranges from `ln B = -4.23`
  (CSP, favouring LCDM) to `+1.09` (MLCS31, favouring timescape), with
  the sign tracking the light-curve reduction method: SALT-type
  reductions favour LCDM, MLCS2k2 reductions favour timescape.
- **C2 Source.** arXiv:1009.5855, MNRAS 413 (2011) 367-385, Tables 5 and
  6, Secs. 3.4, 4.1, 4.2, 4.3.
- **C3 Dataset.** Riess07 Gold (182), R140 (140), MLCS17 (372), MLCS31
  (366), SDSS-II (288), Union (307), Constitution (397), SALT2 (351 in
  Table 6, 352 in Table 1 - the paper's own two tables disagree), Union2
  (557), CSP (56). Each at no cut, `z >= 0.024` (the Hubble-bubble
  partition) and `z >= 0.033` (the statistical homogeneity scale, ~100
  h^-1 Mpc). At `z >= 0.033`, Union2 retains 457 of 557.
- **C4 Analysis method.** **Mixed, and this is the key field.** SALT-type
  rows were recomputed with the timescape luminosity distance, refitting
  the empirical parameters: "taking the published stretch and colour
  parameters for each supernova, and recomputing [Omega_M0] along with
  the empirical parameters M, alpha and beta" (Sec. 4.2). MLCS2k2 rows
  were analysed from **published distance moduli** "out of the box"
  (Sec. 4.1), with the cosmology step "decoupled" from the
  distance-modulus determination (Sec. 3.1) - that is, **inherited**
  standardisation. So the paper's headline reduction-method dependence is
  confounded with the refit-versus-inherit distinction, and the paper
  does not separate them.
- **C5 Free parameters.** **Not established.** The paper says the general
  timescape solution "has four free parameters" but "The solutions then
  depend effectively on two free parameters", the dressed `H_0` and
  `Omega_M0` (Sec. 2). No count is given for flat LCDM. For the SALT
  fits both models fit `alpha`, `beta`, `M` and the cosmological
  parameter, but no count is stated.
- **C6 Comparison statistic.** `ln B = ln(E_TS/E_LCDM)`, positive favours
  timescape, Jeffreys scale. Values at `z >= 0.033`: Gold `-1.18`, R140
  `+0.78`, MLCS17 `+0.57`, MLCS31 `+1.09`, SDSS-II `+0.53`, Union
  `-0.86`, Constitution `-1.06`, SALT2 `-1.55`, Union2 `-3.46`, CSP
  `-3.34`. **Under the ledger's own rule this should be recorded as
  uninterpretable, because C5 could not be established; it is reported
  here because the pattern across reduction methods is the finding, and
  `REVIEW.md` records the rule violation.** Also unreconciled: Sec. 1
  gives `ln B = -1.12` for Riess07 after correcting a numerical bug in
  Leith et al. (2008), while Table 6 gives `-1.20` for the same sample
  under wider priors.
- **C7 Systematics, the authors' own.** Residual systematics in reddening
  and extinction; intrinsic colour; Hubble-bubble degeneracy (Sec. 3.3).
- **C8 Published responses.** Kwan, Francis & Lewis, arXiv:0902.4249,
  MNRAS Lett. 399 (2009) L6, pre-dating this paper and answered by it:
  "the FB model is weakly disfavoured when using the Union compilation or
  the Constitution set (ln B = -1.38, -1.469, respectively)", with the
  core argument that "there is significant tension in the best fit
  parameters obtained from different samples, whereas LCDM is able to fit
  all datasets consistently". Smale & Wiltshire reply, Sec. 4.3: "This
  demonstrates that the main criticism of Kwan et al. 2009 is invalid
  once the SHS cut is made."
- **C9 Status.** `contested`, and partly `superseded` by C-SN-1 to
  C-SN-4.
- **C10 What would change it.** Retained not because it is current but
  because it is the only analysis that varies the reduction method, and
  it shows the sign of the preference is not a property of the data. Its
  own conclusion, Sec. 3.4: "it is fair to say one cannot reliably
  distinguish the TS and LCDM models on the basis of SNe Ia data alone."

---

## C-CMB-1. Nazer & Wiltshire 2015, Planck 2013 TT spectrum

- **C1 Statement.** A fit to the Planck 2013 TT power spectrum over
  `50 <= l <= 2500` gives `-ln L = 3925.16` for timescape under the
  headlined matching prescription, against `3895.5`-`3896.9` for flat
  LCDM over the same range, with `f_v0 = 0.627 (+0.014/-0.012)`, dressed
  `H_0 = 60.997 (+0.791/-0.733)` km/s/Mpc, volume-average age
  `16.579 +/- 0.042` Gyr and wall age `13.806 (+0.067/-0.065)` Gyr.
- **C2 Source.** arXiv:1410.3470, Phys. Rev. D 91 (2015) 063519, Secs.
  III-VI and Table 2.
- **C3 Dataset.** Planck **2013** temperature power spectrum,
  `50 <= l <= 2500`, CamSpec likelihood, cited to A&A 571, A15 (2014).
  **Not Planck 2015 or 2018.** No polarization. WMAP9 used only for `n_s`
  and `eta_Bgamma` comparison. No timescape CMB paper exists after this
  one.
- **C4 Analysis method.** **The spectrum is not computed from timescape
  perturbation theory.** A matched FLRW model is built and its spectrum
  computed with a standard Boltzmann code: "We fit the parameters of each
  matched FLRW universe by computing its CMB power spectrum with the
  CLASS Boltzmann code" (Sec. IV). Three matching prescriptions:
  `A(H-bar_dec)`, `W(k=0)`, `W(k!=0)`. The analysis must "implicitly
  assume that the key features of the CMB anisotropy spectrum are close
  to those of a FLRW model" (Sec. III). "since the effects of backreaction
  are neglected in the early Universe" (Sec. III.2); late-time ISW
  differences "will be neglected here" (Sec. III.2 item 5). emcee MCMC,
  getdist/CosmoMC, 14 CamSpec foreground and calibration nuisance
  parameters, `N_eff = 3.046` fixed in the main run, `T_0` not varied.
- **C5 Free parameters.** Timescape **5** varied cosmological
  (`f_v0`, `H_0`, `eta_Bgamma`, `n_s`, `A_s`) plus 14 nuisance; flat LCDM
  **6** base plus the same nuisance set. **These are this run's
  reconstruction from Tables 1 and 2.** The paper states no `k` for
  either side and gives no degrees of freedom.
- **C6 Comparison statistic.** `-ln L`, lower better. `3925.16` (A),
  `3897.90` (W k=0), `3896.47` (W k!=0) against LCDM `3895.5` (MINUIT) /
  `3896.9` (CosmoMC). The paper says method A is "only 0.7% larger". No
  chi-squared separate from `-ln L`, no degrees of freedom, no
  information criterion. Sound-horizon outputs, Eq. (64):
  `r_drag = 149.3 +/- 0.7` Mpc (A), `147.0 +/- 0.7` (W0),
  `147.5 +/- 0.7` (Wk), against Planck LCDM `147.34` Mpc.
- **C7 Systematics, the authors' own.** "systematic uncertainties could
  be as high as 8-13%, as compared to the 1-2% statistical
  uncertainties", and "the table uncertainties do not include any
  estimate of the systematic uncertainties" (Sec. V). "these results
  depend heavily on perturbation theory in the early Universe" (Sec. VI).
  The late ISW effect "has not yet been computed for the timescape
  scenario" (Sec. VI). The abstract: conclusions "may change if
  backreaction terms are also included". Foregrounds "do not have a
  critical impact on parameter estimation" but "we cannot entirely rule
  out" an effect (Sec. IV.5). **Matching-prescription dependence is a
  systematic the paper does not label as one:** `f_v0 = 0.628 / 0.550 /
  0.557` across the three prescriptions, a 12% spread.
  **`Omega_b h^2` is not reported for timescape.** I attempted to derive
  it and got inconsistent values by the dressed and bare routes (~0.033
  versus ~0.010), so it is recorded as unretrievable from this paper.
- **C8 Published responses.** None found. Paper age: 11 years.
- **C9 Status.** `contested`.
- **C10 What would change it.** A fit to Planck 2018 using a timescape
  perturbation calculation rather than an FLRW proxy. Neither exists.
  **Note the paper's own most important result is a withdrawal:** "we
  cannot make the claim that the timescape model solves the primordial
  lithium abundance anomaly" (Sec. V), reversing the 2013 claim after
  `eta_Bgamma` was revised from `(5.1 +/- 0.5) x 10^-10` to
  `~6.47 x 10^-10`.

---

## C-CMB-2. Duley, Nazer & Wiltshire 2013, two summary numbers

- **C1 Statement.** Matching two CMB and BAO summary numbers - the
  acoustic angle `theta* = 0.0104139` to within 2% and an effective
  comoving drag scale of `98.88` h^-1 Mpc to within 6% - yields
  `f_v0 = 0.695 (+0.041/-0.051)`, dressed `H_0 = 61.7 +/- 3.0` km/s/Mpc,
  bare `H-bar_0 = 50.1 +/- 1.7`, dressed `Omega_M0 = 0.41 (+0.06/-0.05)`,
  bare `Omega-bar_M0 = 0.167 (+0.036/-0.037)`,
  `gamma-bar_0 = 1.348 (+0.021/-0.025)`,
  `eta_Bgamma = (5.1 +/- 0.5) x 10^-10`, `z_acc = 0.46 (+0.26/-0.25)`,
  and ages `t_0 = 17.5 +/- 0.6` Gyr (volume average) against
  `tau_w0 = 14.2 +/- 0.5` Gyr (wall).
- **C2 Source.** arXiv:1306.3208, Class. Quantum Grav. 30 (2013) 175006,
  DOI 10.1088/0264-9381/30/17/175006, Sec. 3.2, Table 1, Figs. 1-5.
  Title note: the paper is "Timescape cosmology with radiation fluid",
  not "CMB constraints on timescape" as the seed bibliography has it.
- **C3 Dataset.** "recent values from the Planck satellite analysis" -
  **the paper never names the release.** Two summary statistics.
- **C4 Analysis method.** Parameter matching to two numbers with adopted
  tolerances of 2% on `theta*` and 6% on the drag scale, the looser BAO
  tolerance justified because timescape "may require recalibrating the
  baryonic and nonbaryonic dark matter proportions". The authors state
  what this is not: "not statistical constraints of the sort that could
  be obtained by fully fitting the Planck data directly".
- **C5 Free parameters.** Not stated, and not meaningful for a matching
  exercise.
- **C6 Comparison statistic.** **None.** No chi-squared, no likelihood,
  no degrees of freedom. Recorded as uninterpretable.
- **C7 Systematics.** The 6% drag-scale tolerance is itself a modelling
  choice absorbing the unrecalibrated matter proportions. The
  `eta_Bgamma` value was later revised upward, which forced the
  lithium-7 withdrawal in C-CMB-1.
- **C8 Published responses.** None found.
- **C9 Status.** `superseded` for the CMB by C-CMB-1, and its lithium-7
  claim withdrawn there.
- **C10 What would change it.** Retained in this ledger only because its
  Table 1 is the source of the bare parameter budget used in chain step
  `T8`, which is the run's central structural finding.

---

## C-BAO-1. No timescape BAO parameter constraint exists

- **C1 Statement.** No timescape analysis has ever constrained timescape
  parameters from BAO distance data. The one dedicated paper fixes
  `Omega_M0 = 0.3` as a fiducial, tests only Alcock-Paczynski isotropy,
  and finds both fiducials consistent with no anisotropic distortion;
  under the timescape fiducial the BOSS DR12 CMASS scale comes out at
  `95.4 +/- 1.6` Mpc/h against `102.6 +/- 1.5` Mpc/h under LCDM.
- **C2 Source.** Heinesen, Blake, Li & Wiltshire, arXiv:1811.11963, JCAP
  03 (2019) 003, DOI 10.1088/1475-7516/2019/03/003, Secs. 1, 2.4,
  4.1-4.2, 5, 6 and Tables 1-2.
- **C3 Dataset.** BOSS DR12: LOWZ, `0.15 <= z <= 0.43`, 361,762 galaxies;
  CMASS, `0.43 <= z <= 0.7`, 777,202 galaxies; each split NGC/SGC.
  Validated against LCDM QPM mocks (`r_BAO/alpha = 102.1 +/- 0.4` CMASS,
  `101.8 +/- 0.5` LOWZ; mock `r_s = 103.05` Mpc/h).
- **C4 Analysis method.** An empirical fitting procedure for a
  characteristic scale, applied under two fiducial cosmologies. The
  timescape fiducial has `Omega_M0 = 0.3` **fixed**, "equal to that of
  the LCDM matter density parameter", because "we aim to demonstrate
  feasibility of the method" and it "is just fixed in the present paper
  to develop the methodology". No sound-horizon calibration: "we do not
  assume any calibration of r_BAO in this study" (Sec. 4.1 fn. 11). **No
  `f_v0` or `H_0` value appears anywhere in the paper**; footnote 10 only
  says timescape `H_0` runs "around 10% smaller" than LCDM.
- **C5 Free parameters.** **Zero cosmological parameters are fitted for
  either model.** This is a fiducial comparison, not a constraint.
- **C6 Comparison statistic.** The Alcock-Paczynski anisotropy parameter
  `epsilon`. Timescape CMASS `0.021 +/- 0.017`; LCDM CMASS
  `-0.021 +/- 0.017`; LOWZ `0.013 +/- 0.110` and `-0.022 +/- 0.084`.
  Verdict, Sec. 6: "both models are consistent with no anisotropic
  distortion".
- **C7 Systematics, the authors' own.** A ~1% BAO-scale calibration
  systematic. Results "may not be suitable for extrapolation to other
  model cosmologies, depending on the Alcock-Paczynski scaling"; the
  fitting function is "left as an ansatz for other cosmologies".
  "Systematic errors in a empirical fitting procedure will inevitably be
  larger, and dependent on the cosmological model". CMB constraints on
  the BAO scale are "much less precise for timescape as compared to
  LCDM". LOWZ errors are large.
- **C8 Published responses.** None. Separately, on whether the measured
  BAO scale is model-independent, the measurement papers say it is not:
  DESI DR2's fiducial cosmology "is used to convert redshifts to
  distances" and to define the power-spectrum template, scaled to Planck
  best-fit values (arXiv:2503.14738, Sec. III.1); DES expresses
  `BAO-theta*` as ratios so `r_d` cancels and says the dependence of
  `r*/r_d` "may be neglected", which is an approximation, not a
  model-independence claim.
- **C9 Status.** `untested`.
- **C10 What would change it.** A timescape BAO likelihood with a
  timescape drag-epoch calibration. **This is the single most
  consequential missing analysis in the record**, because the DES result
  in C-SN-4 turns on exactly this and the timescape group's published
  reply asserts the calibration is different without supplying one. An
  earlier fit did use "the effective comoving baryon acoustic oscillation
  scale in galaxy clustering" as one of three summary tests (Leith, Ng &
  Wiltshire, arXiv:0709.2535, Astrophys. J. 672 (2008) L91, DOI
  10.1086/527034), which is a single scale, not a likelihood.

---

## C-HUB-1. Local Hubble flow variance

- **C1 Statement.** Timescape predicts 17-22% present local Hubble-flow
  variance, with a peak local `H_0` near dominant voids of ~72 km/s/Mpc
  at 30 h^-1 Mpc; the later review gives a local minimum
  `50.1 +/- 1.7` km/s/Mpc toward Virgo and a local maximum
  `75.2 (+2.0/-2.6)` across local voids, with an asymptotic `H_0`
  expected on 70-100 h^-1 Mpc scales.
- **C2 Source.** Prediction: Wiltshire, arXiv:0912.5236, AIP Conf. Proc.
  1241 (2010) 1182, Sec. 2; also arXiv:1311.3787, Secs. 5.3, 7 for the
  minimum and maximum. Measurement: Wiltshire, Smale, Mattsson &
  Watkins, arXiv:1201.5371, Phys. Rev. D 88 (2013) 083529, DOI
  10.1103/PhysRevD.88.083529.
- **C3 Dataset.** The COMPOSITE sample of Watkins, Feldman & Hudson as
  updated by Feldman, Watkins & Hudson: **4534 data points**, Local Group
  within 2 h^-1 Mpc excluded, nine independent full-sky samples combined,
  ~15% distance uncertainty per galaxy. Cosmicflows-II used only for
  comparison in the 2016 follow-up.
- **C4 Analysis method.** Shell-by-shell fits of the angular Hubble-flow
  variation, in both the CMB and Local Group frames, correlated against
  the residual CMB temperature dipole. The 0.5% figure is **derived
  inside the 2013 paper** in Sec. V.2 from the Local Group residual
  dipole: `delta T/T_0 = -delta z/(1+z_dec)` with `z_dec = 1089`,
  `delta T = +/-(5.77 +/- 0.36)` mK, giving `delta D = ∓(0.33 +/- 0.02)`
  h^-1 Mpc and hence "a maximum 0.5% difference" over ~65 h^-1 Mpc. So it
  is a result, not the prior prediction. The 2016 follow-up
  (arXiv:1512.07364, JCAP 06 (2016) 035) simulates a **quasispherical
  Szekeres solution**, not timescape; timescape appears there only in
  Sec. 2.2 and a footnote.
- **C5 Free parameters.** Not established; the Bayesian comparison is
  between fit forms, not cosmologies.
- **C6 Comparison statistic.** `ln B` for a scale-dependent against a
  uniform Hubble flow, Table 1: 58.62 at the innermost shell falling to
  0.49 at the outermost, with `ln B <= 1` for `r_s >= 106.25` h^-1 Mpc,
  about 3.6 at 37.5, above 5 for `r_s <= 25` and above 10 for
  `r_s < 14.5`. The paper calls it "decisive Bayesian evidence (ln B >>
  5)". Pearson `rho = -0.92` between the LG-frame variation map and the
  residual CMB dipole (Table 3); for raw COMPOSITE peculiar velocities
  `rho = -0.35` at more than 24 sigma. **This compares fit forms rather
  than cosmologies, so it is not evidence for timescape, and under the
  ledger's own rule it should not be reported without parameter counts;
  `REVIEW.md` records that.**
- **C7 Systematics, the authors' own.** Extending the velocity field over
  large distances "is merely an ansatz, whose validity remains to be
  justified". "information for the high multipoles is not reliable";
  "caution should be exercised about fitting a simple dipole in the
  outermost shells". Excluding high-scatter points means "the Bayes
  factors are somewhat reduced". Void boundaries are "subject to redshift
  space distortions as large as the Hubble flow variance". "much high
  quality data in the range 100 h^-1 Mpc <~ r <~ 150 h^-1 Mpc is needed
  to fully constrain any potential variations". Units are inconsistent
  between Secs. III.2 and III.3.
- **C8 Published responses.** **The only published exchange on whether a
  void-style test applies to timescape.** Saulder, Mieske, van Kampen &
  Zeilinger, arXiv:1811.11976, A&A 622 (2019) A83: SDSS and 2MRS
  group-scale Hubble-flow variation against Millennium Simulation mocks
  for LCDM and a deformed stronger-differential-expansion version;
  statistical tests "consistently favored LCDM over the approximated
  timescape model", with "no evidence that the variation of expansion
  differs" from LCDM. Wiltshire's reply, arXiv:1812.01586, A&A 624 (2019)
  A12: the dressed metric "cannot be obtained by a spatial rescaling of a
  FLRW metric", the dressed Hubble parameter "includes a contribution
  from the rate of change of the phenomenological lapse function" and "is
  not linearly related to any void fraction", so the model they tested
  "cannot be considered to approximate the timescape cosmology"; he
  quantifies the omitted lapse-rate term at about `-5.8` km/s/Mpc. No
  counter-reply. Separately, Shao & Bengaly, arXiv:2510.19945, Phys. Rev.
  D 113 (2026) 123510, DOI 10.1103/g5zv-xfrt: "the Hubble flow becomes
  statistically uniform at around 70-100 Mpc" and the results "are in
  good agreement with the expected Hubble variance in the standard model
  across cosmic scales of 20-150 Mpc". **Timescape is not mentioned
  there, and the two results have never been compared.**
- **C9 Status.** `contested`.
- **C10 What would change it.** Recasting the 17-22% prediction into the
  statistic Shao & Bengaly measure, on published data. **The most
  actionable item in this run:** the one distinctive prediction with both
  a prior locator and a published measurement, and the comparison has
  never been made.

---

## C-H0-1. The Hubble tension

- **C1 Statement.** Timescape does not address the Hubble tension in any
  published analysis. Its CMB-matched dressed
  `H_0 = 60.997 (+0.791/-0.733)` km/s/Mpc lies **below** Planck 2018's
  `67.4 +/- 0.5`, not between Planck and the distance ladder, and the
  supernova analyses fix `H_0` as a nuisance parameter and report no
  value.
- **C2 Source.** arXiv:1410.3470, Table 2. Planck: arXiv:1807.06209, A&A
  641 (2020) A6. Nuisance treatment: arXiv:2412.15143, Sec. 3.
- **C3 Dataset.** Planck 2013 for timescape; Planck 2018 for the LCDM
  comparison. Distance-ladder values for context:
  `73.2 +/- 0.9` (arXiv:2408.11770, full HST sample, 42 SNe, 4 anchors),
  `72.6 +/- 2.0` (JWST three-method),
  `70.39 +/- 1.22 (stat) +/- 1.33 (sys) +/- 0.70` (arXiv:2408.06153,
  CCHP TRGB), `68.81 +/- 1.79 +/- 1.32` (CCHP TRGB JWST-only),
  `67.80 +/- 2.17 +/- 1.64` (CCHP JAGB JWST-only),
  `73.30 +/- 0.92` (arXiv:2606.26831, seven-route combination, stated as
  5.6 sigma above Planck base LCDM).
- **C4 Analysis method.** **No joint early-versus-late analysis exists.**
  The only tension claim is in a Gravity Research Foundation essay with
  no journal reference, no numbers and no data fit (Wiltshire,
  arXiv:2404.02129), stating the result "potentially resolves the Hubble
  tension".
- **C5 Free parameters.** Not applicable; nothing is fitted.
- **C6 Comparison statistic.** None computed.
- **C7 Systematics.** Timescape `H_0` systematics are stated at 8%
  (arXiv:1410.3470, Sec. V). On the LCDM side the direction depends on
  the standard candle, and the CCHP authors state their result is
  "consistent with the current standard LambdaCDM model, without the need
  for the inclusion of additional new physics".
  **Downstream inconsistency to flag:** arXiv:2511.17160, Sec. 5.1.1
  adopts `f_v0 = 0.737` together with `H_0 = 73.03` km/s/Mpc attributed
  to "the best-fit results from" Seifert et al. 2025, but Seifert et al.
  fix `H_0` as a nuisance parameter and report no `H_0`. 73.03 is the
  distance-ladder value. This should be checked before being asserted,
  and it matters because a prediction of `H_0 ~ 61` and a calculation run
  at `H_0 = 73` cannot both describe the same model.
- **C8 Published responses.** None, because there is no analysis to
  respond to.
- **C9 Status.** `untested`.
- **C10 What would change it.** A timescape analysis fitting early- and
  late-universe `H_0` jointly. On present numbers the model's CMB-matched
  `H_0` is **further** from the distance ladder than Planck's is, which
  if anything makes the tension worse - but no paper computes that, so
  this is recorded as untested rather than as a failure.

---

## C-GROWTH-1. Structure growth

- **C1 Statement.** No published timescape `sigma_8`, `S_8` or
  `f sigma_8` exists. The first linear-perturbation treatment on an
  averaged background reports that in a barotropic closure the
  sub-horizon dust perturbations reverse sign and become underdensities,
  which the authors call "highly unexpected and, we argue, ultimately
  unphysical", and that "the Meszaros approximation should not be
  applicable in the timescape framework".
- **C2 Source.** Galoppo & Mourier, arXiv:2511.17160, JCAP 02 (2026) 066,
  DOI 10.1088/1475-7516/2026/02/066, Secs. 5.1.1, 5.1.2 and Figs. 1-3.
- **C3 Dataset.** **None.** A formalism paper. Initial conditions seeded
  at `z = 20` from an LCDM growing mode of amplitude `6 x 10^-5` at
  comoving scale `c/H_0`, with `Delta^(d)(t_i) ~ 3.1 x 10^-3`.
- **C4 Analysis method.** Buchert-style covariant averaging; backreaction
  and dynamical curvature modelled as an effective perfect fluid with
  pressure; two closure choices for the effective-fluid perturbations
  (comoving and barotropic). Timescape is model 1 of 4. Closure
  conditions: uniform quasilocal Hubble expansion, and radial null
  geodesic matching. The effective fluid's squared sound speed is
  negative. Parameters `f_v0 = 0.737` and `H_0 = 73.03` km/s/Mpc; see
  C-H0-1 on the second.
- **C5 Free parameters.** Not applicable; nothing is fitted to data.
- **C6 Comparison statistic.** None against data. The comparison is
  against the Meszaros approximation, not against LCDM.
- **C7 Systematics.** The barotropic-closure result is called unphysical
  by its own authors and noted as able in principle to produce anomalous
  ISW signatures. Initial conditions are seeded from LCDM, justified by
  timescape asymptoting to LCDM early. The `f sigma_8` probe is discussed
  for two of the other three models, not for timescape.
- **C8 Published responses.** None; the paper is recent and this is the
  first such calculation.
- **C9 Status.** `unverified-in-this-run`, and arguably `untested`.
- **C10 What would change it.** A timescape `S_8` calculation. Against a
  combined CMB baseline `S_8 = 0.836 (+0.012/-0.013)` (arXiv:2602.12238,
  Phys. Dark Univ. 52 (2026) 102286), timescape currently has no
  prediction to compare. The seed lists structure growth as something a
  viable alternative "must not break"; the position is that **nobody has
  checked**, which is a different thing from it being fine.

---

## C-BBN-1. Big Bang nucleosynthesis

- **C1 Statement.** No dedicated timescape BBN calculation exists. The
  only treatment is a statement that BBN is unchanged "apart from
  recalibrating the baryon-to-photon ratio and the helium abundance",
  with no computed light-element abundances, and the 2013 claim to
  resolve the primordial lithium-7 anomaly was withdrawn in 2015.
- **C2 Source.** arXiv:1410.3470, Sec. III.2 for the BBN statement; Secs.
  V and VI for the withdrawal, which the authors call "our most important
  result". Earlier: arXiv:1306.3208, Sec. 3.2 fn. 2.
- **C3 Dataset.** **None.** The 2013 paper notes "an intrinsic tension in
  the light element data between abundances of deuterium and lithium-7"
  and that for its adopted `eta` range "all abundances fall within 2
  sigma", with **no abundance numbers given**.
- **C4 Analysis method.** No calculation.
  `eta_Bgamma = (5.1 +/- 0.5) x 10^-10` in 2013, revised to
  `~6.47 x 10^-10` in 2015, which is what forced the withdrawal. The 2015
  abstract adds that the lithium issue "cannot be changed as long as the
  standard cosmology is assumed up to the surface of last scattering".
- **C5 Free parameters.** Not applicable.
- **C6 Comparison statistic.** None.
- **C7 Systematics.** The entire pre-decoupling history is assumed
  standard, so timescape inherits the standard BBN systematics plus the
  `eta` recalibration.
- **C8 Published responses.** None.
- **C9 Status.** `unverified-in-this-run`.
- **C10 What would change it.** A BBN abundance calculation with the
  timescape `eta` and expansion history. None exists. Recording this as
  fine would be an assumption, which is exactly what the ledger scaffold
  warns against.
