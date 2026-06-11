"""
55_price_level_distress — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative price-level features — acceleration of velocity
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

_LVL_1  = 1.0
_LVL_2  = 2.0
_LVL_5  = 5.0
_LVL_10 = 10.0

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


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

def pld_drv3_001_log_close_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of log-close (acceleration of nominal price velocity)."""
    vel = _log_safe(close).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pld_drv3_002_log_close_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day log-close velocity (jerk in monthly price movement)."""
    vel21 = _log_safe(close).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pld_drv3_003_dist_to_5_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of distance-to-$5 (acceleration of approach to threshold)."""
    vel = (close - _LVL_5).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pld_drv3_004_consec_below_5_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of below-$5 streak (acceleration of streak growth)."""
    streak = _consec_streak(close < _LVL_5)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pld_drv3_005_consec_below_5_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of below-$5 streak."""
    streak = _consec_streak(close < _LVL_5)
    vel21 = streak.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pld_drv3_006_frac_below_5_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day fraction-below-$5 (jerk in regime persistence)."""
    frac = _rolling_count_true(close < _LVL_5, _TD_QTR) / _TD_QTR
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pld_drv3_007_depth_below_5_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of dollar depth below $5."""
    depth = (_LVL_5 - close).clip(lower=0.0)
    vel = depth.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pld_drv3_008_trailing_min_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day trailing minimum (acceleration of floor decline)."""
    tmin = _rolling_min(close, _TD_QTR)
    vel = tmin.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pld_drv3_009_log_close_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of log-close (rate of slope change)."""
    slp = _linslope(_log_safe(close), _TD_MON)
    return slp.diff(_TD_WEEK)


def pld_drv3_010_log_close_slope_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day OLS slope of log-close."""
    slp = _linslope(_log_safe(close), _TD_QTR)
    return slp.diff(_TD_WEEK)


def pld_drv3_011_close_norm_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of close-to-252d-mean ratio (acceleration of relative decline)."""
    norm = _safe_div(close, _rolling_mean(close, _TD_YEAR))
    vel = norm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pld_drv3_012_close_norm_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in close-to-252d-mean ratio."""
    norm = _safe_div(close, _rolling_mean(close, _TD_YEAR))
    vel21 = norm.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pld_drv3_013_multi_threshold_score_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of multi-threshold distress score."""
    score = (
        (close < _LVL_1).astype(float)
        + (close < _LVL_2).astype(float)
        + (close < _LVL_5).astype(float)
        + (close < _LVL_10).astype(float)
    )
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pld_drv3_014_close_zscore_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day z-score (acceleration of z-score change)."""
    m = _rolling_mean(close, _TD_YEAR)
    s = _rolling_std(close, _TD_YEAR)
    z = _safe_div(close - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pld_drv3_015_frac_below_5_63d_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63-day fraction-below-$5."""
    frac = _rolling_count_true(close < _LVL_5, _TD_QTR) / _TD_QTR
    slp = _linslope(frac, _TD_MON)
    return slp.diff(_TD_WEEK)


def pld_drv3_016_depth_below_5_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in dollar depth below $5."""
    depth = (_LVL_5 - close).clip(lower=0.0)
    vel21 = depth.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pld_drv3_017_consec_below_1_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive-below-$1 streak (acceleration of $1 streak)."""
    streak = _consec_streak(close < _LVL_1)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pld_drv3_018_trailing_min_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day trailing minimum."""
    tmin = _rolling_min(close, _TD_YEAR)
    vel21 = tmin.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pld_drv3_019_vwap21_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day VWAP level (acceleration of VWAP decline)."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    vel = vwap.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pld_drv3_020_frac_below_1_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day fraction-below-$1."""
    frac = _rolling_count_true(close < _LVL_1, _TD_YEAR) / _TD_YEAR
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pld_drv3_021_log_close_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day log-close velocity (trend in velocity)."""
    vel = _log_safe(close).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def pld_drv3_022_close_pct_rank_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day percentile rank of close."""
    pct_rank = close.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = pct_rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pld_drv3_023_dist_to_5_21d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day change in distance-to-$5."""
    vel21 = (close - _LVL_5).diff(_TD_MON)
    return _linslope(vel21, _TD_MON)


def pld_drv3_024_price_level_cv_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day coefficient of variation."""
    cv = _safe_div(_rolling_std(close, _TD_QTR), _rolling_mean(close, _TD_QTR))
    vel21 = cv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pld_drv3_025_frac_below_5_252d_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 252-day fraction-below-$5 over 21 days."""
    frac = _rolling_count_true(close < _LVL_5, _TD_YEAR) / _TD_YEAR
    slp = _linslope(frac, _TD_MON)
    return slp.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

PRICE_LEVEL_DISTRESS_REGISTRY_3RD_DERIVATIVES = {
    "pld_drv3_001_log_close_5d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_001_log_close_5d_diff_5d_diff},
    "pld_drv3_002_log_close_21d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_002_log_close_21d_diff_5d_diff},
    "pld_drv3_003_dist_to_5_5d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_003_dist_to_5_5d_diff_5d_diff},
    "pld_drv3_004_consec_below_5_5d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_004_consec_below_5_5d_diff_5d_diff},
    "pld_drv3_005_consec_below_5_21d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_005_consec_below_5_21d_diff_5d_diff},
    "pld_drv3_006_frac_below_5_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_006_frac_below_5_63d_5d_diff_5d_diff},
    "pld_drv3_007_depth_below_5_5d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_007_depth_below_5_5d_diff_5d_diff},
    "pld_drv3_008_trailing_min_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_008_trailing_min_63d_5d_diff_5d_diff},
    "pld_drv3_009_log_close_slope_21d_5d_diff": {"inputs": ["close"], "func": pld_drv3_009_log_close_slope_21d_5d_diff},
    "pld_drv3_010_log_close_slope_63d_5d_diff": {"inputs": ["close"], "func": pld_drv3_010_log_close_slope_63d_5d_diff},
    "pld_drv3_011_close_norm_252d_5d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_011_close_norm_252d_5d_diff_5d_diff},
    "pld_drv3_012_close_norm_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_012_close_norm_252d_21d_diff_5d_diff},
    "pld_drv3_013_multi_threshold_score_5d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_013_multi_threshold_score_5d_diff_5d_diff},
    "pld_drv3_014_close_zscore_252d_5d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_014_close_zscore_252d_5d_diff_5d_diff},
    "pld_drv3_015_frac_below_5_63d_slope_5d_diff": {"inputs": ["close"], "func": pld_drv3_015_frac_below_5_63d_slope_5d_diff},
    "pld_drv3_016_depth_below_5_21d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_016_depth_below_5_21d_diff_5d_diff},
    "pld_drv3_017_consec_below_1_5d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_017_consec_below_1_5d_diff_5d_diff},
    "pld_drv3_018_trailing_min_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_018_trailing_min_252d_21d_diff_5d_diff},
    "pld_drv3_019_vwap21_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": pld_drv3_019_vwap21_5d_diff_5d_diff},
    "pld_drv3_020_frac_below_1_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_020_frac_below_1_252d_21d_diff_5d_diff},
    "pld_drv3_021_log_close_5d_diff_slope_21d": {"inputs": ["close"], "func": pld_drv3_021_log_close_5d_diff_slope_21d},
    "pld_drv3_022_close_pct_rank_252d_5d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_022_close_pct_rank_252d_5d_diff_5d_diff},
    "pld_drv3_023_dist_to_5_21d_diff_slope_21d": {"inputs": ["close"], "func": pld_drv3_023_dist_to_5_21d_diff_slope_21d},
    "pld_drv3_024_price_level_cv_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": pld_drv3_024_price_level_cv_63d_21d_diff_5d_diff},
    "pld_drv3_025_frac_below_5_252d_slope_5d_diff": {"inputs": ["close"], "func": pld_drv3_025_frac_below_5_252d_slope_5d_diff},
}
