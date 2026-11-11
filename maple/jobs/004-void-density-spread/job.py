"""Job 004 - is the void mass fraction enough, or does the spread of void densities matter?

Run:  .venv/Scripts/python maple/jobs/004-void-density-spread/job.py
Output: see JOB.md "Exact expected output form". Nothing else on stdout.

Engine: SymPy for the N-phase dressed q (analytic phase accelerations);
SciPy solve_ivp for the phase scale factors. The independent check is
verify/void_density_spread.py (parametric solutions + finite differences).
"""

import warnings

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

warnings.filterwarnings("ignore")

# ------------------------------------------------- item 1: N-phase dressed q
N = 3  # wall (index 0) + two void sub-phases
f = sp.symbols(f"f0:{N}", positive=True)
H = sp.symbols(f"H0:{N}", positive=True)
Hd = sp.symbols(f"Hd0:{N}")
Hdd = sp.symbols(f"Hdd0:{N}")


def dressed_q(f, H, Hd, Hdd):
    """Dressed q from phase fractions, rates and their first two derivatives.

    df_i/dt = 3 f_i (H_i - Hbar)  (from f_i = w_i a_i^3 / sum_j w_j a_j^3)
    gamma = Hbar / H_wall (arXiv:0709.0732 Eq. 7); dressed H = gamma Hbar - dgamma/dt;
    q = -1 - gamma (dH/dt) / H^2.
    """
    n = len(f)
    Hbar = sum(f[i] * H[i] for i in range(n))
    fd = [3 * f[i] * (H[i] - Hbar) for i in range(n)]
    Hbar_d = sum(fd[i] * H[i] + f[i] * Hd[i] for i in range(n))
    fdd = [3 * fd[i] * (H[i] - Hbar) + 3 * f[i] * (Hd[i] - Hbar_d) for i in range(n)]
    Hbar_dd = sum(fdd[i] * H[i] + 2 * fd[i] * Hd[i] + f[i] * Hdd[i] for i in range(n))
    g = Hbar / H[0]
    g_d = (Hbar_d * H[0] - Hbar * Hd[0]) / H[0] ** 2
    g_dd = (Hbar_dd * H[0] ** 2 - Hbar * Hdd[0] * H[0] - 2 * Hbar_d * Hd[0] * H[0]
            + 2 * Hbar * Hd[0] ** 2) / H[0] ** 3
    Hdr = g * Hbar - g_d
    Hdr_d = g_d * Hbar + g * Hbar_d - g_dd
    return -1 - g * Hdr_d / Hdr**2


# reduction check: wall a = t^(2/3), one empty void a = t  ->  Eq. (26)
t, F = sp.symbols("t F", positive=True)
q2 = dressed_q((1 - F, F), (2 / (3 * t), 1 / t),
               (-2 / (3 * t**2), -1 / t**2), (4 / (3 * t**3), 2 / t**3))
EQ26 = -(1 - F) * (8 * F**3 + 39 * F**2 - 12 * F - 8) / (4 + F + 4 * F**2) ** 2
reduces = sp.simplify(sp.together(q2 - EQ26)) == 0

qN = sp.lambdify((f, H, Hd, Hdd), dressed_q(f, H, Hd, Hdd), "numpy", cse=True)

# ------------------------------------------------- item 2: numerics
FV0, MV = 0.695, 0.0695
JOB003_ROW = (-0.034244, 0.680228, -0.006557)  # delta_v = -0.900000 row


def run(s, t0=1e-9, t1=1e6, n=400001):
    C = (4 / 9) * MV / (1 - MV)
    Cs = np.array([4 / 9, C * (1 + s), C * (1 - s)])  # wall, void 1, void 2
    K = np.array([0.0, 1.0, 1.0])
    X = np.array([1.0, (MV / 2) / (1 - MV), (MV / 2) / (1 - MV)])  # early volume shares, wall = 1
    w = X / ((9 / 4) * Cs)  # w_i (9 C_i / 4) = X_i: early volume share equals mass share

    def rhs(lt, y):
        a = np.exp(y)
        return np.exp(lt) * np.sqrt(Cs / a**3 + K / a**2)

    y0 = np.log((9 * Cs / 4) ** (1 / 3) * t0 ** (2 / 3))
    lt = np.linspace(np.log(t0), np.log(t1), n)
    sol = solve_ivp(rhs, (lt[0], lt[-1]), y0, t_eval=lt, rtol=1e-12, atol=1e-14, method="DOP853")
    a = np.exp(sol.y)
    Hh = np.sqrt(Cs[:, None] / a**3 + K[:, None] / a**2)
    Hd_ = -Hh**2 - Cs[:, None] / (2 * a**3)
    Hdd_ = -2 * Hh * Hd_ + 1.5 * Cs[:, None] * Hh / a**3
    vol = w[:, None] * a**3
    ff = vol / vol.sum(axis=0)
    q = qN(tuple(ff), tuple(Hh), tuple(Hd_), tuple(Hdd_))
    rho = Cs[:, None] / a**3
    rbar = (ff * rho).sum(axis=0)
    delta = rho / rbar - 1
    fv = ff[1] + ff[2]
    m = (fv > 0.3) & (fv < 0.999)
    Fv, Q = fv[m], q[m]
    i = int(np.argmin(Q))
    # parabolic refinement of the minimum
    if 0 < i < len(Q) - 1:
        y1, y2, y3 = Q[i - 1], Q[i], Q[i + 1]
        den = y1 - 2 * y2 + y3
        qmin = y2 - (y1 - y3) ** 2 / (8 * den) if den != 0 else y2
    else:
        qmin = Q[i]
    sc = np.where(np.diff(np.sign(Q)) != 0)[0]
    fs = np.interp(0.0, [Q[sc[0]], Q[sc[0] + 1]], [Fv[sc[0]], Fv[sc[0] + 1]]) if len(sc) else float("nan")
    q0 = float(np.interp(FV0, Fv, Q))
    d1 = float(np.interp(FV0, Fv, delta[1][m]))
    d2 = float(np.interp(FV0, Fv, delta[2][m]))
    return qmin, fs, q0, d1, d2


rows = {s: run(s) for s in (0.0, 0.25, 0.5, 0.9)}
dq = max(abs(r[0] - rows[0.0][0]) for r in rows.values())
r0 = rows[0.0]
ok = reduces and all(abs(x - y) < 2e-4 for x, y in zip(r0[:3], JOB003_ROW))

print(f"SYMBOLIC_Q_REDUCES_TO_JOB003 = {'true' if reduces else 'false'}")
for s, (qm, fs, q0, d1, d2) in rows.items():
    print(f"SPREAD s={s:.2f} q_min={qm:+.6f} fv_signchange={fs:.6f} q_at_fv0={q0:+.6f} "
          f"delta_1={d1:+.6f} delta_2={d2:+.6f}")
print(f"MAX_ABS_DQMIN_OVER_S = {dq:.6f}")
print(f"SETUP_SELFCHECK = {'ok' if ok else 'failed'}")
