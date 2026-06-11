"""
Domain 12: high_water_distance (hwd_)
Asset Class: US Equities
Target Context: Distance from high water marks and recovery metrics.
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
def hwd_001_hwd_dist_5d(close) -> pd.Series:
    return _safe_div(close.rolling(252, min_periods=1).max() - close, close.rolling(252, min_periods=1).max())

def hwd_002_hwd_dist_21d(close) -> pd.Series:
    return _safe_div(close.rolling(252, min_periods=1).max() - close, close.rolling(252, min_periods=1).max())

def hwd_003_hwd_dist_63d(close) -> pd.Series:
    return _safe_div(close.rolling(252, min_periods=1).max() - close, close.rolling(252, min_periods=1).max())

def hwd_004_hwd_dist_126d(close) -> pd.Series:
    return _safe_div(close.rolling(252, min_periods=1).max() - close, close.rolling(252, min_periods=1).max())

def hwd_005_hwd_dist_252d(close) -> pd.Series:
    return _safe_div(close.rolling(252, min_periods=1).max() - close, close.rolling(252, min_periods=1).max())

def hwd_006_days_since_high_5d(close) -> pd.Series:
    return (lambda x: (x == x.rolling(252, min_periods=1).max()).astype(int).groupby((x == x.rolling(252, min_periods=1).max()).cumsum()).cumcount())(close)

def hwd_007_days_since_high_21d(close) -> pd.Series:
    return (lambda x: (x == x.rolling(252, min_periods=1).max()).astype(int).groupby((x == x.rolling(252, min_periods=1).max()).cumsum()).cumcount())(close)

def hwd_008_days_since_high_63d(close) -> pd.Series:
    return (lambda x: (x == x.rolling(252, min_periods=1).max()).astype(int).groupby((x == x.rolling(252, min_periods=1).max()).cumsum()).cumcount())(close)

def hwd_009_days_since_high_126d(close) -> pd.Series:
    return (lambda x: (x == x.rolling(252, min_periods=1).max()).astype(int).groupby((x == x.rolling(252, min_periods=1).max()).cumsum()).cumcount())(close)

def hwd_010_days_since_high_252d(close) -> pd.Series:
    return (lambda x: (x == x.rolling(252, min_periods=1).max()).astype(int).groupby((x == x.rolling(252, min_periods=1).max()).cumsum()).cumcount())(close)

def hwd_011_dist_to_52w_low_5d(close) -> pd.Series:
    return _safe_div(close - close.rolling(252, min_periods=1).min(), close.rolling(252, min_periods=1).min())

def hwd_012_dist_to_52w_low_21d(close) -> pd.Series:
    return _safe_div(close - close.rolling(252, min_periods=1).min(), close.rolling(252, min_periods=1).min())

def hwd_013_dist_to_52w_low_63d(close) -> pd.Series:
    return _safe_div(close - close.rolling(252, min_periods=1).min(), close.rolling(252, min_periods=1).min())

def hwd_014_dist_to_52w_low_126d(close) -> pd.Series:
    return _safe_div(close - close.rolling(252, min_periods=1).min(), close.rolling(252, min_periods=1).min())

def hwd_015_dist_to_52w_low_252d(close) -> pd.Series:
    return _safe_div(close - close.rolling(252, min_periods=1).min(), close.rolling(252, min_periods=1).min())

def hwd_016_high_intensity_5d(close) -> pd.Series:
    return _rolling_mean((close == close.rolling(252, min_periods=1).max()).astype(float), 5)

def hwd_017_high_intensity_21d(close) -> pd.Series:
    return _rolling_mean((close == close.rolling(252, min_periods=1).max()).astype(float), 21)

def hwd_018_high_intensity_63d(close) -> pd.Series:
    return _rolling_mean((close == close.rolling(252, min_periods=1).max()).astype(float), 63)

def hwd_019_high_intensity_126d(close) -> pd.Series:
    return _rolling_mean((close == close.rolling(252, min_periods=1).max()).astype(float), 126)

def hwd_020_high_intensity_252d(close) -> pd.Series:
    return _rolling_mean((close == close.rolling(252, min_periods=1).max()).astype(float), 252)

def hwd_021_recovery_factor_5d(close) -> pd.Series:
    return _safe_div(close - close.rolling(5).min(), close.rolling(5).max() - close.rolling(5).min())

def hwd_022_recovery_factor_21d(close) -> pd.Series:
    return _safe_div(close - close.rolling(21).min(), close.rolling(21).max() - close.rolling(21).min())

def hwd_023_recovery_factor_63d(close) -> pd.Series:
    return _safe_div(close - close.rolling(63).min(), close.rolling(63).max() - close.rolling(63).min())

def hwd_024_recovery_factor_126d(close) -> pd.Series:
    return _safe_div(close - close.rolling(126).min(), close.rolling(126).max() - close.rolling(126).min())

def hwd_025_recovery_factor_252d(close) -> pd.Series:
    return _safe_div(close - close.rolling(252).min(), close.rolling(252).max() - close.rolling(252).min())

def hwd_026_hwd_dist_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(hwd_001_hwd_dist_5d(close), 252)

def hwd_027_hwd_dist_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(hwd_002_hwd_dist_21d(close), 252)

def hwd_028_hwd_dist_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(hwd_003_hwd_dist_63d(close), 252)

def hwd_029_hwd_dist_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(hwd_004_hwd_dist_126d(close), 252)

def hwd_030_hwd_dist_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(hwd_005_hwd_dist_252d(close), 252)

def hwd_031_days_since_high_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(hwd_006_days_since_high_5d(close), 252)

def hwd_032_days_since_high_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(hwd_007_days_since_high_21d(close), 252)

def hwd_033_days_since_high_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(hwd_008_days_since_high_63d(close), 252)

def hwd_034_days_since_high_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(hwd_009_days_since_high_126d(close), 252)

def hwd_035_days_since_high_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(hwd_010_days_since_high_252d(close), 252)

def hwd_036_dist_to_52w_low_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(hwd_011_dist_to_52w_low_5d(close), 252)

def hwd_037_dist_to_52w_low_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(hwd_012_dist_to_52w_low_21d(close), 252)

def hwd_038_dist_to_52w_low_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(hwd_013_dist_to_52w_low_63d(close), 252)

def hwd_039_dist_to_52w_low_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(hwd_014_dist_to_52w_low_126d(close), 252)

def hwd_040_dist_to_52w_low_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(hwd_015_dist_to_52w_low_252d(close), 252)

def hwd_041_high_intensity_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(hwd_016_high_intensity_5d(close), 252)

def hwd_042_high_intensity_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(hwd_017_high_intensity_21d(close), 252)

def hwd_043_high_intensity_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(hwd_018_high_intensity_63d(close), 252)

def hwd_044_high_intensity_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(hwd_019_high_intensity_126d(close), 252)

def hwd_045_high_intensity_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(hwd_020_high_intensity_252d(close), 252)

def hwd_046_recovery_factor_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(hwd_021_recovery_factor_5d(close), 252)

def hwd_047_recovery_factor_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(hwd_022_recovery_factor_21d(close), 252)

def hwd_048_recovery_factor_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(hwd_023_recovery_factor_63d(close), 252)

def hwd_049_recovery_factor_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(hwd_024_recovery_factor_126d(close), 252)

def hwd_050_recovery_factor_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(hwd_025_recovery_factor_252d(close), 252)

def hwd_051_hwd_dist_rank_5d(close) -> pd.Series:
    return hwd_001_hwd_dist_5d(close).rolling(252).rank(pct=True)

def hwd_052_hwd_dist_rank_21d(close) -> pd.Series:
    return hwd_002_hwd_dist_21d(close).rolling(252).rank(pct=True)

def hwd_053_hwd_dist_rank_63d(close) -> pd.Series:
    return hwd_003_hwd_dist_63d(close).rolling(252).rank(pct=True)

def hwd_054_hwd_dist_rank_126d(close) -> pd.Series:
    return hwd_004_hwd_dist_126d(close).rolling(252).rank(pct=True)

def hwd_055_hwd_dist_rank_252d(close) -> pd.Series:
    return hwd_005_hwd_dist_252d(close).rolling(252).rank(pct=True)

def hwd_056_days_since_high_rank_5d(close) -> pd.Series:
    return hwd_006_days_since_high_5d(close).rolling(252).rank(pct=True)

def hwd_057_days_since_high_rank_21d(close) -> pd.Series:
    return hwd_007_days_since_high_21d(close).rolling(252).rank(pct=True)

def hwd_058_days_since_high_rank_63d(close) -> pd.Series:
    return hwd_008_days_since_high_63d(close).rolling(252).rank(pct=True)

def hwd_059_days_since_high_rank_126d(close) -> pd.Series:
    return hwd_009_days_since_high_126d(close).rolling(252).rank(pct=True)

def hwd_060_days_since_high_rank_252d(close) -> pd.Series:
    return hwd_010_days_since_high_252d(close).rolling(252).rank(pct=True)

def hwd_061_dist_to_52w_low_rank_5d(close) -> pd.Series:
    return hwd_011_dist_to_52w_low_5d(close).rolling(252).rank(pct=True)

def hwd_062_dist_to_52w_low_rank_21d(close) -> pd.Series:
    return hwd_012_dist_to_52w_low_21d(close).rolling(252).rank(pct=True)

def hwd_063_dist_to_52w_low_rank_63d(close) -> pd.Series:
    return hwd_013_dist_to_52w_low_63d(close).rolling(252).rank(pct=True)

def hwd_064_dist_to_52w_low_rank_126d(close) -> pd.Series:
    return hwd_014_dist_to_52w_low_126d(close).rolling(252).rank(pct=True)

def hwd_065_dist_to_52w_low_rank_252d(close) -> pd.Series:
    return hwd_015_dist_to_52w_low_252d(close).rolling(252).rank(pct=True)

def hwd_066_high_intensity_rank_5d(close) -> pd.Series:
    return hwd_016_high_intensity_5d(close).rolling(252).rank(pct=True)

def hwd_067_high_intensity_rank_21d(close) -> pd.Series:
    return hwd_017_high_intensity_21d(close).rolling(252).rank(pct=True)

def hwd_068_high_intensity_rank_63d(close) -> pd.Series:
    return hwd_018_high_intensity_63d(close).rolling(252).rank(pct=True)

def hwd_069_high_intensity_rank_126d(close) -> pd.Series:
    return hwd_019_high_intensity_126d(close).rolling(252).rank(pct=True)

def hwd_070_high_intensity_rank_252d(close) -> pd.Series:
    return hwd_020_high_intensity_252d(close).rolling(252).rank(pct=True)

def hwd_071_recovery_factor_rank_5d(close) -> pd.Series:
    return hwd_021_recovery_factor_5d(close).rolling(252).rank(pct=True)

def hwd_072_recovery_factor_rank_21d(close) -> pd.Series:
    return hwd_022_recovery_factor_21d(close).rolling(252).rank(pct=True)

def hwd_073_recovery_factor_rank_63d(close) -> pd.Series:
    return hwd_023_recovery_factor_63d(close).rolling(252).rank(pct=True)

def hwd_074_recovery_factor_rank_126d(close) -> pd.Series:
    return hwd_024_recovery_factor_126d(close).rolling(252).rank(pct=True)

def hwd_075_recovery_factor_rank_252d(close) -> pd.Series:
    return hwd_025_recovery_factor_252d(close).rolling(252).rank(pct=True)


# --- Registry ---
V12_REGISTRY = {
    "hwd_001_hwd_dist_5d": {"inputs": ['close'], "func": hwd_001_hwd_dist_5d},
    "hwd_002_hwd_dist_21d": {"inputs": ['close'], "func": hwd_002_hwd_dist_21d},
    "hwd_003_hwd_dist_63d": {"inputs": ['close'], "func": hwd_003_hwd_dist_63d},
    "hwd_004_hwd_dist_126d": {"inputs": ['close'], "func": hwd_004_hwd_dist_126d},
    "hwd_005_hwd_dist_252d": {"inputs": ['close'], "func": hwd_005_hwd_dist_252d},
    "hwd_006_days_since_high_5d": {"inputs": ['close'], "func": hwd_006_days_since_high_5d},
    "hwd_007_days_since_high_21d": {"inputs": ['close'], "func": hwd_007_days_since_high_21d},
    "hwd_008_days_since_high_63d": {"inputs": ['close'], "func": hwd_008_days_since_high_63d},
    "hwd_009_days_since_high_126d": {"inputs": ['close'], "func": hwd_009_days_since_high_126d},
    "hwd_010_days_since_high_252d": {"inputs": ['close'], "func": hwd_010_days_since_high_252d},
    "hwd_011_dist_to_52w_low_5d": {"inputs": ['close'], "func": hwd_011_dist_to_52w_low_5d},
    "hwd_012_dist_to_52w_low_21d": {"inputs": ['close'], "func": hwd_012_dist_to_52w_low_21d},
    "hwd_013_dist_to_52w_low_63d": {"inputs": ['close'], "func": hwd_013_dist_to_52w_low_63d},
    "hwd_014_dist_to_52w_low_126d": {"inputs": ['close'], "func": hwd_014_dist_to_52w_low_126d},
    "hwd_015_dist_to_52w_low_252d": {"inputs": ['close'], "func": hwd_015_dist_to_52w_low_252d},
    "hwd_016_high_intensity_5d": {"inputs": ['close'], "func": hwd_016_high_intensity_5d},
    "hwd_017_high_intensity_21d": {"inputs": ['close'], "func": hwd_017_high_intensity_21d},
    "hwd_018_high_intensity_63d": {"inputs": ['close'], "func": hwd_018_high_intensity_63d},
    "hwd_019_high_intensity_126d": {"inputs": ['close'], "func": hwd_019_high_intensity_126d},
    "hwd_020_high_intensity_252d": {"inputs": ['close'], "func": hwd_020_high_intensity_252d},
    "hwd_021_recovery_factor_5d": {"inputs": ['close'], "func": hwd_021_recovery_factor_5d},
    "hwd_022_recovery_factor_21d": {"inputs": ['close'], "func": hwd_022_recovery_factor_21d},
    "hwd_023_recovery_factor_63d": {"inputs": ['close'], "func": hwd_023_recovery_factor_63d},
    "hwd_024_recovery_factor_126d": {"inputs": ['close'], "func": hwd_024_recovery_factor_126d},
    "hwd_025_recovery_factor_252d": {"inputs": ['close'], "func": hwd_025_recovery_factor_252d},
    "hwd_026_hwd_dist_zscore_5d": {"inputs": ['close'], "func": hwd_026_hwd_dist_zscore_5d},
    "hwd_027_hwd_dist_zscore_21d": {"inputs": ['close'], "func": hwd_027_hwd_dist_zscore_21d},
    "hwd_028_hwd_dist_zscore_63d": {"inputs": ['close'], "func": hwd_028_hwd_dist_zscore_63d},
    "hwd_029_hwd_dist_zscore_126d": {"inputs": ['close'], "func": hwd_029_hwd_dist_zscore_126d},
    "hwd_030_hwd_dist_zscore_252d": {"inputs": ['close'], "func": hwd_030_hwd_dist_zscore_252d},
    "hwd_031_days_since_high_zscore_5d": {"inputs": ['close'], "func": hwd_031_days_since_high_zscore_5d},
    "hwd_032_days_since_high_zscore_21d": {"inputs": ['close'], "func": hwd_032_days_since_high_zscore_21d},
    "hwd_033_days_since_high_zscore_63d": {"inputs": ['close'], "func": hwd_033_days_since_high_zscore_63d},
    "hwd_034_days_since_high_zscore_126d": {"inputs": ['close'], "func": hwd_034_days_since_high_zscore_126d},
    "hwd_035_days_since_high_zscore_252d": {"inputs": ['close'], "func": hwd_035_days_since_high_zscore_252d},
    "hwd_036_dist_to_52w_low_zscore_5d": {"inputs": ['close'], "func": hwd_036_dist_to_52w_low_zscore_5d},
    "hwd_037_dist_to_52w_low_zscore_21d": {"inputs": ['close'], "func": hwd_037_dist_to_52w_low_zscore_21d},
    "hwd_038_dist_to_52w_low_zscore_63d": {"inputs": ['close'], "func": hwd_038_dist_to_52w_low_zscore_63d},
    "hwd_039_dist_to_52w_low_zscore_126d": {"inputs": ['close'], "func": hwd_039_dist_to_52w_low_zscore_126d},
    "hwd_040_dist_to_52w_low_zscore_252d": {"inputs": ['close'], "func": hwd_040_dist_to_52w_low_zscore_252d},
    "hwd_041_high_intensity_zscore_5d": {"inputs": ['close'], "func": hwd_041_high_intensity_zscore_5d},
    "hwd_042_high_intensity_zscore_21d": {"inputs": ['close'], "func": hwd_042_high_intensity_zscore_21d},
    "hwd_043_high_intensity_zscore_63d": {"inputs": ['close'], "func": hwd_043_high_intensity_zscore_63d},
    "hwd_044_high_intensity_zscore_126d": {"inputs": ['close'], "func": hwd_044_high_intensity_zscore_126d},
    "hwd_045_high_intensity_zscore_252d": {"inputs": ['close'], "func": hwd_045_high_intensity_zscore_252d},
    "hwd_046_recovery_factor_zscore_5d": {"inputs": ['close'], "func": hwd_046_recovery_factor_zscore_5d},
    "hwd_047_recovery_factor_zscore_21d": {"inputs": ['close'], "func": hwd_047_recovery_factor_zscore_21d},
    "hwd_048_recovery_factor_zscore_63d": {"inputs": ['close'], "func": hwd_048_recovery_factor_zscore_63d},
    "hwd_049_recovery_factor_zscore_126d": {"inputs": ['close'], "func": hwd_049_recovery_factor_zscore_126d},
    "hwd_050_recovery_factor_zscore_252d": {"inputs": ['close'], "func": hwd_050_recovery_factor_zscore_252d},
    "hwd_051_hwd_dist_rank_5d": {"inputs": ['close'], "func": hwd_051_hwd_dist_rank_5d},
    "hwd_052_hwd_dist_rank_21d": {"inputs": ['close'], "func": hwd_052_hwd_dist_rank_21d},
    "hwd_053_hwd_dist_rank_63d": {"inputs": ['close'], "func": hwd_053_hwd_dist_rank_63d},
    "hwd_054_hwd_dist_rank_126d": {"inputs": ['close'], "func": hwd_054_hwd_dist_rank_126d},
    "hwd_055_hwd_dist_rank_252d": {"inputs": ['close'], "func": hwd_055_hwd_dist_rank_252d},
    "hwd_056_days_since_high_rank_5d": {"inputs": ['close'], "func": hwd_056_days_since_high_rank_5d},
    "hwd_057_days_since_high_rank_21d": {"inputs": ['close'], "func": hwd_057_days_since_high_rank_21d},
    "hwd_058_days_since_high_rank_63d": {"inputs": ['close'], "func": hwd_058_days_since_high_rank_63d},
    "hwd_059_days_since_high_rank_126d": {"inputs": ['close'], "func": hwd_059_days_since_high_rank_126d},
    "hwd_060_days_since_high_rank_252d": {"inputs": ['close'], "func": hwd_060_days_since_high_rank_252d},
    "hwd_061_dist_to_52w_low_rank_5d": {"inputs": ['close'], "func": hwd_061_dist_to_52w_low_rank_5d},
    "hwd_062_dist_to_52w_low_rank_21d": {"inputs": ['close'], "func": hwd_062_dist_to_52w_low_rank_21d},
    "hwd_063_dist_to_52w_low_rank_63d": {"inputs": ['close'], "func": hwd_063_dist_to_52w_low_rank_63d},
    "hwd_064_dist_to_52w_low_rank_126d": {"inputs": ['close'], "func": hwd_064_dist_to_52w_low_rank_126d},
    "hwd_065_dist_to_52w_low_rank_252d": {"inputs": ['close'], "func": hwd_065_dist_to_52w_low_rank_252d},
    "hwd_066_high_intensity_rank_5d": {"inputs": ['close'], "func": hwd_066_high_intensity_rank_5d},
    "hwd_067_high_intensity_rank_21d": {"inputs": ['close'], "func": hwd_067_high_intensity_rank_21d},
    "hwd_068_high_intensity_rank_63d": {"inputs": ['close'], "func": hwd_068_high_intensity_rank_63d},
    "hwd_069_high_intensity_rank_126d": {"inputs": ['close'], "func": hwd_069_high_intensity_rank_126d},
    "hwd_070_high_intensity_rank_252d": {"inputs": ['close'], "func": hwd_070_high_intensity_rank_252d},
    "hwd_071_recovery_factor_rank_5d": {"inputs": ['close'], "func": hwd_071_recovery_factor_rank_5d},
    "hwd_072_recovery_factor_rank_21d": {"inputs": ['close'], "func": hwd_072_recovery_factor_rank_21d},
    "hwd_073_recovery_factor_rank_63d": {"inputs": ['close'], "func": hwd_073_recovery_factor_rank_63d},
    "hwd_074_recovery_factor_rank_126d": {"inputs": ['close'], "func": hwd_074_recovery_factor_rank_126d},
    "hwd_075_recovery_factor_rank_252d": {"inputs": ['close'], "func": hwd_075_recovery_factor_rank_252d},
}
