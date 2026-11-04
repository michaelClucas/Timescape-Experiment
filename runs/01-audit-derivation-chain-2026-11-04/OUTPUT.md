# Part 1 - The chain

The seed chain `D1`-`D8` is wrong in three structural ways, and the
corrections move where the weight sits.

1. The seed's `D2` `THEOREM` tag covers two claims. One is an exact
   identity. The other is nowhere a theorem in the retrieved literature,
   and timescape does not use it.
2. The seed's `D4` ("backreaction can be large enough to matter") is not
   the link timescape needs, and not the thing the Green-Wald dispute is
   about. Wiltshire's own fitted solution has kinematical backreaction at
   `Omega-bar_Q0 = -0.0293 (+0.0033/-0.0036)`, **negative**, with
   `|Omega-bar_Q| <~ 0.042` at all times and no volume acceleration
   (`q-bar > 0`). The bare energy budget is dominated by **average
   negative spatial curvature**, `Omega-bar_k0 = 0.862 (+0.024/-0.032)`
   [SOURCED: arXiv:1311.3787, Table 1 and Sec. 5.3]. Smale & Wiltshire
   say it in one sentence: "the backreaction is relatively small as a
   fraction of the total energy density (<5%)" [SOURCED: arXiv:1009.5855,
   MNRAS 413 (2011) 367, Sec. 2].
3. The seed has no step for light propagation. Getting a
   distance-redshift relation out of a scalar-averaged model is a
   separate step which both Buchert and Wiltshire say in print is not yet
   justified. It carries weight 3.

Steps are renumbered `T1`-`T13`, with the seed mapping given per step.

---

### T1. The late universe is inhomogeneous, and voids occupy the majority of present volume
**Kind: OBSERVATION.** `[SOURCED]`
**Seed: `D1`, tagged `THEOREM` / observational. I disagree with the
tag.** "Theorem" is the wrong word for a measurement. The schema's five
values do not contain a right one, so this step is recorded outside them
rather than mis-tagged; in `OUTPUT.json` it is carried as
`INTERPRETATION` with `kind_disagrees_with_seed: true` and this note.

Statement: voids with effective radii above 10 h^-1 Mpc fill 62% of the
SDSS DR7 sample volume; 1054 voids; median effective radius 17 h^-1 Mpc;
largest just over 30 h^-1 Mpc; density contrast `delta < -0.85` at void
edges [SOURCED: Pan, Vogeley, Hoyle, Choi & Park, arXiv:1103.4156, MNRAS
421 (2012) 926, DOI 10.1111/j.1365-2966.2011.20197.x, abstract].

**The same paper states the void fractions and sizes are similar to those
in LCDM mock catalogues** from an SPH halo model and other LCDM
simulations [SOURCED: same]. So the observed void filling factor is
reproduced by LCDM and is not by itself a discriminating observable.

The number is strongly algorithm-dependent across `VoidFinder`,
`V2/VIDE` and `V2/REVOLVER` applied to the same volume. I retrieved the
paper that reports those comparisons (Douglass, Veyrat & BenZvi,
arXiv:2202.01226, ApJS 265:7, 2023, DOI 10.3847/1538-4365/acabcf) but its
abstract page gives only "the volume fraction of the catalog contained
within voids" with no values, and I did not retrieve its tables. The
spread is therefore `[LEAD]`, not `[SOURCED]`.

Homogeneity scale, which the seed asks about: `R_H = 63.3 +/- 0.7 h^-1
Mpc` from BOSS DR12 CMASS against an LCDM prediction of 62.0 h^-1 Mpc
[SOURCED: Ntelis et al., arXiv:1702.02159, JCAP 06 (2017) 019, DOI
10.1088/1475-7516/2017/06/019, abstract], and `R_H = 70.33 +/- 10.74
Mpc/h` at `z_eff = 0.128` from SDSS blue galaxies [SOURCED: Dias, Avila
& Bernui, arXiv:2310.04594, abstract]. These central values are not
consistent and both are threshold-definition dependent: Ntelis et al.
define `R_H` as where the fractal correlation dimension `D2` reaches 3
within 1%. Timescape does **not** require a larger homogeneity scale than
the standard value; it coarse-grains dust at ~100 h^-1 Mpc, tied to the
statistical homogeneity and BAO scale [SOURCED: arXiv:1106.1693, Class.
Quantum Grav. 28 (2011) 164006, Sec. 4.1].

Strongest objection: none to the measurement.

**If this fails: 3.**

---

### T2. Spatial averaging of scalars does not commute with time evolution
**Kind: THEOREM.** `[SOURCED]`
**Seed: half of `D2`. The `THEOREM` tag is correct for this half and I
keep it.**

For a scalar `Psi` averaged over a comoving domain `D`:

    d/dt <Psi>_D - <dPsi/dt>_D = <Psi.theta>_D - <Psi>_D <theta>_D

An exact identity, labelled a Lemma, at Eq. (9f) [SOURCED: Buchert,
arXiv:gr-qc/9906015, "On average properties of inhomogeneous fluids in
general relativity I: dust cosmologies", Gen. Rel. Grav. 32 (2000) 105,
Sec. 2.2]. Restated at Eq. (7) of the 2008 review, where Buchert adds
that the non-commutativity is "purely kinematical", so it is not
necessarily the nonlinearity of the field equations that causes
backreaction [SOURCED: arXiv:0707.2153, Gen. Rel. Grav. 40 (2008) 467,
DOI 10.1007/s10714-007-0554-8, Sec. 1.3.2].

Strongest objection: none. It is an identity.

**If this fails: 3.** If averaging commuted, the averaged equations would
be Friedmann's and there would be no model.

---

### T3. The Einstein tensor of an averaged metric differs from the average of the Einstein tensors
**Kind: INTERPRETATION, not `THEOREM`.** `[SOURCED]` for the
classification, in the sense that I retrieved the places this is stated
and none states it as a theorem.
**Seed: the other half of `D2`, tagged `THEOREM`. I disagree, and this is
the run's most consequential kind correction.**

Ellis calls it "the basic point", not a theorem or a lemma: "averaging
the geometry and calculating the field equations do not commute" and
"coarse-graining (or averaging) does not commute with calculating the EFE
from the metric tensor" [SOURCED: Ellis, arXiv:1103.2335, Class. Quantum
Grav. 28 (2011) 164001, DOI 10.1088/0264-9381/28/16/164001, Sec. 2.2]. In
the same section Ellis says the averaging operation used to make the
point is not well defined: averaging tensors is "not a well-defined
tensorial operation", and changing coordinates changes the result
[SOURCED: same]. The symbolic version,
`E[<g>] - <E[g]> ~ <Gamma>^2 - <Gamma^2> != 0`, is introduced with
"irrespective of any details of the averaging operation, one notes that";
the `~` are order-of-magnitude and the inequality is argued from term
structure rather than proved [SOURCED: Paranjape, arXiv:0906.3165, PhD
thesis, TIFR 2009, Sec. 1, Eq. (1.3)]. Buchert's 2008 review does **not**
state it [SOURCED, negative: arXiv:0707.2153, searched].

**If this fails: 0.** Timescape does not use it; its formalism rests on
T2, which is exact for scalars. This matters because the seed puts a
`THEOREM` tag on the step that is not a theorem, and because the
literature's habit of motivating backreaction with the metric-averaging
version while deriving everything from the scalar version is precisely
the blur this repository exists to catch.

---

### T4. The Buchert averaged scalar equations, with a kinematical backreaction term
**Kind: THEOREM, conditional on the scheme choices in T5.** `[SOURCED]`
**Seed: `D3`, tagged `SCHEME`. Defensible but imprecise. The equations
are theorems; what is a scheme is the set of conditions they are derived
under, plus the closure that must be added (T5).**

From the Theorem of Sec. 2.2 of arXiv:gr-qc/9906015:

    3 a_D''/a_D + 4 pi G M_D/(V_D0 a_D^3) - Lambda = Q_D                     (10a)
    3 (a_D'/a_D)^2 - 8 pi G M_D/(V_D0 a_D^3) + (1/2)<R>_D - Lambda = -Q_D/2  (10b)
    Q_D := (2/3)<(theta - <theta>_D)^2>_D - 2<sigma^2>_D                     (10c)

with the integrability condition, Corollary 3, Eq. (13a):

    Q_D' + 6(a_D'/a_D)Q_D + <R>_D' + 2(a_D'/a_D)<R>_D = 0

called "a universal relation between the averaged Ricci scalar and the
'backreaction' term" [SOURCED: arXiv:gr-qc/9906015, Sec. 2.2, Theorem
Eqs. (10a)-(10c), Corollary 3 Eqs. (13a)-(13b)]. Same system at Eqs.
(24), (27), (29) of arXiv:0707.2153 and Eqs. (7)-(10) of Buchert &
Rasanen, arXiv:1112.5335, Annu. Rev. Nucl. Part. Sci. 62 (2012) 57, DOI
10.1146/annurev.nucl.012809.104435.

What sign and magnitude `Q_D` is *allowed*, separately from what any model
needs: no fixed sign, since expansion variance enters with `+` and mean
squared shear with `-`. Volume acceleration with `Lambda = 0` requires
`Q_D > 4 pi G <rho>_D`, i.e. expansion fluctuations must supersede shear
fluctuations, and `Q_D` must decay more slowly than the averaged density,
which Buchert says is "not obvious" to satisfy [SOURCED:
arXiv:0707.2153, Sec. 3.2.1, Eq. (63)]. For on-average flat domains the
integrability condition gives `Q_D = Q_D0 a_D^-6` [SOURCED:
arXiv:gr-qc/9906015, Appendix B, Eq. (B.1a)]; the scaling-solution
analysis gives `n = -6, p = -2` as the only solution with `n != p`
[SOURCED: arXiv:0707.2153, Sec. 3.3.5, Eqs. (74)-(76)]. A slower decay
therefore requires nonzero coupling between `Q_D` and `<R>_D`: the
integrability condition is what does the work. Buchert & Rasanen add an
upper bound: "the volume acceleration is bounded from above by the
variance of the expansion rate" [SOURCED: arXiv:1112.5335, Sec. 3.2.1].

Strongest objection: Green & Wald, Sec. 3 footnote 4 of arXiv:1407.8084:
"A further difficulty with the Buchert approach is that the equations are
underdetermined." Buchert says the same himself (T5), so this is a point
of agreement, not a dispute - and that is worth recording, because the
dispute is usually presented as total.

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
which one can describe the effective dynamics. Ellis, independently: the
Buchert approach "can in principle provide an effective acceleration
term" but the closure Ansatz is "not fully justified from the underlying
dynamics" [SOURCED: arXiv:1103.2335, Sec. 2.3.2].

The conditions T4 is derived under, each chosen rather than derived, all
from arXiv:gr-qc/9906015: irrotational dust (Sec. 2.1, "irrotational
fluid motion with the simplest matter model 'dust'"); a flow-orthogonal
constant-proper-time foliation (Sec. 2.1, "We choose a flow-orthogonal
coordinate system"); scalars only (Sec. 2.2 footnote 3, "we do not
attempt to average the spacetime geometry as a whole"); and a given,
time-evolving domain, the averaging "functionally depend[ing] on content,
shape and position of the spatial domain of averaging" (Sec. 2.2 footnote
3). Buchert & Rasanen state the hypersurface dependence flatly: "The
result does, however, depend on the hypersurface on which the average is
taken" [SOURCED: arXiv:1112.5335, Sec. 2.2].

**If this fails: 3.** There is no quantitative model without a closure,
and every number in timescape comes from a particular one (T6, T7).

---

### T6. A two-phase ansatz: spatially flat walls bounded by finite-infinity surfaces, negatively curved voids, one void curvature scale
**Kind: SCHEME.** `[SOURCED]`
**Seed: `D5`, tagged `SCHEME`. Correct; I keep the tag and add what the
seed asks for, namely what fixes the split.**

Finite infinity is the boundary of a compact domain within which the
average expansion vanishes, with `theta > 0` outside [SOURCED:
arXiv:gr-qc/0702082, New J. Phys. 9 (2007) 377, Sec. 3.2, Eq. (11);
restated arXiv:1106.1693, Eq. (22), Fig. 1]. The split is
`a-bar^3 = f_wi a_w^3 + f_vi a_v^3`, `f_wi + f_vi = 1`, with
`f_v(t) = f_vi a_v^3 / a-bar^3` and `f_vi` the initial void fraction at
last scattering [SOURCED: arXiv:gr-qc/0702082, Sec. 5.1, Eq. (22)]. Walls
are *assumed* spatially flat: "The local average geometry at the boundary
of a finite infinity region is assumed to be spatially flat" [SOURCED:
arXiv:0709.0732, Phys. Rev. Lett. 99 (2007) 251101, text at Eq. (1)].
Voids are negatively curved with `k_v < 0`.

What fixes two phases rather than a continuum of densities: nothing, by
Wiltshire's own account. He asserts the structure, says "a single
negative curvature scale is assumed as a simplification", and notes one
"could potentially use different curvature scales" for voids and
minivoids [SOURCED: arXiv:1106.1693, Sec. 4.2]. **I found no quantitative
sensitivity analysis of the result to the two-phase choice in anything
retrieved.** He also concedes "There is an intrinsic ambiguity in
assigning the shape to the boundary" of finite infinity [SOURCED:
arXiv:gr-qc/0702082, Sec. 3.2]. The construction further assumes no
backreaction *within* walls and *within* voids separately [SOURCED:
arXiv:0909.0749, Phys. Rev. D 80 (2009) 123512, Sec. II].

Strongest objection: Green & Wald, Sec. 3 of arXiv:1407.8084, that large
averaged scalar curvature produced this way is an artifact of a poor
metric approximation - "these apparent backreaction effects are entirely
spurious" - illustrated with a Minkowski example whose averaged scalar
curvature "is enormous for sufficiently large N", and a
two-disconnected-universes example of which they write "Obviously, this
acceleration is not a physical effect" [SOURCED: arXiv:1407.8084, Class.
Quantum Grav. 31 (2014) 234003, Sec. 3, at Eq. (16)]. **This, not the
traceless-stress theorem, is the Green-Wald line of attack that reaches
timescape's mechanism.** See O1.

**If this fails: 3.**

---

### T7. There is an exact general solution of the two-scale averaged equations, and all phenomenology uses a special-case tracker attractor
**Kind: THEOREM of the averaged equations under T6, plus SCHEME for the
restriction to the tracker.** `[SOURCED]`
**Seed: absent. The seed does not distinguish "exact solution" from
"solution actually used", and the PRL title invites the confusion.**

What is exact: a general exact solution of the two-scale **Buchert**
equations (5) and (6), not of the Einstein field equations. The paper says
it will "derive the general exact solution to the Buchert equations", and
notes Buchert's scheme "does not average all of the Einstein equations"
[SOURCED: arXiv:0709.0732, Introduction]. The general solution is Eqs.
(11) and (13); Eq. (13) is transcendental, so `a-bar(t)` and `f_v(t)` are
only implicit. Matter-dominated epoch only: "Here we restrict attention
to the matter-dominated epoch."

What is used: all observational work runs on a **late-time tracker**
special case (`eps_i = 0`), "a late-time tracker solution, an attractor",
with `h_r = 2/3` exactly and `f_v(t)` from Eq. (19) [SOURCED:
arXiv:0709.0732, at Eqs. (18)-(19)]. The general solution approaches it to
within 1% by `z ~ 37`; tracker accuracy against the full solution is
quoted as 0.1% in `H_0`, 1% in `f_v0`, 3% in `Omega_M0` [SOURCED:
arXiv:gr-qc/0702082, footnote 65].

Separately, and against the title: the averaged metrics are "not exact
solutions of the Einstein equations" [SOURCED: arXiv:1009.5855, Sec. 2],
and the spherically symmetric dressed metric "is not a LTB solution"
because it is not an exact solution of Einstein's equations [SOURCED:
arXiv:1311.3787, Sec. 5.1].

**If this fails: 2.** The qualitative claim survives; every number does
not.

---

### T8. In the fitted solution the bare budget is curvature-dominated, backreaction is small and negative, and there is no volume acceleration
**Kind: FIT, with the structure a consequence of T4-T7.** `[SOURCED]`
**Seed: `D4`, "Backreaction can be large enough to matter", tagged
`INTERPRETATION` / disputed. I disagree. Timescape does not claim large
backreaction, and says so.**

From Wiltshire's own review, Table 1: `f_v0 = 0.695 (+0.041/-0.051)`,
`Omega-bar_M0 = 0.167 (+0.036/-0.037)`,
`Omega-bar_k0 = 0.862 (+0.024/-0.032)`,
`Omega-bar_Q0 = -0.0293 (+0.0033/-0.0036)`,
`Omega-bar_R0 = (5.00 +0.56/-0.48) x 10^-5`, dressed
`Omega_M0 = 0.41 (+0.06/-0.05)`, dressed `H_0 = 61.7 +/- 3.0`, bare
`H-bar_0 = 50.1 +/- 1.7` km/s/Mpc [SOURCED: arXiv:1311.3787, Table 1].
Sec. 5.3: "|Omega-bar_Q| <~ 0.042 at all times which means that the
backreaction is never large enough to make q-bar negative" [SOURCED:
same]. In the 2009 paper: the backreaction term "is at most of order
4.2%", `Omega-bar_Q` is negative, it is "never large enough relative to"
`Omega-bar_M` to give volume average cosmic acceleration, and the bare
deceleration parameter `q-bar = (1/2) Omega-bar_M + 2 Omega-bar_Q` "is
positive" [SOURCED: arXiv:0909.0749, Secs. II.3, II.4, Eqs. (18)-(21)].
And in plain words: "the backreaction is relatively small as a fraction
of the total energy density (<5%)" [SOURCED: arXiv:1009.5855, Sec. 2].

`Omega-bar_k0 / |Omega-bar_Q0| = 29`. The apparent acceleration in
timescape is not produced by kinematical backreaction. It is produced by
large average negative spatial curvature plus the lapse (T9-T11)
`[INFERENCE]`; premises: the bare budget above, `q-bar > 0`, and the
dressed-parameter map being the only remaining place a sign change can
come from.

**If this fails: 3** - but note what "fails" means. If the fitted
`Omega-bar_k0` is wrong, timescape fails. If `Omega-bar_Q` turned out
large, timescape would not need it.

Strongest objection: O1, re-aimed. Green & Wald's theorems (effective
stress-energy traceless, satisfies the weak energy condition, "must be of
the form of a P=rho/3 fluid, and therefore cannot mimic dark energy"
[SOURCED: arXiv:1407.8084, Sec. 2, Theorems 1 and 2, Eqs. (7)-(8)]) are
about `Q`-type backreaction and do not engage this step. Their Sec. 3
spurious-curvature argument does. They restrict to `k = 0` and make no
statement that average spatial curvature must stay near FLRW [SOURCED,
negative: arXiv:1407.8084, Sec. 4.1 after Eq. (21)].

---

### T9. The Cosmological Equivalence Principle
**Kind: POSTULATE.** `[SOURCED]`, and Wiltshire settles it himself.
**Seed: `D6`, tagged `POSTULATE`. Correct. I confirm it with his own
words because the seed asks whether it is claimed to follow from GR, and
the answer is a clear no.**

Statement, Sec. II.1 of arXiv:0809.1183, Phys. Rev. D 78 (2008) 084032,
around Eq. (1): "At any event, always and everywhere, it is possible to
choose a suitably defined spacetime neighbourhood" / "in which average
motions (timelike and null) can be described by geodesics in a geometry
which is Minkowski" up to a time-dependent conformal transformation, with
Eq. (1) `ds^2 = a^2(eta)[-d eta^2 + dr^2 + r^2 d Omega^2]` [SOURCED]. The
neighbourhood is named a "cosmological inertial region" in later work
[SOURCED: arXiv:1106.1693, Sec. 3.3.1; arXiv:1311.3787, Sec. 4.1].

Status, in his own words, all from arXiv:0809.1183: abstract, "The strong
equivalence principle is extended in application to averaged dynamical
fields in cosmology"; Sec. I, "by proposing an extension of the SEP to
cosmology"; Sec. II.1, "the CEP thus represents a refinement in the
definition of inertial frames"; Sec. VII, "I have extended the strong
equivalence principle to account for the average effect of the density of
matter". The word "postulate" does not appear. The sentence that settles
it as content additional to GR is in a later paper: there is "a further
principle of relativity that is lacking in general relativity with the
SEP alone", and it "would reduce to the standard SEP if" the conformal
factor were constant [SOURCED: arXiv:1106.1693, Sec. 3.3.1].

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
the CEP was introduced in 2008 to underwrite a 2007 model `[INFERENCE]`;
premises: the publication dates and the absence of the term from the
retrieved portion of the 2007 paper. This should be checked against the
remainder of that paper before being relied on.

Is there a laboratory or solar-system regime where it is checkable? The
implied present relative deceleration is
`alpha_0 = 8.6 (+1.9/-1.5) x 10^-11 m/s^2`, close to the MOND scale
`8.1 (+3.0/-2.0) x 10^-11 m/s^2` at the same `H_0` [SOURCED:
arXiv:1311.3787, Sec. 5.2]; an earlier value is
`alpha_0 ~ 6.7 x 10^-11 m/s^2` [SOURCED: arXiv:0809.1183, Sec. V.1, Eq.
(29)]. Wiltshire says the coincidence "may be purely coincidental", that
"no firm conclusions should be drawn until a compelling theoretical case
is assembled", and that "no detailed quantitative comparisons can be made
until the transition zone around finite infinity is more directly
modelled" [SOURCED: arXiv:0809.1183, Sec. V.2]. A later paper applies the
quasilocal approach to galactic dynamics [SOURCED: Galoppo, Re &
Wiltshire, arXiv:2408.00358, Class. Quantum Grav. 42 (2025) 135004], which
I did not retrieve in full. See Part 6.

**If this fails: 3.** This is where the model lives or dies, and the seed
is right about that.

---

### T10. The relative lapse between wall and volume-average clocks is physical, and cumulatively of order 35-38% today
**Kind: POSTULATE for the existence, FIT for the magnitude.** `[SOURCED]`
**Seed: folded into `D6`. Splitting existence from magnitude is
necessary, because the magnitude is not an independent prediction.**

The relative lapse is `gamma-bar`, with
`gamma-bar_w = 1 + (1 - h_r) f_v / h_r`, `h_r = H_w/H_v < 1` [SOURCED:
arXiv:0709.0732, Eq. (7)]. On the tracker `h_r = 2/3`, so

    gamma-bar = 1 + f_v / 2

[SOURCED: arXiv:0709.0732, text after Eq. (19); equivalently
arXiv:0909.0749, Appendix B, Eq. (77)]. There is a ceiling: `gamma < 3/2`,
i.e. 50% [SOURCED: arXiv:gr-qc/0702082, abstract and Sec. 4.2].

Magnitudes retrieved: "accumulated relative difference of 38%" [SOURCED:
arXiv:0809.1183, abstract]; "can typically grow to the order of 38% by
the present epoch" [SOURCED: arXiv:1009.5855, Sec. 2]; "can cumulatively
lead to present epoch clock rate differences of order 35%" [SOURCED:
arXiv:1410.3470, Phys. Rev. D 91 (2015) 063519, Sec. I]; "present epoch
large variation of clock rates, of order 35%" [SOURCED: arXiv:1311.3787,
Sec. 5.2]; `gamma-bar = 1.38 (+0.06/-0.05)` [SOURCED: arXiv:0809.1183,
Sec. III.1]; `gamma-bar_0 = 1.348 (+0.021/-0.025)` [SOURCED:
arXiv:1306.3208, Class. Quantum Grav. 30 (2013) 175006, Table 1]; and for
a void density contrast `delta = -0.9` to `-0.95`, `gamma = 1.42` to
`1.46`, with "These clock rate variances of 42%-46% are large, and
counter intuitive" [SOURCED: arXiv:0809.1183, Sec. III.1, Eqs. (11)-(12)].

**No uncertainty is attached to the 35% or 38% figure in any paper I
retrieved.** And because `gamma-bar = 1 + f_v/2` on the tracker, the
figure is an algebraic restatement of the fitted `f_v0`: 38% tracks
`f_v0 ~ 0.76`, 35% tracks `f_v0 ~ 0.695`. The drift from 38% to 35%
across papers follows the drift in the fitted `f_v0` and is not flagged
as a change in any paper I retrieved. The headline number is therefore a
`FIT`, not a prediction `[INFERENCE]`; premises: the tracker relation and
the fitted `f_v0` values in T13 and Part 2.

Same mechanism, further consequences: the volume-average present CMB
temperature is "up to about 35% cooler" than the wall value,
`T-bar = gamma-bar^-1 T` [SOURCED: arXiv:1410.3470, Sec. III.2, Eq. (20)];
and the age of the universe is observer-dependent, `tau_w0 = 14.2 +/- 0.5`
Gyr for a wall observer against `t_0 = 17.5 +/- 0.6` Gyr for a
volume-average observer [SOURCED: arXiv:1306.3208, Table 1].

Strongest objection: O2. The most damaging statement on the gauge
question is Wiltshire's own: "The argument above relies on it being
possible to choose a locally uniform Hubble flow gauge" and "Such a gauge
can be maintained outside finite infinity regions, but not within them"
[SOURCED: arXiv:0809.1183, Sec. III.1] - that is, not in the regions
where observers actually are.

**If this fails: 3.** Independently of T8.

---

### T11. Dressed versus bare parameters
**Kind: SCHEME plus INTERPRETATION.** `[SOURCED]`
**Seed: `D7`, tagged `INTERPRETATION` + `SCHEME`. Correct; I keep it.**

Dressed Hubble `H = gamma-bar H-bar - d(gamma-bar)/dt` [SOURCED:
arXiv:0709.0732, Eq. (8); arXiv:0909.0749, Eq. (27)]; dressed matter
density `Omega_M = gamma-bar^3 Omega-bar_M` [SOURCED: arXiv:0709.0732,
after Eq. (7); arXiv:0909.0749, Eq. (26)]; dressed
`H_0 = (4 f_v0^2 + f_v0 + 4) H-bar_0 / [2(2 + f_v0)]` [SOURCED:
arXiv:0709.0732, Eq. (25)].

The dressed parameters obey **no** sum rule: they "do not satisfy a simple
relation analogous to" the bare one [SOURCED: arXiv:0709.0732], and
dressed density parameters do not sum to one, so they are "just a
convenient parametrization" [SOURCED: arXiv:1410.3470, Sec. III.1].

The lapse-rate term is not a small correction: it reduces the inferred
Hubble parameter by about `-5.8` km/s/Mpc, taking
`H-bar_{tau,0} = 67.5 (+3.4/-3.5)` to dressed `H_0 = 61.7 +/- 3.0`
[SOURCED: arXiv:1812.01586, A&A 624 (2019) A12, DOI
10.1051/0004-6361/201834833, Sec. 2].

**If this fails: 3.**

---

### T12. The dressed effective metric correctly gives luminosity distances along the observer's past light cone
**Kind: SCHEME / POSTULATE, acknowledged as not yet justified.**
`[SOURCED]`
**Seed: absent entirely. This is a weight-3 step the seed omits, and both
Buchert and Wiltshire say in print that it is unjustified.**

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
distance-redshift relation from averaged quantities. His main result, Eq.
(38) of arXiv:0812.2872 (JCAP 0902:011, 2009, DOI
10.1088/1475-7516/2009/02/011), requires zero vorticity,
constant-proper-time averaging, an informal statistical homogeneity and
isotropy with coherence scale much smaller than the propagation distance,
small initial shear, shear uncorrelated with ray direction, and small
variances; and it integrates in closed form only when `Q = 0` and the
null shear vanishes (Eq. 40). He retains the null-shear term because
"since we do not have a general theoretical argument for the smallness of
the Weyl contribution, we will retain" it (Sec. 3.2), and concedes he
gives no formal definition of statistical homogeneity and isotropy: "it
would be worthwhile to have a more precise notion of statistical
homogeneity and isotropy in a general dust spacetime" (Sec. 3.1) [all
SOURCED].

**If this fails: 3.** The entire supernova, CMB and BAO comparison runs
through this step.

---

### T13. The model fits the data at least as well as LCDM
**Kind: FIT.** `[SOURCED]`
**Seed: `D8`, tagged `FIT` / empirical. Correct.** Part 2 has the
field-by-field ledger. Stated here only because it bears on the weight:
`f_v0`, the single parameter that generates the whole effect, is **fitted**
in every analysis retrieved, with values 0.550, 0.557, 0.627, 0.628,
0.665, 0.675, 0.695, 0.737, 0.76, 0.778, 0.791, and 0.72-0.95 across the
Smale & Wiltshire datasets - a spread far exceeding the quoted
uncertainties.

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

Plainly: of thirteen steps, **two are theorems** - T2, and T4 conditional
on T5's choices. Everything else carrying weight 3 is a scheme, a
postulate, a fit, or an interpretation. The weight does not sit on the
theorems, and it does not sit on one postulate either. It sits on a
**chain of eight non-theorem steps, each individually sufficient to break
the conclusion**: T5, T6, T8, T9, T10, T11, T12, T13.

That is neither of the two situations the seed anticipates. The seed asks
whether the weight concentrates on one postulate or is spread across
well-established steps. It is spread across many steps, none of which is
well established. The practical consequence is that the model is harder
to refute than a one-postulate model and harder to confirm than a
theorem-chain model: no single measurement reaches it, because any failure
can be absorbed by a different closure (T5), a finer phase decomposition
(T6), or a better light-propagation treatment (T12), none of which is
pinned down.

Two further points the published presentations do not make clear:

- **The acceleration being explained is small in the model.** The dressed
  deceleration parameter changes sign at `f_v ~= 0.5867` and its most
  negative value anywhere is `q ~= -0.043`, at `f_v ~= 0.7736` [SOURCED:
  arXiv:0709.0732, text after Eq. (26)], consistent with the fitted
  `q_0 = -0.043 (+0.004/-0.000)` [SOURCED: arXiv:1706.07236, MNRAS 472
  (2017) 835, abstract]. Flat LCDM at `Omega_M0 = 0.33` has
  `q_0 ~= -0.5` `[INFERENCE]`, premise: `q_0 = (3/2)Omega_M0 - 1` in flat
  LCDM, which I did not retrieve in this run. Timescape does not
  reproduce LCDM's deceleration parameter; it reproduces a
  distance-redshift relation, and those are different claims.
- **"Apparent acceleration" in Buchert's own framework is weaker than
  "acceleration".** "Model-independently it is possible to say only that
  the expansion has decelerated less, not that it would have
  accelerated", and "present observations provide strong support for
  apparent acceleration, whereas average acceleration has not been
  established in a model-independent manner" [SOURCED: arXiv:1112.5335,
  Secs. 1.2, 2.3].

---

# Part 2 - The ledger

Full entries are in `LEDGER.md`. This part states the findings and the
fields that could not be filled.

## The one fact that governs every supernova entry

Pantheon+ generates its bias corrections from flat-LCDM simulations and
declines to carry a systematic for that choice. Verbatim: "The
simulations used for bias corrections for all surveys are performed in
LCDM (w = -1.0, Omega_M = 0.3, Omega_Lambda = 0.7) with the SALT2-B22
model", and "the sensitivity of the bias corrections to the input
cosmology is relatively weak ... We therefore do not include this as an
additional systematic" [SOURCED: Brout et al., arXiv:2202.04077, ApJ 938
(2022) 110, DOI 10.3847/1538-4357/ac8e04, Sec. III.3.1]. DES states the
same risk more sharply: "The bias correction step thus holds the biggest
potential for harbouring cosmological assumptions that could influence
the cosmological results" [SOURCED: Camilleri et al., arXiv:2406.05048,
Sec. 2.3.2].

The timescape analyses respond by discarding those corrections: "are not
accounted for, as they introduce a bias towards the standard cosmology
based on the FLRW metric" [SOURCED: Lane, Seifert, Ridden-Harper &
Wiltshire, arXiv:2311.01438, MNRAS 536 (2025) 1752, DOI
10.1093/mnras/stae2437, Sec. 2]. They also decline Scolnic et al.'s
`alpha`, `beta` because those were fitted in `wCDM`: "we do not use these
values" [SOURCED: same].

**So the circularity objection O3 is real and is acknowledged on both
sides, and no analysis retrieved has resolved it.** The timescape
analyses avoid inheriting an LCDM calibration and thereby inherit
uncorrected selection bias instead: "Without the standard corrections,
biases such as the Malmquist bias are present in our analysis" [SOURCED:
arXiv:2311.01438, Sec. 5]. DES avoids selection bias and inherits a
flat-LCDM reference cosmology whose effect it validates only *within*
FLRW, with 25 realisations in flat `wCDM` analysed under six reference
cosmologies [SOURCED: arXiv:2406.05048, Sec. 4]. **No published analysis
does both.** That is the single most consequential technical finding of
this run, and it is checkable.

## Supernovae - what the comparison statistics actually say

Every value below is `ln B` with positive favouring timescape unless
stated.

| Analysis | Data | Cut | k (TS / LCDM) | Statistic | Value |
|---|---|---|---|---|---|
| Smale & Wiltshire 2011 | Union2 | z>=0.033, 457 SNe | not stated / not stated | ln B | **-3.46** (LCDM) |
| Smale & Wiltshire 2011 | CSP | z>=0.033, 43 | not stated | ln B | **-4.23** (LCDM) |
| Smale & Wiltshire 2011 | MLCS31 | z>=0.033, 229 | not stated | ln B | **+1.09** (TS) |
| Smale & Wiltshire 2011 | SALT2 | z>=0.033, 235 | not stated | ln B | **-1.55** (LCDM) |
| Kwan, Francis & Lewis 2009 | Union | none | not stated | ln B | **-1.38** (LCDM) |
| Kwan, Francis & Lewis 2009 | Constitution | none | not stated | ln B | **-1.469** (LCDM) |
| Dam et al. 2017 | JLA | z_min=0.033 | **9 / 9** | ln B | **+0.085 +/- 0.01** |
| Dam et al. 2017 | JLA | z_min=0.024 | **9 / 9** | ln B | **+0.600 +/- 0.007** |
| Lane et al. 2025 | P+1690 | z_min=0 | 9 sampled, 1 cosmological each | ln B | **+2.93** |
| Lane et al. 2025 | P+1690 | z_min=0.04 | same | ln B | **-2.82** (LCDM) |
| Lane et al. 2025 | P+580 | z_min=0.04 | same | ln B | **+0.98** |
| Lane et al. 2025 | P+580 | bootstrapped | same | ln B | **+1.02 +/- 0.04** |
| Lane et al. 2025 | P+1690 | z_min>0.075 | same | ln B | **~0** |
| Lane et al. 2025 | P+1690 | integrated | same | - | "marginally favouring LCDM", **no number given** |
| Seifert et al. 2025 | P+1690 | all | **cannot be established** | ln B | **>5** |
| Seifert et al. 2025 | P+1690 | z_min>=0.075 | **cannot be established** | ln B | **>1** |
| DES 2024 | DES-SN5YR cut | z_min=0.033 | **1 / 1** | half-Delta-AIC | **-1.7** (TS, weak) |
| DES 2024 | + BAO-theta*-perp | z_min=0.033 | **1 / 1** | half-Delta-AIC | **+6.3** (LCDM) |

Locators: arXiv:1009.5855, MNRAS 413 (2011) 367, Table 6; Kwan, Francis &
Lewis, arXiv:0902.4249, MNRAS Lett. 399 (2009) L6; arXiv:1706.07236,
MNRAS 472 (2017) 835, Sec. 4.1.1 and Table 3; arXiv:2311.01438, MNRAS 536
(2025) 1752, Secs. 4.7.1, 4.7.3, Fig. 11; Seifert, Lane, Galoppo,
Ridden-Harper & Wiltshire, arXiv:2412.15143, MNRAS Lett. 537 (2025) L55,
DOI 10.1093/mnrasl/slae112, Sec. 3 and Figs. 1-2; arXiv:2406.05048, MNRAS
533 (2024) 2615, DOI 10.1093/mnras/stae1988, Tables 5 and 7, Sec. 7.8.
The DES sign convention is stated verbatim: "A more negative half-Delta-AIC
and Delta ln S value indicates a stronger preference over Flat-LCDM."

Four things follow, and none of them appears in any summary of this
literature.

1. **The sign of the supernova preference is not stable.** It flips with
   the light-curve reduction method (MLCS2k2 versus SALT/SALT2 in Smale &
   Wiltshire), with the redshift cut (+2.93 to -2.82 in Lane et al. on
   the *same* sample), with the subsample (P+580 versus P+1690 at the
   same cut), and with the addition of BAO (DES). Reporting any one of
   these as the result is a selection.
2. **The headline `ln B > 5` is not comparable with the others and its
   parameter count cannot be established.** Seifert et al. say "nine
   parameters" in one place and "only requiring five parameters" in
   another, and Table 1 lists eight rows, unreconciled [SOURCED:
   arXiv:2412.15143, Secs. 2-3, Table 1]. Under
   `docs/claim-ledger.md` rule C5 the comparison statistic is therefore
   recorded as **uninterpretable**. The authors attribute the jump in
   evidence relative to Lane et al. to "the lifting of the Gaussian
   assumption" on the `x1` and `c` populations [SOURCED: same] - a change
   in the supernova population model, not in the cosmology. The same
   paper's own characterisation is "the evidence in favour of timescape
   remains small but modest" [SOURCED: same, Sec. 3], which does not
   match the abstract's "very strong evidence".
3. **The only two analyses with matched, stated parameter counts both
   return "indistinguishable".** Dam et al. 2017, k = 9 on both sides,
   `ln B = 0.085 +/- 0.01` at the cut they headline. DES 2024, k = 1 on
   both sides, half-Delta-AIC = -1.7 on supernovae alone. Neither is
   evidence for timescape on the interpretation scales the papers cite.
4. **Light-curve parameters move at the homogeneity scale.** "there is a
   marked 30% jump in c_0 as z_min is varied from 0.01 up to z ~= 0.033",
   and "there is clear evidence for some systematic effect at precisely
   the scale where we expect it" [SOURCED: arXiv:1706.07236, Sec. 4.1.1].
   Lane et al. report that `beta` "does not converge for varying sample
   size" [SOURCED: arXiv:2311.01438, Sec. 5]. Whether this is the
   timescape signal or an uncorrected selection effect is exactly what
   the missing analysis in the box above would settle.

## CMB

Two papers, both at least eleven years old, and no Planck 2015 or 2018
timescape fit exists [SOURCED, negative: https://arxiv.org/a/wiltshire_d_1
and an arXiv API search on `abs:"timescape"`].

Duley, Nazer & Wiltshire 2013 fit **two summary numbers**:
`theta* = 0.0104139` at 2% tolerance and a 98.88 h^-1 Mpc effective
comoving drag scale at 6% tolerance, the looser tolerance justified
because timescape "may require recalibrating the baryonic and nonbaryonic
dark matter proportions". They say what this is: "not statistical
constraints of the sort that could be obtained by fully fitting the
Planck data directly" [SOURCED: arXiv:1306.3208, Class. Quantum Grav. 30
(2013) 175006, DOI 10.1088/0264-9381/30/17/175006, Sec. 3.2]. **No
chi-squared, no likelihood, no parameter count, no degrees of freedom.**
The paper never names the Planck release.

Nazer & Wiltshire 2015 fit the full Planck TT spectrum over
`50 <= l <= 2500` with the CamSpec likelihood and 14 nuisance parameters -
but the spectrum is not computed from timescape perturbation theory. A
matched FLRW model is constructed and run through a standard Boltzmann
code: "We fit the parameters of each matched FLRW universe by computing
its CMB power spectrum with the CLASS Boltzmann code" [SOURCED:
arXiv:1410.3470, Sec. IV]. The data are Planck **2013** (A&A 571, A15),
not 2015 or 2018. Results, by matching prescription: `-ln L = 3925.16`
(method A), `3897.90` (W, k=0), `3896.47` (W, k!=0), against LCDM
`3895.5`-`3896.9` over the same range, with method A "only 0.7% larger".
`f_v0 = 0.628` (A), `0.550` (W k=0), `0.557` (W k!=0) - a 12% spread
across prescriptions that are all supposed to describe the same universe.
Systematics are stated at 8-13% against 1-2% statistical [SOURCED: same,
Sec. V]. **`Omega_b h^2` is not published for timescape in either paper.**

Severity, honestly: this is weaker than a passed severe test and stronger
than nothing. The fit is to a real power spectrum but through an FLRW
proxy, with backreaction neglected before decoupling ("since the effects
of backreaction are neglected in the early Universe", Sec. III.2), the
late ISW effect uncomputed ("has not yet been computed for the timescape
scenario", Sec. VI), and conclusions that "may change if backreaction
terms are also included" [SOURCED: same, abstract and Secs. III.2, VI].

The 2013 lithium-7 resolution claim is **withdrawn** in 2015: "we cannot
make the claim that the timescape model solves the primordial lithium
abundance anomaly", which the authors call "our most important result"
[SOURCED: arXiv:1410.3470, Secs. V, VI]. The withdrawal follows the
upward revision of `eta_Bgamma` from `(5.1 +/- 0.5) x 10^-10`
[arXiv:1306.3208, Sec. 3.2] to `6.465`-`6.489 x 10^-10` [arXiv:1410.3470,
Table 2].

## BAO

**No timescape analysis has ever constrained timescape parameters from
BAO distance data.** The one dedicated paper uses timescape only as a
fiducial with `Omega_M0 = 0.3` **fixed** - "equal to that of the LCDM
matter density parameter", and "we aim to demonstrate feasibility of the
method" - and tests only Alcock-Paczynski isotropy, which is consistent
with zero distortion under both fiducials [SOURCED: Heinesen, Blake, Li &
Wiltshire, arXiv:1811.11963, JCAP 03 (2019) 003, DOI
10.1088/1475-7516/2019/03/003, Secs. 1, 2.4, 4.2, 6]. It assumes no
sound-horizon calibration: "we do not assume any calibration of r_BAO in
this study" (Sec. 4.1 fn. 11). Under the timescape fiducial the BOSS DR12
CMASS scale comes out at `95.4 +/- 1.6` Mpc/h against `102.6 +/- 1.5`
Mpc/h under LCDM (Tables 1-2) - a 7% shift, which is the size of the
effect that would have to be calibrated, not a measurement of it.

The earlier `f_v0 = 0.76 (+0.12/-0.09)` fit did use "the effective
comoving baryon acoustic oscillation scale in galaxy clustering" as one
of three tests [SOURCED: Leith, Ng & Wiltshire, arXiv:0709.2535,
Astrophys. J. 672 (2008) L91, DOI 10.1086/527034, abstract], but that is
a single summary scale, not a BAO likelihood.

On whether the measured BAO scale is model-independent, the measurement
papers say it is not. DESI DR2: the fiducial cosmology "is used to convert
redshifts to distances" and to define the power-spectrum template, scaled
to Planck best-fit values [SOURCED: arXiv:2503.14738, Phys. Rev. D 112
(2025) 083515, Sec. III.1, Eq. 2, Fig. 1 caption]. Heinesen et al.: "BAO
analysis is usually performed assuming a fiducial spatially flat LCDM
cosmology", and their own empirical procedure's "Systematic errors ... will
inevitably be larger, and dependent on the cosmological model" (Secs. 1,
4.2 fn. 12). DES expresses `BAO-theta*` as ratios so `r_d` cancels and
says the cosmological dependence of `r*/r_d` "may be neglected" - an
approximation, not a model-independence claim [SOURCED: arXiv:2406.05048,
Sec. 2.4].

## Local Hubble flow variance

There **is** a prior quantitative prediction, and it is 17-22% present
local Hubble-flow variance, with a peak local `H_0` near dominant voids
of ~72 km/s/Mpc at 30 h^-1 Mpc, dressed `H_0 = 61.7 (+1.2/-1.1)`, bare
`H_0 = 48.2 (+2.0/-2.4)` [SOURCED: Wiltshire, arXiv:0912.5236, AIP Conf.
Proc. 1241 (2010) 1182, Sec. 2]. The later review gives a local minimum
`50.1 +/- 1.7` toward Virgo and a local maximum `75.2 (+2.0/-2.6)` across
local voids, with an asymptotic `H_0` expected on 70-100 h^-1 Mpc scales
[SOURCED: arXiv:1311.3787, Secs. 5.3, 7].

What was measured by the proposing group: the COMPOSITE sample, 4534
distances; `H_0` closer to its asymptotic value in the Local Group frame;
correlation coefficient `-0.92` between the LG-frame Hubble-variation map
and the residual CMB temperature dipole; and "a foreground nonkinematic
anisotropy in the distance-redshift relation of 0.5% on scales up to 65
h^-1 Mpc", with "decisive Bayesian evidence (ln B >> 5)" for a
scale-dependent fit [SOURCED: Wiltshire, Smale, Mattsson & Watkins,
arXiv:1201.5371, Phys. Rev. D 88 (2013) 083529, DOI
10.1103/PhysRevD.88.083529, abstract, Secs. II-V, Table 3]. The 0.5%
figure is derived inside that paper in Sec. V.2 from the Local Group
residual CMB dipole; it is a result, not the prior prediction. The
follow-up simulates a quasispherical **Szekeres** solution, not timescape,
and timescape appears there only in Sec. 2.2 and a footnote [SOURCED:
Bolejko, Nazer & Wiltshire, arXiv:1512.07364, JCAP 06 (2016) 035].

Independent measurement: "the Hubble flow becomes statistically uniform
at around 70-100 Mpc" and the results "are in good agreement with the
expected Hubble variance in the standard model across cosmic scales of
20-150 Mpc" [SOURCED: Shao & Bengaly, arXiv:2510.19945, Phys. Rev. D 113
(2026) 123510, DOI 10.1103/g5zv-xfrt, abstract]. Timescape is not
mentioned there. Whether 17-22% variance is consistent with that result
is **not** established in anything I retrieved, because the two are not
stated as the same quantity on the same scales. `[UNKNOWN]`; what would
settle it is a reanalysis of the Shao & Bengaly data against the
arXiv:0912.5236 Sec. 2 prediction, which nobody has done.

## Hubble tension

**No timescape paper performs a joint early-versus-late `H_0` analysis.**
The CMB-matched value is `H_0 = 60.984 / 60.997 (+0.791/-0.733)` km/s/Mpc
[SOURCED: arXiv:1410.3470, Table 2], which is **below** Planck 2018's
`67.4 +/- 0.5` [SOURCED: Planck Collaboration, arXiv:1807.06209, A&A 641
(2020) A6], not between Planck and the distance ladder. The supernova
papers fix `H_0` as a nuisance parameter and report none [SOURCED:
arXiv:2412.15143, Sec. 3]. The claim that the model "potentially resolves
the Hubble tension" appears only in a Gravity Research Foundation essay
with no journal reference, no numbers and no data fit [SOURCED:
Wiltshire, arXiv:2404.02129]. Timescape addressing the Hubble tension is
therefore an assertion, not a derived or fitted result.

One discrepancy to flag. Galoppo & Mourier adopt `f_v0 = 0.737` together
with `H_0 = 73.03` km/s/Mpc, attributed to "the best-fit results from"
Seifert et al. 2025 [SOURCED: arXiv:2511.17160, JCAP 02 (2026) 066, DOI
10.1088/1475-7516/2026/02/066, Sec. 5.1.1, Fig. 1]. Seifert et al. fix
`H_0` as a nuisance parameter and report no `H_0`. 73.03 is the
distance-ladder value. This looks like a misattribution `[INFERENCE]`;
premises: the two statements above. It should be checked against the
remainder of the Seifert et al. text before being asserted, and it matters
because a timescape prediction of `H_0 ~ 61` and a timescape calculation
run at `H_0 = 73` cannot both be right.

## Structure growth and BBN

**`unverified-in-this-run`, bordering on `untested`.** No published
timescape `sigma_8` or `S_8` exists in anything retrieved. The first
linear-perturbation treatment on an averaged background is Galoppo &
Mourier 2026; in its barotropic closure the sub-horizon dust
perturbations reverse sign and become underdensities, which the authors
call "highly unexpected and, we argue, ultimately unphysical", and they
conclude "the Meszaros approximation should not be applicable in the
timescape framework" [SOURCED: arXiv:2511.17160, Secs. 5.1.1, 5.1.2, Fig.
3]. No `sigma_8`, `S_8` or `f sigma_8` is computed for timescape there.

No dedicated timescape BBN calculation exists. The only treatment is
inline: BBN is unchanged "apart from recalibrating the baryon-to-photon
ratio and the helium abundance" [SOURCED: arXiv:1410.3470, Sec. III.2],
with no computed abundances, and the lithium-7 claim withdrawn as above.

## Independence - the status every entry gets

`protocol/EVIDENCE-RULES.md` Sec. 7: `supported` requires confirmation
from outside the proposing group. Outside analyses retrieved: three.

1. **Kwan, Francis & Lewis 2009**, arXiv:0902.4249, MNRAS Lett. 399
   (2009) L6: `ln B = -1.38` (Union), `-1.469` (Constitution), and the
   core argument that "there is significant tension in the best fit
   parameters obtained from different samples, whereas LCDM is able to
   fit all datasets consistently". Smale & Wiltshire reply that the
   criticism is "invalid once the SHS cut is made" [SOURCED:
   arXiv:1009.5855, Sec. 4.3].
2. **DES Collaboration 2024**, arXiv:2406.05048: weakly favours timescape
   on supernovae alone, strongly favours LCDM once BAO is added, with
   "a strong tension between the DES-SN5YR with BAO-theta*-perp datasets
   when fitting the Timescape model" - reported for none of the other 14
   non-standard models. The timescape group has replied in print: "the
   BAO analysis of Camilleri et al. 2024 assumes purely geometric
   adjustments to the standard FLRW pipeline, using a LCDM calibration of
   the BAO drag epoch, which is not the case in timescape" [SOURCED:
   arXiv:2412.15143, Sec. 1].
3. **Saulder, Mieske, van Kampen & Zeilinger 2019**, arXiv:1811.11976,
   A&A 622 (2019) A83: statistical tests "consistently favored LCDM over
   the approximated timescape model". Wiltshire replies that their
   Millennium rescaling omits the lapse-rate contribution and that the
   dressed metric "cannot be obtained by a spatial rescaling of a FLRW
   metric", so the model they tested "cannot be considered to approximate
   the timescape cosmology" [SOURCED: arXiv:1812.01586, A&A 624 (2019)
   A12, Secs. 2-3].

All three go against the model and all three have a proponent reply
disputing the setup. None has a counter-reply. **So no timescape
empirical claim reaches `supported`; the honest status is `contested`
throughout.** That is a statement about the state of the record, not
about who is right.

There is also no published comment, reply, erratum or independent
reanalysis of the 2025 `ln B > 5` claim. INSPIRE lists 21 citing records
for arXiv:2412.15143 and 26 for arXiv:2311.01438, none of which is a
comment or reanalysis of the timescape supernova result [SOURCED:
INSPIRE citing lists, recids 2861436 and 2717911, retrieved in this run].
Age at the time of this run: roughly 23 months since the preprint. Under
ledger rule C8 that is a different evidential situation from a claim with
critiques, and it should not be read either as acceptance or as rejection.

---

# Part 3 - The live objections

## O1. Backreaction magnitude. Attacks T8 (seed `D4`). **Unresolved.**

**Green & Wald's position.** Four assumptions, numbered in the source:
(i) Einstein's equation holds for all `lambda > 0` with a source
satisfying the weak energy condition (Eq. 2); (ii) the perturbation is
bounded, `|gamma_ab| <= lambda C_1(x)` (Eq. 3), so it goes to zero as
`lambda -> 0`; (iii) first derivatives are bounded,
`|grad_c gamma_ab| <= C_2(x)` (Eq. 4), and are **not** required to be
small; (iv) local averages of quadratic products of first derivatives
have a weak limit (Eq. 5). Theorem 1 (Eq. 7): the effective
stress-energy is traceless. Theorem 2 (Eq. 8): it satisfies the weak
energy condition. Conclusion: it "must be of the form of a P=rho/3 fluid,
and therefore cannot mimic dark energy" [all SOURCED: Green & Wald,
arXiv:1407.8084, Class. Quantum Grav. 31 (2014) 234003, DOI
10.1088/0264-9381/31/23/234003, Sec. 2]. Their assumption in their own
words: the perturbation "is small but its first spacetime derivatives
need not be small" (Sec. 2).

Earlier statement of the same programme: Ishibashi & Wald, "Can the
Acceleration of Our Universe Be Explained by the Effects of
Inhomogeneities?", answer "No", on the premise that the universe is
accurately described by a Newtonianly perturbed FLRW metric [SOURCED:
arXiv:gr-qc/0509108, Class. Quantum Grav. 23 (2006) 235, DOI
10.1088/0264-9381/23/1/012].

**Buchert et al.'s position.** Assumption (iv) is the one doing the work:
"The condition (iv) is not motivated by any transparent and natural
physical argument" (Sec. 3.4), and it excludes the realistic regime
because it requires perturbations down to arbitrarily small wavelengths,
whereas "real perturbations do not continue to zero wavelength" (Sec.
4.2). On the two-dimensional analogy, the curvature-averaging assumption
"assumes what is to be proven" (abstract). On the status of the theorem:
it "fails to be a mathematically general statement" (abstract), and a
weak-energy-condition result "would be fine but irrelevant for
backreaction" (Sec. 5.2) [all SOURCED: Buchert, Carfora, Ellis, Kolb,
MacCallum, Ostrowski, Rasanen, Roukema, Andersson, Coley & Wiltshire,
arXiv:1505.07800, Class. Quantum Grav. 32 (2015) 215021, DOI
10.1088/0264-9381/32/21/215021].

**What the disagreement turns on: which idealisation applies, not
mathematics.** Neither side alleges a mathematical error. Green & Wald
record that the revision removed them: "all assertions that we made
mathematical errors in our work have been removed" [SOURCED: Green &
Wald, "Comments on Backreaction", arXiv:1506.06452, Introduction]. They
say most criticisms are "irrelevant to our main arguments" and some rest
on "misinterpretations of our work". Their one factual concession is
narrow: "The authors of [2] correctly say that we obtain our matter
stress-energy" (Appendix C).

**Green & Wald themselves disclaim the strong reading.** "whether, in our
actual universe, there might be significant backreaction" is not
addressed by their analysis, and the closeness of the metric to FLRW
"does not imply that backreaction effects of inhomogeneities must be
negligible" [SOURCED: arXiv:1407.8084, Sec. 2]. Also Sec. 4.3:
observables in the actual universe "can differ considerably from
observables computed in the FLRW background". This is stated here because
the "Green-Wald proved backreaction cannot work" reading is common and is
not what the paper claims.

**Concessions on the other side:** Buchert and Buchert & Rasanen concede
the magnitude is not established. "the effect has not been quantified in
a fully realistic model"; "At the moment it is not yet clear whether
backreaction is quantitatively important or not" [SOURCED:
arXiv:1112.5335, Sec. 5; Rasanen, arXiv:1102.0408, Class. Quantum Grav.
28 (2011) 164008, DOI 10.1088/0264-9381/28/16/164008, Sec. 1.1]. And both
sides agree the Buchert system is underdetermined (Part 1, T4-T5).

**Third-party adjudication: none found.** The only candidate,
arXiv:1512.02947 (Ostrowski & Roukema, MG14 proceedings), is by a
co-author of arXiv:1505.07800 and is therefore not independent. Green &
Wald's reply was **never published in a journal** [SOURCED:
arXiv:1506.06452, no journal reference, no DOI], while the Buchert et al.
side was published in CQG. The exchange never closed in the refereed
literature.

**`resolved: false`.** No locator shows the field resolved it.

**Two corrections to how O1 is usually framed, both bearing on
timescape.** First, Green & Wald's theorems concern `Q`-type effective
stress-energy and so do not engage timescape's mechanism, which is
average negative spatial curvature at `Omega-bar_k0 = 0.862` with
`Omega-bar_Q0 = -0.0293` (Part 1, T8). The Green-Wald argument that does
reach it is their Sec. 3 claim that large averaged scalar curvature in
Buchert's scheme is "entirely spurious". Second, Green & Wald do not
mention timescape or Wiltshire anywhere; they critique Buchert by name
[SOURCED, negative: arXiv:1407.8084, searched]. So the dispute as fought
is not about timescape, and treating it as timescape's decisive
battleground - as the seed does - is a category error.

Separately, Kaiser's "no Newtonian backreaction" argument was identified
as relevant but **I did not retrieve it**, so I cannot state its content.
`[LEAD]`.

## O2. The clock effect as a calibration convention. Attacks T9-T10 (seed `D6`). **Unresolved, and weaker in the published record than the seed assumes.**

**The CEP's status is settled and is not in dispute.** It is Wiltshire's
own extension of the SEP, with content he states is absent from GR: "a
further principle of relativity that is lacking in general relativity
with the SEP alone" [SOURCED: arXiv:1106.1693, Sec. 3.3.1]. See Part 1,
T9 for the full quotation set. So the question is not whether it is an
extra postulate - it is - but whether the postulated effect is
gauge-invariant.

**What a measurement of the effect would measure.** The gauge-invariant
content, as far as I can establish it, is not the lapse itself but its
observable consequences: the dressed-versus-bare parameter split and a
scale-dependent, direction-dependent inferred expansion rate. Wiltshire's
own framing supports this reading: the dressed density parameters do not
sum to one and are "just a convenient parametrization" [SOURCED:
arXiv:1410.3470, Sec. III.1]; and the Hubble parameter is a "gauge
choice" that is not physically observable [SOURCED: arXiv:1106.1693, Sec.
3.3]. That is `[INFERENCE]` from those two statements, not a retrieved
claim, and it is the weakest link in this section.

**The strongest statement of the objection I retrieved is Wiltshire's
own.** "The argument above relies on it being possible to choose a
locally uniform Hubble flow gauge" and "Such a gauge can be maintained
outside finite infinity regions, but not within them" [SOURCED:
arXiv:0809.1183, Sec. III.1]. Also: the frame of minimum Hubble expansion
variance "still remains to be determined" [SOURCED: arXiv:1311.3787, Sec.
7.2]; "energy, momenta, and angular momenta are only defined with respect
to a frame" [SOURCED: arXiv:0809.1183, Sec. VII]; and the mathematical
procedures for patching cosmological inertial frames "have not been
developed yet" [SOURCED: arXiv:1106.1693, Sec. 3.3.1].

**The published critique by name: one sentence, no calculation.** Rasanen
argues that the dust approximation's inadequacies concern pressure,
anisotropic stress and energy flux rather than granularity, and concludes
"it is unlikely that the effects would be captured by simply having clocks
run at different rates in different regions", citing Wiltshire [SOURCED:
Rasanen, arXiv:1102.0408, Sec. 4.3, ref. [55] verified against the
bibliography as Wiltshire arXiv:0712.3984, arXiv:0809.1183,
arXiv:0909.0749]. The word "timescape" does not appear in that paper and
"lapse function" is not mentioned. This is an assertion of implausibility,
not the gauge-artifact argument the seed describes. Buchert & Rasanen's
review mentions timescape once, neutrally: "A similar construction has
been used in the so-called timescape cosmology proposed by Wiltshire"
[SOURCED: arXiv:1112.5335, Sec. 3.2.3], and does not mention the clock
effect at all.

**I did not retrieve a published paper arguing that the clock effect is a
gauge artifact, and I did not retrieve a proposed test distinguishing a
physical clock effect from a calibration convention.** `[UNKNOWN]` on
both. This is a finding, and it cuts against the seed: O2 as the seed
states it is a *reconstructed* objection, sharper than anything in the
published record. The record contains the proponent's own gauge
concessions and one dismissive sentence from Rasanen. What would settle
it: a search of the CQG and JCAP comment literature 2008-2015, and of
citations to arXiv:0809.1183, for a paper making the gauge argument
explicitly. I searched citing lists for the supernova papers, not for the
CEP paper.

**`resolved: false`.** Not because the field weighed it and could not
decide, but because it has largely not been engaged.

## O1 and O2 are independent, and the output should be explicit about it

They are independent in both directions, and timescape's own numbers make
this sharper than the seed does.

- Granting O1 entirely in backreaction's favour does not help with O2.
  The clock-rate postulate is an addition to GR (T9); no magnitude of `Q`
  establishes it.
- Granting O2 entirely in Wiltshire's favour does not require winning
  O1 - and more than that, **timescape does not need a large `Q` at all.**
  Its own fitted `Omega-bar_Q0 = -0.0293`, with `|Omega-bar_Q| <~ 0.042`
  always and `q-bar > 0` (T8). Smale & Wiltshire: backreaction "<5%" of
  the total energy density. So a resolution of O1 against large
  backreaction would not by itself refute timescape; it would refute the
  Buchert-acceleration programme that timescape is usually grouped with.

What timescape needs from the averaging literature is not large `Q` but
large average negative spatial curvature, and the only argument retrieved
against *that* is Green & Wald Sec. 3's spurious-curvature claim, which
has no published reply addressed to timescape.

## O3. Circularity in the supernova evidence. Attacks T13 (seed `D8`). **Live, acknowledged on both sides, and unresolved.** See the box at the head of Part 2. The checkable finding: no published analysis both avoids an LCDM-derived bias calibration and corrects for selection bias.

## O4. Prediction versus postdiction. Attacks T11-T13 (seed `D7`). **Resolves against "prediction", with a caveat that cuts both ways.**

`f_v0` is **fitted** in every analysis retrieved. Values, with sources:
0.76 (+0.12/-0.09) from CMB angular sound horizon + BAO scale + SNe
[arXiv:0709.2535]; 0.72-0.95 across datasets, with 0.95 (+0.03/-0.04) for
Union2 [arXiv:1009.5855, Tables 1, 3, 5]; 0.695 (+0.041/-0.051) from
Planck sound-horizon scales [arXiv:1306.3208, Table 1]; 0.628 / 0.550 /
0.557 by CMB matching prescription [arXiv:1410.3470, Table 2]; 0.778
[arXiv:1706.07236, Table 3]; 0.675 [arXiv:2311.01438, Fig. 8]; 0.737 +/-
0.029 [arXiv:2412.15143, Sec. 3]; 0.791 (+0.039/-0.034) and 0.665
(+0.008/-0.009) [arXiv:2406.05048, Table 5]. **The spread, 0.550 to 0.95,
far exceeds the quoted uncertainties, so these fits are mutually
inconsistent.** That is itself a finding and no paper I retrieved
confronts it.

Wiltshire cites an observed void fraction as motivation - "Some 40-50% of
the present volume" [arXiv:0709.0732, introduction], and ~40% citing
Hoyle & Vogeley [arXiv:1410.3470, Sec. I] - but **never sets it against
the fitted value**, which exceeds it in every case.

The caveat that cuts both ways: the best measurement I retrieved is 62%
of the SDSS DR7 sample volume [arXiv:1103.4156], which is closer to the
CMB-fitted 0.628 than the cited 40-50% is. But that same paper reports
the void fractions are reproduced by LCDM mocks, so even exact agreement
would not discriminate. And timescape's `f_v` is a bare volume fraction
of the Buchert average at ~100 h^-1 Mpc, defined through finite-infinity
surfaces where the average expansion vanishes - **not** the same quantity
as a galaxy-survey void-finder filling factor. Equating them requires an
argument nobody has made `[INFERENCE]`; premises: the `f_v` definition in
arXiv:gr-qc/0702082 Sec. 5.1 and the `VoidFinder` definition in
arXiv:1103.4156.

So: `f_v0` is fitted; the model postdicts. The seed's conditional - "If
they agree within errors and the measurement was not derived under an
LCDM assumption, that is substantial evidence" - is not satisfied,
because no such comparison has been made and the two quantities are not
the same.

## O5. Are LTB void constraints transferable? Attacks the programme. **Genuinely unaddressed in the literature. This is the cleanest negative in the run.**

The constraints are real and severe for LTB. Moss, Zibin & Scott: void
models are "overwhelmingly at odds with several types of observations",
with void `h_0 = 0.45 +/- 0.02` against Cepheid `0.738 +/- 0.024`, void
ages 17.6-18.8 Gyr against LCDM `13.7 +/- 0.1`, void `sigma_8 ~ 0.48 +/-
0.04` against `0.86 +/- 0.04`, Compton `y = 3.0 x 10^-5` against the
COBE/FIRAS limit `y < 1.5 x 10^-5` (2 sigma), and radial-BAO
`Delta chi^2 = 7.5`-`10.1`; **note their supernova chi-squared is
534-541 against 531 for LCDM, so the supernovae do not do the excluding**
[SOURCED: arXiv:1007.3725, Phys. Rev. D 83 (2011) 103515, DOI
10.1103/PhysRevD.83.103515, abstract, Secs. III.2-III.3, V]. kSZ: void
models inside the 3 sigma supernova contour give
`Delta T^2 > 10^3 micro-K^2` at `l = 3000`, "two orders of magnitude
larger than the SPT upper limit 6.5 micro-K^2" [SOURCED: Zhang &
Stebbins, arXiv:1009.3967, Phys. Rev. Lett. 107 (2011) 041301]. Zibin &
Moss put the excess at "at least a factor of roughly 30" and list eight
caveats that could reduce it [SOURCED: arXiv:1105.0909, Secs. IV, VII].
Bull, Clifton & Ferreira: relaxing the bang-time function is "not enough
to simultaneously explain the supernovae observations, the small-angle
CMB, the local Hubble rate, and the kSZ effect", which "effectively rules
out simple LTB models" [SOURCED: arXiv:1108.2222, Phys. Rev. D 85 (2012)
024002, DOI 10.1103/PhysRevD.85.024002, abstract].

**None of those papers mentions timescape, Wiltshire, backreaction,
Buchert or averaging** [SOURCED, negative: full text of arXiv:1007.3725
read in two passes; arXiv:1009.3967; arXiv:1105.0909; and the abstracts
of arXiv:1108.2222, arXiv:0807.1326, arXiv:1201.2790]. **And no paper, by
anyone, argues either that these constraints transfer to timescape or
that they do not.**

The nearest material is all on the proponent's side and none of it
engages kSZ, `y`-distortion or local `sigma_8`: "LTB models are clearly
applicable to individual expanding spherical voids" and "galaxies in
clusters do not collapse inwards in coherent spherical shells"
[arXiv:1311.3787, Sec. 2.3 and fn. 1]; the dressed metric "is not a LTB
solution" [same, Sec. 5.1]; and a note that an LTB Hubble bubble "will
also have different characteristics to the apparent Hubble bubble in the
TS model" [arXiv:1009.5855, fn. 8]. The structurally analogous argument
exists but for a different test: Wiltshire's 2019 Comment that the
dressed metric "cannot be obtained by a spatial rescaling of a FLRW
metric" and the dressed Hubble parameter "is not linearly related to any
void fraction" [arXiv:1812.01586, Secs. 2-3].

So the seed is right that the argument has to be made explicitly, and the
answer is that **it has not been made, by either side.** Making it would
be new work, not an audit finding.

## O6. Severity of the CMB test. Attacks T13 (seed `D8`). **Partly resolved, against the claim of a passed severe test, but not against the model.**

See Part 2. The current state: no Planck 2015 or 2018 timescape fit
exists; the one full-spectrum fit uses Planck 2013 through a matched FLRW
proxy, with backreaction neglected before decoupling and the late ISW
uncomputed; `-ln L` is 0.7% worse than LCDM for the matching prescription
the paper headlines and essentially equal for two others; `f_v0` varies
12% across prescriptions; systematics are 8-13% against 1-2% statistical;
and `Omega_b h^2` is unpublished. Claimed consistency is therefore not
demonstrated consistency at the precision of current data - which is what
the seed suspected - but neither is it a failed test. The honest status is
that the severe version of the test has not been performed.

## Objections the seed does not have, which I would add

- **O7. Light propagation.** T12. Weight 3, conceded unjustified by both
  Buchert and Wiltshire, and not treated as an objection anywhere in the
  literature retrieved. This is the largest gap between what the model
  needs and what has been shown.
- **O8. Mutually inconsistent `f_v0` fits.** O4 above. The parameter
  spans 0.550-0.95 across datasets with quoted errors of a few percent.
  Nobody has reported this as a problem.
- **O9. Structure growth.** Part 2. The one perturbation calculation on an
  averaged background produces a result its authors call "ultimately
  unphysical" in one closure, and no `sigma_8` or `S_8` has been
  computed. The seed lists structure growth as a candidate; the retrieved
  position is worse than "unverified".
- **O10. No sensitivity analysis of the two-phase split.** T6. Wiltshire
  states the single-curvature-scale simplification and suggests
  alternatives but reports no sensitivity test.

---

# Part 4 - Rivals and discrimination

## The priority comparison: Buchert averaging with backreaction, without the clock-effect postulate

**The number exists, in three forms, and the answer is that on supernovae
alone the clock effect buys nothing measurable - while off supernovae it
buys the ability to avoid needing volume acceleration at all.**

**Form 1, the cleanest: matched parameter counts, same data, both models
fitted.** Buchert-scheme scaling solutions with dynamical spatial
curvature and no clock-rate postulate, fitted to JLA alongside both LCDM
and timescape at `z_min = 0.033`, 655 of 740 SNe, with `alpha` and `beta`
fitted globally. AIC values: flat LCDM `-228` (9 parameters), timescape
`-227` (9), scaling solution with `n = -1` `-227` (9), scaling solution
with `n` free `-225` (10), LCDM with `Omega_k` free `-226` (10). The
authors' statement: "the scaling solution with n=-1 and the timescape
model overall have the highest AIC likelihoods", and the fit quality is
indistinguishable from LCDM and timescape for `z <~ 1` [SOURCED:
Desgrange, Heinesen & Buchert, arXiv:1902.07915, Int. J. Mod. Phys. D 28
(2019) 1950143, DOI 10.1142/S0218271819501438, abstract and Table 2].
**At matched parameter count on the same supernovae, dropping the clock
effect costs nothing.** Caveat: the AIC sign convention in that table
should be confirmed from the paper before the direction is quoted; I have
the values and the authors' own ranking statement, not the convention.

**Form 2: an independent fit to supernovae plus CMB peaks, and what it
costs.** Buchert averaging with a smoothed template metric and
time-evolving constant spatial curvature, no clock-rate postulate, fitted
to SNLS supernovae plus WMAP 3-year peak and dip positions, with
`Omega_m^D0`, the scaling index `n`, `H_D0` and `Omega_b h^2` free.
"The difference in the chi^2 between the two models is 3.9" against flat
FLRW with quintessence; best fit `Omega_m^D0 = 0.38`, `n = 0.12`,
`H_D0 = 78.54` km/s/Mpc, `Omega_b h^2 = 0.0255`. **No absolute
chi-squared is reported anywhere in the paper and there are no numerical
error bars or tables**, so under ledger rule C6 the statistic is
**uninterpretable**. The decisive qualitative statement is theirs: the
model works "without requiring an additional Dark Energy component",
"(though a volume acceleration is still needed)", and "a high level of
backreaction is needed and acceleration of the effective scale factor
still occurs". Their own assessment of the constraint: "it is consistent
with current data, but the constraints are not very strong" [all SOURCED:
Larena, Alimi, Buchert, Kunz & Corasaniti, arXiv:0808.1161, Phys. Rev. D
79 (2009) 083011, DOI 10.1103/PhysRevD.79.083011, Secs. 4.2, 4.3].

**Form 3: whether the required backreaction is achievable.** This is
where the backreaction-only route is in trouble on its own terms, and the
numbers come from the programme's own proponents. Rasanen's peak-model
calculation: the expansion rate rises relative to FRW "on a timescale of
10-100 billion years" and "the increase is not rapid enough to correspond
to acceleration", with the backreaction density parameter "below 0.04 in
absolute value" against "`|Omega_Q| >~ 0.2` is needed to obtain
acceleration of the observed magnitude" - short by a factor of about five
[SOURCED: Rasanen, arXiv:0801.2692, JCAP 0804 (2008) 026, DOI
10.1088/1475-7516/2008/04/026, Sec. 4.3]. The semi-realistic model
achieves "a change of the right order of magnitude in H t, 15-25%"
against a target of 20-70%, but "the change is not sufficiently rapid for
the expansion to accelerate, there is just less deceleration", and "The
model cannot be trusted beyond an order of magnitude" [SOURCED:
arXiv:1102.0408, Secs. 1.1, 3.2, 6; same numbers at arXiv:1112.5335, Sec.
3.2.2]. The strong-backreaction option costs the matter budget: a
three-parameter multiscale model reproduces LCDM-like scale-factor
behaviour without `Lambda`, but requires `Omega_m^D0 ~ 3%`, reinterpreted
as "kinematical Dark Matter" [SOURCED: Wiegand & Buchert,
arXiv:1002.3912, Phys. Rev. D 82 (2010) 023523, DOI
10.1103/PhysRevD.82.023523].

**What the clock effect is therefore buying, stated precisely.** Not a
better supernova fit: Form 1 shows none at matched parameter count. What
it buys is that timescape does **not** need volume acceleration, and so
does not need the large `Q` that the backreaction-only route requires and
that the best realistic estimates fail to deliver. Timescape's split is
backreaction "<5%" plus a 38% clock-rate differential
[arXiv:1009.5855, Sec. 2]; the backreaction-only route needs "a high
level of backreaction" and genuine volume acceleration
[arXiv:0808.1161, Sec. 4.2]. **That is the isolation the prompt asked
for, and it is a real result**: the clock effect relocates the required
large quantity from `Q`, where the realistic estimates come up short by
roughly a factor of five, to `<R>`, where no comparable realistic
estimate exists at all.

**Clean negative: no ablation study exists.** No paper fits the same
supernova dataset with and without the clock-rate postulate and reports
the difference in chi-squared or Bayes factor. The Desgrange et al. table
is the closest thing, and it fits both models to the same data but does
not frame the comparison as an ablation. Searches run are listed in Part 6.

## The other rivals

**LTB / large local void.** Excluded, severely, by local `H_0`, age,
local `sigma_8`, Compton `y`, radial BAO and kSZ. See O5 for the numbers.
Whether the constraints transfer to timescape is unaddressed by anyone.

**Swiss-cheese and perturbative backreaction.** Small effects, and the
authors are explicit about why in two of three cases. Marra, Kolb &
Matarrese: the light-cone averaged density ratio "decreases by 17%" but
the expansion rate is unaffected, best fit `w ~= 0`; the FLRW matching at
hole boundaries is explicit in the construction, but they do not draw the
inference that it is what forces the effect to be small [SOURCED:
arXiv:0710.5505, Secs. II.2.2, III.4.1, IV.1; journal reference not
retrieved]. Vanderveld, Flanagan & Wasserman: Monte Carlo over 10,000
realisations of five void passages gives a mean distance-modulus shift of
`-0.003` mag with standard deviation `0.11` mag, and they conclude "this
particular model cannot explain the supernova data"; they attribute the
smallness to weak-field lensing and mass compensation, "true within the
domain of validity of weak lensing theory", not to the FLRW matching
[SOURCED: arXiv:0808.1080, Secs. III-V; journal reference not retrieved].
Clarkson, Ananda & Larena: for the concordance model averaged on Hubble
scales the change today is about `10^-5`, and the smallness is "as
expected in perturbation theory" - an expectation of the second-order
construction rather than an independent result; they also note
backreaction "cannot be said to vanish on very large scales" [SOURCED:
arXiv:0907.3377, Secs. I, IV.1; journal reference `[LEAD]`].

So: for the perturbative case the smallness is substantially a
consequence of the construction, by the authors' own accounts. For the
Swiss-cheese case it follows from mass compensation within weak lensing.
Neither bounds a non-perturbative, non-mass-compensated scheme, which is
the regime Buchert et al. say the Green-Wald conditions exclude. That
connects O5 and O1 and is worth stating.

**Rasanen's peak-structure averaging.** He does not agree with Wiltshire
on magnitude and dismisses the mechanism in one sentence without a
calculation. See O2. On magnitude his own numbers fall short (Form 3
above). The only timescape mention in the review he co-wrote is neutral.

**LCDM.** The `H_0` tension persists and is direction-dependent on which
standard candle is trusted. A seven-route covariance combination gives
`H_0 = 73.30 +/- 0.92` km/s/Mpc, "more than 5 sigma higher" than the CMB
value in base LCDM, at `5.6 sigma` against Planck [SOURCED: Chen & Wang,
arXiv:2606.26831, accepted in Research in Astronomy and Astrophysics].
The full HST sample gives `73.2 +/- 0.9`, with JWST three-method
`72.6 +/- 2.0` [SOURCED: Riess et al., arXiv:2408.11770]. Against that,
the CCHP programme's TRGB result is `70.39 +/- 1.22` (stat) `+/- 1.33`
(sys) `+/- 0.70` and their own verdict is "Our results are consistent
with the current standard LambdaCDM model, without the need for the
inclusion of additional new physics"; their JWST-only values are
`68.81 +/- 1.79 +/- 1.32` (TRGB) and `67.80 +/- 2.17 +/- 1.64` (JAGB)
[SOURCED: Freedman et al., arXiv:2408.06153]. Both sides' JWST-only
errors are large enough to overlap the gap. `S_8` has partly dissolved
into a survey-versus-survey disagreement: against a combined CMB baseline
`S_8 = 0.836 (+0.012/-0.013)`, DES Year 6 is at `2.4`-`2.7 sigma` while
KiDS Legacy is consistent at `< 1 sigma`, and cluster counts split with
eROSITA favouring high and SPT low - a "striking bifurcation" with
survey-specific systematics contributing substantially [SOURCED: Pantos &
Perivolaropoulos, arXiv:2602.12238, Phys. Dark Univ. 52 (2026) 102286,
DOI 10.1016/j.dark.2026.102286].

**Dynamical dark energy.** DESI DR2: `3.1 sigma` for evolving dark energy
from DESI BAO + CMB, and `2.8 sigma` (Pantheon+), `3.8 sigma` (Union3),
`4.2 sigma` (DES-Y5) with supernovae added; DESI BAO versus CMB shows
"mild, 2.3 sigma tension" within LCDM [SOURCED: arXiv:2503.14738, Phys.
Rev. D 112 (2025) 083515, Table 6]. The DESI team's own caveats, with
sections: "While this form of w(a) does not arise directly from an
underlying physical model" (Sec. VII); "the marginalized means and limits
quoted above are prior-dependent" and "the statistical significances from
all data depend somewhat on the choice of SNe dataset included" (Sec.
VII.1); "it does not yet rise to the 5 sigma threshold commonly accepted
for establishing new physics" (Sec. VII.3); and they name as candidate
explanations "an undetected systematic error in our BAO measurements" and
unknown CMB systematics (Sec. VII.3) [all SOURCED: same]. Arguing the
evidence is weaker: Efstathiou finds "evidence for an offset of ~0.04
mag. between low and high redshifts" among supernovae common to DES5Y and
Pantheon+, and that "Systematics of this order can bring the DES5Y sample
into good agreement with the Planck LCDM cosmology and Pantheon+"
[SOURCED: arXiv:2408.07175].

**How this bears on timescape, in both directions.** For: a measured
departure from constant `w` is a departure from the model timescape
rejects, and the timescape group reads it that way `[LEAD]` - the only
place I retrieved that reading is a conference abstract, not a paper
[SOURCED: Wiltshire et al., "Timescape versus LCDM", Transients in Middle
Earth, Univ. of Canterbury, 10 Feb 2026, indico.global/event/16070/
contributions/144489/]. Against: the DESI signal is in the
`w_0 > -1, w_a < 0` quadrant and is extracted from BAO distances
calibrated on a Planck-scaled fiducial template, so it is not a
model-independent result that any non-FLRW model automatically inherits;
and timescape's own effective `w(z)` is one Wiltshire says "has no
physical meaning" [SOURCED: arXiv:1311.3787, Secs. 5-6]. Neither
direction is established.

**Modified gravity.** Hu-Sawicki `f(R)` is constrained to
`log_10 |f_R0| < -4.59` at 95% confidence, length scale today
`lambda < 17.81` Mpc, mediator mass `m_phi > 3.60 x 10^-31` eV, with "We
find no evidence for deviations from GR" [SOURCED: DESI Collaboration
(Gonzalez, Niz, Aviles et al.), arXiv:2604.26915]. The survey reference
is Clifton, Ferreira, Padilla & Skordis, arXiv:1106.2476, Phys. Rep. 513
(2012) 1, DOI 10.1016/j.physrep.2012.01.001. What distinguishes it from
an inhomogeneity-based explanation observationally: `f(R)` keeps an
exactly FLRW background and modifies structure growth through a
scale-dependent effective Newton constant, so it is tested by
`mu(a,k)`/`Sigma(a,k)`, `f sigma_8` and a Yukawa range; inhomogeneity
models change the geometry and the distance-redshift relation, breaking
the FLRW consistency relations while leaving growth standard. `[INFERENCE]`;
premises: the `f(R)` bound being a growth-and-scale constraint, and
Wiltshire predicting "a non-zero C(z) for the timescape model" [SOURCED:
arXiv:0912.5236, Sec. 3.5]. I retrieved no paper that makes this
comparison explicitly.

## The discrimination table

| Observable | Timescape | Rival | Rival predicts | Current precision | Needed | Already decided? |
|---|---|---|---|---|---|---|
| Supernova + BAO joint fit | tension between the two | flat LCDM | no tension | half-Delta-AIC resolved to +/-0.1 | achieved | **Yes, against timescape in the one independent analysis** [arXiv:2406.05048, Table 7] |
| Redshift drift, `delta z` over 10 yr at `z = 4` | `-7.2 x 10^-10` | flat LCDM | `-9.3 x 10^-10` | not measured | ~20 yr Lyman-alpha baseline with ELTs over `2 < z < 5` | No |
| Clarkson-Bassett-Lu `C(z)` | `C(z) != 0` | FLRW, any curvature | `C(z) = 0` | cannot yet constrain `H(z) D'(z)` | not stated | No |
| `Om(0)` | `0.643 (+0.008/-0.004)` | LCDM | `= Omega_M0` | not stated | not stated | No |
| Local Hubble-flow variance | 17-22%; min `50.1 +/- 1.7`, max `75.2 (+2.0/-2.6)` km/s/Mpc | LCDM + local boost | small, from peculiar velocities | uniform at 70-100 Mpc, consistent with LCDM over 20-150 Mpc | a reanalysis against the 17-22% prediction, which nobody has done | **No** - the two results are not stated as the same quantity |
| Onset of apparent acceleration | `z_acc = 0.46 (+0.26/-0.25)`, or `z ~ 0.9` elsewhere | LCDM | `z ~ 0.6`-`0.7` `[LEAD]` | - | - | No; the timescape number is not internally consistent across papers |
| Dressed `q_0` | `-0.043 (+0.004/-0.000)` | flat LCDM | `~ -0.5` `[INFERENCE]` | - | - | No; `q_0` is not measured model-independently |
| Dressed `H_0` | `60.98`-`61.7` | LCDM + distance ladder | `70`-`73.3` | `+/- 0.9` locally | achieved | **Arguably yes, against timescape**, and this is not usually stated |
| BAO scale under each fiducial | `95.4 +/- 1.6` Mpc/h | LCDM fiducial | `102.6 +/- 1.5` Mpc/h | achieved | achieved | Not a prediction; a fiducial-conversion difference |
| `sigma_8` / `S_8` | **not computed** | LCDM | `S_8 = 0.836 (+0.012/-0.013)` | `2.4`-`2.7 sigma` (DES-Y6) to `<1 sigma` (KiDS) | a timescape `S_8` calculation | No; the prediction does not exist |
| Alcock-Paczynski `F(z)` | `0.246, 0.496, 0.776, 1.067` at `z = 0.21, 0.41, 0.60, 0.78` | LCDM | steeper `H(z)/H_0` slope | consistent with WiggleZ | needs both BAO and luminosity distance | No |

Locators: arXiv:2406.05048 Table 7; arXiv:1311.3787 Secs. 5.3, 6.2-6.6, 7
and Table 1; arXiv:0912.5236 Secs. 2, 3.3, 3.5, 3.6; arXiv:1811.11963
Tables 1-2; arXiv:2510.19945 abstract; arXiv:1706.07236 abstract;
arXiv:2602.12238 abstract.

Read the table as a whole and two things stand out. The measurements that
already discriminate, and discriminate against timescape, are the ones
nobody frames as tests: the joint supernova-plus-BAO fit and the dressed
`H_0`. The measurements framed as timescape's distinctive predictions -
redshift drift, the Clarkson-Bassett-Lu test, Hubble-flow variance - are
either decades from the required precision or have a measurement that
exists but has never been compared against the prediction. **That is the
most actionable finding in Part 4: the comparison in the Hubble-flow row
is a few weeks of work on published data and has not been done.**

---

# Part 5 - Seed corrections

Sources for each are given in the Part indicated.

## `docs/derivation-chain.md`

1. **`D1` `THEOREM` tag.** A measurement is not a theorem. The step
   should carry no `THEOREM` tag. Part 1, T1.
2. **`D1` audit question, answered.** Timescape does not require a
   homogeneity scale larger than the standard value; it coarse-grains at
   ~100 h^-1 Mpc, tied to the standard statistical-homogeneity and BAO
   scale. Part 1, T1.
3. **`D2` conflates two claims under one `THEOREM` tag.** The scalar
   commutation rule is an exact identity (T2). The metric-averaging
   version is nowhere a theorem in the retrieved literature, rests on an
   averaging operation Ellis himself calls not well defined, and
   **timescape does not use it** (T3). Weight 3 versus weight 0.
4. **`D3` is under-specified rather than wrong.** The averaged equations
   are theorems conditional on chosen conditions; the scheme content is
   those conditions plus the closure. The seed should split them. Parts
   1, T4-T5.
5. **`D4` is not timescape's mechanism, and this is the largest seed
   error.** `Omega-bar_Q0 = -0.0293`, negative, `|Omega-bar_Q| <~ 0.042`
   always, `q-bar > 0`, no volume acceleration, backreaction "<5%" of the
   energy density. The bare budget is dominated by average negative
   spatial curvature, `Omega-bar_k0 = 0.862`. The seed's claim that `D4`
   "is the first genuinely contested link" and "the highest-priority item
   in the run" mislocates the model. Part 1, T8; Part 3, O1.
6. **`D5` is correct but the seed's audit question has an answer the seed
   does not anticipate:** nothing fixes the two-phase split, Wiltshire
   says the single curvature scale is "assumed as a simplification", and
   **no sensitivity analysis exists**. Part 1, T6.
7. **`D6` should be split.** The CEP (existence) is a `POSTULATE`; the
   35-38% magnitude is a `FIT`, because `gamma-bar = 1 + f_v/2` on the
   tracker and `f_v0` is fitted. The seed treats the magnitude as part of
   the postulate. Part 1, T9-T10.
8. **`D6` audit item 1, answered:** the CEP is explicitly Wiltshire's
   extension of the SEP, with content he says is "lacking in general
   relativity with the SEP alone". Not claimed to follow from GR.
9. **`D6` audit item 2, answered with a correction:** no uncertainty is
   attached to the 35-38% figure in any paper retrieved, and the figure
   drifts with the fitted `f_v0` without being flagged.
10. **`D6` audit item 4, answered:** `alpha_0 = 8.6 (+1.9/-1.5) x 10^-11`
    m/s^2, close to the MOND scale; Wiltshire says it "may be purely
    coincidental" and that no quantitative comparison is possible yet.
11. **`D7` audit question, answered:** `f_v0` is fitted in every analysis.
    The model postdicts. Part 3, O4.
12. **A step is missing between `D7` and `D8`:** light propagation. Weight
    3, conceded unjustified by both Buchert and Wiltshire. Part 1, T12.
13. **A step is missing before `D6`:** the "exact solution" is exact in
    the two-scale Buchert equations under a flat-wall /
    negatively-curved-void ansatz, matter-only, and all phenomenology
    uses a further tracker attractor special case. Part 1, T7.

## `docs/objections.md`

14. **`O1` is not timescape's decisive objection.** It attacks a claim
    timescape does not make. The Green-Wald argument that does reach
    timescape is their Sec. 3 spurious-curvature claim, which has no
    published reply addressed to timescape. Part 3, O1.
15. **`O1`: Green & Wald do not mention timescape or Wiltshire.** They
    critique Buchert by name.
16. **`O1`: "Buchert and a large set of co-authors" includes Wiltshire.**
    The response paper is therefore not independent of the timescape
    proponent. Part 3, O1.
17. **`O1`: Green & Wald's reply was never published in a journal.** The
    exchange did not close in the refereed literature.
18. **`O1`: Green & Wald themselves disclaim the strong reading.**
    "whether, in our actual universe, there might be significant
    backreaction" is not addressed by their analysis.
19. **`O2` as the seed states it is sharper than anything published.** I
    retrieved no paper arguing the clock effect is a gauge artifact, and
    no proposed test distinguishing a physical effect from a calibration
    convention. The record holds Wiltshire's own gauge concessions and one
    dismissive sentence from Rasanen. Part 3, O2.
20. **`O3` is confirmed as real and is acknowledged by both camps**, and
    the sharp version is that **no analysis both avoids an LCDM-derived
    bias calibration and corrects for selection bias.** Part 2.
21. **`O4` resolves against prediction**, and the seed's suggested
    confirmation route does not work, because the timescape `f_v` and a
    void-finder filling factor are not the same quantity and the observed
    filling factor is reproduced by LCDM anyway. Part 3, O4.
22. **`O5` is unaddressed by anyone**, not merely unargued by proponents.
    None of the six LTB-constraint papers mentions timescape. Part 3, O5.
23. **`O5` detail: Moss, Zibin & Scott derive no kSZ constraint.** The
    kSZ bounds are Zhang & Stebbins, Zibin & Moss, García-Bellido &
    Haugbølle, and Bull et al.
24. **`O6`: the seed is right that claimed is not demonstrated**, and the
    specifics are worse than it supposes: Planck 2013 only, through a
    matched FLRW proxy, with systematics 8-13% against 1-2% statistical,
    and the lithium-7 claim withdrawn. Part 2.

## `docs/rival-approaches.md`

25. **The priority comparison has an answer** in three forms, and the
    seed's expectation that it might not exist is wrong. Part 4.
26. **The Buchert-without-clock-effect route requires volume
    acceleration**, which timescape does not have; that is what the clock
    effect buys. The seed does not anticipate this framing.
27. **Rasanen does not agree with Wiltshire on magnitude**, and his
    dismissal is one sentence with no calculation. His own numbers fall
    short by about a factor of five on `Omega_Q`.
28. **"Swiss-cheese ... Generally find small effects. Audit: whether the
    smallness is a result or a consequence of the construction."** The
    answer differs by paper: perturbative smallness is "as expected in
    perturbation theory"; Swiss-cheese smallness follows from mass
    compensation within weak lensing; neither is an FLRW-matching
    artefact in the way the seed implies, and the Marra et al. authors do
    not draw that inference. Part 4.
29. **The `S_8` tension has partly dissolved into a survey-versus-survey
    disagreement** (DES-Y6 2.4-2.7 sigma, KiDS Legacy <1 sigma, eROSITA
    and SPT split). The seed asks for honesty in both directions; this is
    what that looks like.
30. **The `H_0` tension's direction depends on which standard candle is
    trusted**, and the CCHP authors say their result needs no new physics.

## `sources/bibliography.md` - the fabrication probe

Every entry remains `[LEAD]` unless listed in `LEDGER.md` as retrieved.
Specific errors that would have propagated into fabricated citations:

31. **"Duley, Nazer & Wiltshire, CMB constraints on timescape, circa
    2013"** - the actual title is *Timescape cosmology with radiation
    fluid*, Class. Quantum Grav. 30 (2013) 175006, arXiv:1306.3208. There
    is no 2013 paper with "CMB constraints" in the title.
32. **"Seifert, Lane, Haridasu, Wiltshire, Pantheon+ timescape analysis,
    circa 2024-2025"** - the actual authors are Seifert, Lane, Galoppo,
    Ridden-Harper & Wiltshire, arXiv:2412.15143, MNRAS Lett. 537 (2025)
    L55. "Haridasu" is not an author. And the seed is missing the
    companion paper that most of the numbers come from: Lane, Seifert,
    Ridden-Harper & Wiltshire, arXiv:2311.01438, MNRAS 536 (2025) 1752.
33. **"Buchert, on average properties of inhomogeneous fluids in GR: dust
    cosmologies, 2000"** - the title includes "**I:**", and the companion
    is "**II:** perfect fluid cosmologies", Gen. Rel. Grav. 33 (2001)
    1381, arXiv:gr-qc/0102049.
34. **"Green & Wald, comments on backreaction, circa 2015"** - arXiv-only,
    arXiv:1506.06452, never published, no DOI. Citing it with a journal
    reference would be a fabrication.
35. **"Bull, Clifton & Ferreira, kSZ effect and LTB void models, PRD
    2012"** - arXiv:1108.2222, Phys. Rev. D 85 (2012) 024002. The paper's
    subject is relaxing the LTB bang-time function; kSZ is one of four
    observables, not the title subject.
36. **"Ellis, relativistic cosmology and the fitting problem, 1984"** -
    **could not be retrieved at all.** The citation string
    "Relativistic cosmology: its nature, aims and problems", in the
    invited papers of the 10th International Conference on General
    Relativity and Gravitation, p. 215, is verified from three retrieved
    bibliographies, but the paper itself has no DOI or arXiv id I could
    reach. It stays `[LEAD]` and nothing in this run rests on its wording.
37. **"Ellis & Stoeger, the fitting problem in cosmology, CQG 1987"** -
    Class. Quantum Grav. 4 (1987) 1697, DOI 10.1088/0264-9381/4/6/025.
    Landing page only; no full text, no section numbers. Sources conflict
    on the end page (1729 versus 1679) and I verified only the first page.
38. **"Zhang & Stebbins, kSZ constraint on void models, PRL 2011"** -
    correct: arXiv:1009.3967, Phys. Rev. Lett. 107 (2011) 041301. The
    paper has no numbered sections, so a section locator for it is not
    possible.
39. **Missing from the bibliography entirely, and material:** Kwan,
    Francis & Lewis, arXiv:0902.4249, MNRAS Lett. 399 (2009) L6 - the
    only outside critique of a timescape supernova fit; Camilleri et al.
    (DES), arXiv:2406.05048 - the only independent fit of timescape to a
    modern supernova sample; Saulder et al., arXiv:1811.11976, and
    Wiltshire's Comment, arXiv:1812.01586 - the only published exchange
    on whether a void-style test applies to timescape; Larena et al.,
    arXiv:0808.1161, and Desgrange, Heinesen & Buchert,
    arXiv:1902.07915 - the two papers that answer the document's own
    priority question; and Leith, Ng & Wiltshire, arXiv:0709.2535,
    Astrophys. J. 672 (2008) L91 - the original parameter-fit paper the
    foundational papers defer to.

## `docs/claim-ledger.md`

40. The field set is sound and C4/C5 were the right things to insist on.
    One addition would help: a field for **who performed the analysis
    relative to the proposing group**, because rule C7's `supported`
    threshold turns on it and it is otherwise buried in C8.

---

# Part 6 - Open questions and unverified leads

Ranked by how much they would change the audit.

**1. Is there a published argument that the void/wall clock effect is a
gauge artifact?** Why it matters: O2 is the objection on which the model
lives or dies, and I could not find it stated by a critic. If it does not
exist, the correct description of timescape's situation is not "contested
on its central claim" but "largely unengaged on its central claim", which
is a different research situation and changes what run 02 should attack.
What would settle it: citation search on arXiv:0809.1183 and
arXiv:1106.1693 via INSPIRE and NASA ADS, plus the CQG and JCAP comment
literature 2008-2016. I searched citing lists for the supernova papers,
not for the CEP papers.

**2. Does an analysis exist, or can one be made, that both avoids
LCDM-derived bias corrections and corrects for selection bias?** Why it
matters: this is the single checkable technical question behind the
headline supernova evidence, and neither camp has done it. Every `ln B`
in Part 2 is conditional on the answer. What would settle it: a
re-analysis applying selection corrections derived under the timescape
expansion history. That is new work, not an audit finding, and it belongs
to whoever runs the extension track.

**3. Compare the measured local Hubble-flow uniformity against the
17-22% timescape prediction.** Why it matters: it is the one distinctive
prediction with a prior locator and a published measurement, and the
comparison has never been made. Both numbers are in Part 2. What would
settle it: recasting the arXiv:0912.5236 Sec. 2 prediction into the
statistic Shao & Bengaly measure, on published data. Weeks, not years.

**4. Confirm or refute the `H_0 = 73.03` attribution in Galoppo &
Mourier 2026.** Why it matters: if a 2026 calculation on a timescape
background is run at a distance-ladder `H_0` while the model's own
CMB-matched value is ~61, its structure-growth conclusions are about a
different cosmology. What would settle it: the remainder of the
arXiv:2412.15143 text, and the Galoppo & Mourier Sec. 5.1.1 citation.

**5. Reconcile the Seifert et al. parameter count.** Why it matters: it is
the only thing standing between the headline `ln B > 5` and an
interpretable statistic. Five, eight and nine all appear. What would
settle it: the paper's Table 1 and its sampler configuration, read
together, or an author query.

**6. What is timescape's `Omega_b h^2`?** Why it matters: it is the
quantity that decides whether the CMB peak-height ratio can be met, and
it is not published in either timescape CMB paper. What would settle it:
deriving it from arXiv:1410.3470 Table 2, which I attempted and abandoned
because the dressed and bare routes gave inconsistent values (~0.033
versus ~0.010) and I could not determine which is intended.

**7. Does the quasilocal Newtonian limit make a checkable non-cosmological
statement?** Why it matters: the CEP's weakest feature as a physical
postulate is that it may be defined only cosmologically. A galactic-scale
application would change that. What would settle it: the full text of
Galoppo, Re & Wiltshire, arXiv:2408.00358, Class. Quantum Grav. 42 (2025)
135004, which I retrieved the locator for but not the content.

**8. Does the Green-Wald spurious-curvature argument of their Sec. 3
apply to timescape's `Omega-bar_k0 = 0.862`?** Why it matters: this is
the one line of attack that reaches timescape's actual mechanism, and
nobody on either side has aimed it there. What would settle it: an
analysis, not a retrieval. Flagging it rather than attempting it, per the
no-extensions rule.

**9. Confirm the AIC sign convention in Desgrange, Heinesen & Buchert
Table 2.** Why it matters: Part 4's cleanest result depends on reading
the direction correctly. I have the values and the authors' own ranking
sentence; I do not have the convention stated. What would settle it: the
paper's Sec. 4 text around Table 2.

**10. Does the two-phase split survive refinement?** Why it matters: T6
carries weight 3 with no sensitivity analysis in existence. What would
settle it: refitting with two or three void curvature scales, which
Wiltshire himself suggests is possible. New work.

## Unverified leads

- **Kaiser, "why there is no Newtonian backreaction", MNRAS circa 2017.**
  Identified as relevant to O1; **not retrieved.** Needed: an arXiv id or
  DOI and the full text, to establish whether it bears on the
  relativistic case and whether it addresses Buchert or Wiltshire by name.
- **The CosmoVerse White Paper's timescape sections.** Di Valentino et
  al., arXiv:2504.01669, Phys. Dark Univ. 49 (2025) 101965. I confirmed
  from the retrieved table of contents that Secs. 4.6.3.c "Timescape
  cosmology" and 4.6.3.d "Constraints from observations" exist, but the
  HTML rendering truncates before Sec. 4 and **I could not read them.**
  This is likely the most authoritative third-party assessment of
  timescape's observational status in existence and it is unread in this
  run. Needed: the PDF. Highest-value single retrieval for run 02.
- **Buchert, Mourier & Roy, Paper III on general fluid cosmologies**,
  apparently arXiv:1912.04213. The id came from a search snippet, not a
  fetch. Not cited anywhere above.
- **Newer SH0ES values** (reported `73.17 +/- 0.86`, `73.49 +/- 0.93`),
  and arXiv:2603.09457 on `S_8` per-survey significances, and
  arXiv:2511.10631 arguing the DESI evolving-dark-energy preference is
  driven by inter-dataset tension resolution. All from search snippets,
  none fetched. Not relied on above.
- **Journal references not retrieved** for arXiv:0710.5505,
  arXiv:0808.1080, arXiv:0907.3377 and arXiv:1105.0909. The arXiv ids and
  content are retrieved; the volume and page are not, so they are cited
  by arXiv id only.
- **Things I believe but could not source.** That the standard flat-LCDM
  relation `q_0 = (3/2) Omega_M0 - 1` gives `q_0 ~= -0.5` at
  `Omega_M0 = 0.33`: elementary, used in Part 1, tagged `[INFERENCE]`,
  not retrieved in this run. That the LCDM onset of acceleration is near
  `z ~ 0.6`-`0.7`: used in the Part 4 table, tagged `[LEAD]`, not
  retrieved.

## One thing I started building and stopped

While reconciling T8 with O1 it became clear that the natural next move
is to ask what constraint Green & Wald's conditions place on average
spatial curvature specifically, since that is where timescape's weight
sits and their theorems address `Q`. That is a modification to the
argument, not an audit of it, so it is recorded here as open question 8
and not pursued. Nothing in this output proposes a change to the model.

## What I could not establish, stated plainly

- Whether the clock effect is gauge-invariant. No critic's argument
  retrieved; the proponent concedes the required gauge fails inside
  finite-infinity regions.
- Whether the Buchert backreaction magnitude dispute has a resolution.
  It does not, and both sides say so in different words.
- Whether LTB constraints transfer to timescape. Nobody has asked.
- Timescape's `Omega_b h^2`, `sigma_8`, `S_8`, BBN light-element
  abundances, and any BAO parameter constraint. None exists.
- The free-parameter count of the headline supernova analysis.
- Whether 17-22% Hubble-flow variance is consistent with the measured
  uniformity at 70-100 Mpc.
- The contents of the one third-party review that assesses timescape's
  observational status.
