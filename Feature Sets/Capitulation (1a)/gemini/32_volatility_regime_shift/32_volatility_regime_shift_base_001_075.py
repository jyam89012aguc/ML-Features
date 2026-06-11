"""
Domain 32: volatility_regime_shift (vrs_)
Asset Class: US Equities
Target Context: Shifts between different volatility regimes.
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
def vrs_001_regime_shift_prob_5d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 5).diff().abs() / _rolling_std(_daily_ret(close), 252)).rolling(5).mean()

def vrs_002_regime_shift_prob_21d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 21).diff().abs() / _rolling_std(_daily_ret(close), 252)).rolling(21).mean()

def vrs_003_regime_shift_prob_63d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 63).diff().abs() / _rolling_std(_daily_ret(close), 252)).rolling(63).mean()

def vrs_004_regime_shift_prob_126d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 126).diff().abs() / _rolling_std(_daily_ret(close), 252)).rolling(126).mean()

def vrs_005_regime_shift_prob_252d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 252).diff().abs() / _rolling_std(_daily_ret(close), 252)).rolling(252).mean()

def vrs_006_regime_change_5d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 5) > _rolling_std(_daily_ret(close), 252)).astype(float).diff().abs()

def vrs_007_regime_change_21d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 21) > _rolling_std(_daily_ret(close), 252)).astype(float).diff().abs()

def vrs_008_regime_change_63d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 63) > _rolling_std(_daily_ret(close), 252)).astype(float).diff().abs()

def vrs_009_regime_change_126d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 126) > _rolling_std(_daily_ret(close), 252)).astype(float).diff().abs()

def vrs_010_regime_change_252d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 252) > _rolling_std(_daily_ret(close), 252)).astype(float).diff().abs()

def vrs_011_regime_duration_5d(close) -> pd.Series:
    return (lambda x: (x > x.rolling(252).mean()).astype(int).groupby(((x > x.rolling(252).mean()) != (x > x.rolling(252).mean()).shift()).cumsum()).cumcount())(_rolling_std(_daily_ret(close), 5))

def vrs_012_regime_duration_21d(close) -> pd.Series:
    return (lambda x: (x > x.rolling(252).mean()).astype(int).groupby(((x > x.rolling(252).mean()) != (x > x.rolling(252).mean()).shift()).cumsum()).cumcount())(_rolling_std(_daily_ret(close), 21))

def vrs_013_regime_duration_63d(close) -> pd.Series:
    return (lambda x: (x > x.rolling(252).mean()).astype(int).groupby(((x > x.rolling(252).mean()) != (x > x.rolling(252).mean()).shift()).cumsum()).cumcount())(_rolling_std(_daily_ret(close), 63))

def vrs_014_regime_duration_126d(close) -> pd.Series:
    return (lambda x: (x > x.rolling(252).mean()).astype(int).groupby(((x > x.rolling(252).mean()) != (x > x.rolling(252).mean()).shift()).cumsum()).cumcount())(_rolling_std(_daily_ret(close), 126))

def vrs_015_regime_duration_252d(close) -> pd.Series:
    return (lambda x: (x > x.rolling(252).mean()).astype(int).groupby(((x > x.rolling(252).mean()) != (x > x.rolling(252).mean()).shift()).cumsum()).cumcount())(_rolling_std(_daily_ret(close), 252))

def vrs_016_regime_entropy_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5).rolling(5).apply(_entropy_calc, raw=False)

def vrs_017_regime_entropy_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21).rolling(21).apply(_entropy_calc, raw=False)

def vrs_018_regime_entropy_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63).rolling(63).apply(_entropy_calc, raw=False)

def vrs_019_regime_entropy_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126).rolling(126).apply(_entropy_calc, raw=False)

def vrs_020_regime_entropy_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252).rolling(252).apply(_entropy_calc, raw=False)

def vrs_021_regime_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(_rolling_std(_daily_ret(close), 5), 252)

def vrs_022_regime_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(_rolling_std(_daily_ret(close), 21), 252)

def vrs_023_regime_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(_rolling_std(_daily_ret(close), 63), 252)

def vrs_024_regime_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(_rolling_std(_daily_ret(close), 126), 252)

def vrs_025_regime_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(_rolling_std(_daily_ret(close), 252), 252)

def vrs_026_regime_shift_prob_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vrs_001_regime_shift_prob_5d(close), 252)

def vrs_027_regime_shift_prob_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vrs_002_regime_shift_prob_21d(close), 252)

def vrs_028_regime_shift_prob_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vrs_003_regime_shift_prob_63d(close), 252)

def vrs_029_regime_shift_prob_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vrs_004_regime_shift_prob_126d(close), 252)

def vrs_030_regime_shift_prob_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vrs_005_regime_shift_prob_252d(close), 252)

def vrs_031_regime_change_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vrs_006_regime_change_5d(close), 252)

def vrs_032_regime_change_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vrs_007_regime_change_21d(close), 252)

def vrs_033_regime_change_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vrs_008_regime_change_63d(close), 252)

def vrs_034_regime_change_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vrs_009_regime_change_126d(close), 252)

def vrs_035_regime_change_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vrs_010_regime_change_252d(close), 252)

def vrs_036_regime_duration_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vrs_011_regime_duration_5d(close), 252)

def vrs_037_regime_duration_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vrs_012_regime_duration_21d(close), 252)

def vrs_038_regime_duration_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vrs_013_regime_duration_63d(close), 252)

def vrs_039_regime_duration_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vrs_014_regime_duration_126d(close), 252)

def vrs_040_regime_duration_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vrs_015_regime_duration_252d(close), 252)

def vrs_041_regime_entropy_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vrs_016_regime_entropy_5d(close), 252)

def vrs_042_regime_entropy_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vrs_017_regime_entropy_21d(close), 252)

def vrs_043_regime_entropy_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vrs_018_regime_entropy_63d(close), 252)

def vrs_044_regime_entropy_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vrs_019_regime_entropy_126d(close), 252)

def vrs_045_regime_entropy_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vrs_020_regime_entropy_252d(close), 252)

def vrs_046_regime_zscore_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vrs_021_regime_zscore_5d(close), 252)

def vrs_047_regime_zscore_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vrs_022_regime_zscore_21d(close), 252)

def vrs_048_regime_zscore_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vrs_023_regime_zscore_63d(close), 252)

def vrs_049_regime_zscore_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vrs_024_regime_zscore_126d(close), 252)

def vrs_050_regime_zscore_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vrs_025_regime_zscore_252d(close), 252)

def vrs_051_regime_shift_prob_rank_5d(close) -> pd.Series:
    return vrs_001_regime_shift_prob_5d(close).rolling(252).rank(pct=True)

def vrs_052_regime_shift_prob_rank_21d(close) -> pd.Series:
    return vrs_002_regime_shift_prob_21d(close).rolling(252).rank(pct=True)

def vrs_053_regime_shift_prob_rank_63d(close) -> pd.Series:
    return vrs_003_regime_shift_prob_63d(close).rolling(252).rank(pct=True)

def vrs_054_regime_shift_prob_rank_126d(close) -> pd.Series:
    return vrs_004_regime_shift_prob_126d(close).rolling(252).rank(pct=True)

def vrs_055_regime_shift_prob_rank_252d(close) -> pd.Series:
    return vrs_005_regime_shift_prob_252d(close).rolling(252).rank(pct=True)

def vrs_056_regime_change_rank_5d(close) -> pd.Series:
    return vrs_006_regime_change_5d(close).rolling(252).rank(pct=True)

def vrs_057_regime_change_rank_21d(close) -> pd.Series:
    return vrs_007_regime_change_21d(close).rolling(252).rank(pct=True)

def vrs_058_regime_change_rank_63d(close) -> pd.Series:
    return vrs_008_regime_change_63d(close).rolling(252).rank(pct=True)

def vrs_059_regime_change_rank_126d(close) -> pd.Series:
    return vrs_009_regime_change_126d(close).rolling(252).rank(pct=True)

def vrs_060_regime_change_rank_252d(close) -> pd.Series:
    return vrs_010_regime_change_252d(close).rolling(252).rank(pct=True)

def vrs_061_regime_duration_rank_5d(close) -> pd.Series:
    return vrs_011_regime_duration_5d(close).rolling(252).rank(pct=True)

def vrs_062_regime_duration_rank_21d(close) -> pd.Series:
    return vrs_012_regime_duration_21d(close).rolling(252).rank(pct=True)

def vrs_063_regime_duration_rank_63d(close) -> pd.Series:
    return vrs_013_regime_duration_63d(close).rolling(252).rank(pct=True)

def vrs_064_regime_duration_rank_126d(close) -> pd.Series:
    return vrs_014_regime_duration_126d(close).rolling(252).rank(pct=True)

def vrs_065_regime_duration_rank_252d(close) -> pd.Series:
    return vrs_015_regime_duration_252d(close).rolling(252).rank(pct=True)

def vrs_066_regime_entropy_rank_5d(close) -> pd.Series:
    return vrs_016_regime_entropy_5d(close).rolling(252).rank(pct=True)

def vrs_067_regime_entropy_rank_21d(close) -> pd.Series:
    return vrs_017_regime_entropy_21d(close).rolling(252).rank(pct=True)

def vrs_068_regime_entropy_rank_63d(close) -> pd.Series:
    return vrs_018_regime_entropy_63d(close).rolling(252).rank(pct=True)

def vrs_069_regime_entropy_rank_126d(close) -> pd.Series:
    return vrs_019_regime_entropy_126d(close).rolling(252).rank(pct=True)

def vrs_070_regime_entropy_rank_252d(close) -> pd.Series:
    return vrs_020_regime_entropy_252d(close).rolling(252).rank(pct=True)

def vrs_071_regime_zscore_rank_5d(close) -> pd.Series:
    return vrs_021_regime_zscore_5d(close).rolling(252).rank(pct=True)

def vrs_072_regime_zscore_rank_21d(close) -> pd.Series:
    return vrs_022_regime_zscore_21d(close).rolling(252).rank(pct=True)

def vrs_073_regime_zscore_rank_63d(close) -> pd.Series:
    return vrs_023_regime_zscore_63d(close).rolling(252).rank(pct=True)

def vrs_074_regime_zscore_rank_126d(close) -> pd.Series:
    return vrs_024_regime_zscore_126d(close).rolling(252).rank(pct=True)

def vrs_075_regime_zscore_rank_252d(close) -> pd.Series:
    return vrs_025_regime_zscore_252d(close).rolling(252).rank(pct=True)


# --- Registry ---
V32_REGISTRY = {
    "vrs_001_regime_shift_prob_5d": {"inputs": ['close'], "func": vrs_001_regime_shift_prob_5d},
    "vrs_002_regime_shift_prob_21d": {"inputs": ['close'], "func": vrs_002_regime_shift_prob_21d},
    "vrs_003_regime_shift_prob_63d": {"inputs": ['close'], "func": vrs_003_regime_shift_prob_63d},
    "vrs_004_regime_shift_prob_126d": {"inputs": ['close'], "func": vrs_004_regime_shift_prob_126d},
    "vrs_005_regime_shift_prob_252d": {"inputs": ['close'], "func": vrs_005_regime_shift_prob_252d},
    "vrs_006_regime_change_5d": {"inputs": ['close'], "func": vrs_006_regime_change_5d},
    "vrs_007_regime_change_21d": {"inputs": ['close'], "func": vrs_007_regime_change_21d},
    "vrs_008_regime_change_63d": {"inputs": ['close'], "func": vrs_008_regime_change_63d},
    "vrs_009_regime_change_126d": {"inputs": ['close'], "func": vrs_009_regime_change_126d},
    "vrs_010_regime_change_252d": {"inputs": ['close'], "func": vrs_010_regime_change_252d},
    "vrs_011_regime_duration_5d": {"inputs": ['close'], "func": vrs_011_regime_duration_5d},
    "vrs_012_regime_duration_21d": {"inputs": ['close'], "func": vrs_012_regime_duration_21d},
    "vrs_013_regime_duration_63d": {"inputs": ['close'], "func": vrs_013_regime_duration_63d},
    "vrs_014_regime_duration_126d": {"inputs": ['close'], "func": vrs_014_regime_duration_126d},
    "vrs_015_regime_duration_252d": {"inputs": ['close'], "func": vrs_015_regime_duration_252d},
    "vrs_016_regime_entropy_5d": {"inputs": ['close'], "func": vrs_016_regime_entropy_5d},
    "vrs_017_regime_entropy_21d": {"inputs": ['close'], "func": vrs_017_regime_entropy_21d},
    "vrs_018_regime_entropy_63d": {"inputs": ['close'], "func": vrs_018_regime_entropy_63d},
    "vrs_019_regime_entropy_126d": {"inputs": ['close'], "func": vrs_019_regime_entropy_126d},
    "vrs_020_regime_entropy_252d": {"inputs": ['close'], "func": vrs_020_regime_entropy_252d},
    "vrs_021_regime_zscore_5d": {"inputs": ['close'], "func": vrs_021_regime_zscore_5d},
    "vrs_022_regime_zscore_21d": {"inputs": ['close'], "func": vrs_022_regime_zscore_21d},
    "vrs_023_regime_zscore_63d": {"inputs": ['close'], "func": vrs_023_regime_zscore_63d},
    "vrs_024_regime_zscore_126d": {"inputs": ['close'], "func": vrs_024_regime_zscore_126d},
    "vrs_025_regime_zscore_252d": {"inputs": ['close'], "func": vrs_025_regime_zscore_252d},
    "vrs_026_regime_shift_prob_zscore_5d": {"inputs": ['close'], "func": vrs_026_regime_shift_prob_zscore_5d},
    "vrs_027_regime_shift_prob_zscore_21d": {"inputs": ['close'], "func": vrs_027_regime_shift_prob_zscore_21d},
    "vrs_028_regime_shift_prob_zscore_63d": {"inputs": ['close'], "func": vrs_028_regime_shift_prob_zscore_63d},
    "vrs_029_regime_shift_prob_zscore_126d": {"inputs": ['close'], "func": vrs_029_regime_shift_prob_zscore_126d},
    "vrs_030_regime_shift_prob_zscore_252d": {"inputs": ['close'], "func": vrs_030_regime_shift_prob_zscore_252d},
    "vrs_031_regime_change_zscore_5d": {"inputs": ['close'], "func": vrs_031_regime_change_zscore_5d},
    "vrs_032_regime_change_zscore_21d": {"inputs": ['close'], "func": vrs_032_regime_change_zscore_21d},
    "vrs_033_regime_change_zscore_63d": {"inputs": ['close'], "func": vrs_033_regime_change_zscore_63d},
    "vrs_034_regime_change_zscore_126d": {"inputs": ['close'], "func": vrs_034_regime_change_zscore_126d},
    "vrs_035_regime_change_zscore_252d": {"inputs": ['close'], "func": vrs_035_regime_change_zscore_252d},
    "vrs_036_regime_duration_zscore_5d": {"inputs": ['close'], "func": vrs_036_regime_duration_zscore_5d},
    "vrs_037_regime_duration_zscore_21d": {"inputs": ['close'], "func": vrs_037_regime_duration_zscore_21d},
    "vrs_038_regime_duration_zscore_63d": {"inputs": ['close'], "func": vrs_038_regime_duration_zscore_63d},
    "vrs_039_regime_duration_zscore_126d": {"inputs": ['close'], "func": vrs_039_regime_duration_zscore_126d},
    "vrs_040_regime_duration_zscore_252d": {"inputs": ['close'], "func": vrs_040_regime_duration_zscore_252d},
    "vrs_041_regime_entropy_zscore_5d": {"inputs": ['close'], "func": vrs_041_regime_entropy_zscore_5d},
    "vrs_042_regime_entropy_zscore_21d": {"inputs": ['close'], "func": vrs_042_regime_entropy_zscore_21d},
    "vrs_043_regime_entropy_zscore_63d": {"inputs": ['close'], "func": vrs_043_regime_entropy_zscore_63d},
    "vrs_044_regime_entropy_zscore_126d": {"inputs": ['close'], "func": vrs_044_regime_entropy_zscore_126d},
    "vrs_045_regime_entropy_zscore_252d": {"inputs": ['close'], "func": vrs_045_regime_entropy_zscore_252d},
    "vrs_046_regime_zscore_zscore_5d": {"inputs": ['close'], "func": vrs_046_regime_zscore_zscore_5d},
    "vrs_047_regime_zscore_zscore_21d": {"inputs": ['close'], "func": vrs_047_regime_zscore_zscore_21d},
    "vrs_048_regime_zscore_zscore_63d": {"inputs": ['close'], "func": vrs_048_regime_zscore_zscore_63d},
    "vrs_049_regime_zscore_zscore_126d": {"inputs": ['close'], "func": vrs_049_regime_zscore_zscore_126d},
    "vrs_050_regime_zscore_zscore_252d": {"inputs": ['close'], "func": vrs_050_regime_zscore_zscore_252d},
    "vrs_051_regime_shift_prob_rank_5d": {"inputs": ['close'], "func": vrs_051_regime_shift_prob_rank_5d},
    "vrs_052_regime_shift_prob_rank_21d": {"inputs": ['close'], "func": vrs_052_regime_shift_prob_rank_21d},
    "vrs_053_regime_shift_prob_rank_63d": {"inputs": ['close'], "func": vrs_053_regime_shift_prob_rank_63d},
    "vrs_054_regime_shift_prob_rank_126d": {"inputs": ['close'], "func": vrs_054_regime_shift_prob_rank_126d},
    "vrs_055_regime_shift_prob_rank_252d": {"inputs": ['close'], "func": vrs_055_regime_shift_prob_rank_252d},
    "vrs_056_regime_change_rank_5d": {"inputs": ['close'], "func": vrs_056_regime_change_rank_5d},
    "vrs_057_regime_change_rank_21d": {"inputs": ['close'], "func": vrs_057_regime_change_rank_21d},
    "vrs_058_regime_change_rank_63d": {"inputs": ['close'], "func": vrs_058_regime_change_rank_63d},
    "vrs_059_regime_change_rank_126d": {"inputs": ['close'], "func": vrs_059_regime_change_rank_126d},
    "vrs_060_regime_change_rank_252d": {"inputs": ['close'], "func": vrs_060_regime_change_rank_252d},
    "vrs_061_regime_duration_rank_5d": {"inputs": ['close'], "func": vrs_061_regime_duration_rank_5d},
    "vrs_062_regime_duration_rank_21d": {"inputs": ['close'], "func": vrs_062_regime_duration_rank_21d},
    "vrs_063_regime_duration_rank_63d": {"inputs": ['close'], "func": vrs_063_regime_duration_rank_63d},
    "vrs_064_regime_duration_rank_126d": {"inputs": ['close'], "func": vrs_064_regime_duration_rank_126d},
    "vrs_065_regime_duration_rank_252d": {"inputs": ['close'], "func": vrs_065_regime_duration_rank_252d},
    "vrs_066_regime_entropy_rank_5d": {"inputs": ['close'], "func": vrs_066_regime_entropy_rank_5d},
    "vrs_067_regime_entropy_rank_21d": {"inputs": ['close'], "func": vrs_067_regime_entropy_rank_21d},
    "vrs_068_regime_entropy_rank_63d": {"inputs": ['close'], "func": vrs_068_regime_entropy_rank_63d},
    "vrs_069_regime_entropy_rank_126d": {"inputs": ['close'], "func": vrs_069_regime_entropy_rank_126d},
    "vrs_070_regime_entropy_rank_252d": {"inputs": ['close'], "func": vrs_070_regime_entropy_rank_252d},
    "vrs_071_regime_zscore_rank_5d": {"inputs": ['close'], "func": vrs_071_regime_zscore_rank_5d},
    "vrs_072_regime_zscore_rank_21d": {"inputs": ['close'], "func": vrs_072_regime_zscore_rank_21d},
    "vrs_073_regime_zscore_rank_63d": {"inputs": ['close'], "func": vrs_073_regime_zscore_rank_63d},
    "vrs_074_regime_zscore_rank_126d": {"inputs": ['close'], "func": vrs_074_regime_zscore_rank_126d},
    "vrs_075_regime_zscore_rank_252d": {"inputs": ['close'], "func": vrs_075_regime_zscore_rank_252d},
}
