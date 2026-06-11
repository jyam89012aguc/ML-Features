"""
51_shadow_wick_analysis — Extended Features 001-075
Domain: shadow/wick geometry — additional variants: wick on log-range, wick depth at
        new-low days, wick-vs-prior-wick ratios, gap-adjusted wicks, wick acceleration,
        weekly/quarterly aggregated wicks, wick range-position, wick clustering,
        wick-volume conditional measures not present in the four base files.
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


def _lwr(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower-wick-to-range ratio."""
    return _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))


def _uwr(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Upper-wick-to-range ratio."""
    return _safe_div(_upper_wick(open, high, low, close), _candle_range(high, low))


def _zscore(s: pd.Series, w: int) -> pd.Series:
    """Rolling z-score over window w."""
    return _safe_div(s - _rolling_mean(s, w), _rolling_std(s, w))


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Lower wick on log scale and gap-adjusted lower wick ---

def swk_ext_001_log_lower_wick(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log of lower wick as fraction of low price (log-normalized lower wick)."""
    body_low = pd.concat([open, close], axis=1).min(axis=1)
    return np.log(body_low.clip(lower=_EPS)) - np.log(low.clip(lower=_EPS))


def swk_ext_002_log_upper_wick(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log of upper wick as fraction of body-high price (log-normalized upper wick)."""
    body_high = pd.concat([open, close], axis=1).max(axis=1)
    return np.log(high.clip(lower=_EPS)) - np.log(body_high.clip(lower=_EPS))


def swk_ext_003_lower_wick_pct_of_low(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower wick length as a fraction of the day's low price."""
    return _safe_div(_lower_wick(open, high, low, close), low.clip(lower=_EPS))


def swk_ext_004_lower_wick_gap_adjusted(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower wick measured from prior close to day low (true-low rejection depth)."""
    drop = (close.shift(1) - low).clip(lower=0.0)
    return _safe_div(drop, close.shift(1).clip(lower=_EPS))


def swk_ext_005_lower_wick_true_range_ratio(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower wick as fraction of the true range (incl. prior close)."""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _safe_div(_lower_wick(open, high, low, close), tr.clip(lower=_EPS))


def swk_ext_006_lower_wick_pct_of_low_sma21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean of lower-wick-as-fraction-of-low."""
    return _rolling_mean(swk_ext_003_lower_wick_pct_of_low(open, high, low, close), _TD_MON)


def swk_ext_007_lower_wick_pct_of_low_sma63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day mean of lower-wick-as-fraction-of-low."""
    return _rolling_mean(swk_ext_003_lower_wick_pct_of_low(open, high, low, close), _TD_QTR)


def swk_ext_008_lower_wick_true_range_ratio_sma21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean of lower-wick-to-true-range ratio."""
    return _rolling_mean(swk_ext_005_lower_wick_true_range_ratio(open, high, low, close), _TD_MON)


def swk_ext_009_gap_adjusted_lower_wick_max_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day max of gap-adjusted lower wick (deepest intraday reversal in quarter)."""
    return _rolling_max(swk_ext_004_lower_wick_gap_adjusted(open, high, low, close), _TD_QTR)


def swk_ext_010_log_lower_wick_sma21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean of the log-normalized lower wick."""
    return _rolling_mean(swk_ext_001_log_lower_wick(open, high, low, close), _TD_MON)


# --- Group B (011-020): Lower wick measured at new-low days ---

def swk_ext_011_lower_wick_ratio_on_new_21d_low(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower-wick ratio on days that print a new 21-day intraday low (else carried forward)."""
    new_low = low <= _rolling_min(low, _TD_MON)
    return _lwr(open, high, low, close).where(new_low, np.nan).ffill()


def swk_ext_012_lower_wick_ratio_on_new_63d_low(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower-wick ratio on days printing a new 63-day intraday low (carried forward)."""
    new_low = low <= _rolling_min(low, _TD_QTR)
    return _lwr(open, high, low, close).where(new_low, np.nan).ffill()


def swk_ext_013_lower_wick_ratio_on_new_252d_low(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower-wick ratio on days printing a new 252-day intraday low (carried forward)."""
    new_low = low <= _rolling_min(low, _TD_YEAR)
    return _lwr(open, high, low, close).where(new_low, np.nan).ffill()


def swk_ext_014_new_21d_low_long_wick_flag(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: new 21-day low AND lower-wick ratio > 0.40 (rejected new-low day)."""
    new_low = low <= _rolling_min(low, _TD_MON)
    return ((new_low) & (_lwr(open, high, low, close) > 0.40)).astype(float)


def swk_ext_015_new_low_long_wick_count_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day count of rejected new-21d-low days (new low with lower wick > 0.40)."""
    return _rolling_sum(swk_ext_014_new_21d_low_long_wick_flag(open, high, low, close), _TD_QTR)


def swk_ext_016_avg_lower_wick_ratio_new_low_days_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day mean lower-wick ratio over days that set a new 21-day low."""
    new_low = low <= _rolling_min(low, _TD_MON)
    masked = _lwr(open, high, low, close).where(new_low, np.nan)
    return masked.rolling(_TD_QTR, min_periods=1).mean()


def swk_ext_017_wick_asym_on_new_63d_low(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower/upper wick ratio on new-63d-low days (carried forward)."""
    new_low = low <= _rolling_min(low, _TD_QTR)
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close).clip(lower=_EPS)
    return (lw / uw).where(new_low, np.nan).ffill()


def swk_ext_018_lower_wick_depth_at_new_low(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower wick normalized by 21-day ATR, on new-21d-low days only (carried forward)."""
    atr = _rolling_mean(_candle_range(high, low), _TD_MON)
    new_low = low <= _rolling_min(low, _TD_MON)
    return _safe_div(_lower_wick(open, high, low, close), atr).where(new_low, np.nan).ffill()


def swk_ext_019_days_since_rejected_new_low(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Days elapsed since the last rejected new-21d-low day (long lower wick at new low)."""
    flag = swk_ext_014_new_21d_low_long_wick_flag(open, high, low, close).astype(bool)
    idx = pd.Series(range(len(flag)), index=flag.index, dtype=float)
    last = idx.where(flag).ffill()
    return idx - last


def swk_ext_020_new_low_long_wick_fraction_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day fraction of rejected new-21d-low days."""
    return _rolling_mean(swk_ext_014_new_21d_low_long_wick_flag(open, high, low, close), _TD_YEAR)


# --- Group C (021-030): Wick versus prior-day wick (sequential dynamics) ---

def swk_ext_021_lower_wick_vs_prior_ratio(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's lower wick divided by prior day's lower wick."""
    lw = _lower_wick(open, high, low, close)
    return _safe_div(lw, lw.shift(1).clip(lower=_EPS))


def swk_ext_022_lower_wick_ratio_1d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1-day change in lower-wick ratio (daily rejection-intensity change)."""
    return _lwr(open, high, low, close).diff(1)


def swk_ext_023_lower_wick_ratio_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day change in lower-wick ratio (weekly rejection-intensity change)."""
    return _lwr(open, high, low, close).diff(_TD_WEEK)


def swk_ext_024_lower_wick_ratio_21d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day change in lower-wick ratio (monthly rejection-intensity change)."""
    return _lwr(open, high, low, close).diff(_TD_MON)


def swk_ext_025_lower_wick_ratio_acceleration(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second difference of lower-wick ratio (acceleration of rejection intensity)."""
    return _lwr(open, high, low, close).diff(1).diff(1)


def swk_ext_026_lower_wick_bigger_than_prior_flag(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: today's lower wick exceeds prior day's lower wick (expanding rejection)."""
    lw = _lower_wick(open, high, low, close)
    return (lw > lw.shift(1)).astype(float)


def swk_ext_027_lower_wick_rising_streak(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days of rising lower wick."""
    lw = _lower_wick(open, high, low, close)
    return _consec_streak(lw > lw.shift(1))


def swk_ext_028_lower_wick_bigger_than_prior_count_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day count of days with lower wick larger than prior day."""
    return _rolling_sum(swk_ext_026_lower_wick_bigger_than_prior_flag(open, high, low, close), _TD_MON)


def swk_ext_029_lower_wick_ratio_5d_diff_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 5-day lower-wick-ratio change within trailing 63 days."""
    return _zscore(_lwr(open, high, low, close).diff(_TD_WEEK), _TD_QTR)


def swk_ext_030_upper_wick_vs_prior_ratio(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's upper wick divided by prior day's upper wick."""
    uw = _upper_wick(open, high, low, close)
    return _safe_div(uw, uw.shift(1).clip(lower=_EPS))


# --- Group D (031-040): Wick range-position and clustering ---

def swk_ext_031_lower_wick_range_position(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower wick ratio relative to its 63-day [min,max] range (0-1 position)."""
    lwr = _lwr(open, high, low, close)
    mn = _rolling_min(lwr, _TD_QTR)
    mx = _rolling_max(lwr, _TD_QTR)
    return _safe_div(lwr - mn, mx - mn)


def swk_ext_032_lower_wick_range_position_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower wick ratio relative to its 252-day [min,max] range."""
    lwr = _lwr(open, high, low, close)
    mn = _rolling_min(lwr, _TD_YEAR)
    mx = _rolling_max(lwr, _TD_YEAR)
    return _safe_div(lwr - mn, mx - mn)


def swk_ext_033_lower_wick_cluster_5d_sum(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day rolling sum of lower-wick ratio (weekly clustering of rejection)."""
    return _rolling_sum(_lwr(open, high, low, close), _TD_WEEK)


def swk_ext_034_long_lower_wick_cluster_flag_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: at least 3 long-lower-wick days (ratio>0.33) within trailing 5 days."""
    flag = (_lwr(open, high, low, close) > 0.33).astype(float)
    return (_rolling_sum(flag, _TD_WEEK) >= 3.0).astype(float)


def swk_ext_035_long_lower_wick_cluster_flag_10d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: at least 5 long-lower-wick days within trailing 10 days."""
    flag = (_lwr(open, high, low, close) > 0.33).astype(float)
    return (_rolling_sum(flag, 10) >= 5.0).astype(float)


def swk_ext_036_lower_wick_cluster_intensity_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day sum of squared lower-wick ratios (clustered rejection energy)."""
    return _rolling_sum(_lwr(open, high, low, close) ** 2, _TD_MON)


def swk_ext_037_lower_wick_weekly_max_position(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's lower-wick ratio relative to its trailing 5-day maximum."""
    lwr = _lwr(open, high, low, close)
    return _safe_div(lwr, _rolling_max(lwr, _TD_WEEK))


def swk_ext_038_upper_wick_range_position(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Upper-wick ratio relative to its 63-day [min,max] range."""
    uwr = _uwr(open, high, low, close)
    mn = _rolling_min(uwr, _TD_QTR)
    mx = _rolling_max(uwr, _TD_QTR)
    return _safe_div(uwr - mn, mx - mn)


def swk_ext_039_lower_wick_cluster_5d_vs_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day lower-wick sum relative to 63-day average 5-day sum (cluster spike)."""
    s5 = _rolling_sum(_lwr(open, high, low, close), _TD_WEEK)
    return _safe_div(s5, _rolling_mean(s5, _TD_QTR))


def swk_ext_040_consec_lower_wick_above_median(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days lower-wick ratio stays above its 63-day median."""
    lwr = _lwr(open, high, low, close)
    return _consec_streak(lwr > _rolling_median(lwr, _TD_QTR))


# --- Group E (041-050): Multi-day aggregated wick measures ---

def swk_ext_041_lower_wick_weekly_sum_ratio(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of 5-day lower wicks divided by sum of 5-day ranges (weekly wick fill)."""
    lw = _lower_wick(open, high, low, close)
    rng = _candle_range(high, low)
    return _safe_div(_rolling_sum(lw, _TD_WEEK), _rolling_sum(rng, _TD_WEEK))


def swk_ext_042_lower_wick_monthly_sum_ratio(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of 21-day lower wicks divided by sum of 21-day ranges (monthly wick fill)."""
    lw = _lower_wick(open, high, low, close)
    rng = _candle_range(high, low)
    return _safe_div(_rolling_sum(lw, _TD_MON), _rolling_sum(rng, _TD_MON))


def swk_ext_043_lower_wick_quarterly_sum_ratio(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of 63-day lower wicks divided by sum of 63-day ranges (quarterly wick fill)."""
    lw = _lower_wick(open, high, low, close)
    rng = _candle_range(high, low)
    return _safe_div(_rolling_sum(lw, _TD_QTR), _rolling_sum(rng, _TD_QTR))


def swk_ext_044_upper_wick_monthly_sum_ratio(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of 21-day upper wicks divided by sum of 21-day ranges."""
    uw = _upper_wick(open, high, low, close)
    rng = _candle_range(high, low)
    return _safe_div(_rolling_sum(uw, _TD_MON), _rolling_sum(rng, _TD_MON))


def swk_ext_045_net_wick_monthly_sum_ratio(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of 21-day (lower-upper) wicks divided by sum of 21-day ranges (net rejection)."""
    diff = _lower_wick(open, high, low, close) - _upper_wick(open, high, low, close)
    rng = _candle_range(high, low)
    return _safe_div(_rolling_sum(diff, _TD_MON), _rolling_sum(rng, _TD_MON))


def swk_ext_046_lower_wick_ewm5(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-span EWM of lower-wick ratio (fast adaptive smoothing)."""
    return _ewm_mean(_lwr(open, high, low, close), _TD_WEEK)


def swk_ext_047_lower_wick_ewm63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-span EWM of lower-wick ratio (slow adaptive smoothing)."""
    return _ewm_mean(_lwr(open, high, low, close), _TD_QTR)


def swk_ext_048_lower_wick_ewm5_minus_ewm21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EWM5 minus EWM21 of lower-wick ratio (short-term rejection momentum)."""
    lwr = _lwr(open, high, low, close)
    return _ewm_mean(lwr, _TD_WEEK) - _ewm_mean(lwr, _TD_MON)


def swk_ext_049_lower_wick_quarterly_max_position(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's lower-wick ratio relative to its trailing 63-day maximum."""
    lwr = _lwr(open, high, low, close)
    return _safe_div(lwr, _rolling_max(lwr, _TD_QTR))


def swk_ext_050_lower_wick_halfyear_sum_ratio(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of 126-day lower wicks divided by sum of 126-day ranges (half-year wick fill)."""
    lw = _lower_wick(open, high, low, close)
    rng = _candle_range(high, low)
    return _safe_div(_rolling_sum(lw, _TD_HALF), _rolling_sum(rng, _TD_HALF))


# --- Group F (051-060): Wick-volume conditional and weighted features ---

def swk_ext_051_lower_wick_ratio_volume_z_product(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Lower-wick ratio times volume z-score (volume-confirmed rejection)."""
    vz = _zscore(volume, _TD_QTR)
    return _lwr(open, high, low, close) * vz


def swk_ext_052_lower_wick_ratio_on_volume_spike_days(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day mean lower-wick ratio on days with volume > 2x its 63-day mean."""
    spike = volume > 2.0 * _rolling_mean(volume, _TD_QTR)
    masked = _lwr(open, high, low, close).where(spike, np.nan)
    return masked.rolling(_TD_QTR, min_periods=1).mean()


def swk_ext_053_vol_weighted_lower_wick_ratio_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day volume-weighted average lower-wick ratio (weekly weighted rejection)."""
    lwr = _lwr(open, high, low, close)
    return _safe_div(_rolling_sum(lwr * volume, _TD_WEEK), _rolling_sum(volume, _TD_WEEK))


def swk_ext_054_vol_weighted_lower_wick_ratio_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day volume-weighted average lower-wick ratio (annual weighted rejection)."""
    lwr = _lwr(open, high, low, close)
    return _safe_div(_rolling_sum(lwr * volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))


def swk_ext_055_high_vol_long_lower_wick_streak(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days with long lower wick (>0.50) AND volume above 63-day mean."""
    cond = (_lwr(open, high, low, close) > 0.50) & (volume > _rolling_mean(volume, _TD_QTR))
    return _consec_streak(cond)


def swk_ext_056_long_lower_wick_high_vol_count_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day count of long-lower-wick (>0.50) days with above-63d-mean volume."""
    cond = ((_lwr(open, high, low, close) > 0.50) & (volume > _rolling_mean(volume, _TD_QTR))).astype(float)
    return _rolling_sum(cond, _TD_YEAR)


def swk_ext_057_lower_wick_volume_corr_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day rolling correlation between lower-wick ratio and volume."""
    lwr = _lwr(open, high, low, close)
    return lwr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).corr(volume)


def swk_ext_058_vol_weighted_wick_asym_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day volume-weighted average lower/upper wick asymmetry ratio."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close).clip(lower=_EPS)
    asym = lw / uw
    return _safe_div(_rolling_sum(asym * volume, _TD_MON), _rolling_sum(volume, _TD_MON))


def swk_ext_059_lower_wick_dollar_volume_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day sum of lower-wick ratio times dollar volume, normalized by dollar volume."""
    lwr = _lwr(open, high, low, close)
    dv = close * volume
    return _safe_div(_rolling_sum(lwr * dv, _TD_MON), _rolling_sum(dv, _TD_MON))


def swk_ext_060_lower_wick_on_down_volume_days_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day mean lower-wick ratio on down-close, high-volume days (capitulation context)."""
    cond = (close < close.shift(1)) & (volume > _rolling_mean(volume, _TD_MON))
    masked = _lwr(open, high, low, close).where(cond, np.nan)
    return masked.rolling(_TD_MON, min_periods=1).mean()


# --- Group G (061-068): Wick dispersion, skew and structural shape ---

def swk_ext_061_lower_wick_ratio_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling skewness of lower-wick ratio."""
    lwr = _lwr(open, high, low, close)
    return lwr.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).skew()


def swk_ext_062_lower_wick_ratio_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling skewness of lower-wick ratio."""
    lwr = _lwr(open, high, low, close)
    return lwr.rolling(_TD_YEAR, min_periods=max(5, _TD_YEAR // 2)).skew()


def swk_ext_063_lower_wick_ratio_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling kurtosis of lower-wick ratio (tail-heaviness of rejection)."""
    lwr = _lwr(open, high, low, close)
    return lwr.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).kurt()


def swk_ext_064_lower_wick_ratio_iqr_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day interquartile range of lower-wick ratio (robust dispersion)."""
    lwr = _lwr(open, high, low, close)
    q75 = lwr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = lwr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    return q75 - q25


def swk_ext_065_lower_wick_ratio_q90_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day 90th percentile of lower-wick ratio (extreme rejection level)."""
    lwr = _lwr(open, high, low, close)
    return lwr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.90)


def swk_ext_066_lower_wick_ratio_std_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling std of lower-wick ratio (annual rejection variability)."""
    return _rolling_std(_lwr(open, high, low, close), _TD_YEAR)


def swk_ext_067_upper_wick_ratio_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling skewness of upper-wick ratio."""
    uwr = _uwr(open, high, low, close)
    return uwr.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).skew()


def swk_ext_068_total_wick_ratio_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling skewness of total-wick (lower+upper) ratio."""
    twr = _lwr(open, high, low, close) + _uwr(open, high, low, close)
    return twr.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).skew()


# --- Group H (069-075): Wick extremes, expanding stats and composites ---

def swk_ext_069_lower_wick_ratio_expanding_max(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding all-time maximum lower-wick ratio."""
    return _lwr(open, high, low, close).expanding(min_periods=5).max()


def swk_ext_070_lower_wick_ratio_vs_expanding_max(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's lower-wick ratio as fraction of its expanding all-time maximum."""
    lwr = _lwr(open, high, low, close)
    return _safe_div(lwr, lwr.expanding(min_periods=5).max())


def swk_ext_071_lower_wick_abs_expanding_pct_rank(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of absolute lower wick length."""
    return _lower_wick(open, high, low, close).expanding(min_periods=5).rank(pct=True)


def swk_ext_072_lower_wick_ratio_above_q90_streak(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days lower-wick ratio exceeds its 252-day 90th percentile."""
    lwr = _lwr(open, high, low, close)
    p90 = lwr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.90)
    return _consec_streak(lwr > p90)


def swk_ext_073_lower_wick_ratio_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of lower-wick ratio relative to its trailing 126-day distribution."""
    return _zscore(_lwr(open, high, low, close), _TD_HALF)


def swk_ext_074_wick_capitulation_flag(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: new 21-day low, lower-wick ratio > 0.50, and volume above 63-day mean."""
    new_low = low <= _rolling_min(low, _TD_MON)
    cond = new_low & (_lwr(open, high, low, close) > 0.50) & (volume > _rolling_mean(volume, _TD_QTR))
    return cond.astype(float)


def swk_ext_075_wick_capitulation_composite(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Capitulation composite: lower-wick ratio + 63d range-position + volume-weighted lower wick.
    Higher = stronger volume-confirmed rejection of lows."""
    lwr = _lwr(open, high, low, close)
    pos = swk_ext_031_lower_wick_range_position(open, high, low, close).fillna(0.5)
    vw = swk_ext_053_vol_weighted_lower_wick_ratio_5d(open, high, low, close, volume).fillna(0.0)
    return lwr.fillna(0.0) + pos + vw


# ── Registry ──────────────────────────────────────────────────────────────────

SHADOW_WICK_ANALYSIS_EXTENDED_REGISTRY_001_075 = {
    "swk_ext_001_log_lower_wick": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_001_log_lower_wick},
    "swk_ext_002_log_upper_wick": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_002_log_upper_wick},
    "swk_ext_003_lower_wick_pct_of_low": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_003_lower_wick_pct_of_low},
    "swk_ext_004_lower_wick_gap_adjusted": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_004_lower_wick_gap_adjusted},
    "swk_ext_005_lower_wick_true_range_ratio": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_005_lower_wick_true_range_ratio},
    "swk_ext_006_lower_wick_pct_of_low_sma21": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_006_lower_wick_pct_of_low_sma21},
    "swk_ext_007_lower_wick_pct_of_low_sma63": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_007_lower_wick_pct_of_low_sma63},
    "swk_ext_008_lower_wick_true_range_ratio_sma21": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_008_lower_wick_true_range_ratio_sma21},
    "swk_ext_009_gap_adjusted_lower_wick_max_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_009_gap_adjusted_lower_wick_max_63d},
    "swk_ext_010_log_lower_wick_sma21": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_010_log_lower_wick_sma21},
    "swk_ext_011_lower_wick_ratio_on_new_21d_low": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_011_lower_wick_ratio_on_new_21d_low},
    "swk_ext_012_lower_wick_ratio_on_new_63d_low": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_012_lower_wick_ratio_on_new_63d_low},
    "swk_ext_013_lower_wick_ratio_on_new_252d_low": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_013_lower_wick_ratio_on_new_252d_low},
    "swk_ext_014_new_21d_low_long_wick_flag": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_014_new_21d_low_long_wick_flag},
    "swk_ext_015_new_low_long_wick_count_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_015_new_low_long_wick_count_63d},
    "swk_ext_016_avg_lower_wick_ratio_new_low_days_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_016_avg_lower_wick_ratio_new_low_days_63d},
    "swk_ext_017_wick_asym_on_new_63d_low": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_017_wick_asym_on_new_63d_low},
    "swk_ext_018_lower_wick_depth_at_new_low": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_018_lower_wick_depth_at_new_low},
    "swk_ext_019_days_since_rejected_new_low": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_019_days_since_rejected_new_low},
    "swk_ext_020_new_low_long_wick_fraction_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_020_new_low_long_wick_fraction_252d},
    "swk_ext_021_lower_wick_vs_prior_ratio": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_021_lower_wick_vs_prior_ratio},
    "swk_ext_022_lower_wick_ratio_1d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_022_lower_wick_ratio_1d_diff},
    "swk_ext_023_lower_wick_ratio_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_023_lower_wick_ratio_5d_diff},
    "swk_ext_024_lower_wick_ratio_21d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_024_lower_wick_ratio_21d_diff},
    "swk_ext_025_lower_wick_ratio_acceleration": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_025_lower_wick_ratio_acceleration},
    "swk_ext_026_lower_wick_bigger_than_prior_flag": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_026_lower_wick_bigger_than_prior_flag},
    "swk_ext_027_lower_wick_rising_streak": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_027_lower_wick_rising_streak},
    "swk_ext_028_lower_wick_bigger_than_prior_count_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_028_lower_wick_bigger_than_prior_count_21d},
    "swk_ext_029_lower_wick_ratio_5d_diff_zscore_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_029_lower_wick_ratio_5d_diff_zscore_63d},
    "swk_ext_030_upper_wick_vs_prior_ratio": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_030_upper_wick_vs_prior_ratio},
    "swk_ext_031_lower_wick_range_position": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_031_lower_wick_range_position},
    "swk_ext_032_lower_wick_range_position_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_032_lower_wick_range_position_252d},
    "swk_ext_033_lower_wick_cluster_5d_sum": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_033_lower_wick_cluster_5d_sum},
    "swk_ext_034_long_lower_wick_cluster_flag_5d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_034_long_lower_wick_cluster_flag_5d},
    "swk_ext_035_long_lower_wick_cluster_flag_10d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_035_long_lower_wick_cluster_flag_10d},
    "swk_ext_036_lower_wick_cluster_intensity_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_036_lower_wick_cluster_intensity_21d},
    "swk_ext_037_lower_wick_weekly_max_position": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_037_lower_wick_weekly_max_position},
    "swk_ext_038_upper_wick_range_position": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_038_upper_wick_range_position},
    "swk_ext_039_lower_wick_cluster_5d_vs_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_039_lower_wick_cluster_5d_vs_63d},
    "swk_ext_040_consec_lower_wick_above_median": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_040_consec_lower_wick_above_median},
    "swk_ext_041_lower_wick_weekly_sum_ratio": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_041_lower_wick_weekly_sum_ratio},
    "swk_ext_042_lower_wick_monthly_sum_ratio": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_042_lower_wick_monthly_sum_ratio},
    "swk_ext_043_lower_wick_quarterly_sum_ratio": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_043_lower_wick_quarterly_sum_ratio},
    "swk_ext_044_upper_wick_monthly_sum_ratio": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_044_upper_wick_monthly_sum_ratio},
    "swk_ext_045_net_wick_monthly_sum_ratio": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_045_net_wick_monthly_sum_ratio},
    "swk_ext_046_lower_wick_ewm5": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_046_lower_wick_ewm5},
    "swk_ext_047_lower_wick_ewm63": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_047_lower_wick_ewm63},
    "swk_ext_048_lower_wick_ewm5_minus_ewm21": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_048_lower_wick_ewm5_minus_ewm21},
    "swk_ext_049_lower_wick_quarterly_max_position": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_049_lower_wick_quarterly_max_position},
    "swk_ext_050_lower_wick_halfyear_sum_ratio": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_050_lower_wick_halfyear_sum_ratio},
    "swk_ext_051_lower_wick_ratio_volume_z_product": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_ext_051_lower_wick_ratio_volume_z_product},
    "swk_ext_052_lower_wick_ratio_on_volume_spike_days": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_ext_052_lower_wick_ratio_on_volume_spike_days},
    "swk_ext_053_vol_weighted_lower_wick_ratio_5d": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_ext_053_vol_weighted_lower_wick_ratio_5d},
    "swk_ext_054_vol_weighted_lower_wick_ratio_252d": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_ext_054_vol_weighted_lower_wick_ratio_252d},
    "swk_ext_055_high_vol_long_lower_wick_streak": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_ext_055_high_vol_long_lower_wick_streak},
    "swk_ext_056_long_lower_wick_high_vol_count_252d": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_ext_056_long_lower_wick_high_vol_count_252d},
    "swk_ext_057_lower_wick_volume_corr_63d": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_ext_057_lower_wick_volume_corr_63d},
    "swk_ext_058_vol_weighted_wick_asym_21d": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_ext_058_vol_weighted_wick_asym_21d},
    "swk_ext_059_lower_wick_dollar_volume_21d": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_ext_059_lower_wick_dollar_volume_21d},
    "swk_ext_060_lower_wick_on_down_volume_days_21d": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_ext_060_lower_wick_on_down_volume_days_21d},
    "swk_ext_061_lower_wick_ratio_skew_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_061_lower_wick_ratio_skew_21d},
    "swk_ext_062_lower_wick_ratio_skew_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_062_lower_wick_ratio_skew_252d},
    "swk_ext_063_lower_wick_ratio_kurt_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_063_lower_wick_ratio_kurt_63d},
    "swk_ext_064_lower_wick_ratio_iqr_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_064_lower_wick_ratio_iqr_63d},
    "swk_ext_065_lower_wick_ratio_q90_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_065_lower_wick_ratio_q90_63d},
    "swk_ext_066_lower_wick_ratio_std_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_066_lower_wick_ratio_std_252d},
    "swk_ext_067_upper_wick_ratio_skew_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_067_upper_wick_ratio_skew_63d},
    "swk_ext_068_total_wick_ratio_skew_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_068_total_wick_ratio_skew_63d},
    "swk_ext_069_lower_wick_ratio_expanding_max": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_069_lower_wick_ratio_expanding_max},
    "swk_ext_070_lower_wick_ratio_vs_expanding_max": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_070_lower_wick_ratio_vs_expanding_max},
    "swk_ext_071_lower_wick_abs_expanding_pct_rank": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_071_lower_wick_abs_expanding_pct_rank},
    "swk_ext_072_lower_wick_ratio_above_q90_streak": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_072_lower_wick_ratio_above_q90_streak},
    "swk_ext_073_lower_wick_ratio_zscore_126d": {"inputs": ["open", "high", "low", "close"], "func": swk_ext_073_lower_wick_ratio_zscore_126d},
    "swk_ext_074_wick_capitulation_flag": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_ext_074_wick_capitulation_flag},
    "swk_ext_075_wick_capitulation_composite": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_ext_075_wick_capitulation_composite},
}
