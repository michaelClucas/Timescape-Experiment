# Cuts

**Written 2026-11-05, before any volume fraction was computed from these
files.** That ordering is the point of this file: a selection chosen after
seeing the answer is not a selection, it is a result being steered. No
analysis of this dataset has been run in this repository yet.

## Decided in advance

1. **Version 1.3.1 only.** Earlier Zenodo versions give 1159 VoidFinder
   voids rather than 1163. Mixing versions is not permitted.

2. **All three finders, every time.** VoidFinder, V2-VIDE and V2-REVOLVER.
   A result quoted from one finder without the other two is not reportable,
   because the method spread is the measurement WP-4 needs. If the three
   disagree, that disagreement is the finding.

3. **Both cosmologies, every time.** Planck2018 and WMAP5. Report both
   numbers, never an average of them.

4. **Edge voids are reported both ways.** Compute the volume fraction
   including and excluding voids with `edge` set. Excluding them biases the
   fraction down, since a void clipped by the survey boundary still fills
   volume inside it; including them counts volume outside the mask. Neither
   is right, so both are reported and the difference is the systematic.

5. **The denominator is the masked survey volume**, from
   `NSA_main_mask.pickle` with the `z <= 0.114` limit, not a bounding box
   and not a naive solid-angle shell.

6. **VoidFinder volumes are unions of spheres**, computed from the `holes`
   file. Summing sphere volumes from that file is an error that inflates
   the fraction. If the union is computed by Monte Carlo, the sample count
   and seed are recorded with the result, and the seed is fixed before the
   run.

7. **No radius cut is applied**, and if one is later required by the
   comparison to `f_v0`, it is declared as a change to this file with the
   reason, before the recomputation. Pan et al. applied a 10 h^-1 Mpc
   minimum and got 62%; that cut is theirs and is not inherited silently.

8. **Every reported fraction is labelled ΛCDM-conditioned**, per
   `SOURCE.md` field 7, including in the abstract of any write-up.

## Not decided in advance, and deliberately left open

**Whether the volume fraction is recomputed under the timescape
distance-redshift relation** from the catalogue's angles and redshifts
rather than its supplied comoving coordinates. That is the methodologically
correct thing to do and it may exceed WP-4's budget. The decision belongs
to the work package, with the choice and its cost recorded there. What is
decided here is that the ΛCDM-conditioned number may not be presented as a
clean comparison if the recomputation is skipped.

## Changes

A change to this file is a commit of its own, dated, with the reason, made
**before** the recomputation it licenses. An undated change, or one
committed alongside the result it produced, invalidates the result.

| Date | Change | Reason |
|---|---|---|
| 2026-11-05 | Created | Dataset obtained for WP-4 |
