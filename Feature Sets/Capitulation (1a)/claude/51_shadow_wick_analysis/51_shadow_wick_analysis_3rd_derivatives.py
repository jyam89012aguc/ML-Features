"""
51_shadow_wick_analysis — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative wick/shadow geometry features —
        acceleration of velocity of lower-wick ratios, wick asymmetry, wick z-scores.
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

def swk_drv3_001_lower_wick_ratio_5d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of lower-wick ratio (acceleration of rejection signal velocity)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    vel = lwr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def swk_drv3_002_lower_wick_ratio_21d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of lower-wick ratio (jerk in monthly change)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    vel21 = lwr.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def swk_drv3_003_upper_wick_ratio_5d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of upper-wick ratio (acceleration of overhead resistance velocity)."""
    uwr = _safe_div(_upper_wick(open, high, low, close), _candle_range(high, low))
    vel = uwr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def swk_drv3_004_wick_asym_ratio_5d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of lower/upper wick ratio (acceleration of asymmetry velocity)."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close).clip(lower=_EPS)
    asym = lw / uw
    vel = asym.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def swk_drv3_005_wick_asym_ratio_21d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in lower/upper wick ratio (jerk of monthly asym change)."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close).clip(lower=_EPS)
    asym = lw / uw
    vel21 = asym.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def swk_drv3_006_lower_wick_sma21_5d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day mean lower-wick ratio (acceleration of trend)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    sma21 = _rolling_mean(lwr, _TD_MON)
    vel = sma21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def swk_drv3_007_long_lower_wick_freq_5d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day long-lower-wick frequency (acceleration of freq change)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    freq21 = _rolling_mean((lwr > 0.33).astype(float), _TD_MON)
    vel = freq21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def swk_drv3_008_lower_wick_zscore_5d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day z-score of lower-wick ratio (acceleration of extremity)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    m = _rolling_mean(lwr, _TD_YEAR)
    s = _rolling_std(lwr, _TD_YEAR)
    z = _safe_div(lwr - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def swk_drv3_009_lower_wick_ratio_slope_21d_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of lower-wick ratio (rate of slope change)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    slp = _linslope(lwr, _TD_MON)
    return slp.diff(_TD_WEEK)


def swk_drv3_010_lower_wick_ratio_slope_63d_21d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of 63-day OLS slope of lower-wick ratio."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    slp = _linslope(lwr, _TD_QTR)
    return slp.diff(_TD_MON)


def swk_drv3_011_total_wick_ratio_5d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of total-wick ratio (acceleration of wick activity)."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close)
    twr = _safe_div(lw + uw, _candle_range(high, low))
    vel = twr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def swk_drv3_012_lower_dominant_fraction_5d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day lower-dominant fraction (acceleration of fraction velocity)."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close)
    flag = (lw > uw).astype(float)
    freq = _rolling_mean(flag, _TD_MON)
    vel = freq.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def swk_drv3_013_lower_wick_sma21_slope_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day SMA of lower-wick ratio (slope acceleration)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    sma21 = _rolling_mean(lwr, _TD_MON)
    slp = _linslope(sma21, _TD_QTR)
    return slp.diff(_TD_WEEK)


def swk_drv3_014_wick_asym_slope_63d_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 63-day OLS slope of wick asymmetry ratio."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close).clip(lower=_EPS)
    asym = lw / uw
    slp = _linslope(asym, _TD_QTR)
    return slp.diff(_TD_WEEK)


def swk_drv3_015_lower_wick_ewm21_5d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM21 of lower-wick ratio (acceleration of EWM momentum)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    e21 = _ewm_mean(lwr, _TD_MON)
    vel = e21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def swk_drv3_016_lower_wick_max_63d_21d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day max lower-wick ratio."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    mx63 = _rolling_max(lwr, _TD_QTR)
    vel21 = mx63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def swk_drv3_017_lower_wick_ratio_pct_rank_5d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day percentile rank of lower-wick ratio."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    rank = lwr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def swk_drv3_018_lower_wick_std_21d_5d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day std of lower-wick ratio (jerk in wick consistency)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    std21 = _rolling_std(lwr, _TD_MON)
    vel = std21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def swk_drv3_019_lower_wick_sum_63d_21d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day cumulative lower-wick ratio."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    sum63 = _rolling_sum(lwr, _TD_QTR)
    vel21 = sum63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def swk_drv3_020_wick_asym_sma21_5d_diff_slope(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day diff of wick-asymmetry SMA (slope of velocity)."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close).clip(lower=_EPS)
    asym_sma = _rolling_mean(lw / uw, _TD_MON)
    vel = asym_sma.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def swk_drv3_021_lower_wick_ratio_5d_diff_slope_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day diff of lower-wick ratio."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    vel = lwr.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def swk_drv3_022_lower_wick_sma63_21d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day mean lower-wick ratio."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    sma63 = _rolling_mean(lwr, _TD_QTR)
    vel21 = sma63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def swk_drv3_023_upper_wick_ratio_21d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of upper-wick ratio (jerk in overhead resistance)."""
    uwr = _safe_div(_upper_wick(open, high, low, close), _candle_range(high, low))
    vel21 = uwr.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def swk_drv3_024_consec_long_lower_wick_5d_diff_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive long-lower-wick streak (acceleration of streak)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    streak = _consec_streak(lwr > 0.33)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def swk_drv3_025_lower_wick_ratio_slope_21d_slope_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope over 63 days of the 21-day OLS slope of lower-wick ratio (curvature)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    slp21 = _linslope(lwr, _TD_MON)
    return _linslope(slp21, _TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

SHADOW_WICK_ANALYSIS_REGISTRY_3RD_DERIVATIVES = {
    "swk_drv3_001_lower_wick_ratio_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_001_lower_wick_ratio_5d_diff_5d_diff},
    "swk_drv3_002_lower_wick_ratio_21d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_002_lower_wick_ratio_21d_diff_5d_diff},
    "swk_drv3_003_upper_wick_ratio_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_003_upper_wick_ratio_5d_diff_5d_diff},
    "swk_drv3_004_wick_asym_ratio_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_004_wick_asym_ratio_5d_diff_5d_diff},
    "swk_drv3_005_wick_asym_ratio_21d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_005_wick_asym_ratio_21d_diff_5d_diff},
    "swk_drv3_006_lower_wick_sma21_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_006_lower_wick_sma21_5d_diff_5d_diff},
    "swk_drv3_007_long_lower_wick_freq_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_007_long_lower_wick_freq_5d_diff_5d_diff},
    "swk_drv3_008_lower_wick_zscore_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_008_lower_wick_zscore_5d_diff_5d_diff},
    "swk_drv3_009_lower_wick_ratio_slope_21d_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_009_lower_wick_ratio_slope_21d_5d_diff},
    "swk_drv3_010_lower_wick_ratio_slope_63d_21d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_010_lower_wick_ratio_slope_63d_21d_diff},
    "swk_drv3_011_total_wick_ratio_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_011_total_wick_ratio_5d_diff_5d_diff},
    "swk_drv3_012_lower_dominant_fraction_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_012_lower_dominant_fraction_5d_diff_5d_diff},
    "swk_drv3_013_lower_wick_sma21_slope_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_013_lower_wick_sma21_slope_5d_diff},
    "swk_drv3_014_wick_asym_slope_63d_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_014_wick_asym_slope_63d_5d_diff},
    "swk_drv3_015_lower_wick_ewm21_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_015_lower_wick_ewm21_5d_diff_5d_diff},
    "swk_drv3_016_lower_wick_max_63d_21d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_016_lower_wick_max_63d_21d_diff_5d_diff},
    "swk_drv3_017_lower_wick_ratio_pct_rank_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_017_lower_wick_ratio_pct_rank_5d_diff_5d_diff},
    "swk_drv3_018_lower_wick_std_21d_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_018_lower_wick_std_21d_5d_diff_5d_diff},
    "swk_drv3_019_lower_wick_sum_63d_21d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_019_lower_wick_sum_63d_21d_diff_5d_diff},
    "swk_drv3_020_wick_asym_sma21_5d_diff_slope": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_020_wick_asym_sma21_5d_diff_slope},
    "swk_drv3_021_lower_wick_ratio_5d_diff_slope_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_021_lower_wick_ratio_5d_diff_slope_21d},
    "swk_drv3_022_lower_wick_sma63_21d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_022_lower_wick_sma63_21d_diff_5d_diff},
    "swk_drv3_023_upper_wick_ratio_21d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_023_upper_wick_ratio_21d_diff_5d_diff},
    "swk_drv3_024_consec_long_lower_wick_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_024_consec_long_lower_wick_5d_diff_5d_diff},
    "swk_drv3_025_lower_wick_ratio_slope_21d_slope_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_drv3_025_lower_wick_ratio_slope_21d_slope_63d},
}
