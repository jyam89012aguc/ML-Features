"""
Domain 21: volume_concentration (vcc_)
Asset Class: US Equities
Target Context: Statistical concentration of volume.
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
def vcc_001_vol_gini_proxy_5d(volume) -> pd.Series:
    return _rolling_std(volume, 5) / _rolling_sum(volume, 5)

def vcc_002_vol_gini_proxy_21d(volume) -> pd.Series:
    return _rolling_std(volume, 21) / _rolling_sum(volume, 21)

def vcc_003_vol_gini_proxy_63d(volume) -> pd.Series:
    return _rolling_std(volume, 63) / _rolling_sum(volume, 63)

def vcc_004_vol_gini_proxy_126d(volume) -> pd.Series:
    return _rolling_std(volume, 126) / _rolling_sum(volume, 126)

def vcc_005_vol_gini_proxy_252d(volume) -> pd.Series:
    return _rolling_std(volume, 252) / _rolling_sum(volume, 252)

def vcc_006_vol_kurtosis_5d(volume) -> pd.Series:
    return volume.rolling(5).kurt()

def vcc_007_vol_kurtosis_21d(volume) -> pd.Series:
    return volume.rolling(21).kurt()

def vcc_008_vol_kurtosis_63d(volume) -> pd.Series:
    return volume.rolling(63).kurt()

def vcc_009_vol_kurtosis_126d(volume) -> pd.Series:
    return volume.rolling(126).kurt()

def vcc_010_vol_kurtosis_252d(volume) -> pd.Series:
    return volume.rolling(252).kurt()

def vcc_011_vol_skew_5d(volume) -> pd.Series:
    return volume.rolling(5).skew()

def vcc_012_vol_skew_21d(volume) -> pd.Series:
    return volume.rolling(21).skew()

def vcc_013_vol_skew_63d(volume) -> pd.Series:
    return volume.rolling(63).skew()

def vcc_014_vol_skew_126d(volume) -> pd.Series:
    return volume.rolling(126).skew()

def vcc_015_vol_skew_252d(volume) -> pd.Series:
    return volume.rolling(252).skew()

def vcc_016_concentration_index_5d(volume) -> pd.Series:
    return _rolling_max(volume, 5) / _rolling_sum(volume, 5)

def vcc_017_concentration_index_21d(volume) -> pd.Series:
    return _rolling_max(volume, 21) / _rolling_sum(volume, 21)

def vcc_018_concentration_index_63d(volume) -> pd.Series:
    return _rolling_max(volume, 63) / _rolling_sum(volume, 63)

def vcc_019_concentration_index_126d(volume) -> pd.Series:
    return _rolling_max(volume, 126) / _rolling_sum(volume, 126)

def vcc_020_concentration_index_252d(volume) -> pd.Series:
    return _rolling_max(volume, 252) / _rolling_sum(volume, 252)

def vcc_021_vol_entropy_5d(volume) -> pd.Series:
    return volume.rolling(5).apply(_entropy_calc, raw=False)

def vcc_022_vol_entropy_21d(volume) -> pd.Series:
    return volume.rolling(21).apply(_entropy_calc, raw=False)

def vcc_023_vol_entropy_63d(volume) -> pd.Series:
    return volume.rolling(63).apply(_entropy_calc, raw=False)

def vcc_024_vol_entropy_126d(volume) -> pd.Series:
    return volume.rolling(126).apply(_entropy_calc, raw=False)

def vcc_025_vol_entropy_252d(volume) -> pd.Series:
    return volume.rolling(252).apply(_entropy_calc, raw=False)

def vcc_026_vol_gini_proxy_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vcc_001_vol_gini_proxy_5d(volume), 252)

def vcc_027_vol_gini_proxy_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vcc_002_vol_gini_proxy_21d(volume), 252)

def vcc_028_vol_gini_proxy_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vcc_003_vol_gini_proxy_63d(volume), 252)

def vcc_029_vol_gini_proxy_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vcc_004_vol_gini_proxy_126d(volume), 252)

def vcc_030_vol_gini_proxy_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vcc_005_vol_gini_proxy_252d(volume), 252)

def vcc_031_vol_kurtosis_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vcc_006_vol_kurtosis_5d(volume), 252)

def vcc_032_vol_kurtosis_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vcc_007_vol_kurtosis_21d(volume), 252)

def vcc_033_vol_kurtosis_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vcc_008_vol_kurtosis_63d(volume), 252)

def vcc_034_vol_kurtosis_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vcc_009_vol_kurtosis_126d(volume), 252)

def vcc_035_vol_kurtosis_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vcc_010_vol_kurtosis_252d(volume), 252)

def vcc_036_vol_skew_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vcc_011_vol_skew_5d(volume), 252)

def vcc_037_vol_skew_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vcc_012_vol_skew_21d(volume), 252)

def vcc_038_vol_skew_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vcc_013_vol_skew_63d(volume), 252)

def vcc_039_vol_skew_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vcc_014_vol_skew_126d(volume), 252)

def vcc_040_vol_skew_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vcc_015_vol_skew_252d(volume), 252)

def vcc_041_concentration_index_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vcc_016_concentration_index_5d(volume), 252)

def vcc_042_concentration_index_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vcc_017_concentration_index_21d(volume), 252)

def vcc_043_concentration_index_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vcc_018_concentration_index_63d(volume), 252)

def vcc_044_concentration_index_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vcc_019_concentration_index_126d(volume), 252)

def vcc_045_concentration_index_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vcc_020_concentration_index_252d(volume), 252)

def vcc_046_vol_entropy_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vcc_021_vol_entropy_5d(volume), 252)

def vcc_047_vol_entropy_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vcc_022_vol_entropy_21d(volume), 252)

def vcc_048_vol_entropy_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vcc_023_vol_entropy_63d(volume), 252)

def vcc_049_vol_entropy_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vcc_024_vol_entropy_126d(volume), 252)

def vcc_050_vol_entropy_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vcc_025_vol_entropy_252d(volume), 252)

def vcc_051_vol_gini_proxy_rank_5d(volume) -> pd.Series:
    return vcc_001_vol_gini_proxy_5d(volume).rolling(252).rank(pct=True)

def vcc_052_vol_gini_proxy_rank_21d(volume) -> pd.Series:
    return vcc_002_vol_gini_proxy_21d(volume).rolling(252).rank(pct=True)

def vcc_053_vol_gini_proxy_rank_63d(volume) -> pd.Series:
    return vcc_003_vol_gini_proxy_63d(volume).rolling(252).rank(pct=True)

def vcc_054_vol_gini_proxy_rank_126d(volume) -> pd.Series:
    return vcc_004_vol_gini_proxy_126d(volume).rolling(252).rank(pct=True)

def vcc_055_vol_gini_proxy_rank_252d(volume) -> pd.Series:
    return vcc_005_vol_gini_proxy_252d(volume).rolling(252).rank(pct=True)

def vcc_056_vol_kurtosis_rank_5d(volume) -> pd.Series:
    return vcc_006_vol_kurtosis_5d(volume).rolling(252).rank(pct=True)

def vcc_057_vol_kurtosis_rank_21d(volume) -> pd.Series:
    return vcc_007_vol_kurtosis_21d(volume).rolling(252).rank(pct=True)

def vcc_058_vol_kurtosis_rank_63d(volume) -> pd.Series:
    return vcc_008_vol_kurtosis_63d(volume).rolling(252).rank(pct=True)

def vcc_059_vol_kurtosis_rank_126d(volume) -> pd.Series:
    return vcc_009_vol_kurtosis_126d(volume).rolling(252).rank(pct=True)

def vcc_060_vol_kurtosis_rank_252d(volume) -> pd.Series:
    return vcc_010_vol_kurtosis_252d(volume).rolling(252).rank(pct=True)

def vcc_061_vol_skew_rank_5d(volume) -> pd.Series:
    return vcc_011_vol_skew_5d(volume).rolling(252).rank(pct=True)

def vcc_062_vol_skew_rank_21d(volume) -> pd.Series:
    return vcc_012_vol_skew_21d(volume).rolling(252).rank(pct=True)

def vcc_063_vol_skew_rank_63d(volume) -> pd.Series:
    return vcc_013_vol_skew_63d(volume).rolling(252).rank(pct=True)

def vcc_064_vol_skew_rank_126d(volume) -> pd.Series:
    return vcc_014_vol_skew_126d(volume).rolling(252).rank(pct=True)

def vcc_065_vol_skew_rank_252d(volume) -> pd.Series:
    return vcc_015_vol_skew_252d(volume).rolling(252).rank(pct=True)

def vcc_066_concentration_index_rank_5d(volume) -> pd.Series:
    return vcc_016_concentration_index_5d(volume).rolling(252).rank(pct=True)

def vcc_067_concentration_index_rank_21d(volume) -> pd.Series:
    return vcc_017_concentration_index_21d(volume).rolling(252).rank(pct=True)

def vcc_068_concentration_index_rank_63d(volume) -> pd.Series:
    return vcc_018_concentration_index_63d(volume).rolling(252).rank(pct=True)

def vcc_069_concentration_index_rank_126d(volume) -> pd.Series:
    return vcc_019_concentration_index_126d(volume).rolling(252).rank(pct=True)

def vcc_070_concentration_index_rank_252d(volume) -> pd.Series:
    return vcc_020_concentration_index_252d(volume).rolling(252).rank(pct=True)

def vcc_071_vol_entropy_rank_5d(volume) -> pd.Series:
    return vcc_021_vol_entropy_5d(volume).rolling(252).rank(pct=True)

def vcc_072_vol_entropy_rank_21d(volume) -> pd.Series:
    return vcc_022_vol_entropy_21d(volume).rolling(252).rank(pct=True)

def vcc_073_vol_entropy_rank_63d(volume) -> pd.Series:
    return vcc_023_vol_entropy_63d(volume).rolling(252).rank(pct=True)

def vcc_074_vol_entropy_rank_126d(volume) -> pd.Series:
    return vcc_024_vol_entropy_126d(volume).rolling(252).rank(pct=True)

def vcc_075_vol_entropy_rank_252d(volume) -> pd.Series:
    return vcc_025_vol_entropy_252d(volume).rolling(252).rank(pct=True)


# --- Registry ---
V21_REGISTRY = {
    "vcc_001_vol_gini_proxy_5d": {"inputs": ['volume'], "func": vcc_001_vol_gini_proxy_5d},
    "vcc_002_vol_gini_proxy_21d": {"inputs": ['volume'], "func": vcc_002_vol_gini_proxy_21d},
    "vcc_003_vol_gini_proxy_63d": {"inputs": ['volume'], "func": vcc_003_vol_gini_proxy_63d},
    "vcc_004_vol_gini_proxy_126d": {"inputs": ['volume'], "func": vcc_004_vol_gini_proxy_126d},
    "vcc_005_vol_gini_proxy_252d": {"inputs": ['volume'], "func": vcc_005_vol_gini_proxy_252d},
    "vcc_006_vol_kurtosis_5d": {"inputs": ['volume'], "func": vcc_006_vol_kurtosis_5d},
    "vcc_007_vol_kurtosis_21d": {"inputs": ['volume'], "func": vcc_007_vol_kurtosis_21d},
    "vcc_008_vol_kurtosis_63d": {"inputs": ['volume'], "func": vcc_008_vol_kurtosis_63d},
    "vcc_009_vol_kurtosis_126d": {"inputs": ['volume'], "func": vcc_009_vol_kurtosis_126d},
    "vcc_010_vol_kurtosis_252d": {"inputs": ['volume'], "func": vcc_010_vol_kurtosis_252d},
    "vcc_011_vol_skew_5d": {"inputs": ['volume'], "func": vcc_011_vol_skew_5d},
    "vcc_012_vol_skew_21d": {"inputs": ['volume'], "func": vcc_012_vol_skew_21d},
    "vcc_013_vol_skew_63d": {"inputs": ['volume'], "func": vcc_013_vol_skew_63d},
    "vcc_014_vol_skew_126d": {"inputs": ['volume'], "func": vcc_014_vol_skew_126d},
    "vcc_015_vol_skew_252d": {"inputs": ['volume'], "func": vcc_015_vol_skew_252d},
    "vcc_016_concentration_index_5d": {"inputs": ['volume'], "func": vcc_016_concentration_index_5d},
    "vcc_017_concentration_index_21d": {"inputs": ['volume'], "func": vcc_017_concentration_index_21d},
    "vcc_018_concentration_index_63d": {"inputs": ['volume'], "func": vcc_018_concentration_index_63d},
    "vcc_019_concentration_index_126d": {"inputs": ['volume'], "func": vcc_019_concentration_index_126d},
    "vcc_020_concentration_index_252d": {"inputs": ['volume'], "func": vcc_020_concentration_index_252d},
    "vcc_021_vol_entropy_5d": {"inputs": ['volume'], "func": vcc_021_vol_entropy_5d},
    "vcc_022_vol_entropy_21d": {"inputs": ['volume'], "func": vcc_022_vol_entropy_21d},
    "vcc_023_vol_entropy_63d": {"inputs": ['volume'], "func": vcc_023_vol_entropy_63d},
    "vcc_024_vol_entropy_126d": {"inputs": ['volume'], "func": vcc_024_vol_entropy_126d},
    "vcc_025_vol_entropy_252d": {"inputs": ['volume'], "func": vcc_025_vol_entropy_252d},
    "vcc_026_vol_gini_proxy_zscore_5d": {"inputs": ['volume'], "func": vcc_026_vol_gini_proxy_zscore_5d},
    "vcc_027_vol_gini_proxy_zscore_21d": {"inputs": ['volume'], "func": vcc_027_vol_gini_proxy_zscore_21d},
    "vcc_028_vol_gini_proxy_zscore_63d": {"inputs": ['volume'], "func": vcc_028_vol_gini_proxy_zscore_63d},
    "vcc_029_vol_gini_proxy_zscore_126d": {"inputs": ['volume'], "func": vcc_029_vol_gini_proxy_zscore_126d},
    "vcc_030_vol_gini_proxy_zscore_252d": {"inputs": ['volume'], "func": vcc_030_vol_gini_proxy_zscore_252d},
    "vcc_031_vol_kurtosis_zscore_5d": {"inputs": ['volume'], "func": vcc_031_vol_kurtosis_zscore_5d},
    "vcc_032_vol_kurtosis_zscore_21d": {"inputs": ['volume'], "func": vcc_032_vol_kurtosis_zscore_21d},
    "vcc_033_vol_kurtosis_zscore_63d": {"inputs": ['volume'], "func": vcc_033_vol_kurtosis_zscore_63d},
    "vcc_034_vol_kurtosis_zscore_126d": {"inputs": ['volume'], "func": vcc_034_vol_kurtosis_zscore_126d},
    "vcc_035_vol_kurtosis_zscore_252d": {"inputs": ['volume'], "func": vcc_035_vol_kurtosis_zscore_252d},
    "vcc_036_vol_skew_zscore_5d": {"inputs": ['volume'], "func": vcc_036_vol_skew_zscore_5d},
    "vcc_037_vol_skew_zscore_21d": {"inputs": ['volume'], "func": vcc_037_vol_skew_zscore_21d},
    "vcc_038_vol_skew_zscore_63d": {"inputs": ['volume'], "func": vcc_038_vol_skew_zscore_63d},
    "vcc_039_vol_skew_zscore_126d": {"inputs": ['volume'], "func": vcc_039_vol_skew_zscore_126d},
    "vcc_040_vol_skew_zscore_252d": {"inputs": ['volume'], "func": vcc_040_vol_skew_zscore_252d},
    "vcc_041_concentration_index_zscore_5d": {"inputs": ['volume'], "func": vcc_041_concentration_index_zscore_5d},
    "vcc_042_concentration_index_zscore_21d": {"inputs": ['volume'], "func": vcc_042_concentration_index_zscore_21d},
    "vcc_043_concentration_index_zscore_63d": {"inputs": ['volume'], "func": vcc_043_concentration_index_zscore_63d},
    "vcc_044_concentration_index_zscore_126d": {"inputs": ['volume'], "func": vcc_044_concentration_index_zscore_126d},
    "vcc_045_concentration_index_zscore_252d": {"inputs": ['volume'], "func": vcc_045_concentration_index_zscore_252d},
    "vcc_046_vol_entropy_zscore_5d": {"inputs": ['volume'], "func": vcc_046_vol_entropy_zscore_5d},
    "vcc_047_vol_entropy_zscore_21d": {"inputs": ['volume'], "func": vcc_047_vol_entropy_zscore_21d},
    "vcc_048_vol_entropy_zscore_63d": {"inputs": ['volume'], "func": vcc_048_vol_entropy_zscore_63d},
    "vcc_049_vol_entropy_zscore_126d": {"inputs": ['volume'], "func": vcc_049_vol_entropy_zscore_126d},
    "vcc_050_vol_entropy_zscore_252d": {"inputs": ['volume'], "func": vcc_050_vol_entropy_zscore_252d},
    "vcc_051_vol_gini_proxy_rank_5d": {"inputs": ['volume'], "func": vcc_051_vol_gini_proxy_rank_5d},
    "vcc_052_vol_gini_proxy_rank_21d": {"inputs": ['volume'], "func": vcc_052_vol_gini_proxy_rank_21d},
    "vcc_053_vol_gini_proxy_rank_63d": {"inputs": ['volume'], "func": vcc_053_vol_gini_proxy_rank_63d},
    "vcc_054_vol_gini_proxy_rank_126d": {"inputs": ['volume'], "func": vcc_054_vol_gini_proxy_rank_126d},
    "vcc_055_vol_gini_proxy_rank_252d": {"inputs": ['volume'], "func": vcc_055_vol_gini_proxy_rank_252d},
    "vcc_056_vol_kurtosis_rank_5d": {"inputs": ['volume'], "func": vcc_056_vol_kurtosis_rank_5d},
    "vcc_057_vol_kurtosis_rank_21d": {"inputs": ['volume'], "func": vcc_057_vol_kurtosis_rank_21d},
    "vcc_058_vol_kurtosis_rank_63d": {"inputs": ['volume'], "func": vcc_058_vol_kurtosis_rank_63d},
    "vcc_059_vol_kurtosis_rank_126d": {"inputs": ['volume'], "func": vcc_059_vol_kurtosis_rank_126d},
    "vcc_060_vol_kurtosis_rank_252d": {"inputs": ['volume'], "func": vcc_060_vol_kurtosis_rank_252d},
    "vcc_061_vol_skew_rank_5d": {"inputs": ['volume'], "func": vcc_061_vol_skew_rank_5d},
    "vcc_062_vol_skew_rank_21d": {"inputs": ['volume'], "func": vcc_062_vol_skew_rank_21d},
    "vcc_063_vol_skew_rank_63d": {"inputs": ['volume'], "func": vcc_063_vol_skew_rank_63d},
    "vcc_064_vol_skew_rank_126d": {"inputs": ['volume'], "func": vcc_064_vol_skew_rank_126d},
    "vcc_065_vol_skew_rank_252d": {"inputs": ['volume'], "func": vcc_065_vol_skew_rank_252d},
    "vcc_066_concentration_index_rank_5d": {"inputs": ['volume'], "func": vcc_066_concentration_index_rank_5d},
    "vcc_067_concentration_index_rank_21d": {"inputs": ['volume'], "func": vcc_067_concentration_index_rank_21d},
    "vcc_068_concentration_index_rank_63d": {"inputs": ['volume'], "func": vcc_068_concentration_index_rank_63d},
    "vcc_069_concentration_index_rank_126d": {"inputs": ['volume'], "func": vcc_069_concentration_index_rank_126d},
    "vcc_070_concentration_index_rank_252d": {"inputs": ['volume'], "func": vcc_070_concentration_index_rank_252d},
    "vcc_071_vol_entropy_rank_5d": {"inputs": ['volume'], "func": vcc_071_vol_entropy_rank_5d},
    "vcc_072_vol_entropy_rank_21d": {"inputs": ['volume'], "func": vcc_072_vol_entropy_rank_21d},
    "vcc_073_vol_entropy_rank_63d": {"inputs": ['volume'], "func": vcc_073_vol_entropy_rank_63d},
    "vcc_074_vol_entropy_rank_126d": {"inputs": ['volume'], "func": vcc_074_vol_entropy_rank_126d},
    "vcc_075_vol_entropy_rank_252d": {"inputs": ['volume'], "func": vcc_075_vol_entropy_rank_252d},
}
