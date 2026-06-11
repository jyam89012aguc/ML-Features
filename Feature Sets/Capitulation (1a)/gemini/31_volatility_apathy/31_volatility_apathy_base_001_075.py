"""
Domain 31: volatility_apathy (vapt_)
Asset Class: US Equities
Target Context: Periods of volatility apathy and compression.
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
def vapt_001_vol_apathy_5d(close) -> pd.Series:
    return 1.0 / (_rolling_std(_daily_ret(close), 5) + _EPS)

def vapt_002_vol_apathy_21d(close) -> pd.Series:
    return 1.0 / (_rolling_std(_daily_ret(close), 21) + _EPS)

def vapt_003_vol_apathy_63d(close) -> pd.Series:
    return 1.0 / (_rolling_std(_daily_ret(close), 63) + _EPS)

def vapt_004_vol_apathy_126d(close) -> pd.Series:
    return 1.0 / (_rolling_std(_daily_ret(close), 126) + _EPS)

def vapt_005_vol_apathy_252d(close) -> pd.Series:
    return 1.0 / (_rolling_std(_daily_ret(close), 252) + _EPS)

def vapt_006_vol_deadzone_5d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 5) < _rolling_std(_daily_ret(close), 252) * 0.5).astype(float).rolling(5).sum()

def vapt_007_vol_deadzone_21d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 21) < _rolling_std(_daily_ret(close), 252) * 0.5).astype(float).rolling(21).sum()

def vapt_008_vol_deadzone_63d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 63) < _rolling_std(_daily_ret(close), 252) * 0.5).astype(float).rolling(63).sum()

def vapt_009_vol_deadzone_126d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 126) < _rolling_std(_daily_ret(close), 252) * 0.5).astype(float).rolling(126).sum()

def vapt_010_vol_deadzone_252d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 252) < _rolling_std(_daily_ret(close), 252) * 0.5).astype(float).rolling(252).sum()

def vapt_011_vol_sleep_5d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 5) == _rolling_min(_rolling_std(_daily_ret(close), 5), 252)).astype(float)

def vapt_012_vol_sleep_21d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 21) == _rolling_min(_rolling_std(_daily_ret(close), 21), 252)).astype(float)

def vapt_013_vol_sleep_63d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 63) == _rolling_min(_rolling_std(_daily_ret(close), 63), 252)).astype(float)

def vapt_014_vol_sleep_126d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 126) == _rolling_min(_rolling_std(_daily_ret(close), 126), 252)).astype(float)

def vapt_015_vol_sleep_252d(close) -> pd.Series:
    return (_rolling_std(_daily_ret(close), 252) == _rolling_min(_rolling_std(_daily_ret(close), 252), 252)).astype(float)

def vapt_016_vol_compression_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5) / (_rolling_max(_daily_ret(close), 5) - _rolling_min(_daily_ret(close), 5)).replace(0, _EPS)

def vapt_017_vol_compression_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21) / (_rolling_max(_daily_ret(close), 21) - _rolling_min(_daily_ret(close), 21)).replace(0, _EPS)

def vapt_018_vol_compression_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63) / (_rolling_max(_daily_ret(close), 63) - _rolling_min(_daily_ret(close), 63)).replace(0, _EPS)

def vapt_019_vol_compression_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126) / (_rolling_max(_daily_ret(close), 126) - _rolling_min(_daily_ret(close), 126)).replace(0, _EPS)

def vapt_020_vol_compression_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252) / (_rolling_max(_daily_ret(close), 252) - _rolling_min(_daily_ret(close), 252)).replace(0, _EPS)

def vapt_021_vol_quiet_days_5d(close) -> pd.Series:
    return (_daily_ret(close).abs() < _rolling_std(_daily_ret(close), 252) * 0.2).astype(float).rolling(5).sum()

def vapt_022_vol_quiet_days_21d(close) -> pd.Series:
    return (_daily_ret(close).abs() < _rolling_std(_daily_ret(close), 252) * 0.2).astype(float).rolling(21).sum()

def vapt_023_vol_quiet_days_63d(close) -> pd.Series:
    return (_daily_ret(close).abs() < _rolling_std(_daily_ret(close), 252) * 0.2).astype(float).rolling(63).sum()

def vapt_024_vol_quiet_days_126d(close) -> pd.Series:
    return (_daily_ret(close).abs() < _rolling_std(_daily_ret(close), 252) * 0.2).astype(float).rolling(126).sum()

def vapt_025_vol_quiet_days_252d(close) -> pd.Series:
    return (_daily_ret(close).abs() < _rolling_std(_daily_ret(close), 252) * 0.2).astype(float).rolling(252).sum()

def vapt_026_vol_apathy_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vapt_001_vol_apathy_5d(close), 252)

def vapt_027_vol_apathy_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vapt_002_vol_apathy_21d(close), 252)

def vapt_028_vol_apathy_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vapt_003_vol_apathy_63d(close), 252)

def vapt_029_vol_apathy_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vapt_004_vol_apathy_126d(close), 252)

def vapt_030_vol_apathy_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vapt_005_vol_apathy_252d(close), 252)

def vapt_031_vol_deadzone_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vapt_006_vol_deadzone_5d(close), 252)

def vapt_032_vol_deadzone_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vapt_007_vol_deadzone_21d(close), 252)

def vapt_033_vol_deadzone_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vapt_008_vol_deadzone_63d(close), 252)

def vapt_034_vol_deadzone_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vapt_009_vol_deadzone_126d(close), 252)

def vapt_035_vol_deadzone_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vapt_010_vol_deadzone_252d(close), 252)

def vapt_036_vol_sleep_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vapt_011_vol_sleep_5d(close), 252)

def vapt_037_vol_sleep_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vapt_012_vol_sleep_21d(close), 252)

def vapt_038_vol_sleep_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vapt_013_vol_sleep_63d(close), 252)

def vapt_039_vol_sleep_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vapt_014_vol_sleep_126d(close), 252)

def vapt_040_vol_sleep_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vapt_015_vol_sleep_252d(close), 252)

def vapt_041_vol_compression_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vapt_016_vol_compression_5d(close), 252)

def vapt_042_vol_compression_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vapt_017_vol_compression_21d(close), 252)

def vapt_043_vol_compression_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vapt_018_vol_compression_63d(close), 252)

def vapt_044_vol_compression_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vapt_019_vol_compression_126d(close), 252)

def vapt_045_vol_compression_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vapt_020_vol_compression_252d(close), 252)

def vapt_046_vol_quiet_days_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vapt_021_vol_quiet_days_5d(close), 252)

def vapt_047_vol_quiet_days_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vapt_022_vol_quiet_days_21d(close), 252)

def vapt_048_vol_quiet_days_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vapt_023_vol_quiet_days_63d(close), 252)

def vapt_049_vol_quiet_days_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vapt_024_vol_quiet_days_126d(close), 252)

def vapt_050_vol_quiet_days_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vapt_025_vol_quiet_days_252d(close), 252)

def vapt_051_vol_apathy_rank_5d(close) -> pd.Series:
    return vapt_001_vol_apathy_5d(close).rolling(252).rank(pct=True)

def vapt_052_vol_apathy_rank_21d(close) -> pd.Series:
    return vapt_002_vol_apathy_21d(close).rolling(252).rank(pct=True)

def vapt_053_vol_apathy_rank_63d(close) -> pd.Series:
    return vapt_003_vol_apathy_63d(close).rolling(252).rank(pct=True)

def vapt_054_vol_apathy_rank_126d(close) -> pd.Series:
    return vapt_004_vol_apathy_126d(close).rolling(252).rank(pct=True)

def vapt_055_vol_apathy_rank_252d(close) -> pd.Series:
    return vapt_005_vol_apathy_252d(close).rolling(252).rank(pct=True)

def vapt_056_vol_deadzone_rank_5d(close) -> pd.Series:
    return vapt_006_vol_deadzone_5d(close).rolling(252).rank(pct=True)

def vapt_057_vol_deadzone_rank_21d(close) -> pd.Series:
    return vapt_007_vol_deadzone_21d(close).rolling(252).rank(pct=True)

def vapt_058_vol_deadzone_rank_63d(close) -> pd.Series:
    return vapt_008_vol_deadzone_63d(close).rolling(252).rank(pct=True)

def vapt_059_vol_deadzone_rank_126d(close) -> pd.Series:
    return vapt_009_vol_deadzone_126d(close).rolling(252).rank(pct=True)

def vapt_060_vol_deadzone_rank_252d(close) -> pd.Series:
    return vapt_010_vol_deadzone_252d(close).rolling(252).rank(pct=True)

def vapt_061_vol_sleep_rank_5d(close) -> pd.Series:
    return vapt_011_vol_sleep_5d(close).rolling(252).rank(pct=True)

def vapt_062_vol_sleep_rank_21d(close) -> pd.Series:
    return vapt_012_vol_sleep_21d(close).rolling(252).rank(pct=True)

def vapt_063_vol_sleep_rank_63d(close) -> pd.Series:
    return vapt_013_vol_sleep_63d(close).rolling(252).rank(pct=True)

def vapt_064_vol_sleep_rank_126d(close) -> pd.Series:
    return vapt_014_vol_sleep_126d(close).rolling(252).rank(pct=True)

def vapt_065_vol_sleep_rank_252d(close) -> pd.Series:
    return vapt_015_vol_sleep_252d(close).rolling(252).rank(pct=True)

def vapt_066_vol_compression_rank_5d(close) -> pd.Series:
    return vapt_016_vol_compression_5d(close).rolling(252).rank(pct=True)

def vapt_067_vol_compression_rank_21d(close) -> pd.Series:
    return vapt_017_vol_compression_21d(close).rolling(252).rank(pct=True)

def vapt_068_vol_compression_rank_63d(close) -> pd.Series:
    return vapt_018_vol_compression_63d(close).rolling(252).rank(pct=True)

def vapt_069_vol_compression_rank_126d(close) -> pd.Series:
    return vapt_019_vol_compression_126d(close).rolling(252).rank(pct=True)

def vapt_070_vol_compression_rank_252d(close) -> pd.Series:
    return vapt_020_vol_compression_252d(close).rolling(252).rank(pct=True)

def vapt_071_vol_quiet_days_rank_5d(close) -> pd.Series:
    return vapt_021_vol_quiet_days_5d(close).rolling(252).rank(pct=True)

def vapt_072_vol_quiet_days_rank_21d(close) -> pd.Series:
    return vapt_022_vol_quiet_days_21d(close).rolling(252).rank(pct=True)

def vapt_073_vol_quiet_days_rank_63d(close) -> pd.Series:
    return vapt_023_vol_quiet_days_63d(close).rolling(252).rank(pct=True)

def vapt_074_vol_quiet_days_rank_126d(close) -> pd.Series:
    return vapt_024_vol_quiet_days_126d(close).rolling(252).rank(pct=True)

def vapt_075_vol_quiet_days_rank_252d(close) -> pd.Series:
    return vapt_025_vol_quiet_days_252d(close).rolling(252).rank(pct=True)


# --- Registry ---
V31_REGISTRY = {
    "vapt_001_vol_apathy_5d": {"inputs": ['close'], "func": vapt_001_vol_apathy_5d},
    "vapt_002_vol_apathy_21d": {"inputs": ['close'], "func": vapt_002_vol_apathy_21d},
    "vapt_003_vol_apathy_63d": {"inputs": ['close'], "func": vapt_003_vol_apathy_63d},
    "vapt_004_vol_apathy_126d": {"inputs": ['close'], "func": vapt_004_vol_apathy_126d},
    "vapt_005_vol_apathy_252d": {"inputs": ['close'], "func": vapt_005_vol_apathy_252d},
    "vapt_006_vol_deadzone_5d": {"inputs": ['close'], "func": vapt_006_vol_deadzone_5d},
    "vapt_007_vol_deadzone_21d": {"inputs": ['close'], "func": vapt_007_vol_deadzone_21d},
    "vapt_008_vol_deadzone_63d": {"inputs": ['close'], "func": vapt_008_vol_deadzone_63d},
    "vapt_009_vol_deadzone_126d": {"inputs": ['close'], "func": vapt_009_vol_deadzone_126d},
    "vapt_010_vol_deadzone_252d": {"inputs": ['close'], "func": vapt_010_vol_deadzone_252d},
    "vapt_011_vol_sleep_5d": {"inputs": ['close'], "func": vapt_011_vol_sleep_5d},
    "vapt_012_vol_sleep_21d": {"inputs": ['close'], "func": vapt_012_vol_sleep_21d},
    "vapt_013_vol_sleep_63d": {"inputs": ['close'], "func": vapt_013_vol_sleep_63d},
    "vapt_014_vol_sleep_126d": {"inputs": ['close'], "func": vapt_014_vol_sleep_126d},
    "vapt_015_vol_sleep_252d": {"inputs": ['close'], "func": vapt_015_vol_sleep_252d},
    "vapt_016_vol_compression_5d": {"inputs": ['close'], "func": vapt_016_vol_compression_5d},
    "vapt_017_vol_compression_21d": {"inputs": ['close'], "func": vapt_017_vol_compression_21d},
    "vapt_018_vol_compression_63d": {"inputs": ['close'], "func": vapt_018_vol_compression_63d},
    "vapt_019_vol_compression_126d": {"inputs": ['close'], "func": vapt_019_vol_compression_126d},
    "vapt_020_vol_compression_252d": {"inputs": ['close'], "func": vapt_020_vol_compression_252d},
    "vapt_021_vol_quiet_days_5d": {"inputs": ['close'], "func": vapt_021_vol_quiet_days_5d},
    "vapt_022_vol_quiet_days_21d": {"inputs": ['close'], "func": vapt_022_vol_quiet_days_21d},
    "vapt_023_vol_quiet_days_63d": {"inputs": ['close'], "func": vapt_023_vol_quiet_days_63d},
    "vapt_024_vol_quiet_days_126d": {"inputs": ['close'], "func": vapt_024_vol_quiet_days_126d},
    "vapt_025_vol_quiet_days_252d": {"inputs": ['close'], "func": vapt_025_vol_quiet_days_252d},
    "vapt_026_vol_apathy_zscore_5d": {"inputs": ['close'], "func": vapt_026_vol_apathy_zscore_5d},
    "vapt_027_vol_apathy_zscore_21d": {"inputs": ['close'], "func": vapt_027_vol_apathy_zscore_21d},
    "vapt_028_vol_apathy_zscore_63d": {"inputs": ['close'], "func": vapt_028_vol_apathy_zscore_63d},
    "vapt_029_vol_apathy_zscore_126d": {"inputs": ['close'], "func": vapt_029_vol_apathy_zscore_126d},
    "vapt_030_vol_apathy_zscore_252d": {"inputs": ['close'], "func": vapt_030_vol_apathy_zscore_252d},
    "vapt_031_vol_deadzone_zscore_5d": {"inputs": ['close'], "func": vapt_031_vol_deadzone_zscore_5d},
    "vapt_032_vol_deadzone_zscore_21d": {"inputs": ['close'], "func": vapt_032_vol_deadzone_zscore_21d},
    "vapt_033_vol_deadzone_zscore_63d": {"inputs": ['close'], "func": vapt_033_vol_deadzone_zscore_63d},
    "vapt_034_vol_deadzone_zscore_126d": {"inputs": ['close'], "func": vapt_034_vol_deadzone_zscore_126d},
    "vapt_035_vol_deadzone_zscore_252d": {"inputs": ['close'], "func": vapt_035_vol_deadzone_zscore_252d},
    "vapt_036_vol_sleep_zscore_5d": {"inputs": ['close'], "func": vapt_036_vol_sleep_zscore_5d},
    "vapt_037_vol_sleep_zscore_21d": {"inputs": ['close'], "func": vapt_037_vol_sleep_zscore_21d},
    "vapt_038_vol_sleep_zscore_63d": {"inputs": ['close'], "func": vapt_038_vol_sleep_zscore_63d},
    "vapt_039_vol_sleep_zscore_126d": {"inputs": ['close'], "func": vapt_039_vol_sleep_zscore_126d},
    "vapt_040_vol_sleep_zscore_252d": {"inputs": ['close'], "func": vapt_040_vol_sleep_zscore_252d},
    "vapt_041_vol_compression_zscore_5d": {"inputs": ['close'], "func": vapt_041_vol_compression_zscore_5d},
    "vapt_042_vol_compression_zscore_21d": {"inputs": ['close'], "func": vapt_042_vol_compression_zscore_21d},
    "vapt_043_vol_compression_zscore_63d": {"inputs": ['close'], "func": vapt_043_vol_compression_zscore_63d},
    "vapt_044_vol_compression_zscore_126d": {"inputs": ['close'], "func": vapt_044_vol_compression_zscore_126d},
    "vapt_045_vol_compression_zscore_252d": {"inputs": ['close'], "func": vapt_045_vol_compression_zscore_252d},
    "vapt_046_vol_quiet_days_zscore_5d": {"inputs": ['close'], "func": vapt_046_vol_quiet_days_zscore_5d},
    "vapt_047_vol_quiet_days_zscore_21d": {"inputs": ['close'], "func": vapt_047_vol_quiet_days_zscore_21d},
    "vapt_048_vol_quiet_days_zscore_63d": {"inputs": ['close'], "func": vapt_048_vol_quiet_days_zscore_63d},
    "vapt_049_vol_quiet_days_zscore_126d": {"inputs": ['close'], "func": vapt_049_vol_quiet_days_zscore_126d},
    "vapt_050_vol_quiet_days_zscore_252d": {"inputs": ['close'], "func": vapt_050_vol_quiet_days_zscore_252d},
    "vapt_051_vol_apathy_rank_5d": {"inputs": ['close'], "func": vapt_051_vol_apathy_rank_5d},
    "vapt_052_vol_apathy_rank_21d": {"inputs": ['close'], "func": vapt_052_vol_apathy_rank_21d},
    "vapt_053_vol_apathy_rank_63d": {"inputs": ['close'], "func": vapt_053_vol_apathy_rank_63d},
    "vapt_054_vol_apathy_rank_126d": {"inputs": ['close'], "func": vapt_054_vol_apathy_rank_126d},
    "vapt_055_vol_apathy_rank_252d": {"inputs": ['close'], "func": vapt_055_vol_apathy_rank_252d},
    "vapt_056_vol_deadzone_rank_5d": {"inputs": ['close'], "func": vapt_056_vol_deadzone_rank_5d},
    "vapt_057_vol_deadzone_rank_21d": {"inputs": ['close'], "func": vapt_057_vol_deadzone_rank_21d},
    "vapt_058_vol_deadzone_rank_63d": {"inputs": ['close'], "func": vapt_058_vol_deadzone_rank_63d},
    "vapt_059_vol_deadzone_rank_126d": {"inputs": ['close'], "func": vapt_059_vol_deadzone_rank_126d},
    "vapt_060_vol_deadzone_rank_252d": {"inputs": ['close'], "func": vapt_060_vol_deadzone_rank_252d},
    "vapt_061_vol_sleep_rank_5d": {"inputs": ['close'], "func": vapt_061_vol_sleep_rank_5d},
    "vapt_062_vol_sleep_rank_21d": {"inputs": ['close'], "func": vapt_062_vol_sleep_rank_21d},
    "vapt_063_vol_sleep_rank_63d": {"inputs": ['close'], "func": vapt_063_vol_sleep_rank_63d},
    "vapt_064_vol_sleep_rank_126d": {"inputs": ['close'], "func": vapt_064_vol_sleep_rank_126d},
    "vapt_065_vol_sleep_rank_252d": {"inputs": ['close'], "func": vapt_065_vol_sleep_rank_252d},
    "vapt_066_vol_compression_rank_5d": {"inputs": ['close'], "func": vapt_066_vol_compression_rank_5d},
    "vapt_067_vol_compression_rank_21d": {"inputs": ['close'], "func": vapt_067_vol_compression_rank_21d},
    "vapt_068_vol_compression_rank_63d": {"inputs": ['close'], "func": vapt_068_vol_compression_rank_63d},
    "vapt_069_vol_compression_rank_126d": {"inputs": ['close'], "func": vapt_069_vol_compression_rank_126d},
    "vapt_070_vol_compression_rank_252d": {"inputs": ['close'], "func": vapt_070_vol_compression_rank_252d},
    "vapt_071_vol_quiet_days_rank_5d": {"inputs": ['close'], "func": vapt_071_vol_quiet_days_rank_5d},
    "vapt_072_vol_quiet_days_rank_21d": {"inputs": ['close'], "func": vapt_072_vol_quiet_days_rank_21d},
    "vapt_073_vol_quiet_days_rank_63d": {"inputs": ['close'], "func": vapt_073_vol_quiet_days_rank_63d},
    "vapt_074_vol_quiet_days_rank_126d": {"inputs": ['close'], "func": vapt_074_vol_quiet_days_rank_126d},
    "vapt_075_vol_quiet_days_rank_252d": {"inputs": ['close'], "func": vapt_075_vol_quiet_days_rank_252d},
}
