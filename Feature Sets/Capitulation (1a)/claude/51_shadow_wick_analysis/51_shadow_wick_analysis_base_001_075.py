"""
51_shadow_wick_analysis — Base Features 001-075
Domain: upper/lower wick (shadow) geometry — wick lengths, wick-to-range ratios,
        wick asymmetry, long-lower-wick frequency, wick percentile ranks,
        consecutive long-lower-wick days, wick z-scores at price lows.
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods."""
    def _max_run(arr):
        mx = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_max_run, raw=True)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _lower_wick(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower wick = distance from low to the lower of open/close."""
    body_low = pd.concat([open, close], axis=1).min(axis=1)
    return (body_low - low).clip(lower=0.0)


def _upper_wick(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Upper wick = distance from high to the upper of open/close."""
    body_high = pd.concat([open, close], axis=1).max(axis=1)
    return (high - body_high).clip(lower=0.0)


def _candle_range(high: pd.Series, low: pd.Series) -> pd.Series:
    """Full high-low range of the candle."""
    return (high - low).clip(lower=_EPS)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Raw lower-wick length and lower-wick-to-range ratio ---

def swk_001_lower_wick_abs(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute lower wick length (body_low - low) in price units."""
    return _lower_wick(open, high, low, close)


def swk_002_lower_wick_ratio(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower wick as fraction of full high-low range."""
    lw = _lower_wick(open, high, low, close)
    rng = _candle_range(high, low)
    return _safe_div(lw, rng)


def swk_003_lower_wick_pct_of_close(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower wick length as percentage of closing price."""
    lw = _lower_wick(open, high, low, close)
    return _safe_div(lw, close.clip(lower=_EPS))


def swk_004_lower_wick_norm_atr21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower wick normalized by 21-day average true range."""
    lw = _lower_wick(open, high, low, close)
    tr = _candle_range(high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    return _safe_div(lw, atr21)


def swk_005_lower_wick_sma21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling mean of lower wick length."""
    lw = _lower_wick(open, high, low, close)
    return _rolling_mean(lw, _TD_MON)


def swk_006_lower_wick_sma63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling mean of lower wick length."""
    lw = _lower_wick(open, high, low, close)
    return _rolling_mean(lw, _TD_QTR)


def swk_007_lower_wick_ratio_sma21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling mean of lower-wick-to-range ratio."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    return _rolling_mean(lwr, _TD_MON)


def swk_008_lower_wick_ratio_sma63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling mean of lower-wick-to-range ratio."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    return _rolling_mean(lwr, _TD_QTR)


def swk_009_lower_wick_ratio_sma252(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling mean of lower-wick-to-range ratio."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    return _rolling_mean(lwr, _TD_YEAR)


def swk_010_lower_wick_max_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling maximum lower wick length."""
    lw = _lower_wick(open, high, low, close)
    return _rolling_max(lw, _TD_MON)


def swk_011_lower_wick_max_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling maximum lower wick length."""
    lw = _lower_wick(open, high, low, close)
    return _rolling_max(lw, _TD_QTR)


def swk_012_lower_wick_max_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling maximum lower wick length."""
    lw = _lower_wick(open, high, low, close)
    return _rolling_max(lw, _TD_YEAR)


def swk_013_lower_wick_ratio_max_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling maximum lower-wick-to-range ratio."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    return _rolling_max(lwr, _TD_MON)


def swk_014_lower_wick_ratio_max_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling maximum lower-wick-to-range ratio."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    return _rolling_max(lwr, _TD_QTR)


def swk_015_lower_wick_ratio_max_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling maximum lower-wick-to-range ratio."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    return _rolling_max(lwr, _TD_YEAR)


# --- Group B (016-030): Upper wick length and upper-wick-to-range ratio ---

def swk_016_upper_wick_abs(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute upper wick length (high - body_high) in price units."""
    return _upper_wick(open, high, low, close)


def swk_017_upper_wick_ratio(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Upper wick as fraction of full high-low range."""
    uw = _upper_wick(open, high, low, close)
    rng = _candle_range(high, low)
    return _safe_div(uw, rng)


def swk_018_upper_wick_pct_of_close(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Upper wick length as percentage of closing price."""
    uw = _upper_wick(open, high, low, close)
    return _safe_div(uw, close.clip(lower=_EPS))


def swk_019_upper_wick_norm_atr21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Upper wick normalized by 21-day average true range."""
    uw = _upper_wick(open, high, low, close)
    tr = _candle_range(high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    return _safe_div(uw, atr21)


def swk_020_upper_wick_sma21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling mean of upper wick length."""
    uw = _upper_wick(open, high, low, close)
    return _rolling_mean(uw, _TD_MON)


def swk_021_upper_wick_sma63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling mean of upper wick length."""
    uw = _upper_wick(open, high, low, close)
    return _rolling_mean(uw, _TD_QTR)


def swk_022_upper_wick_ratio_sma21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling mean of upper-wick-to-range ratio."""
    uwr = swk_017_upper_wick_ratio(open, high, low, close)
    return _rolling_mean(uwr, _TD_MON)


def swk_023_upper_wick_ratio_sma63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling mean of upper-wick-to-range ratio."""
    uwr = swk_017_upper_wick_ratio(open, high, low, close)
    return _rolling_mean(uwr, _TD_QTR)


def swk_024_upper_wick_ratio_sma252(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling mean of upper-wick-to-range ratio."""
    uwr = swk_017_upper_wick_ratio(open, high, low, close)
    return _rolling_mean(uwr, _TD_YEAR)


def swk_025_upper_wick_max_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling maximum upper wick length."""
    uw = _upper_wick(open, high, low, close)
    return _rolling_max(uw, _TD_MON)


def swk_026_upper_wick_max_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling maximum upper wick length."""
    uw = _upper_wick(open, high, low, close)
    return _rolling_max(uw, _TD_QTR)


def swk_027_upper_wick_max_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling maximum upper wick length."""
    uw = _upper_wick(open, high, low, close)
    return _rolling_max(uw, _TD_YEAR)


def swk_028_upper_wick_ratio_max_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling maximum upper-wick-to-range ratio."""
    uwr = swk_017_upper_wick_ratio(open, high, low, close)
    return _rolling_max(uwr, _TD_MON)


def swk_029_upper_wick_ratio_max_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling maximum upper-wick-to-range ratio."""
    uwr = swk_017_upper_wick_ratio(open, high, low, close)
    return _rolling_max(uwr, _TD_QTR)


def swk_030_upper_wick_ratio_max_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling maximum upper-wick-to-range ratio."""
    uwr = swk_017_upper_wick_ratio(open, high, low, close)
    return _rolling_max(uwr, _TD_YEAR)


# --- Group C (031-045): Lower-vs-upper wick asymmetry ---

def swk_031_wick_asymmetry_ratio(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower wick divided by upper wick (>1 = lower-wick dominant = rejection of lows)."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close)
    return _safe_div(lw, uw.clip(lower=_EPS))


def swk_032_wick_asymmetry_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower wick minus upper wick (positive = lower-wick dominant)."""
    return _lower_wick(open, high, low, close) - _upper_wick(open, high, low, close)


def swk_033_wick_asymmetry_diff_norm_range(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(Lower wick - upper wick) / range; signed asymmetry scaled to range."""
    diff = swk_032_wick_asymmetry_diff(open, high, low, close)
    rng = _candle_range(high, low)
    return _safe_div(diff, rng)


def swk_034_wick_asymmetry_ratio_sma21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling mean of lower/upper wick ratio."""
    asym = swk_031_wick_asymmetry_ratio(open, high, low, close)
    return _rolling_mean(asym, _TD_MON)


def swk_035_wick_asymmetry_ratio_sma63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling mean of lower/upper wick ratio."""
    asym = swk_031_wick_asymmetry_ratio(open, high, low, close)
    return _rolling_mean(asym, _TD_QTR)


def swk_036_wick_asymmetry_ratio_sma252(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling mean of lower/upper wick ratio."""
    asym = swk_031_wick_asymmetry_ratio(open, high, low, close)
    return _rolling_mean(asym, _TD_YEAR)


def swk_037_wick_asymmetry_diff_sma21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling mean of (lower - upper) wick difference."""
    diff = swk_032_wick_asymmetry_diff(open, high, low, close)
    return _rolling_mean(diff, _TD_MON)


def swk_038_wick_asymmetry_diff_sma63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling mean of (lower - upper) wick difference."""
    diff = swk_032_wick_asymmetry_diff(open, high, low, close)
    return _rolling_mean(diff, _TD_QTR)


def swk_039_lower_dominant_flag(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: lower wick > upper wick (rejection of lower prices today)."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close)
    return (lw > uw).astype(float)


def swk_040_lower_dominant_fraction_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 21 days where lower wick > upper wick."""
    flag = swk_039_lower_dominant_flag(open, high, low, close)
    return _rolling_mean(flag, _TD_MON)


def swk_041_lower_dominant_fraction_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63 days where lower wick > upper wick."""
    flag = swk_039_lower_dominant_flag(open, high, low, close)
    return _rolling_mean(flag, _TD_QTR)


def swk_042_lower_dominant_fraction_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 252 days where lower wick > upper wick."""
    flag = swk_039_lower_dominant_flag(open, high, low, close)
    return _rolling_mean(flag, _TD_YEAR)


def swk_043_wick_asym_max_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day max of lower/upper wick ratio (peak rejection intensity)."""
    asym = swk_031_wick_asymmetry_ratio(open, high, low, close)
    return _rolling_max(asym, _TD_MON)


def swk_044_wick_asym_max_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day max of lower/upper wick ratio."""
    asym = swk_031_wick_asymmetry_ratio(open, high, low, close)
    return _rolling_max(asym, _TD_QTR)


def swk_045_wick_asym_norm_diff_sma21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean of range-normalized wick asymmetry diff."""
    nd = swk_033_wick_asymmetry_diff_norm_range(open, high, low, close)
    return _rolling_mean(nd, _TD_MON)


# --- Group D (046-060): Long-lower-wick frequency and counts ---

def swk_046_long_lower_wick_flag_33pct(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: lower wick ratio > 0.33 (lower wick covers >1/3 of range)."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    return (lwr > 0.33).astype(float)


def swk_047_long_lower_wick_flag_50pct(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: lower wick ratio > 0.50 (lower wick is majority of range)."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    return (lwr > 0.50).astype(float)


def swk_048_long_lower_wick_flag_66pct(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: lower wick ratio > 0.66 (lower wick covers >2/3 of range; strong hammer)."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    return (lwr > 0.66).astype(float)


def swk_049_long_lower_wick_count_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of long-lower-wick days (ratio>0.33) in trailing 21 days."""
    flag = swk_046_long_lower_wick_flag_33pct(open, high, low, close)
    return _rolling_sum(flag, _TD_MON)


def swk_050_long_lower_wick_count_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of long-lower-wick days (ratio>0.33) in trailing 63 days."""
    flag = swk_046_long_lower_wick_flag_33pct(open, high, low, close)
    return _rolling_sum(flag, _TD_QTR)


def swk_051_long_lower_wick_count_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of long-lower-wick days (ratio>0.33) in trailing 252 days."""
    flag = swk_046_long_lower_wick_flag_33pct(open, high, low, close)
    return _rolling_sum(flag, _TD_YEAR)


def swk_052_strong_hammer_count_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of strong-hammer days (ratio>0.66) in trailing 21 days."""
    flag = swk_048_long_lower_wick_flag_66pct(open, high, low, close)
    return _rolling_sum(flag, _TD_MON)


def swk_053_strong_hammer_count_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of strong-hammer days (ratio>0.66) in trailing 63 days."""
    flag = swk_048_long_lower_wick_flag_66pct(open, high, low, close)
    return _rolling_sum(flag, _TD_QTR)


def swk_054_long_lower_wick_fraction_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 21 days that had a long lower wick (ratio>0.33)."""
    flag = swk_046_long_lower_wick_flag_33pct(open, high, low, close)
    return _rolling_mean(flag, _TD_MON)


def swk_055_long_lower_wick_fraction_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63 days that had a long lower wick (ratio>0.33)."""
    flag = swk_046_long_lower_wick_flag_33pct(open, high, low, close)
    return _rolling_mean(flag, _TD_QTR)


def swk_056_long_lower_wick_fraction_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 252 days that had a long lower wick (ratio>0.33)."""
    flag = swk_046_long_lower_wick_flag_33pct(open, high, low, close)
    return _rolling_mean(flag, _TD_YEAR)


def swk_057_consec_long_lower_wick(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-day streak of long lower wicks (ratio>0.33)."""
    cond = swk_046_long_lower_wick_flag_33pct(open, high, low, close).astype(bool)
    return _consec_streak(cond)


def swk_058_max_consec_long_lower_wick_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day max consecutive long-lower-wick streak."""
    cond = swk_046_long_lower_wick_flag_33pct(open, high, low, close).astype(bool)
    return _rolling_max_streak(cond, _TD_QTR)


def swk_059_max_consec_long_lower_wick_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day max consecutive long-lower-wick streak."""
    cond = swk_046_long_lower_wick_flag_33pct(open, high, low, close).astype(bool)
    return _rolling_max_streak(cond, _TD_YEAR)


def swk_060_long_lower_wick_ewm21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-span EWM of lower-wick-to-range ratio (adaptive smoothing)."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    return _ewm_mean(lwr, _TD_MON)


# --- Group E (061-075): Wick ratio percentile ranks and z-scores ---

def swk_061_lower_wick_ratio_pct_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's lower-wick ratio within trailing 63 days."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    return lwr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def swk_062_lower_wick_ratio_pct_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's lower-wick ratio within trailing 252 days."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    return lwr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def swk_063_upper_wick_ratio_pct_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's upper-wick ratio within trailing 63 days."""
    uwr = swk_017_upper_wick_ratio(open, high, low, close)
    return uwr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def swk_064_upper_wick_ratio_pct_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's upper-wick ratio within trailing 252 days."""
    uwr = swk_017_upper_wick_ratio(open, high, low, close)
    return uwr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def swk_065_lower_wick_ratio_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of today's lower-wick ratio relative to 63-day distribution."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    m = _rolling_mean(lwr, _TD_QTR)
    s = _rolling_std(lwr, _TD_QTR)
    return _safe_div(lwr - m, s)


def swk_066_lower_wick_ratio_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of today's lower-wick ratio relative to 252-day distribution."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    m = _rolling_mean(lwr, _TD_YEAR)
    s = _rolling_std(lwr, _TD_YEAR)
    return _safe_div(lwr - m, s)


def swk_067_upper_wick_ratio_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of today's upper-wick ratio relative to 63-day distribution."""
    uwr = swk_017_upper_wick_ratio(open, high, low, close)
    m = _rolling_mean(uwr, _TD_QTR)
    s = _rolling_std(uwr, _TD_QTR)
    return _safe_div(uwr - m, s)


def swk_068_upper_wick_ratio_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of today's upper-wick ratio relative to 252-day distribution."""
    uwr = swk_017_upper_wick_ratio(open, high, low, close)
    m = _rolling_mean(uwr, _TD_YEAR)
    s = _rolling_std(uwr, _TD_YEAR)
    return _safe_div(uwr - m, s)


def swk_069_wick_asym_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of lower/upper wick ratio relative to 63-day distribution."""
    asym = swk_031_wick_asymmetry_ratio(open, high, low, close)
    m = _rolling_mean(asym, _TD_QTR)
    s = _rolling_std(asym, _TD_QTR)
    return _safe_div(asym - m, s)


def swk_070_wick_asym_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of lower/upper wick ratio relative to 252-day distribution."""
    asym = swk_031_wick_asymmetry_ratio(open, high, low, close)
    m = _rolling_mean(asym, _TD_YEAR)
    s = _rolling_std(asym, _TD_YEAR)
    return _safe_div(asym - m, s)


def swk_071_lower_wick_ratio_expanding_rank(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding percentile rank of lower-wick ratio (all-history extremity)."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    return lwr.expanding(min_periods=5).rank(pct=True)


def swk_072_lower_wick_ratio_expanding_zscore(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding z-score of lower-wick ratio (all-history deviation)."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    m = lwr.expanding(min_periods=5).mean()
    s = lwr.expanding(min_periods=5).std()
    return _safe_div(lwr - m, s)


def swk_073_lower_wick_abs_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of absolute lower wick length vs 252-day distribution."""
    lw = _lower_wick(open, high, low, close)
    m = _rolling_mean(lw, _TD_YEAR)
    s = _rolling_std(lw, _TD_YEAR)
    return _safe_div(lw - m, s)


def swk_074_lower_wick_ratio_median_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling median of lower-wick-to-range ratio."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    return _rolling_median(lwr, _TD_MON)


def swk_075_lower_wick_ratio_above_median_flag(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: today's lower-wick ratio is above its 63-day rolling median."""
    lwr = swk_002_lower_wick_ratio(open, high, low, close)
    med = _rolling_median(lwr, _TD_QTR)
    return (lwr > med).astype(float)


# ── Registry ──────────────────────────────────────────────────────────────────

SHADOW_WICK_ANALYSIS_REGISTRY_001_075 = {
    "swk_001_lower_wick_abs": {"inputs": ["open", "high", "low", "close"], "func": swk_001_lower_wick_abs},
    "swk_002_lower_wick_ratio": {"inputs": ["open", "high", "low", "close"], "func": swk_002_lower_wick_ratio},
    "swk_003_lower_wick_pct_of_close": {"inputs": ["open", "high", "low", "close"], "func": swk_003_lower_wick_pct_of_close},
    "swk_004_lower_wick_norm_atr21": {"inputs": ["open", "high", "low", "close"], "func": swk_004_lower_wick_norm_atr21},
    "swk_005_lower_wick_sma21": {"inputs": ["open", "high", "low", "close"], "func": swk_005_lower_wick_sma21},
    "swk_006_lower_wick_sma63": {"inputs": ["open", "high", "low", "close"], "func": swk_006_lower_wick_sma63},
    "swk_007_lower_wick_ratio_sma21": {"inputs": ["open", "high", "low", "close"], "func": swk_007_lower_wick_ratio_sma21},
    "swk_008_lower_wick_ratio_sma63": {"inputs": ["open", "high", "low", "close"], "func": swk_008_lower_wick_ratio_sma63},
    "swk_009_lower_wick_ratio_sma252": {"inputs": ["open", "high", "low", "close"], "func": swk_009_lower_wick_ratio_sma252},
    "swk_010_lower_wick_max_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_010_lower_wick_max_21d},
    "swk_011_lower_wick_max_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_011_lower_wick_max_63d},
    "swk_012_lower_wick_max_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_012_lower_wick_max_252d},
    "swk_013_lower_wick_ratio_max_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_013_lower_wick_ratio_max_21d},
    "swk_014_lower_wick_ratio_max_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_014_lower_wick_ratio_max_63d},
    "swk_015_lower_wick_ratio_max_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_015_lower_wick_ratio_max_252d},
    "swk_016_upper_wick_abs": {"inputs": ["open", "high", "low", "close"], "func": swk_016_upper_wick_abs},
    "swk_017_upper_wick_ratio": {"inputs": ["open", "high", "low", "close"], "func": swk_017_upper_wick_ratio},
    "swk_018_upper_wick_pct_of_close": {"inputs": ["open", "high", "low", "close"], "func": swk_018_upper_wick_pct_of_close},
    "swk_019_upper_wick_norm_atr21": {"inputs": ["open", "high", "low", "close"], "func": swk_019_upper_wick_norm_atr21},
    "swk_020_upper_wick_sma21": {"inputs": ["open", "high", "low", "close"], "func": swk_020_upper_wick_sma21},
    "swk_021_upper_wick_sma63": {"inputs": ["open", "high", "low", "close"], "func": swk_021_upper_wick_sma63},
    "swk_022_upper_wick_ratio_sma21": {"inputs": ["open", "high", "low", "close"], "func": swk_022_upper_wick_ratio_sma21},
    "swk_023_upper_wick_ratio_sma63": {"inputs": ["open", "high", "low", "close"], "func": swk_023_upper_wick_ratio_sma63},
    "swk_024_upper_wick_ratio_sma252": {"inputs": ["open", "high", "low", "close"], "func": swk_024_upper_wick_ratio_sma252},
    "swk_025_upper_wick_max_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_025_upper_wick_max_21d},
    "swk_026_upper_wick_max_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_026_upper_wick_max_63d},
    "swk_027_upper_wick_max_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_027_upper_wick_max_252d},
    "swk_028_upper_wick_ratio_max_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_028_upper_wick_ratio_max_21d},
    "swk_029_upper_wick_ratio_max_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_029_upper_wick_ratio_max_63d},
    "swk_030_upper_wick_ratio_max_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_030_upper_wick_ratio_max_252d},
    "swk_031_wick_asymmetry_ratio": {"inputs": ["open", "high", "low", "close"], "func": swk_031_wick_asymmetry_ratio},
    "swk_032_wick_asymmetry_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_032_wick_asymmetry_diff},
    "swk_033_wick_asymmetry_diff_norm_range": {"inputs": ["open", "high", "low", "close"], "func": swk_033_wick_asymmetry_diff_norm_range},
    "swk_034_wick_asymmetry_ratio_sma21": {"inputs": ["open", "high", "low", "close"], "func": swk_034_wick_asymmetry_ratio_sma21},
    "swk_035_wick_asymmetry_ratio_sma63": {"inputs": ["open", "high", "low", "close"], "func": swk_035_wick_asymmetry_ratio_sma63},
    "swk_036_wick_asymmetry_ratio_sma252": {"inputs": ["open", "high", "low", "close"], "func": swk_036_wick_asymmetry_ratio_sma252},
    "swk_037_wick_asym_diff_sma21": {"inputs": ["open", "high", "low", "close"], "func": swk_037_wick_asymmetry_diff_sma21},
    "swk_038_wick_asym_diff_sma63": {"inputs": ["open", "high", "low", "close"], "func": swk_038_wick_asymmetry_diff_sma63},
    "swk_039_lower_dominant_flag": {"inputs": ["open", "high", "low", "close"], "func": swk_039_lower_dominant_flag},
    "swk_040_lower_dominant_fraction_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_040_lower_dominant_fraction_21d},
    "swk_041_lower_dominant_fraction_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_041_lower_dominant_fraction_63d},
    "swk_042_lower_dominant_fraction_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_042_lower_dominant_fraction_252d},
    "swk_043_wick_asym_max_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_043_wick_asym_max_21d},
    "swk_044_wick_asym_max_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_044_wick_asym_max_63d},
    "swk_045_wick_asym_norm_diff_sma21": {"inputs": ["open", "high", "low", "close"], "func": swk_045_wick_asym_norm_diff_sma21},
    "swk_046_long_lower_wick_flag_33pct": {"inputs": ["open", "high", "low", "close"], "func": swk_046_long_lower_wick_flag_33pct},
    "swk_047_long_lower_wick_flag_50pct": {"inputs": ["open", "high", "low", "close"], "func": swk_047_long_lower_wick_flag_50pct},
    "swk_048_long_lower_wick_flag_66pct": {"inputs": ["open", "high", "low", "close"], "func": swk_048_long_lower_wick_flag_66pct},
    "swk_049_long_lower_wick_count_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_049_long_lower_wick_count_21d},
    "swk_050_long_lower_wick_count_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_050_long_lower_wick_count_63d},
    "swk_051_long_lower_wick_count_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_051_long_lower_wick_count_252d},
    "swk_052_strong_hammer_count_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_052_strong_hammer_count_21d},
    "swk_053_strong_hammer_count_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_053_strong_hammer_count_63d},
    "swk_054_long_lower_wick_fraction_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_054_long_lower_wick_fraction_21d},
    "swk_055_long_lower_wick_fraction_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_055_long_lower_wick_fraction_63d},
    "swk_056_long_lower_wick_fraction_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_056_long_lower_wick_fraction_252d},
    "swk_057_consec_long_lower_wick": {"inputs": ["open", "high", "low", "close"], "func": swk_057_consec_long_lower_wick},
    "swk_058_max_consec_long_lower_wick_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_058_max_consec_long_lower_wick_63d},
    "swk_059_max_consec_long_lower_wick_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_059_max_consec_long_lower_wick_252d},
    "swk_060_long_lower_wick_ewm21": {"inputs": ["open", "high", "low", "close"], "func": swk_060_long_lower_wick_ewm21},
    "swk_061_lower_wick_ratio_pct_rank_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_061_lower_wick_ratio_pct_rank_63d},
    "swk_062_lower_wick_ratio_pct_rank_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_062_lower_wick_ratio_pct_rank_252d},
    "swk_063_upper_wick_ratio_pct_rank_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_063_upper_wick_ratio_pct_rank_63d},
    "swk_064_upper_wick_ratio_pct_rank_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_064_upper_wick_ratio_pct_rank_252d},
    "swk_065_lower_wick_ratio_zscore_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_065_lower_wick_ratio_zscore_63d},
    "swk_066_lower_wick_ratio_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_066_lower_wick_ratio_zscore_252d},
    "swk_067_upper_wick_ratio_zscore_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_067_upper_wick_ratio_zscore_63d},
    "swk_068_upper_wick_ratio_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_068_upper_wick_ratio_zscore_252d},
    "swk_069_wick_asym_zscore_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_069_wick_asym_zscore_63d},
    "swk_070_wick_asym_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_070_wick_asym_zscore_252d},
    "swk_071_lower_wick_ratio_expanding_rank": {"inputs": ["open", "high", "low", "close"], "func": swk_071_lower_wick_ratio_expanding_rank},
    "swk_072_lower_wick_ratio_expanding_zscore": {"inputs": ["open", "high", "low", "close"], "func": swk_072_lower_wick_ratio_expanding_zscore},
    "swk_073_lower_wick_abs_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_073_lower_wick_abs_zscore_252d},
    "swk_074_lower_wick_ratio_median_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_074_lower_wick_ratio_median_21d},
    "swk_075_lower_wick_ratio_above_median_flag": {"inputs": ["open", "high", "low", "close"], "func": swk_075_lower_wick_ratio_above_median_flag},
}
