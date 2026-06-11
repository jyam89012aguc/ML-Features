"""
Domain 30: volatility_acceleration (vtac_)
Asset Class: US Equities
Target Context: Acceleration and convexity of volatility.
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
def vtac_001_vol_accel_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5).diff().diff().rolling(5).mean()

def vtac_002_vol_accel_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21).diff().diff().rolling(21).mean()

def vtac_003_vol_accel_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63).diff().diff().rolling(63).mean()

def vtac_004_vol_accel_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126).diff().diff().rolling(126).mean()

def vtac_005_vol_accel_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252).diff().diff().rolling(252).mean()

def vtac_006_vol_convexity_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5).diff().diff()

def vtac_007_vol_convexity_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21).diff().diff()

def vtac_008_vol_convexity_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63).diff().diff()

def vtac_009_vol_convexity_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126).diff().diff()

def vtac_010_vol_convexity_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252).diff().diff()

def vtac_011_vol_jerk_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5).diff().diff().diff().rolling(5).mean()

def vtac_012_vol_jerk_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21).diff().diff().diff().rolling(21).mean()

def vtac_013_vol_jerk_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63).diff().diff().diff().rolling(63).mean()

def vtac_014_vol_jerk_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126).diff().diff().diff().rolling(126).mean()

def vtac_015_vol_jerk_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252).diff().diff().diff().rolling(252).mean()

def vtac_016_vol_speed_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5).diff().rolling(5).mean()

def vtac_017_vol_speed_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21).diff().rolling(21).mean()

def vtac_018_vol_speed_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63).diff().rolling(63).mean()

def vtac_019_vol_speed_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126).diff().rolling(126).mean()

def vtac_020_vol_speed_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252).diff().rolling(252).mean()

def vtac_021_vol_momentum_5d(close) -> pd.Series:
    return _daily_ret(_rolling_std(_daily_ret(close), 5))

def vtac_022_vol_momentum_21d(close) -> pd.Series:
    return _daily_ret(_rolling_std(_daily_ret(close), 21))

def vtac_023_vol_momentum_63d(close) -> pd.Series:
    return _daily_ret(_rolling_std(_daily_ret(close), 63))

def vtac_024_vol_momentum_126d(close) -> pd.Series:
    return _daily_ret(_rolling_std(_daily_ret(close), 126))

def vtac_025_vol_momentum_252d(close) -> pd.Series:
    return _daily_ret(_rolling_std(_daily_ret(close), 252))

def vtac_026_vol_accel_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vtac_001_vol_accel_5d(close), 252)

def vtac_027_vol_accel_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vtac_002_vol_accel_21d(close), 252)

def vtac_028_vol_accel_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vtac_003_vol_accel_63d(close), 252)

def vtac_029_vol_accel_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vtac_004_vol_accel_126d(close), 252)

def vtac_030_vol_accel_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vtac_005_vol_accel_252d(close), 252)

def vtac_031_vol_convexity_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vtac_006_vol_convexity_5d(close), 252)

def vtac_032_vol_convexity_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vtac_007_vol_convexity_21d(close), 252)

def vtac_033_vol_convexity_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vtac_008_vol_convexity_63d(close), 252)

def vtac_034_vol_convexity_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vtac_009_vol_convexity_126d(close), 252)

def vtac_035_vol_convexity_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vtac_010_vol_convexity_252d(close), 252)

def vtac_036_vol_jerk_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vtac_011_vol_jerk_5d(close), 252)

def vtac_037_vol_jerk_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vtac_012_vol_jerk_21d(close), 252)

def vtac_038_vol_jerk_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vtac_013_vol_jerk_63d(close), 252)

def vtac_039_vol_jerk_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vtac_014_vol_jerk_126d(close), 252)

def vtac_040_vol_jerk_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vtac_015_vol_jerk_252d(close), 252)

def vtac_041_vol_speed_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vtac_016_vol_speed_5d(close), 252)

def vtac_042_vol_speed_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vtac_017_vol_speed_21d(close), 252)

def vtac_043_vol_speed_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vtac_018_vol_speed_63d(close), 252)

def vtac_044_vol_speed_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vtac_019_vol_speed_126d(close), 252)

def vtac_045_vol_speed_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vtac_020_vol_speed_252d(close), 252)

def vtac_046_vol_momentum_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vtac_021_vol_momentum_5d(close), 252)

def vtac_047_vol_momentum_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vtac_022_vol_momentum_21d(close), 252)

def vtac_048_vol_momentum_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vtac_023_vol_momentum_63d(close), 252)

def vtac_049_vol_momentum_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vtac_024_vol_momentum_126d(close), 252)

def vtac_050_vol_momentum_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vtac_025_vol_momentum_252d(close), 252)

def vtac_051_vol_accel_rank_5d(close) -> pd.Series:
    return vtac_001_vol_accel_5d(close).rolling(252).rank(pct=True)

def vtac_052_vol_accel_rank_21d(close) -> pd.Series:
    return vtac_002_vol_accel_21d(close).rolling(252).rank(pct=True)

def vtac_053_vol_accel_rank_63d(close) -> pd.Series:
    return vtac_003_vol_accel_63d(close).rolling(252).rank(pct=True)

def vtac_054_vol_accel_rank_126d(close) -> pd.Series:
    return vtac_004_vol_accel_126d(close).rolling(252).rank(pct=True)

def vtac_055_vol_accel_rank_252d(close) -> pd.Series:
    return vtac_005_vol_accel_252d(close).rolling(252).rank(pct=True)

def vtac_056_vol_convexity_rank_5d(close) -> pd.Series:
    return vtac_006_vol_convexity_5d(close).rolling(252).rank(pct=True)

def vtac_057_vol_convexity_rank_21d(close) -> pd.Series:
    return vtac_007_vol_convexity_21d(close).rolling(252).rank(pct=True)

def vtac_058_vol_convexity_rank_63d(close) -> pd.Series:
    return vtac_008_vol_convexity_63d(close).rolling(252).rank(pct=True)

def vtac_059_vol_convexity_rank_126d(close) -> pd.Series:
    return vtac_009_vol_convexity_126d(close).rolling(252).rank(pct=True)

def vtac_060_vol_convexity_rank_252d(close) -> pd.Series:
    return vtac_010_vol_convexity_252d(close).rolling(252).rank(pct=True)

def vtac_061_vol_jerk_rank_5d(close) -> pd.Series:
    return vtac_011_vol_jerk_5d(close).rolling(252).rank(pct=True)

def vtac_062_vol_jerk_rank_21d(close) -> pd.Series:
    return vtac_012_vol_jerk_21d(close).rolling(252).rank(pct=True)

def vtac_063_vol_jerk_rank_63d(close) -> pd.Series:
    return vtac_013_vol_jerk_63d(close).rolling(252).rank(pct=True)

def vtac_064_vol_jerk_rank_126d(close) -> pd.Series:
    return vtac_014_vol_jerk_126d(close).rolling(252).rank(pct=True)

def vtac_065_vol_jerk_rank_252d(close) -> pd.Series:
    return vtac_015_vol_jerk_252d(close).rolling(252).rank(pct=True)

def vtac_066_vol_speed_rank_5d(close) -> pd.Series:
    return vtac_016_vol_speed_5d(close).rolling(252).rank(pct=True)

def vtac_067_vol_speed_rank_21d(close) -> pd.Series:
    return vtac_017_vol_speed_21d(close).rolling(252).rank(pct=True)

def vtac_068_vol_speed_rank_63d(close) -> pd.Series:
    return vtac_018_vol_speed_63d(close).rolling(252).rank(pct=True)

def vtac_069_vol_speed_rank_126d(close) -> pd.Series:
    return vtac_019_vol_speed_126d(close).rolling(252).rank(pct=True)

def vtac_070_vol_speed_rank_252d(close) -> pd.Series:
    return vtac_020_vol_speed_252d(close).rolling(252).rank(pct=True)

def vtac_071_vol_momentum_rank_5d(close) -> pd.Series:
    return vtac_021_vol_momentum_5d(close).rolling(252).rank(pct=True)

def vtac_072_vol_momentum_rank_21d(close) -> pd.Series:
    return vtac_022_vol_momentum_21d(close).rolling(252).rank(pct=True)

def vtac_073_vol_momentum_rank_63d(close) -> pd.Series:
    return vtac_023_vol_momentum_63d(close).rolling(252).rank(pct=True)

def vtac_074_vol_momentum_rank_126d(close) -> pd.Series:
    return vtac_024_vol_momentum_126d(close).rolling(252).rank(pct=True)

def vtac_075_vol_momentum_rank_252d(close) -> pd.Series:
    return vtac_025_vol_momentum_252d(close).rolling(252).rank(pct=True)


# --- Registry ---
V30_REGISTRY = {
    "vtac_001_vol_accel_5d": {"inputs": ['close'], "func": vtac_001_vol_accel_5d},
    "vtac_002_vol_accel_21d": {"inputs": ['close'], "func": vtac_002_vol_accel_21d},
    "vtac_003_vol_accel_63d": {"inputs": ['close'], "func": vtac_003_vol_accel_63d},
    "vtac_004_vol_accel_126d": {"inputs": ['close'], "func": vtac_004_vol_accel_126d},
    "vtac_005_vol_accel_252d": {"inputs": ['close'], "func": vtac_005_vol_accel_252d},
    "vtac_006_vol_convexity_5d": {"inputs": ['close'], "func": vtac_006_vol_convexity_5d},
    "vtac_007_vol_convexity_21d": {"inputs": ['close'], "func": vtac_007_vol_convexity_21d},
    "vtac_008_vol_convexity_63d": {"inputs": ['close'], "func": vtac_008_vol_convexity_63d},
    "vtac_009_vol_convexity_126d": {"inputs": ['close'], "func": vtac_009_vol_convexity_126d},
    "vtac_010_vol_convexity_252d": {"inputs": ['close'], "func": vtac_010_vol_convexity_252d},
    "vtac_011_vol_jerk_5d": {"inputs": ['close'], "func": vtac_011_vol_jerk_5d},
    "vtac_012_vol_jerk_21d": {"inputs": ['close'], "func": vtac_012_vol_jerk_21d},
    "vtac_013_vol_jerk_63d": {"inputs": ['close'], "func": vtac_013_vol_jerk_63d},
    "vtac_014_vol_jerk_126d": {"inputs": ['close'], "func": vtac_014_vol_jerk_126d},
    "vtac_015_vol_jerk_252d": {"inputs": ['close'], "func": vtac_015_vol_jerk_252d},
    "vtac_016_vol_speed_5d": {"inputs": ['close'], "func": vtac_016_vol_speed_5d},
    "vtac_017_vol_speed_21d": {"inputs": ['close'], "func": vtac_017_vol_speed_21d},
    "vtac_018_vol_speed_63d": {"inputs": ['close'], "func": vtac_018_vol_speed_63d},
    "vtac_019_vol_speed_126d": {"inputs": ['close'], "func": vtac_019_vol_speed_126d},
    "vtac_020_vol_speed_252d": {"inputs": ['close'], "func": vtac_020_vol_speed_252d},
    "vtac_021_vol_momentum_5d": {"inputs": ['close'], "func": vtac_021_vol_momentum_5d},
    "vtac_022_vol_momentum_21d": {"inputs": ['close'], "func": vtac_022_vol_momentum_21d},
    "vtac_023_vol_momentum_63d": {"inputs": ['close'], "func": vtac_023_vol_momentum_63d},
    "vtac_024_vol_momentum_126d": {"inputs": ['close'], "func": vtac_024_vol_momentum_126d},
    "vtac_025_vol_momentum_252d": {"inputs": ['close'], "func": vtac_025_vol_momentum_252d},
    "vtac_026_vol_accel_zscore_5d": {"inputs": ['close'], "func": vtac_026_vol_accel_zscore_5d},
    "vtac_027_vol_accel_zscore_21d": {"inputs": ['close'], "func": vtac_027_vol_accel_zscore_21d},
    "vtac_028_vol_accel_zscore_63d": {"inputs": ['close'], "func": vtac_028_vol_accel_zscore_63d},
    "vtac_029_vol_accel_zscore_126d": {"inputs": ['close'], "func": vtac_029_vol_accel_zscore_126d},
    "vtac_030_vol_accel_zscore_252d": {"inputs": ['close'], "func": vtac_030_vol_accel_zscore_252d},
    "vtac_031_vol_convexity_zscore_5d": {"inputs": ['close'], "func": vtac_031_vol_convexity_zscore_5d},
    "vtac_032_vol_convexity_zscore_21d": {"inputs": ['close'], "func": vtac_032_vol_convexity_zscore_21d},
    "vtac_033_vol_convexity_zscore_63d": {"inputs": ['close'], "func": vtac_033_vol_convexity_zscore_63d},
    "vtac_034_vol_convexity_zscore_126d": {"inputs": ['close'], "func": vtac_034_vol_convexity_zscore_126d},
    "vtac_035_vol_convexity_zscore_252d": {"inputs": ['close'], "func": vtac_035_vol_convexity_zscore_252d},
    "vtac_036_vol_jerk_zscore_5d": {"inputs": ['close'], "func": vtac_036_vol_jerk_zscore_5d},
    "vtac_037_vol_jerk_zscore_21d": {"inputs": ['close'], "func": vtac_037_vol_jerk_zscore_21d},
    "vtac_038_vol_jerk_zscore_63d": {"inputs": ['close'], "func": vtac_038_vol_jerk_zscore_63d},
    "vtac_039_vol_jerk_zscore_126d": {"inputs": ['close'], "func": vtac_039_vol_jerk_zscore_126d},
    "vtac_040_vol_jerk_zscore_252d": {"inputs": ['close'], "func": vtac_040_vol_jerk_zscore_252d},
    "vtac_041_vol_speed_zscore_5d": {"inputs": ['close'], "func": vtac_041_vol_speed_zscore_5d},
    "vtac_042_vol_speed_zscore_21d": {"inputs": ['close'], "func": vtac_042_vol_speed_zscore_21d},
    "vtac_043_vol_speed_zscore_63d": {"inputs": ['close'], "func": vtac_043_vol_speed_zscore_63d},
    "vtac_044_vol_speed_zscore_126d": {"inputs": ['close'], "func": vtac_044_vol_speed_zscore_126d},
    "vtac_045_vol_speed_zscore_252d": {"inputs": ['close'], "func": vtac_045_vol_speed_zscore_252d},
    "vtac_046_vol_momentum_zscore_5d": {"inputs": ['close'], "func": vtac_046_vol_momentum_zscore_5d},
    "vtac_047_vol_momentum_zscore_21d": {"inputs": ['close'], "func": vtac_047_vol_momentum_zscore_21d},
    "vtac_048_vol_momentum_zscore_63d": {"inputs": ['close'], "func": vtac_048_vol_momentum_zscore_63d},
    "vtac_049_vol_momentum_zscore_126d": {"inputs": ['close'], "func": vtac_049_vol_momentum_zscore_126d},
    "vtac_050_vol_momentum_zscore_252d": {"inputs": ['close'], "func": vtac_050_vol_momentum_zscore_252d},
    "vtac_051_vol_accel_rank_5d": {"inputs": ['close'], "func": vtac_051_vol_accel_rank_5d},
    "vtac_052_vol_accel_rank_21d": {"inputs": ['close'], "func": vtac_052_vol_accel_rank_21d},
    "vtac_053_vol_accel_rank_63d": {"inputs": ['close'], "func": vtac_053_vol_accel_rank_63d},
    "vtac_054_vol_accel_rank_126d": {"inputs": ['close'], "func": vtac_054_vol_accel_rank_126d},
    "vtac_055_vol_accel_rank_252d": {"inputs": ['close'], "func": vtac_055_vol_accel_rank_252d},
    "vtac_056_vol_convexity_rank_5d": {"inputs": ['close'], "func": vtac_056_vol_convexity_rank_5d},
    "vtac_057_vol_convexity_rank_21d": {"inputs": ['close'], "func": vtac_057_vol_convexity_rank_21d},
    "vtac_058_vol_convexity_rank_63d": {"inputs": ['close'], "func": vtac_058_vol_convexity_rank_63d},
    "vtac_059_vol_convexity_rank_126d": {"inputs": ['close'], "func": vtac_059_vol_convexity_rank_126d},
    "vtac_060_vol_convexity_rank_252d": {"inputs": ['close'], "func": vtac_060_vol_convexity_rank_252d},
    "vtac_061_vol_jerk_rank_5d": {"inputs": ['close'], "func": vtac_061_vol_jerk_rank_5d},
    "vtac_062_vol_jerk_rank_21d": {"inputs": ['close'], "func": vtac_062_vol_jerk_rank_21d},
    "vtac_063_vol_jerk_rank_63d": {"inputs": ['close'], "func": vtac_063_vol_jerk_rank_63d},
    "vtac_064_vol_jerk_rank_126d": {"inputs": ['close'], "func": vtac_064_vol_jerk_rank_126d},
    "vtac_065_vol_jerk_rank_252d": {"inputs": ['close'], "func": vtac_065_vol_jerk_rank_252d},
    "vtac_066_vol_speed_rank_5d": {"inputs": ['close'], "func": vtac_066_vol_speed_rank_5d},
    "vtac_067_vol_speed_rank_21d": {"inputs": ['close'], "func": vtac_067_vol_speed_rank_21d},
    "vtac_068_vol_speed_rank_63d": {"inputs": ['close'], "func": vtac_068_vol_speed_rank_63d},
    "vtac_069_vol_speed_rank_126d": {"inputs": ['close'], "func": vtac_069_vol_speed_rank_126d},
    "vtac_070_vol_speed_rank_252d": {"inputs": ['close'], "func": vtac_070_vol_speed_rank_252d},
    "vtac_071_vol_momentum_rank_5d": {"inputs": ['close'], "func": vtac_071_vol_momentum_rank_5d},
    "vtac_072_vol_momentum_rank_21d": {"inputs": ['close'], "func": vtac_072_vol_momentum_rank_21d},
    "vtac_073_vol_momentum_rank_63d": {"inputs": ['close'], "func": vtac_073_vol_momentum_rank_63d},
    "vtac_074_vol_momentum_rank_126d": {"inputs": ['close'], "func": vtac_074_vol_momentum_rank_126d},
    "vtac_075_vol_momentum_rank_252d": {"inputs": ['close'], "func": vtac_075_vol_momentum_rank_252d},
}
