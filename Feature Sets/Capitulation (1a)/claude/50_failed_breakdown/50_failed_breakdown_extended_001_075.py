"""
50_failed_breakdown — Extended Features 001-075
Domain: undercut-and-reclaim of prior support lows — failed breakdown / bear trap / spring
        Extended variants: additional lookback windows, high/open-based supports, VWAP-proxied
        supports, inter-breakdown interval statistics, trap-success streaks, OBV-confirmed
        springs, percentile ranks and z-scores of ext-base concepts, Heikin-Ashi FB flags,
        weighted-midpoint support tests, and volume-profile false-breakdown composites.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
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


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


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


def _prior_high(high: pd.Series, w: int) -> pd.Series:
    """Rolling max of PRIOR bars: shift(1) then rolling max — strictly backward-looking."""
    return high.shift(1).rolling(w, min_periods=max(1, w // 2)).max()


def _failed_breakdown_flag(close: pd.Series, high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """Binary flag: low < prior w-day low AND close >= prior w-day low (same bar)."""
    support = _prior_low(low, w)
    return ((low < support) & (close >= support)).astype(float)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Average True Range over w periods."""
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    return _rolling_mean(tr, w)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Non-standard lookback window FB flags (net-new windows) ---

def fbd_ext_001_flag_3d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: low < prior 3-day low and close >= prior 3-day low (ultra-short spring)."""
    return _failed_breakdown_flag(close, high, low, 3)


def fbd_ext_002_flag_7d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: low < prior 7-day low and close >= prior 7-day low."""
    return _failed_breakdown_flag(close, high, low, 7)


def fbd_ext_003_flag_15d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: low < prior 15-day low and close >= prior 15-day low."""
    return _failed_breakdown_flag(close, high, low, 15)


def fbd_ext_004_flag_30d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: low < prior 30-day low and close >= prior 30-day low."""
    return _failed_breakdown_flag(close, high, low, 30)


def fbd_ext_005_flag_45d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: low < prior 45-day low and close >= prior 45-day low."""
    return _failed_breakdown_flag(close, high, low, 45)


def fbd_ext_006_flag_90d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: low < prior 90-day low and close >= prior 90-day low."""
    return _failed_breakdown_flag(close, high, low, 90)


def fbd_ext_007_flag_180d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: low < prior 180-day low and close >= prior 180-day low."""
    return _failed_breakdown_flag(close, high, low, 180)


def fbd_ext_008_flag_any_3_levels(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of support levels (15d, 45d, 90d) simultaneously failed-broken on the same bar."""
    f15 = _failed_breakdown_flag(close, high, low, 15).astype(float)
    f45 = _failed_breakdown_flag(close, high, low, 45).astype(float)
    f90 = _failed_breakdown_flag(close, high, low, 90).astype(float)
    return f15 + f45 + f90


def fbd_ext_009_flag_45d_bull_candle(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Failed 45d breakdown where close > open (bullish engulfing-style reclaim)."""
    fb = _failed_breakdown_flag(close, high, low, 45)
    return (fb * (close > open).astype(float))


def fbd_ext_010_flag_90d_high_volume(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Failed 90d breakdown confirmed with volume > 21d avg volume."""
    fb = _failed_breakdown_flag(close, high, low, 90)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (fb * (volume > avg_vol).astype(float))


def fbd_ext_011_flag_180d_near_52wk_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Failed 180d breakdown when close is within 5% of 252-day low (deep multi-level trap)."""
    fb = _failed_breakdown_flag(close, high, low, 180)
    low_252 = _prior_low(low, _TD_YEAR)
    near = _safe_div(close - low_252, low_252.replace(0, np.nan)) < 0.05
    return (fb * near.astype(float))


def fbd_ext_012_consecutive_fb_streak_7d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days with a 7-day failed-breakdown (fast-spring streak)."""
    fb = _failed_breakdown_flag(close, high, low, 7)
    cond = fb > 0
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


# --- Group B (013-025): Undercut depth variants with non-standard windows ---

def fbd_ext_013_undercut_depth_pct_7d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Undercut depth as % of prior 7-day support level on failed breakdowns."""
    support = _prior_low(low, 7)
    fb = _failed_breakdown_flag(close, close, low, 7)
    depth_pct = _safe_div(support - low, support.replace(0, np.nan))
    return depth_pct.clip(lower=0).where(fb > 0, 0.0)


def fbd_ext_014_undercut_depth_pct_45d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Undercut depth as % of prior 45-day support level on failed breakdowns."""
    support = _prior_low(low, 45)
    fb = _failed_breakdown_flag(close, close, low, 45)
    depth_pct = _safe_div(support - low, support.replace(0, np.nan))
    return depth_pct.clip(lower=0).where(fb > 0, 0.0)


def fbd_ext_015_undercut_depth_pct_90d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Undercut depth as % of prior 90-day support level on failed breakdowns."""
    support = _prior_low(low, 90)
    fb = _failed_breakdown_flag(close, close, low, 90)
    depth_pct = _safe_div(support - low, support.replace(0, np.nan))
    return depth_pct.clip(lower=0).where(fb > 0, 0.0)


def fbd_ext_016_undercut_depth_pct_180d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Undercut depth as % of prior 180-day support level on failed breakdowns."""
    support = _prior_low(low, 180)
    fb = _failed_breakdown_flag(close, close, low, 180)
    depth_pct = _safe_div(support - low, support.replace(0, np.nan))
    return depth_pct.clip(lower=0).where(fb > 0, 0.0)


def fbd_ext_017_max_undercut_pct_126d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum undercut depth (% of 21d support) over trailing 126-day window."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, close, low, _TD_MON)
    depth_pct = _safe_div(support - low, support.replace(0, np.nan)).clip(lower=0).where(fb > 0, 0.0)
    return _rolling_max(depth_pct, _TD_HALF)


def fbd_ext_018_avg_undercut_pct_126d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Average undercut depth (% of 21d support) over trailing 126-day window."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, close, low, _TD_MON)
    depth_pct = _safe_div(support - low, support.replace(0, np.nan)).clip(lower=0).where(fb > 0, 0.0)
    cnt = (depth_pct > 0).astype(float)
    total = _rolling_sum(depth_pct, _TD_HALF)
    count = _rolling_sum(cnt, _TD_HALF).clip(lower=1)
    return _safe_div(total, count)


def fbd_ext_019_undercut_depth_atr_ratio_45d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Undercut depth on 45d FB events normalized by 21-day ATR."""
    support = _prior_low(low, 45)
    fb = _failed_breakdown_flag(close, high, low, 45)
    pierce = (support - low).clip(lower=0)
    atr21 = _atr(high, low, close, _TD_MON)
    ratio = _safe_div(pierce, atr21)
    return ratio.where(fb > 0, 0.0)


def fbd_ext_020_undercut_depth_atr_ratio_90d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Undercut depth on 90d FB events normalized by 21-day ATR."""
    support = _prior_low(low, 90)
    fb = _failed_breakdown_flag(close, high, low, 90)
    pierce = (support - low).clip(lower=0)
    atr21 = _atr(high, low, close, _TD_MON)
    ratio = _safe_div(pierce, atr21)
    return ratio.where(fb > 0, 0.0)


def fbd_ext_021_reclaim_pct_45d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Reclaim margin as % of 45-day support level on failed breakdown bars."""
    support = _prior_low(low, 45)
    fb = _failed_breakdown_flag(close, high, low, 45)
    margin_pct = _safe_div(close - support, support.replace(0, np.nan))
    return margin_pct.where(fb > 0, 0.0)


def fbd_ext_022_reclaim_pct_90d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Reclaim margin as % of 90-day support level on failed breakdown bars."""
    support = _prior_low(low, 90)
    fb = _failed_breakdown_flag(close, high, low, 90)
    margin_pct = _safe_div(close - support, support.replace(0, np.nan))
    return margin_pct.where(fb > 0, 0.0)


def fbd_ext_023_wick_below_support_pct_45d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Rejection wick below 45-day support as % of bar range on failed breakdowns."""
    support = _prior_low(low, 45)
    fb = _failed_breakdown_flag(close, high, low, 45)
    wick = (support - low).clip(lower=0)
    bar_range = (high - low).replace(0, np.nan)
    wick_pct = _safe_div(wick, bar_range)
    return wick_pct.where(fb > 0, 0.0)


def fbd_ext_024_wick_below_support_pct_90d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Rejection wick below 90-day support as % of bar range on failed breakdowns."""
    support = _prior_low(low, 90)
    fb = _failed_breakdown_flag(close, high, low, 90)
    wick = (support - low).clip(lower=0)
    bar_range = (high - low).replace(0, np.nan)
    wick_pct = _safe_div(wick, bar_range)
    return wick_pct.where(fb > 0, 0.0)


def fbd_ext_025_intrabar_reversal_pct_45d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Intrabar reversal on 45d FB: (close - low) / (high - low) — % recovery from intraday low."""
    fb = _failed_breakdown_flag(close, high, low, 45)
    bar_range = (high - low).replace(0, np.nan)
    reversal = _safe_div(close - low, bar_range)
    return reversal.where(fb > 0, 0.0)


# --- Group C (026-038): Event counts in non-standard windows ---

def fbd_ext_026_count_45d_fb_in_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 45-day failed-breakdown events in trailing 21 days."""
    return _rolling_sum(_failed_breakdown_flag(close, high, low, 45), _TD_MON)


def fbd_ext_027_count_45d_fb_in_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 45-day failed-breakdown events in trailing 63 days."""
    return _rolling_sum(_failed_breakdown_flag(close, high, low, 45), _TD_QTR)


def fbd_ext_028_count_90d_fb_in_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 90-day failed-breakdown events in trailing 63 days."""
    return _rolling_sum(_failed_breakdown_flag(close, high, low, 90), _TD_QTR)


def fbd_ext_029_count_90d_fb_in_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 90-day failed-breakdown events in trailing 252 days."""
    return _rolling_sum(_failed_breakdown_flag(close, high, low, 90), _TD_YEAR)


def fbd_ext_030_count_180d_fb_in_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 180-day failed-breakdown events in trailing 252 days."""
    return _rolling_sum(_failed_breakdown_flag(close, high, low, 180), _TD_YEAR)


def fbd_ext_031_count_7d_fb_in_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 7-day failed-breakdown events in trailing 21 days."""
    return _rolling_sum(_failed_breakdown_flag(close, high, low, 7), _TD_MON)


def fbd_ext_032_count_7d_fb_in_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 7-day failed-breakdown events in trailing 63 days."""
    return _rolling_sum(_failed_breakdown_flag(close, high, low, 7), _TD_QTR)


def fbd_ext_033_count_15d_fb_in_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 15-day failed-breakdown events in trailing 63 days."""
    return _rolling_sum(_failed_breakdown_flag(close, high, low, 15), _TD_QTR)


def fbd_ext_034_count_15d_fb_in_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 15-day failed-breakdown events in trailing 252 days."""
    return _rolling_sum(_failed_breakdown_flag(close, high, low, 15), _TD_YEAR)


def fbd_ext_035_count_30d_fb_in_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 30-day failed-breakdown events in trailing 63 days."""
    return _rolling_sum(_failed_breakdown_flag(close, high, low, 30), _TD_QTR)


def fbd_ext_036_count_30d_fb_in_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 30-day failed-breakdown events in trailing 252 days."""
    return _rolling_sum(_failed_breakdown_flag(close, high, low, 30), _TD_YEAR)


def fbd_ext_037_reclaim_rate_45d_window(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 45d-support undercuts reclaimed (FB) over trailing 63-day window."""
    fb = _failed_breakdown_flag(close, high, low, 45)
    support = _prior_low(low, 45)
    total_undercut = (low < support).astype(float)
    fb_cnt = _rolling_sum(fb, _TD_QTR)
    undercut_cnt = _rolling_sum(total_undercut, _TD_QTR).clip(lower=1)
    return _safe_div(fb_cnt, undercut_cnt)


def fbd_ext_038_reclaim_rate_90d_window(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 90d-support undercuts reclaimed (FB) over trailing 126-day window."""
    fb = _failed_breakdown_flag(close, high, low, 90)
    support = _prior_low(low, 90)
    total_undercut = (low < support).astype(float)
    fb_cnt = _rolling_sum(fb, _TD_HALF)
    undercut_cnt = _rolling_sum(total_undercut, _TD_HALF).clip(lower=1)
    return _safe_div(fb_cnt, undercut_cnt)


# --- Group D (039-050): Inter-breakdown interval and recency statistics ---

def fbd_ext_039_days_since_last_fb_7d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Trading days since the most recent 7-day failed-breakdown event."""
    fb = _failed_breakdown_flag(close, high, low, 7)
    not_fb = (fb == 0)
    group = fb.cumsum()
    out = not_fb.astype(int).groupby(group).cumsum().astype(float)
    return out.where(group > 0, np.nan)


def fbd_ext_040_days_since_last_fb_45d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Trading days since the most recent 45-day failed-breakdown event."""
    fb = _failed_breakdown_flag(close, high, low, 45)
    not_fb = (fb == 0)
    group = fb.cumsum()
    out = not_fb.astype(int).groupby(group).cumsum().astype(float)
    return out.where(group > 0, np.nan)


def fbd_ext_041_days_since_last_fb_90d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Trading days since the most recent 90-day failed-breakdown event."""
    fb = _failed_breakdown_flag(close, high, low, 90)
    not_fb = (fb == 0)
    group = fb.cumsum()
    out = not_fb.astype(int).groupby(group).cumsum().astype(float)
    return out.where(group > 0, np.nan)


def fbd_ext_042_inter_fb_21d_interval_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Rolling mean of days between consecutive 21d FB events over 252-day window."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    not_fb = (fb == 0)
    group = fb.cumsum()
    days_since = not_fb.astype(int).groupby(group).cumsum().astype(float)
    days_since = days_since.where(group > 0, np.nan)
    # Keep only values on FB bars (= interval length at each event)
    interval = days_since.shift(1).where(fb > 0, np.nan)
    return interval.rolling(_TD_YEAR, min_periods=2).mean()


def fbd_ext_043_inter_fb_21d_interval_std(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Rolling std of days between consecutive 21d FB events over 252-day window."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    not_fb = (fb == 0)
    group = fb.cumsum()
    days_since = not_fb.astype(int).groupby(group).cumsum().astype(float)
    days_since = days_since.where(group > 0, np.nan)
    interval = days_since.shift(1).where(fb > 0, np.nan)
    return interval.rolling(_TD_YEAR, min_periods=2).std()


def fbd_ext_044_fb_21d_within_10d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: a 21-day failed-breakdown occurred within the past 10 trading days."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), 10)
    return (cnt >= 1).astype(float)


def fbd_ext_045_fb_45d_within_21d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: a 45-day failed-breakdown occurred within the past 21 trading days."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, 45), _TD_MON)
    return (cnt >= 1).astype(float)


def fbd_ext_046_fb_90d_within_63d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: a 90-day failed-breakdown occurred within the past 63 trading days."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, 90), _TD_QTR)
    return (cnt >= 1).astype(float)


def fbd_ext_047_fb_21d_count_pct_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21d FB count (21d window) within trailing 126-day distribution."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_MON)
    return cnt.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)


def fbd_ext_048_fb_63d_count_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 63d FB count (63d window) within trailing 252-day distribution."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_QTR), _TD_QTR)
    return cnt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fbd_ext_049_fb_21d_count_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 21-day FB count relative to 126-day history."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_MON)
    m = _rolling_mean(cnt, _TD_HALF)
    s = _rolling_std(cnt, _TD_HALF)
    return _safe_div(cnt - m, s)


def fbd_ext_050_fb_45d_count_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 45-day FB count (45d window) relative to 252-day history."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, 45), 45)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    return _safe_div(cnt - m, s)


# --- Group E (051-062): OBV-based and volume-profile FB confirmations ---

def fbd_ext_051_obv_change_on_fb_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV single-day change on 21d FB bars (sign of OBV move at spring point)."""
    obv_delta = pd.Series(np.where(close > close.shift(1), volume,
                          np.where(close < close.shift(1), -volume, 0.0)),
                          index=close.index)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    return obv_delta.where(fb > 0, 0.0)


def fbd_ext_052_obv_change_on_fb_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV single-day change on 63d FB bars (volume at 63d-support spring)."""
    obv_delta = pd.Series(np.where(close > close.shift(1), volume,
                          np.where(close < close.shift(1), -volume, 0.0)),
                          index=close.index)
    fb = _failed_breakdown_flag(close, high, low, _TD_QTR)
    return obv_delta.where(fb > 0, 0.0)


def fbd_ext_053_cumvol_21d_on_fb_ratio(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day cumulative volume ratio (vs 63d avg period volume) on 21d FB days."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    vol21 = _rolling_sum(volume, _TD_MON)
    avg_vol63 = _rolling_mean(volume, _TD_QTR) * _TD_MON
    ratio = _safe_div(vol21, avg_vol63)
    return ratio.where(fb > 0, 0.0)


def fbd_ext_054_vol_3x_spike_fb_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Failed 21d breakdown where volume > 3x its 21-day average (panic capitulation)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (fb * (volume > 3.0 * avg_vol).astype(float))


def fbd_ext_055_vol_dryup_on_fb_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Failed 21d breakdown where volume < 50% of 21-day average (quiet spring, no selling)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (fb * (volume < 0.5 * avg_vol).astype(float))


def fbd_ext_056_vol_ratio_45d_fb(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on 45d failed breakdown bars as ratio to 21-day avg volume."""
    fb = _failed_breakdown_flag(close, high, low, 45)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol)
    return vol_ratio.where(fb > 0, np.nan).fillna(0.0)


def fbd_ext_057_vol_ratio_90d_fb(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on 90d failed breakdown bars as ratio to 21-day avg volume."""
    fb = _failed_breakdown_flag(close, high, low, 90)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol)
    return vol_ratio.where(fb > 0, np.nan).fillna(0.0)


def fbd_ext_058_vol_avg_45d_fb_63d_window(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume ratio on 45d FB events over trailing 63 days."""
    fb = _failed_breakdown_flag(close, high, low, 45)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol).where(fb > 0, np.nan)
    return vol_ratio.rolling(_TD_QTR, min_periods=1).mean().fillna(0.0)


def fbd_ext_059_vwap_support_gap_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Gap between 21d support and 21d VWAP proxy: support - VWAP (negative = support below VWAP)."""
    support = _prior_low(low, _TD_MON)
    vwap_num = _rolling_sum(close * volume, _TD_MON)
    vwap_den = _rolling_sum(volume, _TD_MON)
    vwap = _safe_div(vwap_num, vwap_den)
    return _safe_div(support - vwap, vwap.replace(0, np.nan))


def fbd_ext_060_fb_21d_below_vwap_flag(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Failed 21d breakdown where close is BELOW 21d VWAP proxy (weak spring)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    vwap_num = _rolling_sum(close * volume, _TD_MON)
    vwap_den = _rolling_sum(volume, _TD_MON)
    vwap = _safe_div(vwap_num, vwap_den)
    return (fb * (close < vwap).astype(float))


def fbd_ext_061_fb_21d_high_above_support_pct(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """High as % above 21d support on FB bars (upper wick strength of spring candle)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    support = _prior_low(low, _TD_MON)
    high_pct = _safe_div(high - support, support.replace(0, np.nan))
    return high_pct.where(fb > 0, 0.0)


def fbd_ext_062_fb_63d_high_above_support_pct(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """High as % above 63d support on FB bars (upper wick strength)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_QTR)
    support = _prior_low(low, _TD_QTR)
    high_pct = _safe_div(high - support, support.replace(0, np.nan))
    return high_pct.where(fb > 0, 0.0)


# --- Group F (063-075): Heikin-Ashi-derived, open-based, and composite new features ---

def fbd_ext_063_ha_close_above_ha_open_fb_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Failed 21d breakdown where Heikin-Ashi close > Heikin-Ashi open (HA bullish reclaim)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    ha_close = (open + high + low + close) / 4.0
    ha_open = (open.shift(1) + close.shift(1)) / 2.0
    ha_bull = (ha_close > ha_open).astype(float)
    return (fb * ha_bull)


def fbd_ext_064_open_above_support_21d_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: bar opened ABOVE 21d support (gap-up reclaim into support from below not applicable) — open >= support."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    return (fb * (open >= support).astype(float))


def fbd_ext_065_open_below_support_21d_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: FB bar opened BELOW 21d support but closed above (gap-down open, recovery close)."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    return (fb * (open < support).astype(float))


def fbd_ext_066_support_21d_vs_sma50(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day support as % above/below the 50-day SMA (support vs mid-term trend)."""
    support = _prior_low(low, _TD_MON)
    sma50 = _rolling_mean(close, 50)
    return _safe_div(support - sma50, sma50.replace(0, np.nan))


def fbd_ext_067_support_63d_vs_sma50(close: pd.Series, low: pd.Series) -> pd.Series:
    """63-day support as % above/below the 50-day SMA."""
    support = _prior_low(low, _TD_QTR)
    sma50 = _rolling_mean(close, 50)
    return _safe_div(support - sma50, sma50.replace(0, np.nan))


def fbd_ext_068_close_vs_support_45d_pct(close: pd.Series, low: pd.Series) -> pd.Series:
    """Close as % above/below prior 45-day support (positive = above)."""
    support = _prior_low(low, 45)
    return _safe_div(close - support, support.replace(0, np.nan))


def fbd_ext_069_close_vs_support_90d_pct(close: pd.Series, low: pd.Series) -> pd.Series:
    """Close as % above/below prior 90-day support."""
    support = _prior_low(low, 90)
    return _safe_div(close - support, support.replace(0, np.nan))


def fbd_ext_070_support_45d_pct_rank_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 45-day support level within its 252-day historical range."""
    support = _prior_low(low, 45)
    return support.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fbd_ext_071_support_90d_pct_rank_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 90-day support level within its 252-day historical range."""
    support = _prior_low(low, 90)
    return support.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fbd_ext_072_fb_21d_body_top_half_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Failed 21d breakdown where close is in top quartile of bar's high-low range."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    bar_range = (high - low).replace(0, np.nan)
    in_top_25 = ((close - low) / bar_range >= 0.75).astype(float)
    return (fb * in_top_25)


def fbd_ext_073_fb_capitulation_composite_45d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite bear-trap quality score for 45d FB: undercut_pct + vol_ratio + reclaim_pct."""
    support = _prior_low(low, 45)
    fb = _failed_breakdown_flag(close, high, low, 45)
    depth = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_r = _safe_div(volume, avg_vol).fillna(1).clip(upper=5)
    reclaim = _safe_div((close - support).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    score = (depth + vol_r / 5.0 + reclaim).where(fb > 0, 0.0)
    return score


def fbd_ext_074_fb_21d_cluster_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Pct rank of 21d FB count (21d window) within 252-day dist — expanding version."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_MON)
    return cnt.expanding(min_periods=_TD_MON).rank(pct=True)


def fbd_ext_075_support_21d_63d_spread_pct(close: pd.Series, low: pd.Series) -> pd.Series:
    """Spread between 21d and 63d support levels as % of 63d support (compression gauge)."""
    s21 = _prior_low(low, _TD_MON)
    s63 = _prior_low(low, _TD_QTR)
    return _safe_div(s63 - s21, s63.replace(0, np.nan))


# ── Registry ──────────────────────────────────────────────────────────────────

FAILED_BREAKDOWN_EXTENDED_REGISTRY_001_075 = {
    "fbd_ext_001_flag_3d": {"inputs": ["close", "high", "low"], "func": fbd_ext_001_flag_3d},
    "fbd_ext_002_flag_7d": {"inputs": ["close", "high", "low"], "func": fbd_ext_002_flag_7d},
    "fbd_ext_003_flag_15d": {"inputs": ["close", "high", "low"], "func": fbd_ext_003_flag_15d},
    "fbd_ext_004_flag_30d": {"inputs": ["close", "high", "low"], "func": fbd_ext_004_flag_30d},
    "fbd_ext_005_flag_45d": {"inputs": ["close", "high", "low"], "func": fbd_ext_005_flag_45d},
    "fbd_ext_006_flag_90d": {"inputs": ["close", "high", "low"], "func": fbd_ext_006_flag_90d},
    "fbd_ext_007_flag_180d": {"inputs": ["close", "high", "low"], "func": fbd_ext_007_flag_180d},
    "fbd_ext_008_flag_any_3_levels": {"inputs": ["close", "high", "low"], "func": fbd_ext_008_flag_any_3_levels},
    "fbd_ext_009_flag_45d_bull_candle": {"inputs": ["close", "high", "low", "open"], "func": fbd_ext_009_flag_45d_bull_candle},
    "fbd_ext_010_flag_90d_high_volume": {"inputs": ["close", "high", "low", "volume"], "func": fbd_ext_010_flag_90d_high_volume},
    "fbd_ext_011_flag_180d_near_52wk_low": {"inputs": ["close", "high", "low"], "func": fbd_ext_011_flag_180d_near_52wk_low},
    "fbd_ext_012_consecutive_fb_streak_7d": {"inputs": ["close", "high", "low"], "func": fbd_ext_012_consecutive_fb_streak_7d},
    "fbd_ext_013_undercut_depth_pct_7d": {"inputs": ["close", "low"], "func": fbd_ext_013_undercut_depth_pct_7d},
    "fbd_ext_014_undercut_depth_pct_45d": {"inputs": ["close", "low"], "func": fbd_ext_014_undercut_depth_pct_45d},
    "fbd_ext_015_undercut_depth_pct_90d": {"inputs": ["close", "low"], "func": fbd_ext_015_undercut_depth_pct_90d},
    "fbd_ext_016_undercut_depth_pct_180d": {"inputs": ["close", "low"], "func": fbd_ext_016_undercut_depth_pct_180d},
    "fbd_ext_017_max_undercut_pct_126d": {"inputs": ["close", "low"], "func": fbd_ext_017_max_undercut_pct_126d},
    "fbd_ext_018_avg_undercut_pct_126d": {"inputs": ["close", "low"], "func": fbd_ext_018_avg_undercut_pct_126d},
    "fbd_ext_019_undercut_depth_atr_ratio_45d": {"inputs": ["close", "high", "low"], "func": fbd_ext_019_undercut_depth_atr_ratio_45d},
    "fbd_ext_020_undercut_depth_atr_ratio_90d": {"inputs": ["close", "high", "low"], "func": fbd_ext_020_undercut_depth_atr_ratio_90d},
    "fbd_ext_021_reclaim_pct_45d": {"inputs": ["close", "high", "low"], "func": fbd_ext_021_reclaim_pct_45d},
    "fbd_ext_022_reclaim_pct_90d": {"inputs": ["close", "high", "low"], "func": fbd_ext_022_reclaim_pct_90d},
    "fbd_ext_023_wick_below_support_pct_45d": {"inputs": ["close", "high", "low"], "func": fbd_ext_023_wick_below_support_pct_45d},
    "fbd_ext_024_wick_below_support_pct_90d": {"inputs": ["close", "high", "low"], "func": fbd_ext_024_wick_below_support_pct_90d},
    "fbd_ext_025_intrabar_reversal_pct_45d": {"inputs": ["close", "high", "low", "open"], "func": fbd_ext_025_intrabar_reversal_pct_45d},
    "fbd_ext_026_count_45d_fb_in_21d": {"inputs": ["close", "high", "low"], "func": fbd_ext_026_count_45d_fb_in_21d},
    "fbd_ext_027_count_45d_fb_in_63d": {"inputs": ["close", "high", "low"], "func": fbd_ext_027_count_45d_fb_in_63d},
    "fbd_ext_028_count_90d_fb_in_63d": {"inputs": ["close", "high", "low"], "func": fbd_ext_028_count_90d_fb_in_63d},
    "fbd_ext_029_count_90d_fb_in_252d": {"inputs": ["close", "high", "low"], "func": fbd_ext_029_count_90d_fb_in_252d},
    "fbd_ext_030_count_180d_fb_in_252d": {"inputs": ["close", "high", "low"], "func": fbd_ext_030_count_180d_fb_in_252d},
    "fbd_ext_031_count_7d_fb_in_21d": {"inputs": ["close", "high", "low"], "func": fbd_ext_031_count_7d_fb_in_21d},
    "fbd_ext_032_count_7d_fb_in_63d": {"inputs": ["close", "high", "low"], "func": fbd_ext_032_count_7d_fb_in_63d},
    "fbd_ext_033_count_15d_fb_in_63d": {"inputs": ["close", "high", "low"], "func": fbd_ext_033_count_15d_fb_in_63d},
    "fbd_ext_034_count_15d_fb_in_252d": {"inputs": ["close", "high", "low"], "func": fbd_ext_034_count_15d_fb_in_252d},
    "fbd_ext_035_count_30d_fb_in_63d": {"inputs": ["close", "high", "low"], "func": fbd_ext_035_count_30d_fb_in_63d},
    "fbd_ext_036_count_30d_fb_in_252d": {"inputs": ["close", "high", "low"], "func": fbd_ext_036_count_30d_fb_in_252d},
    "fbd_ext_037_reclaim_rate_45d_window": {"inputs": ["close", "high", "low"], "func": fbd_ext_037_reclaim_rate_45d_window},
    "fbd_ext_038_reclaim_rate_90d_window": {"inputs": ["close", "high", "low"], "func": fbd_ext_038_reclaim_rate_90d_window},
    "fbd_ext_039_days_since_last_fb_7d": {"inputs": ["close", "high", "low"], "func": fbd_ext_039_days_since_last_fb_7d},
    "fbd_ext_040_days_since_last_fb_45d": {"inputs": ["close", "high", "low"], "func": fbd_ext_040_days_since_last_fb_45d},
    "fbd_ext_041_days_since_last_fb_90d": {"inputs": ["close", "high", "low"], "func": fbd_ext_041_days_since_last_fb_90d},
    "fbd_ext_042_inter_fb_21d_interval_mean": {"inputs": ["close", "high", "low"], "func": fbd_ext_042_inter_fb_21d_interval_mean},
    "fbd_ext_043_inter_fb_21d_interval_std": {"inputs": ["close", "high", "low"], "func": fbd_ext_043_inter_fb_21d_interval_std},
    "fbd_ext_044_fb_21d_within_10d_flag": {"inputs": ["close", "high", "low"], "func": fbd_ext_044_fb_21d_within_10d_flag},
    "fbd_ext_045_fb_45d_within_21d_flag": {"inputs": ["close", "high", "low"], "func": fbd_ext_045_fb_45d_within_21d_flag},
    "fbd_ext_046_fb_90d_within_63d_flag": {"inputs": ["close", "high", "low"], "func": fbd_ext_046_fb_90d_within_63d_flag},
    "fbd_ext_047_fb_21d_count_pct_rank_126d": {"inputs": ["close", "high", "low"], "func": fbd_ext_047_fb_21d_count_pct_rank_126d},
    "fbd_ext_048_fb_63d_count_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": fbd_ext_048_fb_63d_count_pct_rank_252d},
    "fbd_ext_049_fb_21d_count_zscore_126d": {"inputs": ["close", "high", "low"], "func": fbd_ext_049_fb_21d_count_zscore_126d},
    "fbd_ext_050_fb_45d_count_zscore_252d": {"inputs": ["close", "high", "low"], "func": fbd_ext_050_fb_45d_count_zscore_252d},
    "fbd_ext_051_obv_change_on_fb_21d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_ext_051_obv_change_on_fb_21d},
    "fbd_ext_052_obv_change_on_fb_63d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_ext_052_obv_change_on_fb_63d},
    "fbd_ext_053_cumvol_21d_on_fb_ratio": {"inputs": ["close", "high", "low", "volume"], "func": fbd_ext_053_cumvol_21d_on_fb_ratio},
    "fbd_ext_054_vol_3x_spike_fb_21d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_ext_054_vol_3x_spike_fb_21d},
    "fbd_ext_055_vol_dryup_on_fb_21d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_ext_055_vol_dryup_on_fb_21d},
    "fbd_ext_056_vol_ratio_45d_fb": {"inputs": ["close", "high", "low", "volume"], "func": fbd_ext_056_vol_ratio_45d_fb},
    "fbd_ext_057_vol_ratio_90d_fb": {"inputs": ["close", "high", "low", "volume"], "func": fbd_ext_057_vol_ratio_90d_fb},
    "fbd_ext_058_vol_avg_45d_fb_63d_window": {"inputs": ["close", "high", "low", "volume"], "func": fbd_ext_058_vol_avg_45d_fb_63d_window},
    "fbd_ext_059_vwap_support_gap_21d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_ext_059_vwap_support_gap_21d},
    "fbd_ext_060_fb_21d_below_vwap_flag": {"inputs": ["close", "high", "low", "volume"], "func": fbd_ext_060_fb_21d_below_vwap_flag},
    "fbd_ext_061_fb_21d_high_above_support_pct": {"inputs": ["close", "high", "low"], "func": fbd_ext_061_fb_21d_high_above_support_pct},
    "fbd_ext_062_fb_63d_high_above_support_pct": {"inputs": ["close", "high", "low"], "func": fbd_ext_062_fb_63d_high_above_support_pct},
    "fbd_ext_063_ha_close_above_ha_open_fb_21d": {"inputs": ["close", "high", "low", "open"], "func": fbd_ext_063_ha_close_above_ha_open_fb_21d},
    "fbd_ext_064_open_above_support_21d_flag": {"inputs": ["close", "high", "low", "open"], "func": fbd_ext_064_open_above_support_21d_flag},
    "fbd_ext_065_open_below_support_21d_flag": {"inputs": ["close", "high", "low", "open"], "func": fbd_ext_065_open_below_support_21d_flag},
    "fbd_ext_066_support_21d_vs_sma50": {"inputs": ["close", "low"], "func": fbd_ext_066_support_21d_vs_sma50},
    "fbd_ext_067_support_63d_vs_sma50": {"inputs": ["close", "low"], "func": fbd_ext_067_support_63d_vs_sma50},
    "fbd_ext_068_close_vs_support_45d_pct": {"inputs": ["close", "low"], "func": fbd_ext_068_close_vs_support_45d_pct},
    "fbd_ext_069_close_vs_support_90d_pct": {"inputs": ["close", "low"], "func": fbd_ext_069_close_vs_support_90d_pct},
    "fbd_ext_070_support_45d_pct_rank_252d": {"inputs": ["close", "low"], "func": fbd_ext_070_support_45d_pct_rank_252d},
    "fbd_ext_071_support_90d_pct_rank_252d": {"inputs": ["close", "low"], "func": fbd_ext_071_support_90d_pct_rank_252d},
    "fbd_ext_072_fb_21d_body_top_half_flag": {"inputs": ["close", "high", "low", "open"], "func": fbd_ext_072_fb_21d_body_top_half_flag},
    "fbd_ext_073_fb_capitulation_composite_45d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_ext_073_fb_capitulation_composite_45d},
    "fbd_ext_074_fb_21d_cluster_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": fbd_ext_074_fb_21d_cluster_pct_rank_252d},
    "fbd_ext_075_support_21d_63d_spread_pct": {"inputs": ["close", "low"], "func": fbd_ext_075_support_21d_63d_spread_pct},
}
