"""
Domain 34: volatility_distribution (vdst_)
Asset Class: US Equities
Target Context: Shape and properties of the volatility distribution.
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
def vdst_001_dist_mean_5d(close) -> pd.Series:
    return _rolling_mean(_rolling_std(_daily_ret(close), 5), 5)

def vdst_002_dist_mean_21d(close) -> pd.Series:
    return _rolling_mean(_rolling_std(_daily_ret(close), 21), 21)

def vdst_003_dist_mean_63d(close) -> pd.Series:
    return _rolling_mean(_rolling_std(_daily_ret(close), 63), 63)

def vdst_004_dist_mean_126d(close) -> pd.Series:
    return _rolling_mean(_rolling_std(_daily_ret(close), 126), 126)

def vdst_005_dist_mean_252d(close) -> pd.Series:
    return _rolling_mean(_rolling_std(_daily_ret(close), 252), 252)

def vdst_006_dist_var_5d(close) -> pd.Series:
    return _rolling_std(_rolling_std(_daily_ret(close), 5), 5)

def vdst_007_dist_var_21d(close) -> pd.Series:
    return _rolling_std(_rolling_std(_daily_ret(close), 21), 21)

def vdst_008_dist_var_63d(close) -> pd.Series:
    return _rolling_std(_rolling_std(_daily_ret(close), 63), 63)

def vdst_009_dist_var_126d(close) -> pd.Series:
    return _rolling_std(_rolling_std(_daily_ret(close), 126), 126)

def vdst_010_dist_var_252d(close) -> pd.Series:
    return _rolling_std(_rolling_std(_daily_ret(close), 252), 252)

def vdst_011_dist_tail_5d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 5) > _rolling_mean(_rolling_std(_daily_ret(close), 5), 252) + 2*_rolling_std(_rolling_std(_daily_ret(close), 5), 252)).astype(float)

def vdst_012_dist_tail_21d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 21) > _rolling_mean(_rolling_std(_daily_ret(close), 21), 252) + 2*_rolling_std(_rolling_std(_daily_ret(close), 21), 252)).astype(float)

def vdst_013_dist_tail_63d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 63) > _rolling_mean(_rolling_std(_daily_ret(close), 63), 252) + 2*_rolling_std(_rolling_std(_daily_ret(close), 63), 252)).astype(float)

def vdst_014_dist_tail_126d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 126) > _rolling_mean(_rolling_std(_daily_ret(close), 126), 252) + 2*_rolling_std(_rolling_std(_daily_ret(close), 126), 252)).astype(float)

def vdst_015_dist_tail_252d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 252) > _rolling_mean(_rolling_std(_daily_ret(close), 252), 252) + 2*_rolling_std(_rolling_std(_daily_ret(close), 252), 252)).astype(float)

def vdst_016_dist_normality_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5).rolling(5).kurt().abs()

def vdst_017_dist_normality_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21).rolling(21).kurt().abs()

def vdst_018_dist_normality_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63).rolling(63).kurt().abs()

def vdst_019_dist_normality_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126).rolling(126).kurt().abs()

def vdst_020_dist_normality_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252).rolling(252).kurt().abs()

def vdst_021_dist_entropy_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5).rolling(5).apply(_entropy_calc, raw=False)

def vdst_022_dist_entropy_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21).rolling(21).apply(_entropy_calc, raw=False)

def vdst_023_dist_entropy_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63).rolling(63).apply(_entropy_calc, raw=False)

def vdst_024_dist_entropy_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126).rolling(126).apply(_entropy_calc, raw=False)

def vdst_025_dist_entropy_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252).rolling(252).apply(_entropy_calc, raw=False)

def vdst_026_dist_mean_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vdst_001_dist_mean_5d(close), 252)

def vdst_027_dist_mean_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vdst_002_dist_mean_21d(close), 252)

def vdst_028_dist_mean_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vdst_003_dist_mean_63d(close), 252)

def vdst_029_dist_mean_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vdst_004_dist_mean_126d(close), 252)

def vdst_030_dist_mean_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vdst_005_dist_mean_252d(close), 252)

def vdst_031_dist_var_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vdst_006_dist_var_5d(close), 252)

def vdst_032_dist_var_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vdst_007_dist_var_21d(close), 252)

def vdst_033_dist_var_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vdst_008_dist_var_63d(close), 252)

def vdst_034_dist_var_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vdst_009_dist_var_126d(close), 252)

def vdst_035_dist_var_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vdst_010_dist_var_252d(close), 252)

def vdst_036_dist_tail_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vdst_011_dist_tail_5d(close), 252)

def vdst_037_dist_tail_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vdst_012_dist_tail_21d(close), 252)

def vdst_038_dist_tail_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vdst_013_dist_tail_63d(close), 252)

def vdst_039_dist_tail_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vdst_014_dist_tail_126d(close), 252)

def vdst_040_dist_tail_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vdst_015_dist_tail_252d(close), 252)

def vdst_041_dist_normality_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vdst_016_dist_normality_5d(close), 252)

def vdst_042_dist_normality_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vdst_017_dist_normality_21d(close), 252)

def vdst_043_dist_normality_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vdst_018_dist_normality_63d(close), 252)

def vdst_044_dist_normality_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vdst_019_dist_normality_126d(close), 252)

def vdst_045_dist_normality_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vdst_020_dist_normality_252d(close), 252)

def vdst_046_dist_entropy_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vdst_021_dist_entropy_5d(close), 252)

def vdst_047_dist_entropy_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vdst_022_dist_entropy_21d(close), 252)

def vdst_048_dist_entropy_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vdst_023_dist_entropy_63d(close), 252)

def vdst_049_dist_entropy_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vdst_024_dist_entropy_126d(close), 252)

def vdst_050_dist_entropy_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vdst_025_dist_entropy_252d(close), 252)

def vdst_051_dist_mean_rank_5d(close) -> pd.Series:
    return vdst_001_dist_mean_5d(close).rolling(252).rank(pct=True)

def vdst_052_dist_mean_rank_21d(close) -> pd.Series:
    return vdst_002_dist_mean_21d(close).rolling(252).rank(pct=True)

def vdst_053_dist_mean_rank_63d(close) -> pd.Series:
    return vdst_003_dist_mean_63d(close).rolling(252).rank(pct=True)

def vdst_054_dist_mean_rank_126d(close) -> pd.Series:
    return vdst_004_dist_mean_126d(close).rolling(252).rank(pct=True)

def vdst_055_dist_mean_rank_252d(close) -> pd.Series:
    return vdst_005_dist_mean_252d(close).rolling(252).rank(pct=True)

def vdst_056_dist_var_rank_5d(close) -> pd.Series:
    return vdst_006_dist_var_5d(close).rolling(252).rank(pct=True)

def vdst_057_dist_var_rank_21d(close) -> pd.Series:
    return vdst_007_dist_var_21d(close).rolling(252).rank(pct=True)

def vdst_058_dist_var_rank_63d(close) -> pd.Series:
    return vdst_008_dist_var_63d(close).rolling(252).rank(pct=True)

def vdst_059_dist_var_rank_126d(close) -> pd.Series:
    return vdst_009_dist_var_126d(close).rolling(252).rank(pct=True)

def vdst_060_dist_var_rank_252d(close) -> pd.Series:
    return vdst_010_dist_var_252d(close).rolling(252).rank(pct=True)

def vdst_061_dist_tail_rank_5d(close) -> pd.Series:
    return vdst_011_dist_tail_5d(close).rolling(252).rank(pct=True)

def vdst_062_dist_tail_rank_21d(close) -> pd.Series:
    return vdst_012_dist_tail_21d(close).rolling(252).rank(pct=True)

def vdst_063_dist_tail_rank_63d(close) -> pd.Series:
    return vdst_013_dist_tail_63d(close).rolling(252).rank(pct=True)

def vdst_064_dist_tail_rank_126d(close) -> pd.Series:
    return vdst_014_dist_tail_126d(close).rolling(252).rank(pct=True)

def vdst_065_dist_tail_rank_252d(close) -> pd.Series:
    return vdst_015_dist_tail_252d(close).rolling(252).rank(pct=True)

def vdst_066_dist_normality_rank_5d(close) -> pd.Series:
    return vdst_016_dist_normality_5d(close).rolling(252).rank(pct=True)

def vdst_067_dist_normality_rank_21d(close) -> pd.Series:
    return vdst_017_dist_normality_21d(close).rolling(252).rank(pct=True)

def vdst_068_dist_normality_rank_63d(close) -> pd.Series:
    return vdst_018_dist_normality_63d(close).rolling(252).rank(pct=True)

def vdst_069_dist_normality_rank_126d(close) -> pd.Series:
    return vdst_019_dist_normality_126d(close).rolling(252).rank(pct=True)

def vdst_070_dist_normality_rank_252d(close) -> pd.Series:
    return vdst_020_dist_normality_252d(close).rolling(252).rank(pct=True)

def vdst_071_dist_entropy_rank_5d(close) -> pd.Series:
    return vdst_021_dist_entropy_5d(close).rolling(252).rank(pct=True)

def vdst_072_dist_entropy_rank_21d(close) -> pd.Series:
    return vdst_022_dist_entropy_21d(close).rolling(252).rank(pct=True)

def vdst_073_dist_entropy_rank_63d(close) -> pd.Series:
    return vdst_023_dist_entropy_63d(close).rolling(252).rank(pct=True)

def vdst_074_dist_entropy_rank_126d(close) -> pd.Series:
    return vdst_024_dist_entropy_126d(close).rolling(252).rank(pct=True)

def vdst_075_dist_entropy_rank_252d(close) -> pd.Series:
    return vdst_025_dist_entropy_252d(close).rolling(252).rank(pct=True)


# --- Registry ---
V34_REGISTRY = {
    "vdst_001_dist_mean_5d": {"inputs": ['close'], "func": vdst_001_dist_mean_5d},
    "vdst_002_dist_mean_21d": {"inputs": ['close'], "func": vdst_002_dist_mean_21d},
    "vdst_003_dist_mean_63d": {"inputs": ['close'], "func": vdst_003_dist_mean_63d},
    "vdst_004_dist_mean_126d": {"inputs": ['close'], "func": vdst_004_dist_mean_126d},
    "vdst_005_dist_mean_252d": {"inputs": ['close'], "func": vdst_005_dist_mean_252d},
    "vdst_006_dist_var_5d": {"inputs": ['close'], "func": vdst_006_dist_var_5d},
    "vdst_007_dist_var_21d": {"inputs": ['close'], "func": vdst_007_dist_var_21d},
    "vdst_008_dist_var_63d": {"inputs": ['close'], "func": vdst_008_dist_var_63d},
    "vdst_009_dist_var_126d": {"inputs": ['close'], "func": vdst_009_dist_var_126d},
    "vdst_010_dist_var_252d": {"inputs": ['close'], "func": vdst_010_dist_var_252d},
    "vdst_011_dist_tail_5d": {"inputs": ['close'], "func": vdst_011_dist_tail_5d},
    "vdst_012_dist_tail_21d": {"inputs": ['close'], "func": vdst_012_dist_tail_21d},
    "vdst_013_dist_tail_63d": {"inputs": ['close'], "func": vdst_013_dist_tail_63d},
    "vdst_014_dist_tail_126d": {"inputs": ['close'], "func": vdst_014_dist_tail_126d},
    "vdst_015_dist_tail_252d": {"inputs": ['close'], "func": vdst_015_dist_tail_252d},
    "vdst_016_dist_normality_5d": {"inputs": ['close'], "func": vdst_016_dist_normality_5d},
    "vdst_017_dist_normality_21d": {"inputs": ['close'], "func": vdst_017_dist_normality_21d},
    "vdst_018_dist_normality_63d": {"inputs": ['close'], "func": vdst_018_dist_normality_63d},
    "vdst_019_dist_normality_126d": {"inputs": ['close'], "func": vdst_019_dist_normality_126d},
    "vdst_020_dist_normality_252d": {"inputs": ['close'], "func": vdst_020_dist_normality_252d},
    "vdst_021_dist_entropy_5d": {"inputs": ['close'], "func": vdst_021_dist_entropy_5d},
    "vdst_022_dist_entropy_21d": {"inputs": ['close'], "func": vdst_022_dist_entropy_21d},
    "vdst_023_dist_entropy_63d": {"inputs": ['close'], "func": vdst_023_dist_entropy_63d},
    "vdst_024_dist_entropy_126d": {"inputs": ['close'], "func": vdst_024_dist_entropy_126d},
    "vdst_025_dist_entropy_252d": {"inputs": ['close'], "func": vdst_025_dist_entropy_252d},
    "vdst_026_dist_mean_zscore_5d": {"inputs": ['close'], "func": vdst_026_dist_mean_zscore_5d},
    "vdst_027_dist_mean_zscore_21d": {"inputs": ['close'], "func": vdst_027_dist_mean_zscore_21d},
    "vdst_028_dist_mean_zscore_63d": {"inputs": ['close'], "func": vdst_028_dist_mean_zscore_63d},
    "vdst_029_dist_mean_zscore_126d": {"inputs": ['close'], "func": vdst_029_dist_mean_zscore_126d},
    "vdst_030_dist_mean_zscore_252d": {"inputs": ['close'], "func": vdst_030_dist_mean_zscore_252d},
    "vdst_031_dist_var_zscore_5d": {"inputs": ['close'], "func": vdst_031_dist_var_zscore_5d},
    "vdst_032_dist_var_zscore_21d": {"inputs": ['close'], "func": vdst_032_dist_var_zscore_21d},
    "vdst_033_dist_var_zscore_63d": {"inputs": ['close'], "func": vdst_033_dist_var_zscore_63d},
    "vdst_034_dist_var_zscore_126d": {"inputs": ['close'], "func": vdst_034_dist_var_zscore_126d},
    "vdst_035_dist_var_zscore_252d": {"inputs": ['close'], "func": vdst_035_dist_var_zscore_252d},
    "vdst_036_dist_tail_zscore_5d": {"inputs": ['close'], "func": vdst_036_dist_tail_zscore_5d},
    "vdst_037_dist_tail_zscore_21d": {"inputs": ['close'], "func": vdst_037_dist_tail_zscore_21d},
    "vdst_038_dist_tail_zscore_63d": {"inputs": ['close'], "func": vdst_038_dist_tail_zscore_63d},
    "vdst_039_dist_tail_zscore_126d": {"inputs": ['close'], "func": vdst_039_dist_tail_zscore_126d},
    "vdst_040_dist_tail_zscore_252d": {"inputs": ['close'], "func": vdst_040_dist_tail_zscore_252d},
    "vdst_041_dist_normality_zscore_5d": {"inputs": ['close'], "func": vdst_041_dist_normality_zscore_5d},
    "vdst_042_dist_normality_zscore_21d": {"inputs": ['close'], "func": vdst_042_dist_normality_zscore_21d},
    "vdst_043_dist_normality_zscore_63d": {"inputs": ['close'], "func": vdst_043_dist_normality_zscore_63d},
    "vdst_044_dist_normality_zscore_126d": {"inputs": ['close'], "func": vdst_044_dist_normality_zscore_126d},
    "vdst_045_dist_normality_zscore_252d": {"inputs": ['close'], "func": vdst_045_dist_normality_zscore_252d},
    "vdst_046_dist_entropy_zscore_5d": {"inputs": ['close'], "func": vdst_046_dist_entropy_zscore_5d},
    "vdst_047_dist_entropy_zscore_21d": {"inputs": ['close'], "func": vdst_047_dist_entropy_zscore_21d},
    "vdst_048_dist_entropy_zscore_63d": {"inputs": ['close'], "func": vdst_048_dist_entropy_zscore_63d},
    "vdst_049_dist_entropy_zscore_126d": {"inputs": ['close'], "func": vdst_049_dist_entropy_zscore_126d},
    "vdst_050_dist_entropy_zscore_252d": {"inputs": ['close'], "func": vdst_050_dist_entropy_zscore_252d},
    "vdst_051_dist_mean_rank_5d": {"inputs": ['close'], "func": vdst_051_dist_mean_rank_5d},
    "vdst_052_dist_mean_rank_21d": {"inputs": ['close'], "func": vdst_052_dist_mean_rank_21d},
    "vdst_053_dist_mean_rank_63d": {"inputs": ['close'], "func": vdst_053_dist_mean_rank_63d},
    "vdst_054_dist_mean_rank_126d": {"inputs": ['close'], "func": vdst_054_dist_mean_rank_126d},
    "vdst_055_dist_mean_rank_252d": {"inputs": ['close'], "func": vdst_055_dist_mean_rank_252d},
    "vdst_056_dist_var_rank_5d": {"inputs": ['close'], "func": vdst_056_dist_var_rank_5d},
    "vdst_057_dist_var_rank_21d": {"inputs": ['close'], "func": vdst_057_dist_var_rank_21d},
    "vdst_058_dist_var_rank_63d": {"inputs": ['close'], "func": vdst_058_dist_var_rank_63d},
    "vdst_059_dist_var_rank_126d": {"inputs": ['close'], "func": vdst_059_dist_var_rank_126d},
    "vdst_060_dist_var_rank_252d": {"inputs": ['close'], "func": vdst_060_dist_var_rank_252d},
    "vdst_061_dist_tail_rank_5d": {"inputs": ['close'], "func": vdst_061_dist_tail_rank_5d},
    "vdst_062_dist_tail_rank_21d": {"inputs": ['close'], "func": vdst_062_dist_tail_rank_21d},
    "vdst_063_dist_tail_rank_63d": {"inputs": ['close'], "func": vdst_063_dist_tail_rank_63d},
    "vdst_064_dist_tail_rank_126d": {"inputs": ['close'], "func": vdst_064_dist_tail_rank_126d},
    "vdst_065_dist_tail_rank_252d": {"inputs": ['close'], "func": vdst_065_dist_tail_rank_252d},
    "vdst_066_dist_normality_rank_5d": {"inputs": ['close'], "func": vdst_066_dist_normality_rank_5d},
    "vdst_067_dist_normality_rank_21d": {"inputs": ['close'], "func": vdst_067_dist_normality_rank_21d},
    "vdst_068_dist_normality_rank_63d": {"inputs": ['close'], "func": vdst_068_dist_normality_rank_63d},
    "vdst_069_dist_normality_rank_126d": {"inputs": ['close'], "func": vdst_069_dist_normality_rank_126d},
    "vdst_070_dist_normality_rank_252d": {"inputs": ['close'], "func": vdst_070_dist_normality_rank_252d},
    "vdst_071_dist_entropy_rank_5d": {"inputs": ['close'], "func": vdst_071_dist_entropy_rank_5d},
    "vdst_072_dist_entropy_rank_21d": {"inputs": ['close'], "func": vdst_072_dist_entropy_rank_21d},
    "vdst_073_dist_entropy_rank_63d": {"inputs": ['close'], "func": vdst_073_dist_entropy_rank_63d},
    "vdst_074_dist_entropy_rank_126d": {"inputs": ['close'], "func": vdst_074_dist_entropy_rank_126d},
    "vdst_075_dist_entropy_rank_252d": {"inputs": ['close'], "func": vdst_075_dist_entropy_rank_252d},
}
