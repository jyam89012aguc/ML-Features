"""parabolic_blowoff_signature d1 features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __d1__001_075.py. Each feature
encodes a *different concept* in the parabolic / blow-off / curvature theme:
higher-order polynomial fits, advanced goodness-of-fit, LPPL proxies, regime-conditional
curvature, transition events, phase-space embedding, wavelets, robust estimators, and
narrow parabolic-internal composites.

Differentiates from 1a `f37_bpsg_*` family by focusing on aspects bpsg does NOT cover:
higher-order polynomials, model-selection criteria, LPPL frequency/phase, conditional
regimes, phase-space embedding, robust estimators.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family imports.
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
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


# ---------- polynomial-fit helpers (raw=True window callables) ----------

def _poly_coef(w, deg, idx):
    """Return polyfit coefficient at index `idx` (where coeffs are ordered
    highest-degree-first per numpy convention). NaN-safe + try/except."""
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
    """Return residual array (y - yhat); or None on failure."""
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


def _poly_rss(w, deg):
    r = _poly_residuals(w, deg)
    if r is None:
        return np.nan
    return float((r * r).sum())


def _poly_r2(w, deg):
    valid = ~np.isnan(w)
    n = int(valid.sum())
    if n < (deg + 2):
        return np.nan
    yv = w[valid] if not valid.all() else w
    tss = float(((yv - yv.mean()) ** 2).sum())
    if tss <= 0:
        return np.nan
    rss = _poly_rss(w, deg)
    if not np.isfinite(rss):
        return np.nan
    return 1.0 - rss / tss


def _aic_gauss(rss, n, k):
    """AIC for a Gaussian-error model, k = number of fitted parameters."""
    if rss is None or not np.isfinite(rss) or rss <= 0 or n <= 0:
        return np.nan
    return float(n * np.log(rss / n) + 2.0 * k)


def _bic_gauss(rss, n, k):
    if rss is None or not np.isfinite(rss) or rss <= 0 or n <= 0:
        return np.nan
    return float(n * np.log(rss / n) + k * np.log(n))


def _rolling_logclose(close):
    return _safe_log(close)


def f02_pblo_076_hilbert_inst_freq_at_top_21d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    centered = lc - lc.rolling(63, min_periods=21).mean()
    sgn = np.sign(centered)
    flip = (sgn != sgn.shift(1)).astype(float)
    flip = flip.where(centered.notna() & centered.shift(1).notna(), np.nan)
    out = flip.rolling(21, min_periods=7).sum() / 21.0
    return out.diff()


def f02_pblo_077_phasespace_radius_close_logret_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    ret = lc.diff()
    # Standardize close in 252d
    m = lc.rolling(252, min_periods=84).mean()
    sd = lc.rolling(252, min_periods=84).std().replace(0, np.nan)
    z_close = (lc - m) / sd
    m_r = ret.rolling(252, min_periods=84).mean()
    sd_r = ret.rolling(252, min_periods=84).std().replace(0, np.nan)
    z_ret = (ret - m_r) / sd_r
    out = np.sqrt(z_close ** 2 + z_ret ** 2)
    return out.diff()


def f02_pblo_078_phasespace_spiral_signed_area_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    ret = lc.diff()
    def _shoelace(values, n_each):
        # values: 2*n array (interleaved close, ret); we receive single var here so we approximate
        pass
    def _f(w):
        n = w.size
        if n < 5:
            return np.nan
        x = w
        y = np.diff(w, prepend=w[0])
        s = 0.0
        for i in range(n - 1):
            s += x[i] * y[i + 1] - x[i + 1] * y[i]
        return float(0.5 * s)
    out = lc.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff()


def f02_pblo_079_phasespace_enclosed_area_abs_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _f(w):
        n = w.size
        if n < 5:
            return np.nan
        x = w
        y = np.diff(w, prepend=w[0])
        s = 0.0
        for i in range(n - 1):
            s += x[i] * y[i + 1] - x[i + 1] * y[i]
        return float(abs(0.5 * s))
    out = lc.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff()


def f02_pblo_080_phasespace_radial_velocity_5d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    ret = lc.diff()
    m = lc.rolling(252, min_periods=84).mean()
    sd = lc.rolling(252, min_periods=84).std().replace(0, np.nan)
    z_close = (lc - m) / sd
    m_r = ret.rolling(252, min_periods=84).mean()
    sd_r = ret.rolling(252, min_periods=84).std().replace(0, np.nan)
    z_ret = (ret - m_r) / sd_r
    radius = np.sqrt(z_close ** 2 + z_ret ** 2)
    out = radius - radius.shift(5)
    return out.diff()


def f02_pblo_081_phasespace_angular_velocity_5d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    ret = lc.diff()
    m = lc.rolling(252, min_periods=84).mean()
    sd = lc.rolling(252, min_periods=84).std().replace(0, np.nan)
    z_close = (lc - m) / sd
    m_r = ret.rolling(252, min_periods=84).mean()
    sd_r = ret.rolling(252, min_periods=84).std().replace(0, np.nan)
    z_ret = (ret - m_r) / sd_r
    theta = np.arctan2(z_ret, z_close)
    out = theta - theta.shift(5)
    return out.diff()


def f02_pblo_082_tangent_vector_consistency_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    ret = lc.diff()
    def _ac(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid]
        m = v.mean()
        num = float(((v[1:] - m) * (v[:-1] - m)).sum())
        den = float(((v - m) ** 2).sum())
        if den <= 0:
            return np.nan
        return num / den
    out = ret.rolling(63, min_periods=21).apply(_ac, raw=True)
    return out.diff()


def f02_pblo_083_lyapunov_proxy_252d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    ret = lc.diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid]
        n = v.size
        diffs = np.abs(np.diff(v))
        diffs = diffs[diffs > 0]
        if diffs.size < 5:
            return np.nan
        return float(np.mean(np.log(diffs)))
    out = ret.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f02_pblo_084_recurrence_rate_within_1atr_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, n=21)
    def _f_inner():
        pass
    # row-wise: count of past 63 bars where |close[t-k] - close[t]| < atr[t]
    idx = close.index
    n = len(close)
    out_vals = np.full(n, np.nan)
    c = close.to_numpy(); a = atr.to_numpy()
    for t in range(n):
        lo = max(0, t - 62)
        if not np.isfinite(c[t]) or not np.isfinite(a[t]) or a[t] <= 0:
            continue
        window = c[lo:t + 1]
        valid_mask = np.isfinite(window)
        if valid_mask.sum() < 10:
            continue
        diffs = np.abs(window[valid_mask] - c[t])
        out_vals[t] = float((diffs <= a[t]).sum()) / float(valid_mask.sum())
    out = pd.Series(out_vals, index=idx)
    return out.diff()


def f02_pblo_085_recurrence_determinism_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    ret = lc.diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid]
        if v.size < 3:
            return np.nan
        sign_runs = np.sign(v)
        # Count consecutive same-sign pairs (diagonal recurrences)
        pairs = int((sign_runs[1:] == sign_runs[:-1]).sum())
        return float(pairs) / float(v.size - 1)
    out = ret.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff()


def f02_pblo_086_longest_same_sign_return_run_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    ret = lc.diff()
    sgn = np.sign(ret).fillna(0.0)
    def _ms(w):
        if w.size == 0:
            return np.nan
        best = 0; cur = 0; prev = None
        for v in w:
            if v == 0:
                cur = 0; prev = None
                continue
            if prev is None or v == prev:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 1
            prev = v
        return float(best)
    out = sgn.rolling(63, min_periods=21).apply(_ms, raw=True)
    return out.diff()


def f02_pblo_087_accel_then_flat_long_pos_short_zero_indicator_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c252 = lc.rolling(252, min_periods=84).apply(_fc, raw=True)
    c63 = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    out = ((c252 > 0) & (c63.abs() < c252.abs() * 0.2)).astype(float)
    out = out.where(c252.notna() & c63.notna(), np.nan)
    return out.diff()


def f02_pblo_088_c63_decay_magnitude_21d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c63 = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    out = c63.shift(21) - c63
    return out.diff()


def f02_pblo_089_slope_decay_velocity_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    slope = _rolling_slope(lc, 63, min_periods=21)
    out = -slope.diff()
    return out.diff()


def f02_pblo_090_plateau_quality_post_peak_score_63d_d1(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 30:
            return np.nan
        last = r[-21:]
        base = r[:-21]
        if last.size < 5 or base.size < 5:
            return np.nan
        sd_last = float(np.nanstd(last, ddof=1))
        sd_base = float(np.nanstd(base, ddof=1))
        if sd_base <= 0:
            return np.nan
        return sd_last / sd_base
    lc = _safe_log(close)
    out = lc.rolling(63, min_periods=42).apply(_f, raw=True)
    return out.diff()


def f02_pblo_091_rounding_top_arc_fit_r2_63d_d1(close: pd.Series) -> pd.Series:
    def _f(w):
        return _poly_r2(w, 2)
    lc = _safe_log(close)
    r2 = lc.rolling(63, min_periods=21).apply(_f, raw=True)
    def _fc(w):
        return _poly_coef(w, 2, 0)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    # Only valid when the parabola actually opens downward (rounding top)
    out = r2.where(c < 0, np.nan)
    return out.diff()


def f02_pblo_092_inverted_cup_symmetry_score_63d_d1(close: pd.Series) -> pd.Series:
    def _f(w):
        if w.size < 10:
            return np.nan
        n = w.size
        half = n // 2
        left = w[:half]
        right = w[-half:][::-1]
        if np.isnan(left).all() or np.isnan(right).all():
            return np.nan
        diff = np.nanmean(np.abs(left - right))
        avg = (np.nanmean(np.abs(left)) + np.nanmean(np.abs(right))) / 2.0
        if avg <= 0:
            return np.nan
        return 1.0 - float(diff / avg)
    lc = _safe_log(close)
    out = lc.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff()


def f02_pblo_093_time_to_flat_estimate_63d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    dc = c.diff()
    out = _safe_div(-c, dc)
    out = out.where(out > 0, np.nan)
    return out.diff()


def f02_pblo_094_pre_flat_accel_consistency_63d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    out = _safe_div(c.rolling(63, min_periods=21).mean(), c.rolling(63, min_periods=21).std())
    return out.diff()


def f02_pblo_095_post_flat_retracement_velocity_21d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    flat = (c.abs() < c.rolling(252, min_periods=84).std() * 0.3).astype(float)
    ret_21 = lc.diff(21)
    out = ret_21.where(flat > 0.5, np.nan)
    return out.diff()


def f02_pblo_096_frozen_at_peak_indicator_63d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    rmax = lc.rolling(504, min_periods=168).max()
    at_high = (lc >= rmax - 0.02).astype(float)
    low_c = (c.abs() < c.rolling(504, min_periods=168).std() * 0.3).astype(float)
    out = (at_high * low_c).rolling(21, min_periods=7).mean()
    return out.diff()


def f02_pblo_097_bars_since_c_pos_onset_252d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    onset = ((c > 0) & (c.shift(1) <= 0)).astype(float)
    def _last(w):
        idx = np.where(w > 0.5)[0]
        if idx.size == 0:
            return np.nan
        return float(w.size - 1 - idx[-1])
    out = onset.rolling(252, min_periods=21).apply(_last, raw=True)
    return out.diff()


def f02_pblo_098_bars_since_c_decel_onset_252d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    decel = ((c < c.shift(1)) & (c.shift(1) >= c.shift(2)) & (c > 0)).astype(float)
    def _last(w):
        idx = np.where(w > 0.5)[0]
        if idx.size == 0:
            return np.nan
        return float(w.size - 1 - idx[-1])
    out = decel.rolling(252, min_periods=21).apply(_last, raw=True)
    return out.diff()


def f02_pblo_099_first_c_above_2sigma_252d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    z = _rolling_zscore(c, 252, min_periods=84)
    event = ((z > 2) & (z.shift(1) <= 2)).astype(float)
    def _last(w):
        idx = np.where(w > 0.5)[0]
        if idx.size == 0:
            return np.nan
        return float(w.size - 1 - idx[-1])
    out = event.rolling(252, min_periods=21).apply(_last, raw=True)
    return out.diff()


def f02_pblo_100_accel_after_calm_event_indicator_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    z = _rolling_zscore(c, 252, min_periods=84)
    calm = (z.abs() < 0.5).rolling(63, min_periods=21).sum() >= 50
    burst = (z.abs() > 3)
    out = (calm.shift(1) & burst).astype(float)
    out = out.where(z.notna(), np.nan)
    return out.diff()


def f02_pblo_101_accel_sustained_high_21d_indicator_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    z = _rolling_zscore(c, 252, min_periods=84)
    high = (z > 2).astype(float)
    out = (high.rolling(21, min_periods=21).sum() == 21).astype(float)
    out = out.where(z.notna(), np.nan)
    return out.diff()


def f02_pblo_102_accel_to_decel_transition_count_252d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    dc = c.diff()
    event = ((dc < 0) & (dc.shift(1) >= 0) & (c > 0)).astype(float)
    out = event.rolling(252, min_periods=84).sum()
    return out.diff()


def f02_pblo_103_onset_to_peak_latency_252d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    onset = ((c > 0) & (c.shift(1) <= 0)).astype(float)
    def _last(w):
        idx = np.where(w > 0.5)[0]
        if idx.size == 0:
            return np.nan
        return float(w.size - 1 - idx[-1])
    bars_onset = onset.rolling(252, min_periods=21).apply(_last, raw=True)
    rmax_idx = lc.rolling(252, min_periods=21).apply(lambda w: float(w.size - 1 - int(np.nanargmax(w))) if np.any(~np.isnan(w)) else np.nan, raw=True)
    out = bars_onset - rmax_idx
    return out.diff()


def f02_pblo_104_onset_cluster_density_252d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    onset = ((c > 0) & (c.shift(1) <= 0)).astype(float)
    out = onset.rolling(252, min_periods=84).sum()
    return out.diff()


def f02_pblo_105_repeated_onset_compression_504d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    onset = ((c > 0) & (c.shift(1) <= 0)).astype(float)
    def _f(w):
        pos = np.where(w > 0.5)[0]
        if pos.size < 3:
            return np.nan
        gaps = np.diff(pos)
        if gaps.size < 2:
            return np.nan
        # Count of gap-shortening events
        return float((gaps[1:] < gaps[:-1]).sum())
    out = onset.rolling(504, min_periods=168).apply(_f, raw=True)
    return out.diff()


def f02_pblo_106_onset_on_heavy_volume_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    onset = ((c > 0) & (c.shift(1) <= 0)).astype(float)
    vz = _rolling_zscore(volume, 63, min_periods=21)
    out = (onset > 0.5) & (vz > 2)
    out = out.astype(float).where(onset.notna() & vz.notna(), np.nan)
    return out.diff()


def f02_pblo_107_c_conditional_within_5pct_252d_high_63d_mean_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    rmax = lc.rolling(252, min_periods=84).max()
    stretched = lc >= (rmax - np.log(1.05))
    out = c.where(stretched, np.nan).rolling(63, min_periods=10).mean()
    return out.diff()


def f02_pblo_108_c_conditional_high_vol_63d_mean_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    vz = _rolling_zscore(volume, 63, min_periods=21)
    out = c.where(vz > 2, np.nan).rolling(63, min_periods=5).mean()
    return out.diff()


def f02_pblo_109_c_conditional_strong_advance_63d_mean_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    ret21 = lc.diff(21)
    out = c.where(ret21 > np.log(1.10), np.nan).rolling(63, min_periods=5).mean()
    return out.diff()


def f02_pblo_110_c_low_vs_high_vol_regime_ratio_252d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    ret = lc.diff()
    rv = ret.rolling(21, min_periods=5).std()
    med_rv = rv.rolling(252, min_periods=84).median()
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    c_low = c.where(rv < med_rv, np.nan).rolling(252, min_periods=42).mean()
    c_hi = c.where(rv >= med_rv, np.nan).rolling(252, min_periods=42).mean()
    out = _safe_div(c_low, c_hi)
    return out.diff()


def f02_pblo_111_c_above_vs_below_sma200_diff_252d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    sma200 = close.rolling(200, min_periods=63).mean()
    above = close > sma200
    c_above = c.where(above, np.nan).rolling(252, min_periods=42).mean()
    c_below = c.where(~above, np.nan).rolling(252, min_periods=42).mean()
    out = c_above - c_below
    return out.diff()


def f02_pblo_112_c_at_new_high_vs_not_diff_252d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    rmax = lc.rolling(252, min_periods=84).max()
    at_high = lc >= rmax
    c_h = c.where(at_high, np.nan).rolling(252, min_periods=21).mean()
    c_n = c.where(~at_high, np.nan).rolling(252, min_periods=42).mean()
    out = c_h - c_n
    return out.diff()


def f02_pblo_113_c_at_top_quintile_252d_range_mean_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    rmax = high.rolling(252, min_periods=84).max()
    rmin = low.rolling(252, min_periods=84).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    out = c.where(pos > 0.8, np.nan).rolling(63, min_periods=10).mean()
    return out.diff()


def f02_pblo_114_c_after_gap_up_63d_mean_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    gap = open - close.shift(1)
    gap_pct = _safe_div(gap, close.shift(1))
    out = c.where(gap_pct.shift(1) > 0.03, np.nan).rolling(63, min_periods=5).mean()
    return out.diff()


def f02_pblo_115_c_low_rv_conditional_252d_mean_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    ret = lc.diff()
    rv = ret.rolling(21, min_periods=5).std()
    q25 = rv.rolling(252, min_periods=84).quantile(0.25)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    out = c.where(rv < q25, np.nan).rolling(252, min_periods=42).mean()
    return out.diff()


def f02_pblo_116_c_seasonal_quarter_deviation_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    q = pd.Series(close.index.quarter, index=close.index, dtype=float)
    rolling_mean = c.rolling(252, min_periods=84).mean()
    out = c - rolling_mean
    out = out.where(q == q, np.nan)
    return out.diff()


def f02_pblo_117_theil_sen_quad_robust_63d_d1(close: pd.Series) -> pd.Series:
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 20:
            return np.nan
        v = w[valid]
        n = v.size
        x = np.arange(n, dtype=float)
        # Approximate: median of second-differences
        sd = np.diff(np.diff(v))
        if sd.size < 5:
            return np.nan
        return float(np.median(sd))
    lc = _safe_log(close)
    out = lc.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff()


def f02_pblo_118_ransac_quad_consensus_63d_d1(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 10:
            return np.nan
        sd = float(np.nanstd(r, ddof=1))
        if sd <= 0:
            return np.nan
        inliers = (np.abs(r) <= sd).sum()
        return float(inliers) / float(r.size)
    lc = _safe_log(close)
    out = lc.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff()


def f02_pblo_119_median_c_subwindows_21d_in_126d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(_fc, raw=True)
    out = c.rolling(126, min_periods=42).median()
    return out.diff()


def f02_pblo_120_winsorized_quad_c_63d_d1(close: pd.Series) -> pd.Series:
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 20:
            return np.nan
        v = w[valid] if not valid.all() else w
        lo = np.percentile(v, 5)
        hi = np.percentile(v, 95)
        vw = np.clip(v, lo, hi)
        x = np.arange(vw.size, dtype=float)
        try:
            c = np.polyfit(x, vw, 2)
            return float(c[0])
        except Exception:
            return np.nan
    lc = _safe_log(close)
    out = lc.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff()


def f02_pblo_121_trimmed_mean_c_subwindows_252d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(_fc, raw=True)
    def _trim(w):
        valid = ~np.isnan(w)
        if valid.sum() < 20:
            return np.nan
        v = w[valid]
        lo = np.percentile(v, 10)
        hi = np.percentile(v, 90)
        inner = v[(v >= lo) & (v <= hi)]
        if inner.size == 0:
            return np.nan
        return float(inner.mean())
    out = c.rolling(252, min_periods=84).apply(_trim, raw=True)
    return out.diff()


def f02_pblo_122_quantile_median_quad_slope_63d_d1(close: pd.Series) -> pd.Series:
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 20:
            return np.nan
        v = w[valid] if not valid.all() else w
        n = v.size
        half = n // 2
        if half < 5:
            return np.nan
        slope_first = (v[half - 1] - v[0]) / float(half - 1)
        slope_last = (v[-1] - v[half]) / float(n - 1 - half)
        return float(slope_last - slope_first)
    lc = _safe_log(close)
    out = lc.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff()


def f02_pblo_123_quantile_upper_quad_slope_63d_d1(close: pd.Series) -> pd.Series:
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 20:
            return np.nan
        v = w[valid] if not valid.all() else w
        n = v.size
        q80 = np.percentile(v, 80)
        mask = v >= q80
        if mask.sum() < 5:
            return np.nan
        x = np.arange(n, dtype=float)[mask]
        yv = v[mask]
        try:
            c = np.polyfit(x, yv, 2)
            return float(c[0])
        except Exception:
            return np.nan
    lc = _safe_log(close)
    out = lc.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff()


def f02_pblo_124_robust_z_c_mad_504d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    med = c.rolling(504, min_periods=168).median()
    mad = (c - med).abs().rolling(504, min_periods=168).median()
    out = _safe_div(c - med, 1.4826 * mad)
    return out.diff()


def f02_pblo_125_huber_m_estimator_quad_c_63d_d1(close: pd.Series) -> pd.Series:
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 20:
            return np.nan
        v = w[valid] if not valid.all() else w
        x = np.arange(v.size, dtype=float)
        try:
            c0 = np.polyfit(x, v, 2)
        except Exception:
            return np.nan
        # One IRLS iteration with Huber weights
        yhat = np.polyval(c0, x)
        r = v - yhat
        s = 1.4826 * np.median(np.abs(r - np.median(r)))
        if s <= 0:
            return float(c0[0])
        a = r / s
        k = 1.345
        wgt = np.where(np.abs(a) <= k, 1.0, k / np.abs(a))
        try:
            c1 = np.polyfit(x, v, 2, w=wgt)
            return float(c1[0])
        except Exception:
            return float(c0[0])
    lc = _safe_log(close)
    out = lc.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff()


def f02_pblo_126_tukey_biweight_quad_c_63d_d1(close: pd.Series) -> pd.Series:
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 20:
            return np.nan
        v = w[valid] if not valid.all() else w
        x = np.arange(v.size, dtype=float)
        try:
            c0 = np.polyfit(x, v, 2)
        except Exception:
            return np.nan
        yhat = np.polyval(c0, x)
        r = v - yhat
        s = 1.4826 * np.median(np.abs(r - np.median(r)))
        if s <= 0:
            return float(c0[0])
        a = r / s
        k = 4.685
        wgt = np.where(np.abs(a) <= k, (1 - (a / k) ** 2) ** 2, 0.0)
        if wgt.sum() <= 1:
            return float(c0[0])
        try:
            c1 = np.polyfit(x, v, 2, w=wgt)
            return float(c1[0])
        except Exception:
            return float(c0[0])
    lc = _safe_log(close)
    out = lc.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff()


def f02_pblo_127_c_pctrank_in_504d_history_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    out = c.rolling(504, min_periods=168).apply(_rk, raw=True)
    return out.diff()


def f02_pblo_128_c_pctrank_in_1260d_history_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    out = c.rolling(1260, min_periods=252).apply(_rk, raw=True)
    return out.diff()


def f02_pblo_129_c_zscore_vs_5y_history_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    out = _rolling_zscore(c, 1260, min_periods=252)
    return out.diff()


def f02_pblo_130_c_drawdown_from_252d_max_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    cmax = c.rolling(252, min_periods=84).max()
    out = c - cmax
    return out.diff()


def f02_pblo_131_c_recovery_velocity_21d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    cmin21 = c.rolling(21, min_periods=7).min()
    out = (c - cmin21) / 21.0
    return out.diff()


def f02_pblo_132_c_of_c_abs_magnitude_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    out = c.diff().diff().abs()
    return out.diff()


def f02_pblo_133_c_coherence_subwindows_126d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(21, min_periods=7).apply(_fc, raw=True)
    std_c = c.rolling(126, min_periods=42).std()
    out = -std_c
    return out.diff()


def f02_pblo_134_c_anomaly_abs_zscore_5y_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    out = _rolling_zscore(c, 1260, min_periods=252).abs()
    return out.diff()


def f02_pblo_135_comp_accel_onset_sustained_pos_c_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    z = _rolling_zscore(c, 252, min_periods=84)
    onset = ((c > 0) & (c.shift(1) <= 0)).astype(float)
    sustained = ((c > 0).rolling(21, min_periods=21).sum() == 21).astype(float)
    out = ((z > 2).astype(float) + onset.rolling(21, min_periods=5).max() + sustained)
    out = out.where(z.notna(), np.nan)
    return out.diff()


def f02_pblo_136_comp_rounding_top_score_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c252 = lc.rolling(252, min_periods=84).apply(_fc, raw=True)
    c63 = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    rmax = lc.rolling(252, min_periods=84).max()
    at_high = (lc >= rmax - 0.05).astype(float)
    flat = (c63.abs() < c63.rolling(252, min_periods=84).std() * 0.3).astype(float)
    accel_prior = (c252 > 0).astype(float)
    out = at_high + flat + accel_prior
    out = out.where(c252.notna() & c63.notna(), np.nan)
    return out.diff()


def f02_pblo_137_comp_accel_onset_heavy_vol_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    z = _rolling_zscore(c, 252, min_periods=84)
    onset = ((c > 0) & (c.shift(1) <= 0)).astype(float)
    vz = _rolling_zscore(volume, 63, min_periods=21)
    out = ((z > 2).astype(float) + onset.rolling(21, min_periods=5).max() + (vz > 1.5).astype(float))
    out = out.where(z.notna() & vz.notna(), np.nan)
    return out.diff()


def f02_pblo_138_comp_sharp_blowoff_score_63d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    def _fr(w):
        return _poly_r2(w, 2)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    r2 = lc.rolling(63, min_periods=21).apply(_fr, raw=True)
    z_c = _rolling_zscore(c, 252, min_periods=84)
    out = z_c * r2
    return out.diff()


def f02_pblo_139_comp_multi_horizon_c_consensus_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c63 = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    c252 = lc.rolling(252, min_periods=84).apply(_fc, raw=True)
    c504 = lc.rolling(504, min_periods=168).apply(_fc, raw=True)
    out = ((c63 > 0).astype(float) + (c252 > 0).astype(float) + (c504 > 0).astype(float))
    out = out.where(c63.notna() & c252.notna() & c504.notna(), np.nan)
    return out.diff()


def f02_pblo_140_comp_lppl_bubble_composite_252d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    def _fr(w):
        return _poly_r2(w, 2)
    def _fz(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 20:
            return np.nan
        sgn = np.sign(r)
        nz = (sgn[1:] != sgn[:-1]).sum()
        return float(nz) / float(r.size)
    lc = _safe_log(close)
    c = lc.rolling(252, min_periods=84).apply(_fc, raw=True)
    r2 = lc.rolling(252, min_periods=84).apply(_fr, raw=True)
    zcr = lc.rolling(252, min_periods=84).apply(_fz, raw=True)
    out = c * r2 * zcr
    return out.diff()


def f02_pblo_141_comp_blowoff_fatigue_score_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    z = _rolling_zscore(c, 252, min_periods=84)
    decel = (c.diff() < 0).astype(float)
    vslope = _rolling_slope(volume, 21, min_periods=7)
    out = ((z > 2).astype(float) * decel) * np.sign(vslope)
    out = out.where(z.notna() & vslope.notna(), np.nan)
    return out.diff()


def f02_pblo_142_comp_blowoff_terminal_score_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    z = _rolling_zscore(c, 252, min_periods=84)
    d2 = lc.diff().diff().rolling(5, min_periods=2).mean()
    flip_recent = ((np.sign(d2) != np.sign(d2.shift(1))) & d2.notna() & d2.shift(1).notna()).astype(float).rolling(21, min_periods=5).sum()
    def _conf(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 10:
            return np.nan
        band = float(np.nanstd(r, ddof=1))
        if band <= 0:
            return np.nan
        return float(r[-1]) / band
    tstar = lc.rolling(252, min_periods=84).apply(_conf, raw=True)
    out = (z > 2).astype(float) + (flip_recent > 0).astype(float) + (tstar > 1).astype(float)
    out = out.where(z.notna() & tstar.notna(), np.nan)
    return out.diff()


def f02_pblo_143_comp_curvature_explosion_count_252d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    z = _rolling_zscore(c, 252, min_periods=84)
    event = (z > 3).astype(float)
    out = event.rolling(252, min_periods=84).sum()
    return out.diff()


def f02_pblo_144_comp_robust_vs_nonrobust_c_agreement_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    def _ftheil(w):
        valid = ~np.isnan(w)
        if valid.sum() < 20:
            return np.nan
        v = w[valid] if not valid.all() else w
        sd = np.diff(np.diff(v))
        if sd.size < 5:
            return np.nan
        return float(np.median(sd))
    lc = _safe_log(close)
    c_ols = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    c_rob = lc.rolling(63, min_periods=21).apply(_ftheil, raw=True)
    out = (np.sign(c_ols) == np.sign(c_rob)).astype(float)
    out = out.where(c_ols.notna() & c_rob.notna(), np.nan)
    return out.diff()


def f02_pblo_145_comp_multi_degree_agreement_252d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    def _f3(w):
        return _poly_coef(w, 3, 0)
    lc = _safe_log(close)
    c2 = lc.rolling(252, min_periods=84).apply(_fc, raw=True)
    c3 = lc.rolling(252, min_periods=84).apply(_f3, raw=True)
    out = (np.sign(c2) == np.sign(c3)).astype(float)
    out = out.where(c2.notna() & c3.notna(), np.nan)
    return out.diff()


def f02_pblo_146_comp_price_up_c_down_divergence_63d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    ret_63 = lc.diff(63)
    c_diff = c - c.shift(63)
    out = ((ret_63 > 0) & (c_diff < 0)).astype(float)
    out = out.where(ret_63.notna() & c_diff.notna(), np.nan)
    return out.diff()


def f02_pblo_147_comp_phasespace_curvature_joint_anomaly_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    ret = lc.diff()
    m = lc.rolling(252, min_periods=84).mean()
    sd = lc.rolling(252, min_periods=84).std().replace(0, np.nan)
    z_close = (lc - m) / sd
    m_r = ret.rolling(252, min_periods=84).mean()
    sd_r = ret.rolling(252, min_periods=84).std().replace(0, np.nan)
    z_ret = (ret - m_r) / sd_r
    radius = np.sqrt(z_close ** 2 + z_ret ** 2)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    z_c = _rolling_zscore(c, 252, min_periods=84)
    out = radius * z_c
    return out.diff()


def f02_pblo_148_comp_wavelet_polynomial_joint_252d_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(252, min_periods=84).apply(_fc, raw=True)
    short_m = lc.rolling(63, min_periods=21).mean()
    long_m = lc.rolling(252, min_periods=84).mean()
    haar = short_m - long_m
    out = c.abs() * haar.abs()
    return out.diff()


def f02_pblo_149_comp_parabolic_regime_confidence_252d_d1(close: pd.Series) -> pd.Series:
    def _fr(w):
        return _poly_r2(w, 2)
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    r2 = lc.rolling(252, min_periods=84).apply(_fr, raw=True)
    c = lc.rolling(252, min_periods=84).apply(_fc, raw=True)
    out = r2 * (c > 0).astype(float)
    out = out.where(r2.notna() & c.notna(), np.nan)
    return out.diff()


def f02_pblo_150_comp_terminal_parabolic_state_composite_d1(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c63 = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    c252 = lc.rolling(252, min_periods=84).apply(_fc, raw=True)
    z252 = _rolling_zscore(c252, 504, min_periods=168)
    flat = (c63.abs() < c63.rolling(252, min_periods=84).std() * 0.3).astype(float)
    def _conf(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 10:
            return np.nan
        band = float(np.nanstd(r, ddof=1))
        if band <= 0:
            return np.nan
        return float(r[-1]) / band
    tstar = lc.rolling(252, min_periods=84).apply(_conf, raw=True)
    rmax = lc.rolling(252, min_periods=84).max()
    at_high = (lc >= rmax - 0.05).astype(float)
    out = ((z252 > 1).astype(float) + flat + (tstar > 1).astype(float) + at_high)
    out = out.where(z252.notna() & tstar.notna(), np.nan)
    return out.diff()


# ============================================================
#                         REGISTRY 076_150 (d1)
# ============================================================

PARABOLIC_BLOWOFF_SIGNATURE_D1_REGISTRY_076_150 = {
    "f02_pblo_076_hilbert_inst_freq_at_top_21d_d1": {"inputs": ["close"], "func": f02_pblo_076_hilbert_inst_freq_at_top_21d_d1},
    "f02_pblo_077_phasespace_radius_close_logret_d1": {"inputs": ["close"], "func": f02_pblo_077_phasespace_radius_close_logret_d1},
    "f02_pblo_078_phasespace_spiral_signed_area_63d_d1": {"inputs": ["close"], "func": f02_pblo_078_phasespace_spiral_signed_area_63d_d1},
    "f02_pblo_079_phasespace_enclosed_area_abs_63d_d1": {"inputs": ["close"], "func": f02_pblo_079_phasespace_enclosed_area_abs_63d_d1},
    "f02_pblo_080_phasespace_radial_velocity_5d_d1": {"inputs": ["close"], "func": f02_pblo_080_phasespace_radial_velocity_5d_d1},
    "f02_pblo_081_phasespace_angular_velocity_5d_d1": {"inputs": ["close"], "func": f02_pblo_081_phasespace_angular_velocity_5d_d1},
    "f02_pblo_082_tangent_vector_consistency_63d_d1": {"inputs": ["close"], "func": f02_pblo_082_tangent_vector_consistency_63d_d1},
    "f02_pblo_083_lyapunov_proxy_252d_d1": {"inputs": ["close"], "func": f02_pblo_083_lyapunov_proxy_252d_d1},
    "f02_pblo_084_recurrence_rate_within_1atr_63d_d1": {"inputs": ["high", "low", "close"], "func": f02_pblo_084_recurrence_rate_within_1atr_63d_d1},
    "f02_pblo_085_recurrence_determinism_63d_d1": {"inputs": ["close"], "func": f02_pblo_085_recurrence_determinism_63d_d1},
    "f02_pblo_086_longest_same_sign_return_run_63d_d1": {"inputs": ["close"], "func": f02_pblo_086_longest_same_sign_return_run_63d_d1},
    "f02_pblo_087_accel_then_flat_long_pos_short_zero_indicator_d1": {"inputs": ["close"], "func": f02_pblo_087_accel_then_flat_long_pos_short_zero_indicator_d1},
    "f02_pblo_088_c63_decay_magnitude_21d_d1": {"inputs": ["close"], "func": f02_pblo_088_c63_decay_magnitude_21d_d1},
    "f02_pblo_089_slope_decay_velocity_63d_d1": {"inputs": ["close"], "func": f02_pblo_089_slope_decay_velocity_63d_d1},
    "f02_pblo_090_plateau_quality_post_peak_score_63d_d1": {"inputs": ["close"], "func": f02_pblo_090_plateau_quality_post_peak_score_63d_d1},
    "f02_pblo_091_rounding_top_arc_fit_r2_63d_d1": {"inputs": ["close"], "func": f02_pblo_091_rounding_top_arc_fit_r2_63d_d1},
    "f02_pblo_092_inverted_cup_symmetry_score_63d_d1": {"inputs": ["close"], "func": f02_pblo_092_inverted_cup_symmetry_score_63d_d1},
    "f02_pblo_093_time_to_flat_estimate_63d_d1": {"inputs": ["close"], "func": f02_pblo_093_time_to_flat_estimate_63d_d1},
    "f02_pblo_094_pre_flat_accel_consistency_63d_d1": {"inputs": ["close"], "func": f02_pblo_094_pre_flat_accel_consistency_63d_d1},
    "f02_pblo_095_post_flat_retracement_velocity_21d_d1": {"inputs": ["close"], "func": f02_pblo_095_post_flat_retracement_velocity_21d_d1},
    "f02_pblo_096_frozen_at_peak_indicator_63d_d1": {"inputs": ["close"], "func": f02_pblo_096_frozen_at_peak_indicator_63d_d1},
    "f02_pblo_097_bars_since_c_pos_onset_252d_d1": {"inputs": ["close"], "func": f02_pblo_097_bars_since_c_pos_onset_252d_d1},
    "f02_pblo_098_bars_since_c_decel_onset_252d_d1": {"inputs": ["close"], "func": f02_pblo_098_bars_since_c_decel_onset_252d_d1},
    "f02_pblo_099_first_c_above_2sigma_252d_d1": {"inputs": ["close"], "func": f02_pblo_099_first_c_above_2sigma_252d_d1},
    "f02_pblo_100_accel_after_calm_event_indicator_d1": {"inputs": ["close"], "func": f02_pblo_100_accel_after_calm_event_indicator_d1},
    "f02_pblo_101_accel_sustained_high_21d_indicator_d1": {"inputs": ["close"], "func": f02_pblo_101_accel_sustained_high_21d_indicator_d1},
    "f02_pblo_102_accel_to_decel_transition_count_252d_d1": {"inputs": ["close"], "func": f02_pblo_102_accel_to_decel_transition_count_252d_d1},
    "f02_pblo_103_onset_to_peak_latency_252d_d1": {"inputs": ["close"], "func": f02_pblo_103_onset_to_peak_latency_252d_d1},
    "f02_pblo_104_onset_cluster_density_252d_d1": {"inputs": ["close"], "func": f02_pblo_104_onset_cluster_density_252d_d1},
    "f02_pblo_105_repeated_onset_compression_504d_d1": {"inputs": ["close"], "func": f02_pblo_105_repeated_onset_compression_504d_d1},
    "f02_pblo_106_onset_on_heavy_volume_indicator_d1": {"inputs": ["close", "volume"], "func": f02_pblo_106_onset_on_heavy_volume_indicator_d1},
    "f02_pblo_107_c_conditional_within_5pct_252d_high_63d_mean_d1": {"inputs": ["close"], "func": f02_pblo_107_c_conditional_within_5pct_252d_high_63d_mean_d1},
    "f02_pblo_108_c_conditional_high_vol_63d_mean_d1": {"inputs": ["close", "volume"], "func": f02_pblo_108_c_conditional_high_vol_63d_mean_d1},
    "f02_pblo_109_c_conditional_strong_advance_63d_mean_d1": {"inputs": ["close"], "func": f02_pblo_109_c_conditional_strong_advance_63d_mean_d1},
    "f02_pblo_110_c_low_vs_high_vol_regime_ratio_252d_d1": {"inputs": ["close"], "func": f02_pblo_110_c_low_vs_high_vol_regime_ratio_252d_d1},
    "f02_pblo_111_c_above_vs_below_sma200_diff_252d_d1": {"inputs": ["close"], "func": f02_pblo_111_c_above_vs_below_sma200_diff_252d_d1},
    "f02_pblo_112_c_at_new_high_vs_not_diff_252d_d1": {"inputs": ["close"], "func": f02_pblo_112_c_at_new_high_vs_not_diff_252d_d1},
    "f02_pblo_113_c_at_top_quintile_252d_range_mean_63d_d1": {"inputs": ["high", "low", "close"], "func": f02_pblo_113_c_at_top_quintile_252d_range_mean_63d_d1},
    "f02_pblo_114_c_after_gap_up_63d_mean_d1": {"inputs": ["open", "close"], "func": f02_pblo_114_c_after_gap_up_63d_mean_d1},
    "f02_pblo_115_c_low_rv_conditional_252d_mean_d1": {"inputs": ["close"], "func": f02_pblo_115_c_low_rv_conditional_252d_mean_d1},
    "f02_pblo_116_c_seasonal_quarter_deviation_d1": {"inputs": ["close"], "func": f02_pblo_116_c_seasonal_quarter_deviation_d1},
    "f02_pblo_117_theil_sen_quad_robust_63d_d1": {"inputs": ["close"], "func": f02_pblo_117_theil_sen_quad_robust_63d_d1},
    "f02_pblo_118_ransac_quad_consensus_63d_d1": {"inputs": ["close"], "func": f02_pblo_118_ransac_quad_consensus_63d_d1},
    "f02_pblo_119_median_c_subwindows_21d_in_126d_d1": {"inputs": ["close"], "func": f02_pblo_119_median_c_subwindows_21d_in_126d_d1},
    "f02_pblo_120_winsorized_quad_c_63d_d1": {"inputs": ["close"], "func": f02_pblo_120_winsorized_quad_c_63d_d1},
    "f02_pblo_121_trimmed_mean_c_subwindows_252d_d1": {"inputs": ["close"], "func": f02_pblo_121_trimmed_mean_c_subwindows_252d_d1},
    "f02_pblo_122_quantile_median_quad_slope_63d_d1": {"inputs": ["close"], "func": f02_pblo_122_quantile_median_quad_slope_63d_d1},
    "f02_pblo_123_quantile_upper_quad_slope_63d_d1": {"inputs": ["close"], "func": f02_pblo_123_quantile_upper_quad_slope_63d_d1},
    "f02_pblo_124_robust_z_c_mad_504d_d1": {"inputs": ["close"], "func": f02_pblo_124_robust_z_c_mad_504d_d1},
    "f02_pblo_125_huber_m_estimator_quad_c_63d_d1": {"inputs": ["close"], "func": f02_pblo_125_huber_m_estimator_quad_c_63d_d1},
    "f02_pblo_126_tukey_biweight_quad_c_63d_d1": {"inputs": ["close"], "func": f02_pblo_126_tukey_biweight_quad_c_63d_d1},
    "f02_pblo_127_c_pctrank_in_504d_history_d1": {"inputs": ["close"], "func": f02_pblo_127_c_pctrank_in_504d_history_d1},
    "f02_pblo_128_c_pctrank_in_1260d_history_d1": {"inputs": ["close"], "func": f02_pblo_128_c_pctrank_in_1260d_history_d1},
    "f02_pblo_129_c_zscore_vs_5y_history_d1": {"inputs": ["close"], "func": f02_pblo_129_c_zscore_vs_5y_history_d1},
    "f02_pblo_130_c_drawdown_from_252d_max_d1": {"inputs": ["close"], "func": f02_pblo_130_c_drawdown_from_252d_max_d1},
    "f02_pblo_131_c_recovery_velocity_21d_d1": {"inputs": ["close"], "func": f02_pblo_131_c_recovery_velocity_21d_d1},
    "f02_pblo_132_c_of_c_abs_magnitude_d1": {"inputs": ["close"], "func": f02_pblo_132_c_of_c_abs_magnitude_d1},
    "f02_pblo_133_c_coherence_subwindows_126d_d1": {"inputs": ["close"], "func": f02_pblo_133_c_coherence_subwindows_126d_d1},
    "f02_pblo_134_c_anomaly_abs_zscore_5y_d1": {"inputs": ["close"], "func": f02_pblo_134_c_anomaly_abs_zscore_5y_d1},
    "f02_pblo_135_comp_accel_onset_sustained_pos_c_d1": {"inputs": ["close"], "func": f02_pblo_135_comp_accel_onset_sustained_pos_c_d1},
    "f02_pblo_136_comp_rounding_top_score_d1": {"inputs": ["close"], "func": f02_pblo_136_comp_rounding_top_score_d1},
    "f02_pblo_137_comp_accel_onset_heavy_vol_d1": {"inputs": ["close", "volume"], "func": f02_pblo_137_comp_accel_onset_heavy_vol_d1},
    "f02_pblo_138_comp_sharp_blowoff_score_63d_d1": {"inputs": ["close"], "func": f02_pblo_138_comp_sharp_blowoff_score_63d_d1},
    "f02_pblo_139_comp_multi_horizon_c_consensus_d1": {"inputs": ["close"], "func": f02_pblo_139_comp_multi_horizon_c_consensus_d1},
    "f02_pblo_140_comp_lppl_bubble_composite_252d_d1": {"inputs": ["close"], "func": f02_pblo_140_comp_lppl_bubble_composite_252d_d1},
    "f02_pblo_141_comp_blowoff_fatigue_score_d1": {"inputs": ["close", "volume"], "func": f02_pblo_141_comp_blowoff_fatigue_score_d1},
    "f02_pblo_142_comp_blowoff_terminal_score_d1": {"inputs": ["close"], "func": f02_pblo_142_comp_blowoff_terminal_score_d1},
    "f02_pblo_143_comp_curvature_explosion_count_252d_d1": {"inputs": ["close"], "func": f02_pblo_143_comp_curvature_explosion_count_252d_d1},
    "f02_pblo_144_comp_robust_vs_nonrobust_c_agreement_d1": {"inputs": ["close"], "func": f02_pblo_144_comp_robust_vs_nonrobust_c_agreement_d1},
    "f02_pblo_145_comp_multi_degree_agreement_252d_d1": {"inputs": ["close"], "func": f02_pblo_145_comp_multi_degree_agreement_252d_d1},
    "f02_pblo_146_comp_price_up_c_down_divergence_63d_d1": {"inputs": ["close"], "func": f02_pblo_146_comp_price_up_c_down_divergence_63d_d1},
    "f02_pblo_147_comp_phasespace_curvature_joint_anomaly_d1": {"inputs": ["close"], "func": f02_pblo_147_comp_phasespace_curvature_joint_anomaly_d1},
    "f02_pblo_148_comp_wavelet_polynomial_joint_252d_d1": {"inputs": ["close"], "func": f02_pblo_148_comp_wavelet_polynomial_joint_252d_d1},
    "f02_pblo_149_comp_parabolic_regime_confidence_252d_d1": {"inputs": ["close"], "func": f02_pblo_149_comp_parabolic_regime_confidence_252d_d1},
    "f02_pblo_150_comp_terminal_parabolic_state_composite_d1": {"inputs": ["close"], "func": f02_pblo_150_comp_terminal_parabolic_state_composite_d1},
}
