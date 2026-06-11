"""
Domain 27: volatility_skewness (vsk_)
Asset Class: US Equities
Target Context: Asymmetry in the return distribution.
"""

import numpy as np
import pandas as pd
from scipy.stats import entropy

# --- Constants ---
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# --- Utility Helpers ---
def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(window=w, min_periods=max(1, w // 2)).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(window=w, min_periods=max(1, w // 2)).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(window=w, min_periods=max(1, w // 2)).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(window=w, min_periods=max(1, w // 2)).std()

def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(window=w, min_periods=max(1, w // 2)).sum()

def _ewm_mean(s: pd.Series, w: int) -> pd.Series:
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    return _safe_div(s - _rolling_mean(s, w), _rolling_std(s, w))

def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.replace(0, np.nan))

def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change()

def _entropy_calc(s: pd.Series, bins: int = 10) -> float:
    if s.isna().all(): return np.nan
    counts, _ = np.histogram(s.dropna(), bins=bins, density=True)
    return entropy(counts + _EPS)

# --- Feature Functions ---
def vsk_001_ret_skew_5d(close) -> pd.Series:
    return _daily_ret(close).rolling(5).skew()

def vsk_002_ret_skew_21d(close) -> pd.Series:
    return _daily_ret(close).rolling(21).skew()

def vsk_003_ret_skew_63d(close) -> pd.Series:
    return _daily_ret(close).rolling(63).skew()

def vsk_004_ret_skew_126d(close) -> pd.Series:
    return _daily_ret(close).rolling(126).skew()

def vsk_005_ret_skew_252d(close) -> pd.Series:
    return _daily_ret(close).rolling(252).skew()

def vsk_006_dd_skew_5d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).rolling(5).skew())(close)

def vsk_007_dd_skew_21d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).rolling(21).skew())(close)

def vsk_008_dd_skew_63d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).rolling(63).skew())(close)

def vsk_009_dd_skew_126d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).rolling(126).skew())(close)

def vsk_010_dd_skew_252d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).rolling(252).skew())(close)

def vsk_011_range_skew_5d(close, high, low) -> pd.Series:
    return _safe_div(high - low, close).rolling(5).skew()

def vsk_012_range_skew_21d(close, high, low) -> pd.Series:
    return _safe_div(high - low, close).rolling(21).skew()

def vsk_013_range_skew_63d(close, high, low) -> pd.Series:
    return _safe_div(high - low, close).rolling(63).skew()

def vsk_014_range_skew_126d(close, high, low) -> pd.Series:
    return _safe_div(high - low, close).rolling(126).skew()

def vsk_015_range_skew_252d(close, high, low) -> pd.Series:
    return _safe_div(high - low, close).rolling(252).skew()

def vsk_016_skew_mom_5d(close) -> pd.Series:
    return _daily_ret(close).rolling(5).skew().diff(5)

def vsk_017_skew_mom_21d(close) -> pd.Series:
    return _daily_ret(close).rolling(21).skew().diff(21)

def vsk_018_skew_mom_63d(close) -> pd.Series:
    return _daily_ret(close).rolling(63).skew().diff(63)

def vsk_019_skew_mom_126d(close) -> pd.Series:
    return _daily_ret(close).rolling(126).skew().diff(126)

def vsk_020_skew_mom_252d(close) -> pd.Series:
    return _daily_ret(close).rolling(252).skew().diff(252)

def vsk_021_skew_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(_daily_ret(close).rolling(5).skew(), 252)

def vsk_022_skew_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(_daily_ret(close).rolling(21).skew(), 252)

def vsk_023_skew_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(_daily_ret(close).rolling(63).skew(), 252)

def vsk_024_skew_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(_daily_ret(close).rolling(126).skew(), 252)

def vsk_025_skew_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(_daily_ret(close).rolling(252).skew(), 252)

def vsk_026_ret_skew_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vsk_001_ret_skew_5d(close), 252)

def vsk_027_ret_skew_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vsk_002_ret_skew_21d(close), 252)

def vsk_028_ret_skew_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vsk_003_ret_skew_63d(close), 252)

def vsk_029_ret_skew_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vsk_004_ret_skew_126d(close), 252)

def vsk_030_ret_skew_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vsk_005_ret_skew_252d(close), 252)

def vsk_031_dd_skew_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vsk_006_dd_skew_5d(close), 252)

def vsk_032_dd_skew_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vsk_007_dd_skew_21d(close), 252)

def vsk_033_dd_skew_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vsk_008_dd_skew_63d(close), 252)

def vsk_034_dd_skew_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vsk_009_dd_skew_126d(close), 252)

def vsk_035_dd_skew_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vsk_010_dd_skew_252d(close), 252)

def vsk_036_range_skew_zscore_5d(close, high, low) -> pd.Series:
    return _zscore_rolling(vsk_011_range_skew_5d(close, high, low), 252)

def vsk_037_range_skew_zscore_21d(close, high, low) -> pd.Series:
    return _zscore_rolling(vsk_012_range_skew_21d(close, high, low), 252)

def vsk_038_range_skew_zscore_63d(close, high, low) -> pd.Series:
    return _zscore_rolling(vsk_013_range_skew_63d(close, high, low), 252)

def vsk_039_range_skew_zscore_126d(close, high, low) -> pd.Series:
    return _zscore_rolling(vsk_014_range_skew_126d(close, high, low), 252)

def vsk_040_range_skew_zscore_252d(close, high, low) -> pd.Series:
    return _zscore_rolling(vsk_015_range_skew_252d(close, high, low), 252)

def vsk_041_skew_mom_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vsk_016_skew_mom_5d(close), 252)

def vsk_042_skew_mom_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vsk_017_skew_mom_21d(close), 252)

def vsk_043_skew_mom_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vsk_018_skew_mom_63d(close), 252)

def vsk_044_skew_mom_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vsk_019_skew_mom_126d(close), 252)

def vsk_045_skew_mom_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vsk_020_skew_mom_252d(close), 252)

def vsk_046_skew_zscore_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vsk_021_skew_zscore_5d(close), 252)

def vsk_047_skew_zscore_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vsk_022_skew_zscore_21d(close), 252)

def vsk_048_skew_zscore_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vsk_023_skew_zscore_63d(close), 252)

def vsk_049_skew_zscore_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vsk_024_skew_zscore_126d(close), 252)

def vsk_050_skew_zscore_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vsk_025_skew_zscore_252d(close), 252)

def vsk_051_ret_skew_rank_5d(close) -> pd.Series:
    return vsk_001_ret_skew_5d(close).rolling(252).rank(pct=True)

def vsk_052_ret_skew_rank_21d(close) -> pd.Series:
    return vsk_002_ret_skew_21d(close).rolling(252).rank(pct=True)

def vsk_053_ret_skew_rank_63d(close) -> pd.Series:
    return vsk_003_ret_skew_63d(close).rolling(252).rank(pct=True)

def vsk_054_ret_skew_rank_126d(close) -> pd.Series:
    return vsk_004_ret_skew_126d(close).rolling(252).rank(pct=True)

def vsk_055_ret_skew_rank_252d(close) -> pd.Series:
    return vsk_005_ret_skew_252d(close).rolling(252).rank(pct=True)

def vsk_056_dd_skew_rank_5d(close) -> pd.Series:
    return vsk_006_dd_skew_5d(close).rolling(252).rank(pct=True)

def vsk_057_dd_skew_rank_21d(close) -> pd.Series:
    return vsk_007_dd_skew_21d(close).rolling(252).rank(pct=True)

def vsk_058_dd_skew_rank_63d(close) -> pd.Series:
    return vsk_008_dd_skew_63d(close).rolling(252).rank(pct=True)

def vsk_059_dd_skew_rank_126d(close) -> pd.Series:
    return vsk_009_dd_skew_126d(close).rolling(252).rank(pct=True)

def vsk_060_dd_skew_rank_252d(close) -> pd.Series:
    return vsk_010_dd_skew_252d(close).rolling(252).rank(pct=True)

def vsk_061_range_skew_rank_5d(close, high, low) -> pd.Series:
    return vsk_011_range_skew_5d(close, high, low).rolling(252).rank(pct=True)

def vsk_062_range_skew_rank_21d(close, high, low) -> pd.Series:
    return vsk_012_range_skew_21d(close, high, low).rolling(252).rank(pct=True)

def vsk_063_range_skew_rank_63d(close, high, low) -> pd.Series:
    return vsk_013_range_skew_63d(close, high, low).rolling(252).rank(pct=True)

def vsk_064_range_skew_rank_126d(close, high, low) -> pd.Series:
    return vsk_014_range_skew_126d(close, high, low).rolling(252).rank(pct=True)

def vsk_065_range_skew_rank_252d(close, high, low) -> pd.Series:
    return vsk_015_range_skew_252d(close, high, low).rolling(252).rank(pct=True)

def vsk_066_skew_mom_rank_5d(close) -> pd.Series:
    return vsk_016_skew_mom_5d(close).rolling(252).rank(pct=True)

def vsk_067_skew_mom_rank_21d(close) -> pd.Series:
    return vsk_017_skew_mom_21d(close).rolling(252).rank(pct=True)

def vsk_068_skew_mom_rank_63d(close) -> pd.Series:
    return vsk_018_skew_mom_63d(close).rolling(252).rank(pct=True)

def vsk_069_skew_mom_rank_126d(close) -> pd.Series:
    return vsk_019_skew_mom_126d(close).rolling(252).rank(pct=True)

def vsk_070_skew_mom_rank_252d(close) -> pd.Series:
    return vsk_020_skew_mom_252d(close).rolling(252).rank(pct=True)

def vsk_071_skew_zscore_rank_5d(close) -> pd.Series:
    return vsk_021_skew_zscore_5d(close).rolling(252).rank(pct=True)

def vsk_072_skew_zscore_rank_21d(close) -> pd.Series:
    return vsk_022_skew_zscore_21d(close).rolling(252).rank(pct=True)

def vsk_073_skew_zscore_rank_63d(close) -> pd.Series:
    return vsk_023_skew_zscore_63d(close).rolling(252).rank(pct=True)

def vsk_074_skew_zscore_rank_126d(close) -> pd.Series:
    return vsk_024_skew_zscore_126d(close).rolling(252).rank(pct=True)

def vsk_075_skew_zscore_rank_252d(close) -> pd.Series:
    return vsk_025_skew_zscore_252d(close).rolling(252).rank(pct=True)


# --- Registry ---
V27_REGISTRY = {
    "vsk_001_ret_skew_5d": {"inputs": ['close'], "func": vsk_001_ret_skew_5d},
    "vsk_002_ret_skew_21d": {"inputs": ['close'], "func": vsk_002_ret_skew_21d},
    "vsk_003_ret_skew_63d": {"inputs": ['close'], "func": vsk_003_ret_skew_63d},
    "vsk_004_ret_skew_126d": {"inputs": ['close'], "func": vsk_004_ret_skew_126d},
    "vsk_005_ret_skew_252d": {"inputs": ['close'], "func": vsk_005_ret_skew_252d},
    "vsk_006_dd_skew_5d": {"inputs": ['close'], "func": vsk_006_dd_skew_5d},
    "vsk_007_dd_skew_21d": {"inputs": ['close'], "func": vsk_007_dd_skew_21d},
    "vsk_008_dd_skew_63d": {"inputs": ['close'], "func": vsk_008_dd_skew_63d},
    "vsk_009_dd_skew_126d": {"inputs": ['close'], "func": vsk_009_dd_skew_126d},
    "vsk_010_dd_skew_252d": {"inputs": ['close'], "func": vsk_010_dd_skew_252d},
    "vsk_011_range_skew_5d": {"inputs": ['close', 'high', 'low'], "func": vsk_011_range_skew_5d},
    "vsk_012_range_skew_21d": {"inputs": ['close', 'high', 'low'], "func": vsk_012_range_skew_21d},
    "vsk_013_range_skew_63d": {"inputs": ['close', 'high', 'low'], "func": vsk_013_range_skew_63d},
    "vsk_014_range_skew_126d": {"inputs": ['close', 'high', 'low'], "func": vsk_014_range_skew_126d},
    "vsk_015_range_skew_252d": {"inputs": ['close', 'high', 'low'], "func": vsk_015_range_skew_252d},
    "vsk_016_skew_mom_5d": {"inputs": ['close'], "func": vsk_016_skew_mom_5d},
    "vsk_017_skew_mom_21d": {"inputs": ['close'], "func": vsk_017_skew_mom_21d},
    "vsk_018_skew_mom_63d": {"inputs": ['close'], "func": vsk_018_skew_mom_63d},
    "vsk_019_skew_mom_126d": {"inputs": ['close'], "func": vsk_019_skew_mom_126d},
    "vsk_020_skew_mom_252d": {"inputs": ['close'], "func": vsk_020_skew_mom_252d},
    "vsk_021_skew_zscore_5d": {"inputs": ['close'], "func": vsk_021_skew_zscore_5d},
    "vsk_022_skew_zscore_21d": {"inputs": ['close'], "func": vsk_022_skew_zscore_21d},
    "vsk_023_skew_zscore_63d": {"inputs": ['close'], "func": vsk_023_skew_zscore_63d},
    "vsk_024_skew_zscore_126d": {"inputs": ['close'], "func": vsk_024_skew_zscore_126d},
    "vsk_025_skew_zscore_252d": {"inputs": ['close'], "func": vsk_025_skew_zscore_252d},
    "vsk_026_ret_skew_zscore_5d": {"inputs": ['close'], "func": vsk_026_ret_skew_zscore_5d},
    "vsk_027_ret_skew_zscore_21d": {"inputs": ['close'], "func": vsk_027_ret_skew_zscore_21d},
    "vsk_028_ret_skew_zscore_63d": {"inputs": ['close'], "func": vsk_028_ret_skew_zscore_63d},
    "vsk_029_ret_skew_zscore_126d": {"inputs": ['close'], "func": vsk_029_ret_skew_zscore_126d},
    "vsk_030_ret_skew_zscore_252d": {"inputs": ['close'], "func": vsk_030_ret_skew_zscore_252d},
    "vsk_031_dd_skew_zscore_5d": {"inputs": ['close'], "func": vsk_031_dd_skew_zscore_5d},
    "vsk_032_dd_skew_zscore_21d": {"inputs": ['close'], "func": vsk_032_dd_skew_zscore_21d},
    "vsk_033_dd_skew_zscore_63d": {"inputs": ['close'], "func": vsk_033_dd_skew_zscore_63d},
    "vsk_034_dd_skew_zscore_126d": {"inputs": ['close'], "func": vsk_034_dd_skew_zscore_126d},
    "vsk_035_dd_skew_zscore_252d": {"inputs": ['close'], "func": vsk_035_dd_skew_zscore_252d},
    "vsk_036_range_skew_zscore_5d": {"inputs": ['close', 'high', 'low'], "func": vsk_036_range_skew_zscore_5d},
    "vsk_037_range_skew_zscore_21d": {"inputs": ['close', 'high', 'low'], "func": vsk_037_range_skew_zscore_21d},
    "vsk_038_range_skew_zscore_63d": {"inputs": ['close', 'high', 'low'], "func": vsk_038_range_skew_zscore_63d},
    "vsk_039_range_skew_zscore_126d": {"inputs": ['close', 'high', 'low'], "func": vsk_039_range_skew_zscore_126d},
    "vsk_040_range_skew_zscore_252d": {"inputs": ['close', 'high', 'low'], "func": vsk_040_range_skew_zscore_252d},
    "vsk_041_skew_mom_zscore_5d": {"inputs": ['close'], "func": vsk_041_skew_mom_zscore_5d},
    "vsk_042_skew_mom_zscore_21d": {"inputs": ['close'], "func": vsk_042_skew_mom_zscore_21d},
    "vsk_043_skew_mom_zscore_63d": {"inputs": ['close'], "func": vsk_043_skew_mom_zscore_63d},
    "vsk_044_skew_mom_zscore_126d": {"inputs": ['close'], "func": vsk_044_skew_mom_zscore_126d},
    "vsk_045_skew_mom_zscore_252d": {"inputs": ['close'], "func": vsk_045_skew_mom_zscore_252d},
    "vsk_046_skew_zscore_zscore_5d": {"inputs": ['close'], "func": vsk_046_skew_zscore_zscore_5d},
    "vsk_047_skew_zscore_zscore_21d": {"inputs": ['close'], "func": vsk_047_skew_zscore_zscore_21d},
    "vsk_048_skew_zscore_zscore_63d": {"inputs": ['close'], "func": vsk_048_skew_zscore_zscore_63d},
    "vsk_049_skew_zscore_zscore_126d": {"inputs": ['close'], "func": vsk_049_skew_zscore_zscore_126d},
    "vsk_050_skew_zscore_zscore_252d": {"inputs": ['close'], "func": vsk_050_skew_zscore_zscore_252d},
    "vsk_051_ret_skew_rank_5d": {"inputs": ['close'], "func": vsk_051_ret_skew_rank_5d},
    "vsk_052_ret_skew_rank_21d": {"inputs": ['close'], "func": vsk_052_ret_skew_rank_21d},
    "vsk_053_ret_skew_rank_63d": {"inputs": ['close'], "func": vsk_053_ret_skew_rank_63d},
    "vsk_054_ret_skew_rank_126d": {"inputs": ['close'], "func": vsk_054_ret_skew_rank_126d},
    "vsk_055_ret_skew_rank_252d": {"inputs": ['close'], "func": vsk_055_ret_skew_rank_252d},
    "vsk_056_dd_skew_rank_5d": {"inputs": ['close'], "func": vsk_056_dd_skew_rank_5d},
    "vsk_057_dd_skew_rank_21d": {"inputs": ['close'], "func": vsk_057_dd_skew_rank_21d},
    "vsk_058_dd_skew_rank_63d": {"inputs": ['close'], "func": vsk_058_dd_skew_rank_63d},
    "vsk_059_dd_skew_rank_126d": {"inputs": ['close'], "func": vsk_059_dd_skew_rank_126d},
    "vsk_060_dd_skew_rank_252d": {"inputs": ['close'], "func": vsk_060_dd_skew_rank_252d},
    "vsk_061_range_skew_rank_5d": {"inputs": ['close', 'high', 'low'], "func": vsk_061_range_skew_rank_5d},
    "vsk_062_range_skew_rank_21d": {"inputs": ['close', 'high', 'low'], "func": vsk_062_range_skew_rank_21d},
    "vsk_063_range_skew_rank_63d": {"inputs": ['close', 'high', 'low'], "func": vsk_063_range_skew_rank_63d},
    "vsk_064_range_skew_rank_126d": {"inputs": ['close', 'high', 'low'], "func": vsk_064_range_skew_rank_126d},
    "vsk_065_range_skew_rank_252d": {"inputs": ['close', 'high', 'low'], "func": vsk_065_range_skew_rank_252d},
    "vsk_066_skew_mom_rank_5d": {"inputs": ['close'], "func": vsk_066_skew_mom_rank_5d},
    "vsk_067_skew_mom_rank_21d": {"inputs": ['close'], "func": vsk_067_skew_mom_rank_21d},
    "vsk_068_skew_mom_rank_63d": {"inputs": ['close'], "func": vsk_068_skew_mom_rank_63d},
    "vsk_069_skew_mom_rank_126d": {"inputs": ['close'], "func": vsk_069_skew_mom_rank_126d},
    "vsk_070_skew_mom_rank_252d": {"inputs": ['close'], "func": vsk_070_skew_mom_rank_252d},
    "vsk_071_skew_zscore_rank_5d": {"inputs": ['close'], "func": vsk_071_skew_zscore_rank_5d},
    "vsk_072_skew_zscore_rank_21d": {"inputs": ['close'], "func": vsk_072_skew_zscore_rank_21d},
    "vsk_073_skew_zscore_rank_63d": {"inputs": ['close'], "func": vsk_073_skew_zscore_rank_63d},
    "vsk_074_skew_zscore_rank_126d": {"inputs": ['close'], "func": vsk_074_skew_zscore_rank_126d},
    "vsk_075_skew_zscore_rank_252d": {"inputs": ['close'], "func": vsk_075_skew_zscore_rank_252d},
}
