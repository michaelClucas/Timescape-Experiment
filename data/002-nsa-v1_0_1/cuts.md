# Dataset 002 cuts, fixed before analysis

**Committed 2026-11-11, before the galaxy positions were read.** Every
choice the measurement makes is here. A choice made later is appended with
its date and the reason, and the result is reported both ways.

**What was already known when these were written.** These facts came from
dataset 001 and from conventions, not from galaxy positions:
- The coordinate convention, checked on V2 void centres: in Planck 2018,
  `x, y, z = r cos(dec) cos(ra), r cos(dec) sin(ra), r sin(dec)` with
  `r = D_C(z)` for flat LCDM, `H0 = 100`, `Om0 = 0.315`, matches to 4e-11
  h^-1 Mpc. WMAP5, `Om0 = 0.258`, matches to 0.053.
- The mask's radial limit, 332.38565, equals `D_C(0.114)` in Planck 2018.
- `galzones` lists 194,125 unique NSAIDs, all with `out = 0`.

## Cuts

1. **Sample.** The NSAIDs in `V2_VIDE-nsa_v1_0_1_<cosmology>_galzones.dat`:
   VAST's galaxy input for that cosmology. Galaxies are matched to the NSA
   by `NSAID`. Any NSAID with no NSA match is counted and reported, not
   dropped silently.
2. **Redshift.** NSA column `Z`, used as given.
3. **Positions.** As in the convention above, per cosmology. Planck 2018 is
   the headline cosmology and WMAP5 the variant, as in WP-4.
4. **Survey volume.**
   - `r <= 332.38565` and `z < 0.114`;
   - inside `NSA_main_mask.pickle` under VAST's own index convention:
     RA index `int(res * ra)`, Dec index `int(res * dec) + 90 * res`,
     truncating toward zero, per Q-4 on PR #14;
   - also reported under WP-4's pre-fix convention, `int((dec + 90) * res)`,
     for continuity.
5. **In a void.** Inside at least one sphere of
   `VoidFinder-nsa_v1_0_1_<cosmology>_comoving_holes.txt`, i.e.
   `|x - c| <= R` for some hole. All holes are used, edge voids included,
   matching WP-4's edge-included 0.6228.
6. **Outputs.**
   - `N_tot` and `N_void` for each cosmology and each mask convention.
   - `M_v,gal = N_void / N_tot`.
   - `delta_g = M_v,gal / f_v - 1`, with `f_v` = WP-4's edge-included
     VoidFinder fraction for the same cosmology: 0.6228 for Planck 2018 and
     0.6263 for WMAP5 on `main` (`findings/WP-4-void-fraction.md` §6). Under
     the mask fix on PR #14 they are 0.6157 and 0.6192.
7. **Reading `M_v,gal` against the model.** It is compared with
   `verify/void_matter_sensitivity.py`'s thresholds:
   - 0.0265 (`q_min` moves by the published `q_0` error);
   - 0.0852 (dressed `q` at `f_v0 = 0.695` reaches zero);
   - 0.270 (K4).

   The galaxy share is **not** the matter share. `[INFERENCE]`, premise
   named: galaxy formation is suppressed in low-density regions, so the void
   share of a luminosity-limited sample is more likely to understate the
   void share of matter than to overstate it. The measurement is therefore
   reported as an estimate of `M_v` that is **probably low**, never as
   `M_v`.
8. **Sanity bound, stated now.** Pan et al.'s abstract (arXiv:1103.4156)
   gives about 7% of `M_r < -20.09` galaxies in voids, from a different
   VoidFinder run on DR7. A result outside 2%-20% is investigated for a
   pipeline error before it is reported. A result inside that range is not
   thereby confirmed.

---

## Appended 2026-11-11, after the first run: cut 5a

**Cut 5 was wrong as registered.** VoidFinder grows each hole until four
wall galaxies lie exactly on its surface. `|x - c| <= R` therefore counts
those **defining wall galaxies**: 35,530 galaxies in Planck 2018 sit within
1e-3 h^-1 Mpc of a hole surface. On the first run, cut 5 gave
`M_v,gal = 0.1718`.

**Cut 5a**: inside means `|x - c| <= R - 1e-3`. The interior share is flat
from 1e-3 to 1e-1 h^-1 Mpc (0.0609, 0.0608, 0.0603), so the boundary is
resolved and the choice of 1e-3 does not drive the result. Both cuts are
printed by `verify/wp6_void_galaxy_share.py`. The headline is cut 5a,
because VoidFinder's construction defines hole-surface galaxies as wall
galaxies.

A diagnostic run that was not part of the registered outputs:
- the sample is volume-limited, `M_r < -20.0` and `z < 0.114`, as the
  catalogue paper states;
- with Pan et al.'s `M_r < -20.09`, the cut-5a share is 0.0596.

These figures come from an ad-hoc diagnostic, not from a committed script.
They are recorded so that the reason for cut 5a is checkable, and they are
not quoted as results.
