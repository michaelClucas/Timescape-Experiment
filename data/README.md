# Datasets: provenance and what is committed

Raw data is **not** committed. This repository commits the record of what
was obtained and the code that obtained it, so a fit can be reproduced
without the repository carrying gigabytes.

```
data/
  README.md              this file
  NNN-<dataset>/
    SOURCE.md            where it came from, exactly
    fetch.sh             the command that downloads it, runnable
    MANIFEST.sha256      checksums of every file used
    cuts.md              the selection applied, and why
```

`.gitignore` already excludes `data/raw/`, `*.fits` and `*.npz`.

## SOURCE.md must answer

1. **The URL or archive**, specific to the release, not a project homepage.
2. **The release or version string**, as the providers name it.
3. **Size on disk**, so the next person knows what they are committing to.
4. **The reference to cite**, with a DOI or arXiv identifier.
5. **What it can settle**, in this programme's terms.
6. **What it cannot settle.** This is the field most often left out and the
   one that prevents a dataset being quietly reused for a question it
   cannot answer.
7. **Whether any of it was derived under an assumed cosmology**, and if so
   which. This is the circularity question, and for supernova data it is
   the whole question: a light-curve standardisation calibrated under LCDM
   cannot be used to test a non-LCDM model without the dependence being
   accounted for.

Field 7 is why this directory exists in this form rather than as a loose
download. Run 01 could not settle, from published method sections alone,
whether the timescape supernova results inherit an LCDM-calibrated
standardisation. The answer changes how much the headline evidence is
worth, and it is a property of the data as obtained, so it is recorded with
the data.

## Checksums

`MANIFEST.sha256` covers every file a fit actually reads. Not the archive:
the files. A dataset that changes under you without the checksum changing
is the failure this guards against, and public cosmology datasets are
revised more often than people expect.

Verify with:

    sha256sum -c data/NNN-<dataset>/MANIFEST.sha256

## Cuts

`cuts.md` states the selection and the reason for each cut, with the
number of objects before and after. A redshift cut is a modelling choice,
not a technicality: timescape's distinctive signature is at low to
intermediate redshift, and the published analyses differ in where they cut.
Any fit this programme runs reports its cuts alongside its result, and
reports the result's sensitivity to them.
