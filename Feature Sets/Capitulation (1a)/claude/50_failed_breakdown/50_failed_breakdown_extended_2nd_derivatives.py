"""
50_failed_breakdown — Extended 2nd Derivatives (Features fbd_extdrv2_001-025)
Domain: rate of change of extended base failed-breakdown feature concepts —
        velocity of ext-window spring behavior (7d/15d/30d/45d/90d/180d lookbacks),
        OBV spring velocity, VWAP-gap velocity, composite score velocity.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def fbd_extdrv2_001_fb_7d_count_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 7-day FB count in 21d window (velocity of fast-spring frequency)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, 7), _TD_MON)
    return cnt.diff(_TD_WEEK)


def fbd_extdrv2_002_fb_45d_count_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 45-day FB count in 63d window."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, 45), _TD_QTR)
    return cnt.diff(_TD_WEEK)


def fbd_extdrv2_003_fb_90d_count_252d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 90-day FB count in 252d window (monthly velocity of deep-support springs)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, 90), _TD_YEAR)
    return cnt.diff(_TD_MON)


def fbd_extdrv2_004_undercut_depth_pct_45d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of smoothed 45d undercut depth % (velocity of pierce severity)."""
    support = _prior_low(low, 45)
    fb = _failed_breakdown_flag(close, high, low, 45)
    depth = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    smoothed = _rolling_mean(depth.where(fb > 0, 0.0), _TD_MON)
    return smoothed.diff(_TD_WEEK)


def fbd_extdrv2_005_undercut_depth_pct_90d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of smoothed 90d undercut depth % (monthly change in pierce severity)."""
    support = _prior_low(low, 90)
    fb = _failed_breakdown_flag(close, high, low, 90)
    depth = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    smoothed = _rolling_mean(depth.where(fb > 0, 0.0), _TD_QTR)
    return smoothed.diff(_TD_MON)


def fbd_extdrv2_006_reclaim_rate_45d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 45d-window reclaim rate (fraction of 45d undercuts becoming FB)."""
    fb = _failed_breakdown_flag(close, high, low, 45)
    support = _prior_low(low, 45)
    total_undercut = (low < support).astype(float)
    rate = _safe_div(
        _rolling_sum(fb, _TD_QTR),
        _rolling_sum(total_undercut, _TD_QTR).clip(lower=1)
    )
    return rate.diff(_TD_WEEK)


def fbd_extdrv2_007_reclaim_rate_90d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of the 90d-window reclaim rate."""
    fb = _failed_breakdown_flag(close, high, low, 90)
    support = _prior_low(low, 90)
    total_undercut = (low < support).astype(float)
    rate = _safe_div(
        _rolling_sum(fb, _TD_HALF),
        _rolling_sum(total_undercut, _TD_HALF).clip(lower=1)
    )
    return rate.diff(_TD_MON)


def fbd_extdrv2_008_close_vs_support_45d_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of close/45d-support ratio (velocity of distance from 45d floor)."""
    support = _prior_low(low, 45)
    ratio = _safe_div(close, support.replace(0, np.nan))
    return ratio.diff(_TD_WEEK)


def fbd_extdrv2_009_close_vs_support_90d_21d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of close/90d-support ratio (monthly velocity of distance from 90d floor)."""
    support = _prior_low(low, 90)
    ratio = _safe_div(close, support.replace(0, np.nan))
    return ratio.diff(_TD_MON)


def fbd_extdrv2_010_support_45d_slope_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 45d support over 21 days (acceleration of 45d floor)."""
    support = _prior_low(low, 45)
    slp = _linslope(support, _TD_MON)
    return slp.diff(_TD_WEEK)


def fbd_extdrv2_011_support_90d_slope_21d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of OLS slope of 90d support over 21 days."""
    support = _prior_low(low, 90)
    slp = _linslope(support, _TD_MON)
    return slp.diff(_TD_MON)


def fbd_extdrv2_012_fb_45d_composite_score_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of rolling-mean 45d FB composite bear-trap score (velocity of trap quality)."""
    support = _prior_low(low, 45)
    fb = _failed_breakdown_flag(close, high, low, 45)
    depth = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_r = _safe_div(volume, avg_vol).fillna(1).clip(upper=5)
    reclaim = _safe_div((close - support).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    score = (depth + vol_r / 5.0 + reclaim).where(fb > 0, 0.0)
    smoothed = _rolling_mean(score, _TD_QTR)
    return smoothed.diff(_TD_WEEK)


def fbd_extdrv2_013_vol_ratio_45d_fb_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of smoothed volume ratio on 45d FB events."""
    fb = _failed_breakdown_flag(close, high, low, 45)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol).fillna(1)
    smoothed = _rolling_mean(vol_ratio.where(fb > 0, 0.0), _TD_MON)
    return smoothed.diff(_TD_WEEK)


def fbd_extdrv2_014_vol_ratio_90d_fb_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of smoothed volume ratio on 90d FB events."""
    fb = _failed_breakdown_flag(close, high, low, 90)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol).fillna(1)
    smoothed = _rolling_mean(vol_ratio.where(fb > 0, 0.0), _TD_QTR)
    return smoothed.diff(_TD_MON)


def fbd_extdrv2_015_support_45d_pct_rank_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of percentile rank of 45d support within 252-day range."""
    support = _prior_low(low, 45)
    rank = support.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_WEEK)


def fbd_extdrv2_016_support_90d_pct_rank_21d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of percentile rank of 90d support within 252-day range."""
    support = _prior_low(low, 90)
    rank = support.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_MON)


def fbd_extdrv2_017_fb_21d_count_zscore_126d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of z-score of 21d FB count vs 126-day history."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_MON)
    m = _rolling_mean(cnt, _TD_HALF)
    s = _rolling_std(cnt, _TD_HALF)
    z = _safe_div(cnt - m, s)
    return z.diff(_TD_WEEK)


def fbd_extdrv2_018_fb_45d_count_zscore_252d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of z-score of 45d FB count vs 252-day history."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, 45), 45)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    z = _safe_div(cnt - m, s)
    return z.diff(_TD_WEEK)


def fbd_extdrv2_019_obv_on_fb_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of smoothed OBV-delta on 21d FB bars (velocity of OBV conviction at spring)."""
    obv_delta = pd.Series(np.where(close > close.shift(1), volume,
                          np.where(close < close.shift(1), -volume, 0.0)),
                          index=close.index)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    smoothed = _rolling_mean(obv_delta.where(fb > 0, 0.0), _TD_MON)
    return smoothed.diff(_TD_WEEK)


def fbd_extdrv2_020_vwap_support_gap_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of VWAP-support gap ratio (velocity of support vs price center)."""
    support = _prior_low(low, _TD_MON)
    vwap_num = _rolling_sum(close * volume, _TD_MON)
    vwap_den = _rolling_sum(volume, _TD_MON)
    vwap = _safe_div(vwap_num, vwap_den)
    gap = _safe_div(support - vwap, vwap.replace(0, np.nan))
    return gap.diff(_TD_WEEK)


def fbd_extdrv2_021_reclaim_pct_45d_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of smoothed reclaim-margin-pct on 45d FB bars."""
    support = _prior_low(low, 45)
    fb = _failed_breakdown_flag(close, high, low, 45)
    margin_pct = _safe_div(close - support, support.replace(0, np.nan)).fillna(0)
    smoothed = _rolling_mean(margin_pct.where(fb > 0, 0.0), _TD_MON)
    return _linslope(smoothed, _TD_MON)


def fbd_extdrv2_022_support_21d_63d_spread_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (63d support - 21d support) / 63d support (velocity of support compression)."""
    s21 = _prior_low(low, _TD_MON)
    s63 = _prior_low(low, _TD_QTR)
    spread = _safe_div(s63 - s21, s63.replace(0, np.nan))
    return spread.diff(_TD_WEEK)


def fbd_extdrv2_023_fb_7d_count_21d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 7-day FB count in 21d window (monthly velocity of fast-spring cluster)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, 7), _TD_MON)
    return cnt.diff(_TD_MON)


def fbd_extdrv2_024_wick_pct_45d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of smoothed wick-below-support-pct on 45d FB bars."""
    support = _prior_low(low, 45)
    fb = _failed_breakdown_flag(close, high, low, 45)
    wick = (support - low).clip(lower=0)
    bar_range = (high - low).replace(0, np.nan)
    wick_pct = _safe_div(wick, bar_range).fillna(0)
    smoothed = _rolling_mean(wick_pct.where(fb > 0, 0.0), _TD_MON)
    return smoothed.diff(_TD_WEEK)


def fbd_extdrv2_025_fb_180d_count_252d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 180-day FB count in 252-day window (velocity of ultra-long spring events)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, 180), _TD_YEAR)
    return cnt.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

FAILED_BREAKDOWN_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "fbd_extdrv2_001_fb_7d_count_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv2_001_fb_7d_count_21d_5d_diff},
    "fbd_extdrv2_002_fb_45d_count_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv2_002_fb_45d_count_63d_5d_diff},
    "fbd_extdrv2_003_fb_90d_count_252d_21d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv2_003_fb_90d_count_252d_21d_diff},
    "fbd_extdrv2_004_undercut_depth_pct_45d_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv2_004_undercut_depth_pct_45d_5d_diff},
    "fbd_extdrv2_005_undercut_depth_pct_90d_21d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv2_005_undercut_depth_pct_90d_21d_diff},
    "fbd_extdrv2_006_reclaim_rate_45d_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv2_006_reclaim_rate_45d_5d_diff},
    "fbd_extdrv2_007_reclaim_rate_90d_21d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv2_007_reclaim_rate_90d_21d_diff},
    "fbd_extdrv2_008_close_vs_support_45d_5d_diff": {"inputs": ["close", "low"], "func": fbd_extdrv2_008_close_vs_support_45d_5d_diff},
    "fbd_extdrv2_009_close_vs_support_90d_21d_diff": {"inputs": ["close", "low"], "func": fbd_extdrv2_009_close_vs_support_90d_21d_diff},
    "fbd_extdrv2_010_support_45d_slope_5d_diff": {"inputs": ["close", "low"], "func": fbd_extdrv2_010_support_45d_slope_5d_diff},
    "fbd_extdrv2_011_support_90d_slope_21d_diff": {"inputs": ["close", "low"], "func": fbd_extdrv2_011_support_90d_slope_21d_diff},
    "fbd_extdrv2_012_fb_45d_composite_score_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": fbd_extdrv2_012_fb_45d_composite_score_5d_diff},
    "fbd_extdrv2_013_vol_ratio_45d_fb_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": fbd_extdrv2_013_vol_ratio_45d_fb_5d_diff},
    "fbd_extdrv2_014_vol_ratio_90d_fb_21d_diff": {"inputs": ["close", "high", "low", "volume"], "func": fbd_extdrv2_014_vol_ratio_90d_fb_21d_diff},
    "fbd_extdrv2_015_support_45d_pct_rank_5d_diff": {"inputs": ["close", "low"], "func": fbd_extdrv2_015_support_45d_pct_rank_5d_diff},
    "fbd_extdrv2_016_support_90d_pct_rank_21d_diff": {"inputs": ["close", "low"], "func": fbd_extdrv2_016_support_90d_pct_rank_21d_diff},
    "fbd_extdrv2_017_fb_21d_count_zscore_126d_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv2_017_fb_21d_count_zscore_126d_5d_diff},
    "fbd_extdrv2_018_fb_45d_count_zscore_252d_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv2_018_fb_45d_count_zscore_252d_5d_diff},
    "fbd_extdrv2_019_obv_on_fb_21d_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": fbd_extdrv2_019_obv_on_fb_21d_5d_diff},
    "fbd_extdrv2_020_vwap_support_gap_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": fbd_extdrv2_020_vwap_support_gap_5d_diff},
    "fbd_extdrv2_021_reclaim_pct_45d_slope_21d": {"inputs": ["close", "high", "low"], "func": fbd_extdrv2_021_reclaim_pct_45d_slope_21d},
    "fbd_extdrv2_022_support_21d_63d_spread_5d_diff": {"inputs": ["close", "low"], "func": fbd_extdrv2_022_support_21d_63d_spread_5d_diff},
    "fbd_extdrv2_023_fb_7d_count_21d_21d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv2_023_fb_7d_count_21d_21d_diff},
    "fbd_extdrv2_024_wick_pct_45d_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv2_024_wick_pct_45d_5d_diff},
    "fbd_extdrv2_025_fb_180d_count_252d_21d_diff": {"inputs": ["close", "high", "low"], "func": fbd_extdrv2_025_fb_180d_count_252d_21d_diff},
}
