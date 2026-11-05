# VAST void catalogs for SDSS DR7

Obtained 2026-11-05 for **WP-4**: is the fitted void fraction `f_v0`
measuring what it claims?

## 1. The archive

Zenodo record **11043278**, files fetched through the Zenodo REST API. See
`fetch.sh`, which is runnable and idempotent.

## 2. Release

**Version 1.3.1**, published 2024-04-22. Licence CC-BY-4.0.

v1.3.1 is not cosmetic: it corrected the `NSAID` column in the `galzones`
files. Earlier versions (1.0.0, record 5834787, superseded; 1.1, record
6081273) report slightly different void counts — 1159 VoidFinder voids
against 1163 here. Pin to 1.3.1 and say so in any result.

## 3. Size

20.4 MB across 17 files. Not committed; see `MANIFEST.sha256`.

## 4. Citation

Douglass, Veyrat & BenZvi, *Updated Void Catalogs of the SDSS DR7 Main
Sample*, ApJS **265**, 7 (2023).

- Paper: `arXiv:2202.01226`, `doi:10.3847/1538-4365/acabcf`
- Dataset: `doi:10.5281/zenodo.11043278`
- Also mirrored at VizieR as `J/ApJS/265/7`.

Both DOIs get cited: the paper for the method, the dataset for the version.

## 5. What it can settle

The three catalogues run **three different void finders over the same
survey volume**, which is what makes this dataset the right one for WP-4
rather than any single catalogue. Counts in the DR7 main volume to
`z = 0.114`, under Planck 2018:

| Finder | Voids |
|---|---|
| VoidFinder | 1163 |
| V2, VIDE pruning | 531 |
| V2, REVOLVER pruning | 518 |

Reproduced on download: the Planck2018 `maximal` file has 1163 rows after
its header and the V2-VIDE `zobovoids` file has 531. The counts match the
paper, which is the first integrity check on the files.

A volume fraction computed under each finder in turn gives a **spread**,
and WP-4's question is whether the fitted `f_v0` lies inside or outside it.
That is K5: if the measured void fraction excludes every fitted `f_v0`,
`f_v0` is a fitting parameter rather than an observable and `T13`'s
evidential weight collapses.

Each catalogue is also supplied under **two cosmologies**, Planck 2018 and
WMAP5. The difference between those two is a lower bound on the sensitivity
of any answer to the assumed distance scale, and it is free: both are in
the archive.

## 6. What it cannot settle

- **It cannot define a void.** The literature's void volume fraction runs
  from roughly 10% to 83% depending on the finder, the density threshold
  and the volume cut. This dataset bounds the *method* spread over one
  survey; it does not privilege one number.
- **It cannot be compared to `f_v0` without a matching definition.**
  Timescape's `f_v0` is the present-epoch volume fraction of the void
  phase in a two-phase split of a Buchert average. A void finder's output
  is a set of regions below a density threshold in a galaxy survey. These
  are not the same quantity, and WP-4's first job is to say precisely how
  far apart they are. **An answer that compares the two numbers without
  that step is not a result.**
- **It is one survey, to `z = 0.114`.** No redshift evolution of the void
  fraction is available from it.
- **It says nothing about void curvature**, which is WP-5's question and a
  different measurement.

## 7. What model assumptions it was reduced under

**This is the field that matters here, and the answer is: a lot.**

The catalogues are supplied in **comoving Cartesian coordinates**. Getting
there from observed angles and redshifts requires a distance-redshift
relation, and the providers used one — hence the `Planck2018` and `WMAP5`
variants. Every `x`, `y`, `z`, every `radius`, and every derived volume is
therefore **conditional on a FLRW distance scale that timescape does not
share**.

So the naive comparison is circular in exactly the way the sibling
repository's data conventions warn about: a void fraction computed from
ΛCDM comoving volumes, set against an `f_v0` fitted inside a model with a
different distance-redshift relation and a different volume measure.

What follows for WP-4:

1. The **angles and redshifts** are the model-independent content. The
   comoving positions are derived.
2. Any volume fraction computed from the supplied coordinates is a
   **ΛCDM-conditioned** quantity and must be labelled so, every time.
3. The Planck2018-versus-WMAP5 difference gives the sensitivity to the
   assumed parameters *within* FLRW. It does **not** bound the error from
   assuming FLRW at all, which is the larger effect and the one at issue.
4. Doing this properly means recomputing volumes under the timescape
   distance-redshift relation from the angles and redshifts. Whether that
   is in WP-4's budget is a real question; if it is not, the honest output
   is the ΛCDM-conditioned number with this limitation stated as the
   result's main caveat, **not** a comparison presented as clean.

Point 4 is the whole reason this file has a field 7. It was the question
Run 01 could not settle for the supernova data, and it recurs here in a
different form.

## 8. File layout

Raw files land in `data/raw/001-sdss-dr7-voids/`, which `.gitignore`
excludes.

- `VoidFinder-*_comoving_maximal.txt` — one row per void: the maximal
  sphere, with `radius` and `Reff`.
- `VoidFinder-*_comoving_holes.txt` — all spheres making up each void.
  **A void's volume is the union of its spheres, not the sum.** Summing
  overlapping sphere volumes overcounts, and that mistake would inflate the
  volume fraction in the direction that favours a large `f_v0`.
- `V2_*_zobovoids.dat` — ZOBOV voids with `radius`, `area`, and an `edge`
  flag.
- `V2_*_zonevoids.dat`, `V2_*_galzones.dat` — zone and galaxy membership.
- `NSA_main_mask.pickle` — the survey mask. **Required**: a volume fraction
  needs the surveyed volume as its denominator, and the `edge` flags mark
  voids touching the boundary. A Python pickle is executable content; load
  it only with the repository's own venv and treat it as data.

## 9. Appended notes, after the analysis

This file was written **before** any analysis touched the dataset, which is
the point of it. Notes that only became available afterwards are appended
here, dated, rather than written back into the fields above - because a
provenance file edited to agree with the result it produced is no longer
provenance.

### 2026-11-05, second session: field 7's priority is wrong for this survey

**Field 7's reasoning is right and its implied priority is wrong.** It
presents the ΛCDM conditioning as the headline problem for WP-4. The
conditioning is real, and `findings/WP-4-void-fraction.md` §5 puts it at
**~2.0 percentage points** against a **17.5-point** survey-edge systematic
(`verify/wp4_fv0_comparison.py`). So the thing field 7 names as the main
caveat is about eight times smaller than the one it does not mention.

The reason is specific to this dataset and does not generalise. `f_v` is a
**ratio of volumes**, so a uniform rescaling of all distances cancels exactly;
what survives is only the change in the *shape* of `D_C(z)` over
`0 < z < 0.114`, and this survey is shallow enough that the shape barely
moves. On a deep survey the term would not be small, and field 7's priority
would be right.

Two further notes from the same session, both bearing on field 7's point 4,
which asks what the ΛCDM-conditioned number may be presented as:

- The measured fraction is a **lower bound** on timescape's `f_v0`, not an
  estimate of it, and `findings/WP-4-void-fraction.md` §10 now supports that
  by three independent routes rather than the one `[INFERENCE]` it originally
  rested on. A lower bound is a weaker object than field 7 anticipated and a
  more robust one: it survives the conditioning, because the conditioning
  moves the number by 2 points and the bound is one-sided.
- There is **no numerical density threshold** in timescape to condition
  against. arXiv:0712.3984 §5 Eq. (7) explicitly denies that the critical
  density has the form `3 H_av^2 / (8 pi G)` in an inhomogeneous cosmology,
  and defines the wall/void boundary kinematically instead, as the surface of
  zero average expansion. Field 7's framing assumes the comparison is between
  two numbers reduced under two distance relations. Part of it is not: one
  side of the comparison has no numerical definition at all.

**Nothing above this line was changed.** `cuts.md` is also unmodified; no
radius cut was applied, so its cut 7 never came into play.
