"""
55_price_level_distress — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base price-level distress concepts — velocity of penny-stock signals
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def pld_drv2_001_log_close_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of log-close level (velocity of nominal price in log space)."""
    return _log_safe(close).diff(_TD_WEEK)


def pld_drv2_002_log_close_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of log-close level (monthly velocity of nominal price)."""
    return _log_safe(close).diff(_TD_MON)


def pld_drv2_003_dist_to_5_abs_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of absolute distance to $5 (velocity of approach to penny threshold)."""
    return (close - _LVL_5).diff(_TD_WEEK)


def pld_drv2_004_dist_to_5_abs_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of absolute distance to $5."""
    return (close - _LVL_5).diff(_TD_MON)


def pld_drv2_005_consec_below_5_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive-days-below-$5 streak (velocity of streak growth)."""
    streak = _consec_streak(close < _LVL_5)
    return streak.diff(_TD_WEEK)


def pld_drv2_006_consec_below_5_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of consecutive-days-below-$5 streak."""
    streak = _consec_streak(close < _LVL_5)
    return streak.diff(_TD_MON)


def pld_drv2_007_frac_below_5_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day fraction of days below $5."""
    frac = _rolling_count_true(close < _LVL_5, _TD_QTR) / _TD_QTR
    return frac.diff(_TD_WEEK)


def pld_drv2_008_frac_below_5_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day fraction of days below $5."""
    frac = _rolling_count_true(close < _LVL_5, _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def pld_drv2_009_depth_below_5_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of dollar depth below $5 (velocity of sinking into penny territory)."""
    depth = (_LVL_5 - close).clip(lower=0.0)
    return depth.diff(_TD_WEEK)


def pld_drv2_010_depth_below_5_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of dollar depth below $5."""
    depth = (_LVL_5 - close).clip(lower=0.0)
    return depth.diff(_TD_MON)


def pld_drv2_011_trailing_min_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day trailing minimum price (is the floor getting lower?)."""
    tmin = _rolling_min(close, _TD_QTR)
    return tmin.diff(_TD_WEEK)


def pld_drv2_012_trailing_min_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day trailing minimum price."""
    tmin = _rolling_min(close, _TD_YEAR)
    return tmin.diff(_TD_MON)


def pld_drv2_013_frac_below_1_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day fraction of days below $1."""
    frac = _rolling_count_true(close < _LVL_1, _TD_YEAR) / _TD_YEAR
    return frac.diff(_TD_MON)


def pld_drv2_014_log_close_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of log-close over trailing 21 days (trend in nominal price level)."""
    return _linslope(_log_safe(close), _TD_MON)


def pld_drv2_015_log_close_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of log-close over trailing 63 days."""
    return _linslope(_log_safe(close), _TD_QTR)


def pld_drv2_016_close_norm_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close-to-252d-mean ratio (velocity of relative price decline)."""
    norm = _safe_div(close, _rolling_mean(close, _TD_YEAR))
    return norm.diff(_TD_WEEK)


def pld_drv2_017_close_norm_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of close-to-252d-mean ratio."""
    norm = _safe_div(close, _rolling_mean(close, _TD_YEAR))
    return norm.diff(_TD_MON)


def pld_drv2_018_multi_threshold_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of multi-threshold distress score (are more flags being tripped?)."""
    score = (
        (close < _LVL_1).astype(float)
        + (close < _LVL_2).astype(float)
        + (close < _LVL_5).astype(float)
        + (close < _LVL_10).astype(float)
    )
    return score.diff(_TD_WEEK)


def pld_drv2_019_consec_below_1_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive-days-below-$1 streak."""
    streak = _consec_streak(close < _LVL_1)
    return streak.diff(_TD_WEEK)


def pld_drv2_020_depth_below_1_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of dollar depth below $1."""
    depth = (_LVL_1 - close).clip(lower=0.0)
    return depth.diff(_TD_MON)


def pld_drv2_021_close_zscore_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day z-score of nominal close (velocity of z-score decline)."""
    m = _rolling_mean(close, _TD_YEAR)
    s = _rolling_std(close, _TD_YEAR)
    z = _safe_div(close - m, s)
    return z.diff(_TD_WEEK)


def pld_drv2_022_vwap21_level_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day VWAP level (velocity of volume-weighted price decline)."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    return vwap.diff(_TD_WEEK)


def pld_drv2_023_frac_below_5_252d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 252-day fraction-below-$5 over trailing 21 days."""
    frac = _rolling_count_true(close < _LVL_5, _TD_YEAR) / _TD_YEAR
    return _linslope(frac, _TD_MON)


def pld_drv2_024_close_pct_rank_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day percentile rank of nominal close."""
    pct_rank = close.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return pct_rank.diff(_TD_WEEK)


def pld_drv2_025_price_level_cv_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day coefficient of variation of nominal price."""
    cv = _safe_div(_rolling_std(close, _TD_QTR), _rolling_mean(close, _TD_QTR))
    return cv.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

PRICE_LEVEL_DISTRESS_REGISTRY_2ND_DERIVATIVES = {
    "pld_drv2_001_log_close_5d_diff": {"inputs": ["close"], "func": pld_drv2_001_log_close_5d_diff},
    "pld_drv2_002_log_close_21d_diff": {"inputs": ["close"], "func": pld_drv2_002_log_close_21d_diff},
    "pld_drv2_003_dist_to_5_abs_5d_diff": {"inputs": ["close"], "func": pld_drv2_003_dist_to_5_abs_5d_diff},
    "pld_drv2_004_dist_to_5_abs_21d_diff": {"inputs": ["close"], "func": pld_drv2_004_dist_to_5_abs_21d_diff},
    "pld_drv2_005_consec_below_5_5d_diff": {"inputs": ["close"], "func": pld_drv2_005_consec_below_5_5d_diff},
    "pld_drv2_006_consec_below_5_21d_diff": {"inputs": ["close"], "func": pld_drv2_006_consec_below_5_21d_diff},
    "pld_drv2_007_frac_below_5_63d_5d_diff": {"inputs": ["close"], "func": pld_drv2_007_frac_below_5_63d_5d_diff},
    "pld_drv2_008_frac_below_5_63d_21d_diff": {"inputs": ["close"], "func": pld_drv2_008_frac_below_5_63d_21d_diff},
    "pld_drv2_009_depth_below_5_5d_diff": {"inputs": ["close"], "func": pld_drv2_009_depth_below_5_5d_diff},
    "pld_drv2_010_depth_below_5_21d_diff": {"inputs": ["close"], "func": pld_drv2_010_depth_below_5_21d_diff},
    "pld_drv2_011_trailing_min_63d_5d_diff": {"inputs": ["close"], "func": pld_drv2_011_trailing_min_63d_5d_diff},
    "pld_drv2_012_trailing_min_252d_21d_diff": {"inputs": ["close"], "func": pld_drv2_012_trailing_min_252d_21d_diff},
    "pld_drv2_013_frac_below_1_252d_21d_diff": {"inputs": ["close"], "func": pld_drv2_013_frac_below_1_252d_21d_diff},
    "pld_drv2_014_log_close_slope_21d": {"inputs": ["close"], "func": pld_drv2_014_log_close_slope_21d},
    "pld_drv2_015_log_close_slope_63d": {"inputs": ["close"], "func": pld_drv2_015_log_close_slope_63d},
    "pld_drv2_016_close_norm_252d_5d_diff": {"inputs": ["close"], "func": pld_drv2_016_close_norm_252d_5d_diff},
    "pld_drv2_017_close_norm_252d_21d_diff": {"inputs": ["close"], "func": pld_drv2_017_close_norm_252d_21d_diff},
    "pld_drv2_018_multi_threshold_score_5d_diff": {"inputs": ["close"], "func": pld_drv2_018_multi_threshold_score_5d_diff},
    "pld_drv2_019_consec_below_1_5d_diff": {"inputs": ["close"], "func": pld_drv2_019_consec_below_1_5d_diff},
    "pld_drv2_020_depth_below_1_21d_diff": {"inputs": ["close"], "func": pld_drv2_020_depth_below_1_21d_diff},
    "pld_drv2_021_close_zscore_252d_5d_diff": {"inputs": ["close"], "func": pld_drv2_021_close_zscore_252d_5d_diff},
    "pld_drv2_022_vwap21_level_5d_diff": {"inputs": ["close", "volume"], "func": pld_drv2_022_vwap21_level_5d_diff},
    "pld_drv2_023_frac_below_5_252d_slope_21d": {"inputs": ["close"], "func": pld_drv2_023_frac_below_5_252d_slope_21d},
    "pld_drv2_024_close_pct_rank_252d_5d_diff": {"inputs": ["close"], "func": pld_drv2_024_close_pct_rank_252d_5d_diff},
    "pld_drv2_025_price_level_cv_63d_21d_diff": {"inputs": ["close"], "func": pld_drv2_025_price_level_cv_63d_21d_diff},
}
