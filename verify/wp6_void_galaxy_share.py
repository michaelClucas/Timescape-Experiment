#!/usr/bin/env python3
"""WP-6/WP-5: the share of VAST's galaxy sample lying inside VoidFinder voids.

    python verify/wp6_void_galaxy_share.py

Exits 0 if every check passes, 1 otherwise. Implements
data/002-nsa-v1_0_1/cuts.md exactly. Cut numbers are cited inline. The
headline uses cut 5a, appended to cuts.md on 2026-11-11 after the
registered cut 5 (|x-c| <= R) was found to count VoidFinder's hole-defining
wall galaxies, which sit exactly on hole surfaces. Both are printed. The
result is M_v,gal, the GALAXY share, which cut 7 says is reported as a
probably-low estimate of the matter share M_v and never as M_v itself.

Inputs (gitignored, fetched by the two datasets' fetch.sh):
  data/raw/002-nsa-v1_0_1/nsa_v1_0_1.fits
  data/raw/001-sdss-dr7-voids/V2_VIDE-*_galzones.dat, *_comoving_holes.txt,
  NSA_main_mask.pickle (a pickle: loaded only with the repo venv, as data)
"""

import os
import pickle
import sys

import numpy as np
from astropy.cosmology import FlatLambdaCDM
from astropy.io import fits
from scipy.spatial import cKDTree

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW1 = os.path.join(ROOT, "data", "raw", "001-sdss-dr7-voids")
RAW2 = os.path.join(ROOT, "data", "raw", "002-nsa-v1_0_1")
COSMO = {"Planck2018": 0.315, "WMAP5": 0.258}  # [DVB23] Sec. 2.1, as WP-4
FV_WP4 = {"Planck2018": (0.6228, 0.6157), "WMAP5": (0.6263, 0.6192)}  # cut 6: main, PR #14
THRESH = {"0.0265 (q_min moves by the q_0 error)": 0.0265,
          "0.0852 (q at f_v0=0.695 reaches 0)": 0.0852,
          "0.270 (K4)": 0.270}  # cut 7, verify/void_matter_sensitivity.py
R_MAX, Z_MAX = 332.38565, 0.114  # cut 4
EPS = 1e-3  # cut 5a (appended 2026-11-11): strict interior, excludes hole-defining surface galaxies
CHECKS = []


def check(name, ok, detail):
    CHECKS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


with open(os.path.join(RAW1, "NSA_main_mask.pickle"), "rb") as fh:
    mask, res, rlim = pickle.load(fh)
mask, res = np.asarray(mask, dtype=bool), int(res)


def in_mask(ra, dec, convention):
    i = np.clip(np.floor(res * ra).astype(np.int64), 0, mask.shape[0] - 1)
    if convention == "vast":  # int(res*dec) - res*dec_offset, int truncates toward zero
        j = np.trunc(res * dec).astype(np.int64) + 90 * res
    else:  # WP-4 pre-fix: int((dec + 90) * res)
        j = np.floor((dec + 90.0) * res).astype(np.int64)
    j = np.clip(j, 0, mask.shape[1] - 1)
    return mask[i, j]


print("reading NSA columns NSAID, RA, DEC, Z (memmap) ...")
with fits.open(os.path.join(RAW2, "nsa_v1_0_1.fits"), memmap=True) as hd:
    d = hd[1].data
    nsaid = np.asarray(d["NSAID"], dtype=np.int64)
    ra_all = np.asarray(d["RA"], dtype=float)
    dec_all = np.asarray(d["DEC"], dtype=float)
    z_all = np.asarray(d["Z"], dtype=float)
order = np.argsort(nsaid)
nsaid_s = nsaid[order]

results = {}
for cos, om in COSMO.items():
    gz = np.loadtxt(os.path.join(RAW1, f"V2_VIDE-nsa_v1_0_1_{cos}_galzones.dat"), dtype=np.int64)
    ids = gz[:, 0]
    # cut 1: match by NSAID
    k = np.searchsorted(nsaid_s, ids)
    k = np.clip(k, 0, len(nsaid_s) - 1)
    hit = nsaid_s[k] == ids
    check(f"{cos} cut 1 every galzones NSAID matches the NSA", hit.all(),
          f"{hit.sum()} of {len(ids)} matched, {np.count_nonzero(~hit)} unmatched")
    row = order[k[hit]]
    ra, dec, z = ra_all[row], dec_all[row], z_all[row]
    # cut 3: positions
    r = FlatLambdaCDM(H0=100, Om0=om).comoving_distance(z).value
    cd = np.cos(np.radians(dec))
    xyz = np.column_stack([r * cd * np.cos(np.radians(ra)), r * cd * np.sin(np.radians(ra)),
                           r * np.sin(np.radians(dec))])
    # cut 5: inside any hole sphere
    holes = np.loadtxt(os.path.join(RAW1, f"VoidFinder-nsa_v1_0_1_{cos}_comoving_holes.txt"))
    # margin = min over holes of (|x - c| - R); negative means inside
    tree = cKDTree(xyz)
    margin = np.full(len(xyz), np.inf)
    for h, lst in enumerate(tree.query_ball_point(holes[:, :3], holes[:, 3] + 1.0)):
        if lst:
            dd = np.linalg.norm(xyz[lst] - holes[h, :3], axis=1) - holes[h, 3]
            np.minimum.at(margin, lst, dd)
    n_surface = int(np.count_nonzero(np.abs(margin) < EPS))
    print(f"  {cos}: {n_surface} galaxies lie within {EPS} h^-1 Mpc of a hole surface "
          f"(VoidFinder's defining wall galaxies)")
    surv4 = (r <= R_MAX) & (z < Z_MAX)
    plateau = [np.mean(margin[surv4] <= -e) for e in (1e-3, 1e-2, 1e-1)]
    check(f"{cos} cut 5a plateau: interior share flat from 1e-3 to 1e-1 h^-1 Mpc",
          max(plateau) - min(plateau) < 0.002, ", ".join(f"{x:.4f}" for x in plateau))
    for rule, inside in (("cut5-as-registered(<=R)", margin <= 0), ("cut5a-strict(<R-1e-3)", margin <= -EPS)):
        for conv in ("vast", "wp4-prefix"):
            surv = surv4 & in_mask(ra, dec, conv)  # cut 4
            n_tot, n_void = int(surv.sum()), int((surv & inside).sum())
            m = n_void / n_tot
            results[(cos, conv, rule)] = (n_tot, n_void, m)
            fv_main, fv_fix = FV_WP4[cos]
            print(f"  {cos:10s} {rule:24s} mask={conv:10s} N_tot={n_tot:6d} N_void={n_void:5d} "
                  f"M_v,gal={m:.4f}  delta_g={m / fv_main - 1:+.4f} (f_v {fv_main}) "
                  f"/ {m / fv_fix - 1:+.4f} (f_v {fv_fix})")
    n_out = int(np.count_nonzero(~((r <= R_MAX) & (z < Z_MAX))))
    print(f"  {cos}: {n_out} of {len(r)} sample galaxies fall outside r <= {R_MAX} or z < {Z_MAX}")

m_head = results[("Planck2018", "vast", "cut5a-strict(<R-1e-3)")][2]
strict = [v[2] for k, v in results.items() if k[2].startswith("cut5a")]
spread = max(strict) - min(strict)
check("cut 8 sanity bound 2%-20%", 0.02 <= m_head <= 0.20, f"headline M_v,gal = {m_head:.4f}")
check("cut 5a result stable across cosmology and mask convention", spread < 0.005,
      f"spread {spread:.4f} across the four strict variants")
print("  cut 7, against the model's thresholds (galaxy share, probably low):")
for label, thr in THRESH.items():
    print(f"    {label}: M_v,gal {'above' if m_head > thr else 'below'} ({m_head:.4f} vs {thr})")

print(f"\n{sum(CHECKS)}/{len(CHECKS)} checks passed")
sys.exit(0 if all(CHECKS) else 1)
