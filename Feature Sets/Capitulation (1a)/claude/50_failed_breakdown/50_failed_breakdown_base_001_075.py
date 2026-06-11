"""
50_failed_breakdown — Base Features 001-075
Domain: undercut-and-reclaim of prior support lows — failed breakdown / bear trap / spring
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Same-bar detection: low pierces prior support, close reclaims above it on the SAME bar.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _prior_low(low: pd.Series, w: int) -> pd.Series:
    """Rolling min of PRIOR bars: shift(1) then rolling min — strictly backward-looking."""
    return low.shift(1).rolling(w, min_periods=max(1, w // 2)).min()


def _failed_breakdown_flag(close: pd.Series, high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """Binary flag: low < prior w-day low AND close >= prior w-day low (same bar)."""
    support = _prior_low(low, w)
    return ((low < support) & (close >= support)).astype(float)


def _undercut_depth(close: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """How far low pierced below prior w-day support (positive = pierced deeper)."""
    support = _prior_low(low, w)
    pierce = support - low
    fb = _failed_breakdown_flag(close, close, low, w)
    return pierce.where(fb > 0, np.nan).fillna(0.0)


def _days_since_fb(fb_flag: pd.Series) -> pd.Series:
    """Trading days elapsed since the most recent failed-breakdown event."""
    not_fb = (fb_flag == 0)
    group = fb_flag.cumsum()
    out = not_fb.astype(int).groupby(group).cumsum().astype(float)
    out = out.where(group > 0, np.nan)
    return out


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Core same-bar failed-breakdown flags across lookback windows ---

def fbd_001_flag_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: low < prior 5-day low and close >= prior 5-day low (same bar)."""
    return _failed_breakdown_flag(close, high, low, _TD_WEEK)


def fbd_002_flag_10d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: low < prior 10-day low and close >= prior 10-day low."""
    return _failed_breakdown_flag(close, high, low, 10)


def fbd_003_flag_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: low < prior 21-day low and close >= prior 21-day low."""
    return _failed_breakdown_flag(close, high, low, _TD_MON)


def fbd_004_flag_42d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: low < prior 42-day low and close >= prior 42-day low."""
    return _failed_breakdown_flag(close, high, low, 42)


def fbd_005_flag_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: low < prior 63-day low and close >= prior 63-day low."""
    return _failed_breakdown_flag(close, high, low, _TD_QTR)


def fbd_006_flag_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: low < prior 126-day low and close >= prior 126-day low."""
    return _failed_breakdown_flag(close, high, low, _TD_HALF)


def fbd_007_flag_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: low < prior 252-day low and close >= prior 252-day low."""
    return _failed_breakdown_flag(close, high, low, _TD_YEAR)


def fbd_008_flag_any_21_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: failed breakdown on either 21-day or 63-day support level."""
    return ((fbd_003_flag_21d(close, high, low) + fbd_005_flag_63d(close, high, low)) > 0).astype(float)


def fbd_009_flag_close_above_open_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Failed 21d breakdown where bar also closes above its open (bullish reclaim candle)."""
    fb = fbd_003_flag_21d(close, high, low)
    bull_candle = (close > open).astype(float)
    return (fb * bull_candle)


def fbd_010_flag_high_volume_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Failed 21d breakdown confirmed with volume > 21-day avg volume."""
    fb = fbd_003_flag_21d(close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (fb * (volume > avg_vol).astype(float))


def fbd_011_flag_close_above_open_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Failed 63d breakdown where bar closes above its open."""
    fb = fbd_005_flag_63d(close, high, low)
    bull_candle = (close > open).astype(float)
    return (fb * bull_candle)


def fbd_012_flag_close_above_sma21_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Failed 21d breakdown and close also reclaims the 21-day SMA."""
    fb = fbd_003_flag_21d(close, high, low)
    sma21 = _rolling_mean(close, _TD_MON)
    return (fb * (close >= sma21).astype(float))


def fbd_013_flag_close_midpoint_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Failed 21d breakdown where close is in top half of today's bar range."""
    fb = fbd_003_flag_21d(close, high, low)
    midpoint = (high + low) / 2.0
    return (fb * (close >= midpoint).astype(float))


def fbd_014_flag_double_bottom_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Failed breakdown at 21d low when prior failed breakdown at same level within 21 bars."""
    fb = fbd_003_flag_21d(close, high, low)
    prior_fb = fb.shift(1).rolling(_TD_MON, min_periods=1).sum()
    return (fb * (prior_fb >= 1).astype(float))


def fbd_015_flag_63d_with_volume_spike(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Failed 63d breakdown with volume > 2x its 21-day average (capitulation spring)."""
    fb = fbd_005_flag_63d(close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (fb * (volume > 2 * avg_vol).astype(float))


# --- Group B (016-030): Undercut depth measures (how far below support the low pierced) ---

def fbd_016_undercut_depth_5d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute points: how far low pierced prior 5-day support on failed breakdowns."""
    return _undercut_depth(close, low, _TD_WEEK)


def fbd_017_undercut_depth_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute points: low pierced prior 21-day support on failed breakdowns."""
    return _undercut_depth(close, low, _TD_MON)


def fbd_018_undercut_depth_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute points: low pierced prior 63-day support on failed breakdowns."""
    return _undercut_depth(close, low, _TD_QTR)


def fbd_019_undercut_depth_pct_5d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Undercut depth as % of prior 5-day support level on failed breakdowns."""
    support = _prior_low(low, _TD_WEEK)
    fb = fbd_001_flag_5d(close, close, low)
    depth_pct = _safe_div(support - low, support)
    return depth_pct.where(fb > 0, 0.0)


def fbd_020_undercut_depth_pct_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Undercut depth as % of prior 21-day support level on failed breakdowns."""
    support = _prior_low(low, _TD_MON)
    fb = fbd_003_flag_21d(close, close, low)
    depth_pct = _safe_div(support - low, support)
    return depth_pct.where(fb > 0, 0.0)


def fbd_021_undercut_depth_pct_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Undercut depth as % of prior 63-day support level on failed breakdowns."""
    support = _prior_low(low, _TD_QTR)
    fb = fbd_005_flag_63d(close, close, low)
    depth_pct = _safe_div(support - low, support)
    return depth_pct.where(fb > 0, 0.0)


def fbd_022_undercut_depth_pct_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Undercut depth as % of prior 252-day support level on failed breakdowns."""
    support = _prior_low(low, _TD_YEAR)
    fb = fbd_007_flag_252d(close, close, low)
    depth_pct = _safe_div(support - low, support)
    return depth_pct.where(fb > 0, 0.0)


def fbd_023_max_undercut_pct_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum undercut depth (% of support) over trailing 63-day window."""
    depth = fbd_020_undercut_depth_pct_21d(close, low)
    return _rolling_max(depth, _TD_QTR)


def fbd_024_max_undercut_pct_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum undercut depth (% of support) over trailing 252-day window."""
    depth = fbd_020_undercut_depth_pct_21d(close, low)
    return _rolling_max(depth, _TD_YEAR)


def fbd_025_avg_undercut_pct_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Average undercut depth (% of support) over trailing 63-day window."""
    depth = fbd_020_undercut_depth_pct_21d(close, low)
    cnt = (depth > 0).astype(float)
    total = _rolling_sum(depth, _TD_QTR)
    count = _rolling_sum(cnt, _TD_QTR).clip(lower=1)
    return _safe_div(total, count)


def fbd_026_wick_below_support_pct_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Rejection wick below 21-day support as % of full bar range on failed breakdowns."""
    support = _prior_low(low, _TD_MON)
    fb = fbd_003_flag_21d(close, high, low)
    wick = (support - low).clip(lower=0)
    bar_range = (high - low).replace(0, np.nan)
    wick_pct = _safe_div(wick, bar_range)
    return wick_pct.where(fb > 0, 0.0)


def fbd_027_wick_below_support_pct_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Rejection wick below 63-day support as % of full bar range on failed breakdowns."""
    support = _prior_low(low, _TD_QTR)
    fb = fbd_005_flag_63d(close, high, low)
    wick = (support - low).clip(lower=0)
    bar_range = (high - low).replace(0, np.nan)
    wick_pct = _safe_div(wick, bar_range)
    return wick_pct.where(fb > 0, 0.0)


def fbd_028_reclaim_close_vs_support_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close minus prior 21-day support on failed breakdown bars (reclaim margin)."""
    support = _prior_low(low, _TD_MON)
    fb = fbd_003_flag_21d(close, high, low)
    margin = close - support
    return margin.where(fb > 0, 0.0)


def fbd_029_reclaim_close_vs_support_pct_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Reclaim margin as % of support level (quality of reclaim on 21d FB)."""
    support = _prior_low(low, _TD_MON)
    fb = fbd_003_flag_21d(close, high, low)
    margin_pct = _safe_div(close - support, support)
    return margin_pct.where(fb > 0, 0.0)


def fbd_030_reclaim_close_vs_support_pct_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Reclaim margin as % of support level (quality of reclaim on 63d FB)."""
    support = _prior_low(low, _TD_QTR)
    fb = fbd_005_flag_63d(close, high, low)
    margin_pct = _safe_div(close - support, support)
    return margin_pct.where(fb > 0, 0.0)


# --- Group C (031-045): Event counts in rolling windows ---

def fbd_031_count_21d_fb_in_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 21-day failed-breakdown events in trailing 5 days."""
    return _rolling_sum(fbd_003_flag_21d(close, high, low), _TD_WEEK)


def fbd_032_count_21d_fb_in_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 21-day failed-breakdown events in trailing 21 days."""
    return _rolling_sum(fbd_003_flag_21d(close, high, low), _TD_MON)


def fbd_033_count_21d_fb_in_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 21-day failed-breakdown events in trailing 63 days."""
    return _rolling_sum(fbd_003_flag_21d(close, high, low), _TD_QTR)


def fbd_034_count_21d_fb_in_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 21-day failed-breakdown events in trailing 126 days."""
    return _rolling_sum(fbd_003_flag_21d(close, high, low), _TD_HALF)


def fbd_035_count_21d_fb_in_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 21-day failed-breakdown events in trailing 252 days."""
    return _rolling_sum(fbd_003_flag_21d(close, high, low), _TD_YEAR)


def fbd_036_count_63d_fb_in_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 63-day failed-breakdown events in trailing 21 days."""
    return _rolling_sum(fbd_005_flag_63d(close, high, low), _TD_MON)


def fbd_037_count_63d_fb_in_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 63-day failed-breakdown events in trailing 63 days."""
    return _rolling_sum(fbd_005_flag_63d(close, high, low), _TD_QTR)


def fbd_038_count_63d_fb_in_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 63-day failed-breakdown events in trailing 252 days."""
    return _rolling_sum(fbd_005_flag_63d(close, high, low), _TD_YEAR)


def fbd_039_count_252d_fb_in_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 252-day failed-breakdown events in trailing 252 days."""
    return _rolling_sum(fbd_007_flag_252d(close, high, low), _TD_YEAR)


def fbd_040_count_multi_level_fb_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars testing BOTH 21d and 63d support simultaneously as failed breakdowns."""
    both = ((fbd_003_flag_21d(close, high, low) > 0) & (fbd_005_flag_63d(close, high, low) > 0)).astype(float)
    return _rolling_sum(both, _TD_MON)


def fbd_041_count_multi_level_fb_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of multi-level (21d+63d) failed breakdowns in trailing 63 days."""
    both = ((fbd_003_flag_21d(close, high, low) > 0) & (fbd_005_flag_63d(close, high, low) > 0)).astype(float)
    return _rolling_sum(both, _TD_QTR)


def fbd_042_fb_21d_cluster_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: 2 or more 21d failed-breakdown events within trailing 21 days (clustering)."""
    return (fbd_032_count_21d_fb_in_21d(close, high, low) >= 2).astype(float)


def fbd_043_fb_63d_cluster_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: 2 or more 63d failed-breakdown events within trailing 63 days (clustering)."""
    return (fbd_037_count_63d_fb_in_63d(close, high, low) >= 2).astype(float)


def fbd_044_multi_test_support_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of times 21-day support low was tested (low < support, regardless of close)."""
    support = _prior_low(low, _TD_MON)
    test = (low < support).astype(float)
    return _rolling_sum(test, _TD_MON)


def fbd_045_multi_test_support_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of times 63-day support low was tested in trailing 63 days."""
    support = _prior_low(low, _TD_QTR)
    test = (low < support).astype(float)
    return _rolling_sum(test, _TD_QTR)


# --- Group D (046-060): Days-since and recency measures ---

def fbd_046_days_since_last_fb_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Trading days since the most recent 21-day failed-breakdown event."""
    fb = fbd_003_flag_21d(close, high, low)
    return _days_since_fb(fb)


def fbd_047_days_since_last_fb_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Trading days since the most recent 63-day failed-breakdown event."""
    fb = fbd_005_flag_63d(close, high, low)
    return _days_since_fb(fb)


def fbd_048_days_since_last_fb_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Trading days since the most recent 252-day failed-breakdown event."""
    fb = fbd_007_flag_252d(close, high, low)
    return _days_since_fb(fb)


def fbd_049_days_since_log_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Log1p of days since last 21-day failed-breakdown (compressed recency)."""
    return np.log1p(fbd_046_days_since_last_fb_21d(close, high, low).fillna(0))


def fbd_050_days_since_log_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Log1p of days since last 63-day failed-breakdown (compressed recency)."""
    return np.log1p(fbd_047_days_since_last_fb_63d(close, high, low).fillna(0))


def fbd_051_fb_within_5d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: a 21d failed-breakdown occurred within the past 5 trading days."""
    cnt = fbd_031_count_21d_fb_in_5d(close, high, low)
    return (cnt >= 1).astype(float)


def fbd_052_fb_within_21d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: a 21d failed-breakdown occurred within the past 21 trading days."""
    cnt = fbd_032_count_21d_fb_in_21d(close, high, low)
    return (cnt >= 1).astype(float)


def fbd_053_fb_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21d FB count (21d window) within trailing 252 days."""
    cnt = fbd_032_count_21d_fb_in_21d(close, high, low)
    return cnt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fbd_054_fb_21d_freq_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Annualized frequency of 21d failed-breakdown events (count per 252 days)."""
    return fbd_035_count_21d_fb_in_252d(close, high, low)


def fbd_055_fb_63d_freq_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Annualized frequency of 63d failed-breakdown events (count per 252 days)."""
    return fbd_038_count_63d_fb_in_252d(close, high, low)


def fbd_056_time_since_fb_norm_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since last 21d FB normalized by 252-day avg inter-FB interval."""
    days = fbd_046_days_since_last_fb_21d(close, high, low).fillna(_TD_YEAR)
    avg_interval = _rolling_mean(days, _TD_YEAR)
    return _safe_div(days, avg_interval)


def fbd_057_fb_count_21d_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 21-day FB count relative to 252-day history."""
    cnt = fbd_032_count_21d_fb_in_21d(close, high, low)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    return _safe_div(cnt - m, s)


def fbd_058_support_level_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Prior 21-day rolling support low level (the reference price being tested)."""
    return _prior_low(low, _TD_MON)


def fbd_059_support_level_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Prior 63-day rolling support low level."""
    return _prior_low(low, _TD_QTR)


def fbd_060_support_level_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Prior 252-day rolling support low level (multi-year support)."""
    return _prior_low(low, _TD_YEAR)


# --- Group E (061-075): Support-level proximity, MA reclaim, round-number tests ---

def fbd_061_close_above_support_21d_pct(close: pd.Series, low: pd.Series) -> pd.Series:
    """Close as % above/below prior 21-day support (positive = above support)."""
    support = _prior_low(low, _TD_MON)
    return _safe_div(close - support, support)


def fbd_062_close_above_support_63d_pct(close: pd.Series, low: pd.Series) -> pd.Series:
    """Close as % above/below prior 63-day support."""
    support = _prior_low(low, _TD_QTR)
    return _safe_div(close - support, support)


def fbd_063_low_below_support_21d_pct(close: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday low as % below prior 21-day support (depth of any undercut, regardless of close)."""
    support = _prior_low(low, _TD_MON)
    undercut = support - low
    return _safe_div(undercut.clip(lower=0), support)


def fbd_064_low_below_support_63d_pct(close: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday low as % below prior 63-day support (depth of any undercut)."""
    support = _prior_low(low, _TD_QTR)
    undercut = support - low
    return _safe_div(undercut.clip(lower=0), support)


def fbd_065_fb_21d_with_sma50_reclaim(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Failed 21d breakdown where close also reclaims the 50-day SMA."""
    fb = fbd_003_flag_21d(close, high, low)
    sma50 = _rolling_mean(close, 50)
    return (fb * (close >= sma50).astype(float))


def fbd_066_fb_21d_with_sma200_reclaim(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Failed 21d breakdown where close also reclaims the 200-day SMA."""
    fb = fbd_003_flag_21d(close, high, low)
    sma200 = _rolling_mean(close, 200)
    return (fb * (close >= sma200).astype(float))


def fbd_067_fb_21d_with_ema21_reclaim(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Failed 21d breakdown where close also reclaims the 21-day EMA."""
    fb = fbd_003_flag_21d(close, high, low)
    ema21 = _ewm_mean(close, _TD_MON)
    return (fb * (close >= ema21).astype(float))


def fbd_068_round_number_proximity_1pct(close: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: prior 21d support is within 1% of a round dollar (integer price level)."""
    support = _prior_low(low, _TD_MON)
    nearest_round = support.round(0)
    pct_from_round = _safe_div((support - nearest_round).abs(), nearest_round.replace(0, np.nan))
    return (pct_from_round <= 0.01).astype(float)


def fbd_069_fb_at_round_number_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Failed 21d breakdown occurring at a round-number support level (within 1%)."""
    fb = fbd_003_flag_21d(close, high, low)
    support = _prior_low(low, _TD_MON)
    nearest_round = support.round(0)
    pct_from_round = _safe_div((support - nearest_round).abs(), nearest_round.replace(0, np.nan))
    round_flag = (pct_from_round <= 0.01).astype(float)
    return (fb * round_flag)


def fbd_070_fb_bar_range_pct_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bar range (high-low) as % of close on 21d failed breakdown bars."""
    fb = fbd_003_flag_21d(close, high, low)
    bar_range_pct = _safe_div(high - low, close)
    return bar_range_pct.where(fb > 0, 0.0)


def fbd_071_fb_volume_ratio_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on 21d failed breakdown bars as ratio to 21-day avg volume."""
    fb = fbd_003_flag_21d(close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol)
    return vol_ratio.where(fb > 0, np.nan).fillna(0.0)


def fbd_072_fb_volume_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on 63d failed breakdown bars as ratio to 21-day avg volume."""
    fb = fbd_005_flag_63d(close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol)
    return vol_ratio.where(fb > 0, np.nan).fillna(0.0)


def fbd_073_avg_fb_volume_ratio_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume ratio on 21d FB events over trailing 252 days."""
    vol_ratio = fbd_071_fb_volume_ratio_21d(close, high, low, volume)
    cnt = (vol_ratio > 0).astype(float)
    total = _rolling_sum(vol_ratio, _TD_YEAR)
    count = _rolling_sum(cnt, _TD_YEAR).clip(lower=1)
    return _safe_div(total, count)


def fbd_074_close_vs_52wk_low_on_fb(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close as % above 252-day low on 21d failed breakdown bars."""
    fb = fbd_003_flag_21d(close, high, low)
    low_252 = _prior_low(low, _TD_YEAR)
    pct_above = _safe_div(close - low_252, low_252)
    return pct_above.where(fb > 0, np.nan).fillna(0.0)


def fbd_075_fb_body_to_wick_ratio_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of candle body to lower wick (below support) on 21d failed breakdowns."""
    fb = fbd_003_flag_21d(close, high, low)
    support = _prior_low(low, _TD_MON)
    body = (close - open).abs()
    lower_wick = (support - low).clip(lower=0)
    ratio = _safe_div(body, lower_wick.replace(0, np.nan))
    return ratio.where(fb > 0, np.nan).fillna(0.0)


# ── Registry ──────────────────────────────────────────────────────────────────

FAILED_BREAKDOWN_REGISTRY_001_075 = {
    "fbd_001_flag_5d": {"inputs": ["close", "high", "low"], "func": fbd_001_flag_5d},
    "fbd_002_flag_10d": {"inputs": ["close", "high", "low"], "func": fbd_002_flag_10d},
    "fbd_003_flag_21d": {"inputs": ["close", "high", "low"], "func": fbd_003_flag_21d},
    "fbd_004_flag_42d": {"inputs": ["close", "high", "low"], "func": fbd_004_flag_42d},
    "fbd_005_flag_63d": {"inputs": ["close", "high", "low"], "func": fbd_005_flag_63d},
    "fbd_006_flag_126d": {"inputs": ["close", "high", "low"], "func": fbd_006_flag_126d},
    "fbd_007_flag_252d": {"inputs": ["close", "high", "low"], "func": fbd_007_flag_252d},
    "fbd_008_flag_any_21_63d": {"inputs": ["close", "high", "low"], "func": fbd_008_flag_any_21_63d},
    "fbd_009_flag_close_above_open_21d": {"inputs": ["close", "high", "low", "open"], "func": fbd_009_flag_close_above_open_21d},
    "fbd_010_flag_high_volume_21d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_010_flag_high_volume_21d},
    "fbd_011_flag_close_above_open_63d": {"inputs": ["close", "high", "low", "open"], "func": fbd_011_flag_close_above_open_63d},
    "fbd_012_flag_close_above_sma21_21d": {"inputs": ["close", "high", "low"], "func": fbd_012_flag_close_above_sma21_21d},
    "fbd_013_flag_close_midpoint_21d": {"inputs": ["close", "high", "low"], "func": fbd_013_flag_close_midpoint_21d},
    "fbd_014_flag_double_bottom_21d": {"inputs": ["close", "high", "low"], "func": fbd_014_flag_double_bottom_21d},
    "fbd_015_flag_63d_with_volume_spike": {"inputs": ["close", "high", "low", "volume"], "func": fbd_015_flag_63d_with_volume_spike},
    "fbd_016_undercut_depth_5d": {"inputs": ["close", "low"], "func": fbd_016_undercut_depth_5d},
    "fbd_017_undercut_depth_21d": {"inputs": ["close", "low"], "func": fbd_017_undercut_depth_21d},
    "fbd_018_undercut_depth_63d": {"inputs": ["close", "low"], "func": fbd_018_undercut_depth_63d},
    "fbd_019_undercut_depth_pct_5d": {"inputs": ["close", "low"], "func": fbd_019_undercut_depth_pct_5d},
    "fbd_020_undercut_depth_pct_21d": {"inputs": ["close", "low"], "func": fbd_020_undercut_depth_pct_21d},
    "fbd_021_undercut_depth_pct_63d": {"inputs": ["close", "low"], "func": fbd_021_undercut_depth_pct_63d},
    "fbd_022_undercut_depth_pct_252d": {"inputs": ["close", "low"], "func": fbd_022_undercut_depth_pct_252d},
    "fbd_023_max_undercut_pct_63d": {"inputs": ["close", "low"], "func": fbd_023_max_undercut_pct_63d},
    "fbd_024_max_undercut_pct_252d": {"inputs": ["close", "low"], "func": fbd_024_max_undercut_pct_252d},
    "fbd_025_avg_undercut_pct_63d": {"inputs": ["close", "low"], "func": fbd_025_avg_undercut_pct_63d},
    "fbd_026_wick_below_support_pct_21d": {"inputs": ["close", "high", "low"], "func": fbd_026_wick_below_support_pct_21d},
    "fbd_027_wick_below_support_pct_63d": {"inputs": ["close", "high", "low"], "func": fbd_027_wick_below_support_pct_63d},
    "fbd_028_reclaim_close_vs_support_21d": {"inputs": ["close", "high", "low"], "func": fbd_028_reclaim_close_vs_support_21d},
    "fbd_029_reclaim_close_vs_support_pct_21d": {"inputs": ["close", "high", "low"], "func": fbd_029_reclaim_close_vs_support_pct_21d},
    "fbd_030_reclaim_close_vs_support_pct_63d": {"inputs": ["close", "high", "low"], "func": fbd_030_reclaim_close_vs_support_pct_63d},
    "fbd_031_count_21d_fb_in_5d": {"inputs": ["close", "high", "low"], "func": fbd_031_count_21d_fb_in_5d},
    "fbd_032_count_21d_fb_in_21d": {"inputs": ["close", "high", "low"], "func": fbd_032_count_21d_fb_in_21d},
    "fbd_033_count_21d_fb_in_63d": {"inputs": ["close", "high", "low"], "func": fbd_033_count_21d_fb_in_63d},
    "fbd_034_count_21d_fb_in_126d": {"inputs": ["close", "high", "low"], "func": fbd_034_count_21d_fb_in_126d},
    "fbd_035_count_21d_fb_in_252d": {"inputs": ["close", "high", "low"], "func": fbd_035_count_21d_fb_in_252d},
    "fbd_036_count_63d_fb_in_21d": {"inputs": ["close", "high", "low"], "func": fbd_036_count_63d_fb_in_21d},
    "fbd_037_count_63d_fb_in_63d": {"inputs": ["close", "high", "low"], "func": fbd_037_count_63d_fb_in_63d},
    "fbd_038_count_63d_fb_in_252d": {"inputs": ["close", "high", "low"], "func": fbd_038_count_63d_fb_in_252d},
    "fbd_039_count_252d_fb_in_252d": {"inputs": ["close", "high", "low"], "func": fbd_039_count_252d_fb_in_252d},
    "fbd_040_count_multi_level_fb_21d": {"inputs": ["close", "high", "low"], "func": fbd_040_count_multi_level_fb_21d},
    "fbd_041_count_multi_level_fb_63d": {"inputs": ["close", "high", "low"], "func": fbd_041_count_multi_level_fb_63d},
    "fbd_042_fb_21d_cluster_flag": {"inputs": ["close", "high", "low"], "func": fbd_042_fb_21d_cluster_flag},
    "fbd_043_fb_63d_cluster_flag": {"inputs": ["close", "high", "low"], "func": fbd_043_fb_63d_cluster_flag},
    "fbd_044_multi_test_support_21d": {"inputs": ["close", "high", "low"], "func": fbd_044_multi_test_support_21d},
    "fbd_045_multi_test_support_63d": {"inputs": ["close", "high", "low"], "func": fbd_045_multi_test_support_63d},
    "fbd_046_days_since_last_fb_21d": {"inputs": ["close", "high", "low"], "func": fbd_046_days_since_last_fb_21d},
    "fbd_047_days_since_last_fb_63d": {"inputs": ["close", "high", "low"], "func": fbd_047_days_since_last_fb_63d},
    "fbd_048_days_since_last_fb_252d": {"inputs": ["close", "high", "low"], "func": fbd_048_days_since_last_fb_252d},
    "fbd_049_days_since_log_21d": {"inputs": ["close", "high", "low"], "func": fbd_049_days_since_log_21d},
    "fbd_050_days_since_log_63d": {"inputs": ["close", "high", "low"], "func": fbd_050_days_since_log_63d},
    "fbd_051_fb_within_5d_flag": {"inputs": ["close", "high", "low"], "func": fbd_051_fb_within_5d_flag},
    "fbd_052_fb_within_21d_flag": {"inputs": ["close", "high", "low"], "func": fbd_052_fb_within_21d_flag},
    "fbd_053_fb_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": fbd_053_fb_pct_rank_252d},
    "fbd_054_fb_21d_freq_252d": {"inputs": ["close", "high", "low"], "func": fbd_054_fb_21d_freq_252d},
    "fbd_055_fb_63d_freq_252d": {"inputs": ["close", "high", "low"], "func": fbd_055_fb_63d_freq_252d},
    "fbd_056_time_since_fb_norm_252d": {"inputs": ["close", "high", "low"], "func": fbd_056_time_since_fb_norm_252d},
    "fbd_057_fb_count_21d_zscore_252d": {"inputs": ["close", "high", "low"], "func": fbd_057_fb_count_21d_zscore_252d},
    "fbd_058_support_level_21d": {"inputs": ["close", "low"], "func": fbd_058_support_level_21d},
    "fbd_059_support_level_63d": {"inputs": ["close", "low"], "func": fbd_059_support_level_63d},
    "fbd_060_support_level_252d": {"inputs": ["close", "low"], "func": fbd_060_support_level_252d},
    "fbd_061_close_above_support_21d_pct": {"inputs": ["close", "low"], "func": fbd_061_close_above_support_21d_pct},
    "fbd_062_close_above_support_63d_pct": {"inputs": ["close", "low"], "func": fbd_062_close_above_support_63d_pct},
    "fbd_063_low_below_support_21d_pct": {"inputs": ["close", "low"], "func": fbd_063_low_below_support_21d_pct},
    "fbd_064_low_below_support_63d_pct": {"inputs": ["close", "low"], "func": fbd_064_low_below_support_63d_pct},
    "fbd_065_fb_21d_with_sma50_reclaim": {"inputs": ["close", "high", "low"], "func": fbd_065_fb_21d_with_sma50_reclaim},
    "fbd_066_fb_21d_with_sma200_reclaim": {"inputs": ["close", "high", "low"], "func": fbd_066_fb_21d_with_sma200_reclaim},
    "fbd_067_fb_21d_with_ema21_reclaim": {"inputs": ["close", "high", "low"], "func": fbd_067_fb_21d_with_ema21_reclaim},
    "fbd_068_round_number_proximity_1pct": {"inputs": ["close", "low"], "func": fbd_068_round_number_proximity_1pct},
    "fbd_069_fb_at_round_number_21d": {"inputs": ["close", "high", "low"], "func": fbd_069_fb_at_round_number_21d},
    "fbd_070_fb_bar_range_pct_21d": {"inputs": ["close", "high", "low"], "func": fbd_070_fb_bar_range_pct_21d},
    "fbd_071_fb_volume_ratio_21d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_071_fb_volume_ratio_21d},
    "fbd_072_fb_volume_ratio_63d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_072_fb_volume_ratio_63d},
    "fbd_073_avg_fb_volume_ratio_252d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_073_avg_fb_volume_ratio_252d},
    "fbd_074_close_vs_52wk_low_on_fb": {"inputs": ["close", "high", "low"], "func": fbd_074_close_vs_52wk_low_on_fb},
    "fbd_075_fb_body_to_wick_ratio_21d": {"inputs": ["close", "high", "low", "open"], "func": fbd_075_fb_body_to_wick_ratio_21d},
}
