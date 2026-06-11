"""
55_price_level_distress — Base Features 001-075
Domain: absolute price level distress — sub-$1/$5 penny-stock flags, nominal dollar price
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

# Penny-stock / delisting threshold levels (USD)
_LVL_1  = 1.0
_LVL_2  = 2.0
_LVL_3  = 3.0
_LVL_5  = 5.0
_LVL_10 = 10.0

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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """
    Count consecutive True values up to each row (backward-looking).
    Uses cumsum-group trick: each time cond is False, the group counter increments.
    Returns 0 on False rows and the current streak length on True rows.
    """
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods (scalar apply)."""
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Absolute close level and log-price level ---

def pld_001_close_level(close: pd.Series) -> pd.Series:
    """Raw nominal closing price (absolute dollar level)."""
    return close.astype(float)


def pld_002_log_close_level(close: pd.Series) -> pd.Series:
    """Natural log of the nominal closing price."""
    return _log_safe(close)


def pld_003_close_level_norm_252d_mean(close: pd.Series) -> pd.Series:
    """Close normalized by its trailing 252-day mean (how low vs recent history)."""
    return _safe_div(close, _rolling_mean(close, _TD_YEAR))


def pld_004_close_level_norm_63d_mean(close: pd.Series) -> pd.Series:
    """Close normalized by its trailing 63-day mean."""
    return _safe_div(close, _rolling_mean(close, _TD_QTR))


def pld_005_close_level_norm_21d_mean(close: pd.Series) -> pd.Series:
    """Close normalized by its trailing 21-day mean."""
    return _safe_div(close, _rolling_mean(close, _TD_MON))


def pld_006_close_level_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of today's close within trailing 252-day price distribution."""
    return close.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def pld_007_close_level_pct_rank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of today's close within trailing 63-day price distribution."""
    return close.rolling(_TD_QTR, min_periods=_TD_MON).rank(pct=True)


def pld_008_close_level_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of nominal close relative to 252-day rolling mean and std."""
    m = _rolling_mean(close, _TD_YEAR)
    s = _rolling_std(close, _TD_YEAR)
    return _safe_div(close - m, s)


def pld_009_close_level_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of the nominal close price."""
    return close.expanding(min_periods=1).rank(pct=True)


def pld_010_close_below_5d_sma_ratio(close: pd.Series) -> pd.Series:
    """Close divided by its 5-day SMA (how far below short-term average)."""
    return _safe_div(close, _rolling_mean(close, _TD_WEEK))


# --- Group B (011-020): Sub-threshold binary flags ($1 / $2 / $3 / $5 / $10) ---

def pld_011_below_1_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is below $1 (active NYSE delisting threshold)."""
    return (close < _LVL_1).astype(float)


def pld_012_below_2_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is below $2."""
    return (close < _LVL_2).astype(float)


def pld_013_below_3_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is below $3."""
    return (close < _LVL_3).astype(float)


def pld_014_below_5_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is below $5 (standard penny-stock definition)."""
    return (close < _LVL_5).astype(float)


def pld_015_below_10_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is below $10 (micro-cap distress zone)."""
    return (close < _LVL_10).astype(float)


def pld_016_above_1_below_5_flag(close: pd.Series) -> pd.Series:
    """Flag: close is in the [$1, $5) penny-stock band."""
    return ((close >= _LVL_1) & (close < _LVL_5)).astype(float)


def pld_017_above_1_below_2_flag(close: pd.Series) -> pd.Series:
    """Flag: close is in the [$1, $2) near-delisting band."""
    return ((close >= _LVL_1) & (close < _LVL_2)).astype(float)


def pld_018_above_2_below_5_flag(close: pd.Series) -> pd.Series:
    """Flag: close is in the [$2, $5) deep penny-stock band."""
    return ((close >= _LVL_2) & (close < _LVL_5)).astype(float)


def pld_019_above_5_below_10_flag(close: pd.Series) -> pd.Series:
    """Flag: close is in the [$5, $10) low-price distress zone."""
    return ((close >= _LVL_5) & (close < _LVL_10)).astype(float)


def pld_020_low_below_1_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: intraday low touched below $1 even if close recovered."""
    return (low < _LVL_1).astype(float)


# --- Group C (021-030): Distance to the $1 delisting line ---

def pld_021_dist_to_1_abs(close: pd.Series) -> pd.Series:
    """Absolute distance from close to $1 (negative = already below $1)."""
    return close - _LVL_1


def pld_022_dist_to_1_pct(close: pd.Series) -> pd.Series:
    """Percentage distance from close to $1 ((close-1)/close)."""
    return _safe_div(close - _LVL_1, close)


def pld_023_dist_to_5_abs(close: pd.Series) -> pd.Series:
    """Absolute distance from close to $5 (negative = below $5)."""
    return close - _LVL_5


def pld_024_dist_to_5_pct(close: pd.Series) -> pd.Series:
    """Percentage distance from close to $5."""
    return _safe_div(close - _LVL_5, close)


def pld_025_dist_to_2_abs(close: pd.Series) -> pd.Series:
    """Absolute distance from close to $2."""
    return close - _LVL_2


def pld_026_dist_to_10_abs(close: pd.Series) -> pd.Series:
    """Absolute distance from close to $10."""
    return close - _LVL_10


def pld_027_dist_to_1_log(close: pd.Series) -> pd.Series:
    """Log-distance to $1: log(close) - log(1) = log(close), a signed level signal."""
    return _log_safe(close)


def pld_028_dist_to_5_log(close: pd.Series) -> pd.Series:
    """Log-distance to $5: log(close/5), negative when below $5."""
    return np.log(close.clip(lower=_EPS) / _LVL_5)


def pld_029_dist_to_1_norm_by_252d_std(close: pd.Series) -> pd.Series:
    """Distance to $1 normalized by 252-day price std (how many sigmas above $1)."""
    return _safe_div(close - _LVL_1, _rolling_std(close, _TD_YEAR))


def pld_030_dist_to_5_norm_by_252d_std(close: pd.Series) -> pd.Series:
    """Distance to $5 normalized by 252-day price std."""
    return _safe_div(close - _LVL_5, _rolling_std(close, _TD_YEAR))


# --- Group D (031-040): Days spent below each threshold (rolling counts) ---

def pld_031_days_below_1_21d(close: pd.Series) -> pd.Series:
    """Count of trading days with close < $1 in the past 21 days."""
    return _rolling_count_true(close < _LVL_1, _TD_MON)


def pld_032_days_below_1_63d(close: pd.Series) -> pd.Series:
    """Count of trading days with close < $1 in the past 63 days."""
    return _rolling_count_true(close < _LVL_1, _TD_QTR)


def pld_033_days_below_1_252d(close: pd.Series) -> pd.Series:
    """Count of trading days with close < $1 in the past 252 days."""
    return _rolling_count_true(close < _LVL_1, _TD_YEAR)


def pld_034_days_below_5_21d(close: pd.Series) -> pd.Series:
    """Count of trading days with close < $5 in the past 21 days."""
    return _rolling_count_true(close < _LVL_5, _TD_MON)


def pld_035_days_below_5_63d(close: pd.Series) -> pd.Series:
    """Count of trading days with close < $5 in the past 63 days."""
    return _rolling_count_true(close < _LVL_5, _TD_QTR)


def pld_036_days_below_5_252d(close: pd.Series) -> pd.Series:
    """Count of trading days with close < $5 in the past 252 days."""
    return _rolling_count_true(close < _LVL_5, _TD_YEAR)


def pld_037_days_below_2_63d(close: pd.Series) -> pd.Series:
    """Count of trading days with close < $2 in the past 63 days."""
    return _rolling_count_true(close < _LVL_2, _TD_QTR)


def pld_038_days_below_10_63d(close: pd.Series) -> pd.Series:
    """Count of trading days with close < $10 in the past 63 days."""
    return _rolling_count_true(close < _LVL_10, _TD_QTR)


def pld_039_frac_days_below_5_63d(close: pd.Series) -> pd.Series:
    """Fraction of past 63 days where close was below $5."""
    return _rolling_count_true(close < _LVL_5, _TD_QTR) / _TD_QTR


def pld_040_frac_days_below_5_252d(close: pd.Series) -> pd.Series:
    """Fraction of past 252 days where close was below $5."""
    return _rolling_count_true(close < _LVL_5, _TD_YEAR) / _TD_YEAR


# --- Group E (041-050): Consecutive days below each price threshold ---

def pld_041_consec_days_below_1(close: pd.Series) -> pd.Series:
    """Current consecutive days with close continuously below $1."""
    return _consec_streak(close < _LVL_1)


def pld_042_consec_days_below_2(close: pd.Series) -> pd.Series:
    """Current consecutive days with close continuously below $2."""
    return _consec_streak(close < _LVL_2)


def pld_043_consec_days_below_3(close: pd.Series) -> pd.Series:
    """Current consecutive days with close continuously below $3."""
    return _consec_streak(close < _LVL_3)


def pld_044_consec_days_below_5(close: pd.Series) -> pd.Series:
    """Current consecutive days with close continuously below $5."""
    return _consec_streak(close < _LVL_5)


def pld_045_consec_days_below_10(close: pd.Series) -> pd.Series:
    """Current consecutive days with close continuously below $10."""
    return _consec_streak(close < _LVL_10)


def pld_046_consec_days_below_5_log1p(close: pd.Series) -> pd.Series:
    """Log1p of consecutive days below $5 (compresses long tails)."""
    return np.log1p(pld_044_consec_days_below_5(close))


def pld_047_max_consec_days_below_5_63d(close: pd.Series) -> pd.Series:
    """Maximum consecutive days below $5 within trailing 63-day window."""
    return _rolling_max_streak(close < _LVL_5, _TD_QTR)


def pld_048_max_consec_days_below_5_252d(close: pd.Series) -> pd.Series:
    """Maximum consecutive days below $5 within trailing 252-day window."""
    return _rolling_max_streak(close < _LVL_5, _TD_YEAR)


def pld_049_max_consec_days_below_1_252d(close: pd.Series) -> pd.Series:
    """Maximum consecutive days below $1 within trailing 252-day window."""
    return _rolling_max_streak(close < _LVL_1, _TD_YEAR)


def pld_050_consec_days_below_5_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of consecutive-below-$5 streak within trailing 252-day series."""
    streak = pld_044_consec_days_below_5(close)
    return streak.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group F (051-060): Trailing minimum nominal price ---

def pld_051_trailing_min_21d(close: pd.Series) -> pd.Series:
    """Trailing 21-day minimum nominal closing price."""
    return _rolling_min(close, _TD_MON)


def pld_052_trailing_min_63d(close: pd.Series) -> pd.Series:
    """Trailing 63-day minimum nominal closing price."""
    return _rolling_min(close, _TD_QTR)


def pld_053_trailing_min_126d(close: pd.Series) -> pd.Series:
    """Trailing 126-day minimum nominal closing price."""
    return _rolling_min(close, _TD_HALF)


def pld_054_trailing_min_252d(close: pd.Series) -> pd.Series:
    """Trailing 252-day minimum nominal closing price."""
    return _rolling_min(close, _TD_YEAR)


def pld_055_trailing_min_504d(close: pd.Series) -> pd.Series:
    """Trailing 504-day minimum nominal closing price (2-year all-time low proxy)."""
    return _rolling_min(close, 504)


def pld_056_close_vs_min21_ratio(close: pd.Series) -> pd.Series:
    """Ratio of current close to its 21-day trailing minimum."""
    return _safe_div(close, _rolling_min(close, _TD_MON))


def pld_057_close_vs_min63_ratio(close: pd.Series) -> pd.Series:
    """Ratio of current close to its 63-day trailing minimum."""
    return _safe_div(close, _rolling_min(close, _TD_QTR))


def pld_058_close_vs_min252_ratio(close: pd.Series) -> pd.Series:
    """Ratio of current close to its 252-day trailing minimum."""
    return _safe_div(close, _rolling_min(close, _TD_YEAR))


def pld_059_log_trailing_min_252d(close: pd.Series) -> pd.Series:
    """Natural log of the 252-day trailing minimum price."""
    return _log_safe(_rolling_min(close, _TD_YEAR))


def pld_060_expanding_min_price(close: pd.Series) -> pd.Series:
    """Expanding all-history minimum nominal closing price."""
    return close.expanding(min_periods=1).min()


# --- Group G (061-075): Depth below $5, crossing events, regime persistence ---

def pld_061_depth_below_5(close: pd.Series) -> pd.Series:
    """Dollar amount by which close is below $5 (zero when at or above $5)."""
    return (_LVL_5 - close).clip(lower=0.0)


def pld_062_depth_below_1(close: pd.Series) -> pd.Series:
    """Dollar amount by which close is below $1 (zero when at or above $1)."""
    return (_LVL_1 - close).clip(lower=0.0)


def pld_063_depth_below_2(close: pd.Series) -> pd.Series:
    """Dollar amount by which close is below $2 (zero when at or above $2)."""
    return (_LVL_2 - close).clip(lower=0.0)


def pld_064_depth_below_10(close: pd.Series) -> pd.Series:
    """Dollar amount by which close is below $10 (zero when at or above $10)."""
    return (_LVL_10 - close).clip(lower=0.0)


def pld_065_depth_below_5_pct_of_5(close: pd.Series) -> pd.Series:
    """Depth below $5 as a fraction of $5 (0 to 1 scale when under $5)."""
    return ((_LVL_5 - close) / _LVL_5).clip(lower=0.0)


def pld_066_depth_below_1_pct_of_1(close: pd.Series) -> pd.Series:
    """Depth below $1 as a fraction of $1."""
    return ((_LVL_1 - close) / _LVL_1).clip(lower=0.0)


def pld_067_cross_below_5_event(close: pd.Series) -> pd.Series:
    """Binary flag: today close crossed below $5 (was >= $5 yesterday, < $5 today)."""
    was_above = close.shift(1) >= _LVL_5
    is_below = close < _LVL_5
    return (was_above & is_below).astype(float)


def pld_068_cross_below_1_event(close: pd.Series) -> pd.Series:
    """Binary flag: today close crossed below $1."""
    was_above = close.shift(1) >= _LVL_1
    is_below = close < _LVL_1
    return (was_above & is_below).astype(float)


def pld_069_cross_below_2_event(close: pd.Series) -> pd.Series:
    """Binary flag: today close crossed below $2."""
    was_above = close.shift(1) >= _LVL_2
    is_below = close < _LVL_2
    return (was_above & is_below).astype(float)


def pld_070_cross_below_10_event(close: pd.Series) -> pd.Series:
    """Binary flag: today close crossed below $10."""
    was_above = close.shift(1) >= _LVL_10
    is_below = close < _LVL_10
    return (was_above & is_below).astype(float)


def pld_071_cross_below_5_count_63d(close: pd.Series) -> pd.Series:
    """Count of $5 cross-below events in the trailing 63 days."""
    events = pld_067_cross_below_5_event(close)
    return _rolling_sum(events, _TD_QTR)


def pld_072_cross_below_5_count_252d(close: pd.Series) -> pd.Series:
    """Count of $5 cross-below events in the trailing 252 days."""
    events = pld_067_cross_below_5_event(close)
    return _rolling_sum(events, _TD_YEAR)


def pld_073_penny_regime_persistence_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days spent below $1 (penny-stock regime persistence)."""
    return _rolling_count_true(close < _LVL_1, _TD_QTR) / _TD_QTR


def pld_074_penny_regime_persistence_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days spent below $1 (annual penny-stock persistence)."""
    return _rolling_count_true(close < _LVL_1, _TD_YEAR) / _TD_YEAR


def pld_075_sub5_regime_persistence_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days spent below $5 (annual sub-$5 persistence)."""
    return _rolling_count_true(close < _LVL_5, _TD_YEAR) / _TD_YEAR


# ── Registry ──────────────────────────────────────────────────────────────────

PRICE_LEVEL_DISTRESS_REGISTRY_001_075 = {
    "pld_001_close_level": {"inputs": ["close"], "func": pld_001_close_level},
    "pld_002_log_close_level": {"inputs": ["close"], "func": pld_002_log_close_level},
    "pld_003_close_level_norm_252d_mean": {"inputs": ["close"], "func": pld_003_close_level_norm_252d_mean},
    "pld_004_close_level_norm_63d_mean": {"inputs": ["close"], "func": pld_004_close_level_norm_63d_mean},
    "pld_005_close_level_norm_21d_mean": {"inputs": ["close"], "func": pld_005_close_level_norm_21d_mean},
    "pld_006_close_level_pct_rank_252d": {"inputs": ["close"], "func": pld_006_close_level_pct_rank_252d},
    "pld_007_close_level_pct_rank_63d": {"inputs": ["close"], "func": pld_007_close_level_pct_rank_63d},
    "pld_008_close_level_zscore_252d": {"inputs": ["close"], "func": pld_008_close_level_zscore_252d},
    "pld_009_close_level_expanding_pct_rank": {"inputs": ["close"], "func": pld_009_close_level_expanding_pct_rank},
    "pld_010_close_below_5d_sma_ratio": {"inputs": ["close"], "func": pld_010_close_below_5d_sma_ratio},
    "pld_011_below_1_flag": {"inputs": ["close"], "func": pld_011_below_1_flag},
    "pld_012_below_2_flag": {"inputs": ["close"], "func": pld_012_below_2_flag},
    "pld_013_below_3_flag": {"inputs": ["close"], "func": pld_013_below_3_flag},
    "pld_014_below_5_flag": {"inputs": ["close"], "func": pld_014_below_5_flag},
    "pld_015_below_10_flag": {"inputs": ["close"], "func": pld_015_below_10_flag},
    "pld_016_above_1_below_5_flag": {"inputs": ["close"], "func": pld_016_above_1_below_5_flag},
    "pld_017_above_1_below_2_flag": {"inputs": ["close"], "func": pld_017_above_1_below_2_flag},
    "pld_018_above_2_below_5_flag": {"inputs": ["close"], "func": pld_018_above_2_below_5_flag},
    "pld_019_above_5_below_10_flag": {"inputs": ["close"], "func": pld_019_above_5_below_10_flag},
    "pld_020_low_below_1_flag": {"inputs": ["close", "low"], "func": pld_020_low_below_1_flag},
    "pld_021_dist_to_1_abs": {"inputs": ["close"], "func": pld_021_dist_to_1_abs},
    "pld_022_dist_to_1_pct": {"inputs": ["close"], "func": pld_022_dist_to_1_pct},
    "pld_023_dist_to_5_abs": {"inputs": ["close"], "func": pld_023_dist_to_5_abs},
    "pld_024_dist_to_5_pct": {"inputs": ["close"], "func": pld_024_dist_to_5_pct},
    "pld_025_dist_to_2_abs": {"inputs": ["close"], "func": pld_025_dist_to_2_abs},
    "pld_026_dist_to_10_abs": {"inputs": ["close"], "func": pld_026_dist_to_10_abs},
    "pld_027_dist_to_1_log": {"inputs": ["close"], "func": pld_027_dist_to_1_log},
    "pld_028_dist_to_5_log": {"inputs": ["close"], "func": pld_028_dist_to_5_log},
    "pld_029_dist_to_1_norm_by_252d_std": {"inputs": ["close"], "func": pld_029_dist_to_1_norm_by_252d_std},
    "pld_030_dist_to_5_norm_by_252d_std": {"inputs": ["close"], "func": pld_030_dist_to_5_norm_by_252d_std},
    "pld_031_days_below_1_21d": {"inputs": ["close"], "func": pld_031_days_below_1_21d},
    "pld_032_days_below_1_63d": {"inputs": ["close"], "func": pld_032_days_below_1_63d},
    "pld_033_days_below_1_252d": {"inputs": ["close"], "func": pld_033_days_below_1_252d},
    "pld_034_days_below_5_21d": {"inputs": ["close"], "func": pld_034_days_below_5_21d},
    "pld_035_days_below_5_63d": {"inputs": ["close"], "func": pld_035_days_below_5_63d},
    "pld_036_days_below_5_252d": {"inputs": ["close"], "func": pld_036_days_below_5_252d},
    "pld_037_days_below_2_63d": {"inputs": ["close"], "func": pld_037_days_below_2_63d},
    "pld_038_days_below_10_63d": {"inputs": ["close"], "func": pld_038_days_below_10_63d},
    "pld_039_frac_days_below_5_63d": {"inputs": ["close"], "func": pld_039_frac_days_below_5_63d},
    "pld_040_frac_days_below_5_252d": {"inputs": ["close"], "func": pld_040_frac_days_below_5_252d},
    "pld_041_consec_days_below_1": {"inputs": ["close"], "func": pld_041_consec_days_below_1},
    "pld_042_consec_days_below_2": {"inputs": ["close"], "func": pld_042_consec_days_below_2},
    "pld_043_consec_days_below_3": {"inputs": ["close"], "func": pld_043_consec_days_below_3},
    "pld_044_consec_days_below_5": {"inputs": ["close"], "func": pld_044_consec_days_below_5},
    "pld_045_consec_days_below_10": {"inputs": ["close"], "func": pld_045_consec_days_below_10},
    "pld_046_consec_days_below_5_log1p": {"inputs": ["close"], "func": pld_046_consec_days_below_5_log1p},
    "pld_047_max_consec_days_below_5_63d": {"inputs": ["close"], "func": pld_047_max_consec_days_below_5_63d},
    "pld_048_max_consec_days_below_5_252d": {"inputs": ["close"], "func": pld_048_max_consec_days_below_5_252d},
    "pld_049_max_consec_days_below_1_252d": {"inputs": ["close"], "func": pld_049_max_consec_days_below_1_252d},
    "pld_050_consec_days_below_5_pct_rank_252d": {"inputs": ["close"], "func": pld_050_consec_days_below_5_pct_rank_252d},
    "pld_051_trailing_min_21d": {"inputs": ["close"], "func": pld_051_trailing_min_21d},
    "pld_052_trailing_min_63d": {"inputs": ["close"], "func": pld_052_trailing_min_63d},
    "pld_053_trailing_min_126d": {"inputs": ["close"], "func": pld_053_trailing_min_126d},
    "pld_054_trailing_min_252d": {"inputs": ["close"], "func": pld_054_trailing_min_252d},
    "pld_055_trailing_min_504d": {"inputs": ["close"], "func": pld_055_trailing_min_504d},
    "pld_056_close_vs_min21_ratio": {"inputs": ["close"], "func": pld_056_close_vs_min21_ratio},
    "pld_057_close_vs_min63_ratio": {"inputs": ["close"], "func": pld_057_close_vs_min63_ratio},
    "pld_058_close_vs_min252_ratio": {"inputs": ["close"], "func": pld_058_close_vs_min252_ratio},
    "pld_059_log_trailing_min_252d": {"inputs": ["close"], "func": pld_059_log_trailing_min_252d},
    "pld_060_expanding_min_price": {"inputs": ["close"], "func": pld_060_expanding_min_price},
    "pld_061_depth_below_5": {"inputs": ["close"], "func": pld_061_depth_below_5},
    "pld_062_depth_below_1": {"inputs": ["close"], "func": pld_062_depth_below_1},
    "pld_063_depth_below_2": {"inputs": ["close"], "func": pld_063_depth_below_2},
    "pld_064_depth_below_10": {"inputs": ["close"], "func": pld_064_depth_below_10},
    "pld_065_depth_below_5_pct_of_5": {"inputs": ["close"], "func": pld_065_depth_below_5_pct_of_5},
    "pld_066_depth_below_1_pct_of_1": {"inputs": ["close"], "func": pld_066_depth_below_1_pct_of_1},
    "pld_067_cross_below_5_event": {"inputs": ["close"], "func": pld_067_cross_below_5_event},
    "pld_068_cross_below_1_event": {"inputs": ["close"], "func": pld_068_cross_below_1_event},
    "pld_069_cross_below_2_event": {"inputs": ["close"], "func": pld_069_cross_below_2_event},
    "pld_070_cross_below_10_event": {"inputs": ["close"], "func": pld_070_cross_below_10_event},
    "pld_071_cross_below_5_count_63d": {"inputs": ["close"], "func": pld_071_cross_below_5_count_63d},
    "pld_072_cross_below_5_count_252d": {"inputs": ["close"], "func": pld_072_cross_below_5_count_252d},
    "pld_073_penny_regime_persistence_63d": {"inputs": ["close"], "func": pld_073_penny_regime_persistence_63d},
    "pld_074_penny_regime_persistence_252d": {"inputs": ["close"], "func": pld_074_penny_regime_persistence_252d},
    "pld_075_sub5_regime_persistence_252d": {"inputs": ["close"], "func": pld_075_sub5_regime_persistence_252d},
}
