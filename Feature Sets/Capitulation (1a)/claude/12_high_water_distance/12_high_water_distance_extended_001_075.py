"""
12_high_water_distance — Extended Features 001-075
Domain: distance, time, and recovery metrics relative to high-water marks — extended variants
        using high/low/open prices as HWM anchors, EWM-decayed HWM, rolling-window HWM across
        additional horizons, HWM gap velocity and acceleration, HWM gap z-scores, percentile
        ranks of distance metrics, combined time-distance composites, and capitulation signals.
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


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _expanding_hwm(s: pd.Series) -> pd.Series:
    return s.expanding(min_periods=1).max()


def _days_since_expanding_max(s: pd.Series) -> pd.Series:
    hwm = _expanding_hwm(s)
    at_peak = (s >= hwm).astype(float)
    result = pd.Series(np.nan, index=s.index)
    last_peak = -1
    for i, val in enumerate(at_peak):
        if val == 1.0:
            last_peak = i
        if last_peak >= 0:
            result.iloc[i] = i - last_peak
    return result


def _days_since_rolling_max(s: pd.Series, w: int) -> pd.Series:
    roll_max = _rolling_max(s, w)
    at_peak = (s >= roll_max).astype(float)
    result = pd.Series(np.nan, index=s.index)
    last_peak = -1
    for i, val in enumerate(at_peak):
        if val == 1.0:
            last_peak = i
        if last_peak >= 0:
            result.iloc[i] = i - last_peak
    return result


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): HWM from daily high prices (intraday-peak anchor) ---

def hwd_ext_001_hwm_high_pct_below_ath(high: pd.Series, close: pd.Series) -> pd.Series:
    """Percent of close below all-time high-of-highs: (close - ATH_high) / ATH_high."""
    hwm = _expanding_hwm(high)
    return _safe_div(close - hwm, hwm)


def hwd_ext_002_hwm_high_log_dist_ath(high: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance of close below all-time high-of-highs: log(ATH_high) - log(close)."""
    hwm = _expanding_hwm(high)
    return _log_safe(hwm) - _log_safe(close)


def hwd_ext_003_hwm_high_pct_below_1y(high: pd.Series, close: pd.Series) -> pd.Series:
    """Percent of close below 1-year rolling HWM of daily highs."""
    hwm = _rolling_max(high, _TD_YEAR)
    return _safe_div(close - hwm, hwm)


def hwd_ext_004_hwm_high_pct_below_2y(high: pd.Series, close: pd.Series) -> pd.Series:
    """Percent of close below 2-year rolling HWM of daily highs."""
    hwm = _rolling_max(high, 504)
    return _safe_div(close - hwm, hwm)


def hwd_ext_005_hwm_high_regain_multiple_ath(high: pd.Series, close: pd.Series) -> pd.Series:
    """Multiple needed for close to reach all-time high-of-highs: ATH_high / close."""
    hwm = _expanding_hwm(high)
    return _safe_div(hwm, close)


def hwd_ext_006_days_since_high_ath(high: pd.Series) -> pd.Series:
    """Days since the daily-high ATH was last set."""
    return _days_since_expanding_max(high)


def hwd_ext_007_days_since_high_1y_hwm(high: pd.Series) -> pd.Series:
    """Days since the 1-year rolling max of daily highs was last set."""
    return _days_since_rolling_max(high, _TD_YEAR)


def hwd_ext_008_frac_252d_close_below_high_ath(high: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 252 days where close was below expanding ATH-of-highs."""
    hwm = _expanding_hwm(high)
    below = (close < hwm).astype(float)
    return _rolling_mean(below, _TD_YEAR)


def hwd_ext_009_hwm_high_1y_vs_hwm_close_1y_ratio(high: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 1y high-HWM to 1y close-HWM (measures intraday-peak premium vs close peak)."""
    hwm_high  = _rolling_max(high, _TD_YEAR)
    hwm_close = _rolling_max(close, _TD_YEAR)
    return _safe_div(hwm_high, hwm_close)


def hwd_ext_010_hwm_high_ath_log_dist_zscore_252d(high: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (252d) of log distance from close to ATH-of-highs."""
    dist = _log_safe(_expanding_hwm(high)) - _log_safe(close)
    return _zscore_rolling(dist, _TD_YEAR)


# --- Group B (011-020): Low-price and mid-price HWM variants ---

def hwd_ext_011_hwm_low_ath_pct_below(low: pd.Series, close: pd.Series) -> pd.Series:
    """Percent of close below all-time HWM of daily lows (the highest low ever seen)."""
    hwm = _expanding_hwm(low)
    return _safe_div(close - hwm, hwm)


def hwd_ext_012_hwm_low_1y_pct_below(low: pd.Series, close: pd.Series) -> pd.Series:
    """Percent of close below 1-year rolling HWM of daily lows."""
    hwm = _rolling_max(low, _TD_YEAR)
    return _safe_div(close - hwm, hwm)


def hwd_ext_013_hwm_hl_mid_ath_pct_below(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percent of close below all-time HWM of (H+L)/2 midpoints."""
    mid = (high + low) / 2.0
    hwm = _expanding_hwm(mid)
    return _safe_div(close - hwm, hwm)


def hwd_ext_014_hwm_hl_mid_1y_pct_below(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percent of close below 1-year rolling HWM of (H+L)/2 midpoints."""
    mid = (high + low) / 2.0
    hwm = _rolling_max(mid, _TD_YEAR)
    return _safe_div(close - hwm, hwm)


def hwd_ext_015_hwm_wclose_ath_pct_below(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percent of close below ATH of weighted close (H+L+2C)/4."""
    wc = (high + low + 2.0 * close) / 4.0
    hwm = _expanding_hwm(wc)
    return _safe_div(close - hwm, hwm)


def hwd_ext_016_hwm_open_ath_pct_below(open: pd.Series, close: pd.Series) -> pd.Series:
    """Percent of close below all-time HWM of daily open prices."""
    hwm = _expanding_hwm(open)
    return _safe_div(close - hwm, hwm)


def hwd_ext_017_days_since_hl_mid_ath(high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since the ATH of (H+L)/2 midpoints was last set."""
    mid = (high + low) / 2.0
    return _days_since_expanding_max(mid)


def hwd_ext_018_hwm_low_1y_vs_hwm_close_1y_ratio(low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 1y-high-of-lows to 1y-high-of-closes (lowest-low premium to close peak)."""
    hwm_low   = _rolling_max(low, _TD_YEAR)
    hwm_close = _rolling_max(close, _TD_YEAR)
    return _safe_div(hwm_low, hwm_close)


def hwd_ext_019_hwm_high_ath_pct_below_zscore_252d(high: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (252d) of percent below ATH-of-highs."""
    dist = _safe_div(close - _expanding_hwm(high), _expanding_hwm(high))
    return _zscore_rolling(dist, _TD_YEAR)


def hwd_ext_020_hwm_hl_mid_1y_pct_below_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (252d) of percent of close below 1y HWM of midpoints."""
    mid = (high + low) / 2.0
    hwm = _rolling_max(mid, _TD_YEAR)
    dist = _safe_div(close - hwm, hwm)
    return _zscore_rolling(dist, _TD_YEAR)


# --- Group C (021-030): Additional rolling-window HWM distances ---

def hwd_ext_021_hwm_pct_below_6mo(close: pd.Series) -> pd.Series:
    """Percent below 6-month (126-day) rolling HWM of close."""
    hwm = _rolling_max(close, _TD_HALF)
    return _safe_div(close - hwm, hwm)


def hwd_ext_022_hwm_pct_below_4y(close: pd.Series) -> pd.Series:
    """Percent below 4-year (1008-day) rolling HWM of close."""
    hwm = _rolling_max(close, 1008)
    return _safe_div(close - hwm, hwm)


def hwd_ext_023_hwm_log_dist_6mo(close: pd.Series) -> pd.Series:
    """Log distance below 6-month rolling HWM."""
    hwm = _rolling_max(close, _TD_HALF)
    return _log_safe(hwm) - _log_safe(close)


def hwd_ext_024_hwm_log_dist_4y(close: pd.Series) -> pd.Series:
    """Log distance below 4-year rolling HWM."""
    hwm = _rolling_max(close, 1008)
    return _log_safe(hwm) - _log_safe(close)


def hwd_ext_025_hwm_1y_pct_below_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 1-year HWM distance within 252-day history."""
    dist = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return dist.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def hwd_ext_026_hwm_ath_pct_below_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of ATH distance within 252-day history."""
    hwm = _expanding_hwm(close)
    dist = _safe_div(close - hwm, hwm)
    return dist.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def hwd_ext_027_hwm_6mo_vs_1y_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 6-month HWM to 1-year HWM (recency premium of high-water mark)."""
    hwm6 = _rolling_max(close, _TD_HALF)
    hwm1y = _rolling_max(close, _TD_YEAR)
    return _safe_div(hwm6, hwm1y)


def hwd_ext_028_hwm_1y_vs_2y_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 1-year HWM to 2-year HWM."""
    hwm1y = _rolling_max(close, _TD_YEAR)
    hwm2y = _rolling_max(close, 504)
    return _safe_div(hwm1y, hwm2y)


def hwd_ext_029_hwm_2y_vs_3y_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 2-year HWM to 3-year HWM."""
    hwm2y = _rolling_max(close, 504)
    hwm3y = _rolling_max(close, 756)
    return _safe_div(hwm2y, hwm3y)


def hwd_ext_030_frac_history_below_1y_hwm_expanding(close: pd.Series) -> pd.Series:
    """Expanding fraction of all-history bars where close was below 1-year rolling HWM."""
    hwm = _rolling_max(close, _TD_YEAR)
    below = (close < hwm).astype(float)
    return below.expanding(min_periods=1).mean()


# --- Group D (031-040): Velocity and acceleration of HWM gap ---

def hwd_ext_031_hwm_ath_gap_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day change in percent-below ATH (velocity of gap widening)."""
    dist = _safe_div(close - _expanding_hwm(close), _expanding_hwm(close))
    return dist.diff(_TD_WEEK)


def hwd_ext_032_hwm_ath_gap_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in percent-below ATH (monthly gap velocity)."""
    dist = _safe_div(close - _expanding_hwm(close), _expanding_hwm(close))
    return dist.diff(_TD_MON)


def hwd_ext_033_hwm_1y_gap_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day change in percent-below 1-year HWM."""
    dist = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return dist.diff(_TD_WEEK)


def hwd_ext_034_hwm_1y_gap_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in percent-below 1-year HWM."""
    dist = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return dist.diff(_TD_MON)


def hwd_ext_035_hwm_ath_gap_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day ATH-gap velocity (2nd derivative — is gap widening faster?)."""
    dist = _safe_div(close - _expanding_hwm(close), _expanding_hwm(close))
    vel = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def hwd_ext_036_hwm_1y_gap_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day 1y-HWM-gap velocity (acceleration of recent deterioration)."""
    dist = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    vel = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def hwd_ext_037_hwm_ath_gap_ewm_slope_21d(close: pd.Series) -> pd.Series:
    """EWM-smoothed (21d span) 5-day velocity of ATH gap (smoothed acceleration signal)."""
    dist = _safe_div(close - _expanding_hwm(close), _expanding_hwm(close))
    vel = dist.diff(_TD_WEEK)
    return _ewm_mean(vel, _TD_MON)


def hwd_ext_038_hwm_1y_gap_rolling_std_21d(close: pd.Series) -> pd.Series:
    """21-day rolling std of 1-year HWM gap (volatility of the underwater curve)."""
    dist = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return _rolling_std(dist, _TD_MON)


def hwd_ext_039_hwm_ath_gap_rolling_std_63d(close: pd.Series) -> pd.Series:
    """63-day rolling std of ATH gap."""
    dist = _safe_div(close - _expanding_hwm(close), _expanding_hwm(close))
    return _rolling_std(dist, _TD_QTR)


def hwd_ext_040_hwm_1y_gap_velocity_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score (252d) of 21-day 1y-HWM-gap velocity."""
    dist = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    vel = dist.diff(_TD_MON)
    return _zscore_rolling(vel, _TD_YEAR)


# --- Group E (041-050): EWM-decayed and time-weighted HWM variants ---

def hwd_ext_041_ewm_hwm_52w_pct_below(close: pd.Series) -> pd.Series:
    """Percent of close below its EWM-based 52-week (252-day span) peak proxy."""
    ewm_level = _ewm_mean(close, _TD_YEAR)
    ewm_peak  = ewm_level.expanding(min_periods=1).max()
    return _safe_div(close - ewm_peak, ewm_peak)


def hwd_ext_042_ewm_hwm_26w_pct_below(close: pd.Series) -> pd.Series:
    """Percent of close below its EWM-based 26-week (126-day span) peak proxy."""
    ewm_level = _ewm_mean(close, _TD_HALF)
    ewm_peak  = ewm_level.expanding(min_periods=1).max()
    return _safe_div(close - ewm_peak, ewm_peak)


def hwd_ext_043_hwm_ath_gap_time_product(close: pd.Series) -> pd.Series:
    """Product of ATH-gap fraction and log(days_since_ATH+1) — joint depth-time signal."""
    dist = (-_safe_div(close - _expanding_hwm(close), _expanding_hwm(close))).clip(lower=0.0)
    days = _days_since_expanding_max(close).fillna(0.0)
    return dist * np.log1p(days)


def hwd_ext_044_hwm_ath_gap_times_log_days(close: pd.Series) -> pd.Series:
    """ATH gap magnitude × log(1 + days_since_ATH) / log(252) — normalized staleness-depth."""
    dist = (-_safe_div(close - _expanding_hwm(close), _expanding_hwm(close))).clip(lower=0.0)
    days = _days_since_expanding_max(close).fillna(0.0)
    return dist * np.log1p(days) / np.log(1.0 + _TD_YEAR)


def hwd_ext_045_hwm_1y_gap_times_log_days_1y(close: pd.Series) -> pd.Series:
    """1y-HWM gap magnitude × log(1 + days_since_1y_hwm) — 1-year staleness-depth product."""
    hwm = _rolling_max(close, _TD_YEAR)
    dist = (-_safe_div(close - hwm, hwm)).clip(lower=0.0)
    days = _days_since_rolling_max(close, _TD_YEAR).fillna(0.0)
    return dist * np.log1p(days)


def hwd_ext_046_hwm_ath_gap_pct_rank_expanding(close: pd.Series) -> pd.Series:
    """Expanding (all-history) percentile rank of percent-below-ATH."""
    dist = _safe_div(close - _expanding_hwm(close), _expanding_hwm(close))
    return dist.expanding(min_periods=1).rank(pct=True)


def hwd_ext_047_hwm_1y_gap_pct_rank_expanding(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of percent-below-1y-HWM."""
    dist = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return dist.expanding(min_periods=1).rank(pct=True)


def hwd_ext_048_hwm_ath_gap_ewm_21d(close: pd.Series) -> pd.Series:
    """EWM(21d) of percent-below-ATH (smoothed underwater depth)."""
    dist = _safe_div(close - _expanding_hwm(close), _expanding_hwm(close))
    return _ewm_mean(dist, _TD_MON)


def hwd_ext_049_hwm_1y_gap_ewm_21d(close: pd.Series) -> pd.Series:
    """EWM(21d) of percent-below-1y-HWM."""
    dist = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return _ewm_mean(dist, _TD_MON)


def hwd_ext_050_hwm_ath_gap_expanding_min(close: pd.Series) -> pd.Series:
    """Expanding minimum of percent-below-ATH (deepest-ever underwater fraction)."""
    dist = _safe_div(close - _expanding_hwm(close), _expanding_hwm(close))
    return dist.expanding(min_periods=1).min()


# --- Group F (051-060): HWM gap consecutive / frequency streaks ---

def hwd_ext_051_consec_below_1y_hwm(close: pd.Series) -> pd.Series:
    """Consecutive days below 1-year rolling HWM (unbroken underwater streak)."""
    hwm = _rolling_max(close, _TD_YEAR)
    below = (close < hwm).astype(float)
    result = pd.Series(0.0, index=close.index)
    streak = 0
    for i, b in enumerate(below):
        streak = streak + 1 if b == 1.0 else 0
        result.iloc[i] = streak
    return result


def hwd_ext_052_consec_below_2y_hwm(close: pd.Series) -> pd.Series:
    """Consecutive days below 2-year rolling HWM."""
    hwm = _rolling_max(close, 504)
    below = (close < hwm).astype(float)
    result = pd.Series(0.0, index=close.index)
    streak = 0
    for i, b in enumerate(below):
        streak = streak + 1 if b == 1.0 else 0
        result.iloc[i] = streak
    return result


def hwd_ext_053_frac_63d_below_1y_hwm(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days where close was below 1-year rolling HWM."""
    hwm = _rolling_max(close, _TD_YEAR)
    below = (close < hwm).astype(float)
    return _rolling_mean(below, _TD_QTR)


def hwd_ext_054_frac_21d_below_ath(close: pd.Series) -> pd.Series:
    """Fraction of last 21 days where close was below expanding ATH."""
    hwm = _expanding_hwm(close)
    below = (close < hwm).astype(float)
    return _rolling_mean(below, _TD_MON)


def hwd_ext_055_consec_below_ath_log(close: pd.Series) -> pd.Series:
    """Log(1 + consecutive days below ATH) — compresses extreme underwater streaks."""
    hwm = _expanding_hwm(close)
    below = (close < hwm).astype(float)
    streak = pd.Series(0.0, index=close.index)
    s = 0
    for i, b in enumerate(below):
        s = s + 1 if b == 1.0 else 0
        streak.iloc[i] = s
    return np.log1p(streak)


def hwd_ext_056_days_since_1y_hwm_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of days-since-1y-HWM within 252-day history."""
    days = _days_since_rolling_max(close, _TD_YEAR)
    return days.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def hwd_ext_057_days_since_ath_pct_rank_expanding(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of days-since-ATH."""
    days = _days_since_expanding_max(close)
    return days.expanding(min_periods=1).rank(pct=True)


def hwd_ext_058_frac_504d_below_1y_hwm(close: pd.Series) -> pd.Series:
    """Fraction of last 504 days where close was below the 1-year rolling HWM."""
    hwm = _rolling_max(close, _TD_YEAR)
    below = (close < hwm).astype(float)
    return _rolling_mean(below, 504)


def hwd_ext_059_consec_1y_hwm_below_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score (252d) of current consecutive-below-1y-HWM streak."""
    hwm = _rolling_max(close, _TD_YEAR)
    below = (close < hwm).astype(float)
    streak = pd.Series(0.0, index=close.index)
    s = 0
    for i, b in enumerate(below):
        s = s + 1 if b == 1.0 else 0
        streak.iloc[i] = s
    return _zscore_rolling(streak, _TD_YEAR)


def hwd_ext_060_new_ath_count_252d(close: pd.Series) -> pd.Series:
    """Count of new all-time-high days (close sets a new ATH) in trailing 252 days."""
    hwm_prev = _expanding_hwm(close.shift(1).bfill())
    new_ath = (close > hwm_prev).astype(float)
    return _rolling_sum(new_ath, _TD_YEAR)


# --- Group G (061-068): HWM distance normalized by volatility / volume ---

def hwd_ext_061_hwm_ath_gap_atr_normalized_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATH gap divided by 21-day average true range (ATR) — volatility-normalized depth."""
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    atr = _rolling_mean(tr, _TD_MON)
    gap = (_expanding_hwm(close) - close).clip(lower=0.0)
    return _safe_div(gap, atr)


def hwd_ext_062_hwm_1y_gap_atr_normalized_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """1y-HWM gap divided by 21-day ATR."""
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    atr = _rolling_mean(tr, _TD_MON)
    gap = (_rolling_max(close, _TD_YEAR) - close).clip(lower=0.0)
    return _safe_div(gap, atr)


def hwd_ext_063_hwm_ath_gap_vol_std_normalized_63d(close: pd.Series) -> pd.Series:
    """ATH gap normalized by 63-day return std (z-score style distance from peak)."""
    gap = (-_safe_div(close - _expanding_hwm(close), _expanding_hwm(close))).clip(lower=0.0)
    std = _rolling_std(close.pct_change(1), _TD_QTR)
    return _safe_div(gap, std)


def hwd_ext_064_hwm_1y_gap_vol_std_normalized_63d(close: pd.Series) -> pd.Series:
    """1y-HWM gap normalized by 63-day return std."""
    hwm = _rolling_max(close, _TD_YEAR)
    gap = (-_safe_div(close - hwm, hwm)).clip(lower=0.0)
    std = _rolling_std(close.pct_change(1), _TD_QTR)
    return _safe_div(gap, std)


def hwd_ext_065_hwm_ath_gap_times_volume_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """ATH gap × (volume / 63d-median volume) — high-volume distress amplifier."""
    gap = (-_safe_div(close - _expanding_hwm(close), _expanding_hwm(close))).clip(lower=0.0)
    vol_ratio = _safe_div(volume, _rolling_median(volume, _TD_QTR))
    return gap * vol_ratio


def hwd_ext_066_hwm_1y_gap_ewm_vol_normalized_21d(close: pd.Series) -> pd.Series:
    """EWM(21d) of 1y-HWM gap divided by EWM(21d) of absolute daily return std."""
    hwm = _rolling_max(close, _TD_YEAR)
    gap = (-_safe_div(close - hwm, hwm)).clip(lower=0.0)
    vol_ewm = _ewm_mean(close.pct_change(1).abs(), _TD_MON)
    return _safe_div(_ewm_mean(gap, _TD_MON), vol_ewm)


def hwd_ext_067_hwm_ath_gap_median_63d(close: pd.Series) -> pd.Series:
    """63-day rolling median of percent-below-ATH (robust average underwater depth)."""
    dist = _safe_div(close - _expanding_hwm(close), _expanding_hwm(close))
    return _rolling_median(dist, _TD_QTR)


def hwd_ext_068_hwm_1y_gap_median_63d(close: pd.Series) -> pd.Series:
    """63-day rolling median of percent-below-1y-HWM."""
    dist = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return _rolling_median(dist, _TD_QTR)


# --- Group H (069-075): Composite and capitulation signals ---

def hwd_ext_069_hwm_depth_time_composite_ath(close: pd.Series) -> pd.Series:
    """Capitulation composite: pct-rank(ATH gap) + pct-rank(days_since_ATH)
    within 252-day history, averaged. Higher = deeper and more prolonged distress."""
    hwm = _expanding_hwm(close)
    dist = _safe_div(close - hwm, hwm)
    days = _days_since_expanding_max(close)
    r_dist = dist.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.5)
    r_days = days.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.5)
    return (r_dist + r_days) / 2.0


def hwd_ext_070_hwm_depth_time_composite_1y(close: pd.Series) -> pd.Series:
    """Composite: pct-rank(1y-HWM gap) + pct-rank(days_since_1y_hwm) averaged."""
    hwm = _rolling_max(close, _TD_YEAR)
    dist = _safe_div(close - hwm, hwm)
    days = _days_since_rolling_max(close, _TD_YEAR)
    r_dist = dist.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.5)
    r_days = days.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.5)
    return (r_dist + r_days) / 2.0


def hwd_ext_071_hwm_multi_horizon_gap_sum(close: pd.Series) -> pd.Series:
    """Sum of pct-below HWMs across 1y, 2y, 3y, ATH (multi-horizon distress aggregate)."""
    d1y  = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR)).fillna(0.0)
    d2y  = _safe_div(close - _rolling_max(close, 504), _rolling_max(close, 504)).fillna(0.0)
    d3y  = _safe_div(close - _rolling_max(close, 756), _rolling_max(close, 756)).fillna(0.0)
    dath = _safe_div(close - _expanding_hwm(close), _expanding_hwm(close)).fillna(0.0)
    return d1y + d2y + d3y + dath


def hwd_ext_072_hwm_1y_gap_vs_ath_gap_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 1y-HWM gap to ATH gap (how much of total depth is in the last year)."""
    d1y  = (-_safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))).clip(lower=_EPS)
    dath = (-_safe_div(close - _expanding_hwm(close), _expanding_hwm(close))).clip(lower=_EPS)
    return _safe_div(d1y, dath)


def hwd_ext_073_hwm_ath_gap_consecutive_new_low(close: pd.Series) -> pd.Series:
    """Consecutive days where the ATH gap is wider than the prior day (price declining vs ATH)."""
    gap = (-_safe_div(close - _expanding_hwm(close), _expanding_hwm(close))).clip(lower=0.0)
    widening = (gap > gap.shift(1)).astype(float)
    result = pd.Series(0.0, index=close.index)
    s = 0
    for i, w in enumerate(widening):
        s = s + 1 if w == 1.0 else 0
        result.iloc[i] = s
    return result


def hwd_ext_074_hwm_1y_gap_accel_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day 1y-HWM gap velocity (monthly acceleration)."""
    dist = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    vel = dist.diff(_TD_MON)
    return vel.diff(_TD_MON)


def hwd_ext_075_hwm_capitulation_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Capitulation score: avg of pct-rank(ATH gap) + pct-rank(1y gap) + pct-rank(ATR-norm gap)
    within 252-day window. Higher = more extreme underwater distress."""
    hwm_ath = _expanding_hwm(close)
    d_ath = _safe_div(close - hwm_ath, hwm_ath)
    d_1y  = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    atr = _rolling_mean(tr, _TD_MON)
    d_atr = _safe_div((hwm_ath - close).clip(lower=0.0), atr)
    r1 = d_ath.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.5)
    r2 = d_1y.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.5)
    r3 = d_atr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.5)
    return (r1 + r2 + r3) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

HIGH_WATER_DISTANCE_EXTENDED_REGISTRY_001_075 = {
    "hwd_ext_001_hwm_high_pct_below_ath": {"inputs": ["high", "close"], "func": hwd_ext_001_hwm_high_pct_below_ath},
    "hwd_ext_002_hwm_high_log_dist_ath": {"inputs": ["high", "close"], "func": hwd_ext_002_hwm_high_log_dist_ath},
    "hwd_ext_003_hwm_high_pct_below_1y": {"inputs": ["high", "close"], "func": hwd_ext_003_hwm_high_pct_below_1y},
    "hwd_ext_004_hwm_high_pct_below_2y": {"inputs": ["high", "close"], "func": hwd_ext_004_hwm_high_pct_below_2y},
    "hwd_ext_005_hwm_high_regain_multiple_ath": {"inputs": ["high", "close"], "func": hwd_ext_005_hwm_high_regain_multiple_ath},
    "hwd_ext_006_days_since_high_ath": {"inputs": ["high"], "func": hwd_ext_006_days_since_high_ath},
    "hwd_ext_007_days_since_high_1y_hwm": {"inputs": ["high"], "func": hwd_ext_007_days_since_high_1y_hwm},
    "hwd_ext_008_frac_252d_close_below_high_ath": {"inputs": ["high", "close"], "func": hwd_ext_008_frac_252d_close_below_high_ath},
    "hwd_ext_009_hwm_high_1y_vs_hwm_close_1y_ratio": {"inputs": ["high", "close"], "func": hwd_ext_009_hwm_high_1y_vs_hwm_close_1y_ratio},
    "hwd_ext_010_hwm_high_ath_log_dist_zscore_252d": {"inputs": ["high", "close"], "func": hwd_ext_010_hwm_high_ath_log_dist_zscore_252d},
    "hwd_ext_011_hwm_low_ath_pct_below": {"inputs": ["low", "close"], "func": hwd_ext_011_hwm_low_ath_pct_below},
    "hwd_ext_012_hwm_low_1y_pct_below": {"inputs": ["low", "close"], "func": hwd_ext_012_hwm_low_1y_pct_below},
    "hwd_ext_013_hwm_hl_mid_ath_pct_below": {"inputs": ["high", "low", "close"], "func": hwd_ext_013_hwm_hl_mid_ath_pct_below},
    "hwd_ext_014_hwm_hl_mid_1y_pct_below": {"inputs": ["high", "low", "close"], "func": hwd_ext_014_hwm_hl_mid_1y_pct_below},
    "hwd_ext_015_hwm_wclose_ath_pct_below": {"inputs": ["close", "high", "low"], "func": hwd_ext_015_hwm_wclose_ath_pct_below},
    "hwd_ext_016_hwm_open_ath_pct_below": {"inputs": ["open", "close"], "func": hwd_ext_016_hwm_open_ath_pct_below},
    "hwd_ext_017_days_since_hl_mid_ath": {"inputs": ["high", "low"], "func": hwd_ext_017_days_since_hl_mid_ath},
    "hwd_ext_018_hwm_low_1y_vs_hwm_close_1y_ratio": {"inputs": ["low", "close"], "func": hwd_ext_018_hwm_low_1y_vs_hwm_close_1y_ratio},
    "hwd_ext_019_hwm_high_ath_pct_below_zscore_252d": {"inputs": ["high", "close"], "func": hwd_ext_019_hwm_high_ath_pct_below_zscore_252d},
    "hwd_ext_020_hwm_hl_mid_1y_pct_below_zscore_252d": {"inputs": ["high", "low", "close"], "func": hwd_ext_020_hwm_hl_mid_1y_pct_below_zscore_252d},
    "hwd_ext_021_hwm_pct_below_6mo": {"inputs": ["close"], "func": hwd_ext_021_hwm_pct_below_6mo},
    "hwd_ext_022_hwm_pct_below_4y": {"inputs": ["close"], "func": hwd_ext_022_hwm_pct_below_4y},
    "hwd_ext_023_hwm_log_dist_6mo": {"inputs": ["close"], "func": hwd_ext_023_hwm_log_dist_6mo},
    "hwd_ext_024_hwm_log_dist_4y": {"inputs": ["close"], "func": hwd_ext_024_hwm_log_dist_4y},
    "hwd_ext_025_hwm_1y_pct_below_pct_rank_252d": {"inputs": ["close"], "func": hwd_ext_025_hwm_1y_pct_below_pct_rank_252d},
    "hwd_ext_026_hwm_ath_pct_below_pct_rank_252d": {"inputs": ["close"], "func": hwd_ext_026_hwm_ath_pct_below_pct_rank_252d},
    "hwd_ext_027_hwm_6mo_vs_1y_ratio": {"inputs": ["close"], "func": hwd_ext_027_hwm_6mo_vs_1y_ratio},
    "hwd_ext_028_hwm_1y_vs_2y_ratio": {"inputs": ["close"], "func": hwd_ext_028_hwm_1y_vs_2y_ratio},
    "hwd_ext_029_hwm_2y_vs_3y_ratio": {"inputs": ["close"], "func": hwd_ext_029_hwm_2y_vs_3y_ratio},
    "hwd_ext_030_frac_history_below_1y_hwm_expanding": {"inputs": ["close"], "func": hwd_ext_030_frac_history_below_1y_hwm_expanding},
    "hwd_ext_031_hwm_ath_gap_velocity_5d": {"inputs": ["close"], "func": hwd_ext_031_hwm_ath_gap_velocity_5d},
    "hwd_ext_032_hwm_ath_gap_velocity_21d": {"inputs": ["close"], "func": hwd_ext_032_hwm_ath_gap_velocity_21d},
    "hwd_ext_033_hwm_1y_gap_velocity_5d": {"inputs": ["close"], "func": hwd_ext_033_hwm_1y_gap_velocity_5d},
    "hwd_ext_034_hwm_1y_gap_velocity_21d": {"inputs": ["close"], "func": hwd_ext_034_hwm_1y_gap_velocity_21d},
    "hwd_ext_035_hwm_ath_gap_accel_5d": {"inputs": ["close"], "func": hwd_ext_035_hwm_ath_gap_accel_5d},
    "hwd_ext_036_hwm_1y_gap_accel_5d": {"inputs": ["close"], "func": hwd_ext_036_hwm_1y_gap_accel_5d},
    "hwd_ext_037_hwm_ath_gap_ewm_slope_21d": {"inputs": ["close"], "func": hwd_ext_037_hwm_ath_gap_ewm_slope_21d},
    "hwd_ext_038_hwm_1y_gap_rolling_std_21d": {"inputs": ["close"], "func": hwd_ext_038_hwm_1y_gap_rolling_std_21d},
    "hwd_ext_039_hwm_ath_gap_rolling_std_63d": {"inputs": ["close"], "func": hwd_ext_039_hwm_ath_gap_rolling_std_63d},
    "hwd_ext_040_hwm_1y_gap_velocity_21d_zscore_252d": {"inputs": ["close"], "func": hwd_ext_040_hwm_1y_gap_velocity_21d_zscore_252d},
    "hwd_ext_041_ewm_hwm_52w_pct_below": {"inputs": ["close"], "func": hwd_ext_041_ewm_hwm_52w_pct_below},
    "hwd_ext_042_ewm_hwm_26w_pct_below": {"inputs": ["close"], "func": hwd_ext_042_ewm_hwm_26w_pct_below},
    "hwd_ext_043_hwm_ath_gap_time_product": {"inputs": ["close"], "func": hwd_ext_043_hwm_ath_gap_time_product},
    "hwd_ext_044_hwm_ath_gap_times_log_days": {"inputs": ["close"], "func": hwd_ext_044_hwm_ath_gap_times_log_days},
    "hwd_ext_045_hwm_1y_gap_times_log_days_1y": {"inputs": ["close"], "func": hwd_ext_045_hwm_1y_gap_times_log_days_1y},
    "hwd_ext_046_hwm_ath_gap_pct_rank_expanding": {"inputs": ["close"], "func": hwd_ext_046_hwm_ath_gap_pct_rank_expanding},
    "hwd_ext_047_hwm_1y_gap_pct_rank_expanding": {"inputs": ["close"], "func": hwd_ext_047_hwm_1y_gap_pct_rank_expanding},
    "hwd_ext_048_hwm_ath_gap_ewm_21d": {"inputs": ["close"], "func": hwd_ext_048_hwm_ath_gap_ewm_21d},
    "hwd_ext_049_hwm_1y_gap_ewm_21d": {"inputs": ["close"], "func": hwd_ext_049_hwm_1y_gap_ewm_21d},
    "hwd_ext_050_hwm_ath_gap_expanding_min": {"inputs": ["close"], "func": hwd_ext_050_hwm_ath_gap_expanding_min},
    "hwd_ext_051_consec_below_1y_hwm": {"inputs": ["close"], "func": hwd_ext_051_consec_below_1y_hwm},
    "hwd_ext_052_consec_below_2y_hwm": {"inputs": ["close"], "func": hwd_ext_052_consec_below_2y_hwm},
    "hwd_ext_053_frac_63d_below_1y_hwm": {"inputs": ["close"], "func": hwd_ext_053_frac_63d_below_1y_hwm},
    "hwd_ext_054_frac_21d_below_ath": {"inputs": ["close"], "func": hwd_ext_054_frac_21d_below_ath},
    "hwd_ext_055_consec_below_ath_log": {"inputs": ["close"], "func": hwd_ext_055_consec_below_ath_log},
    "hwd_ext_056_days_since_1y_hwm_pct_rank_252d": {"inputs": ["close"], "func": hwd_ext_056_days_since_1y_hwm_pct_rank_252d},
    "hwd_ext_057_days_since_ath_pct_rank_expanding": {"inputs": ["close"], "func": hwd_ext_057_days_since_ath_pct_rank_expanding},
    "hwd_ext_058_frac_504d_below_1y_hwm": {"inputs": ["close"], "func": hwd_ext_058_frac_504d_below_1y_hwm},
    "hwd_ext_059_consec_1y_hwm_below_zscore_252d": {"inputs": ["close"], "func": hwd_ext_059_consec_1y_hwm_below_zscore_252d},
    "hwd_ext_060_new_ath_count_252d": {"inputs": ["close"], "func": hwd_ext_060_new_ath_count_252d},
    "hwd_ext_061_hwm_ath_gap_atr_normalized_21d": {"inputs": ["close", "high", "low"], "func": hwd_ext_061_hwm_ath_gap_atr_normalized_21d},
    "hwd_ext_062_hwm_1y_gap_atr_normalized_21d": {"inputs": ["close", "high", "low"], "func": hwd_ext_062_hwm_1y_gap_atr_normalized_21d},
    "hwd_ext_063_hwm_ath_gap_vol_std_normalized_63d": {"inputs": ["close"], "func": hwd_ext_063_hwm_ath_gap_vol_std_normalized_63d},
    "hwd_ext_064_hwm_1y_gap_vol_std_normalized_63d": {"inputs": ["close"], "func": hwd_ext_064_hwm_1y_gap_vol_std_normalized_63d},
    "hwd_ext_065_hwm_ath_gap_times_volume_ratio_63d": {"inputs": ["close", "volume"], "func": hwd_ext_065_hwm_ath_gap_times_volume_ratio_63d},
    "hwd_ext_066_hwm_1y_gap_ewm_vol_normalized_21d": {"inputs": ["close"], "func": hwd_ext_066_hwm_1y_gap_ewm_vol_normalized_21d},
    "hwd_ext_067_hwm_ath_gap_median_63d": {"inputs": ["close"], "func": hwd_ext_067_hwm_ath_gap_median_63d},
    "hwd_ext_068_hwm_1y_gap_median_63d": {"inputs": ["close"], "func": hwd_ext_068_hwm_1y_gap_median_63d},
    "hwd_ext_069_hwm_depth_time_composite_ath": {"inputs": ["close"], "func": hwd_ext_069_hwm_depth_time_composite_ath},
    "hwd_ext_070_hwm_depth_time_composite_1y": {"inputs": ["close"], "func": hwd_ext_070_hwm_depth_time_composite_1y},
    "hwd_ext_071_hwm_multi_horizon_gap_sum": {"inputs": ["close"], "func": hwd_ext_071_hwm_multi_horizon_gap_sum},
    "hwd_ext_072_hwm_1y_gap_vs_ath_gap_ratio": {"inputs": ["close"], "func": hwd_ext_072_hwm_1y_gap_vs_ath_gap_ratio},
    "hwd_ext_073_hwm_ath_gap_consecutive_new_low": {"inputs": ["close"], "func": hwd_ext_073_hwm_ath_gap_consecutive_new_low},
    "hwd_ext_074_hwm_1y_gap_accel_21d": {"inputs": ["close"], "func": hwd_ext_074_hwm_1y_gap_accel_21d},
    "hwd_ext_075_hwm_capitulation_score": {"inputs": ["close", "high", "low"], "func": hwd_ext_075_hwm_capitulation_score},
}
