"""topping_pattern base 001-075 — Pipeline 1a-inverse short-side blowup family.

Hypothesis: classical topping patterns (rounding tops, double/triple tops,
H&S, broadening / wedges, failed breakouts) signal exhaustion at the peak.
PIT note: classical "pivot highs" require forward bars; we use right-anchored
rolling-max-as-pivot (bar where high equals K-bar trailing max) — captures
the same concept without leakage. 75 distinct hypotheses (continued in
__base__076_150.py for 150 total). SEP-only OHLCV.
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


# ============================================================
#                    FEATURES 001-075
# ============================================================

def f04_topp_001_dome_quadratic_coef_252d(close: pd.Series) -> pd.Series:
    """Quadratic coefficient of polyfit on close over 252d — negative = dome shape."""
    def _c2(w):
        if np.isnan(w).any():
            return np.nan
        try:
            return float(np.polyfit(np.arange(len(w)), w, 2)[0])
        except Exception:
            return np.nan
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_c2, raw=True)


def f04_topp_002_dome_quadratic_coef_63d(close: pd.Series) -> pd.Series:
    """Quadratic coefficient of polyfit on close over 63d — short-horizon dome."""
    def _c2(w):
        if np.isnan(w).any():
            return np.nan
        try:
            return float(np.polyfit(np.arange(len(w)), w, 2)[0])
        except Exception:
            return np.nan
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_c2, raw=True)


def f04_topp_003_dome_concave_R2_252d(close: pd.Series) -> pd.Series:
    """R² of concave-only quadratic fit (c2<0) on close over 252d; 0 if c2>=0."""
    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        try:
            coefs = np.polyfit(x, w, 2)
        except Exception:
            return np.nan
        if coefs[0] >= 0:
            return 0.0
        pred = np.polyval(coefs, x)
        ss = ((w - w.mean()) ** 2).sum()
        if ss == 0:
            return np.nan
        return float(max(0.0, 1.0 - ((w - pred) ** 2).sum() / ss))
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True)


def f04_topp_004_dome_concave_R2_63d(close: pd.Series) -> pd.Series:
    """R² of concave-only quadratic fit on close over 63d."""
    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        try:
            coefs = np.polyfit(x, w, 2)
        except Exception:
            return np.nan
        if coefs[0] >= 0:
            return 0.0
        pred = np.polyval(coefs, x)
        ss = ((w - w.mean()) ** 2).sum()
        if ss == 0:
            return np.nan
        return float(max(0.0, 1.0 - ((w - pred) ** 2).sum() / ss))
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_r2, raw=True)


def f04_topp_005_dome_apex_position_in_window_63d(close: pd.Series) -> pd.Series:
    """Position of fitted dome apex inside last 63 bars (0=start, 1=end). Apex near middle = mature top."""
    def _apex(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        try:
            coefs = np.polyfit(x, w, 2)
        except Exception:
            return np.nan
        if coefs[0] >= 0:
            return np.nan
        apex_x = -coefs[1] / (2.0 * coefs[0])
        return float(np.clip(apex_x / (len(w) - 1), 0.0, 1.0))
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_apex, raw=True)


def f04_topp_006_dome_apex_position_in_window_252d(close: pd.Series) -> pd.Series:
    """Position of fitted dome apex inside last 252 bars."""
    def _apex(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        try:
            coefs = np.polyfit(x, w, 2)
        except Exception:
            return np.nan
        if coefs[0] >= 0:
            return np.nan
        apex_x = -coefs[1] / (2.0 * coefs[0])
        return float(np.clip(apex_x / (len(w) - 1), 0.0, 1.0))
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_apex, raw=True)


def f04_topp_007_dome_apex_close_proximity_63d(close: pd.Series) -> pd.Series:
    """1 - |apex_position - 0.5| × 2 over 63d — peaks at 1.0 when apex is mid-window."""
    def _prox(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        try:
            coefs = np.polyfit(x, w, 2)
        except Exception:
            return np.nan
        if coefs[0] >= 0:
            return 0.0
        apex_x = -coefs[1] / (2.0 * coefs[0])
        apex_pos = float(np.clip(apex_x / (len(w) - 1), 0.0, 1.0))
        return float(1.0 - abs(apex_pos - 0.5) * 2.0)
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_prox, raw=True)


def f04_topp_008_log_close_curvature_change_63d_vs_252d(close: pd.Series) -> pd.Series:
    """63d log-price curvature minus 252d log-price curvature — short-horizon dome forming."""
    lp = _safe_log(close)
    def _c2(w):
        if np.isnan(w).any():
            return np.nan
        try:
            return float(np.polyfit(np.arange(len(w)), w, 2)[0])
        except Exception:
            return np.nan
    c63 = lp.rolling(QDAYS, min_periods=MDAYS).apply(_c2, raw=True)
    c252 = lp.rolling(YDAYS, min_periods=QDAYS).apply(_c2, raw=True)
    return c63 - c252


def f04_topp_009_close_diff_sign_change_count_21d_over_63d(close: pd.Series) -> pd.Series:
    """Count of sign flips in close.diff(21) over 63d — meandering top behavior."""
    s = np.sign(close.diff(MDAYS))
    flip = (s != s.shift(1)).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum()


def f04_topp_010_momentum_peak_offset_63d(close: pd.Series) -> pd.Series:
    """Bars between price 63d-argmax and 21d-ROC 63d-argmax — momentum peak leading price peak."""
    roc = close.pct_change(MDAYS)
    def _pidx(w):
        if np.isnan(w).any():
            return np.nan
        return float(int(np.argmax(w)))
    p_arg = close.rolling(QDAYS, min_periods=MDAYS).apply(_pidx, raw=True)
    m_arg = roc.rolling(QDAYS, min_periods=MDAYS).apply(_pidx, raw=True)
    return m_arg - p_arg


def f04_topp_011_smoothed_close_curvature_mean_252d(close: pd.Series) -> pd.Series:
    """Mean of (SMA21 - 2*SMA21.shift(11) + SMA21.shift(22)) over 252d — discrete second-derivative of smoothed close."""
    s = close.rolling(MDAYS, min_periods=WDAYS).mean()
    d2 = s - 2.0 * s.shift(11) + s.shift(22)
    return d2.rolling(YDAYS, min_periods=QDAYS).mean()


def f04_topp_012_dome_residual_max_252d(close: pd.Series) -> pd.Series:
    """Max negative residual (below linear fit) of close polyfit-2 over 252d, scaled by close."""
    def _resid(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        try:
            coefs = np.polyfit(x, w, 1)
        except Exception:
            return np.nan
        pred = np.polyval(coefs, x)
        resid = w - pred
        return float(resid.max())
    raw = close.rolling(YDAYS, min_periods=QDAYS).apply(_resid, raw=True)
    return _safe_div(raw, close)


def f04_topp_013_sma_inflection_distance_63d(close: pd.Series) -> pd.Series:
    """Bars since SMA63's discrete second-derivative last crossed zero (inflection age)."""
    s = close.rolling(QDAYS, min_periods=MDAYS).mean()
    d2 = s - 2.0 * s.shift(1) + s.shift(2)
    cross = (np.sign(d2) != np.sign(d2.shift(1)))
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last = pos.where(cross).ffill()
    return pos - last


def f04_topp_014_close_distribution_skew_around_window_mid_252d(close: pd.Series) -> pd.Series:
    """Skewness of (close - 252d-mean) over 252d — negative skew = peak near end of distribution."""
    def _skew_centered(w):
        if np.isnan(w).any():
            return np.nan
        c = w - w.mean()
        sd = c.std()
        if sd == 0:
            return np.nan
        return float(((c) ** 3).mean() / (sd ** 3))
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_skew_centered, raw=True)


def f04_topp_015_dome_height_to_age_ratio_252d(close: pd.Series) -> pd.Series:
    """(252d max(close) - close) × bars-since-252d-max — peaked dome aging."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    def _pa(w):
        return float((len(w) - 1) - int(np.argmax(w)))
    pa = close.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    return _safe_div((rmax - close) * pa, close)


def f04_topp_016_double_top_proximity_score_252d(high: pd.Series) -> pd.Series:
    """1 - |2nd-highest high in 252d / 252d-max - 1|, clipped to [0,1] — close-but-second-pivot proximity."""
    def _dt(w):
        if np.isnan(w).any() or len(w) < 5:
            return np.nan
        srt = np.sort(w)[-5:]
        mx = srt[-1]
        if mx == 0:
            return np.nan
        second = srt[-2]
        return float(np.clip(1.0 - abs(second / mx - 1.0) * 50.0, 0.0, 1.0))
    return high.rolling(YDAYS, min_periods=QDAYS).apply(_dt, raw=True)


def f04_topp_017_top2_pivot_price_match_pct_252d(high: pd.Series) -> pd.Series:
    """100 × (top-2 high / top-1 high) over 252d — closer to 100 = stronger double-top."""
    def _ratio(w):
        if np.isnan(w).any() or len(w) < 2:
            return np.nan
        srt = np.sort(w)
        if srt[-1] == 0:
            return np.nan
        return float(100.0 * srt[-2] / srt[-1])
    return high.rolling(YDAYS, min_periods=QDAYS).apply(_ratio, raw=True)


def f04_topp_018_top2_pivot_time_separation_252d(high: pd.Series) -> pd.Series:
    """Bars between argmax of high and argmax-of-high-excluding-argmax (top-2 pivot) over 252d."""
    def _sep(w):
        if np.isnan(w).any() or len(w) < 2:
            return np.nan
        a = int(np.argmax(w))
        w2 = w.copy()
        w2[a] = -np.inf
        b = int(np.argmax(w2))
        return float(abs(a - b))
    return high.rolling(YDAYS, min_periods=QDAYS).apply(_sep, raw=True)


def f04_topp_019_double_top_volume_divergence_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of (volume on 2nd-peak day) / (volume on 1st-peak day) over 252d — <1 = bearish divergence."""
    def _vd(w_h, w_v):
        if np.isnan(w_h).any() or len(w_h) < 2:
            return np.nan
        a = int(np.argmax(w_h))
        w2 = w_h.copy(); w2[a] = -np.inf
        b = int(np.argmax(w2))
        if w_v[a] == 0:
            return np.nan
        return float(w_v[b] / w_v[a])
    return pd.Series(
        [
            _vd(high.iloc[max(0, i - YDAYS + 1): i + 1].values, volume.iloc[max(0, i - YDAYS + 1): i + 1].values)
            if i >= QDAYS - 1 else np.nan
            for i in range(len(high))
        ],
        index=high.index,
    )


def f04_topp_020_double_top_neckline_position_proximity_252d(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Close vs neckline (min low between top-1 and top-2 in 252d) — close near = near breakdown."""
    def _nb(w_c, w_l, w_h):
        if np.isnan(w_h).any() or len(w_h) < 5:
            return np.nan
        a = int(np.argmax(w_h))
        w2 = w_h.copy(); w2[a] = -np.inf
        b = int(np.argmax(w2))
        lo, hi = min(a, b), max(a, b)
        if hi - lo < 2:
            return np.nan
        neckline = w_l[lo:hi + 1].min()
        if neckline == 0:
            return np.nan
        return float(w_c[-1] / neckline - 1.0)
    return pd.Series(
        [
            _nb(close.iloc[max(0, i - YDAYS + 1): i + 1].values,
                low.iloc[max(0, i - YDAYS + 1): i + 1].values,
                high.iloc[max(0, i - YDAYS + 1): i + 1].values)
            if i >= QDAYS - 1 else np.nan
            for i in range(len(close))
        ],
        index=close.index,
    )


def f04_topp_021_pivot_high_cluster_count_at_top_252d(high: pd.Series) -> pd.Series:
    """Count of bars in 252d where high >= 0.97 × 252d-max(high) — top-cluster size."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (high >= 0.97 * rmax).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f04_topp_022_triple_top_pattern_score_252d(high: pd.Series) -> pd.Series:
    """Top-3 average / top-1 high over 252d — closer to 1 = three similar highs."""
    def _t3(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        srt = np.sort(w)
        if srt[-1] == 0:
            return np.nan
        return float(srt[-3:].mean() / srt[-1])
    return high.rolling(YDAYS, min_periods=QDAYS).apply(_t3, raw=True)


def f04_topp_023_top3_pivot_max_spread_pct_252d(high: pd.Series) -> pd.Series:
    """(top-1 - top-3) / top-1 over 252d — small spread = tight triple top."""
    def _spr(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        srt = np.sort(w)
        if srt[-1] == 0:
            return np.nan
        return float((srt[-1] - srt[-3]) / srt[-1])
    return high.rolling(YDAYS, min_periods=QDAYS).apply(_spr, raw=True)


def f04_topp_024_pivot_high_cluster_age_252d(high: pd.Series) -> pd.Series:
    """Bars between the earliest and latest member of the top-cluster (>=0.97×252d-max(high)) in 252d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    in_cluster = (high >= 0.97 * rmax).astype(int)
    def _age(w):
        if np.isnan(w).any():
            return np.nan
        idx = np.where(w > 0.5)[0]
        if len(idx) < 2:
            return 0.0
        return float(idx[-1] - idx[0])
    return in_cluster.rolling(YDAYS, min_periods=QDAYS).apply(_age, raw=True)


def f04_topp_025_pivot_high_cluster_spread_pct_252d(high: pd.Series) -> pd.Series:
    """Max-minus-min within the top-cluster (>=0.97×252d-max(high)) / 252d-max(high)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    def _sp(w_h, w_m):
        if np.isnan(w_h).any():
            return np.nan
        members = w_h[w_h >= 0.97 * w_m[-1]]
        if len(members) < 2:
            return 0.0
        if w_m[-1] == 0:
            return np.nan
        return float((members.max() - members.min()) / w_m[-1])
    pairs = pd.concat([high, rmax], axis=1).rolling(YDAYS, min_periods=QDAYS)
    # Cannot directly apply on multi-column rolling cleanly — fallback to apply over high with extra arg
    res = pd.Series(np.nan, index=high.index)
    h_vals = high.values
    m_vals = rmax.values
    for i in range(QDAYS - 1, len(h_vals)):
        w = h_vals[max(0, i - YDAYS + 1): i + 1]
        mx = m_vals[i]
        if np.isnan(w).any() or np.isnan(mx) or mx == 0:
            continue
        members = w[w >= 0.97 * mx]
        if len(members) < 2:
            res.iloc[i] = 0.0
            continue
        res.iloc[i] = (members.max() - members.min()) / mx
    return res


def f04_topp_026_last_pivot_high_vs_recent_pivot_high_ratio_252d(high: pd.Series) -> pd.Series:
    """Latest high above 0.97×252d-max divided by latest 252d-max — late-cluster price decay."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    cluster = high.where(high >= 0.97 * rmax)
    last_cluster = cluster.ffill()
    return _safe_div(last_cluster, rmax)


def f04_topp_027_secondary_peak_lower_than_primary_count_252d(high: pd.Series) -> pd.Series:
    """Count of 21d-rolling-max bars in 252d that are NOT also 252d-max — secondary peaks below primary."""
    rmax_21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    rmax_252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    flag = ((high == rmax_21) & (high < rmax_252)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f04_topp_028_retest_failed_count_at_252d_high_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count over 63d of new-252d-highs that failed (close < open or close < prior bar's close)."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high > prior_max
    fail = close < close.shift(1)
    return (new_high & fail).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f04_topp_029_retest_succeeded_count_at_252d_high_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count over 63d of new-252d-highs that held (close > prior close)."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high > prior_max
    hold = close > close.shift(1)
    return (new_high & hold).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f04_topp_030_m_pattern_score_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """1 - |0.5 - close_position_in_252d_range| × 2, weighted by top-2 spread tightness — composite M-detection."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = high.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    def _t2(w):
        if np.isnan(w).any() or len(w) < 2:
            return np.nan
        srt = np.sort(w)
        if srt[-1] == 0:
            return np.nan
        return float(srt[-2] / srt[-1])
    t2_tightness = high.rolling(YDAYS, min_periods=QDAYS).apply(_t2, raw=True)
    return (1.0 - (pos - 0.5).abs() * 2.0).clip(lower=0) * t2_tightness


def f04_topp_031_head_shoulders_left_high_ratio_252d(high: pd.Series) -> pd.Series:
    """Max high in first third / max high in middle third of 252d window — left-shoulder height ratio."""
    third = YDAYS // 3
    left = high.shift(YDAYS - third).rolling(third, min_periods=WDAYS).max()
    head = high.shift(YDAYS - 2 * third).rolling(third, min_periods=WDAYS).max()
    return _safe_div(left, head)


def f04_topp_032_head_shoulders_right_high_ratio_252d(high: pd.Series) -> pd.Series:
    """Max high in last third / max high in middle third of 252d window — right-shoulder height ratio."""
    third = YDAYS // 3
    right = high.rolling(third, min_periods=WDAYS).max()
    head = high.shift(YDAYS - 2 * third).rolling(third, min_periods=WDAYS).max()
    return _safe_div(right, head)


def f04_topp_033_head_shoulders_symmetry_score_252d(high: pd.Series) -> pd.Series:
    """1 - |left-shoulder ratio - right-shoulder ratio| — high = symmetric H&S."""
    third = YDAYS // 3
    left = high.shift(YDAYS - third).rolling(third, min_periods=WDAYS).max()
    head = high.shift(YDAYS - 2 * third).rolling(third, min_periods=WDAYS).max()
    right = high.rolling(third, min_periods=WDAYS).max()
    l_ratio = _safe_div(left, head)
    r_ratio = _safe_div(right, head)
    return 1.0 - (l_ratio - r_ratio).abs()


def f04_topp_034_HS_head_above_shoulders_score_252d(high: pd.Series) -> pd.Series:
    """Head height minus avg(left,right) shoulder height, scaled by head — distinctive head."""
    third = YDAYS // 3
    left = high.shift(YDAYS - third).rolling(third, min_periods=WDAYS).max()
    head = high.shift(YDAYS - 2 * third).rolling(third, min_periods=WDAYS).max()
    right = high.rolling(third, min_periods=WDAYS).max()
    avg_sh = (left + right) / 2.0
    return _safe_div(head - avg_sh, head)


def f04_topp_035_HS_neckline_break_distance_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """(close - min(low) in middle third) / close — close vs neckline (min low between shoulders)."""
    third = YDAYS // 3
    neckline = low.shift(YDAYS - 2 * third).rolling(third, min_periods=WDAYS).min()
    return _safe_div(close - neckline, close)


def f04_topp_036_HS_head_max_close_proximity_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """close / max-high-in-middle-third(252d) — proximity to H&S head; <1 confirms head passed."""
    third = YDAYS // 3
    head = high.shift(YDAYS - 2 * third).rolling(third, min_periods=WDAYS).max()
    return _safe_div(close, head)


def f04_topp_037_HS_volume_pattern_score_252d(volume: pd.Series, high: pd.Series) -> pd.Series:
    """log(max-volume left-third / max-volume right-third) when high pattern holds — heavier left vol = bearish."""
    third = YDAYS // 3
    left_v = volume.shift(YDAYS - third).rolling(third, min_periods=WDAYS).max()
    right_v = volume.rolling(third, min_periods=WDAYS).max()
    return _safe_log(_safe_div(left_v, right_v))


def f04_topp_038_inverse_HS_no_pattern_count_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars in 252 where left high > head high (inverse H&S — bullish, not topping)."""
    third = YDAYS // 3
    left = high.shift(YDAYS - third).rolling(third, min_periods=WDAYS).max()
    head = high.shift(YDAYS - 2 * third).rolling(third, min_periods=WDAYS).max()
    flag = (left > head).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f04_topp_039_HS_neckline_age_score_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since close last touched neckline (= 252d window min low in middle third) — pattern age."""
    third = YDAYS // 3
    neckline = low.shift(YDAYS - 2 * third).rolling(third, min_periods=WDAYS).min()
    touched = (close <= neckline * 1.005) & (close >= neckline * 0.995)
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last = pos.where(touched).ffill()
    return pos - last


def f04_topp_040_shoulder_high_count_within_5pct_252d(high: pd.Series) -> pd.Series:
    """Count of bars in 252 with high within 5% of 252d-max in left or right thirds (shoulder candidates)."""
    third = YDAYS // 3
    rmax_252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high >= 0.95 * rmax_252)
    # mark bars in left third (lag YDAYS-third..YDAYS) and right third (0..third) — approximate via day-since-peak
    def _pa(w):
        return float((len(w) - 1) - int(np.argmax(w)))
    pa = high.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    in_outer = ((pa < third) | (pa > 2 * third)).astype(float)
    return (near.astype(float) * in_outer).rolling(YDAYS, min_periods=QDAYS).sum()


def f04_topp_041_head_proximity_to_252d_max_score(high: pd.Series) -> pd.Series:
    """Max high in middle third of 252d window / 252d-max — head needs to be the global max."""
    third = YDAYS // 3
    head = high.shift(YDAYS - 2 * third).rolling(third, min_periods=WDAYS).max()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(head, rmax)


def f04_topp_042_head_proximity_to_close_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Close / head (middle-third max high) — proximity of current close to historical H&S head."""
    third = YDAYS // 3
    head = high.shift(YDAYS - 2 * third).rolling(third, min_periods=WDAYS).max()
    return _safe_div(close, head)


def f04_topp_043_right_shoulder_age_score_252d(high: pd.Series) -> pd.Series:
    """Bars since right-shoulder high (max high in last third) — recent shoulder = pattern in progress."""
    third = YDAYS // 3
    def _pa(w):
        return float((len(w) - 1) - int(np.argmax(w)))
    return high.rolling(third, min_periods=WDAYS).apply(_pa, raw=True)


def f04_topp_044_shoulder_count_252d(high: pd.Series) -> pd.Series:
    """Count of 21d-rolling-max touches that are NOT the 252d max — generic shoulder count."""
    rmax_21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    rmax_252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((high == rmax_21) & (high < 0.98 * rmax_252)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f04_topp_045_HS_completion_proximity_score_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite: HS_symmetry × HS_head_distinct × (close near neckline) — overall completion."""
    third = YDAYS // 3
    left = high.shift(YDAYS - third).rolling(third, min_periods=WDAYS).max()
    head = high.shift(YDAYS - 2 * third).rolling(third, min_periods=WDAYS).max()
    right = high.rolling(third, min_periods=WDAYS).max()
    sym = 1.0 - (_safe_div(left, head) - _safe_div(right, head)).abs()
    head_dist = _safe_div(head - (left + right) / 2.0, head).clip(lower=0)
    neckline = low.shift(YDAYS - 2 * third).rolling(third, min_periods=WDAYS).min()
    nb = 1.0 - (_safe_div(close, neckline) - 1.0).abs() * 5.0
    return sym * head_dist * nb.clip(lower=0)


def f04_topp_046_broadening_top_highs_slope_252d(high: pd.Series) -> pd.Series:
    """Slope of running max of high over 252d — positive = highs expanding (broadening top)."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    return _rolling_slope(rmax, YDAYS)


def f04_topp_047_broadening_top_lows_slope_252d(low: pd.Series) -> pd.Series:
    """Slope of running min of low over 252d — negative = lows declining (broadening top)."""
    rmin = low.rolling(MDAYS, min_periods=WDAYS).min()
    return _rolling_slope(rmin, YDAYS)


def f04_topp_048_broadening_top_pattern_score_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """max(0, slope of 21d-max(high)) × max(0, -slope of 21d-min(low)) — score peaks when both diverge."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    rmin = low.rolling(MDAYS, min_periods=WDAYS).min()
    sh = _rolling_slope(rmax, YDAYS).clip(lower=0)
    sl = (-_rolling_slope(rmin, YDAYS)).clip(lower=0)
    return sh * sl


def f04_topp_049_megaphone_range_growth_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Last 21d (max(high)-min(low)) divided by first 21d of 252d window — megaphone range expansion."""
    rng_recent = (high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min())
    rng_old = rng_recent.shift(YDAYS - MDAYS)
    return _safe_div(rng_recent, rng_old)


def f04_topp_050_rising_wedge_pattern_score_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """(slope of highs) - (slope of lows) — negative = lows rising faster than highs (rising wedge)."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    rmin = low.rolling(MDAYS, min_periods=WDAYS).min()
    return _rolling_slope(rmax, YDAYS) - _rolling_slope(rmin, YDAYS)


def f04_topp_051_rising_wedge_convergence_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Last 21d range divided by first 21d range — <1 = narrowing wedge."""
    rng_recent = (high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min())
    rng_old = rng_recent.shift(YDAYS - MDAYS)
    return _safe_div(rng_recent, rng_old)


def f04_topp_052_falling_wedge_pattern_score_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """(slope of lows) - (slope of highs) over 63d — positive = falling wedge (rare top signal)."""
    rmax = high.rolling(WDAYS, min_periods=2).max()
    rmin = low.rolling(WDAYS, min_periods=2).min()
    return _rolling_slope(rmin, QDAYS) - _rolling_slope(rmax, QDAYS)


def f04_topp_053_bearish_pennant_score_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Inverse of 63d range standard deviation (smaller = pennant tightening), normalized."""
    rng = high - low
    sd = rng.rolling(QDAYS, min_periods=MDAYS).std()
    m = rng.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(1.0, 1.0 + sd / m.replace(0, np.nan))


def f04_topp_054_bearish_flag_top_score_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Sharp 21d rally then 21d sideways: (21d-return shift 21) - |21d return now| — flag-pattern proxy."""
    r21 = _safe_log(close).diff(MDAYS)
    return r21.shift(MDAYS) - r21.abs()


def f04_topp_055_higher_lows_lower_highs_count_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars in 252 where low > prior low AND high < prior high — coiling pattern."""
    flag = ((low > low.shift(1)) & (high < high.shift(1))).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f04_topp_056_highs_volatility_growth_252d(high: pd.Series) -> pd.Series:
    """Last 63d std of 21d-max(high) / first 63d std — volatility expansion of highs."""
    rh = high.rolling(MDAYS, min_periods=WDAYS).max()
    sd_recent = rh.rolling(QDAYS, min_periods=MDAYS).std()
    sd_old = sd_recent.shift(YDAYS - QDAYS)
    return _safe_div(sd_recent, sd_old)


def f04_topp_057_lows_volatility_growth_252d(low: pd.Series) -> pd.Series:
    """Last 63d std of 21d-min(low) / first 63d std — volatility expansion of lows."""
    rl = low.rolling(MDAYS, min_periods=WDAYS).min()
    sd_recent = rl.rolling(QDAYS, min_periods=MDAYS).std()
    sd_old = sd_recent.shift(YDAYS - QDAYS)
    return _safe_div(sd_recent, sd_old)


def f04_topp_058_trading_range_compression_to_breakout_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21 today / 252d-median ATR21 — compression-to-expansion ratio (bottom = top setup)."""
    atr = _atr(high, low, close, MDAYS)
    return _safe_div(atr, atr.rolling(YDAYS, min_periods=QDAYS).median())


def f04_topp_059_range_volatility_collapse_at_top_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d ATR / 63d ATR — <1 = volatility collapsing while near top."""
    atr_21 = _atr(high, low, close, MDAYS)
    atr_63 = _atr(high, low, close, QDAYS)
    return _safe_div(atr_21, atr_63)


def f04_topp_060_diamond_top_pattern_score_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """First 63d range expansion × last 63d range compression — diamond top topology."""
    rng = high - low
    early = rng.shift(YDAYS - QDAYS).rolling(QDAYS, min_periods=MDAYS).mean()
    mid = rng.shift(YDAYS - 2 * QDAYS).rolling(QDAYS, min_periods=MDAYS).mean()
    late = rng.rolling(QDAYS, min_periods=MDAYS).mean()
    expand = _safe_div(mid, early)
    contract = _safe_div(mid, late)
    return expand * contract


def f04_topp_061_new_252d_high_then_fail_count_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count over 63d of bars setting a new 252d-high but closing below their own open or prior close."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high > prior_max
    fail = close < close.shift(1)
    return (new_high & fail).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f04_topp_062_new_252d_high_reverse_within_5d_count_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count over 63d of new-252d-highs (5d ago) where close has since fallen below that day's close."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high_5_ago = (high.shift(WDAYS) > prior_max.shift(WDAYS))
    fail_now = close < close.shift(WDAYS)
    return (new_high_5_ago & fail_now).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f04_topp_063_failed_breakout_after_consolidation_count_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count over 252d of: prior bar was a new high, preceded by consolidation, current close drops."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high > prior_max
    r = _safe_log(close).diff().abs()
    tight = r.rolling(MDAYS, min_periods=WDAYS).std()
    norm = r.rolling(QDAYS, min_periods=MDAYS).std()
    was_consol = (tight < 0.5 * norm).shift(1)
    flag = (new_high.shift(1) & was_consol.shift(1) & (close < close.shift(1))).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f04_topp_064_breakout_failure_severity_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Mean of -(close - prior 252d-high) / prior 252d-high on new-high-then-fail bars, over 252d."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high > prior_max
    fail = close < close.shift(1)
    severity = (-(close - prior_max) / prior_max.replace(0, np.nan)).where(new_high & fail)
    return severity.rolling(YDAYS, min_periods=QDAYS).mean()


def f04_topp_065_false_breakout_score_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars where high > 21d prior max but close < 21d prior min, over 252d."""
    prior_max_21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    prior_min_21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    flag = ((high > prior_max_21) & (close < prior_min_21)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f04_topp_066_bull_trap_count_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count over 63d of bars where high > prior 63d-high but close <= prior close (intraday bull trap)."""
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    flag = ((high > prior_max) & (close <= close.shift(1))).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f04_topp_067_pivot_high_failure_count_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count over 252d of bars where high == 21d-rolling-max (right-anchored pivot) and close < open of bar."""
    rmax_21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    pivot = high == rmax_21
    weak = close < close.shift(1)
    return (pivot & weak).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f04_topp_068_close_in_lower_half_at_new_21d_high_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count over 21d of new-21d-highs where close sits in lower half of bar range."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    pivot = high == rmax
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    weak = pos < 0.5
    return (pivot & weak).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f04_topp_069_outside_bar_at_252d_high_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Outside-bar (engulfs prior bar's range) that also touches 252d-high, over last 21 bars."""
    outside = (high > high.shift(1)) & (low < low.shift(1))
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = (high >= 0.99 * rmax)
    return (outside & at_top).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f04_topp_070_reversal_bar_at_252d_high_score_21d(open_: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite: at-top × bearish-body × long-upper-wick, summed over 21 bars."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = (high >= 0.99 * rmax)
    body_bear = close < open_
    rng = (high - low).replace(0, np.nan)
    upper = high - close.where(close > open_, open_)
    long_wick = (upper / rng) > 0.5
    return (at_top & body_bear & long_wick).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f04_topp_071_breakout_then_below_breakout_level_count_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count over 63d of bars where 5d-ago made a new 21d high but today's close < that high."""
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    bo_5_ago = (high.shift(WDAYS) > prior_max.shift(WDAYS))
    failed = close < high.shift(WDAYS)
    return (bo_5_ago & failed).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f04_topp_072_distribution_after_breakout_count_252d(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of new-252d-high bars in 252 where next 5d mean close < bar close AND volume above 252d median."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high.shift(WDAYS) > prior_max.shift(WDAYS)
    # PIT: look at lagged-5 new-high event, evaluate close drift since
    drift = close - close.shift(WDAYS)
    hi_vol = volume.shift(WDAYS) > volume.rolling(YDAYS, min_periods=QDAYS).median().shift(WDAYS)
    flag = (new_high & (drift < 0) & hi_vol).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f04_topp_073_breakout_volume_lacking_count_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of new-252d-high bars where bar volume < 252d-median volume — no-confirmation breakouts."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high > prior_max
    med_v = volume.rolling(YDAYS, min_periods=QDAYS).median()
    weak_v = volume < med_v
    return (new_high & weak_v).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f04_topp_074_breakout_failure_to_recover_count_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of new-252d-highs where in the next 21d (lagged) close never re-touched the high level."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high.shift(MDAYS) > prior_max.shift(MDAYS)
    # In the 21 bars since, did close get back to that high?
    recovered = (close.rolling(MDAYS, min_periods=WDAYS).max() >= high.shift(MDAYS))
    flag = (new_high & ~recovered).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f04_topp_075_reversal_signal_at_top_composite_21d(open_: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum over 21d of any single-bar reversal flag at the 252d top (outside, hammer-inverted, doji at top, weak close)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.98 * rmax
    rng = (high - low).replace(0, np.nan)
    body = (close - open_).abs()
    upper = high - close.where(close > open_, open_)
    pos = (close - low) / rng
    outside = (high > high.shift(1)) & (low < low.shift(1))
    inverted_hammer = ((upper / rng) > 0.6) & ((body / rng) < 0.3)
    doji = (body / rng) < 0.1
    weak_close = pos < (1.0 / 3.0)
    flag = (near & (outside | inverted_hammer | doji | weak_close)).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


# ============================================================
#                        REGISTRY
# ============================================================

TOPPING_PATTERN_BASE_REGISTRY_001_075 = {
    "f04_topp_001_dome_quadratic_coef_252d": {"inputs": ["close"], "func": f04_topp_001_dome_quadratic_coef_252d},
    "f04_topp_002_dome_quadratic_coef_63d": {"inputs": ["close"], "func": f04_topp_002_dome_quadratic_coef_63d},
    "f04_topp_003_dome_concave_R2_252d": {"inputs": ["close"], "func": f04_topp_003_dome_concave_R2_252d},
    "f04_topp_004_dome_concave_R2_63d": {"inputs": ["close"], "func": f04_topp_004_dome_concave_R2_63d},
    "f04_topp_005_dome_apex_position_in_window_63d": {"inputs": ["close"], "func": f04_topp_005_dome_apex_position_in_window_63d},
    "f04_topp_006_dome_apex_position_in_window_252d": {"inputs": ["close"], "func": f04_topp_006_dome_apex_position_in_window_252d},
    "f04_topp_007_dome_apex_close_proximity_63d": {"inputs": ["close"], "func": f04_topp_007_dome_apex_close_proximity_63d},
    "f04_topp_008_log_close_curvature_change_63d_vs_252d": {"inputs": ["close"], "func": f04_topp_008_log_close_curvature_change_63d_vs_252d},
    "f04_topp_009_close_diff_sign_change_count_21d_over_63d": {"inputs": ["close"], "func": f04_topp_009_close_diff_sign_change_count_21d_over_63d},
    "f04_topp_010_momentum_peak_offset_63d": {"inputs": ["close"], "func": f04_topp_010_momentum_peak_offset_63d},
    "f04_topp_011_smoothed_close_curvature_mean_252d": {"inputs": ["close"], "func": f04_topp_011_smoothed_close_curvature_mean_252d},
    "f04_topp_012_dome_residual_max_252d": {"inputs": ["close"], "func": f04_topp_012_dome_residual_max_252d},
    "f04_topp_013_sma_inflection_distance_63d": {"inputs": ["close"], "func": f04_topp_013_sma_inflection_distance_63d},
    "f04_topp_014_close_distribution_skew_around_window_mid_252d": {"inputs": ["close"], "func": f04_topp_014_close_distribution_skew_around_window_mid_252d},
    "f04_topp_015_dome_height_to_age_ratio_252d": {"inputs": ["close"], "func": f04_topp_015_dome_height_to_age_ratio_252d},
    "f04_topp_016_double_top_proximity_score_252d": {"inputs": ["high"], "func": f04_topp_016_double_top_proximity_score_252d},
    "f04_topp_017_top2_pivot_price_match_pct_252d": {"inputs": ["high"], "func": f04_topp_017_top2_pivot_price_match_pct_252d},
    "f04_topp_018_top2_pivot_time_separation_252d": {"inputs": ["high"], "func": f04_topp_018_top2_pivot_time_separation_252d},
    "f04_topp_019_double_top_volume_divergence_252d": {"inputs": ["high", "volume"], "func": f04_topp_019_double_top_volume_divergence_252d},
    "f04_topp_020_double_top_neckline_position_proximity_252d": {"inputs": ["close", "low", "high"], "func": f04_topp_020_double_top_neckline_position_proximity_252d},
    "f04_topp_021_pivot_high_cluster_count_at_top_252d": {"inputs": ["high"], "func": f04_topp_021_pivot_high_cluster_count_at_top_252d},
    "f04_topp_022_triple_top_pattern_score_252d": {"inputs": ["high"], "func": f04_topp_022_triple_top_pattern_score_252d},
    "f04_topp_023_top3_pivot_max_spread_pct_252d": {"inputs": ["high"], "func": f04_topp_023_top3_pivot_max_spread_pct_252d},
    "f04_topp_024_pivot_high_cluster_age_252d": {"inputs": ["high"], "func": f04_topp_024_pivot_high_cluster_age_252d},
    "f04_topp_025_pivot_high_cluster_spread_pct_252d": {"inputs": ["high"], "func": f04_topp_025_pivot_high_cluster_spread_pct_252d},
    "f04_topp_026_last_pivot_high_vs_recent_pivot_high_ratio_252d": {"inputs": ["high"], "func": f04_topp_026_last_pivot_high_vs_recent_pivot_high_ratio_252d},
    "f04_topp_027_secondary_peak_lower_than_primary_count_252d": {"inputs": ["high"], "func": f04_topp_027_secondary_peak_lower_than_primary_count_252d},
    "f04_topp_028_retest_failed_count_at_252d_high_63d": {"inputs": ["close", "high"], "func": f04_topp_028_retest_failed_count_at_252d_high_63d},
    "f04_topp_029_retest_succeeded_count_at_252d_high_63d": {"inputs": ["close", "high"], "func": f04_topp_029_retest_succeeded_count_at_252d_high_63d},
    "f04_topp_030_m_pattern_score_252d": {"inputs": ["close", "high"], "func": f04_topp_030_m_pattern_score_252d},
    "f04_topp_031_head_shoulders_left_high_ratio_252d": {"inputs": ["high"], "func": f04_topp_031_head_shoulders_left_high_ratio_252d},
    "f04_topp_032_head_shoulders_right_high_ratio_252d": {"inputs": ["high"], "func": f04_topp_032_head_shoulders_right_high_ratio_252d},
    "f04_topp_033_head_shoulders_symmetry_score_252d": {"inputs": ["high"], "func": f04_topp_033_head_shoulders_symmetry_score_252d},
    "f04_topp_034_HS_head_above_shoulders_score_252d": {"inputs": ["high"], "func": f04_topp_034_HS_head_above_shoulders_score_252d},
    "f04_topp_035_HS_neckline_break_distance_252d": {"inputs": ["close", "low"], "func": f04_topp_035_HS_neckline_break_distance_252d},
    "f04_topp_036_HS_head_max_close_proximity_252d": {"inputs": ["close", "high"], "func": f04_topp_036_HS_head_max_close_proximity_252d},
    "f04_topp_037_HS_volume_pattern_score_252d": {"inputs": ["volume", "high"], "func": f04_topp_037_HS_volume_pattern_score_252d},
    "f04_topp_038_inverse_HS_no_pattern_count_252d": {"inputs": ["high", "low"], "func": f04_topp_038_inverse_HS_no_pattern_count_252d},
    "f04_topp_039_HS_neckline_age_score_252d": {"inputs": ["close", "low"], "func": f04_topp_039_HS_neckline_age_score_252d},
    "f04_topp_040_shoulder_high_count_within_5pct_252d": {"inputs": ["high"], "func": f04_topp_040_shoulder_high_count_within_5pct_252d},
    "f04_topp_041_head_proximity_to_252d_max_score": {"inputs": ["high"], "func": f04_topp_041_head_proximity_to_252d_max_score},
    "f04_topp_042_head_proximity_to_close_252d": {"inputs": ["close", "high"], "func": f04_topp_042_head_proximity_to_close_252d},
    "f04_topp_043_right_shoulder_age_score_252d": {"inputs": ["high"], "func": f04_topp_043_right_shoulder_age_score_252d},
    "f04_topp_044_shoulder_count_252d": {"inputs": ["high"], "func": f04_topp_044_shoulder_count_252d},
    "f04_topp_045_HS_completion_proximity_score_252d": {"inputs": ["close", "high", "low"], "func": f04_topp_045_HS_completion_proximity_score_252d},
    "f04_topp_046_broadening_top_highs_slope_252d": {"inputs": ["high"], "func": f04_topp_046_broadening_top_highs_slope_252d},
    "f04_topp_047_broadening_top_lows_slope_252d": {"inputs": ["low"], "func": f04_topp_047_broadening_top_lows_slope_252d},
    "f04_topp_048_broadening_top_pattern_score_252d": {"inputs": ["high", "low"], "func": f04_topp_048_broadening_top_pattern_score_252d},
    "f04_topp_049_megaphone_range_growth_252d": {"inputs": ["high", "low"], "func": f04_topp_049_megaphone_range_growth_252d},
    "f04_topp_050_rising_wedge_pattern_score_252d": {"inputs": ["high", "low"], "func": f04_topp_050_rising_wedge_pattern_score_252d},
    "f04_topp_051_rising_wedge_convergence_252d": {"inputs": ["high", "low"], "func": f04_topp_051_rising_wedge_convergence_252d},
    "f04_topp_052_falling_wedge_pattern_score_63d": {"inputs": ["high", "low"], "func": f04_topp_052_falling_wedge_pattern_score_63d},
    "f04_topp_053_bearish_pennant_score_63d": {"inputs": ["high", "low"], "func": f04_topp_053_bearish_pennant_score_63d},
    "f04_topp_054_bearish_flag_top_score_63d": {"inputs": ["close", "high"], "func": f04_topp_054_bearish_flag_top_score_63d},
    "f04_topp_055_higher_lows_lower_highs_count_252d": {"inputs": ["high", "low"], "func": f04_topp_055_higher_lows_lower_highs_count_252d},
    "f04_topp_056_highs_volatility_growth_252d": {"inputs": ["high"], "func": f04_topp_056_highs_volatility_growth_252d},
    "f04_topp_057_lows_volatility_growth_252d": {"inputs": ["low"], "func": f04_topp_057_lows_volatility_growth_252d},
    "f04_topp_058_trading_range_compression_to_breakout_252d": {"inputs": ["high", "low", "close"], "func": f04_topp_058_trading_range_compression_to_breakout_252d},
    "f04_topp_059_range_volatility_collapse_at_top_21d": {"inputs": ["high", "low", "close"], "func": f04_topp_059_range_volatility_collapse_at_top_21d},
    "f04_topp_060_diamond_top_pattern_score_252d": {"inputs": ["high", "low"], "func": f04_topp_060_diamond_top_pattern_score_252d},
    "f04_topp_061_new_252d_high_then_fail_count_63d": {"inputs": ["close", "high"], "func": f04_topp_061_new_252d_high_then_fail_count_63d},
    "f04_topp_062_new_252d_high_reverse_within_5d_count_63d": {"inputs": ["close", "high"], "func": f04_topp_062_new_252d_high_reverse_within_5d_count_63d},
    "f04_topp_063_failed_breakout_after_consolidation_count_252d": {"inputs": ["close", "high"], "func": f04_topp_063_failed_breakout_after_consolidation_count_252d},
    "f04_topp_064_breakout_failure_severity_252d": {"inputs": ["close", "high"], "func": f04_topp_064_breakout_failure_severity_252d},
    "f04_topp_065_false_breakout_score_252d": {"inputs": ["close", "high", "low"], "func": f04_topp_065_false_breakout_score_252d},
    "f04_topp_066_bull_trap_count_63d": {"inputs": ["close", "high"], "func": f04_topp_066_bull_trap_count_63d},
    "f04_topp_067_pivot_high_failure_count_252d": {"inputs": ["close", "high"], "func": f04_topp_067_pivot_high_failure_count_252d},
    "f04_topp_068_close_in_lower_half_at_new_21d_high_count_21d": {"inputs": ["close", "high", "low"], "func": f04_topp_068_close_in_lower_half_at_new_21d_high_count_21d},
    "f04_topp_069_outside_bar_at_252d_high_count_21d": {"inputs": ["close", "high", "low"], "func": f04_topp_069_outside_bar_at_252d_high_count_21d},
    "f04_topp_070_reversal_bar_at_252d_high_score_21d": {"inputs": ["open", "close", "high", "low"], "func": f04_topp_070_reversal_bar_at_252d_high_score_21d},
    "f04_topp_071_breakout_then_below_breakout_level_count_63d": {"inputs": ["close", "high"], "func": f04_topp_071_breakout_then_below_breakout_level_count_63d},
    "f04_topp_072_distribution_after_breakout_count_252d": {"inputs": ["close", "high", "volume"], "func": f04_topp_072_distribution_after_breakout_count_252d},
    "f04_topp_073_breakout_volume_lacking_count_252d": {"inputs": ["high", "volume"], "func": f04_topp_073_breakout_volume_lacking_count_252d},
    "f04_topp_074_breakout_failure_to_recover_count_252d": {"inputs": ["close", "high"], "func": f04_topp_074_breakout_failure_to_recover_count_252d},
    "f04_topp_075_reversal_signal_at_top_composite_21d": {"inputs": ["open", "close", "high", "low"], "func": f04_topp_075_reversal_signal_at_top_composite_21d},
}
