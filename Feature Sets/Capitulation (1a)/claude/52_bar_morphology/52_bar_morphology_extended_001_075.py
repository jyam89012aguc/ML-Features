"""
52_bar_morphology — Extended Features 001-075
Domain: candlestick body/range structural statistics — additional variants: body
        gap interaction, close-position-in-range, body vs range-position, body entropy,
        weekly/half-year aggregates, body autocorrelation, body-direction persistence,
        range-fill quantiles, body acceleration ratios, structural composites not
        present in the four base files.
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
    """Element-wise division; zero denominator → NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_quantile(s: pd.Series, w: int, q: float) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).quantile(q)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _body(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Signed body: close - open."""
    return close - open_


def _body_abs(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Absolute body size: |close - open|."""
    return (close - open_).abs()


def _range(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bar range: high - low (always >= 0)."""
    return (high - low).clip(lower=0.0)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _zscore(s: pd.Series, w: int) -> pd.Series:
    """Rolling z-score over window w."""
    return _safe_div(s - _rolling_mean(s, w), _rolling_std(s, w))


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Close position within the daily range ---

def bmf_ext_001_close_position_in_range(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close location within the high-low range (0 = at low, 1 = at high)."""
    return _safe_div(close - low, _range(high, low).clip(lower=_EPS))


def bmf_ext_002_open_position_in_range(open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Open location within the high-low range (0 = at low, 1 = at high)."""
    return _safe_div(open - low, _range(high, low).clip(lower=_EPS))


def bmf_ext_003_close_position_sma21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day mean of close-position-in-range (persistent weak/strong closes)."""
    return _rolling_mean(bmf_ext_001_close_position_in_range(close, high, low), _TD_MON)


def bmf_ext_004_close_position_sma63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day mean of close-position-in-range."""
    return _rolling_mean(bmf_ext_001_close_position_in_range(close, high, low), _TD_QTR)


def bmf_ext_005_weak_close_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close in bottom 20% of the day's range (weak close)."""
    return (bmf_ext_001_close_position_in_range(close, high, low) < 0.20).astype(float)


def bmf_ext_006_weak_close_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day count of weak-close days (close in bottom 20% of range)."""
    return _rolling_sum(bmf_ext_005_weak_close_flag(close, high, low), _TD_MON)


def bmf_ext_007_weak_close_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day count of weak-close days."""
    return _rolling_sum(bmf_ext_005_weak_close_flag(close, high, low), _TD_QTR)


def bmf_ext_008_weak_close_streak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive-day streak of weak closes (close in bottom 20% of range)."""
    cond = bmf_ext_001_close_position_in_range(close, high, low) < 0.20
    return _consec_streak(cond)


def bmf_ext_009_close_position_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of close-position-in-range vs trailing 63-day distribution."""
    return _zscore(bmf_ext_001_close_position_in_range(close, high, low), _TD_QTR)


def bmf_ext_010_open_to_close_position_diff(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close-position minus open-position in range (intraday drift within bar)."""
    return (bmf_ext_001_close_position_in_range(close, high, low)
            - bmf_ext_002_open_position_in_range(open, high, low))


# --- Group B (011-020): Body interaction with overnight gaps ---

def bmf_ext_011_gap_abs(open: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute overnight gap: |open - prior close|."""
    return (open - close.shift(1)).abs()


def bmf_ext_012_gap_signed(open: pd.Series, close: pd.Series) -> pd.Series:
    """Signed overnight gap: open - prior close."""
    return open - close.shift(1)


def bmf_ext_013_gap_to_body_ratio(close: pd.Series, open: pd.Series) -> pd.Series:
    """Absolute gap divided by today's absolute body (gap dominance)."""
    gap = (open - close.shift(1)).abs()
    return _safe_div(gap, _body_abs(close, open).clip(lower=_EPS))


def bmf_ext_014_gap_pct_of_close(open: pd.Series, close: pd.Series) -> pd.Series:
    """Signed overnight gap as a fraction of prior close."""
    return _safe_div(open - close.shift(1), close.shift(1).clip(lower=_EPS))


def bmf_ext_015_down_gap_flag(open: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: open below prior close (overnight down gap)."""
    return (open < close.shift(1)).astype(float)


def bmf_ext_016_down_gap_count_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day count of overnight down-gap days."""
    return _rolling_sum(bmf_ext_015_down_gap_flag(open, close), _TD_MON)


def bmf_ext_017_down_gap_count_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """63-day count of overnight down-gap days."""
    return _rolling_sum(bmf_ext_015_down_gap_flag(open, close), _TD_QTR)


def bmf_ext_018_gap_plus_body_total_move(close: pd.Series, open: pd.Series) -> pd.Series:
    """Total move = signed gap + signed body (close - prior close), as fraction of prior close."""
    total = close - close.shift(1)
    return _safe_div(total, close.shift(1).clip(lower=_EPS))


def bmf_ext_019_gap_abs_sma21(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean of absolute overnight gap."""
    return _rolling_mean((open - close.shift(1)).abs(), _TD_MON)


def bmf_ext_020_down_gap_bear_body_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day count of days with both an overnight down gap and a bear body."""
    cond = ((open < close.shift(1)) & (close < open)).astype(float)
    return _rolling_sum(cond, _TD_MON)


# --- Group C (021-030): Body relative to range position and extremes ---

def bmf_ext_021_body_high_in_range(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Body-high (max of open/close) location within the high-low range."""
    body_high = pd.concat([open, close], axis=1).max(axis=1)
    return _safe_div(body_high - low, _range(high, low).clip(lower=_EPS))


def bmf_ext_022_body_low_in_range(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Body-low (min of open/close) location within the high-low range."""
    body_low = pd.concat([open, close], axis=1).min(axis=1)
    return _safe_div(body_low - low, _range(high, low).clip(lower=_EPS))


def bmf_ext_023_body_midpoint_in_range(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Body-midpoint location within the high-low range."""
    mid = (open + close) / 2.0
    return _safe_div(mid - low, _range(high, low).clip(lower=_EPS))


def bmf_ext_024_body_midpoint_in_range_sma21(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day mean of body-midpoint location within range."""
    return _rolling_mean(bmf_ext_023_body_midpoint_in_range(close, open, high, low), _TD_MON)


def bmf_ext_025_body_to_range_pct_rank_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of body-to-range ratio within trailing 63 days."""
    btr = _safe_div(_body_abs(close, open), _range(high, low).clip(lower=_EPS))
    return btr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def bmf_ext_026_body_to_range_pct_rank_126d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of body-to-range ratio within trailing 126 days."""
    btr = _safe_div(_body_abs(close, open), _range(high, low).clip(lower=_EPS))
    return btr.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def bmf_ext_027_body_to_range_zscore_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of body-to-range ratio within trailing 63 days."""
    btr = _safe_div(_body_abs(close, open), _range(high, low).clip(lower=_EPS))
    return _zscore(btr, _TD_QTR)


def bmf_ext_028_body_to_range_zscore_252d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of body-to-range ratio within trailing 252 days."""
    btr = _safe_div(_body_abs(close, open), _range(high, low).clip(lower=_EPS))
    return _zscore(btr, _TD_YEAR)


def bmf_ext_029_full_range_body_flag(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: body-to-range ratio >= 0.95 (near-complete range fill)."""
    btr = _safe_div(_body_abs(close, open), _range(high, low).clip(lower=_EPS))
    return (btr >= 0.95).astype(float)


def bmf_ext_030_full_range_body_count_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day count of near-complete-range-fill bars (body/range >= 0.95)."""
    return _rolling_sum(bmf_ext_029_full_range_body_flag(close, open, high, low), _TD_QTR)


# --- Group D (031-040): Body-direction persistence and run statistics ---

def bmf_ext_031_body_sign(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sign of the signed body (+1 bull, -1 bear, 0 flat)."""
    return np.sign(_body(close, open)).astype(float)


def bmf_ext_032_body_sign_autocorr_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day autocorrelation (lag 1) of body sign (direction persistence)."""
    sign = np.sign(_body(close, open))
    return sign.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        lambda a: pd.Series(a).autocorr(lag=1), raw=False)


def bmf_ext_033_signed_body_autocorr_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day autocorrelation (lag 1) of signed body size."""
    body = _body(close, open)
    return body.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        lambda a: pd.Series(a).autocorr(lag=1), raw=False)


def bmf_ext_034_bear_run_persistence_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current bear-body streak divided by 21-day mean bear streak (persistence ratio)."""
    streak = _consec_streak(close < open)
    return _safe_div(streak, _rolling_mean(streak, _TD_MON))


def bmf_ext_035_bear_body_run_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day count of distinct bear-body runs (run starts) — clustering of down days."""
    bear = (close < open)
    prev_bear = bear.shift(1, fill_value=False)
    run_start = (bear & ~prev_bear).astype(float)
    return _rolling_sum(run_start, _TD_MON)


def bmf_ext_036_two_bear_in_row_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: today and prior day both bear bodies (two consecutive down candles)."""
    bear = close < open
    return (bear & bear.shift(1, fill_value=False)).astype(float)


def bmf_ext_037_three_bear_in_row_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: three consecutive bear-body candles ending today."""
    bear = close < open
    b1 = bear.shift(1, fill_value=False)
    b2 = bear.shift(2, fill_value=False)
    return (bear & b1 & b2).astype(float)


def bmf_ext_038_three_bear_count_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day count of three-consecutive-bear-body occurrences."""
    return _rolling_sum(bmf_ext_037_three_bear_in_row_flag(close, open), _TD_QTR)


def bmf_ext_039_bear_body_fraction_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of bear-body bars in trailing 5 days (weekly down pressure)."""
    return _rolling_mean((close < open).astype(float), _TD_WEEK)


def bmf_ext_040_bear_body_fraction_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of bear-body bars in trailing 126 days (half-year down pressure)."""
    return _rolling_mean((close < open).astype(float), _TD_HALF)


# --- Group E (041-050): Body magnitude — weekly/half-year aggregates and ratios ---

def bmf_ext_041_body_abs_sma10(close: pd.Series, open: pd.Series) -> pd.Series:
    """10-day SMA of absolute body size (two-week body level)."""
    return _rolling_mean(_body_abs(close, open), 10)


def bmf_ext_042_body_abs_sma126(close: pd.Series, open: pd.Series) -> pd.Series:
    """126-day SMA of absolute body size (half-year body level)."""
    return _rolling_mean(_body_abs(close, open), _TD_HALF)


def bmf_ext_043_body_abs_ema63(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day EMA of absolute body size."""
    return _ewm_mean(_body_abs(close, open), _TD_QTR)


def bmf_ext_044_body_abs_max_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """252-day rolling maximum absolute body size (largest candle in a year)."""
    return _rolling_max(_body_abs(close, open), _TD_YEAR)


def bmf_ext_045_body_abs_min_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day rolling minimum absolute body size (smallest candle recently)."""
    return _rolling_min(_body_abs(close, open), _TD_MON)


def bmf_ext_046_body_abs_norm_by_sma252(close: pd.Series, open: pd.Series) -> pd.Series:
    """Today's absolute body normalized by its 252-day SMA."""
    babs = _body_abs(close, open)
    return _safe_div(babs, _rolling_mean(babs, _TD_YEAR))


def bmf_ext_047_body_abs_norm_by_median63(close: pd.Series, open: pd.Series) -> pd.Series:
    """Today's absolute body normalized by its 63-day rolling median (robust scaling)."""
    babs = _body_abs(close, open)
    return _safe_div(babs, _rolling_median(babs, _TD_QTR).clip(lower=_EPS))


def bmf_ext_048_body_abs_ema21_vs_ema63(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 21-day EMA body to 63-day EMA body (medium-term body momentum)."""
    babs = _body_abs(close, open)
    return _safe_div(_ewm_mean(babs, _TD_MON), _ewm_mean(babs, _TD_QTR))


def bmf_ext_049_body_abs_range_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day range (max - min) of absolute body size (body-size dispersion)."""
    babs = _body_abs(close, open)
    return _rolling_max(babs, _TD_MON) - _rolling_min(babs, _TD_MON)


def bmf_ext_050_body_abs_zscore_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of absolute body size within trailing 126-day window."""
    return _zscore(_body_abs(close, open), _TD_HALF)


# --- Group F (051-060): Range structure and range-fill dynamics ---

def bmf_ext_051_range_pct_of_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bar range as a fraction of closing price (normalized daily range)."""
    return _safe_div(_range(high, low), close.clip(lower=_EPS))


def bmf_ext_052_range_pct_of_close_sma21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean of range-as-fraction-of-close."""
    return _rolling_mean(bmf_ext_051_range_pct_of_close(high, low, close), _TD_MON)


def bmf_ext_053_range_zscore_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of bar range within trailing 63 days."""
    return _zscore(_range(high, low), _TD_QTR)


def bmf_ext_054_range_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of bar range within trailing 252 days."""
    return _zscore(_range(high, low), _TD_YEAR)


def bmf_ext_055_range_expansion_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's range exceeds 2x its 21-day mean (range-expansion bar)."""
    rng = _range(high, low)
    return (rng > 2.0 * _rolling_mean(rng, _TD_MON)).astype(float)


def bmf_ext_056_range_expansion_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day count of range-expansion bars (range > 2x 21-day mean)."""
    return _rolling_sum(bmf_ext_055_range_expansion_flag(high, low), _TD_QTR)


def bmf_ext_057_range_vs_prior_ratio(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's range divided by prior day's range (daily range change)."""
    rng = _range(high, low)
    return _safe_div(rng, rng.shift(1).clip(lower=_EPS))


def bmf_ext_058_range_pct_rank_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of bar range within trailing 252 days."""
    return _range(high, low).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def bmf_ext_059_range_sum_5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day rolling sum of bar range (cumulative weekly travel)."""
    return _rolling_sum(_range(high, low), _TD_WEEK)


def bmf_ext_060_range_cv_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of bar range over 63 days."""
    rng = _range(high, low)
    return _safe_div(_rolling_std(rng, _TD_QTR), _rolling_mean(rng, _TD_QTR))


# --- Group G (061-068): Body-shape entropy and distributional structure ---

def bmf_ext_061_body_to_range_skew_252d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day rolling skewness of body-to-range ratio."""
    btr = _safe_div(_body_abs(close, open), _range(high, low).clip(lower=_EPS))
    return btr.rolling(_TD_YEAR, min_periods=max(5, _TD_YEAR // 2)).skew()


def bmf_ext_062_body_to_range_kurt_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day rolling kurtosis of body-to-range ratio."""
    btr = _safe_div(_body_abs(close, open), _range(high, low).clip(lower=_EPS))
    return btr.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).kurt()


def bmf_ext_063_body_abs_kurt_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day rolling kurtosis of absolute body size (tail-heaviness of bodies)."""
    return _body_abs(close, open).rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).kurt()


def bmf_ext_064_body_to_range_iqr_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day interquartile range of body-to-range ratio."""
    btr = _safe_div(_body_abs(close, open), _range(high, low).clip(lower=_EPS))
    return _rolling_quantile(btr, _TD_QTR, 0.75) - _rolling_quantile(btr, _TD_QTR, 0.25)


def bmf_ext_065_body_to_range_median_252d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day rolling median of body-to-range ratio (annual typical fill)."""
    btr = _safe_div(_body_abs(close, open), _range(high, low).clip(lower=_EPS))
    return _rolling_median(btr, _TD_YEAR)


def bmf_ext_066_body_direction_entropy_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary entropy of bull/bear body mix over 21 days (0 = trending, 1 = balanced)."""
    bull_frac = _rolling_mean((close > open).astype(float), _TD_MON).clip(_EPS, 1.0 - _EPS)
    p = bull_frac
    return -(p * np.log2(p) + (1.0 - p) * np.log2(1.0 - p))


def bmf_ext_067_body_direction_entropy_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary entropy of bull/bear body mix over 63 days."""
    bull_frac = _rolling_mean((close > open).astype(float), _TD_QTR).clip(_EPS, 1.0 - _EPS)
    p = bull_frac
    return -(p * np.log2(p) + (1.0 - p) * np.log2(1.0 - p))


def bmf_ext_068_body_to_range_q25_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day 25th percentile of body-to-range ratio (how doji-prone bars are)."""
    btr = _safe_div(_body_abs(close, open), _range(high, low).clip(lower=_EPS))
    return _rolling_quantile(btr, _TD_QTR, 0.25)


# --- Group H (069-075): Body acceleration, momentum ratios and composites ---

def bmf_ext_069_body_5d_pct_change_zscore_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of 5-day body percent change within trailing 63 days."""
    babs = _body_abs(close, open)
    pc = _safe_div(babs - babs.shift(_TD_WEEK), babs.shift(_TD_WEEK).clip(lower=_EPS))
    return _zscore(pc, _TD_QTR)


def bmf_ext_070_signed_body_ema21_vs_ema63(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day EMA of signed body minus 63-day EMA of signed body (directional momentum)."""
    body = _body(close, open)
    return _ewm_mean(body, _TD_MON) - _ewm_mean(body, _TD_QTR)


def bmf_ext_071_body_acceleration_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day second difference of absolute body size (weekly body acceleration)."""
    return _body_abs(close, open).diff(_TD_WEEK).diff(_TD_WEEK)


def bmf_ext_072_signed_body_sum_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day rolling sum of signed body (net weekly body pressure)."""
    return _rolling_sum(_body(close, open), _TD_WEEK)


def bmf_ext_073_signed_body_sum_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """252-day rolling sum of signed body (net annual body pressure)."""
    return _rolling_sum(_body(close, open), _TD_YEAR)


def bmf_ext_074_bear_capitulation_bar_flag(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: large bear marubozu-style bar — body z-score(63d)>2, bear body, weak close."""
    babs = _body_abs(close, open)
    bz = _zscore(babs, _TD_QTR)
    weak_close = bmf_ext_001_close_position_in_range(close, high, low) < 0.20
    return ((bz > 2.0) & (close < open) & weak_close).astype(float)


def bmf_ext_075_bar_capitulation_composite(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Capitulation composite: body z-score(63d) + (1 - close-position) + body-to-range ratio.
    Higher = larger bar closing weak with full-range fill (distress bar)."""
    babs = _body_abs(close, open)
    bz = _zscore(babs, _TD_QTR).fillna(0.0).clip(-3.0, 3.0) / 3.0
    weak = 1.0 - bmf_ext_001_close_position_in_range(close, high, low).fillna(0.5)
    btr = _safe_div(babs, _range(high, low).clip(lower=_EPS)).fillna(0.0)
    return bz + weak + btr


# ── Registry ──────────────────────────────────────────────────────────────────

BAR_MORPHOLOGY_EXTENDED_REGISTRY_001_075 = {
    "bmf_ext_001_close_position_in_range": {"inputs": ["close", "high", "low"], "func": bmf_ext_001_close_position_in_range},
    "bmf_ext_002_open_position_in_range": {"inputs": ["open", "high", "low"], "func": bmf_ext_002_open_position_in_range},
    "bmf_ext_003_close_position_sma21": {"inputs": ["close", "high", "low"], "func": bmf_ext_003_close_position_sma21},
    "bmf_ext_004_close_position_sma63": {"inputs": ["close", "high", "low"], "func": bmf_ext_004_close_position_sma63},
    "bmf_ext_005_weak_close_flag": {"inputs": ["close", "high", "low"], "func": bmf_ext_005_weak_close_flag},
    "bmf_ext_006_weak_close_count_21d": {"inputs": ["close", "high", "low"], "func": bmf_ext_006_weak_close_count_21d},
    "bmf_ext_007_weak_close_count_63d": {"inputs": ["close", "high", "low"], "func": bmf_ext_007_weak_close_count_63d},
    "bmf_ext_008_weak_close_streak": {"inputs": ["close", "high", "low"], "func": bmf_ext_008_weak_close_streak},
    "bmf_ext_009_close_position_zscore_63d": {"inputs": ["close", "high", "low"], "func": bmf_ext_009_close_position_zscore_63d},
    "bmf_ext_010_open_to_close_position_diff": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_010_open_to_close_position_diff},
    "bmf_ext_011_gap_abs": {"inputs": ["open", "close"], "func": bmf_ext_011_gap_abs},
    "bmf_ext_012_gap_signed": {"inputs": ["open", "close"], "func": bmf_ext_012_gap_signed},
    "bmf_ext_013_gap_to_body_ratio": {"inputs": ["close", "open"], "func": bmf_ext_013_gap_to_body_ratio},
    "bmf_ext_014_gap_pct_of_close": {"inputs": ["open", "close"], "func": bmf_ext_014_gap_pct_of_close},
    "bmf_ext_015_down_gap_flag": {"inputs": ["open", "close"], "func": bmf_ext_015_down_gap_flag},
    "bmf_ext_016_down_gap_count_21d": {"inputs": ["open", "close"], "func": bmf_ext_016_down_gap_count_21d},
    "bmf_ext_017_down_gap_count_63d": {"inputs": ["open", "close"], "func": bmf_ext_017_down_gap_count_63d},
    "bmf_ext_018_gap_plus_body_total_move": {"inputs": ["close", "open"], "func": bmf_ext_018_gap_plus_body_total_move},
    "bmf_ext_019_gap_abs_sma21": {"inputs": ["open", "close"], "func": bmf_ext_019_gap_abs_sma21},
    "bmf_ext_020_down_gap_bear_body_count_21d": {"inputs": ["close", "open"], "func": bmf_ext_020_down_gap_bear_body_count_21d},
    "bmf_ext_021_body_high_in_range": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_021_body_high_in_range},
    "bmf_ext_022_body_low_in_range": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_022_body_low_in_range},
    "bmf_ext_023_body_midpoint_in_range": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_023_body_midpoint_in_range},
    "bmf_ext_024_body_midpoint_in_range_sma21": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_024_body_midpoint_in_range_sma21},
    "bmf_ext_025_body_to_range_pct_rank_63d": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_025_body_to_range_pct_rank_63d},
    "bmf_ext_026_body_to_range_pct_rank_126d": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_026_body_to_range_pct_rank_126d},
    "bmf_ext_027_body_to_range_zscore_63d": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_027_body_to_range_zscore_63d},
    "bmf_ext_028_body_to_range_zscore_252d": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_028_body_to_range_zscore_252d},
    "bmf_ext_029_full_range_body_flag": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_029_full_range_body_flag},
    "bmf_ext_030_full_range_body_count_63d": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_030_full_range_body_count_63d},
    "bmf_ext_031_body_sign": {"inputs": ["close", "open"], "func": bmf_ext_031_body_sign},
    "bmf_ext_032_body_sign_autocorr_63d": {"inputs": ["close", "open"], "func": bmf_ext_032_body_sign_autocorr_63d},
    "bmf_ext_033_signed_body_autocorr_63d": {"inputs": ["close", "open"], "func": bmf_ext_033_signed_body_autocorr_63d},
    "bmf_ext_034_bear_run_persistence_21d": {"inputs": ["close", "open"], "func": bmf_ext_034_bear_run_persistence_21d},
    "bmf_ext_035_bear_body_run_count_21d": {"inputs": ["close", "open"], "func": bmf_ext_035_bear_body_run_count_21d},
    "bmf_ext_036_two_bear_in_row_flag": {"inputs": ["close", "open"], "func": bmf_ext_036_two_bear_in_row_flag},
    "bmf_ext_037_three_bear_in_row_flag": {"inputs": ["close", "open"], "func": bmf_ext_037_three_bear_in_row_flag},
    "bmf_ext_038_three_bear_count_63d": {"inputs": ["close", "open"], "func": bmf_ext_038_three_bear_count_63d},
    "bmf_ext_039_bear_body_fraction_5d": {"inputs": ["close", "open"], "func": bmf_ext_039_bear_body_fraction_5d},
    "bmf_ext_040_bear_body_fraction_126d": {"inputs": ["close", "open"], "func": bmf_ext_040_bear_body_fraction_126d},
    "bmf_ext_041_body_abs_sma10": {"inputs": ["close", "open"], "func": bmf_ext_041_body_abs_sma10},
    "bmf_ext_042_body_abs_sma126": {"inputs": ["close", "open"], "func": bmf_ext_042_body_abs_sma126},
    "bmf_ext_043_body_abs_ema63": {"inputs": ["close", "open"], "func": bmf_ext_043_body_abs_ema63},
    "bmf_ext_044_body_abs_max_252d": {"inputs": ["close", "open"], "func": bmf_ext_044_body_abs_max_252d},
    "bmf_ext_045_body_abs_min_21d": {"inputs": ["close", "open"], "func": bmf_ext_045_body_abs_min_21d},
    "bmf_ext_046_body_abs_norm_by_sma252": {"inputs": ["close", "open"], "func": bmf_ext_046_body_abs_norm_by_sma252},
    "bmf_ext_047_body_abs_norm_by_median63": {"inputs": ["close", "open"], "func": bmf_ext_047_body_abs_norm_by_median63},
    "bmf_ext_048_body_abs_ema21_vs_ema63": {"inputs": ["close", "open"], "func": bmf_ext_048_body_abs_ema21_vs_ema63},
    "bmf_ext_049_body_abs_range_21d": {"inputs": ["close", "open"], "func": bmf_ext_049_body_abs_range_21d},
    "bmf_ext_050_body_abs_zscore_126d": {"inputs": ["close", "open"], "func": bmf_ext_050_body_abs_zscore_126d},
    "bmf_ext_051_range_pct_of_close": {"inputs": ["high", "low", "close"], "func": bmf_ext_051_range_pct_of_close},
    "bmf_ext_052_range_pct_of_close_sma21": {"inputs": ["high", "low", "close"], "func": bmf_ext_052_range_pct_of_close_sma21},
    "bmf_ext_053_range_zscore_63d": {"inputs": ["high", "low"], "func": bmf_ext_053_range_zscore_63d},
    "bmf_ext_054_range_zscore_252d": {"inputs": ["high", "low"], "func": bmf_ext_054_range_zscore_252d},
    "bmf_ext_055_range_expansion_flag": {"inputs": ["high", "low"], "func": bmf_ext_055_range_expansion_flag},
    "bmf_ext_056_range_expansion_count_63d": {"inputs": ["high", "low"], "func": bmf_ext_056_range_expansion_count_63d},
    "bmf_ext_057_range_vs_prior_ratio": {"inputs": ["high", "low"], "func": bmf_ext_057_range_vs_prior_ratio},
    "bmf_ext_058_range_pct_rank_252d": {"inputs": ["high", "low"], "func": bmf_ext_058_range_pct_rank_252d},
    "bmf_ext_059_range_sum_5d": {"inputs": ["high", "low"], "func": bmf_ext_059_range_sum_5d},
    "bmf_ext_060_range_cv_63d": {"inputs": ["high", "low"], "func": bmf_ext_060_range_cv_63d},
    "bmf_ext_061_body_to_range_skew_252d": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_061_body_to_range_skew_252d},
    "bmf_ext_062_body_to_range_kurt_63d": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_062_body_to_range_kurt_63d},
    "bmf_ext_063_body_abs_kurt_63d": {"inputs": ["close", "open"], "func": bmf_ext_063_body_abs_kurt_63d},
    "bmf_ext_064_body_to_range_iqr_63d": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_064_body_to_range_iqr_63d},
    "bmf_ext_065_body_to_range_median_252d": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_065_body_to_range_median_252d},
    "bmf_ext_066_body_direction_entropy_21d": {"inputs": ["close", "open"], "func": bmf_ext_066_body_direction_entropy_21d},
    "bmf_ext_067_body_direction_entropy_63d": {"inputs": ["close", "open"], "func": bmf_ext_067_body_direction_entropy_63d},
    "bmf_ext_068_body_to_range_q25_63d": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_068_body_to_range_q25_63d},
    "bmf_ext_069_body_5d_pct_change_zscore_63d": {"inputs": ["close", "open"], "func": bmf_ext_069_body_5d_pct_change_zscore_63d},
    "bmf_ext_070_signed_body_ema21_vs_ema63": {"inputs": ["close", "open"], "func": bmf_ext_070_signed_body_ema21_vs_ema63},
    "bmf_ext_071_body_acceleration_5d": {"inputs": ["close", "open"], "func": bmf_ext_071_body_acceleration_5d},
    "bmf_ext_072_signed_body_sum_5d": {"inputs": ["close", "open"], "func": bmf_ext_072_signed_body_sum_5d},
    "bmf_ext_073_signed_body_sum_252d": {"inputs": ["close", "open"], "func": bmf_ext_073_signed_body_sum_252d},
    "bmf_ext_074_bear_capitulation_bar_flag": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_074_bear_capitulation_bar_flag},
    "bmf_ext_075_bar_capitulation_composite": {"inputs": ["close", "open", "high", "low"], "func": bmf_ext_075_bar_capitulation_composite},
}
