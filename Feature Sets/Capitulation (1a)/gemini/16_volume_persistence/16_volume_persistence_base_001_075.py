"""
Domain 16: volume_persistence (vper_)
Asset Class: US Equities
Target Context: Consistency and persistence of volume trends.
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
def vper_001_vol_consistency_5d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 5), _rolling_std(volume, 5))

def vper_002_vol_consistency_21d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 21), _rolling_std(volume, 21))

def vper_003_vol_consistency_63d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 63), _rolling_std(volume, 63))

def vper_004_vol_consistency_126d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 126), _rolling_std(volume, 126))

def vper_005_vol_consistency_252d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 252), _rolling_std(volume, 252))

def vper_006_vol_trend_slope_5d(volume) -> pd.Series:
    return volume.diff().rolling(5).sum()

def vper_007_vol_trend_slope_21d(volume) -> pd.Series:
    return volume.diff().rolling(21).sum()

def vper_008_vol_trend_slope_63d(volume) -> pd.Series:
    return volume.diff().rolling(63).sum()

def vper_009_vol_trend_slope_126d(volume) -> pd.Series:
    return volume.diff().rolling(126).sum()

def vper_010_vol_trend_slope_252d(volume) -> pd.Series:
    return volume.diff().rolling(252).sum()

def vper_011_vol_stability_5d(volume) -> pd.Series:
    return (1.0 / (_rolling_std(volume, 5) / _rolling_mean(volume, 5)))

def vper_012_vol_stability_21d(volume) -> pd.Series:
    return (1.0 / (_rolling_std(volume, 21) / _rolling_mean(volume, 21)))

def vper_013_vol_stability_63d(volume) -> pd.Series:
    return (1.0 / (_rolling_std(volume, 63) / _rolling_mean(volume, 63)))

def vper_014_vol_stability_126d(volume) -> pd.Series:
    return (1.0 / (_rolling_std(volume, 126) / _rolling_mean(volume, 126)))

def vper_015_vol_stability_252d(volume) -> pd.Series:
    return (1.0 / (_rolling_std(volume, 252) / _rolling_mean(volume, 252)))

def vper_016_persistence_index_5d(volume) -> pd.Series:
    return ((volume > volume.shift(1)).astype(int)).rolling(5).sum()

def vper_017_persistence_index_21d(volume) -> pd.Series:
    return ((volume > volume.shift(1)).astype(int)).rolling(21).sum()

def vper_018_persistence_index_63d(volume) -> pd.Series:
    return ((volume > volume.shift(1)).astype(int)).rolling(63).sum()

def vper_019_persistence_index_126d(volume) -> pd.Series:
    return ((volume > volume.shift(1)).astype(int)).rolling(126).sum()

def vper_020_persistence_index_252d(volume) -> pd.Series:
    return ((volume > volume.shift(1)).astype(int)).rolling(252).sum()

def vper_021_vol_ma_ratio_5d(volume) -> pd.Series:
    return _safe_div(volume, _rolling_mean(volume, 5))

def vper_022_vol_ma_ratio_21d(volume) -> pd.Series:
    return _safe_div(volume, _rolling_mean(volume, 21))

def vper_023_vol_ma_ratio_63d(volume) -> pd.Series:
    return _safe_div(volume, _rolling_mean(volume, 63))

def vper_024_vol_ma_ratio_126d(volume) -> pd.Series:
    return _safe_div(volume, _rolling_mean(volume, 126))

def vper_025_vol_ma_ratio_252d(volume) -> pd.Series:
    return _safe_div(volume, _rolling_mean(volume, 252))

def vper_026_vol_consistency_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vper_001_vol_consistency_5d(volume), 252)

def vper_027_vol_consistency_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vper_002_vol_consistency_21d(volume), 252)

def vper_028_vol_consistency_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vper_003_vol_consistency_63d(volume), 252)

def vper_029_vol_consistency_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vper_004_vol_consistency_126d(volume), 252)

def vper_030_vol_consistency_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vper_005_vol_consistency_252d(volume), 252)

def vper_031_vol_trend_slope_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vper_006_vol_trend_slope_5d(volume), 252)

def vper_032_vol_trend_slope_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vper_007_vol_trend_slope_21d(volume), 252)

def vper_033_vol_trend_slope_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vper_008_vol_trend_slope_63d(volume), 252)

def vper_034_vol_trend_slope_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vper_009_vol_trend_slope_126d(volume), 252)

def vper_035_vol_trend_slope_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vper_010_vol_trend_slope_252d(volume), 252)

def vper_036_vol_stability_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vper_011_vol_stability_5d(volume), 252)

def vper_037_vol_stability_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vper_012_vol_stability_21d(volume), 252)

def vper_038_vol_stability_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vper_013_vol_stability_63d(volume), 252)

def vper_039_vol_stability_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vper_014_vol_stability_126d(volume), 252)

def vper_040_vol_stability_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vper_015_vol_stability_252d(volume), 252)

def vper_041_persistence_index_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vper_016_persistence_index_5d(volume), 252)

def vper_042_persistence_index_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vper_017_persistence_index_21d(volume), 252)

def vper_043_persistence_index_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vper_018_persistence_index_63d(volume), 252)

def vper_044_persistence_index_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vper_019_persistence_index_126d(volume), 252)

def vper_045_persistence_index_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vper_020_persistence_index_252d(volume), 252)

def vper_046_vol_ma_ratio_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vper_021_vol_ma_ratio_5d(volume), 252)

def vper_047_vol_ma_ratio_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vper_022_vol_ma_ratio_21d(volume), 252)

def vper_048_vol_ma_ratio_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vper_023_vol_ma_ratio_63d(volume), 252)

def vper_049_vol_ma_ratio_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vper_024_vol_ma_ratio_126d(volume), 252)

def vper_050_vol_ma_ratio_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vper_025_vol_ma_ratio_252d(volume), 252)

def vper_051_vol_consistency_rank_5d(volume) -> pd.Series:
    return vper_001_vol_consistency_5d(volume).rolling(252).rank(pct=True)

def vper_052_vol_consistency_rank_21d(volume) -> pd.Series:
    return vper_002_vol_consistency_21d(volume).rolling(252).rank(pct=True)

def vper_053_vol_consistency_rank_63d(volume) -> pd.Series:
    return vper_003_vol_consistency_63d(volume).rolling(252).rank(pct=True)

def vper_054_vol_consistency_rank_126d(volume) -> pd.Series:
    return vper_004_vol_consistency_126d(volume).rolling(252).rank(pct=True)

def vper_055_vol_consistency_rank_252d(volume) -> pd.Series:
    return vper_005_vol_consistency_252d(volume).rolling(252).rank(pct=True)

def vper_056_vol_trend_slope_rank_5d(volume) -> pd.Series:
    return vper_006_vol_trend_slope_5d(volume).rolling(252).rank(pct=True)

def vper_057_vol_trend_slope_rank_21d(volume) -> pd.Series:
    return vper_007_vol_trend_slope_21d(volume).rolling(252).rank(pct=True)

def vper_058_vol_trend_slope_rank_63d(volume) -> pd.Series:
    return vper_008_vol_trend_slope_63d(volume).rolling(252).rank(pct=True)

def vper_059_vol_trend_slope_rank_126d(volume) -> pd.Series:
    return vper_009_vol_trend_slope_126d(volume).rolling(252).rank(pct=True)

def vper_060_vol_trend_slope_rank_252d(volume) -> pd.Series:
    return vper_010_vol_trend_slope_252d(volume).rolling(252).rank(pct=True)

def vper_061_vol_stability_rank_5d(volume) -> pd.Series:
    return vper_011_vol_stability_5d(volume).rolling(252).rank(pct=True)

def vper_062_vol_stability_rank_21d(volume) -> pd.Series:
    return vper_012_vol_stability_21d(volume).rolling(252).rank(pct=True)

def vper_063_vol_stability_rank_63d(volume) -> pd.Series:
    return vper_013_vol_stability_63d(volume).rolling(252).rank(pct=True)

def vper_064_vol_stability_rank_126d(volume) -> pd.Series:
    return vper_014_vol_stability_126d(volume).rolling(252).rank(pct=True)

def vper_065_vol_stability_rank_252d(volume) -> pd.Series:
    return vper_015_vol_stability_252d(volume).rolling(252).rank(pct=True)

def vper_066_persistence_index_rank_5d(volume) -> pd.Series:
    return vper_016_persistence_index_5d(volume).rolling(252).rank(pct=True)

def vper_067_persistence_index_rank_21d(volume) -> pd.Series:
    return vper_017_persistence_index_21d(volume).rolling(252).rank(pct=True)

def vper_068_persistence_index_rank_63d(volume) -> pd.Series:
    return vper_018_persistence_index_63d(volume).rolling(252).rank(pct=True)

def vper_069_persistence_index_rank_126d(volume) -> pd.Series:
    return vper_019_persistence_index_126d(volume).rolling(252).rank(pct=True)

def vper_070_persistence_index_rank_252d(volume) -> pd.Series:
    return vper_020_persistence_index_252d(volume).rolling(252).rank(pct=True)

def vper_071_vol_ma_ratio_rank_5d(volume) -> pd.Series:
    return vper_021_vol_ma_ratio_5d(volume).rolling(252).rank(pct=True)

def vper_072_vol_ma_ratio_rank_21d(volume) -> pd.Series:
    return vper_022_vol_ma_ratio_21d(volume).rolling(252).rank(pct=True)

def vper_073_vol_ma_ratio_rank_63d(volume) -> pd.Series:
    return vper_023_vol_ma_ratio_63d(volume).rolling(252).rank(pct=True)

def vper_074_vol_ma_ratio_rank_126d(volume) -> pd.Series:
    return vper_024_vol_ma_ratio_126d(volume).rolling(252).rank(pct=True)

def vper_075_vol_ma_ratio_rank_252d(volume) -> pd.Series:
    return vper_025_vol_ma_ratio_252d(volume).rolling(252).rank(pct=True)


# --- Registry ---
V16_REGISTRY = {
    "vper_001_vol_consistency_5d": {"inputs": ['volume'], "func": vper_001_vol_consistency_5d},
    "vper_002_vol_consistency_21d": {"inputs": ['volume'], "func": vper_002_vol_consistency_21d},
    "vper_003_vol_consistency_63d": {"inputs": ['volume'], "func": vper_003_vol_consistency_63d},
    "vper_004_vol_consistency_126d": {"inputs": ['volume'], "func": vper_004_vol_consistency_126d},
    "vper_005_vol_consistency_252d": {"inputs": ['volume'], "func": vper_005_vol_consistency_252d},
    "vper_006_vol_trend_slope_5d": {"inputs": ['volume'], "func": vper_006_vol_trend_slope_5d},
    "vper_007_vol_trend_slope_21d": {"inputs": ['volume'], "func": vper_007_vol_trend_slope_21d},
    "vper_008_vol_trend_slope_63d": {"inputs": ['volume'], "func": vper_008_vol_trend_slope_63d},
    "vper_009_vol_trend_slope_126d": {"inputs": ['volume'], "func": vper_009_vol_trend_slope_126d},
    "vper_010_vol_trend_slope_252d": {"inputs": ['volume'], "func": vper_010_vol_trend_slope_252d},
    "vper_011_vol_stability_5d": {"inputs": ['volume'], "func": vper_011_vol_stability_5d},
    "vper_012_vol_stability_21d": {"inputs": ['volume'], "func": vper_012_vol_stability_21d},
    "vper_013_vol_stability_63d": {"inputs": ['volume'], "func": vper_013_vol_stability_63d},
    "vper_014_vol_stability_126d": {"inputs": ['volume'], "func": vper_014_vol_stability_126d},
    "vper_015_vol_stability_252d": {"inputs": ['volume'], "func": vper_015_vol_stability_252d},
    "vper_016_persistence_index_5d": {"inputs": ['volume'], "func": vper_016_persistence_index_5d},
    "vper_017_persistence_index_21d": {"inputs": ['volume'], "func": vper_017_persistence_index_21d},
    "vper_018_persistence_index_63d": {"inputs": ['volume'], "func": vper_018_persistence_index_63d},
    "vper_019_persistence_index_126d": {"inputs": ['volume'], "func": vper_019_persistence_index_126d},
    "vper_020_persistence_index_252d": {"inputs": ['volume'], "func": vper_020_persistence_index_252d},
    "vper_021_vol_ma_ratio_5d": {"inputs": ['volume'], "func": vper_021_vol_ma_ratio_5d},
    "vper_022_vol_ma_ratio_21d": {"inputs": ['volume'], "func": vper_022_vol_ma_ratio_21d},
    "vper_023_vol_ma_ratio_63d": {"inputs": ['volume'], "func": vper_023_vol_ma_ratio_63d},
    "vper_024_vol_ma_ratio_126d": {"inputs": ['volume'], "func": vper_024_vol_ma_ratio_126d},
    "vper_025_vol_ma_ratio_252d": {"inputs": ['volume'], "func": vper_025_vol_ma_ratio_252d},
    "vper_026_vol_consistency_zscore_5d": {"inputs": ['volume'], "func": vper_026_vol_consistency_zscore_5d},
    "vper_027_vol_consistency_zscore_21d": {"inputs": ['volume'], "func": vper_027_vol_consistency_zscore_21d},
    "vper_028_vol_consistency_zscore_63d": {"inputs": ['volume'], "func": vper_028_vol_consistency_zscore_63d},
    "vper_029_vol_consistency_zscore_126d": {"inputs": ['volume'], "func": vper_029_vol_consistency_zscore_126d},
    "vper_030_vol_consistency_zscore_252d": {"inputs": ['volume'], "func": vper_030_vol_consistency_zscore_252d},
    "vper_031_vol_trend_slope_zscore_5d": {"inputs": ['volume'], "func": vper_031_vol_trend_slope_zscore_5d},
    "vper_032_vol_trend_slope_zscore_21d": {"inputs": ['volume'], "func": vper_032_vol_trend_slope_zscore_21d},
    "vper_033_vol_trend_slope_zscore_63d": {"inputs": ['volume'], "func": vper_033_vol_trend_slope_zscore_63d},
    "vper_034_vol_trend_slope_zscore_126d": {"inputs": ['volume'], "func": vper_034_vol_trend_slope_zscore_126d},
    "vper_035_vol_trend_slope_zscore_252d": {"inputs": ['volume'], "func": vper_035_vol_trend_slope_zscore_252d},
    "vper_036_vol_stability_zscore_5d": {"inputs": ['volume'], "func": vper_036_vol_stability_zscore_5d},
    "vper_037_vol_stability_zscore_21d": {"inputs": ['volume'], "func": vper_037_vol_stability_zscore_21d},
    "vper_038_vol_stability_zscore_63d": {"inputs": ['volume'], "func": vper_038_vol_stability_zscore_63d},
    "vper_039_vol_stability_zscore_126d": {"inputs": ['volume'], "func": vper_039_vol_stability_zscore_126d},
    "vper_040_vol_stability_zscore_252d": {"inputs": ['volume'], "func": vper_040_vol_stability_zscore_252d},
    "vper_041_persistence_index_zscore_5d": {"inputs": ['volume'], "func": vper_041_persistence_index_zscore_5d},
    "vper_042_persistence_index_zscore_21d": {"inputs": ['volume'], "func": vper_042_persistence_index_zscore_21d},
    "vper_043_persistence_index_zscore_63d": {"inputs": ['volume'], "func": vper_043_persistence_index_zscore_63d},
    "vper_044_persistence_index_zscore_126d": {"inputs": ['volume'], "func": vper_044_persistence_index_zscore_126d},
    "vper_045_persistence_index_zscore_252d": {"inputs": ['volume'], "func": vper_045_persistence_index_zscore_252d},
    "vper_046_vol_ma_ratio_zscore_5d": {"inputs": ['volume'], "func": vper_046_vol_ma_ratio_zscore_5d},
    "vper_047_vol_ma_ratio_zscore_21d": {"inputs": ['volume'], "func": vper_047_vol_ma_ratio_zscore_21d},
    "vper_048_vol_ma_ratio_zscore_63d": {"inputs": ['volume'], "func": vper_048_vol_ma_ratio_zscore_63d},
    "vper_049_vol_ma_ratio_zscore_126d": {"inputs": ['volume'], "func": vper_049_vol_ma_ratio_zscore_126d},
    "vper_050_vol_ma_ratio_zscore_252d": {"inputs": ['volume'], "func": vper_050_vol_ma_ratio_zscore_252d},
    "vper_051_vol_consistency_rank_5d": {"inputs": ['volume'], "func": vper_051_vol_consistency_rank_5d},
    "vper_052_vol_consistency_rank_21d": {"inputs": ['volume'], "func": vper_052_vol_consistency_rank_21d},
    "vper_053_vol_consistency_rank_63d": {"inputs": ['volume'], "func": vper_053_vol_consistency_rank_63d},
    "vper_054_vol_consistency_rank_126d": {"inputs": ['volume'], "func": vper_054_vol_consistency_rank_126d},
    "vper_055_vol_consistency_rank_252d": {"inputs": ['volume'], "func": vper_055_vol_consistency_rank_252d},
    "vper_056_vol_trend_slope_rank_5d": {"inputs": ['volume'], "func": vper_056_vol_trend_slope_rank_5d},
    "vper_057_vol_trend_slope_rank_21d": {"inputs": ['volume'], "func": vper_057_vol_trend_slope_rank_21d},
    "vper_058_vol_trend_slope_rank_63d": {"inputs": ['volume'], "func": vper_058_vol_trend_slope_rank_63d},
    "vper_059_vol_trend_slope_rank_126d": {"inputs": ['volume'], "func": vper_059_vol_trend_slope_rank_126d},
    "vper_060_vol_trend_slope_rank_252d": {"inputs": ['volume'], "func": vper_060_vol_trend_slope_rank_252d},
    "vper_061_vol_stability_rank_5d": {"inputs": ['volume'], "func": vper_061_vol_stability_rank_5d},
    "vper_062_vol_stability_rank_21d": {"inputs": ['volume'], "func": vper_062_vol_stability_rank_21d},
    "vper_063_vol_stability_rank_63d": {"inputs": ['volume'], "func": vper_063_vol_stability_rank_63d},
    "vper_064_vol_stability_rank_126d": {"inputs": ['volume'], "func": vper_064_vol_stability_rank_126d},
    "vper_065_vol_stability_rank_252d": {"inputs": ['volume'], "func": vper_065_vol_stability_rank_252d},
    "vper_066_persistence_index_rank_5d": {"inputs": ['volume'], "func": vper_066_persistence_index_rank_5d},
    "vper_067_persistence_index_rank_21d": {"inputs": ['volume'], "func": vper_067_persistence_index_rank_21d},
    "vper_068_persistence_index_rank_63d": {"inputs": ['volume'], "func": vper_068_persistence_index_rank_63d},
    "vper_069_persistence_index_rank_126d": {"inputs": ['volume'], "func": vper_069_persistence_index_rank_126d},
    "vper_070_persistence_index_rank_252d": {"inputs": ['volume'], "func": vper_070_persistence_index_rank_252d},
    "vper_071_vol_ma_ratio_rank_5d": {"inputs": ['volume'], "func": vper_071_vol_ma_ratio_rank_5d},
    "vper_072_vol_ma_ratio_rank_21d": {"inputs": ['volume'], "func": vper_072_vol_ma_ratio_rank_21d},
    "vper_073_vol_ma_ratio_rank_63d": {"inputs": ['volume'], "func": vper_073_vol_ma_ratio_rank_63d},
    "vper_074_vol_ma_ratio_rank_126d": {"inputs": ['volume'], "func": vper_074_vol_ma_ratio_rank_126d},
    "vper_075_vol_ma_ratio_rank_252d": {"inputs": ['volume'], "func": vper_075_vol_ma_ratio_rank_252d},
}
