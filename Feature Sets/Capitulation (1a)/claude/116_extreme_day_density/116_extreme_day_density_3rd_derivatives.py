"""
116_extreme_day_density — 3rd Derivatives (Features edd_drv3_001-025)
Domain: rate of change of 2nd-derivative extreme-day-density features — acceleration of
        extreme day arrival velocity, jerk in density changes, second-order dynamics.
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


def _daily_return(close: pd.Series) -> pd.Series:
    """Simple daily log return."""
    return np.log(close / close.shift(1))


def _extreme_flag(close: pd.Series, threshold: float) -> pd.Series:
    """Binary flag: 1 where daily log return <= threshold, else 0."""
    ret = _daily_return(close)
    return (ret <= threshold).astype(float)


def _sigma_extreme_flag(close: pd.Series, window: int, sigma_mult: float) -> pd.Series:
    """Binary flag: 1 where return <= -sigma_mult * rolling_std over window."""
    ret = _daily_return(close)
    std = _rolling_std(ret, window)
    threshold = -sigma_mult * std
    return (ret <= threshold).astype(float)


def _time_since_last_extreme(flag: pd.Series) -> pd.Series:
    """Days elapsed since the most recent 1 in flag."""
    idx = pd.Series(np.arange(len(flag), dtype=float), index=flag.index)
    last = idx.where(flag == 1.0).ffill()
    elapsed = idx - last
    elapsed = elapsed.where(~flag.isna(), np.nan)
    return elapsed


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def edd_drv3_001_count_neg5pct_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day -5% count (acceleration of extreme day arrival rate)."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def edd_drv3_002_count_neg5pct_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day -5% count (jerk in quarterly density)."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def edd_drv3_003_count_2sigma_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day 2-sigma count (acceleration of sigma extreme arrival)."""
    cnt = _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def edd_drv3_004_frac_neg5pct_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day -5% density fraction (acceleration of density)."""
    frac = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def edd_drv3_005_frac_neg5pct_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day -5% density fraction."""
    frac = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR) / _TD_QTR
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def edd_drv3_006_days_since_last_neg5pct_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of days-since-last-(-5%) (acceleration in elapsed-time change)."""
    elapsed = _time_since_last_extreme(_extreme_flag(close, -0.05))
    vel = elapsed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def edd_drv3_007_days_since_last_2sigma_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of days-since-last-2-sigma-day."""
    elapsed = _time_since_last_extreme(_sigma_extreme_flag(close, _TD_QTR, 2.0))
    vel = elapsed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def edd_drv3_008_extreme_density_accel_21_vs_63_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (21d - 63d) -5% density (jerk in density acceleration)."""
    d21 = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON) / _TD_MON
    d63 = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR) / _TD_QTR
    accel = d21 - d63
    vel = accel.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def edd_drv3_009_ewm_extreme_density_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM-21 extreme density (acceleration of smooth density signal)."""
    ewm = _extreme_flag(close, -0.05).ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    vel = ewm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def edd_drv3_010_count_neg5pct_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 21-day -5% count."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def edd_drv3_011_extreme_sum_ret_5pct_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day extreme return sum (jerk in cumulative damage velocity)."""
    ret = _daily_return(close)
    flag = _extreme_flag(close, -0.05)
    s = _rolling_sum(ret * flag, _TD_QTR)
    vel = s.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def edd_drv3_012_frac_2sigma_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day 2-sigma fraction."""
    frac = _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_QTR) / _TD_QTR
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def edd_drv3_013_multi_threshold_score_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d weighted multi-threshold score (jerk in composite density)."""
    c3 = _rolling_sum(_extreme_flag(close, -0.03), _TD_MON)
    c5 = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    c10 = _rolling_sum(_extreme_flag(close, -0.10), _TD_MON)
    score = c3 + 2.0 * c5 + 4.0 * c10
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def edd_drv3_014_extreme_ret_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day return z-score (acceleration of z-score movement)."""
    ret = _daily_return(close)
    m = _rolling_mean(ret, _TD_YEAR)
    s = _rolling_std(ret, _TD_YEAR)
    z = _safe_div(ret - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def edd_drv3_015_count_neg5pct_21d_vs_252d_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d/252d density ratio (acceleration of relative density shift)."""
    d21 = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON) / _TD_MON
    d252 = _rolling_sum(_extreme_flag(close, -0.05), _TD_YEAR) / _TD_YEAR
    ratio = _safe_div(d21, d252.clip(lower=_EPS))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def edd_drv3_016_count_neg5pct_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21-day -5% count."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def edd_drv3_017_frac_neg5pct_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21-day -5% density fraction."""
    frac = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def edd_drv3_018_count_2sigma_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21-day 2-sigma count."""
    cnt = _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def edd_drv3_019_ewm_extreme_density_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of EWM-21 extreme density."""
    ewm = _extreme_flag(close, -0.05).ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    vel = ewm.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def edd_drv3_020_extreme_depth_score_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day excess depth score on -5% days."""
    ret = _daily_return(close)
    excess = (ret - (-0.05)).clip(upper=0.0)
    s = _rolling_sum(excess, _TD_QTR)
    vel = s.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def edd_drv3_021_frac_neg5pct_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day -5% fraction."""
    frac = _rolling_sum(_extreme_flag(close, -0.05), _TD_YEAR) / _TD_YEAR
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def edd_drv3_022_count_neg5pct_63d_slope_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 63-day OLS slope of 63-day -5% count."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR)
    slope = _linslope(cnt, _TD_QTR)
    return slope.diff(_TD_WEEK)


def edd_drv3_023_frac_neg3pct_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day -3% density fraction."""
    frac = _rolling_sum(_extreme_flag(close, -0.03), _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def edd_drv3_024_days_since_last_neg5pct_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of days-since-last-(-5%)."""
    elapsed = _time_since_last_extreme(_extreme_flag(close, -0.05))
    vel = elapsed.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def edd_drv3_025_count_neg5pct_21d_21d_diff_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of the 5-day diff of 21-day changes in -5% count (slope of velocity slope)."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    vel21 = cnt.diff(_TD_MON)
    vel5 = vel21.diff(_TD_WEEK)
    return _linslope(vel5, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

EXTREME_DAY_DENSITY_REGISTRY_3RD_DERIVATIVES = {
    "edd_drv3_001_count_neg5pct_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_001_count_neg5pct_21d_5d_diff_5d_diff},
    "edd_drv3_002_count_neg5pct_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_002_count_neg5pct_63d_21d_diff_5d_diff},
    "edd_drv3_003_count_2sigma_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_003_count_2sigma_21d_5d_diff_5d_diff},
    "edd_drv3_004_frac_neg5pct_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_004_frac_neg5pct_21d_5d_diff_5d_diff},
    "edd_drv3_005_frac_neg5pct_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_005_frac_neg5pct_63d_21d_diff_5d_diff},
    "edd_drv3_006_days_since_last_neg5pct_5d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_006_days_since_last_neg5pct_5d_diff_5d_diff},
    "edd_drv3_007_days_since_last_2sigma_5d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_007_days_since_last_2sigma_5d_diff_5d_diff},
    "edd_drv3_008_extreme_density_accel_21_vs_63_5d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_008_extreme_density_accel_21_vs_63_5d_diff_5d_diff},
    "edd_drv3_009_ewm_extreme_density_5d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_009_ewm_extreme_density_5d_diff_5d_diff},
    "edd_drv3_010_count_neg5pct_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_010_count_neg5pct_21d_21d_diff_5d_diff},
    "edd_drv3_011_extreme_sum_ret_5pct_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_011_extreme_sum_ret_5pct_63d_5d_diff_5d_diff},
    "edd_drv3_012_frac_2sigma_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_012_frac_2sigma_63d_21d_diff_5d_diff},
    "edd_drv3_013_multi_threshold_score_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_013_multi_threshold_score_21d_5d_diff_5d_diff},
    "edd_drv3_014_extreme_ret_zscore_5d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_014_extreme_ret_zscore_5d_diff_5d_diff},
    "edd_drv3_015_count_neg5pct_21d_vs_252d_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_015_count_neg5pct_21d_vs_252d_ratio_5d_diff_5d_diff},
    "edd_drv3_016_count_neg5pct_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": edd_drv3_016_count_neg5pct_21d_5d_diff_slope_21d},
    "edd_drv3_017_frac_neg5pct_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": edd_drv3_017_frac_neg5pct_21d_5d_diff_slope_21d},
    "edd_drv3_018_count_2sigma_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": edd_drv3_018_count_2sigma_21d_5d_diff_slope_21d},
    "edd_drv3_019_ewm_extreme_density_5d_diff_slope_21d": {"inputs": ["close"], "func": edd_drv3_019_ewm_extreme_density_5d_diff_slope_21d},
    "edd_drv3_020_extreme_depth_score_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_020_extreme_depth_score_63d_5d_diff_5d_diff},
    "edd_drv3_021_frac_neg5pct_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_021_frac_neg5pct_252d_21d_diff_5d_diff},
    "edd_drv3_022_count_neg5pct_63d_slope_63d_5d_diff": {"inputs": ["close"], "func": edd_drv3_022_count_neg5pct_63d_slope_63d_5d_diff},
    "edd_drv3_023_frac_neg3pct_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": edd_drv3_023_frac_neg3pct_21d_5d_diff_5d_diff},
    "edd_drv3_024_days_since_last_neg5pct_5d_diff_slope_21d": {"inputs": ["close"], "func": edd_drv3_024_days_since_last_neg5pct_5d_diff_slope_21d},
    "edd_drv3_025_count_neg5pct_21d_21d_diff_5d_diff_slope_21d": {"inputs": ["close"], "func": edd_drv3_025_count_neg5pct_21d_21d_diff_5d_diff_slope_21d},
}
