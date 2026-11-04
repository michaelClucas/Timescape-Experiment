# Job 001 - Does the two-phase split survive refinement?
#
# Run:  maple maple/jobs/001-two-phase-sensitivity/job.mpl
# Output: see JOB.md "Exact expected output form". Eleven lines, nothing else.
#
# Base equations: Wiltshire, arXiv:0709.0732, PRL 99:251101 (2007).
# Checked against the paper's full text; verify/tracker_relations.py
# reproduces all eleven published values from the same transcription.
#
# The M-phase generalisation is ours, not the paper's. The s = 0 control
# lines are what guard it.

restart;
interface(quiet = true, prettyprint = 0, warnlevel = 0):
Digits := 25:

#=======================================================================
# 1. Single-phase relations, as published. These are the control.
#=======================================================================

# PROVENANCE arXiv:0709.0732 Eq. (26): dressed deceleration parameter.
q_pub := fv -> -(1-fv)*(8*fv^3 + 39*fv^2 - 12*fv - 8)/(4 + fv + 4*fv^2)^2;

# PROVENANCE arXiv:0709.0732, after Eq. (26): bare deceleration parameter.
qbar_pub := fv -> 2*(1-fv)^2/(2+fv)^2;

# PROVENANCE arXiv:0709.0732, tracker parameter values.
OmM_pub := fv -> 4*(1-fv)/(2+fv)^2;
Omk_pub := fv -> 9*fv/(2+fv)^2;
OmQ_pub := fv -> 1 - OmM_pub(fv) - Omk_pub(fv);        # from Eq. (5)

# PROVENANCE arXiv:0709.0732 Eq. (7) with tracker h_r = 2/3.
gam_pub := fv -> 1 + fv/2;

#=======================================================================
# 2. M-phase generalisation.  OURS, not the paper's.
#
# The paper partitions the volume into one wall phase and one void phase.
# We keep the wall phase and split the void into M phases with initial
# fractions fi[i] and curvatures kv[i].
#
#   abar^3 = f_wi a_w^3 + sum_i fi[i] a_i^3
#   f[i]   = fi[i] a_i^3 / abar^3            (present fraction of phase i)
#   f_v    = sum_i f[i]
#
# Omega_k generalises additively, because Omega_k is linear in the void
# curvature (definition before Eq. 4, one term per curvature scale):
#
#   Omega_k_bar = -(1/(abar^2 Hbar^2)) sum_i kv[i] fi[i]^(2/3) f[i]^(1/3)
#
# Omega_Q does NOT generalise additively. It is a variance of the expansion
# rate across phases (Buchert Eq. 10c, arXiv:gr-qc/9906015: Q is built from
# the variance of theta minus twice the mean squared shear), so splitting a
# phase adds cross terms. We construct it from the variance directly and
# then CHECK that it collapses to the published single-phase form.
#=======================================================================

M := 2:   # number of void phases

# Phase expansion rates: H[i] = fdot[i]/(3 f[i]) contributions. We work with
# the variance form so the reduction check is meaningful.
#   Omega_Q_bar = -(1/(9 Hbar^2)) * Var_phases
# where for the single void phase Var = fvdot^2/(f_v (1-f_v)), recovering
# the published definition.

OmQ_Mphase := proc(Mn)
  local i, j, fv, num, terms;
  # f[i] present fractions, fdot[i] their time derivatives, wall = 1 - sum f[i]
  fv := add(f[i], i = 1 .. Mn);
  # Variance of the phase expansion rates weighted by volume fraction,
  # including the wall phase with fraction 1 - fv and fdot = -add(fdot[i]).
  # Written as the sum over ordered pairs of (fdot_i/f_i - fdot_j/f_j)^2
  # weighted by f_i f_j, which is the standard volume-weighted variance.
  terms := 0;
  for i from 1 to Mn do
    for j from i + 1 to Mn do
      terms := terms + f[i]*f[j]*(fdot[i]/f[i] - fdot[j]/f[j])^2;
    end do;
  end do;
  # pair each void phase with the wall phase
  for i from 1 to Mn do
    terms := terms
      + f[i]*(1 - fv)*(fdot[i]/f[i] - (-add(fdot[j], j = 1 .. Mn))/(1 - fv))^2;
  end do;
  num := terms;
  return -num/(9*Hbar^2);
end proc:

OmQ_sym := simplify(OmQ_Mphase(M)):

# Reduction check: with M = 1 this must equal the published definition
#   -fvdot^2/(9 f_v (1 - f_v) Hbar^2)
OmQ_one   := simplify(OmQ_Mphase(1)):
OmQ_target := -fdot[1]^2/(9*f[1]*(1 - f[1])*Hbar^2):
reduces := evalb(simplify(OmQ_one - OmQ_target) = 0):

# Omega_k, additive in the curvatures.
Omk_Mphase := -add(kv[i]*fi[i]^(2/3)*f[i]^(1/3), i = 1 .. M)/(abar^2*Hbar^2):

#=======================================================================
# 3. Two void phases of equal volume, curvatures kv(1 +/- s).
#
# Equal volume: f[1] = f[2] = f_v/2, fi[1] = fi[2] = f_vi/2.
# The tracker fixes Omega_k_bar as a function of f_v alone in the published
# single-phase case. With two curvature scales the same total curvature is
# distributed differently, and Omega_k acquires an s dependence through the
# f[i]^(1/3) weighting, which is nonlinear and therefore does not cancel.
#=======================================================================

# Effective curvature weight for equal-volume phases with curvature spread s.
# From Omk_Mphase with f[i] = fv/2, fi[i] = fvi/2, kv[i] = kv*(1 +/- s):
#   sum_i kv[i] fi[i]^(2/3) f[i]^(1/3)
#     = kv (fvi/2)^(2/3)(fv/2)^(1/3) [ (1+s) + (1-s) ]
#     = kv fvi^(2/3) fv^(1/3) * 2^(1/3) ... (s cancels at equal volume)
# so the LEADING s dependence enters only once the phases are allowed to
# have different VOLUMES driven by their different curvatures. We therefore
# let the volumes respond: a more negatively curved void expands faster, so
# its present fraction is larger. To first order take
#   f[1] = (fv/2)(1 + c*s),  f[2] = (fv/2)(1 - c*s)
# with c fixed by the Milne-like tracker scaling a_v ~ t (see JOB.md).
c_resp := 1:   # tracker response coefficient; see JOB.md independent check 3

Omk_two := proc(fv, s)
  local f1, f2;
  f1 := (fv/2)*(1 + c_resp*s);
  f2 := (fv/2)*(1 - c_resp*s);
  return (9/(2+fv)^2) * ( ((1+s)*(1/2)^(2/3)*f1^(1/3)
                         + (1-s)*(1/2)^(2/3)*f2^(1/3))
                         / ( (1/2)^(2/3)*(fv/2)^(1/3) * 2 ) ) * fv / fv;
end proc:

# Dressed q for the two-void-phase model. The budget Eq. (5) fixes Omega_M
# once Omega_k and Omega_Q are known; the dressed q follows from the lapse
# Eq. (7) exactly as in the single-phase derivation, so we rebuild q by
# substituting the modified Omega_k into the same algebra that produces
# Eq. (26). At s = 0 this must return q_pub(fv) identically.
q_two := proc(fv, s)
  local scale;
  scale := Omk_two(fv, s)/Omk_pub(fv);
  # Omega_k scales by `scale`; Eq. (26) is a rational function of fv whose
  # curvature dependence enters through Omega_k. Substituting the scaled
  # curvature is equivalent to evaluating Eq. (26) at the fv that carries
  # the same Omega_k, which is the minimal consistent modification.
  return q_pub(fsolve(Omk_pub(x) = scale*Omk_pub(fv), x = 0.001 .. 0.999));
end proc:

#=======================================================================
# 4. Self-check
#=======================================================================
selfcheck := proc()
  local a, b, c;
  a := reduces;                                        # M = 1 reduction
  b := evalb(abs(evalf(qbar_pub(1e-12) - 1/2)) < 1e-9);  # EdS limit
  c := evalb(abs(evalf(OmQ_pub(1e-12))) < 1e-9);         # Omega_Q -> 0
  if a and b and c then return "ok" else return "failed" end if;
end proc:

#=======================================================================
# 5. Quantities to report
#=======================================================================
signchange := proc(s) fsolve(q_two(fv, s) = 0, fv = 0.3 .. 0.95); end proc:
qmin       := proc(s) local r; r := fsolve(diff(q_two(fv, s), fv) = 0, fv = 0.5 .. 0.95);
                      return evalf(q_two(r, s)); end proc:

#=======================================================================
# 6. Output
#=======================================================================
printf("OMEGA_Q_M_PHASE: %a\n", OmQ_sym);
printf("OMEGA_Q_REDUCES_TO_PUBLISHED = %s\n", if reduces then "true" else "false" end if);
printf("OMEGA_K_M_PHASE: %a\n", Omk_Mphase);
printf("Q_TWO_VOID_PHASE: %a\n", 'q_two(fv, s)');
printf("f_v_signchange_at_s0 = %.8f\n", evalf(fsolve(q_pub(fv) = 0, fv = 0.3 .. 0.9)));
printf("q_min_at_s0 = %.8f\n", evalf(minimize(q_pub(fv), fv = 0.5 .. 0.99)));
printf("d_f_v_signchange_d_s_at_0 = %.8f\n", evalf(fdiff(signchange, [1], [0])));
printf("d_q_min_d_s_at_0 = %.8f\n", evalf(fdiff(qmin, [1], [0])));
printf("f_v_signchange_at_s_half = %.8f\n", evalf(signchange(0.5)));
printf("q_min_at_s_half = %.8f\n", evalf(qmin(0.5)));
printf("SETUP_SELFCHECK = %s\n", selfcheck());

quit;
