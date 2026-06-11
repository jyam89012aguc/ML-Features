"""
Domain 28: volatility_kurtosis (vkt_)
Asset Class: US Equities
Target Context: Fat-tail risk and extreme return frequency.
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
def vkt_001_ret_kurt_5d(close) -> pd.Series:
    return _daily_ret(close).rolling(5).kurt()

def vkt_002_ret_kurt_21d(close) -> pd.Series:
    return _daily_ret(close).rolling(21).kurt()

def vkt_003_ret_kurt_63d(close) -> pd.Series:
    return _daily_ret(close).rolling(63).kurt()

def vkt_004_ret_kurt_126d(close) -> pd.Series:
    return _daily_ret(close).rolling(126).kurt()

def vkt_005_ret_kurt_252d(close) -> pd.Series:
    return _daily_ret(close).rolling(252).kurt()

def vkt_006_dd_kurt_5d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).rolling(5).kurt())(close)

def vkt_007_dd_kurt_21d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).rolling(21).kurt())(close)

def vkt_008_dd_kurt_63d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).rolling(63).kurt())(close)

def vkt_009_dd_kurt_126d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).rolling(126).kurt())(close)

def vkt_010_dd_kurt_252d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).rolling(252).kurt())(close)

def vkt_011_range_kurt_5d(close, high, low) -> pd.Series:
    return _safe_div(high - low, close).rolling(5).kurt()

def vkt_012_range_kurt_21d(close, high, low) -> pd.Series:
    return _safe_div(high - low, close).rolling(21).kurt()

def vkt_013_range_kurt_63d(close, high, low) -> pd.Series:
    return _safe_div(high - low, close).rolling(63).kurt()

def vkt_014_range_kurt_126d(close, high, low) -> pd.Series:
    return _safe_div(high - low, close).rolling(126).kurt()

def vkt_015_range_kurt_252d(close, high, low) -> pd.Series:
    return _safe_div(high - low, close).rolling(252).kurt()

def vkt_016_kurt_mom_5d(close) -> pd.Series:
    return _daily_ret(close).rolling(5).kurt().diff(5)

def vkt_017_kurt_mom_21d(close) -> pd.Series:
    return _daily_ret(close).rolling(21).kurt().diff(21)

def vkt_018_kurt_mom_63d(close) -> pd.Series:
    return _daily_ret(close).rolling(63).kurt().diff(63)

def vkt_019_kurt_mom_126d(close) -> pd.Series:
    return _daily_ret(close).rolling(126).kurt().diff(126)

def vkt_020_kurt_mom_252d(close) -> pd.Series:
    return _daily_ret(close).rolling(252).kurt().diff(252)

def vkt_021_kurt_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(_daily_ret(close).rolling(5).kurt(), 252)

def vkt_022_kurt_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(_daily_ret(close).rolling(21).kurt(), 252)

def vkt_023_kurt_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(_daily_ret(close).rolling(63).kurt(), 252)

def vkt_024_kurt_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(_daily_ret(close).rolling(126).kurt(), 252)

def vkt_025_kurt_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(_daily_ret(close).rolling(252).kurt(), 252)

def vkt_026_ret_kurt_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vkt_001_ret_kurt_5d(close), 252)

def vkt_027_ret_kurt_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vkt_002_ret_kurt_21d(close), 252)

def vkt_028_ret_kurt_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vkt_003_ret_kurt_63d(close), 252)

def vkt_029_ret_kurt_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vkt_004_ret_kurt_126d(close), 252)

def vkt_030_ret_kurt_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vkt_005_ret_kurt_252d(close), 252)

def vkt_031_dd_kurt_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vkt_006_dd_kurt_5d(close), 252)

def vkt_032_dd_kurt_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vkt_007_dd_kurt_21d(close), 252)

def vkt_033_dd_kurt_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vkt_008_dd_kurt_63d(close), 252)

def vkt_034_dd_kurt_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vkt_009_dd_kurt_126d(close), 252)

def vkt_035_dd_kurt_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vkt_010_dd_kurt_252d(close), 252)

def vkt_036_range_kurt_zscore_5d(close, high, low) -> pd.Series:
    return _zscore_rolling(vkt_011_range_kurt_5d(close, high, low), 252)

def vkt_037_range_kurt_zscore_21d(close, high, low) -> pd.Series:
    return _zscore_rolling(vkt_012_range_kurt_21d(close, high, low), 252)

def vkt_038_range_kurt_zscore_63d(close, high, low) -> pd.Series:
    return _zscore_rolling(vkt_013_range_kurt_63d(close, high, low), 252)

def vkt_039_range_kurt_zscore_126d(close, high, low) -> pd.Series:
    return _zscore_rolling(vkt_014_range_kurt_126d(close, high, low), 252)

def vkt_040_range_kurt_zscore_252d(close, high, low) -> pd.Series:
    return _zscore_rolling(vkt_015_range_kurt_252d(close, high, low), 252)

def vkt_041_kurt_mom_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vkt_016_kurt_mom_5d(close), 252)

def vkt_042_kurt_mom_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vkt_017_kurt_mom_21d(close), 252)

def vkt_043_kurt_mom_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vkt_018_kurt_mom_63d(close), 252)

def vkt_044_kurt_mom_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vkt_019_kurt_mom_126d(close), 252)

def vkt_045_kurt_mom_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vkt_020_kurt_mom_252d(close), 252)

def vkt_046_kurt_zscore_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vkt_021_kurt_zscore_5d(close), 252)

def vkt_047_kurt_zscore_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vkt_022_kurt_zscore_21d(close), 252)

def vkt_048_kurt_zscore_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vkt_023_kurt_zscore_63d(close), 252)

def vkt_049_kurt_zscore_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vkt_024_kurt_zscore_126d(close), 252)

def vkt_050_kurt_zscore_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vkt_025_kurt_zscore_252d(close), 252)

def vkt_051_ret_kurt_rank_5d(close) -> pd.Series:
    return vkt_001_ret_kurt_5d(close).rolling(252).rank(pct=True)

def vkt_052_ret_kurt_rank_21d(close) -> pd.Series:
    return vkt_002_ret_kurt_21d(close).rolling(252).rank(pct=True)

def vkt_053_ret_kurt_rank_63d(close) -> pd.Series:
    return vkt_003_ret_kurt_63d(close).rolling(252).rank(pct=True)

def vkt_054_ret_kurt_rank_126d(close) -> pd.Series:
    return vkt_004_ret_kurt_126d(close).rolling(252).rank(pct=True)

def vkt_055_ret_kurt_rank_252d(close) -> pd.Series:
    return vkt_005_ret_kurt_252d(close).rolling(252).rank(pct=True)

def vkt_056_dd_kurt_rank_5d(close) -> pd.Series:
    return vkt_006_dd_kurt_5d(close).rolling(252).rank(pct=True)

def vkt_057_dd_kurt_rank_21d(close) -> pd.Series:
    return vkt_007_dd_kurt_21d(close).rolling(252).rank(pct=True)

def vkt_058_dd_kurt_rank_63d(close) -> pd.Series:
    return vkt_008_dd_kurt_63d(close).rolling(252).rank(pct=True)

def vkt_059_dd_kurt_rank_126d(close) -> pd.Series:
    return vkt_009_dd_kurt_126d(close).rolling(252).rank(pct=True)

def vkt_060_dd_kurt_rank_252d(close) -> pd.Series:
    return vkt_010_dd_kurt_252d(close).rolling(252).rank(pct=True)

def vkt_061_range_kurt_rank_5d(close, high, low) -> pd.Series:
    return vkt_011_range_kurt_5d(close, high, low).rolling(252).rank(pct=True)

def vkt_062_range_kurt_rank_21d(close, high, low) -> pd.Series:
    return vkt_012_range_kurt_21d(close, high, low).rolling(252).rank(pct=True)

def vkt_063_range_kurt_rank_63d(close, high, low) -> pd.Series:
    return vkt_013_range_kurt_63d(close, high, low).rolling(252).rank(pct=True)

def vkt_064_range_kurt_rank_126d(close, high, low) -> pd.Series:
    return vkt_014_range_kurt_126d(close, high, low).rolling(252).rank(pct=True)

def vkt_065_range_kurt_rank_252d(close, high, low) -> pd.Series:
    return vkt_015_range_kurt_252d(close, high, low).rolling(252).rank(pct=True)

def vkt_066_kurt_mom_rank_5d(close) -> pd.Series:
    return vkt_016_kurt_mom_5d(close).rolling(252).rank(pct=True)

def vkt_067_kurt_mom_rank_21d(close) -> pd.Series:
    return vkt_017_kurt_mom_21d(close).rolling(252).rank(pct=True)

def vkt_068_kurt_mom_rank_63d(close) -> pd.Series:
    return vkt_018_kurt_mom_63d(close).rolling(252).rank(pct=True)

def vkt_069_kurt_mom_rank_126d(close) -> pd.Series:
    return vkt_019_kurt_mom_126d(close).rolling(252).rank(pct=True)

def vkt_070_kurt_mom_rank_252d(close) -> pd.Series:
    return vkt_020_kurt_mom_252d(close).rolling(252).rank(pct=True)

def vkt_071_kurt_zscore_rank_5d(close) -> pd.Series:
    return vkt_021_kurt_zscore_5d(close).rolling(252).rank(pct=True)

def vkt_072_kurt_zscore_rank_21d(close) -> pd.Series:
    return vkt_022_kurt_zscore_21d(close).rolling(252).rank(pct=True)

def vkt_073_kurt_zscore_rank_63d(close) -> pd.Series:
    return vkt_023_kurt_zscore_63d(close).rolling(252).rank(pct=True)

def vkt_074_kurt_zscore_rank_126d(close) -> pd.Series:
    return vkt_024_kurt_zscore_126d(close).rolling(252).rank(pct=True)

def vkt_075_kurt_zscore_rank_252d(close) -> pd.Series:
    return vkt_025_kurt_zscore_252d(close).rolling(252).rank(pct=True)


# --- Registry ---
V28_REGISTRY = {
    "vkt_001_ret_kurt_5d": {"inputs": ['close'], "func": vkt_001_ret_kurt_5d},
    "vkt_002_ret_kurt_21d": {"inputs": ['close'], "func": vkt_002_ret_kurt_21d},
    "vkt_003_ret_kurt_63d": {"inputs": ['close'], "func": vkt_003_ret_kurt_63d},
    "vkt_004_ret_kurt_126d": {"inputs": ['close'], "func": vkt_004_ret_kurt_126d},
    "vkt_005_ret_kurt_252d": {"inputs": ['close'], "func": vkt_005_ret_kurt_252d},
    "vkt_006_dd_kurt_5d": {"inputs": ['close'], "func": vkt_006_dd_kurt_5d},
    "vkt_007_dd_kurt_21d": {"inputs": ['close'], "func": vkt_007_dd_kurt_21d},
    "vkt_008_dd_kurt_63d": {"inputs": ['close'], "func": vkt_008_dd_kurt_63d},
    "vkt_009_dd_kurt_126d": {"inputs": ['close'], "func": vkt_009_dd_kurt_126d},
    "vkt_010_dd_kurt_252d": {"inputs": ['close'], "func": vkt_010_dd_kurt_252d},
    "vkt_011_range_kurt_5d": {"inputs": ['close', 'high', 'low'], "func": vkt_011_range_kurt_5d},
    "vkt_012_range_kurt_21d": {"inputs": ['close', 'high', 'low'], "func": vkt_012_range_kurt_21d},
    "vkt_013_range_kurt_63d": {"inputs": ['close', 'high', 'low'], "func": vkt_013_range_kurt_63d},
    "vkt_014_range_kurt_126d": {"inputs": ['close', 'high', 'low'], "func": vkt_014_range_kurt_126d},
    "vkt_015_range_kurt_252d": {"inputs": ['close', 'high', 'low'], "func": vkt_015_range_kurt_252d},
    "vkt_016_kurt_mom_5d": {"inputs": ['close'], "func": vkt_016_kurt_mom_5d},
    "vkt_017_kurt_mom_21d": {"inputs": ['close'], "func": vkt_017_kurt_mom_21d},
    "vkt_018_kurt_mom_63d": {"inputs": ['close'], "func": vkt_018_kurt_mom_63d},
    "vkt_019_kurt_mom_126d": {"inputs": ['close'], "func": vkt_019_kurt_mom_126d},
    "vkt_020_kurt_mom_252d": {"inputs": ['close'], "func": vkt_020_kurt_mom_252d},
    "vkt_021_kurt_zscore_5d": {"inputs": ['close'], "func": vkt_021_kurt_zscore_5d},
    "vkt_022_kurt_zscore_21d": {"inputs": ['close'], "func": vkt_022_kurt_zscore_21d},
    "vkt_023_kurt_zscore_63d": {"inputs": ['close'], "func": vkt_023_kurt_zscore_63d},
    "vkt_024_kurt_zscore_126d": {"inputs": ['close'], "func": vkt_024_kurt_zscore_126d},
    "vkt_025_kurt_zscore_252d": {"inputs": ['close'], "func": vkt_025_kurt_zscore_252d},
    "vkt_026_ret_kurt_zscore_5d": {"inputs": ['close'], "func": vkt_026_ret_kurt_zscore_5d},
    "vkt_027_ret_kurt_zscore_21d": {"inputs": ['close'], "func": vkt_027_ret_kurt_zscore_21d},
    "vkt_028_ret_kurt_zscore_63d": {"inputs": ['close'], "func": vkt_028_ret_kurt_zscore_63d},
    "vkt_029_ret_kurt_zscore_126d": {"inputs": ['close'], "func": vkt_029_ret_kurt_zscore_126d},
    "vkt_030_ret_kurt_zscore_252d": {"inputs": ['close'], "func": vkt_030_ret_kurt_zscore_252d},
    "vkt_031_dd_kurt_zscore_5d": {"inputs": ['close'], "func": vkt_031_dd_kurt_zscore_5d},
    "vkt_032_dd_kurt_zscore_21d": {"inputs": ['close'], "func": vkt_032_dd_kurt_zscore_21d},
    "vkt_033_dd_kurt_zscore_63d": {"inputs": ['close'], "func": vkt_033_dd_kurt_zscore_63d},
    "vkt_034_dd_kurt_zscore_126d": {"inputs": ['close'], "func": vkt_034_dd_kurt_zscore_126d},
    "vkt_035_dd_kurt_zscore_252d": {"inputs": ['close'], "func": vkt_035_dd_kurt_zscore_252d},
    "vkt_036_range_kurt_zscore_5d": {"inputs": ['close', 'high', 'low'], "func": vkt_036_range_kurt_zscore_5d},
    "vkt_037_range_kurt_zscore_21d": {"inputs": ['close', 'high', 'low'], "func": vkt_037_range_kurt_zscore_21d},
    "vkt_038_range_kurt_zscore_63d": {"inputs": ['close', 'high', 'low'], "func": vkt_038_range_kurt_zscore_63d},
    "vkt_039_range_kurt_zscore_126d": {"inputs": ['close', 'high', 'low'], "func": vkt_039_range_kurt_zscore_126d},
    "vkt_040_range_kurt_zscore_252d": {"inputs": ['close', 'high', 'low'], "func": vkt_040_range_kurt_zscore_252d},
    "vkt_041_kurt_mom_zscore_5d": {"inputs": ['close'], "func": vkt_041_kurt_mom_zscore_5d},
    "vkt_042_kurt_mom_zscore_21d": {"inputs": ['close'], "func": vkt_042_kurt_mom_zscore_21d},
    "vkt_043_kurt_mom_zscore_63d": {"inputs": ['close'], "func": vkt_043_kurt_mom_zscore_63d},
    "vkt_044_kurt_mom_zscore_126d": {"inputs": ['close'], "func": vkt_044_kurt_mom_zscore_126d},
    "vkt_045_kurt_mom_zscore_252d": {"inputs": ['close'], "func": vkt_045_kurt_mom_zscore_252d},
    "vkt_046_kurt_zscore_zscore_5d": {"inputs": ['close'], "func": vkt_046_kurt_zscore_zscore_5d},
    "vkt_047_kurt_zscore_zscore_21d": {"inputs": ['close'], "func": vkt_047_kurt_zscore_zscore_21d},
    "vkt_048_kurt_zscore_zscore_63d": {"inputs": ['close'], "func": vkt_048_kurt_zscore_zscore_63d},
    "vkt_049_kurt_zscore_zscore_126d": {"inputs": ['close'], "func": vkt_049_kurt_zscore_zscore_126d},
    "vkt_050_kurt_zscore_zscore_252d": {"inputs": ['close'], "func": vkt_050_kurt_zscore_zscore_252d},
    "vkt_051_ret_kurt_rank_5d": {"inputs": ['close'], "func": vkt_051_ret_kurt_rank_5d},
    "vkt_052_ret_kurt_rank_21d": {"inputs": ['close'], "func": vkt_052_ret_kurt_rank_21d},
    "vkt_053_ret_kurt_rank_63d": {"inputs": ['close'], "func": vkt_053_ret_kurt_rank_63d},
    "vkt_054_ret_kurt_rank_126d": {"inputs": ['close'], "func": vkt_054_ret_kurt_rank_126d},
    "vkt_055_ret_kurt_rank_252d": {"inputs": ['close'], "func": vkt_055_ret_kurt_rank_252d},
    "vkt_056_dd_kurt_rank_5d": {"inputs": ['close'], "func": vkt_056_dd_kurt_rank_5d},
    "vkt_057_dd_kurt_rank_21d": {"inputs": ['close'], "func": vkt_057_dd_kurt_rank_21d},
    "vkt_058_dd_kurt_rank_63d": {"inputs": ['close'], "func": vkt_058_dd_kurt_rank_63d},
    "vkt_059_dd_kurt_rank_126d": {"inputs": ['close'], "func": vkt_059_dd_kurt_rank_126d},
    "vkt_060_dd_kurt_rank_252d": {"inputs": ['close'], "func": vkt_060_dd_kurt_rank_252d},
    "vkt_061_range_kurt_rank_5d": {"inputs": ['close', 'high', 'low'], "func": vkt_061_range_kurt_rank_5d},
    "vkt_062_range_kurt_rank_21d": {"inputs": ['close', 'high', 'low'], "func": vkt_062_range_kurt_rank_21d},
    "vkt_063_range_kurt_rank_63d": {"inputs": ['close', 'high', 'low'], "func": vkt_063_range_kurt_rank_63d},
    "vkt_064_range_kurt_rank_126d": {"inputs": ['close', 'high', 'low'], "func": vkt_064_range_kurt_rank_126d},
    "vkt_065_range_kurt_rank_252d": {"inputs": ['close', 'high', 'low'], "func": vkt_065_range_kurt_rank_252d},
    "vkt_066_kurt_mom_rank_5d": {"inputs": ['close'], "func": vkt_066_kurt_mom_rank_5d},
    "vkt_067_kurt_mom_rank_21d": {"inputs": ['close'], "func": vkt_067_kurt_mom_rank_21d},
    "vkt_068_kurt_mom_rank_63d": {"inputs": ['close'], "func": vkt_068_kurt_mom_rank_63d},
    "vkt_069_kurt_mom_rank_126d": {"inputs": ['close'], "func": vkt_069_kurt_mom_rank_126d},
    "vkt_070_kurt_mom_rank_252d": {"inputs": ['close'], "func": vkt_070_kurt_mom_rank_252d},
    "vkt_071_kurt_zscore_rank_5d": {"inputs": ['close'], "func": vkt_071_kurt_zscore_rank_5d},
    "vkt_072_kurt_zscore_rank_21d": {"inputs": ['close'], "func": vkt_072_kurt_zscore_rank_21d},
    "vkt_073_kurt_zscore_rank_63d": {"inputs": ['close'], "func": vkt_073_kurt_zscore_rank_63d},
    "vkt_074_kurt_zscore_rank_126d": {"inputs": ['close'], "func": vkt_074_kurt_zscore_rank_126d},
    "vkt_075_kurt_zscore_rank_252d": {"inputs": ['close'], "func": vkt_075_kurt_zscore_rank_252d},
}
