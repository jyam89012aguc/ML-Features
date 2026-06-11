"""
106_support_violation — Base Features 001-075
Domain: violation of historical support — breaks below prior trailing lows, prior
        congestion-zone lows, and recent swing lows; distance/depth below broken
        support; count and recency of support breaks; round-number level undercuts;
        how decisively support is lost.
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


def _prior_low(low: pd.Series, w: int) -> pd.Series:
    """Trailing minimum of low over w days, shifted 1 so today is excluded."""
    return low.shift(1).rolling(w, min_periods=max(1, w // 2)).min()


def _depth_below(price: pd.Series, support: pd.Series) -> pd.Series:
    """Signed depth of price below support level (positive = below support)."""
    return (support - price).clip(lower=0.0)


def _pct_depth_below(price: pd.Series, support: pd.Series) -> pd.Series:
    """Percentage depth below support level (0 when at or above support)."""
    depth = (support - price).clip(lower=0.0)
    return _safe_div(depth, support.clip(lower=_EPS))


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Depth below trailing-low support levels ---

def sv_001_close_depth_below_21d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute depth of close below the prior 21-day trailing low (0 when above)."""
    support = _prior_low(low, _TD_MON)
    return _depth_below(close, support)


def sv_002_close_depth_below_63d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute depth of close below the prior 63-day trailing low."""
    support = _prior_low(low, _TD_QTR)
    return _depth_below(close, support)


def sv_003_close_depth_below_126d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute depth of close below the prior 126-day trailing low."""
    support = _prior_low(low, _TD_HALF)
    return _depth_below(close, support)


def sv_004_close_depth_below_252d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute depth of close below the prior 252-day trailing low."""
    support = _prior_low(low, _TD_YEAR)
    return _depth_below(close, support)


def sv_005_close_pct_depth_below_21d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentage depth of close below the prior 21-day trailing low."""
    support = _prior_low(low, _TD_MON)
    return _pct_depth_below(close, support)


def sv_006_close_pct_depth_below_63d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentage depth of close below the prior 63-day trailing low."""
    support = _prior_low(low, _TD_QTR)
    return _pct_depth_below(close, support)


def sv_007_close_pct_depth_below_126d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentage depth of close below the prior 126-day trailing low."""
    support = _prior_low(low, _TD_HALF)
    return _pct_depth_below(close, support)


def sv_008_close_pct_depth_below_252d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentage depth of close below the prior 252-day trailing low."""
    support = _prior_low(low, _TD_YEAR)
    return _pct_depth_below(close, support)


def sv_009_low_depth_below_21d_low(low: pd.Series) -> pd.Series:
    """Absolute depth of today's low below the prior 21-day trailing low."""
    support = _prior_low(low, _TD_MON)
    return _depth_below(low, support)


def sv_010_low_depth_below_63d_low(low: pd.Series) -> pd.Series:
    """Absolute depth of today's low below the prior 63-day trailing low."""
    support = _prior_low(low, _TD_QTR)
    return _depth_below(low, support)


def sv_011_low_depth_below_126d_low(low: pd.Series) -> pd.Series:
    """Absolute depth of today's low below the prior 126-day trailing low."""
    support = _prior_low(low, _TD_HALF)
    return _depth_below(low, support)


def sv_012_low_depth_below_252d_low(low: pd.Series) -> pd.Series:
    """Absolute depth of today's low below the prior 252-day trailing low."""
    support = _prior_low(low, _TD_YEAR)
    return _depth_below(low, support)


def sv_013_low_pct_depth_below_63d_low(low: pd.Series) -> pd.Series:
    """Percentage depth of today's low below the prior 63-day trailing low."""
    support = _prior_low(low, _TD_QTR)
    return _pct_depth_below(low, support)


def sv_014_low_pct_depth_below_252d_low(low: pd.Series) -> pd.Series:
    """Percentage depth of today's low below the prior 252-day trailing low."""
    support = _prior_low(low, _TD_YEAR)
    return _pct_depth_below(low, support)


def sv_015_close_depth_below_504d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute depth of close below the prior 504-day (2-year) trailing low."""
    support = low.shift(1).rolling(504, min_periods=126).min()
    return _depth_below(close, support)


# --- Group B (016-030): Binary break flags at multiple lookbacks ---

def sv_016_close_below_21d_low_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close is below prior 21-day trailing low."""
    support = _prior_low(low, _TD_MON)
    return (close < support).astype(float)


def sv_017_close_below_63d_low_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close is below prior 63-day trailing low."""
    support = _prior_low(low, _TD_QTR)
    return (close < support).astype(float)


def sv_018_close_below_126d_low_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close is below prior 126-day trailing low."""
    support = _prior_low(low, _TD_HALF)
    return (close < support).astype(float)


def sv_019_close_below_252d_low_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close is below prior 252-day trailing low."""
    support = _prior_low(low, _TD_YEAR)
    return (close < support).astype(float)


def sv_020_low_below_21d_low_flag(low: pd.Series) -> pd.Series:
    """Binary flag: today's low breaks the prior 21-day trailing low."""
    support = _prior_low(low, _TD_MON)
    return (low < support).astype(float)


def sv_021_low_below_63d_low_flag(low: pd.Series) -> pd.Series:
    """Binary flag: today's low breaks the prior 63-day trailing low."""
    support = _prior_low(low, _TD_QTR)
    return (low < support).astype(float)


def sv_022_low_below_126d_low_flag(low: pd.Series) -> pd.Series:
    """Binary flag: today's low breaks the prior 126-day trailing low."""
    support = _prior_low(low, _TD_HALF)
    return (low < support).astype(float)


def sv_023_low_below_252d_low_flag(low: pd.Series) -> pd.Series:
    """Binary flag: today's low breaks the prior 252-day trailing low."""
    support = _prior_low(low, _TD_YEAR)
    return (low < support).astype(float)


def sv_024_close_multi_support_break_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close simultaneously breaks 21d, 63d, and 126d trailing lows."""
    s21 = _prior_low(low, _TD_MON)
    s63 = _prior_low(low, _TD_QTR)
    s126 = _prior_low(low, _TD_HALF)
    return ((close < s21) & (close < s63) & (close < s126)).astype(float)


def sv_025_close_all4_support_break_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close breaks all four support levels: 21d, 63d, 126d, 252d."""
    s21 = _prior_low(low, _TD_MON)
    s63 = _prior_low(low, _TD_QTR)
    s126 = _prior_low(low, _TD_HALF)
    s252 = _prior_low(low, _TD_YEAR)
    return ((close < s21) & (close < s63) & (close < s126) & (close < s252)).astype(float)


def sv_026_low_new_52wk_low_flag(low: pd.Series) -> pd.Series:
    """Binary flag: today's low is a new 52-week (252-day) low."""
    support = _prior_low(low, _TD_YEAR)
    return (low < support).astype(float)


def sv_027_low_new_2yr_low_flag(low: pd.Series) -> pd.Series:
    """Binary flag: today's low is a new 2-year (504-day) low."""
    support = low.shift(1).rolling(504, min_periods=126).min()
    return (low < support).astype(float)


def sv_028_close_new_52wk_low_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is a new 52-week closing low."""
    support = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_QTR).min()
    return (close < support).astype(float)


def sv_029_close_new_ytd_low_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is a new year-to-date low (trailing 252 sessions)."""
    support = close.shift(1).rolling(_TD_YEAR, min_periods=1).min()
    return (close < support).astype(float)


def sv_030_low_new_qtd_low_flag(low: pd.Series) -> pd.Series:
    """Binary flag: today's low is a new quarter-to-date low (trailing 63 sessions)."""
    support = _prior_low(low, _TD_QTR)
    return (low < support).astype(float)


# --- Group C (031-045): Count and recency of support breaks ---

def sv_031_breaks_below_21d_low_in_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days in trailing 21d where close broke the rolling 21d prior low."""
    flag = (close < _prior_low(low, _TD_MON)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def sv_032_breaks_below_63d_low_in_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where close broke the rolling 63d prior low."""
    flag = (close < _prior_low(low, _TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def sv_033_breaks_below_252d_low_in_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days in trailing 252d where close broke the rolling 252d prior low."""
    flag = (close < _prior_low(low, _TD_YEAR)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def sv_034_consec_days_close_below_63d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days where close has remained below the 63d trailing low."""
    return _consec_streak(close < _prior_low(low, _TD_QTR))


def sv_035_consec_days_close_below_252d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days where close has remained below the 252d trailing low."""
    return _consec_streak(close < _prior_low(low, _TD_YEAR))


def sv_036_consec_days_low_below_63d_low(low: pd.Series) -> pd.Series:
    """Consecutive days where today's low has broken the 63d trailing low."""
    return _consec_streak(low < _prior_low(low, _TD_QTR))


def sv_037_consec_days_low_below_252d_low(low: pd.Series) -> pd.Series:
    """Consecutive days where today's low has broken the 252d trailing low."""
    return _consec_streak(low < _prior_low(low, _TD_YEAR))


def sv_038_days_since_last_52wk_low_break(low: pd.Series) -> pd.Series:
    """Days since the last time the 52-week low was broken (0 = currently breaking)."""
    flag = (low < _prior_low(low, _TD_YEAR)).astype(float)
    idx = pd.Series(range(len(flag)), index=flag.index, dtype=float)
    last_idx = idx.where(flag == 1.0).ffill().fillna(0)
    return (idx - last_idx).where(~low.isna(), np.nan)


def sv_039_days_since_last_21d_low_break(low: pd.Series) -> pd.Series:
    """Days since the last time the 21-day low was broken."""
    flag = (low < _prior_low(low, _TD_MON)).astype(float)
    idx = pd.Series(range(len(flag)), index=flag.index, dtype=float)
    last_idx = idx.where(flag == 1.0).ffill().fillna(0)
    return (idx - last_idx).where(~low.isna(), np.nan)


def sv_040_days_since_last_63d_low_break(low: pd.Series) -> pd.Series:
    """Days since the last time the 63-day low was broken."""
    flag = (low < _prior_low(low, _TD_QTR)).astype(float)
    idx = pd.Series(range(len(flag)), index=flag.index, dtype=float)
    last_idx = idx.where(flag == 1.0).ffill().fillna(0)
    return (idx - last_idx).where(~low.isna(), np.nan)


def sv_041_break_count_below_63d_in_21d(low: pd.Series) -> pd.Series:
    """Count of days in trailing 21d where today's low broke the rolling 63d prior low."""
    flag = (low < _prior_low(low, _TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def sv_042_break_count_below_252d_in_63d(low: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where today's low broke the rolling 252d prior low."""
    flag = (low < _prior_low(low, _TD_YEAR)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def sv_043_fraction_below_63d_low_in_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of trailing 252d where close was below the rolling 63d prior low."""
    flag = (close < _prior_low(low, _TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


def sv_044_fraction_below_252d_low_in_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of trailing 252d where close was below the rolling 252d prior low."""
    flag = (close < _prior_low(low, _TD_YEAR)).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


def sv_045_break_recency_weighted_score_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Recency-weighted support-break score: sum of exp-decayed daily break flags (252d)."""
    flag = (close < _prior_low(low, _TD_YEAR)).astype(float)
    return flag.ewm(span=_TD_QTR, min_periods=1, adjust=True).mean()


# --- Group D (046-060): Depth composites and distance ratios ---

def sv_046_depth_below_63d_low_zscore_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of pct-depth-below-63d-low relative to its 252-day distribution."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    m = _rolling_mean(depth, _TD_YEAR)
    s = _rolling_std(depth, _TD_YEAR)
    return _safe_div(depth - m, s)


def sv_047_depth_below_252d_low_zscore_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of pct-depth-below-252d-low relative to its own 252-day distribution."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    m = _rolling_mean(depth, _TD_YEAR)
    s = _rolling_std(depth, _TD_YEAR)
    return _safe_div(depth - m, s)


def sv_048_close_to_63d_low_ratio(close: pd.Series, low: pd.Series) -> pd.Series:
    """Close divided by the prior 63-day low (below 1.0 = below support)."""
    support = _prior_low(low, _TD_QTR)
    return _safe_div(close, support.clip(lower=_EPS))


def sv_049_close_to_252d_low_ratio(close: pd.Series, low: pd.Series) -> pd.Series:
    """Close divided by the prior 252-day low (below 1.0 = below support)."""
    support = _prior_low(low, _TD_YEAR)
    return _safe_div(close, support.clip(lower=_EPS))


def sv_050_multi_support_depth_sum(close: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of pct-depths below 21d, 63d, 126d, 252d support levels."""
    d21 = _pct_depth_below(close, _prior_low(low, _TD_MON))
    d63 = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    d126 = _pct_depth_below(close, _prior_low(low, _TD_HALF))
    d252 = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    return d21 + d63 + d126 + d252


def sv_051_depth_below_63d_low_pct_rank_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of pct-depth-below-63d-low within trailing 252-day distribution."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    return depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def sv_052_depth_below_252d_low_pct_rank_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of pct-depth-below-252d-low within trailing 252-day distribution."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    return depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def sv_053_close_to_21d_low_ratio(close: pd.Series, low: pd.Series) -> pd.Series:
    """Close divided by the prior 21-day low (below 1.0 = below support)."""
    support = _prior_low(low, _TD_MON)
    return _safe_div(close, support.clip(lower=_EPS))


def sv_054_max_depth_below_252d_low_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum pct-depth below 252d low achieved in trailing 21 days."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    return _rolling_max(depth, _TD_MON)


def sv_055_max_depth_below_252d_low_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum pct-depth below 252d low achieved in trailing 63 days."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    return _rolling_max(depth, _TD_QTR)


def sv_056_depth_below_63d_low_expanding_max(close: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding all-time maximum pct-depth below 63d prior low."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    return depth.expanding(min_periods=1).max()


def sv_057_depth_below_252d_low_expanding_max(close: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding all-time maximum pct-depth below 252d prior low."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    return depth.expanding(min_periods=1).max()


def sv_058_close_pct_below_63d_low_intensity_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Rolling sum of pct-depth below 63d low over 21 days (oversold intensity)."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    return _rolling_sum(depth, _TD_MON)


def sv_059_close_pct_below_252d_low_intensity_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Rolling sum of pct-depth below 252d low over 63 days (oversold intensity)."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    return _rolling_sum(depth, _TD_QTR)


def sv_060_low_to_close_break_ratio(close: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of low's pct-depth below 252d support to close's pct-depth (decisiveness)."""
    low_depth = _pct_depth_below(low, _prior_low(low, _TD_YEAR))
    close_depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    return _safe_div(close_depth, low_depth.clip(lower=_EPS))


# --- Group E (061-075): Round-number undercuts and decisiveness ---

def sv_061_round_dollar_undercut_1(close: pd.Series) -> pd.Series:
    """Distance below the nearest $1 round-number floor (close mod $1)."""
    floor = np.floor(close.values)
    return pd.Series(close.values - floor, index=close.index).clip(lower=0.0)


def sv_062_pct_below_nearest_whole_dollar(close: pd.Series) -> pd.Series:
    """Percentage below the nearest whole-dollar floor price."""
    floor = pd.Series(np.floor(close.values), index=close.index).clip(lower=_EPS)
    dist = (floor - close).clip(lower=0.0)
    return _safe_div(dist, floor)


def sv_063_round_5dollar_undercut(close: pd.Series) -> pd.Series:
    """Distance below the nearest $5 round-number level."""
    floor5 = pd.Series(np.floor(close.values / 5.0) * 5.0, index=close.index)
    return (floor5 - close).clip(lower=0.0)


def sv_064_round_10dollar_undercut(close: pd.Series) -> pd.Series:
    """Distance below the nearest $10 round-number level."""
    floor10 = pd.Series(np.floor(close.values / 10.0) * 10.0, index=close.index)
    return (floor10 - close).clip(lower=0.0)


def sv_065_below_1dollar_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close has fallen below $1.00 (penny-stock threshold)."""
    return (close < 1.0).astype(float)


def sv_066_below_5dollar_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close has fallen below $5.00."""
    return (close < 5.0).astype(float)


def sv_067_below_2dollar_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close has fallen below $2.00."""
    return (close < 2.0).astype(float)


def sv_068_consec_days_below_5dollar(close: pd.Series) -> pd.Series:
    """Consecutive days close has remained below $5."""
    return _consec_streak(close < 5.0)


def sv_069_consec_days_below_1dollar(close: pd.Series) -> pd.Series:
    """Consecutive days close has remained below $1."""
    return _consec_streak(close < 1.0)


def sv_070_close_low_gap_on_break_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """On days where close breaks 252d support, close-to-low range as pct of low.
    Measures how far below the intraday low the close settled."""
    support = _prior_low(low, _TD_YEAR)
    broke = (close < support).astype(float)
    hl_range = _safe_div((close - low).abs(), low.clip(lower=_EPS))
    return hl_range * broke


def sv_071_break_magnitude_63d_low_21d_avg(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day average pct-depth below 63d low (sustained breakdown magnitude)."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    return _rolling_mean(depth, _TD_MON)


def sv_072_break_magnitude_252d_low_21d_avg(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day average pct-depth below 252d low (sustained breakdown magnitude)."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    return _rolling_mean(depth, _TD_MON)


def sv_073_support_break_score_composite(close: pd.Series, low: pd.Series) -> pd.Series:
    """Composite support violation score: sum of binary breaks across 21d/63d/126d/252d."""
    b21 = (close < _prior_low(low, _TD_MON)).astype(float)
    b63 = (close < _prior_low(low, _TD_QTR)).astype(float)
    b126 = (close < _prior_low(low, _TD_HALF)).astype(float)
    b252 = (close < _prior_low(low, _TD_YEAR)).astype(float)
    return b21 + b63 + b126 + b252


def sv_074_close_below_63d_low_norm_intensity(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day oversold intensity (pct-depth sum) normalized by 252-day mean intensity."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    intensity21 = _rolling_sum(depth, _TD_MON)
    avg252 = _rolling_mean(intensity21, _TD_YEAR)
    return _safe_div(intensity21, avg252.clip(lower=_EPS))


def sv_075_low_expansion_on_break_252d(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """On support-break days (252d), measures daily range expansion: (high-low)/close.
    Higher = more volatile / decisive breakdown bar."""
    support = _prior_low(low, _TD_YEAR)
    broke = (close < support).astype(float)
    bar_range = _safe_div(high - low, close.clip(lower=_EPS))
    return bar_range * broke


# ── Registry ──────────────────────────────────────────────────────────────────

SUPPORT_VIOLATION_REGISTRY_001_075 = {
    "sv_001_close_depth_below_21d_low": {"inputs": ["close", "low"], "func": sv_001_close_depth_below_21d_low},
    "sv_002_close_depth_below_63d_low": {"inputs": ["close", "low"], "func": sv_002_close_depth_below_63d_low},
    "sv_003_close_depth_below_126d_low": {"inputs": ["close", "low"], "func": sv_003_close_depth_below_126d_low},
    "sv_004_close_depth_below_252d_low": {"inputs": ["close", "low"], "func": sv_004_close_depth_below_252d_low},
    "sv_005_close_pct_depth_below_21d_low": {"inputs": ["close", "low"], "func": sv_005_close_pct_depth_below_21d_low},
    "sv_006_close_pct_depth_below_63d_low": {"inputs": ["close", "low"], "func": sv_006_close_pct_depth_below_63d_low},
    "sv_007_close_pct_depth_below_126d_low": {"inputs": ["close", "low"], "func": sv_007_close_pct_depth_below_126d_low},
    "sv_008_close_pct_depth_below_252d_low": {"inputs": ["close", "low"], "func": sv_008_close_pct_depth_below_252d_low},
    "sv_009_low_depth_below_21d_low": {"inputs": ["low"], "func": sv_009_low_depth_below_21d_low},
    "sv_010_low_depth_below_63d_low": {"inputs": ["low"], "func": sv_010_low_depth_below_63d_low},
    "sv_011_low_depth_below_126d_low": {"inputs": ["low"], "func": sv_011_low_depth_below_126d_low},
    "sv_012_low_depth_below_252d_low": {"inputs": ["low"], "func": sv_012_low_depth_below_252d_low},
    "sv_013_low_pct_depth_below_63d_low": {"inputs": ["low"], "func": sv_013_low_pct_depth_below_63d_low},
    "sv_014_low_pct_depth_below_252d_low": {"inputs": ["low"], "func": sv_014_low_pct_depth_below_252d_low},
    "sv_015_close_depth_below_504d_low": {"inputs": ["close", "low"], "func": sv_015_close_depth_below_504d_low},
    "sv_016_close_below_21d_low_flag": {"inputs": ["close", "low"], "func": sv_016_close_below_21d_low_flag},
    "sv_017_close_below_63d_low_flag": {"inputs": ["close", "low"], "func": sv_017_close_below_63d_low_flag},
    "sv_018_close_below_126d_low_flag": {"inputs": ["close", "low"], "func": sv_018_close_below_126d_low_flag},
    "sv_019_close_below_252d_low_flag": {"inputs": ["close", "low"], "func": sv_019_close_below_252d_low_flag},
    "sv_020_low_below_21d_low_flag": {"inputs": ["low"], "func": sv_020_low_below_21d_low_flag},
    "sv_021_low_below_63d_low_flag": {"inputs": ["low"], "func": sv_021_low_below_63d_low_flag},
    "sv_022_low_below_126d_low_flag": {"inputs": ["low"], "func": sv_022_low_below_126d_low_flag},
    "sv_023_low_below_252d_low_flag": {"inputs": ["low"], "func": sv_023_low_below_252d_low_flag},
    "sv_024_close_multi_support_break_flag": {"inputs": ["close", "low"], "func": sv_024_close_multi_support_break_flag},
    "sv_025_close_all4_support_break_flag": {"inputs": ["close", "low"], "func": sv_025_close_all4_support_break_flag},
    "sv_026_low_new_52wk_low_flag": {"inputs": ["low"], "func": sv_026_low_new_52wk_low_flag},
    "sv_027_low_new_2yr_low_flag": {"inputs": ["low"], "func": sv_027_low_new_2yr_low_flag},
    "sv_028_close_new_52wk_low_flag": {"inputs": ["close"], "func": sv_028_close_new_52wk_low_flag},
    "sv_029_close_new_ytd_low_flag": {"inputs": ["close"], "func": sv_029_close_new_ytd_low_flag},
    "sv_030_low_new_qtd_low_flag": {"inputs": ["low"], "func": sv_030_low_new_qtd_low_flag},
    "sv_031_breaks_below_21d_low_in_21d": {"inputs": ["close", "low"], "func": sv_031_breaks_below_21d_low_in_21d},
    "sv_032_breaks_below_63d_low_in_63d": {"inputs": ["close", "low"], "func": sv_032_breaks_below_63d_low_in_63d},
    "sv_033_breaks_below_252d_low_in_252d": {"inputs": ["close", "low"], "func": sv_033_breaks_below_252d_low_in_252d},
    "sv_034_consec_days_close_below_63d_low": {"inputs": ["close", "low"], "func": sv_034_consec_days_close_below_63d_low},
    "sv_035_consec_days_close_below_252d_low": {"inputs": ["close", "low"], "func": sv_035_consec_days_close_below_252d_low},
    "sv_036_consec_days_low_below_63d_low": {"inputs": ["low"], "func": sv_036_consec_days_low_below_63d_low},
    "sv_037_consec_days_low_below_252d_low": {"inputs": ["low"], "func": sv_037_consec_days_low_below_252d_low},
    "sv_038_days_since_last_52wk_low_break": {"inputs": ["low"], "func": sv_038_days_since_last_52wk_low_break},
    "sv_039_days_since_last_21d_low_break": {"inputs": ["low"], "func": sv_039_days_since_last_21d_low_break},
    "sv_040_days_since_last_63d_low_break": {"inputs": ["low"], "func": sv_040_days_since_last_63d_low_break},
    "sv_041_break_count_below_63d_in_21d": {"inputs": ["low"], "func": sv_041_break_count_below_63d_in_21d},
    "sv_042_break_count_below_252d_in_63d": {"inputs": ["low"], "func": sv_042_break_count_below_252d_in_63d},
    "sv_043_fraction_below_63d_low_in_252d": {"inputs": ["close", "low"], "func": sv_043_fraction_below_63d_low_in_252d},
    "sv_044_fraction_below_252d_low_in_252d": {"inputs": ["close", "low"], "func": sv_044_fraction_below_252d_low_in_252d},
    "sv_045_break_recency_weighted_score_252d": {"inputs": ["close", "low"], "func": sv_045_break_recency_weighted_score_252d},
    "sv_046_depth_below_63d_low_zscore_252d": {"inputs": ["close", "low"], "func": sv_046_depth_below_63d_low_zscore_252d},
    "sv_047_depth_below_252d_low_zscore_252d": {"inputs": ["close", "low"], "func": sv_047_depth_below_252d_low_zscore_252d},
    "sv_048_close_to_63d_low_ratio": {"inputs": ["close", "low"], "func": sv_048_close_to_63d_low_ratio},
    "sv_049_close_to_252d_low_ratio": {"inputs": ["close", "low"], "func": sv_049_close_to_252d_low_ratio},
    "sv_050_multi_support_depth_sum": {"inputs": ["close", "low"], "func": sv_050_multi_support_depth_sum},
    "sv_051_depth_below_63d_low_pct_rank_252d": {"inputs": ["close", "low"], "func": sv_051_depth_below_63d_low_pct_rank_252d},
    "sv_052_depth_below_252d_low_pct_rank_252d": {"inputs": ["close", "low"], "func": sv_052_depth_below_252d_low_pct_rank_252d},
    "sv_053_close_to_21d_low_ratio": {"inputs": ["close", "low"], "func": sv_053_close_to_21d_low_ratio},
    "sv_054_max_depth_below_252d_low_21d": {"inputs": ["close", "low"], "func": sv_054_max_depth_below_252d_low_21d},
    "sv_055_max_depth_below_252d_low_63d": {"inputs": ["close", "low"], "func": sv_055_max_depth_below_252d_low_63d},
    "sv_056_depth_below_63d_low_expanding_max": {"inputs": ["close", "low"], "func": sv_056_depth_below_63d_low_expanding_max},
    "sv_057_depth_below_252d_low_expanding_max": {"inputs": ["close", "low"], "func": sv_057_depth_below_252d_low_expanding_max},
    "sv_058_close_pct_below_63d_low_intensity_21d": {"inputs": ["close", "low"], "func": sv_058_close_pct_below_63d_low_intensity_21d},
    "sv_059_close_pct_below_252d_low_intensity_63d": {"inputs": ["close", "low"], "func": sv_059_close_pct_below_252d_low_intensity_63d},
    "sv_060_low_to_close_break_ratio": {"inputs": ["close", "low"], "func": sv_060_low_to_close_break_ratio},
    "sv_061_round_dollar_undercut_1": {"inputs": ["close"], "func": sv_061_round_dollar_undercut_1},
    "sv_062_pct_below_nearest_whole_dollar": {"inputs": ["close"], "func": sv_062_pct_below_nearest_whole_dollar},
    "sv_063_round_5dollar_undercut": {"inputs": ["close"], "func": sv_063_round_5dollar_undercut},
    "sv_064_round_10dollar_undercut": {"inputs": ["close"], "func": sv_064_round_10dollar_undercut},
    "sv_065_below_1dollar_flag": {"inputs": ["close"], "func": sv_065_below_1dollar_flag},
    "sv_066_below_5dollar_flag": {"inputs": ["close"], "func": sv_066_below_5dollar_flag},
    "sv_067_below_2dollar_flag": {"inputs": ["close"], "func": sv_067_below_2dollar_flag},
    "sv_068_consec_days_below_5dollar": {"inputs": ["close"], "func": sv_068_consec_days_below_5dollar},
    "sv_069_consec_days_below_1dollar": {"inputs": ["close"], "func": sv_069_consec_days_below_1dollar},
    "sv_070_close_low_gap_on_break_252d": {"inputs": ["close", "low"], "func": sv_070_close_low_gap_on_break_252d},
    "sv_071_break_magnitude_63d_low_21d_avg": {"inputs": ["close", "low"], "func": sv_071_break_magnitude_63d_low_21d_avg},
    "sv_072_break_magnitude_252d_low_21d_avg": {"inputs": ["close", "low"], "func": sv_072_break_magnitude_252d_low_21d_avg},
    "sv_073_support_break_score_composite": {"inputs": ["close", "low"], "func": sv_073_support_break_score_composite},
    "sv_074_close_below_63d_low_norm_intensity": {"inputs": ["close", "low"], "func": sv_074_close_below_63d_low_norm_intensity},
    "sv_075_low_expansion_on_break_252d": {"inputs": ["close", "low", "high"], "func": sv_075_low_expansion_on_break_252d},
}
