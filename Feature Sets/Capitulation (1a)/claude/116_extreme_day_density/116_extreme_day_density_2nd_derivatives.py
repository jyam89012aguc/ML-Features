"""
116_extreme_day_density — 2nd Derivatives (Features edd_drv2_001-025)
Domain: rate of change of base extreme-day-density features — velocity of extreme day
        arrival rate, spacing changes, density acceleration, and recurrence dynamics.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def edd_drv2_001_count_neg5pct_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day -5% count (velocity of extreme-day arrival rate)."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    return cnt.diff(_TD_WEEK)


def edd_drv2_002_count_neg5pct_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day -5% count (monthly change in quarterly extreme density)."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR)
    return cnt.diff(_TD_MON)


def edd_drv2_003_count_2sigma_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day 2-sigma count (velocity of sigma-extreme arrival)."""
    cnt = _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_MON)
    return cnt.diff(_TD_WEEK)


def edd_drv2_004_frac_neg5pct_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day -5% density fraction (how fast density is rising)."""
    frac = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def edd_drv2_005_frac_neg5pct_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day -5% density fraction."""
    frac = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def edd_drv2_006_days_since_last_neg5pct_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of days-since-last-(-5%)-day (how quickly time elapsed is changing)."""
    elapsed = _time_since_last_extreme(_extreme_flag(close, -0.05))
    return elapsed.diff(_TD_WEEK)


def edd_drv2_007_days_since_last_2sigma_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of days-since-last-2-sigma-day."""
    elapsed = _time_since_last_extreme(_sigma_extreme_flag(close, _TD_QTR, 2.0))
    return elapsed.diff(_TD_WEEK)


def edd_drv2_008_count_neg5pct_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day -5% count (month-over-month change in extreme day count)."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    return cnt.diff(_TD_MON)


def edd_drv2_009_count_neg10pct_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day -10% count."""
    cnt = _rolling_sum(_extreme_flag(close, -0.10), _TD_YEAR)
    return cnt.diff(_TD_MON)


def edd_drv2_010_extreme_sum_ret_5pct_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day sum of returns on -5% days (velocity of cumulative extreme damage)."""
    ret = _daily_return(close)
    flag = _extreme_flag(close, -0.05)
    s = _rolling_sum(ret * flag, _TD_QTR)
    return s.diff(_TD_WEEK)


def edd_drv2_011_frac_2sigma_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day 2-sigma fraction."""
    frac = _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def edd_drv2_012_extreme_density_accel_21_vs_63_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (21d density - 63d density) for -5% days."""
    d21 = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON) / _TD_MON
    d63 = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR) / _TD_QTR
    accel = d21 - d63
    return accel.diff(_TD_WEEK)


def edd_drv2_013_ewm_extreme_density_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EWM-21 extreme density for -5% days."""
    from pandas import Series
    ewm = _extreme_flag(close, -0.05).ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    return ewm.diff(_TD_WEEK)


def edd_drv2_014_count_neg5pct_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day -5% count (trend in extreme arrival rate)."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    return _linslope(cnt, _TD_MON)


def edd_drv2_015_count_2sigma_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day 2-sigma count."""
    cnt = _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_QTR)
    return cnt.diff(_TD_MON)


def edd_drv2_016_multi_threshold_score_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of weighted multi-threshold extreme density score (21d window)."""
    c3 = _rolling_sum(_extreme_flag(close, -0.03), _TD_MON)
    c5 = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    c10 = _rolling_sum(_extreme_flag(close, -0.10), _TD_MON)
    score = c3 + 2.0 * c5 + 4.0 * c10
    return score.diff(_TD_WEEK)


def edd_drv2_017_extreme_ret_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day return z-score (velocity of extreme zscore movement)."""
    ret = _daily_return(close)
    m = _rolling_mean(ret, _TD_YEAR)
    s = _rolling_std(ret, _TD_YEAR)
    z = _safe_div(ret - m, s)
    return z.diff(_TD_WEEK)


def edd_drv2_018_count_neg5pct_21d_vs_252d_ratio_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d/252d -5% density ratio."""
    d21 = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON) / _TD_MON
    d252 = _rolling_sum(_extreme_flag(close, -0.05), _TD_YEAR) / _TD_YEAR
    ratio = _safe_div(d21, d252.clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def edd_drv2_019_days_since_last_neg10pct_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of days-since-last-(-10%)-day."""
    elapsed = _time_since_last_extreme(_extreme_flag(close, -0.10))
    return elapsed.diff(_TD_MON)


def edd_drv2_020_frac_neg5pct_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day -5% fraction."""
    frac = _rolling_sum(_extreme_flag(close, -0.05), _TD_YEAR) / _TD_YEAR
    return frac.diff(_TD_MON)


def edd_drv2_021_extreme_depth_score_5pct_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day excess depth score on -5% days."""
    ret = _daily_return(close)
    excess = (ret - (-0.05)).clip(upper=0.0)
    s = _rolling_sum(excess, _TD_QTR)
    return s.diff(_TD_WEEK)


def edd_drv2_022_count_neg5pct_63d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope over 63 days of the 63-day -5% count (long-run trend in extreme density)."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR)
    return _linslope(cnt, _TD_QTR)


def edd_drv2_023_frac_neg3pct_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day -3% density fraction."""
    frac = _rolling_sum(_extreme_flag(close, -0.03), _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def edd_drv2_024_extreme_density_neg5pct_ewm5_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EWM-5 of -5% flag (very short-term extreme density velocity)."""
    ewm5 = _extreme_flag(close, -0.05).ewm(span=_TD_WEEK, min_periods=max(1, _TD_WEEK // 2)).mean()
    return ewm5.diff(_TD_WEEK)


def edd_drv2_025_count_neg5pct_21d_21d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day change in -5% count over 21 days (slope of velocity)."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    vel = cnt.diff(_TD_MON)
    return _linslope(vel, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

EXTREME_DAY_DENSITY_REGISTRY_2ND_DERIVATIVES = {
    "edd_drv2_001_count_neg5pct_21d_5d_diff": {"inputs": ["close"], "func": edd_drv2_001_count_neg5pct_21d_5d_diff},
    "edd_drv2_002_count_neg5pct_63d_21d_diff": {"inputs": ["close"], "func": edd_drv2_002_count_neg5pct_63d_21d_diff},
    "edd_drv2_003_count_2sigma_21d_5d_diff": {"inputs": ["close"], "func": edd_drv2_003_count_2sigma_21d_5d_diff},
    "edd_drv2_004_frac_neg5pct_21d_5d_diff": {"inputs": ["close"], "func": edd_drv2_004_frac_neg5pct_21d_5d_diff},
    "edd_drv2_005_frac_neg5pct_63d_21d_diff": {"inputs": ["close"], "func": edd_drv2_005_frac_neg5pct_63d_21d_diff},
    "edd_drv2_006_days_since_last_neg5pct_5d_diff": {"inputs": ["close"], "func": edd_drv2_006_days_since_last_neg5pct_5d_diff},
    "edd_drv2_007_days_since_last_2sigma_5d_diff": {"inputs": ["close"], "func": edd_drv2_007_days_since_last_2sigma_5d_diff},
    "edd_drv2_008_count_neg5pct_21d_21d_diff": {"inputs": ["close"], "func": edd_drv2_008_count_neg5pct_21d_21d_diff},
    "edd_drv2_009_count_neg10pct_252d_21d_diff": {"inputs": ["close"], "func": edd_drv2_009_count_neg10pct_252d_21d_diff},
    "edd_drv2_010_extreme_sum_ret_5pct_63d_5d_diff": {"inputs": ["close"], "func": edd_drv2_010_extreme_sum_ret_5pct_63d_5d_diff},
    "edd_drv2_011_frac_2sigma_63d_21d_diff": {"inputs": ["close"], "func": edd_drv2_011_frac_2sigma_63d_21d_diff},
    "edd_drv2_012_extreme_density_accel_21_vs_63_5d_diff": {"inputs": ["close"], "func": edd_drv2_012_extreme_density_accel_21_vs_63_5d_diff},
    "edd_drv2_013_ewm_extreme_density_5d_diff": {"inputs": ["close"], "func": edd_drv2_013_ewm_extreme_density_5d_diff},
    "edd_drv2_014_count_neg5pct_21d_slope_21d": {"inputs": ["close"], "func": edd_drv2_014_count_neg5pct_21d_slope_21d},
    "edd_drv2_015_count_2sigma_63d_21d_diff": {"inputs": ["close"], "func": edd_drv2_015_count_2sigma_63d_21d_diff},
    "edd_drv2_016_multi_threshold_score_21d_5d_diff": {"inputs": ["close"], "func": edd_drv2_016_multi_threshold_score_21d_5d_diff},
    "edd_drv2_017_extreme_ret_zscore_5d_diff": {"inputs": ["close"], "func": edd_drv2_017_extreme_ret_zscore_5d_diff},
    "edd_drv2_018_count_neg5pct_21d_vs_252d_ratio_5d_diff": {"inputs": ["close"], "func": edd_drv2_018_count_neg5pct_21d_vs_252d_ratio_5d_diff},
    "edd_drv2_019_days_since_last_neg10pct_21d_diff": {"inputs": ["close"], "func": edd_drv2_019_days_since_last_neg10pct_21d_diff},
    "edd_drv2_020_frac_neg5pct_252d_21d_diff": {"inputs": ["close"], "func": edd_drv2_020_frac_neg5pct_252d_21d_diff},
    "edd_drv2_021_extreme_depth_score_5pct_63d_5d_diff": {"inputs": ["close"], "func": edd_drv2_021_extreme_depth_score_5pct_63d_5d_diff},
    "edd_drv2_022_count_neg5pct_63d_slope_63d": {"inputs": ["close"], "func": edd_drv2_022_count_neg5pct_63d_slope_63d},
    "edd_drv2_023_frac_neg3pct_21d_5d_diff": {"inputs": ["close"], "func": edd_drv2_023_frac_neg3pct_21d_5d_diff},
    "edd_drv2_024_extreme_density_neg5pct_ewm5_5d_diff": {"inputs": ["close"], "func": edd_drv2_024_extreme_density_neg5pct_ewm5_5d_diff},
    "edd_drv2_025_count_neg5pct_21d_21d_diff_slope_21d": {"inputs": ["close"], "func": edd_drv2_025_count_neg5pct_21d_21d_diff_slope_21d},
}
