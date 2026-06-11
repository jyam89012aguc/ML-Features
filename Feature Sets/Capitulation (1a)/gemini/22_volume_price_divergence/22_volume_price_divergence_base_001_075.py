"""
Domain 22: volume_price_divergence (vpd_)
Asset Class: US Equities
Target Context: Divergence between price action and volume.
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
def vpd_001_div_magnitude_5d(close, volume) -> pd.Series:
    return (_daily_ret(close).abs() - _daily_ret(volume).abs()).rolling(5).mean()

def vpd_002_div_magnitude_21d(close, volume) -> pd.Series:
    return (_daily_ret(close).abs() - _daily_ret(volume).abs()).rolling(21).mean()

def vpd_003_div_magnitude_63d(close, volume) -> pd.Series:
    return (_daily_ret(close).abs() - _daily_ret(volume).abs()).rolling(63).mean()

def vpd_004_div_magnitude_126d(close, volume) -> pd.Series:
    return (_daily_ret(close).abs() - _daily_ret(volume).abs()).rolling(126).mean()

def vpd_005_div_magnitude_252d(close, volume) -> pd.Series:
    return (_daily_ret(close).abs() - _daily_ret(volume).abs()).rolling(252).mean()

def vpd_006_div_duration_5d(close, volume) -> pd.Series:
    return (np.sign(_daily_ret(close)) != np.sign(_daily_ret(volume))).astype(float).rolling(5).sum()

def vpd_007_div_duration_21d(close, volume) -> pd.Series:
    return (np.sign(_daily_ret(close)) != np.sign(_daily_ret(volume))).astype(float).rolling(21).sum()

def vpd_008_div_duration_63d(close, volume) -> pd.Series:
    return (np.sign(_daily_ret(close)) != np.sign(_daily_ret(volume))).astype(float).rolling(63).sum()

def vpd_009_div_duration_126d(close, volume) -> pd.Series:
    return (np.sign(_daily_ret(close)) != np.sign(_daily_ret(volume))).astype(float).rolling(126).sum()

def vpd_010_div_duration_252d(close, volume) -> pd.Series:
    return (np.sign(_daily_ret(close)) != np.sign(_daily_ret(volume))).astype(float).rolling(252).sum()

def vpd_011_price_up_vol_down_5d(close, volume) -> pd.Series:
    return ((close > close.shift(1)) & (volume < volume.shift(1))).astype(float).rolling(5).sum()

def vpd_012_price_up_vol_down_21d(close, volume) -> pd.Series:
    return ((close > close.shift(1)) & (volume < volume.shift(1))).astype(float).rolling(21).sum()

def vpd_013_price_up_vol_down_63d(close, volume) -> pd.Series:
    return ((close > close.shift(1)) & (volume < volume.shift(1))).astype(float).rolling(63).sum()

def vpd_014_price_up_vol_down_126d(close, volume) -> pd.Series:
    return ((close > close.shift(1)) & (volume < volume.shift(1))).astype(float).rolling(126).sum()

def vpd_015_price_up_vol_down_252d(close, volume) -> pd.Series:
    return ((close > close.shift(1)) & (volume < volume.shift(1))).astype(float).rolling(252).sum()

def vpd_016_price_down_vol_up_5d(close, volume) -> pd.Series:
    return ((close < close.shift(1)) & (volume > volume.shift(1))).astype(float).rolling(5).sum()

def vpd_017_price_down_vol_up_21d(close, volume) -> pd.Series:
    return ((close < close.shift(1)) & (volume > volume.shift(1))).astype(float).rolling(21).sum()

def vpd_018_price_down_vol_up_63d(close, volume) -> pd.Series:
    return ((close < close.shift(1)) & (volume > volume.shift(1))).astype(float).rolling(63).sum()

def vpd_019_price_down_vol_up_126d(close, volume) -> pd.Series:
    return ((close < close.shift(1)) & (volume > volume.shift(1))).astype(float).rolling(126).sum()

def vpd_020_price_down_vol_up_252d(close, volume) -> pd.Series:
    return ((close < close.shift(1)) & (volume > volume.shift(1))).astype(float).rolling(252).sum()

def vpd_021_div_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(_daily_ret(close) - _daily_ret(volume), 5)

def vpd_022_div_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(_daily_ret(close) - _daily_ret(volume), 21)

def vpd_023_div_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(_daily_ret(close) - _daily_ret(volume), 63)

def vpd_024_div_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(_daily_ret(close) - _daily_ret(volume), 126)

def vpd_025_div_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(_daily_ret(close) - _daily_ret(volume), 252)

def vpd_026_div_magnitude_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_001_div_magnitude_5d(close, volume), 252)

def vpd_027_div_magnitude_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_002_div_magnitude_21d(close, volume), 252)

def vpd_028_div_magnitude_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_003_div_magnitude_63d(close, volume), 252)

def vpd_029_div_magnitude_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_004_div_magnitude_126d(close, volume), 252)

def vpd_030_div_magnitude_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_005_div_magnitude_252d(close, volume), 252)

def vpd_031_div_duration_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_006_div_duration_5d(close, volume), 252)

def vpd_032_div_duration_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_007_div_duration_21d(close, volume), 252)

def vpd_033_div_duration_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_008_div_duration_63d(close, volume), 252)

def vpd_034_div_duration_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_009_div_duration_126d(close, volume), 252)

def vpd_035_div_duration_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_010_div_duration_252d(close, volume), 252)

def vpd_036_price_up_vol_down_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_011_price_up_vol_down_5d(close, volume), 252)

def vpd_037_price_up_vol_down_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_012_price_up_vol_down_21d(close, volume), 252)

def vpd_038_price_up_vol_down_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_013_price_up_vol_down_63d(close, volume), 252)

def vpd_039_price_up_vol_down_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_014_price_up_vol_down_126d(close, volume), 252)

def vpd_040_price_up_vol_down_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_015_price_up_vol_down_252d(close, volume), 252)

def vpd_041_price_down_vol_up_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_016_price_down_vol_up_5d(close, volume), 252)

def vpd_042_price_down_vol_up_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_017_price_down_vol_up_21d(close, volume), 252)

def vpd_043_price_down_vol_up_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_018_price_down_vol_up_63d(close, volume), 252)

def vpd_044_price_down_vol_up_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_019_price_down_vol_up_126d(close, volume), 252)

def vpd_045_price_down_vol_up_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_020_price_down_vol_up_252d(close, volume), 252)

def vpd_046_div_zscore_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_021_div_zscore_5d(close, volume), 252)

def vpd_047_div_zscore_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_022_div_zscore_21d(close, volume), 252)

def vpd_048_div_zscore_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_023_div_zscore_63d(close, volume), 252)

def vpd_049_div_zscore_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_024_div_zscore_126d(close, volume), 252)

def vpd_050_div_zscore_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(vpd_025_div_zscore_252d(close, volume), 252)

def vpd_051_div_magnitude_rank_5d(close, volume) -> pd.Series:
    return vpd_001_div_magnitude_5d(close, volume).rolling(252).rank(pct=True)

def vpd_052_div_magnitude_rank_21d(close, volume) -> pd.Series:
    return vpd_002_div_magnitude_21d(close, volume).rolling(252).rank(pct=True)

def vpd_053_div_magnitude_rank_63d(close, volume) -> pd.Series:
    return vpd_003_div_magnitude_63d(close, volume).rolling(252).rank(pct=True)

def vpd_054_div_magnitude_rank_126d(close, volume) -> pd.Series:
    return vpd_004_div_magnitude_126d(close, volume).rolling(252).rank(pct=True)

def vpd_055_div_magnitude_rank_252d(close, volume) -> pd.Series:
    return vpd_005_div_magnitude_252d(close, volume).rolling(252).rank(pct=True)

def vpd_056_div_duration_rank_5d(close, volume) -> pd.Series:
    return vpd_006_div_duration_5d(close, volume).rolling(252).rank(pct=True)

def vpd_057_div_duration_rank_21d(close, volume) -> pd.Series:
    return vpd_007_div_duration_21d(close, volume).rolling(252).rank(pct=True)

def vpd_058_div_duration_rank_63d(close, volume) -> pd.Series:
    return vpd_008_div_duration_63d(close, volume).rolling(252).rank(pct=True)

def vpd_059_div_duration_rank_126d(close, volume) -> pd.Series:
    return vpd_009_div_duration_126d(close, volume).rolling(252).rank(pct=True)

def vpd_060_div_duration_rank_252d(close, volume) -> pd.Series:
    return vpd_010_div_duration_252d(close, volume).rolling(252).rank(pct=True)

def vpd_061_price_up_vol_down_rank_5d(close, volume) -> pd.Series:
    return vpd_011_price_up_vol_down_5d(close, volume).rolling(252).rank(pct=True)

def vpd_062_price_up_vol_down_rank_21d(close, volume) -> pd.Series:
    return vpd_012_price_up_vol_down_21d(close, volume).rolling(252).rank(pct=True)

def vpd_063_price_up_vol_down_rank_63d(close, volume) -> pd.Series:
    return vpd_013_price_up_vol_down_63d(close, volume).rolling(252).rank(pct=True)

def vpd_064_price_up_vol_down_rank_126d(close, volume) -> pd.Series:
    return vpd_014_price_up_vol_down_126d(close, volume).rolling(252).rank(pct=True)

def vpd_065_price_up_vol_down_rank_252d(close, volume) -> pd.Series:
    return vpd_015_price_up_vol_down_252d(close, volume).rolling(252).rank(pct=True)

def vpd_066_price_down_vol_up_rank_5d(close, volume) -> pd.Series:
    return vpd_016_price_down_vol_up_5d(close, volume).rolling(252).rank(pct=True)

def vpd_067_price_down_vol_up_rank_21d(close, volume) -> pd.Series:
    return vpd_017_price_down_vol_up_21d(close, volume).rolling(252).rank(pct=True)

def vpd_068_price_down_vol_up_rank_63d(close, volume) -> pd.Series:
    return vpd_018_price_down_vol_up_63d(close, volume).rolling(252).rank(pct=True)

def vpd_069_price_down_vol_up_rank_126d(close, volume) -> pd.Series:
    return vpd_019_price_down_vol_up_126d(close, volume).rolling(252).rank(pct=True)

def vpd_070_price_down_vol_up_rank_252d(close, volume) -> pd.Series:
    return vpd_020_price_down_vol_up_252d(close, volume).rolling(252).rank(pct=True)

def vpd_071_div_zscore_rank_5d(close, volume) -> pd.Series:
    return vpd_021_div_zscore_5d(close, volume).rolling(252).rank(pct=True)

def vpd_072_div_zscore_rank_21d(close, volume) -> pd.Series:
    return vpd_022_div_zscore_21d(close, volume).rolling(252).rank(pct=True)

def vpd_073_div_zscore_rank_63d(close, volume) -> pd.Series:
    return vpd_023_div_zscore_63d(close, volume).rolling(252).rank(pct=True)

def vpd_074_div_zscore_rank_126d(close, volume) -> pd.Series:
    return vpd_024_div_zscore_126d(close, volume).rolling(252).rank(pct=True)

def vpd_075_div_zscore_rank_252d(close, volume) -> pd.Series:
    return vpd_025_div_zscore_252d(close, volume).rolling(252).rank(pct=True)


# --- Registry ---
V22_REGISTRY = {
    "vpd_001_div_magnitude_5d": {"inputs": ['close', 'volume'], "func": vpd_001_div_magnitude_5d},
    "vpd_002_div_magnitude_21d": {"inputs": ['close', 'volume'], "func": vpd_002_div_magnitude_21d},
    "vpd_003_div_magnitude_63d": {"inputs": ['close', 'volume'], "func": vpd_003_div_magnitude_63d},
    "vpd_004_div_magnitude_126d": {"inputs": ['close', 'volume'], "func": vpd_004_div_magnitude_126d},
    "vpd_005_div_magnitude_252d": {"inputs": ['close', 'volume'], "func": vpd_005_div_magnitude_252d},
    "vpd_006_div_duration_5d": {"inputs": ['close', 'volume'], "func": vpd_006_div_duration_5d},
    "vpd_007_div_duration_21d": {"inputs": ['close', 'volume'], "func": vpd_007_div_duration_21d},
    "vpd_008_div_duration_63d": {"inputs": ['close', 'volume'], "func": vpd_008_div_duration_63d},
    "vpd_009_div_duration_126d": {"inputs": ['close', 'volume'], "func": vpd_009_div_duration_126d},
    "vpd_010_div_duration_252d": {"inputs": ['close', 'volume'], "func": vpd_010_div_duration_252d},
    "vpd_011_price_up_vol_down_5d": {"inputs": ['close', 'volume'], "func": vpd_011_price_up_vol_down_5d},
    "vpd_012_price_up_vol_down_21d": {"inputs": ['close', 'volume'], "func": vpd_012_price_up_vol_down_21d},
    "vpd_013_price_up_vol_down_63d": {"inputs": ['close', 'volume'], "func": vpd_013_price_up_vol_down_63d},
    "vpd_014_price_up_vol_down_126d": {"inputs": ['close', 'volume'], "func": vpd_014_price_up_vol_down_126d},
    "vpd_015_price_up_vol_down_252d": {"inputs": ['close', 'volume'], "func": vpd_015_price_up_vol_down_252d},
    "vpd_016_price_down_vol_up_5d": {"inputs": ['close', 'volume'], "func": vpd_016_price_down_vol_up_5d},
    "vpd_017_price_down_vol_up_21d": {"inputs": ['close', 'volume'], "func": vpd_017_price_down_vol_up_21d},
    "vpd_018_price_down_vol_up_63d": {"inputs": ['close', 'volume'], "func": vpd_018_price_down_vol_up_63d},
    "vpd_019_price_down_vol_up_126d": {"inputs": ['close', 'volume'], "func": vpd_019_price_down_vol_up_126d},
    "vpd_020_price_down_vol_up_252d": {"inputs": ['close', 'volume'], "func": vpd_020_price_down_vol_up_252d},
    "vpd_021_div_zscore_5d": {"inputs": ['close', 'volume'], "func": vpd_021_div_zscore_5d},
    "vpd_022_div_zscore_21d": {"inputs": ['close', 'volume'], "func": vpd_022_div_zscore_21d},
    "vpd_023_div_zscore_63d": {"inputs": ['close', 'volume'], "func": vpd_023_div_zscore_63d},
    "vpd_024_div_zscore_126d": {"inputs": ['close', 'volume'], "func": vpd_024_div_zscore_126d},
    "vpd_025_div_zscore_252d": {"inputs": ['close', 'volume'], "func": vpd_025_div_zscore_252d},
    "vpd_026_div_magnitude_zscore_5d": {"inputs": ['close', 'volume'], "func": vpd_026_div_magnitude_zscore_5d},
    "vpd_027_div_magnitude_zscore_21d": {"inputs": ['close', 'volume'], "func": vpd_027_div_magnitude_zscore_21d},
    "vpd_028_div_magnitude_zscore_63d": {"inputs": ['close', 'volume'], "func": vpd_028_div_magnitude_zscore_63d},
    "vpd_029_div_magnitude_zscore_126d": {"inputs": ['close', 'volume'], "func": vpd_029_div_magnitude_zscore_126d},
    "vpd_030_div_magnitude_zscore_252d": {"inputs": ['close', 'volume'], "func": vpd_030_div_magnitude_zscore_252d},
    "vpd_031_div_duration_zscore_5d": {"inputs": ['close', 'volume'], "func": vpd_031_div_duration_zscore_5d},
    "vpd_032_div_duration_zscore_21d": {"inputs": ['close', 'volume'], "func": vpd_032_div_duration_zscore_21d},
    "vpd_033_div_duration_zscore_63d": {"inputs": ['close', 'volume'], "func": vpd_033_div_duration_zscore_63d},
    "vpd_034_div_duration_zscore_126d": {"inputs": ['close', 'volume'], "func": vpd_034_div_duration_zscore_126d},
    "vpd_035_div_duration_zscore_252d": {"inputs": ['close', 'volume'], "func": vpd_035_div_duration_zscore_252d},
    "vpd_036_price_up_vol_down_zscore_5d": {"inputs": ['close', 'volume'], "func": vpd_036_price_up_vol_down_zscore_5d},
    "vpd_037_price_up_vol_down_zscore_21d": {"inputs": ['close', 'volume'], "func": vpd_037_price_up_vol_down_zscore_21d},
    "vpd_038_price_up_vol_down_zscore_63d": {"inputs": ['close', 'volume'], "func": vpd_038_price_up_vol_down_zscore_63d},
    "vpd_039_price_up_vol_down_zscore_126d": {"inputs": ['close', 'volume'], "func": vpd_039_price_up_vol_down_zscore_126d},
    "vpd_040_price_up_vol_down_zscore_252d": {"inputs": ['close', 'volume'], "func": vpd_040_price_up_vol_down_zscore_252d},
    "vpd_041_price_down_vol_up_zscore_5d": {"inputs": ['close', 'volume'], "func": vpd_041_price_down_vol_up_zscore_5d},
    "vpd_042_price_down_vol_up_zscore_21d": {"inputs": ['close', 'volume'], "func": vpd_042_price_down_vol_up_zscore_21d},
    "vpd_043_price_down_vol_up_zscore_63d": {"inputs": ['close', 'volume'], "func": vpd_043_price_down_vol_up_zscore_63d},
    "vpd_044_price_down_vol_up_zscore_126d": {"inputs": ['close', 'volume'], "func": vpd_044_price_down_vol_up_zscore_126d},
    "vpd_045_price_down_vol_up_zscore_252d": {"inputs": ['close', 'volume'], "func": vpd_045_price_down_vol_up_zscore_252d},
    "vpd_046_div_zscore_zscore_5d": {"inputs": ['close', 'volume'], "func": vpd_046_div_zscore_zscore_5d},
    "vpd_047_div_zscore_zscore_21d": {"inputs": ['close', 'volume'], "func": vpd_047_div_zscore_zscore_21d},
    "vpd_048_div_zscore_zscore_63d": {"inputs": ['close', 'volume'], "func": vpd_048_div_zscore_zscore_63d},
    "vpd_049_div_zscore_zscore_126d": {"inputs": ['close', 'volume'], "func": vpd_049_div_zscore_zscore_126d},
    "vpd_050_div_zscore_zscore_252d": {"inputs": ['close', 'volume'], "func": vpd_050_div_zscore_zscore_252d},
    "vpd_051_div_magnitude_rank_5d": {"inputs": ['close', 'volume'], "func": vpd_051_div_magnitude_rank_5d},
    "vpd_052_div_magnitude_rank_21d": {"inputs": ['close', 'volume'], "func": vpd_052_div_magnitude_rank_21d},
    "vpd_053_div_magnitude_rank_63d": {"inputs": ['close', 'volume'], "func": vpd_053_div_magnitude_rank_63d},
    "vpd_054_div_magnitude_rank_126d": {"inputs": ['close', 'volume'], "func": vpd_054_div_magnitude_rank_126d},
    "vpd_055_div_magnitude_rank_252d": {"inputs": ['close', 'volume'], "func": vpd_055_div_magnitude_rank_252d},
    "vpd_056_div_duration_rank_5d": {"inputs": ['close', 'volume'], "func": vpd_056_div_duration_rank_5d},
    "vpd_057_div_duration_rank_21d": {"inputs": ['close', 'volume'], "func": vpd_057_div_duration_rank_21d},
    "vpd_058_div_duration_rank_63d": {"inputs": ['close', 'volume'], "func": vpd_058_div_duration_rank_63d},
    "vpd_059_div_duration_rank_126d": {"inputs": ['close', 'volume'], "func": vpd_059_div_duration_rank_126d},
    "vpd_060_div_duration_rank_252d": {"inputs": ['close', 'volume'], "func": vpd_060_div_duration_rank_252d},
    "vpd_061_price_up_vol_down_rank_5d": {"inputs": ['close', 'volume'], "func": vpd_061_price_up_vol_down_rank_5d},
    "vpd_062_price_up_vol_down_rank_21d": {"inputs": ['close', 'volume'], "func": vpd_062_price_up_vol_down_rank_21d},
    "vpd_063_price_up_vol_down_rank_63d": {"inputs": ['close', 'volume'], "func": vpd_063_price_up_vol_down_rank_63d},
    "vpd_064_price_up_vol_down_rank_126d": {"inputs": ['close', 'volume'], "func": vpd_064_price_up_vol_down_rank_126d},
    "vpd_065_price_up_vol_down_rank_252d": {"inputs": ['close', 'volume'], "func": vpd_065_price_up_vol_down_rank_252d},
    "vpd_066_price_down_vol_up_rank_5d": {"inputs": ['close', 'volume'], "func": vpd_066_price_down_vol_up_rank_5d},
    "vpd_067_price_down_vol_up_rank_21d": {"inputs": ['close', 'volume'], "func": vpd_067_price_down_vol_up_rank_21d},
    "vpd_068_price_down_vol_up_rank_63d": {"inputs": ['close', 'volume'], "func": vpd_068_price_down_vol_up_rank_63d},
    "vpd_069_price_down_vol_up_rank_126d": {"inputs": ['close', 'volume'], "func": vpd_069_price_down_vol_up_rank_126d},
    "vpd_070_price_down_vol_up_rank_252d": {"inputs": ['close', 'volume'], "func": vpd_070_price_down_vol_up_rank_252d},
    "vpd_071_div_zscore_rank_5d": {"inputs": ['close', 'volume'], "func": vpd_071_div_zscore_rank_5d},
    "vpd_072_div_zscore_rank_21d": {"inputs": ['close', 'volume'], "func": vpd_072_div_zscore_rank_21d},
    "vpd_073_div_zscore_rank_63d": {"inputs": ['close', 'volume'], "func": vpd_073_div_zscore_rank_63d},
    "vpd_074_div_zscore_rank_126d": {"inputs": ['close', 'volume'], "func": vpd_074_div_zscore_rank_126d},
    "vpd_075_div_zscore_rank_252d": {"inputs": ['close', 'volume'], "func": vpd_075_div_zscore_rank_252d},
}
