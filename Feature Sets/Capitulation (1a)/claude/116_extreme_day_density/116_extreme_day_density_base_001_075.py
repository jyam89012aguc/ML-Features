"""
116_extreme_day_density — Base Features 001-075
Domain: density, spacing and clustering of isolated extreme down-days — count of days
        breaching return thresholds in trailing windows, time since last extreme day,
        average/min spacing between extreme days, clustering vs dispersion, share of
        total decline delivered by extreme days.
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


def _daily_return(close: pd.Series) -> pd.Series:
    """Simple daily log return."""
    return np.log(close / close.shift(1))


def _extreme_flag(close: pd.Series, threshold: float) -> pd.Series:
    """Binary flag: 1 where daily log return <= threshold, else 0."""
    ret = _daily_return(close)
    return (ret <= threshold).astype(float)


def _sigma_extreme_flag(close: pd.Series, window: int, sigma_mult: float) -> pd.Series:
    """Binary flag: 1 where return <= -sigma_mult * rolling_std over window."""
    ret = _daily_return(close)
    std = _rolling_std(ret, window)
    threshold = -sigma_mult * std
    return (ret <= threshold).astype(float)


def _time_since_last_extreme(flag: pd.Series) -> pd.Series:
    """Days elapsed since the most recent 1 in flag (0 = current day is extreme)."""
    idx = pd.Series(np.arange(len(flag), dtype=float), index=flag.index)
    last = idx.where(flag == 1.0).ffill()
    elapsed = idx - last
    # Where flag is NaN propagate NaN
    elapsed = elapsed.where(~flag.isna(), np.nan)
    return elapsed


def _rolling_spacing_mean(flag: pd.Series, w: int) -> pd.Series:
    """Mean gap (in days) between consecutive extreme days in trailing w-day window.
    NaN-safe: returns NaN when fewer than 2 extreme days in window."""
    def _mean_gap(arr):
        hits = np.where(arr == 1.0)[0]
        if len(hits) < 2:
            return np.nan
        gaps = np.diff(hits.astype(float))
        gaps = gaps[~np.isnan(gaps)]
        if len(gaps) == 0:
            return np.nan
        return gaps.mean()
    return flag.rolling(w, min_periods=max(2, w // 2)).apply(_mean_gap, raw=True)


def _rolling_spacing_min(flag: pd.Series, w: int) -> pd.Series:
    """Min gap (in days) between consecutive extreme days in trailing w-day window."""
    def _min_gap(arr):
        hits = np.where(arr == 1.0)[0]
        if len(hits) < 2:
            return np.nan
        gaps = np.diff(hits.astype(float))
        gaps = gaps[~np.isnan(gaps)]
        if len(gaps) == 0:
            return np.nan
        return gaps.min()
    return flag.rolling(w, min_periods=max(2, w // 2)).apply(_min_gap, raw=True)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Count of extreme days in trailing windows (fixed thresholds) ---

def edd_001_count_ret_neg5pct_21d(close: pd.Series) -> pd.Series:
    """Count of days with log return <= -5% in trailing 21 days."""
    return _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)


def edd_002_count_ret_neg5pct_63d(close: pd.Series) -> pd.Series:
    """Count of days with log return <= -5% in trailing 63 days."""
    return _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR)


def edd_003_count_ret_neg5pct_252d(close: pd.Series) -> pd.Series:
    """Count of days with log return <= -5% in trailing 252 days."""
    return _rolling_sum(_extreme_flag(close, -0.05), _TD_YEAR)


def edd_004_count_ret_neg10pct_21d(close: pd.Series) -> pd.Series:
    """Count of days with log return <= -10% in trailing 21 days."""
    return _rolling_sum(_extreme_flag(close, -0.10), _TD_MON)


def edd_005_count_ret_neg10pct_63d(close: pd.Series) -> pd.Series:
    """Count of days with log return <= -10% in trailing 63 days."""
    return _rolling_sum(_extreme_flag(close, -0.10), _TD_QTR)


def edd_006_count_ret_neg10pct_252d(close: pd.Series) -> pd.Series:
    """Count of days with log return <= -10% in trailing 252 days."""
    return _rolling_sum(_extreme_flag(close, -0.10), _TD_YEAR)


def edd_007_count_ret_neg3pct_21d(close: pd.Series) -> pd.Series:
    """Count of days with log return <= -3% in trailing 21 days."""
    return _rolling_sum(_extreme_flag(close, -0.03), _TD_MON)


def edd_008_count_ret_neg3pct_63d(close: pd.Series) -> pd.Series:
    """Count of days with log return <= -3% in trailing 63 days."""
    return _rolling_sum(_extreme_flag(close, -0.03), _TD_QTR)


def edd_009_count_ret_neg3pct_252d(close: pd.Series) -> pd.Series:
    """Count of days with log return <= -3% in trailing 252 days."""
    return _rolling_sum(_extreme_flag(close, -0.03), _TD_YEAR)


def edd_010_count_ret_neg7pct_63d(close: pd.Series) -> pd.Series:
    """Count of days with log return <= -7% in trailing 63 days."""
    return _rolling_sum(_extreme_flag(close, -0.07), _TD_QTR)


def edd_011_count_ret_neg7pct_252d(close: pd.Series) -> pd.Series:
    """Count of days with log return <= -7% in trailing 252 days."""
    return _rolling_sum(_extreme_flag(close, -0.07), _TD_YEAR)


def edd_012_count_ret_neg15pct_252d(close: pd.Series) -> pd.Series:
    """Count of days with log return <= -15% in trailing 252 days (gap-down events)."""
    return _rolling_sum(_extreme_flag(close, -0.15), _TD_YEAR)


def edd_013_count_ret_neg20pct_252d(close: pd.Series) -> pd.Series:
    """Count of days with log return <= -20% in trailing 252 days (crash-level events)."""
    return _rolling_sum(_extreme_flag(close, -0.20), _TD_YEAR)


def edd_014_count_ret_neg5pct_126d(close: pd.Series) -> pd.Series:
    """Count of days with log return <= -5% in trailing 126 days."""
    return _rolling_sum(_extreme_flag(close, -0.05), _TD_HALF)


def edd_015_count_ret_neg3pct_126d(close: pd.Series) -> pd.Series:
    """Count of days with log return <= -3% in trailing 126 days."""
    return _rolling_sum(_extreme_flag(close, -0.03), _TD_HALF)


# --- Group B (016-025): Count of sigma-based extreme days in trailing windows ---

def edd_016_count_2sigma_neg_21d(close: pd.Series) -> pd.Series:
    """Count of days with return <= -2 sigma (63d std) in trailing 21 days."""
    return _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_MON)


def edd_017_count_2sigma_neg_63d(close: pd.Series) -> pd.Series:
    """Count of days with return <= -2 sigma (63d std) in trailing 63 days."""
    return _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_QTR)


def edd_018_count_2sigma_neg_252d(close: pd.Series) -> pd.Series:
    """Count of days with return <= -2 sigma (63d std) in trailing 252 days."""
    return _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_YEAR)


def edd_019_count_3sigma_neg_63d(close: pd.Series) -> pd.Series:
    """Count of days with return <= -3 sigma (63d std) in trailing 63 days."""
    return _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 3.0), _TD_QTR)


def edd_020_count_3sigma_neg_252d(close: pd.Series) -> pd.Series:
    """Count of days with return <= -3 sigma (63d std) in trailing 252 days."""
    return _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 3.0), _TD_YEAR)


def edd_021_count_15sigma_neg_21d(close: pd.Series) -> pd.Series:
    """Count of days with return <= -1.5 sigma (21d std) in trailing 21 days."""
    return _rolling_sum(_sigma_extreme_flag(close, _TD_MON, 1.5), _TD_MON)


def edd_022_count_15sigma_neg_63d(close: pd.Series) -> pd.Series:
    """Count of days with return <= -1.5 sigma (21d std) in trailing 63 days."""
    return _rolling_sum(_sigma_extreme_flag(close, _TD_MON, 1.5), _TD_QTR)


def edd_023_count_25sigma_neg_63d(close: pd.Series) -> pd.Series:
    """Count of days with return <= -2.5 sigma (63d std) in trailing 63 days."""
    return _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.5), _TD_QTR)


def edd_024_count_25sigma_neg_252d(close: pd.Series) -> pd.Series:
    """Count of days with return <= -2.5 sigma (63d std) in trailing 252 days."""
    return _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.5), _TD_YEAR)


def edd_025_count_2sigma_neg_126d(close: pd.Series) -> pd.Series:
    """Count of days with return <= -2 sigma (63d std) in trailing 126 days."""
    return _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_HALF)


# --- Group C (026-035): Density fractions — extreme days as fraction of window ---

def edd_026_frac_neg5pct_21d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days with log return <= -5%."""
    return _rolling_sum(_extreme_flag(close, -0.05), _TD_MON) / _TD_MON


def edd_027_frac_neg5pct_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days with log return <= -5%."""
    return _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR) / _TD_QTR


def edd_028_frac_neg5pct_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days with log return <= -5%."""
    return _rolling_sum(_extreme_flag(close, -0.05), _TD_YEAR) / _TD_YEAR


def edd_029_frac_neg3pct_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days with log return <= -3%."""
    return _rolling_sum(_extreme_flag(close, -0.03), _TD_QTR) / _TD_QTR


def edd_030_frac_neg10pct_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days with log return <= -10%."""
    return _rolling_sum(_extreme_flag(close, -0.10), _TD_YEAR) / _TD_YEAR


def edd_031_frac_2sigma_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days with return <= -2 sigma (63d std)."""
    return _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_QTR) / _TD_QTR


def edd_032_frac_2sigma_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days with return <= -2 sigma (63d std)."""
    return _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_YEAR) / _TD_YEAR


def edd_033_frac_neg5pct_21d_norm252d(close: pd.Series) -> pd.Series:
    """21-day extreme-5% density normalized by 252-day average density."""
    frac21 = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON) / _TD_MON
    avg252 = _rolling_mean(frac21, _TD_YEAR)
    return _safe_div(frac21, avg252.clip(lower=_EPS))


def edd_034_frac_neg3pct_21d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days with log return <= -3%."""
    return _rolling_sum(_extreme_flag(close, -0.03), _TD_MON) / _TD_MON


def edd_035_frac_3sigma_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days with return <= -3 sigma (63d std)."""
    return _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 3.0), _TD_YEAR) / _TD_YEAR


# --- Group D (036-050): Time since last extreme day ---

def edd_036_days_since_last_neg5pct(close: pd.Series) -> pd.Series:
    """Days elapsed since most recent day with log return <= -5%."""
    return _time_since_last_extreme(_extreme_flag(close, -0.05))


def edd_037_days_since_last_neg10pct(close: pd.Series) -> pd.Series:
    """Days elapsed since most recent day with log return <= -10%."""
    return _time_since_last_extreme(_extreme_flag(close, -0.10))


def edd_038_days_since_last_neg3pct(close: pd.Series) -> pd.Series:
    """Days elapsed since most recent day with log return <= -3%."""
    return _time_since_last_extreme(_extreme_flag(close, -0.03))


def edd_039_days_since_last_neg7pct(close: pd.Series) -> pd.Series:
    """Days elapsed since most recent day with log return <= -7%."""
    return _time_since_last_extreme(_extreme_flag(close, -0.07))


def edd_040_days_since_last_2sigma(close: pd.Series) -> pd.Series:
    """Days elapsed since most recent 2-sigma down day (63d std)."""
    return _time_since_last_extreme(_sigma_extreme_flag(close, _TD_QTR, 2.0))


def edd_041_days_since_last_3sigma(close: pd.Series) -> pd.Series:
    """Days elapsed since most recent 3-sigma down day (63d std)."""
    return _time_since_last_extreme(_sigma_extreme_flag(close, _TD_QTR, 3.0))


def edd_042_days_since_last_neg15pct(close: pd.Series) -> pd.Series:
    """Days elapsed since most recent day with log return <= -15%."""
    return _time_since_last_extreme(_extreme_flag(close, -0.15))


def edd_043_days_since_last_neg5pct_log(close: pd.Series) -> pd.Series:
    """Log(1 + days_since_last -5% day) — compressed elapsed time."""
    elapsed = _time_since_last_extreme(_extreme_flag(close, -0.05))
    return np.log1p(elapsed.clip(lower=0.0))


def edd_044_days_since_last_neg10pct_log(close: pd.Series) -> pd.Series:
    """Log(1 + days_since_last -10% day) — compressed elapsed time."""
    elapsed = _time_since_last_extreme(_extreme_flag(close, -0.10))
    return np.log1p(elapsed.clip(lower=0.0))


def edd_045_days_since_last_2sigma_norm21d(close: pd.Series) -> pd.Series:
    """Days since last 2-sigma day normalized by 21-day window length."""
    elapsed = _time_since_last_extreme(_sigma_extreme_flag(close, _TD_QTR, 2.0))
    return elapsed / _TD_MON


def edd_046_days_since_last_neg5pct_norm252d(close: pd.Series) -> pd.Series:
    """Days since last -5% day normalized by 252-day window."""
    elapsed = _time_since_last_extreme(_extreme_flag(close, -0.05))
    return elapsed / _TD_YEAR


def edd_047_days_since_last_15sigma(close: pd.Series) -> pd.Series:
    """Days elapsed since most recent 1.5-sigma down day (21d std)."""
    return _time_since_last_extreme(_sigma_extreme_flag(close, _TD_MON, 1.5))


def edd_048_days_since_last_neg3pct_norm63d(close: pd.Series) -> pd.Series:
    """Days since last -3% day normalized by 63-day window."""
    elapsed = _time_since_last_extreme(_extreme_flag(close, -0.03))
    return elapsed / _TD_QTR


def edd_049_days_since_last_neg7pct_log(close: pd.Series) -> pd.Series:
    """Log(1 + days_since_last -7% day)."""
    elapsed = _time_since_last_extreme(_extreme_flag(close, -0.07))
    return np.log1p(elapsed.clip(lower=0.0))


def edd_050_days_since_last_25sigma(close: pd.Series) -> pd.Series:
    """Days elapsed since most recent 2.5-sigma down day (63d std)."""
    return _time_since_last_extreme(_sigma_extreme_flag(close, _TD_QTR, 2.5))


# --- Group E (051-065): Spacing between extreme days ---

def edd_051_mean_spacing_neg5pct_63d(close: pd.Series) -> pd.Series:
    """Mean gap in days between consecutive -5% days in trailing 63 days."""
    return _rolling_spacing_mean(_extreme_flag(close, -0.05), _TD_QTR)


def edd_052_mean_spacing_neg5pct_252d(close: pd.Series) -> pd.Series:
    """Mean gap in days between consecutive -5% days in trailing 252 days."""
    return _rolling_spacing_mean(_extreme_flag(close, -0.05), _TD_YEAR)


def edd_053_min_spacing_neg5pct_63d(close: pd.Series) -> pd.Series:
    """Minimum gap in days between consecutive -5% days in trailing 63 days."""
    return _rolling_spacing_min(_extreme_flag(close, -0.05), _TD_QTR)


def edd_054_min_spacing_neg5pct_252d(close: pd.Series) -> pd.Series:
    """Minimum gap in days between consecutive -5% days in trailing 252 days."""
    return _rolling_spacing_min(_extreme_flag(close, -0.05), _TD_YEAR)


def edd_055_mean_spacing_2sigma_63d(close: pd.Series) -> pd.Series:
    """Mean gap between consecutive 2-sigma down days in trailing 63 days."""
    return _rolling_spacing_mean(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_QTR)


def edd_056_mean_spacing_2sigma_252d(close: pd.Series) -> pd.Series:
    """Mean gap between consecutive 2-sigma down days in trailing 252 days."""
    return _rolling_spacing_mean(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_YEAR)


def edd_057_min_spacing_2sigma_252d(close: pd.Series) -> pd.Series:
    """Minimum gap between consecutive 2-sigma down days in trailing 252 days."""
    return _rolling_spacing_min(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_YEAR)


def edd_058_mean_spacing_neg3pct_63d(close: pd.Series) -> pd.Series:
    """Mean gap between consecutive -3% days in trailing 63 days."""
    return _rolling_spacing_mean(_extreme_flag(close, -0.03), _TD_QTR)


def edd_059_mean_spacing_neg10pct_252d(close: pd.Series) -> pd.Series:
    """Mean gap between consecutive -10% days in trailing 252 days."""
    return _rolling_spacing_mean(_extreme_flag(close, -0.10), _TD_YEAR)


def edd_060_min_spacing_neg3pct_63d(close: pd.Series) -> pd.Series:
    """Minimum gap between consecutive -3% days in trailing 63 days."""
    return _rolling_spacing_min(_extreme_flag(close, -0.03), _TD_QTR)


def edd_061_mean_spacing_neg5pct_126d(close: pd.Series) -> pd.Series:
    """Mean gap between consecutive -5% days in trailing 126 days."""
    return _rolling_spacing_mean(_extreme_flag(close, -0.05), _TD_HALF)


def edd_062_min_spacing_2sigma_63d(close: pd.Series) -> pd.Series:
    """Minimum gap between consecutive 2-sigma down days in trailing 63 days."""
    return _rolling_spacing_min(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_QTR)


def edd_063_mean_spacing_neg7pct_252d(close: pd.Series) -> pd.Series:
    """Mean gap between consecutive -7% days in trailing 252 days."""
    return _rolling_spacing_mean(_extreme_flag(close, -0.07), _TD_YEAR)


def edd_064_spacing_cv_neg5pct_252d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of gaps between -5% days in trailing 252 days.
    High CV = irregular/clustered; low CV = evenly spaced."""
    def _cv_gap(arr):
        hits = np.where(arr == 1.0)[0]
        if len(hits) < 3:
            return np.nan
        gaps = np.diff(hits.astype(float))
        gaps = gaps[~np.isnan(gaps)]
        if len(gaps) < 2 or gaps.mean() < _EPS:
            return np.nan
        return gaps.std() / gaps.mean()
    return _extreme_flag(close, -0.05).rolling(_TD_YEAR, min_periods=_TD_QTR).apply(_cv_gap, raw=True)


def edd_065_spacing_cv_2sigma_252d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of gaps between 2-sigma down days in trailing 252 days."""
    def _cv_gap(arr):
        hits = np.where(arr == 1.0)[0]
        if len(hits) < 3:
            return np.nan
        gaps = np.diff(hits.astype(float))
        gaps = gaps[~np.isnan(gaps)]
        if len(gaps) < 2 or gaps.mean() < _EPS:
            return np.nan
        return gaps.std() / gaps.mean()
    return _sigma_extreme_flag(close, _TD_QTR, 2.0).rolling(_TD_YEAR, min_periods=_TD_QTR).apply(_cv_gap, raw=True)


# --- Group F (066-075): Share of total decline from extreme days ---

def edd_066_extreme5pct_share_decline_63d(close: pd.Series) -> pd.Series:
    """Share of total negative return in 63d delivered by -5% days (0 if no decline)."""
    ret = _daily_return(close)
    flag5 = _extreme_flag(close, -0.05)
    extreme_sum = _rolling_sum(ret * flag5, _TD_QTR)
    total_neg = _rolling_sum(ret.clip(upper=0.0), _TD_QTR)
    return _safe_div(extreme_sum, total_neg.clip(upper=-_EPS))


def edd_067_extreme5pct_share_decline_252d(close: pd.Series) -> pd.Series:
    """Share of total negative return in 252d delivered by -5% days."""
    ret = _daily_return(close)
    flag5 = _extreme_flag(close, -0.05)
    extreme_sum = _rolling_sum(ret * flag5, _TD_YEAR)
    total_neg = _rolling_sum(ret.clip(upper=0.0), _TD_YEAR)
    return _safe_div(extreme_sum, total_neg.clip(upper=-_EPS))


def edd_068_extreme3pct_share_decline_63d(close: pd.Series) -> pd.Series:
    """Share of total negative return in 63d delivered by -3% days."""
    ret = _daily_return(close)
    flag3 = _extreme_flag(close, -0.03)
    extreme_sum = _rolling_sum(ret * flag3, _TD_QTR)
    total_neg = _rolling_sum(ret.clip(upper=0.0), _TD_QTR)
    return _safe_div(extreme_sum, total_neg.clip(upper=-_EPS))


def edd_069_extreme10pct_share_decline_252d(close: pd.Series) -> pd.Series:
    """Share of total negative return in 252d delivered by -10% days."""
    ret = _daily_return(close)
    flag10 = _extreme_flag(close, -0.10)
    extreme_sum = _rolling_sum(ret * flag10, _TD_YEAR)
    total_neg = _rolling_sum(ret.clip(upper=0.0), _TD_YEAR)
    return _safe_div(extreme_sum, total_neg.clip(upper=-_EPS))


def edd_070_extreme5pct_share_decline_126d(close: pd.Series) -> pd.Series:
    """Share of total negative return in 126d delivered by -5% days."""
    ret = _daily_return(close)
    flag5 = _extreme_flag(close, -0.05)
    extreme_sum = _rolling_sum(ret * flag5, _TD_HALF)
    total_neg = _rolling_sum(ret.clip(upper=0.0), _TD_HALF)
    return _safe_div(extreme_sum, total_neg.clip(upper=-_EPS))


def edd_071_extreme_sum_ret_neg5pct_21d(close: pd.Series) -> pd.Series:
    """Sum of log returns on -5% days in trailing 21 days."""
    ret = _daily_return(close)
    flag5 = _extreme_flag(close, -0.05)
    return _rolling_sum(ret * flag5, _TD_MON)


def edd_072_extreme_sum_ret_neg5pct_63d(close: pd.Series) -> pd.Series:
    """Sum of log returns on -5% days in trailing 63 days."""
    ret = _daily_return(close)
    flag5 = _extreme_flag(close, -0.05)
    return _rolling_sum(ret * flag5, _TD_QTR)


def edd_073_extreme_avg_ret_neg5pct_63d(close: pd.Series) -> pd.Series:
    """Average log return on -5% days in trailing 63 days (mean severity)."""
    ret = _daily_return(close)
    flag5 = _extreme_flag(close, -0.05)
    cnt = _rolling_sum(flag5, _TD_QTR).replace(0, np.nan)
    return _safe_div(_rolling_sum(ret * flag5, _TD_QTR), cnt)


def edd_074_extreme5pct_count_norm_vs_neg3pct_63d(close: pd.Series) -> pd.Series:
    """Ratio of -5% day count to -3% day count in 63d (how many moderate lows are extreme)."""
    cnt5 = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR)
    cnt3 = _rolling_sum(_extreme_flag(close, -0.03), _TD_QTR)
    return _safe_div(cnt5, cnt3.clip(lower=_EPS))


def edd_075_extreme_day_flag_current(close: pd.Series) -> pd.Series:
    """Binary flag: today's log return <= -5% (current day is extreme down)."""
    return _extreme_flag(close, -0.05)


# ── Registry ──────────────────────────────────────────────────────────────────

EXTREME_DAY_DENSITY_REGISTRY_001_075 = {
    "edd_001_count_ret_neg5pct_21d": {"inputs": ["close"], "func": edd_001_count_ret_neg5pct_21d},
    "edd_002_count_ret_neg5pct_63d": {"inputs": ["close"], "func": edd_002_count_ret_neg5pct_63d},
    "edd_003_count_ret_neg5pct_252d": {"inputs": ["close"], "func": edd_003_count_ret_neg5pct_252d},
    "edd_004_count_ret_neg10pct_21d": {"inputs": ["close"], "func": edd_004_count_ret_neg10pct_21d},
    "edd_005_count_ret_neg10pct_63d": {"inputs": ["close"], "func": edd_005_count_ret_neg10pct_63d},
    "edd_006_count_ret_neg10pct_252d": {"inputs": ["close"], "func": edd_006_count_ret_neg10pct_252d},
    "edd_007_count_ret_neg3pct_21d": {"inputs": ["close"], "func": edd_007_count_ret_neg3pct_21d},
    "edd_008_count_ret_neg3pct_63d": {"inputs": ["close"], "func": edd_008_count_ret_neg3pct_63d},
    "edd_009_count_ret_neg3pct_252d": {"inputs": ["close"], "func": edd_009_count_ret_neg3pct_252d},
    "edd_010_count_ret_neg7pct_63d": {"inputs": ["close"], "func": edd_010_count_ret_neg7pct_63d},
    "edd_011_count_ret_neg7pct_252d": {"inputs": ["close"], "func": edd_011_count_ret_neg7pct_252d},
    "edd_012_count_ret_neg15pct_252d": {"inputs": ["close"], "func": edd_012_count_ret_neg15pct_252d},
    "edd_013_count_ret_neg20pct_252d": {"inputs": ["close"], "func": edd_013_count_ret_neg20pct_252d},
    "edd_014_count_ret_neg5pct_126d": {"inputs": ["close"], "func": edd_014_count_ret_neg5pct_126d},
    "edd_015_count_ret_neg3pct_126d": {"inputs": ["close"], "func": edd_015_count_ret_neg3pct_126d},
    "edd_016_count_2sigma_neg_21d": {"inputs": ["close"], "func": edd_016_count_2sigma_neg_21d},
    "edd_017_count_2sigma_neg_63d": {"inputs": ["close"], "func": edd_017_count_2sigma_neg_63d},
    "edd_018_count_2sigma_neg_252d": {"inputs": ["close"], "func": edd_018_count_2sigma_neg_252d},
    "edd_019_count_3sigma_neg_63d": {"inputs": ["close"], "func": edd_019_count_3sigma_neg_63d},
    "edd_020_count_3sigma_neg_252d": {"inputs": ["close"], "func": edd_020_count_3sigma_neg_252d},
    "edd_021_count_15sigma_neg_21d": {"inputs": ["close"], "func": edd_021_count_15sigma_neg_21d},
    "edd_022_count_15sigma_neg_63d": {"inputs": ["close"], "func": edd_022_count_15sigma_neg_63d},
    "edd_023_count_25sigma_neg_63d": {"inputs": ["close"], "func": edd_023_count_25sigma_neg_63d},
    "edd_024_count_25sigma_neg_252d": {"inputs": ["close"], "func": edd_024_count_25sigma_neg_252d},
    "edd_025_count_2sigma_neg_126d": {"inputs": ["close"], "func": edd_025_count_2sigma_neg_126d},
    "edd_026_frac_neg5pct_21d": {"inputs": ["close"], "func": edd_026_frac_neg5pct_21d},
    "edd_027_frac_neg5pct_63d": {"inputs": ["close"], "func": edd_027_frac_neg5pct_63d},
    "edd_028_frac_neg5pct_252d": {"inputs": ["close"], "func": edd_028_frac_neg5pct_252d},
    "edd_029_frac_neg3pct_63d": {"inputs": ["close"], "func": edd_029_frac_neg3pct_63d},
    "edd_030_frac_neg10pct_252d": {"inputs": ["close"], "func": edd_030_frac_neg10pct_252d},
    "edd_031_frac_2sigma_63d": {"inputs": ["close"], "func": edd_031_frac_2sigma_63d},
    "edd_032_frac_2sigma_252d": {"inputs": ["close"], "func": edd_032_frac_2sigma_252d},
    "edd_033_frac_neg5pct_21d_norm252d": {"inputs": ["close"], "func": edd_033_frac_neg5pct_21d_norm252d},
    "edd_034_frac_neg3pct_21d": {"inputs": ["close"], "func": edd_034_frac_neg3pct_21d},
    "edd_035_frac_3sigma_252d": {"inputs": ["close"], "func": edd_035_frac_3sigma_252d},
    "edd_036_days_since_last_neg5pct": {"inputs": ["close"], "func": edd_036_days_since_last_neg5pct},
    "edd_037_days_since_last_neg10pct": {"inputs": ["close"], "func": edd_037_days_since_last_neg10pct},
    "edd_038_days_since_last_neg3pct": {"inputs": ["close"], "func": edd_038_days_since_last_neg3pct},
    "edd_039_days_since_last_neg7pct": {"inputs": ["close"], "func": edd_039_days_since_last_neg7pct},
    "edd_040_days_since_last_2sigma": {"inputs": ["close"], "func": edd_040_days_since_last_2sigma},
    "edd_041_days_since_last_3sigma": {"inputs": ["close"], "func": edd_041_days_since_last_3sigma},
    "edd_042_days_since_last_neg15pct": {"inputs": ["close"], "func": edd_042_days_since_last_neg15pct},
    "edd_043_days_since_last_neg5pct_log": {"inputs": ["close"], "func": edd_043_days_since_last_neg5pct_log},
    "edd_044_days_since_last_neg10pct_log": {"inputs": ["close"], "func": edd_044_days_since_last_neg10pct_log},
    "edd_045_days_since_last_2sigma_norm21d": {"inputs": ["close"], "func": edd_045_days_since_last_2sigma_norm21d},
    "edd_046_days_since_last_neg5pct_norm252d": {"inputs": ["close"], "func": edd_046_days_since_last_neg5pct_norm252d},
    "edd_047_days_since_last_15sigma": {"inputs": ["close"], "func": edd_047_days_since_last_15sigma},
    "edd_048_days_since_last_neg3pct_norm63d": {"inputs": ["close"], "func": edd_048_days_since_last_neg3pct_norm63d},
    "edd_049_days_since_last_neg7pct_log": {"inputs": ["close"], "func": edd_049_days_since_last_neg7pct_log},
    "edd_050_days_since_last_25sigma": {"inputs": ["close"], "func": edd_050_days_since_last_25sigma},
    "edd_051_mean_spacing_neg5pct_63d": {"inputs": ["close"], "func": edd_051_mean_spacing_neg5pct_63d},
    "edd_052_mean_spacing_neg5pct_252d": {"inputs": ["close"], "func": edd_052_mean_spacing_neg5pct_252d},
    "edd_053_min_spacing_neg5pct_63d": {"inputs": ["close"], "func": edd_053_min_spacing_neg5pct_63d},
    "edd_054_min_spacing_neg5pct_252d": {"inputs": ["close"], "func": edd_054_min_spacing_neg5pct_252d},
    "edd_055_mean_spacing_2sigma_63d": {"inputs": ["close"], "func": edd_055_mean_spacing_2sigma_63d},
    "edd_056_mean_spacing_2sigma_252d": {"inputs": ["close"], "func": edd_056_mean_spacing_2sigma_252d},
    "edd_057_min_spacing_2sigma_252d": {"inputs": ["close"], "func": edd_057_min_spacing_2sigma_252d},
    "edd_058_mean_spacing_neg3pct_63d": {"inputs": ["close"], "func": edd_058_mean_spacing_neg3pct_63d},
    "edd_059_mean_spacing_neg10pct_252d": {"inputs": ["close"], "func": edd_059_mean_spacing_neg10pct_252d},
    "edd_060_min_spacing_neg3pct_63d": {"inputs": ["close"], "func": edd_060_min_spacing_neg3pct_63d},
    "edd_061_mean_spacing_neg5pct_126d": {"inputs": ["close"], "func": edd_061_mean_spacing_neg5pct_126d},
    "edd_062_min_spacing_2sigma_63d": {"inputs": ["close"], "func": edd_062_min_spacing_2sigma_63d},
    "edd_063_mean_spacing_neg7pct_252d": {"inputs": ["close"], "func": edd_063_mean_spacing_neg7pct_252d},
    "edd_064_spacing_cv_neg5pct_252d": {"inputs": ["close"], "func": edd_064_spacing_cv_neg5pct_252d},
    "edd_065_spacing_cv_2sigma_252d": {"inputs": ["close"], "func": edd_065_spacing_cv_2sigma_252d},
    "edd_066_extreme5pct_share_decline_63d": {"inputs": ["close"], "func": edd_066_extreme5pct_share_decline_63d},
    "edd_067_extreme5pct_share_decline_252d": {"inputs": ["close"], "func": edd_067_extreme5pct_share_decline_252d},
    "edd_068_extreme3pct_share_decline_63d": {"inputs": ["close"], "func": edd_068_extreme3pct_share_decline_63d},
    "edd_069_extreme10pct_share_decline_252d": {"inputs": ["close"], "func": edd_069_extreme10pct_share_decline_252d},
    "edd_070_extreme5pct_share_decline_126d": {"inputs": ["close"], "func": edd_070_extreme5pct_share_decline_126d},
    "edd_071_extreme_sum_ret_neg5pct_21d": {"inputs": ["close"], "func": edd_071_extreme_sum_ret_neg5pct_21d},
    "edd_072_extreme_sum_ret_neg5pct_63d": {"inputs": ["close"], "func": edd_072_extreme_sum_ret_neg5pct_63d},
    "edd_073_extreme_avg_ret_neg5pct_63d": {"inputs": ["close"], "func": edd_073_extreme_avg_ret_neg5pct_63d},
    "edd_074_extreme5pct_count_norm_vs_neg3pct_63d": {"inputs": ["close"], "func": edd_074_extreme5pct_count_norm_vs_neg3pct_63d},
    "edd_075_extreme_day_flag_current": {"inputs": ["close"], "func": edd_075_extreme_day_flag_current},
}
