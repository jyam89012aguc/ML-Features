"""
50_failed_breakdown — Extended 3rd Derivatives (Features fbd_extdrv3_001-025)
Domain: rate of change of extended 2nd-derivative failed-breakdown features —
        acceleration of velocity in ext-window spring behavior.
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _prior_low(low: pd.Series, w: int) -> pd.Series:
    """Rolling min of PRIOR bars — strictly backward-looking."""
    return low.shift(1).rolling(w, min_periods=max(1, w // 2)).min()


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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def fbd_extdrv3_001_fb_7d_count_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 7d FB count in 21d window (jerk of fast-spring frequency)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, 7), _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_extdrv3_002_fb_45d_count_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 45d FB count in 63d window (jerk in medium-spring density)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, 45), _TD_QTR)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_extdrv3_003_fb_90d_count_252d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21d-velocity of 90d FB count in 252d window."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, 90), _TD_YEAR)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fbd_extdrv3_004_undercut_depth_45d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of smoothed 45d undercut depth % (jerk in pierce severity)."""
    support = _prior_low(low, 45)
    fb = _failed_breakdown_flag(close, high, low, 45)
    depth = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    smoothed = _rolling_mean(depth.where(fb > 0, 0.0), _TD_MON)
    vel = smoothed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_extdrv3_005_undercut_depth_90d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21d-velocity of smoothed 90d undercut depth %."""
    support = _prior_low(low, 90)
    fb = _failed_breakdown_flag(close, high, low, 90)
    depth = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    smoothed = _rolling_mean(depth.where(fb > 0, 0.0), _TD_QTR)
    vel21 = smoothed.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fbd_extdrv3_006_reclaim_rate_45d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 45d reclaim rate (acceleration of 45d spring success)."""
    fb = _failed_breakdown_flag(close, high, low, 45)
    support = _prior_low(low, 45)
    total_undercut = (low < support).astype(float)
    rate = _safe_div(
        _rolling_sum(fb, _TD_QTR),
        _rolling_sum(total_undercut, _TD_QTR).clip(lower=1)
    )
    vel = rate.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_extdrv3_007_reclaim_rate_90d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21d-velocity of 90d reclaim rate (jerk in 90d spring success trend)."""
    fb = _failed_breakdown_flag(close, high, low, 90)
    support = _prior_low(low, 90)
    total_undercut = (low < support).astype(float)
    rate = _safe_div(
        _rolling_sum(fb, _TD_HALF),
        _rolling_sum(total_undercut, _TD_HALF).clip(lower=1)
    )
    vel21 = rate.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fbd_extdrv3_008_close_vs_support_45d_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of close/45d-support ratio (jerk in 45d floor distance)."""
    support = _prior_low(low, 45)
    ratio = _safe_div(close, support.replace(0, np.nan))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_extdrv3_009_close_vs_support_90d_21d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21d-velocity of close/90d-support ratio."""
    support = _prior_low(low, 90)
    ratio = _safe_div(close, support.replace(0, np.nan))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fbd_extdrv3_010_support_45d_slope_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of OLS slope of 45d support (jerk in 45d floor acceleration)."""
    support = _prior_low(low, 45)
    slp = _linslope(support, _TD_MON)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_extdrv3_011_support_90d_slope_21d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21d-velocity of OLS slope of 90d support."""
    support = _prior_low(low, 90)
    slp = _linslope(support, _TD_MON)
    vel21 = slp.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fbd_extdrv3_012_fb_45d_composite_score_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of rolling-mean 45d FB composite score (jerk in trap quality)."""
    support = _prior_low(low, 45)
    fb = _failed_breakdown_flag(close, high, low, 45)
    depth = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_r = _safe_div(volume, avg_vol).fillna(1).clip(upper=5)
    reclaim = _safe_div((close - support).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    score = (depth + vol_r / 5.0 + reclaim).where(fb > 0, 0.0)
    smoothed = _rolling_mean(score, _TD_QTR)
    vel = smoothed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_extdrv3_013_vol_ratio_45d_fb_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of smoothed volume ratio on 45d FB (jerk in spring conviction)."""
    fb = _failed_breakdown_flag(close, high, low, 45)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol).fillna(1)
    smoothed = _rolling_mean(vol_ratio.where(fb > 0, 0.0), _TD_MON)
    vel = smoothed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_extdrv3_014_vol_ratio_90d_fb_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21d-velocity of smoothed volume ratio on 90d FB events."""
    fb = _failed_breakdown_flag(close, high, low, 90)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol).fillna(1)
    smoothed = _rolling_mean(vol_ratio.where(fb > 0, 0.0), _TD_QTR)
    vel21 = smoothed.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fbd_extdrv3_015_support_45d_pct_rank_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of percentile rank of 45d support (jerk in relative floor level)."""
    support = _prior_low(low, 45)
    rank = support.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_extdrv3_016_support_90d_pct_rank_21d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21d-velocity of percentile rank of 90d support."""
    support = _prior_low(low, 90)
    rank = support.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel21 = rank.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fbd_extdrv3_017_fb_21d_count_zscore_126d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of z-score of 21d FB count vs 126d (jerk in relative spring frequency)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_MON)
    m = _rolling_mean(cnt, _TD_HALF)
    s = _rolling_std(cnt, _TD_HALF)
    z = _safe_div(cnt - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_extdrv3_018_fb_45d_count_zscore_252d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of z-score of 45d FB count vs 252d history."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, 45), 45)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    z = _safe_div(cnt - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_extdrv3_019_obv_on_fb_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of smoothed OBV-delta on 21d FB (jerk in OBV spring conviction)."""
    obv_delta = pd.Series(np.where(close > close.shift(1), volume,
                          np.where(close < close.shift(1), -volume, 0.0)),
                          index=close.index)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    smoothed = _rolling_mean(obv_delta.where(fb > 0, 0.0), _TD_MON)
    vel = smoothed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_extdrv3_020_vwap_support_gap_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of VWAP-support gap ratio (jerk in support vs price center)."""
    support = _prior_low(low, _TD_MON)
    vwap_num = _rolling_sum(close * volume, _TD_MON)
    vwap_den = _rolling_sum(volume, _TD_MON)
    vwap = _safe_div(vwap_num, vwap_den)
    gap = _safe_div(support - vwap, vwap.replace(0, np.nan))
    vel = gap.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_extdrv3_021_reclaim_pct_45d_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of smoothed reclaim-margin-pct on 45d FB (slope change rate)."""
    support = _prior_low(low, 45)
    fb = _failed_breakdown_flag(close, high, low, 45)
    margin_pct = _safe_div(close - support, support.replace(0, np.nan)).fillna(0)
    smoothed = _rolling_mean(margin_pct.where(fb > 0, 0.0), _TD_MON)
    slp = _linslope(smoothed, _TD_MON)
    return slp.diff(_TD_WEEK)


def fbd_extdrv3_022_support_21d_63d_spread_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of support spread (21d vs 63d) — jerk in compression velocity."""
    s21 = _prior_low(low, _TD_MON)
    s63 = _prior_low(low, _TD_QTR)
    spread = _safe_div(s63 - s21, s63.replace(0, np.nan))
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_extdrv3_023_fb_7d_count_21d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21d-velocity of 7d FB count in 21d window (jerk in fast-spring monthly trend)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, 7), _TD_MON)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fbd_extdrv3_024_wick_pct_45d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of smoothed wick-below-support-pct on 45d FB (jerk in candle structure)."""
    support = _prior_low(low, 45)
    fb = _failed_breakdown_flag(close, high, low, 45)
    wick = (support - low).clip(lower=0)
    bar_range = (high - low).replace(0, np.nan)
    wick_pct = _safe_div(wick, bar_range).fillna(0)
    smoothed = _rolling_mean(wick_pct.where(fb > 0, 0.0), _TD_MON)
    vel = smoothed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_extdrv3_025_fb_180d_count_252d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21d-velocity of 180d FB count in 252d window (jerk in ultra-long spring trend)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, 180), _TD_YEAR)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

FAILED_BREAKDOWN_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "fbd_extdrv3_001_fb_7d_count_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv3_001_fb_7d_count_21d_5d_diff_5d_diff},
    "fbd_extdrv3_002_fb_45d_count_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv3_002_fb_45d_count_63d_5d_diff_5d_diff},
    "fbd_extdrv3_003_fb_90d_count_252d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv3_003_fb_90d_count_252d_21d_diff_5d_diff},
    "fbd_extdrv3_004_undercut_depth_45d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv3_004_undercut_depth_45d_5d_diff_5d_diff},
    "fbd_extdrv3_005_undercut_depth_90d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv3_005_undercut_depth_90d_21d_diff_5d_diff},
    "fbd_extdrv3_006_reclaim_rate_45d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv3_006_reclaim_rate_45d_5d_diff_5d_diff},
    "fbd_extdrv3_007_reclaim_rate_90d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv3_007_reclaim_rate_90d_21d_diff_5d_diff},
    "fbd_extdrv3_008_close_vs_support_45d_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": fbd_extdrv3_008_close_vs_support_45d_5d_diff_5d_diff},
    "fbd_extdrv3_009_close_vs_support_90d_21d_diff_5d_diff": {"inputs": ["close", "low"], "func": fbd_extdrv3_009_close_vs_support_90d_21d_diff_5d_diff},
    "fbd_extdrv3_010_support_45d_slope_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": fbd_extdrv3_010_support_45d_slope_5d_diff_5d_diff},
    "fbd_extdrv3_011_support_90d_slope_21d_diff_5d_diff": {"inputs": ["close", "low"], "func": fbd_extdrv3_011_support_90d_slope_21d_diff_5d_diff},
    "fbd_extdrv3_012_fb_45d_composite_score_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": fbd_extdrv3_012_fb_45d_composite_score_5d_diff_5d_diff},
    "fbd_extdrv3_013_vol_ratio_45d_fb_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": fbd_extdrv3_013_vol_ratio_45d_fb_5d_diff_5d_diff},
    "fbd_extdrv3_014_vol_ratio_90d_fb_21d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": fbd_extdrv3_014_vol_ratio_90d_fb_21d_diff_5d_diff},
    "fbd_extdrv3_015_support_45d_pct_rank_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": fbd_extdrv3_015_support_45d_pct_rank_5d_diff_5d_diff},
    "fbd_extdrv3_016_support_90d_pct_rank_21d_diff_5d_diff": {"inputs": ["close", "low"], "func": fbd_extdrv3_016_support_90d_pct_rank_21d_diff_5d_diff},
    "fbd_extdrv3_017_fb_21d_count_zscore_126d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv3_017_fb_21d_count_zscore_126d_5d_diff_5d_diff},
    "fbd_extdrv3_018_fb_45d_count_zscore_252d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv3_018_fb_45d_count_zscore_252d_5d_diff_5d_diff},
    "fbd_extdrv3_019_obv_on_fb_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": fbd_extdrv3_019_obv_on_fb_21d_5d_diff_5d_diff},
    "fbd_extdrv3_020_vwap_support_gap_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": fbd_extdrv3_020_vwap_support_gap_5d_diff_5d_diff},
    "fbd_extdrv3_021_reclaim_pct_45d_slope_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv3_021_reclaim_pct_45d_slope_5d_diff},
    "fbd_extdrv3_022_support_21d_63d_spread_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": fbd_extdrv3_022_support_21d_63d_spread_5d_diff_5d_diff},
    "fbd_extdrv3_023_fb_7d_count_21d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv3_023_fb_7d_count_21d_21d_diff_5d_diff},
    "fbd_extdrv3_024_wick_pct_45d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv3_024_wick_pct_45d_5d_diff_5d_diff},
    "fbd_extdrv3_025_fb_180d_count_252d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv3_025_fb_180d_count_252d_21d_diff_5d_diff},
}
