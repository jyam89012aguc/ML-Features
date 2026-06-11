"""
40_close_location — Base Features 001-075
Domain: close's position within the daily range — close location value (CLV)
Measures where the close sits between the day's low and high:
CLV = ((close-low)-(high-close))/(high-low), fractions, streaks, averages.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

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


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


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


def _clv_raw(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Core CLV = ((close-low)-(high-close))/(high-low), NaN when range=0."""
    hl = high - low
    return _safe_div((close - low) - (high - close), hl)


def _close_frac(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close as fraction of range: (close-low)/(high-low), in [0,1]."""
    return _safe_div(close - low, high - low)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Raw CLV and close-fraction fundamentals ---

def clv_001_clv_raw(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CLV = ((close-low)-(high-close))/(high-low); ranges [-1, +1]."""
    return _clv_raw(close, high, low)


def clv_002_close_frac_of_range(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close as fraction of daily range: (close-low)/(high-low), in [0, 1]."""
    return _close_frac(close, high, low)


def clv_003_clv_shifted1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CLV lagged by 1 day (prior day close location)."""
    return _clv_raw(close, high, low).shift(1)


def clv_004_clv_shifted5(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CLV lagged by 5 days (one week ago close location)."""
    return _clv_raw(close, high, low).shift(5)


def clv_005_clv_shifted21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CLV lagged by 21 days (one month ago close location)."""
    return _clv_raw(close, high, low).shift(21)


def clv_006_clv_abs(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute value of CLV (magnitude of close displacement from midpoint)."""
    return _clv_raw(close, high, low).abs()


def clv_007_clv_sign(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sign of CLV: +1 upper half, -1 lower half, 0 at midpoint."""
    return np.sign(_clv_raw(close, high, low))


def clv_008_close_frac_complement(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """1 minus close-fraction: measures proximity to low end of range."""
    return 1.0 - _close_frac(close, high, low)


def clv_009_clv_distance_from_mid(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Signed distance of close from bar midpoint as fraction of half-range."""
    mid = (high + low) / 2.0
    half_range = (high - low) / 2.0
    return _safe_div(close - mid, half_range)


def clv_010_close_near_low_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close in bottom 25% of range (close-frac <= 0.25)."""
    return (_close_frac(close, high, low) <= 0.25).astype(float)


# --- Group B (011-020): Rolling average CLV over standard windows ---

def clv_011_clv_sma5(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day simple moving average of CLV."""
    return _rolling_mean(_clv_raw(close, high, low), _TD_WEEK)


def clv_012_clv_sma21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day simple moving average of CLV."""
    return _rolling_mean(_clv_raw(close, high, low), _TD_MON)


def clv_013_clv_sma63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day simple moving average of CLV."""
    return _rolling_mean(_clv_raw(close, high, low), _TD_QTR)


def clv_014_clv_sma126(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """126-day simple moving average of CLV."""
    return _rolling_mean(_clv_raw(close, high, low), _TD_HALF)


def clv_015_clv_sma252(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day simple moving average of CLV."""
    return _rolling_mean(_clv_raw(close, high, low), _TD_YEAR)


def clv_016_clv_ema5(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day EMA of CLV."""
    return _ewm_mean(_clv_raw(close, high, low), _TD_WEEK)


def clv_017_clv_ema21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day EMA of CLV."""
    return _ewm_mean(_clv_raw(close, high, low), _TD_MON)


def clv_018_clv_ema63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day EMA of CLV."""
    return _ewm_mean(_clv_raw(close, high, low), _TD_QTR)


def clv_019_close_frac_sma21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day average close-fraction-of-range."""
    return _rolling_mean(_close_frac(close, high, low), _TD_MON)


def clv_020_close_frac_sma63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day average close-fraction-of-range."""
    return _rolling_mean(_close_frac(close, high, low), _TD_QTR)


# --- Group C (021-030): CLV percentile ranks ---

def clv_021_clv_pct_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's CLV within trailing 21 days."""
    clv = _clv_raw(close, high, low)
    return clv.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)


def clv_022_clv_pct_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's CLV within trailing 63 days."""
    clv = _clv_raw(close, high, low)
    return clv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def clv_023_clv_pct_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's CLV within trailing 126 days."""
    clv = _clv_raw(close, high, low)
    return clv.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def clv_024_clv_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's CLV within trailing 252 days."""
    clv = _clv_raw(close, high, low)
    return clv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def clv_025_clv_expanding_pct_rank(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding percentile rank of CLV (full history)."""
    clv = _clv_raw(close, high, low)
    return clv.expanding(min_periods=5).rank(pct=True)


def clv_026_close_frac_pct_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of close-fraction within trailing 63 days."""
    cf = _close_frac(close, high, low)
    return cf.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def clv_027_close_frac_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of close-fraction within trailing 252 days."""
    cf = _close_frac(close, high, low)
    return cf.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def clv_028_clv_below_minus05_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: CLV <= -0.5 (close in bottom quarter of range)."""
    return (_clv_raw(close, high, low) <= -0.5).astype(float)


def clv_029_clv_below_zero_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: CLV < 0 (close in lower half of range)."""
    return (_clv_raw(close, high, low) < 0).astype(float)


def clv_030_clv_above_plus05_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: CLV >= +0.5 (close in top quarter of range, bullish close)."""
    return (_clv_raw(close, high, low) >= 0.5).astype(float)


# --- Group D (031-040): Consecutive weak/strong close streaks ---

def clv_031_consec_close_near_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days closing in bottom 25% of range (close-frac <= 0.25)."""
    cond = _close_frac(close, high, low) <= 0.25
    return _consec_streak(cond)


def clv_032_consec_close_near_high(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days closing in top 25% of range (close-frac >= 0.75)."""
    cond = _close_frac(close, high, low) >= 0.75
    return _consec_streak(cond)


def clv_033_consec_clv_negative(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days with negative CLV (close below bar midpoint)."""
    cond = _clv_raw(close, high, low) < 0
    return _consec_streak(cond)


def clv_034_consec_clv_positive(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days with positive CLV (close above bar midpoint)."""
    cond = _clv_raw(close, high, low) > 0
    return _consec_streak(cond)


def clv_035_consec_close_below_mid(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days closing below bar midpoint."""
    mid = (high + low) / 2.0
    cond = close < mid
    return _consec_streak(cond)


def clv_036_max_consec_near_low_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max consecutive near-low-close streak within trailing 21 days."""
    cond = _close_frac(close, high, low) <= 0.25
    return _rolling_max_streak(cond, _TD_MON)


def clv_037_max_consec_near_low_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max consecutive near-low-close streak within trailing 63 days."""
    cond = _close_frac(close, high, low) <= 0.25
    return _rolling_max_streak(cond, _TD_QTR)


def clv_038_max_consec_near_low_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max consecutive near-low-close streak within trailing 252 days."""
    cond = _close_frac(close, high, low) <= 0.25
    return _rolling_max_streak(cond, _TD_YEAR)


def clv_039_consec_clv_lt_minus08(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days with CLV < -0.8 (extreme close near low)."""
    cond = _clv_raw(close, high, low) < -0.8
    return _consec_streak(cond)


def clv_040_max_consec_clv_negative_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max consecutive negative-CLV streak within trailing 63 days."""
    cond = _clv_raw(close, high, low) < 0
    return _rolling_max_streak(cond, _TD_QTR)


# --- Group E (041-050): Count of weak/strong closes in windows ---

def clv_041_count_near_low_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of near-low closes (frac<=0.25) in trailing 5 days."""
    return _rolling_count_true(_close_frac(close, high, low) <= 0.25, _TD_WEEK)


def clv_042_count_near_low_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of near-low closes (frac<=0.25) in trailing 21 days."""
    return _rolling_count_true(_close_frac(close, high, low) <= 0.25, _TD_MON)


def clv_043_count_near_low_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of near-low closes (frac<=0.25) in trailing 63 days."""
    return _rolling_count_true(_close_frac(close, high, low) <= 0.25, _TD_QTR)


def clv_044_count_near_low_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of near-low closes (frac<=0.25) in trailing 252 days."""
    return _rolling_count_true(_close_frac(close, high, low) <= 0.25, _TD_YEAR)


def clv_045_count_near_high_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of near-high closes (frac>=0.75) in trailing 21 days."""
    return _rolling_count_true(_close_frac(close, high, low) >= 0.75, _TD_MON)


def clv_046_count_near_high_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of near-high closes (frac>=0.75) in trailing 63 days."""
    return _rolling_count_true(_close_frac(close, high, low) >= 0.75, _TD_QTR)


def clv_047_frac_near_low_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 21 days closing near low (<=25% of range)."""
    return _rolling_count_true(_close_frac(close, high, low) <= 0.25, _TD_MON) / _TD_MON


def clv_048_frac_near_low_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 63 days closing near low."""
    return _rolling_count_true(_close_frac(close, high, low) <= 0.25, _TD_QTR) / _TD_QTR


def clv_049_frac_near_low_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 252 days closing near low."""
    return _rolling_count_true(_close_frac(close, high, low) <= 0.25, _TD_YEAR) / _TD_YEAR


def clv_050_low_vs_high_close_ratio_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of near-low count to near-high count over 21 days."""
    lo = _rolling_count_true(_close_frac(close, high, low) <= 0.25, _TD_MON)
    hi = _rolling_count_true(_close_frac(close, high, low) >= 0.75, _TD_MON)
    return _safe_div(lo, hi)


# --- Group F (051-060): CLV spread, std, z-score and dispersion ---

def clv_051_clv_std_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day standard deviation of CLV."""
    return _rolling_std(_clv_raw(close, high, low), _TD_MON)


def clv_052_clv_std_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day standard deviation of CLV."""
    return _rolling_std(_clv_raw(close, high, low), _TD_QTR)


def clv_053_clv_std_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day standard deviation of CLV."""
    return _rolling_std(_clv_raw(close, high, low), _TD_YEAR)


def clv_054_clv_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of CLV relative to trailing 21-day mean and std."""
    clv = _clv_raw(close, high, low)
    m = _rolling_mean(clv, _TD_MON)
    s = _rolling_std(clv, _TD_MON)
    return _safe_div(clv - m, s)


def clv_055_clv_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of CLV relative to trailing 63-day mean and std."""
    clv = _clv_raw(close, high, low)
    m = _rolling_mean(clv, _TD_QTR)
    s = _rolling_std(clv, _TD_QTR)
    return _safe_div(clv - m, s)


def clv_056_clv_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of CLV relative to trailing 252-day mean and std."""
    clv = _clv_raw(close, high, low)
    m = _rolling_mean(clv, _TD_YEAR)
    s = _rolling_std(clv, _TD_YEAR)
    return _safe_div(clv - m, s)


def clv_057_clv_min_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Trailing 21-day minimum CLV."""
    return _rolling_min(_clv_raw(close, high, low), _TD_MON)


def clv_058_clv_min_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Trailing 63-day minimum CLV."""
    return _rolling_min(_clv_raw(close, high, low), _TD_QTR)


def clv_059_clv_min_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Trailing 252-day minimum CLV."""
    return _rolling_min(_clv_raw(close, high, low), _TD_YEAR)


def clv_060_clv_max_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Trailing 21-day maximum CLV."""
    return _rolling_max(_clv_raw(close, high, low), _TD_MON)


# --- Group G (061-075): Accumulation/distribution interpretation, normalization, composites ---

def clv_061_clv_vs_sma21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CLV minus its 21-day SMA (deviation from short-term CLV baseline)."""
    clv = _clv_raw(close, high, low)
    return clv - _rolling_mean(clv, _TD_MON)


def clv_062_clv_vs_sma63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CLV minus its 63-day SMA (deviation from quarterly CLV baseline)."""
    clv = _clv_raw(close, high, low)
    return clv - _rolling_mean(clv, _TD_QTR)


def clv_063_clv_vs_sma252(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CLV minus its 252-day SMA (deviation from annual CLV baseline)."""
    clv = _clv_raw(close, high, low)
    return clv - _rolling_mean(clv, _TD_YEAR)


def clv_064_clv_cumsum_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Cumulative sum of CLV over trailing 21 days (A/D-style pressure)."""
    return _rolling_sum(_clv_raw(close, high, low), _TD_MON)


def clv_065_clv_cumsum_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Cumulative sum of CLV over trailing 63 days."""
    return _rolling_sum(_clv_raw(close, high, low), _TD_QTR)


def clv_066_clv_cumsum_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Cumulative sum of CLV over trailing 252 days."""
    return _rolling_sum(_clv_raw(close, high, low), _TD_YEAR)


def clv_067_clv_sum_neg_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of negative CLV values only over trailing 21 days (bear pressure)."""
    clv = _clv_raw(close, high, low)
    neg = clv.where(clv < 0, 0.0)
    return _rolling_sum(neg, _TD_MON)


def clv_068_clv_sum_neg_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of negative CLV values only over trailing 63 days."""
    clv = _clv_raw(close, high, low)
    neg = clv.where(clv < 0, 0.0)
    return _rolling_sum(neg, _TD_QTR)


def clv_069_clv_sum_pos_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of positive CLV values only over trailing 21 days (bull pressure)."""
    clv = _clv_raw(close, high, low)
    pos = clv.where(clv > 0, 0.0)
    return _rolling_sum(pos, _TD_MON)


def clv_070_clv_bull_bear_ratio_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of sum(positive CLV) to abs(sum(negative CLV)) over 21 days."""
    clv = _clv_raw(close, high, low)
    pos = _rolling_sum(clv.where(clv > 0, 0.0), _TD_MON)
    neg = _rolling_sum(clv.where(clv < 0, 0.0).abs(), _TD_MON)
    return _safe_div(pos, neg)


def clv_071_clv_median_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day median CLV."""
    return _rolling_median(_clv_raw(close, high, low), _TD_MON)


def clv_072_clv_median_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day median CLV."""
    return _rolling_median(_clv_raw(close, high, low), _TD_QTR)


def clv_073_clv_ema5_vs_ema21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Difference between 5-day EMA and 21-day EMA of CLV (short-term trend)."""
    clv = _clv_raw(close, high, low)
    return _ewm_mean(clv, _TD_WEEK) - _ewm_mean(clv, _TD_MON)


def clv_074_clv_ema21_vs_ema63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Difference between 21-day EMA and 63-day EMA of CLV (medium-term trend)."""
    clv = _clv_raw(close, high, low)
    return _ewm_mean(clv, _TD_MON) - _ewm_mean(clv, _TD_QTR)


def clv_075_close_frac_expanding_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding mean of close-fraction-of-range (long-run average position)."""
    return _close_frac(close, high, low).expanding(min_periods=1).mean()


# ── Registry ──────────────────────────────────────────────────────────────────

CLOSE_LOCATION_REGISTRY_001_075 = {
    "clv_001_clv_raw": {"inputs": ["close", "high", "low"], "func": clv_001_clv_raw},
    "clv_002_close_frac_of_range": {"inputs": ["close", "high", "low"], "func": clv_002_close_frac_of_range},
    "clv_003_clv_shifted1": {"inputs": ["close", "high", "low"], "func": clv_003_clv_shifted1},
    "clv_004_clv_shifted5": {"inputs": ["close", "high", "low"], "func": clv_004_clv_shifted5},
    "clv_005_clv_shifted21": {"inputs": ["close", "high", "low"], "func": clv_005_clv_shifted21},
    "clv_006_clv_abs": {"inputs": ["close", "high", "low"], "func": clv_006_clv_abs},
    "clv_007_clv_sign": {"inputs": ["close", "high", "low"], "func": clv_007_clv_sign},
    "clv_008_close_frac_complement": {"inputs": ["close", "high", "low"], "func": clv_008_close_frac_complement},
    "clv_009_clv_distance_from_mid": {"inputs": ["close", "high", "low"], "func": clv_009_clv_distance_from_mid},
    "clv_010_close_near_low_flag": {"inputs": ["close", "high", "low"], "func": clv_010_close_near_low_flag},
    "clv_011_clv_sma5": {"inputs": ["close", "high", "low"], "func": clv_011_clv_sma5},
    "clv_012_clv_sma21": {"inputs": ["close", "high", "low"], "func": clv_012_clv_sma21},
    "clv_013_clv_sma63": {"inputs": ["close", "high", "low"], "func": clv_013_clv_sma63},
    "clv_014_clv_sma126": {"inputs": ["close", "high", "low"], "func": clv_014_clv_sma126},
    "clv_015_clv_sma252": {"inputs": ["close", "high", "low"], "func": clv_015_clv_sma252},
    "clv_016_clv_ema5": {"inputs": ["close", "high", "low"], "func": clv_016_clv_ema5},
    "clv_017_clv_ema21": {"inputs": ["close", "high", "low"], "func": clv_017_clv_ema21},
    "clv_018_clv_ema63": {"inputs": ["close", "high", "low"], "func": clv_018_clv_ema63},
    "clv_019_close_frac_sma21": {"inputs": ["close", "high", "low"], "func": clv_019_close_frac_sma21},
    "clv_020_close_frac_sma63": {"inputs": ["close", "high", "low"], "func": clv_020_close_frac_sma63},
    "clv_021_clv_pct_rank_21d": {"inputs": ["close", "high", "low"], "func": clv_021_clv_pct_rank_21d},
    "clv_022_clv_pct_rank_63d": {"inputs": ["close", "high", "low"], "func": clv_022_clv_pct_rank_63d},
    "clv_023_clv_pct_rank_126d": {"inputs": ["close", "high", "low"], "func": clv_023_clv_pct_rank_126d},
    "clv_024_clv_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": clv_024_clv_pct_rank_252d},
    "clv_025_clv_expanding_pct_rank": {"inputs": ["close", "high", "low"], "func": clv_025_clv_expanding_pct_rank},
    "clv_026_close_frac_pct_rank_63d": {"inputs": ["close", "high", "low"], "func": clv_026_close_frac_pct_rank_63d},
    "clv_027_close_frac_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": clv_027_close_frac_pct_rank_252d},
    "clv_028_clv_below_minus05_flag": {"inputs": ["close", "high", "low"], "func": clv_028_clv_below_minus05_flag},
    "clv_029_clv_below_zero_flag": {"inputs": ["close", "high", "low"], "func": clv_029_clv_below_zero_flag},
    "clv_030_clv_above_plus05_flag": {"inputs": ["close", "high", "low"], "func": clv_030_clv_above_plus05_flag},
    "clv_031_consec_close_near_low": {"inputs": ["close", "high", "low"], "func": clv_031_consec_close_near_low},
    "clv_032_consec_close_near_high": {"inputs": ["close", "high", "low"], "func": clv_032_consec_close_near_high},
    "clv_033_consec_clv_negative": {"inputs": ["close", "high", "low"], "func": clv_033_consec_clv_negative},
    "clv_034_consec_clv_positive": {"inputs": ["close", "high", "low"], "func": clv_034_consec_clv_positive},
    "clv_035_consec_close_below_mid": {"inputs": ["close", "high", "low"], "func": clv_035_consec_close_below_mid},
    "clv_036_max_consec_near_low_21d": {"inputs": ["close", "high", "low"], "func": clv_036_max_consec_near_low_21d},
    "clv_037_max_consec_near_low_63d": {"inputs": ["close", "high", "low"], "func": clv_037_max_consec_near_low_63d},
    "clv_038_max_consec_near_low_252d": {"inputs": ["close", "high", "low"], "func": clv_038_max_consec_near_low_252d},
    "clv_039_consec_clv_lt_minus08": {"inputs": ["close", "high", "low"], "func": clv_039_consec_clv_lt_minus08},
    "clv_040_max_consec_clv_negative_63d": {"inputs": ["close", "high", "low"], "func": clv_040_max_consec_clv_negative_63d},
    "clv_041_count_near_low_5d": {"inputs": ["close", "high", "low"], "func": clv_041_count_near_low_5d},
    "clv_042_count_near_low_21d": {"inputs": ["close", "high", "low"], "func": clv_042_count_near_low_21d},
    "clv_043_count_near_low_63d": {"inputs": ["close", "high", "low"], "func": clv_043_count_near_low_63d},
    "clv_044_count_near_low_252d": {"inputs": ["close", "high", "low"], "func": clv_044_count_near_low_252d},
    "clv_045_count_near_high_21d": {"inputs": ["close", "high", "low"], "func": clv_045_count_near_high_21d},
    "clv_046_count_near_high_63d": {"inputs": ["close", "high", "low"], "func": clv_046_count_near_high_63d},
    "clv_047_frac_near_low_21d": {"inputs": ["close", "high", "low"], "func": clv_047_frac_near_low_21d},
    "clv_048_frac_near_low_63d": {"inputs": ["close", "high", "low"], "func": clv_048_frac_near_low_63d},
    "clv_049_frac_near_low_252d": {"inputs": ["close", "high", "low"], "func": clv_049_frac_near_low_252d},
    "clv_050_low_vs_high_close_ratio_21d": {"inputs": ["close", "high", "low"], "func": clv_050_low_vs_high_close_ratio_21d},
    "clv_051_clv_std_21d": {"inputs": ["close", "high", "low"], "func": clv_051_clv_std_21d},
    "clv_052_clv_std_63d": {"inputs": ["close", "high", "low"], "func": clv_052_clv_std_63d},
    "clv_053_clv_std_252d": {"inputs": ["close", "high", "low"], "func": clv_053_clv_std_252d},
    "clv_054_clv_zscore_21d": {"inputs": ["close", "high", "low"], "func": clv_054_clv_zscore_21d},
    "clv_055_clv_zscore_63d": {"inputs": ["close", "high", "low"], "func": clv_055_clv_zscore_63d},
    "clv_056_clv_zscore_252d": {"inputs": ["close", "high", "low"], "func": clv_056_clv_zscore_252d},
    "clv_057_clv_min_21d": {"inputs": ["close", "high", "low"], "func": clv_057_clv_min_21d},
    "clv_058_clv_min_63d": {"inputs": ["close", "high", "low"], "func": clv_058_clv_min_63d},
    "clv_059_clv_min_252d": {"inputs": ["close", "high", "low"], "func": clv_059_clv_min_252d},
    "clv_060_clv_max_21d": {"inputs": ["close", "high", "low"], "func": clv_060_clv_max_21d},
    "clv_061_clv_vs_sma21": {"inputs": ["close", "high", "low"], "func": clv_061_clv_vs_sma21},
    "clv_062_clv_vs_sma63": {"inputs": ["close", "high", "low"], "func": clv_062_clv_vs_sma63},
    "clv_063_clv_vs_sma252": {"inputs": ["close", "high", "low"], "func": clv_063_clv_vs_sma252},
    "clv_064_clv_cumsum_21d": {"inputs": ["close", "high", "low"], "func": clv_064_clv_cumsum_21d},
    "clv_065_clv_cumsum_63d": {"inputs": ["close", "high", "low"], "func": clv_065_clv_cumsum_63d},
    "clv_066_clv_cumsum_252d": {"inputs": ["close", "high", "low"], "func": clv_066_clv_cumsum_252d},
    "clv_067_clv_sum_neg_21d": {"inputs": ["close", "high", "low"], "func": clv_067_clv_sum_neg_21d},
    "clv_068_clv_sum_neg_63d": {"inputs": ["close", "high", "low"], "func": clv_068_clv_sum_neg_63d},
    "clv_069_clv_sum_pos_21d": {"inputs": ["close", "high", "low"], "func": clv_069_clv_sum_pos_21d},
    "clv_070_clv_bull_bear_ratio_21d": {"inputs": ["close", "high", "low"], "func": clv_070_clv_bull_bear_ratio_21d},
    "clv_071_clv_median_21d": {"inputs": ["close", "high", "low"], "func": clv_071_clv_median_21d},
    "clv_072_clv_median_63d": {"inputs": ["close", "high", "low"], "func": clv_072_clv_median_63d},
    "clv_073_clv_ema5_vs_ema21": {"inputs": ["close", "high", "low"], "func": clv_073_clv_ema5_vs_ema21},
    "clv_074_clv_ema21_vs_ema63": {"inputs": ["close", "high", "low"], "func": clv_074_clv_ema21_vs_ema63},
    "clv_075_close_frac_expanding_mean": {"inputs": ["close", "high", "low"], "func": clv_075_close_frac_expanding_mean},
}
