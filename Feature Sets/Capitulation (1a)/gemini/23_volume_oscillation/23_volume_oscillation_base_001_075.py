"""
Domain 23: volume_oscillation (vosc_)
Asset Class: US Equities
Target Context: Oscillation patterns in volume.
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
def vosc_001_vosc_value_5d(volume) -> pd.Series:
    return (_rolling_mean(volume, 5) - _rolling_mean(volume, 5*4)) / _rolling_mean(volume, 5*4)

def vosc_002_vosc_value_21d(volume) -> pd.Series:
    return (_rolling_mean(volume, 21) - _rolling_mean(volume, 21*4)) / _rolling_mean(volume, 21*4)

def vosc_003_vosc_value_63d(volume) -> pd.Series:
    return (_rolling_mean(volume, 63) - _rolling_mean(volume, 63*4)) / _rolling_mean(volume, 63*4)

def vosc_004_vosc_value_126d(volume) -> pd.Series:
    return (_rolling_mean(volume, 126) - _rolling_mean(volume, 126*4)) / _rolling_mean(volume, 126*4)

def vosc_005_vosc_value_252d(volume) -> pd.Series:
    return (_rolling_mean(volume, 252) - _rolling_mean(volume, 252*4)) / _rolling_mean(volume, 252*4)

def vosc_006_vosc_slope_5d(volume) -> pd.Series:
    return ((_rolling_mean(volume, 5) - _rolling_mean(volume, 5*4)) / _rolling_mean(volume, 5*4)).diff()

def vosc_007_vosc_slope_21d(volume) -> pd.Series:
    return ((_rolling_mean(volume, 21) - _rolling_mean(volume, 21*4)) / _rolling_mean(volume, 21*4)).diff()

def vosc_008_vosc_slope_63d(volume) -> pd.Series:
    return ((_rolling_mean(volume, 63) - _rolling_mean(volume, 63*4)) / _rolling_mean(volume, 63*4)).diff()

def vosc_009_vosc_slope_126d(volume) -> pd.Series:
    return ((_rolling_mean(volume, 126) - _rolling_mean(volume, 126*4)) / _rolling_mean(volume, 126*4)).diff()

def vosc_010_vosc_slope_252d(volume) -> pd.Series:
    return ((_rolling_mean(volume, 252) - _rolling_mean(volume, 252*4)) / _rolling_mean(volume, 252*4)).diff()

def vosc_011_vosc_extremity_5d(volume) -> pd.Series:
    return _zscore_rolling(_rolling_mean(volume, 5) - _rolling_mean(volume, 5*4), 252)

def vosc_012_vosc_extremity_21d(volume) -> pd.Series:
    return _zscore_rolling(_rolling_mean(volume, 21) - _rolling_mean(volume, 21*4), 252)

def vosc_013_vosc_extremity_63d(volume) -> pd.Series:
    return _zscore_rolling(_rolling_mean(volume, 63) - _rolling_mean(volume, 63*4), 252)

def vosc_014_vosc_extremity_126d(volume) -> pd.Series:
    return _zscore_rolling(_rolling_mean(volume, 126) - _rolling_mean(volume, 126*4), 252)

def vosc_015_vosc_extremity_252d(volume) -> pd.Series:
    return _zscore_rolling(_rolling_mean(volume, 252) - _rolling_mean(volume, 252*4), 252)

def vosc_016_vosc_cycle_5d(volume) -> pd.Series:
    return (np.sign((_rolling_mean(volume, 5) - _rolling_mean(volume, 5*4)).diff()) != np.sign((_rolling_mean(volume, 5) - _rolling_mean(volume, 5*4)).diff().shift(1))).astype(float).rolling(5).sum()

def vosc_017_vosc_cycle_21d(volume) -> pd.Series:
    return (np.sign((_rolling_mean(volume, 21) - _rolling_mean(volume, 21*4)).diff()) != np.sign((_rolling_mean(volume, 21) - _rolling_mean(volume, 21*4)).diff().shift(1))).astype(float).rolling(21).sum()

def vosc_018_vosc_cycle_63d(volume) -> pd.Series:
    return (np.sign((_rolling_mean(volume, 63) - _rolling_mean(volume, 63*4)).diff()) != np.sign((_rolling_mean(volume, 63) - _rolling_mean(volume, 63*4)).diff().shift(1))).astype(float).rolling(63).sum()

def vosc_019_vosc_cycle_126d(volume) -> pd.Series:
    return (np.sign((_rolling_mean(volume, 126) - _rolling_mean(volume, 126*4)).diff()) != np.sign((_rolling_mean(volume, 126) - _rolling_mean(volume, 126*4)).diff().shift(1))).astype(float).rolling(126).sum()

def vosc_020_vosc_cycle_252d(volume) -> pd.Series:
    return (np.sign((_rolling_mean(volume, 252) - _rolling_mean(volume, 252*4)).diff()) != np.sign((_rolling_mean(volume, 252) - _rolling_mean(volume, 252*4)).diff().shift(1))).astype(float).rolling(252).sum()

def vosc_021_vosc_range_5d(volume) -> pd.Series:
    return _rolling_max(_rolling_mean(volume, 5), 5) - _rolling_min(_rolling_mean(volume, 5), 5)

def vosc_022_vosc_range_21d(volume) -> pd.Series:
    return _rolling_max(_rolling_mean(volume, 21), 21) - _rolling_min(_rolling_mean(volume, 21), 21)

def vosc_023_vosc_range_63d(volume) -> pd.Series:
    return _rolling_max(_rolling_mean(volume, 63), 63) - _rolling_min(_rolling_mean(volume, 63), 63)

def vosc_024_vosc_range_126d(volume) -> pd.Series:
    return _rolling_max(_rolling_mean(volume, 126), 126) - _rolling_min(_rolling_mean(volume, 126), 126)

def vosc_025_vosc_range_252d(volume) -> pd.Series:
    return _rolling_max(_rolling_mean(volume, 252), 252) - _rolling_min(_rolling_mean(volume, 252), 252)

def vosc_026_vosc_value_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vosc_001_vosc_value_5d(volume), 252)

def vosc_027_vosc_value_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vosc_002_vosc_value_21d(volume), 252)

def vosc_028_vosc_value_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vosc_003_vosc_value_63d(volume), 252)

def vosc_029_vosc_value_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vosc_004_vosc_value_126d(volume), 252)

def vosc_030_vosc_value_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vosc_005_vosc_value_252d(volume), 252)

def vosc_031_vosc_slope_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vosc_006_vosc_slope_5d(volume), 252)

def vosc_032_vosc_slope_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vosc_007_vosc_slope_21d(volume), 252)

def vosc_033_vosc_slope_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vosc_008_vosc_slope_63d(volume), 252)

def vosc_034_vosc_slope_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vosc_009_vosc_slope_126d(volume), 252)

def vosc_035_vosc_slope_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vosc_010_vosc_slope_252d(volume), 252)

def vosc_036_vosc_extremity_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vosc_011_vosc_extremity_5d(volume), 252)

def vosc_037_vosc_extremity_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vosc_012_vosc_extremity_21d(volume), 252)

def vosc_038_vosc_extremity_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vosc_013_vosc_extremity_63d(volume), 252)

def vosc_039_vosc_extremity_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vosc_014_vosc_extremity_126d(volume), 252)

def vosc_040_vosc_extremity_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vosc_015_vosc_extremity_252d(volume), 252)

def vosc_041_vosc_cycle_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vosc_016_vosc_cycle_5d(volume), 252)

def vosc_042_vosc_cycle_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vosc_017_vosc_cycle_21d(volume), 252)

def vosc_043_vosc_cycle_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vosc_018_vosc_cycle_63d(volume), 252)

def vosc_044_vosc_cycle_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vosc_019_vosc_cycle_126d(volume), 252)

def vosc_045_vosc_cycle_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vosc_020_vosc_cycle_252d(volume), 252)

def vosc_046_vosc_range_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vosc_021_vosc_range_5d(volume), 252)

def vosc_047_vosc_range_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vosc_022_vosc_range_21d(volume), 252)

def vosc_048_vosc_range_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vosc_023_vosc_range_63d(volume), 252)

def vosc_049_vosc_range_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vosc_024_vosc_range_126d(volume), 252)

def vosc_050_vosc_range_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vosc_025_vosc_range_252d(volume), 252)

def vosc_051_vosc_value_rank_5d(volume) -> pd.Series:
    return vosc_001_vosc_value_5d(volume).rolling(252).rank(pct=True)

def vosc_052_vosc_value_rank_21d(volume) -> pd.Series:
    return vosc_002_vosc_value_21d(volume).rolling(252).rank(pct=True)

def vosc_053_vosc_value_rank_63d(volume) -> pd.Series:
    return vosc_003_vosc_value_63d(volume).rolling(252).rank(pct=True)

def vosc_054_vosc_value_rank_126d(volume) -> pd.Series:
    return vosc_004_vosc_value_126d(volume).rolling(252).rank(pct=True)

def vosc_055_vosc_value_rank_252d(volume) -> pd.Series:
    return vosc_005_vosc_value_252d(volume).rolling(252).rank(pct=True)

def vosc_056_vosc_slope_rank_5d(volume) -> pd.Series:
    return vosc_006_vosc_slope_5d(volume).rolling(252).rank(pct=True)

def vosc_057_vosc_slope_rank_21d(volume) -> pd.Series:
    return vosc_007_vosc_slope_21d(volume).rolling(252).rank(pct=True)

def vosc_058_vosc_slope_rank_63d(volume) -> pd.Series:
    return vosc_008_vosc_slope_63d(volume).rolling(252).rank(pct=True)

def vosc_059_vosc_slope_rank_126d(volume) -> pd.Series:
    return vosc_009_vosc_slope_126d(volume).rolling(252).rank(pct=True)

def vosc_060_vosc_slope_rank_252d(volume) -> pd.Series:
    return vosc_010_vosc_slope_252d(volume).rolling(252).rank(pct=True)

def vosc_061_vosc_extremity_rank_5d(volume) -> pd.Series:
    return vosc_011_vosc_extremity_5d(volume).rolling(252).rank(pct=True)

def vosc_062_vosc_extremity_rank_21d(volume) -> pd.Series:
    return vosc_012_vosc_extremity_21d(volume).rolling(252).rank(pct=True)

def vosc_063_vosc_extremity_rank_63d(volume) -> pd.Series:
    return vosc_013_vosc_extremity_63d(volume).rolling(252).rank(pct=True)

def vosc_064_vosc_extremity_rank_126d(volume) -> pd.Series:
    return vosc_014_vosc_extremity_126d(volume).rolling(252).rank(pct=True)

def vosc_065_vosc_extremity_rank_252d(volume) -> pd.Series:
    return vosc_015_vosc_extremity_252d(volume).rolling(252).rank(pct=True)

def vosc_066_vosc_cycle_rank_5d(volume) -> pd.Series:
    return vosc_016_vosc_cycle_5d(volume).rolling(252).rank(pct=True)

def vosc_067_vosc_cycle_rank_21d(volume) -> pd.Series:
    return vosc_017_vosc_cycle_21d(volume).rolling(252).rank(pct=True)

def vosc_068_vosc_cycle_rank_63d(volume) -> pd.Series:
    return vosc_018_vosc_cycle_63d(volume).rolling(252).rank(pct=True)

def vosc_069_vosc_cycle_rank_126d(volume) -> pd.Series:
    return vosc_019_vosc_cycle_126d(volume).rolling(252).rank(pct=True)

def vosc_070_vosc_cycle_rank_252d(volume) -> pd.Series:
    return vosc_020_vosc_cycle_252d(volume).rolling(252).rank(pct=True)

def vosc_071_vosc_range_rank_5d(volume) -> pd.Series:
    return vosc_021_vosc_range_5d(volume).rolling(252).rank(pct=True)

def vosc_072_vosc_range_rank_21d(volume) -> pd.Series:
    return vosc_022_vosc_range_21d(volume).rolling(252).rank(pct=True)

def vosc_073_vosc_range_rank_63d(volume) -> pd.Series:
    return vosc_023_vosc_range_63d(volume).rolling(252).rank(pct=True)

def vosc_074_vosc_range_rank_126d(volume) -> pd.Series:
    return vosc_024_vosc_range_126d(volume).rolling(252).rank(pct=True)

def vosc_075_vosc_range_rank_252d(volume) -> pd.Series:
    return vosc_025_vosc_range_252d(volume).rolling(252).rank(pct=True)


# --- Registry ---
V23_REGISTRY = {
    "vosc_001_vosc_value_5d": {"inputs": ['volume'], "func": vosc_001_vosc_value_5d},
    "vosc_002_vosc_value_21d": {"inputs": ['volume'], "func": vosc_002_vosc_value_21d},
    "vosc_003_vosc_value_63d": {"inputs": ['volume'], "func": vosc_003_vosc_value_63d},
    "vosc_004_vosc_value_126d": {"inputs": ['volume'], "func": vosc_004_vosc_value_126d},
    "vosc_005_vosc_value_252d": {"inputs": ['volume'], "func": vosc_005_vosc_value_252d},
    "vosc_006_vosc_slope_5d": {"inputs": ['volume'], "func": vosc_006_vosc_slope_5d},
    "vosc_007_vosc_slope_21d": {"inputs": ['volume'], "func": vosc_007_vosc_slope_21d},
    "vosc_008_vosc_slope_63d": {"inputs": ['volume'], "func": vosc_008_vosc_slope_63d},
    "vosc_009_vosc_slope_126d": {"inputs": ['volume'], "func": vosc_009_vosc_slope_126d},
    "vosc_010_vosc_slope_252d": {"inputs": ['volume'], "func": vosc_010_vosc_slope_252d},
    "vosc_011_vosc_extremity_5d": {"inputs": ['volume'], "func": vosc_011_vosc_extremity_5d},
    "vosc_012_vosc_extremity_21d": {"inputs": ['volume'], "func": vosc_012_vosc_extremity_21d},
    "vosc_013_vosc_extremity_63d": {"inputs": ['volume'], "func": vosc_013_vosc_extremity_63d},
    "vosc_014_vosc_extremity_126d": {"inputs": ['volume'], "func": vosc_014_vosc_extremity_126d},
    "vosc_015_vosc_extremity_252d": {"inputs": ['volume'], "func": vosc_015_vosc_extremity_252d},
    "vosc_016_vosc_cycle_5d": {"inputs": ['volume'], "func": vosc_016_vosc_cycle_5d},
    "vosc_017_vosc_cycle_21d": {"inputs": ['volume'], "func": vosc_017_vosc_cycle_21d},
    "vosc_018_vosc_cycle_63d": {"inputs": ['volume'], "func": vosc_018_vosc_cycle_63d},
    "vosc_019_vosc_cycle_126d": {"inputs": ['volume'], "func": vosc_019_vosc_cycle_126d},
    "vosc_020_vosc_cycle_252d": {"inputs": ['volume'], "func": vosc_020_vosc_cycle_252d},
    "vosc_021_vosc_range_5d": {"inputs": ['volume'], "func": vosc_021_vosc_range_5d},
    "vosc_022_vosc_range_21d": {"inputs": ['volume'], "func": vosc_022_vosc_range_21d},
    "vosc_023_vosc_range_63d": {"inputs": ['volume'], "func": vosc_023_vosc_range_63d},
    "vosc_024_vosc_range_126d": {"inputs": ['volume'], "func": vosc_024_vosc_range_126d},
    "vosc_025_vosc_range_252d": {"inputs": ['volume'], "func": vosc_025_vosc_range_252d},
    "vosc_026_vosc_value_zscore_5d": {"inputs": ['volume'], "func": vosc_026_vosc_value_zscore_5d},
    "vosc_027_vosc_value_zscore_21d": {"inputs": ['volume'], "func": vosc_027_vosc_value_zscore_21d},
    "vosc_028_vosc_value_zscore_63d": {"inputs": ['volume'], "func": vosc_028_vosc_value_zscore_63d},
    "vosc_029_vosc_value_zscore_126d": {"inputs": ['volume'], "func": vosc_029_vosc_value_zscore_126d},
    "vosc_030_vosc_value_zscore_252d": {"inputs": ['volume'], "func": vosc_030_vosc_value_zscore_252d},
    "vosc_031_vosc_slope_zscore_5d": {"inputs": ['volume'], "func": vosc_031_vosc_slope_zscore_5d},
    "vosc_032_vosc_slope_zscore_21d": {"inputs": ['volume'], "func": vosc_032_vosc_slope_zscore_21d},
    "vosc_033_vosc_slope_zscore_63d": {"inputs": ['volume'], "func": vosc_033_vosc_slope_zscore_63d},
    "vosc_034_vosc_slope_zscore_126d": {"inputs": ['volume'], "func": vosc_034_vosc_slope_zscore_126d},
    "vosc_035_vosc_slope_zscore_252d": {"inputs": ['volume'], "func": vosc_035_vosc_slope_zscore_252d},
    "vosc_036_vosc_extremity_zscore_5d": {"inputs": ['volume'], "func": vosc_036_vosc_extremity_zscore_5d},
    "vosc_037_vosc_extremity_zscore_21d": {"inputs": ['volume'], "func": vosc_037_vosc_extremity_zscore_21d},
    "vosc_038_vosc_extremity_zscore_63d": {"inputs": ['volume'], "func": vosc_038_vosc_extremity_zscore_63d},
    "vosc_039_vosc_extremity_zscore_126d": {"inputs": ['volume'], "func": vosc_039_vosc_extremity_zscore_126d},
    "vosc_040_vosc_extremity_zscore_252d": {"inputs": ['volume'], "func": vosc_040_vosc_extremity_zscore_252d},
    "vosc_041_vosc_cycle_zscore_5d": {"inputs": ['volume'], "func": vosc_041_vosc_cycle_zscore_5d},
    "vosc_042_vosc_cycle_zscore_21d": {"inputs": ['volume'], "func": vosc_042_vosc_cycle_zscore_21d},
    "vosc_043_vosc_cycle_zscore_63d": {"inputs": ['volume'], "func": vosc_043_vosc_cycle_zscore_63d},
    "vosc_044_vosc_cycle_zscore_126d": {"inputs": ['volume'], "func": vosc_044_vosc_cycle_zscore_126d},
    "vosc_045_vosc_cycle_zscore_252d": {"inputs": ['volume'], "func": vosc_045_vosc_cycle_zscore_252d},
    "vosc_046_vosc_range_zscore_5d": {"inputs": ['volume'], "func": vosc_046_vosc_range_zscore_5d},
    "vosc_047_vosc_range_zscore_21d": {"inputs": ['volume'], "func": vosc_047_vosc_range_zscore_21d},
    "vosc_048_vosc_range_zscore_63d": {"inputs": ['volume'], "func": vosc_048_vosc_range_zscore_63d},
    "vosc_049_vosc_range_zscore_126d": {"inputs": ['volume'], "func": vosc_049_vosc_range_zscore_126d},
    "vosc_050_vosc_range_zscore_252d": {"inputs": ['volume'], "func": vosc_050_vosc_range_zscore_252d},
    "vosc_051_vosc_value_rank_5d": {"inputs": ['volume'], "func": vosc_051_vosc_value_rank_5d},
    "vosc_052_vosc_value_rank_21d": {"inputs": ['volume'], "func": vosc_052_vosc_value_rank_21d},
    "vosc_053_vosc_value_rank_63d": {"inputs": ['volume'], "func": vosc_053_vosc_value_rank_63d},
    "vosc_054_vosc_value_rank_126d": {"inputs": ['volume'], "func": vosc_054_vosc_value_rank_126d},
    "vosc_055_vosc_value_rank_252d": {"inputs": ['volume'], "func": vosc_055_vosc_value_rank_252d},
    "vosc_056_vosc_slope_rank_5d": {"inputs": ['volume'], "func": vosc_056_vosc_slope_rank_5d},
    "vosc_057_vosc_slope_rank_21d": {"inputs": ['volume'], "func": vosc_057_vosc_slope_rank_21d},
    "vosc_058_vosc_slope_rank_63d": {"inputs": ['volume'], "func": vosc_058_vosc_slope_rank_63d},
    "vosc_059_vosc_slope_rank_126d": {"inputs": ['volume'], "func": vosc_059_vosc_slope_rank_126d},
    "vosc_060_vosc_slope_rank_252d": {"inputs": ['volume'], "func": vosc_060_vosc_slope_rank_252d},
    "vosc_061_vosc_extremity_rank_5d": {"inputs": ['volume'], "func": vosc_061_vosc_extremity_rank_5d},
    "vosc_062_vosc_extremity_rank_21d": {"inputs": ['volume'], "func": vosc_062_vosc_extremity_rank_21d},
    "vosc_063_vosc_extremity_rank_63d": {"inputs": ['volume'], "func": vosc_063_vosc_extremity_rank_63d},
    "vosc_064_vosc_extremity_rank_126d": {"inputs": ['volume'], "func": vosc_064_vosc_extremity_rank_126d},
    "vosc_065_vosc_extremity_rank_252d": {"inputs": ['volume'], "func": vosc_065_vosc_extremity_rank_252d},
    "vosc_066_vosc_cycle_rank_5d": {"inputs": ['volume'], "func": vosc_066_vosc_cycle_rank_5d},
    "vosc_067_vosc_cycle_rank_21d": {"inputs": ['volume'], "func": vosc_067_vosc_cycle_rank_21d},
    "vosc_068_vosc_cycle_rank_63d": {"inputs": ['volume'], "func": vosc_068_vosc_cycle_rank_63d},
    "vosc_069_vosc_cycle_rank_126d": {"inputs": ['volume'], "func": vosc_069_vosc_cycle_rank_126d},
    "vosc_070_vosc_cycle_rank_252d": {"inputs": ['volume'], "func": vosc_070_vosc_cycle_rank_252d},
    "vosc_071_vosc_range_rank_5d": {"inputs": ['volume'], "func": vosc_071_vosc_range_rank_5d},
    "vosc_072_vosc_range_rank_21d": {"inputs": ['volume'], "func": vosc_072_vosc_range_rank_21d},
    "vosc_073_vosc_range_rank_63d": {"inputs": ['volume'], "func": vosc_073_vosc_range_rank_63d},
    "vosc_074_vosc_range_rank_126d": {"inputs": ['volume'], "func": vosc_074_vosc_range_rank_126d},
    "vosc_075_vosc_range_rank_252d": {"inputs": ['volume'], "func": vosc_075_vosc_range_rank_252d},
}
