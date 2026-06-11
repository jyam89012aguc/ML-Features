"""
Domain 25: realized_volatility (rvl_)
Asset Class: US Equities
Target Context: Realized volatility and price variance metrics.
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
def rvl_001_real_vol_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5) * np.sqrt(252)

def rvl_002_real_vol_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21) * np.sqrt(252)

def rvl_003_real_vol_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63) * np.sqrt(252)

def rvl_004_real_vol_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126) * np.sqrt(252)

def rvl_005_real_vol_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252) * np.sqrt(252)

def rvl_006_vol_range_5d(close, high, low) -> pd.Series:
    return _rolling_std(_safe_div(high - low, close), 5)

def rvl_007_vol_range_21d(close, high, low) -> pd.Series:
    return _rolling_std(_safe_div(high - low, close), 21)

def rvl_008_vol_range_63d(close, high, low) -> pd.Series:
    return _rolling_std(_safe_div(high - low, close), 63)

def rvl_009_vol_range_126d(close, high, low) -> pd.Series:
    return _rolling_std(_safe_div(high - low, close), 126)

def rvl_010_vol_range_252d(close, high, low) -> pd.Series:
    return _rolling_std(_safe_div(high - low, close), 252)

def rvl_011_vol_sd_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5)

def rvl_012_vol_sd_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21)

def rvl_013_vol_sd_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63)

def rvl_014_vol_sd_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126)

def rvl_015_vol_sd_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252)

def rvl_016_vol_var_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5)**2

def rvl_017_vol_var_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21)**2

def rvl_018_vol_var_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63)**2

def rvl_019_vol_var_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126)**2

def rvl_020_vol_var_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252)**2

def rvl_021_vol_log_ret_5d(close) -> pd.Series:
    return _rolling_std(np.log(close/close.shift(1)), 5)

def rvl_022_vol_log_ret_21d(close) -> pd.Series:
    return _rolling_std(np.log(close/close.shift(1)), 21)

def rvl_023_vol_log_ret_63d(close) -> pd.Series:
    return _rolling_std(np.log(close/close.shift(1)), 63)

def rvl_024_vol_log_ret_126d(close) -> pd.Series:
    return _rolling_std(np.log(close/close.shift(1)), 126)

def rvl_025_vol_log_ret_252d(close) -> pd.Series:
    return _rolling_std(np.log(close/close.shift(1)), 252)

def rvl_026_real_vol_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(rvl_001_real_vol_5d(close), 252)

def rvl_027_real_vol_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(rvl_002_real_vol_21d(close), 252)

def rvl_028_real_vol_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(rvl_003_real_vol_63d(close), 252)

def rvl_029_real_vol_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(rvl_004_real_vol_126d(close), 252)

def rvl_030_real_vol_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(rvl_005_real_vol_252d(close), 252)

def rvl_031_vol_range_zscore_5d(close, high, low) -> pd.Series:
    return _zscore_rolling(rvl_006_vol_range_5d(close, high, low), 252)

def rvl_032_vol_range_zscore_21d(close, high, low) -> pd.Series:
    return _zscore_rolling(rvl_007_vol_range_21d(close, high, low), 252)

def rvl_033_vol_range_zscore_63d(close, high, low) -> pd.Series:
    return _zscore_rolling(rvl_008_vol_range_63d(close, high, low), 252)

def rvl_034_vol_range_zscore_126d(close, high, low) -> pd.Series:
    return _zscore_rolling(rvl_009_vol_range_126d(close, high, low), 252)

def rvl_035_vol_range_zscore_252d(close, high, low) -> pd.Series:
    return _zscore_rolling(rvl_010_vol_range_252d(close, high, low), 252)

def rvl_036_vol_sd_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(rvl_011_vol_sd_5d(close), 252)

def rvl_037_vol_sd_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(rvl_012_vol_sd_21d(close), 252)

def rvl_038_vol_sd_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(rvl_013_vol_sd_63d(close), 252)

def rvl_039_vol_sd_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(rvl_014_vol_sd_126d(close), 252)

def rvl_040_vol_sd_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(rvl_015_vol_sd_252d(close), 252)

def rvl_041_vol_var_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(rvl_016_vol_var_5d(close), 252)

def rvl_042_vol_var_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(rvl_017_vol_var_21d(close), 252)

def rvl_043_vol_var_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(rvl_018_vol_var_63d(close), 252)

def rvl_044_vol_var_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(rvl_019_vol_var_126d(close), 252)

def rvl_045_vol_var_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(rvl_020_vol_var_252d(close), 252)

def rvl_046_vol_log_ret_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(rvl_021_vol_log_ret_5d(close), 252)

def rvl_047_vol_log_ret_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(rvl_022_vol_log_ret_21d(close), 252)

def rvl_048_vol_log_ret_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(rvl_023_vol_log_ret_63d(close), 252)

def rvl_049_vol_log_ret_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(rvl_024_vol_log_ret_126d(close), 252)

def rvl_050_vol_log_ret_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(rvl_025_vol_log_ret_252d(close), 252)

def rvl_051_real_vol_rank_5d(close) -> pd.Series:
    return rvl_001_real_vol_5d(close).rolling(252).rank(pct=True)

def rvl_052_real_vol_rank_21d(close) -> pd.Series:
    return rvl_002_real_vol_21d(close).rolling(252).rank(pct=True)

def rvl_053_real_vol_rank_63d(close) -> pd.Series:
    return rvl_003_real_vol_63d(close).rolling(252).rank(pct=True)

def rvl_054_real_vol_rank_126d(close) -> pd.Series:
    return rvl_004_real_vol_126d(close).rolling(252).rank(pct=True)

def rvl_055_real_vol_rank_252d(close) -> pd.Series:
    return rvl_005_real_vol_252d(close).rolling(252).rank(pct=True)

def rvl_056_vol_range_rank_5d(close, high, low) -> pd.Series:
    return rvl_006_vol_range_5d(close, high, low).rolling(252).rank(pct=True)

def rvl_057_vol_range_rank_21d(close, high, low) -> pd.Series:
    return rvl_007_vol_range_21d(close, high, low).rolling(252).rank(pct=True)

def rvl_058_vol_range_rank_63d(close, high, low) -> pd.Series:
    return rvl_008_vol_range_63d(close, high, low).rolling(252).rank(pct=True)

def rvl_059_vol_range_rank_126d(close, high, low) -> pd.Series:
    return rvl_009_vol_range_126d(close, high, low).rolling(252).rank(pct=True)

def rvl_060_vol_range_rank_252d(close, high, low) -> pd.Series:
    return rvl_010_vol_range_252d(close, high, low).rolling(252).rank(pct=True)

def rvl_061_vol_sd_rank_5d(close) -> pd.Series:
    return rvl_011_vol_sd_5d(close).rolling(252).rank(pct=True)

def rvl_062_vol_sd_rank_21d(close) -> pd.Series:
    return rvl_012_vol_sd_21d(close).rolling(252).rank(pct=True)

def rvl_063_vol_sd_rank_63d(close) -> pd.Series:
    return rvl_013_vol_sd_63d(close).rolling(252).rank(pct=True)

def rvl_064_vol_sd_rank_126d(close) -> pd.Series:
    return rvl_014_vol_sd_126d(close).rolling(252).rank(pct=True)

def rvl_065_vol_sd_rank_252d(close) -> pd.Series:
    return rvl_015_vol_sd_252d(close).rolling(252).rank(pct=True)

def rvl_066_vol_var_rank_5d(close) -> pd.Series:
    return rvl_016_vol_var_5d(close).rolling(252).rank(pct=True)

def rvl_067_vol_var_rank_21d(close) -> pd.Series:
    return rvl_017_vol_var_21d(close).rolling(252).rank(pct=True)

def rvl_068_vol_var_rank_63d(close) -> pd.Series:
    return rvl_018_vol_var_63d(close).rolling(252).rank(pct=True)

def rvl_069_vol_var_rank_126d(close) -> pd.Series:
    return rvl_019_vol_var_126d(close).rolling(252).rank(pct=True)

def rvl_070_vol_var_rank_252d(close) -> pd.Series:
    return rvl_020_vol_var_252d(close).rolling(252).rank(pct=True)

def rvl_071_vol_log_ret_rank_5d(close) -> pd.Series:
    return rvl_021_vol_log_ret_5d(close).rolling(252).rank(pct=True)

def rvl_072_vol_log_ret_rank_21d(close) -> pd.Series:
    return rvl_022_vol_log_ret_21d(close).rolling(252).rank(pct=True)

def rvl_073_vol_log_ret_rank_63d(close) -> pd.Series:
    return rvl_023_vol_log_ret_63d(close).rolling(252).rank(pct=True)

def rvl_074_vol_log_ret_rank_126d(close) -> pd.Series:
    return rvl_024_vol_log_ret_126d(close).rolling(252).rank(pct=True)

def rvl_075_vol_log_ret_rank_252d(close) -> pd.Series:
    return rvl_025_vol_log_ret_252d(close).rolling(252).rank(pct=True)


# --- Registry ---
V25_REGISTRY = {
    "rvl_001_real_vol_5d": {"inputs": ['close'], "func": rvl_001_real_vol_5d},
    "rvl_002_real_vol_21d": {"inputs": ['close'], "func": rvl_002_real_vol_21d},
    "rvl_003_real_vol_63d": {"inputs": ['close'], "func": rvl_003_real_vol_63d},
    "rvl_004_real_vol_126d": {"inputs": ['close'], "func": rvl_004_real_vol_126d},
    "rvl_005_real_vol_252d": {"inputs": ['close'], "func": rvl_005_real_vol_252d},
    "rvl_006_vol_range_5d": {"inputs": ['close', 'high', 'low'], "func": rvl_006_vol_range_5d},
    "rvl_007_vol_range_21d": {"inputs": ['close', 'high', 'low'], "func": rvl_007_vol_range_21d},
    "rvl_008_vol_range_63d": {"inputs": ['close', 'high', 'low'], "func": rvl_008_vol_range_63d},
    "rvl_009_vol_range_126d": {"inputs": ['close', 'high', 'low'], "func": rvl_009_vol_range_126d},
    "rvl_010_vol_range_252d": {"inputs": ['close', 'high', 'low'], "func": rvl_010_vol_range_252d},
    "rvl_011_vol_sd_5d": {"inputs": ['close'], "func": rvl_011_vol_sd_5d},
    "rvl_012_vol_sd_21d": {"inputs": ['close'], "func": rvl_012_vol_sd_21d},
    "rvl_013_vol_sd_63d": {"inputs": ['close'], "func": rvl_013_vol_sd_63d},
    "rvl_014_vol_sd_126d": {"inputs": ['close'], "func": rvl_014_vol_sd_126d},
    "rvl_015_vol_sd_252d": {"inputs": ['close'], "func": rvl_015_vol_sd_252d},
    "rvl_016_vol_var_5d": {"inputs": ['close'], "func": rvl_016_vol_var_5d},
    "rvl_017_vol_var_21d": {"inputs": ['close'], "func": rvl_017_vol_var_21d},
    "rvl_018_vol_var_63d": {"inputs": ['close'], "func": rvl_018_vol_var_63d},
    "rvl_019_vol_var_126d": {"inputs": ['close'], "func": rvl_019_vol_var_126d},
    "rvl_020_vol_var_252d": {"inputs": ['close'], "func": rvl_020_vol_var_252d},
    "rvl_021_vol_log_ret_5d": {"inputs": ['close'], "func": rvl_021_vol_log_ret_5d},
    "rvl_022_vol_log_ret_21d": {"inputs": ['close'], "func": rvl_022_vol_log_ret_21d},
    "rvl_023_vol_log_ret_63d": {"inputs": ['close'], "func": rvl_023_vol_log_ret_63d},
    "rvl_024_vol_log_ret_126d": {"inputs": ['close'], "func": rvl_024_vol_log_ret_126d},
    "rvl_025_vol_log_ret_252d": {"inputs": ['close'], "func": rvl_025_vol_log_ret_252d},
    "rvl_026_real_vol_zscore_5d": {"inputs": ['close'], "func": rvl_026_real_vol_zscore_5d},
    "rvl_027_real_vol_zscore_21d": {"inputs": ['close'], "func": rvl_027_real_vol_zscore_21d},
    "rvl_028_real_vol_zscore_63d": {"inputs": ['close'], "func": rvl_028_real_vol_zscore_63d},
    "rvl_029_real_vol_zscore_126d": {"inputs": ['close'], "func": rvl_029_real_vol_zscore_126d},
    "rvl_030_real_vol_zscore_252d": {"inputs": ['close'], "func": rvl_030_real_vol_zscore_252d},
    "rvl_031_vol_range_zscore_5d": {"inputs": ['close', 'high', 'low'], "func": rvl_031_vol_range_zscore_5d},
    "rvl_032_vol_range_zscore_21d": {"inputs": ['close', 'high', 'low'], "func": rvl_032_vol_range_zscore_21d},
    "rvl_033_vol_range_zscore_63d": {"inputs": ['close', 'high', 'low'], "func": rvl_033_vol_range_zscore_63d},
    "rvl_034_vol_range_zscore_126d": {"inputs": ['close', 'high', 'low'], "func": rvl_034_vol_range_zscore_126d},
    "rvl_035_vol_range_zscore_252d": {"inputs": ['close', 'high', 'low'], "func": rvl_035_vol_range_zscore_252d},
    "rvl_036_vol_sd_zscore_5d": {"inputs": ['close'], "func": rvl_036_vol_sd_zscore_5d},
    "rvl_037_vol_sd_zscore_21d": {"inputs": ['close'], "func": rvl_037_vol_sd_zscore_21d},
    "rvl_038_vol_sd_zscore_63d": {"inputs": ['close'], "func": rvl_038_vol_sd_zscore_63d},
    "rvl_039_vol_sd_zscore_126d": {"inputs": ['close'], "func": rvl_039_vol_sd_zscore_126d},
    "rvl_040_vol_sd_zscore_252d": {"inputs": ['close'], "func": rvl_040_vol_sd_zscore_252d},
    "rvl_041_vol_var_zscore_5d": {"inputs": ['close'], "func": rvl_041_vol_var_zscore_5d},
    "rvl_042_vol_var_zscore_21d": {"inputs": ['close'], "func": rvl_042_vol_var_zscore_21d},
    "rvl_043_vol_var_zscore_63d": {"inputs": ['close'], "func": rvl_043_vol_var_zscore_63d},
    "rvl_044_vol_var_zscore_126d": {"inputs": ['close'], "func": rvl_044_vol_var_zscore_126d},
    "rvl_045_vol_var_zscore_252d": {"inputs": ['close'], "func": rvl_045_vol_var_zscore_252d},
    "rvl_046_vol_log_ret_zscore_5d": {"inputs": ['close'], "func": rvl_046_vol_log_ret_zscore_5d},
    "rvl_047_vol_log_ret_zscore_21d": {"inputs": ['close'], "func": rvl_047_vol_log_ret_zscore_21d},
    "rvl_048_vol_log_ret_zscore_63d": {"inputs": ['close'], "func": rvl_048_vol_log_ret_zscore_63d},
    "rvl_049_vol_log_ret_zscore_126d": {"inputs": ['close'], "func": rvl_049_vol_log_ret_zscore_126d},
    "rvl_050_vol_log_ret_zscore_252d": {"inputs": ['close'], "func": rvl_050_vol_log_ret_zscore_252d},
    "rvl_051_real_vol_rank_5d": {"inputs": ['close'], "func": rvl_051_real_vol_rank_5d},
    "rvl_052_real_vol_rank_21d": {"inputs": ['close'], "func": rvl_052_real_vol_rank_21d},
    "rvl_053_real_vol_rank_63d": {"inputs": ['close'], "func": rvl_053_real_vol_rank_63d},
    "rvl_054_real_vol_rank_126d": {"inputs": ['close'], "func": rvl_054_real_vol_rank_126d},
    "rvl_055_real_vol_rank_252d": {"inputs": ['close'], "func": rvl_055_real_vol_rank_252d},
    "rvl_056_vol_range_rank_5d": {"inputs": ['close', 'high', 'low'], "func": rvl_056_vol_range_rank_5d},
    "rvl_057_vol_range_rank_21d": {"inputs": ['close', 'high', 'low'], "func": rvl_057_vol_range_rank_21d},
    "rvl_058_vol_range_rank_63d": {"inputs": ['close', 'high', 'low'], "func": rvl_058_vol_range_rank_63d},
    "rvl_059_vol_range_rank_126d": {"inputs": ['close', 'high', 'low'], "func": rvl_059_vol_range_rank_126d},
    "rvl_060_vol_range_rank_252d": {"inputs": ['close', 'high', 'low'], "func": rvl_060_vol_range_rank_252d},
    "rvl_061_vol_sd_rank_5d": {"inputs": ['close'], "func": rvl_061_vol_sd_rank_5d},
    "rvl_062_vol_sd_rank_21d": {"inputs": ['close'], "func": rvl_062_vol_sd_rank_21d},
    "rvl_063_vol_sd_rank_63d": {"inputs": ['close'], "func": rvl_063_vol_sd_rank_63d},
    "rvl_064_vol_sd_rank_126d": {"inputs": ['close'], "func": rvl_064_vol_sd_rank_126d},
    "rvl_065_vol_sd_rank_252d": {"inputs": ['close'], "func": rvl_065_vol_sd_rank_252d},
    "rvl_066_vol_var_rank_5d": {"inputs": ['close'], "func": rvl_066_vol_var_rank_5d},
    "rvl_067_vol_var_rank_21d": {"inputs": ['close'], "func": rvl_067_vol_var_rank_21d},
    "rvl_068_vol_var_rank_63d": {"inputs": ['close'], "func": rvl_068_vol_var_rank_63d},
    "rvl_069_vol_var_rank_126d": {"inputs": ['close'], "func": rvl_069_vol_var_rank_126d},
    "rvl_070_vol_var_rank_252d": {"inputs": ['close'], "func": rvl_070_vol_var_rank_252d},
    "rvl_071_vol_log_ret_rank_5d": {"inputs": ['close'], "func": rvl_071_vol_log_ret_rank_5d},
    "rvl_072_vol_log_ret_rank_21d": {"inputs": ['close'], "func": rvl_072_vol_log_ret_rank_21d},
    "rvl_073_vol_log_ret_rank_63d": {"inputs": ['close'], "func": rvl_073_vol_log_ret_rank_63d},
    "rvl_074_vol_log_ret_rank_126d": {"inputs": ['close'], "func": rvl_074_vol_log_ret_rank_126d},
    "rvl_075_vol_log_ret_rank_252d": {"inputs": ['close'], "func": rvl_075_vol_log_ret_rank_252d},
}
