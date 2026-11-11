#!/usr/bin/env bash
# Fetch NSA v1_0_1 (2.46 GB) and verify it against SDSS's published SHA-1.
# Idempotent and resumable.
set -euo pipefail
BASE=https://data.sdss.org/sas/dr17/sdss/atlas/v1
DEST="$(git rev-parse --show-toplevel)/data/raw/002-nsa-v1_0_1"
mkdir -p "$DEST"
cd "$DEST"
curl -sS --retry 3 -o sdss_atlas_v1.sha1sum "$BASE/sdss_atlas_v1.sha1sum"
curl -sSL --retry 5 -C - -o nsa_v1_0_1.fits "$BASE/nsa_v1_0_1.fits"
grep ' nsa_v1_0_1.fits$' sdss_atlas_v1.sha1sum | sha1sum -c -
