"""
Domain 13: drawdown_acceleration (dacc_)
Asset Class: US Equities
Target Context: Acceleration and velocity of price drawdowns.
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
def dacc_001_dd_vel_5d(close) -> pd.Series:
    return _daily_ret(close).rolling(5).mean()

def dacc_002_dd_vel_21d(close) -> pd.Series:
    return _daily_ret(close).rolling(21).mean()

def dacc_003_dd_vel_63d(close) -> pd.Series:
    return _daily_ret(close).rolling(63).mean()

def dacc_004_dd_vel_126d(close) -> pd.Series:
    return _daily_ret(close).rolling(126).mean()

def dacc_005_dd_vel_252d(close) -> pd.Series:
    return _daily_ret(close).rolling(252).mean()

def dacc_006_dd_accel_5d(close) -> pd.Series:
    return _daily_ret(close).diff().rolling(5).mean()

def dacc_007_dd_accel_21d(close) -> pd.Series:
    return _daily_ret(close).diff().rolling(21).mean()

def dacc_008_dd_accel_63d(close) -> pd.Series:
    return _daily_ret(close).diff().rolling(63).mean()

def dacc_009_dd_accel_126d(close) -> pd.Series:
    return _daily_ret(close).diff().rolling(126).mean()

def dacc_010_dd_accel_252d(close) -> pd.Series:
    return _daily_ret(close).diff().rolling(252).mean()

def dacc_011_dd_jerk_5d(close) -> pd.Series:
    return _daily_ret(close).diff().diff().rolling(5).mean()

def dacc_012_dd_jerk_21d(close) -> pd.Series:
    return _daily_ret(close).diff().diff().rolling(21).mean()

def dacc_013_dd_jerk_63d(close) -> pd.Series:
    return _daily_ret(close).diff().diff().rolling(63).mean()

def dacc_014_dd_jerk_126d(close) -> pd.Series:
    return _daily_ret(close).diff().diff().rolling(126).mean()

def dacc_015_dd_jerk_252d(close) -> pd.Series:
    return _daily_ret(close).diff().diff().rolling(252).mean()

def dacc_016_underwater_velocity_5d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).diff().rolling(5).mean())(close)

def dacc_017_underwater_velocity_21d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).diff().rolling(21).mean())(close)

def dacc_018_underwater_velocity_63d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).diff().rolling(63).mean())(close)

def dacc_019_underwater_velocity_126d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).diff().rolling(126).mean())(close)

def dacc_020_underwater_velocity_252d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).diff().rolling(252).mean())(close)

def dacc_021_recovery_velocity_5d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(5).min(), x.rolling(5).min()).diff().rolling(5).mean())(close)

def dacc_022_recovery_velocity_21d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(21).min(), x.rolling(21).min()).diff().rolling(21).mean())(close)

def dacc_023_recovery_velocity_63d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(63).min(), x.rolling(63).min()).diff().rolling(63).mean())(close)

def dacc_024_recovery_velocity_126d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(126).min(), x.rolling(126).min()).diff().rolling(126).mean())(close)

def dacc_025_recovery_velocity_252d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252).min(), x.rolling(252).min()).diff().rolling(252).mean())(close)

def dacc_026_dd_vel_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(dacc_001_dd_vel_5d(close), 252)

def dacc_027_dd_vel_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(dacc_002_dd_vel_21d(close), 252)

def dacc_028_dd_vel_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(dacc_003_dd_vel_63d(close), 252)

def dacc_029_dd_vel_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(dacc_004_dd_vel_126d(close), 252)

def dacc_030_dd_vel_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(dacc_005_dd_vel_252d(close), 252)

def dacc_031_dd_accel_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(dacc_006_dd_accel_5d(close), 252)

def dacc_032_dd_accel_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(dacc_007_dd_accel_21d(close), 252)

def dacc_033_dd_accel_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(dacc_008_dd_accel_63d(close), 252)

def dacc_034_dd_accel_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(dacc_009_dd_accel_126d(close), 252)

def dacc_035_dd_accel_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(dacc_010_dd_accel_252d(close), 252)

def dacc_036_dd_jerk_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(dacc_011_dd_jerk_5d(close), 252)

def dacc_037_dd_jerk_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(dacc_012_dd_jerk_21d(close), 252)

def dacc_038_dd_jerk_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(dacc_013_dd_jerk_63d(close), 252)

def dacc_039_dd_jerk_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(dacc_014_dd_jerk_126d(close), 252)

def dacc_040_dd_jerk_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(dacc_015_dd_jerk_252d(close), 252)

def dacc_041_underwater_velocity_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(dacc_016_underwater_velocity_5d(close), 252)

def dacc_042_underwater_velocity_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(dacc_017_underwater_velocity_21d(close), 252)

def dacc_043_underwater_velocity_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(dacc_018_underwater_velocity_63d(close), 252)

def dacc_044_underwater_velocity_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(dacc_019_underwater_velocity_126d(close), 252)

def dacc_045_underwater_velocity_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(dacc_020_underwater_velocity_252d(close), 252)

def dacc_046_recovery_velocity_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(dacc_021_recovery_velocity_5d(close), 252)

def dacc_047_recovery_velocity_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(dacc_022_recovery_velocity_21d(close), 252)

def dacc_048_recovery_velocity_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(dacc_023_recovery_velocity_63d(close), 252)

def dacc_049_recovery_velocity_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(dacc_024_recovery_velocity_126d(close), 252)

def dacc_050_recovery_velocity_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(dacc_025_recovery_velocity_252d(close), 252)

def dacc_051_dd_vel_rank_5d(close) -> pd.Series:
    return dacc_001_dd_vel_5d(close).rolling(252).rank(pct=True)

def dacc_052_dd_vel_rank_21d(close) -> pd.Series:
    return dacc_002_dd_vel_21d(close).rolling(252).rank(pct=True)

def dacc_053_dd_vel_rank_63d(close) -> pd.Series:
    return dacc_003_dd_vel_63d(close).rolling(252).rank(pct=True)

def dacc_054_dd_vel_rank_126d(close) -> pd.Series:
    return dacc_004_dd_vel_126d(close).rolling(252).rank(pct=True)

def dacc_055_dd_vel_rank_252d(close) -> pd.Series:
    return dacc_005_dd_vel_252d(close).rolling(252).rank(pct=True)

def dacc_056_dd_accel_rank_5d(close) -> pd.Series:
    return dacc_006_dd_accel_5d(close).rolling(252).rank(pct=True)

def dacc_057_dd_accel_rank_21d(close) -> pd.Series:
    return dacc_007_dd_accel_21d(close).rolling(252).rank(pct=True)

def dacc_058_dd_accel_rank_63d(close) -> pd.Series:
    return dacc_008_dd_accel_63d(close).rolling(252).rank(pct=True)

def dacc_059_dd_accel_rank_126d(close) -> pd.Series:
    return dacc_009_dd_accel_126d(close).rolling(252).rank(pct=True)

def dacc_060_dd_accel_rank_252d(close) -> pd.Series:
    return dacc_010_dd_accel_252d(close).rolling(252).rank(pct=True)

def dacc_061_dd_jerk_rank_5d(close) -> pd.Series:
    return dacc_011_dd_jerk_5d(close).rolling(252).rank(pct=True)

def dacc_062_dd_jerk_rank_21d(close) -> pd.Series:
    return dacc_012_dd_jerk_21d(close).rolling(252).rank(pct=True)

def dacc_063_dd_jerk_rank_63d(close) -> pd.Series:
    return dacc_013_dd_jerk_63d(close).rolling(252).rank(pct=True)

def dacc_064_dd_jerk_rank_126d(close) -> pd.Series:
    return dacc_014_dd_jerk_126d(close).rolling(252).rank(pct=True)

def dacc_065_dd_jerk_rank_252d(close) -> pd.Series:
    return dacc_015_dd_jerk_252d(close).rolling(252).rank(pct=True)

def dacc_066_underwater_velocity_rank_5d(close) -> pd.Series:
    return dacc_016_underwater_velocity_5d(close).rolling(252).rank(pct=True)

def dacc_067_underwater_velocity_rank_21d(close) -> pd.Series:
    return dacc_017_underwater_velocity_21d(close).rolling(252).rank(pct=True)

def dacc_068_underwater_velocity_rank_63d(close) -> pd.Series:
    return dacc_018_underwater_velocity_63d(close).rolling(252).rank(pct=True)

def dacc_069_underwater_velocity_rank_126d(close) -> pd.Series:
    return dacc_019_underwater_velocity_126d(close).rolling(252).rank(pct=True)

def dacc_070_underwater_velocity_rank_252d(close) -> pd.Series:
    return dacc_020_underwater_velocity_252d(close).rolling(252).rank(pct=True)

def dacc_071_recovery_velocity_rank_5d(close) -> pd.Series:
    return dacc_021_recovery_velocity_5d(close).rolling(252).rank(pct=True)

def dacc_072_recovery_velocity_rank_21d(close) -> pd.Series:
    return dacc_022_recovery_velocity_21d(close).rolling(252).rank(pct=True)

def dacc_073_recovery_velocity_rank_63d(close) -> pd.Series:
    return dacc_023_recovery_velocity_63d(close).rolling(252).rank(pct=True)

def dacc_074_recovery_velocity_rank_126d(close) -> pd.Series:
    return dacc_024_recovery_velocity_126d(close).rolling(252).rank(pct=True)

def dacc_075_recovery_velocity_rank_252d(close) -> pd.Series:
    return dacc_025_recovery_velocity_252d(close).rolling(252).rank(pct=True)


# --- Registry ---
V13_REGISTRY = {
    "dacc_001_dd_vel_5d": {"inputs": ['close'], "func": dacc_001_dd_vel_5d},
    "dacc_002_dd_vel_21d": {"inputs": ['close'], "func": dacc_002_dd_vel_21d},
    "dacc_003_dd_vel_63d": {"inputs": ['close'], "func": dacc_003_dd_vel_63d},
    "dacc_004_dd_vel_126d": {"inputs": ['close'], "func": dacc_004_dd_vel_126d},
    "dacc_005_dd_vel_252d": {"inputs": ['close'], "func": dacc_005_dd_vel_252d},
    "dacc_006_dd_accel_5d": {"inputs": ['close'], "func": dacc_006_dd_accel_5d},
    "dacc_007_dd_accel_21d": {"inputs": ['close'], "func": dacc_007_dd_accel_21d},
    "dacc_008_dd_accel_63d": {"inputs": ['close'], "func": dacc_008_dd_accel_63d},
    "dacc_009_dd_accel_126d": {"inputs": ['close'], "func": dacc_009_dd_accel_126d},
    "dacc_010_dd_accel_252d": {"inputs": ['close'], "func": dacc_010_dd_accel_252d},
    "dacc_011_dd_jerk_5d": {"inputs": ['close'], "func": dacc_011_dd_jerk_5d},
    "dacc_012_dd_jerk_21d": {"inputs": ['close'], "func": dacc_012_dd_jerk_21d},
    "dacc_013_dd_jerk_63d": {"inputs": ['close'], "func": dacc_013_dd_jerk_63d},
    "dacc_014_dd_jerk_126d": {"inputs": ['close'], "func": dacc_014_dd_jerk_126d},
    "dacc_015_dd_jerk_252d": {"inputs": ['close'], "func": dacc_015_dd_jerk_252d},
    "dacc_016_underwater_velocity_5d": {"inputs": ['close'], "func": dacc_016_underwater_velocity_5d},
    "dacc_017_underwater_velocity_21d": {"inputs": ['close'], "func": dacc_017_underwater_velocity_21d},
    "dacc_018_underwater_velocity_63d": {"inputs": ['close'], "func": dacc_018_underwater_velocity_63d},
    "dacc_019_underwater_velocity_126d": {"inputs": ['close'], "func": dacc_019_underwater_velocity_126d},
    "dacc_020_underwater_velocity_252d": {"inputs": ['close'], "func": dacc_020_underwater_velocity_252d},
    "dacc_021_recovery_velocity_5d": {"inputs": ['close'], "func": dacc_021_recovery_velocity_5d},
    "dacc_022_recovery_velocity_21d": {"inputs": ['close'], "func": dacc_022_recovery_velocity_21d},
    "dacc_023_recovery_velocity_63d": {"inputs": ['close'], "func": dacc_023_recovery_velocity_63d},
    "dacc_024_recovery_velocity_126d": {"inputs": ['close'], "func": dacc_024_recovery_velocity_126d},
    "dacc_025_recovery_velocity_252d": {"inputs": ['close'], "func": dacc_025_recovery_velocity_252d},
    "dacc_026_dd_vel_zscore_5d": {"inputs": ['close'], "func": dacc_026_dd_vel_zscore_5d},
    "dacc_027_dd_vel_zscore_21d": {"inputs": ['close'], "func": dacc_027_dd_vel_zscore_21d},
    "dacc_028_dd_vel_zscore_63d": {"inputs": ['close'], "func": dacc_028_dd_vel_zscore_63d},
    "dacc_029_dd_vel_zscore_126d": {"inputs": ['close'], "func": dacc_029_dd_vel_zscore_126d},
    "dacc_030_dd_vel_zscore_252d": {"inputs": ['close'], "func": dacc_030_dd_vel_zscore_252d},
    "dacc_031_dd_accel_zscore_5d": {"inputs": ['close'], "func": dacc_031_dd_accel_zscore_5d},
    "dacc_032_dd_accel_zscore_21d": {"inputs": ['close'], "func": dacc_032_dd_accel_zscore_21d},
    "dacc_033_dd_accel_zscore_63d": {"inputs": ['close'], "func": dacc_033_dd_accel_zscore_63d},
    "dacc_034_dd_accel_zscore_126d": {"inputs": ['close'], "func": dacc_034_dd_accel_zscore_126d},
    "dacc_035_dd_accel_zscore_252d": {"inputs": ['close'], "func": dacc_035_dd_accel_zscore_252d},
    "dacc_036_dd_jerk_zscore_5d": {"inputs": ['close'], "func": dacc_036_dd_jerk_zscore_5d},
    "dacc_037_dd_jerk_zscore_21d": {"inputs": ['close'], "func": dacc_037_dd_jerk_zscore_21d},
    "dacc_038_dd_jerk_zscore_63d": {"inputs": ['close'], "func": dacc_038_dd_jerk_zscore_63d},
    "dacc_039_dd_jerk_zscore_126d": {"inputs": ['close'], "func": dacc_039_dd_jerk_zscore_126d},
    "dacc_040_dd_jerk_zscore_252d": {"inputs": ['close'], "func": dacc_040_dd_jerk_zscore_252d},
    "dacc_041_underwater_velocity_zscore_5d": {"inputs": ['close'], "func": dacc_041_underwater_velocity_zscore_5d},
    "dacc_042_underwater_velocity_zscore_21d": {"inputs": ['close'], "func": dacc_042_underwater_velocity_zscore_21d},
    "dacc_043_underwater_velocity_zscore_63d": {"inputs": ['close'], "func": dacc_043_underwater_velocity_zscore_63d},
    "dacc_044_underwater_velocity_zscore_126d": {"inputs": ['close'], "func": dacc_044_underwater_velocity_zscore_126d},
    "dacc_045_underwater_velocity_zscore_252d": {"inputs": ['close'], "func": dacc_045_underwater_velocity_zscore_252d},
    "dacc_046_recovery_velocity_zscore_5d": {"inputs": ['close'], "func": dacc_046_recovery_velocity_zscore_5d},
    "dacc_047_recovery_velocity_zscore_21d": {"inputs": ['close'], "func": dacc_047_recovery_velocity_zscore_21d},
    "dacc_048_recovery_velocity_zscore_63d": {"inputs": ['close'], "func": dacc_048_recovery_velocity_zscore_63d},
    "dacc_049_recovery_velocity_zscore_126d": {"inputs": ['close'], "func": dacc_049_recovery_velocity_zscore_126d},
    "dacc_050_recovery_velocity_zscore_252d": {"inputs": ['close'], "func": dacc_050_recovery_velocity_zscore_252d},
    "dacc_051_dd_vel_rank_5d": {"inputs": ['close'], "func": dacc_051_dd_vel_rank_5d},
    "dacc_052_dd_vel_rank_21d": {"inputs": ['close'], "func": dacc_052_dd_vel_rank_21d},
    "dacc_053_dd_vel_rank_63d": {"inputs": ['close'], "func": dacc_053_dd_vel_rank_63d},
    "dacc_054_dd_vel_rank_126d": {"inputs": ['close'], "func": dacc_054_dd_vel_rank_126d},
    "dacc_055_dd_vel_rank_252d": {"inputs": ['close'], "func": dacc_055_dd_vel_rank_252d},
    "dacc_056_dd_accel_rank_5d": {"inputs": ['close'], "func": dacc_056_dd_accel_rank_5d},
    "dacc_057_dd_accel_rank_21d": {"inputs": ['close'], "func": dacc_057_dd_accel_rank_21d},
    "dacc_058_dd_accel_rank_63d": {"inputs": ['close'], "func": dacc_058_dd_accel_rank_63d},
    "dacc_059_dd_accel_rank_126d": {"inputs": ['close'], "func": dacc_059_dd_accel_rank_126d},
    "dacc_060_dd_accel_rank_252d": {"inputs": ['close'], "func": dacc_060_dd_accel_rank_252d},
    "dacc_061_dd_jerk_rank_5d": {"inputs": ['close'], "func": dacc_061_dd_jerk_rank_5d},
    "dacc_062_dd_jerk_rank_21d": {"inputs": ['close'], "func": dacc_062_dd_jerk_rank_21d},
    "dacc_063_dd_jerk_rank_63d": {"inputs": ['close'], "func": dacc_063_dd_jerk_rank_63d},
    "dacc_064_dd_jerk_rank_126d": {"inputs": ['close'], "func": dacc_064_dd_jerk_rank_126d},
    "dacc_065_dd_jerk_rank_252d": {"inputs": ['close'], "func": dacc_065_dd_jerk_rank_252d},
    "dacc_066_underwater_velocity_rank_5d": {"inputs": ['close'], "func": dacc_066_underwater_velocity_rank_5d},
    "dacc_067_underwater_velocity_rank_21d": {"inputs": ['close'], "func": dacc_067_underwater_velocity_rank_21d},
    "dacc_068_underwater_velocity_rank_63d": {"inputs": ['close'], "func": dacc_068_underwater_velocity_rank_63d},
    "dacc_069_underwater_velocity_rank_126d": {"inputs": ['close'], "func": dacc_069_underwater_velocity_rank_126d},
    "dacc_070_underwater_velocity_rank_252d": {"inputs": ['close'], "func": dacc_070_underwater_velocity_rank_252d},
    "dacc_071_recovery_velocity_rank_5d": {"inputs": ['close'], "func": dacc_071_recovery_velocity_rank_5d},
    "dacc_072_recovery_velocity_rank_21d": {"inputs": ['close'], "func": dacc_072_recovery_velocity_rank_21d},
    "dacc_073_recovery_velocity_rank_63d": {"inputs": ['close'], "func": dacc_073_recovery_velocity_rank_63d},
    "dacc_074_recovery_velocity_rank_126d": {"inputs": ['close'], "func": dacc_074_recovery_velocity_rank_126d},
    "dacc_075_recovery_velocity_rank_252d": {"inputs": ['close'], "func": dacc_075_recovery_velocity_rank_252d},
}
