"""
117_price_clustering_psychology — Base Features 001-075
Domain: price-level psychology and digit clustering — proximity to and clustering at round
        numbers (whole dollars, $5/$10 increments), trailing-digit preference, behaviour and
        pinning near psychological round levels, absolute price-level distress zones (sub-$5,
        sub-$1 penny-stock thresholds), fraction of recent closes at round levels, distance to
        the nearest round number.
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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _dist_to_round(price: pd.Series, increment: float) -> pd.Series:
    """Absolute distance from price to the nearest multiple of increment."""
    mod = price % increment
    down = mod
    up = increment - mod
    return np.minimum(down, up)


def _frac_near_round(price: pd.Series, increment: float, tol: float,
                     window: int) -> pd.Series:
    """Rolling fraction of bars where close is within tol of a round increment."""
    near = (_dist_to_round(price, increment) <= tol).astype(float)
    return _rolling_sum(near, window) / window


def _trailing_digit(price: pd.Series, base: float) -> pd.Series:
    """Trailing digit of price modulo base (e.g. cents digit for base=1.0)."""
    return price % base


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Distance to nearest whole-dollar round number ---

def pcp_001_dist_to_nearest_dollar(close: pd.Series) -> pd.Series:
    """Absolute distance from close to nearest whole-dollar level."""
    return _dist_to_round(close, 1.0)


def pcp_002_dist_to_nearest_dollar_pct(close: pd.Series) -> pd.Series:
    """Distance to nearest whole dollar as fraction of price (0–0.5/price)."""
    return _safe_div(_dist_to_round(close, 1.0), close.clip(lower=_EPS))


def pcp_003_dist_to_nearest_5dollar(close: pd.Series) -> pd.Series:
    """Absolute distance from close to nearest $5 round level."""
    return _dist_to_round(close, 5.0)


def pcp_004_dist_to_nearest_5dollar_pct(close: pd.Series) -> pd.Series:
    """$5-level distance as fraction of price."""
    return _safe_div(_dist_to_round(close, 5.0), close.clip(lower=_EPS))


def pcp_005_dist_to_nearest_10dollar(close: pd.Series) -> pd.Series:
    """Absolute distance from close to nearest $10 round level."""
    return _dist_to_round(close, 10.0)


def pcp_006_dist_to_nearest_10dollar_pct(close: pd.Series) -> pd.Series:
    """$10-level distance as fraction of price."""
    return _safe_div(_dist_to_round(close, 10.0), close.clip(lower=_EPS))


def pcp_007_dist_to_nearest_25dollar(close: pd.Series) -> pd.Series:
    """Absolute distance from close to nearest $25 round level."""
    return _dist_to_round(close, 25.0)


def pcp_008_dist_to_nearest_25dollar_pct(close: pd.Series) -> pd.Series:
    """$25-level distance as fraction of price."""
    return _safe_div(_dist_to_round(close, 25.0), close.clip(lower=_EPS))


def pcp_009_dist_to_nearest_50dollar(close: pd.Series) -> pd.Series:
    """Absolute distance from close to nearest $50 round level."""
    return _dist_to_round(close, 50.0)


def pcp_010_dist_to_nearest_50dollar_pct(close: pd.Series) -> pd.Series:
    """$50-level distance as fraction of price."""
    return _safe_div(_dist_to_round(close, 50.0), close.clip(lower=_EPS))


# --- Group B (011-020): Binary flags — at round number pinning ---

def pcp_011_at_whole_dollar_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is within $0.05 of a whole-dollar level."""
    return (_dist_to_round(close, 1.0) <= 0.05).astype(float)


def pcp_012_at_5dollar_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is within $0.10 of a $5 level."""
    return (_dist_to_round(close, 5.0) <= 0.10).astype(float)


def pcp_013_at_10dollar_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is within $0.10 of a $10 level."""
    return (_dist_to_round(close, 10.0) <= 0.10).astype(float)


def pcp_014_at_25dollar_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is within $0.25 of a $25 level."""
    return (_dist_to_round(close, 25.0) <= 0.25).astype(float)


def pcp_015_at_50dollar_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is within $0.50 of a $50 level."""
    return (_dist_to_round(close, 50.0) <= 0.50).astype(float)


def pcp_016_at_100dollar_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is within $0.50 of a $100 round level."""
    return (_dist_to_round(close, 100.0) <= 0.50).astype(float)


def pcp_017_at_1dollar_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is within $0.02 of the $1.00 level (penny-stock boundary)."""
    return (close.sub(1.0).abs() <= 0.02).astype(float)


def pcp_018_at_5dollar_exact_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is within $0.05 of the $5.00 level (distress boundary)."""
    return (close.sub(5.0).abs() <= 0.05).astype(float)


def pcp_019_below_round_level_flag(close: pd.Series) -> pd.Series:
    """Binary flag: fractional part of close is in the lower half (below round number)."""
    return (close % 1.0 < 0.50).astype(float)


def pcp_020_above_round_level_flag(close: pd.Series) -> pd.Series:
    """Binary flag: fractional part of close is in the upper half (above round number)."""
    return (close % 1.0 >= 0.50).astype(float)


# --- Group C (021-030): Penny-stock / absolute price-level distress zones ---

def pcp_021_sub1_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close < $1.00 (penny-stock threshold)."""
    return (close < 1.0).astype(float)


def pcp_022_sub2_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close < $2.00 (near-penny distress zone)."""
    return (close < 2.0).astype(float)


def pcp_023_sub5_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close < $5.00 (micro-cap distress threshold)."""
    return (close < 5.0).astype(float)


def pcp_024_sub10_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close < $10.00 (low-priced stock zone)."""
    return (close < 10.0).astype(float)


def pcp_025_depth_below_1dollar(close: pd.Series) -> pd.Series:
    """Depth below $1.00 (0 when above or at $1)."""
    return (1.0 - close).clip(lower=0.0)


def pcp_026_depth_below_5dollar(close: pd.Series) -> pd.Series:
    """Depth below $5.00 (0 when above or at $5)."""
    return (5.0 - close).clip(lower=0.0)


def pcp_027_depth_below_10dollar(close: pd.Series) -> pd.Series:
    """Depth below $10.00 (0 when above or at $10)."""
    return (10.0 - close).clip(lower=0.0)


def pcp_028_consec_days_sub5(close: pd.Series) -> pd.Series:
    """Consecutive days close has been below $5.00."""
    return _consec_streak(close < 5.0)


def pcp_029_consec_days_sub1(close: pd.Series) -> pd.Series:
    """Consecutive days close has been below $1.00."""
    return _consec_streak(close < 1.0)


def pcp_030_fraction_sub5_in_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days where close < $5."""
    return _rolling_sum((close < 5.0).astype(float), _TD_QTR) / _TD_QTR


# --- Group D (031-040): Fraction of closes near round numbers (windows) ---

def pcp_031_frac_near_dollar_21d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days close within $0.05 of a whole dollar."""
    return _frac_near_round(close, 1.0, 0.05, _TD_MON)


def pcp_032_frac_near_dollar_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days close within $0.05 of a whole dollar."""
    return _frac_near_round(close, 1.0, 0.05, _TD_QTR)


def pcp_033_frac_near_5dollar_21d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days close within $0.10 of a $5 level."""
    return _frac_near_round(close, 5.0, 0.10, _TD_MON)


def pcp_034_frac_near_5dollar_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days close within $0.10 of a $5 level."""
    return _frac_near_round(close, 5.0, 0.10, _TD_QTR)


def pcp_035_frac_near_10dollar_21d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days close within $0.10 of a $10 level."""
    return _frac_near_round(close, 10.0, 0.10, _TD_MON)


def pcp_036_frac_near_10dollar_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days close within $0.10 of a $10 level."""
    return _frac_near_round(close, 10.0, 0.10, _TD_QTR)


def pcp_037_frac_near_dollar_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days close within $0.05 of a whole dollar."""
    return _frac_near_round(close, 1.0, 0.05, _TD_YEAR)


def pcp_038_frac_near_5dollar_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days close within $0.10 of a $5 level."""
    return _frac_near_round(close, 5.0, 0.10, _TD_YEAR)


def pcp_039_frac_near_dollar_5d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 5 days close within $0.05 of a whole dollar."""
    return _frac_near_round(close, 1.0, 0.05, _TD_WEEK)


def pcp_040_frac_near_10dollar_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days close within $0.10 of a $10 level."""
    return _frac_near_round(close, 10.0, 0.10, _TD_YEAR)


# --- Group E (041-050): Trailing-digit clustering (digit preference) ---

def pcp_041_cents_digit(close: pd.Series) -> pd.Series:
    """Cents component of close price (price mod $1.00 — trailing-digit proxy)."""
    return close % 1.0


def pcp_042_dime_digit(close: pd.Series) -> pd.Series:
    """Dime digit: cents mod $0.10 (sub-dime clustering)."""
    return close % 0.10


def pcp_043_trailing_digit_zero_flag(close: pd.Series) -> pd.Series:
    """Binary flag: cents component is in [0.00, 0.05) — round-zero pinning."""
    return (close % 1.0 < 0.05).astype(float)


def pcp_044_trailing_digit_50_flag(close: pd.Series) -> pd.Series:
    """Binary flag: cents component is in [0.45, 0.55) — round-50-cent pinning."""
    cents = close % 1.0
    return ((cents >= 0.45) & (cents < 0.55)).astype(float)


def pcp_045_trailing_digit_25_flag(close: pd.Series) -> pd.Series:
    """Binary flag: cents component is in [0.20, 0.30) — quarter-dollar cluster."""
    cents = close % 1.0
    return ((cents >= 0.20) & (cents < 0.30)).astype(float)


def pcp_046_trailing_digit_75_flag(close: pd.Series) -> pd.Series:
    """Binary flag: cents component is in [0.70, 0.80) — 75-cent cluster."""
    cents = close % 1.0
    return ((cents >= 0.70) & (cents < 0.80)).astype(float)


def pcp_047_frac_zero_cents_21d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days where close has cents in [0, 0.05)."""
    flag = (close % 1.0 < 0.05).astype(float)
    return _rolling_sum(flag, _TD_MON) / _TD_MON


def pcp_048_frac_50_cents_21d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days where close has cents in [0.45, 0.55)."""
    cents = close % 1.0
    flag = ((cents >= 0.45) & (cents < 0.55)).astype(float)
    return _rolling_sum(flag, _TD_MON) / _TD_MON


def pcp_049_frac_zero_cents_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days where close has cents in [0, 0.05)."""
    flag = (close % 1.0 < 0.05).astype(float)
    return _rolling_sum(flag, _TD_QTR) / _TD_QTR


def pcp_050_frac_even_dollar_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days where close is within $0.02 of a whole dollar."""
    flag = (_dist_to_round(close, 1.0) <= 0.02).astype(float)
    return _rolling_sum(flag, _TD_QTR) / _TD_QTR


# --- Group F (051-060): Pinning / range compression near round levels ---

def pcp_051_high_low_straddles_dollar_flag(close: pd.Series, high: pd.Series,
                                            low: pd.Series) -> pd.Series:
    """Binary flag: the day's high-low range straddles a whole-dollar level."""
    nearest_lo = (low / 1.0).apply(np.floor) * 1.0
    nearest_hi = (low / 1.0).apply(np.floor) * 1.0 + 1.0
    return (high >= nearest_hi).astype(float)


def pcp_052_range_within_dollar_pct(close: pd.Series, high: pd.Series,
                                     low: pd.Series) -> pd.Series:
    """Daily H-L range as fraction of the whole-dollar unit (pinning proxy)."""
    rng = (high - low).clip(lower=0.0)
    return _safe_div(rng, close.clip(lower=_EPS))


def pcp_053_close_vs_nearest_dollar_below(close: pd.Series) -> pd.Series:
    """How far close is above the floor whole-dollar (0 = just above round number)."""
    return close % 1.0


def pcp_054_close_vs_nearest_dollar_above(close: pd.Series) -> pd.Series:
    """How far close is below the ceiling whole-dollar (0 = just below round number)."""
    return 1.0 - (close % 1.0)


def pcp_055_close_pct_thru_5dollar_zone(close: pd.Series) -> pd.Series:
    """Position of close within the current $5 zone (0=floor, 1=ceiling)."""
    return _safe_div(close % 5.0, pd.Series(5.0, index=close.index))


def pcp_056_close_pct_thru_10dollar_zone(close: pd.Series) -> pd.Series:
    """Position of close within the current $10 zone (0=floor, 1=ceiling)."""
    return _safe_div(close % 10.0, pd.Series(10.0, index=close.index))


def pcp_057_rolling_dist_dollar_mean_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day mean of absolute distance to nearest whole dollar."""
    return _rolling_mean(_dist_to_round(close, 1.0), _TD_MON)


def pcp_058_rolling_dist_dollar_std_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day std dev of distance to nearest whole dollar."""
    return _rolling_std(_dist_to_round(close, 1.0), _TD_MON)


def pcp_059_rolling_dist_5dollar_mean_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day mean of distance to nearest $5 level."""
    return _rolling_mean(_dist_to_round(close, 5.0), _TD_MON)


def pcp_060_rolling_dist_10dollar_mean_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day mean of distance to nearest $10 level."""
    return _rolling_mean(_dist_to_round(close, 10.0), _TD_MON)


# --- Group G (061-075): Price-level absolute distress — sub-zone dynamics ---

def pcp_061_fraction_sub1_in_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where close < $1."""
    return _rolling_sum((close < 1.0).astype(float), _TD_YEAR) / _TD_YEAR


def pcp_062_fraction_sub2_in_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where close < $2."""
    return _rolling_sum((close < 2.0).astype(float), _TD_YEAR) / _TD_YEAR


def pcp_063_fraction_sub5_in_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where close < $5."""
    return _rolling_sum((close < 5.0).astype(float), _TD_YEAR) / _TD_YEAR


def pcp_064_fraction_sub10_in_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where close < $10."""
    return _rolling_sum((close < 10.0).astype(float), _TD_YEAR) / _TD_YEAR


def pcp_065_time_since_last_above_5dollar(close: pd.Series) -> pd.Series:
    """Days since close last closed at or above $5 (0 = currently above)."""
    above = (close >= 5.0).astype(float)
    idx = pd.Series(range(len(close)), index=close.index, dtype=float)
    last_idx = idx.where(above == 1.0).ffill().fillna(0.0)
    return (idx - last_idx).where(~close.isna(), np.nan)


def pcp_066_time_since_last_above_10dollar(close: pd.Series) -> pd.Series:
    """Days since close last closed at or above $10."""
    above = (close >= 10.0).astype(float)
    idx = pd.Series(range(len(close)), index=close.index, dtype=float)
    last_idx = idx.where(above == 1.0).ffill().fillna(0.0)
    return (idx - last_idx).where(~close.isna(), np.nan)


def pcp_067_time_since_last_above_1dollar(close: pd.Series) -> pd.Series:
    """Days since close last closed at or above $1."""
    above = (close >= 1.0).astype(float)
    idx = pd.Series(range(len(close)), index=close.index, dtype=float)
    last_idx = idx.where(above == 1.0).ffill().fillna(0.0)
    return (idx - last_idx).where(~close.isna(), np.nan)


def pcp_068_close_level_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of close vs its 252-day distribution (absolute level context)."""
    m = _rolling_mean(close, _TD_YEAR)
    s = _rolling_std(close, _TD_YEAR)
    return _safe_div(close - m, s)


def pcp_069_close_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of close within trailing 252-day distribution."""
    return close.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def pcp_070_close_pct_rank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of close within trailing 63-day distribution."""
    return close.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def pcp_071_close_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of close (1 = highest ever, 0 = lowest)."""
    return close.expanding(min_periods=1).rank(pct=True)


def pcp_072_price_in_sub5_zone_depth_pct(close: pd.Series) -> pd.Series:
    """When below $5, depth as pct of $5; else 0. Captures severity in distress zone."""
    depth = (5.0 - close).clip(lower=0.0)
    return _safe_div(depth, pd.Series(5.0, index=close.index))


def pcp_073_consec_days_sub10(close: pd.Series) -> pd.Series:
    """Consecutive days close has been below $10.00."""
    return _consec_streak(close < 10.0)


def pcp_074_low_below_5dollar_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: intraday low dipped below $5 (even if close recovered)."""
    return (low < 5.0).astype(float)


def pcp_075_low_below_1dollar_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: intraday low dipped below $1 (even if close recovered)."""
    return (low < 1.0).astype(float)


# ── Registry ──────────────────────────────────────────────────────────────────

PRICE_CLUSTERING_PSYCHOLOGY_REGISTRY_001_075 = {
    "pcp_001_dist_to_nearest_dollar": {"inputs": ["close"], "func": pcp_001_dist_to_nearest_dollar},
    "pcp_002_dist_to_nearest_dollar_pct": {"inputs": ["close"], "func": pcp_002_dist_to_nearest_dollar_pct},
    "pcp_003_dist_to_nearest_5dollar": {"inputs": ["close"], "func": pcp_003_dist_to_nearest_5dollar},
    "pcp_004_dist_to_nearest_5dollar_pct": {"inputs": ["close"], "func": pcp_004_dist_to_nearest_5dollar_pct},
    "pcp_005_dist_to_nearest_10dollar": {"inputs": ["close"], "func": pcp_005_dist_to_nearest_10dollar},
    "pcp_006_dist_to_nearest_10dollar_pct": {"inputs": ["close"], "func": pcp_006_dist_to_nearest_10dollar_pct},
    "pcp_007_dist_to_nearest_25dollar": {"inputs": ["close"], "func": pcp_007_dist_to_nearest_25dollar},
    "pcp_008_dist_to_nearest_25dollar_pct": {"inputs": ["close"], "func": pcp_008_dist_to_nearest_25dollar_pct},
    "pcp_009_dist_to_nearest_50dollar": {"inputs": ["close"], "func": pcp_009_dist_to_nearest_50dollar},
    "pcp_010_dist_to_nearest_50dollar_pct": {"inputs": ["close"], "func": pcp_010_dist_to_nearest_50dollar_pct},
    "pcp_011_at_whole_dollar_flag": {"inputs": ["close"], "func": pcp_011_at_whole_dollar_flag},
    "pcp_012_at_5dollar_flag": {"inputs": ["close"], "func": pcp_012_at_5dollar_flag},
    "pcp_013_at_10dollar_flag": {"inputs": ["close"], "func": pcp_013_at_10dollar_flag},
    "pcp_014_at_25dollar_flag": {"inputs": ["close"], "func": pcp_014_at_25dollar_flag},
    "pcp_015_at_50dollar_flag": {"inputs": ["close"], "func": pcp_015_at_50dollar_flag},
    "pcp_016_at_100dollar_flag": {"inputs": ["close"], "func": pcp_016_at_100dollar_flag},
    "pcp_017_at_1dollar_flag": {"inputs": ["close"], "func": pcp_017_at_1dollar_flag},
    "pcp_018_at_5dollar_exact_flag": {"inputs": ["close"], "func": pcp_018_at_5dollar_exact_flag},
    "pcp_019_below_round_level_flag": {"inputs": ["close"], "func": pcp_019_below_round_level_flag},
    "pcp_020_above_round_level_flag": {"inputs": ["close"], "func": pcp_020_above_round_level_flag},
    "pcp_021_sub1_flag": {"inputs": ["close"], "func": pcp_021_sub1_flag},
    "pcp_022_sub2_flag": {"inputs": ["close"], "func": pcp_022_sub2_flag},
    "pcp_023_sub5_flag": {"inputs": ["close"], "func": pcp_023_sub5_flag},
    "pcp_024_sub10_flag": {"inputs": ["close"], "func": pcp_024_sub10_flag},
    "pcp_025_depth_below_1dollar": {"inputs": ["close"], "func": pcp_025_depth_below_1dollar},
    "pcp_026_depth_below_5dollar": {"inputs": ["close"], "func": pcp_026_depth_below_5dollar},
    "pcp_027_depth_below_10dollar": {"inputs": ["close"], "func": pcp_027_depth_below_10dollar},
    "pcp_028_consec_days_sub5": {"inputs": ["close"], "func": pcp_028_consec_days_sub5},
    "pcp_029_consec_days_sub1": {"inputs": ["close"], "func": pcp_029_consec_days_sub1},
    "pcp_030_fraction_sub5_in_63d": {"inputs": ["close"], "func": pcp_030_fraction_sub5_in_63d},
    "pcp_031_frac_near_dollar_21d": {"inputs": ["close"], "func": pcp_031_frac_near_dollar_21d},
    "pcp_032_frac_near_dollar_63d": {"inputs": ["close"], "func": pcp_032_frac_near_dollar_63d},
    "pcp_033_frac_near_5dollar_21d": {"inputs": ["close"], "func": pcp_033_frac_near_5dollar_21d},
    "pcp_034_frac_near_5dollar_63d": {"inputs": ["close"], "func": pcp_034_frac_near_5dollar_63d},
    "pcp_035_frac_near_10dollar_21d": {"inputs": ["close"], "func": pcp_035_frac_near_10dollar_21d},
    "pcp_036_frac_near_10dollar_63d": {"inputs": ["close"], "func": pcp_036_frac_near_10dollar_63d},
    "pcp_037_frac_near_dollar_252d": {"inputs": ["close"], "func": pcp_037_frac_near_dollar_252d},
    "pcp_038_frac_near_5dollar_252d": {"inputs": ["close"], "func": pcp_038_frac_near_5dollar_252d},
    "pcp_039_frac_near_dollar_5d": {"inputs": ["close"], "func": pcp_039_frac_near_dollar_5d},
    "pcp_040_frac_near_10dollar_252d": {"inputs": ["close"], "func": pcp_040_frac_near_10dollar_252d},
    "pcp_041_cents_digit": {"inputs": ["close"], "func": pcp_041_cents_digit},
    "pcp_042_dime_digit": {"inputs": ["close"], "func": pcp_042_dime_digit},
    "pcp_043_trailing_digit_zero_flag": {"inputs": ["close"], "func": pcp_043_trailing_digit_zero_flag},
    "pcp_044_trailing_digit_50_flag": {"inputs": ["close"], "func": pcp_044_trailing_digit_50_flag},
    "pcp_045_trailing_digit_25_flag": {"inputs": ["close"], "func": pcp_045_trailing_digit_25_flag},
    "pcp_046_trailing_digit_75_flag": {"inputs": ["close"], "func": pcp_046_trailing_digit_75_flag},
    "pcp_047_frac_zero_cents_21d": {"inputs": ["close"], "func": pcp_047_frac_zero_cents_21d},
    "pcp_048_frac_50_cents_21d": {"inputs": ["close"], "func": pcp_048_frac_50_cents_21d},
    "pcp_049_frac_zero_cents_63d": {"inputs": ["close"], "func": pcp_049_frac_zero_cents_63d},
    "pcp_050_frac_even_dollar_63d": {"inputs": ["close"], "func": pcp_050_frac_even_dollar_63d},
    "pcp_051_high_low_straddles_dollar_flag": {"inputs": ["close", "high", "low"], "func": pcp_051_high_low_straddles_dollar_flag},
    "pcp_052_range_within_dollar_pct": {"inputs": ["close", "high", "low"], "func": pcp_052_range_within_dollar_pct},
    "pcp_053_close_vs_nearest_dollar_below": {"inputs": ["close"], "func": pcp_053_close_vs_nearest_dollar_below},
    "pcp_054_close_vs_nearest_dollar_above": {"inputs": ["close"], "func": pcp_054_close_vs_nearest_dollar_above},
    "pcp_055_close_pct_thru_5dollar_zone": {"inputs": ["close"], "func": pcp_055_close_pct_thru_5dollar_zone},
    "pcp_056_close_pct_thru_10dollar_zone": {"inputs": ["close"], "func": pcp_056_close_pct_thru_10dollar_zone},
    "pcp_057_rolling_dist_dollar_mean_21d": {"inputs": ["close"], "func": pcp_057_rolling_dist_dollar_mean_21d},
    "pcp_058_rolling_dist_dollar_std_21d": {"inputs": ["close"], "func": pcp_058_rolling_dist_dollar_std_21d},
    "pcp_059_rolling_dist_5dollar_mean_21d": {"inputs": ["close"], "func": pcp_059_rolling_dist_5dollar_mean_21d},
    "pcp_060_rolling_dist_10dollar_mean_21d": {"inputs": ["close"], "func": pcp_060_rolling_dist_10dollar_mean_21d},
    "pcp_061_fraction_sub1_in_252d": {"inputs": ["close"], "func": pcp_061_fraction_sub1_in_252d},
    "pcp_062_fraction_sub2_in_252d": {"inputs": ["close"], "func": pcp_062_fraction_sub2_in_252d},
    "pcp_063_fraction_sub5_in_252d": {"inputs": ["close"], "func": pcp_063_fraction_sub5_in_252d},
    "pcp_064_fraction_sub10_in_252d": {"inputs": ["close"], "func": pcp_064_fraction_sub10_in_252d},
    "pcp_065_time_since_last_above_5dollar": {"inputs": ["close"], "func": pcp_065_time_since_last_above_5dollar},
    "pcp_066_time_since_last_above_10dollar": {"inputs": ["close"], "func": pcp_066_time_since_last_above_10dollar},
    "pcp_067_time_since_last_above_1dollar": {"inputs": ["close"], "func": pcp_067_time_since_last_above_1dollar},
    "pcp_068_close_level_zscore_252d": {"inputs": ["close"], "func": pcp_068_close_level_zscore_252d},
    "pcp_069_close_pct_rank_252d": {"inputs": ["close"], "func": pcp_069_close_pct_rank_252d},
    "pcp_070_close_pct_rank_63d": {"inputs": ["close"], "func": pcp_070_close_pct_rank_63d},
    "pcp_071_close_expanding_pct_rank": {"inputs": ["close"], "func": pcp_071_close_expanding_pct_rank},
    "pcp_072_price_in_sub5_zone_depth_pct": {"inputs": ["close"], "func": pcp_072_price_in_sub5_zone_depth_pct},
    "pcp_073_consec_days_sub10": {"inputs": ["close"], "func": pcp_073_consec_days_sub10},
    "pcp_074_low_below_5dollar_flag": {"inputs": ["close", "low"], "func": pcp_074_low_below_5dollar_flag},
    "pcp_075_low_below_1dollar_flag": {"inputs": ["close", "low"], "func": pcp_075_low_below_1dollar_flag},
}
