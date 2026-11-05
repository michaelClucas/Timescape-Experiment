# WP-1: are the two "already decided" comparisons like-for-like?

**Status:** complete, for the comparability question only. No refit was done
and none is in scope: fitting supernovae is WP-2.
**Provisional on WP-0.** Run 02 has not run and K7 could invalidate the audit
premises this package started from.
**Evidence:** `verify/wp1_comparability.py`, 19 of 19 checks pass.
**Kill criteria tested:** K1. **It does not fire.** Two independent reasons,
in §4.

---

## 1. What was asked

`docs/RESEARCH-PLAN.md` WP-1 flags two published results that Run 01's
discrimination table marks as "arguably already decided against timescape":

- the supernova + BAO joint fit of Camilleri et al. (DES), reporting tension
  for timescape where flat LCDM has none;
- the dressed `H_0` of `60.98`-`61.7` km/s/Mpc against local determinations of
  `70`-`73.3`.

The package's whole job: establish **what was fitted, with how many free
parameters on each side**, and for `H_0` whether the two numbers are the same
quantity. Not whether timescape is right.

## 2. Sources, all fetched and read in full text

Nothing below is from an abstract alone, a citing paper, or a search snippet.
Where a value is from an abstract, the abstract was fetched.

| Tag | Source | What was used |
|---|---|---|
| `[DES]` | Camilleri et al. (DES), arXiv:2406.05048, MNRAS 533 (2024) 2615, DOI 10.1093/mnras/stae1988 | Tables 5/6, Table 7, Sec. 7.8, Eq. (49) |
| `[SW11]` | Smale & Wiltshire, arXiv:1009.5855, MNRAS 413 (2011) 367 | Sec. 2, Eq. (17) |
| `[DNW13]` | Duley, Nazer & Wiltshire, arXiv:1306.3208 | parameter table, p. 9 |
| `[W19]` | Wiltshire, arXiv:1812.01586, A&A 624 (2019) A12 | Secs. 2-3 |
| `[LNW08]` | Leith, Ng & Wiltshire, arXiv:0709.2535, ApJ 672 (2008) L91 | abstract |
| `[R22]` | Riess et al. (SH0ES), arXiv:2112.04510, ApJL 934 (2022) L7, DOI 10.3847/2041-8213/ac5c5b | abstract |

## 3. The joint fit: like-for-like, and it confirms

`[SOURCED]` `[DES]` Sec. 7.8 states the timescape model has **one** free
cosmological parameter, the void fraction `f_v0`, with `H_0` marginalised as a
nuisance parameter. Flat LCDM as fitted in the same pipeline has one free
cosmological parameter, `Omega_m`, with the same nuisance treatment. The
dressed matter density is not independent: `Omega_m = (1/2)(1 - f_v0)(2 + f_v0)`,
`[DES]` Table 6 footnote.

So `k = 1` on both sides. Run 01 recorded this and it is now confirmed, and
confirmed **arithmetically** rather than by reading the prose. `[DES]` defines
`AIC = 2k - 2 ln L_max` and `chi2 = -2 ln L_max`, so

```
half-Delta-AIC = (1/2) [ 2 Delta_k + Delta_chi2 ]
```

At `Delta_k = 0` this is half the chi-squared difference, and the published
chi-squared values reproduce the published `half-Delta-AIC` in both rows:

| Data | Model | `chi2` | published `half-dAIC` | recovered at `Delta_k = 0` |
|---|---|---|---|---|
| DES-SN5YRcut | Flat-LCDM | 1616 | 0.0 | - |
| DES-SN5YRcut | Timescape | 1612 | **-1.7** | -2.0 |
| + BAO-`theta*`perp | Flat-LCDM | 1624 | 0.0 | - |
| + BAO-`theta*`perp | Timescape | 1637 | **+6.3** | +6.5 |

`chi2` is tabulated to the nearest integer, so the recovered value carries
`+/- 0.5`. A parameter-count mismatch of one would move it by `1.0`, twice
that, so the check discriminates. `[INFERENCE]`; premises: `[DES]`'s own AIC
and `chi2` definitions, and its tabulated values.

**`Delta_AIC = 12.6` against timescape on supernovae + BAO**, with no
parameter-count penalty on either side. Conventionally "very strong" on the
AIC scale. `[SOURCED]` `[DES]` Table 7.

The sign convention is stated verbatim in the Table 7 caption: "A more
negative half-Delta-AIC and Delta ln S value indicates a stronger preference
over Flat-LCDM." So the `+6.3` is a preference for flat LCDM. This closes Run
01's open worry about an unconfirmed sign convention in this table.

**The result is the sign flip, not either row.** `half-dAIC` moves by `8.0`
on adding one BAO measurement to the same supernova sample. Timescape is
weakly preferred on supernovae alone and strongly disfavoured once the BAO
angular scale is added.

### Two caveats that belong with it

`[SOURCED]` `[DES]` Sec. 7.8: the CMB summary statistic is **excluded** from
the timescape comparison, and only the SDSS `BAO-theta*perp` angular
measurements are used, "because the two models assume different spatial
curvature conventions". So the joint fit is supernovae plus one angular BAO
observable, not supernovae plus the full external dataset the other 15 models
in that paper were tested against.

`[SOURCED]` `[DES]` Sec. 2.3.2, on the pipeline's own largest risk: "The bias
correction step thus holds the biggest potential for harbouring cosmological
assumptions that could influence the cosmological results." The bias
corrections are generated in flat LCDM. `[DES]` validates the choice within
FLRW only. This is the circularity that WP-2 exists to settle and it is
unsettled; it bears on this row as much as on any other.

### A by-product that belongs to WP-4

`[SOURCED]` `[DES]` Table 6: `f_v0 = 0.791 (+0.039/-0.034)` on supernovae
alone, `0.665 (+0.008/-0.009)` with BAO added. The fitted value moves by
`0.126`, which is **3.6 sigma on its own quoted uncertainties**, between two
data combinations that share the supernova sample. Carried into WP-4 as an
input to K5.

## 4. The `H_0` comparison: not like-for-like, on timescape's own criterion

### 4.1 There are three timescape Hubble constants, not one

The relation between the volume-average ("bare") and wall-observer ("dressed")
Hubble constants on the tracker solution, written both ways in two independent
papers, `[SW11]` Eq. (17) and `[DES]` Eq. (49):

```
H_0 = (4 f_v0^2 + f_v0 + 4) H_bar_0 / [ 2 (2 + f_v0) ]
```

`[SOURCED]` `[DNW13]` parameter table, from the CMB acoustic-scale fit:
`f_v0 = 0.695 (+0.041/-0.051)`, `gamma_bar_0 = 1.348 (+0.021/-0.025)`,
`H_bar_0 = 50.1 +/- 1.7` km/s/Mpc.

| Quantity | Value | Where it comes from |
|---|---|---|
| bare `H_bar_0` | `50.1 +/- 1.7` | `[DNW13]`, fitted to Planck acoustic scales |
| dressed `H_0` | `61.7 +/- 3.0` | `[W19]` Sec. 2; reproduced here as `61.60` from `50.1` at `f_v0 = 0.695` |
| `H_bar_tau_0 = gamma_bar_0 H_bar_0` | `67.5 (+3.4/-3.5)` | `[W19]` Sec. 2; reproduced here as `67.53` |

The transcription is independently confirmed at a different `f_v0` from a
different paper: `[LNW08]` fit supernovae and report dressed `61.7 (+1.2/-1.1)`
with bare `48.2 (+2.0/-2.4)` at `f_v0 = 0.76 (+0.12/-0.09)`. The same relation
carries `61.7` to `48.17` at `f_v0 = 0.76`, sharing no number with the CMB fit.

Note `gamma_bar_0 = 1.348` is **not** the dressed/bare ratio, which is
`1.2295`. The two differ by `0.118`. "The timescape Hubble constant" names
three numbers spanning 35%, and the discrimination table compares exactly one
of them to the distance ladder without saying why that one.

`[SOURCED]` `[W19]` Sec. 2 states that `H_bar_tau_0 = 67.5` is the quantity
matching the FLRW Hubble constant inferred from the same CMB data. That is
already a warning: if the CMB comparator is `67.5` and not `61.7`, the
question of which quantity a *distance ladder* determines cannot be assumed.

### 4.2 Timescape's own stated comparability criterion excludes SH0ES

`[SOURCED]` `[SW11]` Sec. 2, verbatim: "Ideally the global average Hubble
constant should be determined only on scales significantly larger than the
scale of statistical homogeneity, z > 0.033, by methods which do not depend on
calibrations below that scale."

`[SOURCED]` `[R22]`: `H_0 = 73.04 +/- 1.04` km/s/Mpc, Cepheid-calibrated, with
the calibrating SNe Ia at `z < 0.01`.

`z < 0.01` is below `z = 0.033`. **The SH0ES determination is of the kind
`[SW11]` explicitly excludes**, and it is excluded for a reason internal to the
model rather than invented here. So the comparison as the discrimination table
states it is **not like-for-like**.

`[SOURCED]` `[SW11]` Sec. 2 names the method it regards as satisfying the
criterion: strong-lens time delays, citing a then-current `H_0 = 62 (+6/-4)`.
That comparator has since moved. `[LEAD]` Modern time-delay cosmography
reports `73.3 (+1.7/-1.8)` (H0LiCOW) and `67.4 (+4.1/-3.2)` (TDCOSMO+SLACS
hierarchical). I have the locators arXiv:1907.04869 and arXiv:2007.02941 but
did not fetch either, so these are leads, not sourced. **If they hold, the one
method timescape named as like-for-like no longer gives a value in its
admissible band, and WP-1 should be reopened on exactly that point.** This is
the single most useful follow-up from this package.

### 4.3 But the comparison is not a rescue either, and here is the number

The authors do not treat the `H_0` gap as harmless. `[SOURCED]` `[SW11]`
Sec. 2, verbatim: "values of 57 < H_0 < 68 km sec-1 Mpc-1 would be admissible
in the TS scenario, but values as large as the recent H_0 = 74.2 +/- 3.6 km
sec-1 Mpc-1 determined by the SH0ES survey (Riess et al. 2009) would represent
a severe challenge to the model."

Against their own ceiling of `68`, the current SH0ES value is **4.85 sigma
high** on the SH0ES error alone. Against the dressed `61.60`, it is an **18.6%
excess**.

Now the escape, stated quantitatively. `[SOURCED]` `[SW11]` Sec. 2, verbatim:
"The Hubble 'constant' inferred in this manner should peak at the dominant void
scale 30/h Mpc, i.e. at z ~ 0.01, with a maximum value up to 17% greater than
the global average and then steadily decrease to near the global average value
when the scale of statistical homogeneity is reached."

The excess that has to be explained is 18.6%. The enhancement the model
predicts, at the scale where the ladder is calibrated, is up to 17%. **Those
are the same size.** Applying the full predicted 17% to the dressed value
gives `72.07` against the measured `73.04 +/- 1.04`: a residual gap of **0.93
sigma**.

That is the finding. It is neither a kill nor a rescue. It means the `H_0` row
cannot decide anything by itself, because the discrepancy and the model's own
predicted local variance are degenerate at the precision available. The row
**collapses into the Hubble-flow-variance question**, which is WP-8, and which
`docs/RESEARCH-PLAN.md` records as never having been done.

`[INFERENCE]`; premises: that the 17% peak enhancement at `z ~ 0.01` is the
right figure to apply to a Cepheid-calibrated ladder. **It is probably not
exactly right**, and the gap is the reason to say so: a ladder is not a
measurement of `H(z ~ 0.01)`, it is a calibration of SN absolute magnitude from
hosts at `z < 0.01` applied to SNe out to `z ~ 0.15`. Constructing the
predicted quantity and the measured quantity as the same statistic is WP-8's
actual work and is not done here. What is established here is only that the two
numbers are the same order, which is what makes the `H_0` row
non-discriminating.

### 4.4 Why `60.98` is not used above

Run 01's table gives the dressed range as `60.98`-`61.7`. I sourced `61.7`
from three papers and did not locate `60.98` in any source I fetched.
`[UNKNOWN]` where it comes from. Nothing here depends on it; the conclusions
use `61.7` and `61.60`.

## 5. Does K1 fire? No.

K1: "WP-1 confirms both the joint-fit tension and the `H_0` discrepancy as
like-for-like and significant, **and** WP-2 finds the supernova fit is not
circular."

Both limbs fail, independently.

1. **First limb.** The joint-fit tension is confirmed as like-for-like and
   significant. The `H_0` discrepancy is **not** confirmed as like-for-like, on
   the model's own stated criterion (§4.2), and is non-discriminating at
   current precision (§4.3). K1 requires both.
2. **Second limb.** WP-2 is out of scope for the standing loop and has not
   run. Run 01 found the circularity real and acknowledged on both sides, with
   no published analysis resolving it; `[DES]` itself names the bias-correction
   step as the biggest risk. So the second limb is not merely unestablished,
   the available evidence runs against it.

**K1 does not fire and the programme does not stop here.** Had the `H_0` row
held, the first limb would still have been insufficient.

## 6. What this changes in the plan

- The discrimination table's `H_0` row should read **"No - not the same
  quantity; refers to the Hubble-flow-variance row"**, not "arguably yes,
  against timescape". That is a correction to a Run 01 output, so it belongs to
  WP-10, not to an edit here. Recorded in the day log for WP-10 to pick up.
- **WP-8 is promoted in value.** It was Phase 2 and dependent on nothing. It is
  now the package the `H_0` question routes through, and the only one that can
  settle it. It is also out of scope for this loop.
- **WP-1 has one live follow-up**, §4.2: fetch arXiv:1907.04869 and
  arXiv:2007.02941 and establish whether the comparator timescape itself named
  as like-for-like still sits inside its admissible band. If it does not, the
  `H_0` objection returns in a form the 17% escape does not answer, because
  time-delay cosmography is not calibrated below `z = 0.033`.
- The joint-fit row stands, at matched parameter count, with `Delta_AIC = 12.6`,
  and with the two caveats in §3 attached to it.

## 7. One discrepancy in the literature, recorded

`[DNW13]` p. 9 writes the dressed/bare relation with `4 f_v0` as the middle
term where `[SW11]` Eq. (17) and `[DES]` Eq. (49) both have `f_v0`. The forms
are not equivalent. Only the `f_v0` form reproduces `[DNW13]`'s own published
dressed `61.7` from its own bare `50.1`; the as-printed form gives `80.98`.
Either a typo in that line or an artefact of PDF text extraction, which I
cannot distinguish without the published typeset version. The `f_v0` form is
the one used everywhere downstream and the one used here. Not a result; a note
so that nobody rediscovers it as a contradiction.
