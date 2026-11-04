# Job 002 - What void curvature does the model actually require?
#
# Run:  maple maple/jobs/002-curvature-budget-requirement/job.mpl
# Output: see JOB.md "Exact expected output form". Nine lines, nothing else.
#
# Equations from Wiltshire, arXiv:0709.0732, PRL 99:251101 (2007), retrieved
# from the paper's full text. The same transcription is validated on eleven
# published values by verify/tracker_relations.py.

restart;
interface(quiet = true, prettyprint = 0, warnlevel = 0):
Digits := 25:

#=======================================================================
# Inputs. Every one carries its source.
#=======================================================================

fv0_fit   := 0.695:        # arXiv:1311.3787 Table 1
Hbar0_kms := 61.7:         # dressed H_0 upper end, Run 01 discrimination table
fv0_lo    := 0.550:        # published spread, Run 01 T13
fv0_hi    := 0.791:        # published spread, Run 01 T13

# f_vi, void fraction at last scattering. NOT fixed by the equations below
# and NOT recorded in Run 01. Assumed here and FLAGGED in the output.
# Prerequisite: retrieve the fitted value from arXiv:1311.3787.
fvi_assumed := 1e-5:
fvi_is_assumed := true:

# Unit conversion. 1 Mpc = 3.0856775814913673e19 km.
km_per_Mpc := 3.0856775814913673e19:
# Hbar0 in units of 1/Mpc: (km/s/Mpc) / (km/Mpc) gives 1/s; multiply by
# c^-1? No: we want inverse length, so divide by c in km/s.
c_kms := 299792.458:
Hbar0_invMpc := Hbar0_kms/c_kms:     # 1/Mpc, since (km/s/Mpc)/(km/s) = 1/Mpc

#=======================================================================
# 1. The two expressions for Omega_k_bar, and the inversion.
#=======================================================================

# PROVENANCE arXiv:0709.0732, tracker parameter values.
Omk_tracker := fv -> 9*fv/(2+fv)^2;

# PROVENANCE arXiv:0709.0732, definition stated before Eq. (4):
#   Omega_k_bar = -k_v f_vi^(2/3) f_v^(1/3) / (abar^2 Hbar^2)
# with k_v < 0 so Omega_k_bar > 0. Normalise abar_0 = 1 at the present
# epoch, which is the paper's convention for the fitted solution.
Omk_def := (kv, fvi, fv, Hbar) -> -kv*fvi^(2/3)*fv^(1/3)/(1^2*Hbar^2);

# Invert for the required k_v:
#   -k_v fvi^(2/3) fv^(1/3) / Hbar^2 = 9 fv/(2+fv)^2
kv_required_sym := solve(
    Omk_def(kv, fvi, fv0, Hbar0) = Omk_tracker(fv0), kv):

kv_req := proc(fv0v, fviv, Hbar0v)
  return evalf(eval(kv_required_sym,
                    [fv0 = fv0v, fvi = fviv, Hbar0 = Hbar0v]));
end proc:

# Curvature radius: R = |k_v|^(-1/2), in Mpc when k_v is in Mpc^-2.
Rcurv := proc(fv0v, fviv, Hbar0v)
  return evalf(1/sqrt(abs(kv_req(fv0v, fviv, Hbar0v))));
end proc:

#=======================================================================
# 2. Implied void density contrast.
#
# The void phase in the tracker is Milne-like, a_v ~ t (PROVENANCE
# arXiv:0709.0732, h_r = 2/3 tracker, a_v = a_v0 t), i.e. empty and
# curvature dominated. The present mean density contrast of the void phase
# relative to the volume average follows from the phase decomposition:
#   delta_v = rho_v/<rho> - 1
# With walls carrying the matter and voids Milne-like, the void matter
# density is set by what the partition leaves in them.
#
# For the tracker the bare matter density is
#   Omega_M_bar0 = 4(1-fv0)/(2+fv0)^2
# all of which sits in the wall phase of volume fraction 1-fv0, so
#   rho_wall/<rho> = 1/(1-fv0)   and   delta_v = -1 exactly in the strict
# Milne limit.
#
# The strict limit is unphysical as a statement about observed voids, which
# have delta ~ -0.85 at their edges, so we report the DEVIATION the model
# tolerates: the void density contrast consistent with the curvature
# requirement if the voids are not exactly empty, parameterised by how much
# matter they may hold before Omega_k_bar0 falls below the tracker value.
#=======================================================================

delta_v_implied := proc(fv0v)
  # Fraction of the bare matter density that may sit in voids while the
  # curvature still supplies Omega_k_bar0. In the strict tracker, zero.
  # Solve Omega_M_bar(void share x) + Omega_k_tracker = 1 for x.
  local OmM, x;
  OmM := 4*(1 - fv0v)/(2 + fv0v)^2;
  x := solve(OmM*xx + Omk_tracker(fv0v) = 1, xx);
  # density contrast of the void phase holding share x of the matter
  return evalf(x/fv0v - 1);
end proc:

#=======================================================================
# 3. Self-check
#=======================================================================
selfcheck := proc()
  local back, lim;
  # (a) substitute k_v back and recover the tracker value to 10 digits
  back := evalf(Omk_def(kv_req(fv0_fit, fvi_assumed, Hbar0_invMpc),
                        fvi_assumed, fv0_fit, Hbar0_invMpc)
                - Omk_tracker(fv0_fit));
  # (b) fv0 -> 0 sends k_v -> 0
  lim := evalf(abs(kv_req(1e-9, fvi_assumed, Hbar0_invMpc)));
  if abs(back) < 1e-10 and lim < 1e-6 then return "ok" else return "failed" end if;
end proc:

#=======================================================================
# 4. Output
#=======================================================================
printf("KV_REQUIRED_SYMBOLIC: %a\n", kv_required_sym);
printf("kv_required_Mpc^-2 = %.8e\n", kv_req(fv0_fit, fvi_assumed, Hbar0_invMpc));
printf("R_curv_Mpc = %.6f\n", Rcurv(fv0_fit, fvi_assumed, Hbar0_invMpc));
printf("delta_v_implied = %.6f\n", delta_v_implied(fv0_fit));
printf("dR_curv_d_fv0_Mpc = %.6f\n",
       evalf(fdiff(x -> Rcurv(x, fvi_assumed, Hbar0_invMpc), [1], [fv0_fit])));
printf("dR_curv_d_fvi_Mpc = %.6e\n",
       evalf(fdiff(x -> Rcurv(fv0_fit, x, Hbar0_invMpc), [1], [fvi_assumed])));
printf("R_curv_at_fv0_0550_Mpc = %.6f\n", Rcurv(fv0_lo, fvi_assumed, Hbar0_invMpc));
printf("R_curv_at_fv0_0791_Mpc = %.6f\n", Rcurv(fv0_hi, fvi_assumed, Hbar0_invMpc));
printf("SETUP_SELFCHECK = %s\n", selfcheck());
if fvi_is_assumed then
  printf("# WARNING f_vi ASSUMED = %a, NOT retrieved; items 2 and 3 are "
         "conditional on it. See JOB.md.\n", fvi_assumed);
end if;

quit;
