"""Job 003 - does the two-phase result survive voids that are not empty?

Run:  .venv/Scripts/python maple/jobs/003-void-matter-refinement/job.py
Output: see JOB.md "Exact expected output form". Nothing else on stdout.

Engine: SymPy (prompts/standing-loop.md constraint 2). Numeric evaluation of
the SymPy expressions uses lambdify + scipy root/minimum finders; the
independent check is verify/void_matter_sensitivity.py, which shares no code.
"""

import warnings

import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize_scalar

warnings.filterwarnings("ignore")

f = sp.symbols("f", positive=True)
t = sp.symbols("t", positive=True)

EQ26 = -(1 - f) * (8 * f**3 + 39 * f**2 - 12 * f - 8) / (4 + f + 4 * f**2) ** 2  # arXiv:0709.0732 Eq. (26)
OMK_TRACKER = 9 * f / (2 + f) ** 2  # arXiv:0709.0732 tracker values


def dressed(aw, phases, tt):
    """Bare and dressed quantities from wall scale factor aw(t) and void phases.

    phases: list of (initial_fraction_weight, a_i(t)). Wall weight is folded in.
    Returns fv, Hbar, gamma, H_dressed, q_dressed as expressions in tt.
    """
    V = aw**3 + sum(w * a**3 for w, a in phases)
    fs = [w * a**3 / V for w, a in phases]
    fv = sum(fs)
    Hw = sp.diff(aw, tt) / aw
    Hs = [sp.diff(a, tt) / a for _, a in phases]
    Hbar = (1 - fv) * Hw + sum(fi * Hi for fi, Hi in zip(fs, Hs))
    gam = Hbar / Hw  # arXiv:0709.0732 Eq. (7): gamma_bar = Hbar / H_w
    H = gam * Hbar - sp.diff(gam, tt)  # dressed a = abar/gamma, d tau = dt/gamma
    q = -1 - gam * sp.diff(H, tt) / H**2
    return fv, Hbar, gam, H, q, V, fs


def in_f(expr, fv):
    sol = sp.solve(sp.Eq(fv, f), t)
    assert len(sol) == 1, sol
    return sp.simplify(expr.subs(t, sol[0]))


# ---------------------------------------------------------------- item 1
R = sp.symbols("R", positive=True)
fv1, Hb1, g1, H1, q1, _, _ = dressed(t ** sp.Rational(2, 3), [(1 / R, t)], t)
ctrl_res = sp.simplify(in_f(q1, fv1) - EQ26)
ctrl_gam = in_f(g1, fv1)
ctrl_ratio = sp.factor(in_f(H1 / Hb1, fv1))
ratio_ok = sp.simplify(ctrl_ratio - (4 * f**2 + f + 4) / (2 * (2 + f))) == 0

# ---------------------------------------------------------------- item 2
l1, l2, w1, w2 = sp.symbols("l1 l2 w1 w2", positive=True)
k1, k2 = -(l1**2), -(l2**2)  # empty phases: a_i = sqrt(-k_i) t
a1, a2 = l1 * t, l2 * t
fv2, Hb2, g2, H2, q2, V2, fs2 = dressed(t ** sp.Rational(2, 3), [(w1, a1), (w2, a2)], t)
abar = V2 ** sp.Rational(1, 3)
# Omega_k_bar by the definition, one term per phase:
#   -k_i fi_i^(2/3) f_i^(1/3) / (abar^2 Hbar^2), with fi_i the weight in abar^3
omk2 = sum(-k * w ** sp.Rational(2, 3) * fi ** sp.Rational(1, 3)
           for k, w, fi in zip((k1, k2), (w1, w2), fs2)) / (abar**2 * Hb2**2)
split_q_res = sp.simplify(in_f(q2, fv2) - EQ26)
split_omk_res = sp.simplify(in_f(omk2, fv2) - OMK_TRACKER)

# ---------------------------------------------------------------- items 3-5
eta, Cv, Rr = sp.symbols("eta C_v R", positive=True)
tv = Cv / 2 * (sp.sinh(eta) - eta)
av = Cv / 2 * (sp.cosh(eta) - 1)  # open FRW, K = 1
aw = tv ** sp.Rational(2, 3)  # EdS wall, C_w = 4/9
dt = sp.diff(tv, eta)
D = lambda x: sp.diff(x, eta) / dt  # noqa: E731
Hv, Hw = D(av) / av, D(aw) / aw
fvN = av**3 / (Rr * aw**3 + av**3)
HbN = fvN * Hv + (1 - fvN) * Hw
gN = HbN / Hw
HN = gN * HbN - D(gN)
qN = -1 - gN * D(HN) / HN**2
rho_v, rho_w = Cv / av**3, sp.Rational(4, 9) / aw**3
delta_v = rho_v / (fvN * rho_v + (1 - fvN) * rho_w) - 1
om_v = Cv / (Cv + av)
num = sp.lambdify((eta, Cv, Rr), [fvN, qN, delta_v, om_v], "numpy", cse=True)

FV0 = 0.695  # arXiv:1311.3787 Table 1


def curve_stats(C, Rv=1.0):
    def F(e):
        return float(num(e, C, Rv)[0])

    def Q(e):
        return float(num(e, C, Rv)[1])

    # bracket the f_v window by bisection in log eta
    def eta_at(fval):
        return np.exp(brentq(lambda le: F(np.exp(le)) - fval, np.log(1e-3), np.log(200.0), xtol=1e-14))

    e_lo, e_hi, e0 = eta_at(0.3), eta_at(0.999), eta_at(FV0)
    grid = np.exp(np.linspace(np.log(e_lo), np.log(e_hi), 4001))
    qs = np.array([Q(e) for e in grid])
    i = int(np.argmin(qs))
    r = minimize_scalar(Q, bounds=(grid[max(i - 1, 0)], grid[min(i + 1, len(grid) - 1)]),
                        method="bounded", options={"xatol": 1e-12})
    sc = np.where(np.diff(np.sign(qs)) != 0)[0]
    fsign = F(brentq(Q, grid[sc[0]], grid[sc[0] + 1], xtol=1e-14)) if len(sc) else float("nan")
    _, q0, d0, o0 = (float(x) for x in num(e0, C, Rv))
    return dict(delta=d0, om=o0, qmin=r.fun, fqmin=F(r.x), fsign=fsign, q0=q0, grid=grid, F=F, Q=Q)


# item 3: scaling (C, R) -> (10 C, 10 R)
base, scaled = curve_stats(1e-2, 1.0), curve_stats(1e-1, 10.0)
fgrid = np.linspace(0.35, 0.99, 200)


def q_on_f(st):
    out = []
    for fval in fgrid:
        e = brentq(lambda le: st["F"](np.exp(le)) - fval, np.log(1e-3), np.log(200.0), xtol=1e-14)
        out.append(st["Q"](np.exp(e)))
    return np.array(out)


scaling = float(np.max(np.abs(q_on_f(base) - q_on_f(scaled))))


# item 4: solve for C giving each target delta_v at f_v = FV0
def c_for_delta(target):
    return np.exp(brentq(lambda lc: curve_stats(np.exp(lc))["delta"] - target,
                         np.log(1e-9), np.log(0.15), xtol=1e-10))


empty = curve_stats(1e-10)
rows = []
for target in (-0.999, -0.99, -0.95, -0.90, -0.85, -0.80):
    rows.append(curve_stats(c_for_delta(target)))


# item 5: thresholds
C_MAX = 0.18  # keeps the early void fraction (9C/4)/(1+9C/4) below 0.3, the window's lower edge


def delta_where(fun, value):
    """delta_v at which fun reaches value; nan if not reached for any C in (1e-9, C_MAX)."""
    g = lambda lc: fun(curve_stats(np.exp(lc))) - value  # noqa: E731
    lo, hi = np.log(1e-9), np.log(C_MAX)
    if np.sign(g(lo)) == np.sign(g(hi)):
        return float("nan")
    return curve_stats(np.exp(brentq(g, lo, hi, xtol=1e-10)))["delta"]


d004 = delta_where(lambda s: s["qmin"] - empty["qmin"], 0.004)
d0215 = delta_where(lambda s: s["qmin"] - empty["qmin"], 0.0215)
dq0 = delta_where(lambda s: s["q0"], 0.0)

ok = (ctrl_res == 0 and sp.simplify(ctrl_gam - (f / 2 + 1)) == 0 and ratio_ok
      and split_q_res == 0 and split_omk_res == 0 and scaling < 1e-8
      and abs(rows[0]["qmin"] - (-0.0430145)) < 1e-3 and abs(rows[0]["fsign"] - 0.586708) < 1e-3)

print(f"CONTROL_EQ26_RESIDUAL: {sp.sstr(ctrl_res)}")
print(f"CONTROL_GAMMA: {sp.sstr(ctrl_gam)}")
print(f"CONTROL_H_DRESSED_OVER_BARE: {sp.sstr(ctrl_ratio)}")
print(f"EMPTY_SPLIT_Q_RESIDUAL: {sp.sstr(split_q_res)}")
print(f"EMPTY_SPLIT_OMK_RESIDUAL: {sp.sstr(split_omk_res)}")
print(f"SCALING_MAX_ABS_DQ = {scaling:.3e}")
for s in rows:
    print(f"VOIDMATTER delta_v={s['delta']:+.6f} Omega_m_v={s['om']:.6f} q_min={s['qmin']:+.6f} "
          f"fv_at_qmin={s['fqmin']:.6f} fv_signchange={s['fsign']:.6f} q_at_fv0={s['q0']:+.6f}")
print(f"DELTA_V_AT_DQMIN_0p004 = {d004:+.6f}")
print(f"DELTA_V_AT_DQMIN_0p0215 = {d0215:+.6f}")
print(f"DELTA_V_AT_Q_FV0_ZERO = {dq0:+.6f}")
print(f"SETUP_SELFCHECK = {'ok' if ok else 'failed'}")
