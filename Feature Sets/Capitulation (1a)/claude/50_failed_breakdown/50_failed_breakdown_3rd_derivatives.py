"""
50_failed_breakdown — 3rd Derivatives (Features fbd_drv3_001-025)
Domain: rate of change of 2nd-derivative failed-breakdown features — acceleration of velocity
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def fbd_drv3_001_fb_21d_count_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day FB count (acceleration of spring frequency velocity)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_drv3_002_fb_21d_count_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day-velocity of FB count (jerk in monthly spring frequency)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_MON)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fbd_drv3_003_undercut_depth_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of smoothed 21d undercut depth (jerk in pierce severity)."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    depth = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    smoothed = _rolling_mean(depth.where(fb > 0, 0.0), _TD_MON)
    vel = smoothed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_drv3_004_reclaim_rate_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d reclaim rate (acceleration of spring success rate)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    support = _prior_low(low, _TD_MON)
    total_undercut = (low < support).astype(float)
    rate = _safe_div(
        _rolling_sum(fb, _TD_MON),
        _rolling_sum(total_undercut, _TD_MON).clip(lower=1)
    )
    vel = rate.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_drv3_005_support_21d_slope_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d support OLS slope (jerk in floor-trend acceleration)."""
    support = _prior_low(low, _TD_MON)
    slp = _linslope(support, _TD_MON)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_drv3_006_close_to_support_21d_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of close/21d-support ratio (jerk in distance from floor)."""
    support = _prior_low(low, _TD_MON)
    ratio = _safe_div(close, support.replace(0, np.nan))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_drv3_007_fb_63d_count_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day FB count (jerk in medium-term spring density)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_QTR), _TD_QTR)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fbd_drv3_008_vol_ratio_fb_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of smoothed volume ratio on FB (jerk in capitulation conviction)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol).fillna(1)
    smoothed = _rolling_mean(vol_ratio.where(fb > 0, 0.0), _TD_MON)
    vel = smoothed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_drv3_009_support_stability_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d std-dev of 21d support (jerk in floor stability)."""
    support = _prior_low(low, _TD_MON)
    stability = _rolling_std(support, _TD_QTR)
    vel = stability.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_drv3_010_undercut_depth_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in smoothed 63d undercut depth (jerk in pier severity)."""
    support = _prior_low(low, _TD_QTR)
    fb = _failed_breakdown_flag(close, high, low, _TD_QTR)
    depth = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    smoothed = _rolling_mean(depth.where(fb > 0, 0.0), _TD_QTR)
    vel21 = smoothed.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fbd_drv3_011_reclaim_rate_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day reclaim rate (jerk in spring success trend)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    support = _prior_low(low, _TD_MON)
    total_undercut = (low < support).astype(float)
    rate = _safe_div(
        _rolling_sum(fb, _TD_QTR),
        _rolling_sum(total_undercut, _TD_QTR).clip(lower=1)
    )
    vel21 = rate.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fbd_drv3_012_fb_composite_score_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day rolling mean FB composite score (jerk in trap quality)."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    depth = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_r = _safe_div(volume, avg_vol).fillna(1).clip(upper=5)
    reclaim = _safe_div((close - support).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    score = (depth + vol_r / 5.0 + reclaim).where(fb > 0, 0.0)
    smoothed = _rolling_mean(score, _TD_QTR)
    vel = smoothed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_drv3_013_support_21d_change_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of pct-change in 21d support (jerk in floor erosion rate)."""
    support = _prior_low(low, _TD_MON)
    chg = _safe_div(support - support.shift(_TD_MON), support.shift(_TD_MON))
    vel = chg.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_drv3_014_low_to_support_21d_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of low/21d-support ratio (jerk in undercut depth velocity)."""
    support = _prior_low(low, _TD_MON)
    ratio = _safe_div(low, support.replace(0, np.nan))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_drv3_015_close_to_support_63d_21d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in close/63d-support ratio."""
    support = _prior_low(low, _TD_QTR)
    ratio = _safe_div(close, support.replace(0, np.nan))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fbd_drv3_016_support_63d_slope_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of OLS slope of 63d support (acceleration of medium-term floor trend)."""
    support = _prior_low(low, _TD_QTR)
    slp = _linslope(support, _TD_MON)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_drv3_017_fb_count_zscore_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of z-score of 21-day FB count (jerk in relative spring frequency)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_MON)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    z = _safe_div(cnt - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_drv3_018_multi_test_count_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d support multi-test count (jerk in test acceleration)."""
    support = _prior_low(low, _TD_MON)
    test = (low < support).astype(float)
    cnt = _rolling_sum(test, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_drv3_019_reclaim_pct_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of smoothed reclaim-margin-pct over 21 days."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    margin_pct = _safe_div(close - support, support.replace(0, np.nan)).fillna(0)
    smoothed = _rolling_mean(margin_pct.where(fb > 0, 0.0), _TD_MON)
    slp = _linslope(smoothed, _TD_MON)
    return slp.diff(_TD_WEEK)


def fbd_drv3_020_undercut_atr_ratio_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of ATR-normalized undercut depth on 21d FBs."""
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
    vel = smoothed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_drv3_021_fb_21d_cluster_5d_diff_slope(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day-diff of FB cluster count (trend in clustering jerk)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_WEEK)
    vel = cnt.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def fbd_drv3_022_support_21d_pct_rank_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of percentile rank of 21d support level."""
    support = _prior_low(low, _TD_MON)
    rank = support.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fbd_drv3_023_support_distance_21d_slope_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of close/21d-support ratio (rate of slope change)."""
    support = _prior_low(low, _TD_MON)
    ratio = _safe_div(close, support.replace(0, np.nan))
    slp = _linslope(ratio, _TD_MON)
    return slp.diff(_TD_WEEK)


def fbd_drv3_024_vol_ratio_fb_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of smoothed FB volume ratio (rate of conviction change)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol).fillna(1)
    smoothed = _rolling_mean(vol_ratio.where(fb > 0, 0.0), _TD_MON)
    slp = _linslope(smoothed, _TD_MON)
    return slp.diff(_TD_WEEK)


def fbd_drv3_025_fb_bear_trap_score_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63d rolling mean bear-trap score."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    depth = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_r = _safe_div(volume, avg_vol).fillna(1).clip(upper=5)
    reclaim = _safe_div((close - support).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    score = (depth + vol_r / 5.0 + reclaim).where(fb > 0, 0.0)
    smoothed = _rolling_mean(score, _TD_QTR)
    vel21 = smoothed.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

FAILED_BREAKDOWN_REGISTRY_3RD_DERIVATIVES = {
    "fbd_drv3_001_fb_21d_count_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv3_001_fb_21d_count_5d_diff_5d_diff},
    "fbd_drv3_002_fb_21d_count_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv3_002_fb_21d_count_21d_diff_5d_diff},
    "fbd_drv3_003_undercut_depth_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv3_003_undercut_depth_5d_diff_5d_diff},
    "fbd_drv3_004_reclaim_rate_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv3_004_reclaim_rate_21d_5d_diff_5d_diff},
    "fbd_drv3_005_support_21d_slope_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": fbd_drv3_005_support_21d_slope_5d_diff_5d_diff},
    "fbd_drv3_006_close_to_support_21d_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": fbd_drv3_006_close_to_support_21d_5d_diff_5d_diff},
    "fbd_drv3_007_fb_63d_count_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv3_007_fb_63d_count_21d_diff_5d_diff},
    "fbd_drv3_008_vol_ratio_fb_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": fbd_drv3_008_vol_ratio_fb_5d_diff_5d_diff},
    "fbd_drv3_009_support_stability_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": fbd_drv3_009_support_stability_5d_diff_5d_diff},
    "fbd_drv3_010_undercut_depth_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv3_010_undercut_depth_63d_21d_diff_5d_diff},
    "fbd_drv3_011_reclaim_rate_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv3_011_reclaim_rate_63d_21d_diff_5d_diff},
    "fbd_drv3_012_fb_composite_score_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": fbd_drv3_012_fb_composite_score_5d_diff_5d_diff},
    "fbd_drv3_013_support_21d_change_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": fbd_drv3_013_support_21d_change_5d_diff_5d_diff},
    "fbd_drv3_014_low_to_support_21d_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": fbd_drv3_014_low_to_support_21d_5d_diff_5d_diff},
    "fbd_drv3_015_close_to_support_63d_21d_diff_5d_diff": {"inputs": ["close", "low"], "func": fbd_drv3_015_close_to_support_63d_21d_diff_5d_diff},
    "fbd_drv3_016_support_63d_slope_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": fbd_drv3_016_support_63d_slope_5d_diff_5d_diff},
    "fbd_drv3_017_fb_count_zscore_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv3_017_fb_count_zscore_5d_diff_5d_diff},
    "fbd_drv3_018_multi_test_count_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv3_018_multi_test_count_5d_diff_5d_diff},
    "fbd_drv3_019_reclaim_pct_slope_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv3_019_reclaim_pct_slope_5d_diff},
    "fbd_drv3_020_undercut_atr_ratio_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": fbd_drv3_020_undercut_atr_ratio_5d_diff_5d_diff},
    "fbd_drv3_021_fb_21d_cluster_5d_diff_slope": {"inputs": ["close", "high", "low"], "func": fbd_drv3_021_fb_21d_cluster_5d_diff_slope},
    "fbd_drv3_022_support_21d_pct_rank_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": fbd_drv3_022_support_21d_pct_rank_5d_diff_5d_diff},
    "fbd_drv3_023_support_distance_21d_slope_5d_diff": {"inputs": ["close", "low"], "func": fbd_drv3_023_support_distance_21d_slope_5d_diff},
    "fbd_drv3_024_vol_ratio_fb_slope_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": fbd_drv3_024_vol_ratio_fb_slope_5d_diff},
    "fbd_drv3_025_fb_bear_trap_score_21d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": fbd_drv3_025_fb_bear_trap_score_21d_diff_5d_diff},
}
