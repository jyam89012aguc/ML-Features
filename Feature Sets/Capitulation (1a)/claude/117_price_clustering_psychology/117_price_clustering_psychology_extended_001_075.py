"""
117_price_clustering_psychology — Extended Features 001-075
Domain: price-level psychology and digit clustering — deeper variants, multi-scale
        round-level confluence, regime flags, volume-weighted round-level proximity,
        additional distress zone dynamics, non-standard increments, clustering
        statistics, and capitulation composite scores.
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
    """Rolling fraction of bars where price is within tol of a round increment."""
    near = (_dist_to_round(price, increment) <= tol).astype(float)
    return _rolling_sum(near, window) / window


# ── Extended Feature Functions 001-075 ────────────────────────────────────────

# --- Group A (001-010): Non-standard round increments ---

def pcp_ext_001_dist_to_nearest_2dollar(close: pd.Series) -> pd.Series:
    """Absolute distance from close to nearest $2 level."""
    return _dist_to_round(close, 2.0)


def pcp_ext_002_dist_to_nearest_2dollar_pct(close: pd.Series) -> pd.Series:
    """$2-level distance as fraction of price."""
    return _safe_div(_dist_to_round(close, 2.0), close.clip(lower=_EPS))


def pcp_ext_003_dist_to_nearest_3dollar(close: pd.Series) -> pd.Series:
    """Absolute distance from close to nearest $3 level."""
    return _dist_to_round(close, 3.0)


def pcp_ext_004_dist_to_nearest_quarter(close: pd.Series) -> pd.Series:
    """Absolute distance from close to nearest $0.25 level (quarter-dollar clustering)."""
    return _dist_to_round(close, 0.25)


def pcp_ext_005_dist_to_nearest_half_dollar(close: pd.Series) -> pd.Series:
    """Absolute distance from close to nearest $0.50 level."""
    return _dist_to_round(close, 0.50)


def pcp_ext_006_dist_to_nearest_20dollar(close: pd.Series) -> pd.Series:
    """Absolute distance from close to nearest $20 level."""
    return _dist_to_round(close, 20.0)


def pcp_ext_007_dist_to_nearest_20dollar_pct(close: pd.Series) -> pd.Series:
    """$20-level distance as fraction of price."""
    return _safe_div(_dist_to_round(close, 20.0), close.clip(lower=_EPS))


def pcp_ext_008_dist_to_nearest_100dollar(close: pd.Series) -> pd.Series:
    """Absolute distance from close to nearest $100 level."""
    return _dist_to_round(close, 100.0)


def pcp_ext_009_at_quarter_dollar_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close within $0.02 of a $0.25 increment."""
    return (_dist_to_round(close, 0.25) <= 0.02).astype(float)


def pcp_ext_010_at_half_dollar_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close within $0.03 of a $0.50 level."""
    return (_dist_to_round(close, 0.50) <= 0.03).astype(float)


# --- Group B (011-020): Longer-window fraction near round levels ---

def pcp_ext_011_frac_near_dollar_126d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 126 days close within $0.05 of a whole dollar."""
    return _frac_near_round(close, 1.0, 0.05, _TD_HALF)


def pcp_ext_012_frac_near_5dollar_126d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 126 days close within $0.10 of a $5 level."""
    return _frac_near_round(close, 5.0, 0.10, _TD_HALF)


def pcp_ext_013_frac_near_quarter_dollar_21d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days close within $0.02 of a $0.25 level."""
    return _frac_near_round(close, 0.25, 0.02, _TD_MON)


def pcp_ext_014_frac_near_half_dollar_21d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days close within $0.03 of a $0.50 level."""
    return _frac_near_round(close, 0.50, 0.03, _TD_MON)


def pcp_ext_015_frac_near_10dollar_126d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 126 days close within $0.10 of a $10 level."""
    return _frac_near_round(close, 10.0, 0.10, _TD_HALF)


def pcp_ext_016_frac_zero_cents_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where close cents component < $0.05."""
    flag = (close % 1.0 < 0.05).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


def pcp_ext_017_frac_50cents_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where close cents in [0.45, 0.55)."""
    cents = close % 1.0
    flag = ((cents >= 0.45) & (cents < 0.55)).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


def pcp_ext_018_frac_near_dollar_5d_expanding(close: pd.Series) -> pd.Series:
    """Expanding fraction of all days where close within $0.05 of a whole dollar."""
    near = (_dist_to_round(close, 1.0) <= 0.05).astype(float)
    return near.expanding(min_periods=1).mean()


def pcp_ext_019_frac_sub5_126d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 126 days where close < $5."""
    return _rolling_sum((close < 5.0).astype(float), _TD_HALF) / _TD_HALF


def pcp_ext_020_frac_sub1_126d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 126 days where close < $1."""
    return _rolling_sum((close < 1.0).astype(float), _TD_HALF) / _TD_HALF


# --- Group C (021-030): Weighted-close and HL-midpoint round-level features ---

def pcp_ext_021_weighted_close_dist_to_dollar(close: pd.Series, high: pd.Series,
                                               low: pd.Series) -> pd.Series:
    """Distance of weighted close (H+L+2C)/4 to nearest whole dollar."""
    wc = (high + low + 2.0 * close) / 4.0
    return _dist_to_round(wc, 1.0)


def pcp_ext_022_hl_midpoint_dist_to_dollar(high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of HL midpoint (H+L)/2 to nearest whole dollar."""
    mid = (high + low) / 2.0
    return _dist_to_round(mid, 1.0)


def pcp_ext_023_hl_midpoint_dist_to_5dollar(high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of HL midpoint to nearest $5 level."""
    mid = (high + low) / 2.0
    return _dist_to_round(mid, 5.0)


def pcp_ext_024_hl_midpoint_sub5_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: HL midpoint < $5."""
    mid = (high + low) / 2.0
    return (mid < 5.0).astype(float)


def pcp_ext_025_weighted_close_sub5_flag(close: pd.Series, high: pd.Series,
                                          low: pd.Series) -> pd.Series:
    """Binary flag: weighted close (H+L+2C)/4 < $5."""
    wc = (high + low + 2.0 * close) / 4.0
    return (wc < 5.0).astype(float)


def pcp_ext_026_hl_midpoint_pct_thru_dollar_zone(high: pd.Series,
                                                   low: pd.Series) -> pd.Series:
    """Position of HL midpoint within its current whole-dollar zone (0=floor, 1=ceiling)."""
    mid = (high + low) / 2.0
    return mid % 1.0


def pcp_ext_027_hl_midpoint_near_dollar_21d_frac(high: pd.Series,
                                                   low: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days HL midpoint within $0.05 of a whole dollar."""
    mid = (high + low) / 2.0
    return _frac_near_round(mid, 1.0, 0.05, _TD_MON)


def pcp_ext_028_typical_price_dist_to_dollar(close: pd.Series, high: pd.Series,
                                              low: pd.Series) -> pd.Series:
    """Distance of typical price (H+L+C)/3 to nearest whole dollar."""
    tp = (high + low + close) / 3.0
    return _dist_to_round(tp, 1.0)


def pcp_ext_029_typical_price_sub5_flag(close: pd.Series, high: pd.Series,
                                         low: pd.Series) -> pd.Series:
    """Binary flag: typical price (H+L+C)/3 < $5."""
    tp = (high + low + close) / 3.0
    return (tp < 5.0).astype(float)


def pcp_ext_030_close_minus_hl_midpoint_dist_to_dollar_diff(close: pd.Series,
                                                             high: pd.Series,
                                                             low: pd.Series) -> pd.Series:
    """Difference: close dist-to-dollar minus HL-midpoint dist-to-dollar."""
    mid = (high + low) / 2.0
    return _dist_to_round(close, 1.0) - _dist_to_round(mid, 1.0)


# --- Group D (031-040): Volume-weighted round-level features ---

def pcp_ext_031_vwap_dist_to_dollar_proxy(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21d VWAP proxy dist-to-dollar: |VWAP - nearest dollar|."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_MON),
                     _rolling_sum(volume, _TD_MON).clip(lower=_EPS))
    return _dist_to_round(vwap, 1.0)


def pcp_ext_032_vwap_sub5_flag_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: rolling 21d VWAP proxy < $5."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_MON),
                     _rolling_sum(volume, _TD_MON).clip(lower=_EPS))
    return (vwap < 5.0).astype(float)


def pcp_ext_033_vwap_dist_to_5dollar_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21d VWAP proxy dist-to-$5 level."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_MON),
                     _rolling_sum(volume, _TD_MON).clip(lower=_EPS))
    return _dist_to_round(vwap, 5.0)


def pcp_ext_034_vol_weighted_dist_dollar_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average of distance-to-nearest-dollar over trailing 21 days."""
    d = _dist_to_round(close, 1.0)
    return _safe_div(_rolling_sum(d * volume, _TD_MON),
                     _rolling_sum(volume, _TD_MON).clip(lower=_EPS))


def pcp_ext_035_vol_weighted_sub5_depth_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average of depth-below-$5 over trailing 21 days."""
    depth = (5.0 - close).clip(lower=0.0)
    return _safe_div(_rolling_sum(depth * volume, _TD_MON),
                     _rolling_sum(volume, _TD_MON).clip(lower=_EPS))


def pcp_ext_036_vol_near_dollar_excess_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Excess volume on near-dollar days vs off-dollar days (trailing 21d ratio)."""
    near = (_dist_to_round(close, 1.0) <= 0.05).astype(float)
    far = 1.0 - near
    avg_near = _safe_div(_rolling_sum(near * volume, _TD_MON),
                         _rolling_sum(near, _TD_MON).clip(lower=_EPS))
    avg_far = _safe_div(_rolling_sum(far * volume, _TD_MON),
                        _rolling_sum(far, _TD_MON).clip(lower=_EPS))
    return _safe_div(avg_near, avg_far.clip(lower=_EPS))


def pcp_ext_037_vol_on_sub5_vs_above5_ratio_63d(close: pd.Series,
                                                  volume: pd.Series) -> pd.Series:
    """Ratio of avg daily volume when sub-$5 to avg daily volume when above-$5 (63d)."""
    sub5 = (close < 5.0).astype(float)
    above5 = 1.0 - sub5
    avg_sub = _safe_div(_rolling_sum(sub5 * volume, _TD_QTR),
                        _rolling_sum(sub5, _TD_QTR).clip(lower=_EPS))
    avg_above = _safe_div(_rolling_sum(above5 * volume, _TD_QTR),
                          _rolling_sum(above5, _TD_QTR).clip(lower=_EPS))
    return _safe_div(avg_sub, avg_above.clip(lower=_EPS))


def pcp_ext_038_dollar_vol_at_sub5_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total dollar volume (close * volume) on sub-$5 days, trailing 21d."""
    sub5 = (close < 5.0).astype(float)
    return _rolling_sum(sub5 * close * volume, _TD_MON)


def pcp_ext_039_dollar_vol_at_sub5_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total dollar volume on sub-$5 days, trailing 63d."""
    sub5 = (close < 5.0).astype(float)
    return _rolling_sum(sub5 * close * volume, _TD_QTR)


def pcp_ext_040_vol_fraction_near_5dollar_21d(close: pd.Series,
                                               volume: pd.Series) -> pd.Series:
    """Fraction of 21-day volume on days close within $0.10 of a $5 level."""
    near = (_dist_to_round(close, 5.0) <= 0.10).astype(float)
    return _safe_div(_rolling_sum(near * volume, _TD_MON),
                     _rolling_sum(volume, _TD_MON).clip(lower=_EPS))


# --- Group E (041-050): Distress zone regime flags and durations ---

def pcp_ext_041_sub5_regime_fraction_252d(close: pd.Series) -> pd.Series:
    """Expanding fraction of all time (capped to 252d) in sub-$5 regime."""
    return _rolling_sum((close < 5.0).astype(float), _TD_YEAR) / _TD_YEAR


def pcp_ext_042_sub5_entry_count_252d(close: pd.Series) -> pd.Series:
    """Number of times close crossed below $5 in trailing 252 days."""
    cross = ((close < 5.0) & (close.shift(1) >= 5.0)).astype(float)
    return _rolling_sum(cross, _TD_YEAR)


def pcp_ext_043_sub5_exit_count_252d(close: pd.Series) -> pd.Series:
    """Number of times close recovered above $5 in trailing 252 days."""
    cross = ((close >= 5.0) & (close.shift(1) < 5.0)).astype(float)
    return _rolling_sum(cross, _TD_YEAR)


def pcp_ext_044_sub10_regime_entry_count_252d(close: pd.Series) -> pd.Series:
    """Number of times close crossed below $10 in trailing 252 days."""
    cross = ((close < 10.0) & (close.shift(1) >= 10.0)).astype(float)
    return _rolling_sum(cross, _TD_YEAR)


def pcp_ext_045_sub1_regime_entry_count_252d(close: pd.Series) -> pd.Series:
    """Number of times close crossed below $1 in trailing 252 days."""
    cross = ((close < 1.0) & (close.shift(1) >= 1.0)).astype(float)
    return _rolling_sum(cross, _TD_YEAR)


def pcp_ext_046_consec_sub5_max_in_252d(close: pd.Series) -> pd.Series:
    """Longest consecutive-day sub-$5 streak seen in trailing 252 days."""
    streak = _consec_streak(close < 5.0)
    return _rolling_max(streak, _TD_YEAR)


def pcp_ext_047_consec_sub10_max_in_252d(close: pd.Series) -> pd.Series:
    """Longest consecutive-day sub-$10 streak seen in trailing 252 days."""
    streak = _consec_streak(close < 10.0)
    return _rolling_max(streak, _TD_YEAR)


def pcp_ext_048_sub5_bounce_back_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close recovered to above $5 today after being below $5 yesterday."""
    return ((close >= 5.0) & (close.shift(1) < 5.0)).astype(float)


def pcp_ext_049_sub5_new_low_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close < $5 and is a new 252-day low."""
    mn252 = _rolling_min(close, _TD_YEAR)
    return ((close < 5.0) & (close <= mn252 + _EPS)).astype(float)


def pcp_ext_050_sub1_new_low_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close < $1 and is a new 252-day low."""
    mn252 = _rolling_min(close, _TD_YEAR)
    return ((close < 1.0) & (close <= mn252 + _EPS)).astype(float)


# --- Group F (051-060): Clustering statistics and dispersion ---

def pcp_ext_051_dist_dollar_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of dist-to-nearest-dollar in trailing 252-day distribution."""
    d = _dist_to_round(close, 1.0)
    return d.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def pcp_ext_052_dist_5dollar_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of dist-to-nearest-$5 in trailing 252-day distribution."""
    d = _dist_to_round(close, 5.0)
    return d.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def pcp_ext_053_dist_dollar_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of distance-to-dollar vs trailing 63-day distribution."""
    d = _dist_to_round(close, 1.0)
    m = _rolling_mean(d, _TD_QTR)
    s = _rolling_std(d, _TD_QTR)
    return _safe_div(d - m, s)


def pcp_ext_054_cents_digit_mean_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day mean of cents digit (trailing-digit level)."""
    return _rolling_mean(close % 1.0, _TD_MON)


def pcp_ext_055_cents_digit_std_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day std dev of cents digit (trailing-digit variability)."""
    return _rolling_std(close % 1.0, _TD_MON)


def pcp_ext_056_cents_digit_min_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day minimum of cents digit."""
    return _rolling_min(close % 1.0, _TD_MON)


def pcp_ext_057_cents_digit_max_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day maximum of cents digit."""
    return _rolling_max(close % 1.0, _TD_MON)


def pcp_ext_058_dist_dollar_ewma_span21(close: pd.Series) -> pd.Series:
    """EWM (span=21) of distance-to-nearest-dollar (smooth clustering proximity signal)."""
    return _ewm_mean(_dist_to_round(close, 1.0), _TD_MON)


def pcp_ext_059_dist_5dollar_ewma_span21(close: pd.Series) -> pd.Series:
    """EWM (span=21) of distance-to-nearest-$5 level."""
    return _ewm_mean(_dist_to_round(close, 5.0), _TD_MON)


def pcp_ext_060_round_level_pinning_index_21d(close: pd.Series) -> pd.Series:
    """Pinning index: fraction of near-dollar days / rolling-mean dist-to-dollar (21d).
    Higher = strong round-level pinning relative to average proximity."""
    frac = _frac_near_round(close, 1.0, 0.05, _TD_MON)
    avg_dist = _rolling_mean(_dist_to_round(close, 1.0), _TD_MON)
    return _safe_div(frac, avg_dist.clip(lower=_EPS))


# --- Group G (061-075): Multi-scale confluence and composite scores ---

def pcp_ext_061_all_three_increments_near_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close simultaneously within tol of $1, $5, and $10 levels
    (i.e. close is near a $10 level, which is also $5 and $1 aligned)."""
    return (
        (_dist_to_round(close, 1.0) <= 0.05) &
        (_dist_to_round(close, 5.0) <= 0.10) &
        (_dist_to_round(close, 10.0) <= 0.10)
    ).astype(float)


def pcp_ext_062_sub5_and_near_dollar_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close < $5 AND within $0.05 of a whole dollar (distress + pinning)."""
    return (
        (close < 5.0) & (_dist_to_round(close, 1.0) <= 0.05)
    ).astype(float)


def pcp_ext_063_sub5_and_near_1dollar_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close < $5 AND within $0.10 of $1.00 (penny-stock boundary pinning)."""
    return (
        (close < 5.0) & (close.sub(1.0).abs() <= 0.10)
    ).astype(float)


def pcp_ext_064_sub10_and_at_5dollar_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close < $10 AND within $0.10 of $5 (testing $5 support from above)."""
    return (
        (close < 10.0) & (_dist_to_round(close, 5.0) <= 0.10)
    ).astype(float)


def pcp_ext_065_dist_dollar_trend_acceleration(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day rolling mean of dist-to-dollar (trend acceleration)."""
    avg = _rolling_mean(_dist_to_round(close, 1.0), _TD_MON)
    return avg.diff(_TD_WEEK)


def pcp_ext_066_depth_sub5_norm_by_price(close: pd.Series) -> pd.Series:
    """Depth below $5 normalized by close price (deeper + cheaper = higher signal)."""
    depth = (5.0 - close).clip(lower=0.0)
    return _safe_div(depth, close.clip(lower=_EPS))


def pcp_ext_067_depth_sub1_norm_by_price(close: pd.Series) -> pd.Series:
    """Depth below $1 normalized by close price."""
    depth = (1.0 - close).clip(lower=0.0)
    return _safe_div(depth, close.clip(lower=_EPS))


def pcp_ext_068_dist_dollar_pct_rank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of dist-to-dollar in trailing 63-day distribution."""
    d = _dist_to_round(close, 1.0)
    return d.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def pcp_ext_069_round_level_confluence_count(close: pd.Series) -> pd.Series:
    """Count of round levels (dollar, $5, $10, $25, $50) within $0.20 of close."""
    d1 = (_dist_to_round(close, 1.0) <= 0.20).astype(float)
    d5 = (_dist_to_round(close, 5.0) <= 0.20).astype(float)
    d10 = (_dist_to_round(close, 10.0) <= 0.20).astype(float)
    d25 = (_dist_to_round(close, 25.0) <= 0.20).astype(float)
    d50 = (_dist_to_round(close, 50.0) <= 0.20).astype(float)
    return d1 + d5 + d10 + d25 + d50


def pcp_ext_070_round_level_multi_scale_magnet_score(close: pd.Series) -> pd.Series:
    """Multi-scale magnet: avg of magnet scores at $1, $5, $10 increments (21d rolling)."""
    m1 = 1.0 - (_dist_to_round(close, 1.0) / 0.5).clip(upper=1.0)
    m5 = 1.0 - (_dist_to_round(close, 5.0) / 2.5).clip(upper=1.0)
    m10 = 1.0 - (_dist_to_round(close, 10.0) / 5.0).clip(upper=1.0)
    combo = (m1 + m5 + m10) / 3.0
    return _rolling_mean(combo, _TD_MON)


def pcp_ext_071_abs_price_zscore_expanding(close: pd.Series) -> pd.Series:
    """Expanding z-score of close price vs all-history mean/std."""
    m = close.expanding(min_periods=1).mean()
    s = close.expanding(min_periods=2).std()
    return _safe_div(close - m, s)


def pcp_ext_072_close_pct_rank_126d(close: pd.Series) -> pd.Series:
    """Percentile rank of close within trailing 126-day distribution."""
    return close.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)


def pcp_ext_073_close_at_all_time_low_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close equals expanding all-time minimum (new all-time low)."""
    exp_min = close.expanding(min_periods=1).min()
    return (close <= exp_min + _EPS).astype(float)


def pcp_ext_074_sub5_and_at_all_time_low_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close < $5 AND at all-time low (deep distress capitulation)."""
    exp_min = close.expanding(min_periods=1).min()
    return ((close < 5.0) & (close <= exp_min + _EPS)).astype(float)


def pcp_ext_075_pcp_capitulation_composite(close: pd.Series) -> pd.Series:
    """Full PCP capitulation composite: weighted sum of sub-zone depth, round-level
    pinning strength, 252-day rank deterioration, and all-time-low proximity.
    Higher = more psychologically distressed at round levels near all-time lows."""
    sub5_depth = (5.0 - close).clip(lower=0.0) / 5.0
    sub1_depth = (1.0 - close).clip(lower=0.0) * 2.0
    magnet = 1.0 - (_dist_to_round(close, 1.0) / 0.5).clip(upper=1.0)
    rank_invert = 1.0 - close.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(
        pct=True).fillna(0.5)
    exp_min = close.expanding(min_periods=1).min()
    atl_prox = 1.0 - _safe_div(close - exp_min.clip(lower=_EPS),
                                exp_min.clip(lower=_EPS)).clip(upper=1.0).fillna(0.0)
    return sub5_depth + sub1_depth + magnet + rank_invert + atl_prox


# ── Registry ──────────────────────────────────────────────────────────────────

PRICE_CLUSTERING_PSYCHOLOGY_EXTENDED_REGISTRY_001_075 = {
    "pcp_ext_001_dist_to_nearest_2dollar": {"inputs": ["close"], "func": pcp_ext_001_dist_to_nearest_2dollar},
    "pcp_ext_002_dist_to_nearest_2dollar_pct": {"inputs": ["close"], "func": pcp_ext_002_dist_to_nearest_2dollar_pct},
    "pcp_ext_003_dist_to_nearest_3dollar": {"inputs": ["close"], "func": pcp_ext_003_dist_to_nearest_3dollar},
    "pcp_ext_004_dist_to_nearest_quarter": {"inputs": ["close"], "func": pcp_ext_004_dist_to_nearest_quarter},
    "pcp_ext_005_dist_to_nearest_half_dollar": {"inputs": ["close"], "func": pcp_ext_005_dist_to_nearest_half_dollar},
    "pcp_ext_006_dist_to_nearest_20dollar": {"inputs": ["close"], "func": pcp_ext_006_dist_to_nearest_20dollar},
    "pcp_ext_007_dist_to_nearest_20dollar_pct": {"inputs": ["close"], "func": pcp_ext_007_dist_to_nearest_20dollar_pct},
    "pcp_ext_008_dist_to_nearest_100dollar": {"inputs": ["close"], "func": pcp_ext_008_dist_to_nearest_100dollar},
    "pcp_ext_009_at_quarter_dollar_flag": {"inputs": ["close"], "func": pcp_ext_009_at_quarter_dollar_flag},
    "pcp_ext_010_at_half_dollar_flag": {"inputs": ["close"], "func": pcp_ext_010_at_half_dollar_flag},
    "pcp_ext_011_frac_near_dollar_126d": {"inputs": ["close"], "func": pcp_ext_011_frac_near_dollar_126d},
    "pcp_ext_012_frac_near_5dollar_126d": {"inputs": ["close"], "func": pcp_ext_012_frac_near_5dollar_126d},
    "pcp_ext_013_frac_near_quarter_dollar_21d": {"inputs": ["close"], "func": pcp_ext_013_frac_near_quarter_dollar_21d},
    "pcp_ext_014_frac_near_half_dollar_21d": {"inputs": ["close"], "func": pcp_ext_014_frac_near_half_dollar_21d},
    "pcp_ext_015_frac_near_10dollar_126d": {"inputs": ["close"], "func": pcp_ext_015_frac_near_10dollar_126d},
    "pcp_ext_016_frac_zero_cents_252d": {"inputs": ["close"], "func": pcp_ext_016_frac_zero_cents_252d},
    "pcp_ext_017_frac_50cents_252d": {"inputs": ["close"], "func": pcp_ext_017_frac_50cents_252d},
    "pcp_ext_018_frac_near_dollar_5d_expanding": {"inputs": ["close"], "func": pcp_ext_018_frac_near_dollar_5d_expanding},
    "pcp_ext_019_frac_sub5_126d": {"inputs": ["close"], "func": pcp_ext_019_frac_sub5_126d},
    "pcp_ext_020_frac_sub1_126d": {"inputs": ["close"], "func": pcp_ext_020_frac_sub1_126d},
    "pcp_ext_021_weighted_close_dist_to_dollar": {"inputs": ["close", "high", "low"], "func": pcp_ext_021_weighted_close_dist_to_dollar},
    "pcp_ext_022_hl_midpoint_dist_to_dollar": {"inputs": ["high", "low"], "func": pcp_ext_022_hl_midpoint_dist_to_dollar},
    "pcp_ext_023_hl_midpoint_dist_to_5dollar": {"inputs": ["high", "low"], "func": pcp_ext_023_hl_midpoint_dist_to_5dollar},
    "pcp_ext_024_hl_midpoint_sub5_flag": {"inputs": ["high", "low"], "func": pcp_ext_024_hl_midpoint_sub5_flag},
    "pcp_ext_025_weighted_close_sub5_flag": {"inputs": ["close", "high", "low"], "func": pcp_ext_025_weighted_close_sub5_flag},
    "pcp_ext_026_hl_midpoint_pct_thru_dollar_zone": {"inputs": ["high", "low"], "func": pcp_ext_026_hl_midpoint_pct_thru_dollar_zone},
    "pcp_ext_027_hl_midpoint_near_dollar_21d_frac": {"inputs": ["high", "low"], "func": pcp_ext_027_hl_midpoint_near_dollar_21d_frac},
    "pcp_ext_028_typical_price_dist_to_dollar": {"inputs": ["close", "high", "low"], "func": pcp_ext_028_typical_price_dist_to_dollar},
    "pcp_ext_029_typical_price_sub5_flag": {"inputs": ["close", "high", "low"], "func": pcp_ext_029_typical_price_sub5_flag},
    "pcp_ext_030_close_minus_hl_midpoint_dist_to_dollar_diff": {"inputs": ["close", "high", "low"], "func": pcp_ext_030_close_minus_hl_midpoint_dist_to_dollar_diff},
    "pcp_ext_031_vwap_dist_to_dollar_proxy": {"inputs": ["close", "volume"], "func": pcp_ext_031_vwap_dist_to_dollar_proxy},
    "pcp_ext_032_vwap_sub5_flag_21d": {"inputs": ["close", "volume"], "func": pcp_ext_032_vwap_sub5_flag_21d},
    "pcp_ext_033_vwap_dist_to_5dollar_21d": {"inputs": ["close", "volume"], "func": pcp_ext_033_vwap_dist_to_5dollar_21d},
    "pcp_ext_034_vol_weighted_dist_dollar_21d": {"inputs": ["close", "volume"], "func": pcp_ext_034_vol_weighted_dist_dollar_21d},
    "pcp_ext_035_vol_weighted_sub5_depth_21d": {"inputs": ["close", "volume"], "func": pcp_ext_035_vol_weighted_sub5_depth_21d},
    "pcp_ext_036_vol_near_dollar_excess_21d": {"inputs": ["close", "volume"], "func": pcp_ext_036_vol_near_dollar_excess_21d},
    "pcp_ext_037_vol_on_sub5_vs_above5_ratio_63d": {"inputs": ["close", "volume"], "func": pcp_ext_037_vol_on_sub5_vs_above5_ratio_63d},
    "pcp_ext_038_dollar_vol_at_sub5_21d": {"inputs": ["close", "volume"], "func": pcp_ext_038_dollar_vol_at_sub5_21d},
    "pcp_ext_039_dollar_vol_at_sub5_63d": {"inputs": ["close", "volume"], "func": pcp_ext_039_dollar_vol_at_sub5_63d},
    "pcp_ext_040_vol_fraction_near_5dollar_21d": {"inputs": ["close", "volume"], "func": pcp_ext_040_vol_fraction_near_5dollar_21d},
    "pcp_ext_041_sub5_regime_fraction_252d": {"inputs": ["close"], "func": pcp_ext_041_sub5_regime_fraction_252d},
    "pcp_ext_042_sub5_entry_count_252d": {"inputs": ["close"], "func": pcp_ext_042_sub5_entry_count_252d},
    "pcp_ext_043_sub5_exit_count_252d": {"inputs": ["close"], "func": pcp_ext_043_sub5_exit_count_252d},
    "pcp_ext_044_sub10_regime_entry_count_252d": {"inputs": ["close"], "func": pcp_ext_044_sub10_regime_entry_count_252d},
    "pcp_ext_045_sub1_regime_entry_count_252d": {"inputs": ["close"], "func": pcp_ext_045_sub1_regime_entry_count_252d},
    "pcp_ext_046_consec_sub5_max_in_252d": {"inputs": ["close"], "func": pcp_ext_046_consec_sub5_max_in_252d},
    "pcp_ext_047_consec_sub10_max_in_252d": {"inputs": ["close"], "func": pcp_ext_047_consec_sub10_max_in_252d},
    "pcp_ext_048_sub5_bounce_back_flag": {"inputs": ["close"], "func": pcp_ext_048_sub5_bounce_back_flag},
    "pcp_ext_049_sub5_new_low_flag": {"inputs": ["close"], "func": pcp_ext_049_sub5_new_low_flag},
    "pcp_ext_050_sub1_new_low_flag": {"inputs": ["close"], "func": pcp_ext_050_sub1_new_low_flag},
    "pcp_ext_051_dist_dollar_pct_rank_252d": {"inputs": ["close"], "func": pcp_ext_051_dist_dollar_pct_rank_252d},
    "pcp_ext_052_dist_5dollar_pct_rank_252d": {"inputs": ["close"], "func": pcp_ext_052_dist_5dollar_pct_rank_252d},
    "pcp_ext_053_dist_dollar_zscore_63d": {"inputs": ["close"], "func": pcp_ext_053_dist_dollar_zscore_63d},
    "pcp_ext_054_cents_digit_mean_21d": {"inputs": ["close"], "func": pcp_ext_054_cents_digit_mean_21d},
    "pcp_ext_055_cents_digit_std_21d": {"inputs": ["close"], "func": pcp_ext_055_cents_digit_std_21d},
    "pcp_ext_056_cents_digit_min_21d": {"inputs": ["close"], "func": pcp_ext_056_cents_digit_min_21d},
    "pcp_ext_057_cents_digit_max_21d": {"inputs": ["close"], "func": pcp_ext_057_cents_digit_max_21d},
    "pcp_ext_058_dist_dollar_ewma_span21": {"inputs": ["close"], "func": pcp_ext_058_dist_dollar_ewma_span21},
    "pcp_ext_059_dist_5dollar_ewma_span21": {"inputs": ["close"], "func": pcp_ext_059_dist_5dollar_ewma_span21},
    "pcp_ext_060_round_level_pinning_index_21d": {"inputs": ["close"], "func": pcp_ext_060_round_level_pinning_index_21d},
    "pcp_ext_061_all_three_increments_near_flag": {"inputs": ["close"], "func": pcp_ext_061_all_three_increments_near_flag},
    "pcp_ext_062_sub5_and_near_dollar_flag": {"inputs": ["close"], "func": pcp_ext_062_sub5_and_near_dollar_flag},
    "pcp_ext_063_sub5_and_near_1dollar_flag": {"inputs": ["close"], "func": pcp_ext_063_sub5_and_near_1dollar_flag},
    "pcp_ext_064_sub10_and_at_5dollar_flag": {"inputs": ["close"], "func": pcp_ext_064_sub10_and_at_5dollar_flag},
    "pcp_ext_065_dist_dollar_trend_acceleration": {"inputs": ["close"], "func": pcp_ext_065_dist_dollar_trend_acceleration},
    "pcp_ext_066_depth_sub5_norm_by_price": {"inputs": ["close"], "func": pcp_ext_066_depth_sub5_norm_by_price},
    "pcp_ext_067_depth_sub1_norm_by_price": {"inputs": ["close"], "func": pcp_ext_067_depth_sub1_norm_by_price},
    "pcp_ext_068_dist_dollar_pct_rank_63d": {"inputs": ["close"], "func": pcp_ext_068_dist_dollar_pct_rank_63d},
    "pcp_ext_069_round_level_confluence_count": {"inputs": ["close"], "func": pcp_ext_069_round_level_confluence_count},
    "pcp_ext_070_round_level_multi_scale_magnet_score": {"inputs": ["close"], "func": pcp_ext_070_round_level_multi_scale_magnet_score},
    "pcp_ext_071_abs_price_zscore_expanding": {"inputs": ["close"], "func": pcp_ext_071_abs_price_zscore_expanding},
    "pcp_ext_072_close_pct_rank_126d": {"inputs": ["close"], "func": pcp_ext_072_close_pct_rank_126d},
    "pcp_ext_073_close_at_all_time_low_flag": {"inputs": ["close"], "func": pcp_ext_073_close_at_all_time_low_flag},
    "pcp_ext_074_sub5_and_at_all_time_low_flag": {"inputs": ["close"], "func": pcp_ext_074_sub5_and_at_all_time_low_flag},
    "pcp_ext_075_pcp_capitulation_composite": {"inputs": ["close"], "func": pcp_ext_075_pcp_capitulation_composite},
}
