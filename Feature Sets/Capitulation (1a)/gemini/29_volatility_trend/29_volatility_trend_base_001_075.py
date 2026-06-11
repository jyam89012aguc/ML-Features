"""
Domain 29: volatility_trend (vtrd_)
Asset Class: US Equities
Target Context: Trends and corridors in volatility.
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
def vtrd_001_vol_trend_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5).diff(5)

def vtrd_002_vol_trend_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21).diff(21)

def vtrd_003_vol_trend_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63).diff(63)

def vtrd_004_vol_trend_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126).diff(126)

def vtrd_005_vol_trend_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252).diff(252)

def vtrd_006_vol_ma_ratio_5d(close) -> pd.Series:
    return _safe_div(_rolling_std(_daily_ret(close), 5), _rolling_std(_daily_ret(close), 252))

def vtrd_007_vol_ma_ratio_21d(close) -> pd.Series:
    return _safe_div(_rolling_std(_daily_ret(close), 21), _rolling_std(_daily_ret(close), 252))

def vtrd_008_vol_ma_ratio_63d(close) -> pd.Series:
    return _safe_div(_rolling_std(_daily_ret(close), 63), _rolling_std(_daily_ret(close), 252))

def vtrd_009_vol_ma_ratio_126d(close) -> pd.Series:
    return _safe_div(_rolling_std(_daily_ret(close), 126), _rolling_std(_daily_ret(close), 252))

def vtrd_010_vol_ma_ratio_252d(close) -> pd.Series:
    return _safe_div(_rolling_std(_daily_ret(close), 252), _rolling_std(_daily_ret(close), 252))

def vtrd_011_vol_corridor_5d(close) -> pd.Series:
    return _rolling_max(_rolling_std(_daily_ret(close), 5), 5) - _rolling_min(_rolling_std(_daily_ret(close), 5), 5)

def vtrd_012_vol_corridor_21d(close) -> pd.Series:
    return _rolling_max(_rolling_std(_daily_ret(close), 21), 21) - _rolling_min(_rolling_std(_daily_ret(close), 21), 21)

def vtrd_013_vol_corridor_63d(close) -> pd.Series:
    return _rolling_max(_rolling_std(_daily_ret(close), 63), 63) - _rolling_min(_rolling_std(_daily_ret(close), 63), 63)

def vtrd_014_vol_corridor_126d(close) -> pd.Series:
    return _rolling_max(_rolling_std(_daily_ret(close), 126), 126) - _rolling_min(_rolling_std(_daily_ret(close), 126), 126)

def vtrd_015_vol_corridor_252d(close) -> pd.Series:
    return _rolling_max(_rolling_std(_daily_ret(close), 252), 252) - _rolling_min(_rolling_std(_daily_ret(close), 252), 252)

def vtrd_016_vol_expansion_5d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 5) > _rolling_std(_daily_ret(close), 5).shift(1)).astype(float).rolling(5).sum()

def vtrd_017_vol_expansion_21d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 21) > _rolling_std(_daily_ret(close), 21).shift(1)).astype(float).rolling(21).sum()

def vtrd_018_vol_expansion_63d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 63) > _rolling_std(_daily_ret(close), 63).shift(1)).astype(float).rolling(63).sum()

def vtrd_019_vol_expansion_126d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 126) > _rolling_std(_daily_ret(close), 126).shift(1)).astype(float).rolling(126).sum()

def vtrd_020_vol_expansion_252d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 252) > _rolling_std(_daily_ret(close), 252).shift(1)).astype(float).rolling(252).sum()

def vtrd_021_vol_slope_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5).rolling(5).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0] if len(x)>0 else np.nan, raw=True)

def vtrd_022_vol_slope_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21).rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0] if len(x)>0 else np.nan, raw=True)

def vtrd_023_vol_slope_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63).rolling(63).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0] if len(x)>0 else np.nan, raw=True)

def vtrd_024_vol_slope_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126).rolling(126).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0] if len(x)>0 else np.nan, raw=True)

def vtrd_025_vol_slope_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252).rolling(252).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0] if len(x)>0 else np.nan, raw=True)

def vtrd_026_vol_trend_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vtrd_001_vol_trend_5d(close), 252)

def vtrd_027_vol_trend_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vtrd_002_vol_trend_21d(close), 252)

def vtrd_028_vol_trend_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vtrd_003_vol_trend_63d(close), 252)

def vtrd_029_vol_trend_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vtrd_004_vol_trend_126d(close), 252)

def vtrd_030_vol_trend_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vtrd_005_vol_trend_252d(close), 252)

def vtrd_031_vol_ma_ratio_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vtrd_006_vol_ma_ratio_5d(close), 252)

def vtrd_032_vol_ma_ratio_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vtrd_007_vol_ma_ratio_21d(close), 252)

def vtrd_033_vol_ma_ratio_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vtrd_008_vol_ma_ratio_63d(close), 252)

def vtrd_034_vol_ma_ratio_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vtrd_009_vol_ma_ratio_126d(close), 252)

def vtrd_035_vol_ma_ratio_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vtrd_010_vol_ma_ratio_252d(close), 252)

def vtrd_036_vol_corridor_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vtrd_011_vol_corridor_5d(close), 252)

def vtrd_037_vol_corridor_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vtrd_012_vol_corridor_21d(close), 252)

def vtrd_038_vol_corridor_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vtrd_013_vol_corridor_63d(close), 252)

def vtrd_039_vol_corridor_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vtrd_014_vol_corridor_126d(close), 252)

def vtrd_040_vol_corridor_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vtrd_015_vol_corridor_252d(close), 252)

def vtrd_041_vol_expansion_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vtrd_016_vol_expansion_5d(close), 252)

def vtrd_042_vol_expansion_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vtrd_017_vol_expansion_21d(close), 252)

def vtrd_043_vol_expansion_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vtrd_018_vol_expansion_63d(close), 252)

def vtrd_044_vol_expansion_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vtrd_019_vol_expansion_126d(close), 252)

def vtrd_045_vol_expansion_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vtrd_020_vol_expansion_252d(close), 252)

def vtrd_046_vol_slope_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vtrd_021_vol_slope_5d(close), 252)

def vtrd_047_vol_slope_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vtrd_022_vol_slope_21d(close), 252)

def vtrd_048_vol_slope_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vtrd_023_vol_slope_63d(close), 252)

def vtrd_049_vol_slope_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vtrd_024_vol_slope_126d(close), 252)

def vtrd_050_vol_slope_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vtrd_025_vol_slope_252d(close), 252)

def vtrd_051_vol_trend_rank_5d(close) -> pd.Series:
    return vtrd_001_vol_trend_5d(close).rolling(252).rank(pct=True)

def vtrd_052_vol_trend_rank_21d(close) -> pd.Series:
    return vtrd_002_vol_trend_21d(close).rolling(252).rank(pct=True)

def vtrd_053_vol_trend_rank_63d(close) -> pd.Series:
    return vtrd_003_vol_trend_63d(close).rolling(252).rank(pct=True)

def vtrd_054_vol_trend_rank_126d(close) -> pd.Series:
    return vtrd_004_vol_trend_126d(close).rolling(252).rank(pct=True)

def vtrd_055_vol_trend_rank_252d(close) -> pd.Series:
    return vtrd_005_vol_trend_252d(close).rolling(252).rank(pct=True)

def vtrd_056_vol_ma_ratio_rank_5d(close) -> pd.Series:
    return vtrd_006_vol_ma_ratio_5d(close).rolling(252).rank(pct=True)

def vtrd_057_vol_ma_ratio_rank_21d(close) -> pd.Series:
    return vtrd_007_vol_ma_ratio_21d(close).rolling(252).rank(pct=True)

def vtrd_058_vol_ma_ratio_rank_63d(close) -> pd.Series:
    return vtrd_008_vol_ma_ratio_63d(close).rolling(252).rank(pct=True)

def vtrd_059_vol_ma_ratio_rank_126d(close) -> pd.Series:
    return vtrd_009_vol_ma_ratio_126d(close).rolling(252).rank(pct=True)

def vtrd_060_vol_ma_ratio_rank_252d(close) -> pd.Series:
    return vtrd_010_vol_ma_ratio_252d(close).rolling(252).rank(pct=True)

def vtrd_061_vol_corridor_rank_5d(close) -> pd.Series:
    return vtrd_011_vol_corridor_5d(close).rolling(252).rank(pct=True)

def vtrd_062_vol_corridor_rank_21d(close) -> pd.Series:
    return vtrd_012_vol_corridor_21d(close).rolling(252).rank(pct=True)

def vtrd_063_vol_corridor_rank_63d(close) -> pd.Series:
    return vtrd_013_vol_corridor_63d(close).rolling(252).rank(pct=True)

def vtrd_064_vol_corridor_rank_126d(close) -> pd.Series:
    return vtrd_014_vol_corridor_126d(close).rolling(252).rank(pct=True)

def vtrd_065_vol_corridor_rank_252d(close) -> pd.Series:
    return vtrd_015_vol_corridor_252d(close).rolling(252).rank(pct=True)

def vtrd_066_vol_expansion_rank_5d(close) -> pd.Series:
    return vtrd_016_vol_expansion_5d(close).rolling(252).rank(pct=True)

def vtrd_067_vol_expansion_rank_21d(close) -> pd.Series:
    return vtrd_017_vol_expansion_21d(close).rolling(252).rank(pct=True)

def vtrd_068_vol_expansion_rank_63d(close) -> pd.Series:
    return vtrd_018_vol_expansion_63d(close).rolling(252).rank(pct=True)

def vtrd_069_vol_expansion_rank_126d(close) -> pd.Series:
    return vtrd_019_vol_expansion_126d(close).rolling(252).rank(pct=True)

def vtrd_070_vol_expansion_rank_252d(close) -> pd.Series:
    return vtrd_020_vol_expansion_252d(close).rolling(252).rank(pct=True)

def vtrd_071_vol_slope_rank_5d(close) -> pd.Series:
    return vtrd_021_vol_slope_5d(close).rolling(252).rank(pct=True)

def vtrd_072_vol_slope_rank_21d(close) -> pd.Series:
    return vtrd_022_vol_slope_21d(close).rolling(252).rank(pct=True)

def vtrd_073_vol_slope_rank_63d(close) -> pd.Series:
    return vtrd_023_vol_slope_63d(close).rolling(252).rank(pct=True)

def vtrd_074_vol_slope_rank_126d(close) -> pd.Series:
    return vtrd_024_vol_slope_126d(close).rolling(252).rank(pct=True)

def vtrd_075_vol_slope_rank_252d(close) -> pd.Series:
    return vtrd_025_vol_slope_252d(close).rolling(252).rank(pct=True)


# --- Registry ---
V29_REGISTRY = {
    "vtrd_001_vol_trend_5d": {"inputs": ['close'], "func": vtrd_001_vol_trend_5d},
    "vtrd_002_vol_trend_21d": {"inputs": ['close'], "func": vtrd_002_vol_trend_21d},
    "vtrd_003_vol_trend_63d": {"inputs": ['close'], "func": vtrd_003_vol_trend_63d},
    "vtrd_004_vol_trend_126d": {"inputs": ['close'], "func": vtrd_004_vol_trend_126d},
    "vtrd_005_vol_trend_252d": {"inputs": ['close'], "func": vtrd_005_vol_trend_252d},
    "vtrd_006_vol_ma_ratio_5d": {"inputs": ['close'], "func": vtrd_006_vol_ma_ratio_5d},
    "vtrd_007_vol_ma_ratio_21d": {"inputs": ['close'], "func": vtrd_007_vol_ma_ratio_21d},
    "vtrd_008_vol_ma_ratio_63d": {"inputs": ['close'], "func": vtrd_008_vol_ma_ratio_63d},
    "vtrd_009_vol_ma_ratio_126d": {"inputs": ['close'], "func": vtrd_009_vol_ma_ratio_126d},
    "vtrd_010_vol_ma_ratio_252d": {"inputs": ['close'], "func": vtrd_010_vol_ma_ratio_252d},
    "vtrd_011_vol_corridor_5d": {"inputs": ['close'], "func": vtrd_011_vol_corridor_5d},
    "vtrd_012_vol_corridor_21d": {"inputs": ['close'], "func": vtrd_012_vol_corridor_21d},
    "vtrd_013_vol_corridor_63d": {"inputs": ['close'], "func": vtrd_013_vol_corridor_63d},
    "vtrd_014_vol_corridor_126d": {"inputs": ['close'], "func": vtrd_014_vol_corridor_126d},
    "vtrd_015_vol_corridor_252d": {"inputs": ['close'], "func": vtrd_015_vol_corridor_252d},
    "vtrd_016_vol_expansion_5d": {"inputs": ['close'], "func": vtrd_016_vol_expansion_5d},
    "vtrd_017_vol_expansion_21d": {"inputs": ['close'], "func": vtrd_017_vol_expansion_21d},
    "vtrd_018_vol_expansion_63d": {"inputs": ['close'], "func": vtrd_018_vol_expansion_63d},
    "vtrd_019_vol_expansion_126d": {"inputs": ['close'], "func": vtrd_019_vol_expansion_126d},
    "vtrd_020_vol_expansion_252d": {"inputs": ['close'], "func": vtrd_020_vol_expansion_252d},
    "vtrd_021_vol_slope_5d": {"inputs": ['close'], "func": vtrd_021_vol_slope_5d},
    "vtrd_022_vol_slope_21d": {"inputs": ['close'], "func": vtrd_022_vol_slope_21d},
    "vtrd_023_vol_slope_63d": {"inputs": ['close'], "func": vtrd_023_vol_slope_63d},
    "vtrd_024_vol_slope_126d": {"inputs": ['close'], "func": vtrd_024_vol_slope_126d},
    "vtrd_025_vol_slope_252d": {"inputs": ['close'], "func": vtrd_025_vol_slope_252d},
    "vtrd_026_vol_trend_zscore_5d": {"inputs": ['close'], "func": vtrd_026_vol_trend_zscore_5d},
    "vtrd_027_vol_trend_zscore_21d": {"inputs": ['close'], "func": vtrd_027_vol_trend_zscore_21d},
    "vtrd_028_vol_trend_zscore_63d": {"inputs": ['close'], "func": vtrd_028_vol_trend_zscore_63d},
    "vtrd_029_vol_trend_zscore_126d": {"inputs": ['close'], "func": vtrd_029_vol_trend_zscore_126d},
    "vtrd_030_vol_trend_zscore_252d": {"inputs": ['close'], "func": vtrd_030_vol_trend_zscore_252d},
    "vtrd_031_vol_ma_ratio_zscore_5d": {"inputs": ['close'], "func": vtrd_031_vol_ma_ratio_zscore_5d},
    "vtrd_032_vol_ma_ratio_zscore_21d": {"inputs": ['close'], "func": vtrd_032_vol_ma_ratio_zscore_21d},
    "vtrd_033_vol_ma_ratio_zscore_63d": {"inputs": ['close'], "func": vtrd_033_vol_ma_ratio_zscore_63d},
    "vtrd_034_vol_ma_ratio_zscore_126d": {"inputs": ['close'], "func": vtrd_034_vol_ma_ratio_zscore_126d},
    "vtrd_035_vol_ma_ratio_zscore_252d": {"inputs": ['close'], "func": vtrd_035_vol_ma_ratio_zscore_252d},
    "vtrd_036_vol_corridor_zscore_5d": {"inputs": ['close'], "func": vtrd_036_vol_corridor_zscore_5d},
    "vtrd_037_vol_corridor_zscore_21d": {"inputs": ['close'], "func": vtrd_037_vol_corridor_zscore_21d},
    "vtrd_038_vol_corridor_zscore_63d": {"inputs": ['close'], "func": vtrd_038_vol_corridor_zscore_63d},
    "vtrd_039_vol_corridor_zscore_126d": {"inputs": ['close'], "func": vtrd_039_vol_corridor_zscore_126d},
    "vtrd_040_vol_corridor_zscore_252d": {"inputs": ['close'], "func": vtrd_040_vol_corridor_zscore_252d},
    "vtrd_041_vol_expansion_zscore_5d": {"inputs": ['close'], "func": vtrd_041_vol_expansion_zscore_5d},
    "vtrd_042_vol_expansion_zscore_21d": {"inputs": ['close'], "func": vtrd_042_vol_expansion_zscore_21d},
    "vtrd_043_vol_expansion_zscore_63d": {"inputs": ['close'], "func": vtrd_043_vol_expansion_zscore_63d},
    "vtrd_044_vol_expansion_zscore_126d": {"inputs": ['close'], "func": vtrd_044_vol_expansion_zscore_126d},
    "vtrd_045_vol_expansion_zscore_252d": {"inputs": ['close'], "func": vtrd_045_vol_expansion_zscore_252d},
    "vtrd_046_vol_slope_zscore_5d": {"inputs": ['close'], "func": vtrd_046_vol_slope_zscore_5d},
    "vtrd_047_vol_slope_zscore_21d": {"inputs": ['close'], "func": vtrd_047_vol_slope_zscore_21d},
    "vtrd_048_vol_slope_zscore_63d": {"inputs": ['close'], "func": vtrd_048_vol_slope_zscore_63d},
    "vtrd_049_vol_slope_zscore_126d": {"inputs": ['close'], "func": vtrd_049_vol_slope_zscore_126d},
    "vtrd_050_vol_slope_zscore_252d": {"inputs": ['close'], "func": vtrd_050_vol_slope_zscore_252d},
    "vtrd_051_vol_trend_rank_5d": {"inputs": ['close'], "func": vtrd_051_vol_trend_rank_5d},
    "vtrd_052_vol_trend_rank_21d": {"inputs": ['close'], "func": vtrd_052_vol_trend_rank_21d},
    "vtrd_053_vol_trend_rank_63d": {"inputs": ['close'], "func": vtrd_053_vol_trend_rank_63d},
    "vtrd_054_vol_trend_rank_126d": {"inputs": ['close'], "func": vtrd_054_vol_trend_rank_126d},
    "vtrd_055_vol_trend_rank_252d": {"inputs": ['close'], "func": vtrd_055_vol_trend_rank_252d},
    "vtrd_056_vol_ma_ratio_rank_5d": {"inputs": ['close'], "func": vtrd_056_vol_ma_ratio_rank_5d},
    "vtrd_057_vol_ma_ratio_rank_21d": {"inputs": ['close'], "func": vtrd_057_vol_ma_ratio_rank_21d},
    "vtrd_058_vol_ma_ratio_rank_63d": {"inputs": ['close'], "func": vtrd_058_vol_ma_ratio_rank_63d},
    "vtrd_059_vol_ma_ratio_rank_126d": {"inputs": ['close'], "func": vtrd_059_vol_ma_ratio_rank_126d},
    "vtrd_060_vol_ma_ratio_rank_252d": {"inputs": ['close'], "func": vtrd_060_vol_ma_ratio_rank_252d},
    "vtrd_061_vol_corridor_rank_5d": {"inputs": ['close'], "func": vtrd_061_vol_corridor_rank_5d},
    "vtrd_062_vol_corridor_rank_21d": {"inputs": ['close'], "func": vtrd_062_vol_corridor_rank_21d},
    "vtrd_063_vol_corridor_rank_63d": {"inputs": ['close'], "func": vtrd_063_vol_corridor_rank_63d},
    "vtrd_064_vol_corridor_rank_126d": {"inputs": ['close'], "func": vtrd_064_vol_corridor_rank_126d},
    "vtrd_065_vol_corridor_rank_252d": {"inputs": ['close'], "func": vtrd_065_vol_corridor_rank_252d},
    "vtrd_066_vol_expansion_rank_5d": {"inputs": ['close'], "func": vtrd_066_vol_expansion_rank_5d},
    "vtrd_067_vol_expansion_rank_21d": {"inputs": ['close'], "func": vtrd_067_vol_expansion_rank_21d},
    "vtrd_068_vol_expansion_rank_63d": {"inputs": ['close'], "func": vtrd_068_vol_expansion_rank_63d},
    "vtrd_069_vol_expansion_rank_126d": {"inputs": ['close'], "func": vtrd_069_vol_expansion_rank_126d},
    "vtrd_070_vol_expansion_rank_252d": {"inputs": ['close'], "func": vtrd_070_vol_expansion_rank_252d},
    "vtrd_071_vol_slope_rank_5d": {"inputs": ['close'], "func": vtrd_071_vol_slope_rank_5d},
    "vtrd_072_vol_slope_rank_21d": {"inputs": ['close'], "func": vtrd_072_vol_slope_rank_21d},
    "vtrd_073_vol_slope_rank_63d": {"inputs": ['close'], "func": vtrd_073_vol_slope_rank_63d},
    "vtrd_074_vol_slope_rank_126d": {"inputs": ['close'], "func": vtrd_074_vol_slope_rank_126d},
    "vtrd_075_vol_slope_rank_252d": {"inputs": ['close'], "func": vtrd_075_vol_slope_rank_252d},
}
