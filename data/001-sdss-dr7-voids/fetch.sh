#!/usr/bin/env bash
# Fetch the VAST SDSS DR7 void catalogs (Douglass, Veyrat & BenZvi).
# Zenodo record 11043278, version 1.3.1, DOI 10.5281/zenodo.11043278.
# ~20.4 MB across 17 files. Idempotent: skips a file already present.
set -euo pipefail

RECORD=11043278
DEST="$(git rev-parse --show-toplevel)/data/raw/001-sdss-dr7-voids"
mkdir -p "$DEST"

FILES=(
  VoidFinder-nsa_v1_0_1_Planck2018_comoving_maximal.txt
  VoidFinder-nsa_v1_0_1_Planck2018_comoving_holes.txt
  VoidFinder-nsa_v1_0_1_WMAP5_comoving_maximal.txt
  VoidFinder-nsa_v1_0_1_WMAP5_comoving_holes.txt
  V2_VIDE-nsa_v1_0_1_Planck2018_zobovoids.dat
  V2_VIDE-nsa_v1_0_1_Planck2018_zonevoids.dat
  V2_VIDE-nsa_v1_0_1_Planck2018_galzones.dat
  V2_VIDE-nsa_v1_0_1_WMAP5_zobovoids.dat
  V2_VIDE-nsa_v1_0_1_WMAP5_zonevoids.dat
  V2_VIDE-nsa_v1_0_1_WMAP5_galzones.dat
  V2_REVOLVER-nsa_v1_0_1_Planck2018_zobovoids.dat
  V2_REVOLVER-nsa_v1_0_1_Planck2018_zonevoids.dat
  V2_REVOLVER-nsa_v1_0_1_Planck2018_galzones.dat
  V2_REVOLVER-nsa_v1_0_1_WMAP5_zobovoids.dat
  V2_REVOLVER-nsa_v1_0_1_WMAP5_zonevoids.dat
  V2_REVOLVER-nsa_v1_0_1_WMAP5_galzones.dat
  NSA_main_mask.pickle
)

for f in "${FILES[@]}"; do
  if [ -s "$DEST/$f" ]; then
    echo "have    $f"
    continue
  fi
  echo "fetch   $f"
  curl -sSL --retry 3 --max-time 300 \
    -o "$DEST/$f" \
    "https://zenodo.org/api/records/$RECORD/files/$f/content"
done

echo
echo "Verify against the committed manifest:"
echo "  (cd \"$DEST\" && sha256sum -c \"$(git rev-parse --show-toplevel)/data/001-sdss-dr7-voids/MANIFEST.sha256\")"
