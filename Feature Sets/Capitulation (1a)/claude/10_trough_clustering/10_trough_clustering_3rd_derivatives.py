"""
10_trough_clustering — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative trough-clustering features —
        acceleration-of-acceleration of local-minima density and basing dynamics.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Each feature computes diff/slope/pct-change of a 2nd-derivative trough concept.
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
    """Backward-only local-minimum flag."""
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


# ── 2nd-derivative base computations (inline, self-contained) ────────────────

def _drv2_local_min_count_63d_5d_diff(low):
    cnt = _rolling_sum(_local_min_flag(low, 5), _TD_QTR)
    return cnt.diff(5)


def _drv2_local_min_count_63d_21d_diff(low):
    cnt = _rolling_sum(_local_min_flag(low, 5), _TD_QTR)
    return cnt.diff(_TD_MON)


def _drv2_local_min_fraction_63d_5d_diff(low):
    frac = _rolling_mean(_local_min_flag(low, 5), _TD_QTR)
    return frac.diff(5)


def _drv2_troughs_2pct_63d_5d_diff(low):
    def _cnt(x):
        return _trough_count_raw(x, 0.02)
    cnt = low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_cnt, raw=True)
    return cnt.diff(5)


def _drv2_support_retest_count_5d_diff(low):
    rmin_252 = _rolling_min(low, _TD_YEAR)
    near = (low <= rmin_252 * 1.03 + _EPS).astype(float)
    cnt = _rolling_sum(near, _TD_QTR)
    return cnt.diff(5)


def _drv2_support_retest_count_21d_diff(low):
    rmin_252 = _rolling_min(low, _TD_YEAR)
    near = (low <= rmin_252 * 1.03 + _EPS).astype(float)
    cnt = _rolling_sum(near, _TD_QTR)
    return cnt.diff(_TD_MON)


def _drv2_basing_range_63d_5d_diff(low, high):
    rng = _safe_div(_rolling_max(high, _TD_QTR) - _rolling_min(low, _TD_QTR),
                    _rolling_min(low, _TD_QTR))
    return rng.diff(5)


def _drv2_basing_range_63d_21d_diff(low, high):
    rng = _safe_div(_rolling_max(high, _TD_QTR) - _rolling_min(low, _TD_QTR),
                    _rolling_min(low, _TD_QTR))
    return rng.diff(_TD_MON)


def _drv2_trough_cv_63d_5d_diff(low):
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
    cv = low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_cv, raw=True)
    return cv.diff(5)


def _drv2_volume_trough_frac_5d_diff(low, volume):
    flag = _local_min_flag(low, 5)
    vol_t = flag * volume
    frac = _safe_div(_rolling_sum(vol_t, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    return frac.diff(5)


def _drv2_rolling_min_slope_63d_5d_diff(low):
    rmin = _rolling_min(low, _TD_QTR)
    slp = _linslope(rmin, _TD_QTR)
    return slp.diff(5)


def _drv2_trough_zscore_5d_diff(low):
    cnt = _rolling_sum(_local_min_flag(low, 5), _TD_QTR)
    z = _safe_div(cnt - _rolling_mean(cnt, _TD_YEAR), _rolling_std(cnt, _TD_YEAR))
    return z.diff(5)


def _drv2_local_min_count_63d_slope_21d(low):
    cnt = _rolling_sum(_local_min_flag(low, 5), _TD_QTR)
    return _linslope(cnt, _TD_MON)


def _drv2_support_retest_slope_63d(low):
    rmin_252 = _rolling_min(low, _TD_YEAR)
    near = (low <= rmin_252 * 1.03 + _EPS).astype(float)
    cnt = _rolling_sum(near, _TD_QTR)
    return _linslope(cnt, _TD_QTR)


def _drv2_volume_trough_slope_63d(low, volume):
    flag = _local_min_flag(low, 5)
    vol_t = flag * volume
    frac = _safe_div(_rolling_sum(vol_t, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    return _linslope(frac, _TD_QTR)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def tcl_drv3_001_cnt63d_5d_diff_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of the 5-day diff of 63d trough count (jerk of density change)."""
    return _drv2_local_min_count_63d_5d_diff(low).diff(5)


def tcl_drv3_002_cnt63d_21d_diff_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day diff of 63d trough count."""
    return _drv2_local_min_count_63d_21d_diff(low).diff(5)


def tcl_drv3_003_cnt63d_21d_diff_21d_diff(low: pd.Series) -> pd.Series:
    """21-day diff of the 21-day diff of 63d trough count."""
    return _drv2_local_min_count_63d_21d_diff(low).diff(_TD_MON)


def tcl_drv3_004_frac63d_5d_diff_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of the 5-day diff of 63d local-min fraction."""
    return _drv2_local_min_fraction_63d_5d_diff(low).diff(5)


def tcl_drv3_005_frac63d_5d_diff_21d_diff(low: pd.Series) -> pd.Series:
    """21-day diff of the 5-day diff of 63d local-min fraction."""
    return _drv2_local_min_fraction_63d_5d_diff(low).diff(_TD_MON)


def tcl_drv3_006_troughs2pct_5d_diff_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of the 5-day diff of 63d within-2pct trough count."""
    return _drv2_troughs_2pct_63d_5d_diff(low).diff(5)


def tcl_drv3_007_troughs2pct_5d_diff_21d_diff(low: pd.Series) -> pd.Series:
    """21-day diff of the 5-day diff of 63d within-2pct trough count."""
    return _drv2_troughs_2pct_63d_5d_diff(low).diff(_TD_MON)


def tcl_drv3_008_retest_5d_diff_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of the 5-day diff of 63d support retest count."""
    return _drv2_support_retest_count_5d_diff(low).diff(5)


def tcl_drv3_009_retest_21d_diff_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day diff of 63d support retest count."""
    return _drv2_support_retest_count_21d_diff(low).diff(5)


def tcl_drv3_010_basing_range_5d_diff_5d_diff(low: pd.Series, high: pd.Series) -> pd.Series:
    """5-day diff of the 5-day diff of 63d basing range."""
    return _drv2_basing_range_63d_5d_diff(low, high).diff(5)


def tcl_drv3_011_basing_range_21d_diff_5d_diff(low: pd.Series, high: pd.Series) -> pd.Series:
    """5-day diff of the 21-day diff of 63d basing range."""
    return _drv2_basing_range_63d_21d_diff(low, high).diff(5)


def tcl_drv3_012_basing_range_21d_diff_21d_diff(low: pd.Series, high: pd.Series) -> pd.Series:
    """21-day diff of the 21-day diff of 63d basing range."""
    return _drv2_basing_range_63d_21d_diff(low, high).diff(_TD_MON)


def tcl_drv3_013_trough_cv_5d_diff_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of the 5-day diff of 63d trough price CV."""
    return _drv2_trough_cv_63d_5d_diff(low).diff(5)


def tcl_drv3_014_vol_trough_frac_5d_diff_5d_diff(low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 5-day diff of 63d volume-at-troughs fraction."""
    return _drv2_volume_trough_frac_5d_diff(low, volume).diff(5)


def tcl_drv3_015_vol_trough_frac_5d_diff_21d_diff(low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of the 5-day diff of 63d volume-at-troughs fraction."""
    return _drv2_volume_trough_frac_5d_diff(low, volume).diff(_TD_MON)


def tcl_drv3_016_rolling_min_slope_5d_diff_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of the 5-day diff of 63d rolling-min slope."""
    return _drv2_rolling_min_slope_63d_5d_diff(low).diff(5)


def tcl_drv3_017_rolling_min_slope_5d_diff_21d_diff(low: pd.Series) -> pd.Series:
    """21-day diff of the 5-day diff of 63d rolling-min slope."""
    return _drv2_rolling_min_slope_63d_5d_diff(low).diff(_TD_MON)


def tcl_drv3_018_trough_zscore_5d_diff_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of the 5-day diff of 63d trough cluster z-score."""
    return _drv2_trough_zscore_5d_diff(low).diff(5)


def tcl_drv3_019_trough_zscore_5d_diff_21d_diff(low: pd.Series) -> pd.Series:
    """21-day diff of the 5-day diff of 63d trough cluster z-score."""
    return _drv2_trough_zscore_5d_diff(low).diff(_TD_MON)


def tcl_drv3_020_cnt63d_slope_21d_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63d trough count over 21d (jerk of density slope)."""
    return _drv2_local_min_count_63d_slope_21d(low).diff(5)


def tcl_drv3_021_cnt63d_slope_21d_21d_diff(low: pd.Series) -> pd.Series:
    """21-day diff of OLS slope of 63d trough count over 21d."""
    return _drv2_local_min_count_63d_slope_21d(low).diff(_TD_MON)


def tcl_drv3_022_retest_slope_63d_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63d support retest count over 63d."""
    return _drv2_support_retest_slope_63d(low).diff(5)


def tcl_drv3_023_retest_slope_63d_21d_diff(low: pd.Series) -> pd.Series:
    """21-day diff of OLS slope of 63d support retest count over 63d."""
    return _drv2_support_retest_slope_63d(low).diff(_TD_MON)


def tcl_drv3_024_vol_trough_slope_5d_diff(low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63d volume-at-troughs fraction over 63d."""
    return _drv2_volume_trough_slope_63d(low, volume).diff(5)


def tcl_drv3_025_vol_trough_slope_21d_diff(low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of OLS slope of 63d volume-at-troughs fraction over 63d."""
    return _drv2_volume_trough_slope_63d(low, volume).diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

TROUGH_CLUSTERING_REGISTRY_3RD_DERIVATIVES = {
    "tcl_drv3_001_cnt63d_5d_diff_5d_diff":          {"inputs": ["low"],           "func": tcl_drv3_001_cnt63d_5d_diff_5d_diff},
    "tcl_drv3_002_cnt63d_21d_diff_5d_diff":         {"inputs": ["low"],           "func": tcl_drv3_002_cnt63d_21d_diff_5d_diff},
    "tcl_drv3_003_cnt63d_21d_diff_21d_diff":        {"inputs": ["low"],           "func": tcl_drv3_003_cnt63d_21d_diff_21d_diff},
    "tcl_drv3_004_frac63d_5d_diff_5d_diff":         {"inputs": ["low"],           "func": tcl_drv3_004_frac63d_5d_diff_5d_diff},
    "tcl_drv3_005_frac63d_5d_diff_21d_diff":        {"inputs": ["low"],           "func": tcl_drv3_005_frac63d_5d_diff_21d_diff},
    "tcl_drv3_006_troughs2pct_5d_diff_5d_diff":     {"inputs": ["low"],           "func": tcl_drv3_006_troughs2pct_5d_diff_5d_diff},
    "tcl_drv3_007_troughs2pct_5d_diff_21d_diff":    {"inputs": ["low"],           "func": tcl_drv3_007_troughs2pct_5d_diff_21d_diff},
    "tcl_drv3_008_retest_5d_diff_5d_diff":          {"inputs": ["low"],           "func": tcl_drv3_008_retest_5d_diff_5d_diff},
    "tcl_drv3_009_retest_21d_diff_5d_diff":         {"inputs": ["low"],           "func": tcl_drv3_009_retest_21d_diff_5d_diff},
    "tcl_drv3_010_basing_range_5d_diff_5d_diff":    {"inputs": ["low", "high"],   "func": tcl_drv3_010_basing_range_5d_diff_5d_diff},
    "tcl_drv3_011_basing_range_21d_diff_5d_diff":   {"inputs": ["low", "high"],   "func": tcl_drv3_011_basing_range_21d_diff_5d_diff},
    "tcl_drv3_012_basing_range_21d_diff_21d_diff":  {"inputs": ["low", "high"],   "func": tcl_drv3_012_basing_range_21d_diff_21d_diff},
    "tcl_drv3_013_trough_cv_5d_diff_5d_diff":       {"inputs": ["low"],           "func": tcl_drv3_013_trough_cv_5d_diff_5d_diff},
    "tcl_drv3_014_vol_trough_frac_5d_diff_5d_diff": {"inputs": ["low", "volume"], "func": tcl_drv3_014_vol_trough_frac_5d_diff_5d_diff},
    "tcl_drv3_015_vol_trough_frac_5d_diff_21d_diff":{"inputs": ["low", "volume"], "func": tcl_drv3_015_vol_trough_frac_5d_diff_21d_diff},
    "tcl_drv3_016_rolling_min_slope_5d_diff_5d_diff":{"inputs": ["low"],          "func": tcl_drv3_016_rolling_min_slope_5d_diff_5d_diff},
    "tcl_drv3_017_rolling_min_slope_5d_diff_21d_diff":{"inputs": ["low"],         "func": tcl_drv3_017_rolling_min_slope_5d_diff_21d_diff},
    "tcl_drv3_018_trough_zscore_5d_diff_5d_diff":   {"inputs": ["low"],           "func": tcl_drv3_018_trough_zscore_5d_diff_5d_diff},
    "tcl_drv3_019_trough_zscore_5d_diff_21d_diff":  {"inputs": ["low"],           "func": tcl_drv3_019_trough_zscore_5d_diff_21d_diff},
    "tcl_drv3_020_cnt63d_slope_21d_5d_diff":        {"inputs": ["low"],           "func": tcl_drv3_020_cnt63d_slope_21d_5d_diff},
    "tcl_drv3_021_cnt63d_slope_21d_21d_diff":       {"inputs": ["low"],           "func": tcl_drv3_021_cnt63d_slope_21d_21d_diff},
    "tcl_drv3_022_retest_slope_63d_5d_diff":        {"inputs": ["low"],           "func": tcl_drv3_022_retest_slope_63d_5d_diff},
    "tcl_drv3_023_retest_slope_63d_21d_diff":       {"inputs": ["low"],           "func": tcl_drv3_023_retest_slope_63d_21d_diff},
    "tcl_drv3_024_vol_trough_slope_5d_diff":        {"inputs": ["low", "volume"], "func": tcl_drv3_024_vol_trough_slope_5d_diff},
    "tcl_drv3_025_vol_trough_slope_21d_diff":       {"inputs": ["low", "volume"], "func": tcl_drv3_025_vol_trough_slope_21d_diff},
}
