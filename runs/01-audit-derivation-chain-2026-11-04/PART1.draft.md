# Part 1 - The chain

The seed chain `D1`-`D8` is wrong in three structural ways, and the
corrections change where the weight sits.

1. The seed's `D2` conflates a proved identity with a statement that is
   not a theorem anywhere in the retrieved literature, and timescape only
   uses the former.
2. The seed's `D4` ("backreaction can be large enough to matter") is not a
   link timescape needs in the form the Green-Wald dispute is about.
   Wiltshire's own fitted solution has kinematical backreaction at
   `Omega-bar_Q0 = -0.0293 (+0.0033/-0.0036)`, negative, with
   `|Omega-bar_Q| <~ 0.042` at all times, and no volume acceleration
   (`q-bar > 0`). The bare energy budget is dominated by **average
   negative spatial curvature**, `Omega-bar_k0 = 0.862 (+0.024/-0.032)`
   [SOURCED: arXiv:1311.3787, Table 1 and Sec. 5.3]. Any audit that
   treats the Q-magnitude dispute as timescape's load-bearing link has
   mislocated the model's mechanism.
3. The seed has no step for light propagation. Getting a
   distance-redshift relation out of a scalar-averaged model is a separate
   and, by both Buchert's and Wiltshire's own statements, unjustified
   step. It carries weight 3.

Steps are renumbered `T1`-`T13`. The mapping to the seed is given per
step.

---

### T1. The late universe is inhomogeneous, and voids occupy the majority of present volume
**Kind: OBSERVATION** (not a kind in the schema's list; the nearest schema
value is `INTERPRETATION`, which is wrong, so this is recorded as a
measurement). `[SOURCED]`
**Seed: `D1`, tagged `THEOREM` / observational. I disagree with the tag.**
"Theorem" is the wrong word for a measurement and the seed's own
annotation concedes this; the entry should not carry a `THEOREM` tag at
all.

Statement: voids with effective radii above 10 h^-1 Mpc fill 62% of the
SDSS DR7 sample volume, median effective radius 17 h^-1 Mpc, largest just
over 30 h^-1 Mpc, with density contrast `delta < -0.85` at void edges
[SOURCED: Pan, Vogeley, Hoyle, Choi & Park, arXiv:1103.4156, MNRAS 421
(2012) 926, DOI 10.1111/j.1365-2966.2011.20197.x, abstract].

Support: the same paper states the void fractions and sizes are similar
to those in LCDM mock catalogues from SPH halo-model and other LCDM
simulations [SOURCED: same, abstract]. **This matters: the observed void
filling factor is reproduced by LCDM, so it is not by itself a
discriminating observable.**

The number is strongly algorithm-dependent. Watershed-based `V2/VIDE`,
`V2/REVOLVER` and `VoidFinder` applied to the same SDSS DR7 volume give
materially different filling factors `[LEAD]`; I retrieved the paper that
reports them (Douglass, Veyrat & BenZvi, arXiv:2202.01226, ApJS 265:7,
2023, DOI 10.3847/1538-4365/acabcf) but the abstract page states only
that it extracts "the volume fraction of the catalog contained within
voids" without values, and I did not retrieve the values from its tables.
So the spread is `[LEAD]`, not `[SOURCED]`.

Homogeneity scale, which the seed asks about: `R_H = 63.3 +/- 0.7 h^-1
Mpc` from BOSS DR12 CMASS, against an LCDM prediction of 62.0 h^-1 Mpc
[SOURCED: Ntelis et al., arXiv:1702.02159, JCAP 06 (2017) 019, DOI
10.1088/1475-7516/2017/06/019, abstract]; and `R_H = 70.33 +/- 10.74
Mpc/h` at `z_eff = 0.128` from SDSS blue galaxies [SOURCED: Dias, Avila &
Bernui, arXiv:2310.04594, abstract]. These are not consistent central
values and both are threshold-definition dependent: Ntelis et al. define
`R_H` as where the fractal correlation dimension `D2` reaches 3 within
1%. Timescape does **not** require a larger homogeneity scale than the
standard value; it coarse-grains dust at ~100 h^-1 Mpc, tied to the
statistical homogeneity / BAO scale [SOURCED: arXiv:1106.1693, Sec. 4.1].

Strongest objection: none to the measurement. The live question is
whether the scale of statistical homogeneity is reached within survey
volumes, and the retrieved numbers disagree with each other.

**If this fails: 3.** Everything collapses.

---

### T2. Spatial averaging of scalars does not commute with time evolution
**Kind: THEOREM.** `[SOURCED]`
**Seed: part of `D2`. The seed's `THEOREM` tag is correct for this half
and I keep it.**

Statement, exactly: for a scalar `Psi` averaged over a comoving domain
`D`,

    d/dt <Psi>_D - <dPsi/dt>_D = <Psi.theta>_D - <Psi>_D <theta>_D

This is an exact identity, labelled a Lemma, at Eq. (9f) of Buchert's
first averaging paper [SOURCED: Buchert, arXiv:gr-qc/9906015, Gen. Rel.
Grav. 32 (2000) 105, Sec. 2.2, Lemma Eq. (9f)]. Restated as Eq. (7) of
the 2008 review, where Buchert adds that the non-commutativity is "purely
kinematical", so it is not necessarily the nonlinearity of the field
equations that causes backreaction [SOURCED: Buchert, arXiv:0707.2153,
Gen. Rel. Grav. 40 (2008) 467, Sec. 1.3.2].

Strongest objection: none. It is an identity.

**If this fails: 3.** If averaging commuted, the averaged equations would
be Friedmann's and there would be no model.

---

### T3. The Einstein tensor of an averaged metric differs from the average of the Einstein tensors
**Kind: INTERPRETATION, not `THEOREM`.** `[SOURCED]` for the
classification, in the sense that I retrieved the places this is stated
and none states it as a theorem.
**Seed: the other half of `D2`, tagged `THEOREM`. I disagree with the
tag, and this is the run's single most consequential kind correction.**

In the sources I retrieved, this is nowhere a proved theorem with a
stated definition of the average. Ellis calls it "the basic point", not a
theorem or a lemma: "averaging the geometry and calculating the field
equations do not commute" and "coarse-graining (or averaging) does not
commute with calculating the EFE from the metric tensor" [SOURCED: Ellis,
arXiv:1103.2335, Class. Quantum Grav. 28 (2011) 164001, Sec. 2.2]. In the
same section Ellis says the averaging operation used to make the point is
not well defined: averaging tensors is "not a well-defined tensorial
operation" and changing coordinates changes the result [SOURCED: same,
Sec. 2.2]. The symbolic version, `E[<g>] - <E[g]> ~ <Gamma>^2 -
<Gamma^2> != 0`, is introduced with "irrespective of any details of the
averaging operation, one notes that" and the `~` are order-of-magnitude,
with the inequality argued from term structure rather than proved
[SOURCED: Paranjape, arXiv:0906.3165, PhD thesis TIFR 2009, Sec. 1, Eq.
(1.3)]. Buchert's 2008 review does **not** state it [SOURCED, negative:
arXiv:0707.2153, searched].

**If this fails: 0.** Timescape does not use it. Its formalism rests on
T2, which is exact for scalars. Noting this matters because the seed
places a `THEOREM` tag on the step that is not a theorem, and the
literature's habit of motivating backreaction with the metric-averaging
version while deriving everything from the scalar version is exactly the
blur this repository exists to catch.

---

### T4. The Buchert averaged scalar equations, with a kinematical backreaction term
**Kind: THEOREM, conditional on the scheme choices in T5.** `[SOURCED]`
**Seed: `D3`, tagged `SCHEME`. The tag is defensible but imprecise: the
equations themselves are theorems; what is a scheme is the set of
conditions they are derived under, and the closure that has to be added
on top (T5, T6).**

Statement, from the Theorem of Sec. 2.2 of arXiv:gr-qc/9906015:

    3 a_D''/a_D + 4 pi G M_D/(V_D0 a_D^3) - Lambda = Q_D        (10a)
    3 (a_D'/a_D)^2 - 8 pi G M_D/(V_D0 a_D^3) + (1/2)<R>_D - Lambda = -Q_D/2   (10b)
    Q_D := (2/3)<(theta - <theta>_D)^2>_D - 2<sigma^2>_D        (10c)

with the integrability condition, Corollary 3, Eq. (13a):

    Q_D' + 6(a_D'/a_D)Q_D + <R>_D' + 2(a_D'/a_D)<R>_D = 0

called "a universal relation between the averaged Ricci scalar and the
'backreaction' term" [SOURCED: arXiv:gr-qc/9906015, Sec. 2.2, Theorem
Eqs. (10a)-(10c), Corollary 3 Eqs. (13a)-(13b)]. Same system at Eqs.
(24), (27), (29) of arXiv:0707.2153 and Eqs. (7)-(10) of Buchert &
Rasanen, arXiv:1112.5335, Annu. Rev. Nucl. Part. Sci. 62 (2012) 57, DOI
10.1146/annurev.nucl.012809.104435.

Sign and magnitude Q is *allowed*, separately from what any model needs:
`Q_D` has no fixed sign, since expansion variance enters with `+` and
mean squared shear with `-`. Volume acceleration with `Lambda = 0`
requires `Q_D > 4 pi G <rho>_D`, i.e. expansion fluctuations must
supersede shear fluctuations, and `Q_D` must decay more slowly than the
averaged density, which Buchert says is "not obvious" to satisfy
[SOURCED: arXiv:0707.2153, Sec. 3.2.1, Eq. (63)]. For on-average flat
domains the integrability condition gives `Q_D = Q_D0 a_D^-6` [SOURCED:
arXiv:gr-qc/9906015, Appendix B Eq. (B.1a)]; the scaling-solution
analysis gives `n = -6, p = -2` as the only solution with `n != p`
[SOURCED: arXiv:0707.2153, Sec. 3.3.5, Eqs. (74)-(76)]. So a slower decay
requires nonzero coupling between `Q_D` and `<R>_D` - the integrability
condition is what does the work.

Strongest objection: Green & Wald, footnote 4 of Sec. 3 of
arXiv:1407.8084: "A further difficulty with the Buchert approach is that
the equations are underdetermined." Buchert says the same thing himself
(T5), so this is a point of agreement, not a dispute.

**If this fails: 3.**

---

### T5. The Buchert system does not close, so any number requires an added closure assumption
**Kind: SCHEME.** `[SOURCED]`
**Seed: absent as a separate step; folded into `D3`. Separating it is
necessary, because this is where "theorem" stops and "model" starts.**

Buchert, in the paper that proves T4: "Therefore, we cannot solve the
'backreaction problem' for scalars based on this system" [SOURCED:
arXiv:gr-qc/9906015, Sec. 2.2]. Sec. 3.3: "Forthcoming efforts should be
directed towards finding a topological closure condition for the
hypersurfaces". Sec. 3.5 calls the result "a general framework" with
which one can describe the effective dynamics. Ellis, independently:
the Buchert approach "can in principle provide an effective acceleration
term" but the closure Ansatz is "not fully justified from the underlying
dynamics" [SOURCED: arXiv:1103.2335, Sec. 2.3.2].

The conditions T4 is derived under, each chosen rather than derived:
irrotational dust (Sec. 2.1, "irrotational fluid motion with the simplest
matter model 'dust'"); a flow-orthogonal constant-proper-time foliation
(Sec. 2.1, "We choose a flow-orthogonal coordinate system"); scalars only
(Sec. 2.2 footnote 3, "we do not attempt to average the spacetime
geometry as a whole"); and a given domain, with the averaging
"functionally depend[ing] on content, shape and position of the spatial
domain of averaging" (Sec. 2.2 footnote 3) [all SOURCED:
arXiv:gr-qc/9906015]. Buchert & Rasanen state the hypersurface dependence
flatly: "The result does, however, depend on the hypersurface on which
the average is taken" [SOURCED: arXiv:1112.5335, Sec. 2.2].

**If this fails: 3.** There is no quantitative model without a closure,
and every number in timescape comes from a particular one (T6, T7).

---

### T6. A two-phase ansatz: spatially flat walls bounded by finite-infinity surfaces, negatively curved voids, one void curvature scale
**Kind: SCHEME.** `[SOURCED]`
**Seed: `D5`, tagged `SCHEME`. Correct; I keep the tag and add what the
seed asks for, namely what fixes the split.**

Construction: finite infinity is the boundary of a compact domain within
which the average expansion vanishes, with `theta > 0` outside [SOURCED:
arXiv:gr-qc/0702082, New J. Phys. 9 (2007) 377, Sec. 3.2, Eq. (11);
restated arXiv:1106.1693, Eq. (22) and Fig. 1]. The split is
`a-bar^3 = f_wi a_w^3 + f_vi a_v^3` with `f_wi + f_vi = 1`, and
`f_v(t) = f_vi a_v^3 / a-bar^3` [SOURCED: arXiv:gr-qc/0702082, Sec. 5.1,
Eq. (22)]. Walls are *assumed* spatially flat: "The local average geometry
at the boundary of a finite infinity region is assumed to be spatially
flat" [SOURCED: arXiv:0709.0732, Phys. Rev. Lett. 99 (2007) 251101, text
at Eq. (1)]. Voids are negatively curved with `k_v < 0`.

What fixes two phases rather than a continuum: nothing, by Wiltshire's
own account. He asserts the structure rather than deriving it, says "a
single negative curvature scale is assumed as a simplification", and
notes one "could potentially use different curvature scales" for voids
and minivoids [SOURCED: arXiv:1106.1693, Sec. 4.2]. I found **no
quantitative sensitivity analysis** of the result to the two-phase choice
in anything I retrieved. He also concedes "There is an intrinsic
ambiguity in assigning the shape to the boundary" of finite infinity
[SOURCED: arXiv:gr-qc/0702082, Sec. 3.2]. The construction additionally
assumes no backreaction *within* walls and *within* voids separately
[SOURCED: arXiv:0909.0749, Phys. Rev. D 80 (2009) 123512, Sec. II].

Strongest objection: Green & Wald, Sec. 3 of arXiv:1407.8084, that large
averaged scalar curvature produced this way is an artifact of a poor
metric approximation - "these apparent backreaction effects are entirely
spurious" - illustrated with a Minkowski example in which the averaged
scalar curvature "is enormous for sufficiently large N", and a
two-disconnected-universes example of which they write "Obviously, this
acceleration is not a physical effect" [SOURCED: arXiv:1407.8084, Sec. 3,
at Eq. (16)]. This, not the traceless-stress theorem, is the Green-Wald
line of attack that actually reaches timescape's mechanism. See O1.

**If this fails: 3.**

---

### T7. There is an exact general solution of the two-scale averaged equations, and the phenomenology uses a special-case tracker attractor
**Kind: THEOREM of the averaged equations under T6, plus SCHEME for the
restriction to the tracker.** `[SOURCED]`
**Seed: absent. The seed does not distinguish "exact solution" from
"solution actually used", and the title of the PRL invites the confusion.**

What is exact: a general exact solution of the two-scale **Buchert**
equations (5) and (6), not of the Einstein field equations. The paper
says it will "derive the general exact solution to the Buchert
equations", and notes Buchert's scheme "does not average all of the
Einstein equations" [SOURCED: arXiv:0709.0732, Introduction]. The general
solution is Eqs. (11) and (13); Eq. (13) is transcendental, so
`a-bar(t)` and `f_v(t)` are only implicit. Matter-dominated epoch only:
"Here we restrict attention to the matter-dominated epoch."

What is used: all observational work runs on a **late-time tracker**
special case (`eps_i = 0`), described as "a late-time tracker solution,
an attractor", with `h_r = 2/3` exactly and `f_v(t)` given by Eq. (19)
[SOURCED: arXiv:0709.0732, at Eqs. (18)-(19)]. The general solution
approaches it to within 1% by `z ~ 37`; tracker accuracy against the full
solution is quoted as 0.1% in `H_0`, 1% in `f_v0`, 3% in `Omega_M0`
[SOURCED: arXiv:gr-qc/0702082, footnote 65].

Separately: the averaged metrics are "not exact solutions of the Einstein
equations" [SOURCED: Smale & Wiltshire, arXiv:1009.5855, MNRAS 413 (2011)
367, Sec. 2].

**If this fails: 2.** The qualitative claim survives; every number does
not.

---

### T8. In the fitted solution the bare budget is curvature-dominated, backreaction is small and negative, and there is no volume acceleration
**Kind: FIT, with the structure a consequence of T4-T7.** `[SOURCED]`
**Seed: `D4`, "Backreaction can be large enough to matter", tagged
`INTERPRETATION` / disputed. I disagree, and this is the second
consequential correction. Timescape does not claim large backreaction.**

From Wiltshire's own review, Table 1: `f_v0 = 0.695 (+0.041/-0.051)`,
`Omega-bar_M0 = 0.167 (+0.036/-0.037)`,
`Omega-bar_k0 = 0.862 (+0.024/-0.032)`,
`Omega-bar_Q0 = -0.0293 (+0.0033/-0.0036)`,
`Omega-bar_R0 = (5.00 +0.56/-0.48) x 10^-5`, dressed
`Omega_M0 = 0.41 (+0.06/-0.05)`, dressed `H_0 = 61.7 +/- 3.0`, bare
`H-bar_0 = 50.1 +/- 1.7` km/s/Mpc [SOURCED: arXiv:1311.3787, Table 1].
Sec. 5.3 of the same: "|Omega-bar_Q| <~ 0.042 at all times which means
that the backreaction is never large enough to make q-bar negative"
[SOURCED: same, Sec. 5.3]. In the 2009 paper: the backreaction term "is
at most of order 4.2%", `Omega-bar_Q` is negative, it is "never large
enough relative to" `Omega-bar_M` to give volume average cosmic
acceleration, and the bare deceleration parameter `q-bar = (1/2)
Omega-bar_M + 2 Omega-bar_Q` "is positive" [SOURCED: arXiv:0909.0749,
Sec. II.3 and Sec. II.4, Eqs. (18)-(21)].

So: `Omega-bar_k0 / |Omega-bar_Q0| = 29`. The apparent acceleration in
timescape is not produced by kinematical backreaction. It is produced by
large average negative spatial curvature plus the lapse (T10, T11)
`[INFERENCE]`, premises: the bare budget values above, `q-bar > 0`, and
the fact that the dressed-parameter map is the only remaining place the
sign change can come from (T11, T12).

**If this fails: 3** - but note what "fails" means here. If the fitted
`Omega-bar_k0` is wrong, timescape fails. If `Omega-bar_Q` turned out
large, timescape would not need it.

Strongest objection: O1, re-aimed. The Green-Wald framework's theorems
(effective stress-energy traceless, satisfies the weak energy condition,
"must be of the form of a P=rho/3 fluid, and therefore cannot mimic dark
energy" [SOURCED: arXiv:1407.8084, Sec. 2, Theorems 1 and 2, Eqs. (7)-(8)])
are about `Q`-type backreaction and therefore do not engage this step.
Their Sec. 3 argument that large averaged scalar curvature is spurious
does engage it. Green & Wald restrict to `k = 0` and make no statement
that average spatial curvature must stay near FLRW [SOURCED, negative:
arXiv:1407.8084, Sec. 4.1 after Eq. (21)].

---

### T9. The Cosmological Equivalence Principle
**Kind: POSTULATE.** `[SOURCED]`, and Wiltshire settles it himself.
**Seed: `D6`, tagged `POSTULATE`. The tag is correct. I am confirming it
with his own words because the seed asks whether it is claimed to follow
from GR, and the answer is a clear no.**

Statement, Sec. II.1 of arXiv:0809.1183, Phys. Rev. D 78 (2008) 084032,
around Eq. (1): "At any event, always and everywhere, it is possible to
choose a suitably defined spacetime neighbourhood" / "in which average
motions (timelike and null) can be described by geodesics in a geometry
which is Minkowski" up to a time-dependent conformal transformation, with
Eq. (1) `ds^2 = a^2(eta)[-d eta^2 + dr^2 + r^2 d Omega^2]` [SOURCED].

Status, in his own words, all from arXiv:0809.1183: abstract, "The strong
equivalence principle is extended in application to averaged dynamical
fields in cosmology"; Sec. I, "by proposing an extension of the SEP to
cosmology"; Sec. II.1, "the CEP thus represents a refinement in the
definition of inertial frames"; Sec. VII, "I have extended the strong
equivalence principle to account for the average effect of the density of
matter". The word "postulate" does not appear. The sentence that settles
it as content additional to GR is in a later paper: there is "a further
principle of relativity that is lacking in general relativity with the
SEP alone" [SOURCED: arXiv:1106.1693, Class. Quantum Grav. 28 (2011)
164006, Sec. 3.3.1], and it "would reduce to the standard SEP if" the
conformal factor were constant [SOURCED: same].

He nowhere claims it follows from standard GR, and he treats its scope as
open: "A question remains as to what extent we should take it as a
universal principle?" [SOURCED: arXiv:0809.1183, Sec. VI]. The machinery
is admittedly unbuilt: the procedures for patching cosmological inertial
frames into a uniform-flow slicing "have not been developed yet"
[SOURCED: arXiv:1106.1693, Sec. 3.3.1].

The CEP is **not** in the first timescape papers. It does not appear in
arXiv:gr-qc/0702082 in the portion retrieved, which uses the ordinary
equivalence principle only negatively: "on account of the equivalence
principle there is no local definition of gravitational energy" (Sec.
4.1) `[SOURCED, partial: first 100k characters of the ar5iv text]`. So
the CEP was introduced in 2008 to underwrite a 2007 model `[INFERENCE]`,
premises: the publication dates and the absence of the term from the
retrieved portion of the 2007 paper.

Is there a laboratory or solar-system regime where it is checkable? The
one lead I retrieved is that the implied present relative deceleration is
`alpha_0 ~ 6.7 x 10^-11 m/s^2` [SOURCED: arXiv:0809.1183, Sec. V.1, Eq.
(29)], and Wiltshire himself says of the coincidence with the MOND
acceleration scale that it "may be purely coincidental" and that "no firm
conclusions should be drawn until a compelling theoretical case is
assembled", and that "no detailed quantitative comparisons can be made
until the transition zone around finite infinity is more directly
modelled" [SOURCED: arXiv:0809.1183, Sec. V.2]. A later paper applies the
quasilocal approach to galactic dynamics [SOURCED: Galoppo, Re &
Wiltshire, arXiv:2408.00358, Class. Quantum Grav. 42 (2025) 135004,
title and listing], which I did not retrieve in full. See Part 6.

**If this fails: 3.** This is where the model lives or dies, and the seed
is right about that.

---

### T10. The relative lapse between wall and volume-average clocks is physical, and cumulatively of order 35-38% today
**Kind: POSTULATE for the existence, FIT for the magnitude.** `[SOURCED]`
**Seed: folded into `D6`. Splitting existence from magnitude is
necessary, because the magnitude is not an independent prediction.**

Notation and relation: the relative lapse is `gamma-bar`, with
`gamma-bar_w = 1 + (1 - h_r) f_v / h_r`, `h_r = H_w/H_v < 1` [SOURCED:
arXiv:0709.0732, Eq. (7)]. On the tracker `h_r = 2/3`, so

    gamma-bar = 1 + f_v / 2

[SOURCED: arXiv:0709.0732, text after Eq. (19)]. There is a ceiling:
`gamma < 3/2`, i.e. 50% [SOURCED: arXiv:gr-qc/0702082, abstract and Sec.
4.2].

Magnitudes found, with sources: "accumulated relative difference of 38%"
[SOURCED: arXiv:0809.1183, abstract]; "can typically grow to the order of
38% by the present epoch" [SOURCED: arXiv:1009.5855, Sec. 2]; "can
cumulatively lead to present epoch clock rate differences of order 35%"
[SOURCED: Nazer & Wiltshire, arXiv:1410.3470, Phys. Rev. D 91 (2015)
063519, Sec. I]; "present epoch large variation of clock rates, of order
35%" [SOURCED: arXiv:1311.3787, Sec. 5.2]; `gamma-bar = 1.38
(+0.06/-0.05)` [SOURCED: arXiv:0809.1183, Sec. III.1]; and for a void
density contrast `delta = -0.9` to `-0.95`, `gamma = 1.42` to `1.46`,
with "These clock rate variances of 42%-46% are large, and counter
intuitive" [SOURCED: arXiv:0809.1183, Sec. III.1, Eqs. (11)-(12)].

**No uncertainty is ever attached to the 35% or 38% figure in any paper I
retrieved.** And because `gamma-bar = 1 + f_v/2` on the tracker, the
figure is an algebraic restatement of the fitted `f_v0`: 38% tracks
`f_v0 ~ 0.76`, 35% tracks `f_v0 ~ 0.695`. The drift from 38% to 35%
across papers follows the drift in the fitted `f_v0` and is not flagged
as a change in any paper I retrieved. So the headline number is a `FIT`,
not a prediction `[INFERENCE]`, premises: the tracker relation and the
fitted `f_v0` values in T13.

Consequence of the same mechanism: the volume-average present CMB
temperature is "up to about 35% cooler" than the wall value, `T-bar =
gamma-bar^-1 T` [SOURCED: arXiv:1410.3470, Sec. III.2, Eq. (20)]; and the
age of the universe is observer-dependent, 14.2 Gyr for a wall observer
against 17.5 Gyr for a volume-average observer [SOURCED:
arXiv:1311.3787, Secs. 5-6].

Strongest objection: O2. Wiltshire's own most damaging concession on this
point is about the gauge the construction needs: "The argument above
relies on it being possible to choose a locally uniform Hubble flow
gauge" and "Such a gauge can be maintained outside finite infinity
regions, but not within them" [SOURCED: arXiv:0809.1183, Sec. III.1] -
that is, not in the regions where observers actually are.

**If this fails: 3.** Independently of T8. Granting backreaction in full
does not help here, and vice versa.

---

### T11. Dressed versus bare parameters, and the dressed effective metric
**Kind: SCHEME plus INTERPRETATION.** `[SOURCED]`
**Seed: `D7`, tagged `INTERPRETATION` + `SCHEME`. Correct; I keep it.**

The map: dressed Hubble `H = gamma-bar H-bar - d(gamma-bar)/dt`
[SOURCED: arXiv:0709.0732, Eq. (8); arXiv:0909.0749, Eq. (27)]; dressed
matter density `Omega_M = gamma-bar^3 Omega-bar_M` [SOURCED:
arXiv:0709.0732 after Eq. (7); arXiv:0909.0749, Eq. (26)]; dressed
`H_0 = (4 f_v0^2 + f_v0 + 4) H-bar_0 / [2(2 + f_v0)]` [SOURCED:
arXiv:0709.0732, Eq. (25)].

The dressed parameters are **not** constrained by a sum rule: they "do
not satisfy a simple relation analogous to" the bare one [SOURCED:
arXiv:0709.0732], and dressed density parameters do not sum to one, so
they are "just a convenient parametrization" [SOURCED: arXiv:1410.3470,
Sec. III.1].

**If this fails: 3.**

---

### T12. The dressed effective metric correctly gives luminosity distances along the observer's past light cone
**Kind: SCHEME / POSTULATE, acknowledged as not yet justified.**
`[SOURCED]`
**Seed: absent entirely. This is a weight-3 step that the seed omits, and
both Buchert and Wiltshire say in print that it is unjustified.**

Buchert: "The averaged equations cannot predict luminosity distances
unless one considers averages on the lightcone" [SOURCED:
arXiv:0707.2153, Sec. 3.3.7]; using a template metric for luminosity
distances "still neglects the effect of inhomogeneities on light
propagation" [SOURCED: same, Sec. 4.3.1]. Wiltshire: identifying the
volume-average Hubble parameter with the observed one, and the observed
redshift with `a-bar_0/a-bar`, "remains to be rigorously justified"
[SOURCED: arXiv:1106.1693, Sec. 4]; the dressed metric is spherically
symmetric but not homogeneous and is not an exact solution of the
Einstein equations [SOURCED: arXiv:0909.0749, Sec. II]; wall time is
"assumed to be a good approximation to the time measured by typical
observers in galaxies" [SOURCED: arXiv:0909.0749, Appendix B]; and
`tau_w` is taken to equal our clock time though "ultimately this may also
require some correction" [SOURCED: arXiv:gr-qc/0702082, Sec. 5.2].

Rasanen's light-propagation analysis shows what it takes to get a
distance-redshift relation from averaged quantities: his main result, Eq.
(38) of arXiv:0812.2872 (JCAP 0902:011, 2009, DOI
10.1088/1475-7516/2009/02/011), requires zero vorticity,
constant-proper-time averaging, an informal statistical homogeneity and
isotropy with coherence scale much smaller than the propagation distance,
small initial shear, shear uncorrelated with ray direction, and small
variances; and it integrates in closed form only when `Q = 0` and the
null shear vanishes (Eq. 40). He retains the null-shear term because
"since we do not have a general theoretical argument for the smallness of
the Weyl contribution, we will retain" it (Sec. 3.2), and concedes he
gives no formal definition of statistical homogeneity and isotropy,
saying "it would be worthwhile to have a more precise notion of
statistical homogeneity and isotropy in a general dust spacetime" (Sec.
3.1) [all SOURCED].

**If this fails: 3.** The entire supernova, CMB and BAO comparison runs
through this step.

---

### T13. The model fits the data at least as well as LCDM
**Kind: FIT.** `[SOURCED]`
**Seed: `D8`, tagged `FIT` / empirical. Correct.** See Part 2 for the
field-by-field ledger. The headline, stated here only because it bears on
the weight: the void fraction `f_v0`, which is the single parameter that
generates the whole effect, is **fitted** in every analysis I retrieved,
with best-fit values spanning 0.627 to 0.95 across datasets, and the
observationally measured void filling factor (T1) is reproduced by LCDM
simulations and is not the same quantity. This is O4 and it resolves
against "prediction".

**If this fails: 3.**

---

## The weight distribution - the main result of this run

| Step | Kind | Weight | Secure? |
|---|---|---|---|
| T1 inhomogeneity | observation | 3 | yes |
| T2 scalar commutation | THEOREM | 3 | yes, exact identity |
| T3 metric-averaging non-commutation | INTERPRETATION | **0** | not a theorem; unused |
| T4 Buchert averaged equations | THEOREM given T5 | 3 | yes, conditionally |
| T5 closure required | SCHEME | 3 | **no** |
| T6 two-phase ansatz | SCHEME | 3 | **no**, no sensitivity analysis exists |
| T7 exact solution / tracker | THEOREM + SCHEME | 2 | partly |
| T8 curvature-dominated bare budget | FIT | 3 | **no**, contested (O1 re-aimed) |
| T9 Cosmological Equivalence Principle | POSTULATE | 3 | **no** |
| T10 clock rate physical, 35-38% | POSTULATE + FIT | 3 | **no** (O2) |
| T11 dressed/bare map | SCHEME + INTERPRETATION | 3 | **no** |
| T12 light propagation | SCHEME / POSTULATE | 3 | **no**, conceded unjustified |
| T13 fits the data | FIT | 3 | contested, see Part 2 |

Read plainly: of the thirteen steps, **two are theorems** (T2, and T4
conditional on T5's choices). Everything else that carries weight 3 is a
scheme, a postulate, a fit, or an interpretation. The weight does not sit
on the theorems and it does not sit on one postulate either; it sits on a
**chain of eight non-theorem steps, each of which is individually
sufficient to break the conclusion** (T5, T6, T8, T9, T10, T11, T12,
T13).

That is a different research situation from both of the two the seed
anticipates. The seed asks whether the weight concentrates on one
postulate or is spread across well-established steps. It is neither: it
is spread across many steps, none of which is well established.

Two further points the published presentations do not make clear:

- **The acceleration being explained is tiny in the model.** The dressed
  deceleration parameter changes sign at `f_v ~= 0.5867` and its most
  negative value anywhere is `q ~= -0.043`, at `f_v ~= 0.7736` [SOURCED:
  arXiv:0709.0732, text after Eq. (26)]. For comparison, flat LCDM at
  `Omega_M0 = 0.33` has `q_0 ~= -0.5` `[INFERENCE]`, premise: `q_0 =
  (3/2)Omega_M0 - 1` in flat LCDM, which I did not retrieve in this run
  and tag accordingly. Timescape does not reproduce LCDM's deceleration
  parameter; it reproduces a distance-redshift relation, and the two are
  not the same claim.
- **"Apparent acceleration" in Buchert's own framework is weaker than
  "acceleration".** "Model-independently it is possible to say only that
  the expansion has decelerated less, not that it would have
  accelerated", and "present observations provide strong support for
  apparent acceleration, whereas average acceleration has not been
  established in a model-independent manner" [SOURCED:
  arXiv:1112.5335, Secs. 1.2 and 2.3].
