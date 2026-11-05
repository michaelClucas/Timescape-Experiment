#!/usr/bin/env python3
"""WP-4a: the measured void volume fraction in SDSS DR7, from the raw catalogues.

**CORRECTION NOTICE, appended 2026-11-05 by the third session of that date.
Read this before quoting any number from this script.**

`in_mask` below indexes the declination axis as `((dec + 90) * res)` truncated.
**That is not the convention the mask file was written with.** [VAST], the
software that produced `NSA_main_mask.pickle`, builds and reads the array as
`int(res * dec) - res * dec_offset` with `dec_offset = -90`
(`multizmask.py` lines 15, 166, 192; `voidfinder_functions.py` line 249;
unchanged between commit `133cfcf` of 2022-02-10 and `24e66e1`). Truncation
toward zero is applied *after* scaling and *before* the offset, so the two
expressions differ by one pixel wherever `dec < 0`, which is 2.3% of this
survey's footprint.

Correcting it moves the VoidFinder edge-included fraction from 62.280% to
**61.570%** (Planck2018) and from 62.628% to **61.923%** (WMAP5), i.e. by
-0.710 and -0.705 points, and halves the residual against [DVB23] Table 6.
`verify/wp4_vast_mask_convention.py` (10/10) sources the convention, computes
the corrected numbers and checks what they do and do not change.

**Nothing in this file has been altered.** Its numbers and its 14 checks stand
as committed, so that every finding quoting them stays resolvable, and the
correction is appended in `findings/WP-4-void-fraction.md` §12 rather than
applied in place. Whether this script should instead be corrected is
`OPEN-QUESTIONS.md` Q-4; the reversible default taken was to leave it and point
here.

    .venv/Scripts/python verify/wp4_void_fraction.py

Exits 0 if every check passes, 1 otherwise. Takes a few minutes: it rasterises
~40,000 spheres onto a 1 h^-1 Mpc grid, which is the method the catalogue paper
used and is reproduced here rather than trusted.

This script computes numbers. It does **not** compare them to the fitted
`f_v0`: the two are not the same quantity, and the gap between them is analysed
in `findings/WP-4-void-fraction.md`. `data/001-sdss-dr7-voids/SOURCE.md`
section 6 is explicit that a comparison without that step is not a result.

**What this script found that was not expected.** The VoidFinder volume
fraction reproduces the published value. The V2/VIDE and V2/REVOLVER volume
fractions do **not**, and the discrepancy runs in opposite directions for the
two pruning methods, so it is not one systematic. Those two published numbers
are not reproducible from the published catalogue files, for the reason given
in `v2_limitation()` below. The checks pin that disagreement as a fact rather
than asserting an agreement that does not hold.

Binding constraints from `data/001-sdss-dr7-voids/cuts.md`, written before any
number was computed:

  cut 1  version 1.3.1 only                      - fixed by the download
  cut 2  all three finders, every time           - all three below
  cut 3  both cosmologies, never averaged        - both below, reported apart
  cut 4  edge voids reported both ways           - both below
  cut 5  denominator is the masked survey volume - from NSA_main_mask.pickle
  cut 6  VoidFinder volumes are unions of spheres - rasterised union, not a sum
  cut 7  no radius cut applied                   - none applied
  cut 8  every fraction labelled LCDM-conditioned - see the printed banner

Sources, both fetched and read in full text:

  [DVB23] Douglass, Veyrat & BenZvi, "Updated Void Catalogs of the SDSS DR7
          Main Sample", arXiv:2202.01226, ApJS 265, 7 (2023).
          Sec. 2.1 (cosmologies), Sec. 3.1 (VoidFinder), Sec. 3.2 (V2),
          Sec. 4.1 (edge definitions), Sec. 4.2 and Table 6 (volume fractions).
  Dataset: doi:10.5281/zenodo.11043278, version 1.3.1.
"""

import os
import pickle
import sys

import numpy as np
from scipy.integrate import quad

RAW = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "data", "raw", "001-sdss-dr7-voids"))

GRID = 1.0        # h^-1 Mpc. [DVB23] Sec. 4.2: "test particles placed on a 1 h-1 Mpc grid".
Z_MAX = 0.114     # [DVB23] Table 6 note: volume-limited catalogue, z < 0.114.
C_OVER_100 = 2997.92458  # c / (100 km/s/Mpc), in h^-1 Mpc.

# [DVB23] Sec. 2.1: two flat LCDM cosmologies, WMAP5 (Omega_M = 0.258) and
# Planck 2018 (Omega_M = 0.315). Comoving distances in h^-1 Mpc do not depend
# on h, so Omega_M is the whole input.
OMEGA_M = {"Planck2018": 0.315, "WMAP5": 0.258}

# [DVB23] Table 6, the validation targets. Its note says "Edge voids are
# excluded from all properties except Nvoid", but Sec. 4.2 describes the
# VoidFinder volume fraction as a count of grid particles falling "within one
# of the VoidFinder void spheres", with no edge filter. Which of those governs
# the volume column is resolved below by seeing which variant reproduces it.
PUBLISHED = {
    ("Planck2018", "VoidFinder"): (1163, 60.8),
    ("Planck2018", "V2_VIDE"): (531, 68.1),
    ("Planck2018", "V2_REVOLVER"): (518, 90.8),
    ("WMAP5", "VoidFinder"): (1184, 61.1),
    ("WMAP5", "V2_VIDE"): (534, 63.0),
    ("WMAP5", "V2_REVOLVER"): (518, 86.5),
}

CHECKS = []
RESULTS = {}
NOTES = []


def check(name, ok, detail=""):
    CHECKS.append((bool(ok), name, detail))


def close(name, got, want, tol, detail=""):
    CHECKS.append((abs(got - want) <= tol, name,
                   "got %.4g, want %.4g +/- %.3g. %s" % (got, want, tol, detail)))


def comoving_distance(z, omega_m):
    """Flat LCDM comoving distance in h^-1 Mpc. Matter plus Lambda, no radiation."""
    return C_OVER_100 * quad(
        lambda zz: 1.0 / np.sqrt(omega_m * (1 + zz) ** 3 + (1 - omega_m)), 0.0, z)[0]


# ---------------------------------------------------------------------------
# The survey mask
# ---------------------------------------------------------------------------

def load_mask():
    """Return (mask2d, resolution, r_min, r_max) from the VAST mask pickle.

    The pickle is a 3-tuple and its layout is not documented in SOURCE.md, so
    the indexing convention is established by test below rather than assumed.
    SOURCE.md section 8: a pickle is executable content, loaded with the
    repository venv and treated as data.
    """
    with open(os.path.join(RAW, "NSA_main_mask.pickle"), "rb") as fh:
        mask, res, rlim = pickle.load(fh)
    return np.asarray(mask), int(res), float(rlim[0]), float(rlim[1])


def in_mask(mask, res, ra, dec):
    i = np.clip((ra * res).astype(np.int64), 0, mask.shape[0] - 1)
    j = np.clip(((dec + 90.0) * res).astype(np.int64), 0, mask.shape[1] - 1)
    return mask[i, j]


def read_table(path):
    with open(path) as fh:
        cols = fh.readline().lstrip("#").split()
    data = np.genfromtxt(path, skip_header=1)
    return {c: data[:, i] for i, c in enumerate(cols)}


def grid_axis(lo, hi):
    return lo + GRID * np.arange(int(np.floor((hi - lo) / GRID)) + 1)


def grid_box(mask, res, r_max):
    """A box tight enough to contain the survey cone out to r_max."""
    ii, jj = np.nonzero(mask)
    ra_c = (ii + 0.5) / res
    dec_c = (jj + 0.5) / res - 90.0
    cd = np.cos(np.radians(dec_c))
    u = np.stack([cd * np.cos(np.radians(ra_c)),
                  cd * np.sin(np.radians(ra_c)),
                  np.sin(np.radians(dec_c))])
    pad = r_max * np.radians(1.5 / res) + 2 * GRID
    lo = np.minimum(u.min(axis=1) * r_max - pad, 0.0)
    hi = np.maximum(u.max(axis=1) * r_max + pad, 0.0)
    return [grid_axis(lo[k], hi[k]) for k in range(3)]


def survey_cells(mask, res, axes, r_min, r_max):
    """Boolean, per x-slab, of grid cells inside the masked survey volume.

    Returned as a list of (slab index, flat boolean over the y-z plane) so the
    caller can reuse it across edge variants without recomputing, and so peak
    memory stays one slab.
    """
    xs, ys, zs = axes
    YY, ZZ = np.meshgrid(ys, zs, indexing="ij")
    yz2 = YY * YY + ZZ * ZZ
    out = []
    total = 0
    for i, x in enumerate(xs):
        r = np.sqrt(x * x + yz2)
        shell = (r >= r_min) & (r <= r_max)
        if not shell.any():
            out.append(None)
            continue
        ra = np.degrees(np.arctan2(YY[shell], x)) % 360.0
        dec = np.degrees(np.arcsin(np.clip(ZZ[shell] / r[shell], -1, 1)))
        inm = in_mask(mask, res, ra, dec)
        sel = np.zeros(shell.shape, dtype=bool)
        sel[shell] = inm
        total += int(inm.sum())
        out.append(sel if inm.any() else None)
    return out, total


def rasterise_union(axes, hx, hy, hz, hr):
    """Boolean grid of the union of the given spheres.

    cut 6: a void's volume is the union of its spheres, not the sum. Summing
    overlapping sphere volumes overcounts and inflates the fraction in the
    direction that would favour a large f_v0, which is why this is rasterised.
    """
    xs, ys, zs = axes
    shape = (len(xs), len(ys), len(zs))
    grid = np.zeros(shape, dtype=bool)
    for cx, cy, cz, cr in zip(hx, hy, hz, hr):
        i0 = max(0, int(np.ceil((cx - cr - xs[0]) / GRID)))
        i1 = min(shape[0] - 1, int(np.floor((cx + cr - xs[0]) / GRID)))
        j0 = max(0, int(np.ceil((cy - cr - ys[0]) / GRID)))
        j1 = min(shape[1] - 1, int(np.floor((cy + cr - ys[0]) / GRID)))
        k0 = max(0, int(np.ceil((cz - cr - zs[0]) / GRID)))
        k1 = min(shape[2] - 1, int(np.floor((cz + cr - zs[0]) / GRID)))
        if i0 > i1 or j0 > j1 or k0 > k1:
            continue
        dx = xs[i0:i1 + 1] - cx
        dy = ys[j0:j1 + 1] - cy
        dz = zs[k0:k1 + 1] - cz
        d2 = ((dx * dx)[:, None, None] + (dy * dy)[None, :, None]
              + (dz * dz)[None, None, :])
        grid[i0:i1 + 1, j0:j1 + 1, k0:k1 + 1] |= d2 <= cr * cr
    return grid


def count_in(void_grid, surv):
    n = 0
    for i, sel in enumerate(surv):
        if sel is not None:
            n += int(void_grid[i][sel].sum())
    return n


def v2_limitation():
    return (
        "Why the V2 fractions are not reproducible from the published files.\n"
        "  [DVB23] Sec. 3.2 states that V2 'assigns a volume of 0 to any cell\n"
        "  that extends outside the edge of a survey'. The `radius` column is\n"
        "  the effective radius from that volume ([DVB23] Eqn. 1), so\n"
        "  sum (4/3) pi r_eff^3 is the tessellation volume with boundary cells\n"
        "  zeroed, not the spatial extent of the void regions. Recomputing the\n"
        "  spatial extent needs the Voronoi tessellation, which needs the\n"
        "  galaxy positions. The `galzones` files carry only NSAID and zone\n"
        "  membership, not coordinates, and the NSA galaxy catalogue is not\n"
        "  part of this dataset. So the tessellation cannot be rebuilt here.\n"
        "  That explanation predicts a shortfall in one direction. The measured\n"
        "  discrepancy is NOT one-directional (VIDE high, REVOLVER low), so it\n"
        "  is not fully explained and is recorded as unexplained.")


def main():
    print("=" * 78)
    print("WP-4a: measured void volume fraction, SDSS DR7, VAST v1.3.1")
    print("=" * 78)
    print("EVERY FRACTION BELOW IS LCDM-CONDITIONED. The catalogues are supplied")
    print("in comoving Cartesian coordinates derived under a FLRW")
    print("distance-redshift relation that timescape does not share. See")
    print("data/001-sdss-dr7-voids/SOURCE.md field 7. Per cut 8 this label")
    print("travels with the number everywhere it is quoted.")
    print()

    mask, res, r_min, r_mask = load_mask()
    print("mask %s at resolution %d; pickle radial range [%.3f, %.3f] h^-1 Mpc"
          % (mask.shape, res, r_min, r_mask))
    print("mask pixels set: %d of %d (%.4f of the sphere)"
          % (mask.sum(), mask.size, mask.sum() / mask.size))
    print()

    # Which cosmology does the single mask pickle belong to? There is one mask
    # for two catalogue cosmologies, and its radial limit can only match one.
    # Getting this wrong puts the wrong denominator under one of the two sets
    # of numbers, so it is established rather than assumed.
    r_of = {c: comoving_distance(Z_MAX, OMEGA_M[c]) for c in OMEGA_M}
    for c, r in sorted(r_of.items()):
        print("  comoving distance to z = %.3f under %s (Omega_M = %.3f): "
              "%.3f h^-1 Mpc" % (Z_MAX, c, OMEGA_M[c], r))
    owner = min(r_of, key=lambda c: abs(r_of[c] - r_mask))
    close("the mask's radial limit matches one catalogue cosmology",
          r_of[owner], r_mask, 0.5,
          "closest is %s; the other is %.3f, off by %.2f h^-1 Mpc"
          % (owner, r_of[[c for c in r_of if c != owner][0]],
             abs(r_of[[c for c in r_of if c != owner][0]] - r_mask)))
    # The two depths differ by 1.62 h^-1 Mpc, which is 0.5% in radius and so
    # 1.5% in volume: small, but it is the whole difference between the two
    # cosmologies' denominators and sharing one would put a 1.5% error on one
    # of the two sets of fractions.
    check("the two cosmologies give different survey depths",
          abs(r_of["WMAP5"] - r_of["Planck2018"]) > 1.0,
          "WMAP5 is %.2f h^-1 Mpc deeper (%.2f%% in volume), so the "
          "denominator is not shared"
          % (r_of["WMAP5"] - r_of["Planck2018"],
             100 * ((r_of["WMAP5"] / r_of["Planck2018"]) ** 3 - 1)))
    print("  -> the mask pickle belongs to %s; each cosmology below uses its "
          "own r_max" % owner)
    print()

    for cosmo in ("Planck2018", "WMAP5"):
        r_max = r_of[cosmo]
        print("-" * 78)
        print("COSMOLOGY: %s   Omega_M = %.3f   r_max = %.3f h^-1 Mpc"
              % (cosmo, OMEGA_M[cosmo], r_max))
        print("(cut 3: reported apart, never averaged)")
        print("-" * 78)

        axes = grid_box(mask, res, r_max)
        print("  grid %d x %d x %d = %.3g cells"
              % (len(axes[0]), len(axes[1]), len(axes[2]),
                 len(axes[0]) * len(axes[1]) * len(axes[2])))
        surv, n_survey = survey_cells(mask, res, axes, r_min, r_max)
        v_survey = n_survey * GRID ** 3
        print("  survey cells %d  ->  V_survey = %.5g h^-3 Mpc^3 (cut 5)"
              % (n_survey, v_survey))

        # --- VoidFinder -----------------------------------------------------
        maximal = read_table(os.path.join(
            RAW, "VoidFinder-nsa_v1_0_1_%s_comoving_maximal.txt" % cosmo))
        holes = read_table(os.path.join(
            RAW, "VoidFinder-nsa_v1_0_1_%s_comoving_holes.txt" % cosmo))
        nvoid = len(maximal["x"])
        want_n, want_pct = PUBLISHED[(cosmo, "VoidFinder")]
        close("%s VoidFinder void count" % cosmo, nvoid, want_n, 0,
              "[DVB23] Table 6")

        if cosmo == "Planck2018":
            frac_in = in_mask(mask, res, maximal["ra"], maximal["dec"]).mean()
            i = np.clip((maximal["dec"] + 90).astype(np.int64) * res,
                        0, mask.shape[0] - 1)
            j = np.clip(maximal["ra"].astype(np.int64) * res, 0, mask.shape[1] - 1)
            check("mask convention [ra, dec+90] validated on void centres",
                  frac_in > 0.97,
                  "%.4f of %d centres inside; transposed convention gives %.4f"
                  % (frac_in, nvoid, mask[i, j].mean()))
            r_col = np.sqrt(maximal["x"] ** 2 + maximal["y"] ** 2 + maximal["z"] ** 2)
            check("Cartesian-to-sky convention reproduces the file's own columns",
                  np.abs(r_col - maximal["r"]).max() < 1e-6,
                  "max |d r| = %.3g h^-1 Mpc" % np.abs(r_col - maximal["r"]).max())

        edge = maximal["edge"].astype(int)
        print("  VoidFinder: %d voids; edge flag 0/1/2 = %d/%d/%d"
              % (nvoid, (edge == 0).sum(), (edge == 1).sum(), (edge == 2).sum()))
        void_ids = maximal["void"].astype(np.int64)
        flag_by_id = np.zeros(int(void_ids.max()) + 1, dtype=int)
        flag_by_id[void_ids] = edge
        hole_flag = flag_by_id[holes["void"].astype(np.int64)]

        for label, keep in (("all voids (edge included)",
                             np.ones(len(hole_flag), dtype=bool)),
                            ("edge flag 0 only", hole_flag == 0),
                            ("edge flag != 1", hole_flag != 1)):
            g = rasterise_union(axes, holes["x"][keep], holes["y"][keep],
                                holes["z"][keep], holes["radius"][keep])
            frac = 100.0 * count_in(g, surv) / n_survey
            RESULTS[(cosmo, "VoidFinder", label)] = frac
            print("    %-26s f_v = %6.2f %%  [LCDM-conditioned]" % (label, frac))
            del g

        # [DVB23] Sec. 4.2 describes the volume fraction as a grid-particle
        # count over the void spheres with no edge filter, so the all-voids
        # variant is the one that should match Table 6. Checked, not assumed.
        got = RESULTS[(cosmo, "VoidFinder", "all voids (edge included)")]
        close("%s VoidFinder fraction reproduces Table 6" % cosmo,
              got, want_pct, 2.5,
              "all-voids variant; edge-excluded gives %.2f%%, far from the "
              "published %.1f%%, so Table 6's volume column does NOT exclude "
              "edge voids despite its note"
              % (RESULTS[(cosmo, "VoidFinder", "edge flag 0 only")], want_pct))

        # --- V2 -------------------------------------------------------------
        for finder in ("V2_VIDE", "V2_REVOLVER"):
            zv = read_table(os.path.join(
                RAW, "%s-nsa_v1_0_1_%s_zobovoids.dat" % (finder, cosmo)))
            n = len(zv["radius"])
            want_n, want_pct = PUBLISHED[(cosmo, finder)]
            close("%s %s void count" % (cosmo, finder), n, want_n, 0,
                  "[DVB23] Table 6")
            vol = (4.0 / 3.0) * np.pi * zv["radius"] ** 3
            interior = (zv["edge"] / zv["area"]) <= 0.1   # [DVB23] Sec. 4.1
            print("  %s: %d voids, %d with A_edge/A_total > 0.1 (%.0f%%)"
                  % (finder, n, (~interior).sum(), 100 * (~interior).mean()))
            for label, sel in (("all voids (edge included)", np.ones(n, bool)),
                               ("A_edge/A_total <= 0.1", interior)):
                frac = 100.0 * vol[sel].sum() / v_survey
                RESULTS[(cosmo, finder, label)] = frac
                print("    %-26s f_v = %6.2f %%  [LCDM-conditioned]" % (label, frac))
            NOTES.append((cosmo, finder,
                          RESULTS[(cosmo, finder, "all voids (edge included)")],
                          want_pct))
        print()

    # --- The V2 disagreement, pinned as a fact ------------------------------
    print("=" * 78)
    print("V2: sum of effective-radius volumes against [DVB23] Table 6")
    print("=" * 78)
    print("%-12s %-13s %10s %10s %9s" % ("cosmology", "finder", "computed",
                                         "published", "ratio"))
    for cosmo, finder, got, want in NOTES:
        print("%-12s %-13s %9.2f%% %9.1f%% %9.3f"
              % (cosmo, finder, got, want, got / want))
    signs = {np.sign(got - want) for _, _, got, want in NOTES}
    check("the V2 discrepancy is not one-directional",
          len(signs) > 1,
          "VIDE computes high and REVOLVER low, so no single systematic "
          "explains it; it is recorded unexplained, not reconciled")
    check("V2 Table 6 values are not reproduced from the published files",
          all(abs(got - want) > 4.0 for _, _, got, want in NOTES),
          "all four differ by more than 4 percentage points")
    print()
    print(v2_limitation())
    print()

    # --- Summary ------------------------------------------------------------
    print("=" * 78)
    print("SUMMARY: measured void volume fraction, per cuts 2, 3 and 4")
    print("=" * 78)
    print("%-12s %-13s %-28s %8s" % ("cosmology", "finder", "edge treatment", "f_v %"))
    for (cosmo, finder, label), frac in RESULTS.items():
        print("%-12s %-13s %-28s %8.2f" % (cosmo, finder, label, frac))
    print()

    vf = [v for k, v in RESULTS.items()
          if k[1] == "VoidFinder" and k[2] == "all voids (edge included)"]
    print("VoidFinder, both cosmologies, edge included (the only variant this")
    print("script reproduces against the literature): %.2f to %.2f %%"
          % (min(vf), max(vf)))
    vfe = [v for k, v in RESULTS.items()
           if k[1] == "VoidFinder" and k[2] == "edge flag 0 only"]
    print("The same, edge-excluded, which is NOT published: %.2f to %.2f %%"
          % (min(vfe), max(vfe)))
    print("The edge treatment moves VoidFinder's answer by %.1f percentage"
          % (min(vf) - max(vfe)))
    print("points, which is cut 4's systematic and is larger than the")
    print("difference between the two cosmologies (%.2f points)."
          % abs(vf[1] - vf[0]))
    print()
    print("All of the above are LCDM-conditioned (cut 8). None is compared to")
    print("any fitted f_v0 here; see findings/WP-4-void-fraction.md.")
    print()

    width = max(len(c[1]) for c in CHECKS)
    failed = 0
    for ok, name, detail in CHECKS:
        if not ok:
            failed += 1
        print("%s  %-*s %s" % ("PASS" if ok else "FAIL", width, name, detail))
    print()
    if failed:
        print("FAIL: %d of %d checks failed. No WP-4 number is quotable."
              % (failed, len(CHECKS)))
        return 1
    print("PASS: %d of %d checks." % (len(CHECKS), len(CHECKS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
