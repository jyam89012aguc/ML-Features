"""
Domain 20: up_down_volume (udv_)
Asset Class: US Equities
Target Context: Buying vs selling intensity via up/down volume.
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
def udv_001_up_down_ratio_5d(close, volume) -> pd.Series:
    return _safe_div(_rolling_sum(volume * (close > close.shift(1)).astype(float), 5), _rolling_sum(volume * (close < close.shift(1)).astype(float), 5))

def udv_002_up_down_ratio_21d(close, volume) -> pd.Series:
    return _safe_div(_rolling_sum(volume * (close > close.shift(1)).astype(float), 21), _rolling_sum(volume * (close < close.shift(1)).astype(float), 21))

def udv_003_up_down_ratio_63d(close, volume) -> pd.Series:
    return _safe_div(_rolling_sum(volume * (close > close.shift(1)).astype(float), 63), _rolling_sum(volume * (close < close.shift(1)).astype(float), 63))

def udv_004_up_down_ratio_126d(close, volume) -> pd.Series:
    return _safe_div(_rolling_sum(volume * (close > close.shift(1)).astype(float), 126), _rolling_sum(volume * (close < close.shift(1)).astype(float), 126))

def udv_005_up_down_ratio_252d(close, volume) -> pd.Series:
    return _safe_div(_rolling_sum(volume * (close > close.shift(1)).astype(float), 252), _rolling_sum(volume * (close < close.shift(1)).astype(float), 252))

def udv_006_obv_slope_5d(close, volume) -> pd.Series:
    return ((np.sign(close.diff()) * volume).rolling(5).sum()).diff(5)

def udv_007_obv_slope_21d(close, volume) -> pd.Series:
    return ((np.sign(close.diff()) * volume).rolling(21).sum()).diff(21)

def udv_008_obv_slope_63d(close, volume) -> pd.Series:
    return ((np.sign(close.diff()) * volume).rolling(63).sum()).diff(63)

def udv_009_obv_slope_126d(close, volume) -> pd.Series:
    return ((np.sign(close.diff()) * volume).rolling(126).sum()).diff(126)

def udv_010_obv_slope_252d(close, volume) -> pd.Series:
    return ((np.sign(close.diff()) * volume).rolling(252).sum()).diff(252)

def udv_011_buying_intensity_5d(close, volume) -> pd.Series:
    return _safe_div(_rolling_sum(volume * (close > close.shift(1)).astype(float), 5), _rolling_sum(volume, 5))

def udv_012_buying_intensity_21d(close, volume) -> pd.Series:
    return _safe_div(_rolling_sum(volume * (close > close.shift(1)).astype(float), 21), _rolling_sum(volume, 21))

def udv_013_buying_intensity_63d(close, volume) -> pd.Series:
    return _safe_div(_rolling_sum(volume * (close > close.shift(1)).astype(float), 63), _rolling_sum(volume, 63))

def udv_014_buying_intensity_126d(close, volume) -> pd.Series:
    return _safe_div(_rolling_sum(volume * (close > close.shift(1)).astype(float), 126), _rolling_sum(volume, 126))

def udv_015_buying_intensity_252d(close, volume) -> pd.Series:
    return _safe_div(_rolling_sum(volume * (close > close.shift(1)).astype(float), 252), _rolling_sum(volume, 252))

def udv_016_selling_intensity_5d(close, volume) -> pd.Series:
    return _safe_div(_rolling_sum(volume * (close < close.shift(1)).astype(float), 5), _rolling_sum(volume, 5))

def udv_017_selling_intensity_21d(close, volume) -> pd.Series:
    return _safe_div(_rolling_sum(volume * (close < close.shift(1)).astype(float), 21), _rolling_sum(volume, 21))

def udv_018_selling_intensity_63d(close, volume) -> pd.Series:
    return _safe_div(_rolling_sum(volume * (close < close.shift(1)).astype(float), 63), _rolling_sum(volume, 63))

def udv_019_selling_intensity_126d(close, volume) -> pd.Series:
    return _safe_div(_rolling_sum(volume * (close < close.shift(1)).astype(float), 126), _rolling_sum(volume, 126))

def udv_020_selling_intensity_252d(close, volume) -> pd.Series:
    return _safe_div(_rolling_sum(volume * (close < close.shift(1)).astype(float), 252), _rolling_sum(volume, 252))

def udv_021_vol_force_5d(close, volume) -> pd.Series:
    return (_daily_ret(close) * volume).rolling(5).mean()

def udv_022_vol_force_21d(close, volume) -> pd.Series:
    return (_daily_ret(close) * volume).rolling(21).mean()

def udv_023_vol_force_63d(close, volume) -> pd.Series:
    return (_daily_ret(close) * volume).rolling(63).mean()

def udv_024_vol_force_126d(close, volume) -> pd.Series:
    return (_daily_ret(close) * volume).rolling(126).mean()

def udv_025_vol_force_252d(close, volume) -> pd.Series:
    return (_daily_ret(close) * volume).rolling(252).mean()

def udv_026_up_down_ratio_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_001_up_down_ratio_5d(close, volume), 252)

def udv_027_up_down_ratio_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_002_up_down_ratio_21d(close, volume), 252)

def udv_028_up_down_ratio_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_003_up_down_ratio_63d(close, volume), 252)

def udv_029_up_down_ratio_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_004_up_down_ratio_126d(close, volume), 252)

def udv_030_up_down_ratio_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_005_up_down_ratio_252d(close, volume), 252)

def udv_031_obv_slope_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_006_obv_slope_5d(close, volume), 252)

def udv_032_obv_slope_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_007_obv_slope_21d(close, volume), 252)

def udv_033_obv_slope_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_008_obv_slope_63d(close, volume), 252)

def udv_034_obv_slope_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_009_obv_slope_126d(close, volume), 252)

def udv_035_obv_slope_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_010_obv_slope_252d(close, volume), 252)

def udv_036_buying_intensity_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_011_buying_intensity_5d(close, volume), 252)

def udv_037_buying_intensity_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_012_buying_intensity_21d(close, volume), 252)

def udv_038_buying_intensity_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_013_buying_intensity_63d(close, volume), 252)

def udv_039_buying_intensity_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_014_buying_intensity_126d(close, volume), 252)

def udv_040_buying_intensity_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_015_buying_intensity_252d(close, volume), 252)

def udv_041_selling_intensity_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_016_selling_intensity_5d(close, volume), 252)

def udv_042_selling_intensity_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_017_selling_intensity_21d(close, volume), 252)

def udv_043_selling_intensity_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_018_selling_intensity_63d(close, volume), 252)

def udv_044_selling_intensity_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_019_selling_intensity_126d(close, volume), 252)

def udv_045_selling_intensity_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_020_selling_intensity_252d(close, volume), 252)

def udv_046_vol_force_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_021_vol_force_5d(close, volume), 252)

def udv_047_vol_force_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_022_vol_force_21d(close, volume), 252)

def udv_048_vol_force_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_023_vol_force_63d(close, volume), 252)

def udv_049_vol_force_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_024_vol_force_126d(close, volume), 252)

def udv_050_vol_force_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(udv_025_vol_force_252d(close, volume), 252)

def udv_051_up_down_ratio_rank_5d(close, volume) -> pd.Series:
    return udv_001_up_down_ratio_5d(close, volume).rolling(252).rank(pct=True)

def udv_052_up_down_ratio_rank_21d(close, volume) -> pd.Series:
    return udv_002_up_down_ratio_21d(close, volume).rolling(252).rank(pct=True)

def udv_053_up_down_ratio_rank_63d(close, volume) -> pd.Series:
    return udv_003_up_down_ratio_63d(close, volume).rolling(252).rank(pct=True)

def udv_054_up_down_ratio_rank_126d(close, volume) -> pd.Series:
    return udv_004_up_down_ratio_126d(close, volume).rolling(252).rank(pct=True)

def udv_055_up_down_ratio_rank_252d(close, volume) -> pd.Series:
    return udv_005_up_down_ratio_252d(close, volume).rolling(252).rank(pct=True)

def udv_056_obv_slope_rank_5d(close, volume) -> pd.Series:
    return udv_006_obv_slope_5d(close, volume).rolling(252).rank(pct=True)

def udv_057_obv_slope_rank_21d(close, volume) -> pd.Series:
    return udv_007_obv_slope_21d(close, volume).rolling(252).rank(pct=True)

def udv_058_obv_slope_rank_63d(close, volume) -> pd.Series:
    return udv_008_obv_slope_63d(close, volume).rolling(252).rank(pct=True)

def udv_059_obv_slope_rank_126d(close, volume) -> pd.Series:
    return udv_009_obv_slope_126d(close, volume).rolling(252).rank(pct=True)

def udv_060_obv_slope_rank_252d(close, volume) -> pd.Series:
    return udv_010_obv_slope_252d(close, volume).rolling(252).rank(pct=True)

def udv_061_buying_intensity_rank_5d(close, volume) -> pd.Series:
    return udv_011_buying_intensity_5d(close, volume).rolling(252).rank(pct=True)

def udv_062_buying_intensity_rank_21d(close, volume) -> pd.Series:
    return udv_012_buying_intensity_21d(close, volume).rolling(252).rank(pct=True)

def udv_063_buying_intensity_rank_63d(close, volume) -> pd.Series:
    return udv_013_buying_intensity_63d(close, volume).rolling(252).rank(pct=True)

def udv_064_buying_intensity_rank_126d(close, volume) -> pd.Series:
    return udv_014_buying_intensity_126d(close, volume).rolling(252).rank(pct=True)

def udv_065_buying_intensity_rank_252d(close, volume) -> pd.Series:
    return udv_015_buying_intensity_252d(close, volume).rolling(252).rank(pct=True)

def udv_066_selling_intensity_rank_5d(close, volume) -> pd.Series:
    return udv_016_selling_intensity_5d(close, volume).rolling(252).rank(pct=True)

def udv_067_selling_intensity_rank_21d(close, volume) -> pd.Series:
    return udv_017_selling_intensity_21d(close, volume).rolling(252).rank(pct=True)

def udv_068_selling_intensity_rank_63d(close, volume) -> pd.Series:
    return udv_018_selling_intensity_63d(close, volume).rolling(252).rank(pct=True)

def udv_069_selling_intensity_rank_126d(close, volume) -> pd.Series:
    return udv_019_selling_intensity_126d(close, volume).rolling(252).rank(pct=True)

def udv_070_selling_intensity_rank_252d(close, volume) -> pd.Series:
    return udv_020_selling_intensity_252d(close, volume).rolling(252).rank(pct=True)

def udv_071_vol_force_rank_5d(close, volume) -> pd.Series:
    return udv_021_vol_force_5d(close, volume).rolling(252).rank(pct=True)

def udv_072_vol_force_rank_21d(close, volume) -> pd.Series:
    return udv_022_vol_force_21d(close, volume).rolling(252).rank(pct=True)

def udv_073_vol_force_rank_63d(close, volume) -> pd.Series:
    return udv_023_vol_force_63d(close, volume).rolling(252).rank(pct=True)

def udv_074_vol_force_rank_126d(close, volume) -> pd.Series:
    return udv_024_vol_force_126d(close, volume).rolling(252).rank(pct=True)

def udv_075_vol_force_rank_252d(close, volume) -> pd.Series:
    return udv_025_vol_force_252d(close, volume).rolling(252).rank(pct=True)


# --- Registry ---
V20_REGISTRY = {
    "udv_001_up_down_ratio_5d": {"inputs": ['close', 'volume'], "func": udv_001_up_down_ratio_5d},
    "udv_002_up_down_ratio_21d": {"inputs": ['close', 'volume'], "func": udv_002_up_down_ratio_21d},
    "udv_003_up_down_ratio_63d": {"inputs": ['close', 'volume'], "func": udv_003_up_down_ratio_63d},
    "udv_004_up_down_ratio_126d": {"inputs": ['close', 'volume'], "func": udv_004_up_down_ratio_126d},
    "udv_005_up_down_ratio_252d": {"inputs": ['close', 'volume'], "func": udv_005_up_down_ratio_252d},
    "udv_006_obv_slope_5d": {"inputs": ['close', 'volume'], "func": udv_006_obv_slope_5d},
    "udv_007_obv_slope_21d": {"inputs": ['close', 'volume'], "func": udv_007_obv_slope_21d},
    "udv_008_obv_slope_63d": {"inputs": ['close', 'volume'], "func": udv_008_obv_slope_63d},
    "udv_009_obv_slope_126d": {"inputs": ['close', 'volume'], "func": udv_009_obv_slope_126d},
    "udv_010_obv_slope_252d": {"inputs": ['close', 'volume'], "func": udv_010_obv_slope_252d},
    "udv_011_buying_intensity_5d": {"inputs": ['close', 'volume'], "func": udv_011_buying_intensity_5d},
    "udv_012_buying_intensity_21d": {"inputs": ['close', 'volume'], "func": udv_012_buying_intensity_21d},
    "udv_013_buying_intensity_63d": {"inputs": ['close', 'volume'], "func": udv_013_buying_intensity_63d},
    "udv_014_buying_intensity_126d": {"inputs": ['close', 'volume'], "func": udv_014_buying_intensity_126d},
    "udv_015_buying_intensity_252d": {"inputs": ['close', 'volume'], "func": udv_015_buying_intensity_252d},
    "udv_016_selling_intensity_5d": {"inputs": ['close', 'volume'], "func": udv_016_selling_intensity_5d},
    "udv_017_selling_intensity_21d": {"inputs": ['close', 'volume'], "func": udv_017_selling_intensity_21d},
    "udv_018_selling_intensity_63d": {"inputs": ['close', 'volume'], "func": udv_018_selling_intensity_63d},
    "udv_019_selling_intensity_126d": {"inputs": ['close', 'volume'], "func": udv_019_selling_intensity_126d},
    "udv_020_selling_intensity_252d": {"inputs": ['close', 'volume'], "func": udv_020_selling_intensity_252d},
    "udv_021_vol_force_5d": {"inputs": ['close', 'volume'], "func": udv_021_vol_force_5d},
    "udv_022_vol_force_21d": {"inputs": ['close', 'volume'], "func": udv_022_vol_force_21d},
    "udv_023_vol_force_63d": {"inputs": ['close', 'volume'], "func": udv_023_vol_force_63d},
    "udv_024_vol_force_126d": {"inputs": ['close', 'volume'], "func": udv_024_vol_force_126d},
    "udv_025_vol_force_252d": {"inputs": ['close', 'volume'], "func": udv_025_vol_force_252d},
    "udv_026_up_down_ratio_zscore_5d": {"inputs": ['close', 'volume'], "func": udv_026_up_down_ratio_zscore_5d},
    "udv_027_up_down_ratio_zscore_21d": {"inputs": ['close', 'volume'], "func": udv_027_up_down_ratio_zscore_21d},
    "udv_028_up_down_ratio_zscore_63d": {"inputs": ['close', 'volume'], "func": udv_028_up_down_ratio_zscore_63d},
    "udv_029_up_down_ratio_zscore_126d": {"inputs": ['close', 'volume'], "func": udv_029_up_down_ratio_zscore_126d},
    "udv_030_up_down_ratio_zscore_252d": {"inputs": ['close', 'volume'], "func": udv_030_up_down_ratio_zscore_252d},
    "udv_031_obv_slope_zscore_5d": {"inputs": ['close', 'volume'], "func": udv_031_obv_slope_zscore_5d},
    "udv_032_obv_slope_zscore_21d": {"inputs": ['close', 'volume'], "func": udv_032_obv_slope_zscore_21d},
    "udv_033_obv_slope_zscore_63d": {"inputs": ['close', 'volume'], "func": udv_033_obv_slope_zscore_63d},
    "udv_034_obv_slope_zscore_126d": {"inputs": ['close', 'volume'], "func": udv_034_obv_slope_zscore_126d},
    "udv_035_obv_slope_zscore_252d": {"inputs": ['close', 'volume'], "func": udv_035_obv_slope_zscore_252d},
    "udv_036_buying_intensity_zscore_5d": {"inputs": ['close', 'volume'], "func": udv_036_buying_intensity_zscore_5d},
    "udv_037_buying_intensity_zscore_21d": {"inputs": ['close', 'volume'], "func": udv_037_buying_intensity_zscore_21d},
    "udv_038_buying_intensity_zscore_63d": {"inputs": ['close', 'volume'], "func": udv_038_buying_intensity_zscore_63d},
    "udv_039_buying_intensity_zscore_126d": {"inputs": ['close', 'volume'], "func": udv_039_buying_intensity_zscore_126d},
    "udv_040_buying_intensity_zscore_252d": {"inputs": ['close', 'volume'], "func": udv_040_buying_intensity_zscore_252d},
    "udv_041_selling_intensity_zscore_5d": {"inputs": ['close', 'volume'], "func": udv_041_selling_intensity_zscore_5d},
    "udv_042_selling_intensity_zscore_21d": {"inputs": ['close', 'volume'], "func": udv_042_selling_intensity_zscore_21d},
    "udv_043_selling_intensity_zscore_63d": {"inputs": ['close', 'volume'], "func": udv_043_selling_intensity_zscore_63d},
    "udv_044_selling_intensity_zscore_126d": {"inputs": ['close', 'volume'], "func": udv_044_selling_intensity_zscore_126d},
    "udv_045_selling_intensity_zscore_252d": {"inputs": ['close', 'volume'], "func": udv_045_selling_intensity_zscore_252d},
    "udv_046_vol_force_zscore_5d": {"inputs": ['close', 'volume'], "func": udv_046_vol_force_zscore_5d},
    "udv_047_vol_force_zscore_21d": {"inputs": ['close', 'volume'], "func": udv_047_vol_force_zscore_21d},
    "udv_048_vol_force_zscore_63d": {"inputs": ['close', 'volume'], "func": udv_048_vol_force_zscore_63d},
    "udv_049_vol_force_zscore_126d": {"inputs": ['close', 'volume'], "func": udv_049_vol_force_zscore_126d},
    "udv_050_vol_force_zscore_252d": {"inputs": ['close', 'volume'], "func": udv_050_vol_force_zscore_252d},
    "udv_051_up_down_ratio_rank_5d": {"inputs": ['close', 'volume'], "func": udv_051_up_down_ratio_rank_5d},
    "udv_052_up_down_ratio_rank_21d": {"inputs": ['close', 'volume'], "func": udv_052_up_down_ratio_rank_21d},
    "udv_053_up_down_ratio_rank_63d": {"inputs": ['close', 'volume'], "func": udv_053_up_down_ratio_rank_63d},
    "udv_054_up_down_ratio_rank_126d": {"inputs": ['close', 'volume'], "func": udv_054_up_down_ratio_rank_126d},
    "udv_055_up_down_ratio_rank_252d": {"inputs": ['close', 'volume'], "func": udv_055_up_down_ratio_rank_252d},
    "udv_056_obv_slope_rank_5d": {"inputs": ['close', 'volume'], "func": udv_056_obv_slope_rank_5d},
    "udv_057_obv_slope_rank_21d": {"inputs": ['close', 'volume'], "func": udv_057_obv_slope_rank_21d},
    "udv_058_obv_slope_rank_63d": {"inputs": ['close', 'volume'], "func": udv_058_obv_slope_rank_63d},
    "udv_059_obv_slope_rank_126d": {"inputs": ['close', 'volume'], "func": udv_059_obv_slope_rank_126d},
    "udv_060_obv_slope_rank_252d": {"inputs": ['close', 'volume'], "func": udv_060_obv_slope_rank_252d},
    "udv_061_buying_intensity_rank_5d": {"inputs": ['close', 'volume'], "func": udv_061_buying_intensity_rank_5d},
    "udv_062_buying_intensity_rank_21d": {"inputs": ['close', 'volume'], "func": udv_062_buying_intensity_rank_21d},
    "udv_063_buying_intensity_rank_63d": {"inputs": ['close', 'volume'], "func": udv_063_buying_intensity_rank_63d},
    "udv_064_buying_intensity_rank_126d": {"inputs": ['close', 'volume'], "func": udv_064_buying_intensity_rank_126d},
    "udv_065_buying_intensity_rank_252d": {"inputs": ['close', 'volume'], "func": udv_065_buying_intensity_rank_252d},
    "udv_066_selling_intensity_rank_5d": {"inputs": ['close', 'volume'], "func": udv_066_selling_intensity_rank_5d},
    "udv_067_selling_intensity_rank_21d": {"inputs": ['close', 'volume'], "func": udv_067_selling_intensity_rank_21d},
    "udv_068_selling_intensity_rank_63d": {"inputs": ['close', 'volume'], "func": udv_068_selling_intensity_rank_63d},
    "udv_069_selling_intensity_rank_126d": {"inputs": ['close', 'volume'], "func": udv_069_selling_intensity_rank_126d},
    "udv_070_selling_intensity_rank_252d": {"inputs": ['close', 'volume'], "func": udv_070_selling_intensity_rank_252d},
    "udv_071_vol_force_rank_5d": {"inputs": ['close', 'volume'], "func": udv_071_vol_force_rank_5d},
    "udv_072_vol_force_rank_21d": {"inputs": ['close', 'volume'], "func": udv_072_vol_force_rank_21d},
    "udv_073_vol_force_rank_63d": {"inputs": ['close', 'volume'], "func": udv_073_vol_force_rank_63d},
    "udv_074_vol_force_rank_126d": {"inputs": ['close', 'volume'], "func": udv_074_vol_force_rank_126d},
    "udv_075_vol_force_rank_252d": {"inputs": ['close', 'volume'], "func": udv_075_vol_force_rank_252d},
}
