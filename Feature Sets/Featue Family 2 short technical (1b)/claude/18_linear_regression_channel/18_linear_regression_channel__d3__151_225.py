"""lrch base 151-225 — robust/quantile/Kalman/LOWESS/HP/stability tests."""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

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
            x = x[valid]; wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _ols_pack(w):
    """OLS on window. Returns (slope, intercept, sigma_resid, r2, n_used) or NaNs."""
    valid = ~np.isnan(w)
    nv = int(valid.sum())
    if nv < 3:
        return (np.nan, np.nan, np.nan, np.nan, 0)
    x = np.arange(len(w), dtype=float)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    xm = x.mean(); ym = yv.mean()
    den = float(((x - xm) ** 2).sum())
    if den <= 0:
        return (np.nan, np.nan, np.nan, np.nan, nv)
    b = float(((x - xm) * (yv - ym)).sum() / den)
    a = ym - b * xm
    r = yv - (a + b * x)
    if r.size < 2:
        return (np.nan, np.nan, np.nan, np.nan, nv)
    sd = float(np.std(r, ddof=1))
    tss = float(((yv - ym) ** 2).sum())
    r2 = 1.0 - float((r * r).sum()) / tss if tss > 0 else np.nan
    return (b, a, sd, r2, nv)


def _rolling_resid_std(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _f(w):
        b, a, sd, r2, nv = _ols_pack(w)
        if nv < min_periods:
            return np.nan
        return sd
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def _rolling_r2(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _f(w):
        b, a, sd, r2, nv = _ols_pack(w)
        if nv < min_periods:
            return np.nan
        return r2
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def _theil_sen_slope(w):
    """Median of pairwise slopes. Subsamples for windows >100 to bound cost."""
    valid = ~np.isnan(w)
    nv = int(valid.sum())
    if nv < 3:
        return np.nan
    x = np.arange(len(w), dtype=float)
    if not valid.all():
        x = x[valid]; yv = w[valid]
    else:
        yv = w
    m = yv.size
    if m > 100:
        idx = np.linspace(0, m - 1, 100).astype(int)
        x = x[idx]; yv = yv[idx]; m = 100
    xi, xj = np.triu_indices(m, k=1)
    dx = x[xj] - x[xi]
    dy = yv[xj] - yv[xi]
    ok = dx != 0
    if not ok.any():
        return np.nan
    return float(np.median(dy[ok] / dx[ok]))


def _huber_slope(w, c=1.345, max_iter=10):
    """IRLS Huber slope. Returns (slope, resid_sigma)."""
    valid = ~np.isnan(w)
    nv = int(valid.sum())
    if nv < 5:
        return (np.nan, np.nan)
    x = np.arange(len(w), dtype=float)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    # init OLS
    xm = x.mean(); ym = yv.mean()
    den = float(((x - xm) ** 2).sum())
    if den <= 0:
        return (np.nan, np.nan)
    b = float(((x - xm) * (yv - ym)).sum() / den)
    a = ym - b * xm
    for _ in range(max_iter):
        r = yv - (a + b * x)
        s_mad = 1.4826 * float(np.median(np.abs(r - np.median(r))))
        if s_mad <= 0:
            break
        u = r / s_mad
        wts = np.where(np.abs(u) <= c, 1.0, c / np.maximum(np.abs(u), 1e-12))
        sw = wts.sum()
        if sw <= 0:
            break
        xw = (wts * x).sum() / sw
        yw = (wts * yv).sum() / sw
        num = (wts * (x - xw) * (yv - yw)).sum()
        deno = (wts * (x - xw) ** 2).sum()
        if deno <= 0:
            break
        b_new = num / deno
        a_new = yw - b_new * xw
        if abs(b_new - b) < 1e-9 and abs(a_new - a) < 1e-9:
            b, a = b_new, a_new
            break
        b, a = b_new, a_new
    r_final = yv - (a + b * x)
    sd = float(np.std(r_final, ddof=1)) if r_final.size > 1 else np.nan
    return (float(b), sd)


def _quantile_slope(w, q=0.5):
    """Quantile regression slope via iterative weighted least squares (simplified)."""
    valid = ~np.isnan(w)
    nv = int(valid.sum())
    if nv < 5:
        return np.nan
    x = np.arange(len(w), dtype=float)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    # init OLS
    xm = x.mean(); ym = yv.mean()
    den = float(((x - xm) ** 2).sum())
    if den <= 0:
        return np.nan
    b = float(((x - xm) * (yv - ym)).sum() / den)
    a = ym - b * xm
    eps = 1e-6
    for _ in range(15):
        r = yv - (a + b * x)
        wts = np.where(r > 0, q, 1.0 - q) / np.maximum(np.abs(r), eps)
        sw = wts.sum()
        if sw <= 0:
            break
        xw = (wts * x).sum() / sw
        yw = (wts * yv).sum() / sw
        num = (wts * (x - xw) * (yv - yw)).sum()
        deno = (wts * (x - xw) ** 2).sum()
        if deno <= 0:
            break
        b_new = num / deno
        a_new = yw - b_new * xw
        if abs(b_new - b) < 1e-9:
            b, a = b_new, a_new
            break
        b, a = b_new, a_new
    return float(b)


def _lts_slope(w, h_frac=0.75):
    """Least-trimmed-squares: fit OLS then refit on the h_frac smallest residuals."""
    valid = ~np.isnan(w)
    nv = int(valid.sum())
    if nv < 8:
        return np.nan
    x = np.arange(len(w), dtype=float)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    xm = x.mean(); ym = yv.mean()
    den = float(((x - xm) ** 2).sum())
    if den <= 0:
        return np.nan
    b = float(((x - xm) * (yv - ym)).sum() / den)
    a = ym - b * xm
    r = np.abs(yv - (a + b * x))
    h = max(int(h_frac * yv.size), 3)
    ord_idx = np.argsort(r)[:h]
    xs = x[ord_idx]; ys = yv[ord_idx]
    xsm = xs.mean(); ysm = ys.mean()
    den2 = float(((xs - xsm) ** 2).sum())
    if den2 <= 0:
        return np.nan
    return float(((xs - xsm) * (ys - ysm)).sum() / den2)


def _poly_curvature(w, deg=2):
    """Returns 2nd derivative coeff for deg=2 (curvature) at endpoint, scaled."""
    valid = ~np.isnan(w)
    nv = int(valid.sum())
    if nv < deg + 2:
        return np.nan
    x = np.arange(len(w), dtype=float)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    try:
        coef = np.polyfit(x, yv, deg)
    except (np.linalg.LinAlgError, ValueError):
        return np.nan
    # coef order: highest first. For deg=2, coef[0]=a; curvature = 2a
    return float(2.0 * coef[0])


def _poly3_inflection_dist(w):
    """Distance (bars from endpoint) of cubic-fit inflection point. f''=0 at x=-b/(3a)."""
    valid = ~np.isnan(w)
    nv = int(valid.sum())
    if nv < 5:
        return np.nan
    x = np.arange(len(w), dtype=float)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    try:
        coef = np.polyfit(x, yv, 3)
    except (np.linalg.LinAlgError, ValueError):
        return np.nan
    a3, b3 = coef[0], coef[1]
    if abs(a3) < 1e-12:
        return np.nan
    x_inf = -b3 / (3.0 * a3)
    return float((len(w) - 1) - x_inf)


def _kalman_local_lin(y_arr, q_lev=1e-5, q_sl=1e-7, r_obs=1e-3):
    """Local-linear-trend Kalman filter. Returns (level_end, slope_end, innov_z_end, slope_path)."""
    valid = ~np.isnan(y_arr)
    if valid.sum() < 5:
        return (np.nan, np.nan, np.nan, np.full(y_arr.size, np.nan))
    # Init
    y0 = y_arr[valid][0]
    lev = y0; sl = 0.0
    P = np.array([[1.0, 0.0], [0.0, 1.0]])
    Q = np.array([[q_lev, 0.0], [0.0, q_sl]])
    F = np.array([[1.0, 1.0], [0.0, 1.0]])
    H = np.array([[1.0, 0.0]])
    slope_path = np.full(y_arr.size, np.nan)
    innov_var_end = np.nan
    innov_end = np.nan
    for i in range(y_arr.size):
        # Predict
        state = F @ np.array([lev, sl])
        P = F @ P @ F.T + Q
        if not np.isnan(y_arr[i]):
            v = y_arr[i] - (H @ state)[0]
            S = (H @ P @ H.T)[0, 0] + r_obs
            K = (P @ H.T).ravel() / S
            state = state + K * v
            P = P - np.outer(K, H @ P)
            innov_var_end = S
            innov_end = v
        lev, sl = float(state[0]), float(state[1])
        slope_path[i] = sl
    if innov_var_end is None or np.isnan(innov_var_end) or innov_var_end <= 0:
        iz = np.nan
    else:
        iz = innov_end / np.sqrt(innov_var_end)
    return (lev, sl, float(iz) if iz is not None else np.nan, slope_path)


def _lowess_endpoint_slope(w, frac=0.3):
    """Local-linear regression at endpoint with tricube weights."""
    valid = ~np.isnan(w)
    nv = int(valid.sum())
    if nv < 5:
        return (np.nan, np.nan)
    x = np.arange(len(w), dtype=float)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    x0 = x[-1]
    bw = max(int(np.ceil(frac * len(w))), 5)
    d = np.abs(x - x0)
    if d.max() <= 0:
        return (np.nan, np.nan)
    h = np.partition(d, min(bw - 1, d.size - 1))[min(bw - 1, d.size - 1)]
    if h <= 0:
        h = d.max()
    u = np.clip(d / h, 0.0, 1.0)
    wts = (1.0 - u ** 3) ** 3
    sw = wts.sum()
    if sw <= 0:
        return (np.nan, np.nan)
    xw = (wts * x).sum() / sw
    yw_ = (wts * yv).sum() / sw
    num = (wts * (x - xw) * (yv - yw_)).sum()
    deno = (wts * (x - xw) ** 2).sum()
    if deno <= 0:
        return (np.nan, np.nan)
    b = num / deno
    a = yw_ - b * xw
    fit_end = a + b * x0
    return (float(b), float(yv[-1] - fit_end))


def _hp_filter_trend(y_arr, lam=1600.0):
    """Hodrick-Prescott trend (banded system solve). Returns trend array; NaNs if too short."""
    n = y_arr.size
    valid = ~np.isnan(y_arr)
    if valid.sum() < 10 or n < 10:
        return np.full(n, np.nan)
    yv = y_arr.copy()
    # forward-fill NaN inside (locally — only for HP solve)
    if not valid.all():
        s = pd.Series(yv).ffill().bfill().values
    else:
        s = yv
    # Build second-difference matrix K (n-2) x n
    e = np.ones(n)
    # Construct (I + lam*K'K) — pentadiagonal; solve via np.linalg.solve on small n_max
    if n > 800:
        return np.full(n, np.nan)
    K = np.zeros((n - 2, n))
    for i in range(n - 2):
        K[i, i] = 1.0; K[i, i + 1] = -2.0; K[i, i + 2] = 1.0
    A = np.eye(n) + lam * (K.T @ K)
    try:
        trend = np.linalg.solve(A, s)
    except np.linalg.LinAlgError:
        return np.full(n, np.nan)
    return trend


def _cusum_recursive_resid_end(w):
    """Brown-Durbin-Evans CUSUM of recursive residuals at endpoint (cumulative sum / sigma)."""
    valid = ~np.isnan(w)
    nv = int(valid.sum())
    if nv < 10:
        return np.nan
    x = np.arange(len(w), dtype=float)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    n = yv.size
    rr = np.full(n, np.nan)
    for k in range(3, n):
        xs = x[:k]; ys = yv[:k]
        xm = xs.mean(); ym = ys.mean()
        den = ((xs - xm) ** 2).sum()
        if den <= 0:
            continue
        b = ((xs - xm) * (ys - ym)).sum() / den
        a = ym - b * xm
        xt = x[k]; yt = yv[k]
        f = 1.0 + 1.0 / k + (xt - xm) ** 2 / den
        rr[k] = (yt - (a + b * xt)) / np.sqrt(max(f, 1e-12))
    ok = ~np.isnan(rr)
    if ok.sum() < 5:
        return np.nan
    sd = float(np.std(rr[ok], ddof=1))
    if sd <= 0:
        return np.nan
    return float(np.nansum(rr) / sd)


def f18_lrch_151_theilsen_slope_63d(close: pd.Series) -> pd.Series:
    """Theil-Sen slope."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_theil_sen_slope, raw=True)


def f18_lrch_152_huber_slope_63d(close: pd.Series) -> pd.Series:
    """Huber-M slope."""
    return _safe_log(close).rolling(63, min_periods=21).apply(lambda w: _huber_slope(w)[0], raw=True)


def f18_lrch_153_huber_residual_sigma_63d(close: pd.Series) -> pd.Series:
    """Huber-M residual sigma."""
    return _safe_log(close).rolling(63, min_periods=21).apply(lambda w: _huber_slope(w)[1], raw=True)


def f18_lrch_154_lts_slope_252d(close: pd.Series) -> pd.Series:
    """LTS slope."""
    return _safe_log(close).rolling(252, min_periods=84).apply(lambda w: _lts_slope(w, 0.75), raw=True)


def f18_lrch_155_quantile_reg_slope_q50_252d(close: pd.Series) -> pd.Series:
    """Q50 quantile-reg slope."""
    return _safe_log(close).rolling(252, min_periods=84).apply(lambda w: _quantile_slope(w, 0.5), raw=True)


def f18_lrch_156_quantile_reg_slope_q90_minus_q10_252d(close: pd.Series) -> pd.Series:
    """Q90-Q10 quantile-reg slope spread."""
    lc = _safe_log(close)
    return lc.rolling(252, min_periods=84).apply(lambda w: _quantile_slope(w, 0.9), raw=True) - lc.rolling(252, min_periods=84).apply(lambda w: _quantile_slope(w, 0.1), raw=True)


def f18_lrch_157_poly2_curvature_63d(close: pd.Series) -> pd.Series:
    """Poly2 curvature 63d."""
    return _safe_log(close).rolling(63, min_periods=21).apply(lambda w: _poly_curvature(w, 2), raw=True)


def f18_lrch_158_poly2_curvature_252d(close: pd.Series) -> pd.Series:
    """Poly2 curvature 252d."""
    return _safe_log(close).rolling(252, min_periods=84).apply(lambda w: _poly_curvature(w, 2), raw=True)


def f18_lrch_159_poly2_neg_curvature_at_upper_band_63d(close: pd.Series) -> pd.Series:
    """Neg curvature at upper band."""
    lc = _safe_log(close)
    curv = lc.rolling(63, min_periods=21).apply(lambda w: _poly_curvature(w, 2), raw=True)
    z = _safe_div(lc - lc.rolling(63, min_periods=21).mean(), lc.rolling(63, min_periods=21).std())
    return ((curv < 0) & (z > 1.0)).astype(float).where(curv.notna() & z.notna(), np.nan)


def f18_lrch_160_poly3_inflection_distance_252d(close: pd.Series) -> pd.Series:
    """Cubic inflection-point distance."""
    return _safe_log(close).rolling(252, min_periods=84).apply(_poly3_inflection_dist, raw=True)


def _ewlr_slope(w, halflife):
    valid = ~np.isnan(w)
    nv = int(valid.sum())
    if nv < 5:
        return np.nan
    x = np.arange(len(w), dtype=float)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    age = (len(w) - 1) - x
    wts = np.power(0.5, age / max(halflife, 1.0))
    sw = wts.sum()
    if sw <= 0:
        return np.nan
    xw = (wts * x).sum() / sw
    yw_ = (wts * yv).sum() / sw
    num = (wts * (x - xw) * (yv - yw_)).sum()
    deno = (wts * (x - xw) ** 2).sum()
    if deno <= 0:
        return np.nan
    return float(num / deno)


def f18_lrch_161_ewlr_slope_halflife_21d(close: pd.Series) -> pd.Series:
    """EWLR slope hl=21."""
    return _safe_log(close).rolling(126, min_periods=42).apply(lambda w: _ewlr_slope(w, 21.0), raw=True)


def f18_lrch_162_ewlr_slope_halflife_63d(close: pd.Series) -> pd.Series:
    """EWLR slope hl=63."""
    return _safe_log(close).rolling(252, min_periods=84).apply(lambda w: _ewlr_slope(w, 63.0), raw=True)


def f18_lrch_163_ewlr_vs_ols_slope_diff_63d(close: pd.Series) -> pd.Series:
    """EWLR minus OLS slope."""
    lc = _safe_log(close)
    return lc.rolling(63, min_periods=21).apply(lambda w: _ewlr_slope(w, 21.0), raw=True) - _rolling_slope(lc, 63, min_periods=21)


def f18_lrch_164_kalman_localslope_endpoint(close: pd.Series) -> pd.Series:
    """Kalman local-linear slope endpoint."""
    _, _, _, sl_path = _kalman_local_lin(_safe_log(close).values)
    return pd.Series(sl_path, index=close.index)


def f18_lrch_165_kalman_slope_volatility_63d(close: pd.Series) -> pd.Series:
    """Kalman slope vol 63d."""
    _, _, _, sl_path = _kalman_local_lin(_safe_log(close).values)
    return pd.Series(sl_path, index=close.index).rolling(63, min_periods=21).std()


def f18_lrch_166_kalman_innovation_zscore_endpoint(close: pd.Series) -> pd.Series:
    """Kalman innovation z 63d."""
    return _safe_log(close).rolling(63, min_periods=21).apply(lambda w: _kalman_local_lin(np.asarray(w, dtype=float))[2], raw=True)


def f18_lrch_167_lowess_local_slope_frac03(close: pd.Series) -> pd.Series:
    """LOWESS slope frac=0.3."""
    return _safe_log(close).rolling(63, min_periods=21).apply(lambda w: _lowess_endpoint_slope(w, frac=0.3)[0], raw=True)


def f18_lrch_168_lowess_endpoint_residual_252d(close: pd.Series) -> pd.Series:
    """LOWESS endpoint residual."""
    return _safe_log(close).rolling(252, min_periods=84).apply(lambda w: _lowess_endpoint_slope(w, frac=0.3)[1], raw=True)


def _hp_trend_slope(w):
    tr = _hp_filter_trend(np.asarray(w, dtype=float), 1600.0)
    if np.isnan(tr).all() or tr.size < 2:
        return np.nan
    return float(tr[-1] - tr[-2])


def _hp_cycle_z(w):
    a = np.asarray(w, dtype=float)
    tr = _hp_filter_trend(a, 1600.0)
    if np.isnan(tr).all():
        return np.nan
    cyc = a - tr
    ok = ~np.isnan(cyc)
    if ok.sum() < 5:
        return np.nan
    sd = float(np.std(cyc[ok], ddof=1))
    if sd <= 0:
        return np.nan
    return float((cyc[-1] - float(np.mean(cyc[ok]))) / sd)


def f18_lrch_169_hp_filter_trend_slope_lambda1600(close: pd.Series) -> pd.Series:
    """HP trend slope lam=1600."""
    return _safe_log(close).rolling(252, min_periods=84).apply(_hp_trend_slope, raw=True)


def f18_lrch_170_hp_filter_cycle_endpoint_zscore(close: pd.Series) -> pd.Series:
    """HP cycle endpoint z."""
    return _safe_log(close).rolling(252, min_periods=84).apply(_hp_cycle_z, raw=True)


def _slope_tstat(w):
    b, a, sd, r2, nv = _ols_pack(w)
    if nv < 3 or np.isnan(sd) or sd <= 0:
        return np.nan
    x = np.arange(len(w), dtype=float)
    valid = ~np.isnan(w)
    if not valid.all():
        x = x[valid]
    xm = x.mean()
    den = float(((x - xm) ** 2).sum())
    if den <= 0:
        return np.nan
    se = sd / np.sqrt(den)
    if se <= 0:
        return np.nan
    return float(b / se)


def f18_lrch_171_slope_tstat_21d(close: pd.Series) -> pd.Series:
    """Slope t-stat 21d."""
    return _safe_log(close).rolling(21, min_periods=7).apply(_slope_tstat, raw=True)


def f18_lrch_172_slope_tstat_504d(close: pd.Series) -> pd.Series:
    """Slope t-stat 504d."""
    return _safe_log(close).rolling(504, min_periods=168).apply(_slope_tstat, raw=True)


def _slope_ci_w(w):
    b, a, sd, r2, nv = _ols_pack(w)
    if nv < 3 or np.isnan(sd) or sd <= 0:
        return np.nan
    x = np.arange(len(w), dtype=float)
    valid = ~np.isnan(w)
    if not valid.all():
        x = x[valid]
    xm = x.mean()
    den = float(((x - xm) ** 2).sum())
    if den <= 0:
        return np.nan
    return float(2.0 * 1.96 * sd / np.sqrt(den))


def f18_lrch_173_slope_ci95_width_63d(close: pd.Series) -> pd.Series:
    """Slope 95% CI width 63d."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_slope_ci_w, raw=True)


def _resid_arr(w):
    b, a, sd, r2, nv = _ols_pack(w)
    if nv < 3:
        return None
    x = np.arange(len(w), dtype=float)
    valid = ~np.isnan(w)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    return yv - (a + b * x)


def _dw_stat(w):
    r = _resid_arr(w)
    if r is None or r.size < 3:
        return np.nan
    den = float((r * r).sum())
    if den <= 0:
        return np.nan
    return float(((r[1:] - r[:-1]) ** 2).sum()) / den


def f18_lrch_174_durbin_watson_residuals_63d(close: pd.Series) -> pd.Series:
    """DW statistic."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_dw_stat, raw=True)


def _lb_q(w):
    r = _resid_arr(w)
    if r is None or r.size < 15:
        return np.nan
    n = r.size
    var = float((r * r).sum())
    if var <= 0:
        return np.nan
    rho2 = [(float((r[k:] * r[:-k]).sum()) / var) ** 2 / max(n - k, 1) for k in range(1, 11)]
    return float(n * (n + 2) * sum(rho2))


def f18_lrch_175_ljung_box_q_residuals_lag10_63d(close: pd.Series) -> pd.Series:
    """Ljung-Box Q lag10."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_lb_q, raw=True)


def _runs_z(w):
    r = _resid_arr(w)
    if r is None or r.size < 10:
        return np.nan
    sgn = np.sign(r)
    sgn = sgn[sgn != 0]
    if sgn.size < 10:
        return np.nan
    n1 = int((sgn > 0).sum()); n2 = int((sgn < 0).sum())
    n = n1 + n2
    if n1 == 0 or n2 == 0:
        return np.nan
    runs = 1 + int((sgn[1:] != sgn[:-1]).sum())
    mu = 2.0 * n1 * n2 / n + 1.0
    var = (2.0 * n1 * n2 * (2.0 * n1 * n2 - n)) / (n * n * (n - 1))
    if var <= 0:
        return np.nan
    return float((runs - mu) / np.sqrt(var))


def f18_lrch_176_runs_test_zscore_residuals_63d(close: pd.Series) -> pd.Series:
    """Runs-test z."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_runs_z, raw=True)


def _mk_tau(w):
    valid = ~np.isnan(w)
    nv = int(valid.sum())
    if nv < 10:
        return np.nan
    yv = w[valid]
    if yv.size > 100:
        idx = np.linspace(0, yv.size - 1, 100).astype(int)
        yv = yv[idx]
    m = yv.size
    i, j = np.triu_indices(m, k=1)
    d = np.sign(yv[j] - yv[i])
    denom = m * (m - 1) / 2.0
    if denom <= 0:
        return np.nan
    return float(d.sum() / denom)


def f18_lrch_177_mann_kendall_tau_252d(close: pd.Series) -> pd.Series:
    """Mann-Kendall tau."""
    return _safe_log(close).rolling(252, min_periods=84).apply(_mk_tau, raw=True)


def _cs_z(w):
    valid = ~np.isnan(w)
    if valid.sum() < 10:
        return np.nan
    yv = w[valid]
    m = yv.size // 2
    if m < 5:
        return np.nan
    d = yv[-m:] - yv[:m]
    d = d[d != 0]
    if d.size < 5:
        return np.nan
    n_pos = int((d > 0).sum())
    n = d.size
    sd = np.sqrt(n / 4.0)
    if sd <= 0:
        return np.nan
    return float((n_pos - n / 2.0) / sd)


def f18_lrch_178_cox_stuart_trend_zscore_252d(close: pd.Series) -> pd.Series:
    """Cox-Stuart z."""
    return _safe_log(close).rolling(252, min_periods=84).apply(_cs_z, raw=True)


def _spear(w):
    valid = ~np.isnan(w)
    nv = int(valid.sum())
    if nv < 5:
        return np.nan
    x = np.arange(len(w), dtype=float)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    rx = pd.Series(x).rank().values
    ry = pd.Series(yv).rank().values
    rxm = rx.mean(); rym = ry.mean()
    d1 = np.sqrt(((rx - rxm) ** 2).sum())
    d2 = np.sqrt(((ry - rym) ** 2).sum())
    if d1 <= 0 or d2 <= 0:
        return np.nan
    return float(((rx - rxm) * (ry - rym)).sum() / (d1 * d2))


def f18_lrch_179_spearman_rank_slope_63d(close: pd.Series) -> pd.Series:
    """Spearman rho."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_spear, raw=True)


def _recursive_slope_path(w):
    """Helper: returns expanding-window slope array for window w."""
    valid = ~np.isnan(w)
    if int(valid.sum()) < 10:
        return None, None
    x = np.arange(len(w), dtype=float)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    n = yv.size
    sl = np.full(n, np.nan)
    rr = np.full(n, np.nan)
    for k in range(3, n):
        xs = x[:k]; ys = yv[:k]
        xm = xs.mean(); ym = ys.mean()
        den = ((xs - xm) ** 2).sum()
        if den <= 0:
            continue
        b = ((xs - xm) * (ys - ym)).sum() / den
        a = ym - b * xm
        sl[k] = b
        xt = x[k]; yt = yv[k]
        f = 1.0 + 1.0 / k + (xt - xm) ** 2 / den
        rr[k] = (yt - (a + b * xt)) / np.sqrt(max(f, 1e-12))
    return sl, rr


def _bp_break(w):
    valid = ~np.isnan(w)
    if int(valid.sum()) < 100:
        return np.nan
    n = w.size
    blk = 21
    slopes = []
    for k in range(0, n - blk + 1, blk):
        sub = w[k:k + blk]
        v = ~np.isnan(sub)
        if v.sum() < 7:
            slopes.append(np.nan); continue
        x = np.arange(blk, dtype=float)[v]; y = sub[v]
        xm = x.mean(); ym = y.mean()
        den = ((x - xm) ** 2).sum()
        if den <= 0:
            slopes.append(np.nan); continue
        slopes.append(((x - xm) * (y - ym)).sum() / den)
    sa = np.array(slopes); sa = sa[~np.isnan(sa)]
    if sa.size < 3:
        return np.nan
    sd = sa.std(ddof=1)
    if sd <= 0:
        return 0.0
    return float((np.abs(np.diff(sa)) > 1.5 * sd).sum())


def f18_lrch_180_bai_perron_break_count_252d(close: pd.Series) -> pd.Series:
    """Bai-Perron break count approx."""
    return _safe_log(close).rolling(252, min_periods=126).apply(_bp_break, raw=True)


def _qa_supf(w):
    valid = ~np.isnan(w)
    if int(valid.sum()) < 60:
        return np.nan
    x = np.arange(len(w), dtype=float)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    n = yv.size
    xm = x.mean(); ym = yv.mean()
    denf = ((x - xm) ** 2).sum()
    if denf <= 0:
        return np.nan
    bf = ((x - xm) * (yv - ym)).sum() / denf
    af = ym - bf * xm
    ssr_full = float(((yv - (af + bf * x)) ** 2).sum())
    best_f = -np.inf
    for tau in range(15, n - 15, max(1, n // 30)):
        x1 = x[:tau]; y1 = yv[:tau]
        x2 = x[tau:]; y2 = yv[tau:]
        if x1.size < 5 or x2.size < 5:
            continue
        xm1 = x1.mean(); ym1 = y1.mean()
        d1 = ((x1 - xm1) ** 2).sum()
        xm2 = x2.mean(); ym2 = y2.mean()
        d2 = ((x2 - xm2) ** 2).sum()
        if d1 <= 0 or d2 <= 0:
            continue
        b1 = ((x1 - xm1) * (y1 - ym1)).sum() / d1; a1 = ym1 - b1 * xm1
        b2 = ((x2 - xm2) * (y2 - ym2)).sum() / d2; a2 = ym2 - b2 * xm2
        ssr_r = float(((y1 - (a1 + b1 * x1)) ** 2).sum() + ((y2 - (a2 + b2 * x2)) ** 2).sum())
        df_r = max(n - 4, 1)
        fs = ((ssr_full - ssr_r) / 2.0) / max(ssr_r / df_r, 1e-12)
        if fs > best_f:
            best_f = fs
    return float(best_f) if best_f > -np.inf else np.nan


def f18_lrch_181_quandt_andrews_supf_504d(close: pd.Series) -> pd.Series:
    """Quandt-Andrews sup-F."""
    return _safe_log(close).rolling(504, min_periods=168).apply(_qa_supf, raw=True)


def f18_lrch_182_cusum_recursive_resid_endpoint_252d(close: pd.Series) -> pd.Series:
    """CUSUM recursive resid."""
    return _safe_log(close).rolling(252, min_periods=84).apply(_cusum_recursive_resid_end, raw=True)


def _cusum_sq(w):
    sl, rr = _recursive_slope_path(w)
    if rr is None:
        return np.nan
    rr2 = rr * rr
    tot = float(np.nansum(rr2))
    if tot <= 0:
        return np.nan
    n = rr.size
    return float(np.nansum(rr2[: 3 * n // 4])) / tot


def f18_lrch_183_cusum_squares_recursive_resid_252d(close: pd.Series) -> pd.Series:
    """CUSUM-of-squares."""
    return _safe_log(close).rolling(252, min_periods=84).apply(_cusum_sq, raw=True)


def _rec_slope_range(w):
    sl, _ = _recursive_slope_path(w)
    if sl is None:
        return np.nan
    ok = ~np.isnan(sl)
    if ok.sum() < 5:
        return np.nan
    return float(np.nanmax(sl) - np.nanmin(sl))


def f18_lrch_184_recursive_slope_range_252d(close: pd.Series) -> pd.Series:
    """Recursive-slope range."""
    return _safe_log(close).rolling(252, min_periods=84).apply(_rec_slope_range, raw=True)


def _adj_r2(w):
    b, a, sd, r2, nv = _ols_pack(w)
    if nv < 5 or np.isnan(r2):
        return np.nan
    return float(1.0 - (1.0 - r2) * (nv - 1) / max(nv - 2, 1))


def f18_lrch_185_adjusted_r2_63d(close: pd.Series) -> pd.Series:
    """Adjusted R2."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_adj_r2, raw=True)


def _aic(w):
    b, a, sd, r2, nv = _ols_pack(w)
    if nv < 5 or np.isnan(sd) or sd <= 0:
        return np.nan
    rss = (sd ** 2) * max(nv - 2, 1)
    return float(nv * np.log(rss / nv) + 4)


def f18_lrch_186_aic_slope_model_63d(close: pd.Series) -> pd.Series:
    """AIC slope model."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_aic, raw=True)


def _fstat_full(w):
    b, a, sd, r2, nv = _ols_pack(w)
    if nv < 5 or np.isnan(r2):
        return np.nan
    denom = 1.0 - r2
    if denom <= 1e-9:
        return np.nan
    return float(r2 / denom * max(nv - 2, 1))


def f18_lrch_187_f_stat_overall_model_63d(close: pd.Series) -> pd.Series:
    """F-stat overall model."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_fstat_full, raw=True)


def _pi_width(w, alpha_z=1.96):
    """Endpoint prediction-interval half-width."""
    b, a, sd, r2, nv = _ols_pack(w)
    if nv < 4 or np.isnan(sd) or sd <= 0:
        return np.nan
    x = np.arange(len(w), dtype=float)
    valid = ~np.isnan(w)
    if not valid.all():
        x = x[valid]
    xm = x.mean()
    den = float(((x - xm) ** 2).sum())
    if den <= 0:
        return np.nan
    xp = len(w) - 1
    return float(2.0 * alpha_z * sd * np.sqrt(1.0 + 1.0 / nv + (xp - xm) ** 2 / den))


def _ci_width(w, alpha_z=1.96):
    """Endpoint mean-response CI half-width (no '1+')."""
    b, a, sd, r2, nv = _ols_pack(w)
    if nv < 4 or np.isnan(sd) or sd <= 0:
        return np.nan
    x = np.arange(len(w), dtype=float)
    valid = ~np.isnan(w)
    if not valid.all():
        x = x[valid]
    xm = x.mean()
    den = float(((x - xm) ** 2).sum())
    if den <= 0:
        return np.nan
    xp = len(w) - 1
    return float(2.0 * alpha_z * sd * np.sqrt(1.0 / nv + (xp - xm) ** 2 / den))


def f18_lrch_188_prediction_interval_width_endpoint_63d(close: pd.Series) -> pd.Series:
    """PI width endpoint."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_pi_width, raw=True)


def _pi_ci_ratio(w):
    pi = _pi_width(w); ci = _ci_width(w)
    if np.isnan(pi) or np.isnan(ci) or ci <= 0:
        return np.nan
    return float(pi / ci)


def f18_lrch_189_pi_to_ci_width_ratio_63d(close: pd.Series) -> pd.Series:
    """PI/CI ratio."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_pi_ci_ratio, raw=True)


def _wh_band(w):
    ci_half = _ci_width(w) / (2.0 * 1.96)
    if np.isnan(ci_half):
        return np.nan
    return float(2.45 * ci_half)


def f18_lrch_190_working_hotelling_band_factor_252d(close: pd.Series) -> pd.Series:
    """Working-Hotelling band."""
    return _safe_log(close).rolling(252, min_periods=84).apply(_wh_band, raw=True)


def f18_lrch_191_residual_sigma_expansion_21d_63d(close: pd.Series) -> pd.Series:
    """Resid sigma 21/63 ratio."""
    lc = _safe_log(close)
    return _safe_div(_rolling_resid_std(lc, 21, min_periods=7), _rolling_resid_std(lc, 63, min_periods=21))


def _stud_end(w):
    b, a, sd, r2, nv = _ols_pack(w)
    if nv < 4 or np.isnan(sd) or sd <= 0:
        return np.nan
    x = np.arange(len(w), dtype=float)
    valid = ~np.isnan(w)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    xm = x.mean()
    den = float(((x - xm) ** 2).sum())
    if den <= 0:
        return np.nan
    hp = 1.0 / nv + (x[-1] - xm) ** 2 / den
    r_end = yv[-1] - (a + b * x[-1])
    denom = sd * np.sqrt(max(1.0 - hp, 1e-12))
    if denom <= 0:
        return np.nan
    return float(r_end / denom)


def f18_lrch_192_studentized_residual_endpoint_63d(close: pd.Series) -> pd.Series:
    """Studentized resid endpoint."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_stud_end, raw=True)


def _ext_stud_max(w):
    b, a, sd, r2, nv = _ols_pack(w)
    if nv < 6 or np.isnan(sd) or sd <= 0:
        return np.nan
    x = np.arange(len(w), dtype=float)
    valid = ~np.isnan(w)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    xm = x.mean()
    den = float(((x - xm) ** 2).sum())
    if den <= 0:
        return np.nan
    h = 1.0 / nv + (x - xm) ** 2 / den
    r = yv - (a + b * x)
    sse = float((r * r).sum())
    denom_i = np.maximum(1.0 - h, 1e-12)
    s_ext = np.sqrt(np.maximum(sse - (r * r) / denom_i, 0.0) / max(nv - 3, 1))
    t = r / (s_ext * np.sqrt(denom_i) + 1e-12)
    return float(np.nanmax(np.abs(t)))


def f18_lrch_193_externally_studentized_resid_max_252d(close: pd.Series) -> pd.Series:
    """Max ext-studentized resid."""
    return _safe_log(close).rolling(252, min_periods=84).apply(_ext_stud_max, raw=True)


def _cooks_end(w):
    b, a, sd, r2, nv = _ols_pack(w)
    if nv < 4 or np.isnan(sd) or sd <= 0:
        return np.nan
    x = np.arange(len(w), dtype=float)
    valid = ~np.isnan(w)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    xm = x.mean()
    den = float(((x - xm) ** 2).sum())
    if den <= 0:
        return np.nan
    h = 1.0 / nv + (x[-1] - xm) ** 2 / den
    r_end = yv[-1] - (a + b * x[-1])
    denom = 2.0 * sd * sd * (1.0 - h) ** 2
    if denom <= 0:
        return np.nan
    return float((r_end ** 2) * h / denom)


def f18_lrch_194_cooks_distance_endpoint_63d(close: pd.Series) -> pd.Series:
    """Cook's D endpoint."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_cooks_end, raw=True)


def _cooks_max(w):
    b, a, sd, r2, nv = _ols_pack(w)
    if nv < 6 or np.isnan(sd) or sd <= 0:
        return np.nan
    x = np.arange(len(w), dtype=float)
    valid = ~np.isnan(w)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    xm = x.mean()
    den = float(((x - xm) ** 2).sum())
    if den <= 0:
        return np.nan
    h = 1.0 / nv + (x - xm) ** 2 / den
    r = yv - (a + b * x)
    denom = 2.0 * sd * sd * (1.0 - h) ** 2
    ok = denom > 0
    cd = np.zeros_like(r)
    cd[ok] = (r[ok] ** 2) * h[ok] / denom[ok]
    return float(cd.max())


def f18_lrch_195_max_cooks_distance_252d(close: pd.Series) -> pd.Series:
    """Max Cook's D."""
    return _safe_log(close).rolling(252, min_periods=84).apply(_cooks_max, raw=True)


def _leverage_end(w):
    valid = ~np.isnan(w)
    nv = int(valid.sum())
    if nv < 4:
        return np.nan
    x = np.arange(len(w), dtype=float)
    if not valid.all():
        x = x[valid]
    xm = x.mean()
    den = float(((x - xm) ** 2).sum())
    if den <= 0:
        return np.nan
    return float(1.0 / nv + (x[-1] - xm) ** 2 / den)


def f18_lrch_196_hat_leverage_endpoint_63d(close: pd.Series) -> pd.Series:
    """Hat leverage endpoint."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_leverage_end, raw=True)


def f18_lrch_197_r2_lag_lead_diff_21d_vs_t_minus_21(close: pd.Series) -> pd.Series:
    """R2 lag-lead diff."""
    r2 = _rolling_r2(_safe_log(close), 63, min_periods=21)
    return r2 - r2.shift(21)


def f18_lrch_198_r2_decay_recent_3_subwindows_63d(close: pd.Series) -> pd.Series:
    """R2 decay 3-subwindows."""
    r21 = _rolling_r2(_safe_log(close), 21, min_periods=7)
    return (r21 - r21.shift(42)) / 2.0


def f18_lrch_199_half_sample_slope_diff_126d(close: pd.Series) -> pd.Series:
    """Half-sample slope diff."""
    s = _rolling_slope(_safe_log(close), 63, min_periods=21)
    return s - s.shift(63)


def _chow_f(w):
    valid = ~np.isnan(w)
    nv = int(valid.sum())
    if nv < 20:
        return np.nan
    x = np.arange(len(w), dtype=float)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    n = yv.size
    xm = x.mean(); ym = yv.mean()
    denf = ((x - xm) ** 2).sum()
    if denf <= 0:
        return np.nan
    bf = ((x - xm) * (yv - ym)).sum() / denf
    af = ym - bf * xm
    ssr_full = float(((yv - (af + bf * x)) ** 2).sum())
    tau = n // 2
    x1 = x[:tau]; y1 = yv[:tau]
    x2 = x[tau:]; y2 = yv[tau:]
    if x1.size < 5 or x2.size < 5:
        return np.nan
    xm1 = x1.mean(); ym1 = y1.mean()
    d1 = ((x1 - xm1) ** 2).sum()
    xm2 = x2.mean(); ym2 = y2.mean()
    d2 = ((x2 - xm2) ** 2).sum()
    if d1 <= 0 or d2 <= 0:
        return np.nan
    b1 = ((x1 - xm1) * (y1 - ym1)).sum() / d1; a1 = ym1 - b1 * xm1
    b2 = ((x2 - xm2) * (y2 - ym2)).sum() / d2; a2 = ym2 - b2 * xm2
    ssr_r = float(((y1 - (a1 + b1 * x1)) ** 2).sum() + ((y2 - (a2 + b2 * x2)) ** 2).sum())
    return float(((ssr_full - ssr_r) / 2.0) / max(ssr_r / max(n - 4, 1), 1e-12))


def f18_lrch_200_chow_f_statistic_126d_split(close: pd.Series) -> pd.Series:
    """Chow-F mid-split."""
    return _safe_log(close).rolling(126, min_periods=42).apply(_chow_f, raw=True)


def f18_lrch_201_multi_horizon_r2_variance_3h(close: pd.Series) -> pd.Series:
    """R2 variance 3-horizon."""
    lc = _safe_log(close)
    return pd.concat([_rolling_r2(lc, 21, min_periods=7).rename(0), _rolling_r2(lc, 63, min_periods=21).rename(1), _rolling_r2(lc, 252, min_periods=84).rename(2)], axis=1).var(axis=1)


def f18_lrch_202_slope_angle_degrees_63d(close: pd.Series) -> pd.Series:
    """Slope angle 63d."""
    return np.degrees(np.arctan(_rolling_slope(_safe_log(close), 63, min_periods=21)))


def f18_lrch_203_slope_angle_degrees_252d(close: pd.Series) -> pd.Series:
    """Slope angle 252d."""
    return np.degrees(np.arctan(_rolling_slope(_safe_log(close), 252, min_periods=84)))


def _bayes_pack(w, prior_sd=1.0):
    b, a, sd, r2, nv = _ols_pack(w)
    if nv < 5 or np.isnan(sd) or sd <= 0:
        return (np.nan, np.nan)
    x = np.arange(len(w), dtype=float)
    valid = ~np.isnan(w)
    if not valid.all():
        x = x[valid]
    xm = x.mean()
    den = float(((x - xm) ** 2).sum())
    if den <= 0:
        return (np.nan, np.nan)
    tau2 = (sd / np.sqrt(den)) ** 2
    tau02 = prior_sd * prior_sd
    pv = 1.0 / (1.0 / tau02 + 1.0 / tau2)
    return (float(pv * (b / tau2)), float(np.sqrt(pv)))


def f18_lrch_204_bayesian_posterior_slope_mean_63d(close: pd.Series) -> pd.Series:
    """Bayes post-mean slope."""
    return _safe_log(close).rolling(63, min_periods=21).apply(lambda w: _bayes_pack(w)[0], raw=True)


def f18_lrch_205_bayesian_posterior_slope_sd_63d(close: pd.Series) -> pd.Series:
    """Bayes post-sd slope."""
    return _safe_log(close).rolling(63, min_periods=21).apply(lambda w: _bayes_pack(w)[1], raw=True)


def _cp_mid(w):
    valid = ~np.isnan(w)
    if int(valid.sum()) < 40:
        return np.nan
    x = np.arange(len(w), dtype=float)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    n = yv.size
    xm = x.mean(); ym = yv.mean()
    denf = ((x - xm) ** 2).sum()
    if denf <= 0:
        return np.nan
    bf = ((x - xm) * (yv - ym)).sum() / denf
    af = ym - bf * xm
    ssr_full = float(((yv - (af + bf * x)) ** 2).sum())
    best_drop = -np.inf; best_tau = np.nan
    for tau in range(10, n - 10, max(1, n // 30)):
        x1 = x[:tau]; y1 = yv[:tau]
        x2 = x[tau:]; y2 = yv[tau:]
        xm1 = x1.mean(); ym1 = y1.mean()
        d1 = ((x1 - xm1) ** 2).sum()
        xm2 = x2.mean(); ym2 = y2.mean()
        d2 = ((x2 - xm2) ** 2).sum()
        if d1 <= 0 or d2 <= 0:
            continue
        b1 = ((x1 - xm1) * (y1 - ym1)).sum() / d1; a1 = ym1 - b1 * xm1
        b2 = ((x2 - xm2) * (y2 - ym2)).sum() / d2; a2 = ym2 - b2 * xm2
        ssr_r = float(((y1 - (a1 + b1 * x1)) ** 2).sum() + ((y2 - (a2 + b2 * x2)) ** 2).sum())
        drop = ssr_full - ssr_r
        if drop > best_drop:
            best_drop = drop; best_tau = tau / float(n)
    return float(best_tau)


def f18_lrch_206_slope_changepoint_midpoint_252d(close: pd.Series) -> pd.Series:
    """Changepoint loc."""
    return _safe_log(close).rolling(252, min_periods=84).apply(_cp_mid, raw=True)


def _asym(w):
    r = _resid_arr(w)
    if r is None or r.size < 5:
        return np.nan
    pos = float(r[r > 0].max()) if (r > 0).any() else 0.0
    neg = float(-r[r < 0].min()) if (r < 0).any() else 0.0
    if neg <= 0:
        return np.nan
    return pos / neg


def f18_lrch_207_channel_asymmetry_upper_vs_lower_dist_63d(close: pd.Series) -> pd.Series:
    """Channel asymmetry."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_asym, raw=True)


def _breach1(w):
    r = _resid_arr(w)
    if r is None or r.size < 5:
        return np.nan
    sd = float(np.std(r, ddof=1))
    if sd <= 0:
        return np.nan
    return float((np.abs(r) > sd).sum())


def f18_lrch_208_breach_count_1sigma_63d(close: pd.Series) -> pd.Series:
    """1-sigma breach count."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_breach1, raw=True)


def _mean_sign(w):
    r = _resid_arr(w)
    if r is None or r.size < 5:
        return np.nan
    return float(np.mean(np.sign(r)))


def f18_lrch_209_mean_residual_sign_252d(close: pd.Series) -> pd.Series:
    """Mean residual sign."""
    return _safe_log(close).rolling(252, min_periods=84).apply(_mean_sign, raw=True)


def _arch_lm(w):
    r = _resid_arr(w)
    if r is None or r.size < 15:
        return np.nan
    r2 = r * r
    n = r2.size
    if n < 12:
        return np.nan
    Y = r2[5:]
    X = np.column_stack([np.ones(n - 5)] + [r2[5 - k:n - k] for k in range(1, 6)])
    try:
        beta, *_ = np.linalg.lstsq(X, Y, rcond=None)
    except np.linalg.LinAlgError:
        return np.nan
    ss_res = float(((Y - X @ beta) ** 2).sum())
    ss_tot = float(((Y - Y.mean()) ** 2).sum())
    if ss_tot <= 0:
        return np.nan
    return float((n - 5) * (1.0 - ss_res / ss_tot))


def f18_lrch_210_arch_lm_residuals_lag5_63d(close: pd.Series) -> pd.Series:
    """ARCH-LM lag5."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_arch_lm, raw=True)


def _bp_het(w):
    r = _resid_arr(w)
    if r is None or r.size < 8:
        return np.nan
    n = r.size
    x = np.arange(n, dtype=float)
    r2 = r * r
    xm = x.mean(); rm = r2.mean()
    denx = ((x - xm) ** 2).sum()
    if denx <= 0:
        return np.nan
    b = ((x - xm) * (r2 - rm)).sum() / denx
    a = rm - b * xm
    rss = float(((r2 - (a + b * x)) ** 2).sum())
    tss = float(((r2 - rm) ** 2).sum())
    if tss <= 0:
        return np.nan
    return float(n * (1.0 - rss / tss))


def f18_lrch_211_breusch_pagan_het_test_63d(close: pd.Series) -> pd.Series:
    """Breusch-Pagan."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_bp_het, raw=True)


def _bg_lm(w):
    r = _resid_arr(w)
    if r is None or r.size < 10:
        return np.nan
    n = r.size
    if n < 7:
        return np.nan
    Y = r[2:]
    X = np.column_stack([np.ones(n - 2), r[1:n - 1], r[0:n - 2]])
    try:
        beta, *_ = np.linalg.lstsq(X, Y, rcond=None)
    except np.linalg.LinAlgError:
        return np.nan
    ss_res = float(((Y - X @ beta) ** 2).sum())
    ss_tot = float(((Y - Y.mean()) ** 2).sum())
    if ss_tot <= 0:
        return np.nan
    return float((n - 2) * (1.0 - ss_res / ss_tot))


def f18_lrch_212_breusch_godfrey_lm_lag2_63d(close: pd.Series) -> pd.Series:
    """Breusch-Godfrey lag2."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_bg_lm, raw=True)


def _co_gls(w):
    valid = ~np.isnan(w)
    nv = int(valid.sum())
    if nv < 15:
        return np.nan
    x = np.arange(len(w), dtype=float)
    yv = w
    if not valid.all():
        x = x[valid]; yv = w[valid]
    xm = x.mean(); ym = yv.mean()
    den = ((x - xm) ** 2).sum()
    if den <= 0:
        return np.nan
    b = ((x - xm) * (yv - ym)).sum() / den
    a = ym - b * xm
    for _ in range(5):
        r = yv - (a + b * x)
        if r.size < 3:
            return np.nan
        de = (r[:-1] * r[:-1]).sum()
        if de <= 0:
            break
        rho = max(min((r[1:] * r[:-1]).sum() / de, 0.999), -0.999)
        y_t = yv[1:] - rho * yv[:-1]
        x_t = x[1:] - rho * x[:-1]
        xtm = x_t.mean(); ytm = y_t.mean()
        dnew = ((x_t - xtm) ** 2).sum()
        if dnew <= 0:
            break
        bn = ((x_t - xtm) * (y_t - ytm)).sum() / dnew
        an = (ytm - bn * xtm) / max(1.0 - rho, 1e-9)
        if abs(bn - b) < 1e-9:
            b, a = bn, an
            break
        b, a = bn, an
    return float(b)


def f18_lrch_213_gls_cochrane_orcutt_slope_252d(close: pd.Series) -> pd.Series:
    """Cochrane-Orcutt GLS slope."""
    return _safe_log(close).rolling(252, min_periods=84).apply(_co_gls, raw=True)


def _hampel_sig(w):
    r = _resid_arr(w)
    if r is None or r.size < 5:
        return np.nan
    med = float(np.median(r))
    return float(1.4826 * float(np.median(np.abs(r - med))))


def f18_lrch_214_hampel_residual_sigma_63d(close: pd.Series) -> pd.Series:
    """Hampel residual sigma."""
    return _safe_log(close).rolling(63, min_periods=21).apply(_hampel_sig, raw=True)


_ENS_H = [(21, 7), (42, 14), (63, 21), (126, 42), (252, 84), (504, 168)]


def _ens_df(close):
    lc = _safe_log(close)
    return pd.concat([_rolling_slope(lc, h, min_periods=mp).rename(h) for h, mp in _ENS_H], axis=1)


def f18_lrch_215_multi_window_slope_ensemble_mean(close: pd.Series) -> pd.Series:
    """Multi-window slope mean."""
    return _ens_df(close).mean(axis=1)


def f18_lrch_216_multi_window_slope_ensemble_disp(close: pd.Series) -> pd.Series:
    """Multi-window slope disp."""
    return _ens_df(close).std(axis=1)


def f18_lrch_217_slope_zero_cross_hysteresis_252d(close: pd.Series) -> pd.Series:
    """Slope zero-cross hysteresis."""
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    th = 0.5 * sl.rolling(252, min_periods=84).std()
    arr = sl.values; tha = th.values
    n = arr.size
    state = np.zeros(n); cur = 0
    for i in range(n):
        if np.isnan(arr[i]) or np.isnan(tha[i]):
            state[i] = np.nan; continue
        if cur == 0:
            if arr[i] > tha[i]: cur = 1
            elif arr[i] < -tha[i]: cur = -1
        elif cur == 1 and arr[i] < -tha[i]: cur = -1
        elif cur == -1 and arr[i] > tha[i]: cur = 1
        state[i] = cur
    st = pd.Series(state, index=sl.index)
    return (st != st.shift(1)).astype(float).where(st.notna() & st.shift(1).notna(), np.nan).rolling(252, min_periods=84).sum()


def f18_lrch_218_stale_trend_indicator_63d(close: pd.Series) -> pd.Series:
    """Stale-trend indicator."""
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    sg = np.sign(sl)
    am = sl.abs().rolling(252, min_periods=84).median()
    return ((sg == sg.shift(63)).astype(float) * (sl.abs() < am).astype(float)).where(sg.notna() & sg.shift(63).notna() & am.notna(), np.nan)


def _rec_drift(w):
    sl, _ = _recursive_slope_path(w)
    if sl is None:
        return np.nan
    ok = ~np.isnan(sl)
    if ok.sum() < 5:
        return np.nan
    idx = np.arange(sl.size, dtype=float)[ok]
    slv = sl[ok]
    im = idx.mean(); sm = slv.mean()
    d2 = ((idx - im) ** 2).sum()
    if d2 <= 0:
        return np.nan
    return float(((idx - im) * (slv - sm)).sum() / d2)


def f18_lrch_219_recursive_slope_drift_252d(close: pd.Series) -> pd.Series:
    """Recursive-slope drift."""
    return _safe_log(close).rolling(252, min_periods=84).apply(_rec_drift, raw=True)


def _resid_acf_k(w, k):
    r = _resid_arr(w)
    if r is None or r.size <= k + 1:
        return np.nan
    rm = r.mean()
    den = ((r - rm) ** 2).sum()
    if den <= 0:
        return np.nan
    return float(((r[k:] - rm) * (r[:-k] - rm)).sum() / den)


def f18_lrch_220_residual_acf_lag1_63d(close: pd.Series) -> pd.Series:
    """Residual ACF lag1."""
    return _safe_log(close).rolling(63, min_periods=21).apply(lambda w: _resid_acf_k(w, 1), raw=True)


def f18_lrch_221_residual_acf_lag5_63d(close: pd.Series) -> pd.Series:
    """Residual ACF lag5."""
    return _safe_log(close).rolling(63, min_periods=21).apply(lambda w: _resid_acf_k(w, 5), raw=True)


def _gq(w):
    r = _resid_arr(w)
    if r is None or r.size < 12:
        return np.nan
    third = r.size // 3
    if third < 3:
        return np.nan
    var_e = float(np.var(r[:third], ddof=1))
    if var_e <= 0:
        return np.nan
    return float(float(np.var(r[-third:], ddof=1)) / var_e)


def f18_lrch_222_resid_var_ratio_late_vs_early_126d(close: pd.Series) -> pd.Series:
    """Goldfeld-Quandt var-ratio."""
    return _safe_log(close).rolling(126, min_periods=42).apply(_gq, raw=True)


def f18_lrch_223_terminal_channel_robust_composite_63d(close: pd.Series) -> pd.Series:
    """Terminal robust composite."""
    lc = _safe_log(close)
    hs = lc.rolling(63, min_periods=21).apply(lambda w: _huber_slope(w)[0], raw=True)
    hr = lc.rolling(63, min_periods=21).apply(lambda w: _huber_slope(w)[1], raw=True)
    med = hr.rolling(252, min_periods=84).median()
    sr = lc.rolling(63, min_periods=21).apply(_stud_end, raw=True)
    return ((hs < 0).astype(float) + (hr > med).astype(float) + (sr > 1.5).astype(float)).where(hs.notna() & med.notna() & sr.notna(), np.nan)


def f18_lrch_224_curvature_sign_flip_count_252d_63d(close: pd.Series) -> pd.Series:
    """Curvature sign-flip count."""
    cv = _safe_log(close).rolling(63, min_periods=21).apply(lambda w: _poly_curvature(w, 2), raw=True)
    sg = np.sign(cv)
    return (sg != sg.shift(1)).astype(float).where(cv.notna() & cv.shift(1).notna(), np.nan).rolling(252, min_periods=84).sum()


def f18_lrch_225_kalman_slope_sign_change_event_63d(close: pd.Series) -> pd.Series:
    """Kalman slope sign-change events."""
    _, _, _, sl_path = _kalman_local_lin(_safe_log(close).values)
    sg = np.sign(pd.Series(sl_path, index=close.index))
    return (sg != sg.shift(1)).astype(float).where(sg.notna() & sg.shift(1).notna(), np.nan).rolling(63, min_periods=21).sum()




def f18_lrch_151_theilsen_slope_63d_d3(close):
    return f18_lrch_151_theilsen_slope_63d(close).diff().diff().diff()


def f18_lrch_152_huber_slope_63d_d3(close):
    return f18_lrch_152_huber_slope_63d(close).diff().diff().diff()


def f18_lrch_153_huber_residual_sigma_63d_d3(close):
    return f18_lrch_153_huber_residual_sigma_63d(close).diff().diff().diff()


def f18_lrch_154_lts_slope_252d_d3(close):
    return f18_lrch_154_lts_slope_252d(close).diff().diff().diff()


def f18_lrch_155_quantile_reg_slope_q50_252d_d3(close):
    return f18_lrch_155_quantile_reg_slope_q50_252d(close).diff().diff().diff()


def f18_lrch_156_quantile_reg_slope_q90_minus_q10_252d_d3(close):
    return f18_lrch_156_quantile_reg_slope_q90_minus_q10_252d(close).diff().diff().diff()


def f18_lrch_157_poly2_curvature_63d_d3(close):
    return f18_lrch_157_poly2_curvature_63d(close).diff().diff().diff()


def f18_lrch_158_poly2_curvature_252d_d3(close):
    return f18_lrch_158_poly2_curvature_252d(close).diff().diff().diff()


def f18_lrch_159_poly2_neg_curvature_at_upper_band_63d_d3(close):
    return f18_lrch_159_poly2_neg_curvature_at_upper_band_63d(close).diff().diff().diff()


def f18_lrch_160_poly3_inflection_distance_252d_d3(close):
    return f18_lrch_160_poly3_inflection_distance_252d(close).diff().diff().diff()


def f18_lrch_161_ewlr_slope_halflife_21d_d3(close):
    return f18_lrch_161_ewlr_slope_halflife_21d(close).diff().diff().diff()


def f18_lrch_162_ewlr_slope_halflife_63d_d3(close):
    return f18_lrch_162_ewlr_slope_halflife_63d(close).diff().diff().diff()


def f18_lrch_163_ewlr_vs_ols_slope_diff_63d_d3(close):
    return f18_lrch_163_ewlr_vs_ols_slope_diff_63d(close).diff().diff().diff()


def f18_lrch_164_kalman_localslope_endpoint_d3(close):
    return f18_lrch_164_kalman_localslope_endpoint(close).diff().diff().diff()


def f18_lrch_165_kalman_slope_volatility_63d_d3(close):
    return f18_lrch_165_kalman_slope_volatility_63d(close).diff().diff().diff()


def f18_lrch_166_kalman_innovation_zscore_endpoint_d3(close):
    return f18_lrch_166_kalman_innovation_zscore_endpoint(close).diff().diff().diff()


def f18_lrch_167_lowess_local_slope_frac03_d3(close):
    return f18_lrch_167_lowess_local_slope_frac03(close).diff().diff().diff()


def f18_lrch_168_lowess_endpoint_residual_252d_d3(close):
    return f18_lrch_168_lowess_endpoint_residual_252d(close).diff().diff().diff()


def f18_lrch_169_hp_filter_trend_slope_lambda1600_d3(close):
    return f18_lrch_169_hp_filter_trend_slope_lambda1600(close).diff().diff().diff()


def f18_lrch_170_hp_filter_cycle_endpoint_zscore_d3(close):
    return f18_lrch_170_hp_filter_cycle_endpoint_zscore(close).diff().diff().diff()


def f18_lrch_171_slope_tstat_21d_d3(close):
    return f18_lrch_171_slope_tstat_21d(close).diff().diff().diff()


def f18_lrch_172_slope_tstat_504d_d3(close):
    return f18_lrch_172_slope_tstat_504d(close).diff().diff().diff()


def f18_lrch_173_slope_ci95_width_63d_d3(close):
    return f18_lrch_173_slope_ci95_width_63d(close).diff().diff().diff()


def f18_lrch_174_durbin_watson_residuals_63d_d3(close):
    return f18_lrch_174_durbin_watson_residuals_63d(close).diff().diff().diff()


def f18_lrch_175_ljung_box_q_residuals_lag10_63d_d3(close):
    return f18_lrch_175_ljung_box_q_residuals_lag10_63d(close).diff().diff().diff()


def f18_lrch_176_runs_test_zscore_residuals_63d_d3(close):
    return f18_lrch_176_runs_test_zscore_residuals_63d(close).diff().diff().diff()


def f18_lrch_177_mann_kendall_tau_252d_d3(close):
    return f18_lrch_177_mann_kendall_tau_252d(close).diff().diff().diff()


def f18_lrch_178_cox_stuart_trend_zscore_252d_d3(close):
    return f18_lrch_178_cox_stuart_trend_zscore_252d(close).diff().diff().diff()


def f18_lrch_179_spearman_rank_slope_63d_d3(close):
    return f18_lrch_179_spearman_rank_slope_63d(close).diff().diff().diff()


def f18_lrch_180_bai_perron_break_count_252d_d3(close):
    return f18_lrch_180_bai_perron_break_count_252d(close).diff().diff().diff()


def f18_lrch_181_quandt_andrews_supf_504d_d3(close):
    return f18_lrch_181_quandt_andrews_supf_504d(close).diff().diff().diff()


def f18_lrch_182_cusum_recursive_resid_endpoint_252d_d3(close):
    return f18_lrch_182_cusum_recursive_resid_endpoint_252d(close).diff().diff().diff()


def f18_lrch_183_cusum_squares_recursive_resid_252d_d3(close):
    return f18_lrch_183_cusum_squares_recursive_resid_252d(close).diff().diff().diff()


def f18_lrch_184_recursive_slope_range_252d_d3(close):
    return f18_lrch_184_recursive_slope_range_252d(close).diff().diff().diff()


def f18_lrch_185_adjusted_r2_63d_d3(close):
    return f18_lrch_185_adjusted_r2_63d(close).diff().diff().diff()


def f18_lrch_186_aic_slope_model_63d_d3(close):
    return f18_lrch_186_aic_slope_model_63d(close).diff().diff().diff()


def f18_lrch_187_f_stat_overall_model_63d_d3(close):
    return f18_lrch_187_f_stat_overall_model_63d(close).diff().diff().diff()


def f18_lrch_188_prediction_interval_width_endpoint_63d_d3(close):
    return f18_lrch_188_prediction_interval_width_endpoint_63d(close).diff().diff().diff()


def f18_lrch_189_pi_to_ci_width_ratio_63d_d3(close):
    return f18_lrch_189_pi_to_ci_width_ratio_63d(close).diff().diff().diff()


def f18_lrch_190_working_hotelling_band_factor_252d_d3(close):
    return f18_lrch_190_working_hotelling_band_factor_252d(close).diff().diff().diff()


def f18_lrch_191_residual_sigma_expansion_21d_63d_d3(close):
    return f18_lrch_191_residual_sigma_expansion_21d_63d(close).diff().diff().diff()


def f18_lrch_192_studentized_residual_endpoint_63d_d3(close):
    return f18_lrch_192_studentized_residual_endpoint_63d(close).diff().diff().diff()


def f18_lrch_193_externally_studentized_resid_max_252d_d3(close):
    return f18_lrch_193_externally_studentized_resid_max_252d(close).diff().diff().diff()


def f18_lrch_194_cooks_distance_endpoint_63d_d3(close):
    return f18_lrch_194_cooks_distance_endpoint_63d(close).diff().diff().diff()


def f18_lrch_195_max_cooks_distance_252d_d3(close):
    return f18_lrch_195_max_cooks_distance_252d(close).diff().diff().diff()


def f18_lrch_196_hat_leverage_endpoint_63d_d3(close):
    return f18_lrch_196_hat_leverage_endpoint_63d(close).diff().diff().diff()


def f18_lrch_197_r2_lag_lead_diff_21d_vs_t_minus_21_d3(close):
    return f18_lrch_197_r2_lag_lead_diff_21d_vs_t_minus_21(close).diff().diff().diff()


def f18_lrch_198_r2_decay_recent_3_subwindows_63d_d3(close):
    return f18_lrch_198_r2_decay_recent_3_subwindows_63d(close).diff().diff().diff()


def f18_lrch_199_half_sample_slope_diff_126d_d3(close):
    return f18_lrch_199_half_sample_slope_diff_126d(close).diff().diff().diff()


def f18_lrch_200_chow_f_statistic_126d_split_d3(close):
    return f18_lrch_200_chow_f_statistic_126d_split(close).diff().diff().diff()


def f18_lrch_201_multi_horizon_r2_variance_3h_d3(close):
    return f18_lrch_201_multi_horizon_r2_variance_3h(close).diff().diff().diff()


def f18_lrch_202_slope_angle_degrees_63d_d3(close):
    return f18_lrch_202_slope_angle_degrees_63d(close).diff().diff().diff()


def f18_lrch_203_slope_angle_degrees_252d_d3(close):
    return f18_lrch_203_slope_angle_degrees_252d(close).diff().diff().diff()


def f18_lrch_204_bayesian_posterior_slope_mean_63d_d3(close):
    return f18_lrch_204_bayesian_posterior_slope_mean_63d(close).diff().diff().diff()


def f18_lrch_205_bayesian_posterior_slope_sd_63d_d3(close):
    return f18_lrch_205_bayesian_posterior_slope_sd_63d(close).diff().diff().diff()


def f18_lrch_206_slope_changepoint_midpoint_252d_d3(close):
    return f18_lrch_206_slope_changepoint_midpoint_252d(close).diff().diff().diff()


def f18_lrch_207_channel_asymmetry_upper_vs_lower_dist_63d_d3(close):
    return f18_lrch_207_channel_asymmetry_upper_vs_lower_dist_63d(close).diff().diff().diff()


def f18_lrch_208_breach_count_1sigma_63d_d3(close):
    return f18_lrch_208_breach_count_1sigma_63d(close).diff().diff().diff()


def f18_lrch_209_mean_residual_sign_252d_d3(close):
    return f18_lrch_209_mean_residual_sign_252d(close).diff().diff().diff()


def f18_lrch_210_arch_lm_residuals_lag5_63d_d3(close):
    return f18_lrch_210_arch_lm_residuals_lag5_63d(close).diff().diff().diff()


def f18_lrch_211_breusch_pagan_het_test_63d_d3(close):
    return f18_lrch_211_breusch_pagan_het_test_63d(close).diff().diff().diff()


def f18_lrch_212_breusch_godfrey_lm_lag2_63d_d3(close):
    return f18_lrch_212_breusch_godfrey_lm_lag2_63d(close).diff().diff().diff()


def f18_lrch_213_gls_cochrane_orcutt_slope_252d_d3(close):
    return f18_lrch_213_gls_cochrane_orcutt_slope_252d(close).diff().diff().diff()


def f18_lrch_214_hampel_residual_sigma_63d_d3(close):
    return f18_lrch_214_hampel_residual_sigma_63d(close).diff().diff().diff()


def f18_lrch_215_multi_window_slope_ensemble_mean_d3(close):
    return f18_lrch_215_multi_window_slope_ensemble_mean(close).diff().diff().diff()


def f18_lrch_216_multi_window_slope_ensemble_disp_d3(close):
    return f18_lrch_216_multi_window_slope_ensemble_disp(close).diff().diff().diff()


def f18_lrch_217_slope_zero_cross_hysteresis_252d_d3(close):
    return f18_lrch_217_slope_zero_cross_hysteresis_252d(close).diff().diff().diff()


def f18_lrch_218_stale_trend_indicator_63d_d3(close):
    return f18_lrch_218_stale_trend_indicator_63d(close).diff().diff().diff()


def f18_lrch_219_recursive_slope_drift_252d_d3(close):
    return f18_lrch_219_recursive_slope_drift_252d(close).diff().diff().diff()


def f18_lrch_220_residual_acf_lag1_63d_d3(close):
    return f18_lrch_220_residual_acf_lag1_63d(close).diff().diff().diff()


def f18_lrch_221_residual_acf_lag5_63d_d3(close):
    return f18_lrch_221_residual_acf_lag5_63d(close).diff().diff().diff()


def f18_lrch_222_resid_var_ratio_late_vs_early_126d_d3(close):
    return f18_lrch_222_resid_var_ratio_late_vs_early_126d(close).diff().diff().diff()


def f18_lrch_223_terminal_channel_robust_composite_63d_d3(close):
    return f18_lrch_223_terminal_channel_robust_composite_63d(close).diff().diff().diff()


def f18_lrch_224_curvature_sign_flip_count_252d_63d_d3(close):
    return f18_lrch_224_curvature_sign_flip_count_252d_63d(close).diff().diff().diff()


def f18_lrch_225_kalman_slope_sign_change_event_63d_d3(close):
    return f18_lrch_225_kalman_slope_sign_change_event_63d(close).diff().diff().diff()


LINEAR_REGRESSION_CHANNEL_D3_REGISTRY_151_225 = {
    "f18_lrch_151_theilsen_slope_63d_d3": {"inputs": ["close"], "func": f18_lrch_151_theilsen_slope_63d_d3},
    "f18_lrch_152_huber_slope_63d_d3": {"inputs": ["close"], "func": f18_lrch_152_huber_slope_63d_d3},
    "f18_lrch_153_huber_residual_sigma_63d_d3": {"inputs": ["close"], "func": f18_lrch_153_huber_residual_sigma_63d_d3},
    "f18_lrch_154_lts_slope_252d_d3": {"inputs": ["close"], "func": f18_lrch_154_lts_slope_252d_d3},
    "f18_lrch_155_quantile_reg_slope_q50_252d_d3": {"inputs": ["close"], "func": f18_lrch_155_quantile_reg_slope_q50_252d_d3},
    "f18_lrch_156_quantile_reg_slope_q90_minus_q10_252d_d3": {"inputs": ["close"], "func": f18_lrch_156_quantile_reg_slope_q90_minus_q10_252d_d3},
    "f18_lrch_157_poly2_curvature_63d_d3": {"inputs": ["close"], "func": f18_lrch_157_poly2_curvature_63d_d3},
    "f18_lrch_158_poly2_curvature_252d_d3": {"inputs": ["close"], "func": f18_lrch_158_poly2_curvature_252d_d3},
    "f18_lrch_159_poly2_neg_curvature_at_upper_band_63d_d3": {"inputs": ["close"], "func": f18_lrch_159_poly2_neg_curvature_at_upper_band_63d_d3},
    "f18_lrch_160_poly3_inflection_distance_252d_d3": {"inputs": ["close"], "func": f18_lrch_160_poly3_inflection_distance_252d_d3},
    "f18_lrch_161_ewlr_slope_halflife_21d_d3": {"inputs": ["close"], "func": f18_lrch_161_ewlr_slope_halflife_21d_d3},
    "f18_lrch_162_ewlr_slope_halflife_63d_d3": {"inputs": ["close"], "func": f18_lrch_162_ewlr_slope_halflife_63d_d3},
    "f18_lrch_163_ewlr_vs_ols_slope_diff_63d_d3": {"inputs": ["close"], "func": f18_lrch_163_ewlr_vs_ols_slope_diff_63d_d3},
    "f18_lrch_164_kalman_localslope_endpoint_d3": {"inputs": ["close"], "func": f18_lrch_164_kalman_localslope_endpoint_d3},
    "f18_lrch_165_kalman_slope_volatility_63d_d3": {"inputs": ["close"], "func": f18_lrch_165_kalman_slope_volatility_63d_d3},
    "f18_lrch_166_kalman_innovation_zscore_endpoint_d3": {"inputs": ["close"], "func": f18_lrch_166_kalman_innovation_zscore_endpoint_d3},
    "f18_lrch_167_lowess_local_slope_frac03_d3": {"inputs": ["close"], "func": f18_lrch_167_lowess_local_slope_frac03_d3},
    "f18_lrch_168_lowess_endpoint_residual_252d_d3": {"inputs": ["close"], "func": f18_lrch_168_lowess_endpoint_residual_252d_d3},
    "f18_lrch_169_hp_filter_trend_slope_lambda1600_d3": {"inputs": ["close"], "func": f18_lrch_169_hp_filter_trend_slope_lambda1600_d3},
    "f18_lrch_170_hp_filter_cycle_endpoint_zscore_d3": {"inputs": ["close"], "func": f18_lrch_170_hp_filter_cycle_endpoint_zscore_d3},
    "f18_lrch_171_slope_tstat_21d_d3": {"inputs": ["close"], "func": f18_lrch_171_slope_tstat_21d_d3},
    "f18_lrch_172_slope_tstat_504d_d3": {"inputs": ["close"], "func": f18_lrch_172_slope_tstat_504d_d3},
    "f18_lrch_173_slope_ci95_width_63d_d3": {"inputs": ["close"], "func": f18_lrch_173_slope_ci95_width_63d_d3},
    "f18_lrch_174_durbin_watson_residuals_63d_d3": {"inputs": ["close"], "func": f18_lrch_174_durbin_watson_residuals_63d_d3},
    "f18_lrch_175_ljung_box_q_residuals_lag10_63d_d3": {"inputs": ["close"], "func": f18_lrch_175_ljung_box_q_residuals_lag10_63d_d3},
    "f18_lrch_176_runs_test_zscore_residuals_63d_d3": {"inputs": ["close"], "func": f18_lrch_176_runs_test_zscore_residuals_63d_d3},
    "f18_lrch_177_mann_kendall_tau_252d_d3": {"inputs": ["close"], "func": f18_lrch_177_mann_kendall_tau_252d_d3},
    "f18_lrch_178_cox_stuart_trend_zscore_252d_d3": {"inputs": ["close"], "func": f18_lrch_178_cox_stuart_trend_zscore_252d_d3},
    "f18_lrch_179_spearman_rank_slope_63d_d3": {"inputs": ["close"], "func": f18_lrch_179_spearman_rank_slope_63d_d3},
    "f18_lrch_180_bai_perron_break_count_252d_d3": {"inputs": ["close"], "func": f18_lrch_180_bai_perron_break_count_252d_d3},
    "f18_lrch_181_quandt_andrews_supf_504d_d3": {"inputs": ["close"], "func": f18_lrch_181_quandt_andrews_supf_504d_d3},
    "f18_lrch_182_cusum_recursive_resid_endpoint_252d_d3": {"inputs": ["close"], "func": f18_lrch_182_cusum_recursive_resid_endpoint_252d_d3},
    "f18_lrch_183_cusum_squares_recursive_resid_252d_d3": {"inputs": ["close"], "func": f18_lrch_183_cusum_squares_recursive_resid_252d_d3},
    "f18_lrch_184_recursive_slope_range_252d_d3": {"inputs": ["close"], "func": f18_lrch_184_recursive_slope_range_252d_d3},
    "f18_lrch_185_adjusted_r2_63d_d3": {"inputs": ["close"], "func": f18_lrch_185_adjusted_r2_63d_d3},
    "f18_lrch_186_aic_slope_model_63d_d3": {"inputs": ["close"], "func": f18_lrch_186_aic_slope_model_63d_d3},
    "f18_lrch_187_f_stat_overall_model_63d_d3": {"inputs": ["close"], "func": f18_lrch_187_f_stat_overall_model_63d_d3},
    "f18_lrch_188_prediction_interval_width_endpoint_63d_d3": {"inputs": ["close"], "func": f18_lrch_188_prediction_interval_width_endpoint_63d_d3},
    "f18_lrch_189_pi_to_ci_width_ratio_63d_d3": {"inputs": ["close"], "func": f18_lrch_189_pi_to_ci_width_ratio_63d_d3},
    "f18_lrch_190_working_hotelling_band_factor_252d_d3": {"inputs": ["close"], "func": f18_lrch_190_working_hotelling_band_factor_252d_d3},
    "f18_lrch_191_residual_sigma_expansion_21d_63d_d3": {"inputs": ["close"], "func": f18_lrch_191_residual_sigma_expansion_21d_63d_d3},
    "f18_lrch_192_studentized_residual_endpoint_63d_d3": {"inputs": ["close"], "func": f18_lrch_192_studentized_residual_endpoint_63d_d3},
    "f18_lrch_193_externally_studentized_resid_max_252d_d3": {"inputs": ["close"], "func": f18_lrch_193_externally_studentized_resid_max_252d_d3},
    "f18_lrch_194_cooks_distance_endpoint_63d_d3": {"inputs": ["close"], "func": f18_lrch_194_cooks_distance_endpoint_63d_d3},
    "f18_lrch_195_max_cooks_distance_252d_d3": {"inputs": ["close"], "func": f18_lrch_195_max_cooks_distance_252d_d3},
    "f18_lrch_196_hat_leverage_endpoint_63d_d3": {"inputs": ["close"], "func": f18_lrch_196_hat_leverage_endpoint_63d_d3},
    "f18_lrch_197_r2_lag_lead_diff_21d_vs_t_minus_21_d3": {"inputs": ["close"], "func": f18_lrch_197_r2_lag_lead_diff_21d_vs_t_minus_21_d3},
    "f18_lrch_198_r2_decay_recent_3_subwindows_63d_d3": {"inputs": ["close"], "func": f18_lrch_198_r2_decay_recent_3_subwindows_63d_d3},
    "f18_lrch_199_half_sample_slope_diff_126d_d3": {"inputs": ["close"], "func": f18_lrch_199_half_sample_slope_diff_126d_d3},
    "f18_lrch_200_chow_f_statistic_126d_split_d3": {"inputs": ["close"], "func": f18_lrch_200_chow_f_statistic_126d_split_d3},
    "f18_lrch_201_multi_horizon_r2_variance_3h_d3": {"inputs": ["close"], "func": f18_lrch_201_multi_horizon_r2_variance_3h_d3},
    "f18_lrch_202_slope_angle_degrees_63d_d3": {"inputs": ["close"], "func": f18_lrch_202_slope_angle_degrees_63d_d3},
    "f18_lrch_203_slope_angle_degrees_252d_d3": {"inputs": ["close"], "func": f18_lrch_203_slope_angle_degrees_252d_d3},
    "f18_lrch_204_bayesian_posterior_slope_mean_63d_d3": {"inputs": ["close"], "func": f18_lrch_204_bayesian_posterior_slope_mean_63d_d3},
    "f18_lrch_205_bayesian_posterior_slope_sd_63d_d3": {"inputs": ["close"], "func": f18_lrch_205_bayesian_posterior_slope_sd_63d_d3},
    "f18_lrch_206_slope_changepoint_midpoint_252d_d3": {"inputs": ["close"], "func": f18_lrch_206_slope_changepoint_midpoint_252d_d3},
    "f18_lrch_207_channel_asymmetry_upper_vs_lower_dist_63d_d3": {"inputs": ["close"], "func": f18_lrch_207_channel_asymmetry_upper_vs_lower_dist_63d_d3},
    "f18_lrch_208_breach_count_1sigma_63d_d3": {"inputs": ["close"], "func": f18_lrch_208_breach_count_1sigma_63d_d3},
    "f18_lrch_209_mean_residual_sign_252d_d3": {"inputs": ["close"], "func": f18_lrch_209_mean_residual_sign_252d_d3},
    "f18_lrch_210_arch_lm_residuals_lag5_63d_d3": {"inputs": ["close"], "func": f18_lrch_210_arch_lm_residuals_lag5_63d_d3},
    "f18_lrch_211_breusch_pagan_het_test_63d_d3": {"inputs": ["close"], "func": f18_lrch_211_breusch_pagan_het_test_63d_d3},
    "f18_lrch_212_breusch_godfrey_lm_lag2_63d_d3": {"inputs": ["close"], "func": f18_lrch_212_breusch_godfrey_lm_lag2_63d_d3},
    "f18_lrch_213_gls_cochrane_orcutt_slope_252d_d3": {"inputs": ["close"], "func": f18_lrch_213_gls_cochrane_orcutt_slope_252d_d3},
    "f18_lrch_214_hampel_residual_sigma_63d_d3": {"inputs": ["close"], "func": f18_lrch_214_hampel_residual_sigma_63d_d3},
    "f18_lrch_215_multi_window_slope_ensemble_mean_d3": {"inputs": ["close"], "func": f18_lrch_215_multi_window_slope_ensemble_mean_d3},
    "f18_lrch_216_multi_window_slope_ensemble_disp_d3": {"inputs": ["close"], "func": f18_lrch_216_multi_window_slope_ensemble_disp_d3},
    "f18_lrch_217_slope_zero_cross_hysteresis_252d_d3": {"inputs": ["close"], "func": f18_lrch_217_slope_zero_cross_hysteresis_252d_d3},
    "f18_lrch_218_stale_trend_indicator_63d_d3": {"inputs": ["close"], "func": f18_lrch_218_stale_trend_indicator_63d_d3},
    "f18_lrch_219_recursive_slope_drift_252d_d3": {"inputs": ["close"], "func": f18_lrch_219_recursive_slope_drift_252d_d3},
    "f18_lrch_220_residual_acf_lag1_63d_d3": {"inputs": ["close"], "func": f18_lrch_220_residual_acf_lag1_63d_d3},
    "f18_lrch_221_residual_acf_lag5_63d_d3": {"inputs": ["close"], "func": f18_lrch_221_residual_acf_lag5_63d_d3},
    "f18_lrch_222_resid_var_ratio_late_vs_early_126d_d3": {"inputs": ["close"], "func": f18_lrch_222_resid_var_ratio_late_vs_early_126d_d3},
    "f18_lrch_223_terminal_channel_robust_composite_63d_d3": {"inputs": ["close"], "func": f18_lrch_223_terminal_channel_robust_composite_63d_d3},
    "f18_lrch_224_curvature_sign_flip_count_252d_63d_d3": {"inputs": ["close"], "func": f18_lrch_224_curvature_sign_flip_count_252d_63d_d3},
    "f18_lrch_225_kalman_slope_sign_change_event_63d_d3": {"inputs": ["close"], "func": f18_lrch_225_kalman_slope_sign_change_event_63d_d3},
}
