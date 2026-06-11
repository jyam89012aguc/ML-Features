"""
10_trough_clustering — Base Features 001-075
Domain: density of local minima, repeated bottoms, double/triple-bottom signatures,
        trough spacing and clustering in price and time.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
A local minimum is identified using only trailing data (rolling-min equality).
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


def _local_min_flag(low: pd.Series, w: int) -> pd.Series:
    """
    Backward-only local-minimum flag.
    A bar is flagged as a local min if its low equals the rolling min
    of the trailing w bars (including itself). Uses shift(1) to compare
    to the prior window so the current bar IS included.
    More precisely: low[t] == rolling_min(low, w)[t].
    This is causal — only uses data up to and including t.
    """
    rmin = low.rolling(w, min_periods=max(1, w // 2)).min()
    return (low <= rmin + _EPS).astype(float)


def _trough_count_raw(x, threshold_pct):
    """
    Scalar helper for rolling apply (raw=True).
    Counts bars within threshold_pct of the window minimum.
    """
    if len(x) == 0:
        return np.nan
    mn = np.min(x)
    count = np.sum(x <= mn * (1.0 + threshold_pct) + _EPS)
    return float(count)


def _trough_std_raw(x):
    """Scalar helper: std of values within 3% of window min (trough price dispersion)."""
    if len(x) < 2:
        return np.nan
    mn = np.min(x)
    near = x[x <= mn * 1.03 + _EPS]
    if len(near) < 2:
        return np.nan
    return float(np.std(near))


def _trough_mean_raw(x):
    """Scalar helper: mean of values within 3% of window min."""
    if len(x) == 0:
        return np.nan
    mn = np.min(x)
    near = x[x <= mn * 1.03 + _EPS]
    if len(near) == 0:
        return np.nan
    return float(np.mean(near))


def _trough_spacing_raw(x):
    """
    Scalar helper: mean spacing (in bars) between successive local-min flags.
    x is a binary array of local-min flags.
    """
    idxs = np.where(x > 0.5)[0]
    if len(idxs) < 2:
        return np.nan
    gaps = np.diff(idxs.astype(float))
    return float(np.mean(gaps))


def _trough_spacing_std_raw(x):
    """Scalar helper: std of spacing between successive local-min flags."""
    idxs = np.where(x > 0.5)[0]
    if len(idxs) < 3:
        return np.nan
    gaps = np.diff(idxs.astype(float))
    return float(np.std(gaps))


def _trough_max_gap_raw(x):
    """Scalar helper: maximum gap between successive local-min flags."""
    idxs = np.where(x > 0.5)[0]
    if len(idxs) < 2:
        return np.nan
    gaps = np.diff(idxs.astype(float))
    return float(np.max(gaps))


def _trough_min_gap_raw(x):
    """Scalar helper: minimum gap between successive local-min flags."""
    idxs = np.where(x > 0.5)[0]
    if len(idxs) < 2:
        return np.nan
    gaps = np.diff(idxs.astype(float))
    return float(np.min(gaps))


def _price_range_of_troughs_raw(x):
    """Scalar helper: (max - min) / min of trough prices within window."""
    if len(x) == 0:
        return np.nan
    mn = np.min(x)
    near = x[x <= mn * 1.05 + _EPS]
    if len(near) < 2:
        return np.nan
    rng = np.max(near) - np.min(near)
    base = np.min(near)
    if base < _EPS:
        return np.nan
    return float(rng / base)


def _count_distinct_lows_pct_raw(x, pct):
    """
    Scalar helper: count bars whose value is within pct of the window minimum.
    """
    if len(x) == 0:
        return np.nan
    mn = np.min(x)
    return float(np.sum(x <= mn * (1.0 + pct) + _EPS))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Count of local minima in rolling windows ---

def tcl_001_local_min_count_21d(low: pd.Series) -> pd.Series:
    """Count of bars flagged as local min (5-bar window) within trailing 21 days."""
    flag = _local_min_flag(low, 5)
    return _rolling_sum(flag, _TD_MON)


def tcl_002_local_min_count_63d(low: pd.Series) -> pd.Series:
    """Count of bars flagged as local min (5-bar window) within trailing 63 days."""
    flag = _local_min_flag(low, 5)
    return _rolling_sum(flag, _TD_QTR)


def tcl_003_local_min_count_126d(low: pd.Series) -> pd.Series:
    """Count of bars flagged as local min (5-bar window) within trailing 126 days."""
    flag = _local_min_flag(low, 5)
    return _rolling_sum(flag, _TD_HALF)


def tcl_004_local_min_count_252d(low: pd.Series) -> pd.Series:
    """Count of bars flagged as local min (5-bar window) within trailing 252 days."""
    flag = _local_min_flag(low, 5)
    return _rolling_sum(flag, _TD_YEAR)


def tcl_005_local_min_count_10bar(low: pd.Series) -> pd.Series:
    """Count of bars flagged as local min using 10-bar look-back within 63 days."""
    flag = _local_min_flag(low, 10)
    return _rolling_sum(flag, _TD_QTR)


def tcl_006_local_min_count_21bar(low: pd.Series) -> pd.Series:
    """Count of bars flagged as local min using 21-bar look-back within 126 days."""
    flag = _local_min_flag(low, 21)
    return _rolling_sum(flag, _TD_HALF)


def tcl_007_local_min_count_63bar(low: pd.Series) -> pd.Series:
    """Count of bars flagged as local min using 63-bar look-back within 252 days."""
    flag = _local_min_flag(low, 63)
    return _rolling_sum(flag, _TD_YEAR)


def tcl_008_local_min_fraction_21d(low: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days that are local minima (5-bar definition)."""
    flag = _local_min_flag(low, 5)
    return _rolling_mean(flag, _TD_MON)


def tcl_009_local_min_fraction_63d(low: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days that are local minima (5-bar definition)."""
    flag = _local_min_flag(low, 5)
    return _rolling_mean(flag, _TD_QTR)


def tcl_010_local_min_fraction_126d(low: pd.Series) -> pd.Series:
    """Fraction of trailing 126 days that are local minima (5-bar definition)."""
    flag = _local_min_flag(low, 5)
    return _rolling_mean(flag, _TD_HALF)


def tcl_011_local_min_fraction_252d(low: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days that are local minima (5-bar definition)."""
    flag = _local_min_flag(low, 5)
    return _rolling_mean(flag, _TD_YEAR)


def tcl_012_local_min_count_close_63d(close: pd.Series) -> pd.Series:
    """Count of close-based local minima (5-bar window) within trailing 63 days."""
    flag = _local_min_flag(close, 5)
    return _rolling_sum(flag, _TD_QTR)


# --- Group B (013-025): Price-proximity trough counts (double/triple bottom) ---

def tcl_013_troughs_within_1pct_63d(low: pd.Series) -> pd.Series:
    """Count of bars within 1% of trailing 63-day low (double/triple bottom density)."""
    def _cnt(x):
        return _trough_count_raw(x, 0.01)
    return low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_cnt, raw=True)


def tcl_014_troughs_within_2pct_63d(low: pd.Series) -> pd.Series:
    """Count of bars within 2% of trailing 63-day low."""
    def _cnt(x):
        return _trough_count_raw(x, 0.02)
    return low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_cnt, raw=True)


def tcl_015_troughs_within_5pct_63d(low: pd.Series) -> pd.Series:
    """Count of bars within 5% of trailing 63-day low."""
    def _cnt(x):
        return _trough_count_raw(x, 0.05)
    return low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_cnt, raw=True)


def tcl_016_troughs_within_1pct_126d(low: pd.Series) -> pd.Series:
    """Count of bars within 1% of trailing 126-day low."""
    def _cnt(x):
        return _trough_count_raw(x, 0.01)
    return low.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_cnt, raw=True)


def tcl_017_troughs_within_2pct_126d(low: pd.Series) -> pd.Series:
    """Count of bars within 2% of trailing 126-day low."""
    def _cnt(x):
        return _trough_count_raw(x, 0.02)
    return low.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_cnt, raw=True)


def tcl_018_troughs_within_5pct_126d(low: pd.Series) -> pd.Series:
    """Count of bars within 5% of trailing 126-day low."""
    def _cnt(x):
        return _trough_count_raw(x, 0.05)
    return low.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_cnt, raw=True)


def tcl_019_troughs_within_1pct_252d(low: pd.Series) -> pd.Series:
    """Count of bars within 1% of trailing 252-day low."""
    def _cnt(x):
        return _trough_count_raw(x, 0.01)
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_cnt, raw=True)


def tcl_020_troughs_within_3pct_252d(low: pd.Series) -> pd.Series:
    """Count of bars within 3% of trailing 252-day low."""
    def _cnt(x):
        return _trough_count_raw(x, 0.03)
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_cnt, raw=True)


def tcl_021_troughs_within_5pct_252d(low: pd.Series) -> pd.Series:
    """Count of bars within 5% of trailing 252-day low."""
    def _cnt(x):
        return _trough_count_raw(x, 0.05)
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_cnt, raw=True)


def tcl_022_trough_fraction_within_2pct_63d(low: pd.Series) -> pd.Series:
    """Fraction of trailing 63-day bars within 2% of 63-day low."""
    def _frac(x):
        if len(x) == 0:
            return np.nan
        mn = np.min(x)
        return float(np.sum(x <= mn * 1.02 + _EPS)) / len(x)
    return low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_frac, raw=True)


def tcl_023_trough_fraction_within_5pct_252d(low: pd.Series) -> pd.Series:
    """Fraction of trailing 252-day bars within 5% of 252-day low."""
    def _frac(x):
        if len(x) == 0:
            return np.nan
        mn = np.min(x)
        return float(np.sum(x <= mn * 1.05 + _EPS)) / len(x)
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_frac, raw=True)


def tcl_024_troughs_within_10pct_252d(low: pd.Series) -> pd.Series:
    """Count of bars within 10% of trailing 252-day low (wide support band)."""
    def _cnt(x):
        return _trough_count_raw(x, 0.10)
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_cnt, raw=True)


def tcl_025_close_troughs_within_3pct_126d(close: pd.Series) -> pd.Series:
    """Count of close bars within 3% of trailing 126-day close low."""
    def _cnt(x):
        return _trough_count_raw(x, 0.03)
    return close.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_cnt, raw=True)


# --- Group C (026-037): Trough price dispersion (how tight is the basing zone?) ---

def tcl_026_trough_price_std_63d(low: pd.Series) -> pd.Series:
    """Std of lows within 3% of 63-day low (basing tightness)."""
    return low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_trough_std_raw, raw=True)


def tcl_027_trough_price_std_126d(low: pd.Series) -> pd.Series:
    """Std of lows within 3% of 126-day low."""
    return low.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_trough_std_raw, raw=True)


def tcl_028_trough_price_std_252d(low: pd.Series) -> pd.Series:
    """Std of lows within 3% of 252-day low."""
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_trough_std_raw, raw=True)


def tcl_029_trough_price_cv_63d(low: pd.Series) -> pd.Series:
    """CV (std/mean) of lows within 3% of 63-day low (normalized dispersion)."""
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


def tcl_030_trough_price_cv_252d(low: pd.Series) -> pd.Series:
    """CV of lows within 3% of 252-day low."""
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
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_cv, raw=True)


def tcl_031_trough_price_range_pct_63d(low: pd.Series) -> pd.Series:
    """(max-min)/min of lows within 5% of 63-day low (range of support band)."""
    return low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_price_range_of_troughs_raw, raw=True)


def tcl_032_trough_price_range_pct_126d(low: pd.Series) -> pd.Series:
    """(max-min)/min of lows within 5% of 126-day low."""
    return low.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_price_range_of_troughs_raw, raw=True)


def tcl_033_trough_price_range_pct_252d(low: pd.Series) -> pd.Series:
    """(max-min)/min of lows within 5% of 252-day low."""
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_price_range_of_troughs_raw, raw=True)


def tcl_034_trough_mean_vs_min_63d(low: pd.Series) -> pd.Series:
    """Mean of near-lows minus window min, normalized by window min (63d)."""
    rmin = _rolling_min(low, _TD_QTR)
    near_mean = low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_trough_mean_raw, raw=True)
    return _safe_div(near_mean - rmin, rmin)


def tcl_035_trough_mean_vs_min_252d(low: pd.Series) -> pd.Series:
    """Mean of near-lows minus window min, normalized by window min (252d)."""
    rmin = _rolling_min(low, _TD_YEAR)
    near_mean = low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_trough_mean_raw, raw=True)
    return _safe_div(near_mean - rmin, rmin)


def tcl_036_close_trough_std_126d(close: pd.Series) -> pd.Series:
    """Std of closes within 3% of 126-day close low (close-based support tightness)."""
    return close.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_trough_std_raw, raw=True)


def tcl_037_close_trough_range_252d(close: pd.Series) -> pd.Series:
    """(max-min)/min of closes within 5% of 252-day close low."""
    return close.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_price_range_of_troughs_raw, raw=True)


# --- Group D (038-050): Trough time-spacing features ---

def tcl_038_trough_spacing_mean_63d(low: pd.Series) -> pd.Series:
    """Mean bar-spacing between consecutive local-min flags in trailing 63 days."""
    flag = _local_min_flag(low, 5)
    return flag.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_trough_spacing_raw, raw=True)


def tcl_039_trough_spacing_mean_126d(low: pd.Series) -> pd.Series:
    """Mean bar-spacing between consecutive local-min flags in trailing 126 days."""
    flag = _local_min_flag(low, 5)
    return flag.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_trough_spacing_raw, raw=True)


def tcl_040_trough_spacing_mean_252d(low: pd.Series) -> pd.Series:
    """Mean bar-spacing between consecutive local-min flags in trailing 252 days."""
    flag = _local_min_flag(low, 5)
    return flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_trough_spacing_raw, raw=True)


def tcl_041_trough_spacing_std_63d(low: pd.Series) -> pd.Series:
    """Std of bar-spacing between local-min flags in trailing 63 days."""
    flag = _local_min_flag(low, 5)
    return flag.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_trough_spacing_std_raw, raw=True)


def tcl_042_trough_spacing_std_252d(low: pd.Series) -> pd.Series:
    """Std of bar-spacing between local-min flags in trailing 252 days."""
    flag = _local_min_flag(low, 5)
    return flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_trough_spacing_std_raw, raw=True)


def tcl_043_trough_max_gap_126d(low: pd.Series) -> pd.Series:
    """Maximum gap between consecutive local-min events in trailing 126 days."""
    flag = _local_min_flag(low, 5)
    return flag.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_trough_max_gap_raw, raw=True)


def tcl_044_trough_min_gap_126d(low: pd.Series) -> pd.Series:
    """Minimum gap between consecutive local-min events in trailing 126 days."""
    flag = _local_min_flag(low, 5)
    return flag.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_trough_min_gap_raw, raw=True)


def tcl_045_trough_max_gap_252d(low: pd.Series) -> pd.Series:
    """Maximum gap between consecutive local-min events in trailing 252 days."""
    flag = _local_min_flag(low, 5)
    return flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_trough_max_gap_raw, raw=True)


def tcl_046_trough_min_gap_252d(low: pd.Series) -> pd.Series:
    """Minimum gap between consecutive local-min events in trailing 252 days."""
    flag = _local_min_flag(low, 5)
    return flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_trough_min_gap_raw, raw=True)


def tcl_047_trough_spacing_cv_252d(low: pd.Series) -> pd.Series:
    """CV of bar-spacing between local-min events in trailing 252 days."""
    def _cv_spacing(x):
        idxs = np.where(x > 0.5)[0]
        if len(idxs) < 3:
            return np.nan
        gaps = np.diff(idxs.astype(float))
        m = np.mean(gaps)
        if m < _EPS:
            return np.nan
        return float(np.std(gaps) / m)
    flag = _local_min_flag(low, 5)
    return flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_cv_spacing, raw=True)


def tcl_048_trough_spacing_mean_10bar_126d(low: pd.Series) -> pd.Series:
    """Mean spacing between 10-bar local-min events in trailing 126 days."""
    flag = _local_min_flag(low, 10)
    return flag.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_trough_spacing_raw, raw=True)


def tcl_049_close_trough_spacing_mean_252d(close: pd.Series) -> pd.Series:
    """Mean spacing between close-based local-min events in trailing 252 days."""
    flag = _local_min_flag(close, 5)
    return flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_trough_spacing_raw, raw=True)


def tcl_050_trough_density_ratio_63_126(low: pd.Series) -> pd.Series:
    """Ratio of 63-day trough count to 126-day trough count (recent vs older density)."""
    cnt_63 = tcl_002_local_min_count_63d(low)
    cnt_126 = tcl_003_local_min_count_126d(low)
    return _safe_div(cnt_63, cnt_126)


# --- Group E (051-063): Support retest and revisit counts ---

def tcl_051_support_retest_count_1pct_63d(low: pd.Series) -> pd.Series:
    """
    Count of times in trailing 63 days the low came within 1% of the
    rolling 252-day low (support retest frequency).
    """
    rmin_252 = _rolling_min(low, _TD_YEAR)
    near_support = (low <= rmin_252 * 1.01 + _EPS).astype(float)
    return _rolling_sum(near_support, _TD_QTR)


def tcl_052_support_retest_count_2pct_63d(low: pd.Series) -> pd.Series:
    """Count of 63-day support retests within 2% of 252-day low."""
    rmin_252 = _rolling_min(low, _TD_YEAR)
    near_support = (low <= rmin_252 * 1.02 + _EPS).astype(float)
    return _rolling_sum(near_support, _TD_QTR)


def tcl_053_support_retest_count_5pct_126d(low: pd.Series) -> pd.Series:
    """Count of 126-day support retests within 5% of 252-day low."""
    rmin_252 = _rolling_min(low, _TD_YEAR)
    near_support = (low <= rmin_252 * 1.05 + _EPS).astype(float)
    return _rolling_sum(near_support, _TD_HALF)


def tcl_054_support_retest_count_3pct_252d(low: pd.Series) -> pd.Series:
    """Count of 252-day support retests within 3% of 252-day low."""
    rmin_252 = _rolling_min(low, _TD_YEAR)
    near_support = (low <= rmin_252 * 1.03 + _EPS).astype(float)
    return _rolling_sum(near_support, _TD_YEAR)


def tcl_055_support_retest_fraction_63d(low: pd.Series) -> pd.Series:
    """Fraction of 63-day bars retesting support within 3% of 252-day low."""
    rmin_252 = _rolling_min(low, _TD_YEAR)
    near_support = (low <= rmin_252 * 1.03 + _EPS).astype(float)
    return _rolling_mean(near_support, _TD_QTR)


def tcl_056_support_retest_fraction_126d(low: pd.Series) -> pd.Series:
    """Fraction of 126-day bars retesting support within 3% of 252-day low."""
    rmin_252 = _rolling_min(low, _TD_YEAR)
    near_support = (low <= rmin_252 * 1.03 + _EPS).astype(float)
    return _rolling_mean(near_support, _TD_HALF)


def tcl_057_support_retest_count_close_2pct_63d(close: pd.Series) -> pd.Series:
    """Count of 63-day close-based support retests within 2% of 252-day close low."""
    rmin_252 = _rolling_min(close, _TD_YEAR)
    near_support = (close <= rmin_252 * 1.02 + _EPS).astype(float)
    return _rolling_sum(near_support, _TD_QTR)


def tcl_058_support_band_width_252d(low: pd.Series, high: pd.Series) -> pd.Series:
    """
    Width of 252-day support band: (21-day high max - 252-day low min) / 252-day low min.
    Measures how wide the price consolidation zone is around the trailing low.
    """
    rmin_252 = _rolling_min(low, _TD_YEAR)
    rmax_21 = _rolling_max(high, _TD_MON)
    return _safe_div(rmax_21 - rmin_252, rmin_252)


def tcl_059_support_band_tightness_63d(low: pd.Series) -> pd.Series:
    """
    1 / (1 + support_band_width_63d): tightness ratio.
    Higher = tighter basing around the 63-day low.
    """
    rmin = _rolling_min(low, _TD_QTR)
    rmax = _rolling_max(low, _TD_QTR)
    width = _safe_div(rmax - rmin, rmin)
    return 1.0 / (1.0 + width.fillna(np.inf))


def tcl_060_support_band_tightness_252d(low: pd.Series) -> pd.Series:
    """1 / (1 + support_band_width_252d): tightness ratio over 252 days."""
    rmin = _rolling_min(low, _TD_YEAR)
    rmax = _rolling_max(low, _TD_YEAR)
    width = _safe_div(rmax - rmin, rmin)
    return 1.0 / (1.0 + width.fillna(np.inf))


def tcl_061_close_near_21d_low_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days where close is within 2% of 21-day rolling low."""
    rmin_21 = _rolling_min(close, _TD_MON)
    near = (close <= rmin_21 * 1.02 + _EPS).astype(float)
    return _rolling_mean(near, _TD_QTR)


def tcl_062_low_near_21d_low_fraction_126d(low: pd.Series) -> pd.Series:
    """Fraction of trailing 126 days where low is within 1% of 21-day rolling low."""
    rmin_21 = _rolling_min(low, _TD_MON)
    near = (low <= rmin_21 * 1.01 + _EPS).astype(float)
    return _rolling_mean(near, _TD_HALF)


def tcl_063_retest_acceleration_63vs126(low: pd.Series) -> pd.Series:
    """Ratio of 63-day retest count to 126-day retest count (recent acceleration)."""
    rmin_252 = _rolling_min(low, _TD_YEAR)
    near = (low <= rmin_252 * 1.03 + _EPS).astype(float)
    cnt_63 = _rolling_sum(near, _TD_QTR)
    cnt_126 = _rolling_sum(near, _TD_HALF)
    return _safe_div(cnt_63, cnt_126)


# --- Group F (064-075): Basing pattern tightness and composite measures ---

def tcl_064_basing_range_21d(low: pd.Series, high: pd.Series) -> pd.Series:
    """21-day (high max - low min) / low min — basing range width."""
    return _safe_div(_rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON),
                     _rolling_min(low, _TD_MON))


def tcl_065_basing_range_63d(low: pd.Series, high: pd.Series) -> pd.Series:
    """63-day (high max - low min) / low min — basing range width."""
    return _safe_div(_rolling_max(high, _TD_QTR) - _rolling_min(low, _TD_QTR),
                     _rolling_min(low, _TD_QTR))


def tcl_066_basing_range_126d(low: pd.Series, high: pd.Series) -> pd.Series:
    """126-day (high max - low min) / low min — basing range width."""
    return _safe_div(_rolling_max(high, _TD_HALF) - _rolling_min(low, _TD_HALF),
                     _rolling_min(low, _TD_HALF))


def tcl_067_close_std_normalized_63d(close: pd.Series) -> pd.Series:
    """Std of close / mean of close over 63 days (normalized close volatility in base)."""
    return _safe_div(_rolling_std(close, _TD_QTR), _rolling_mean(close, _TD_QTR))


def tcl_068_close_std_normalized_126d(close: pd.Series) -> pd.Series:
    """Std of close / mean of close over 126 days."""
    return _safe_div(_rolling_std(close, _TD_HALF), _rolling_mean(close, _TD_HALF))


def tcl_069_low_std_normalized_252d(low: pd.Series) -> pd.Series:
    """Std of low / mean of low over 252 days (normalized low price spread)."""
    return _safe_div(_rolling_std(low, _TD_YEAR), _rolling_mean(low, _TD_YEAR))


def tcl_070_trough_count_density_score_63d(low: pd.Series) -> pd.Series:
    """
    Composite: (troughs_within_3%) * (1 - trough_cv_63d).
    Higher = many tight troughs (strong double/triple bottom signal).
    """
    def _cnt3(x):
        return _trough_count_raw(x, 0.03)
    cnt = low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_cnt3, raw=True)
    cv = tcl_029_trough_price_cv_63d(low).fillna(1.0)
    return cnt * (1.0 - cv.clip(upper=1.0))


def tcl_071_trough_count_density_score_252d(low: pd.Series) -> pd.Series:
    """
    Composite: (troughs_within_5%) * (1 - trough_cv_252d).
    Higher = many tight troughs over 252-day window.
    """
    def _cnt5(x):
        return _trough_count_raw(x, 0.05)
    cnt = low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_cnt5, raw=True)
    cv = tcl_030_trough_price_cv_252d(low).fillna(1.0)
    return cnt * (1.0 - cv.clip(upper=1.0))


def tcl_072_local_min_flag_ewma_63d(low: pd.Series) -> pd.Series:
    """EWM of local-min flag (span=63): exponentially weighted local-min rate."""
    flag = _local_min_flag(low, 5)
    return _ewm_mean(flag, _TD_QTR)


def tcl_073_local_min_flag_ewma_21d(low: pd.Series) -> pd.Series:
    """EWM of local-min flag (span=21): short-term local-min rate."""
    flag = _local_min_flag(low, 5)
    return _ewm_mean(flag, _TD_MON)


def tcl_074_trough_cluster_zscore_63d(low: pd.Series) -> pd.Series:
    """Z-score of 63-day trough count vs its own 252-day rolling mean/std."""
    cnt = tcl_002_local_min_count_63d(low)
    return _safe_div(cnt - _rolling_mean(cnt, _TD_YEAR), _rolling_std(cnt, _TD_YEAR))


def tcl_075_volume_at_troughs_fraction_63d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Fraction of 63-day total volume occurring on local-min days.
    Higher = volume concentrated at trough touches (capitulation signature).
    """
    flag = _local_min_flag(low, 5)
    vol_at_trough = flag * volume
    total_vol = _rolling_sum(volume, _TD_QTR)
    trough_vol = _rolling_sum(vol_at_trough, _TD_QTR)
    return _safe_div(trough_vol, total_vol)


# ── Registry ──────────────────────────────────────────────────────────────────

TROUGH_CLUSTERING_REGISTRY_001_075 = {
    "tcl_001_local_min_count_21d":              {"inputs": ["low"],           "func": tcl_001_local_min_count_21d},
    "tcl_002_local_min_count_63d":              {"inputs": ["low"],           "func": tcl_002_local_min_count_63d},
    "tcl_003_local_min_count_126d":             {"inputs": ["low"],           "func": tcl_003_local_min_count_126d},
    "tcl_004_local_min_count_252d":             {"inputs": ["low"],           "func": tcl_004_local_min_count_252d},
    "tcl_005_local_min_count_10bar":            {"inputs": ["low"],           "func": tcl_005_local_min_count_10bar},
    "tcl_006_local_min_count_21bar":            {"inputs": ["low"],           "func": tcl_006_local_min_count_21bar},
    "tcl_007_local_min_count_63bar":            {"inputs": ["low"],           "func": tcl_007_local_min_count_63bar},
    "tcl_008_local_min_fraction_21d":           {"inputs": ["low"],           "func": tcl_008_local_min_fraction_21d},
    "tcl_009_local_min_fraction_63d":           {"inputs": ["low"],           "func": tcl_009_local_min_fraction_63d},
    "tcl_010_local_min_fraction_126d":          {"inputs": ["low"],           "func": tcl_010_local_min_fraction_126d},
    "tcl_011_local_min_fraction_252d":          {"inputs": ["low"],           "func": tcl_011_local_min_fraction_252d},
    "tcl_012_local_min_count_close_63d":        {"inputs": ["close"],         "func": tcl_012_local_min_count_close_63d},
    "tcl_013_troughs_within_1pct_63d":          {"inputs": ["low"],           "func": tcl_013_troughs_within_1pct_63d},
    "tcl_014_troughs_within_2pct_63d":          {"inputs": ["low"],           "func": tcl_014_troughs_within_2pct_63d},
    "tcl_015_troughs_within_5pct_63d":          {"inputs": ["low"],           "func": tcl_015_troughs_within_5pct_63d},
    "tcl_016_troughs_within_1pct_126d":         {"inputs": ["low"],           "func": tcl_016_troughs_within_1pct_126d},
    "tcl_017_troughs_within_2pct_126d":         {"inputs": ["low"],           "func": tcl_017_troughs_within_2pct_126d},
    "tcl_018_troughs_within_5pct_126d":         {"inputs": ["low"],           "func": tcl_018_troughs_within_5pct_126d},
    "tcl_019_troughs_within_1pct_252d":         {"inputs": ["low"],           "func": tcl_019_troughs_within_1pct_252d},
    "tcl_020_troughs_within_3pct_252d":         {"inputs": ["low"],           "func": tcl_020_troughs_within_3pct_252d},
    "tcl_021_troughs_within_5pct_252d":         {"inputs": ["low"],           "func": tcl_021_troughs_within_5pct_252d},
    "tcl_022_trough_fraction_within_2pct_63d":  {"inputs": ["low"],           "func": tcl_022_trough_fraction_within_2pct_63d},
    "tcl_023_trough_fraction_within_5pct_252d": {"inputs": ["low"],           "func": tcl_023_trough_fraction_within_5pct_252d},
    "tcl_024_troughs_within_10pct_252d":        {"inputs": ["low"],           "func": tcl_024_troughs_within_10pct_252d},
    "tcl_025_close_troughs_within_3pct_126d":   {"inputs": ["close"],         "func": tcl_025_close_troughs_within_3pct_126d},
    "tcl_026_trough_price_std_63d":             {"inputs": ["low"],           "func": tcl_026_trough_price_std_63d},
    "tcl_027_trough_price_std_126d":            {"inputs": ["low"],           "func": tcl_027_trough_price_std_126d},
    "tcl_028_trough_price_std_252d":            {"inputs": ["low"],           "func": tcl_028_trough_price_std_252d},
    "tcl_029_trough_price_cv_63d":              {"inputs": ["low"],           "func": tcl_029_trough_price_cv_63d},
    "tcl_030_trough_price_cv_252d":             {"inputs": ["low"],           "func": tcl_030_trough_price_cv_252d},
    "tcl_031_trough_price_range_pct_63d":       {"inputs": ["low"],           "func": tcl_031_trough_price_range_pct_63d},
    "tcl_032_trough_price_range_pct_126d":      {"inputs": ["low"],           "func": tcl_032_trough_price_range_pct_126d},
    "tcl_033_trough_price_range_pct_252d":      {"inputs": ["low"],           "func": tcl_033_trough_price_range_pct_252d},
    "tcl_034_trough_mean_vs_min_63d":           {"inputs": ["low"],           "func": tcl_034_trough_mean_vs_min_63d},
    "tcl_035_trough_mean_vs_min_252d":          {"inputs": ["low"],           "func": tcl_035_trough_mean_vs_min_252d},
    "tcl_036_close_trough_std_126d":            {"inputs": ["close"],         "func": tcl_036_close_trough_std_126d},
    "tcl_037_close_trough_range_252d":          {"inputs": ["close"],         "func": tcl_037_close_trough_range_252d},
    "tcl_038_trough_spacing_mean_63d":          {"inputs": ["low"],           "func": tcl_038_trough_spacing_mean_63d},
    "tcl_039_trough_spacing_mean_126d":         {"inputs": ["low"],           "func": tcl_039_trough_spacing_mean_126d},
    "tcl_040_trough_spacing_mean_252d":         {"inputs": ["low"],           "func": tcl_040_trough_spacing_mean_252d},
    "tcl_041_trough_spacing_std_63d":           {"inputs": ["low"],           "func": tcl_041_trough_spacing_std_63d},
    "tcl_042_trough_spacing_std_252d":          {"inputs": ["low"],           "func": tcl_042_trough_spacing_std_252d},
    "tcl_043_trough_max_gap_126d":              {"inputs": ["low"],           "func": tcl_043_trough_max_gap_126d},
    "tcl_044_trough_min_gap_126d":              {"inputs": ["low"],           "func": tcl_044_trough_min_gap_126d},
    "tcl_045_trough_max_gap_252d":              {"inputs": ["low"],           "func": tcl_045_trough_max_gap_252d},
    "tcl_046_trough_min_gap_252d":              {"inputs": ["low"],           "func": tcl_046_trough_min_gap_252d},
    "tcl_047_trough_spacing_cv_252d":           {"inputs": ["low"],           "func": tcl_047_trough_spacing_cv_252d},
    "tcl_048_trough_spacing_mean_10bar_126d":   {"inputs": ["low"],           "func": tcl_048_trough_spacing_mean_10bar_126d},
    "tcl_049_close_trough_spacing_mean_252d":   {"inputs": ["close"],         "func": tcl_049_close_trough_spacing_mean_252d},
    "tcl_050_trough_density_ratio_63_126":      {"inputs": ["low"],           "func": tcl_050_trough_density_ratio_63_126},
    "tcl_051_support_retest_count_1pct_63d":    {"inputs": ["low"],           "func": tcl_051_support_retest_count_1pct_63d},
    "tcl_052_support_retest_count_2pct_63d":    {"inputs": ["low"],           "func": tcl_052_support_retest_count_2pct_63d},
    "tcl_053_support_retest_count_5pct_126d":   {"inputs": ["low"],           "func": tcl_053_support_retest_count_5pct_126d},
    "tcl_054_support_retest_count_3pct_252d":   {"inputs": ["low"],           "func": tcl_054_support_retest_count_3pct_252d},
    "tcl_055_support_retest_fraction_63d":      {"inputs": ["low"],           "func": tcl_055_support_retest_fraction_63d},
    "tcl_056_support_retest_fraction_126d":     {"inputs": ["low"],           "func": tcl_056_support_retest_fraction_126d},
    "tcl_057_support_retest_count_close_2pct_63d": {"inputs": ["close"],      "func": tcl_057_support_retest_count_close_2pct_63d},
    "tcl_058_support_band_width_252d":          {"inputs": ["low", "high"],   "func": tcl_058_support_band_width_252d},
    "tcl_059_support_band_tightness_63d":       {"inputs": ["low"],           "func": tcl_059_support_band_tightness_63d},
    "tcl_060_support_band_tightness_252d":      {"inputs": ["low"],           "func": tcl_060_support_band_tightness_252d},
    "tcl_061_close_near_21d_low_fraction_63d":  {"inputs": ["close"],         "func": tcl_061_close_near_21d_low_fraction_63d},
    "tcl_062_low_near_21d_low_fraction_126d":   {"inputs": ["low"],           "func": tcl_062_low_near_21d_low_fraction_126d},
    "tcl_063_retest_acceleration_63vs126":      {"inputs": ["low"],           "func": tcl_063_retest_acceleration_63vs126},
    "tcl_064_basing_range_21d":                 {"inputs": ["low", "high"],   "func": tcl_064_basing_range_21d},
    "tcl_065_basing_range_63d":                 {"inputs": ["low", "high"],   "func": tcl_065_basing_range_63d},
    "tcl_066_basing_range_126d":                {"inputs": ["low", "high"],   "func": tcl_066_basing_range_126d},
    "tcl_067_close_std_normalized_63d":         {"inputs": ["close"],         "func": tcl_067_close_std_normalized_63d},
    "tcl_068_close_std_normalized_126d":        {"inputs": ["close"],         "func": tcl_068_close_std_normalized_126d},
    "tcl_069_low_std_normalized_252d":          {"inputs": ["low"],           "func": tcl_069_low_std_normalized_252d},
    "tcl_070_trough_count_density_score_63d":   {"inputs": ["low"],           "func": tcl_070_trough_count_density_score_63d},
    "tcl_071_trough_count_density_score_252d":  {"inputs": ["low"],           "func": tcl_071_trough_count_density_score_252d},
    "tcl_072_local_min_flag_ewma_63d":          {"inputs": ["low"],           "func": tcl_072_local_min_flag_ewma_63d},
    "tcl_073_local_min_flag_ewma_21d":          {"inputs": ["low"],           "func": tcl_073_local_min_flag_ewma_21d},
    "tcl_074_trough_cluster_zscore_63d":        {"inputs": ["low"],           "func": tcl_074_trough_cluster_zscore_63d},
    "tcl_075_volume_at_troughs_fraction_63d":   {"inputs": ["low", "volume"], "func": tcl_075_volume_at_troughs_fraction_63d},
}
