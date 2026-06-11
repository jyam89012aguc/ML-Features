"""
07_peak_to_trough — Base Features 001-075
Domain: peak-to-trough ratios, trough/peak paired relationships, recovery-fraction
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _peak_trough_span(s: pd.Series, w: int):
    """Returns (peak, trough) rolling within window w."""
    peak = _rolling_max(s, w)
    trough = _rolling_min(s, w)
    return peak, trough


def _recovery_fraction(close: pd.Series, peak: pd.Series, trough: pd.Series) -> pd.Series:
    """(close - trough) / (peak - trough), clamped 0..1 guard on zero span."""
    span = peak - trough
    return _safe_div(close - trough, span)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Core peak-to-trough ratio, multiple horizons ---

def ptt_001_peak_trough_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day rolling max to 21-day rolling min (magnitude of swing)."""
    pk, tr = _peak_trough_span(close, _TD_MON)
    return _safe_div(pk, tr)


def ptt_002_peak_trough_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day rolling max to 63-day rolling min."""
    pk, tr = _peak_trough_span(close, _TD_QTR)
    return _safe_div(pk, tr)


def ptt_003_peak_trough_ratio_126d(close: pd.Series) -> pd.Series:
    """Ratio of 126-day rolling max to 126-day rolling min."""
    pk, tr = _peak_trough_span(close, _TD_HALF)
    return _safe_div(pk, tr)


def ptt_004_peak_trough_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of 252-day rolling max to 252-day rolling min."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    return _safe_div(pk, tr)


def ptt_005_peak_trough_ratio_504d(close: pd.Series) -> pd.Series:
    """Ratio of 504-day rolling max to 504-day rolling min (2-year swing)."""
    pk, tr = _peak_trough_span(close, 504)
    return _safe_div(pk, tr)


def ptt_006_peak_trough_ratio_756d(close: pd.Series) -> pd.Series:
    """Ratio of 756-day rolling max to 756-day rolling min (3-year swing)."""
    pk, tr = _peak_trough_span(close, 756)
    return _safe_div(pk, tr)


def ptt_007_peak_trough_ratio_1260d(close: pd.Series) -> pd.Series:
    """Ratio of 1260-day rolling max to 1260-day rolling min (5-year swing)."""
    pk, tr = _peak_trough_span(close, 1260)
    return _safe_div(pk, tr)


def ptt_008_peak_trough_ratio_expanding(close: pd.Series) -> pd.Series:
    """Ratio of all-time high to all-time low (expanding window)."""
    pk = close.expanding(min_periods=1).max()
    tr = close.expanding(min_periods=1).min()
    return _safe_div(pk, tr)


def ptt_009_log_peak_trough_span_252d(close: pd.Series) -> pd.Series:
    """Log(peak/trough) for 252-day window — log-scale amplitude."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    return _log_safe(pk) - _log_safe(tr)


def ptt_010_log_peak_trough_span_504d(close: pd.Series) -> pd.Series:
    """Log(peak/trough) for 504-day window."""
    pk, tr = _peak_trough_span(close, 504)
    return _log_safe(pk) - _log_safe(tr)


def ptt_011_log_peak_trough_span_1260d(close: pd.Series) -> pd.Series:
    """Log(peak/trough) for 1260-day window."""
    pk, tr = _peak_trough_span(close, 1260)
    return _log_safe(pk) - _log_safe(tr)


def ptt_012_log_peak_trough_span_expanding(close: pd.Series) -> pd.Series:
    """Log(ATH/ATL) — all-time log amplitude."""
    pk = close.expanding(min_periods=1).max()
    tr = close.expanding(min_periods=1).min()
    return _log_safe(pk) - _log_safe(tr)


# --- Group B (013-024): Recovery fraction (backward-looking retracement) ---

def ptt_013_recovery_fraction_21d(close: pd.Series) -> pd.Series:
    """Fraction of 21-day peak-to-trough fall recovered as of today (0=at trough, 1=at peak)."""
    pk, tr = _peak_trough_span(close, _TD_MON)
    return _recovery_fraction(close, pk, tr)


def ptt_014_recovery_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of 63-day peak-to-trough fall recovered as of today."""
    pk, tr = _peak_trough_span(close, _TD_QTR)
    return _recovery_fraction(close, pk, tr)


def ptt_015_recovery_fraction_126d(close: pd.Series) -> pd.Series:
    """Fraction of 126-day peak-to-trough fall recovered."""
    pk, tr = _peak_trough_span(close, _TD_HALF)
    return _recovery_fraction(close, pk, tr)


def ptt_016_recovery_fraction_252d(close: pd.Series) -> pd.Series:
    """Fraction of 252-day peak-to-trough fall recovered."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    return _recovery_fraction(close, pk, tr)


def ptt_017_recovery_fraction_504d(close: pd.Series) -> pd.Series:
    """Fraction of 504-day peak-to-trough fall recovered."""
    pk, tr = _peak_trough_span(close, 504)
    return _recovery_fraction(close, pk, tr)


def ptt_018_recovery_fraction_756d(close: pd.Series) -> pd.Series:
    """Fraction of 756-day peak-to-trough fall recovered."""
    pk, tr = _peak_trough_span(close, 756)
    return _recovery_fraction(close, pk, tr)


def ptt_019_recovery_fraction_1260d(close: pd.Series) -> pd.Series:
    """Fraction of 1260-day peak-to-trough fall recovered."""
    pk, tr = _peak_trough_span(close, 1260)
    return _recovery_fraction(close, pk, tr)


def ptt_020_recovery_fraction_expanding(close: pd.Series) -> pd.Series:
    """Recovery fraction vs all-time high and all-time low (expanding)."""
    pk = close.expanding(min_periods=1).max()
    tr = close.expanding(min_periods=1).min()
    return _recovery_fraction(close, pk, tr)


def ptt_021_recovery_fraction_intraday_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Recovery fraction using intraday high/low as 252-day peak/trough."""
    pk = _rolling_max(high, _TD_YEAR)
    tr = _rolling_min(low, _TD_YEAR)
    return _recovery_fraction(close, pk, tr)


def ptt_022_recovery_fraction_intraday_504d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Recovery fraction using intraday high/low as 504-day peak/trough."""
    pk = _rolling_max(high, 504)
    tr = _rolling_min(low, 504)
    return _recovery_fraction(close, pk, tr)


def ptt_023_recovery_fraction_intraday_expanding(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Recovery fraction using all-time intraday high/low."""
    pk = high.expanding(min_periods=1).max()
    tr = low.expanding(min_periods=1).min()
    return _recovery_fraction(close, pk, tr)


def ptt_024_log_recovery_fraction_252d(close: pd.Series) -> pd.Series:
    """Log-space recovery fraction: log(close/trough) / log(peak/trough) for 252d."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    num = _log_safe(close) - _log_safe(tr)
    den = _log_safe(pk) - _log_safe(tr)
    return _safe_div(num, den)


# --- Group C (025-036): Current price vs peak and vs trough ---

def ptt_025_close_to_peak_ratio_21d(close: pd.Series) -> pd.Series:
    """close / 21-day rolling max (proximity to short-term peak)."""
    pk = _rolling_max(close, _TD_MON)
    return _safe_div(close, pk)


def ptt_026_close_to_peak_ratio_63d(close: pd.Series) -> pd.Series:
    """close / 63-day rolling max."""
    pk = _rolling_max(close, _TD_QTR)
    return _safe_div(close, pk)


def ptt_027_close_to_peak_ratio_252d(close: pd.Series) -> pd.Series:
    """close / 252-day rolling max."""
    pk = _rolling_max(close, _TD_YEAR)
    return _safe_div(close, pk)


def ptt_028_close_to_peak_ratio_504d(close: pd.Series) -> pd.Series:
    """close / 504-day rolling max."""
    pk = _rolling_max(close, 504)
    return _safe_div(close, pk)


def ptt_029_close_to_peak_ratio_expanding(close: pd.Series) -> pd.Series:
    """close / all-time high (expanding max)."""
    pk = close.expanding(min_periods=1).max()
    return _safe_div(close, pk)


def ptt_030_close_to_trough_ratio_21d(close: pd.Series) -> pd.Series:
    """close / 21-day rolling min (bounce off short-term trough)."""
    tr = _rolling_min(close, _TD_MON)
    return _safe_div(close, tr)


def ptt_031_close_to_trough_ratio_63d(close: pd.Series) -> pd.Series:
    """close / 63-day rolling min."""
    tr = _rolling_min(close, _TD_QTR)
    return _safe_div(close, tr)


def ptt_032_close_to_trough_ratio_252d(close: pd.Series) -> pd.Series:
    """close / 252-day rolling min."""
    tr = _rolling_min(close, _TD_YEAR)
    return _safe_div(close, tr)


def ptt_033_close_to_trough_ratio_504d(close: pd.Series) -> pd.Series:
    """close / 504-day rolling min."""
    tr = _rolling_min(close, 504)
    return _safe_div(close, tr)


def ptt_034_close_to_trough_ratio_expanding(close: pd.Series) -> pd.Series:
    """close / all-time low (expanding min)."""
    tr = close.expanding(min_periods=1).min()
    return _safe_div(close, tr)


def ptt_035_trough_to_peak_ratio_vs_prior_252d(close: pd.Series) -> pd.Series:
    """Ratio of current 252d trough to prior-period 252d peak (lagged 63d)."""
    pk_lag = _rolling_max(close, _TD_YEAR).shift(_TD_QTR)
    tr = _rolling_min(close, _TD_YEAR)
    return _safe_div(tr, pk_lag)


def ptt_036_close_above_midpoint_252d(close: pd.Series) -> pd.Series:
    """Binary: 1 if close is above midpoint of 252-day peak-trough range, else 0."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    mid = (pk + tr) / 2.0
    return (close >= mid).astype(float)


# --- Group D (037-048): Peak-trough span (absolute and normalized) ---

def ptt_037_span_abs_21d(close: pd.Series) -> pd.Series:
    """Absolute peak-trough span of 21-day window (price units)."""
    pk, tr = _peak_trough_span(close, _TD_MON)
    return pk - tr


def ptt_038_span_abs_63d(close: pd.Series) -> pd.Series:
    """Absolute peak-trough span of 63-day window."""
    pk, tr = _peak_trough_span(close, _TD_QTR)
    return pk - tr


def ptt_039_span_abs_252d(close: pd.Series) -> pd.Series:
    """Absolute peak-trough span of 252-day window."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    return pk - tr


def ptt_040_span_pct_21d(close: pd.Series) -> pd.Series:
    """Percent span: (peak - trough) / trough for 21-day window."""
    pk, tr = _peak_trough_span(close, _TD_MON)
    return _safe_div(pk - tr, tr)


def ptt_041_span_pct_63d(close: pd.Series) -> pd.Series:
    """Percent span: (peak - trough) / trough for 63-day window."""
    pk, tr = _peak_trough_span(close, _TD_QTR)
    return _safe_div(pk - tr, tr)


def ptt_042_span_pct_252d(close: pd.Series) -> pd.Series:
    """Percent span: (peak - trough) / trough for 252-day window."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    return _safe_div(pk - tr, tr)


def ptt_043_span_pct_504d(close: pd.Series) -> pd.Series:
    """Percent span: (peak - trough) / trough for 504-day window."""
    pk, tr = _peak_trough_span(close, 504)
    return _safe_div(pk - tr, tr)


def ptt_044_span_pct_1260d(close: pd.Series) -> pd.Series:
    """Percent span: (peak - trough) / trough for 1260-day window."""
    pk, tr = _peak_trough_span(close, 1260)
    return _safe_div(pk - tr, tr)


def ptt_045_span_pct_expanding(close: pd.Series) -> pd.Series:
    """Percent span: (ATH - ATL) / ATL — all-time percent range."""
    pk = close.expanding(min_periods=1).max()
    tr = close.expanding(min_periods=1).min()
    return _safe_div(pk - tr, tr)


def ptt_046_span_normalized_by_close_252d(close: pd.Series) -> pd.Series:
    """252-day peak-trough span normalized by current close."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    return _safe_div(pk - tr, close)


def ptt_047_span_normalized_by_mean_252d(close: pd.Series) -> pd.Series:
    """252-day peak-trough span normalized by 252-day mean close."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    mu = _rolling_mean(close, _TD_YEAR)
    return _safe_div(pk - tr, mu)


def ptt_048_intraday_peak_trough_ratio_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 252-day intraday high to 252-day intraday low."""
    pk = _rolling_max(high, _TD_YEAR)
    tr = _rolling_min(low, _TD_YEAR)
    return _safe_div(pk, tr)


# --- Group E (049-060): Trough age, peak age, and relative timing ---

def ptt_049_days_since_252d_trough(close: pd.Series) -> pd.Series:
    """Number of trading days since close was at its 252-day rolling min."""
    tr = _rolling_min(close, _TD_YEAR)
    at_trough = (close == tr).astype(float)
    idx = pd.Series(np.arange(len(close)), index=close.index, dtype=float)
    last_trough_idx = idx.where(at_trough.astype(bool)).ffill()
    return idx - last_trough_idx


def ptt_050_days_since_252d_peak(close: pd.Series) -> pd.Series:
    """Number of trading days since close was at its 252-day rolling max."""
    pk = _rolling_max(close, _TD_YEAR)
    at_peak = (close == pk).astype(float)
    idx = pd.Series(np.arange(len(close)), index=close.index, dtype=float)
    last_peak_idx = idx.where(at_peak.astype(bool)).ffill()
    return idx - last_peak_idx


def ptt_051_trough_age_vs_peak_age_252d(close: pd.Series) -> pd.Series:
    """Ratio of days-since-trough to days-since-peak (252-day window)."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    at_peak = (close == pk).astype(float)
    at_trough = (close == tr).astype(float)
    idx = pd.Series(np.arange(len(close)), index=close.index, dtype=float)
    last_pk = idx.where(at_peak.astype(bool)).ffill()
    last_tr = idx.where(at_trough.astype(bool)).ffill()
    age_tr = idx - last_tr
    age_pk = idx - last_pk
    return _safe_div(age_tr, age_pk + 1.0)


def ptt_052_days_since_504d_trough(close: pd.Series) -> pd.Series:
    """Days since 504-day rolling trough."""
    tr = _rolling_min(close, 504)
    at_trough = (close == tr).astype(float)
    idx = pd.Series(np.arange(len(close)), index=close.index, dtype=float)
    last_trough_idx = idx.where(at_trough.astype(bool)).ffill()
    return idx - last_trough_idx


def ptt_053_days_since_expanding_trough(close: pd.Series) -> pd.Series:
    """Days since all-time expanding min (age of all-time low)."""
    tr = close.expanding(min_periods=1).min()
    at_trough = (close == tr).astype(float)
    idx = pd.Series(np.arange(len(close)), index=close.index, dtype=float)
    last_trough_idx = idx.where(at_trough.astype(bool)).ffill()
    return idx - last_trough_idx


def ptt_054_days_since_expanding_peak(close: pd.Series) -> pd.Series:
    """Days since all-time expanding max (age of all-time high)."""
    pk = close.expanding(min_periods=1).max()
    at_peak = (close == pk).astype(float)
    idx = pd.Series(np.arange(len(close)), index=close.index, dtype=float)
    last_peak_idx = idx.where(at_peak.astype(bool)).ffill()
    return idx - last_peak_idx


def ptt_055_trough_freshness_fraction_252d(close: pd.Series) -> pd.Series:
    """Days-since-252d-trough as fraction of 252 (0=very recent trough)."""
    tr = _rolling_min(close, _TD_YEAR)
    at_trough = (close == tr).astype(float)
    idx = pd.Series(np.arange(len(close)), index=close.index, dtype=float)
    last_trough_idx = idx.where(at_trough.astype(bool)).ffill()
    age = idx - last_trough_idx
    return age / float(_TD_YEAR)


def ptt_056_peak_freshness_fraction_252d(close: pd.Series) -> pd.Series:
    """Days-since-252d-peak as fraction of 252 (0=very recent peak)."""
    pk = _rolling_max(close, _TD_YEAR)
    at_peak = (close == pk).astype(float)
    idx = pd.Series(np.arange(len(close)), index=close.index, dtype=float)
    last_peak_idx = idx.where(at_peak.astype(bool)).ffill()
    age = idx - last_peak_idx
    return age / float(_TD_YEAR)


def ptt_057_trough_age_normalized_by_span_252d(close: pd.Series) -> pd.Series:
    """Days since 252d trough relative to days since 252d peak — direction index."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    at_peak = (close == pk).astype(float)
    at_trough = (close == tr).astype(float)
    idx = pd.Series(np.arange(len(close)), index=close.index, dtype=float)
    last_pk = idx.where(at_peak.astype(bool)).ffill()
    last_tr = idx.where(at_trough.astype(bool)).ffill()
    age_tr = (idx - last_tr).clip(lower=0)
    age_pk = (idx - last_pk).clip(lower=0)
    total = age_tr + age_pk
    return _safe_div(age_tr, total)


def ptt_058_trough_occurs_after_peak_252d(close: pd.Series) -> pd.Series:
    """Binary: 1 if the 252d trough date occurred AFTER the 252d peak date."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    at_peak = (close == pk).astype(float)
    at_trough = (close == tr).astype(float)
    idx = pd.Series(np.arange(len(close)), index=close.index, dtype=float)
    last_pk = idx.where(at_peak.astype(bool)).ffill()
    last_tr = idx.where(at_trough.astype(bool)).ffill()
    return (last_tr > last_pk).astype(float)


def ptt_059_peak_trough_timing_gap_252d(close: pd.Series) -> pd.Series:
    """Signed days between last 252d peak and last 252d trough (positive = trough after peak)."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    at_peak = (close == pk).astype(float)
    at_trough = (close == tr).astype(float)
    idx = pd.Series(np.arange(len(close)), index=close.index, dtype=float)
    last_pk = idx.where(at_peak.astype(bool)).ffill()
    last_tr = idx.where(at_trough.astype(bool)).ffill()
    return last_tr - last_pk


def ptt_060_peak_trough_timing_gap_504d(close: pd.Series) -> pd.Series:
    """Signed days between last 504d peak and last 504d trough."""
    pk = _rolling_max(close, 504)
    tr = _rolling_min(close, 504)
    at_peak = (close == pk).astype(float)
    at_trough = (close == tr).astype(float)
    idx = pd.Series(np.arange(len(close)), index=close.index, dtype=float)
    last_pk = idx.where(at_peak.astype(bool)).ffill()
    last_tr = idx.where(at_trough.astype(bool)).ffill()
    return last_tr - last_pk


# --- Group F (061-075): Multi-scale ratios, composite, and vol-adjusted ---

def ptt_061_ptt_ratio_63d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63d peak-trough ratio to 252d peak-trough ratio."""
    r63 = _safe_div(_rolling_max(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    r252 = _safe_div(_rolling_max(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    return _safe_div(r63, r252)


def ptt_062_ptt_ratio_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21d peak-trough ratio to 63d peak-trough ratio."""
    r21 = _safe_div(_rolling_max(close, _TD_MON), _rolling_min(close, _TD_MON))
    r63 = _safe_div(_rolling_max(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    return _safe_div(r21, r63)


def ptt_063_ptt_ratio_252d_vs_expanding(close: pd.Series) -> pd.Series:
    """252d peak-trough ratio relative to all-time peak-trough ratio."""
    r252 = _safe_div(_rolling_max(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    rexp = _safe_div(close.expanding(min_periods=1).max(), close.expanding(min_periods=1).min())
    return _safe_div(r252, rexp)


def ptt_064_recovery_fraction_diff_252d_vs_63d(close: pd.Series) -> pd.Series:
    """Difference in recovery fraction: 252d minus 63d (multi-horizon retracement gap)."""
    rf252 = ptt_016_recovery_fraction_252d(close)
    rf63 = ptt_014_recovery_fraction_63d(close)
    return rf252 - rf63


def ptt_065_recovery_fraction_diff_504d_vs_252d(close: pd.Series) -> pd.Series:
    """Difference in recovery fraction: 504d minus 252d."""
    pk504, tr504 = _peak_trough_span(close, 504)
    rf504 = _recovery_fraction(close, pk504, tr504)
    rf252 = ptt_016_recovery_fraction_252d(close)
    return rf504 - rf252


def ptt_066_vol_adj_span_252d(close: pd.Series) -> pd.Series:
    """252d peak-trough percent span divided by 252d realized volatility."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    span_pct = _safe_div(pk - tr, tr)
    vol = _rolling_std(_daily_ret(close), _TD_YEAR)
    return _safe_div(span_pct, vol)


def ptt_067_vol_adj_span_63d(close: pd.Series) -> pd.Series:
    """63d peak-trough percent span divided by 63d realized volatility."""
    pk, tr = _peak_trough_span(close, _TD_QTR)
    span_pct = _safe_div(pk - tr, tr)
    vol = _rolling_std(_daily_ret(close), _TD_QTR)
    return _safe_div(span_pct, vol)


def ptt_068_recovery_fraction_zscore_252d(close: pd.Series) -> pd.Series:
    """Rolling z-score of 252d recovery fraction over 252-day window."""
    rf = ptt_016_recovery_fraction_252d(close)
    return _zscore_rolling(rf, _TD_YEAR)


def ptt_069_recovery_fraction_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252d recovery fraction within trailing 252-day window."""
    rf = ptt_016_recovery_fraction_252d(close)
    return _rolling_rank_pct(rf, _TD_YEAR)


def ptt_070_volume_at_trough_fraction_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total 252d volume that occurred on days at or near 252d trough."""
    tr = _rolling_min(close, _TD_YEAR)
    trough_thresh = tr * 1.02
    near_trough = (close <= trough_thresh).astype(float)
    vol_at_trough = _rolling_sum(volume * near_trough, _TD_YEAR)
    vol_total = _rolling_sum(volume, _TD_YEAR)
    return _safe_div(vol_at_trough, vol_total)


def ptt_071_volume_at_peak_fraction_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total 252d volume that occurred on days at or near 252d peak."""
    pk = _rolling_max(close, _TD_YEAR)
    peak_thresh = pk * 0.98
    near_peak = (close >= peak_thresh).astype(float)
    vol_at_peak = _rolling_sum(volume * near_peak, _TD_YEAR)
    vol_total = _rolling_sum(volume, _TD_YEAR)
    return _safe_div(vol_at_peak, vol_total)


def ptt_072_composite_recovery_fraction(close: pd.Series) -> pd.Series:
    """Composite recovery fraction: 50% 21d + 30% 63d + 20% 252d."""
    rf21 = ptt_013_recovery_fraction_21d(close)
    rf63 = ptt_014_recovery_fraction_63d(close)
    rf252 = ptt_016_recovery_fraction_252d(close)
    return 0.5 * rf21 + 0.3 * rf63 + 0.2 * rf252


def ptt_073_composite_ptt_ratio(close: pd.Series) -> pd.Series:
    """Composite peak-trough ratio: 50% 21d + 30% 63d + 20% 252d."""
    r21 = ptt_001_peak_trough_ratio_21d(close)
    r63 = ptt_002_peak_trough_ratio_63d(close)
    r252 = ptt_004_peak_trough_ratio_252d(close)
    return 0.5 * r21 + 0.3 * r63 + 0.2 * r252


def ptt_074_intraday_vs_close_recovery_fraction_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Difference between intraday recovery fraction and close-based recovery fraction (252d)."""
    pk_id = _rolling_max(high, _TD_YEAR)
    tr_id = _rolling_min(low, _TD_YEAR)
    rf_id = _recovery_fraction(close, pk_id, tr_id)
    rf_cl = ptt_016_recovery_fraction_252d(close)
    return rf_id - rf_cl


def ptt_075_span_acceleration_63d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63d span-pct to 252d span-pct (recent volatility surge relative to annual)."""
    pk63, tr63 = _peak_trough_span(close, _TD_QTR)
    pk252, tr252 = _peak_trough_span(close, _TD_YEAR)
    span63 = _safe_div(pk63 - tr63, tr63)
    span252 = _safe_div(pk252 - tr252, tr252)
    return _safe_div(span63, span252)


# ── Registry ──────────────────────────────────────────────────────────────────

PEAK_TO_TROUGH_REGISTRY_001_075 = {
    "ptt_001_peak_trough_ratio_21d": {"inputs": ["close"], "func": ptt_001_peak_trough_ratio_21d},
    "ptt_002_peak_trough_ratio_63d": {"inputs": ["close"], "func": ptt_002_peak_trough_ratio_63d},
    "ptt_003_peak_trough_ratio_126d": {"inputs": ["close"], "func": ptt_003_peak_trough_ratio_126d},
    "ptt_004_peak_trough_ratio_252d": {"inputs": ["close"], "func": ptt_004_peak_trough_ratio_252d},
    "ptt_005_peak_trough_ratio_504d": {"inputs": ["close"], "func": ptt_005_peak_trough_ratio_504d},
    "ptt_006_peak_trough_ratio_756d": {"inputs": ["close"], "func": ptt_006_peak_trough_ratio_756d},
    "ptt_007_peak_trough_ratio_1260d": {"inputs": ["close"], "func": ptt_007_peak_trough_ratio_1260d},
    "ptt_008_peak_trough_ratio_expanding": {"inputs": ["close"], "func": ptt_008_peak_trough_ratio_expanding},
    "ptt_009_log_peak_trough_span_252d": {"inputs": ["close"], "func": ptt_009_log_peak_trough_span_252d},
    "ptt_010_log_peak_trough_span_504d": {"inputs": ["close"], "func": ptt_010_log_peak_trough_span_504d},
    "ptt_011_log_peak_trough_span_1260d": {"inputs": ["close"], "func": ptt_011_log_peak_trough_span_1260d},
    "ptt_012_log_peak_trough_span_expanding": {"inputs": ["close"], "func": ptt_012_log_peak_trough_span_expanding},
    "ptt_013_recovery_fraction_21d": {"inputs": ["close"], "func": ptt_013_recovery_fraction_21d},
    "ptt_014_recovery_fraction_63d": {"inputs": ["close"], "func": ptt_014_recovery_fraction_63d},
    "ptt_015_recovery_fraction_126d": {"inputs": ["close"], "func": ptt_015_recovery_fraction_126d},
    "ptt_016_recovery_fraction_252d": {"inputs": ["close"], "func": ptt_016_recovery_fraction_252d},
    "ptt_017_recovery_fraction_504d": {"inputs": ["close"], "func": ptt_017_recovery_fraction_504d},
    "ptt_018_recovery_fraction_756d": {"inputs": ["close"], "func": ptt_018_recovery_fraction_756d},
    "ptt_019_recovery_fraction_1260d": {"inputs": ["close"], "func": ptt_019_recovery_fraction_1260d},
    "ptt_020_recovery_fraction_expanding": {"inputs": ["close"], "func": ptt_020_recovery_fraction_expanding},
    "ptt_021_recovery_fraction_intraday_252d": {"inputs": ["close", "high", "low"], "func": ptt_021_recovery_fraction_intraday_252d},
    "ptt_022_recovery_fraction_intraday_504d": {"inputs": ["close", "high", "low"], "func": ptt_022_recovery_fraction_intraday_504d},
    "ptt_023_recovery_fraction_intraday_expanding": {"inputs": ["close", "high", "low"], "func": ptt_023_recovery_fraction_intraday_expanding},
    "ptt_024_log_recovery_fraction_252d": {"inputs": ["close"], "func": ptt_024_log_recovery_fraction_252d},
    "ptt_025_close_to_peak_ratio_21d": {"inputs": ["close"], "func": ptt_025_close_to_peak_ratio_21d},
    "ptt_026_close_to_peak_ratio_63d": {"inputs": ["close"], "func": ptt_026_close_to_peak_ratio_63d},
    "ptt_027_close_to_peak_ratio_252d": {"inputs": ["close"], "func": ptt_027_close_to_peak_ratio_252d},
    "ptt_028_close_to_peak_ratio_504d": {"inputs": ["close"], "func": ptt_028_close_to_peak_ratio_504d},
    "ptt_029_close_to_peak_ratio_expanding": {"inputs": ["close"], "func": ptt_029_close_to_peak_ratio_expanding},
    "ptt_030_close_to_trough_ratio_21d": {"inputs": ["close"], "func": ptt_030_close_to_trough_ratio_21d},
    "ptt_031_close_to_trough_ratio_63d": {"inputs": ["close"], "func": ptt_031_close_to_trough_ratio_63d},
    "ptt_032_close_to_trough_ratio_252d": {"inputs": ["close"], "func": ptt_032_close_to_trough_ratio_252d},
    "ptt_033_close_to_trough_ratio_504d": {"inputs": ["close"], "func": ptt_033_close_to_trough_ratio_504d},
    "ptt_034_close_to_trough_ratio_expanding": {"inputs": ["close"], "func": ptt_034_close_to_trough_ratio_expanding},
    "ptt_035_trough_to_peak_ratio_vs_prior_252d": {"inputs": ["close"], "func": ptt_035_trough_to_peak_ratio_vs_prior_252d},
    "ptt_036_close_above_midpoint_252d": {"inputs": ["close"], "func": ptt_036_close_above_midpoint_252d},
    "ptt_037_span_abs_21d": {"inputs": ["close"], "func": ptt_037_span_abs_21d},
    "ptt_038_span_abs_63d": {"inputs": ["close"], "func": ptt_038_span_abs_63d},
    "ptt_039_span_abs_252d": {"inputs": ["close"], "func": ptt_039_span_abs_252d},
    "ptt_040_span_pct_21d": {"inputs": ["close"], "func": ptt_040_span_pct_21d},
    "ptt_041_span_pct_63d": {"inputs": ["close"], "func": ptt_041_span_pct_63d},
    "ptt_042_span_pct_252d": {"inputs": ["close"], "func": ptt_042_span_pct_252d},
    "ptt_043_span_pct_504d": {"inputs": ["close"], "func": ptt_043_span_pct_504d},
    "ptt_044_span_pct_1260d": {"inputs": ["close"], "func": ptt_044_span_pct_1260d},
    "ptt_045_span_pct_expanding": {"inputs": ["close"], "func": ptt_045_span_pct_expanding},
    "ptt_046_span_normalized_by_close_252d": {"inputs": ["close"], "func": ptt_046_span_normalized_by_close_252d},
    "ptt_047_span_normalized_by_mean_252d": {"inputs": ["close"], "func": ptt_047_span_normalized_by_mean_252d},
    "ptt_048_intraday_peak_trough_ratio_252d": {"inputs": ["high", "low"], "func": ptt_048_intraday_peak_trough_ratio_252d},
    "ptt_049_days_since_252d_trough": {"inputs": ["close"], "func": ptt_049_days_since_252d_trough},
    "ptt_050_days_since_252d_peak": {"inputs": ["close"], "func": ptt_050_days_since_252d_peak},
    "ptt_051_trough_age_vs_peak_age_252d": {"inputs": ["close"], "func": ptt_051_trough_age_vs_peak_age_252d},
    "ptt_052_days_since_504d_trough": {"inputs": ["close"], "func": ptt_052_days_since_504d_trough},
    "ptt_053_days_since_expanding_trough": {"inputs": ["close"], "func": ptt_053_days_since_expanding_trough},
    "ptt_054_days_since_expanding_peak": {"inputs": ["close"], "func": ptt_054_days_since_expanding_peak},
    "ptt_055_trough_freshness_fraction_252d": {"inputs": ["close"], "func": ptt_055_trough_freshness_fraction_252d},
    "ptt_056_peak_freshness_fraction_252d": {"inputs": ["close"], "func": ptt_056_peak_freshness_fraction_252d},
    "ptt_057_trough_age_normalized_by_span_252d": {"inputs": ["close"], "func": ptt_057_trough_age_normalized_by_span_252d},
    "ptt_058_trough_occurs_after_peak_252d": {"inputs": ["close"], "func": ptt_058_trough_occurs_after_peak_252d},
    "ptt_059_peak_trough_timing_gap_252d": {"inputs": ["close"], "func": ptt_059_peak_trough_timing_gap_252d},
    "ptt_060_peak_trough_timing_gap_504d": {"inputs": ["close"], "func": ptt_060_peak_trough_timing_gap_504d},
    "ptt_061_ptt_ratio_63d_vs_252d": {"inputs": ["close"], "func": ptt_061_ptt_ratio_63d_vs_252d},
    "ptt_062_ptt_ratio_21d_vs_63d": {"inputs": ["close"], "func": ptt_062_ptt_ratio_21d_vs_63d},
    "ptt_063_ptt_ratio_252d_vs_expanding": {"inputs": ["close"], "func": ptt_063_ptt_ratio_252d_vs_expanding},
    "ptt_064_recovery_fraction_diff_252d_vs_63d": {"inputs": ["close"], "func": ptt_064_recovery_fraction_diff_252d_vs_63d},
    "ptt_065_recovery_fraction_diff_504d_vs_252d": {"inputs": ["close"], "func": ptt_065_recovery_fraction_diff_504d_vs_252d},
    "ptt_066_vol_adj_span_252d": {"inputs": ["close"], "func": ptt_066_vol_adj_span_252d},
    "ptt_067_vol_adj_span_63d": {"inputs": ["close"], "func": ptt_067_vol_adj_span_63d},
    "ptt_068_recovery_fraction_zscore_252d": {"inputs": ["close"], "func": ptt_068_recovery_fraction_zscore_252d},
    "ptt_069_recovery_fraction_pct_rank_252d": {"inputs": ["close"], "func": ptt_069_recovery_fraction_pct_rank_252d},
    "ptt_070_volume_at_trough_fraction_252d": {"inputs": ["close", "volume"], "func": ptt_070_volume_at_trough_fraction_252d},
    "ptt_071_volume_at_peak_fraction_252d": {"inputs": ["close", "volume"], "func": ptt_071_volume_at_peak_fraction_252d},
    "ptt_072_composite_recovery_fraction": {"inputs": ["close"], "func": ptt_072_composite_recovery_fraction},
    "ptt_073_composite_ptt_ratio": {"inputs": ["close"], "func": ptt_073_composite_ptt_ratio},
    "ptt_074_intraday_vs_close_recovery_fraction_252d": {"inputs": ["close", "high", "low"], "func": ptt_074_intraday_vs_close_recovery_fraction_252d},
    "ptt_075_span_acceleration_63d_vs_252d": {"inputs": ["close"], "func": ptt_075_span_acceleration_63d_vs_252d},
}
