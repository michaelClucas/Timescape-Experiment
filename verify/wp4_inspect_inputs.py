#!/usr/bin/env python3
"""WP-4 step 0: inspect the VAST catalogue inputs before computing anything.

    .venv/Scripts/python verify/wp4_inspect_inputs.py

Read-only. Exits 0 if the inputs are shaped as `data/001-sdss-dr7-voids/SOURCE.md`
says, 1 otherwise. No volume fraction is computed here; that is
`verify/wp4_void_fraction.py`. This exists separately because the survey mask is
a Python pickle whose structure is not documented in SOURCE.md, and a volume
fraction computed against a misread mask would be wrong in a way that looks
right.

The pickle is executable content. It is loaded with the repository venv and
treated as data, per SOURCE.md field 8.
"""

import os
import pickle
import sys

import numpy as np

RAW = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "001-sdss-dr7-voids")

EXPECTED_COUNTS = {
    # SOURCE.md section 5, reproduced on download.
    "VoidFinder-nsa_v1_0_1_Planck2018_comoving_maximal.txt": 1163,
    "V2_VIDE-nsa_v1_0_1_Planck2018_zobovoids.dat": 531,
    "V2_REVOLVER-nsa_v1_0_1_Planck2018_zobovoids.dat": 518,
}

FAILED = []


def fail(msg):
    FAILED.append(msg)
    print("FAIL  %s" % msg)


def ok(msg):
    print("PASS  %s" % msg)


def describe(label, v, indent=6):
    pad = " " * indent
    print("%s%-16s %-14s shape=%s dtype=%s" % (
        pad, label, type(v).__name__, getattr(v, "shape", None),
        getattr(v, "dtype", None)))
    if isinstance(v, np.ndarray) and v.size:
        if v.dtype == bool:
            print("%s    True %d of %d (%.5f)" % (pad, v.sum(), v.size, v.sum() / v.size))
        elif np.issubdtype(v.dtype, np.number):
            print("%s    min %.6g  max %.6g" % (pad, v.min(), v.max()))


def main():
    print("=" * 78)
    print("1. Row counts against SOURCE.md section 5")
    print("=" * 78)
    for name, want in EXPECTED_COUNTS.items():
        path = os.path.join(RAW, name)
        if not os.path.exists(path):
            fail("%s missing" % name)
            continue
        with open(path) as fh:
            n = sum(1 for _ in fh) - 1  # one header line
        if n == want:
            ok("%s has %d rows" % (name, n))
        else:
            fail("%s has %d rows, SOURCE.md says %d" % (name, n, want))

    print()
    print("=" * 78)
    print("2. Column headers, as written in the files")
    print("=" * 78)
    for name in sorted(os.listdir(RAW)):
        if name.endswith((".txt", ".dat")):
            with open(os.path.join(RAW, name)) as fh:
                print("  %-56s %s" % (name, fh.readline().strip()))

    print()
    print("=" * 78)
    print("3. The survey mask pickle")
    print("=" * 78)
    mask_path = os.path.join(RAW, "NSA_main_mask.pickle")
    with open(mask_path, "rb") as fh:
        m = pickle.load(fh)
    print("  top-level type: %s" % type(m))
    if isinstance(m, dict):
        for k, v in m.items():
            describe(repr(k), v)
    elif isinstance(m, (tuple, list)):
        print("  length %d" % len(m))
        for i, v in enumerate(m):
            describe("[%d]" % i, v)
    else:
        describe("obj", m)
        if hasattr(m, "__dict__"):
            for k, v in vars(m).items():
                describe(repr(k), v)
        for attr in ("shape", "mask_resolution", "resolution", "mask"):
            if hasattr(m, attr):
                print("      attr %s = %r" % (attr, getattr(m, attr)))

    print()
    print("=" * 78)
    print("4. Coordinate and radius ranges, VoidFinder maximal, Planck2018")
    print("=" * 78)
    vf = np.genfromtxt(
        os.path.join(RAW, "VoidFinder-nsa_v1_0_1_Planck2018_comoving_maximal.txt"),
        names=True, skip_header=0, deletechars="", replace_space="_")
    vf = np.genfromtxt(
        os.path.join(RAW, "VoidFinder-nsa_v1_0_1_Planck2018_comoving_maximal.txt"),
        skip_header=1)
    with open(os.path.join(RAW, "VoidFinder-nsa_v1_0_1_Planck2018_comoving_maximal.txt")) as fh:
        cols = fh.readline().lstrip("#").split()
    for i, c in enumerate(cols):
        print("  %-8s min %12.5f  max %12.5f  mean %12.5f" % (
            c, vf[:, i].min(), vf[:, i].max(), vf[:, i].mean()))
    r = np.sqrt(vf[:, 0] ** 2 + vf[:, 1] ** 2 + vf[:, 2] ** 2)
    print("  %-8s min %12.5f  max %12.5f" % ("|xyz|", r.min(), r.max()))
    # The file carries its own radial coordinate in column 'r'. If |xyz| equals
    # it, the Cartesian coordinates are comoving distances in the same units,
    # which is what the volume calculation needs.
    ir = cols.index("r")
    resid = np.abs(r - vf[:, ir]).max()
    if resid < 1e-6:
        ok("|xyz| equals the file's own r column to %.2g, so units agree" % resid)
    else:
        fail("|xyz| differs from the file's r column by up to %.4g" % resid)

    print()
    print("=" * 78)
    print("5. V2 zobovoids: is `radius` an effective radius from the volume?")
    print("=" * 78)
    for finder in ("V2_VIDE", "V2_REVOLVER"):
        name = "%s-nsa_v1_0_1_Planck2018_zobovoids.dat" % finder
        with open(os.path.join(RAW, name)) as fh:
            cols = fh.readline().lstrip("#").split()
        d = np.genfromtxt(os.path.join(RAW, name), skip_header=1)
        ri, ai, ei = cols.index("radius"), cols.index("area"), cols.index("edge")
        rad, area, edge = d[:, ri], d[:, ai], d[:, ei]
        print("  %s: %d voids" % (finder, len(d)))
        print("      radius  min %8.3f max %8.3f" % (rad.min(), rad.max()))
        print("      area    min %10.1f max %10.1f" % (area.min(), area.max()))
        print("      edge    min %10.1f max %10.1f  nonzero %d of %d" % (
            edge.min(), edge.max(), (edge > 0).sum(), len(edge)))
        # If radius is an effective radius from volume, 4*pi*r^2 should be the
        # same order as the tabulated area, and their ratio tells us whether
        # `area` is a surface area in the same length units.
        sphere_area = 4 * np.pi * rad ** 2
        print("      area / 4*pi*r^2 : median %.4f  min %.4f  max %.4f" % (
            np.median(area / sphere_area), (area / sphere_area).min(),
            (area / sphere_area).max()))
        print("      edge / area     : median %.4f  max %.4f" % (
            np.median(edge / area), (edge / area).max()))

    print()
    if FAILED:
        print("FAIL: %d input check(s) failed. Do not compute a volume fraction "
              "until these are understood." % len(FAILED))
        return 1
    print("PASS: inputs match SOURCE.md. Nothing computed here by design.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
