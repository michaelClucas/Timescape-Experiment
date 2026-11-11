# Dataset 002: NASA-Sloan Atlas v1_0_1 (galaxy positions only)

**Written 2026-11-11, before any analysis touched this dataset.** Notes
learned afterwards are appended at the end, dated, never written back into
the fields above them.

## 1. What it is

The NASA-Sloan Atlas (NSA), version 1_0_1: a catalogue of SDSS galaxies
with redshifts and photometry. This repository uses four columns only:
`NSAID`, `RA`, `DEC`, `Z`. It is the catalogue that the VAST void catalogues
in dataset 001 were built from. The `NSAID` column of
`V2_*_galzones.dat` indexes into it, as corrected in VAST v1.3.1
(`data/001-sdss-dr7-voids/SOURCE.md`).

- File: `nsa_v1_0_1.fits`, 2,460,470,400 bytes.
- URL: `https://data.sdss.org/sas/dr17/sdss/atlas/v1/nsa_v1_0_1.fits`
- SHA-1, as published by SDSS in `sdss_atlas_v1.sha1sum` in the same
  directory: `49c28a4597be3c630440dc997940a8cd37096760`. `fetch.sh` checks
  it.
- Reference: Blanton et al. 2011, AJ 142, 31. `[LEAD]` for anything beyond
  the four columns used.
- Raw file lands in `data/raw/002-nsa-v1_0_1/`, which is gitignored.

## 2. Why it is needed

WP-6 and WP-5 both reduce to one number, `M_v`: the share of all matter that
sits in the void phase (`findings/WP-6-two-phase-sensitivity.md` §4-§5,
`findings/WP-5-curvature-requirement.md` §4). The repository has it only as
a `[LEAD]`, Pan et al.'s abstract figure of about 7% of bright galaxies. This
dataset lets us measure the **galaxy** share for the same VoidFinder voids
whose volume fraction WP-4 measured. Dataset 001 holds void geometry and NSA
IDs, but no galaxy positions.

## 3. What it can and cannot settle

- **It can give `M_v,gal`**: the fraction of VAST's galaxy sample lying
  inside VoidFinder void spheres, within the same masked survey volume.
- **It cannot give the matter share.** Galaxies are biased tracers, and the
  galaxy-to-matter step is an `[INFERENCE]` with a named premise. See
  `cuts.md` cut 7.
- **It inherits dataset 001's LCDM conditioning**, because positions are
  computed in the catalogues' own cosmologies, and Q-2's default leaves that
  in place.
- **It does not decide Q-5**, whether the void phase is VoidFinder's voids or
  only their empty part. Under Q-5's option 2 the result is moot by
  definition.
