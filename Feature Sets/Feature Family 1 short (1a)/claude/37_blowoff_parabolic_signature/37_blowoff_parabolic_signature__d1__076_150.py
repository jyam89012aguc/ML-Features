"""blowoff_parabolic_signature d1 features 076_150 — short blowup pipeline 1a-inverse.

Parabolic / super-exponential blowoff signatures at multi-year peaks: long-horizon log-quadratic fits, LPPL-inspired singularity proxies, volume-confirmed regimes, exhaustion patterns.
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


def _rolling_pctrank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).rank(pct=True)


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


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


def _wilder_rma(s, n):
    return s.ewm(alpha=1.0 / n, adjust=False, min_periods=max(n // 3, 2)).mean()



def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


def _logquad_c(s, n):
    """Quadratic coefficient (c) of polynomial fit y ~ a + b*t + c*t² over rolling window n."""
    def _c(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        t = np.arange(len(w), dtype=float)
        try:
            coefs = np.polyfit(t, w, 2)
            return float(coefs[0])
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=max(n // 3, 5)).apply(_c, raw=True)


def _logquad_b(s, n):
    """Linear coefficient (b) of polynomial fit y ~ a + b*t + c*t² over rolling window n."""
    def _b(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        t = np.arange(len(w), dtype=float)
        try:
            coefs = np.polyfit(t, w, 2)
            return float(coefs[1])
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=max(n // 3, 5)).apply(_b, raw=True)


def _logquad_r2_gain(s, n):
    """R² of quadratic fit minus R² of linear fit (positive = parabola explains more)."""
    def _g(w):
        if np.isnan(w).any() or len(w) < 5:
            return np.nan
        t = np.arange(len(w), dtype=float)
        try:
            ss_tot = float(np.sum((w - w.mean()) ** 2))
            if ss_tot == 0:
                return np.nan
            c_lin = np.polyfit(t, w, 1)
            r_lin = w - np.polyval(c_lin, t)
            r2_lin = 1.0 - float(np.sum(r_lin ** 2)) / ss_tot
            c_q = np.polyfit(t, w, 2)
            r_q = w - np.polyval(c_q, t)
            r2_q = 1.0 - float(np.sum(r_q ** 2)) / ss_tot
            return r2_q - r2_lin
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=max(n // 3, 5)).apply(_g, raw=True)


def _logquad_resid_last(s, n):
    """Last-bar residual of log price minus its quadratic fit over window n."""
    def _r(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        t = np.arange(len(w), dtype=float)
        try:
            c = np.polyfit(t, w, 2)
            return float(w[-1] - np.polyval(c, t[-1]))
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=max(n // 3, 5)).apply(_r, raw=True)


def _logquad_resid_max_abs(s, n):
    """Max absolute residual from quadratic fit over window."""
    def _r(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        t = np.arange(len(w), dtype=float)
        try:
            c = np.polyfit(t, w, 2)
            return float(np.max(np.abs(w - np.polyval(c, t))))
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=max(n // 3, 5)).apply(_r, raw=True)


def _logcubic_r2_gain_over_quad(s, n):
    """R² of cubic minus R² of quadratic fit (positive = cubic explains more)."""
    def _g(w):
        if np.isnan(w).any() or len(w) < 6:
            return np.nan
        t = np.arange(len(w), dtype=float)
        try:
            ss_tot = float(np.sum((w - w.mean()) ** 2))
            if ss_tot == 0:
                return np.nan
            c_q = np.polyfit(t, w, 2)
            r_q = w - np.polyval(c_q, t)
            r2_q = 1.0 - float(np.sum(r_q ** 2)) / ss_tot
            c_c = np.polyfit(t, w, 3)
            r_c = w - np.polyval(c_c, t)
            r2_c = 1.0 - float(np.sum(r_c ** 2)) / ss_tot
            return r2_c - r2_q
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=max(n // 3, 6)).apply(_g, raw=True)


def _doubling_time(s, lookback):
    """Bars over which price doubled (causal): bars where price now is ~2x price `lookback` bars ago.
    Returns the implied doubling rate r such that exp(r*lookback) ~ ratio."""
    ratio = _safe_div(s, s.shift(lookback).abs())
    return _safe_log(ratio) / float(lookback)


def _hyper_growth_score(s, n):
    """Growth rate of growth rate: diff(log diff(log(s))) rolling mean."""
    g = _safe_log(s).diff()
    return g.diff().rolling(n, min_periods=max(n // 3, 2)).mean()


def _time_to_singularity_proxy(s, n):
    """LPPL-inspired finite-time-singularity ETA proxy from quadratic fit: -b/(2c) capped.
    Returns bars-from-now (positive = singularity ahead, NaN if not parabolic up)."""
    def _t(w):
        if np.isnan(w).any() or len(w) < 5:
            return np.nan
        t = np.arange(len(w), dtype=float)
        try:
            c = np.polyfit(t, w, 2)
            cc, bb = float(c[0]), float(c[1])
            if cc <= 0:
                return np.nan
            tc = -bb / (2.0 * cc)
            eta = tc - t[-1]
            if eta <= 0 or eta > 5000:
                return np.nan
            return float(eta)
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=max(n // 3, 5)).apply(_t, raw=True)


def _power_law_exp(s, n):
    """Log-log slope of price vs bar index over rolling n — power-law growth exponent proxy."""
    def _e(w):
        if np.isnan(w).any() or len(w) < 5:
            return np.nan
        t = np.arange(1, len(w) + 1, dtype=float)
        lt = np.log(t)
        try:
            mt = lt.mean(); mw = w.mean()
            num = float(((lt - mt) * (w - mw)).sum())
            den = float(((lt - mt) ** 2).sum())
            return num / den if den != 0 else np.nan
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=max(n // 3, 5)).apply(_e, raw=True)

# ============================================================
#                    D1 FEATURES 076-150
# ============================================================

def f37_bpsg_076_logquad_c_above_zero_fraction_252d_d1(close: pd.Series) -> pd.Series:
    c = _logquad_c(_safe_log(close), 252)
    return ((c > 0).astype(float).rolling(252, min_periods=63).mean()).diff()


def f37_bpsg_077_logquad_c_diff_acceleration_21d_d1(close: pd.Series) -> pd.Series:
    c = _logquad_c(_safe_log(close), 252)
    return (c.diff(21).diff(21)).diff()


def f37_bpsg_078_logquad_c_above_q90_count_252d_d1(close: pd.Series) -> pd.Series:
    c = _logquad_c(_safe_log(close), 252)
    q90 = c.rolling(504, min_periods=126).quantile(0.9)
    return ((c > q90).astype(float).rolling(252, min_periods=63).sum()).diff()


def f37_bpsg_079_logquad_b_acceleration_21d_d1(close: pd.Series) -> pd.Series:
    b = _logquad_b(_safe_log(close), 252)
    return (b.diff(21)).diff()


def f37_bpsg_080_parabolic_overshoot_above_local_fit_63d_d1(close: pd.Series) -> pd.Series:
    r = _logquad_resid_last(_safe_log(close), 252)
    return ((r > 0).astype(float).rolling(63, min_periods=21).mean()).diff()


def f37_bpsg_081_subtrend_count_252d_d1(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 21)
    s = np.sign(sl.fillna(0))
    flips = ((s != s.shift(1)) & s.shift(1).ne(0)).astype(float)
    return (flips.rolling(252, min_periods=63).sum()).diff()


def f37_bpsg_082_subtrend_acceleration_252d_d1(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 21)
    s = np.sign(sl.fillna(0))
    flip_mask = (s != s.shift(1)) & s.shift(1).ne(0)
    diff_at_flip = (sl - sl.shift(21)).where(flip_mask, np.nan)
    return (diff_at_flip.rolling(252, min_periods=63).mean()).diff()


def f37_bpsg_083_uptrend_segment_avg_duration_252d_d1(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 21)
    up = (sl > 0).astype(int)
    grp = (up.diff().ne(0)).cumsum()
    streak = up.groupby(grp).cumsum() * up
    return (streak.rolling(252, min_periods=63).mean()).diff()


def f37_bpsg_084_uptrend_max_streak_252d_d1(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 21)
    up = (sl > 0).astype(int)
    grp = (up.diff().ne(0)).cumsum()
    streak = up.groupby(grp).cumsum() * up
    return (streak.rolling(252, min_periods=63).max().astype(float)).diff()


def f37_bpsg_085_subtrend_acceleration_skew_252d_d1(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 21)
    s = np.sign(sl.fillna(0))
    flip_mask = (s != s.shift(1)) & s.shift(1).ne(0)
    diff_at_flip = (sl - sl.shift(21)).where(flip_mask, np.nan)
    return (diff_at_flip.rolling(252, min_periods=63).skew()).diff()


def f37_bpsg_086_higher_highs_count_252d_63d_windows_d1(close: pd.Series) -> pd.Series:
    hh = (close >= close.rolling(63, min_periods=21).max()).astype(float)
    return (hh.rolling(252, min_periods=63).sum()).diff()


def f37_bpsg_087_higher_high_gap_compression_252d_d1(close: pd.Series) -> pd.Series:
    hh = (close >= close.rolling(63, min_periods=21).max())
    idx = np.arange(len(close))
    last = pd.Series(np.where(hh.values, idx, np.nan), index=close.index).ffill()
    gap = pd.Series(idx, index=close.index) - last
    return (gap.rolling(252, min_periods=63).mean()).diff()


def f37_bpsg_088_subtrend_amplitude_growth_252d_d1(close: pd.Series) -> pd.Series:
    amp = close.rolling(21, min_periods=7).max() - close.rolling(21, min_periods=7).min()
    return (_rolling_slope(amp, 252)).diff()


def f37_bpsg_089_subtrend_duration_decay_252d_d1(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 21)
    up = (sl > 0).astype(int)
    grp = (up.diff().ne(0)).cumsum()
    streak = (up.groupby(grp).cumsum() * up).astype(float)
    return (_rolling_slope(streak, 252)).diff()


def f37_bpsg_090_log_periodic_oscillation_proxy_252d_d1(close: pd.Series) -> pd.Series:
    resid = _logquad_resid_last(_safe_log(close), 252)
    return (resid.pow(2).rolling(21, min_periods=7).sum()).diff()


def f37_bpsg_091_acceleration_streak_pos_d2_max_63d_d1(close: pd.Series) -> pd.Series:
    d2 = _safe_log(close).diff().diff()
    pos = (d2 > 0).astype(int)
    grp = (pos.diff().ne(0)).cumsum()
    streak = pos.groupby(grp).cumsum() * pos
    return (streak.rolling(63, min_periods=21).max().astype(float)).diff()


def f37_bpsg_092_acceleration_pos_count_252d_d1(close: pd.Series) -> pd.Series:
    d2 = _safe_log(close).diff().diff()
    return ((d2 > 0).astype(float).rolling(252, min_periods=63).sum()).diff()


def f37_bpsg_093_acceleration_top_q5_count_252d_d1(close: pd.Series) -> pd.Series:
    d2 = _safe_log(close).diff().diff()
    q95 = d2.rolling(252, min_periods=63).quantile(0.95)
    return ((d2 > q95).astype(float).rolling(252, min_periods=63).sum()).diff()


def f37_bpsg_094_d3_log_price_pos_count_252d_d1(close: pd.Series) -> pd.Series:
    d3 = _safe_log(close).diff().diff().diff()
    return ((d3 > 0).astype(float).rolling(252, min_periods=63).sum()).diff()


def f37_bpsg_095_d3_log_price_max_minus_current_63d_d1(close: pd.Series) -> pd.Series:
    d3 = _safe_log(close).diff().diff().diff()
    return (d3.rolling(63, min_periods=21).max() - d3).diff()


def f37_bpsg_096_d3_log_price_streak_pos_max_63d_d1(close: pd.Series) -> pd.Series:
    d3 = _safe_log(close).diff().diff().diff()
    pos = (d3 > 0).astype(int)
    grp = (pos.diff().ne(0)).cumsum()
    streak = pos.groupby(grp).cumsum() * pos
    return (streak.rolling(63, min_periods=21).max().astype(float)).diff()


def f37_bpsg_097_close_above_500d_high_streak_max_252d_d1(close: pd.Series) -> pd.Series:
    h = (close >= close.rolling(500, min_periods=126).max()).astype(int)
    grp = (h.diff().ne(0)).cumsum()
    streak = h.groupby(grp).cumsum() * h
    return (streak.rolling(252, min_periods=63).max().astype(float)).diff()


def f37_bpsg_098_blowoff_apex_proximity_score_63d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    mx = close.rolling(252, min_periods=63).max()
    atr = _atr(high, low, close, 21)
    return (_safe_div((close - mx).clip(lower=0), atr)).diff()


def f37_bpsg_099_wave_count_at_new_high_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    mx = close.rolling(63, min_periods=21).max()
    prev = mx.shift(21)
    atr = _atr(high, low, close, 21)
    new_thrust = (close > prev + atr).astype(float)
    return (new_thrust.rolling(252, min_periods=63).sum()).diff()


def f37_bpsg_100_apex_compression_index_63d_d1(close: pd.Series) -> pd.Series:
    r63 = close.rolling(63, min_periods=21).max() - close.rolling(63, min_periods=21).min()
    r252 = close.rolling(252, min_periods=63).max() - close.rolling(252, min_periods=63).min()
    return (_safe_div(r63, r252)).diff()


def f37_bpsg_101_volume_logquad_c_252d_d1(volume: pd.Series) -> pd.Series:
    return (_logquad_c(_safe_log(volume), 252)).diff()


def f37_bpsg_102_volume_logquad_c_504d_d1(volume: pd.Series) -> pd.Series:
    return (_logquad_c(_safe_log(volume), 504)).diff()


def f37_bpsg_103_volume_x_price_logquad_c_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    return (_logquad_c(_safe_log(dv), 252)).diff()


def f37_bpsg_104_price_c_x_volume_zscore_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = _logquad_c(_safe_log(close), 252)
    vz = _rolling_zscore(volume, 252)
    return (pc * vz).diff()


def f37_bpsg_105_dollar_volume_parabolic_confluence_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = _logquad_c(_safe_log(close), 252)
    vc = _logquad_c(_safe_log(volume), 252)
    return (((pc > 0) & (vc > 0)).astype(float)).diff()


def f37_bpsg_106_dollar_volume_parabolic_confluence_streak_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = _logquad_c(_safe_log(close), 252)
    vc = _logquad_c(_safe_log(volume), 252)
    both = ((pc > 0) & (vc > 0)).astype(int)
    grp = (both.diff().ne(0)).cumsum()
    streak = both.groupby(grp).cumsum() * both
    return (streak.rolling(252, min_periods=63).max().astype(float)).diff()


def f37_bpsg_107_volume_confirmed_parabolic_residual_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    return (_logquad_resid_last(_safe_log(dv), 252)).diff()


def f37_bpsg_108_price_c_minus_volume_c_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = _logquad_c(_safe_log(close), 252); vc = _logquad_c(_safe_log(volume), 252)
    return (pc - vc).diff()


def f37_bpsg_109_price_parabolic_with_volume_dryup_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = _logquad_c(_safe_log(close), 252)
    v21 = volume.rolling(21, min_periods=7).mean(); v63 = volume.rolling(63, min_periods=21).mean()
    return (((pc > 0) & (v21 < v63)).astype(float)).diff()


def f37_bpsg_110_volume_confirmation_count_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    hh = close >= close.rolling(63, min_periods=21).max()
    vavg = volume.rolling(252, min_periods=63).mean()
    confirmed = (hh & (volume > 1.5 * vavg)).astype(float)
    return (confirmed.rolling(252, min_periods=63).sum()).diff()


def f37_bpsg_111_volume_climax_count_at_parabolic_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = _logquad_c(_safe_log(close), 252)
    vavg = volume.rolling(252, min_periods=63).mean()
    cond = (volume > 3 * vavg) & (pc > 0)
    return (cond.astype(float).rolling(252, min_periods=63).sum()).diff()


def f37_bpsg_112_volume_zscore_at_logquad_resid_max_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _logquad_resid_last(_safe_log(close), 252)
    mx = r.rolling(63, min_periods=21).max()
    at_max = (r >= mx - 1e-12)
    vz = _rolling_zscore(volume, 252)
    return (vz.where(at_max, np.nan).rolling(63, min_periods=21).mean()).diff()


def f37_bpsg_113_parabolic_volume_decel_signal_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = _logquad_c(_safe_log(close), 252); vc = _logquad_c(_safe_log(volume), 252)
    decoupled = ((pc > 0) & (vc < 0)).astype(float)
    return (decoupled.rolling(63, min_periods=21).sum()).diff()


def f37_bpsg_114_vol_weighted_parabolic_score_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = _logquad_c(_safe_log(close), 252)
    vm252 = volume.rolling(252, min_periods=63).mean(); vm1260 = volume.rolling(1260, min_periods=252).mean()
    return (pc * _safe_log(_safe_div(vm252, vm1260))).diff()


def f37_bpsg_115_dollar_volume_zscore_at_new_high_504d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    dvz = _rolling_zscore(dv, 504)
    new_high = close >= close.rolling(504, min_periods=126).max()
    return (dvz.where(new_high, np.nan).rolling(252, min_periods=63).mean()).diff()


def f37_bpsg_116_close_dist_above_504d_high_x_volume_z_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    mx = close.rolling(504, min_periods=126).max()
    dist = (close - mx).clip(lower=0) / close.replace(0, np.nan)
    vz = _rolling_zscore(volume, 252)
    return (dist * vz).diff()


def f37_bpsg_117_parabolic_top_with_high_volume_count_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    at_max = (close >= close.rolling(252, min_periods=63).max())
    vavg = volume.rolling(252, min_periods=63).mean()
    cond = at_max & (volume > 2 * vavg)
    return (cond.astype(float).rolling(252, min_periods=63).sum()).diff()


def f37_bpsg_118_volume_jerk_pos_count_252d_d1(volume: pd.Series) -> pd.Series:
    d3 = _safe_log(volume).diff().diff().diff()
    return ((d3 > 0).astype(float).rolling(252, min_periods=63).sum()).diff()


def f37_bpsg_119_volume_curvature_zscore_252d_d1(volume: pd.Series) -> pd.Series:
    return (_rolling_zscore(_logquad_c(_safe_log(volume), 252), 1260)).diff()


def f37_bpsg_120_conditional_volume_in_high_curvature_regime_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = _logquad_c(_safe_log(close), 252)
    cond = pc > 0
    ratio = _safe_div(volume, volume.rolling(252, min_periods=63).mean())
    return (ratio.where(cond, np.nan).rolling(252, min_periods=63).mean()).diff()


def f37_bpsg_121_multi_scale_curvature_ratio_63_252_504_d1(close: pd.Series) -> pd.Series:
    a = _logquad_c(_safe_log(close), 63).abs()
    b = _logquad_c(_safe_log(close), 252).abs()
    c = _logquad_c(_safe_log(close), 504).abs()
    return ((a.fillna(0) + b.fillna(0) + c.fillna(0)) / 3.0).diff()


def f37_bpsg_122_multi_scale_curvature_dispersion_d1(close: pd.Series) -> pd.Series:
    a = _logquad_c(_safe_log(close), 63); b = _logquad_c(_safe_log(close), 252); c = _logquad_c(_safe_log(close), 504)
    return (pd.concat([a, b, c], axis=1).std(axis=1)).diff()


def f37_bpsg_123_multi_scale_curvature_concordance_d1(close: pd.Series) -> pd.Series:
    a = _logquad_c(_safe_log(close), 63); b = _logquad_c(_safe_log(close), 252); c = _logquad_c(_safe_log(close), 504)
    return (((a > 0) & (b > 0) & (c > 0)).astype(float)).diff()


def f37_bpsg_124_multi_scale_curvature_concordance_streak_max_252d_d1(close: pd.Series) -> pd.Series:
    a = _logquad_c(_safe_log(close), 63); b = _logquad_c(_safe_log(close), 252); c = _logquad_c(_safe_log(close), 504)
    both = ((a > 0) & (b > 0) & (c > 0)).astype(int)
    grp = (both.diff().ne(0)).cumsum()
    streak = both.groupby(grp).cumsum() * both
    return (streak.rolling(252, min_periods=63).max().astype(float)).diff()


def f37_bpsg_125_phase_transition_score_252d_d1(close: pd.Series) -> pd.Series:
    z1 = _rolling_zscore(_logquad_c(_safe_log(close), 252), 1260)
    z2 = _rolling_zscore(_logquad_r2_gain(_safe_log(close), 252), 1260)
    z3 = _rolling_zscore(_power_law_exp(close, 252), 1260)
    return (z1.fillna(0) + z2.fillna(0) + z3.fillna(0)).diff()


def f37_bpsg_126_singularity_imminence_score_d1(close: pd.Series) -> pd.Series:
    eta = _time_to_singularity_proxy(_safe_log(close), 252)
    c = _logquad_c(_safe_log(close), 252).clip(lower=0)
    return (_safe_div(c, eta)).diff()


def f37_bpsg_127_parabolic_advance_decay_ratio_d1(close: pd.Series) -> pd.Series:
    c = _logquad_c(_safe_log(close), 252)
    return (_safe_div(c, _ema(c, 63))).diff()


def f37_bpsg_128_parabolic_to_linear_ascent_ratio_252d_d1(close: pd.Series) -> pd.Series:
    def _lin_resid(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        t = np.arange(len(w), dtype=float)
        try:
            c = np.polyfit(t, w, 1)
            return float(w[-1] - np.polyval(c, t[-1]))
        except Exception:
            return np.nan
    r = _safe_log(close).rolling(252, min_periods=63).apply(_lin_resid, raw=True)
    return (_rolling_slope(r, 21)).diff()


def f37_bpsg_129_blowoff_apex_intensity_252d_d1(close: pd.Series) -> pd.Series:
    ma = close.rolling(252, min_periods=63).mean()
    c = _logquad_c(_safe_log(close), 252)
    return ((close - ma) * c).diff()


def f37_bpsg_130_hyper_growth_index_252d_d1(close: pd.Series) -> pd.Series:
    c = _logquad_c(_safe_log(close), 252)
    pe = _rolling_zscore(_power_law_exp(close, 252), 252)
    gn = _rolling_zscore(_logquad_r2_gain(_safe_log(close), 252), 252)
    return ((c.fillna(0) + pe.fillna(0) + gn.fillna(0)) / 3.0).diff()


def f37_bpsg_131_blowoff_terminal_acceleration_composite_d1(close: pd.Series) -> pd.Series:
    d2 = _safe_log(close).diff().diff()
    d3 = d2.diff()
    c = _logquad_c(_safe_log(close), 252)
    return (_rolling_zscore(d2, 21).fillna(0) + _rolling_zscore(d3, 21).fillna(0) + _rolling_zscore(c, 252).fillna(0)).diff()


def f37_bpsg_132_near_singularity_indicator_d1(close: pd.Series) -> pd.Series:
    c = _logquad_c(_safe_log(close), 252)
    eta = _time_to_singularity_proxy(_safe_log(close), 252)
    pe = _power_law_exp(close, 252)
    return (((c > 0) & (eta < 63) & (pe > 2)).astype(float)).diff()


def f37_bpsg_133_blowoff_failure_imminence_score_d1(close: pd.Series) -> pd.Series:
    r = _logquad_resid_last(_safe_log(close), 252)
    neg_z = (-_rolling_zscore(r, 252)).clip(lower=0)
    decl = (r < r.shift(1)).astype(int)
    grp = (decl.diff().ne(0)).cumsum()
    streak = (decl.groupby(grp).cumsum() * decl).astype(float)
    return (neg_z + _rolling_zscore(streak, 63).fillna(0)).diff()


def f37_bpsg_134_logquad_c_vs_atr_norm_drawdown_63d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    c = _logquad_c(_safe_log(close), 252)
    atr_n = _atr(high, low, close, 252) / close.replace(0, np.nan)
    cn = _safe_div(c, atr_n)
    return (cn - cn.rolling(63, min_periods=21).max()).diff()


def f37_bpsg_135_parabolic_phase_transition_streak_max_252d_d1(close: pd.Series) -> pd.Series:
    z1 = _rolling_zscore(_logquad_c(_safe_log(close), 252), 1260)
    z2 = _rolling_zscore(_logquad_r2_gain(_safe_log(close), 252), 1260)
    z3 = _rolling_zscore(_power_law_exp(close, 252), 1260)
    sc = z1.fillna(0) + z2.fillna(0) + z3.fillna(0)
    pos = (sc > 0).astype(int)
    grp = (pos.diff().ne(0)).cumsum()
    streak = pos.groupby(grp).cumsum() * pos
    return (streak.rolling(252, min_periods=63).max().astype(float)).diff()


def f37_bpsg_136_multi_horizon_curvature_z_sum_252_504_1260_d1(close: pd.Series) -> pd.Series:
    a = _rolling_zscore(_logquad_c(_safe_log(close), 252), 1260)
    b = _rolling_zscore(_logquad_c(_safe_log(close), 504), 1260)
    c = _rolling_zscore(_logquad_c(_safe_log(close), 1260), 1260)
    return (a.fillna(0) + b.fillna(0) + c.fillna(0)).diff()


def f37_bpsg_137_parabolic_blowoff_aggregate_score_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    c = _rolling_zscore(_logquad_c(_safe_log(close), 252), 1260)
    gn = _rolling_zscore(_logquad_r2_gain(_safe_log(close), 252), 1260)
    pe = _rolling_zscore(_power_law_exp(close, 252), 1260)
    vc = _rolling_zscore(_logquad_c(_safe_log(volume), 252), 1260)
    hg = _rolling_zscore(_hyper_growth_score(close, 252), 1260)
    r = _logquad_resid_last(_safe_log(close), 252)
    rp = _rolling_zscore(r.clip(lower=0), 252)
    neg = (r < 0).astype(int)
    grp = (neg.diff().ne(0)).cumsum()
    streak = (neg.groupby(grp).cumsum() * neg).astype(float)
    rs = _rolling_zscore(streak, 63)
    return (c.fillna(0) + gn.fillna(0) + pe.fillna(0) + vc.fillna(0) + hg.fillna(0) + rp.fillna(0) - rs.fillna(0)).diff()


def f37_bpsg_138_curvature_with_breadth_252d_d1(close: pd.Series) -> pd.Series:
    c = _logquad_c(_safe_log(close), 252)
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    above = (close > sma).astype(float).rolling(252, min_periods=63).mean()
    return (c * above).diff()


def f37_bpsg_139_parabolic_run_age_252d_d1(close: pd.Series) -> pd.Series:
    c = _logquad_c(_safe_log(close), 252)
    cross_below = (c < 0) & (c.shift(1) >= 0)
    idx = np.arange(len(close))
    last = pd.Series(np.where(cross_below.values, idx, np.nan), index=close.index).ffill().fillna(0)
    return (pd.Series(idx, index=close.index) - last).diff()


def f37_bpsg_140_parabolic_curvature_diff_atr_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    c = _logquad_c(_safe_log(close), 252)
    atr = _atr(high, low, close, 252)
    return (c * _safe_div(atr, close)).diff()


def f37_bpsg_141_singularity_eta_minus_subtrend_count_div_d1(close: pd.Series) -> pd.Series:
    eta = _time_to_singularity_proxy(_safe_log(close), 252)
    sl = _rolling_slope(_safe_log(close), 21); s = np.sign(sl.fillna(0))
    flips = ((s != s.shift(1)) & s.shift(1).ne(0)).astype(float)
    cnt = flips.rolling(252, min_periods=63).sum().replace(0, np.nan)
    return (_safe_div(eta, cnt)).diff()


def f37_bpsg_142_blowoff_phase_progression_score_d1(close: pd.Series) -> pd.Series:
    c = _logquad_c(_safe_log(close), 252)
    cross = (c < 0) & (c.shift(1) >= 0)
    idx = np.arange(len(close))
    last = pd.Series(np.where(cross.values, idx, np.nan), index=close.index).ffill().fillna(0)
    age = pd.Series(idx, index=close.index) - last
    zc = _rolling_zscore(c, 1260)
    eta = _time_to_singularity_proxy(_safe_log(close), 252).replace(0, np.nan)
    return (_safe_div(age * zc, eta)).diff()


def f37_bpsg_143_curvature_x_volume_climax_at_high_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    mx = close.rolling(252, min_periods=63).max()
    near_top = close >= mx * 0.99
    c = _logquad_c(_safe_log(close), 252).clip(lower=0)
    vz_max = _rolling_zscore(volume, 252).rolling(21, min_periods=7).max()
    return ((c * vz_max).where(near_top, np.nan).rolling(252, min_periods=63).max()).diff()


def f37_bpsg_144_curvature_failing_overlap_signal_63d_d1(close: pd.Series) -> pd.Series:
    c = _logquad_c(_safe_log(close), 252)
    r = _logquad_resid_last(_safe_log(close), 252)
    sd = r.rolling(252, min_periods=63).std()
    ev = ((c < c.shift(21)) & (r < -sd)).astype(float)
    return (ev.rolling(63, min_periods=21).sum()).diff()


def f37_bpsg_145_multi_horizon_parabolic_failure_score_d1(close: pd.Series) -> pd.Series:
    a = _rolling_zscore(_logquad_resid_last(_safe_log(close), 252), 1260).fillna(0).clip(upper=0).abs()
    b = _rolling_zscore(_logquad_resid_last(_safe_log(close), 504), 1260).fillna(0).clip(upper=0).abs()
    c = _rolling_zscore(_logquad_resid_last(_safe_log(close), 1260), 1260).fillna(0).clip(upper=0).abs()
    return (a + b + c).diff()


def f37_bpsg_146_curvature_drift_velocity_252d_diff_63d_d1(close: pd.Series) -> pd.Series:
    c = _logquad_c(_safe_log(close), 252)
    return (c.diff(63)).diff()


def f37_bpsg_147_parabolic_to_linear_advance_ratio_252d_atr_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    def _lr(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        t = np.arange(len(w), dtype=float)
        try:
            c = np.polyfit(t, w, 1)
            return float(w[-1] - np.polyval(c, t[-1]))
        except Exception:
            return np.nan
    r = _safe_log(close).rolling(252, min_periods=63).apply(_lr, raw=True)
    atr_n = _atr(high, low, close, 21) / close.replace(0, np.nan)
    return (_safe_div(r, atr_n)).diff()


def f37_bpsg_148_composite_blowoff_aggregate_atr_norm_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    c = _logquad_c(_safe_log(close), 252)
    atr_n = _atr(high, low, close, 252) / close.replace(0, np.nan)
    cn = c * atr_n.replace(0, np.nan)
    g = _logquad_r2_gain(_safe_log(close), 252)
    pe = _rolling_zscore(_power_law_exp(close, 252), 1260)
    return (cn.fillna(0) + 0.5 * g.fillna(0) + 0.5 * pe.fillna(0)).diff()


def f37_bpsg_149_apex_signal_5y_blowoff_summary_d1(close: pd.Series) -> pd.Series:
    c = _logquad_c(_safe_log(close), 252)
    g = _logquad_r2_gain(_safe_log(close), 252)
    pe = _rolling_zscore(_power_law_exp(close, 252), 1260)
    agg = c.fillna(0) + g.fillna(0) + pe.fillna(0)
    return (agg * (c > 0).astype(float)).diff()


def f37_bpsg_150_parabolic_volume_signature_aggregate_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    z1 = _rolling_zscore(_logquad_c(_safe_log(dv), 252), 1260)
    z2 = _rolling_zscore(_logquad_c(_safe_log(close), 252), 1260)
    pc = _logquad_c(_safe_log(close), 252); vc = _logquad_c(_safe_log(volume), 252)
    both = ((pc > 0) & (vc > 0)).astype(int)
    grp = (both.diff().ne(0)).cumsum()
    streak = (both.groupby(grp).cumsum() * both).astype(float)
    z3 = _rolling_zscore(streak, 252)
    return (z1.fillna(0) + z2.fillna(0) + z3.fillna(0)).diff()


BLOWOFF_PARABOLIC_SIGNATURE_D1_REGISTRY_076_150 = {
    "f37_bpsg_076_logquad_c_above_zero_fraction_252d_d1": {"inputs": ["close"], "func": f37_bpsg_076_logquad_c_above_zero_fraction_252d_d1},
    "f37_bpsg_077_logquad_c_diff_acceleration_21d_d1": {"inputs": ["close"], "func": f37_bpsg_077_logquad_c_diff_acceleration_21d_d1},
    "f37_bpsg_078_logquad_c_above_q90_count_252d_d1": {"inputs": ["close"], "func": f37_bpsg_078_logquad_c_above_q90_count_252d_d1},
    "f37_bpsg_079_logquad_b_acceleration_21d_d1": {"inputs": ["close"], "func": f37_bpsg_079_logquad_b_acceleration_21d_d1},
    "f37_bpsg_080_parabolic_overshoot_above_local_fit_63d_d1": {"inputs": ["close"], "func": f37_bpsg_080_parabolic_overshoot_above_local_fit_63d_d1},
    "f37_bpsg_081_subtrend_count_252d_d1": {"inputs": ["close"], "func": f37_bpsg_081_subtrend_count_252d_d1},
    "f37_bpsg_082_subtrend_acceleration_252d_d1": {"inputs": ["close"], "func": f37_bpsg_082_subtrend_acceleration_252d_d1},
    "f37_bpsg_083_uptrend_segment_avg_duration_252d_d1": {"inputs": ["close"], "func": f37_bpsg_083_uptrend_segment_avg_duration_252d_d1},
    "f37_bpsg_084_uptrend_max_streak_252d_d1": {"inputs": ["close"], "func": f37_bpsg_084_uptrend_max_streak_252d_d1},
    "f37_bpsg_085_subtrend_acceleration_skew_252d_d1": {"inputs": ["close"], "func": f37_bpsg_085_subtrend_acceleration_skew_252d_d1},
    "f37_bpsg_086_higher_highs_count_252d_63d_windows_d1": {"inputs": ["close"], "func": f37_bpsg_086_higher_highs_count_252d_63d_windows_d1},
    "f37_bpsg_087_higher_high_gap_compression_252d_d1": {"inputs": ["close"], "func": f37_bpsg_087_higher_high_gap_compression_252d_d1},
    "f37_bpsg_088_subtrend_amplitude_growth_252d_d1": {"inputs": ["close"], "func": f37_bpsg_088_subtrend_amplitude_growth_252d_d1},
    "f37_bpsg_089_subtrend_duration_decay_252d_d1": {"inputs": ["close"], "func": f37_bpsg_089_subtrend_duration_decay_252d_d1},
    "f37_bpsg_090_log_periodic_oscillation_proxy_252d_d1": {"inputs": ["close"], "func": f37_bpsg_090_log_periodic_oscillation_proxy_252d_d1},
    "f37_bpsg_091_acceleration_streak_pos_d2_max_63d_d1": {"inputs": ["close"], "func": f37_bpsg_091_acceleration_streak_pos_d2_max_63d_d1},
    "f37_bpsg_092_acceleration_pos_count_252d_d1": {"inputs": ["close"], "func": f37_bpsg_092_acceleration_pos_count_252d_d1},
    "f37_bpsg_093_acceleration_top_q5_count_252d_d1": {"inputs": ["close"], "func": f37_bpsg_093_acceleration_top_q5_count_252d_d1},
    "f37_bpsg_094_d3_log_price_pos_count_252d_d1": {"inputs": ["close"], "func": f37_bpsg_094_d3_log_price_pos_count_252d_d1},
    "f37_bpsg_095_d3_log_price_max_minus_current_63d_d1": {"inputs": ["close"], "func": f37_bpsg_095_d3_log_price_max_minus_current_63d_d1},
    "f37_bpsg_096_d3_log_price_streak_pos_max_63d_d1": {"inputs": ["close"], "func": f37_bpsg_096_d3_log_price_streak_pos_max_63d_d1},
    "f37_bpsg_097_close_above_500d_high_streak_max_252d_d1": {"inputs": ["close"], "func": f37_bpsg_097_close_above_500d_high_streak_max_252d_d1},
    "f37_bpsg_098_blowoff_apex_proximity_score_63d_d1": {"inputs": ["close", "high", "low"], "func": f37_bpsg_098_blowoff_apex_proximity_score_63d_d1},
    "f37_bpsg_099_wave_count_at_new_high_252d_d1": {"inputs": ["close", "high", "low"], "func": f37_bpsg_099_wave_count_at_new_high_252d_d1},
    "f37_bpsg_100_apex_compression_index_63d_d1": {"inputs": ["close"], "func": f37_bpsg_100_apex_compression_index_63d_d1},
    "f37_bpsg_101_volume_logquad_c_252d_d1": {"inputs": ["volume"], "func": f37_bpsg_101_volume_logquad_c_252d_d1},
    "f37_bpsg_102_volume_logquad_c_504d_d1": {"inputs": ["volume"], "func": f37_bpsg_102_volume_logquad_c_504d_d1},
    "f37_bpsg_103_volume_x_price_logquad_c_252d_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_103_volume_x_price_logquad_c_252d_d1},
    "f37_bpsg_104_price_c_x_volume_zscore_252d_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_104_price_c_x_volume_zscore_252d_d1},
    "f37_bpsg_105_dollar_volume_parabolic_confluence_252d_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_105_dollar_volume_parabolic_confluence_252d_d1},
    "f37_bpsg_106_dollar_volume_parabolic_confluence_streak_252d_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_106_dollar_volume_parabolic_confluence_streak_252d_d1},
    "f37_bpsg_107_volume_confirmed_parabolic_residual_252d_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_107_volume_confirmed_parabolic_residual_252d_d1},
    "f37_bpsg_108_price_c_minus_volume_c_252d_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_108_price_c_minus_volume_c_252d_d1},
    "f37_bpsg_109_price_parabolic_with_volume_dryup_252d_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_109_price_parabolic_with_volume_dryup_252d_d1},
    "f37_bpsg_110_volume_confirmation_count_252d_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_110_volume_confirmation_count_252d_d1},
    "f37_bpsg_111_volume_climax_count_at_parabolic_252d_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_111_volume_climax_count_at_parabolic_252d_d1},
    "f37_bpsg_112_volume_zscore_at_logquad_resid_max_63d_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_112_volume_zscore_at_logquad_resid_max_63d_d1},
    "f37_bpsg_113_parabolic_volume_decel_signal_63d_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_113_parabolic_volume_decel_signal_63d_d1},
    "f37_bpsg_114_vol_weighted_parabolic_score_252d_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_114_vol_weighted_parabolic_score_252d_d1},
    "f37_bpsg_115_dollar_volume_zscore_at_new_high_504d_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_115_dollar_volume_zscore_at_new_high_504d_d1},
    "f37_bpsg_116_close_dist_above_504d_high_x_volume_z_252d_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_116_close_dist_above_504d_high_x_volume_z_252d_d1},
    "f37_bpsg_117_parabolic_top_with_high_volume_count_252d_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_117_parabolic_top_with_high_volume_count_252d_d1},
    "f37_bpsg_118_volume_jerk_pos_count_252d_d1": {"inputs": ["volume"], "func": f37_bpsg_118_volume_jerk_pos_count_252d_d1},
    "f37_bpsg_119_volume_curvature_zscore_252d_d1": {"inputs": ["volume"], "func": f37_bpsg_119_volume_curvature_zscore_252d_d1},
    "f37_bpsg_120_conditional_volume_in_high_curvature_regime_252d_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_120_conditional_volume_in_high_curvature_regime_252d_d1},
    "f37_bpsg_121_multi_scale_curvature_ratio_63_252_504_d1": {"inputs": ["close"], "func": f37_bpsg_121_multi_scale_curvature_ratio_63_252_504_d1},
    "f37_bpsg_122_multi_scale_curvature_dispersion_d1": {"inputs": ["close"], "func": f37_bpsg_122_multi_scale_curvature_dispersion_d1},
    "f37_bpsg_123_multi_scale_curvature_concordance_d1": {"inputs": ["close"], "func": f37_bpsg_123_multi_scale_curvature_concordance_d1},
    "f37_bpsg_124_multi_scale_curvature_concordance_streak_max_252d_d1": {"inputs": ["close"], "func": f37_bpsg_124_multi_scale_curvature_concordance_streak_max_252d_d1},
    "f37_bpsg_125_phase_transition_score_252d_d1": {"inputs": ["close"], "func": f37_bpsg_125_phase_transition_score_252d_d1},
    "f37_bpsg_126_singularity_imminence_score_d1": {"inputs": ["close"], "func": f37_bpsg_126_singularity_imminence_score_d1},
    "f37_bpsg_127_parabolic_advance_decay_ratio_d1": {"inputs": ["close"], "func": f37_bpsg_127_parabolic_advance_decay_ratio_d1},
    "f37_bpsg_128_parabolic_to_linear_ascent_ratio_252d_d1": {"inputs": ["close"], "func": f37_bpsg_128_parabolic_to_linear_ascent_ratio_252d_d1},
    "f37_bpsg_129_blowoff_apex_intensity_252d_d1": {"inputs": ["close"], "func": f37_bpsg_129_blowoff_apex_intensity_252d_d1},
    "f37_bpsg_130_hyper_growth_index_252d_d1": {"inputs": ["close"], "func": f37_bpsg_130_hyper_growth_index_252d_d1},
    "f37_bpsg_131_blowoff_terminal_acceleration_composite_d1": {"inputs": ["close"], "func": f37_bpsg_131_blowoff_terminal_acceleration_composite_d1},
    "f37_bpsg_132_near_singularity_indicator_d1": {"inputs": ["close"], "func": f37_bpsg_132_near_singularity_indicator_d1},
    "f37_bpsg_133_blowoff_failure_imminence_score_d1": {"inputs": ["close"], "func": f37_bpsg_133_blowoff_failure_imminence_score_d1},
    "f37_bpsg_134_logquad_c_vs_atr_norm_drawdown_63d_d1": {"inputs": ["close", "high", "low"], "func": f37_bpsg_134_logquad_c_vs_atr_norm_drawdown_63d_d1},
    "f37_bpsg_135_parabolic_phase_transition_streak_max_252d_d1": {"inputs": ["close"], "func": f37_bpsg_135_parabolic_phase_transition_streak_max_252d_d1},
    "f37_bpsg_136_multi_horizon_curvature_z_sum_252_504_1260_d1": {"inputs": ["close"], "func": f37_bpsg_136_multi_horizon_curvature_z_sum_252_504_1260_d1},
    "f37_bpsg_137_parabolic_blowoff_aggregate_score_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_137_parabolic_blowoff_aggregate_score_d1},
    "f37_bpsg_138_curvature_with_breadth_252d_d1": {"inputs": ["close"], "func": f37_bpsg_138_curvature_with_breadth_252d_d1},
    "f37_bpsg_139_parabolic_run_age_252d_d1": {"inputs": ["close"], "func": f37_bpsg_139_parabolic_run_age_252d_d1},
    "f37_bpsg_140_parabolic_curvature_diff_atr_252d_d1": {"inputs": ["close", "high", "low"], "func": f37_bpsg_140_parabolic_curvature_diff_atr_252d_d1},
    "f37_bpsg_141_singularity_eta_minus_subtrend_count_div_d1": {"inputs": ["close"], "func": f37_bpsg_141_singularity_eta_minus_subtrend_count_div_d1},
    "f37_bpsg_142_blowoff_phase_progression_score_d1": {"inputs": ["close"], "func": f37_bpsg_142_blowoff_phase_progression_score_d1},
    "f37_bpsg_143_curvature_x_volume_climax_at_high_252d_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_143_curvature_x_volume_climax_at_high_252d_d1},
    "f37_bpsg_144_curvature_failing_overlap_signal_63d_d1": {"inputs": ["close"], "func": f37_bpsg_144_curvature_failing_overlap_signal_63d_d1},
    "f37_bpsg_145_multi_horizon_parabolic_failure_score_d1": {"inputs": ["close"], "func": f37_bpsg_145_multi_horizon_parabolic_failure_score_d1},
    "f37_bpsg_146_curvature_drift_velocity_252d_diff_63d_d1": {"inputs": ["close"], "func": f37_bpsg_146_curvature_drift_velocity_252d_diff_63d_d1},
    "f37_bpsg_147_parabolic_to_linear_advance_ratio_252d_atr_d1": {"inputs": ["close", "high", "low"], "func": f37_bpsg_147_parabolic_to_linear_advance_ratio_252d_atr_d1},
    "f37_bpsg_148_composite_blowoff_aggregate_atr_norm_d1": {"inputs": ["close", "high", "low"], "func": f37_bpsg_148_composite_blowoff_aggregate_atr_norm_d1},
    "f37_bpsg_149_apex_signal_5y_blowoff_summary_d1": {"inputs": ["close"], "func": f37_bpsg_149_apex_signal_5y_blowoff_summary_d1},
    "f37_bpsg_150_parabolic_volume_signature_aggregate_d1": {"inputs": ["close", "volume"], "func": f37_bpsg_150_parabolic_volume_signature_aggregate_d1},
}
