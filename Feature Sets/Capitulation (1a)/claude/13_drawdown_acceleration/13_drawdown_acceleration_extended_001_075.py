"""
13_drawdown_acceleration — Extended Features 001-075
Domain: drawdown acceleration — additional depth beyond the 200 base features:
  acceleration over non-standard windows; expanding-high anchor drawdown accel;
  acceleration regime / sign flags; acceleration percentile rank and z-score variants;
  sustained-acceleration streaks; acceleration vs velocity ratio; peak acceleration
  and its recency; acceleration of absolute underwater depth; convexity-based proxies;
  EWM-smoothed acceleration; rolling skew/kurt of acceleration; RoC of acceleration.
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


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).std()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _drawdown(close: pd.Series, w: int) -> pd.Series:
    """Drawdown from rolling w-period high: (close - roll_high) / roll_high."""
    roll_high = _rolling_max(close, w)
    return _safe_div(close - roll_high, roll_high)


def _expanding_drawdown(close: pd.Series) -> pd.Series:
    """Drawdown from expanding (all-history) high."""
    exp_high = close.expanding(min_periods=1).max()
    return _safe_div(close - exp_high, exp_high)


def _log_drawdown(close: pd.Series, w: int) -> pd.Series:
    return _log_safe(close) - _log_safe(_rolling_max(close, w))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods (raw=False for pandas Series input)."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low  - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


# ── Feature functions ext_001-075 ────────────────────────────────────────────

# --- Group A (ext_001-010): Acceleration over non-standard windows ---

def dacc_ext_001_drawdown_10d_accel_3d(close: pd.Series) -> pd.Series:
    """3-day diff of 3-day velocity of 10-day drawdown (ultra-short acceleration)."""
    vel = _drawdown(close, 10).diff(3)
    return vel.diff(3)


def dacc_ext_002_drawdown_42d_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of 42-day drawdown (2-month horizon)."""
    vel = _drawdown(close, 42).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_ext_003_drawdown_189d_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of 189-day drawdown (3-quarter horizon)."""
    vel = _drawdown(close, 189).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_ext_004_drawdown_504d_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of 504-day drawdown (2-year horizon)."""
    vel = _drawdown(close, 504).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_ext_005_drawdown_252d_accel_10d(close: pd.Series) -> pd.Series:
    """10-day diff of 10-day velocity of 252-day drawdown (bi-weekly cadence)."""
    vel = _drawdown(close, _TD_YEAR).diff(10)
    return vel.diff(10)


def dacc_ext_006_drawdown_252d_accel_3d(close: pd.Series) -> pd.Series:
    """3-day diff of 3-day velocity of 252-day drawdown (3-day cadence)."""
    vel = _drawdown(close, _TD_YEAR).diff(3)
    return vel.diff(3)


def dacc_ext_007_drawdown_126d_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of 126-day drawdown (half-year horizon)."""
    vel = _drawdown(close, _TD_HALF).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_ext_008_drawdown_126d_accel_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 5-day velocity of 126-day drawdown."""
    vel = _drawdown(close, _TD_HALF).diff(_TD_WEEK)
    return vel.diff(_TD_MON)


def dacc_ext_009_drawdown_42d_accel_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 5-day velocity of 42-day drawdown."""
    vel = _drawdown(close, 42).diff(_TD_WEEK)
    return vel.diff(_TD_MON)


def dacc_ext_010_log_drawdown_126d_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of log-126-day drawdown."""
    vel = _log_drawdown(close, _TD_HALF).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group B (ext_011-018): Acceleration from expanding-high anchor ---

def dacc_ext_011_expanding_drawdown_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of expanding-high drawdown (all-time anchor)."""
    vel = _expanding_drawdown(close).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_ext_012_expanding_drawdown_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day change in expanding-high drawdown (velocity with all-time anchor)."""
    return _expanding_drawdown(close).diff(_TD_WEEK)


def dacc_ext_013_expanding_drawdown_accel_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 5-day velocity of expanding-high drawdown."""
    vel = _expanding_drawdown(close).diff(_TD_WEEK)
    return vel.diff(_TD_MON)


def dacc_ext_014_expanding_vs_rolling252_accel_diff(close: pd.Series) -> pd.Series:
    """Difference in 5-day acceleration: expanding-high minus rolling-252d anchor."""
    accel_exp = _expanding_drawdown(close).diff(_TD_WEEK).diff(_TD_WEEK)
    accel_252 = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    return accel_exp - accel_252


def dacc_ext_015_expanding_drawdown_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of expanding-high drawdown series."""
    return _linslope(_expanding_drawdown(close), _TD_MON)


def dacc_ext_016_expanding_drawdown_slope_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in 21-day OLS slope of expanding-high drawdown."""
    slp = _linslope(_expanding_drawdown(close), _TD_MON)
    return slp.diff(_TD_WEEK)


def dacc_ext_017_expanding_drawdown_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of expanding-high drawdown within 252-day rolling distribution."""
    dd = _expanding_drawdown(close)
    m  = _rolling_mean(dd, _TD_YEAR)
    s  = _rolling_std(dd, _TD_YEAR)
    return _safe_div(dd - m, s)


def dacc_ext_018_expanding_drawdown_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of expanding-high drawdown in trailing 252-day distribution."""
    dd = _expanding_drawdown(close)
    return dd.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group C (ext_019-027): Acceleration sign flags and regime indicators ---

def dacc_ext_019_accel_sign_flag_252d_5d(close: pd.Series) -> pd.Series:
    """Flag: 5-day acceleration of 252-day drawdown is negative (decline accelerating)."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    return (accel < 0).astype(float)


def dacc_ext_020_accel_sign_flag_63d_5d(close: pd.Series) -> pd.Series:
    """Flag: 5-day acceleration of 63-day drawdown is negative."""
    accel = _drawdown(close, _TD_QTR).diff(_TD_WEEK).diff(_TD_WEEK)
    return (accel < 0).astype(float)


def dacc_ext_021_accel_sign_flag_21d_5d(close: pd.Series) -> pd.Series:
    """Flag: 5-day acceleration of 21-day drawdown is negative."""
    accel = _drawdown(close, _TD_MON).diff(_TD_WEEK).diff(_TD_WEEK)
    return (accel < 0).astype(float)


def dacc_ext_022_accel_negative_streak_252d(close: pd.Series) -> pd.Series:
    """Consecutive days where 1-day acceleration of 252-day drawdown is negative."""
    accel  = _drawdown(close, _TD_YEAR).diff(1).diff(1)
    is_neg = (accel < 0).astype(int)
    group  = (~is_neg.astype(bool)).astype(int).cumsum()
    return is_neg.groupby(group).cumsum().astype(float)


def dacc_ext_023_accel_negative_streak_63d(close: pd.Series) -> pd.Series:
    """Consecutive days where 5-day acceleration of 63-day drawdown is negative."""
    accel  = _drawdown(close, _TD_QTR).diff(_TD_WEEK).diff(_TD_WEEK)
    is_neg = (accel < 0).astype(int)
    group  = (~is_neg.astype(bool)).astype(int).cumsum()
    return is_neg.groupby(group).cumsum().astype(float)


def dacc_ext_024_accel_worse_than_avg_flag_252d(close: pd.Series) -> pd.Series:
    """Flag: current 5-day 252-day drawdown acceleration is worse than its 252-day mean."""
    accel     = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    avg_accel = _rolling_mean(accel, _TD_YEAR)
    return (accel < avg_accel).astype(float)


def dacc_ext_025_accel_neg_count_63d(close: pd.Series) -> pd.Series:
    """Count of days in past 63 days where daily 252-day drawdown acceleration was negative."""
    accel = _drawdown(close, _TD_YEAR).diff(1).diff(1)
    return _rolling_sum((accel < 0).astype(float), _TD_QTR)


def dacc_ext_026_accel_neg_fraction_252d(close: pd.Series) -> pd.Series:
    """Fraction of past 252 days where daily 252-day drawdown acceleration was negative."""
    accel = _drawdown(close, _TD_YEAR).diff(1).diff(1)
    return _rolling_mean((accel < 0).astype(float), _TD_YEAR)


def dacc_ext_027_dual_accel_neg_flag(close: pd.Series) -> pd.Series:
    """Flag: both 21-day and 252-day window 5-day accelerations are simultaneously negative."""
    a21  = _drawdown(close, _TD_MON).diff(_TD_WEEK).diff(_TD_WEEK)
    a252 = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    return ((a21 < 0) & (a252 < 0)).astype(float)


# --- Group D (ext_028-036): Acceleration percentile rank and z-score variants ---

def dacc_ext_028_accel_252d_pct_rank_126d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5-day 252d drawdown acceleration in trailing 126-day window."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    return accel.rolling(_TD_HALF, min_periods=_TD_MON).rank(pct=True)


def dacc_ext_029_accel_252d_zscore_126d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day 252d drawdown acceleration within trailing 126-day distribution."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    m     = _rolling_mean(accel, _TD_HALF)
    s     = _rolling_std(accel, _TD_HALF)
    return _safe_div(accel - m, s)


def dacc_ext_030_accel_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day 63d drawdown acceleration within trailing 252-day distribution."""
    accel = _drawdown(close, _TD_QTR).diff(_TD_WEEK).diff(_TD_WEEK)
    m     = _rolling_mean(accel, _TD_YEAR)
    s     = _rolling_std(accel, _TD_YEAR)
    return _safe_div(accel - m, s)


def dacc_ext_031_accel_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day 21d drawdown acceleration within trailing 252-day distribution."""
    accel = _drawdown(close, _TD_MON).diff(_TD_WEEK).diff(_TD_WEEK)
    m     = _rolling_mean(accel, _TD_YEAR)
    s     = _rolling_std(accel, _TD_YEAR)
    return _safe_div(accel - m, s)


def dacc_ext_032_accel_252d_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding z-score of 5-day 252d drawdown acceleration (all-history extremity)."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    m     = accel.expanding(min_periods=5).mean()
    s     = accel.expanding(min_periods=5).std()
    return _safe_div(accel - m, s)


def dacc_ext_033_accel_252d_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 5-day 252d drawdown acceleration."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    return accel.expanding(min_periods=5).rank(pct=True)


def dacc_ext_034_accel_median_deviation_252d(close: pd.Series) -> pd.Series:
    """Deviation of current 5-day accel from 252-day rolling median (robust centering)."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    med   = _rolling_median(accel, _TD_YEAR)
    return accel - med


def dacc_ext_035_accel_abs_zscore_252d(close: pd.Series) -> pd.Series:
    """Absolute value of 252-day z-score of 5-day 252d drawdown acceleration."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    m     = _rolling_mean(accel, _TD_YEAR)
    s     = _rolling_std(accel, _TD_YEAR)
    z     = _safe_div(accel - m, s)
    return z.abs()


def dacc_ext_036_accel_ewm_zscore_21d(close: pd.Series) -> pd.Series:
    """EWM-based z-score (span=21) of 5-day 252d drawdown acceleration."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    m     = _ewm_mean(accel, _TD_MON)
    s     = _ewm_std(accel, _TD_MON).clip(lower=_EPS)
    return _safe_div(accel - m, s)


# --- Group E (ext_037-043): Sustained-acceleration streaks ---

def dacc_ext_037_sustained_accel_streak_5d_5d(close: pd.Series) -> pd.Series:
    """Days within current consecutive run of negative 5-day 252d accel (scaled to days)."""
    accel  = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    is_neg = (accel < 0).astype(int)
    group  = (~is_neg.astype(bool)).astype(int).cumsum()
    streak = is_neg.groupby(group).cumsum()
    return (streak * _TD_WEEK).astype(float)


def dacc_ext_038_sustained_vel_and_accel_neg_streak(close: pd.Series) -> pd.Series:
    """Streak days: both 5-day velocity AND 5-day acceleration of 252d drawdown negative."""
    vel   = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    both  = ((vel < 0) & (accel < 0)).astype(int)
    group = (~both.astype(bool)).astype(int).cumsum()
    return both.groupby(group).cumsum().astype(float)


def dacc_ext_039_accel_neg_count_21d(close: pd.Series) -> pd.Series:
    """Count of days in past 21 days where daily 252d drawdown acceleration was negative."""
    accel = _drawdown(close, _TD_YEAR).diff(1).diff(1)
    return _rolling_sum((accel < 0).astype(float), _TD_MON)


def dacc_ext_040_new_accel_low_flag_21d(close: pd.Series) -> pd.Series:
    """Flag: today's 5-day 252d accel is the most negative in the past 21 days."""
    accel     = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    prior_min = accel.shift(1).rolling(_TD_MON, min_periods=1).min()
    return (accel < prior_min).astype(float)


def dacc_ext_041_new_accel_low_flag_63d(close: pd.Series) -> pd.Series:
    """Flag: today's 5-day 252d accel is the most negative in the past 63 days."""
    accel     = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    prior_min = accel.shift(1).rolling(_TD_QTR, min_periods=1).min()
    return (accel < prior_min).astype(float)


def dacc_ext_042_accel_neg_run_max_63d(close: pd.Series) -> pd.Series:
    """Maximum length of consecutive negative-acceleration days in trailing 63 days."""
    accel   = _drawdown(close, _TD_YEAR).diff(1).diff(1)
    is_neg  = (accel < 0).astype(int)
    group   = (~is_neg.astype(bool)).astype(int).cumsum()
    streaks = is_neg.groupby(group).cumsum()
    return streaks.rolling(_TD_QTR, min_periods=1).max()


def dacc_ext_043_accel_neg_run_fraction_126d(close: pd.Series) -> pd.Series:
    """Fraction of past 126 days with negative daily 252d drawdown acceleration."""
    accel = _drawdown(close, _TD_YEAR).diff(1).diff(1)
    return _rolling_mean((accel < 0).astype(float), _TD_HALF)


# --- Group F (ext_044-050): Acceleration vs velocity ratio and interactions ---

def dacc_ext_044_accel_vel_ratio_252d_5d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day acceleration to 5-day velocity of 252-day drawdown."""
    vel   = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return _safe_div(accel, vel.abs().replace(0, np.nan))


def dacc_ext_045_accel_vel_ratio_63d_5d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day acceleration to 5-day velocity of 63-day drawdown."""
    vel   = _drawdown(close, _TD_QTR).diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return _safe_div(accel, vel.abs().replace(0, np.nan))


def dacc_ext_046_accel_vel_ratio_21d_5d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day acceleration to 5-day velocity of 21-day drawdown."""
    vel   = _drawdown(close, _TD_MON).diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return _safe_div(accel, vel.abs().replace(0, np.nan))


def dacc_ext_047_accel_vel_sum_252d(close: pd.Series) -> pd.Series:
    """Sum of z-scored velocity and z-scored acceleration of 252d drawdown."""
    vel   = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    vel_z = _safe_div(vel - _rolling_mean(vel, _TD_YEAR),
                      _rolling_std(vel, _TD_YEAR).clip(lower=_EPS))
    acc_z = _safe_div(accel - _rolling_mean(accel, _TD_YEAR),
                      _rolling_std(accel, _TD_YEAR).clip(lower=_EPS))
    return vel_z + acc_z


def dacc_ext_048_accel_as_frac_of_depth_252d(close: pd.Series) -> pd.Series:
    """5-day acceleration of 252d drawdown expressed as fraction of current drawdown depth."""
    dd    = _drawdown(close, _TD_YEAR)
    accel = dd.diff(_TD_WEEK).diff(_TD_WEEK)
    return _safe_div(accel, dd.abs().replace(0, np.nan))


def dacc_ext_049_vel_accel_product_252d(close: pd.Series) -> pd.Series:
    """Product of 5-day velocity and 5-day acceleration of 252d drawdown (signed severity)."""
    vel   = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return vel * accel


def dacc_ext_050_vel_accel_both_neg_depth_score(close: pd.Series) -> pd.Series:
    """Product of absolute velocity and absolute acceleration when both are negative (0 otherwise)."""
    vel   = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    both_neg = (vel < 0) & (accel < 0)
    return (vel.abs() * accel.abs()).where(both_neg, 0.0)


# --- Group G (ext_051-057): Peak acceleration in window and recency ---

def dacc_ext_051_peak_accel_21d(close: pd.Series) -> pd.Series:
    """Worst (most negative) 5-day 252d drawdown acceleration in past 21 days."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    return _rolling_min(accel, _TD_MON)


def dacc_ext_052_peak_accel_63d(close: pd.Series) -> pd.Series:
    """Worst 5-day 252d drawdown acceleration in past 63 days."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    return _rolling_min(accel, _TD_QTR)


def dacc_ext_053_accel_vs_peak_21d_ratio(close: pd.Series) -> pd.Series:
    """Current accel / 21-day worst accel (proximity to recent peak distress)."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    peak  = _rolling_min(accel, _TD_MON).replace(0, np.nan)
    return _safe_div(accel, peak)


def dacc_ext_054_accel_vs_peak_63d_ratio(close: pd.Series) -> pd.Series:
    """Current accel / 63-day worst accel."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    peak  = _rolling_min(accel, _TD_QTR).replace(0, np.nan)
    return _safe_div(accel, peak)


def dacc_ext_055_accel_recovery_from_peak_21d(close: pd.Series) -> pd.Series:
    """Current accel minus 21-day worst accel (recovery magnitude above trough)."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    peak  = _rolling_min(accel, _TD_MON)
    return accel - peak


def dacc_ext_056_peak_accel_ewm_21d(close: pd.Series) -> pd.Series:
    """EWM-21 of the rolling 5-day minimum accel (decay-weighted peak accel memory)."""
    accel    = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    roll_min = _rolling_min(accel, _TD_WEEK)
    return _ewm_mean(roll_min, _TD_MON)


def dacc_ext_057_accel_near_peak_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of past 63 days where accel was within 90% of its 63-day minimum."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    peak  = _rolling_min(accel, _TD_QTR)
    near  = (accel <= peak * 0.9).astype(float)
    return _rolling_mean(near, _TD_QTR)


# --- Group H (ext_058-064): Acceleration of absolute underwater depth ---

def dacc_ext_058_underwater_depth_abs_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of absolute dollar gap to 252-day rolling high."""
    hwm   = _rolling_max(close, _TD_YEAR)
    depth = (hwm - close).clip(lower=0)
    vel   = depth.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_ext_059_underwater_depth_abs_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of absolute dollar gap to 252-day rolling high."""
    hwm   = _rolling_max(close, _TD_YEAR)
    depth = (hwm - close).clip(lower=0)
    return _linslope(depth, _TD_MON)


def dacc_ext_060_underwater_depth_log_accel_5d(close: pd.Series) -> pd.Series:
    """5-day accel of log(1 + dollar_gap/close) — log-scaled depth acceleration."""
    hwm   = _rolling_max(close, _TD_YEAR)
    gap   = (hwm - close).clip(lower=0)
    norm  = _safe_div(gap, close.clip(lower=_EPS))
    depth = np.log1p(norm.fillna(0))
    vel   = depth.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_ext_061_underwater_depth_ewm_accel(close: pd.Series) -> pd.Series:
    """EWM-5 of 1-day change in absolute underwater depth (smoothed depth acceleration)."""
    hwm   = _rolling_max(close, _TD_YEAR)
    depth = (hwm - close).clip(lower=0)
    vel   = depth.diff(1)
    return _ewm_mean(vel, _TD_WEEK)


def dacc_ext_062_underwater_area_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of 21-day cumulative underwater depth area."""
    hwm   = _rolling_max(close, _TD_YEAR)
    depth = (hwm - close).clip(lower=0)
    area  = _rolling_sum(depth, _TD_MON)
    vel   = area.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_ext_063_underwater_depth_abs_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of current dollar gap to 252-day high within 252-day rolling window."""
    hwm   = _rolling_max(close, _TD_YEAR)
    depth = (hwm - close).clip(lower=0)
    m     = _rolling_mean(depth, _TD_YEAR)
    s     = _rolling_std(depth, _TD_YEAR).clip(lower=_EPS)
    return _safe_div(depth - m, s)


def dacc_ext_064_underwater_atr_norm_accel_5d(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day accel of ATR-normalised absolute underwater depth (volatility-adjusted)."""
    hwm   = _rolling_max(high, _TD_YEAR)
    depth = (hwm - close).clip(lower=0)
    atr   = _rolling_mean(_tr(close, high, low), _TD_MON).clip(lower=_EPS)
    norm  = _safe_div(depth, atr)
    vel   = norm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group I (ext_065-070): Convexity-based acceleration proxies ---

def dacc_ext_065_drawdown_convexity_21d(close: pd.Series) -> pd.Series:
    """Convexity of 252d drawdown path: consecutive 1-day diffs of 21-day smooth dd."""
    dd_smooth = _rolling_mean(_drawdown(close, _TD_YEAR), _TD_MON)
    return dd_smooth.diff(1).diff(1)


def dacc_ext_066_drawdown_convexity_5d(close: pd.Series) -> pd.Series:
    """Convexity of 252d drawdown using 5-day rolling mean: second diff of smooth dd."""
    dd_smooth = _rolling_mean(_drawdown(close, _TD_YEAR), _TD_WEEK)
    return dd_smooth.diff(1).diff(1)


def dacc_ext_067_drawdown_slope_minus_ewm_slope(close: pd.Series) -> pd.Series:
    """Diff between 5-day and 21-day OLS slope of 252d drawdown (short slope vs slow slope)."""
    slp5  = _linslope(_drawdown(close, _TD_YEAR), _TD_WEEK)
    slp21 = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    return slp5 - slp21


def dacc_ext_068_drawdown_ewm_convexity_21d(close: pd.Series) -> pd.Series:
    """Convexity (consecutive 1-day diffs) of EWM-21 of 252d drawdown."""
    dd_ewm = _ewm_mean(_drawdown(close, _TD_YEAR), _TD_MON)
    return dd_ewm.diff(1).diff(1)


def dacc_ext_069_drawdown_slope_curvature_5d(close: pd.Series) -> pd.Series:
    """5-day change in 21-day OLS slope of 252d drawdown (curvature of slope)."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    return slp.diff(_TD_WEEK)


def dacc_ext_070_log_drawdown_convexity_21d(close: pd.Series) -> pd.Series:
    """Convexity (consecutive 1-day diffs) of EWM-21 of log 252-day drawdown."""
    ld_ewm = _ewm_mean(_log_drawdown(close, _TD_YEAR), _TD_MON)
    return ld_ewm.diff(1).diff(1)


# --- Group J (ext_071-075): EWM-smoothed accel, skew, kurt, RoC ---

def dacc_ext_071_accel_ewm5_smoothed(close: pd.Series) -> pd.Series:
    """EWM-5 of 5-day 252d drawdown acceleration (ultra-short smoothed signal)."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    return _ewm_mean(accel, _TD_WEEK)


def dacc_ext_072_accel_ewm63_smoothed(close: pd.Series) -> pd.Series:
    """EWM-63 of 5-day 252d drawdown acceleration (slow-decaying acceleration trend)."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    return _ewm_mean(accel, _TD_QTR)


def dacc_ext_073_accel_rolling_skew_63d(close: pd.Series) -> pd.Series:
    """63-day rolling skewness of daily 252d drawdown acceleration (tail asymmetry)."""
    accel = _drawdown(close, _TD_YEAR).diff(1).diff(1)
    return accel.rolling(_TD_QTR, min_periods=_TD_MON).skew()


def dacc_ext_074_accel_rolling_kurt_63d(close: pd.Series) -> pd.Series:
    """63-day rolling excess kurtosis of daily 252d drawdown acceleration (fat tails)."""
    accel = _drawdown(close, _TD_YEAR).diff(1).diff(1)
    return accel.rolling(_TD_QTR, min_periods=_TD_MON).kurt()


def dacc_ext_075_accel_rate_of_change_5d(close: pd.Series) -> pd.Series:
    """5-day rate-of-change of 5-day 252d drawdown acceleration (relative jerk)."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    prior = accel.shift(_TD_WEEK).replace(0, np.nan)
    return _safe_div(accel - prior, prior.abs())


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_ACCELERATION_EXTENDED_REGISTRY_001_075 = {
    "dacc_ext_001_drawdown_10d_accel_3d": {"inputs": ["close"], "func": dacc_ext_001_drawdown_10d_accel_3d},
    "dacc_ext_002_drawdown_42d_accel_5d": {"inputs": ["close"], "func": dacc_ext_002_drawdown_42d_accel_5d},
    "dacc_ext_003_drawdown_189d_accel_5d": {"inputs": ["close"], "func": dacc_ext_003_drawdown_189d_accel_5d},
    "dacc_ext_004_drawdown_504d_accel_5d": {"inputs": ["close"], "func": dacc_ext_004_drawdown_504d_accel_5d},
    "dacc_ext_005_drawdown_252d_accel_10d": {"inputs": ["close"], "func": dacc_ext_005_drawdown_252d_accel_10d},
    "dacc_ext_006_drawdown_252d_accel_3d": {"inputs": ["close"], "func": dacc_ext_006_drawdown_252d_accel_3d},
    "dacc_ext_007_drawdown_126d_accel_5d": {"inputs": ["close"], "func": dacc_ext_007_drawdown_126d_accel_5d},
    "dacc_ext_008_drawdown_126d_accel_21d": {"inputs": ["close"], "func": dacc_ext_008_drawdown_126d_accel_21d},
    "dacc_ext_009_drawdown_42d_accel_21d": {"inputs": ["close"], "func": dacc_ext_009_drawdown_42d_accel_21d},
    "dacc_ext_010_log_drawdown_126d_accel_5d": {"inputs": ["close"], "func": dacc_ext_010_log_drawdown_126d_accel_5d},
    "dacc_ext_011_expanding_drawdown_accel_5d": {"inputs": ["close"], "func": dacc_ext_011_expanding_drawdown_accel_5d},
    "dacc_ext_012_expanding_drawdown_velocity_5d": {"inputs": ["close"], "func": dacc_ext_012_expanding_drawdown_velocity_5d},
    "dacc_ext_013_expanding_drawdown_accel_21d": {"inputs": ["close"], "func": dacc_ext_013_expanding_drawdown_accel_21d},
    "dacc_ext_014_expanding_vs_rolling252_accel_diff": {"inputs": ["close"], "func": dacc_ext_014_expanding_vs_rolling252_accel_diff},
    "dacc_ext_015_expanding_drawdown_slope_21d": {"inputs": ["close"], "func": dacc_ext_015_expanding_drawdown_slope_21d},
    "dacc_ext_016_expanding_drawdown_slope_5d_chg": {"inputs": ["close"], "func": dacc_ext_016_expanding_drawdown_slope_5d_chg},
    "dacc_ext_017_expanding_drawdown_zscore_252d": {"inputs": ["close"], "func": dacc_ext_017_expanding_drawdown_zscore_252d},
    "dacc_ext_018_expanding_drawdown_pct_rank_252d": {"inputs": ["close"], "func": dacc_ext_018_expanding_drawdown_pct_rank_252d},
    "dacc_ext_019_accel_sign_flag_252d_5d": {"inputs": ["close"], "func": dacc_ext_019_accel_sign_flag_252d_5d},
    "dacc_ext_020_accel_sign_flag_63d_5d": {"inputs": ["close"], "func": dacc_ext_020_accel_sign_flag_63d_5d},
    "dacc_ext_021_accel_sign_flag_21d_5d": {"inputs": ["close"], "func": dacc_ext_021_accel_sign_flag_21d_5d},
    "dacc_ext_022_accel_negative_streak_252d": {"inputs": ["close"], "func": dacc_ext_022_accel_negative_streak_252d},
    "dacc_ext_023_accel_negative_streak_63d": {"inputs": ["close"], "func": dacc_ext_023_accel_negative_streak_63d},
    "dacc_ext_024_accel_worse_than_avg_flag_252d": {"inputs": ["close"], "func": dacc_ext_024_accel_worse_than_avg_flag_252d},
    "dacc_ext_025_accel_neg_count_63d": {"inputs": ["close"], "func": dacc_ext_025_accel_neg_count_63d},
    "dacc_ext_026_accel_neg_fraction_252d": {"inputs": ["close"], "func": dacc_ext_026_accel_neg_fraction_252d},
    "dacc_ext_027_dual_accel_neg_flag": {"inputs": ["close"], "func": dacc_ext_027_dual_accel_neg_flag},
    "dacc_ext_028_accel_252d_pct_rank_126d": {"inputs": ["close"], "func": dacc_ext_028_accel_252d_pct_rank_126d},
    "dacc_ext_029_accel_252d_zscore_126d": {"inputs": ["close"], "func": dacc_ext_029_accel_252d_zscore_126d},
    "dacc_ext_030_accel_63d_zscore_252d": {"inputs": ["close"], "func": dacc_ext_030_accel_63d_zscore_252d},
    "dacc_ext_031_accel_21d_zscore_252d": {"inputs": ["close"], "func": dacc_ext_031_accel_21d_zscore_252d},
    "dacc_ext_032_accel_252d_expanding_zscore": {"inputs": ["close"], "func": dacc_ext_032_accel_252d_expanding_zscore},
    "dacc_ext_033_accel_252d_expanding_pct_rank": {"inputs": ["close"], "func": dacc_ext_033_accel_252d_expanding_pct_rank},
    "dacc_ext_034_accel_median_deviation_252d": {"inputs": ["close"], "func": dacc_ext_034_accel_median_deviation_252d},
    "dacc_ext_035_accel_abs_zscore_252d": {"inputs": ["close"], "func": dacc_ext_035_accel_abs_zscore_252d},
    "dacc_ext_036_accel_ewm_zscore_21d": {"inputs": ["close"], "func": dacc_ext_036_accel_ewm_zscore_21d},
    "dacc_ext_037_sustained_accel_streak_5d_5d": {"inputs": ["close"], "func": dacc_ext_037_sustained_accel_streak_5d_5d},
    "dacc_ext_038_sustained_vel_and_accel_neg_streak": {"inputs": ["close"], "func": dacc_ext_038_sustained_vel_and_accel_neg_streak},
    "dacc_ext_039_accel_neg_count_21d": {"inputs": ["close"], "func": dacc_ext_039_accel_neg_count_21d},
    "dacc_ext_040_new_accel_low_flag_21d": {"inputs": ["close"], "func": dacc_ext_040_new_accel_low_flag_21d},
    "dacc_ext_041_new_accel_low_flag_63d": {"inputs": ["close"], "func": dacc_ext_041_new_accel_low_flag_63d},
    "dacc_ext_042_accel_neg_run_max_63d": {"inputs": ["close"], "func": dacc_ext_042_accel_neg_run_max_63d},
    "dacc_ext_043_accel_neg_run_fraction_126d": {"inputs": ["close"], "func": dacc_ext_043_accel_neg_run_fraction_126d},
    "dacc_ext_044_accel_vel_ratio_252d_5d": {"inputs": ["close"], "func": dacc_ext_044_accel_vel_ratio_252d_5d},
    "dacc_ext_045_accel_vel_ratio_63d_5d": {"inputs": ["close"], "func": dacc_ext_045_accel_vel_ratio_63d_5d},
    "dacc_ext_046_accel_vel_ratio_21d_5d": {"inputs": ["close"], "func": dacc_ext_046_accel_vel_ratio_21d_5d},
    "dacc_ext_047_accel_vel_sum_252d": {"inputs": ["close"], "func": dacc_ext_047_accel_vel_sum_252d},
    "dacc_ext_048_accel_as_frac_of_depth_252d": {"inputs": ["close"], "func": dacc_ext_048_accel_as_frac_of_depth_252d},
    "dacc_ext_049_vel_accel_product_252d": {"inputs": ["close"], "func": dacc_ext_049_vel_accel_product_252d},
    "dacc_ext_050_vel_accel_both_neg_depth_score": {"inputs": ["close"], "func": dacc_ext_050_vel_accel_both_neg_depth_score},
    "dacc_ext_051_peak_accel_21d": {"inputs": ["close"], "func": dacc_ext_051_peak_accel_21d},
    "dacc_ext_052_peak_accel_63d": {"inputs": ["close"], "func": dacc_ext_052_peak_accel_63d},
    "dacc_ext_053_accel_vs_peak_21d_ratio": {"inputs": ["close"], "func": dacc_ext_053_accel_vs_peak_21d_ratio},
    "dacc_ext_054_accel_vs_peak_63d_ratio": {"inputs": ["close"], "func": dacc_ext_054_accel_vs_peak_63d_ratio},
    "dacc_ext_055_accel_recovery_from_peak_21d": {"inputs": ["close"], "func": dacc_ext_055_accel_recovery_from_peak_21d},
    "dacc_ext_056_peak_accel_ewm_21d": {"inputs": ["close"], "func": dacc_ext_056_peak_accel_ewm_21d},
    "dacc_ext_057_accel_near_peak_fraction_63d": {"inputs": ["close"], "func": dacc_ext_057_accel_near_peak_fraction_63d},
    "dacc_ext_058_underwater_depth_abs_accel_5d": {"inputs": ["close"], "func": dacc_ext_058_underwater_depth_abs_accel_5d},
    "dacc_ext_059_underwater_depth_abs_slope_21d": {"inputs": ["close"], "func": dacc_ext_059_underwater_depth_abs_slope_21d},
    "dacc_ext_060_underwater_depth_log_accel_5d": {"inputs": ["close"], "func": dacc_ext_060_underwater_depth_log_accel_5d},
    "dacc_ext_061_underwater_depth_ewm_accel": {"inputs": ["close"], "func": dacc_ext_061_underwater_depth_ewm_accel},
    "dacc_ext_062_underwater_area_accel_5d": {"inputs": ["close"], "func": dacc_ext_062_underwater_area_accel_5d},
    "dacc_ext_063_underwater_depth_abs_zscore_252d": {"inputs": ["close"], "func": dacc_ext_063_underwater_depth_abs_zscore_252d},
    "dacc_ext_064_underwater_atr_norm_accel_5d": {"inputs": ["close", "high", "low"], "func": dacc_ext_064_underwater_atr_norm_accel_5d},
    "dacc_ext_065_drawdown_convexity_21d": {"inputs": ["close"], "func": dacc_ext_065_drawdown_convexity_21d},
    "dacc_ext_066_drawdown_convexity_5d": {"inputs": ["close"], "func": dacc_ext_066_drawdown_convexity_5d},
    "dacc_ext_067_drawdown_slope_minus_ewm_slope": {"inputs": ["close"], "func": dacc_ext_067_drawdown_slope_minus_ewm_slope},
    "dacc_ext_068_drawdown_ewm_convexity_21d": {"inputs": ["close"], "func": dacc_ext_068_drawdown_ewm_convexity_21d},
    "dacc_ext_069_drawdown_slope_curvature_5d": {"inputs": ["close"], "func": dacc_ext_069_drawdown_slope_curvature_5d},
    "dacc_ext_070_log_drawdown_convexity_21d": {"inputs": ["close"], "func": dacc_ext_070_log_drawdown_convexity_21d},
    "dacc_ext_071_accel_ewm5_smoothed": {"inputs": ["close"], "func": dacc_ext_071_accel_ewm5_smoothed},
    "dacc_ext_072_accel_ewm63_smoothed": {"inputs": ["close"], "func": dacc_ext_072_accel_ewm63_smoothed},
    "dacc_ext_073_accel_rolling_skew_63d": {"inputs": ["close"], "func": dacc_ext_073_accel_rolling_skew_63d},
    "dacc_ext_074_accel_rolling_kurt_63d": {"inputs": ["close"], "func": dacc_ext_074_accel_rolling_kurt_63d},
    "dacc_ext_075_accel_rate_of_change_5d": {"inputs": ["close"], "func": dacc_ext_075_accel_rate_of_change_5d},
}
