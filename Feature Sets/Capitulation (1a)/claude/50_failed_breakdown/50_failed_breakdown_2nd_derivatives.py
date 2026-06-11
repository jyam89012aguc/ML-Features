"""
50_failed_breakdown — 2nd Derivatives (Features fbd_drv2_001-025)
Domain: rate of change of failed-breakdown base features — velocity / acceleration of spring behavior
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


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


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

def fbd_drv2_001_fb_21d_count_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day FB event count in 21d window (velocity of spring frequency)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_MON)
    return cnt.diff(_TD_WEEK)


def fbd_drv2_002_fb_21d_count_21d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 21-day FB event count (monthly velocity of spring frequency)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_MON)
    return cnt.diff(_TD_MON)


def fbd_drv2_003_undercut_depth_pct_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of undercut depth % (21d support) smoothed over 21d window."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    depth = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    smoothed = _rolling_mean(depth.where(fb > 0, 0.0), _TD_MON)
    return smoothed.diff(_TD_WEEK)


def fbd_drv2_004_reclaim_rate_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day reclaim rate (fraction of undercuts that became FB)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    support = _prior_low(low, _TD_MON)
    total_undercut = (low < support).astype(float)
    rate = _safe_div(
        _rolling_sum(fb, _TD_MON),
        _rolling_sum(total_undercut, _TD_MON).clip(lower=1)
    )
    return rate.diff(_TD_WEEK)


def fbd_drv2_005_support_21d_slope_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day support OLS slope (acceleration of floor trend)."""
    support = _prior_low(low, _TD_MON)
    slp = _linslope(support, _TD_MON)
    return slp.diff(_TD_WEEK)


def fbd_drv2_006_fb_63d_count_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day FB count in 63d window (monthly change in spring density)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_QTR), _TD_QTR)
    return cnt.diff(_TD_MON)


def fbd_drv2_007_close_to_support_ratio_21d_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of close/21d-support ratio (velocity of distance from floor)."""
    support = _prior_low(low, _TD_MON)
    ratio = _safe_div(close, support.replace(0, np.nan))
    return ratio.diff(_TD_WEEK)


def fbd_drv2_008_close_to_support_ratio_63d_21d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of close/63d-support ratio."""
    support = _prior_low(low, _TD_QTR)
    ratio = _safe_div(close, support.replace(0, np.nan))
    return ratio.diff(_TD_MON)


def fbd_drv2_009_undercut_depth_pct_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of undercut depth % smoothed over 63d window."""
    support = _prior_low(low, _TD_QTR)
    fb = _failed_breakdown_flag(close, high, low, _TD_QTR)
    depth = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    smoothed = _rolling_mean(depth.where(fb > 0, 0.0), _TD_QTR)
    return smoothed.diff(_TD_MON)


def fbd_drv2_010_vol_ratio_on_fb_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of smoothed volume ratio on 21d FB events (velocity of conviction)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol).fillna(1)
    smoothed = _rolling_mean(vol_ratio.where(fb > 0, 0.0), _TD_MON)
    return smoothed.diff(_TD_WEEK)


def fbd_drv2_011_fb_21d_cluster_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 5-day FB event count (very short-term clustering velocity)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_WEEK)
    return cnt.diff(_TD_WEEK)


def fbd_drv2_012_support_stability_21d_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 63-day std dev of 21d support level (volatility of floor)."""
    support = _prior_low(low, _TD_MON)
    stability = _rolling_std(support, _TD_QTR)
    return stability.diff(_TD_WEEK)


def fbd_drv2_013_support_21d_pct_rank_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of percentile rank of 21d support within 252-day range."""
    support = _prior_low(low, _TD_MON)
    rank = support.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_WEEK)


def fbd_drv2_014_low_to_support_ratio_21d_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of intraday-low / 21d-support ratio (velocity of undercut depth)."""
    support = _prior_low(low, _TD_MON)
    ratio = _safe_div(low, support.replace(0, np.nan))
    return ratio.diff(_TD_WEEK)


def fbd_drv2_015_reclaim_close_pct_21d_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of reclaim-margin-pct on 21d FB bars (trend in spring quality)."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    margin_pct = _safe_div(close - support, support.replace(0, np.nan)).fillna(0)
    smoothed = _rolling_mean(margin_pct.where(fb > 0, 0.0), _TD_MON)
    return _linslope(smoothed, _TD_MON)


def fbd_drv2_016_fb_21d_composite_score_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day rolling mean FB composite score."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    depth = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_r = _safe_div(volume, avg_vol).fillna(1).clip(upper=5)
    reclaim = _safe_div((close - support).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    score = (depth + vol_r / 5.0 + reclaim).where(fb > 0, 0.0)
    smoothed = _rolling_mean(score, _TD_QTR)
    return smoothed.diff(_TD_WEEK)


def fbd_drv2_017_support_21d_change_pct_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of pct-change-in-21d-support (acceleration of floor erosion)."""
    support = _prior_low(low, _TD_MON)
    chg = _safe_div(support - support.shift(_TD_MON), support.shift(_TD_MON))
    return chg.diff(_TD_WEEK)


def fbd_drv2_018_fb_bar_range_pct_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of smoothed bar-range-pct on 21d FB events."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    bar_range_pct = _safe_div(high - low, close.replace(0, np.nan)).fillna(0)
    smoothed = _rolling_mean(bar_range_pct.where(fb > 0, 0.0), _TD_MON)
    return smoothed.diff(_TD_WEEK)


def fbd_drv2_019_reclaim_rate_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day reclaim rate (monthly change in fraction of FB vs all undercuts)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    support = _prior_low(low, _TD_MON)
    total_undercut = (low < support).astype(float)
    rate = _safe_div(
        _rolling_sum(fb, _TD_QTR),
        _rolling_sum(total_undercut, _TD_QTR).clip(lower=1)
    )
    return rate.diff(_TD_MON)


def fbd_drv2_020_close_vs_52wk_low_on_fb_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of close-pct-above-52wk-low on 21d FB bars (trend in depth of trap)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    low_252 = _prior_low(low, _TD_YEAR)
    pct_above = _safe_div(close - low_252, low_252.replace(0, np.nan)).fillna(0)
    smoothed = _rolling_mean(pct_above.where(fb > 0, 0.0), _TD_MON)
    return smoothed.diff(_TD_WEEK)


def fbd_drv2_021_support_63d_slope_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63d support over 21 days (acceleration of medium-term floor)."""
    support = _prior_low(low, _TD_QTR)
    slp = _linslope(support, _TD_MON)
    return slp.diff(_TD_WEEK)


def fbd_drv2_022_fb_21d_count_zscore_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of z-score of 21-day FB count (velocity of extremity)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_MON)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    z = _safe_div(cnt - m, s)
    return z.diff(_TD_WEEK)


def fbd_drv2_023_undercut_atr_ratio_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of ATR-normalized undercut depth on 21d FBs (velocity of pierce severity)."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    pierce = (support - low).clip(lower=0)
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    atr21 = _rolling_mean(tr, _TD_MON)
    ratio = _safe_div(pierce, atr21).fillna(0)
    smoothed = _rolling_mean(ratio.where(fb > 0, 0.0), _TD_MON)
    return smoothed.diff(_TD_WEEK)


def fbd_drv2_024_support_distance_21d_slope_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of close/21d-support ratio (trend in distance above floor)."""
    support = _prior_low(low, _TD_MON)
    ratio = _safe_div(close, support.replace(0, np.nan))
    return _linslope(ratio, _TD_MON)


def fbd_drv2_025_multi_test_21d_count_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day support multi-test count in 21d window (acceleration of tests)."""
    support = _prior_low(low, _TD_MON)
    test = (low < support).astype(float)
    cnt = _rolling_sum(test, _TD_MON)
    return cnt.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

FAILED_BREAKDOWN_REGISTRY_2ND_DERIVATIVES = {
    "fbd_drv2_001_fb_21d_count_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv2_001_fb_21d_count_21d_5d_diff},
    "fbd_drv2_002_fb_21d_count_21d_21d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv2_002_fb_21d_count_21d_21d_diff},
    "fbd_drv2_003_undercut_depth_pct_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv2_003_undercut_depth_pct_21d_5d_diff},
    "fbd_drv2_004_reclaim_rate_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv2_004_reclaim_rate_21d_5d_diff},
    "fbd_drv2_005_support_21d_slope_5d_diff": {"inputs": ["close", "low"], "func": fbd_drv2_005_support_21d_slope_5d_diff},
    "fbd_drv2_006_fb_63d_count_63d_21d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv2_006_fb_63d_count_63d_21d_diff},
    "fbd_drv2_007_close_to_support_ratio_21d_5d_diff": {"inputs": ["close", "low"], "func": fbd_drv2_007_close_to_support_ratio_21d_5d_diff},
    "fbd_drv2_008_close_to_support_ratio_63d_21d_diff": {"inputs": ["close", "low"], "func": fbd_drv2_008_close_to_support_ratio_63d_21d_diff},
    "fbd_drv2_009_undercut_depth_pct_63d_21d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv2_009_undercut_depth_pct_63d_21d_diff},
    "fbd_drv2_010_vol_ratio_on_fb_21d_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": fbd_drv2_010_vol_ratio_on_fb_21d_5d_diff},
    "fbd_drv2_011_fb_21d_cluster_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv2_011_fb_21d_cluster_5d_diff},
    "fbd_drv2_012_support_stability_21d_5d_diff": {"inputs": ["close", "low"], "func": fbd_drv2_012_support_stability_21d_5d_diff},
    "fbd_drv2_013_support_21d_pct_rank_5d_diff": {"inputs": ["close", "low"], "func": fbd_drv2_013_support_21d_pct_rank_5d_diff},
    "fbd_drv2_014_low_to_support_ratio_21d_5d_diff": {"inputs": ["close", "low"], "func": fbd_drv2_014_low_to_support_ratio_21d_5d_diff},
    "fbd_drv2_015_reclaim_close_pct_21d_slope_21d": {"inputs": ["close", "high", "low"], "func": fbd_drv2_015_reclaim_close_pct_21d_slope_21d},
    "fbd_drv2_016_fb_21d_composite_score_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": fbd_drv2_016_fb_21d_composite_score_5d_diff},
    "fbd_drv2_017_support_21d_change_pct_5d_diff": {"inputs": ["close", "low"], "func": fbd_drv2_017_support_21d_change_pct_5d_diff},
    "fbd_drv2_018_fb_bar_range_pct_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv2_018_fb_bar_range_pct_21d_5d_diff},
    "fbd_drv2_019_reclaim_rate_63d_21d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv2_019_reclaim_rate_63d_21d_diff},
    "fbd_drv2_020_close_vs_52wk_low_on_fb_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv2_020_close_vs_52wk_low_on_fb_5d_diff},
    "fbd_drv2_021_support_63d_slope_5d_diff": {"inputs": ["close", "low"], "func": fbd_drv2_021_support_63d_slope_5d_diff},
    "fbd_drv2_022_fb_21d_count_zscore_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv2_022_fb_21d_count_zscore_5d_diff},
    "fbd_drv2_023_undercut_atr_ratio_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv2_023_undercut_atr_ratio_21d_5d_diff},
    "fbd_drv2_024_support_distance_21d_slope_21d": {"inputs": ["close", "low"], "func": fbd_drv2_024_support_distance_21d_slope_21d},
    "fbd_drv2_025_multi_test_21d_count_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv2_025_multi_test_21d_count_5d_diff},
}
