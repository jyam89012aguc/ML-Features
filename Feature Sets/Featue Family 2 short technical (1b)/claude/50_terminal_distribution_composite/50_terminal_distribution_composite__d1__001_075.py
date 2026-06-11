"""terminal_distribution_composite base features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py.
Bucket A: classical distribution-day signals (price-down + volume-up patterns).
Bucket B: topping shape / range / structure (dwell, lower-highs, plateau, rounding).
Bucket C: breakdown triggers (N-day-low breaks, MA violations, death cross, gaps).
Bucket D: drawdown / "stuck" patterns (depth, time-underwater, recovery failure).
Bucket E: distribution-then-breakdown composite sequences.

Inputs: SEP OHLCV. PIT-clean (right-anchored rolling, no centered, no shift(-N)).
Self-contained helpers — no cross-family imports.
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


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _bars_since_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.full(arr.shape, np.nan)
    last = -1
    for i in range(arr.size):
        if arr[i]:
            last = i
            out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)


def _streak_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


# ============================================================
# Bucket A — classical distribution-day signals (001-015)
# ============================================================

def f50_tdco_001_distribution_day_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if close fell > 0.2% AND volume > prior 50d-SMA volume — classical IBD distribution day."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    return ((ret < -0.002) & (volume > vavg)).astype(float).where(vavg.notna(), np.nan)


def f50_tdco_002_distribution_day_count_25(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distribution days in trailing 25 bars — IBD distribution-day count (alarm threshold ~5)."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ev = ((ret < -0.002) & (volume > vavg)).astype(float)
    return ev.rolling(25, min_periods=10).sum().where(vavg.notna(), np.nan)


def f50_tdco_003_distribution_day_count_50(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distribution days in trailing 50 bars — bi-monthly distribution-day count."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ev = ((ret < -0.002) & (volume > vavg)).astype(float)
    return ev.rolling(50, min_periods=MDAYS).sum().where(vavg.notna(), np.nan)


def f50_tdco_004_distribution_to_accumulation_ratio_25(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(distribution-day count in 25) / (accumulation-day count in 25) — bearish if ratio high.
    Accumulation = close up > 0.2% AND volume > prior 50d avg."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    ad = ((ret > 0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    return _safe_div(dd, ad)


def f50_tdco_005_heavy_volume_down_day_indicator(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if close < open AND volume > 1.5x prior 50d-SMA — heavy distribution bar."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    return ((close < open) & (volume > 1.5 * vavg)).astype(float).where(vavg.notna(), np.nan)


def f50_tdco_006_heavy_volume_up_day_indicator(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if close > open AND volume > 1.5x prior 50d-SMA — heavy accumulation bar (context)."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    return ((close > open) & (volume > 1.5 * vavg)).astype(float).where(vavg.notna(), np.nan)


def f50_tdco_007_heavy_down_vs_heavy_up_count_25(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(heavy-down count - heavy-up count) over 25 bars — net heavy-volume bias."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    hd = ((close < open) & (volume > 1.5 * vavg)).astype(float)
    hu = ((close > open) & (volume > 1.5 * vavg)).astype(float)
    return (hd - hu).rolling(25, min_periods=10).sum().where(vavg.notna(), np.nan)


def f50_tdco_008_distribution_score_weighted_25(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum over 25 bars of (|return| × volume/avg-volume) on down days — magnitude-weighted distribution."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    vratio = _safe_div(volume, vavg)
    w = (ret.where(ret < 0, 0).abs() * vratio).where(vavg.notna(), np.nan)
    return w.rolling(25, min_periods=10).sum()


def f50_tdco_009_cumulative_volume_on_down_days_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on down-close days in past 63 bars — total bearish-volume."""
    down = (close.diff() < 0)
    return volume.where(down, 0).rolling(QDAYS, min_periods=MDAYS).sum().where(volume.notna(), np.nan)


def f50_tdco_010_cumulative_volume_on_up_days_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on up-close days in past 63 bars — total bullish-volume (context)."""
    up = (close.diff() > 0)
    return volume.where(up, 0).rolling(QDAYS, min_periods=MDAYS).sum().where(volume.notna(), np.nan)


def f50_tdco_011_down_minus_up_volume_ratio_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(down-volume - up-volume) / total-volume over 63 — net volume bias (>0 = bearish flow)."""
    diff = close.diff()
    dv = volume.where(diff < 0, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    uv = volume.where(diff > 0, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(dv - uv, dv + uv)


def f50_tdco_012_max_consecutive_distribution_days_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Longest run of consecutive distribution days in past 63 bars."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ev = (ret < -0.002) & (volume > vavg)
    return _streak_true(ev).rolling(QDAYS, min_periods=MDAYS).max().where(vavg.notna(), np.nan)


def f50_tdco_013_distribution_day_in_last_5(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if any distribution day occurred in past 5 bars — very-recent distribution flag."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ev = ((ret < -0.002) & (volume > vavg)).astype(float)
    return (ev.rolling(WDAYS, min_periods=1).sum() > 0).astype(float).where(vavg.notna(), np.nan)


def f50_tdco_014_distribution_at_or_near_252_high_63(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distribution days that happened while price within 5% of 252d high, past 63 bars
    — distribution AT the top (the most bearish kind)."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    at_top = high >= 0.95 * high.rolling(YDAYS, min_periods=QDAYS).max()
    ev = ((ret < -0.002) & (volume > vavg) & at_top).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(vavg.notna(), np.nan)


def f50_tdco_015_distribution_density_per_session_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(distribution-day count in 63) / 63 — distribution-day density rate."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ev = ((ret < -0.002) & (volume > vavg)).astype(float)
    return (ev.rolling(QDAYS, min_periods=MDAYS).sum() / float(QDAYS)).where(vavg.notna(), np.nan)


# ============================================================
# Bucket B — topping shape / range / structure (016-030)
# ============================================================

def f50_tdco_016_rolling_top_dwell_21d(high: pd.Series) -> pd.Series:
    """Fraction of past 21 bars with high within 1% of 252d max — short-horizon top dwell."""
    top = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high >= 0.99 * top).astype(float)
    return near.rolling(MDAYS, min_periods=WDAYS).mean().where(top.notna(), np.nan)


def f50_tdco_017_rolling_top_dwell_63d(high: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with high within 1% of 252d max — quarterly top dwell."""
    top = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high >= 0.99 * top).astype(float)
    return near.rolling(QDAYS, min_periods=MDAYS).mean().where(top.notna(), np.nan)


def f50_tdco_018_lower_high_count_21d(high: pd.Series) -> pd.Series:
    """Count of bars in past 21 where current high < high 5 bars ago — short-term lower-high count."""
    lh = (high < high.shift(WDAYS)).astype(float)
    return lh.rolling(MDAYS, min_periods=WDAYS).sum().where(high.notna(), np.nan)


def f50_tdco_019_lower_high_count_63d(high: pd.Series) -> pd.Series:
    """Count of bars in past 63 where current 5d high < 5d high from 5 bars ago — quarterly lower-high count."""
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh = (h5 < h5.shift(WDAYS)).astype(float)
    return lh.rolling(QDAYS, min_periods=MDAYS).sum().where(high.notna(), np.nan)


def f50_tdco_020_failed_retest_of_252h_count_63(high: pd.Series) -> pd.Series:
    """Count of bars in past 63 where high reached 95-99% of 252d-max but not >= 100% — failed retests."""
    top = high.rolling(YDAYS, min_periods=QDAYS).max()
    fail = (high >= 0.95 * top) & (high < top)
    return fail.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(top.notna(), np.nan)


def f50_tdco_021_plateau_detection_63(close: pd.Series) -> pd.Series:
    """Std of close in past 63 / mean — plateau if low relative-std at top."""
    return _safe_div(close.rolling(QDAYS, min_periods=MDAYS).std(), close.rolling(QDAYS, min_periods=MDAYS).mean())


def f50_tdco_022_rounding_top_curvature_63(close: pd.Series) -> pd.Series:
    """Quadratic-fit curvature of close over 63 bars: ax^2 coefficient (negative => rounding top)."""
    def _curv(w):
        if np.isnan(w).any() or len(w) < 21:
            return np.nan
        x = np.arange(len(w), dtype=float)
        try:
            a, _, _ = np.polyfit(x, w, 2)
            return float(a)
        except Exception:
            return np.nan
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_curv, raw=True)


def f50_tdco_023_head_shoulders_proxy_63(high: pd.Series) -> pd.Series:
    """1 if past 63 bars contain: peak1, trough1, higher peak2, trough2, lower peak3 sequence (H&S proxy).
    Implementation: simplified via three 21d sub-window maxima."""
    h1 = high.shift(42).rolling(MDAYS, min_periods=WDAYS).max()
    h2 = high.shift(21).rolling(MDAYS, min_periods=WDAYS).max()
    h3 = high.rolling(MDAYS, min_periods=WDAYS).max()
    pattern = (h2 > h1) & (h3 < h2) & (h3 > 0.95 * h1)
    return pattern.astype(float).where(high.notna(), np.nan)


def f50_tdco_024_triangle_top_compression_63(high: pd.Series, low: pd.Series) -> pd.Series:
    """(63d high range) / (21d high range) — converging triangle if ratio drops while at high (compression)."""
    rng_63 = high.rolling(QDAYS, min_periods=MDAYS).max() - low.rolling(QDAYS, min_periods=MDAYS).min()
    rng_21 = high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min()
    return _safe_div(rng_21, rng_63)


def f50_tdco_025_lower_high_sequence_length_63(high: pd.Series) -> pd.Series:
    """Current streak of consecutive bars where 5d-high is lower than the prior 5d-high — sequence length."""
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh = h5 < h5.shift(WDAYS)
    return _streak_true(lh).where(high.notna(), np.nan)


def f50_tdco_026_distribution_density_at_high_63(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 63 bars that are distribution days WHILE near 252d high — at-top distribution density."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    at_top = high >= 0.95 * high.rolling(YDAYS, min_periods=QDAYS).max()
    ev = ((ret < -0.002) & (volume > vavg) & at_top).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).mean().where(vavg.notna(), np.nan)


def f50_tdco_027_topping_range_to_atr_ratio_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(21d high - 21d low) / ATR(21) — wide-range topping (high ratio = volatile distribution)."""
    rng = high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min()
    return _safe_div(rng, _atr(high, low, close, MDAYS))


def f50_tdco_028_median_close_position_in_range_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Median over past 63 of (close - 63d_low) / (63d_high - 63d_low) — typical close position in range."""
    hh = high.rolling(QDAYS, min_periods=MDAYS).max()
    ll = low.rolling(QDAYS, min_periods=MDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    return pos.rolling(QDAYS, min_periods=MDAYS).median()


def f50_tdco_029_bars_in_top_decile_252_range_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of past 63 bars with close in top 10% of 252d range — top-decile dwell."""
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    return (pos > 0.9).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(hh.notna(), np.nan)


def f50_tdco_030_top_decile_dwell_to_atr_ratio_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(bars in top decile of 252d range past 63) / (ATR(21) / close) — top dwell normalized by vol%."""
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    dwell = (pos > 0.9).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    atr_pct = _safe_div(_atr(high, low, close, MDAYS), close)
    return _safe_div(dwell, atr_pct)


# ============================================================
# Bucket C — breakdown triggers (031-050)
# ============================================================

def f50_tdco_031_break_of_21d_low_indicator(low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if today's close < prior 21d low — short-term breakdown trigger."""
    prev_ll = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    return (close < prev_ll).astype(float).where(prev_ll.notna(), np.nan)


def f50_tdco_032_break_of_63d_low_indicator(low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if today's close < prior 63d low — quarterly breakdown trigger."""
    prev_ll = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    return (close < prev_ll).astype(float).where(prev_ll.notna(), np.nan)


def f50_tdco_033_break_of_252d_low_indicator(low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if today's close < prior 252d low — annual breakdown trigger (rare, high-conviction bear signal)."""
    prev_ll = low.shift(1).rolling(YDAYS, min_periods=QDAYS).min()
    return (close < prev_ll).astype(float).where(prev_ll.notna(), np.nan)


def f50_tdco_034_bars_since_first_break_below_50ma(close: pd.Series) -> pd.Series:
    """Bars since the first time close < SMA(50) after a period above it (uses prior bar state for cross)."""
    sma = _sma(close, 50)
    ev = (close.shift(1) >= sma.shift(1)) & (close < sma)
    return _bars_since_true(ev)


def f50_tdco_035_bars_since_first_break_below_100ma(close: pd.Series) -> pd.Series:
    """Bars since first cross below SMA(100)."""
    sma = _sma(close, 100)
    ev = (close.shift(1) >= sma.shift(1)) & (close < sma)
    return _bars_since_true(ev)


def f50_tdco_036_bars_since_first_break_below_200ma(close: pd.Series) -> pd.Series:
    """Bars since first cross below SMA(200) — major-trend break."""
    sma = _sma(close, 200)
    ev = (close.shift(1) >= sma.shift(1)) & (close < sma)
    return _bars_since_true(ev)


def f50_tdco_037_close_below_50ma_state(close: pd.Series) -> pd.Series:
    """1 if close < SMA(50) — short-trend bearish state."""
    sma = _sma(close, 50)
    return (close < sma).astype(float).where(sma.notna(), np.nan)


def f50_tdco_038_close_below_200ma_state(close: pd.Series) -> pd.Series:
    """1 if close < SMA(200) — major-trend bearish state."""
    sma = _sma(close, 200)
    return (close < sma).astype(float).where(sma.notna(), np.nan)


def f50_tdco_039_death_cross_50_200_event_indicator(close: pd.Series) -> pd.Series:
    """1 if SMA(50) crossed below SMA(200) this bar — classical death cross trigger."""
    s50 = _sma(close, 50)
    s200 = _sma(close, 200)
    d = s50 - s200
    return ((d.shift(1) >= 0) & (d < 0)).astype(float).where(d.notna(), np.nan)


def f50_tdco_040_death_cross_50_200_age_252(close: pd.Series) -> pd.Series:
    """Bars since most-recent death cross (50-vs-200 SMA) — death-cross recency."""
    s50 = _sma(close, 50)
    s200 = _sma(close, 200)
    d = s50 - s200
    ev = (d.shift(1) >= 0) & (d < 0)
    return _bars_since_true(ev)


def f50_tdco_041_breakaway_gap_down_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if today's open < prior close by > ATR(21) AND close < open — breakaway gap-down."""
    atr = _atr(high, low, close, MDAYS)
    return ((open < close.shift(1) - atr) & (close < open)).astype(float).where(atr.notna(), np.nan)


def f50_tdco_042_high_volume_break_of_63d_low(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if close < prior 63d low AND volume > 1.5x prior 50d avg — high-volume support break."""
    prev_ll = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    return ((close < prev_ll) & (volume > 1.5 * vavg)).astype(float).where(prev_ll.notna() & vavg.notna(), np.nan)


def f50_tdco_043_multi_day_breakdown_count_5(low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of past 5 bars where close < prior-bar low — consecutive breakdown bars."""
    ev = (close < low.shift(1)).astype(float)
    return ev.rolling(WDAYS, min_periods=2).sum().where(close.notna(), np.nan)


def f50_tdco_044_failure_to_recover_above_50ma_21(close: pd.Series) -> pd.Series:
    """1 if close has been < SMA(50) for every bar in past 21 — extended below-50ma episode."""
    sma = _sma(close, 50)
    below = (close < sma).astype(float)
    return (below.rolling(MDAYS, min_periods=WDAYS).min() == 1.0).astype(float).where(sma.notna(), np.nan)


def f50_tdco_045_count_of_supports_broken_252(low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of distinct support-break events (close < prior 21d low) in past 252 bars."""
    prev_ll = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    ev = ((close < prev_ll) & (close.shift(1) >= prev_ll.shift(1))).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(prev_ll.notna(), np.nan)


def f50_tdco_046_ma_violation_count_in_21d(close: pd.Series) -> pd.Series:
    """Count of MA violations in past 21 (close < SMA50, < SMA100, < SMA200) — multi-MA breakdown breadth."""
    s50 = _sma(close, 50); s100 = _sma(close, 100); s200 = _sma(close, 200)
    v = ((close < s50).astype(float) + (close < s100).astype(float) + (close < s200).astype(float))
    return v.rolling(MDAYS, min_periods=WDAYS).mean().where(s200.notna(), np.nan)


def f50_tdco_047_post_break_acceleration_21(close: pd.Series) -> pd.Series:
    """21d return AFTER the most-recent break of 21d low — post-breakdown momentum.
    Computed as: 21d cumulative return × indicator(close < prior 21d low in last 21 bars)."""
    prev_ll = close.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    broke_recent = ((close < prev_ll).astype(float).rolling(MDAYS, min_periods=1).sum() > 0)
    ret21 = close.pct_change(MDAYS)
    return ret21.where(broke_recent, np.nan)


def f50_tdco_048_trendline_break_count_63(close: pd.Series) -> pd.Series:
    """Count of bars in past 63 where 21d slope just turned negative — trendline-break proxy."""
    sl = _rolling_slope(close, MDAYS)
    ev = ((sl.shift(1) > 0) & (sl <= 0)).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(sl.notna(), np.nan)


def f50_tdco_049_trend_break_with_volume_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trendline-break events in 63 bars that occurred on > 1.3x avg volume — volume-confirmed breaks."""
    sl = _rolling_slope(close, MDAYS)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ev = ((sl.shift(1) > 0) & (sl <= 0) & (volume > 1.3 * vavg)).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(sl.notna() & vavg.notna(), np.nan)


def f50_tdco_050_post_break_failed_bounce_count_21(low: pd.Series, close: pd.Series) -> pd.Series:
    """Past 21 bars: count of bounces (up-day) that immediately re-broke prior 21d low next bar — failed-bounce count."""
    prev_ll = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    up_bar = (close.diff() > 0)
    rebreak_next = (close.shift(1) < prev_ll.shift(1))
    # PIT-clean: use shift(1) to look backward only
    up_yesterday = (close.diff() > 0).shift(1)
    rebroke_today = (close < prev_ll)
    ev = (up_yesterday & rebroke_today).astype(float)
    return ev.rolling(MDAYS, min_periods=WDAYS).sum().where(prev_ll.notna(), np.nan)


# ============================================================
# Bucket D — drawdown / "stuck" patterns (051-070)
# ============================================================

def f50_tdco_051_drawdown_from_21d_max(high: pd.Series, close: pd.Series) -> pd.Series:
    """(21d high - close) / 21d high — short-horizon drawdown."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    return _safe_div(rmax - close, rmax)


def f50_tdco_052_drawdown_from_63d_max(high: pd.Series, close: pd.Series) -> pd.Series:
    """(63d high - close) / 63d high — quarterly drawdown."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    return _safe_div(rmax - close, rmax)


def f50_tdco_053_drawdown_from_252d_max(high: pd.Series, close: pd.Series) -> pd.Series:
    """(252d high - close) / 252d high — annual drawdown."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(rmax - close, rmax)


def f50_tdco_054_drawdown_from_504d_max(high: pd.Series, close: pd.Series) -> pd.Series:
    """(504d high - close) / 504d high — bi-annual drawdown."""
    rmax = high.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    return _safe_div(rmax - close, rmax)


def f50_tdco_055_drawdown_from_alltime_max(high: pd.Series, close: pd.Series) -> pd.Series:
    """(expanding all-time high - close) / all-time high — lifetime drawdown."""
    rmax = high.expanding(min_periods=MDAYS).max()
    return _safe_div(rmax - close, rmax)


def f50_tdco_056_drawdown_speed_21(high: pd.Series, close: pd.Series) -> pd.Series:
    """Drawdown / (bars-since-21d-max + 1) — drawdown speed proxy (steep recent decline => high)."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    bs = _bars_since_true(high == rmax)
    return _safe_div(dd, bs + 1.0)


def f50_tdco_057_time_since_peak_252(high: pd.Series) -> pd.Series:
    """Bars since most-recent 252d-high — time since annual peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(high == rmax)


def f50_tdco_058_time_underwater_below_10pct_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with drawdown-from-252max > 10% — time-underwater fraction."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    return (dd > 0.10).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(rmax.notna(), np.nan)


def f50_tdco_059_time_underwater_below_20pct_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with drawdown-from-252max > 20% — deeper time-underwater."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    return (dd > 0.20).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(rmax.notna(), np.nan)


def f50_tdco_060_bars_since_first_minus20pct_from_peak(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the first time drawdown from 252d-max exceeded 20% — bear-onset recency."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    return _bars_since_true(dd > 0.20)


def f50_tdco_061_failed_recovery_attempts_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bounces in past 63 bars that did NOT reach prior 21d high — failed-recovery count."""
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    bounce = close.pct_change(WDAYS) > 0.05
    failed = bounce & (high < h21)
    return failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(h21.notna(), np.nan)


def f50_tdco_062_recovery_attempt_failure_rate_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """(failed-bounces in 63) / (total-bounces in 63) — failure rate of recovery attempts."""
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    bounce = close.pct_change(WDAYS) > 0.05
    failed = bounce & (high < h21)
    return _safe_div(failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum(),
                     bounce.astype(float).rolling(QDAYS, min_periods=MDAYS).sum())


def f50_tdco_063_longest_decline_streak_63(close: pd.Series) -> pd.Series:
    """Longest run of consecutive down-close bars in past 63 — max bear streak."""
    return _streak_true(close.diff() < 0).rolling(QDAYS, min_periods=MDAYS).max().where(close.notna(), np.nan)


def f50_tdco_064_lower_low_sequence_length_63(low: pd.Series) -> pd.Series:
    """Current streak of consecutive bars where 5d-low is lower than prior 5d-low."""
    l5 = low.rolling(WDAYS, min_periods=2).min()
    ll = l5 < l5.shift(WDAYS)
    return _streak_true(ll).where(low.notna(), np.nan)


def f50_tdco_065_lower_close_count_post_peak_21(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of close-down bars in past 21 conditioned on being post-peak (within 63 bars of 252d max)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post_peak = (bs > 0) & (bs <= QDAYS)
    return (close.diff() < 0).astype(float).where(post_peak, np.nan).rolling(MDAYS, min_periods=WDAYS).sum()


def f50_tdco_066_lower_close_count_post_peak_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of close-down bars in past 63 conditioned on being post-peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post_peak = (bs > 0) & (bs <= QDAYS)
    return (close.diff() < 0).astype(float).where(post_peak, np.nan).rolling(QDAYS, min_periods=MDAYS).sum()


def f50_tdco_067_post_peak_max_consecutive_red_bars(high: pd.Series, close: pd.Series) -> pd.Series:
    """Max consecutive red-bar streak in past 63 bars when post-peak (within 252 bars of peak)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post_peak = (bs > 0) & (bs <= YDAYS)
    streak = _streak_true(close.diff() < 0)
    return streak.where(post_peak, np.nan).rolling(QDAYS, min_periods=MDAYS).max()


def f50_tdco_068_post_peak_rally_amplitude_decay_63(high: pd.Series) -> pd.Series:
    """(21d high - 21d-high-from-21-bars-ago) — negative = decaying rally peaks (bearish post-peak)."""
    h21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    return h21 - h21.shift(MDAYS)


def f50_tdco_069_distance_252max_to_252min_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 252d-min) / (252d-max - 252d-min) — close position in annual range (low = stuck)."""
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(close - ll, hh - ll)


def f50_tdco_070_post_peak_volatility_expansion_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio: ATR(21) / ATR(21) from 63 bars ago — post-peak vol expansion (>1 = expanding)."""
    atr = _atr(high, low, close, MDAYS)
    return _safe_div(atr, atr.shift(QDAYS))


# ============================================================
# Bucket E — distribution-then-breakdown composite sequences (071-075)
# ============================================================

def f50_tdco_071_distribution_then_breakdown_21(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if at least 3 distribution days occurred in past 25 bars AND close just broke 21d low — sequence trigger."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = ((ret < -0.002) & (volume > vavg)).astype(float)
    dd_count = dd.rolling(25, min_periods=10).sum()
    prev_ll = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    broke = close < prev_ll
    return ((dd_count >= 3.0) & broke).astype(float).where(prev_ll.notna() & vavg.notna(), np.nan)


def f50_tdco_072_distribution_count_pre_breakdown_63(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution-day count in 63 bars conditioned on being WITHIN 21 bars of a 63d-low break — pre-break distribution."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = ((ret < -0.002) & (volume > vavg)).astype(float)
    prev_ll = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    broke = (close < prev_ll).astype(float)
    near_break = broke.rolling(MDAYS, min_periods=1).sum() > 0
    return dd.rolling(QDAYS, min_periods=MDAYS).sum().where(near_break, np.nan)


def f50_tdco_073_terminal_pattern_score_at_top(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """At bars where price within 1% of 252d max: sum of {>=3 distribution days in 25, lower-high count>=3 in 21,
    failed-retest >=2 in 63, plateau-stdev/mean low, top-decile dwell >50%}. Else NaN."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd_count = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh_count = (h5 < h5.shift(WDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    top = high.rolling(YDAYS, min_periods=QDAYS).max()
    fr = ((high >= 0.95 * top) & (high < top)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    plat = _safe_div(close.rolling(QDAYS, min_periods=MDAYS).std(), close.rolling(QDAYS, min_periods=MDAYS).mean())
    pos = _safe_div(close - low.rolling(YDAYS, min_periods=QDAYS).min(), top - low.rolling(YDAYS, min_periods=QDAYS).min())
    dwell = (pos > 0.9).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    score = ((dd_count >= 3.0).astype(float).fillna(0)
             + (lh_count >= 3.0).astype(float).fillna(0)
             + (fr >= 2.0).astype(float).fillna(0)
             + (plat < 0.02).astype(float).fillna(0)
             + (dwell > 0.5).astype(float).fillna(0))
    near_top = high >= 0.99 * top
    return score.where(near_top, np.nan)


def f50_tdco_074_pre_break_distribution_zscore_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score (over 252d) of distribution-day-count(25) — distribution-density extreme."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    return _rolling_zscore(dd, YDAYS, min_periods=QDAYS)


def f50_tdco_075_breakdown_severity_score_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum over past 63 of: {break-21d-low, break-63d-low, break-50ma, break-200ma} — multi-trigger severity."""
    prev_ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    prev_ll63 = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    s = ((close < prev_ll21).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().fillna(0)
         + (close < prev_ll63).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().fillna(0)
         + ((close.shift(1) >= s50.shift(1)) & (close < s50)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().fillna(0)
         + ((close.shift(1) >= s200.shift(1)) & (close < s200)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().fillna(0))
    return s.where(s200.notna(), np.nan)


# ============================================================
#                         REGISTRY 001-075
# ============================================================

TERMINAL_DISTRIBUTION_COMPOSITE_BASE_REGISTRY_001_075 = {
    "f50_tdco_001_distribution_day_indicator": {"inputs": ["close", "volume"], "func": f50_tdco_001_distribution_day_indicator},
    "f50_tdco_002_distribution_day_count_25": {"inputs": ["close", "volume"], "func": f50_tdco_002_distribution_day_count_25},
    "f50_tdco_003_distribution_day_count_50": {"inputs": ["close", "volume"], "func": f50_tdco_003_distribution_day_count_50},
    "f50_tdco_004_distribution_to_accumulation_ratio_25": {"inputs": ["close", "volume"], "func": f50_tdco_004_distribution_to_accumulation_ratio_25},
    "f50_tdco_005_heavy_volume_down_day_indicator": {"inputs": ["open", "close", "volume"], "func": f50_tdco_005_heavy_volume_down_day_indicator},
    "f50_tdco_006_heavy_volume_up_day_indicator": {"inputs": ["open", "close", "volume"], "func": f50_tdco_006_heavy_volume_up_day_indicator},
    "f50_tdco_007_heavy_down_vs_heavy_up_count_25": {"inputs": ["open", "close", "volume"], "func": f50_tdco_007_heavy_down_vs_heavy_up_count_25},
    "f50_tdco_008_distribution_score_weighted_25": {"inputs": ["close", "volume"], "func": f50_tdco_008_distribution_score_weighted_25},
    "f50_tdco_009_cumulative_volume_on_down_days_63": {"inputs": ["close", "volume"], "func": f50_tdco_009_cumulative_volume_on_down_days_63},
    "f50_tdco_010_cumulative_volume_on_up_days_63": {"inputs": ["close", "volume"], "func": f50_tdco_010_cumulative_volume_on_up_days_63},
    "f50_tdco_011_down_minus_up_volume_ratio_63": {"inputs": ["close", "volume"], "func": f50_tdco_011_down_minus_up_volume_ratio_63},
    "f50_tdco_012_max_consecutive_distribution_days_63": {"inputs": ["close", "volume"], "func": f50_tdco_012_max_consecutive_distribution_days_63},
    "f50_tdco_013_distribution_day_in_last_5": {"inputs": ["close", "volume"], "func": f50_tdco_013_distribution_day_in_last_5},
    "f50_tdco_014_distribution_at_or_near_252_high_63": {"inputs": ["high", "close", "volume"], "func": f50_tdco_014_distribution_at_or_near_252_high_63},
    "f50_tdco_015_distribution_density_per_session_63": {"inputs": ["close", "volume"], "func": f50_tdco_015_distribution_density_per_session_63},
    "f50_tdco_016_rolling_top_dwell_21d": {"inputs": ["high"], "func": f50_tdco_016_rolling_top_dwell_21d},
    "f50_tdco_017_rolling_top_dwell_63d": {"inputs": ["high"], "func": f50_tdco_017_rolling_top_dwell_63d},
    "f50_tdco_018_lower_high_count_21d": {"inputs": ["high"], "func": f50_tdco_018_lower_high_count_21d},
    "f50_tdco_019_lower_high_count_63d": {"inputs": ["high"], "func": f50_tdco_019_lower_high_count_63d},
    "f50_tdco_020_failed_retest_of_252h_count_63": {"inputs": ["high"], "func": f50_tdco_020_failed_retest_of_252h_count_63},
    "f50_tdco_021_plateau_detection_63": {"inputs": ["close"], "func": f50_tdco_021_plateau_detection_63},
    "f50_tdco_022_rounding_top_curvature_63": {"inputs": ["close"], "func": f50_tdco_022_rounding_top_curvature_63},
    "f50_tdco_023_head_shoulders_proxy_63": {"inputs": ["high"], "func": f50_tdco_023_head_shoulders_proxy_63},
    "f50_tdco_024_triangle_top_compression_63": {"inputs": ["high", "low"], "func": f50_tdco_024_triangle_top_compression_63},
    "f50_tdco_025_lower_high_sequence_length_63": {"inputs": ["high"], "func": f50_tdco_025_lower_high_sequence_length_63},
    "f50_tdco_026_distribution_density_at_high_63": {"inputs": ["high", "close", "volume"], "func": f50_tdco_026_distribution_density_at_high_63},
    "f50_tdco_027_topping_range_to_atr_ratio_21": {"inputs": ["high", "low", "close"], "func": f50_tdco_027_topping_range_to_atr_ratio_21},
    "f50_tdco_028_median_close_position_in_range_63": {"inputs": ["high", "low", "close"], "func": f50_tdco_028_median_close_position_in_range_63},
    "f50_tdco_029_bars_in_top_decile_252_range_63": {"inputs": ["high", "low", "close"], "func": f50_tdco_029_bars_in_top_decile_252_range_63},
    "f50_tdco_030_top_decile_dwell_to_atr_ratio_63": {"inputs": ["high", "low", "close"], "func": f50_tdco_030_top_decile_dwell_to_atr_ratio_63},
    "f50_tdco_031_break_of_21d_low_indicator": {"inputs": ["low", "close"], "func": f50_tdco_031_break_of_21d_low_indicator},
    "f50_tdco_032_break_of_63d_low_indicator": {"inputs": ["low", "close"], "func": f50_tdco_032_break_of_63d_low_indicator},
    "f50_tdco_033_break_of_252d_low_indicator": {"inputs": ["low", "close"], "func": f50_tdco_033_break_of_252d_low_indicator},
    "f50_tdco_034_bars_since_first_break_below_50ma": {"inputs": ["close"], "func": f50_tdco_034_bars_since_first_break_below_50ma},
    "f50_tdco_035_bars_since_first_break_below_100ma": {"inputs": ["close"], "func": f50_tdco_035_bars_since_first_break_below_100ma},
    "f50_tdco_036_bars_since_first_break_below_200ma": {"inputs": ["close"], "func": f50_tdco_036_bars_since_first_break_below_200ma},
    "f50_tdco_037_close_below_50ma_state": {"inputs": ["close"], "func": f50_tdco_037_close_below_50ma_state},
    "f50_tdco_038_close_below_200ma_state": {"inputs": ["close"], "func": f50_tdco_038_close_below_200ma_state},
    "f50_tdco_039_death_cross_50_200_event_indicator": {"inputs": ["close"], "func": f50_tdco_039_death_cross_50_200_event_indicator},
    "f50_tdco_040_death_cross_50_200_age_252": {"inputs": ["close"], "func": f50_tdco_040_death_cross_50_200_age_252},
    "f50_tdco_041_breakaway_gap_down_indicator": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_041_breakaway_gap_down_indicator},
    "f50_tdco_042_high_volume_break_of_63d_low": {"inputs": ["low", "close", "volume"], "func": f50_tdco_042_high_volume_break_of_63d_low},
    "f50_tdco_043_multi_day_breakdown_count_5": {"inputs": ["low", "close"], "func": f50_tdco_043_multi_day_breakdown_count_5},
    "f50_tdco_044_failure_to_recover_above_50ma_21": {"inputs": ["close"], "func": f50_tdco_044_failure_to_recover_above_50ma_21},
    "f50_tdco_045_count_of_supports_broken_252": {"inputs": ["low", "close"], "func": f50_tdco_045_count_of_supports_broken_252},
    "f50_tdco_046_ma_violation_count_in_21d": {"inputs": ["close"], "func": f50_tdco_046_ma_violation_count_in_21d},
    "f50_tdco_047_post_break_acceleration_21": {"inputs": ["close"], "func": f50_tdco_047_post_break_acceleration_21},
    "f50_tdco_048_trendline_break_count_63": {"inputs": ["close"], "func": f50_tdco_048_trendline_break_count_63},
    "f50_tdco_049_trend_break_with_volume_63": {"inputs": ["close", "volume"], "func": f50_tdco_049_trend_break_with_volume_63},
    "f50_tdco_050_post_break_failed_bounce_count_21": {"inputs": ["low", "close"], "func": f50_tdco_050_post_break_failed_bounce_count_21},
    "f50_tdco_051_drawdown_from_21d_max": {"inputs": ["high", "close"], "func": f50_tdco_051_drawdown_from_21d_max},
    "f50_tdco_052_drawdown_from_63d_max": {"inputs": ["high", "close"], "func": f50_tdco_052_drawdown_from_63d_max},
    "f50_tdco_053_drawdown_from_252d_max": {"inputs": ["high", "close"], "func": f50_tdco_053_drawdown_from_252d_max},
    "f50_tdco_054_drawdown_from_504d_max": {"inputs": ["high", "close"], "func": f50_tdco_054_drawdown_from_504d_max},
    "f50_tdco_055_drawdown_from_alltime_max": {"inputs": ["high", "close"], "func": f50_tdco_055_drawdown_from_alltime_max},
    "f50_tdco_056_drawdown_speed_21": {"inputs": ["high", "close"], "func": f50_tdco_056_drawdown_speed_21},
    "f50_tdco_057_time_since_peak_252": {"inputs": ["high"], "func": f50_tdco_057_time_since_peak_252},
    "f50_tdco_058_time_underwater_below_10pct_252": {"inputs": ["high", "close"], "func": f50_tdco_058_time_underwater_below_10pct_252},
    "f50_tdco_059_time_underwater_below_20pct_252": {"inputs": ["high", "close"], "func": f50_tdco_059_time_underwater_below_20pct_252},
    "f50_tdco_060_bars_since_first_minus20pct_from_peak": {"inputs": ["high", "close"], "func": f50_tdco_060_bars_since_first_minus20pct_from_peak},
    "f50_tdco_061_failed_recovery_attempts_63": {"inputs": ["high", "close"], "func": f50_tdco_061_failed_recovery_attempts_63},
    "f50_tdco_062_recovery_attempt_failure_rate_63": {"inputs": ["high", "close"], "func": f50_tdco_062_recovery_attempt_failure_rate_63},
    "f50_tdco_063_longest_decline_streak_63": {"inputs": ["close"], "func": f50_tdco_063_longest_decline_streak_63},
    "f50_tdco_064_lower_low_sequence_length_63": {"inputs": ["low"], "func": f50_tdco_064_lower_low_sequence_length_63},
    "f50_tdco_065_lower_close_count_post_peak_21": {"inputs": ["high", "close"], "func": f50_tdco_065_lower_close_count_post_peak_21},
    "f50_tdco_066_lower_close_count_post_peak_63": {"inputs": ["high", "close"], "func": f50_tdco_066_lower_close_count_post_peak_63},
    "f50_tdco_067_post_peak_max_consecutive_red_bars": {"inputs": ["high", "close"], "func": f50_tdco_067_post_peak_max_consecutive_red_bars},
    "f50_tdco_068_post_peak_rally_amplitude_decay_63": {"inputs": ["high"], "func": f50_tdco_068_post_peak_rally_amplitude_decay_63},
    "f50_tdco_069_distance_252max_to_252min_ratio": {"inputs": ["high", "low", "close"], "func": f50_tdco_069_distance_252max_to_252min_ratio},
    "f50_tdco_070_post_peak_volatility_expansion_63": {"inputs": ["high", "low", "close"], "func": f50_tdco_070_post_peak_volatility_expansion_63},
    "f50_tdco_071_distribution_then_breakdown_21": {"inputs": ["low", "close", "volume"], "func": f50_tdco_071_distribution_then_breakdown_21},
    "f50_tdco_072_distribution_count_pre_breakdown_63": {"inputs": ["low", "close", "volume"], "func": f50_tdco_072_distribution_count_pre_breakdown_63},
    "f50_tdco_073_terminal_pattern_score_at_top": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_073_terminal_pattern_score_at_top},
    "f50_tdco_074_pre_break_distribution_zscore_252": {"inputs": ["close", "volume"], "func": f50_tdco_074_pre_break_distribution_zscore_252},
    "f50_tdco_075_breakdown_severity_score_63": {"inputs": ["high", "low", "close"], "func": f50_tdco_075_breakdown_severity_score_63},
}


# === D1 wrappers + registry (001_075) ===
def f50_tdco_001_distribution_day_indicator_d1(close, volume): return f50_tdco_001_distribution_day_indicator(close, volume).diff()
def f50_tdco_002_distribution_day_count_25_d1(close, volume): return f50_tdco_002_distribution_day_count_25(close, volume).diff()
def f50_tdco_003_distribution_day_count_50_d1(close, volume): return f50_tdco_003_distribution_day_count_50(close, volume).diff()
def f50_tdco_004_distribution_to_accumulation_ratio_25_d1(close, volume): return f50_tdco_004_distribution_to_accumulation_ratio_25(close, volume).diff()
def f50_tdco_005_heavy_volume_down_day_indicator_d1(open, close, volume): return f50_tdco_005_heavy_volume_down_day_indicator(open, close, volume).diff()
def f50_tdco_006_heavy_volume_up_day_indicator_d1(open, close, volume): return f50_tdco_006_heavy_volume_up_day_indicator(open, close, volume).diff()
def f50_tdco_007_heavy_down_vs_heavy_up_count_25_d1(open, close, volume): return f50_tdco_007_heavy_down_vs_heavy_up_count_25(open, close, volume).diff()
def f50_tdco_008_distribution_score_weighted_25_d1(close, volume): return f50_tdco_008_distribution_score_weighted_25(close, volume).diff()
def f50_tdco_009_cumulative_volume_on_down_days_63_d1(close, volume): return f50_tdco_009_cumulative_volume_on_down_days_63(close, volume).diff()
def f50_tdco_010_cumulative_volume_on_up_days_63_d1(close, volume): return f50_tdco_010_cumulative_volume_on_up_days_63(close, volume).diff()
def f50_tdco_011_down_minus_up_volume_ratio_63_d1(close, volume): return f50_tdco_011_down_minus_up_volume_ratio_63(close, volume).diff()
def f50_tdco_012_max_consecutive_distribution_days_63_d1(close, volume): return f50_tdco_012_max_consecutive_distribution_days_63(close, volume).diff()
def f50_tdco_013_distribution_day_in_last_5_d1(close, volume): return f50_tdco_013_distribution_day_in_last_5(close, volume).diff()
def f50_tdco_014_distribution_at_or_near_252_high_63_d1(high, close, volume): return f50_tdco_014_distribution_at_or_near_252_high_63(high, close, volume).diff()
def f50_tdco_015_distribution_density_per_session_63_d1(close, volume): return f50_tdco_015_distribution_density_per_session_63(close, volume).diff()
def f50_tdco_016_rolling_top_dwell_21d_d1(high): return f50_tdco_016_rolling_top_dwell_21d(high).diff()
def f50_tdco_017_rolling_top_dwell_63d_d1(high): return f50_tdco_017_rolling_top_dwell_63d(high).diff()
def f50_tdco_018_lower_high_count_21d_d1(high): return f50_tdco_018_lower_high_count_21d(high).diff()
def f50_tdco_019_lower_high_count_63d_d1(high): return f50_tdco_019_lower_high_count_63d(high).diff()
def f50_tdco_020_failed_retest_of_252h_count_63_d1(high): return f50_tdco_020_failed_retest_of_252h_count_63(high).diff()
def f50_tdco_021_plateau_detection_63_d1(close): return f50_tdco_021_plateau_detection_63(close).diff()
def f50_tdco_022_rounding_top_curvature_63_d1(close): return f50_tdco_022_rounding_top_curvature_63(close).diff()
def f50_tdco_023_head_shoulders_proxy_63_d1(high): return f50_tdco_023_head_shoulders_proxy_63(high).diff()
def f50_tdco_024_triangle_top_compression_63_d1(high, low): return f50_tdco_024_triangle_top_compression_63(high, low).diff()
def f50_tdco_025_lower_high_sequence_length_63_d1(high): return f50_tdco_025_lower_high_sequence_length_63(high).diff()
def f50_tdco_026_distribution_density_at_high_63_d1(high, close, volume): return f50_tdco_026_distribution_density_at_high_63(high, close, volume).diff()
def f50_tdco_027_topping_range_to_atr_ratio_21_d1(high, low, close): return f50_tdco_027_topping_range_to_atr_ratio_21(high, low, close).diff()
def f50_tdco_028_median_close_position_in_range_63_d1(high, low, close): return f50_tdco_028_median_close_position_in_range_63(high, low, close).diff()
def f50_tdco_029_bars_in_top_decile_252_range_63_d1(high, low, close): return f50_tdco_029_bars_in_top_decile_252_range_63(high, low, close).diff()
def f50_tdco_030_top_decile_dwell_to_atr_ratio_63_d1(high, low, close): return f50_tdco_030_top_decile_dwell_to_atr_ratio_63(high, low, close).diff()
def f50_tdco_031_break_of_21d_low_indicator_d1(low, close): return f50_tdco_031_break_of_21d_low_indicator(low, close).diff()
def f50_tdco_032_break_of_63d_low_indicator_d1(low, close): return f50_tdco_032_break_of_63d_low_indicator(low, close).diff()
def f50_tdco_033_break_of_252d_low_indicator_d1(low, close): return f50_tdco_033_break_of_252d_low_indicator(low, close).diff()
def f50_tdco_034_bars_since_first_break_below_50ma_d1(close): return f50_tdco_034_bars_since_first_break_below_50ma(close).diff()
def f50_tdco_035_bars_since_first_break_below_100ma_d1(close): return f50_tdco_035_bars_since_first_break_below_100ma(close).diff()
def f50_tdco_036_bars_since_first_break_below_200ma_d1(close): return f50_tdco_036_bars_since_first_break_below_200ma(close).diff()
def f50_tdco_037_close_below_50ma_state_d1(close): return f50_tdco_037_close_below_50ma_state(close).diff()
def f50_tdco_038_close_below_200ma_state_d1(close): return f50_tdco_038_close_below_200ma_state(close).diff()
def f50_tdco_039_death_cross_50_200_event_indicator_d1(close): return f50_tdco_039_death_cross_50_200_event_indicator(close).diff()
def f50_tdco_040_death_cross_50_200_age_252_d1(close): return f50_tdco_040_death_cross_50_200_age_252(close).diff()
def f50_tdco_041_breakaway_gap_down_indicator_d1(open, high, low, close): return f50_tdco_041_breakaway_gap_down_indicator(open, high, low, close).diff()
def f50_tdco_042_high_volume_break_of_63d_low_d1(low, close, volume): return f50_tdco_042_high_volume_break_of_63d_low(low, close, volume).diff()
def f50_tdco_043_multi_day_breakdown_count_5_d1(low, close): return f50_tdco_043_multi_day_breakdown_count_5(low, close).diff()
def f50_tdco_044_failure_to_recover_above_50ma_21_d1(close): return f50_tdco_044_failure_to_recover_above_50ma_21(close).diff()
def f50_tdco_045_count_of_supports_broken_252_d1(low, close): return f50_tdco_045_count_of_supports_broken_252(low, close).diff()
def f50_tdco_046_ma_violation_count_in_21d_d1(close): return f50_tdco_046_ma_violation_count_in_21d(close).diff()
def f50_tdco_047_post_break_acceleration_21_d1(close): return f50_tdco_047_post_break_acceleration_21(close).diff()
def f50_tdco_048_trendline_break_count_63_d1(close): return f50_tdco_048_trendline_break_count_63(close).diff()
def f50_tdco_049_trend_break_with_volume_63_d1(close, volume): return f50_tdco_049_trend_break_with_volume_63(close, volume).diff()
def f50_tdco_050_post_break_failed_bounce_count_21_d1(low, close): return f50_tdco_050_post_break_failed_bounce_count_21(low, close).diff()
def f50_tdco_051_drawdown_from_21d_max_d1(high, close): return f50_tdco_051_drawdown_from_21d_max(high, close).diff()
def f50_tdco_052_drawdown_from_63d_max_d1(high, close): return f50_tdco_052_drawdown_from_63d_max(high, close).diff()
def f50_tdco_053_drawdown_from_252d_max_d1(high, close): return f50_tdco_053_drawdown_from_252d_max(high, close).diff()
def f50_tdco_054_drawdown_from_504d_max_d1(high, close): return f50_tdco_054_drawdown_from_504d_max(high, close).diff()
def f50_tdco_055_drawdown_from_alltime_max_d1(high, close): return f50_tdco_055_drawdown_from_alltime_max(high, close).diff()
def f50_tdco_056_drawdown_speed_21_d1(high, close): return f50_tdco_056_drawdown_speed_21(high, close).diff()
def f50_tdco_057_time_since_peak_252_d1(high): return f50_tdco_057_time_since_peak_252(high).diff()
def f50_tdco_058_time_underwater_below_10pct_252_d1(high, close): return f50_tdco_058_time_underwater_below_10pct_252(high, close).diff()
def f50_tdco_059_time_underwater_below_20pct_252_d1(high, close): return f50_tdco_059_time_underwater_below_20pct_252(high, close).diff()
def f50_tdco_060_bars_since_first_minus20pct_from_peak_d1(high, close): return f50_tdco_060_bars_since_first_minus20pct_from_peak(high, close).diff()
def f50_tdco_061_failed_recovery_attempts_63_d1(high, close): return f50_tdco_061_failed_recovery_attempts_63(high, close).diff()
def f50_tdco_062_recovery_attempt_failure_rate_63_d1(high, close): return f50_tdco_062_recovery_attempt_failure_rate_63(high, close).diff()
def f50_tdco_063_longest_decline_streak_63_d1(close): return f50_tdco_063_longest_decline_streak_63(close).diff()
def f50_tdco_064_lower_low_sequence_length_63_d1(low): return f50_tdco_064_lower_low_sequence_length_63(low).diff()
def f50_tdco_065_lower_close_count_post_peak_21_d1(high, close): return f50_tdco_065_lower_close_count_post_peak_21(high, close).diff()
def f50_tdco_066_lower_close_count_post_peak_63_d1(high, close): return f50_tdco_066_lower_close_count_post_peak_63(high, close).diff()
def f50_tdco_067_post_peak_max_consecutive_red_bars_d1(high, close): return f50_tdco_067_post_peak_max_consecutive_red_bars(high, close).diff()
def f50_tdco_068_post_peak_rally_amplitude_decay_63_d1(high): return f50_tdco_068_post_peak_rally_amplitude_decay_63(high).diff()
def f50_tdco_069_distance_252max_to_252min_ratio_d1(high, low, close): return f50_tdco_069_distance_252max_to_252min_ratio(high, low, close).diff()
def f50_tdco_070_post_peak_volatility_expansion_63_d1(high, low, close): return f50_tdco_070_post_peak_volatility_expansion_63(high, low, close).diff()
def f50_tdco_071_distribution_then_breakdown_21_d1(low, close, volume): return f50_tdco_071_distribution_then_breakdown_21(low, close, volume).diff()
def f50_tdco_072_distribution_count_pre_breakdown_63_d1(low, close, volume): return f50_tdco_072_distribution_count_pre_breakdown_63(low, close, volume).diff()
def f50_tdco_073_terminal_pattern_score_at_top_d1(high, low, close, volume): return f50_tdco_073_terminal_pattern_score_at_top(high, low, close, volume).diff()
def f50_tdco_074_pre_break_distribution_zscore_252_d1(close, volume): return f50_tdco_074_pre_break_distribution_zscore_252(close, volume).diff()
def f50_tdco_075_breakdown_severity_score_63_d1(high, low, close): return f50_tdco_075_breakdown_severity_score_63(high, low, close).diff()

TERMINAL_DISTRIBUTION_COMPOSITE_D1_REGISTRY_001_075 = {
    "f50_tdco_001_distribution_day_indicator_d1": {"inputs": ["close", "volume"], "func": f50_tdco_001_distribution_day_indicator_d1},
    "f50_tdco_002_distribution_day_count_25_d1": {"inputs": ["close", "volume"], "func": f50_tdco_002_distribution_day_count_25_d1},
    "f50_tdco_003_distribution_day_count_50_d1": {"inputs": ["close", "volume"], "func": f50_tdco_003_distribution_day_count_50_d1},
    "f50_tdco_004_distribution_to_accumulation_ratio_25_d1": {"inputs": ["close", "volume"], "func": f50_tdco_004_distribution_to_accumulation_ratio_25_d1},
    "f50_tdco_005_heavy_volume_down_day_indicator_d1": {"inputs": ["open", "close", "volume"], "func": f50_tdco_005_heavy_volume_down_day_indicator_d1},
    "f50_tdco_006_heavy_volume_up_day_indicator_d1": {"inputs": ["open", "close", "volume"], "func": f50_tdco_006_heavy_volume_up_day_indicator_d1},
    "f50_tdco_007_heavy_down_vs_heavy_up_count_25_d1": {"inputs": ["open", "close", "volume"], "func": f50_tdco_007_heavy_down_vs_heavy_up_count_25_d1},
    "f50_tdco_008_distribution_score_weighted_25_d1": {"inputs": ["close", "volume"], "func": f50_tdco_008_distribution_score_weighted_25_d1},
    "f50_tdco_009_cumulative_volume_on_down_days_63_d1": {"inputs": ["close", "volume"], "func": f50_tdco_009_cumulative_volume_on_down_days_63_d1},
    "f50_tdco_010_cumulative_volume_on_up_days_63_d1": {"inputs": ["close", "volume"], "func": f50_tdco_010_cumulative_volume_on_up_days_63_d1},
    "f50_tdco_011_down_minus_up_volume_ratio_63_d1": {"inputs": ["close", "volume"], "func": f50_tdco_011_down_minus_up_volume_ratio_63_d1},
    "f50_tdco_012_max_consecutive_distribution_days_63_d1": {"inputs": ["close", "volume"], "func": f50_tdco_012_max_consecutive_distribution_days_63_d1},
    "f50_tdco_013_distribution_day_in_last_5_d1": {"inputs": ["close", "volume"], "func": f50_tdco_013_distribution_day_in_last_5_d1},
    "f50_tdco_014_distribution_at_or_near_252_high_63_d1": {"inputs": ["high", "close", "volume"], "func": f50_tdco_014_distribution_at_or_near_252_high_63_d1},
    "f50_tdco_015_distribution_density_per_session_63_d1": {"inputs": ["close", "volume"], "func": f50_tdco_015_distribution_density_per_session_63_d1},
    "f50_tdco_016_rolling_top_dwell_21d_d1": {"inputs": ["high"], "func": f50_tdco_016_rolling_top_dwell_21d_d1},
    "f50_tdco_017_rolling_top_dwell_63d_d1": {"inputs": ["high"], "func": f50_tdco_017_rolling_top_dwell_63d_d1},
    "f50_tdco_018_lower_high_count_21d_d1": {"inputs": ["high"], "func": f50_tdco_018_lower_high_count_21d_d1},
    "f50_tdco_019_lower_high_count_63d_d1": {"inputs": ["high"], "func": f50_tdco_019_lower_high_count_63d_d1},
    "f50_tdco_020_failed_retest_of_252h_count_63_d1": {"inputs": ["high"], "func": f50_tdco_020_failed_retest_of_252h_count_63_d1},
    "f50_tdco_021_plateau_detection_63_d1": {"inputs": ["close"], "func": f50_tdco_021_plateau_detection_63_d1},
    "f50_tdco_022_rounding_top_curvature_63_d1": {"inputs": ["close"], "func": f50_tdco_022_rounding_top_curvature_63_d1},
    "f50_tdco_023_head_shoulders_proxy_63_d1": {"inputs": ["high"], "func": f50_tdco_023_head_shoulders_proxy_63_d1},
    "f50_tdco_024_triangle_top_compression_63_d1": {"inputs": ["high", "low"], "func": f50_tdco_024_triangle_top_compression_63_d1},
    "f50_tdco_025_lower_high_sequence_length_63_d1": {"inputs": ["high"], "func": f50_tdco_025_lower_high_sequence_length_63_d1},
    "f50_tdco_026_distribution_density_at_high_63_d1": {"inputs": ["high", "close", "volume"], "func": f50_tdco_026_distribution_density_at_high_63_d1},
    "f50_tdco_027_topping_range_to_atr_ratio_21_d1": {"inputs": ["high", "low", "close"], "func": f50_tdco_027_topping_range_to_atr_ratio_21_d1},
    "f50_tdco_028_median_close_position_in_range_63_d1": {"inputs": ["high", "low", "close"], "func": f50_tdco_028_median_close_position_in_range_63_d1},
    "f50_tdco_029_bars_in_top_decile_252_range_63_d1": {"inputs": ["high", "low", "close"], "func": f50_tdco_029_bars_in_top_decile_252_range_63_d1},
    "f50_tdco_030_top_decile_dwell_to_atr_ratio_63_d1": {"inputs": ["high", "low", "close"], "func": f50_tdco_030_top_decile_dwell_to_atr_ratio_63_d1},
    "f50_tdco_031_break_of_21d_low_indicator_d1": {"inputs": ["low", "close"], "func": f50_tdco_031_break_of_21d_low_indicator_d1},
    "f50_tdco_032_break_of_63d_low_indicator_d1": {"inputs": ["low", "close"], "func": f50_tdco_032_break_of_63d_low_indicator_d1},
    "f50_tdco_033_break_of_252d_low_indicator_d1": {"inputs": ["low", "close"], "func": f50_tdco_033_break_of_252d_low_indicator_d1},
    "f50_tdco_034_bars_since_first_break_below_50ma_d1": {"inputs": ["close"], "func": f50_tdco_034_bars_since_first_break_below_50ma_d1},
    "f50_tdco_035_bars_since_first_break_below_100ma_d1": {"inputs": ["close"], "func": f50_tdco_035_bars_since_first_break_below_100ma_d1},
    "f50_tdco_036_bars_since_first_break_below_200ma_d1": {"inputs": ["close"], "func": f50_tdco_036_bars_since_first_break_below_200ma_d1},
    "f50_tdco_037_close_below_50ma_state_d1": {"inputs": ["close"], "func": f50_tdco_037_close_below_50ma_state_d1},
    "f50_tdco_038_close_below_200ma_state_d1": {"inputs": ["close"], "func": f50_tdco_038_close_below_200ma_state_d1},
    "f50_tdco_039_death_cross_50_200_event_indicator_d1": {"inputs": ["close"], "func": f50_tdco_039_death_cross_50_200_event_indicator_d1},
    "f50_tdco_040_death_cross_50_200_age_252_d1": {"inputs": ["close"], "func": f50_tdco_040_death_cross_50_200_age_252_d1},
    "f50_tdco_041_breakaway_gap_down_indicator_d1": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_041_breakaway_gap_down_indicator_d1},
    "f50_tdco_042_high_volume_break_of_63d_low_d1": {"inputs": ["low", "close", "volume"], "func": f50_tdco_042_high_volume_break_of_63d_low_d1},
    "f50_tdco_043_multi_day_breakdown_count_5_d1": {"inputs": ["low", "close"], "func": f50_tdco_043_multi_day_breakdown_count_5_d1},
    "f50_tdco_044_failure_to_recover_above_50ma_21_d1": {"inputs": ["close"], "func": f50_tdco_044_failure_to_recover_above_50ma_21_d1},
    "f50_tdco_045_count_of_supports_broken_252_d1": {"inputs": ["low", "close"], "func": f50_tdco_045_count_of_supports_broken_252_d1},
    "f50_tdco_046_ma_violation_count_in_21d_d1": {"inputs": ["close"], "func": f50_tdco_046_ma_violation_count_in_21d_d1},
    "f50_tdco_047_post_break_acceleration_21_d1": {"inputs": ["close"], "func": f50_tdco_047_post_break_acceleration_21_d1},
    "f50_tdco_048_trendline_break_count_63_d1": {"inputs": ["close"], "func": f50_tdco_048_trendline_break_count_63_d1},
    "f50_tdco_049_trend_break_with_volume_63_d1": {"inputs": ["close", "volume"], "func": f50_tdco_049_trend_break_with_volume_63_d1},
    "f50_tdco_050_post_break_failed_bounce_count_21_d1": {"inputs": ["low", "close"], "func": f50_tdco_050_post_break_failed_bounce_count_21_d1},
    "f50_tdco_051_drawdown_from_21d_max_d1": {"inputs": ["high", "close"], "func": f50_tdco_051_drawdown_from_21d_max_d1},
    "f50_tdco_052_drawdown_from_63d_max_d1": {"inputs": ["high", "close"], "func": f50_tdco_052_drawdown_from_63d_max_d1},
    "f50_tdco_053_drawdown_from_252d_max_d1": {"inputs": ["high", "close"], "func": f50_tdco_053_drawdown_from_252d_max_d1},
    "f50_tdco_054_drawdown_from_504d_max_d1": {"inputs": ["high", "close"], "func": f50_tdco_054_drawdown_from_504d_max_d1},
    "f50_tdco_055_drawdown_from_alltime_max_d1": {"inputs": ["high", "close"], "func": f50_tdco_055_drawdown_from_alltime_max_d1},
    "f50_tdco_056_drawdown_speed_21_d1": {"inputs": ["high", "close"], "func": f50_tdco_056_drawdown_speed_21_d1},
    "f50_tdco_057_time_since_peak_252_d1": {"inputs": ["high"], "func": f50_tdco_057_time_since_peak_252_d1},
    "f50_tdco_058_time_underwater_below_10pct_252_d1": {"inputs": ["high", "close"], "func": f50_tdco_058_time_underwater_below_10pct_252_d1},
    "f50_tdco_059_time_underwater_below_20pct_252_d1": {"inputs": ["high", "close"], "func": f50_tdco_059_time_underwater_below_20pct_252_d1},
    "f50_tdco_060_bars_since_first_minus20pct_from_peak_d1": {"inputs": ["high", "close"], "func": f50_tdco_060_bars_since_first_minus20pct_from_peak_d1},
    "f50_tdco_061_failed_recovery_attempts_63_d1": {"inputs": ["high", "close"], "func": f50_tdco_061_failed_recovery_attempts_63_d1},
    "f50_tdco_062_recovery_attempt_failure_rate_63_d1": {"inputs": ["high", "close"], "func": f50_tdco_062_recovery_attempt_failure_rate_63_d1},
    "f50_tdco_063_longest_decline_streak_63_d1": {"inputs": ["close"], "func": f50_tdco_063_longest_decline_streak_63_d1},
    "f50_tdco_064_lower_low_sequence_length_63_d1": {"inputs": ["low"], "func": f50_tdco_064_lower_low_sequence_length_63_d1},
    "f50_tdco_065_lower_close_count_post_peak_21_d1": {"inputs": ["high", "close"], "func": f50_tdco_065_lower_close_count_post_peak_21_d1},
    "f50_tdco_066_lower_close_count_post_peak_63_d1": {"inputs": ["high", "close"], "func": f50_tdco_066_lower_close_count_post_peak_63_d1},
    "f50_tdco_067_post_peak_max_consecutive_red_bars_d1": {"inputs": ["high", "close"], "func": f50_tdco_067_post_peak_max_consecutive_red_bars_d1},
    "f50_tdco_068_post_peak_rally_amplitude_decay_63_d1": {"inputs": ["high"], "func": f50_tdco_068_post_peak_rally_amplitude_decay_63_d1},
    "f50_tdco_069_distance_252max_to_252min_ratio_d1": {"inputs": ["high", "low", "close"], "func": f50_tdco_069_distance_252max_to_252min_ratio_d1},
    "f50_tdco_070_post_peak_volatility_expansion_63_d1": {"inputs": ["high", "low", "close"], "func": f50_tdco_070_post_peak_volatility_expansion_63_d1},
    "f50_tdco_071_distribution_then_breakdown_21_d1": {"inputs": ["low", "close", "volume"], "func": f50_tdco_071_distribution_then_breakdown_21_d1},
    "f50_tdco_072_distribution_count_pre_breakdown_63_d1": {"inputs": ["low", "close", "volume"], "func": f50_tdco_072_distribution_count_pre_breakdown_63_d1},
    "f50_tdco_073_terminal_pattern_score_at_top_d1": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_073_terminal_pattern_score_at_top_d1},
    "f50_tdco_074_pre_break_distribution_zscore_252_d1": {"inputs": ["close", "volume"], "func": f50_tdco_074_pre_break_distribution_zscore_252_d1},
    "f50_tdco_075_breakdown_severity_score_63_d1": {"inputs": ["high", "low", "close"], "func": f50_tdco_075_breakdown_severity_score_63_d1},
}
