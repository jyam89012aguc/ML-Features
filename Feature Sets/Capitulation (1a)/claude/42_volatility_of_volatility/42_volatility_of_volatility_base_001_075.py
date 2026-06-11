"""
42_volatility_of_volatility — Base Features 001-075
Domain: instability/dispersion of the volatility series itself (vol-of-vol)
Measures: std of rolling realized-vol, CV of vol, range of vol over windows,
mean-absolute-change of vol, vol z-score dispersion, path jaggedness,
percentile ranks of vol instability, ATR instability.
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
_SQRT252 = 252 ** 0.5

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


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS) / s.shift(1).clip(lower=_EPS))


def _realized_vol(close: pd.Series, w: int) -> pd.Series:
    """Annualized realized volatility over w-day rolling window."""
    lr = _log_ret(close)
    return lr.rolling(w, min_periods=max(2, w // 2)).std() * _SQRT252


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _atr(close: pd.Series, high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """Average True Range over w-day window."""
    return _rolling_mean(_tr(close, high, low), w)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Std-of-rolling-realized-vol (core vol-of-vol) ---

def vov_001_std_of_rvol21_over_63d(close: pd.Series) -> pd.Series:
    """Std of 21-day realized vol measured over trailing 63 days."""
    rv = _realized_vol(close, _TD_MON)
    return _rolling_std(rv, _TD_QTR)


def vov_002_std_of_rvol21_over_126d(close: pd.Series) -> pd.Series:
    """Std of 21-day realized vol measured over trailing 126 days."""
    rv = _realized_vol(close, _TD_MON)
    return _rolling_std(rv, _TD_HALF)


def vov_003_std_of_rvol21_over_252d(close: pd.Series) -> pd.Series:
    """Std of 21-day realized vol measured over trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    return _rolling_std(rv, _TD_YEAR)


def vov_004_std_of_rvol5_over_21d(close: pd.Series) -> pd.Series:
    """Std of 5-day realized vol measured over trailing 21 days."""
    rv = _realized_vol(close, _TD_WEEK)
    return _rolling_std(rv, _TD_MON)


def vov_005_std_of_rvol5_over_63d(close: pd.Series) -> pd.Series:
    """Std of 5-day realized vol measured over trailing 63 days."""
    rv = _realized_vol(close, _TD_WEEK)
    return _rolling_std(rv, _TD_QTR)


def vov_006_std_of_rvol63_over_252d(close: pd.Series) -> pd.Series:
    """Std of 63-day realized vol measured over trailing 252 days."""
    rv = _realized_vol(close, _TD_QTR)
    return _rolling_std(rv, _TD_YEAR)


def vov_007_std_of_rvol10_over_63d(close: pd.Series) -> pd.Series:
    """Std of 10-day realized vol measured over trailing 63 days."""
    rv = _realized_vol(close, 10)
    return _rolling_std(rv, _TD_QTR)


def vov_008_std_of_rvol10_over_126d(close: pd.Series) -> pd.Series:
    """Std of 10-day realized vol measured over trailing 126 days."""
    rv = _realized_vol(close, 10)
    return _rolling_std(rv, _TD_HALF)


def vov_009_std_of_rvol21_over_21d(close: pd.Series) -> pd.Series:
    """Std of 21-day realized vol measured over trailing 21 days (short-window vov)."""
    rv = _realized_vol(close, _TD_MON)
    return _rolling_std(rv, _TD_MON)


def vov_010_std_of_rvol63_over_126d(close: pd.Series) -> pd.Series:
    """Std of 63-day realized vol measured over trailing 126 days."""
    rv = _realized_vol(close, _TD_QTR)
    return _rolling_std(rv, _TD_HALF)


def vov_011_vov_ratio_63d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of short-window vov (63d) to long-window vov (252d) using 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    s63 = _rolling_std(rv, _TD_QTR)
    s252 = _rolling_std(rv, _TD_YEAR)
    return _safe_div(s63, s252)


def vov_012_vov_ratio_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21d-window vov to 63d-window vov using 5d rvol."""
    rv = _realized_vol(close, _TD_WEEK)
    s21 = _rolling_std(rv, _TD_MON)
    s63 = _rolling_std(rv, _TD_QTR)
    return _safe_div(s21, s63)


def vov_013_std_of_rvol21_norm_by_mean(close: pd.Series) -> pd.Series:
    """63d std of 21d rvol normalized by 63d mean of 21d rvol (CV)."""
    rv = _realized_vol(close, _TD_MON)
    s = _rolling_std(rv, _TD_QTR)
    m = _rolling_mean(rv, _TD_QTR)
    return _safe_div(s, m.clip(lower=_EPS))


def vov_014_vov_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d vov (std of 21d rvol) within trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_QTR)
    return vv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vov_015_expanding_vov_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of 63d vov."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_QTR)
    return vv.expanding(min_periods=_TD_QTR).rank(pct=True)


# --- Group B (016-030): Coefficient of variation of realized vol ---

def vov_016_cv_rvol21_63d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of 21d rvol over 63d window."""
    rv = _realized_vol(close, _TD_MON)
    return _safe_div(_rolling_std(rv, _TD_QTR), _rolling_mean(rv, _TD_QTR).clip(lower=_EPS))


def vov_017_cv_rvol21_126d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of 21d rvol over 126d window."""
    rv = _realized_vol(close, _TD_MON)
    return _safe_div(_rolling_std(rv, _TD_HALF), _rolling_mean(rv, _TD_HALF).clip(lower=_EPS))


def vov_018_cv_rvol21_252d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of 21d rvol over 252d window."""
    rv = _realized_vol(close, _TD_MON)
    return _safe_div(_rolling_std(rv, _TD_YEAR), _rolling_mean(rv, _TD_YEAR).clip(lower=_EPS))


def vov_019_cv_rvol5_63d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of 5d rvol over 63d window."""
    rv = _realized_vol(close, _TD_WEEK)
    return _safe_div(_rolling_std(rv, _TD_QTR), _rolling_mean(rv, _TD_QTR).clip(lower=_EPS))


def vov_020_cv_rvol5_252d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of 5d rvol over 252d window."""
    rv = _realized_vol(close, _TD_WEEK)
    return _safe_div(_rolling_std(rv, _TD_YEAR), _rolling_mean(rv, _TD_YEAR).clip(lower=_EPS))


def vov_021_cv_rvol63_252d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of 63d rvol over 252d window."""
    rv = _realized_vol(close, _TD_QTR)
    return _safe_div(_rolling_std(rv, _TD_YEAR), _rolling_mean(rv, _TD_YEAR).clip(lower=_EPS))


def vov_022_cv_atr21_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Coefficient of variation of 21d ATR over 63d window."""
    a = _atr(close, high, low, _TD_MON)
    return _safe_div(_rolling_std(a, _TD_QTR), _rolling_mean(a, _TD_QTR).clip(lower=_EPS))


def vov_023_cv_atr21_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Coefficient of variation of 21d ATR over 252d window."""
    a = _atr(close, high, low, _TD_MON)
    return _safe_div(_rolling_std(a, _TD_YEAR), _rolling_mean(a, _TD_YEAR).clip(lower=_EPS))


def vov_024_cv_rvol10_63d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of 10d rvol over 63d window."""
    rv = _realized_vol(close, 10)
    return _safe_div(_rolling_std(rv, _TD_QTR), _rolling_mean(rv, _TD_QTR).clip(lower=_EPS))


def vov_025_cv_rvol10_126d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of 10d rvol over 126d window."""
    rv = _realized_vol(close, 10)
    return _safe_div(_rolling_std(rv, _TD_HALF), _rolling_mean(rv, _TD_HALF).clip(lower=_EPS))


def vov_026_cv_rvol21_21d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of 21d rvol over 21d window (short-term instability)."""
    rv = _realized_vol(close, _TD_MON)
    return _safe_div(_rolling_std(rv, _TD_MON), _rolling_mean(rv, _TD_MON).clip(lower=_EPS))


def vov_027_cv_ratio_63d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63d CV of 21d rvol to 252d CV (short vs long instability)."""
    rv = _realized_vol(close, _TD_MON)
    cv63 = _safe_div(_rolling_std(rv, _TD_QTR), _rolling_mean(rv, _TD_QTR).clip(lower=_EPS))
    cv252 = _safe_div(_rolling_std(rv, _TD_YEAR), _rolling_mean(rv, _TD_YEAR).clip(lower=_EPS))
    return _safe_div(cv63, cv252)


def vov_028_cv_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d CV of 21d rvol within trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    cv = _safe_div(_rolling_std(rv, _TD_QTR), _rolling_mean(rv, _TD_QTR).clip(lower=_EPS))
    return cv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vov_029_cv_rvol5_21d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of 5d rvol over 21d window."""
    rv = _realized_vol(close, _TD_WEEK)
    return _safe_div(_rolling_std(rv, _TD_MON), _rolling_mean(rv, _TD_MON).clip(lower=_EPS))


def vov_030_cv_atr5_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Coefficient of variation of 5d ATR over 63d window."""
    a = _atr(close, high, low, _TD_WEEK)
    return _safe_div(_rolling_std(a, _TD_QTR), _rolling_mean(a, _TD_QTR).clip(lower=_EPS))


# --- Group C (031-045): Range of vol over windows (max - min of rvol) ---

def vov_031_range_rvol21_63d(close: pd.Series) -> pd.Series:
    """Range (max-min) of 21d rvol over trailing 63 days."""
    rv = _realized_vol(close, _TD_MON)
    return _rolling_max(rv, _TD_QTR) - _rolling_min(rv, _TD_QTR)


def vov_032_range_rvol21_126d(close: pd.Series) -> pd.Series:
    """Range (max-min) of 21d rvol over trailing 126 days."""
    rv = _realized_vol(close, _TD_MON)
    return _rolling_max(rv, _TD_HALF) - _rolling_min(rv, _TD_HALF)


def vov_033_range_rvol21_252d(close: pd.Series) -> pd.Series:
    """Range (max-min) of 21d rvol over trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    return _rolling_max(rv, _TD_YEAR) - _rolling_min(rv, _TD_YEAR)


def vov_034_range_rvol5_21d(close: pd.Series) -> pd.Series:
    """Range of 5d rvol over trailing 21 days."""
    rv = _realized_vol(close, _TD_WEEK)
    return _rolling_max(rv, _TD_MON) - _rolling_min(rv, _TD_MON)


def vov_035_range_rvol5_63d(close: pd.Series) -> pd.Series:
    """Range of 5d rvol over trailing 63 days."""
    rv = _realized_vol(close, _TD_WEEK)
    return _rolling_max(rv, _TD_QTR) - _rolling_min(rv, _TD_QTR)


def vov_036_range_rvol63_252d(close: pd.Series) -> pd.Series:
    """Range of 63d rvol over trailing 252 days."""
    rv = _realized_vol(close, _TD_QTR)
    return _rolling_max(rv, _TD_YEAR) - _rolling_min(rv, _TD_YEAR)


def vov_037_range_atr21_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Range of 21d ATR over trailing 63 days."""
    a = _atr(close, high, low, _TD_MON)
    return _rolling_max(a, _TD_QTR) - _rolling_min(a, _TD_QTR)


def vov_038_range_atr21_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Range of 21d ATR over trailing 252 days."""
    a = _atr(close, high, low, _TD_MON)
    return _rolling_max(a, _TD_YEAR) - _rolling_min(a, _TD_YEAR)


def vov_039_norm_range_rvol21_63d(close: pd.Series) -> pd.Series:
    """Normalized range of 21d rvol over 63d (range / mean of rvol)."""
    rv = _realized_vol(close, _TD_MON)
    rng = _rolling_max(rv, _TD_QTR) - _rolling_min(rv, _TD_QTR)
    avg = _rolling_mean(rv, _TD_QTR)
    return _safe_div(rng, avg.clip(lower=_EPS))


def vov_040_norm_range_rvol21_252d(close: pd.Series) -> pd.Series:
    """Normalized range of 21d rvol over 252d (range / mean of rvol)."""
    rv = _realized_vol(close, _TD_MON)
    rng = _rolling_max(rv, _TD_YEAR) - _rolling_min(rv, _TD_YEAR)
    avg = _rolling_mean(rv, _TD_YEAR)
    return _safe_div(rng, avg.clip(lower=_EPS))


def vov_041_range_rvol21_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d range of 21d rvol within trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    rng = _rolling_max(rv, _TD_QTR) - _rolling_min(rv, _TD_QTR)
    return rng.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vov_042_range_rvol5_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d range of 5d rvol within trailing 252 days."""
    rv = _realized_vol(close, _TD_WEEK)
    rng = _rolling_max(rv, _TD_QTR) - _rolling_min(rv, _TD_QTR)
    return rng.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vov_043_range_rvol21_21d(close: pd.Series) -> pd.Series:
    """Range of 21d rvol over trailing 21 days (very short instability)."""
    rv = _realized_vol(close, _TD_MON)
    return _rolling_max(rv, _TD_MON) - _rolling_min(rv, _TD_MON)


def vov_044_range_atr5_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Range of 5d ATR over trailing 63 days."""
    a = _atr(close, high, low, _TD_WEEK)
    return _rolling_max(a, _TD_QTR) - _rolling_min(a, _TD_QTR)


def vov_045_range_rvol10_63d(close: pd.Series) -> pd.Series:
    """Range of 10d rvol over trailing 63 days."""
    rv = _realized_vol(close, 10)
    return _rolling_max(rv, _TD_QTR) - _rolling_min(rv, _TD_QTR)


# --- Group D (046-060): Mean-absolute-change (MAD) of daily vol ---

def vov_046_mac_rvol21_21d(close: pd.Series) -> pd.Series:
    """Mean absolute daily change of 21d rvol over trailing 21 days."""
    rv = _realized_vol(close, _TD_MON)
    return rv.diff(1).abs().rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def vov_047_mac_rvol21_63d(close: pd.Series) -> pd.Series:
    """Mean absolute daily change of 21d rvol over trailing 63 days."""
    rv = _realized_vol(close, _TD_MON)
    return rv.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def vov_048_mac_rvol21_126d(close: pd.Series) -> pd.Series:
    """Mean absolute daily change of 21d rvol over trailing 126 days."""
    rv = _realized_vol(close, _TD_MON)
    return rv.diff(1).abs().rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).mean()


def vov_049_mac_rvol21_252d(close: pd.Series) -> pd.Series:
    """Mean absolute daily change of 21d rvol over trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    return rv.diff(1).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def vov_050_mac_rvol5_21d(close: pd.Series) -> pd.Series:
    """Mean absolute daily change of 5d rvol over trailing 21 days."""
    rv = _realized_vol(close, _TD_WEEK)
    return rv.diff(1).abs().rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def vov_051_mac_rvol5_63d(close: pd.Series) -> pd.Series:
    """Mean absolute daily change of 5d rvol over trailing 63 days."""
    rv = _realized_vol(close, _TD_WEEK)
    return rv.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def vov_052_mac_rvol63_252d(close: pd.Series) -> pd.Series:
    """Mean absolute daily change of 63d rvol over trailing 252 days."""
    rv = _realized_vol(close, _TD_QTR)
    return rv.diff(1).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def vov_053_mac_atr21_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean absolute daily change of 21d ATR over trailing 63 days."""
    a = _atr(close, high, low, _TD_MON)
    return a.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def vov_054_mac_atr21_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean absolute daily change of 21d ATR over trailing 252 days."""
    a = _atr(close, high, low, _TD_MON)
    return a.diff(1).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def vov_055_norm_mac_rvol21_63d(close: pd.Series) -> pd.Series:
    """Normalized MAC of 21d rvol over 63d (MAC / mean rvol)."""
    rv = _realized_vol(close, _TD_MON)
    mac = rv.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    avg = _rolling_mean(rv, _TD_QTR)
    return _safe_div(mac, avg.clip(lower=_EPS))


def vov_056_norm_mac_rvol21_252d(close: pd.Series) -> pd.Series:
    """Normalized MAC of 21d rvol over 252d (MAC / mean rvol)."""
    rv = _realized_vol(close, _TD_MON)
    mac = rv.diff(1).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()
    avg = _rolling_mean(rv, _TD_YEAR)
    return _safe_div(mac, avg.clip(lower=_EPS))


def vov_057_mac_rvol21_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d MAC of 21d rvol within trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    mac = rv.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return mac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vov_058_mac_rvol5_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d MAC of 5d rvol within trailing 252 days."""
    rv = _realized_vol(close, _TD_WEEK)
    mac = rv.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return mac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vov_059_mac_rvol21_expanding_rank(close: pd.Series) -> pd.Series:
    """Expanding all-history rank of 63d MAC of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    mac = rv.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return mac.expanding(min_periods=_TD_QTR).rank(pct=True)


def vov_060_mac_atr21_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 63d MAC of 21d ATR within trailing 252 days."""
    a = _atr(close, high, low, _TD_MON)
    mac = a.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return mac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group E (061-075): Vol z-score dispersion, jaggedness, instability of ATR ---

def vov_061_zscore_rvol21_63d(close: pd.Series) -> pd.Series:
    """Z-score of current 21d rvol within its trailing 63d distribution."""
    rv = _realized_vol(close, _TD_MON)
    m = _rolling_mean(rv, _TD_QTR)
    s = _rolling_std(rv, _TD_QTR)
    return _safe_div(rv - m, s.clip(lower=_EPS))


def vov_062_zscore_rvol21_252d(close: pd.Series) -> pd.Series:
    """Z-score of current 21d rvol within its trailing 252d distribution."""
    rv = _realized_vol(close, _TD_MON)
    m = _rolling_mean(rv, _TD_YEAR)
    s = _rolling_std(rv, _TD_YEAR)
    return _safe_div(rv - m, s.clip(lower=_EPS))


def vov_063_zscore_rvol5_63d(close: pd.Series) -> pd.Series:
    """Z-score of current 5d rvol within its trailing 63d distribution."""
    rv = _realized_vol(close, _TD_WEEK)
    m = _rolling_mean(rv, _TD_QTR)
    s = _rolling_std(rv, _TD_QTR)
    return _safe_div(rv - m, s.clip(lower=_EPS))


def vov_064_zscore_dispersion_rvol21_63d(close: pd.Series) -> pd.Series:
    """Std of daily z-scores of 21d rvol over trailing 63 days (2nd order dispersion)."""
    rv = _realized_vol(close, _TD_MON)
    m = _rolling_mean(rv, _TD_YEAR)
    s = _rolling_std(rv, _TD_YEAR)
    z = _safe_div(rv - m, s.clip(lower=_EPS))
    return _rolling_std(z, _TD_QTR)


def vov_065_vol_jaggedness_21d(close: pd.Series) -> pd.Series:
    """Path jaggedness of 21d rvol: sum of absolute daily changes / total variation."""
    rv = _realized_vol(close, _TD_MON)
    abs_changes = rv.diff(1).abs()
    total_abs = _rolling_sum(abs_changes, _TD_MON)
    total_var = (_rolling_max(rv, _TD_MON) - _rolling_min(rv, _TD_MON)).clip(lower=_EPS)
    return _safe_div(total_abs, total_var)


def vov_066_vol_jaggedness_63d(close: pd.Series) -> pd.Series:
    """Path jaggedness of 21d rvol over 63-day window."""
    rv = _realized_vol(close, _TD_MON)
    abs_changes = rv.diff(1).abs()
    total_abs = _rolling_sum(abs_changes, _TD_QTR)
    total_var = (_rolling_max(rv, _TD_QTR) - _rolling_min(rv, _TD_QTR)).clip(lower=_EPS)
    return _safe_div(total_abs, total_var)


def vov_067_vol_jaggedness_252d(close: pd.Series) -> pd.Series:
    """Path jaggedness of 21d rvol over 252-day window."""
    rv = _realized_vol(close, _TD_MON)
    abs_changes = rv.diff(1).abs()
    total_abs = _rolling_sum(abs_changes, _TD_YEAR)
    total_var = (_rolling_max(rv, _TD_YEAR) - _rolling_min(rv, _TD_YEAR)).clip(lower=_EPS)
    return _safe_div(total_abs, total_var)


def vov_068_atr_std_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Std of daily 21d ATR over trailing 63 days (ATR instability)."""
    a = _atr(close, high, low, _TD_MON)
    return _rolling_std(a, _TD_QTR)


def vov_069_atr_std_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Std of daily 21d ATR over trailing 252 days (long-run ATR instability)."""
    a = _atr(close, high, low, _TD_MON)
    return _rolling_std(a, _TD_YEAR)


def vov_070_atr_std_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 63d ATR std within trailing 252 days."""
    a = _atr(close, high, low, _TD_MON)
    s = _rolling_std(a, _TD_QTR)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vov_071_vol_reversal_freq_63d(close: pd.Series) -> pd.Series:
    """Frequency of vol direction reversals (up-then-down or down-then-up) over 63 days."""
    rv = _realized_vol(close, _TD_MON)
    d = rv.diff(1)
    reversal = ((d > 0) & (d.shift(1) < 0)) | ((d < 0) & (d.shift(1) > 0))
    return reversal.astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()


def vov_072_vol_reversal_freq_252d(close: pd.Series) -> pd.Series:
    """Frequency of vol direction reversals over trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    d = rv.diff(1)
    reversal = ((d > 0) & (d.shift(1) < 0)) | ((d < 0) & (d.shift(1) > 0))
    return reversal.astype(float).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum()


def vov_073_vol_above_ewm_freq_63d(close: pd.Series) -> pd.Series:
    """Fraction of days where 21d rvol > its 63d EWM (elevated instability)."""
    rv = _realized_vol(close, _TD_MON)
    ewm = _ewm_mean(rv, _TD_QTR)
    above = (rv > ewm).astype(float)
    return _rolling_mean(above, _TD_QTR)


def vov_074_iqr_rvol21_63d(close: pd.Series) -> pd.Series:
    """Interquartile range (75th-25th pct) of 21d rvol over trailing 63 days."""
    rv = _realized_vol(close, _TD_MON)
    q75 = rv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = rv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    return q75 - q25


def vov_075_iqr_rvol21_252d(close: pd.Series) -> pd.Series:
    """Interquartile range of 21d rvol over trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    q75 = rv.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.75)
    q25 = rv.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.25)
    return q75 - q25


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_OF_VOLATILITY_REGISTRY_001_075 = {
    "vov_001_std_of_rvol21_over_63d": {"inputs": ["close"], "func": vov_001_std_of_rvol21_over_63d},
    "vov_002_std_of_rvol21_over_126d": {"inputs": ["close"], "func": vov_002_std_of_rvol21_over_126d},
    "vov_003_std_of_rvol21_over_252d": {"inputs": ["close"], "func": vov_003_std_of_rvol21_over_252d},
    "vov_004_std_of_rvol5_over_21d": {"inputs": ["close"], "func": vov_004_std_of_rvol5_over_21d},
    "vov_005_std_of_rvol5_over_63d": {"inputs": ["close"], "func": vov_005_std_of_rvol5_over_63d},
    "vov_006_std_of_rvol63_over_252d": {"inputs": ["close"], "func": vov_006_std_of_rvol63_over_252d},
    "vov_007_std_of_rvol10_over_63d": {"inputs": ["close"], "func": vov_007_std_of_rvol10_over_63d},
    "vov_008_std_of_rvol10_over_126d": {"inputs": ["close"], "func": vov_008_std_of_rvol10_over_126d},
    "vov_009_std_of_rvol21_over_21d": {"inputs": ["close"], "func": vov_009_std_of_rvol21_over_21d},
    "vov_010_std_of_rvol63_over_126d": {"inputs": ["close"], "func": vov_010_std_of_rvol63_over_126d},
    "vov_011_vov_ratio_63d_vs_252d": {"inputs": ["close"], "func": vov_011_vov_ratio_63d_vs_252d},
    "vov_012_vov_ratio_21d_vs_63d": {"inputs": ["close"], "func": vov_012_vov_ratio_21d_vs_63d},
    "vov_013_std_of_rvol21_norm_by_mean": {"inputs": ["close"], "func": vov_013_std_of_rvol21_norm_by_mean},
    "vov_014_vov_pct_rank_252d": {"inputs": ["close"], "func": vov_014_vov_pct_rank_252d},
    "vov_015_expanding_vov_pct_rank": {"inputs": ["close"], "func": vov_015_expanding_vov_pct_rank},
    "vov_016_cv_rvol21_63d": {"inputs": ["close"], "func": vov_016_cv_rvol21_63d},
    "vov_017_cv_rvol21_126d": {"inputs": ["close"], "func": vov_017_cv_rvol21_126d},
    "vov_018_cv_rvol21_252d": {"inputs": ["close"], "func": vov_018_cv_rvol21_252d},
    "vov_019_cv_rvol5_63d": {"inputs": ["close"], "func": vov_019_cv_rvol5_63d},
    "vov_020_cv_rvol5_252d": {"inputs": ["close"], "func": vov_020_cv_rvol5_252d},
    "vov_021_cv_rvol63_252d": {"inputs": ["close"], "func": vov_021_cv_rvol63_252d},
    "vov_022_cv_atr21_63d": {"inputs": ["close", "high", "low"], "func": vov_022_cv_atr21_63d},
    "vov_023_cv_atr21_252d": {"inputs": ["close", "high", "low"], "func": vov_023_cv_atr21_252d},
    "vov_024_cv_rvol10_63d": {"inputs": ["close"], "func": vov_024_cv_rvol10_63d},
    "vov_025_cv_rvol10_126d": {"inputs": ["close"], "func": vov_025_cv_rvol10_126d},
    "vov_026_cv_rvol21_21d": {"inputs": ["close"], "func": vov_026_cv_rvol21_21d},
    "vov_027_cv_ratio_63d_vs_252d": {"inputs": ["close"], "func": vov_027_cv_ratio_63d_vs_252d},
    "vov_028_cv_pct_rank_252d": {"inputs": ["close"], "func": vov_028_cv_pct_rank_252d},
    "vov_029_cv_rvol5_21d": {"inputs": ["close"], "func": vov_029_cv_rvol5_21d},
    "vov_030_cv_atr5_63d": {"inputs": ["close", "high", "low"], "func": vov_030_cv_atr5_63d},
    "vov_031_range_rvol21_63d": {"inputs": ["close"], "func": vov_031_range_rvol21_63d},
    "vov_032_range_rvol21_126d": {"inputs": ["close"], "func": vov_032_range_rvol21_126d},
    "vov_033_range_rvol21_252d": {"inputs": ["close"], "func": vov_033_range_rvol21_252d},
    "vov_034_range_rvol5_21d": {"inputs": ["close"], "func": vov_034_range_rvol5_21d},
    "vov_035_range_rvol5_63d": {"inputs": ["close"], "func": vov_035_range_rvol5_63d},
    "vov_036_range_rvol63_252d": {"inputs": ["close"], "func": vov_036_range_rvol63_252d},
    "vov_037_range_atr21_63d": {"inputs": ["close", "high", "low"], "func": vov_037_range_atr21_63d},
    "vov_038_range_atr21_252d": {"inputs": ["close", "high", "low"], "func": vov_038_range_atr21_252d},
    "vov_039_norm_range_rvol21_63d": {"inputs": ["close"], "func": vov_039_norm_range_rvol21_63d},
    "vov_040_norm_range_rvol21_252d": {"inputs": ["close"], "func": vov_040_norm_range_rvol21_252d},
    "vov_041_range_rvol21_63d_pct_rank_252d": {"inputs": ["close"], "func": vov_041_range_rvol21_63d_pct_rank_252d},
    "vov_042_range_rvol5_63d_pct_rank_252d": {"inputs": ["close"], "func": vov_042_range_rvol5_63d_pct_rank_252d},
    "vov_043_range_rvol21_21d": {"inputs": ["close"], "func": vov_043_range_rvol21_21d},
    "vov_044_range_atr5_63d": {"inputs": ["close", "high", "low"], "func": vov_044_range_atr5_63d},
    "vov_045_range_rvol10_63d": {"inputs": ["close"], "func": vov_045_range_rvol10_63d},
    "vov_046_mac_rvol21_21d": {"inputs": ["close"], "func": vov_046_mac_rvol21_21d},
    "vov_047_mac_rvol21_63d": {"inputs": ["close"], "func": vov_047_mac_rvol21_63d},
    "vov_048_mac_rvol21_126d": {"inputs": ["close"], "func": vov_048_mac_rvol21_126d},
    "vov_049_mac_rvol21_252d": {"inputs": ["close"], "func": vov_049_mac_rvol21_252d},
    "vov_050_mac_rvol5_21d": {"inputs": ["close"], "func": vov_050_mac_rvol5_21d},
    "vov_051_mac_rvol5_63d": {"inputs": ["close"], "func": vov_051_mac_rvol5_63d},
    "vov_052_mac_rvol63_252d": {"inputs": ["close"], "func": vov_052_mac_rvol63_252d},
    "vov_053_mac_atr21_63d": {"inputs": ["close", "high", "low"], "func": vov_053_mac_atr21_63d},
    "vov_054_mac_atr21_252d": {"inputs": ["close", "high", "low"], "func": vov_054_mac_atr21_252d},
    "vov_055_norm_mac_rvol21_63d": {"inputs": ["close"], "func": vov_055_norm_mac_rvol21_63d},
    "vov_056_norm_mac_rvol21_252d": {"inputs": ["close"], "func": vov_056_norm_mac_rvol21_252d},
    "vov_057_mac_rvol21_pct_rank_252d": {"inputs": ["close"], "func": vov_057_mac_rvol21_pct_rank_252d},
    "vov_058_mac_rvol5_pct_rank_252d": {"inputs": ["close"], "func": vov_058_mac_rvol5_pct_rank_252d},
    "vov_059_mac_rvol21_expanding_rank": {"inputs": ["close"], "func": vov_059_mac_rvol21_expanding_rank},
    "vov_060_mac_atr21_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": vov_060_mac_atr21_pct_rank_252d},
    "vov_061_zscore_rvol21_63d": {"inputs": ["close"], "func": vov_061_zscore_rvol21_63d},
    "vov_062_zscore_rvol21_252d": {"inputs": ["close"], "func": vov_062_zscore_rvol21_252d},
    "vov_063_zscore_rvol5_63d": {"inputs": ["close"], "func": vov_063_zscore_rvol5_63d},
    "vov_064_zscore_dispersion_rvol21_63d": {"inputs": ["close"], "func": vov_064_zscore_dispersion_rvol21_63d},
    "vov_065_vol_jaggedness_21d": {"inputs": ["close"], "func": vov_065_vol_jaggedness_21d},
    "vov_066_vol_jaggedness_63d": {"inputs": ["close"], "func": vov_066_vol_jaggedness_63d},
    "vov_067_vol_jaggedness_252d": {"inputs": ["close"], "func": vov_067_vol_jaggedness_252d},
    "vov_068_atr_std_63d": {"inputs": ["close", "high", "low"], "func": vov_068_atr_std_63d},
    "vov_069_atr_std_252d": {"inputs": ["close", "high", "low"], "func": vov_069_atr_std_252d},
    "vov_070_atr_std_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": vov_070_atr_std_pct_rank_252d},
    "vov_071_vol_reversal_freq_63d": {"inputs": ["close"], "func": vov_071_vol_reversal_freq_63d},
    "vov_072_vol_reversal_freq_252d": {"inputs": ["close"], "func": vov_072_vol_reversal_freq_252d},
    "vov_073_vol_above_ewm_freq_63d": {"inputs": ["close"], "func": vov_073_vol_above_ewm_freq_63d},
    "vov_074_iqr_rvol21_63d": {"inputs": ["close"], "func": vov_074_iqr_rvol21_63d},
    "vov_075_iqr_rvol21_252d": {"inputs": ["close"], "func": vov_075_iqr_rvol21_252d},
}
