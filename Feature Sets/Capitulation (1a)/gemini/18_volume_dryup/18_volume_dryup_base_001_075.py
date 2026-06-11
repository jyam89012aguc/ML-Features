"""
Domain 18: volume_dryup (vdry_)
Asset Class: US Equities
Target Context: Periods of volume dryup and liquidity voids.
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
def vdry_001_dryup_intensity_5d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 5), volume)

def vdry_002_dryup_intensity_21d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 21), volume)

def vdry_003_dryup_intensity_63d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 63), volume)

def vdry_004_dryup_intensity_126d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 126), volume)

def vdry_005_dryup_intensity_252d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 252), volume)

def vdry_006_dryup_duration_5d(volume) -> pd.Series:
    return ((volume < _rolling_mean(volume, 252) * 0.5).astype(int)).rolling(5).sum()

def vdry_007_dryup_duration_21d(volume) -> pd.Series:
    return ((volume < _rolling_mean(volume, 252) * 0.5).astype(int)).rolling(21).sum()

def vdry_008_dryup_duration_63d(volume) -> pd.Series:
    return ((volume < _rolling_mean(volume, 252) * 0.5).astype(int)).rolling(63).sum()

def vdry_009_dryup_duration_126d(volume) -> pd.Series:
    return ((volume < _rolling_mean(volume, 252) * 0.5).astype(int)).rolling(126).sum()

def vdry_010_dryup_duration_252d(volume) -> pd.Series:
    return ((volume < _rolling_mean(volume, 252) * 0.5).astype(int)).rolling(252).sum()

def vdry_011_dryup_rebound_5d(close, volume) -> pd.Series:
    return (_daily_ret(close) * (volume < _rolling_mean(volume, 5) * 0.5).astype(float)).rolling(5).sum()

def vdry_012_dryup_rebound_21d(close, volume) -> pd.Series:
    return (_daily_ret(close) * (volume < _rolling_mean(volume, 21) * 0.5).astype(float)).rolling(21).sum()

def vdry_013_dryup_rebound_63d(close, volume) -> pd.Series:
    return (_daily_ret(close) * (volume < _rolling_mean(volume, 63) * 0.5).astype(float)).rolling(63).sum()

def vdry_014_dryup_rebound_126d(close, volume) -> pd.Series:
    return (_daily_ret(close) * (volume < _rolling_mean(volume, 126) * 0.5).astype(float)).rolling(126).sum()

def vdry_015_dryup_rebound_252d(close, volume) -> pd.Series:
    return (_daily_ret(close) * (volume < _rolling_mean(volume, 252) * 0.5).astype(float)).rolling(252).sum()

def vdry_016_liquidity_void_5d(volume) -> pd.Series:
    return _rolling_std(volume, 5) / _rolling_mean(volume, 5)

def vdry_017_liquidity_void_21d(volume) -> pd.Series:
    return _rolling_std(volume, 21) / _rolling_mean(volume, 21)

def vdry_018_liquidity_void_63d(volume) -> pd.Series:
    return _rolling_std(volume, 63) / _rolling_mean(volume, 63)

def vdry_019_liquidity_void_126d(volume) -> pd.Series:
    return _rolling_std(volume, 126) / _rolling_mean(volume, 126)

def vdry_020_liquidity_void_252d(volume) -> pd.Series:
    return _rolling_std(volume, 252) / _rolling_mean(volume, 252)

def vdry_021_low_vol_proximity_5d(volume) -> pd.Series:
    return (volume < _rolling_min(volume, 5) * 1.1).astype(float)

def vdry_022_low_vol_proximity_21d(volume) -> pd.Series:
    return (volume < _rolling_min(volume, 21) * 1.1).astype(float)

def vdry_023_low_vol_proximity_63d(volume) -> pd.Series:
    return (volume < _rolling_min(volume, 63) * 1.1).astype(float)

def vdry_024_low_vol_proximity_126d(volume) -> pd.Series:
    return (volume < _rolling_min(volume, 126) * 1.1).astype(float)

def vdry_025_low_vol_proximity_252d(volume) -> pd.Series:
    return (volume < _rolling_min(volume, 252) * 1.1).astype(float)

def vdry_026_dryup_intensity_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vdry_001_dryup_intensity_5d(volume), 252)

def vdry_027_dryup_intensity_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vdry_002_dryup_intensity_21d(volume), 252)

def vdry_028_dryup_intensity_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vdry_003_dryup_intensity_63d(volume), 252)

def vdry_029_dryup_intensity_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vdry_004_dryup_intensity_126d(volume), 252)

def vdry_030_dryup_intensity_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vdry_005_dryup_intensity_252d(volume), 252)

def vdry_031_dryup_duration_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vdry_006_dryup_duration_5d(volume), 252)

def vdry_032_dryup_duration_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vdry_007_dryup_duration_21d(volume), 252)

def vdry_033_dryup_duration_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vdry_008_dryup_duration_63d(volume), 252)

def vdry_034_dryup_duration_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vdry_009_dryup_duration_126d(volume), 252)

def vdry_035_dryup_duration_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vdry_010_dryup_duration_252d(volume), 252)

def vdry_036_dryup_rebound_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(vdry_011_dryup_rebound_5d(close, volume), 252)

def vdry_037_dryup_rebound_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(vdry_012_dryup_rebound_21d(close, volume), 252)

def vdry_038_dryup_rebound_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(vdry_013_dryup_rebound_63d(close, volume), 252)

def vdry_039_dryup_rebound_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(vdry_014_dryup_rebound_126d(close, volume), 252)

def vdry_040_dryup_rebound_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(vdry_015_dryup_rebound_252d(close, volume), 252)

def vdry_041_liquidity_void_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vdry_016_liquidity_void_5d(volume), 252)

def vdry_042_liquidity_void_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vdry_017_liquidity_void_21d(volume), 252)

def vdry_043_liquidity_void_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vdry_018_liquidity_void_63d(volume), 252)

def vdry_044_liquidity_void_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vdry_019_liquidity_void_126d(volume), 252)

def vdry_045_liquidity_void_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vdry_020_liquidity_void_252d(volume), 252)

def vdry_046_low_vol_proximity_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vdry_021_low_vol_proximity_5d(volume), 252)

def vdry_047_low_vol_proximity_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vdry_022_low_vol_proximity_21d(volume), 252)

def vdry_048_low_vol_proximity_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vdry_023_low_vol_proximity_63d(volume), 252)

def vdry_049_low_vol_proximity_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vdry_024_low_vol_proximity_126d(volume), 252)

def vdry_050_low_vol_proximity_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vdry_025_low_vol_proximity_252d(volume), 252)

def vdry_051_dryup_intensity_rank_5d(volume) -> pd.Series:
    return vdry_001_dryup_intensity_5d(volume).rolling(252).rank(pct=True)

def vdry_052_dryup_intensity_rank_21d(volume) -> pd.Series:
    return vdry_002_dryup_intensity_21d(volume).rolling(252).rank(pct=True)

def vdry_053_dryup_intensity_rank_63d(volume) -> pd.Series:
    return vdry_003_dryup_intensity_63d(volume).rolling(252).rank(pct=True)

def vdry_054_dryup_intensity_rank_126d(volume) -> pd.Series:
    return vdry_004_dryup_intensity_126d(volume).rolling(252).rank(pct=True)

def vdry_055_dryup_intensity_rank_252d(volume) -> pd.Series:
    return vdry_005_dryup_intensity_252d(volume).rolling(252).rank(pct=True)

def vdry_056_dryup_duration_rank_5d(volume) -> pd.Series:
    return vdry_006_dryup_duration_5d(volume).rolling(252).rank(pct=True)

def vdry_057_dryup_duration_rank_21d(volume) -> pd.Series:
    return vdry_007_dryup_duration_21d(volume).rolling(252).rank(pct=True)

def vdry_058_dryup_duration_rank_63d(volume) -> pd.Series:
    return vdry_008_dryup_duration_63d(volume).rolling(252).rank(pct=True)

def vdry_059_dryup_duration_rank_126d(volume) -> pd.Series:
    return vdry_009_dryup_duration_126d(volume).rolling(252).rank(pct=True)

def vdry_060_dryup_duration_rank_252d(volume) -> pd.Series:
    return vdry_010_dryup_duration_252d(volume).rolling(252).rank(pct=True)

def vdry_061_dryup_rebound_rank_5d(close, volume) -> pd.Series:
    return vdry_011_dryup_rebound_5d(close, volume).rolling(252).rank(pct=True)

def vdry_062_dryup_rebound_rank_21d(close, volume) -> pd.Series:
    return vdry_012_dryup_rebound_21d(close, volume).rolling(252).rank(pct=True)

def vdry_063_dryup_rebound_rank_63d(close, volume) -> pd.Series:
    return vdry_013_dryup_rebound_63d(close, volume).rolling(252).rank(pct=True)

def vdry_064_dryup_rebound_rank_126d(close, volume) -> pd.Series:
    return vdry_014_dryup_rebound_126d(close, volume).rolling(252).rank(pct=True)

def vdry_065_dryup_rebound_rank_252d(close, volume) -> pd.Series:
    return vdry_015_dryup_rebound_252d(close, volume).rolling(252).rank(pct=True)

def vdry_066_liquidity_void_rank_5d(volume) -> pd.Series:
    return vdry_016_liquidity_void_5d(volume).rolling(252).rank(pct=True)

def vdry_067_liquidity_void_rank_21d(volume) -> pd.Series:
    return vdry_017_liquidity_void_21d(volume).rolling(252).rank(pct=True)

def vdry_068_liquidity_void_rank_63d(volume) -> pd.Series:
    return vdry_018_liquidity_void_63d(volume).rolling(252).rank(pct=True)

def vdry_069_liquidity_void_rank_126d(volume) -> pd.Series:
    return vdry_019_liquidity_void_126d(volume).rolling(252).rank(pct=True)

def vdry_070_liquidity_void_rank_252d(volume) -> pd.Series:
    return vdry_020_liquidity_void_252d(volume).rolling(252).rank(pct=True)

def vdry_071_low_vol_proximity_rank_5d(volume) -> pd.Series:
    return vdry_021_low_vol_proximity_5d(volume).rolling(252).rank(pct=True)

def vdry_072_low_vol_proximity_rank_21d(volume) -> pd.Series:
    return vdry_022_low_vol_proximity_21d(volume).rolling(252).rank(pct=True)

def vdry_073_low_vol_proximity_rank_63d(volume) -> pd.Series:
    return vdry_023_low_vol_proximity_63d(volume).rolling(252).rank(pct=True)

def vdry_074_low_vol_proximity_rank_126d(volume) -> pd.Series:
    return vdry_024_low_vol_proximity_126d(volume).rolling(252).rank(pct=True)

def vdry_075_low_vol_proximity_rank_252d(volume) -> pd.Series:
    return vdry_025_low_vol_proximity_252d(volume).rolling(252).rank(pct=True)


# --- Registry ---
V18_REGISTRY = {
    "vdry_001_dryup_intensity_5d": {"inputs": ['volume'], "func": vdry_001_dryup_intensity_5d},
    "vdry_002_dryup_intensity_21d": {"inputs": ['volume'], "func": vdry_002_dryup_intensity_21d},
    "vdry_003_dryup_intensity_63d": {"inputs": ['volume'], "func": vdry_003_dryup_intensity_63d},
    "vdry_004_dryup_intensity_126d": {"inputs": ['volume'], "func": vdry_004_dryup_intensity_126d},
    "vdry_005_dryup_intensity_252d": {"inputs": ['volume'], "func": vdry_005_dryup_intensity_252d},
    "vdry_006_dryup_duration_5d": {"inputs": ['volume'], "func": vdry_006_dryup_duration_5d},
    "vdry_007_dryup_duration_21d": {"inputs": ['volume'], "func": vdry_007_dryup_duration_21d},
    "vdry_008_dryup_duration_63d": {"inputs": ['volume'], "func": vdry_008_dryup_duration_63d},
    "vdry_009_dryup_duration_126d": {"inputs": ['volume'], "func": vdry_009_dryup_duration_126d},
    "vdry_010_dryup_duration_252d": {"inputs": ['volume'], "func": vdry_010_dryup_duration_252d},
    "vdry_011_dryup_rebound_5d": {"inputs": ['close', 'volume'], "func": vdry_011_dryup_rebound_5d},
    "vdry_012_dryup_rebound_21d": {"inputs": ['close', 'volume'], "func": vdry_012_dryup_rebound_21d},
    "vdry_013_dryup_rebound_63d": {"inputs": ['close', 'volume'], "func": vdry_013_dryup_rebound_63d},
    "vdry_014_dryup_rebound_126d": {"inputs": ['close', 'volume'], "func": vdry_014_dryup_rebound_126d},
    "vdry_015_dryup_rebound_252d": {"inputs": ['close', 'volume'], "func": vdry_015_dryup_rebound_252d},
    "vdry_016_liquidity_void_5d": {"inputs": ['volume'], "func": vdry_016_liquidity_void_5d},
    "vdry_017_liquidity_void_21d": {"inputs": ['volume'], "func": vdry_017_liquidity_void_21d},
    "vdry_018_liquidity_void_63d": {"inputs": ['volume'], "func": vdry_018_liquidity_void_63d},
    "vdry_019_liquidity_void_126d": {"inputs": ['volume'], "func": vdry_019_liquidity_void_126d},
    "vdry_020_liquidity_void_252d": {"inputs": ['volume'], "func": vdry_020_liquidity_void_252d},
    "vdry_021_low_vol_proximity_5d": {"inputs": ['volume'], "func": vdry_021_low_vol_proximity_5d},
    "vdry_022_low_vol_proximity_21d": {"inputs": ['volume'], "func": vdry_022_low_vol_proximity_21d},
    "vdry_023_low_vol_proximity_63d": {"inputs": ['volume'], "func": vdry_023_low_vol_proximity_63d},
    "vdry_024_low_vol_proximity_126d": {"inputs": ['volume'], "func": vdry_024_low_vol_proximity_126d},
    "vdry_025_low_vol_proximity_252d": {"inputs": ['volume'], "func": vdry_025_low_vol_proximity_252d},
    "vdry_026_dryup_intensity_zscore_5d": {"inputs": ['volume'], "func": vdry_026_dryup_intensity_zscore_5d},
    "vdry_027_dryup_intensity_zscore_21d": {"inputs": ['volume'], "func": vdry_027_dryup_intensity_zscore_21d},
    "vdry_028_dryup_intensity_zscore_63d": {"inputs": ['volume'], "func": vdry_028_dryup_intensity_zscore_63d},
    "vdry_029_dryup_intensity_zscore_126d": {"inputs": ['volume'], "func": vdry_029_dryup_intensity_zscore_126d},
    "vdry_030_dryup_intensity_zscore_252d": {"inputs": ['volume'], "func": vdry_030_dryup_intensity_zscore_252d},
    "vdry_031_dryup_duration_zscore_5d": {"inputs": ['volume'], "func": vdry_031_dryup_duration_zscore_5d},
    "vdry_032_dryup_duration_zscore_21d": {"inputs": ['volume'], "func": vdry_032_dryup_duration_zscore_21d},
    "vdry_033_dryup_duration_zscore_63d": {"inputs": ['volume'], "func": vdry_033_dryup_duration_zscore_63d},
    "vdry_034_dryup_duration_zscore_126d": {"inputs": ['volume'], "func": vdry_034_dryup_duration_zscore_126d},
    "vdry_035_dryup_duration_zscore_252d": {"inputs": ['volume'], "func": vdry_035_dryup_duration_zscore_252d},
    "vdry_036_dryup_rebound_zscore_5d": {"inputs": ['close', 'volume'], "func": vdry_036_dryup_rebound_zscore_5d},
    "vdry_037_dryup_rebound_zscore_21d": {"inputs": ['close', 'volume'], "func": vdry_037_dryup_rebound_zscore_21d},
    "vdry_038_dryup_rebound_zscore_63d": {"inputs": ['close', 'volume'], "func": vdry_038_dryup_rebound_zscore_63d},
    "vdry_039_dryup_rebound_zscore_126d": {"inputs": ['close', 'volume'], "func": vdry_039_dryup_rebound_zscore_126d},
    "vdry_040_dryup_rebound_zscore_252d": {"inputs": ['close', 'volume'], "func": vdry_040_dryup_rebound_zscore_252d},
    "vdry_041_liquidity_void_zscore_5d": {"inputs": ['volume'], "func": vdry_041_liquidity_void_zscore_5d},
    "vdry_042_liquidity_void_zscore_21d": {"inputs": ['volume'], "func": vdry_042_liquidity_void_zscore_21d},
    "vdry_043_liquidity_void_zscore_63d": {"inputs": ['volume'], "func": vdry_043_liquidity_void_zscore_63d},
    "vdry_044_liquidity_void_zscore_126d": {"inputs": ['volume'], "func": vdry_044_liquidity_void_zscore_126d},
    "vdry_045_liquidity_void_zscore_252d": {"inputs": ['volume'], "func": vdry_045_liquidity_void_zscore_252d},
    "vdry_046_low_vol_proximity_zscore_5d": {"inputs": ['volume'], "func": vdry_046_low_vol_proximity_zscore_5d},
    "vdry_047_low_vol_proximity_zscore_21d": {"inputs": ['volume'], "func": vdry_047_low_vol_proximity_zscore_21d},
    "vdry_048_low_vol_proximity_zscore_63d": {"inputs": ['volume'], "func": vdry_048_low_vol_proximity_zscore_63d},
    "vdry_049_low_vol_proximity_zscore_126d": {"inputs": ['volume'], "func": vdry_049_low_vol_proximity_zscore_126d},
    "vdry_050_low_vol_proximity_zscore_252d": {"inputs": ['volume'], "func": vdry_050_low_vol_proximity_zscore_252d},
    "vdry_051_dryup_intensity_rank_5d": {"inputs": ['volume'], "func": vdry_051_dryup_intensity_rank_5d},
    "vdry_052_dryup_intensity_rank_21d": {"inputs": ['volume'], "func": vdry_052_dryup_intensity_rank_21d},
    "vdry_053_dryup_intensity_rank_63d": {"inputs": ['volume'], "func": vdry_053_dryup_intensity_rank_63d},
    "vdry_054_dryup_intensity_rank_126d": {"inputs": ['volume'], "func": vdry_054_dryup_intensity_rank_126d},
    "vdry_055_dryup_intensity_rank_252d": {"inputs": ['volume'], "func": vdry_055_dryup_intensity_rank_252d},
    "vdry_056_dryup_duration_rank_5d": {"inputs": ['volume'], "func": vdry_056_dryup_duration_rank_5d},
    "vdry_057_dryup_duration_rank_21d": {"inputs": ['volume'], "func": vdry_057_dryup_duration_rank_21d},
    "vdry_058_dryup_duration_rank_63d": {"inputs": ['volume'], "func": vdry_058_dryup_duration_rank_63d},
    "vdry_059_dryup_duration_rank_126d": {"inputs": ['volume'], "func": vdry_059_dryup_duration_rank_126d},
    "vdry_060_dryup_duration_rank_252d": {"inputs": ['volume'], "func": vdry_060_dryup_duration_rank_252d},
    "vdry_061_dryup_rebound_rank_5d": {"inputs": ['close', 'volume'], "func": vdry_061_dryup_rebound_rank_5d},
    "vdry_062_dryup_rebound_rank_21d": {"inputs": ['close', 'volume'], "func": vdry_062_dryup_rebound_rank_21d},
    "vdry_063_dryup_rebound_rank_63d": {"inputs": ['close', 'volume'], "func": vdry_063_dryup_rebound_rank_63d},
    "vdry_064_dryup_rebound_rank_126d": {"inputs": ['close', 'volume'], "func": vdry_064_dryup_rebound_rank_126d},
    "vdry_065_dryup_rebound_rank_252d": {"inputs": ['close', 'volume'], "func": vdry_065_dryup_rebound_rank_252d},
    "vdry_066_liquidity_void_rank_5d": {"inputs": ['volume'], "func": vdry_066_liquidity_void_rank_5d},
    "vdry_067_liquidity_void_rank_21d": {"inputs": ['volume'], "func": vdry_067_liquidity_void_rank_21d},
    "vdry_068_liquidity_void_rank_63d": {"inputs": ['volume'], "func": vdry_068_liquidity_void_rank_63d},
    "vdry_069_liquidity_void_rank_126d": {"inputs": ['volume'], "func": vdry_069_liquidity_void_rank_126d},
    "vdry_070_liquidity_void_rank_252d": {"inputs": ['volume'], "func": vdry_070_liquidity_void_rank_252d},
    "vdry_071_low_vol_proximity_rank_5d": {"inputs": ['volume'], "func": vdry_071_low_vol_proximity_rank_5d},
    "vdry_072_low_vol_proximity_rank_21d": {"inputs": ['volume'], "func": vdry_072_low_vol_proximity_rank_21d},
    "vdry_073_low_vol_proximity_rank_63d": {"inputs": ['volume'], "func": vdry_073_low_vol_proximity_rank_63d},
    "vdry_074_low_vol_proximity_rank_126d": {"inputs": ['volume'], "func": vdry_074_low_vol_proximity_rank_126d},
    "vdry_075_low_vol_proximity_rank_252d": {"inputs": ['volume'], "func": vdry_075_low_vol_proximity_rank_252d},
}
