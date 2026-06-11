"""parabolic_blowoff_signature d2 features 151-225 — Pipeline 1b-technical (gap-fill extension).

75 NEW hypotheses extending pblo 001-150. Conceptually distinct from existing pblo coverage
AND from 1a counterpart f37_bpsg_001-153.

Bucket plan (151-225):
  A. Fractal & self-similarity (151-158)        — box-count, Higuchi, DFA-alpha, multi-scale
  B. Catastrophe theory & nonlinear topology    — cusp fit, Hopf/Floquet, stationarity tests
     (159-166)
  C. Spectral / frequency-domain (167-174)      — Lomb-Scargle, spectral entropy, flatness
  D. State-space / Bayesian (175-182)           — Kalman cv/ca, BOCPD posterior, HMM regimes
  E. Spline & nonparametric (183-190)           — B-spline/LOWESS/Chebyshev/Bernstein/P-spline
  F. SSA / EMD extensions (191-196)             — SSA reconstruction, EMD higher IMFs
  G. Volume-weighted parabolic confluence       — VW polynomial fits, divergences, cluster
     (197-204)
  H. Multi-window curvature ANOVA / dispersion  — sub-window ANOVA F, skew/kurt, consensus
     (205-210)
  I. Pre-onset / post-peak (211-215)            — compression, decay half-life, buildup
  J. Robust narrow composites (216-225)         — multi-method joint scores

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods, no centered
windows, no .shift(N). Self-contained helpers — no cross-family imports. No external scientific
deps beyond numpy + pandas.

Technique citations in docstrings:
  - Higuchi (1988) fractal dimension; Hurst R/S — see HFD ≈ 2-H.
  - Zeeman/Thom cusp catastrophe (1976/1977) — bifurcation factor β separates modes.
  - Sornette LPPL — augmented by alternative power-law fits.
  - Lomb-Scargle (1976/1982) — unevenly-sampled periodogram (used as residual periodogram).
  - Adams & MacKay (2007) — Bayesian Online Changepoint Detection (BOCPD) hazard rate λ.
  - SSA — Broomhead & King (1986); diagonal averaging trend extraction.
  - EMD — Huang (1998); higher IMF ratios as residual-cycle complexity proxies.
"""


import numpy as np


import pandas as pd


YDAYS = 252


QDAYS = 63


MDAYS = 21


WDAYS = 5


DDAYS_2Y = 504


DDAYS_3Y = 756


DDAYS_5Y = 1260


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _poly_coef(w, deg, idx):
    valid = ~np.isnan(w)
    n = int(valid.sum())
    if n < (deg + 2):
        return np.nan
    x = np.arange(len(w), dtype=float)
    if not valid.all():
        x = x[valid]
        w = w[valid]
    try:
        c = np.polyfit(x, w, deg)
        return float(c[idx])
    except Exception:
        return np.nan


def _poly_residuals(w, deg):
    valid = ~np.isnan(w)
    n = int(valid.sum())
    if n < (deg + 2):
        return None
    x = np.arange(len(w), dtype=float)
    yv = w
    if not valid.all():
        x = x[valid]
        yv = w[valid]
    try:
        c = np.polyfit(x, yv, deg)
        yhat = np.polyval(c, x)
        return yv - yhat
    except Exception:
        return None


def _higuchi_fd(w, kmax=8):
    """Higuchi (1988) fractal dimension on a 1-D array. HFD ~ 2 - H.

    Returns slope of log(L(k)) vs log(1/k) over k in [1, kmax].
    """
    valid = ~np.isnan(w)
    if valid.sum() < (2 * kmax + 4):
        return np.nan
    x = w[valid].astype(float)
    N = len(x)
    Lk = np.zeros(kmax, dtype=float)
    for k in range(1, kmax + 1):
        Lm = []
        for m in range(k):
            idxs = np.arange(m, N, k)
            if len(idxs) < 2:
                continue
            diffs = np.abs(np.diff(x[idxs]))
            denom = ((N - 1) // k) * k
            if denom <= 0 or len(diffs) == 0:
                continue
            Lm.append((diffs.sum() * (N - 1)) / (denom * len(diffs)))
        if len(Lm) == 0:
            return np.nan
        Lk[k - 1] = np.mean(Lm)
    pos = Lk > 0
    if pos.sum() < 3:
        return np.nan
    ks = np.arange(1, kmax + 1, dtype=float)[pos]
    try:
        slope = np.polyfit(np.log(1.0 / ks), np.log(Lk[pos]), 1)[0]
        return float(slope)
    except Exception:
        return np.nan


def _box_count_fd(w, n_scales=6):
    """Box-counting fractal dimension on a 1-D signal: count boxes covering the
    graph at multiple scales, regress log(N) on log(1/eps)."""
    valid = ~np.isnan(w)
    if valid.sum() < 16:
        return np.nan
    x = w[valid].astype(float)
    n = len(x)
    rng = x.max() - x.min()
    if rng <= 0 or not np.isfinite(rng):
        return np.nan
    xn = (x - x.min()) / rng
    log_inv_eps = []
    log_N = []
    for s in range(n_scales):
        eps = 1.0 / (2 ** (s + 1))
        if eps * n < 1:
            break
        cell_x = np.floor(np.arange(n) / max(int(np.ceil(eps * n)), 1)).astype(int)
        cell_y = np.floor(xn / eps).astype(int)
        keys = cell_x * (10 ** 6) + cell_y
        N = len(np.unique(keys))
        if N <= 0:
            continue
        log_inv_eps.append(np.log(1.0 / eps))
        log_N.append(np.log(N))
    if len(log_N) < 3:
        return np.nan
    try:
        return float(np.polyfit(log_inv_eps, log_N, 1)[0])
    except Exception:
        return np.nan


def _dfa_alpha(w, scales=None):
    """Detrended Fluctuation Analysis (DFA) exponent alpha. Cumulative sum of
    mean-centered series, segment-wise linear detrending, log-log slope of
    RMS fluctuation vs scale."""
    valid = ~np.isnan(w)
    if valid.sum() < 32:
        return np.nan
    x = w[valid].astype(float)
    N = len(x)
    y = np.cumsum(x - x.mean())
    if scales is None:
        scales = [4, 8, 16, 32]
        if N >= 96:
            scales.append(64)
    Fs = []
    use_scales = []
    for n in scales:
        if N // n < 2:
            continue
        nseg = N // n
        F2 = 0.0
        cnt = 0
        for i in range(nseg):
            seg = y[i * n:(i + 1) * n]
            t = np.arange(n, dtype=float)
            try:
                c = np.polyfit(t, seg, 1)
                trend = np.polyval(c, t)
                F2 += ((seg - trend) ** 2).mean()
                cnt += 1
            except Exception:
                pass
        if cnt > 0 and F2 > 0:
            Fs.append(np.sqrt(F2 / cnt))
            use_scales.append(n)
    if len(Fs) < 3:
        return np.nan
    try:
        return float(np.polyfit(np.log(use_scales), np.log(Fs), 1)[0])
    except Exception:
        return np.nan


def f02_pblo_151_box_count_fd_log_close_63d_d2(close: pd.Series) -> pd.Series:
    """Box-counting fractal dimension on log-close (63d). Higher = more complex,
    less smooth blowoff trajectory."""
    lc = _safe_log(close)
    out = lc.rolling(63, min_periods=24).apply(lambda w: _box_count_fd(w), raw=True)
    return (out).diff().diff()


def f02_pblo_152_box_count_fd_log_close_252d_d2(close: pd.Series) -> pd.Series:
    """Box-counting fractal dimension on log-close (252d)."""
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=64).apply(lambda w: _box_count_fd(w), raw=True)
    return (out).diff().diff()


def f02_pblo_152_box_count_fd_log_close_252d(close: pd.Series) -> pd.Series:
    """Box-counting fractal dimension on log-close (252d)."""
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=64).apply(lambda w: _box_count_fd(w), raw=True)
    return out


def f02_pblo_153_box_count_fd_log_close_504d_d2(close: pd.Series) -> pd.Series:
    """Box-counting fractal dimension on log-close (504d)."""
    lc = _safe_log(close)
    out = lc.rolling(504, min_periods=126).apply(lambda w: _box_count_fd(w), raw=True)
    return (out).diff().diff()


def f02_pblo_154_higuchi_fd_log_returns_252d_d2(close: pd.Series) -> pd.Series:
    """Higuchi (1988) fractal dimension on log-returns over 252d. HFD ≈ 2-H."""
    lr = _safe_log(close).diff()
    out = lr.rolling(252, min_periods=64).apply(lambda w: _higuchi_fd(w, kmax=8), raw=True)
    return (out).diff().diff()


def f02_pblo_155_dfa_alpha_log_returns_252d_d2(close: pd.Series) -> pd.Series:
    """Detrended Fluctuation Analysis exponent alpha on log-returns (252d).
    Alpha ~ 0.5 random walk, > 0.5 persistent (parabolic blowoff tends > 0.5)."""
    lr = _safe_log(close).diff()
    out = lr.rolling(252, min_periods=96).apply(lambda w: _dfa_alpha(w), raw=True)
    return (out).diff().diff()


def f02_pblo_155_dfa_alpha_log_returns_252d(close: pd.Series) -> pd.Series:
    """Detrended Fluctuation Analysis exponent alpha on log-returns (252d).
    Alpha ~ 0.5 random walk, > 0.5 persistent (parabolic blowoff tends > 0.5)."""
    lr = _safe_log(close).diff()
    out = lr.rolling(252, min_periods=96).apply(lambda w: _dfa_alpha(w), raw=True)
    return out


def f02_pblo_156_multi_scale_fd_consensus_252d_d2(close: pd.Series) -> pd.Series:
    """Consensus of three fractal-dim estimators (box-count, Higuchi, DFA-derived)
    on log-close/log-returns. Returns mean of standardized values."""
    lc = _safe_log(close)
    lr = lc.diff()
    bc = lc.rolling(252, min_periods=84).apply(lambda w: _box_count_fd(w), raw=True)
    hg = lr.rolling(252, min_periods=84).apply(lambda w: _higuchi_fd(w, kmax=8), raw=True)
    da = lr.rolling(252, min_periods=96).apply(lambda w: _dfa_alpha(w), raw=True)
    # invert DFA-alpha so all three move in same direction (high alpha => low complexity).
    da_inv = 2.0 - da
    zb = _rolling_zscore(bc, 504)
    zh = _rolling_zscore(hg, 504)
    zd = _rolling_zscore(da_inv, 504)
    parts = pd.concat([zb.rename(0), zh.rename(1), zd.rename(2)], axis=1)
    return (parts.mean(axis=1)).diff().diff()


def f02_pblo_157_self_similar_rs_exponent_252d_d2(close: pd.Series) -> pd.Series:
    """Mandelbrot R/S analog: log-log slope of R/S vs sub-window size,
    distinct from a standard Hurst by using sub-windows of geometric scales
    on absolute returns (volatility self-similarity, not return self-similarity)."""
    ar = _safe_log(close).diff().abs()
    def _rs(w):
        valid = ~np.isnan(w)
        if valid.sum() < 32:
            return np.nan
        x = w[valid].astype(float)
        N = len(x)
        scales = [n for n in [8, 16, 32, 64, 128] if N // n >= 2]
        if len(scales) < 3:
            return np.nan
        rs_vals = []
        for n in scales:
            nseg = N // n
            rss = []
            for i in range(nseg):
                seg = x[i * n:(i + 1) * n]
                m = seg.mean()
                y = np.cumsum(seg - m)
                r = y.max() - y.min()
                s = seg.std()
                if s > 0:
                    rss.append(r / s)
            if len(rss) > 0:
                rs_vals.append(np.mean(rss))
            else:
                rs_vals.append(np.nan)
        rs_arr = np.array(rs_vals)
        good = ~np.isnan(rs_arr) & (rs_arr > 0)
        if good.sum() < 3:
            return np.nan
        try:
            sc = np.array(scales, dtype=float)[good]
            return float(np.polyfit(np.log(sc), np.log(rs_arr[good]), 1)[0])
        except Exception:
            return np.nan
    out = ar.rolling(252, min_periods=96).apply(_rs, raw=True)
    return (out).diff().diff()


def f02_pblo_158_fractal_dim_acceleration_252d_d2(close: pd.Series) -> pd.Series:
    """Acceleration (2nd diff over 21d) of the rolling box-count fractal dim.
    Captures whether complexity is rising fast (often pre-break) vs steady."""
    lc = _safe_log(close)
    fd = lc.rolling(252, min_periods=84).apply(lambda w: _box_count_fd(w), raw=True)
    out = fd.diff(21).diff(21)
    return (out).diff().diff()


def _cusp_fit_residual(w):
    """Fit cusp catastrophe potential V(z) = z^4/4 - beta*z^2/2 - alpha*z to
    standardized series via least-squares on derivative dV/dz = 0.
    Returns RSS of the equilibrium-fit residuals."""
    valid = ~np.isnan(w)
    if valid.sum() < 30:
        return np.nan
    x = w[valid].astype(float)
    if x.std() <= 0:
        return np.nan
    z = (x - x.mean()) / x.std()
    # equilibrium of cusp: z^3 - beta*z - alpha = 0
    # treat as regression: z^3 = beta*z + alpha + e, OLS on [z, 1].
    try:
        A = np.column_stack([z, np.ones_like(z)])
        sol, *_ = np.linalg.lstsq(A, z ** 3, rcond=None)
        resid = z ** 3 - A.dot(sol)
        return float((resid ** 2).sum())
    except Exception:
        return np.nan


def _cusp_beta(w):
    """Cusp bifurcation factor beta (from equilibrium regression).
    beta > 0 => bistable / catastrophe domain."""
    valid = ~np.isnan(w)
    if valid.sum() < 30:
        return np.nan
    x = w[valid].astype(float)
    if x.std() <= 0:
        return np.nan
    z = (x - x.mean()) / x.std()
    try:
        A = np.column_stack([z, np.ones_like(z)])
        sol, *_ = np.linalg.lstsq(A, z ** 3, rcond=None)
        return float(sol[0])
    except Exception:
        return np.nan


def _cusp_alpha(w):
    """Cusp asymmetric (skewness-like) factor alpha."""
    valid = ~np.isnan(w)
    if valid.sum() < 30:
        return np.nan
    x = w[valid].astype(float)
    if x.std() <= 0:
        return np.nan
    z = (x - x.mean()) / x.std()
    try:
        A = np.column_stack([z, np.ones_like(z)])
        sol, *_ = np.linalg.lstsq(A, z ** 3, rcond=None)
        return float(sol[1])
    except Exception:
        return np.nan


def f02_pblo_159_cusp_fit_residual_252d_d2(close: pd.Series) -> pd.Series:
    """Zeeman/Thom cusp catastrophe fit RSS on standardized log-close (252d).
    Lower RSS = better fit to bistable potential; large drops signal regime shift."""
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=64).apply(_cusp_fit_residual, raw=True)
    return (out).diff().diff()


def f02_pblo_160_cusp_distance_to_bifurcation_252d_d2(close: pd.Series) -> pd.Series:
    """Distance to bifurcation set: discriminant D = 27*alpha^2 - 4*beta^3.
    D > 0 => mono-stable, D < 0 => bistable region. Returns D."""
    lc = _safe_log(close)
    beta = lc.rolling(252, min_periods=64).apply(_cusp_beta, raw=True)
    alpha = lc.rolling(252, min_periods=64).apply(_cusp_alpha, raw=True)
    return (27.0 * alpha ** 2 - 4.0 * beta ** 3).diff().diff()


def f02_pblo_160_cusp_distance_to_bifurcation_252d(close: pd.Series) -> pd.Series:
    """Distance to bifurcation set: discriminant D = 27*alpha^2 - 4*beta^3.
    D > 0 => mono-stable, D < 0 => bistable region. Returns D."""
    lc = _safe_log(close)
    beta = lc.rolling(252, min_periods=64).apply(_cusp_beta, raw=True)
    alpha = lc.rolling(252, min_periods=64).apply(_cusp_alpha, raw=True)
    return 27.0 * alpha ** 2 - 4.0 * beta ** 3


def f02_pblo_161_cusp_control_beta_252d_d2(close: pd.Series) -> pd.Series:
    """Cusp bifurcation control variable beta (252d). Positive & rising = entering
    catastrophe domain."""
    lc = _safe_log(close)
    return (lc.rolling(252, min_periods=64).apply(_cusp_beta, raw=True)).diff().diff()


def f02_pblo_162_cusp_control_alpha_252d_d2(close: pd.Series) -> pd.Series:
    """Cusp asymmetric control variable alpha (252d). Sign indicates which
    stable branch dominates."""
    lc = _safe_log(close)
    return (lc.rolling(252, min_periods=64).apply(_cusp_alpha, raw=True)).diff().diff()


def f02_pblo_163_hopf_floquet_proxy_63d_d2(close: pd.Series) -> pd.Series:
    """Floquet multiplier proxy for Hopf bifurcation: largest absolute eigenvalue
    of 2x2 transition matrix fit by OLS on (r_t, r_{t-1}) -> (r_{t+1}, r_t).
    |lambda| -> 1 from below = oscillation onset."""
    lr = _safe_log(close).diff()
    def _floq(w):
        valid = ~np.isnan(w)
        if valid.sum() < 20:
            return np.nan
        r = w[valid].astype(float)
        if len(r) < 4:
            return np.nan
        # build VAR(1) on x_t = [r_t, r_{t-1}]
        x = np.column_stack([r[1:-1], r[:-2]])
        y = np.column_stack([r[2:], r[1:-1]])
        try:
            # A^T solves (X A^T) = Y in lstsq sense
            sol, *_ = np.linalg.lstsq(x, y, rcond=None)
            A = sol.T
            evals = np.linalg.eigvals(A)
            return float(np.max(np.abs(evals)))
        except Exception:
            return np.nan
    return (lr.rolling(63, min_periods=24).apply(_floq, raw=True)).diff().diff()


def f02_pblo_164_adf_proxy_first_diff_log_close_252d_d2(close: pd.Series) -> pd.Series:
    """ADF-style t-statistic proxy: OLS of d(lr_t) on lr_{t-1} (no constant).
    Strongly negative => stationary returns (random walk null rejected);
    around zero => non-stationary returns (parabolic drift accumulating)."""
    lr = _safe_log(close).diff()
    def _adf(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        r = w[valid].astype(float)
        if len(r) < 4:
            return np.nan
        y = np.diff(r)
        x = r[:-1]
        if x.std() <= 0 or len(y) < 5:
            return np.nan
        try:
            xm = x.mean(); ym = y.mean()
            beta = ((x - xm) * (y - ym)).sum() / ((x - xm) ** 2).sum()
            yhat = beta * (x - xm) + ym
            resid = y - yhat
            sigma2 = (resid ** 2).sum() / max(len(y) - 1, 1)
            se = np.sqrt(sigma2 / ((x - xm) ** 2).sum())
            return float(beta / se) if se > 0 else np.nan
        except Exception:
            return np.nan
    return (lr.rolling(252, min_periods=64).apply(_adf, raw=True)).diff().diff()


def f02_pblo_165_kpss_proxy_log_curvature_252d_d2(close: pd.Series) -> pd.Series:
    """KPSS-style stationarity statistic on rolling quad-curvature c (sum of
    squared partial sums / variance / N^2). Large => non-stationary curvature
    (unit-root-like behavior in c)."""
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=24).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    def _kpss(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        x = w[valid].astype(float)
        x = x - x.mean()
        S = np.cumsum(x)
        v = (x ** 2).mean()
        if v <= 0:
            return np.nan
        N = len(x)
        return float((S ** 2).sum() / (N ** 2 * v))
    return (c.rolling(252, min_periods=84).apply(_kpss, raw=True)).diff().diff()


def f02_pblo_166_variance_ratio_test_deviation_252d_d2(close: pd.Series) -> pd.Series:
    """Variance-ratio test (Lo & MacKinlay): |VR(q) - 1| where VR(q) =
    var(q-period returns) / (q * var(1-period returns)). Deviation from 1 =>
    deviation from random walk. Uses q=5."""
    lr = _safe_log(close).diff()
    def _vr(w):
        valid = ~np.isnan(w)
        if valid.sum() < 50:
            return np.nan
        r = w[valid].astype(float)
        q = 5
        if len(r) < q + 5:
            return np.nan
        v1 = r.var(ddof=1)
        if v1 <= 0:
            return np.nan
        # overlapping q-period returns
        rq = np.array([r[i:i + q].sum() for i in range(len(r) - q + 1)])
        vq = rq.var(ddof=1)
        return float(abs(vq / (q * v1) - 1.0))
    return (lr.rolling(252, min_periods=84).apply(_vr, raw=True)).diff().diff()


def _lomb_scargle_peak(w, freqs):
    """Peak power in Lomb-Scargle periodogram of w at given (angular) freqs."""
    valid = ~np.isnan(w)
    if valid.sum() < 16:
        return np.nan
    y = w[valid].astype(float)
    t = np.arange(len(w), dtype=float)[valid]
    y = y - y.mean()
    if y.std() <= 0:
        return np.nan
    P = np.zeros_like(freqs)
    for i, om in enumerate(freqs):
        c2 = np.cos(2 * om * t).sum()
        s2 = np.sin(2 * om * t).sum()
        tau = 0.5 * np.arctan2(s2, c2 if c2 != 0 else 1e-12) / max(om, 1e-12)
        ct = np.cos(om * (t - tau))
        st = np.sin(om * (t - tau))
        num1 = (y * ct).sum() ** 2; den1 = (ct ** 2).sum()
        num2 = (y * st).sum() ** 2; den2 = (st ** 2).sum()
        if den1 > 0 and den2 > 0:
            P[i] = 0.5 * (num1 / den1 + num2 / den2)
    if not np.isfinite(P).any():
        return np.nan
    return float(np.nanmax(P))


def _fft_power(w):
    """Return (positive-freq) power spectrum of mean-centered series."""
    valid = ~np.isnan(w)
    if valid.sum() < 16:
        return None
    y = w[valid].astype(float)
    y = y - y.mean()
    n = len(y)
    F = np.fft.rfft(y)
    P = (F.real ** 2 + F.imag ** 2)
    return P[1:]  # drop DC


def f02_pblo_167_lomb_scargle_residual_peak_252d_d2(close: pd.Series) -> pd.Series:
    """Lomb-Scargle peak power on log-quad residuals (252d). High peak power =
    a dominant residual oscillation (consistent with LPPL log-periodic structure)."""
    lc = _safe_log(close)
    freqs = np.linspace(2 * np.pi / 60.0, 2 * np.pi / 5.0, 12)
    def _ls(w):
        r = _poly_residuals(w, 2)
        if r is None:
            return np.nan
        return _lomb_scargle_peak(r, freqs)
    return (lc.rolling(252, min_periods=84).apply(_ls, raw=True)).diff().diff()


def f02_pblo_168_spectral_entropy_residuals_252d_d2(close: pd.Series) -> pd.Series:
    """Spectral (Shannon) entropy of normalized FFT power of log-quad residuals.
    Low entropy => concentrated frequency content; high => noise-like."""
    lc = _safe_log(close)
    def _se(w):
        r = _poly_residuals(w, 2)
        if r is None:
            return np.nan
        P = _fft_power(r)
        if P is None or len(P) == 0 or P.sum() <= 0:
            return np.nan
        p = P / P.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum() / np.log(len(p))) if len(p) > 1 else np.nan
    return (lc.rolling(252, min_periods=84).apply(_se, raw=True)).diff().diff()


def f02_pblo_168_spectral_entropy_residuals_252d(close: pd.Series) -> pd.Series:
    """Spectral (Shannon) entropy of normalized FFT power of log-quad residuals.
    Low entropy => concentrated frequency content; high => noise-like."""
    lc = _safe_log(close)
    def _se(w):
        r = _poly_residuals(w, 2)
        if r is None:
            return np.nan
        P = _fft_power(r)
        if P is None or len(P) == 0 or P.sum() <= 0:
            return np.nan
        p = P / P.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum() / np.log(len(p))) if len(p) > 1 else np.nan
    return lc.rolling(252, min_periods=84).apply(_se, raw=True)


def f02_pblo_169_dominant_fft_freq_shift_252d_d2(close: pd.Series) -> pd.Series:
    """Shift in dominant FFT frequency over 252d. Diff of arg-max bin between
    current and 63d-prior 252d-window. Distinct from MESA (1b family 44)."""
    lc = _safe_log(close)
    def _domf(w):
        P = _fft_power(w)
        if P is None or len(P) == 0:
            return np.nan
        return float(np.argmax(P))
    df = lc.rolling(252, min_periods=84).apply(_domf, raw=True)
    return (df - df.shift(63)).diff().diff()


def f02_pblo_170_high_to_low_freq_power_ratio_252d_d2(close: pd.Series) -> pd.Series:
    """Ratio of high-frequency (top 25% bins) to low-frequency (bottom 25%) power
    in FFT of log-close (252d). Rising = noisier; falling = trend dominates."""
    lc = _safe_log(close)
    def _ratio(w):
        P = _fft_power(w)
        if P is None or len(P) < 4:
            return np.nan
        n = len(P)
        lo = P[: max(n // 4, 1)].sum()
        hi = P[-max(n // 4, 1):].sum()
        if lo <= 0:
            return np.nan
        return float(hi / lo)
    return (lc.rolling(252, min_periods=84).apply(_ratio, raw=True)).diff().diff()


def f02_pblo_171_spectral_flatness_252d_d2(close: pd.Series) -> pd.Series:
    """Spectral flatness = geometric mean / arithmetic mean of FFT power on
    log-returns. 1 = white noise, near 0 = pure tone. Falling flatness during
    blowoff = onset of dominant rhythm."""
    lr = _safe_log(close).diff()
    def _flat(w):
        P = _fft_power(w)
        if P is None or len(P) == 0 or (P <= 0).all():
            return np.nan
        P = P[P > 0]
        if len(P) < 2:
            return np.nan
        gm = np.exp(np.log(P).mean())
        am = P.mean()
        return float(gm / am) if am > 0 else np.nan
    return (lr.rolling(252, min_periods=84).apply(_flat, raw=True)).diff().diff()


def f02_pblo_172_periodogram_tail_weight_252d_d2(close: pd.Series) -> pd.Series:
    """Power concentration in high-freq tail (top 1/3 bins / total) of log-returns
    FFT. Higher = more roughness; useful as terminal-noise indicator."""
    lr = _safe_log(close).diff()
    def _tw(w):
        P = _fft_power(w)
        if P is None or len(P) < 3 or P.sum() <= 0:
            return np.nan
        n = len(P)
        return float(P[-(n // 3):].sum() / P.sum())
    return (lr.rolling(252, min_periods=84).apply(_tw, raw=True)).diff().diff()


def f02_pblo_173_multi_resolution_spectral_consensus_252d_d2(close: pd.Series) -> pd.Series:
    """Consensus of spectral entropy across 3 sub-windows (63/126/252).
    Mean of standardized spectral entropies — joint regime indicator."""
    lc = _safe_log(close)
    def _se(w):
        r = _poly_residuals(w, 2)
        if r is None:
            return np.nan
        P = _fft_power(r)
        if P is None or len(P) == 0 or P.sum() <= 0:
            return np.nan
        p = P / P.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum() / np.log(len(p))) if len(p) > 1 else np.nan
    s63 = lc.rolling(63, min_periods=24).apply(_se, raw=True)
    s126 = lc.rolling(126, min_periods=42).apply(_se, raw=True)
    s252 = lc.rolling(252, min_periods=84).apply(_se, raw=True)
    z63 = _rolling_zscore(s63, 504)
    z126 = _rolling_zscore(s126, 504)
    z252 = _rolling_zscore(s252, 504)
    parts = pd.concat([z63.rename(0), z126.rename(1), z252.rename(2)], axis=1)
    return (parts.mean(axis=1)).diff().diff()


def f02_pblo_174_low_freq_dominance_streak_252d_d2(close: pd.Series) -> pd.Series:
    """Longest streak (in 252d) where low-freq power share > 0.6 (low / total).
    Long streak = sustained trend-dominated spectrum, characteristic of
    parabolic build."""
    lc = _safe_log(close)
    def _share(w):
        P = _fft_power(w)
        if P is None or len(P) < 4 or P.sum() <= 0:
            return np.nan
        n = len(P)
        return float(P[: max(n // 4, 1)].sum() / P.sum())
    sh = lc.rolling(63, min_periods=24).apply(_share, raw=True)
    flag = (sh > 0.6).astype(float).where(sh.notna(), np.nan)
    def _streak(w):
        valid = ~np.isnan(w)
        if not valid.any():
            return np.nan
        best = cur = 0
        for v in w[valid]:
            if v > 0.5:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0
        return float(best)
    return (flag.rolling(252, min_periods=84).apply(_streak, raw=True)).diff().diff()


def _kalman_cv_slope(w, q=1e-3, r=1e-2):
    """1-D Kalman filter with constant-velocity (CV) state [pos, vel].
    Returns terminal velocity estimate."""
    valid = ~np.isnan(w)
    if valid.sum() < 10:
        return np.nan
    y = w[valid].astype(float)
    x = np.array([y[0], 0.0])
    P = np.eye(2) * 1.0
    F = np.array([[1.0, 1.0], [0.0, 1.0]])
    H = np.array([[1.0, 0.0]])
    Q = np.array([[q, 0.0], [0.0, q]])
    R = np.array([[r]])
    for yi in y[1:]:
        x = F.dot(x)
        P = F.dot(P).dot(F.T) + Q
        S = H.dot(P).dot(H.T) + R
        K = P.dot(H.T) / S[0, 0]
        innov = yi - H.dot(x)[0]
        x = x + (K * innov).flatten()
        P = (np.eye(2) - K.dot(H)).dot(P)
    return float(x[1])


def _kalman_ca_accel(w, q=1e-4, r=1e-2):
    """1-D Kalman filter with constant-acceleration (CA) state [pos, vel, acc].
    Returns terminal acceleration estimate."""
    valid = ~np.isnan(w)
    if valid.sum() < 10:
        return np.nan
    y = w[valid].astype(float)
    x = np.array([y[0], 0.0, 0.0])
    P = np.eye(3) * 1.0
    F = np.array([[1.0, 1.0, 0.5], [0.0, 1.0, 1.0], [0.0, 0.0, 1.0]])
    H = np.array([[1.0, 0.0, 0.0]])
    Q = np.eye(3) * q
    R = np.array([[r]])
    for yi in y[1:]:
        x = F.dot(x)
        P = F.dot(P).dot(F.T) + Q
        S = H.dot(P).dot(H.T) + R
        K = P.dot(H.T) / S[0, 0]
        innov = yi - H.dot(x)[0]
        x = x + (K * innov).flatten()
        P = (np.eye(3) - K.dot(H)).dot(P)
    return float(x[2])


def _kalman_cv_innov_var(w, q=1e-3, r=1e-2):
    """Innovation (one-step pred error) variance from CV Kalman filter."""
    valid = ~np.isnan(w)
    if valid.sum() < 10:
        return np.nan
    y = w[valid].astype(float)
    x = np.array([y[0], 0.0])
    P = np.eye(2) * 1.0
    F = np.array([[1.0, 1.0], [0.0, 1.0]])
    H = np.array([[1.0, 0.0]])
    Q = np.array([[q, 0.0], [0.0, q]])
    R = np.array([[r]])
    innovs = []
    for yi in y[1:]:
        x = F.dot(x)
        P = F.dot(P).dot(F.T) + Q
        S = H.dot(P).dot(H.T) + R
        K = P.dot(H.T) / S[0, 0]
        innov = yi - H.dot(x)[0]
        innovs.append(innov)
        x = x + (K * innov).flatten()
        P = (np.eye(2) - K.dot(H)).dot(P)
    if len(innovs) < 3:
        return np.nan
    return float(np.var(innovs))


def f02_pblo_175_kalman_cv_terminal_velocity_252d_d2(close: pd.Series) -> pd.Series:
    """Constant-velocity Kalman filter terminal velocity on log-close (252d).
    Higher = stronger sustained trend."""
    lc = _safe_log(close)
    return (lc.rolling(252, min_periods=64).apply(_kalman_cv_slope, raw=True)).diff().diff()


def f02_pblo_176_kalman_ca_terminal_acceleration_252d_d2(close: pd.Series) -> pd.Series:
    """Constant-acceleration Kalman filter terminal acceleration on log-close
    (252d). Persistent positive = state-space parabolic blowoff signal."""
    lc = _safe_log(close)
    return (lc.rolling(252, min_periods=64).apply(_kalman_ca_accel, raw=True)).diff().diff()


def f02_pblo_176_kalman_ca_terminal_acceleration_252d(close: pd.Series) -> pd.Series:
    """Constant-acceleration Kalman filter terminal acceleration on log-close
    (252d). Persistent positive = state-space parabolic blowoff signal."""
    lc = _safe_log(close)
    return lc.rolling(252, min_periods=64).apply(_kalman_ca_accel, raw=True)


def f02_pblo_177_kalman_innovation_variance_252d_d2(close: pd.Series) -> pd.Series:
    """Variance of one-step Kalman (CV) innovations on log-close (252d).
    Rising innovation variance = model surprise = regime shift."""
    lc = _safe_log(close)
    return (lc.rolling(252, min_periods=64).apply(_kalman_cv_innov_var, raw=True)).diff().diff()


def _bocpd_terminal_post(w, hazard=1.0 / 100.0):
    """Simplified Adams-MacKay BOCPD — Gaussian observation model with running
    mean/var. Returns posterior P(r_t == 0) at the end of the window (i.e.
    probability that the most recent point is a changepoint)."""
    valid = ~np.isnan(w)
    if valid.sum() < 20:
        return np.nan
    y = w[valid].astype(float)
    n = len(y)
    # run length posterior R[t][r]; we just keep current row
    R = np.array([1.0])  # P(r_0 = 0) = 1
    # sufficient stats for each run length: mean, M2, count
    means = np.array([0.0])
    M2 = np.array([0.0])
    counts = np.array([0.0])
    for i in range(n):
        yi = y[i]
        # predictive prob under Student-t approximation as Gaussian with running
        # mean/var (kappa=1) — keep simple and fast.
        var = np.where(counts > 1, M2 / np.maximum(counts - 1, 1.0), 1.0) + 1e-6
        pred = (1.0 / np.sqrt(2 * np.pi * var)) * np.exp(-0.5 * (yi - means) ** 2 / var)
        # grow + cp
        new_R = np.empty(len(R) + 1)
        new_R[1:] = R * pred * (1.0 - hazard)
        new_R[0] = (R * pred * hazard).sum()
        s = new_R.sum()
        if s <= 0 or not np.isfinite(s):
            return np.nan
        new_R /= s
        # update sufficient stats: shift to longer run, prepend fresh
        new_counts = np.empty(len(counts) + 1)
        new_means = np.empty(len(means) + 1)
        new_M2 = np.empty(len(M2) + 1)
        new_counts[0] = 0.0; new_means[0] = 0.0; new_M2[0] = 0.0
        new_counts[1:] = counts + 1.0
        delta = yi - means
        new_means[1:] = means + delta / np.maximum(new_counts[1:], 1.0)
        delta2 = yi - new_means[1:]
        new_M2[1:] = M2 + delta * delta2
        R = new_R; means = new_means; M2 = new_M2; counts = new_counts
        # cap run length to keep memory bounded
        if len(R) > 200:
            R = R[:200]; means = means[:200]; M2 = M2[:200]; counts = counts[:200]
            R = R / R.sum()
    return float(R[0])


def f02_pblo_178_bocpd_posterior_changepoint_252d_d2(close: pd.Series) -> pd.Series:
    """Adams-MacKay BOCPD posterior P(changepoint at t) on log-returns (252d window,
    hazard = 1/100). Spikes mark structural breaks."""
    lr = _safe_log(close).diff()
    return (lr.rolling(252, min_periods=64).apply(_bocpd_terminal_post, raw=True)).diff().diff()


def f02_pblo_179_bocpd_changepoint_intensity_252d_d2(close: pd.Series) -> pd.Series:
    """BOCPD-derived intensity: rolling 21d sum of changepoint-posterior values
    over a 252d trailing window."""
    lr = _safe_log(close).diff()
    cp = lr.rolling(252, min_periods=64).apply(_bocpd_terminal_post, raw=True)
    return (cp.rolling(21, min_periods=7).sum()).diff().diff()


def f02_pblo_179_bocpd_changepoint_intensity_252d(close: pd.Series) -> pd.Series:
    """BOCPD-derived intensity: rolling 21d sum of changepoint-posterior values
    over a 252d trailing window."""
    lr = _safe_log(close).diff()
    cp = lr.rolling(252, min_periods=64).apply(_bocpd_terminal_post, raw=True)
    return cp.rolling(21, min_periods=7).sum()


def _posterior_accel_regime(w):
    """Bayesian 2-state mixture: state 0 = no accel (c ~ N(0, s0)), state 1 = accel
    (c ~ N(mu1>0, s1)). EM 8 iters; returns posterior P(state=1) at last point."""
    valid = ~np.isnan(w)
    if valid.sum() < 20:
        return np.nan
    x = w[valid].astype(float)
    if x.std() <= 0:
        return np.nan
    # init: separate mean / std for top quartile vs bottom
    q75 = np.quantile(x, 0.75); q25 = np.quantile(x, 0.25)
    mu0, mu1 = q25, max(q75, q25 + 1e-6)
    s0 = max(x.std() / 2, 1e-6); s1 = max(x.std() / 2, 1e-6)
    pi1 = 0.3
    for _ in range(8):
        p0 = (1 - pi1) * (1.0 / np.sqrt(2 * np.pi) / s0) * np.exp(-0.5 * ((x - mu0) / s0) ** 2)
        p1 = pi1 * (1.0 / np.sqrt(2 * np.pi) / s1) * np.exp(-0.5 * ((x - mu1) / s1) ** 2)
        tot = p0 + p1 + 1e-30
        gam1 = p1 / tot
        gam0 = 1.0 - gam1
        w0 = gam0.sum(); w1 = gam1.sum()
        if w0 < 1e-6 or w1 < 1e-6:
            break
        mu0 = (gam0 * x).sum() / w0
        mu1 = (gam1 * x).sum() / w1
        s0 = np.sqrt(max((gam0 * (x - mu0) ** 2).sum() / w0, 1e-12))
        s1 = np.sqrt(max((gam1 * (x - mu1) ** 2).sum() / w1, 1e-12))
        pi1 = w1 / len(x)
    # final P(state=1 | last x)
    xt = x[-1]
    p0 = (1 - pi1) * (1.0 / np.sqrt(2 * np.pi) / s0) * np.exp(-0.5 * ((xt - mu0) / s0) ** 2)
    p1 = pi1 * (1.0 / np.sqrt(2 * np.pi) / s1) * np.exp(-0.5 * ((xt - mu1) / s1) ** 2)
    return float(p1 / (p0 + p1 + 1e-30))


def f02_pblo_180_posterior_accel_regime_prob_252d_d2(close: pd.Series) -> pd.Series:
    """Posterior P(accel regime | last curvature) from 2-state Gaussian mixture
    fit on rolling quad c values (252d window)."""
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=24).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    return (c.rolling(252, min_periods=84).apply(_posterior_accel_regime, raw=True)).diff().diff()


def f02_pblo_180_posterior_accel_regime_prob_252d(close: pd.Series) -> pd.Series:
    """Posterior P(accel regime | last curvature) from 2-state Gaussian mixture
    fit on rolling quad c values (252d window)."""
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=24).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    return c.rolling(252, min_periods=84).apply(_posterior_accel_regime, raw=True)


def _hmm_two_state_posterior(w):
    """Compact 2-state HMM (high-vol vs low-vol regime) on returns. Forward
    pass only; returns posterior of high-vol state at the last bar."""
    valid = ~np.isnan(w)
    if valid.sum() < 30:
        return np.nan
    r = w[valid].astype(float)
    if r.std() <= 0:
        return np.nan
    s_lo = max(r.std() / 2, 1e-6)
    s_hi = max(r.std() * 1.5, 1e-6)
    # transition matrix (sticky)
    A = np.array([[0.95, 0.05], [0.10, 0.90]])
    pi = np.array([0.5, 0.5])
    alpha = pi.copy()
    for x in r:
        # emission
        e0 = (1.0 / np.sqrt(2 * np.pi) / s_lo) * np.exp(-0.5 * (x / s_lo) ** 2)
        e1 = (1.0 / np.sqrt(2 * np.pi) / s_hi) * np.exp(-0.5 * (x / s_hi) ** 2)
        e = np.array([e0, e1])
        alpha = (alpha @ A) * e
        s = alpha.sum()
        if s <= 0 or not np.isfinite(s):
            return np.nan
        alpha /= s
    return float(alpha[1])


def f02_pblo_181_hmm_accel_state_posterior_252d_d2(close: pd.Series) -> pd.Series:
    """Compact 2-state HMM posterior P(high-vol | history) on log-returns (252d).
    Distinct from family 35 rvre by using a model-based posterior, not realized
    vol percentile."""
    lr = _safe_log(close).diff()
    return (lr.rolling(252, min_periods=84).apply(_hmm_two_state_posterior, raw=True)).diff().diff()


def f02_pblo_181_hmm_accel_state_posterior_252d(close: pd.Series) -> pd.Series:
    """Compact 2-state HMM posterior P(high-vol | history) on log-returns (252d).
    Distinct from family 35 rvre by using a model-based posterior, not realized
    vol percentile."""
    lr = _safe_log(close).diff()
    return lr.rolling(252, min_periods=84).apply(_hmm_two_state_posterior, raw=True)


def f02_pblo_182_hmm_expected_duration_accel_252d_d2(close: pd.Series) -> pd.Series:
    """Expected duration in accel state from HMM = 1/(1 - A[1,1]) where A[1,1] is
    the self-transition prob of the high-vol state. Here we estimate A[1,1] as
    the average posterior * 0.9 + 0.05 (Bayesian-style) — proxy."""
    p = f02_pblo_181_hmm_accel_state_posterior_252d(close)
    a11 = p.rolling(63, min_periods=21).mean() * 0.9 + 0.05
    return (1.0 / (1.0 - a11.clip(upper=0.999))).diff().diff()


def f02_pblo_183_b_spline_knot_curvature_252d_d2(close: pd.Series) -> pd.Series:
    """Curvature estimate using piecewise-quadratic B-spline at 3 interior knots
    (252d). Returns average 2nd-derivative across knot segments."""
    lc = _safe_log(close)
    def _bsp(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        y = w[valid].astype(float)
        n = len(y)
        knots = [n // 4, n // 2, 3 * n // 4]
        c_acc = 0.0; cnt = 0
        for i in range(len(knots) - 1):
            seg = y[knots[i]:knots[i + 1] + 1]
            if len(seg) < 5:
                continue
            t = np.arange(len(seg), dtype=float)
            try:
                coef = np.polyfit(t, seg, 2)
                c_acc += 2.0 * coef[0]
                cnt += 1
            except Exception:
                pass
        return c_acc / cnt if cnt > 0 else np.nan
    return (lc.rolling(252, min_periods=84).apply(_bsp, raw=True)).diff().diff()


def f02_pblo_183_b_spline_knot_curvature_252d(close: pd.Series) -> pd.Series:
    """Curvature estimate using piecewise-quadratic B-spline at 3 interior knots
    (252d). Returns average 2nd-derivative across knot segments."""
    lc = _safe_log(close)
    def _bsp(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        y = w[valid].astype(float)
        n = len(y)
        knots = [n // 4, n // 2, 3 * n // 4]
        c_acc = 0.0; cnt = 0
        for i in range(len(knots) - 1):
            seg = y[knots[i]:knots[i + 1] + 1]
            if len(seg) < 5:
                continue
            t = np.arange(len(seg), dtype=float)
            try:
                coef = np.polyfit(t, seg, 2)
                c_acc += 2.0 * coef[0]
                cnt += 1
            except Exception:
                pass
        return c_acc / cnt if cnt > 0 else np.nan
    return lc.rolling(252, min_periods=84).apply(_bsp, raw=True)


def f02_pblo_184_smoothing_spline_d2_terminal_63d_d2(close: pd.Series) -> pd.Series:
    """Smoothing-spline approximation: EMA-smoothed log-close, then 5-bar
    finite-difference 2nd derivative at the terminal bar (63d context)."""
    lc = _safe_log(close)
    sm = lc.ewm(span=15, min_periods=8, adjust=False).mean()
    d2 = sm - 2 * sm.shift(5) + sm.shift(10)
    return (d2).diff().diff()


def f02_pblo_185_lowess_residual_std_63d_d2(close: pd.Series) -> pd.Series:
    """LOWESS-style residual std: residuals of log-close minus 21d EMA-of-EMA
    (double-smoothed), then 63d std of these residuals."""
    lc = _safe_log(close)
    e1 = lc.ewm(span=21, min_periods=7, adjust=False).mean()
    e2 = e1.ewm(span=21, min_periods=7, adjust=False).mean()
    return ((lc - e2).rolling(63, min_periods=24).std()).diff().diff()


def f02_pblo_186_chebyshev_t2_coef_252d_d2(close: pd.Series) -> pd.Series:
    """Chebyshev T2 coefficient (2nd-order Chebyshev fit) on standardized log-close
    over 252d. T2 captures parabolic shape on [-1, 1]."""
    lc = _safe_log(close)
    def _cheb(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        y = w[valid].astype(float)
        if y.std() <= 0:
            return np.nan
        y = (y - y.mean()) / y.std()
        n = len(y)
        t = np.linspace(-1.0, 1.0, n)
        # design with T0=1, T1=t, T2=2t^2-1
        T0 = np.ones(n); T1 = t; T2 = 2 * t ** 2 - 1
        A = np.column_stack([T0, T1, T2])
        try:
            sol, *_ = np.linalg.lstsq(A, y, rcond=None)
            return float(sol[2])
        except Exception:
            return np.nan
    return (lc.rolling(252, min_periods=84).apply(_cheb, raw=True)).diff().diff()


def f02_pblo_187_bernstein_polynomial_resid_252d_d2(close: pd.Series) -> pd.Series:
    """Residual std of degree-3 Bernstein polynomial fit on standardized log-close
    (252d). Bernstein basis: B_k(t) = C(3,k) t^k (1-t)^(3-k). Different basis
    from raw polyfit captures shape sensitivity."""
    lc = _safe_log(close)
    def _bern(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        y = w[valid].astype(float)
        if y.std() <= 0:
            return np.nan
        n = len(y)
        t = np.linspace(0.0, 1.0, n)
        B = np.column_stack([
            (1 - t) ** 3,
            3 * t * (1 - t) ** 2,
            3 * t ** 2 * (1 - t),
            t ** 3,
        ])
        try:
            sol, *_ = np.linalg.lstsq(B, y, rcond=None)
            yhat = B.dot(sol)
            return float((y - yhat).std())
        except Exception:
            return np.nan
    return (lc.rolling(252, min_periods=84).apply(_bern, raw=True)).diff().diff()


def f02_pblo_188_p_spline_penalized_curvature_252d_d2(close: pd.Series) -> pd.Series:
    """Penalized-spline curvature proxy: 21-day rolling mean of (log-close minus
    5-day rolling median), then 2nd-difference of that smoothed series. Roughness
    penalty implicit in the median+mean smoothing."""
    lc = _safe_log(close)
    rough = lc - lc.rolling(5, min_periods=3).median()
    sm = rough.rolling(21, min_periods=7).mean()
    base = lc - sm
    return (base.diff().diff().rolling(63, min_periods=24).mean()).diff().diff()


def f02_pblo_189_spline_knot_density_adaptation_252d_d2(close: pd.Series) -> pd.Series:
    """Adaptive knot density: count of sign changes in 21d rolling slope of log-close
    over 252d. Higher count = more knots needed = less parabolic shape."""
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 21)
    sgn = np.sign(sl)
    flips = (sgn != sgn.shift(1)).astype(float).where(sgn.notna() & sgn.shift(1).notna(), np.nan)
    return (flips.rolling(252, min_periods=84).sum()).diff().diff()


def f02_pblo_190_local_quad_slope_of_d2_63d_d2(close: pd.Series) -> pd.Series:
    """Slope (over 21d) of the rolling 5-bar 2nd-derivative of log-close. Positive
    = curvature increasing (parabolic acceleration), negative = curvature falling."""
    lc = _safe_log(close)
    d2 = lc - 2 * lc.shift(5) + lc.shift(10)
    return (_rolling_slope(d2, 21)).diff().diff()


def _ssa_trend_and_resid(w, L=20, ncomp=2):
    """Lightweight SSA: trajectory matrix from window length L, top-ncomp SVD
    components reconstructed via diagonal averaging. Returns (trend, resid)."""
    valid = ~np.isnan(w)
    if valid.sum() < (L + 6):
        return None, None
    x = w[valid].astype(float)
    N = len(x)
    L = min(L, N - 2)
    if L < 5:
        return None, None
    K = N - L + 1
    X = np.zeros((L, K))
    for i in range(L):
        X[i] = x[i:i + K]
    try:
        U, s, Vt = np.linalg.svd(X, full_matrices=False)
        ncomp = min(ncomp, len(s))
        Xr = (U[:, :ncomp] * s[:ncomp]) @ Vt[:ncomp]
    except Exception:
        return None, None
    # diagonal averaging
    trend = np.zeros(N)
    cnt = np.zeros(N)
    for i in range(L):
        for j in range(K):
            trend[i + j] += Xr[i, j]
            cnt[i + j] += 1
    trend = trend / np.maximum(cnt, 1)
    return trend, x - trend


def f02_pblo_191_ssa_trend_residual_at_top_252d_d2(close: pd.Series) -> pd.Series:
    """SSA trend-residual at the terminal bar (252d window, L=20, ncomp=2).
    Large positive = price extension above SSA trend."""
    lc = _safe_log(close)
    def _r(w):
        _, resid = _ssa_trend_and_resid(w, L=20, ncomp=2)
        if resid is None or len(resid) == 0:
            return np.nan
        return float(resid[-1])
    return (lc.rolling(252, min_periods=84).apply(_r, raw=True)).diff().diff()


def f02_pblo_192_ssa_dominant_component_amplitude_252d_d2(close: pd.Series) -> pd.Series:
    """SSA leading-component singular value (252d, L=20). Higher = stronger
    dominant trend-like component."""
    lc = _safe_log(close)
    def _amp(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        x = w[valid].astype(float)
        N = len(x); L = min(20, N - 2)
        if L < 5:
            return np.nan
        K = N - L + 1
        X = np.zeros((L, K))
        for i in range(L):
            X[i] = x[i:i + K]
        try:
            s = np.linalg.svd(X, compute_uv=False)
            return float(s[0])
        except Exception:
            return np.nan
    return (lc.rolling(252, min_periods=84).apply(_amp, raw=True)).diff().diff()


def f02_pblo_193_ssa_reconstruction_error_variance_252d_d2(close: pd.Series) -> pd.Series:
    """Variance of SSA residuals at 252d window (L=20, ncomp=2). Lower => price is
    well-described by 2 SSA components (clean parabolic-style trajectory)."""
    lc = _safe_log(close)
    def _ev(w):
        _, resid = _ssa_trend_and_resid(w, L=20, ncomp=2)
        if resid is None or len(resid) < 3:
            return np.nan
        return float(np.var(resid))
    return (lc.rolling(252, min_periods=84).apply(_ev, raw=True)).diff().diff()


def _emd_one_sift(x, max_iter=10):
    """One IMF via simplified sifting on 1-D array. Returns (imf, residual)."""
    h = x.copy()
    n = len(h)
    for _ in range(max_iter):
        # extrema by local diff sign change
        d = np.diff(h)
        sgn = np.sign(d)
        ext = np.where((sgn[:-1] * sgn[1:]) < 0)[0] + 1
        if len(ext) < 4:
            break
        # split into maxima/minima
        peak_mask = (d[ext - 1] > 0) & (d[ext] < 0)
        trough_mask = (d[ext - 1] < 0) & (d[ext] > 0)
        peaks = ext[peak_mask]; troughs = ext[trough_mask]
        if len(peaks) < 2 or len(troughs) < 2:
            break
        # envelope by linear interpolation
        xs = np.arange(n, dtype=float)
        up = np.interp(xs, peaks.astype(float), h[peaks])
        lo = np.interp(xs, troughs.astype(float), h[troughs])
        mean_env = 0.5 * (up + lo)
        h = h - mean_env
        if np.abs(mean_env).mean() < 1e-6:
            break
    return h, x - h


def f02_pblo_194_emd_imf3_to_imf5_amplitude_ratio_252d_d2(close: pd.Series) -> pd.Series:
    """Ratio of IMF3 amplitude to IMF5 amplitude from simplified EMD (252d).
    Indicates whether mid- or low-freq cycles dominate the residual structure."""
    lc = _safe_log(close)
    def _r(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        x = w[valid].astype(float)
        cur = x.copy()
        amps = []
        for _ in range(5):
            imf, res = _emd_one_sift(cur, max_iter=8)
            amps.append(np.std(imf))
            cur = res
            if np.std(cur) < 1e-8:
                break
        if len(amps) < 5:
            return np.nan
        if amps[4] <= 0:
            return np.nan
        return float(amps[2] / amps[4])
    return (lc.rolling(252, min_periods=84).apply(_r, raw=True)).diff().diff()


def f02_pblo_195_emd_instantaneous_freq_variance_252d_d2(close: pd.Series) -> pd.Series:
    """Variance of instantaneous frequency proxy of IMF1 (zero-cross count in
    21-day rolling sub-windows of 252d sift) — captures rhythm stability."""
    lc = _safe_log(close)
    def _ifv(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        x = w[valid].astype(float)
        imf1, _ = _emd_one_sift(x, max_iter=8)
        # zero-cross count in sub-windows of 21
        zc = []
        sub = 21
        for i in range(0, len(imf1) - sub + 1, sub):
            seg = imf1[i:i + sub]
            sgn = np.sign(seg)
            zc.append(int(((sgn[:-1] * sgn[1:]) < 0).sum()))
        if len(zc) < 3:
            return np.nan
        return float(np.var(zc))
    return (lc.rolling(252, min_periods=84).apply(_ifv, raw=True)).diff().diff()


def f02_pblo_196_emd_trend_acceleration_252d_d2(close: pd.Series) -> pd.Series:
    """Acceleration (2nd-diff over 21d) of the EMD residual trend (after stripping
    top-3 IMFs)."""
    lc = _safe_log(close)
    def _t(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        x = w[valid].astype(float)
        cur = x.copy()
        for _ in range(3):
            imf, res = _emd_one_sift(cur, max_iter=8)
            cur = res
            if np.std(cur) < 1e-8:
                break
        return float(cur[-1] - 2 * cur[-22] + cur[-43]) if len(cur) >= 43 else np.nan
    return (lc.rolling(252, min_periods=84).apply(_t, raw=True)).diff().diff()


def _weighted_quad_c(yv, wv):
    """Weighted quadratic regression coefficient c (y ~ a + b*t + c*t^2).
    yv, wv = aligned arrays; weights wv >= 0."""
    n = len(yv)
    if n < 6:
        return np.nan
    t = np.arange(n, dtype=float)
    A = np.column_stack([np.ones(n), t, t ** 2])
    W = np.diag(wv)
    try:
        AtW = A.T @ W
        sol = np.linalg.solve(AtW @ A, AtW @ yv)
        return float(sol[2])
    except Exception:
        return np.nan


def f02_pblo_197_volume_weighted_quad_c_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted quadratic c on log-close (63d). Each bar weighted by
    volume — emphasizes the curvature happening on heavy-vol bars."""
    lc = _safe_log(close)
    df = pd.concat([lc.rename("y"), volume.rename("v")], axis=1)
    def _f(w_arr):
        # w_arr is 2D? rolling.apply with raw=True works on Series only.
        return np.nan
    out = pd.Series(np.nan, index=lc.index)
    n = 63
    for i in range(n - 1, len(lc)):
        y = lc.iloc[i - n + 1:i + 1].values
        v = volume.iloc[i - n + 1:i + 1].values.astype(float)
        if np.isnan(y).any() or np.isnan(v).any():
            mask = ~np.isnan(y) & ~np.isnan(v)
            if mask.sum() < 21:
                continue
            yv = y[mask]; vv = v[mask]
        else:
            yv = y; vv = v
        vv = np.where(vv > 0, vv, 0.0)
        if vv.sum() <= 0:
            continue
        vv = vv / vv.mean()
        out.iloc[i] = _weighted_quad_c(yv, vv)
    return (out).diff().diff()


def f02_pblo_197_volume_weighted_quad_c_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted quadratic c on log-close (63d). Each bar weighted by
    volume — emphasizes the curvature happening on heavy-vol bars."""
    lc = _safe_log(close)
    df = pd.concat([lc.rename("y"), volume.rename("v")], axis=1)
    def _f(w_arr):
        # w_arr is 2D? rolling.apply with raw=True works on Series only.
        return np.nan
    out = pd.Series(np.nan, index=lc.index)
    n = 63
    for i in range(n - 1, len(lc)):
        y = lc.iloc[i - n + 1:i + 1].values
        v = volume.iloc[i - n + 1:i + 1].values.astype(float)
        if np.isnan(y).any() or np.isnan(v).any():
            mask = ~np.isnan(y) & ~np.isnan(v)
            if mask.sum() < 21:
                continue
            yv = y[mask]; vv = v[mask]
        else:
            yv = y; vv = v
        vv = np.where(vv > 0, vv, 0.0)
        if vv.sum() <= 0:
            continue
        vv = vv / vv.mean()
        out.iloc[i] = _weighted_quad_c(yv, vv)
    return out


def f02_pblo_198_volume_weighted_quad_r2_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Weighted R² of parabolic fit, weights = volume (63d)."""
    lc = _safe_log(close)
    out = pd.Series(np.nan, index=lc.index)
    n = 63
    for i in range(n - 1, len(lc)):
        y = lc.iloc[i - n + 1:i + 1].values
        v = volume.iloc[i - n + 1:i + 1].values.astype(float)
        mask = ~np.isnan(y) & ~np.isnan(v) & (v > 0)
        if mask.sum() < 21:
            continue
        yv = y[mask]; vv = v[mask]
        vv = vv / vv.mean()
        t = np.arange(len(yv), dtype=float)
        A = np.column_stack([np.ones(len(yv)), t, t ** 2])
        W = np.diag(vv)
        try:
            AtW = A.T @ W
            sol = np.linalg.solve(AtW @ A, AtW @ yv)
            yhat = A @ sol
            wmean = (vv * yv).sum() / vv.sum()
            ss_res = (vv * (yv - yhat) ** 2).sum()
            ss_tot = (vv * (yv - wmean) ** 2).sum()
            if ss_tot <= 0:
                continue
            out.iloc[i] = 1.0 - ss_res / ss_tot
        except Exception:
            continue
    return (out).diff().diff()


def f02_pblo_199_volume_weighted_theil_sen_quad_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted Theil-Sen quadratic slope: median of pairwise (y_j-y_i)/(t_j^2-t_i^2)
    weighted by volume product (63d, sub-sampled to keep cost bounded)."""
    lc = _safe_log(close)
    out = pd.Series(np.nan, index=lc.index)
    n = 63
    for i in range(n - 1, len(lc)):
        y = lc.iloc[i - n + 1:i + 1].values
        v = volume.iloc[i - n + 1:i + 1].values.astype(float)
        mask = ~np.isnan(y) & ~np.isnan(v) & (v > 0)
        if mask.sum() < 21:
            continue
        yv = y[mask]; vv = v[mask]
        t = np.arange(len(yv), dtype=float)
        # subsample pair indices: stride of 3 keeps it bounded
        idx = np.arange(0, len(yv), 3)
        slopes = []
        wts = []
        for a in idx:
            for b in idx:
                if b <= a:
                    continue
                dt2 = t[b] ** 2 - t[a] ** 2
                if dt2 <= 0:
                    continue
                slopes.append((yv[b] - yv[a]) / dt2)
                wts.append(vv[a] * vv[b])
        if len(slopes) < 5:
            continue
        s = np.array(slopes); ww = np.array(wts)
        order = np.argsort(s)
        s_sorted = s[order]; w_sorted = ww[order]
        cw = np.cumsum(w_sorted)
        half = cw[-1] / 2.0
        out.iloc[i] = float(s_sorted[np.searchsorted(cw, half)])
    return (out).diff().diff()


def f02_pblo_200_volume_curvature_lag_corr_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Lag-5 cross-correlation of (volume change) with (log-close curvature).
    Positive => volume leads curvature (effort precedes parabolic move)."""
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    dv = volume.pct_change()
    return (dv.shift(5).rolling(63, min_periods=24).corr(c)).diff().diff()


def f02_pblo_201_volume_curvature_divergence_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Divergence indicator: 1 when curvature rising (21d) but volume falling (21d),
    else 0; 63d sum. High count = unsustainable parabolic move on dry-up volume."""
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    dc = c - c.shift(21)
    dv = volume - volume.shift(21)
    flag = ((dc > 0) & (dv < 0)).astype(float).where(dc.notna() & dv.notna(), np.nan)
    return (flag.rolling(63, min_periods=21).sum()).diff().diff()


def f02_pblo_201_volume_curvature_divergence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Divergence indicator: 1 when curvature rising (21d) but volume falling (21d),
    else 0; 63d sum. High count = unsustainable parabolic move on dry-up volume."""
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    dc = c - c.shift(21)
    dv = volume - volume.shift(21)
    flag = ((dc > 0) & (dv < 0)).astype(float).where(dc.notna() & dv.notna(), np.nan)
    return flag.rolling(63, min_periods=21).sum()


def f02_pblo_202_volume_cluster_around_inflection_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume z-score sum on bars within ±2d of an inflection-point event in 63d.
    Inflection = sign-flip of 5d 2nd-diff of log-close."""
    lc = _safe_log(close)
    d2 = lc - 2 * lc.shift(5) + lc.shift(10)
    sgn = np.sign(d2)
    infl = (sgn != sgn.shift(1)).astype(float).where(sgn.notna() & sgn.shift(1).notna(), 0.0)
    # mark ±2d window
    near = infl
    for k in [1, 2]:
        near = near + infl.shift(k).fillna(0)
    near = (near > 0).astype(float)
    vz = _rolling_zscore(volume.astype(float), 252)
    weighted = (vz * near).where(vz.notna(), np.nan)
    return (weighted.rolling(63, min_periods=21).sum()).diff().diff()


def f02_pblo_203_effort_vs_result_parabolic_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Effort-vs-result: cumulative |log-return| (effort proxy when high volume)
    minus net log-return over 63d, weighted by relative volume. Large positive =
    high effort small result (terminal blow-off churn)."""
    lc = _safe_log(close)
    lr = lc.diff()
    rv = volume / volume.rolling(252, min_periods=84).mean()
    effort = (lr.abs() * rv).rolling(63, min_periods=21).sum()
    result = lr.rolling(63, min_periods=21).sum()
    return (effort - result.abs()).diff().diff()


def f02_pblo_204_acceleration_on_heavy_vol_days_only_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean 21d quad-c computed only on bars where volume z-score > 1 (heavy days)
    averaged over 252d trailing window."""
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    vz = _rolling_zscore(volume.astype(float), 252)
    heavy = (vz > 1).astype(float).where(vz.notna(), np.nan)
    c_heavy = c.where(heavy == 1, np.nan)
    cnt = heavy.rolling(252, min_periods=84).sum()
    s = c_heavy.rolling(252, min_periods=84).sum()
    return (_safe_div(s, cnt)).diff().diff()


def f02_pblo_205_curvature_anova_f_252d_d2(close: pd.Series) -> pd.Series:
    """One-way ANOVA F-statistic across 4 sub-windows of length 63 in 252d:
    between-group variance / within-group variance of log-close levels.
    High F => structural change in mean across sub-windows (consistent with
    accelerating parabolic phase)."""
    lc = _safe_log(close)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 240:
            return np.nan
        x = w[valid].astype(float)
        if len(x) < 240:
            return np.nan
        seg_len = len(x) // 4
        groups = [x[i * seg_len:(i + 1) * seg_len] for i in range(4)]
        gmeans = np.array([g.mean() for g in groups])
        gmean = np.concatenate(groups).mean()
        sizes = np.array([len(g) for g in groups])
        ss_b = (sizes * (gmeans - gmean) ** 2).sum()
        ss_w = sum(((g - g.mean()) ** 2).sum() for g in groups)
        k = 4; n = sum(sizes)
        if ss_w <= 0 or n <= k:
            return np.nan
        return float((ss_b / (k - 1)) / (ss_w / (n - k)))
    return (lc.rolling(252, min_periods=240).apply(_f, raw=True)).diff().diff()


def f02_pblo_205_curvature_anova_f_252d(close: pd.Series) -> pd.Series:
    """One-way ANOVA F-statistic across 4 sub-windows of length 63 in 252d:
    between-group variance / within-group variance of log-close levels.
    High F => structural change in mean across sub-windows (consistent with
    accelerating parabolic phase)."""
    lc = _safe_log(close)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 240:
            return np.nan
        x = w[valid].astype(float)
        if len(x) < 240:
            return np.nan
        seg_len = len(x) // 4
        groups = [x[i * seg_len:(i + 1) * seg_len] for i in range(4)]
        gmeans = np.array([g.mean() for g in groups])
        gmean = np.concatenate(groups).mean()
        sizes = np.array([len(g) for g in groups])
        ss_b = (sizes * (gmeans - gmean) ** 2).sum()
        ss_w = sum(((g - g.mean()) ** 2).sum() for g in groups)
        k = 4; n = sum(sizes)
        if ss_w <= 0 or n <= k:
            return np.nan
        return float((ss_b / (k - 1)) / (ss_w / (n - k)))
    return lc.rolling(252, min_periods=240).apply(_f, raw=True)


def f02_pblo_206_subwindow_curvature_variance_252d_d2(close: pd.Series) -> pd.Series:
    """Variance of 21d-quad-c across 12 non-overlapping sub-windows in 252d."""
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    def _v(w):
        valid = ~np.isnan(w)
        if valid.sum() < 200:
            return np.nan
        x = w[valid].astype(float)
        seg = len(x) // 12
        vals = [x[i * seg:(i + 1) * seg].mean() for i in range(12)]
        return float(np.var(vals))
    return (c.rolling(252, min_periods=200).apply(_v, raw=True)).diff().diff()


def f02_pblo_207_subwindow_curvature_skew_252d_d2(close: pd.Series) -> pd.Series:
    """Skewness of 21d-quad-c across 12 sub-windows in 252d."""
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    def _sk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 200:
            return np.nan
        x = w[valid].astype(float)
        seg = len(x) // 12
        vals = np.array([x[i * seg:(i + 1) * seg].mean() for i in range(12)])
        m = vals.mean(); s = vals.std()
        if s <= 0:
            return np.nan
        return float(((vals - m) ** 3).mean() / s ** 3)
    return (c.rolling(252, min_periods=200).apply(_sk, raw=True)).diff().diff()


def f02_pblo_208_subwindow_curvature_kurt_252d_d2(close: pd.Series) -> pd.Series:
    """Excess kurtosis of 21d-quad-c across 12 sub-windows in 252d."""
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    def _kt(w):
        valid = ~np.isnan(w)
        if valid.sum() < 200:
            return np.nan
        x = w[valid].astype(float)
        seg = len(x) // 12
        vals = np.array([x[i * seg:(i + 1) * seg].mean() for i in range(12)])
        m = vals.mean(); s = vals.std()
        if s <= 0:
            return np.nan
        return float(((vals - m) ** 4).mean() / s ** 4 - 3.0)
    return (c.rolling(252, min_periods=200).apply(_kt, raw=True)).diff().diff()


def f02_pblo_209_curvature_dispersion_zscore_504d_d2(close: pd.Series) -> pd.Series:
    """Z-score of 252d curvature-std vs its 504d trailing distribution."""
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    disp = c.rolling(252, min_periods=84).std()
    return (_rolling_zscore(disp, 504)).diff().diff()


def f02_pblo_210_curvature_consensus_index_252d_d2(close: pd.Series) -> pd.Series:
    """Curvature consensus: fraction of 12 sub-windows (each 21d) whose mean
    quad-c is positive, in trailing 252d. 1.0 = unanimous accel; 0 = unanimous
    decel."""
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    def _ci(w):
        valid = ~np.isnan(w)
        if valid.sum() < 200:
            return np.nan
        x = w[valid].astype(float)
        seg = len(x) // 12
        vals = [x[i * seg:(i + 1) * seg].mean() for i in range(12)]
        return float(np.mean(np.array(vals) > 0))
    return (c.rolling(252, min_periods=200).apply(_ci, raw=True)).diff().diff()


def f02_pblo_210_curvature_consensus_index_252d(close: pd.Series) -> pd.Series:
    """Curvature consensus: fraction of 12 sub-windows (each 21d) whose mean
    quad-c is positive, in trailing 252d. 1.0 = unanimous accel; 0 = unanimous
    decel."""
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    def _ci(w):
        valid = ~np.isnan(w)
        if valid.sum() < 200:
            return np.nan
        x = w[valid].astype(float)
        seg = len(x) // 12
        vals = [x[i * seg:(i + 1) * seg].mean() for i in range(12)]
        return float(np.mean(np.array(vals) > 0))
    return c.rolling(252, min_periods=200).apply(_ci, raw=True)


def f02_pblo_211_pre_onset_compression_score_63d_d2(close: pd.Series) -> pd.Series:
    """Pre-onset compression: 21d realized vol just BEFORE the most recent
    curvature-acceleration onset, divided by 63d trailing mean realized vol.
    Low values = quiet calm before parabolic burst."""
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    rv = lc.diff().rolling(21, min_periods=7).std()
    onset = ((c > 0) & (c.shift(1) <= 0)).astype(float)
    # if no onset in trailing window, NaN
    onset_idx = onset.where(onset == 1)
    # value at most recent onset day's prior 21d rv (look-back BEFORE event)
    pre_rv = rv.shift(21)
    val = pre_rv.where(onset == 1)
    val = val.ffill(limit=62)
    base = rv.rolling(63, min_periods=21).mean()
    return (_safe_div(val, base)).diff().diff()


def f02_pblo_212_post_peak_curvature_halflife_63d_d2(close: pd.Series) -> pd.Series:
    """Half-life of curvature decay from peak: bars taken for c to fall below
    50% of its 63d trailing max. NaN if not yet halved."""
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    def _hl(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        x = w[valid].astype(float)
        mx = x.max()
        if mx <= 0:
            return np.nan
        imax = np.argmax(x)
        half = 0.5 * mx
        # bars after imax until x <= half
        for k, v in enumerate(x[imax + 1:]):
            if v <= half:
                return float(k + 1)
        return np.nan
    return (c.rolling(63, min_periods=24).apply(_hl, raw=True)).diff().diff()


def f02_pblo_213_acceleration_buildup_gradient_63d_d2(close: pd.Series) -> pd.Series:
    """Gradient (linear slope) of 21d-quad-c over 63d trailing window. Positive
    & rising = monotone build-up of curvature toward parabolic phase."""
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    return (_rolling_slope(c, 63)).diff().diff()


def f02_pblo_214_curvature_volatility_ratio_recent_vs_prior_252d_d2(close: pd.Series) -> pd.Series:
    """Ratio: std of quad-c in trailing 63d / std of quad-c in prior 63d (lagged
    63d). Rising = curvature variability expanding (regime shift)."""
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    recent = c.rolling(63, min_periods=24).std()
    prior = recent.shift(63)
    return (_safe_div(recent, prior)).diff().diff()


def f02_pblo_215_time_from_c_trough_to_c_peak_252d_d2(close: pd.Series) -> pd.Series:
    """Bars between the trailing 252d trough of quad-c and the trailing 252d peak.
    Positive = peak came after trough (build phase); negative = peak came first
    (already declining)."""
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    def _gap(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        x = w[valid].astype(float)
        return float(np.argmax(x) - np.argmin(x))
    return (c.rolling(252, min_periods=84).apply(_gap, raw=True)).diff().diff()


def f02_pblo_216_comp_multi_method_c_consensus_252d_d2(close: pd.Series) -> pd.Series:
    """Multi-method consensus: count of methods (polyfit, Theil-Sen, Kalman-CA,
    Bayesian-mixture posterior > 0.5) agreeing that curvature regime is positive."""
    lc = _safe_log(close)
    c_poly = lc.rolling(63, min_periods=24).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    # robust Theil-Sen proxy: median of pairwise (y_b-y_a)/(t_b^2-t_a^2)
    def _ts(w):
        valid = ~np.isnan(w)
        if valid.sum() < 21:
            return np.nan
        y = w[valid].astype(float)
        t = np.arange(len(y), dtype=float)
        idx = np.arange(0, len(y), 3)
        sl = []
        for a in idx:
            for b in idx:
                if b > a and t[b] ** 2 - t[a] ** 2 > 0:
                    sl.append((y[b] - y[a]) / (t[b] ** 2 - t[a] ** 2))
        if len(sl) < 5:
            return np.nan
        return float(np.median(sl))
    c_ts = lc.rolling(63, min_periods=24).apply(_ts, raw=True)
    c_kal = lc.rolling(252, min_periods=84).apply(_kalman_ca_accel, raw=True)
    c_bay = c_poly.rolling(252, min_periods=84).apply(_posterior_accel_regime, raw=True)
    parts = pd.concat([
        (c_poly > 0).astype(float).rename(0),
        (c_ts > 0).astype(float).rename(1),
        (c_kal > 0).astype(float).rename(2),
        (c_bay > 0.5).astype(float).rename(3),
    ], axis=1)
    return (parts.sum(axis=1).where(c_poly.notna() & c_ts.notna() & c_kal.notna() & c_bay.notna(), np.nan)).diff().diff()


def f02_pblo_217_comp_fractal_spectral_joint_anomaly_252d_d2(close: pd.Series) -> pd.Series:
    """Joint anomaly: |z(box-count fd)| + |z(spectral entropy)| in 504d history."""
    fd = f02_pblo_152_box_count_fd_log_close_252d(close)
    se = f02_pblo_168_spectral_entropy_residuals_252d(close)
    return (_rolling_zscore(fd, 504).abs() + _rolling_zscore(se, 504).abs()).diff().diff()


def f02_pblo_218_comp_catastrophe_lppl_joint_bubble_252d_d2(close: pd.Series) -> pd.Series:
    """Joint catastrophe-LPPL bubble score: positive cusp beta AND high quad-c
    (top quartile in 252d). 1 if both, 0.5 if one, 0 if none, NaN if missing."""
    lc = _safe_log(close)
    beta = lc.rolling(252, min_periods=64).apply(_cusp_beta, raw=True)
    c = lc.rolling(63, min_periods=24).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    cq = c.rolling(252, min_periods=84).quantile(0.75)
    a = (beta > 0).astype(float)
    b = (c > cq).astype(float)
    score = 0.5 * a + 0.5 * b
    return (score.where(beta.notna() & c.notna() & cq.notna(), np.nan)).diff().diff()


def f02_pblo_219_comp_statespace_changepoint_joint_252d_d2(close: pd.Series) -> pd.Series:
    """State-space + change-point joint: Kalman terminal accel * BOCPD intensity
    (both standardized over 504d)."""
    ka = f02_pblo_176_kalman_ca_terminal_acceleration_252d(close)
    cp = f02_pblo_179_bocpd_changepoint_intensity_252d(close)
    return (_rolling_zscore(ka, 504) * _rolling_zscore(cp, 504)).diff().diff()


def f02_pblo_220_comp_spline_polynomial_agreement_252d_d2(close: pd.Series) -> pd.Series:
    """Agreement between B-spline curvature and polynomial quad-c: 1 if signs match,
    -1 if they differ, NaN if either missing. Magnitude weighted by min(|bsp|, |c|)."""
    bsp = f02_pblo_183_b_spline_knot_curvature_252d(close)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=24).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    sgn = np.sign(bsp) * np.sign(c)
    mag = pd.concat([bsp.abs().rename(0), c.abs().rename(1)], axis=1).min(axis=1)
    return ((sgn * mag).where(bsp.notna() & c.notna(), np.nan)).diff().diff()


def f02_pblo_221_comp_vw_multihorizon_curvature_consensus_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted multi-horizon curvature consensus: sign agreement across
    63d / 126d / 252d weighted quad-c. Returns net signed agreement in [-3, 3]."""
    c63 = f02_pblo_197_volume_weighted_quad_c_63d(close, volume)
    # construct 126d and 252d versions inline (use shift+rolling of 63d not appropriate)
    lc = _safe_log(close)
    def _vwc(n):
        out = pd.Series(np.nan, index=lc.index)
        for i in range(n - 1, len(lc)):
            y = lc.iloc[i - n + 1:i + 1].values
            v = volume.iloc[i - n + 1:i + 1].values.astype(float)
            mask = ~np.isnan(y) & ~np.isnan(v) & (v > 0)
            if mask.sum() < n // 3:
                continue
            yv = y[mask]; vv = v[mask]
            vv = vv / vv.mean()
            out.iloc[i] = _weighted_quad_c(yv, vv)
        return out
    c126 = _vwc(126)
    c252 = _vwc(252)
    s = np.sign(c63) + np.sign(c126) + np.sign(c252)
    return (s.where(c63.notna() & c126.notna() & c252.notna(), np.nan)).diff().diff()


def f02_pblo_222_comp_onset_detector_consensus_252d_d2(close: pd.Series) -> pd.Series:
    """Onset-detector consensus: count (0..3) of methods firing onset in trailing
    21d: (1) c crosses above 0, (2) Kalman terminal accel crosses above 0,
    (3) BOCPD intensity > rolling 75th percentile."""
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=24).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    e1 = ((c > 0) & (c.shift(1) <= 0)).astype(float)
    fire1 = e1.rolling(21, min_periods=7).sum().clip(upper=1)
    ka = f02_pblo_176_kalman_ca_terminal_acceleration_252d(close)
    e2 = ((ka > 0) & (ka.shift(1) <= 0)).astype(float)
    fire2 = e2.rolling(21, min_periods=7).sum().clip(upper=1)
    cp = f02_pblo_179_bocpd_changepoint_intensity_252d(close)
    q = cp.rolling(252, min_periods=84).quantile(0.75)
    fire3 = (cp > q).astype(float).rolling(21, min_periods=7).max()
    parts = pd.concat([fire1.rename(0), fire2.rename(1), fire3.rename(2)], axis=1)
    return (parts.sum(axis=1).where(c.notna() & ka.notna() & cp.notna(), np.nan)).diff().diff()


def f02_pblo_223_comp_post_onset_extension_velocity_252d_d2(close: pd.Series) -> pd.Series:
    """Post-onset extension velocity: 21d log-return magnitude conditioned on
    most-recent onset event firing within trailing 63d. NaN if no onset."""
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=24).apply(lambda w: _poly_coef(w, 2, 0), raw=True)
    onset = ((c > 0) & (c.shift(1) <= 0)).astype(float)
    fired = onset.rolling(63, min_periods=21).sum()
    vel = lc.diff(21)
    return (vel.where(fired > 0, np.nan)).diff().diff()


def f02_pblo_224_comp_bubble_probability_ensemble_252d_d2(close: pd.Series) -> pd.Series:
    """Ensemble bubble probability score: average of three standardized indicators
    (DFA-alpha > 0.5 boost, posterior accel regime, |cusp distance to bifurcation|
    sign). Output in approximately [0, 1]."""
    da = f02_pblo_155_dfa_alpha_log_returns_252d(close)
    pa = f02_pblo_180_posterior_accel_regime_prob_252d(close)
    dd = f02_pblo_160_cusp_distance_to_bifurcation_252d(close)
    s1 = ((da - 0.5) * 2.0).clip(lower=0.0, upper=1.0)
    s2 = pa.clip(lower=0.0, upper=1.0)
    s3 = (dd < 0).astype(float).where(dd.notna(), np.nan)
    parts = pd.concat([s1.rename(0), s2.rename(1), s3.rename(2)], axis=1)
    return (parts.mean(axis=1)).diff().diff()


def f02_pblo_225_comp_terminal_parabolic_confidence_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Terminal parabolic-state confidence composite (narrow, parabolic-internal):
    mean of standardized values from (a) Kalman-CA terminal accel, (b) ANOVA F-stat
    across sub-windows, (c) curvature consensus index, (d) volume-curvature
    divergence. Higher = stronger conviction in terminal parabolic phase."""
    ka = f02_pblo_176_kalman_ca_terminal_acceleration_252d(close)
    fa = f02_pblo_205_curvature_anova_f_252d(close)
    ci = f02_pblo_210_curvature_consensus_index_252d(close)
    vd = f02_pblo_201_volume_curvature_divergence_63d(close, volume)
    parts = pd.concat([
        _rolling_zscore(ka, 504).rename(0),
        _rolling_zscore(fa, 504).rename(1),
        _rolling_zscore(ci, 504).rename(2),
        _rolling_zscore(vd, 504).rename(3),
    ], axis=1)
    return (parts.mean(axis=1)).diff().diff()


PARABOLIC_BLOWOFF_SIGNATURE_D2_REGISTRY_151_225 = {
    "f02_pblo_151_box_count_fd_log_close_63d_d2": {"inputs": ["close"], "func": f02_pblo_151_box_count_fd_log_close_63d_d2},
    "f02_pblo_152_box_count_fd_log_close_252d_d2": {"inputs": ["close"], "func": f02_pblo_152_box_count_fd_log_close_252d_d2},
    "f02_pblo_153_box_count_fd_log_close_504d_d2": {"inputs": ["close"], "func": f02_pblo_153_box_count_fd_log_close_504d_d2},
    "f02_pblo_154_higuchi_fd_log_returns_252d_d2": {"inputs": ["close"], "func": f02_pblo_154_higuchi_fd_log_returns_252d_d2},
    "f02_pblo_155_dfa_alpha_log_returns_252d_d2": {"inputs": ["close"], "func": f02_pblo_155_dfa_alpha_log_returns_252d_d2},
    "f02_pblo_156_multi_scale_fd_consensus_252d_d2": {"inputs": ["close"], "func": f02_pblo_156_multi_scale_fd_consensus_252d_d2},
    "f02_pblo_157_self_similar_rs_exponent_252d_d2": {"inputs": ["close"], "func": f02_pblo_157_self_similar_rs_exponent_252d_d2},
    "f02_pblo_158_fractal_dim_acceleration_252d_d2": {"inputs": ["close"], "func": f02_pblo_158_fractal_dim_acceleration_252d_d2},
    "f02_pblo_159_cusp_fit_residual_252d_d2": {"inputs": ["close"], "func": f02_pblo_159_cusp_fit_residual_252d_d2},
    "f02_pblo_160_cusp_distance_to_bifurcation_252d_d2": {"inputs": ["close"], "func": f02_pblo_160_cusp_distance_to_bifurcation_252d_d2},
    "f02_pblo_161_cusp_control_beta_252d_d2": {"inputs": ["close"], "func": f02_pblo_161_cusp_control_beta_252d_d2},
    "f02_pblo_162_cusp_control_alpha_252d_d2": {"inputs": ["close"], "func": f02_pblo_162_cusp_control_alpha_252d_d2},
    "f02_pblo_163_hopf_floquet_proxy_63d_d2": {"inputs": ["close"], "func": f02_pblo_163_hopf_floquet_proxy_63d_d2},
    "f02_pblo_164_adf_proxy_first_diff_log_close_252d_d2": {"inputs": ["close"], "func": f02_pblo_164_adf_proxy_first_diff_log_close_252d_d2},
    "f02_pblo_165_kpss_proxy_log_curvature_252d_d2": {"inputs": ["close"], "func": f02_pblo_165_kpss_proxy_log_curvature_252d_d2},
    "f02_pblo_166_variance_ratio_test_deviation_252d_d2": {"inputs": ["close"], "func": f02_pblo_166_variance_ratio_test_deviation_252d_d2},
    "f02_pblo_167_lomb_scargle_residual_peak_252d_d2": {"inputs": ["close"], "func": f02_pblo_167_lomb_scargle_residual_peak_252d_d2},
    "f02_pblo_168_spectral_entropy_residuals_252d_d2": {"inputs": ["close"], "func": f02_pblo_168_spectral_entropy_residuals_252d_d2},
    "f02_pblo_169_dominant_fft_freq_shift_252d_d2": {"inputs": ["close"], "func": f02_pblo_169_dominant_fft_freq_shift_252d_d2},
    "f02_pblo_170_high_to_low_freq_power_ratio_252d_d2": {"inputs": ["close"], "func": f02_pblo_170_high_to_low_freq_power_ratio_252d_d2},
    "f02_pblo_171_spectral_flatness_252d_d2": {"inputs": ["close"], "func": f02_pblo_171_spectral_flatness_252d_d2},
    "f02_pblo_172_periodogram_tail_weight_252d_d2": {"inputs": ["close"], "func": f02_pblo_172_periodogram_tail_weight_252d_d2},
    "f02_pblo_173_multi_resolution_spectral_consensus_252d_d2": {"inputs": ["close"], "func": f02_pblo_173_multi_resolution_spectral_consensus_252d_d2},
    "f02_pblo_174_low_freq_dominance_streak_252d_d2": {"inputs": ["close"], "func": f02_pblo_174_low_freq_dominance_streak_252d_d2},
    "f02_pblo_175_kalman_cv_terminal_velocity_252d_d2": {"inputs": ["close"], "func": f02_pblo_175_kalman_cv_terminal_velocity_252d_d2},
    "f02_pblo_176_kalman_ca_terminal_acceleration_252d_d2": {"inputs": ["close"], "func": f02_pblo_176_kalman_ca_terminal_acceleration_252d_d2},
    "f02_pblo_177_kalman_innovation_variance_252d_d2": {"inputs": ["close"], "func": f02_pblo_177_kalman_innovation_variance_252d_d2},
    "f02_pblo_178_bocpd_posterior_changepoint_252d_d2": {"inputs": ["close"], "func": f02_pblo_178_bocpd_posterior_changepoint_252d_d2},
    "f02_pblo_179_bocpd_changepoint_intensity_252d_d2": {"inputs": ["close"], "func": f02_pblo_179_bocpd_changepoint_intensity_252d_d2},
    "f02_pblo_180_posterior_accel_regime_prob_252d_d2": {"inputs": ["close"], "func": f02_pblo_180_posterior_accel_regime_prob_252d_d2},
    "f02_pblo_181_hmm_accel_state_posterior_252d_d2": {"inputs": ["close"], "func": f02_pblo_181_hmm_accel_state_posterior_252d_d2},
    "f02_pblo_182_hmm_expected_duration_accel_252d_d2": {"inputs": ["close"], "func": f02_pblo_182_hmm_expected_duration_accel_252d_d2},
    "f02_pblo_183_b_spline_knot_curvature_252d_d2": {"inputs": ["close"], "func": f02_pblo_183_b_spline_knot_curvature_252d_d2},
    "f02_pblo_184_smoothing_spline_d2_terminal_63d_d2": {"inputs": ["close"], "func": f02_pblo_184_smoothing_spline_d2_terminal_63d_d2},
    "f02_pblo_185_lowess_residual_std_63d_d2": {"inputs": ["close"], "func": f02_pblo_185_lowess_residual_std_63d_d2},
    "f02_pblo_186_chebyshev_t2_coef_252d_d2": {"inputs": ["close"], "func": f02_pblo_186_chebyshev_t2_coef_252d_d2},
    "f02_pblo_187_bernstein_polynomial_resid_252d_d2": {"inputs": ["close"], "func": f02_pblo_187_bernstein_polynomial_resid_252d_d2},
    "f02_pblo_188_p_spline_penalized_curvature_252d_d2": {"inputs": ["close"], "func": f02_pblo_188_p_spline_penalized_curvature_252d_d2},
    "f02_pblo_189_spline_knot_density_adaptation_252d_d2": {"inputs": ["close"], "func": f02_pblo_189_spline_knot_density_adaptation_252d_d2},
    "f02_pblo_190_local_quad_slope_of_d2_63d_d2": {"inputs": ["close"], "func": f02_pblo_190_local_quad_slope_of_d2_63d_d2},
    "f02_pblo_191_ssa_trend_residual_at_top_252d_d2": {"inputs": ["close"], "func": f02_pblo_191_ssa_trend_residual_at_top_252d_d2},
    "f02_pblo_192_ssa_dominant_component_amplitude_252d_d2": {"inputs": ["close"], "func": f02_pblo_192_ssa_dominant_component_amplitude_252d_d2},
    "f02_pblo_193_ssa_reconstruction_error_variance_252d_d2": {"inputs": ["close"], "func": f02_pblo_193_ssa_reconstruction_error_variance_252d_d2},
    "f02_pblo_194_emd_imf3_to_imf5_amplitude_ratio_252d_d2": {"inputs": ["close"], "func": f02_pblo_194_emd_imf3_to_imf5_amplitude_ratio_252d_d2},
    "f02_pblo_195_emd_instantaneous_freq_variance_252d_d2": {"inputs": ["close"], "func": f02_pblo_195_emd_instantaneous_freq_variance_252d_d2},
    "f02_pblo_196_emd_trend_acceleration_252d_d2": {"inputs": ["close"], "func": f02_pblo_196_emd_trend_acceleration_252d_d2},
    "f02_pblo_197_volume_weighted_quad_c_63d_d2": {"inputs": ["close", "volume"], "func": f02_pblo_197_volume_weighted_quad_c_63d_d2},
    "f02_pblo_198_volume_weighted_quad_r2_63d_d2": {"inputs": ["close", "volume"], "func": f02_pblo_198_volume_weighted_quad_r2_63d_d2},
    "f02_pblo_199_volume_weighted_theil_sen_quad_63d_d2": {"inputs": ["close", "volume"], "func": f02_pblo_199_volume_weighted_theil_sen_quad_63d_d2},
    "f02_pblo_200_volume_curvature_lag_corr_63d_d2": {"inputs": ["close", "volume"], "func": f02_pblo_200_volume_curvature_lag_corr_63d_d2},
    "f02_pblo_201_volume_curvature_divergence_63d_d2": {"inputs": ["close", "volume"], "func": f02_pblo_201_volume_curvature_divergence_63d_d2},
    "f02_pblo_202_volume_cluster_around_inflection_63d_d2": {"inputs": ["close", "volume"], "func": f02_pblo_202_volume_cluster_around_inflection_63d_d2},
    "f02_pblo_203_effort_vs_result_parabolic_63d_d2": {"inputs": ["close", "volume"], "func": f02_pblo_203_effort_vs_result_parabolic_63d_d2},
    "f02_pblo_204_acceleration_on_heavy_vol_days_only_252d_d2": {"inputs": ["close", "volume"], "func": f02_pblo_204_acceleration_on_heavy_vol_days_only_252d_d2},
    "f02_pblo_205_curvature_anova_f_252d_d2": {"inputs": ["close"], "func": f02_pblo_205_curvature_anova_f_252d_d2},
    "f02_pblo_206_subwindow_curvature_variance_252d_d2": {"inputs": ["close"], "func": f02_pblo_206_subwindow_curvature_variance_252d_d2},
    "f02_pblo_207_subwindow_curvature_skew_252d_d2": {"inputs": ["close"], "func": f02_pblo_207_subwindow_curvature_skew_252d_d2},
    "f02_pblo_208_subwindow_curvature_kurt_252d_d2": {"inputs": ["close"], "func": f02_pblo_208_subwindow_curvature_kurt_252d_d2},
    "f02_pblo_209_curvature_dispersion_zscore_504d_d2": {"inputs": ["close"], "func": f02_pblo_209_curvature_dispersion_zscore_504d_d2},
    "f02_pblo_210_curvature_consensus_index_252d_d2": {"inputs": ["close"], "func": f02_pblo_210_curvature_consensus_index_252d_d2},
    "f02_pblo_211_pre_onset_compression_score_63d_d2": {"inputs": ["close"], "func": f02_pblo_211_pre_onset_compression_score_63d_d2},
    "f02_pblo_212_post_peak_curvature_halflife_63d_d2": {"inputs": ["close"], "func": f02_pblo_212_post_peak_curvature_halflife_63d_d2},
    "f02_pblo_213_acceleration_buildup_gradient_63d_d2": {"inputs": ["close"], "func": f02_pblo_213_acceleration_buildup_gradient_63d_d2},
    "f02_pblo_214_curvature_volatility_ratio_recent_vs_prior_252d_d2": {"inputs": ["close"], "func": f02_pblo_214_curvature_volatility_ratio_recent_vs_prior_252d_d2},
    "f02_pblo_215_time_from_c_trough_to_c_peak_252d_d2": {"inputs": ["close"], "func": f02_pblo_215_time_from_c_trough_to_c_peak_252d_d2},
    "f02_pblo_216_comp_multi_method_c_consensus_252d_d2": {"inputs": ["close"], "func": f02_pblo_216_comp_multi_method_c_consensus_252d_d2},
    "f02_pblo_217_comp_fractal_spectral_joint_anomaly_252d_d2": {"inputs": ["close"], "func": f02_pblo_217_comp_fractal_spectral_joint_anomaly_252d_d2},
    "f02_pblo_218_comp_catastrophe_lppl_joint_bubble_252d_d2": {"inputs": ["close"], "func": f02_pblo_218_comp_catastrophe_lppl_joint_bubble_252d_d2},
    "f02_pblo_219_comp_statespace_changepoint_joint_252d_d2": {"inputs": ["close"], "func": f02_pblo_219_comp_statespace_changepoint_joint_252d_d2},
    "f02_pblo_220_comp_spline_polynomial_agreement_252d_d2": {"inputs": ["close"], "func": f02_pblo_220_comp_spline_polynomial_agreement_252d_d2},
    "f02_pblo_221_comp_vw_multihorizon_curvature_consensus_252d_d2": {"inputs": ["close", "volume"], "func": f02_pblo_221_comp_vw_multihorizon_curvature_consensus_252d_d2},
    "f02_pblo_222_comp_onset_detector_consensus_252d_d2": {"inputs": ["close"], "func": f02_pblo_222_comp_onset_detector_consensus_252d_d2},
    "f02_pblo_223_comp_post_onset_extension_velocity_252d_d2": {"inputs": ["close"], "func": f02_pblo_223_comp_post_onset_extension_velocity_252d_d2},
    "f02_pblo_224_comp_bubble_probability_ensemble_252d_d2": {"inputs": ["close"], "func": f02_pblo_224_comp_bubble_probability_ensemble_252d_d2},
    "f02_pblo_225_comp_terminal_parabolic_confidence_252d_d2": {"inputs": ["close", "volume"], "func": f02_pblo_225_comp_terminal_parabolic_confidence_252d_d2},
}
