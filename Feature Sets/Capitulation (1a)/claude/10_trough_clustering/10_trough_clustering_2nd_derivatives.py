"""
10_trough_clustering — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base trough-clustering features — velocity and acceleration
        of local-minima density, support-retest frequency, basing-zone tightness.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Each feature computes a .diff(n) or slope/pct-change of a base trough-clustering concept.
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _local_min_flag(low: pd.Series, w: int) -> pd.Series:
    """Backward-only local-minimum flag: low[t] == rolling_min(low, w)[t]."""
    rmin = low.rolling(w, min_periods=max(1, w // 2)).min()
    return (low <= rmin + _EPS).astype(float)


def _trough_count_raw(x, threshold_pct):
    if len(x) == 0:
        return np.nan
    mn = np.min(x)
    return float(np.sum(x <= mn * (1.0 + threshold_pct) + _EPS))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        num = ((xi - xi_m) * (x - x.mean())).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Base feature computations (inline, self-contained) ───────────────────────

def _base_local_min_count_63d(low):
    return _rolling_sum(_local_min_flag(low, 5), _TD_QTR)


def _base_local_min_count_252d(low):
    return _rolling_sum(_local_min_flag(low, 5), _TD_YEAR)


def _base_local_min_fraction_63d(low):
    return _rolling_mean(_local_min_flag(low, 5), _TD_QTR)


def _base_troughs_within_2pct_63d(low):
    def _cnt(x):
        return _trough_count_raw(x, 0.02)
    return low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_cnt, raw=True)


def _base_troughs_within_3pct_252d(low):
    def _cnt(x):
        return _trough_count_raw(x, 0.03)
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_cnt, raw=True)


def _base_support_retest_count_3pct_63d(low):
    rmin_252 = _rolling_min(low, _TD_YEAR)
    near = (low <= rmin_252 * 1.03 + _EPS).astype(float)
    return _rolling_sum(near, _TD_QTR)


def _base_support_retest_fraction_126d(low):
    rmin_252 = _rolling_min(low, _TD_YEAR)
    near = (low <= rmin_252 * 1.03 + _EPS).astype(float)
    return _rolling_mean(near, _TD_HALF)


def _base_basing_range_63d(low, high):
    return _safe_div(_rolling_max(high, _TD_QTR) - _rolling_min(low, _TD_QTR),
                     _rolling_min(low, _TD_QTR))


def _base_trough_price_cv_63d(low):
    def _cv(x):
        if len(x) == 0:
            return np.nan
        mn = np.min(x)
        near = x[x <= mn * 1.03 + _EPS]
        if len(near) < 2:
            return np.nan
        m = np.mean(near)
        if abs(m) < _EPS:
            return np.nan
        return float(np.std(near) / abs(m))
    return low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_cv, raw=True)


def _base_volume_at_troughs_fraction_63d(low, volume):
    flag = _local_min_flag(low, 5)
    vol_t = flag * volume
    return _safe_div(_rolling_sum(vol_t, _TD_QTR), _rolling_sum(volume, _TD_QTR))


def _base_trough_spacing_mean_252d(low):
    flag = _local_min_flag(low, 5)
    def _sp(x):
        idxs = np.where(x > 0.5)[0]
        if len(idxs) < 2:
            return np.nan
        return float(np.mean(np.diff(idxs.astype(float))))
    return flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_sp, raw=True)


def _base_rolling_min_slope_63d(low):
    rmin = _rolling_min(low, _TD_QTR)
    return _linslope(rmin, _TD_QTR)


def _base_trough_cluster_zscore_63d(low):
    cnt = _rolling_sum(_local_min_flag(low, 5), _TD_QTR)
    return _safe_div(cnt - _rolling_mean(cnt, _TD_YEAR), _rolling_std(cnt, _TD_YEAR))


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def tcl_drv2_001_local_min_count_63d_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of 63-day trough count (velocity of trough-density change)."""
    return _base_local_min_count_63d(low).diff(5)


def tcl_drv2_002_local_min_count_63d_21d_diff(low: pd.Series) -> pd.Series:
    """21-day diff of 63-day trough count (monthly velocity of density change)."""
    return _base_local_min_count_63d(low).diff(_TD_MON)


def tcl_drv2_003_local_min_count_252d_21d_diff(low: pd.Series) -> pd.Series:
    """21-day diff of 252-day trough count (monthly change in annual density)."""
    return _base_local_min_count_252d(low).diff(_TD_MON)


def tcl_drv2_004_local_min_fraction_63d_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of 63-day local-min fraction (pace of increasing trough frequency)."""
    return _base_local_min_fraction_63d(low).diff(5)


def tcl_drv2_005_local_min_fraction_63d_21d_diff(low: pd.Series) -> pd.Series:
    """21-day diff of 63-day local-min fraction."""
    return _base_local_min_fraction_63d(low).diff(_TD_MON)


def tcl_drv2_006_troughs_2pct_63d_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of count of bars within 2% of 63-day low."""
    return _base_troughs_within_2pct_63d(low).diff(5)


def tcl_drv2_007_troughs_3pct_252d_21d_diff(low: pd.Series) -> pd.Series:
    """21-day diff of count of bars within 3% of 252-day low."""
    return _base_troughs_within_3pct_252d(low).diff(_TD_MON)


def tcl_drv2_008_support_retest_count_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of 63-day support retest count (3% of 252-day low)."""
    return _base_support_retest_count_3pct_63d(low).diff(5)


def tcl_drv2_009_support_retest_count_21d_diff(low: pd.Series) -> pd.Series:
    """21-day diff of 63-day support retest count."""
    return _base_support_retest_count_3pct_63d(low).diff(_TD_MON)


def tcl_drv2_010_support_retest_fraction_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of 126-day support retest fraction."""
    return _base_support_retest_fraction_126d(low).diff(5)


def tcl_drv2_011_basing_range_63d_5d_diff(low: pd.Series, high: pd.Series) -> pd.Series:
    """5-day diff of 63-day basing range (narrowing = positive basing development)."""
    return _base_basing_range_63d(low, high).diff(5)


def tcl_drv2_012_basing_range_63d_21d_diff(low: pd.Series, high: pd.Series) -> pd.Series:
    """21-day diff of 63-day basing range."""
    return _base_basing_range_63d(low, high).diff(_TD_MON)


def tcl_drv2_013_trough_cv_63d_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of 63-day trough price CV (acceleration of support convergence)."""
    return _base_trough_price_cv_63d(low).diff(5)


def tcl_drv2_014_volume_trough_frac_5d_diff(low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day volume-at-troughs fraction (increasing accumulation?)."""
    return _base_volume_at_troughs_fraction_63d(low, volume).diff(5)


def tcl_drv2_015_volume_trough_frac_21d_diff(low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume-at-troughs fraction."""
    return _base_volume_at_troughs_fraction_63d(low, volume).diff(_TD_MON)


def tcl_drv2_016_trough_spacing_252d_21d_diff(low: pd.Series) -> pd.Series:
    """21-day diff of 252-day mean trough spacing (are troughs coming closer together?)."""
    return _base_trough_spacing_mean_252d(low).diff(_TD_MON)


def tcl_drv2_017_rolling_min_slope_63d_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of 63-day rolling-min slope (acceleration of floor movement)."""
    return _base_rolling_min_slope_63d(low).diff(5)


def tcl_drv2_018_rolling_min_slope_63d_21d_diff(low: pd.Series) -> pd.Series:
    """21-day diff of 63-day rolling-min slope."""
    return _base_rolling_min_slope_63d(low).diff(_TD_MON)


def tcl_drv2_019_trough_zscore_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of 63-day trough cluster z-score."""
    return _base_trough_cluster_zscore_63d(low).diff(5)


def tcl_drv2_020_trough_zscore_21d_diff(low: pd.Series) -> pd.Series:
    """21-day diff of 63-day trough cluster z-score."""
    return _base_trough_cluster_zscore_63d(low).diff(_TD_MON)


def tcl_drv2_021_local_min_count_63d_slope_21d(low: pd.Series) -> pd.Series:
    """OLS slope of 63-day trough count over 21-day window (trend of density)."""
    cnt = _base_local_min_count_63d(low)
    return _linslope(cnt, _TD_MON)


def tcl_drv2_022_support_retest_count_slope_63d(low: pd.Series) -> pd.Series:
    """OLS slope of 63-day support retest count over 63-day window."""
    cnt = _base_support_retest_count_3pct_63d(low)
    return _linslope(cnt, _TD_QTR)


def tcl_drv2_023_basing_range_pct_change_21d(low: pd.Series, high: pd.Series) -> pd.Series:
    """21-day pct-change of 63-day basing range (relative narrowing speed)."""
    rng = _base_basing_range_63d(low, high)
    return rng.pct_change(_TD_MON)


def tcl_drv2_024_trough_fraction_ewma_diff_5d(low: pd.Series) -> pd.Series:
    """5-day diff of EWM(span=21) of local-min fraction (smoothed velocity)."""
    frac = _base_local_min_fraction_63d(low)
    return _ewm_mean(frac, _TD_MON).diff(5)


def tcl_drv2_025_volume_trough_slope_63d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day volume-at-troughs fraction over 63-day window."""
    frac = _base_volume_at_troughs_fraction_63d(low, volume)
    return _linslope(frac, _TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

TROUGH_CLUSTERING_REGISTRY_2ND_DERIVATIVES = {
    "tcl_drv2_001_local_min_count_63d_5d_diff":    {"inputs": ["low"],           "func": tcl_drv2_001_local_min_count_63d_5d_diff},
    "tcl_drv2_002_local_min_count_63d_21d_diff":   {"inputs": ["low"],           "func": tcl_drv2_002_local_min_count_63d_21d_diff},
    "tcl_drv2_003_local_min_count_252d_21d_diff":  {"inputs": ["low"],           "func": tcl_drv2_003_local_min_count_252d_21d_diff},
    "tcl_drv2_004_local_min_fraction_63d_5d_diff": {"inputs": ["low"],           "func": tcl_drv2_004_local_min_fraction_63d_5d_diff},
    "tcl_drv2_005_local_min_fraction_63d_21d_diff":{"inputs": ["low"],           "func": tcl_drv2_005_local_min_fraction_63d_21d_diff},
    "tcl_drv2_006_troughs_2pct_63d_5d_diff":       {"inputs": ["low"],           "func": tcl_drv2_006_troughs_2pct_63d_5d_diff},
    "tcl_drv2_007_troughs_3pct_252d_21d_diff":     {"inputs": ["low"],           "func": tcl_drv2_007_troughs_3pct_252d_21d_diff},
    "tcl_drv2_008_support_retest_count_5d_diff":   {"inputs": ["low"],           "func": tcl_drv2_008_support_retest_count_5d_diff},
    "tcl_drv2_009_support_retest_count_21d_diff":  {"inputs": ["low"],           "func": tcl_drv2_009_support_retest_count_21d_diff},
    "tcl_drv2_010_support_retest_fraction_5d_diff":{"inputs": ["low"],           "func": tcl_drv2_010_support_retest_fraction_5d_diff},
    "tcl_drv2_011_basing_range_63d_5d_diff":       {"inputs": ["low", "high"],   "func": tcl_drv2_011_basing_range_63d_5d_diff},
    "tcl_drv2_012_basing_range_63d_21d_diff":      {"inputs": ["low", "high"],   "func": tcl_drv2_012_basing_range_63d_21d_diff},
    "tcl_drv2_013_trough_cv_63d_5d_diff":          {"inputs": ["low"],           "func": tcl_drv2_013_trough_cv_63d_5d_diff},
    "tcl_drv2_014_volume_trough_frac_5d_diff":     {"inputs": ["low", "volume"], "func": tcl_drv2_014_volume_trough_frac_5d_diff},
    "tcl_drv2_015_volume_trough_frac_21d_diff":    {"inputs": ["low", "volume"], "func": tcl_drv2_015_volume_trough_frac_21d_diff},
    "tcl_drv2_016_trough_spacing_252d_21d_diff":   {"inputs": ["low"],           "func": tcl_drv2_016_trough_spacing_252d_21d_diff},
    "tcl_drv2_017_rolling_min_slope_63d_5d_diff":  {"inputs": ["low"],           "func": tcl_drv2_017_rolling_min_slope_63d_5d_diff},
    "tcl_drv2_018_rolling_min_slope_63d_21d_diff": {"inputs": ["low"],           "func": tcl_drv2_018_rolling_min_slope_63d_21d_diff},
    "tcl_drv2_019_trough_zscore_5d_diff":          {"inputs": ["low"],           "func": tcl_drv2_019_trough_zscore_5d_diff},
    "tcl_drv2_020_trough_zscore_21d_diff":         {"inputs": ["low"],           "func": tcl_drv2_020_trough_zscore_21d_diff},
    "tcl_drv2_021_local_min_count_63d_slope_21d":  {"inputs": ["low"],           "func": tcl_drv2_021_local_min_count_63d_slope_21d},
    "tcl_drv2_022_support_retest_count_slope_63d": {"inputs": ["low"],           "func": tcl_drv2_022_support_retest_count_slope_63d},
    "tcl_drv2_023_basing_range_pct_change_21d":    {"inputs": ["low", "high"],   "func": tcl_drv2_023_basing_range_pct_change_21d},
    "tcl_drv2_024_trough_fraction_ewma_diff_5d":   {"inputs": ["low"],           "func": tcl_drv2_024_trough_fraction_ewma_diff_5d},
    "tcl_drv2_025_volume_trough_slope_63d":        {"inputs": ["low", "volume"], "func": tcl_drv2_025_volume_trough_slope_63d},
}
