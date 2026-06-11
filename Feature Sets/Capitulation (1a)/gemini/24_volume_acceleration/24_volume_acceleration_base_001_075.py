"""
Domain 24: volume_acceleration (vacc_)
Asset Class: US Equities
Target Context: Acceleration and momentum of volume surges.
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
def vacc_001_vol_accel_5d(volume) -> pd.Series:
    return volume.diff().diff().rolling(5).mean()

def vacc_002_vol_accel_21d(volume) -> pd.Series:
    return volume.diff().diff().rolling(21).mean()

def vacc_003_vol_accel_63d(volume) -> pd.Series:
    return volume.diff().diff().rolling(63).mean()

def vacc_004_vol_accel_126d(volume) -> pd.Series:
    return volume.diff().diff().rolling(126).mean()

def vacc_005_vol_accel_252d(volume) -> pd.Series:
    return volume.diff().diff().rolling(252).mean()

def vacc_006_vol_jerk_5d(volume) -> pd.Series:
    return volume.diff().diff().diff().rolling(5).mean()

def vacc_007_vol_jerk_21d(volume) -> pd.Series:
    return volume.diff().diff().diff().rolling(21).mean()

def vacc_008_vol_jerk_63d(volume) -> pd.Series:
    return volume.diff().diff().diff().rolling(63).mean()

def vacc_009_vol_jerk_126d(volume) -> pd.Series:
    return volume.diff().diff().diff().rolling(126).mean()

def vacc_010_vol_jerk_252d(volume) -> pd.Series:
    return volume.diff().diff().diff().rolling(252).mean()

def vacc_011_vol_mom_5d(volume) -> pd.Series:
    return volume.pct_change(5)

def vacc_012_vol_mom_21d(volume) -> pd.Series:
    return volume.pct_change(21)

def vacc_013_vol_mom_63d(volume) -> pd.Series:
    return volume.pct_change(63)

def vacc_014_vol_mom_126d(volume) -> pd.Series:
    return volume.pct_change(126)

def vacc_015_vol_mom_252d(volume) -> pd.Series:
    return volume.pct_change(252)

def vacc_016_surge_intensity_5d(volume) -> pd.Series:
    return _safe_div(volume, volume.rolling(5).mean())

def vacc_017_surge_intensity_21d(volume) -> pd.Series:
    return _safe_div(volume, volume.rolling(21).mean())

def vacc_018_surge_intensity_63d(volume) -> pd.Series:
    return _safe_div(volume, volume.rolling(63).mean())

def vacc_019_surge_intensity_126d(volume) -> pd.Series:
    return _safe_div(volume, volume.rolling(126).mean())

def vacc_020_surge_intensity_252d(volume) -> pd.Series:
    return _safe_div(volume, volume.rolling(252).mean())

def vacc_021_vol_velocity_5d(volume) -> pd.Series:
    return volume.diff().rolling(5).mean()

def vacc_022_vol_velocity_21d(volume) -> pd.Series:
    return volume.diff().rolling(21).mean()

def vacc_023_vol_velocity_63d(volume) -> pd.Series:
    return volume.diff().rolling(63).mean()

def vacc_024_vol_velocity_126d(volume) -> pd.Series:
    return volume.diff().rolling(126).mean()

def vacc_025_vol_velocity_252d(volume) -> pd.Series:
    return volume.diff().rolling(252).mean()

def vacc_026_vol_accel_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vacc_001_vol_accel_5d(volume), 252)

def vacc_027_vol_accel_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vacc_002_vol_accel_21d(volume), 252)

def vacc_028_vol_accel_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vacc_003_vol_accel_63d(volume), 252)

def vacc_029_vol_accel_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vacc_004_vol_accel_126d(volume), 252)

def vacc_030_vol_accel_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vacc_005_vol_accel_252d(volume), 252)

def vacc_031_vol_jerk_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vacc_006_vol_jerk_5d(volume), 252)

def vacc_032_vol_jerk_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vacc_007_vol_jerk_21d(volume), 252)

def vacc_033_vol_jerk_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vacc_008_vol_jerk_63d(volume), 252)

def vacc_034_vol_jerk_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vacc_009_vol_jerk_126d(volume), 252)

def vacc_035_vol_jerk_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vacc_010_vol_jerk_252d(volume), 252)

def vacc_036_vol_mom_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vacc_011_vol_mom_5d(volume), 252)

def vacc_037_vol_mom_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vacc_012_vol_mom_21d(volume), 252)

def vacc_038_vol_mom_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vacc_013_vol_mom_63d(volume), 252)

def vacc_039_vol_mom_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vacc_014_vol_mom_126d(volume), 252)

def vacc_040_vol_mom_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vacc_015_vol_mom_252d(volume), 252)

def vacc_041_surge_intensity_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vacc_016_surge_intensity_5d(volume), 252)

def vacc_042_surge_intensity_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vacc_017_surge_intensity_21d(volume), 252)

def vacc_043_surge_intensity_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vacc_018_surge_intensity_63d(volume), 252)

def vacc_044_surge_intensity_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vacc_019_surge_intensity_126d(volume), 252)

def vacc_045_surge_intensity_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vacc_020_surge_intensity_252d(volume), 252)

def vacc_046_vol_velocity_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vacc_021_vol_velocity_5d(volume), 252)

def vacc_047_vol_velocity_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vacc_022_vol_velocity_21d(volume), 252)

def vacc_048_vol_velocity_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vacc_023_vol_velocity_63d(volume), 252)

def vacc_049_vol_velocity_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vacc_024_vol_velocity_126d(volume), 252)

def vacc_050_vol_velocity_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vacc_025_vol_velocity_252d(volume), 252)

def vacc_051_vol_accel_rank_5d(volume) -> pd.Series:
    return vacc_001_vol_accel_5d(volume).rolling(252).rank(pct=True)

def vacc_052_vol_accel_rank_21d(volume) -> pd.Series:
    return vacc_002_vol_accel_21d(volume).rolling(252).rank(pct=True)

def vacc_053_vol_accel_rank_63d(volume) -> pd.Series:
    return vacc_003_vol_accel_63d(volume).rolling(252).rank(pct=True)

def vacc_054_vol_accel_rank_126d(volume) -> pd.Series:
    return vacc_004_vol_accel_126d(volume).rolling(252).rank(pct=True)

def vacc_055_vol_accel_rank_252d(volume) -> pd.Series:
    return vacc_005_vol_accel_252d(volume).rolling(252).rank(pct=True)

def vacc_056_vol_jerk_rank_5d(volume) -> pd.Series:
    return vacc_006_vol_jerk_5d(volume).rolling(252).rank(pct=True)

def vacc_057_vol_jerk_rank_21d(volume) -> pd.Series:
    return vacc_007_vol_jerk_21d(volume).rolling(252).rank(pct=True)

def vacc_058_vol_jerk_rank_63d(volume) -> pd.Series:
    return vacc_008_vol_jerk_63d(volume).rolling(252).rank(pct=True)

def vacc_059_vol_jerk_rank_126d(volume) -> pd.Series:
    return vacc_009_vol_jerk_126d(volume).rolling(252).rank(pct=True)

def vacc_060_vol_jerk_rank_252d(volume) -> pd.Series:
    return vacc_010_vol_jerk_252d(volume).rolling(252).rank(pct=True)

def vacc_061_vol_mom_rank_5d(volume) -> pd.Series:
    return vacc_011_vol_mom_5d(volume).rolling(252).rank(pct=True)

def vacc_062_vol_mom_rank_21d(volume) -> pd.Series:
    return vacc_012_vol_mom_21d(volume).rolling(252).rank(pct=True)

def vacc_063_vol_mom_rank_63d(volume) -> pd.Series:
    return vacc_013_vol_mom_63d(volume).rolling(252).rank(pct=True)

def vacc_064_vol_mom_rank_126d(volume) -> pd.Series:
    return vacc_014_vol_mom_126d(volume).rolling(252).rank(pct=True)

def vacc_065_vol_mom_rank_252d(volume) -> pd.Series:
    return vacc_015_vol_mom_252d(volume).rolling(252).rank(pct=True)

def vacc_066_surge_intensity_rank_5d(volume) -> pd.Series:
    return vacc_016_surge_intensity_5d(volume).rolling(252).rank(pct=True)

def vacc_067_surge_intensity_rank_21d(volume) -> pd.Series:
    return vacc_017_surge_intensity_21d(volume).rolling(252).rank(pct=True)

def vacc_068_surge_intensity_rank_63d(volume) -> pd.Series:
    return vacc_018_surge_intensity_63d(volume).rolling(252).rank(pct=True)

def vacc_069_surge_intensity_rank_126d(volume) -> pd.Series:
    return vacc_019_surge_intensity_126d(volume).rolling(252).rank(pct=True)

def vacc_070_surge_intensity_rank_252d(volume) -> pd.Series:
    return vacc_020_surge_intensity_252d(volume).rolling(252).rank(pct=True)

def vacc_071_vol_velocity_rank_5d(volume) -> pd.Series:
    return vacc_021_vol_velocity_5d(volume).rolling(252).rank(pct=True)

def vacc_072_vol_velocity_rank_21d(volume) -> pd.Series:
    return vacc_022_vol_velocity_21d(volume).rolling(252).rank(pct=True)

def vacc_073_vol_velocity_rank_63d(volume) -> pd.Series:
    return vacc_023_vol_velocity_63d(volume).rolling(252).rank(pct=True)

def vacc_074_vol_velocity_rank_126d(volume) -> pd.Series:
    return vacc_024_vol_velocity_126d(volume).rolling(252).rank(pct=True)

def vacc_075_vol_velocity_rank_252d(volume) -> pd.Series:
    return vacc_025_vol_velocity_252d(volume).rolling(252).rank(pct=True)


# --- Registry ---
V24_REGISTRY = {
    "vacc_001_vol_accel_5d": {"inputs": ['volume'], "func": vacc_001_vol_accel_5d},
    "vacc_002_vol_accel_21d": {"inputs": ['volume'], "func": vacc_002_vol_accel_21d},
    "vacc_003_vol_accel_63d": {"inputs": ['volume'], "func": vacc_003_vol_accel_63d},
    "vacc_004_vol_accel_126d": {"inputs": ['volume'], "func": vacc_004_vol_accel_126d},
    "vacc_005_vol_accel_252d": {"inputs": ['volume'], "func": vacc_005_vol_accel_252d},
    "vacc_006_vol_jerk_5d": {"inputs": ['volume'], "func": vacc_006_vol_jerk_5d},
    "vacc_007_vol_jerk_21d": {"inputs": ['volume'], "func": vacc_007_vol_jerk_21d},
    "vacc_008_vol_jerk_63d": {"inputs": ['volume'], "func": vacc_008_vol_jerk_63d},
    "vacc_009_vol_jerk_126d": {"inputs": ['volume'], "func": vacc_009_vol_jerk_126d},
    "vacc_010_vol_jerk_252d": {"inputs": ['volume'], "func": vacc_010_vol_jerk_252d},
    "vacc_011_vol_mom_5d": {"inputs": ['volume'], "func": vacc_011_vol_mom_5d},
    "vacc_012_vol_mom_21d": {"inputs": ['volume'], "func": vacc_012_vol_mom_21d},
    "vacc_013_vol_mom_63d": {"inputs": ['volume'], "func": vacc_013_vol_mom_63d},
    "vacc_014_vol_mom_126d": {"inputs": ['volume'], "func": vacc_014_vol_mom_126d},
    "vacc_015_vol_mom_252d": {"inputs": ['volume'], "func": vacc_015_vol_mom_252d},
    "vacc_016_surge_intensity_5d": {"inputs": ['volume'], "func": vacc_016_surge_intensity_5d},
    "vacc_017_surge_intensity_21d": {"inputs": ['volume'], "func": vacc_017_surge_intensity_21d},
    "vacc_018_surge_intensity_63d": {"inputs": ['volume'], "func": vacc_018_surge_intensity_63d},
    "vacc_019_surge_intensity_126d": {"inputs": ['volume'], "func": vacc_019_surge_intensity_126d},
    "vacc_020_surge_intensity_252d": {"inputs": ['volume'], "func": vacc_020_surge_intensity_252d},
    "vacc_021_vol_velocity_5d": {"inputs": ['volume'], "func": vacc_021_vol_velocity_5d},
    "vacc_022_vol_velocity_21d": {"inputs": ['volume'], "func": vacc_022_vol_velocity_21d},
    "vacc_023_vol_velocity_63d": {"inputs": ['volume'], "func": vacc_023_vol_velocity_63d},
    "vacc_024_vol_velocity_126d": {"inputs": ['volume'], "func": vacc_024_vol_velocity_126d},
    "vacc_025_vol_velocity_252d": {"inputs": ['volume'], "func": vacc_025_vol_velocity_252d},
    "vacc_026_vol_accel_zscore_5d": {"inputs": ['volume'], "func": vacc_026_vol_accel_zscore_5d},
    "vacc_027_vol_accel_zscore_21d": {"inputs": ['volume'], "func": vacc_027_vol_accel_zscore_21d},
    "vacc_028_vol_accel_zscore_63d": {"inputs": ['volume'], "func": vacc_028_vol_accel_zscore_63d},
    "vacc_029_vol_accel_zscore_126d": {"inputs": ['volume'], "func": vacc_029_vol_accel_zscore_126d},
    "vacc_030_vol_accel_zscore_252d": {"inputs": ['volume'], "func": vacc_030_vol_accel_zscore_252d},
    "vacc_031_vol_jerk_zscore_5d": {"inputs": ['volume'], "func": vacc_031_vol_jerk_zscore_5d},
    "vacc_032_vol_jerk_zscore_21d": {"inputs": ['volume'], "func": vacc_032_vol_jerk_zscore_21d},
    "vacc_033_vol_jerk_zscore_63d": {"inputs": ['volume'], "func": vacc_033_vol_jerk_zscore_63d},
    "vacc_034_vol_jerk_zscore_126d": {"inputs": ['volume'], "func": vacc_034_vol_jerk_zscore_126d},
    "vacc_035_vol_jerk_zscore_252d": {"inputs": ['volume'], "func": vacc_035_vol_jerk_zscore_252d},
    "vacc_036_vol_mom_zscore_5d": {"inputs": ['volume'], "func": vacc_036_vol_mom_zscore_5d},
    "vacc_037_vol_mom_zscore_21d": {"inputs": ['volume'], "func": vacc_037_vol_mom_zscore_21d},
    "vacc_038_vol_mom_zscore_63d": {"inputs": ['volume'], "func": vacc_038_vol_mom_zscore_63d},
    "vacc_039_vol_mom_zscore_126d": {"inputs": ['volume'], "func": vacc_039_vol_mom_zscore_126d},
    "vacc_040_vol_mom_zscore_252d": {"inputs": ['volume'], "func": vacc_040_vol_mom_zscore_252d},
    "vacc_041_surge_intensity_zscore_5d": {"inputs": ['volume'], "func": vacc_041_surge_intensity_zscore_5d},
    "vacc_042_surge_intensity_zscore_21d": {"inputs": ['volume'], "func": vacc_042_surge_intensity_zscore_21d},
    "vacc_043_surge_intensity_zscore_63d": {"inputs": ['volume'], "func": vacc_043_surge_intensity_zscore_63d},
    "vacc_044_surge_intensity_zscore_126d": {"inputs": ['volume'], "func": vacc_044_surge_intensity_zscore_126d},
    "vacc_045_surge_intensity_zscore_252d": {"inputs": ['volume'], "func": vacc_045_surge_intensity_zscore_252d},
    "vacc_046_vol_velocity_zscore_5d": {"inputs": ['volume'], "func": vacc_046_vol_velocity_zscore_5d},
    "vacc_047_vol_velocity_zscore_21d": {"inputs": ['volume'], "func": vacc_047_vol_velocity_zscore_21d},
    "vacc_048_vol_velocity_zscore_63d": {"inputs": ['volume'], "func": vacc_048_vol_velocity_zscore_63d},
    "vacc_049_vol_velocity_zscore_126d": {"inputs": ['volume'], "func": vacc_049_vol_velocity_zscore_126d},
    "vacc_050_vol_velocity_zscore_252d": {"inputs": ['volume'], "func": vacc_050_vol_velocity_zscore_252d},
    "vacc_051_vol_accel_rank_5d": {"inputs": ['volume'], "func": vacc_051_vol_accel_rank_5d},
    "vacc_052_vol_accel_rank_21d": {"inputs": ['volume'], "func": vacc_052_vol_accel_rank_21d},
    "vacc_053_vol_accel_rank_63d": {"inputs": ['volume'], "func": vacc_053_vol_accel_rank_63d},
    "vacc_054_vol_accel_rank_126d": {"inputs": ['volume'], "func": vacc_054_vol_accel_rank_126d},
    "vacc_055_vol_accel_rank_252d": {"inputs": ['volume'], "func": vacc_055_vol_accel_rank_252d},
    "vacc_056_vol_jerk_rank_5d": {"inputs": ['volume'], "func": vacc_056_vol_jerk_rank_5d},
    "vacc_057_vol_jerk_rank_21d": {"inputs": ['volume'], "func": vacc_057_vol_jerk_rank_21d},
    "vacc_058_vol_jerk_rank_63d": {"inputs": ['volume'], "func": vacc_058_vol_jerk_rank_63d},
    "vacc_059_vol_jerk_rank_126d": {"inputs": ['volume'], "func": vacc_059_vol_jerk_rank_126d},
    "vacc_060_vol_jerk_rank_252d": {"inputs": ['volume'], "func": vacc_060_vol_jerk_rank_252d},
    "vacc_061_vol_mom_rank_5d": {"inputs": ['volume'], "func": vacc_061_vol_mom_rank_5d},
    "vacc_062_vol_mom_rank_21d": {"inputs": ['volume'], "func": vacc_062_vol_mom_rank_21d},
    "vacc_063_vol_mom_rank_63d": {"inputs": ['volume'], "func": vacc_063_vol_mom_rank_63d},
    "vacc_064_vol_mom_rank_126d": {"inputs": ['volume'], "func": vacc_064_vol_mom_rank_126d},
    "vacc_065_vol_mom_rank_252d": {"inputs": ['volume'], "func": vacc_065_vol_mom_rank_252d},
    "vacc_066_surge_intensity_rank_5d": {"inputs": ['volume'], "func": vacc_066_surge_intensity_rank_5d},
    "vacc_067_surge_intensity_rank_21d": {"inputs": ['volume'], "func": vacc_067_surge_intensity_rank_21d},
    "vacc_068_surge_intensity_rank_63d": {"inputs": ['volume'], "func": vacc_068_surge_intensity_rank_63d},
    "vacc_069_surge_intensity_rank_126d": {"inputs": ['volume'], "func": vacc_069_surge_intensity_rank_126d},
    "vacc_070_surge_intensity_rank_252d": {"inputs": ['volume'], "func": vacc_070_surge_intensity_rank_252d},
    "vacc_071_vol_velocity_rank_5d": {"inputs": ['volume'], "func": vacc_071_vol_velocity_rank_5d},
    "vacc_072_vol_velocity_rank_21d": {"inputs": ['volume'], "func": vacc_072_vol_velocity_rank_21d},
    "vacc_073_vol_velocity_rank_63d": {"inputs": ['volume'], "func": vacc_073_vol_velocity_rank_63d},
    "vacc_074_vol_velocity_rank_126d": {"inputs": ['volume'], "func": vacc_074_vol_velocity_rank_126d},
    "vacc_075_vol_velocity_rank_252d": {"inputs": ['volume'], "func": vacc_075_vol_velocity_rank_252d},
}
