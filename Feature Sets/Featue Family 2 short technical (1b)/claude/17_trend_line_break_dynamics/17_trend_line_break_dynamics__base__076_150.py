"""trend_line_break_dynamics base features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__001_075.py. Each
feature encodes a different concept in the trendline-fit / break-event / retest-failure /
durability / support-resistance-flip / breakdown-asymmetry theme.

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


def _rolling_lr_endpoint(s, n, min_periods=None):
    """Last-point value of OLS y = a + b*x fit on rolling window (the fitted trendline value)."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _f(w):
        valid = ~np.isnan(w)
        nv = int(valid.sum())
        if nv < min_periods:
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
        return float(a + b * (len(w) - 1))
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def _rolling_resid_std(s, n, min_periods=None):
    """Std of residuals from OLS fit on rolling window."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _f(w):
        valid = ~np.isnan(w)
        nv = int(valid.sum())
        if nv < min_periods:
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
        r = yv - (a + b * x)
        if r.size < 2:
            return np.nan
        return float(np.std(r, ddof=1))
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def _rolling_r2(s, n, min_periods=None):
    """R² of OLS y vs x on rolling window."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _f(w):
        valid = ~np.isnan(w)
        nv = int(valid.sum())
        if nv < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        yv = w
        if not valid.all():
            x = x[valid]; yv = w[valid]
        xm = x.mean(); ym = yv.mean()
        tss = float(((yv - ym) ** 2).sum())
        if tss <= 0:
            return np.nan
        den = float(((x - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        b = float(((x - xm) * (yv - ym)).sum() / den)
        a = ym - b * xm
        yhat = a + b * x
        rss = float(((yv - yhat) ** 2).sum())
        return 1.0 - rss / tss
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def _theil_sen_slope(w):
    """Median-of-pairs slope (Theil-Sen) on a 1D window array. NaN-safe."""
    valid = ~np.isnan(w)
    nv = int(valid.sum())
    if nv < 5:
        return np.nan
    x = np.arange(len(w), dtype=float)
    if not valid.all():
        x = x[valid]; w = w[valid]
    n = w.size
    # subsample if too long, keep deterministic stride
    if n > 50:
        step = max(1, n // 50)
        idx = np.arange(0, n, step)
        x = x[idx]; w = w[idx]
        n = w.size
    slopes = []
    for i in range(n - 1):
        dx = x[i+1:] - x[i]
        dy = w[i+1:] - w[i]
        mask = dx != 0
        if mask.any():
            slopes.extend((dy[mask] / dx[mask]).tolist())
    if not slopes:
        return np.nan
    return float(np.median(slopes))


def _bars_since_true(b: pd.Series) -> pd.Series:
    """For each bar, bars since the most-recent True in boolean series b (NaN before first True)."""
    arr = b.fillna(False).astype(bool).values
    n = arr.size
    out = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=b.index)


def f17_tlbk_076_log_dist_close_to_trendline_21d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    out = lc - _rolling_lr_endpoint(lc, 21, min_periods=7)
    return out


def f17_tlbk_077_log_dist_close_to_trendline_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    out = lc - _rolling_lr_endpoint(lc, 63, min_periods=21)
    return out


def f17_tlbk_078_log_dist_close_to_trendline_252d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    out = lc - _rolling_lr_endpoint(lc, 252, min_periods=84)
    return out


def f17_tlbk_079_log_dist_close_to_trendline_504d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    out = lc - _rolling_lr_endpoint(lc, 504, min_periods=168)
    return out


def f17_tlbk_080_atr_dist_close_to_trendline_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl_lvl = np.exp(_rolling_lr_endpoint(lc, 63, min_periods=21))
    out = _safe_div(close - tl_lvl, _atr(high, low, close, n=21))
    return out


def f17_tlbk_081_atr_dist_close_to_trendline_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl_lvl = np.exp(_rolling_lr_endpoint(lc, 252, min_periods=84))
    out = _safe_div(close - tl_lvl, _atr(high, low, close, n=21))
    return out


def f17_tlbk_082_sigma_dist_close_to_trendline_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    out = _safe_div(lc - tl, rs)
    return out


def f17_tlbk_083_sigma_dist_close_to_trendline_252d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 252, min_periods=84)
    rs = _rolling_resid_std(lc, 252, min_periods=84)
    out = _safe_div(lc - tl, rs)
    return out


def f17_tlbk_084_trendline_gap_zscore_63d_over_252d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    gap = lc - _rolling_lr_endpoint(lc, 63, min_periods=21)
    out = _rolling_zscore(gap, 252, min_periods=84)
    return out


def f17_tlbk_085_trendline_gap_zscore_252d_over_504d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    gap = lc - _rolling_lr_endpoint(lc, 252, min_periods=84)
    out = _rolling_zscore(gap, 504, min_periods=168)
    return out


def f17_tlbk_086_trendline_gap_pct_rank_63d_in_252d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    gap = lc - _rolling_lr_endpoint(lc, 63, min_periods=21)
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
    out = gap.rolling(252, min_periods=84).apply(_rk, raw=True)
    return out


def f17_tlbk_087_high_minus_low_trendline_gap_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    lh = _safe_log(high); ll = _safe_log(low); lc = _safe_log(close)
    uh = _rolling_lr_endpoint(lh, 252, min_periods=84)
    ul = _rolling_lr_endpoint(ll, 252, min_periods=84)
    out = (lc - uh) - (lc - ul)
    return out


def f17_tlbk_088_trendline_gap_5d_accel_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    gap = lc - _rolling_lr_endpoint(lc, 63, min_periods=21)
    out = gap - gap.shift(5)
    return out


def f17_tlbk_089_low_trendline_gap_log_close_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    ll = _safe_log(low); lc = _safe_log(close)
    out = lc - _rolling_lr_endpoint(ll, 63, min_periods=21)
    return out


def f17_tlbk_090_high_trendline_gap_log_close_63d(high: pd.Series, close: pd.Series) -> pd.Series:
    lh = _safe_log(high); lc = _safe_log(close)
    out = lc - _rolling_lr_endpoint(lh, 63, min_periods=21)
    return out


def f17_tlbk_091_trendline_angle_deg_logclose_63d(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    out = np.degrees(np.arctan(sl))
    return out


def f17_tlbk_092_trendline_angle_deg_logclose_252d(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 252, min_periods=84)
    out = np.degrees(np.arctan(sl))
    return out


def f17_tlbk_093_trendline_angle_deg_logclose_504d(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 504, min_periods=168)
    out = np.degrees(np.arctan(sl))
    return out


def f17_tlbk_094_angle_top_quintile_63d_in_252d(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    ang = np.degrees(np.arctan(sl))
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
    rk = ang.rolling(252, min_periods=84).apply(_rk, raw=True)
    out = (rk >= 0.8).astype(float).where(rk.notna(), np.nan)
    return out


def f17_tlbk_095_angle_zscore_63d_over_252d(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    ang = np.degrees(np.arctan(sl))
    out = _rolling_zscore(ang, 252, min_periods=84)
    return out


def f17_tlbk_096_angle_decel_21d_63d_slope(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    ang = np.degrees(np.arctan(sl))
    out = ang - ang.shift(21)
    return out


def f17_tlbk_097_angle_decel_63d_252d_slope(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 252, min_periods=84)
    ang = np.degrees(np.arctan(sl))
    out = ang - ang.shift(63)
    return out


def f17_tlbk_098_angle_volatility_63d_over_63d(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    ang = np.degrees(np.arctan(sl))
    out = ang.rolling(63, min_periods=21).std()
    return out


def f17_tlbk_099_angle_above_45deg_indicator_63d(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    ang = np.degrees(np.arctan(sl)).abs()
    out = (ang > 45.0).astype(float).where(ang.notna(), np.nan)
    return out


def f17_tlbk_100_frac_steep_angle_30deg_252d_63d(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    ang = np.degrees(np.arctan(sl)).abs()
    steep = (ang > 30.0).astype(float).where(ang.notna(), np.nan)
    out = steep.rolling(252, min_periods=84).mean()
    return out


def f17_tlbk_101_angle_ratio_21d_over_252d(close: pd.Series) -> pd.Series:
    s21 = _rolling_slope(_safe_log(close), 21, min_periods=7)
    s252 = _rolling_slope(_safe_log(close), 252, min_periods=84)
    out = _safe_div(np.arctan(s21), np.arctan(s252))
    return out


def f17_tlbk_102_angle_blowoff_indicator_21d_vs_252d_median(close: pd.Series) -> pd.Series:
    s21 = _rolling_slope(_safe_log(close), 21, min_periods=7)
    ang21 = np.degrees(np.arctan(s21)).abs()
    med = ang21.rolling(252, min_periods=84).median()
    out = (ang21 > 2.0 * med).astype(float).where(med.notna(), np.nan)
    return out


def f17_tlbk_103_angle_range_max_min_63d(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 21, min_periods=7)
    ang = np.degrees(np.arctan(sl))
    out = ang.rolling(63, min_periods=21).max() - ang.rolling(63, min_periods=21).min()
    return out


def f17_tlbk_104_angle_inversion_event_63d(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    ang = np.degrees(np.arctan(sl))
    was_pos = (ang.shift(63) > 30.0).astype(float)
    is_neg = (ang < -30.0).astype(float)
    out = (was_pos * is_neg).where(ang.shift(63).notna() & ang.notna(), np.nan)
    return out


def f17_tlbk_105_angle_21d_decay_rate(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    ang = np.degrees(np.arctan(sl))
    out = _rolling_slope(ang, 21, min_periods=7)
    return out


def f17_tlbk_106_broken_line_rejection_indicator_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    below = (lc < tl).astype(float)
    recently_broken = (((below.shift(1) < 0.5) & (below > 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    near_from_below = ((tl - lc).abs() <= 0.5 * rs) & (lc < tl)
    out = (near_from_below.astype(float) * (recently_broken > 0).astype(float)).where(rs.notna(), np.nan)
    return out


def f17_tlbk_107_broken_line_rejection_indicator_252d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 252, min_periods=84)
    below = (lc < tl).astype(float)
    recently_broken = (((below.shift(1) < 0.5) & (below > 0.5)).astype(float)).rolling(63, min_periods=21).sum()
    rs = _rolling_resid_std(lc, 252, min_periods=84)
    near_from_below = ((tl - lc).abs() <= 0.5 * rs) & (lc < tl)
    out = (near_from_below.astype(float) * (recently_broken > 0).astype(float)).where(rs.notna(), np.nan)
    return out


def f17_tlbk_108_rejection_drop_10d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    below = (lc < tl).astype(float)
    rb = (((below.shift(1) < 0.5) & (below > 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    rej = (((tl - lc).abs() <= 0.5 * rs) & (lc < tl)).astype(float) * (rb > 0).astype(float)
    min_lc_10 = lc.rolling(10, min_periods=3).min()
    drop = lc - min_lc_10
    out = (drop * (rej.shift(10) > 0.5).astype(float)).where(rej.shift(10).notna(), np.nan)
    return out


def f17_tlbk_109_bars_break_to_first_rejection_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    break_e = ((above.shift(1) > 0.5) & (above < 0.5)) & tl.notna() & tl.shift(1).notna()
    rej = ((tl - lc).abs() <= 0.5 * rs) & (lc < tl) & rs.notna()
    bars_since_break = _bars_since_true(break_e)
    bars_since_rej = _bars_since_true(rej)
    # bars from break to current rej (if rej is current and break is older)
    gap = bars_since_break - bars_since_rej
    out = gap.where((bars_since_rej == 0) & (bars_since_break > 0), np.nan)
    return out


def f17_tlbk_110_rejection_count_63d_in_252d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    below = (lc < tl).astype(float)
    rb = (((below.shift(1) < 0.5) & (below > 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    rej = (((tl - lc).abs() <= 0.5 * rs) & (lc < tl)).astype(float) * (rb > 0).astype(float)
    out = rej.where(rs.notna(), np.nan).rolling(252, min_periods=84).sum()
    return out


def f17_tlbk_111_successful_rejection_rate_63d_in_252d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    br = (((above.shift(1) > 0.5) & (above < 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    retests = (((lc - tl).abs() <= 0.5 * rs) & (br > 0)).astype(float)
    rej_after = (retests.shift(5) * (lc < tl).astype(float)).where(retests.shift(5).notna(), np.nan)
    out = _safe_div(rej_after.rolling(252, min_periods=84).sum(), retests.rolling(252, min_periods=84).sum())
    return out


def f17_tlbk_112_broken_line_role_reversal_score_63d_in_252d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    below = (lc < tl).astype(float)
    rb = (((below.shift(1) < 0.5) & (below > 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    rej = (((tl - lc).abs() <= 0.5 * rs) & (lc < tl)).astype(float) * (rb > 0).astype(float)
    rec = (((below.shift(1) > 0.5) & (below < 0.5)).astype(float)).where(tl.notna(), np.nan)
    out = rej.rolling(252, min_periods=84).sum() - rec.rolling(252, min_periods=84).sum()
    return out


def f17_tlbk_113_three_plus_rejections_in_63d_indicator(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    below = (lc < tl).astype(float)
    rb = (((below.shift(1) < 0.5) & (below > 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    rej = (((tl - lc).abs() <= 0.5 * rs) & (lc < tl)).astype(float) * (rb > 0).astype(float)
    cnt = rej.where(rs.notna(), np.nan).rolling(63, min_periods=21).sum()
    out = (cnt >= 3).astype(float).where(cnt.notna(), np.nan)
    return out


def f17_tlbk_114_rejection_drop_atr_units_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    below = (lc < tl).astype(float)
    rb = (((below.shift(1) < 0.5) & (below > 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    rej = (((tl - lc).abs() <= 0.5 * rs) & (lc < tl)).astype(float) * (rb > 0).astype(float)
    min_lc_10 = close.rolling(10, min_periods=3).min()
    drop = close - min_lc_10
    atr = _atr(high, low, close, n=21)
    val = _safe_div(drop, atr) * (rej.shift(10) > 0.5).astype(float)
    out = val.where(rej.shift(10).notna(), np.nan)
    return out


def f17_tlbk_115_first_rejection_after_21d_broken_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    below = (lc < tl).astype(float)
    broken_long = (below.rolling(21, min_periods=10).min() > 0.5).astype(float)
    rej = (((tl - lc).abs() <= 0.5 * rs) & (lc < tl)).astype(float)
    out = (rej * broken_long).where(rs.notna(), np.nan)
    return out


def f17_tlbk_116_broken_high_line_rejection_63d(high: pd.Series, close: pd.Series) -> pd.Series:
    lh = _safe_log(high); lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lh, 63, min_periods=21)
    below = (lc < tl).astype(float)
    rb = (((below.shift(1) < 0.5) & (below > 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    rs = _rolling_resid_std(lh, 63, min_periods=21)
    rej = (((tl - lc).abs() <= 0.5 * rs) & (lc < tl)).astype(float) * (rb > 0).astype(float)
    out = rej.where(rs.notna(), np.nan)
    return out


def f17_tlbk_117_broken_low_line_acts_as_support_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    ll = _safe_log(low); lc = _safe_log(close)
    tl = _rolling_lr_endpoint(ll, 63, min_periods=21)
    below = (lc < tl).astype(float)
    rb = (((below.shift(1) < 0.5) & (below > 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    rs = _rolling_resid_std(ll, 63, min_periods=21)
    recover = (((below.shift(1) > 0.5) & (below < 0.5)).astype(float)) * (rb > 0).astype(float)
    out = recover.where(rs.notna(), np.nan)
    return out


def f17_tlbk_118_rejection_then_lower_low_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    ll = _safe_log(low); lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    below = (lc < tl).astype(float)
    rb = (((below.shift(1) < 0.5) & (below > 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    rej = (((tl - lc).abs() <= 0.5 * rs) & (lc < tl)).astype(float) * (rb > 0).astype(float)
    prior_min = ll.shift(21).rolling(63, min_periods=21).min()
    post_min = ll.rolling(21, min_periods=5).min()
    ll_lower = (post_min < prior_min).astype(float)
    out = (rej.shift(21).fillna(0) * ll_lower).where(rej.shift(21).notna(), np.nan)
    return out


def f17_tlbk_119_break_then_slope_flip_neg_21d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    be = ((above.shift(1) > 0.5) & (above < 0.5)).astype(float)
    sl = _rolling_slope(lc, 63, min_periods=21)
    flip_neg = ((sl < 0) & (sl.shift(21) >= 0)).astype(float)
    out = (be.shift(21).fillna(0) * flip_neg).where(be.shift(21).notna(), np.nan)
    return out


def f17_tlbk_120_cumulative_flip_events_score_63d_in_252d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    be = ((above.shift(1) > 0.5) & (above < 0.5)).astype(float).where(tl.notna() & tl.shift(1).notna(), np.nan)
    below = (lc < tl).astype(float)
    rb = (((below.shift(1) < 0.5) & (below > 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    rej = (((tl - lc).abs() <= 0.5 * rs) & (lc < tl)).astype(float) * (rb > 0).astype(float)
    rej = rej.where(rs.notna(), np.nan)
    out = (be + rej).rolling(252, min_periods=84).sum()
    return out


def f17_tlbk_121_r2_logclose_fit_63d(close: pd.Series) -> pd.Series:
    out = _rolling_r2(_safe_log(close), 63, min_periods=21)
    return out


def f17_tlbk_122_r2_logclose_fit_252d(close: pd.Series) -> pd.Series:
    out = _rolling_r2(_safe_log(close), 252, min_periods=84)
    return out


def f17_tlbk_123_r2_logclose_fit_504d(close: pd.Series) -> pd.Series:
    out = _rolling_r2(_safe_log(close), 504, min_periods=168)
    return out


def f17_tlbk_124_current_slope_regime_age_63d(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    sgn = np.sign(sl)
    block = (sgn != sgn.shift(1)).fillna(False).cumsum()
    out = sl.groupby(block).cumcount().astype(float).where(sl.notna(), np.nan)
    return out


def f17_tlbk_125_current_slope_regime_age_252d(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 252, min_periods=84)
    sgn = np.sign(sl)
    block = (sgn != sgn.shift(1)).fillna(False).cumsum()
    out = sl.groupby(block).cumcount().astype(float).where(sl.notna(), np.nan)
    return out


def f17_tlbk_126_touchpoint_count_quarter_sigma_63d_in_252d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    touch = ((lc - tl).abs() <= 0.25 * rs).astype(float).where(rs.notna(), np.nan)
    out = touch.rolling(252, min_periods=84).sum()
    return out


def f17_tlbk_127_distinct_touch_density_63d_in_252d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    touch = ((lc - tl).abs() <= 0.25 * rs).astype(float).where(rs.notna(), np.nan)
    out = touch.rolling(252, min_periods=84).sum() / 12.0
    return out


def f17_tlbk_128_trendline_hazard_inv_age_63d(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    sgn = np.sign(sl)
    block = (sgn != sgn.shift(1)).fillna(False).cumsum()
    age = sl.groupby(block).cumcount().astype(float)
    out = 1.0 / (age + 1.0).where(sl.notna(), np.nan)
    return out


def f17_tlbk_129_trendline_strength_composite_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    r2 = _rolling_r2(lc, 63, min_periods=21)
    sl = _rolling_slope(lc, 63, min_periods=21)
    ang = np.degrees(np.arctan(sl)).abs()
    out = (r2 * np.sign(sl) * ang).where(r2.notna() & sl.notna(), np.nan)
    return out


def f17_tlbk_130_trendline_strength_composite_252d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    r2 = _rolling_r2(lc, 252, min_periods=84)
    sl = _rolling_slope(lc, 252, min_periods=84)
    ang = np.degrees(np.arctan(sl)).abs()
    out = (r2 * np.sign(sl) * ang).where(r2.notna() & sl.notna(), np.nan)
    return out


def f17_tlbk_131_r2_decay_63d_in_252d_fit(close: pd.Series) -> pd.Series:
    r2 = _rolling_r2(_safe_log(close), 252, min_periods=84)
    out = r2 - r2.shift(63)
    return out


def f17_tlbk_132_r2_accel_21d_in_63d_fit(close: pd.Series) -> pd.Series:
    r2 = _rolling_r2(_safe_log(close), 63, min_periods=21)
    out = (r2 - r2.shift(21)) - (r2.shift(21) - r2.shift(42))
    return out


def f17_tlbk_133_touchpoint_mean_gap_63d_in_252d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    touch_idx = ((lc - tl).abs() <= 0.25 * rs).astype(float).where(rs.notna(), np.nan)
    cnt = touch_idx.rolling(252, min_periods=84).sum()
    out = 252.0 / cnt.replace(0, np.nan)
    return out


def f17_tlbk_134_high_r2_regime_indicator_63d(close: pd.Series) -> pd.Series:
    r2 = _rolling_r2(_safe_log(close), 63, min_periods=21)
    out = (r2 > 0.7).astype(float).where(r2.notna(), np.nan)
    return out


def f17_tlbk_135_frac_high_r2_252d_63d(close: pd.Series) -> pd.Series:
    r2 = _rolling_r2(_safe_log(close), 63, min_periods=21)
    hr = (r2 > 0.7).astype(float).where(r2.notna(), np.nan)
    out = hr.rolling(252, min_periods=84).mean()
    return out


def f17_tlbk_136_upside_breakout_event_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    ub = tl + rs
    above_ub = (lc > ub).astype(float)
    ev = ((above_ub.shift(1) < 0.5) & (above_ub > 0.5)).astype(float).where(rs.notna(), np.nan)
    out = ev
    return out


def f17_tlbk_137_downside_breakdown_event_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    lb = tl - rs
    below_lb = (lc < lb).astype(float)
    ev = ((below_lb.shift(1) < 0.5) & (below_lb > 0.5)).astype(float).where(rs.notna(), np.nan)
    out = ev
    return out


def f17_tlbk_138_breakout_minus_breakdown_count_252d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    ub = tl + rs; lb = tl - rs
    above_ub = (lc > ub).astype(float)
    below_lb = (lc < lb).astype(float)
    bo = ((above_ub.shift(1) < 0.5) & (above_ub > 0.5)).astype(float).where(rs.notna(), np.nan)
    bd = ((below_lb.shift(1) < 0.5) & (below_lb > 0.5)).astype(float).where(rs.notna(), np.nan)
    out = bo.rolling(252, min_periods=84).sum() - bd.rolling(252, min_periods=84).sum()
    return out


def f17_tlbk_139_breakout_max_gap_5d_post_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    ub = tl + rs
    gap = (lc - ub).clip(lower=0)
    above_ub = (lc > ub).astype(float)
    ev = ((above_ub.shift(1) < 0.5) & (above_ub > 0.5))
    max_gap_5 = gap.rolling(5, min_periods=1).max()
    out = max_gap_5.where(ev, np.nan)
    return out


def f17_tlbk_140_breakdown_max_gap_5d_post_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    lb = tl - rs
    gap = (lb - lc).clip(lower=0)
    below_lb = (lc < lb).astype(float)
    ev = ((below_lb.shift(1) < 0.5) & (below_lb > 0.5))
    max_gap_5 = gap.rolling(5, min_periods=1).max()
    out = max_gap_5.where(ev, np.nan)
    return out


def f17_tlbk_141_magnitude_asym_breakout_minus_breakdown_252d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    ub = tl + rs; lb = tl - rs
    bo_gap = (lc - ub).clip(lower=0)
    bd_gap = (lb - lc).clip(lower=0)
    out = bo_gap.rolling(252, min_periods=84).max() - bd_gap.rolling(252, min_periods=84).max()
    return out


def f17_tlbk_142_high_slope_then_flat_then_break_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 63, min_periods=21).abs()
    flat = (sl.shift(21) < sl.rolling(252, min_periods=84).median() * 0.3).astype(float)
    high_past = (sl.shift(42) > sl.rolling(252, min_periods=84).median() * 1.5).astype(float)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    break_e = ((above.shift(1) > 0.5) & (above < 0.5)).astype(float)
    out = (high_past * flat * break_e).where(sl.notna() & sl.shift(42).notna(), np.nan)
    return out


def f17_tlbk_143_long_durability_violent_break_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 63, min_periods=21)
    sgn = np.sign(sl)
    block = (sgn != sgn.shift(1)).fillna(False).cumsum()
    age = sl.groupby(block).cumcount().astype(float)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    be = ((above.shift(1) > 0.5) & (above < 0.5)).astype(float)
    gap_below = (tl - lc) / rs
    violent = (gap_below > 1.5).astype(float)
    old = (age.shift(1) > 126).astype(float)
    out = (be * violent * old).where(rs.notna() & age.notna(), np.nan)
    return out


def f17_tlbk_144_breakdown_share_of_events_252d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    ub = tl + rs; lb = tl - rs
    a_ub = (lc > ub).astype(float); b_lb = (lc < lb).astype(float)
    bo = ((a_ub.shift(1) < 0.5) & (a_ub > 0.5)).astype(float).where(rs.notna(), np.nan)
    bd = ((b_lb.shift(1) < 0.5) & (b_lb > 0.5)).astype(float).where(rs.notna(), np.nan)
    bo_c = bo.rolling(252, min_periods=84).sum()
    bd_c = bd.rolling(252, min_periods=84).sum()
    out = _safe_div(bd_c, (bo_c + bd_c + 1.0))
    return out


def f17_tlbk_145_sustained_breakdown_5d_indicator_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    lb = tl - rs
    out = ((lc < lb).astype(float).rolling(5, min_periods=5).min()).where(rs.notna(), np.nan)
    return out


def f17_tlbk_146_sustained_breakout_failure_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    ub = tl + rs
    above = (lc > ub).astype(float)
    short_pop = (above.rolling(3, min_periods=1).max() > 0.5).astype(float)
    back_in = (above < 0.5).astype(float)
    recent_pop = above.shift(1).rolling(3, min_periods=1).max()
    out = ((recent_pop > 0.5) & (back_in > 0.5)).astype(float).where(rs.notna(), np.nan)
    return out


def f17_tlbk_147_ramp_then_trendline_break_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    ramp = lc - lc.shift(63)
    big_ramp = (ramp > 0.5).astype(float)
    tl = _rolling_lr_endpoint(lc, 21, min_periods=7)
    above = (lc >= tl).astype(float)
    be = ((above.shift(1) > 0.5) & (above < 0.5)).astype(float)
    out = (big_ramp.shift(1) * be).where(big_ramp.shift(1).notna() & be.notna(), np.nan)
    return out


def f17_tlbk_148_break_with_r2_collapse_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    be = ((above.shift(1) > 0.5) & (above < 0.5)).astype(float)
    r2 = _rolling_r2(lc, 63, min_periods=21)
    dr2 = r2.shift(21) - r2
    coll = (dr2 > 0.3).astype(float)
    out = (be * coll).where(r2.notna() & r2.shift(21).notna(), np.nan)
    return out


def f17_tlbk_149_hampel_outlier_break_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    gap = (lc - tl).abs()
    med = gap.rolling(63, min_periods=21).median()
    mad = (gap - med).abs().rolling(63, min_periods=21).median()
    z = _safe_div(gap - med, 1.4826 * mad)
    above = (lc >= tl).astype(float)
    be = ((above.shift(1) > 0.5) & (above < 0.5)).astype(float)
    out = (be * (z > 3.0).astype(float)).where(z.notna(), np.nan)
    return out


def f17_tlbk_150_comp_terminal_break_multicriteria_63d(high: pd.Series, close: pd.Series) -> pd.Series:
    lc = _safe_log(close); lh = _safe_log(high)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    be = ((above.shift(1) > 0.5) & (above < 0.5)).astype(float)
    r2_prior = _rolling_r2(lc, 63, min_periods=21).shift(1)
    sl_prior = _rolling_slope(lc, 63, min_periods=21).shift(1)
    ang_prior = np.degrees(np.arctan(sl_prior)).abs()
    rmax = lh.rolling(252, min_periods=84).max().shift(1)
    at_high = (lh.shift(1) >= rmax - 0.05).astype(float)
    out = (be * (r2_prior > 0.5).astype(float) * (ang_prior > 30.0).astype(float) * at_high).where(r2_prior.notna() & at_high.notna(), np.nan)
    return out


# ============================================================
#                         REGISTRY 076_150 (base)
# ============================================================

TREND_LINE_BREAK_DYNAMICS_BASE_REGISTRY_076_150 = {
    "f17_tlbk_076_log_dist_close_to_trendline_21d": {"inputs": ["close"], "func": f17_tlbk_076_log_dist_close_to_trendline_21d},
    "f17_tlbk_077_log_dist_close_to_trendline_63d": {"inputs": ["close"], "func": f17_tlbk_077_log_dist_close_to_trendline_63d},
    "f17_tlbk_078_log_dist_close_to_trendline_252d": {"inputs": ["close"], "func": f17_tlbk_078_log_dist_close_to_trendline_252d},
    "f17_tlbk_079_log_dist_close_to_trendline_504d": {"inputs": ["close"], "func": f17_tlbk_079_log_dist_close_to_trendline_504d},
    "f17_tlbk_080_atr_dist_close_to_trendline_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_080_atr_dist_close_to_trendline_63d},
    "f17_tlbk_081_atr_dist_close_to_trendline_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_081_atr_dist_close_to_trendline_252d},
    "f17_tlbk_082_sigma_dist_close_to_trendline_63d": {"inputs": ["close"], "func": f17_tlbk_082_sigma_dist_close_to_trendline_63d},
    "f17_tlbk_083_sigma_dist_close_to_trendline_252d": {"inputs": ["close"], "func": f17_tlbk_083_sigma_dist_close_to_trendline_252d},
    "f17_tlbk_084_trendline_gap_zscore_63d_over_252d": {"inputs": ["close"], "func": f17_tlbk_084_trendline_gap_zscore_63d_over_252d},
    "f17_tlbk_085_trendline_gap_zscore_252d_over_504d": {"inputs": ["close"], "func": f17_tlbk_085_trendline_gap_zscore_252d_over_504d},
    "f17_tlbk_086_trendline_gap_pct_rank_63d_in_252d": {"inputs": ["close"], "func": f17_tlbk_086_trendline_gap_pct_rank_63d_in_252d},
    "f17_tlbk_087_high_minus_low_trendline_gap_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_087_high_minus_low_trendline_gap_252d},
    "f17_tlbk_088_trendline_gap_5d_accel_63d": {"inputs": ["close"], "func": f17_tlbk_088_trendline_gap_5d_accel_63d},
    "f17_tlbk_089_low_trendline_gap_log_close_63d": {"inputs": ["low", "close"], "func": f17_tlbk_089_low_trendline_gap_log_close_63d},
    "f17_tlbk_090_high_trendline_gap_log_close_63d": {"inputs": ["high", "close"], "func": f17_tlbk_090_high_trendline_gap_log_close_63d},
    "f17_tlbk_091_trendline_angle_deg_logclose_63d": {"inputs": ["close"], "func": f17_tlbk_091_trendline_angle_deg_logclose_63d},
    "f17_tlbk_092_trendline_angle_deg_logclose_252d": {"inputs": ["close"], "func": f17_tlbk_092_trendline_angle_deg_logclose_252d},
    "f17_tlbk_093_trendline_angle_deg_logclose_504d": {"inputs": ["close"], "func": f17_tlbk_093_trendline_angle_deg_logclose_504d},
    "f17_tlbk_094_angle_top_quintile_63d_in_252d": {"inputs": ["close"], "func": f17_tlbk_094_angle_top_quintile_63d_in_252d},
    "f17_tlbk_095_angle_zscore_63d_over_252d": {"inputs": ["close"], "func": f17_tlbk_095_angle_zscore_63d_over_252d},
    "f17_tlbk_096_angle_decel_21d_63d_slope": {"inputs": ["close"], "func": f17_tlbk_096_angle_decel_21d_63d_slope},
    "f17_tlbk_097_angle_decel_63d_252d_slope": {"inputs": ["close"], "func": f17_tlbk_097_angle_decel_63d_252d_slope},
    "f17_tlbk_098_angle_volatility_63d_over_63d": {"inputs": ["close"], "func": f17_tlbk_098_angle_volatility_63d_over_63d},
    "f17_tlbk_099_angle_above_45deg_indicator_63d": {"inputs": ["close"], "func": f17_tlbk_099_angle_above_45deg_indicator_63d},
    "f17_tlbk_100_frac_steep_angle_30deg_252d_63d": {"inputs": ["close"], "func": f17_tlbk_100_frac_steep_angle_30deg_252d_63d},
    "f17_tlbk_101_angle_ratio_21d_over_252d": {"inputs": ["close"], "func": f17_tlbk_101_angle_ratio_21d_over_252d},
    "f17_tlbk_102_angle_blowoff_indicator_21d_vs_252d_median": {"inputs": ["close"], "func": f17_tlbk_102_angle_blowoff_indicator_21d_vs_252d_median},
    "f17_tlbk_103_angle_range_max_min_63d": {"inputs": ["close"], "func": f17_tlbk_103_angle_range_max_min_63d},
    "f17_tlbk_104_angle_inversion_event_63d": {"inputs": ["close"], "func": f17_tlbk_104_angle_inversion_event_63d},
    "f17_tlbk_105_angle_21d_decay_rate": {"inputs": ["close"], "func": f17_tlbk_105_angle_21d_decay_rate},
    "f17_tlbk_106_broken_line_rejection_indicator_63d": {"inputs": ["close"], "func": f17_tlbk_106_broken_line_rejection_indicator_63d},
    "f17_tlbk_107_broken_line_rejection_indicator_252d": {"inputs": ["close"], "func": f17_tlbk_107_broken_line_rejection_indicator_252d},
    "f17_tlbk_108_rejection_drop_10d_63d": {"inputs": ["close"], "func": f17_tlbk_108_rejection_drop_10d_63d},
    "f17_tlbk_109_bars_break_to_first_rejection_63d": {"inputs": ["close"], "func": f17_tlbk_109_bars_break_to_first_rejection_63d},
    "f17_tlbk_110_rejection_count_63d_in_252d": {"inputs": ["close"], "func": f17_tlbk_110_rejection_count_63d_in_252d},
    "f17_tlbk_111_successful_rejection_rate_63d_in_252d": {"inputs": ["close"], "func": f17_tlbk_111_successful_rejection_rate_63d_in_252d},
    "f17_tlbk_112_broken_line_role_reversal_score_63d_in_252d": {"inputs": ["close"], "func": f17_tlbk_112_broken_line_role_reversal_score_63d_in_252d},
    "f17_tlbk_113_three_plus_rejections_in_63d_indicator": {"inputs": ["close"], "func": f17_tlbk_113_three_plus_rejections_in_63d_indicator},
    "f17_tlbk_114_rejection_drop_atr_units_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_114_rejection_drop_atr_units_63d},
    "f17_tlbk_115_first_rejection_after_21d_broken_63d": {"inputs": ["close"], "func": f17_tlbk_115_first_rejection_after_21d_broken_63d},
    "f17_tlbk_116_broken_high_line_rejection_63d": {"inputs": ["high", "close"], "func": f17_tlbk_116_broken_high_line_rejection_63d},
    "f17_tlbk_117_broken_low_line_acts_as_support_63d": {"inputs": ["low", "close"], "func": f17_tlbk_117_broken_low_line_acts_as_support_63d},
    "f17_tlbk_118_rejection_then_lower_low_63d": {"inputs": ["low", "close"], "func": f17_tlbk_118_rejection_then_lower_low_63d},
    "f17_tlbk_119_break_then_slope_flip_neg_21d_63d": {"inputs": ["close"], "func": f17_tlbk_119_break_then_slope_flip_neg_21d_63d},
    "f17_tlbk_120_cumulative_flip_events_score_63d_in_252d": {"inputs": ["close"], "func": f17_tlbk_120_cumulative_flip_events_score_63d_in_252d},
    "f17_tlbk_121_r2_logclose_fit_63d": {"inputs": ["close"], "func": f17_tlbk_121_r2_logclose_fit_63d},
    "f17_tlbk_122_r2_logclose_fit_252d": {"inputs": ["close"], "func": f17_tlbk_122_r2_logclose_fit_252d},
    "f17_tlbk_123_r2_logclose_fit_504d": {"inputs": ["close"], "func": f17_tlbk_123_r2_logclose_fit_504d},
    "f17_tlbk_124_current_slope_regime_age_63d": {"inputs": ["close"], "func": f17_tlbk_124_current_slope_regime_age_63d},
    "f17_tlbk_125_current_slope_regime_age_252d": {"inputs": ["close"], "func": f17_tlbk_125_current_slope_regime_age_252d},
    "f17_tlbk_126_touchpoint_count_quarter_sigma_63d_in_252d": {"inputs": ["close"], "func": f17_tlbk_126_touchpoint_count_quarter_sigma_63d_in_252d},
    "f17_tlbk_127_distinct_touch_density_63d_in_252d": {"inputs": ["close"], "func": f17_tlbk_127_distinct_touch_density_63d_in_252d},
    "f17_tlbk_128_trendline_hazard_inv_age_63d": {"inputs": ["close"], "func": f17_tlbk_128_trendline_hazard_inv_age_63d},
    "f17_tlbk_129_trendline_strength_composite_63d": {"inputs": ["close"], "func": f17_tlbk_129_trendline_strength_composite_63d},
    "f17_tlbk_130_trendline_strength_composite_252d": {"inputs": ["close"], "func": f17_tlbk_130_trendline_strength_composite_252d},
    "f17_tlbk_131_r2_decay_63d_in_252d_fit": {"inputs": ["close"], "func": f17_tlbk_131_r2_decay_63d_in_252d_fit},
    "f17_tlbk_132_r2_accel_21d_in_63d_fit": {"inputs": ["close"], "func": f17_tlbk_132_r2_accel_21d_in_63d_fit},
    "f17_tlbk_133_touchpoint_mean_gap_63d_in_252d": {"inputs": ["close"], "func": f17_tlbk_133_touchpoint_mean_gap_63d_in_252d},
    "f17_tlbk_134_high_r2_regime_indicator_63d": {"inputs": ["close"], "func": f17_tlbk_134_high_r2_regime_indicator_63d},
    "f17_tlbk_135_frac_high_r2_252d_63d": {"inputs": ["close"], "func": f17_tlbk_135_frac_high_r2_252d_63d},
    "f17_tlbk_136_upside_breakout_event_63d": {"inputs": ["close"], "func": f17_tlbk_136_upside_breakout_event_63d},
    "f17_tlbk_137_downside_breakdown_event_63d": {"inputs": ["close"], "func": f17_tlbk_137_downside_breakdown_event_63d},
    "f17_tlbk_138_breakout_minus_breakdown_count_252d_63d": {"inputs": ["close"], "func": f17_tlbk_138_breakout_minus_breakdown_count_252d_63d},
    "f17_tlbk_139_breakout_max_gap_5d_post_63d": {"inputs": ["close"], "func": f17_tlbk_139_breakout_max_gap_5d_post_63d},
    "f17_tlbk_140_breakdown_max_gap_5d_post_63d": {"inputs": ["close"], "func": f17_tlbk_140_breakdown_max_gap_5d_post_63d},
    "f17_tlbk_141_magnitude_asym_breakout_minus_breakdown_252d_63d": {"inputs": ["close"], "func": f17_tlbk_141_magnitude_asym_breakout_minus_breakdown_252d_63d},
    "f17_tlbk_142_high_slope_then_flat_then_break_63d": {"inputs": ["close"], "func": f17_tlbk_142_high_slope_then_flat_then_break_63d},
    "f17_tlbk_143_long_durability_violent_break_63d": {"inputs": ["close"], "func": f17_tlbk_143_long_durability_violent_break_63d},
    "f17_tlbk_144_breakdown_share_of_events_252d_63d": {"inputs": ["close"], "func": f17_tlbk_144_breakdown_share_of_events_252d_63d},
    "f17_tlbk_145_sustained_breakdown_5d_indicator_63d": {"inputs": ["close"], "func": f17_tlbk_145_sustained_breakdown_5d_indicator_63d},
    "f17_tlbk_146_sustained_breakout_failure_63d": {"inputs": ["close"], "func": f17_tlbk_146_sustained_breakout_failure_63d},
    "f17_tlbk_147_ramp_then_trendline_break_63d": {"inputs": ["close"], "func": f17_tlbk_147_ramp_then_trendline_break_63d},
    "f17_tlbk_148_break_with_r2_collapse_63d": {"inputs": ["close"], "func": f17_tlbk_148_break_with_r2_collapse_63d},
    "f17_tlbk_149_hampel_outlier_break_63d": {"inputs": ["close"], "func": f17_tlbk_149_hampel_outlier_break_63d},
    "f17_tlbk_150_comp_terminal_break_multicriteria_63d": {"inputs": ["high", "close"], "func": f17_tlbk_150_comp_terminal_break_multicriteria_63d},
}
