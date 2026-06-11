"""
Domain 14: recovery_failure (rfl_)
Asset Class: US Equities
Target Context: Failure to recover from drawdowns and resistance testing.
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
def rfl_001_rebound_strength_5d(close) -> pd.Series:
    return _safe_div(close - close.shift(5), close.rolling(5).max() - close.rolling(5).min())

def rfl_002_rebound_strength_21d(close) -> pd.Series:
    return _safe_div(close - close.shift(21), close.rolling(21).max() - close.rolling(21).min())

def rfl_003_rebound_strength_63d(close) -> pd.Series:
    return _safe_div(close - close.shift(63), close.rolling(63).max() - close.rolling(63).min())

def rfl_004_rebound_strength_126d(close) -> pd.Series:
    return _safe_div(close - close.shift(126), close.rolling(126).max() - close.rolling(126).min())

def rfl_005_rebound_strength_252d(close) -> pd.Series:
    return _safe_div(close - close.shift(252), close.rolling(252).max() - close.rolling(252).min())

def rfl_006_resistance_proximity_5d(close) -> pd.Series:
    return _safe_div(close.rolling(5).max() - close, close)

def rfl_007_resistance_proximity_21d(close) -> pd.Series:
    return _safe_div(close.rolling(21).max() - close, close)

def rfl_008_resistance_proximity_63d(close) -> pd.Series:
    return _safe_div(close.rolling(63).max() - close, close)

def rfl_009_resistance_proximity_126d(close) -> pd.Series:
    return _safe_div(close.rolling(126).max() - close, close)

def rfl_010_resistance_proximity_252d(close) -> pd.Series:
    return _safe_div(close.rolling(252).max() - close, close)

def rfl_011_failed_breakout_count_5d(close) -> pd.Series:
    return ((close.shift(1) > close.rolling(5).max().shift(2)) & (close < close.shift(1))).astype(int).rolling(5).sum()

def rfl_012_failed_breakout_count_21d(close) -> pd.Series:
    return ((close.shift(1) > close.rolling(21).max().shift(2)) & (close < close.shift(1))).astype(int).rolling(21).sum()

def rfl_013_failed_breakout_count_63d(close) -> pd.Series:
    return ((close.shift(1) > close.rolling(63).max().shift(2)) & (close < close.shift(1))).astype(int).rolling(63).sum()

def rfl_014_failed_breakout_count_126d(close) -> pd.Series:
    return ((close.shift(1) > close.rolling(126).max().shift(2)) & (close < close.shift(1))).astype(int).rolling(126).sum()

def rfl_015_failed_breakout_count_252d(close) -> pd.Series:
    return ((close.shift(1) > close.rolling(252).max().shift(2)) & (close < close.shift(1))).astype(int).rolling(252).sum()

def rfl_016_rally_fade_ratio_5d(close) -> pd.Series:
    return _safe_div(close.rolling(5).max() - close, close - close.rolling(5).min())

def rfl_017_rally_fade_ratio_21d(close) -> pd.Series:
    return _safe_div(close.rolling(21).max() - close, close - close.rolling(21).min())

def rfl_018_rally_fade_ratio_63d(close) -> pd.Series:
    return _safe_div(close.rolling(63).max() - close, close - close.rolling(63).min())

def rfl_019_rally_fade_ratio_126d(close) -> pd.Series:
    return _safe_div(close.rolling(126).max() - close, close - close.rolling(126).min())

def rfl_020_rally_fade_ratio_252d(close) -> pd.Series:
    return _safe_div(close.rolling(252).max() - close, close - close.rolling(252).min())

def rfl_021_trough_persistence_5d(close) -> pd.Series:
    return _rolling_mean((close < close.rolling(5).min() * 1.05).astype(float), 5)

def rfl_022_trough_persistence_21d(close) -> pd.Series:
    return _rolling_mean((close < close.rolling(21).min() * 1.05).astype(float), 21)

def rfl_023_trough_persistence_63d(close) -> pd.Series:
    return _rolling_mean((close < close.rolling(63).min() * 1.05).astype(float), 63)

def rfl_024_trough_persistence_126d(close) -> pd.Series:
    return _rolling_mean((close < close.rolling(126).min() * 1.05).astype(float), 126)

def rfl_025_trough_persistence_252d(close) -> pd.Series:
    return _rolling_mean((close < close.rolling(252).min() * 1.05).astype(float), 252)

def rfl_026_rebound_strength_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(rfl_001_rebound_strength_5d(close), 252)

def rfl_027_rebound_strength_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(rfl_002_rebound_strength_21d(close), 252)

def rfl_028_rebound_strength_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(rfl_003_rebound_strength_63d(close), 252)

def rfl_029_rebound_strength_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(rfl_004_rebound_strength_126d(close), 252)

def rfl_030_rebound_strength_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(rfl_005_rebound_strength_252d(close), 252)

def rfl_031_resistance_proximity_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(rfl_006_resistance_proximity_5d(close), 252)

def rfl_032_resistance_proximity_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(rfl_007_resistance_proximity_21d(close), 252)

def rfl_033_resistance_proximity_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(rfl_008_resistance_proximity_63d(close), 252)

def rfl_034_resistance_proximity_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(rfl_009_resistance_proximity_126d(close), 252)

def rfl_035_resistance_proximity_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(rfl_010_resistance_proximity_252d(close), 252)

def rfl_036_failed_breakout_count_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(rfl_011_failed_breakout_count_5d(close), 252)

def rfl_037_failed_breakout_count_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(rfl_012_failed_breakout_count_21d(close), 252)

def rfl_038_failed_breakout_count_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(rfl_013_failed_breakout_count_63d(close), 252)

def rfl_039_failed_breakout_count_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(rfl_014_failed_breakout_count_126d(close), 252)

def rfl_040_failed_breakout_count_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(rfl_015_failed_breakout_count_252d(close), 252)

def rfl_041_rally_fade_ratio_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(rfl_016_rally_fade_ratio_5d(close), 252)

def rfl_042_rally_fade_ratio_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(rfl_017_rally_fade_ratio_21d(close), 252)

def rfl_043_rally_fade_ratio_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(rfl_018_rally_fade_ratio_63d(close), 252)

def rfl_044_rally_fade_ratio_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(rfl_019_rally_fade_ratio_126d(close), 252)

def rfl_045_rally_fade_ratio_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(rfl_020_rally_fade_ratio_252d(close), 252)

def rfl_046_trough_persistence_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(rfl_021_trough_persistence_5d(close), 252)

def rfl_047_trough_persistence_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(rfl_022_trough_persistence_21d(close), 252)

def rfl_048_trough_persistence_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(rfl_023_trough_persistence_63d(close), 252)

def rfl_049_trough_persistence_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(rfl_024_trough_persistence_126d(close), 252)

def rfl_050_trough_persistence_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(rfl_025_trough_persistence_252d(close), 252)

def rfl_051_rebound_strength_rank_5d(close) -> pd.Series:
    return rfl_001_rebound_strength_5d(close).rolling(252).rank(pct=True)

def rfl_052_rebound_strength_rank_21d(close) -> pd.Series:
    return rfl_002_rebound_strength_21d(close).rolling(252).rank(pct=True)

def rfl_053_rebound_strength_rank_63d(close) -> pd.Series:
    return rfl_003_rebound_strength_63d(close).rolling(252).rank(pct=True)

def rfl_054_rebound_strength_rank_126d(close) -> pd.Series:
    return rfl_004_rebound_strength_126d(close).rolling(252).rank(pct=True)

def rfl_055_rebound_strength_rank_252d(close) -> pd.Series:
    return rfl_005_rebound_strength_252d(close).rolling(252).rank(pct=True)

def rfl_056_resistance_proximity_rank_5d(close) -> pd.Series:
    return rfl_006_resistance_proximity_5d(close).rolling(252).rank(pct=True)

def rfl_057_resistance_proximity_rank_21d(close) -> pd.Series:
    return rfl_007_resistance_proximity_21d(close).rolling(252).rank(pct=True)

def rfl_058_resistance_proximity_rank_63d(close) -> pd.Series:
    return rfl_008_resistance_proximity_63d(close).rolling(252).rank(pct=True)

def rfl_059_resistance_proximity_rank_126d(close) -> pd.Series:
    return rfl_009_resistance_proximity_126d(close).rolling(252).rank(pct=True)

def rfl_060_resistance_proximity_rank_252d(close) -> pd.Series:
    return rfl_010_resistance_proximity_252d(close).rolling(252).rank(pct=True)

def rfl_061_failed_breakout_count_rank_5d(close) -> pd.Series:
    return rfl_011_failed_breakout_count_5d(close).rolling(252).rank(pct=True)

def rfl_062_failed_breakout_count_rank_21d(close) -> pd.Series:
    return rfl_012_failed_breakout_count_21d(close).rolling(252).rank(pct=True)

def rfl_063_failed_breakout_count_rank_63d(close) -> pd.Series:
    return rfl_013_failed_breakout_count_63d(close).rolling(252).rank(pct=True)

def rfl_064_failed_breakout_count_rank_126d(close) -> pd.Series:
    return rfl_014_failed_breakout_count_126d(close).rolling(252).rank(pct=True)

def rfl_065_failed_breakout_count_rank_252d(close) -> pd.Series:
    return rfl_015_failed_breakout_count_252d(close).rolling(252).rank(pct=True)

def rfl_066_rally_fade_ratio_rank_5d(close) -> pd.Series:
    return rfl_016_rally_fade_ratio_5d(close).rolling(252).rank(pct=True)

def rfl_067_rally_fade_ratio_rank_21d(close) -> pd.Series:
    return rfl_017_rally_fade_ratio_21d(close).rolling(252).rank(pct=True)

def rfl_068_rally_fade_ratio_rank_63d(close) -> pd.Series:
    return rfl_018_rally_fade_ratio_63d(close).rolling(252).rank(pct=True)

def rfl_069_rally_fade_ratio_rank_126d(close) -> pd.Series:
    return rfl_019_rally_fade_ratio_126d(close).rolling(252).rank(pct=True)

def rfl_070_rally_fade_ratio_rank_252d(close) -> pd.Series:
    return rfl_020_rally_fade_ratio_252d(close).rolling(252).rank(pct=True)

def rfl_071_trough_persistence_rank_5d(close) -> pd.Series:
    return rfl_021_trough_persistence_5d(close).rolling(252).rank(pct=True)

def rfl_072_trough_persistence_rank_21d(close) -> pd.Series:
    return rfl_022_trough_persistence_21d(close).rolling(252).rank(pct=True)

def rfl_073_trough_persistence_rank_63d(close) -> pd.Series:
    return rfl_023_trough_persistence_63d(close).rolling(252).rank(pct=True)

def rfl_074_trough_persistence_rank_126d(close) -> pd.Series:
    return rfl_024_trough_persistence_126d(close).rolling(252).rank(pct=True)

def rfl_075_trough_persistence_rank_252d(close) -> pd.Series:
    return rfl_025_trough_persistence_252d(close).rolling(252).rank(pct=True)


# --- Registry ---
V14_REGISTRY = {
    "rfl_001_rebound_strength_5d": {"inputs": ['close'], "func": rfl_001_rebound_strength_5d},
    "rfl_002_rebound_strength_21d": {"inputs": ['close'], "func": rfl_002_rebound_strength_21d},
    "rfl_003_rebound_strength_63d": {"inputs": ['close'], "func": rfl_003_rebound_strength_63d},
    "rfl_004_rebound_strength_126d": {"inputs": ['close'], "func": rfl_004_rebound_strength_126d},
    "rfl_005_rebound_strength_252d": {"inputs": ['close'], "func": rfl_005_rebound_strength_252d},
    "rfl_006_resistance_proximity_5d": {"inputs": ['close'], "func": rfl_006_resistance_proximity_5d},
    "rfl_007_resistance_proximity_21d": {"inputs": ['close'], "func": rfl_007_resistance_proximity_21d},
    "rfl_008_resistance_proximity_63d": {"inputs": ['close'], "func": rfl_008_resistance_proximity_63d},
    "rfl_009_resistance_proximity_126d": {"inputs": ['close'], "func": rfl_009_resistance_proximity_126d},
    "rfl_010_resistance_proximity_252d": {"inputs": ['close'], "func": rfl_010_resistance_proximity_252d},
    "rfl_011_failed_breakout_count_5d": {"inputs": ['close'], "func": rfl_011_failed_breakout_count_5d},
    "rfl_012_failed_breakout_count_21d": {"inputs": ['close'], "func": rfl_012_failed_breakout_count_21d},
    "rfl_013_failed_breakout_count_63d": {"inputs": ['close'], "func": rfl_013_failed_breakout_count_63d},
    "rfl_014_failed_breakout_count_126d": {"inputs": ['close'], "func": rfl_014_failed_breakout_count_126d},
    "rfl_015_failed_breakout_count_252d": {"inputs": ['close'], "func": rfl_015_failed_breakout_count_252d},
    "rfl_016_rally_fade_ratio_5d": {"inputs": ['close'], "func": rfl_016_rally_fade_ratio_5d},
    "rfl_017_rally_fade_ratio_21d": {"inputs": ['close'], "func": rfl_017_rally_fade_ratio_21d},
    "rfl_018_rally_fade_ratio_63d": {"inputs": ['close'], "func": rfl_018_rally_fade_ratio_63d},
    "rfl_019_rally_fade_ratio_126d": {"inputs": ['close'], "func": rfl_019_rally_fade_ratio_126d},
    "rfl_020_rally_fade_ratio_252d": {"inputs": ['close'], "func": rfl_020_rally_fade_ratio_252d},
    "rfl_021_trough_persistence_5d": {"inputs": ['close'], "func": rfl_021_trough_persistence_5d},
    "rfl_022_trough_persistence_21d": {"inputs": ['close'], "func": rfl_022_trough_persistence_21d},
    "rfl_023_trough_persistence_63d": {"inputs": ['close'], "func": rfl_023_trough_persistence_63d},
    "rfl_024_trough_persistence_126d": {"inputs": ['close'], "func": rfl_024_trough_persistence_126d},
    "rfl_025_trough_persistence_252d": {"inputs": ['close'], "func": rfl_025_trough_persistence_252d},
    "rfl_026_rebound_strength_zscore_5d": {"inputs": ['close'], "func": rfl_026_rebound_strength_zscore_5d},
    "rfl_027_rebound_strength_zscore_21d": {"inputs": ['close'], "func": rfl_027_rebound_strength_zscore_21d},
    "rfl_028_rebound_strength_zscore_63d": {"inputs": ['close'], "func": rfl_028_rebound_strength_zscore_63d},
    "rfl_029_rebound_strength_zscore_126d": {"inputs": ['close'], "func": rfl_029_rebound_strength_zscore_126d},
    "rfl_030_rebound_strength_zscore_252d": {"inputs": ['close'], "func": rfl_030_rebound_strength_zscore_252d},
    "rfl_031_resistance_proximity_zscore_5d": {"inputs": ['close'], "func": rfl_031_resistance_proximity_zscore_5d},
    "rfl_032_resistance_proximity_zscore_21d": {"inputs": ['close'], "func": rfl_032_resistance_proximity_zscore_21d},
    "rfl_033_resistance_proximity_zscore_63d": {"inputs": ['close'], "func": rfl_033_resistance_proximity_zscore_63d},
    "rfl_034_resistance_proximity_zscore_126d": {"inputs": ['close'], "func": rfl_034_resistance_proximity_zscore_126d},
    "rfl_035_resistance_proximity_zscore_252d": {"inputs": ['close'], "func": rfl_035_resistance_proximity_zscore_252d},
    "rfl_036_failed_breakout_count_zscore_5d": {"inputs": ['close'], "func": rfl_036_failed_breakout_count_zscore_5d},
    "rfl_037_failed_breakout_count_zscore_21d": {"inputs": ['close'], "func": rfl_037_failed_breakout_count_zscore_21d},
    "rfl_038_failed_breakout_count_zscore_63d": {"inputs": ['close'], "func": rfl_038_failed_breakout_count_zscore_63d},
    "rfl_039_failed_breakout_count_zscore_126d": {"inputs": ['close'], "func": rfl_039_failed_breakout_count_zscore_126d},
    "rfl_040_failed_breakout_count_zscore_252d": {"inputs": ['close'], "func": rfl_040_failed_breakout_count_zscore_252d},
    "rfl_041_rally_fade_ratio_zscore_5d": {"inputs": ['close'], "func": rfl_041_rally_fade_ratio_zscore_5d},
    "rfl_042_rally_fade_ratio_zscore_21d": {"inputs": ['close'], "func": rfl_042_rally_fade_ratio_zscore_21d},
    "rfl_043_rally_fade_ratio_zscore_63d": {"inputs": ['close'], "func": rfl_043_rally_fade_ratio_zscore_63d},
    "rfl_044_rally_fade_ratio_zscore_126d": {"inputs": ['close'], "func": rfl_044_rally_fade_ratio_zscore_126d},
    "rfl_045_rally_fade_ratio_zscore_252d": {"inputs": ['close'], "func": rfl_045_rally_fade_ratio_zscore_252d},
    "rfl_046_trough_persistence_zscore_5d": {"inputs": ['close'], "func": rfl_046_trough_persistence_zscore_5d},
    "rfl_047_trough_persistence_zscore_21d": {"inputs": ['close'], "func": rfl_047_trough_persistence_zscore_21d},
    "rfl_048_trough_persistence_zscore_63d": {"inputs": ['close'], "func": rfl_048_trough_persistence_zscore_63d},
    "rfl_049_trough_persistence_zscore_126d": {"inputs": ['close'], "func": rfl_049_trough_persistence_zscore_126d},
    "rfl_050_trough_persistence_zscore_252d": {"inputs": ['close'], "func": rfl_050_trough_persistence_zscore_252d},
    "rfl_051_rebound_strength_rank_5d": {"inputs": ['close'], "func": rfl_051_rebound_strength_rank_5d},
    "rfl_052_rebound_strength_rank_21d": {"inputs": ['close'], "func": rfl_052_rebound_strength_rank_21d},
    "rfl_053_rebound_strength_rank_63d": {"inputs": ['close'], "func": rfl_053_rebound_strength_rank_63d},
    "rfl_054_rebound_strength_rank_126d": {"inputs": ['close'], "func": rfl_054_rebound_strength_rank_126d},
    "rfl_055_rebound_strength_rank_252d": {"inputs": ['close'], "func": rfl_055_rebound_strength_rank_252d},
    "rfl_056_resistance_proximity_rank_5d": {"inputs": ['close'], "func": rfl_056_resistance_proximity_rank_5d},
    "rfl_057_resistance_proximity_rank_21d": {"inputs": ['close'], "func": rfl_057_resistance_proximity_rank_21d},
    "rfl_058_resistance_proximity_rank_63d": {"inputs": ['close'], "func": rfl_058_resistance_proximity_rank_63d},
    "rfl_059_resistance_proximity_rank_126d": {"inputs": ['close'], "func": rfl_059_resistance_proximity_rank_126d},
    "rfl_060_resistance_proximity_rank_252d": {"inputs": ['close'], "func": rfl_060_resistance_proximity_rank_252d},
    "rfl_061_failed_breakout_count_rank_5d": {"inputs": ['close'], "func": rfl_061_failed_breakout_count_rank_5d},
    "rfl_062_failed_breakout_count_rank_21d": {"inputs": ['close'], "func": rfl_062_failed_breakout_count_rank_21d},
    "rfl_063_failed_breakout_count_rank_63d": {"inputs": ['close'], "func": rfl_063_failed_breakout_count_rank_63d},
    "rfl_064_failed_breakout_count_rank_126d": {"inputs": ['close'], "func": rfl_064_failed_breakout_count_rank_126d},
    "rfl_065_failed_breakout_count_rank_252d": {"inputs": ['close'], "func": rfl_065_failed_breakout_count_rank_252d},
    "rfl_066_rally_fade_ratio_rank_5d": {"inputs": ['close'], "func": rfl_066_rally_fade_ratio_rank_5d},
    "rfl_067_rally_fade_ratio_rank_21d": {"inputs": ['close'], "func": rfl_067_rally_fade_ratio_rank_21d},
    "rfl_068_rally_fade_ratio_rank_63d": {"inputs": ['close'], "func": rfl_068_rally_fade_ratio_rank_63d},
    "rfl_069_rally_fade_ratio_rank_126d": {"inputs": ['close'], "func": rfl_069_rally_fade_ratio_rank_126d},
    "rfl_070_rally_fade_ratio_rank_252d": {"inputs": ['close'], "func": rfl_070_rally_fade_ratio_rank_252d},
    "rfl_071_trough_persistence_rank_5d": {"inputs": ['close'], "func": rfl_071_trough_persistence_rank_5d},
    "rfl_072_trough_persistence_rank_21d": {"inputs": ['close'], "func": rfl_072_trough_persistence_rank_21d},
    "rfl_073_trough_persistence_rank_63d": {"inputs": ['close'], "func": rfl_073_trough_persistence_rank_63d},
    "rfl_074_trough_persistence_rank_126d": {"inputs": ['close'], "func": rfl_074_trough_persistence_rank_126d},
    "rfl_075_trough_persistence_rank_252d": {"inputs": ['close'], "func": rfl_075_trough_persistence_rank_252d},
}
