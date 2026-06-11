"""
51_shadow_wick_analysis — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base wick/shadow geometry features —
        velocity of lower-wick ratios, wick asymmetry, wick frequency, wick z-scores.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def swk_drv2_001_lower_wick_ratio_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of lower-wick-to-range ratio (weekly velocity of rejection signal)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    return lwr.diff(_TD_WEEK)


def swk_drv2_002_lower_wick_ratio_21d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of lower-wick-to-range ratio (monthly velocity of rejection signal)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    return lwr.diff(_TD_MON)


def swk_drv2_003_upper_wick_ratio_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of upper-wick-to-range ratio (velocity of overhead resistance)."""
    uwr = _safe_div(_upper_wick(open, high, low, close), _candle_range(high, low))
    return uwr.diff(_TD_WEEK)


def swk_drv2_004_upper_wick_ratio_21d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of upper-wick-to-range ratio."""
    uwr = _safe_div(_upper_wick(open, high, low, close), _candle_range(high, low))
    return uwr.diff(_TD_MON)


def swk_drv2_005_wick_asym_ratio_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of lower/upper wick ratio (velocity of wick asymmetry)."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close).clip(lower=_EPS)
    asym = lw / uw
    return asym.diff(_TD_WEEK)


def swk_drv2_006_wick_asym_ratio_21d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of lower/upper wick ratio."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close).clip(lower=_EPS)
    asym = lw / uw
    return asym.diff(_TD_MON)


def swk_drv2_007_lower_wick_sma21_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day mean lower-wick ratio (trend velocity)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    sma21 = _rolling_mean(lwr, _TD_MON)
    return sma21.diff(_TD_WEEK)


def swk_drv2_008_lower_wick_sma63_21d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of 63-day mean lower-wick ratio."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    sma63 = _rolling_mean(lwr, _TD_QTR)
    return sma63.diff(_TD_MON)


def swk_drv2_009_long_lower_wick_freq_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day long-lower-wick frequency (ratio>0.33)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    freq21 = _rolling_mean((lwr > 0.33).astype(float), _TD_MON)
    return freq21.diff(_TD_WEEK)


def swk_drv2_010_long_lower_wick_freq_21d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of 63-day long-lower-wick frequency."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    freq63 = _rolling_mean((lwr > 0.33).astype(float), _TD_QTR)
    return freq63.diff(_TD_MON)


def swk_drv2_011_lower_wick_zscore_252d_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 252-day z-score of lower-wick ratio (velocity of extremity)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    m = _rolling_mean(lwr, _TD_YEAR)
    s = _rolling_std(lwr, _TD_YEAR)
    z = _safe_div(lwr - m, s)
    return z.diff(_TD_WEEK)


def swk_drv2_012_wick_asym_sma21_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day mean wick asymmetry ratio."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close).clip(lower=_EPS)
    asym_sma = _rolling_mean(lw / uw, _TD_MON)
    return asym_sma.diff(_TD_WEEK)


def swk_drv2_013_total_wick_ratio_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of total-wick-to-range ratio (velocity of overall wick activity)."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close)
    twr = _safe_div(lw + uw, _candle_range(high, low))
    return twr.diff(_TD_WEEK)


def swk_drv2_014_total_wick_ratio_21d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of total-wick-to-range ratio."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close)
    twr = _safe_div(lw + uw, _candle_range(high, low))
    return twr.diff(_TD_MON)


def swk_drv2_015_lower_wick_ratio_slope_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of lower-wick ratio over trailing 21 days."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    return _linslope(lwr, _TD_MON)


def swk_drv2_016_lower_wick_ratio_slope_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of lower-wick ratio over trailing 63 days."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    return _linslope(lwr, _TD_QTR)


def swk_drv2_017_lower_dominant_fraction_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day lower-dominant fraction (fraction with lw > uw)."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close)
    flag = (lw > uw).astype(float)
    freq = _rolling_mean(flag, _TD_MON)
    return freq.diff(_TD_WEEK)


def swk_drv2_018_lower_wick_ratio_ewm21_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of EWM21 of lower-wick ratio."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    e21 = _ewm_mean(lwr, _TD_MON)
    return e21.diff(_TD_WEEK)


def swk_drv2_019_lower_wick_max_63d_21d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of 63-day max lower-wick ratio."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    mx63 = _rolling_max(lwr, _TD_QTR)
    return mx63.diff(_TD_MON)


def swk_drv2_020_lower_wick_ratio_pct_rank_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 252-day percentile rank of lower-wick ratio."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    rank = lwr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    return rank.diff(_TD_WEEK)


def swk_drv2_021_wick_asym_slope_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of lower/upper wick ratio over trailing 63 days."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close).clip(lower=_EPS)
    asym = lw / uw
    return _linslope(asym, _TD_QTR)


def swk_drv2_022_lower_wick_ratio_sma21_slope_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of 21-day SMA of lower-wick ratio over 63-day window."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    sma21 = _rolling_mean(lwr, _TD_MON)
    return _linslope(sma21, _TD_QTR)


def swk_drv2_023_consec_long_lower_wick_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of consecutive long-lower-wick streak length."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    streak = _consec_streak(lwr > 0.33)
    return streak.diff(_TD_WEEK)


def swk_drv2_024_lower_wick_ratio_std_21d_5d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day std of lower-wick ratio (volatility of rejection signal)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    std21 = _rolling_std(lwr, _TD_MON)
    return std21.diff(_TD_WEEK)


def swk_drv2_025_lower_wick_sum_63d_21d_diff(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of 63-day cumulative sum of lower-wick ratio."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    sum63 = _rolling_sum(lwr, _TD_QTR)
    return sum63.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

SHADOW_WICK_ANALYSIS_REGISTRY_2ND_DERIVATIVES = {
    "swk_drv2_001_lower_wick_ratio_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_001_lower_wick_ratio_5d_diff},
    "swk_drv2_002_lower_wick_ratio_21d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_002_lower_wick_ratio_21d_diff},
    "swk_drv2_003_upper_wick_ratio_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_003_upper_wick_ratio_5d_diff},
    "swk_drv2_004_upper_wick_ratio_21d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_004_upper_wick_ratio_21d_diff},
    "swk_drv2_005_wick_asym_ratio_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_005_wick_asym_ratio_5d_diff},
    "swk_drv2_006_wick_asym_ratio_21d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_006_wick_asym_ratio_21d_diff},
    "swk_drv2_007_lower_wick_sma21_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_007_lower_wick_sma21_5d_diff},
    "swk_drv2_008_lower_wick_sma63_21d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_008_lower_wick_sma63_21d_diff},
    "swk_drv2_009_long_lower_wick_freq_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_009_long_lower_wick_freq_5d_diff},
    "swk_drv2_010_long_lower_wick_freq_21d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_010_long_lower_wick_freq_21d_diff},
    "swk_drv2_011_lower_wick_zscore_252d_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_011_lower_wick_zscore_252d_5d_diff},
    "swk_drv2_012_wick_asym_sma21_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_012_wick_asym_sma21_5d_diff},
    "swk_drv2_013_total_wick_ratio_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_013_total_wick_ratio_5d_diff},
    "swk_drv2_014_total_wick_ratio_21d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_014_total_wick_ratio_21d_diff},
    "swk_drv2_015_lower_wick_ratio_slope_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_015_lower_wick_ratio_slope_21d},
    "swk_drv2_016_lower_wick_ratio_slope_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_016_lower_wick_ratio_slope_63d},
    "swk_drv2_017_lower_dominant_fraction_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_017_lower_dominant_fraction_5d_diff},
    "swk_drv2_018_lower_wick_ratio_ewm21_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_018_lower_wick_ratio_ewm21_5d_diff},
    "swk_drv2_019_lower_wick_max_63d_21d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_019_lower_wick_max_63d_21d_diff},
    "swk_drv2_020_lower_wick_ratio_pct_rank_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_020_lower_wick_ratio_pct_rank_5d_diff},
    "swk_drv2_021_wick_asym_slope_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_021_wick_asym_slope_63d},
    "swk_drv2_022_lower_wick_ratio_sma21_slope_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_022_lower_wick_ratio_sma21_slope_63d},
    "swk_drv2_023_consec_long_lower_wick_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_023_consec_long_lower_wick_5d_diff},
    "swk_drv2_024_lower_wick_ratio_std_21d_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_024_lower_wick_ratio_std_21d_5d_diff},
    "swk_drv2_025_lower_wick_sum_63d_21d_diff": {"inputs": ["open", "high", "low", "close"], "func": swk_drv2_025_lower_wick_sum_63d_21d_diff},
}
