"""
Domain 19: volume_trend (vtr_)
Asset Class: US Equities
Target Context: Volume moving average trends and quality.
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
def vtr_001_vol_ma_ratio_5d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 5), _rolling_mean(volume, 252))

def vtr_002_vol_ma_ratio_21d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 21), _rolling_mean(volume, 252))

def vtr_003_vol_ma_ratio_63d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 63), _rolling_mean(volume, 252))

def vtr_004_vol_ma_ratio_126d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 126), _rolling_mean(volume, 252))

def vtr_005_vol_ma_ratio_252d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 252), _rolling_mean(volume, 252))

def vtr_006_vol_trend_slope_5d(volume) -> pd.Series:
    return _rolling_mean(volume, 5).diff(5)

def vtr_007_vol_trend_slope_21d(volume) -> pd.Series:
    return _rolling_mean(volume, 21).diff(21)

def vtr_008_vol_trend_slope_63d(volume) -> pd.Series:
    return _rolling_mean(volume, 63).diff(63)

def vtr_009_vol_trend_slope_126d(volume) -> pd.Series:
    return _rolling_mean(volume, 126).diff(126)

def vtr_010_vol_trend_slope_252d(volume) -> pd.Series:
    return _rolling_mean(volume, 252).diff(252)

def vtr_011_vol_ad_line_5d(close, high, low, volume) -> pd.Series:
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS)) * volume).rolling(5).sum()

def vtr_012_vol_ad_line_21d(close, high, low, volume) -> pd.Series:
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS)) * volume).rolling(21).sum()

def vtr_013_vol_ad_line_63d(close, high, low, volume) -> pd.Series:
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS)) * volume).rolling(63).sum()

def vtr_014_vol_ad_line_126d(close, high, low, volume) -> pd.Series:
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS)) * volume).rolling(126).sum()

def vtr_015_vol_ad_line_252d(close, high, low, volume) -> pd.Series:
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS)) * volume).rolling(252).sum()

def vtr_016_vol_trend_quality_5d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 5), _rolling_std(volume, 5))

def vtr_017_vol_trend_quality_21d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 21), _rolling_std(volume, 21))

def vtr_018_vol_trend_quality_63d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 63), _rolling_std(volume, 63))

def vtr_019_vol_trend_quality_126d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 126), _rolling_std(volume, 126))

def vtr_020_vol_trend_quality_252d(volume) -> pd.Series:
    return _safe_div(_rolling_mean(volume, 252), _rolling_std(volume, 252))

def vtr_021_vol_momentum_5d(volume) -> pd.Series:
    return _daily_ret(_rolling_mean(volume, 5))

def vtr_022_vol_momentum_21d(volume) -> pd.Series:
    return _daily_ret(_rolling_mean(volume, 21))

def vtr_023_vol_momentum_63d(volume) -> pd.Series:
    return _daily_ret(_rolling_mean(volume, 63))

def vtr_024_vol_momentum_126d(volume) -> pd.Series:
    return _daily_ret(_rolling_mean(volume, 126))

def vtr_025_vol_momentum_252d(volume) -> pd.Series:
    return _daily_ret(_rolling_mean(volume, 252))

def vtr_026_vol_ma_ratio_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vtr_001_vol_ma_ratio_5d(volume), 252)

def vtr_027_vol_ma_ratio_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vtr_002_vol_ma_ratio_21d(volume), 252)

def vtr_028_vol_ma_ratio_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vtr_003_vol_ma_ratio_63d(volume), 252)

def vtr_029_vol_ma_ratio_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vtr_004_vol_ma_ratio_126d(volume), 252)

def vtr_030_vol_ma_ratio_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vtr_005_vol_ma_ratio_252d(volume), 252)

def vtr_031_vol_trend_slope_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vtr_006_vol_trend_slope_5d(volume), 252)

def vtr_032_vol_trend_slope_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vtr_007_vol_trend_slope_21d(volume), 252)

def vtr_033_vol_trend_slope_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vtr_008_vol_trend_slope_63d(volume), 252)

def vtr_034_vol_trend_slope_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vtr_009_vol_trend_slope_126d(volume), 252)

def vtr_035_vol_trend_slope_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vtr_010_vol_trend_slope_252d(volume), 252)

def vtr_036_vol_ad_line_zscore_5d(close, high, low, volume) -> pd.Series:
    return _zscore_rolling(vtr_011_vol_ad_line_5d(close, high, low, volume), 252)

def vtr_037_vol_ad_line_zscore_21d(close, high, low, volume) -> pd.Series:
    return _zscore_rolling(vtr_012_vol_ad_line_21d(close, high, low, volume), 252)

def vtr_038_vol_ad_line_zscore_63d(close, high, low, volume) -> pd.Series:
    return _zscore_rolling(vtr_013_vol_ad_line_63d(close, high, low, volume), 252)

def vtr_039_vol_ad_line_zscore_126d(close, high, low, volume) -> pd.Series:
    return _zscore_rolling(vtr_014_vol_ad_line_126d(close, high, low, volume), 252)

def vtr_040_vol_ad_line_zscore_252d(close, high, low, volume) -> pd.Series:
    return _zscore_rolling(vtr_015_vol_ad_line_252d(close, high, low, volume), 252)

def vtr_041_vol_trend_quality_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vtr_016_vol_trend_quality_5d(volume), 252)

def vtr_042_vol_trend_quality_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vtr_017_vol_trend_quality_21d(volume), 252)

def vtr_043_vol_trend_quality_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vtr_018_vol_trend_quality_63d(volume), 252)

def vtr_044_vol_trend_quality_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vtr_019_vol_trend_quality_126d(volume), 252)

def vtr_045_vol_trend_quality_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vtr_020_vol_trend_quality_252d(volume), 252)

def vtr_046_vol_momentum_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vtr_021_vol_momentum_5d(volume), 252)

def vtr_047_vol_momentum_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vtr_022_vol_momentum_21d(volume), 252)

def vtr_048_vol_momentum_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vtr_023_vol_momentum_63d(volume), 252)

def vtr_049_vol_momentum_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vtr_024_vol_momentum_126d(volume), 252)

def vtr_050_vol_momentum_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vtr_025_vol_momentum_252d(volume), 252)

def vtr_051_vol_ma_ratio_rank_5d(volume) -> pd.Series:
    return vtr_001_vol_ma_ratio_5d(volume).rolling(252).rank(pct=True)

def vtr_052_vol_ma_ratio_rank_21d(volume) -> pd.Series:
    return vtr_002_vol_ma_ratio_21d(volume).rolling(252).rank(pct=True)

def vtr_053_vol_ma_ratio_rank_63d(volume) -> pd.Series:
    return vtr_003_vol_ma_ratio_63d(volume).rolling(252).rank(pct=True)

def vtr_054_vol_ma_ratio_rank_126d(volume) -> pd.Series:
    return vtr_004_vol_ma_ratio_126d(volume).rolling(252).rank(pct=True)

def vtr_055_vol_ma_ratio_rank_252d(volume) -> pd.Series:
    return vtr_005_vol_ma_ratio_252d(volume).rolling(252).rank(pct=True)

def vtr_056_vol_trend_slope_rank_5d(volume) -> pd.Series:
    return vtr_006_vol_trend_slope_5d(volume).rolling(252).rank(pct=True)

def vtr_057_vol_trend_slope_rank_21d(volume) -> pd.Series:
    return vtr_007_vol_trend_slope_21d(volume).rolling(252).rank(pct=True)

def vtr_058_vol_trend_slope_rank_63d(volume) -> pd.Series:
    return vtr_008_vol_trend_slope_63d(volume).rolling(252).rank(pct=True)

def vtr_059_vol_trend_slope_rank_126d(volume) -> pd.Series:
    return vtr_009_vol_trend_slope_126d(volume).rolling(252).rank(pct=True)

def vtr_060_vol_trend_slope_rank_252d(volume) -> pd.Series:
    return vtr_010_vol_trend_slope_252d(volume).rolling(252).rank(pct=True)

def vtr_061_vol_ad_line_rank_5d(close, high, low, volume) -> pd.Series:
    return vtr_011_vol_ad_line_5d(close, high, low, volume).rolling(252).rank(pct=True)

def vtr_062_vol_ad_line_rank_21d(close, high, low, volume) -> pd.Series:
    return vtr_012_vol_ad_line_21d(close, high, low, volume).rolling(252).rank(pct=True)

def vtr_063_vol_ad_line_rank_63d(close, high, low, volume) -> pd.Series:
    return vtr_013_vol_ad_line_63d(close, high, low, volume).rolling(252).rank(pct=True)

def vtr_064_vol_ad_line_rank_126d(close, high, low, volume) -> pd.Series:
    return vtr_014_vol_ad_line_126d(close, high, low, volume).rolling(252).rank(pct=True)

def vtr_065_vol_ad_line_rank_252d(close, high, low, volume) -> pd.Series:
    return vtr_015_vol_ad_line_252d(close, high, low, volume).rolling(252).rank(pct=True)

def vtr_066_vol_trend_quality_rank_5d(volume) -> pd.Series:
    return vtr_016_vol_trend_quality_5d(volume).rolling(252).rank(pct=True)

def vtr_067_vol_trend_quality_rank_21d(volume) -> pd.Series:
    return vtr_017_vol_trend_quality_21d(volume).rolling(252).rank(pct=True)

def vtr_068_vol_trend_quality_rank_63d(volume) -> pd.Series:
    return vtr_018_vol_trend_quality_63d(volume).rolling(252).rank(pct=True)

def vtr_069_vol_trend_quality_rank_126d(volume) -> pd.Series:
    return vtr_019_vol_trend_quality_126d(volume).rolling(252).rank(pct=True)

def vtr_070_vol_trend_quality_rank_252d(volume) -> pd.Series:
    return vtr_020_vol_trend_quality_252d(volume).rolling(252).rank(pct=True)

def vtr_071_vol_momentum_rank_5d(volume) -> pd.Series:
    return vtr_021_vol_momentum_5d(volume).rolling(252).rank(pct=True)

def vtr_072_vol_momentum_rank_21d(volume) -> pd.Series:
    return vtr_022_vol_momentum_21d(volume).rolling(252).rank(pct=True)

def vtr_073_vol_momentum_rank_63d(volume) -> pd.Series:
    return vtr_023_vol_momentum_63d(volume).rolling(252).rank(pct=True)

def vtr_074_vol_momentum_rank_126d(volume) -> pd.Series:
    return vtr_024_vol_momentum_126d(volume).rolling(252).rank(pct=True)

def vtr_075_vol_momentum_rank_252d(volume) -> pd.Series:
    return vtr_025_vol_momentum_252d(volume).rolling(252).rank(pct=True)


# --- Registry ---
V19_REGISTRY = {
    "vtr_001_vol_ma_ratio_5d": {"inputs": ['volume'], "func": vtr_001_vol_ma_ratio_5d},
    "vtr_002_vol_ma_ratio_21d": {"inputs": ['volume'], "func": vtr_002_vol_ma_ratio_21d},
    "vtr_003_vol_ma_ratio_63d": {"inputs": ['volume'], "func": vtr_003_vol_ma_ratio_63d},
    "vtr_004_vol_ma_ratio_126d": {"inputs": ['volume'], "func": vtr_004_vol_ma_ratio_126d},
    "vtr_005_vol_ma_ratio_252d": {"inputs": ['volume'], "func": vtr_005_vol_ma_ratio_252d},
    "vtr_006_vol_trend_slope_5d": {"inputs": ['volume'], "func": vtr_006_vol_trend_slope_5d},
    "vtr_007_vol_trend_slope_21d": {"inputs": ['volume'], "func": vtr_007_vol_trend_slope_21d},
    "vtr_008_vol_trend_slope_63d": {"inputs": ['volume'], "func": vtr_008_vol_trend_slope_63d},
    "vtr_009_vol_trend_slope_126d": {"inputs": ['volume'], "func": vtr_009_vol_trend_slope_126d},
    "vtr_010_vol_trend_slope_252d": {"inputs": ['volume'], "func": vtr_010_vol_trend_slope_252d},
    "vtr_011_vol_ad_line_5d": {"inputs": ['close', 'high', 'low', 'volume'], "func": vtr_011_vol_ad_line_5d},
    "vtr_012_vol_ad_line_21d": {"inputs": ['close', 'high', 'low', 'volume'], "func": vtr_012_vol_ad_line_21d},
    "vtr_013_vol_ad_line_63d": {"inputs": ['close', 'high', 'low', 'volume'], "func": vtr_013_vol_ad_line_63d},
    "vtr_014_vol_ad_line_126d": {"inputs": ['close', 'high', 'low', 'volume'], "func": vtr_014_vol_ad_line_126d},
    "vtr_015_vol_ad_line_252d": {"inputs": ['close', 'high', 'low', 'volume'], "func": vtr_015_vol_ad_line_252d},
    "vtr_016_vol_trend_quality_5d": {"inputs": ['volume'], "func": vtr_016_vol_trend_quality_5d},
    "vtr_017_vol_trend_quality_21d": {"inputs": ['volume'], "func": vtr_017_vol_trend_quality_21d},
    "vtr_018_vol_trend_quality_63d": {"inputs": ['volume'], "func": vtr_018_vol_trend_quality_63d},
    "vtr_019_vol_trend_quality_126d": {"inputs": ['volume'], "func": vtr_019_vol_trend_quality_126d},
    "vtr_020_vol_trend_quality_252d": {"inputs": ['volume'], "func": vtr_020_vol_trend_quality_252d},
    "vtr_021_vol_momentum_5d": {"inputs": ['volume'], "func": vtr_021_vol_momentum_5d},
    "vtr_022_vol_momentum_21d": {"inputs": ['volume'], "func": vtr_022_vol_momentum_21d},
    "vtr_023_vol_momentum_63d": {"inputs": ['volume'], "func": vtr_023_vol_momentum_63d},
    "vtr_024_vol_momentum_126d": {"inputs": ['volume'], "func": vtr_024_vol_momentum_126d},
    "vtr_025_vol_momentum_252d": {"inputs": ['volume'], "func": vtr_025_vol_momentum_252d},
    "vtr_026_vol_ma_ratio_zscore_5d": {"inputs": ['volume'], "func": vtr_026_vol_ma_ratio_zscore_5d},
    "vtr_027_vol_ma_ratio_zscore_21d": {"inputs": ['volume'], "func": vtr_027_vol_ma_ratio_zscore_21d},
    "vtr_028_vol_ma_ratio_zscore_63d": {"inputs": ['volume'], "func": vtr_028_vol_ma_ratio_zscore_63d},
    "vtr_029_vol_ma_ratio_zscore_126d": {"inputs": ['volume'], "func": vtr_029_vol_ma_ratio_zscore_126d},
    "vtr_030_vol_ma_ratio_zscore_252d": {"inputs": ['volume'], "func": vtr_030_vol_ma_ratio_zscore_252d},
    "vtr_031_vol_trend_slope_zscore_5d": {"inputs": ['volume'], "func": vtr_031_vol_trend_slope_zscore_5d},
    "vtr_032_vol_trend_slope_zscore_21d": {"inputs": ['volume'], "func": vtr_032_vol_trend_slope_zscore_21d},
    "vtr_033_vol_trend_slope_zscore_63d": {"inputs": ['volume'], "func": vtr_033_vol_trend_slope_zscore_63d},
    "vtr_034_vol_trend_slope_zscore_126d": {"inputs": ['volume'], "func": vtr_034_vol_trend_slope_zscore_126d},
    "vtr_035_vol_trend_slope_zscore_252d": {"inputs": ['volume'], "func": vtr_035_vol_trend_slope_zscore_252d},
    "vtr_036_vol_ad_line_zscore_5d": {"inputs": ['close', 'high', 'low', 'volume'], "func": vtr_036_vol_ad_line_zscore_5d},
    "vtr_037_vol_ad_line_zscore_21d": {"inputs": ['close', 'high', 'low', 'volume'], "func": vtr_037_vol_ad_line_zscore_21d},
    "vtr_038_vol_ad_line_zscore_63d": {"inputs": ['close', 'high', 'low', 'volume'], "func": vtr_038_vol_ad_line_zscore_63d},
    "vtr_039_vol_ad_line_zscore_126d": {"inputs": ['close', 'high', 'low', 'volume'], "func": vtr_039_vol_ad_line_zscore_126d},
    "vtr_040_vol_ad_line_zscore_252d": {"inputs": ['close', 'high', 'low', 'volume'], "func": vtr_040_vol_ad_line_zscore_252d},
    "vtr_041_vol_trend_quality_zscore_5d": {"inputs": ['volume'], "func": vtr_041_vol_trend_quality_zscore_5d},
    "vtr_042_vol_trend_quality_zscore_21d": {"inputs": ['volume'], "func": vtr_042_vol_trend_quality_zscore_21d},
    "vtr_043_vol_trend_quality_zscore_63d": {"inputs": ['volume'], "func": vtr_043_vol_trend_quality_zscore_63d},
    "vtr_044_vol_trend_quality_zscore_126d": {"inputs": ['volume'], "func": vtr_044_vol_trend_quality_zscore_126d},
    "vtr_045_vol_trend_quality_zscore_252d": {"inputs": ['volume'], "func": vtr_045_vol_trend_quality_zscore_252d},
    "vtr_046_vol_momentum_zscore_5d": {"inputs": ['volume'], "func": vtr_046_vol_momentum_zscore_5d},
    "vtr_047_vol_momentum_zscore_21d": {"inputs": ['volume'], "func": vtr_047_vol_momentum_zscore_21d},
    "vtr_048_vol_momentum_zscore_63d": {"inputs": ['volume'], "func": vtr_048_vol_momentum_zscore_63d},
    "vtr_049_vol_momentum_zscore_126d": {"inputs": ['volume'], "func": vtr_049_vol_momentum_zscore_126d},
    "vtr_050_vol_momentum_zscore_252d": {"inputs": ['volume'], "func": vtr_050_vol_momentum_zscore_252d},
    "vtr_051_vol_ma_ratio_rank_5d": {"inputs": ['volume'], "func": vtr_051_vol_ma_ratio_rank_5d},
    "vtr_052_vol_ma_ratio_rank_21d": {"inputs": ['volume'], "func": vtr_052_vol_ma_ratio_rank_21d},
    "vtr_053_vol_ma_ratio_rank_63d": {"inputs": ['volume'], "func": vtr_053_vol_ma_ratio_rank_63d},
    "vtr_054_vol_ma_ratio_rank_126d": {"inputs": ['volume'], "func": vtr_054_vol_ma_ratio_rank_126d},
    "vtr_055_vol_ma_ratio_rank_252d": {"inputs": ['volume'], "func": vtr_055_vol_ma_ratio_rank_252d},
    "vtr_056_vol_trend_slope_rank_5d": {"inputs": ['volume'], "func": vtr_056_vol_trend_slope_rank_5d},
    "vtr_057_vol_trend_slope_rank_21d": {"inputs": ['volume'], "func": vtr_057_vol_trend_slope_rank_21d},
    "vtr_058_vol_trend_slope_rank_63d": {"inputs": ['volume'], "func": vtr_058_vol_trend_slope_rank_63d},
    "vtr_059_vol_trend_slope_rank_126d": {"inputs": ['volume'], "func": vtr_059_vol_trend_slope_rank_126d},
    "vtr_060_vol_trend_slope_rank_252d": {"inputs": ['volume'], "func": vtr_060_vol_trend_slope_rank_252d},
    "vtr_061_vol_ad_line_rank_5d": {"inputs": ['close', 'high', 'low', 'volume'], "func": vtr_061_vol_ad_line_rank_5d},
    "vtr_062_vol_ad_line_rank_21d": {"inputs": ['close', 'high', 'low', 'volume'], "func": vtr_062_vol_ad_line_rank_21d},
    "vtr_063_vol_ad_line_rank_63d": {"inputs": ['close', 'high', 'low', 'volume'], "func": vtr_063_vol_ad_line_rank_63d},
    "vtr_064_vol_ad_line_rank_126d": {"inputs": ['close', 'high', 'low', 'volume'], "func": vtr_064_vol_ad_line_rank_126d},
    "vtr_065_vol_ad_line_rank_252d": {"inputs": ['close', 'high', 'low', 'volume'], "func": vtr_065_vol_ad_line_rank_252d},
    "vtr_066_vol_trend_quality_rank_5d": {"inputs": ['volume'], "func": vtr_066_vol_trend_quality_rank_5d},
    "vtr_067_vol_trend_quality_rank_21d": {"inputs": ['volume'], "func": vtr_067_vol_trend_quality_rank_21d},
    "vtr_068_vol_trend_quality_rank_63d": {"inputs": ['volume'], "func": vtr_068_vol_trend_quality_rank_63d},
    "vtr_069_vol_trend_quality_rank_126d": {"inputs": ['volume'], "func": vtr_069_vol_trend_quality_rank_126d},
    "vtr_070_vol_trend_quality_rank_252d": {"inputs": ['volume'], "func": vtr_070_vol_trend_quality_rank_252d},
    "vtr_071_vol_momentum_rank_5d": {"inputs": ['volume'], "func": vtr_071_vol_momentum_rank_5d},
    "vtr_072_vol_momentum_rank_21d": {"inputs": ['volume'], "func": vtr_072_vol_momentum_rank_21d},
    "vtr_073_vol_momentum_rank_63d": {"inputs": ['volume'], "func": vtr_073_vol_momentum_rank_63d},
    "vtr_074_vol_momentum_rank_126d": {"inputs": ['volume'], "func": vtr_074_vol_momentum_rank_126d},
    "vtr_075_vol_momentum_rank_252d": {"inputs": ['volume'], "func": vtr_075_vol_momentum_rank_252d},
}
