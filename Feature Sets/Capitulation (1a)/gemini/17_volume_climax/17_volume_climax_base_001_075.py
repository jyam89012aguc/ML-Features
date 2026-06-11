"""
Domain 17: volume_climax (vcl_)
Asset Class: US Equities
Target Context: Volume climax at price exhaustion points.
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
def vcl_001_climax_magnitude_5d(volume) -> pd.Series:
    return _safe_div(volume, _rolling_mean(volume, 252))

def vcl_002_climax_magnitude_21d(volume) -> pd.Series:
    return _safe_div(volume, _rolling_mean(volume, 252))

def vcl_003_climax_magnitude_63d(volume) -> pd.Series:
    return _safe_div(volume, _rolling_mean(volume, 252))

def vcl_004_climax_magnitude_126d(volume) -> pd.Series:
    return _safe_div(volume, _rolling_mean(volume, 252))

def vcl_005_climax_magnitude_252d(volume) -> pd.Series:
    return _safe_div(volume, _rolling_mean(volume, 252))

def vcl_006_climax_exhaustion_5d(high, low, volume) -> pd.Series:
    return _safe_div(volume, (high - low).replace(0, _EPS))

def vcl_007_climax_exhaustion_21d(high, low, volume) -> pd.Series:
    return _safe_div(volume, (high - low).replace(0, _EPS))

def vcl_008_climax_exhaustion_63d(high, low, volume) -> pd.Series:
    return _safe_div(volume, (high - low).replace(0, _EPS))

def vcl_009_climax_exhaustion_126d(high, low, volume) -> pd.Series:
    return _safe_div(volume, (high - low).replace(0, _EPS))

def vcl_010_climax_exhaustion_252d(high, low, volume) -> pd.Series:
    return _safe_div(volume, (high - low).replace(0, _EPS))

def vcl_011_climax_reversal_5d(close, volume) -> pd.Series:
    return ((volume > _rolling_mean(volume, 5) * 2) & (_daily_ret(close).abs() < _daily_ret(close).abs().rolling(5).mean())).astype(float)

def vcl_012_climax_reversal_21d(close, volume) -> pd.Series:
    return ((volume > _rolling_mean(volume, 21) * 2) & (_daily_ret(close).abs() < _daily_ret(close).abs().rolling(21).mean())).astype(float)

def vcl_013_climax_reversal_63d(close, volume) -> pd.Series:
    return ((volume > _rolling_mean(volume, 63) * 2) & (_daily_ret(close).abs() < _daily_ret(close).abs().rolling(63).mean())).astype(float)

def vcl_014_climax_reversal_126d(close, volume) -> pd.Series:
    return ((volume > _rolling_mean(volume, 126) * 2) & (_daily_ret(close).abs() < _daily_ret(close).abs().rolling(126).mean())).astype(float)

def vcl_015_climax_reversal_252d(close, volume) -> pd.Series:
    return ((volume > _rolling_mean(volume, 252) * 2) & (_daily_ret(close).abs() < _daily_ret(close).abs().rolling(252).mean())).astype(float)

def vcl_016_climax_intensity_5d(volume) -> pd.Series:
    return _rolling_mean(volume, 5) / _rolling_mean(volume, 252)

def vcl_017_climax_intensity_21d(volume) -> pd.Series:
    return _rolling_mean(volume, 21) / _rolling_mean(volume, 252)

def vcl_018_climax_intensity_63d(volume) -> pd.Series:
    return _rolling_mean(volume, 63) / _rolling_mean(volume, 252)

def vcl_019_climax_intensity_126d(volume) -> pd.Series:
    return _rolling_mean(volume, 126) / _rolling_mean(volume, 252)

def vcl_020_climax_intensity_252d(volume) -> pd.Series:
    return _rolling_mean(volume, 252) / _rolling_mean(volume, 252)

def vcl_021_vol_price_divergence_5d(close, volume) -> pd.Series:
    return (np.sign(_daily_ret(close)) != np.sign(volume.diff())).astype(float).rolling(5).sum()

def vcl_022_vol_price_divergence_21d(close, volume) -> pd.Series:
    return (np.sign(_daily_ret(close)) != np.sign(volume.diff())).astype(float).rolling(21).sum()

def vcl_023_vol_price_divergence_63d(close, volume) -> pd.Series:
    return (np.sign(_daily_ret(close)) != np.sign(volume.diff())).astype(float).rolling(63).sum()

def vcl_024_vol_price_divergence_126d(close, volume) -> pd.Series:
    return (np.sign(_daily_ret(close)) != np.sign(volume.diff())).astype(float).rolling(126).sum()

def vcl_025_vol_price_divergence_252d(close, volume) -> pd.Series:
    return (np.sign(_daily_ret(close)) != np.sign(volume.diff())).astype(float).rolling(252).sum()

def vcl_026_climax_magnitude_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vcl_001_climax_magnitude_5d(volume), 252)

def vcl_027_climax_magnitude_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vcl_002_climax_magnitude_21d(volume), 252)

def vcl_028_climax_magnitude_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vcl_003_climax_magnitude_63d(volume), 252)

def vcl_029_climax_magnitude_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vcl_004_climax_magnitude_126d(volume), 252)

def vcl_030_climax_magnitude_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vcl_005_climax_magnitude_252d(volume), 252)

def vcl_031_climax_exhaustion_zscore_5d(high, low, volume) -> pd.Series:
    return _zscore_rolling(vcl_006_climax_exhaustion_5d(high, low, volume), 252)

def vcl_032_climax_exhaustion_zscore_21d(high, low, volume) -> pd.Series:
    return _zscore_rolling(vcl_007_climax_exhaustion_21d(high, low, volume), 252)

def vcl_033_climax_exhaustion_zscore_63d(high, low, volume) -> pd.Series:
    return _zscore_rolling(vcl_008_climax_exhaustion_63d(high, low, volume), 252)

def vcl_034_climax_exhaustion_zscore_126d(high, low, volume) -> pd.Series:
    return _zscore_rolling(vcl_009_climax_exhaustion_126d(high, low, volume), 252)

def vcl_035_climax_exhaustion_zscore_252d(high, low, volume) -> pd.Series:
    return _zscore_rolling(vcl_010_climax_exhaustion_252d(high, low, volume), 252)

def vcl_036_climax_reversal_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(vcl_011_climax_reversal_5d(close, volume), 252)

def vcl_037_climax_reversal_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(vcl_012_climax_reversal_21d(close, volume), 252)

def vcl_038_climax_reversal_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(vcl_013_climax_reversal_63d(close, volume), 252)

def vcl_039_climax_reversal_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(vcl_014_climax_reversal_126d(close, volume), 252)

def vcl_040_climax_reversal_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(vcl_015_climax_reversal_252d(close, volume), 252)

def vcl_041_climax_intensity_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vcl_016_climax_intensity_5d(volume), 252)

def vcl_042_climax_intensity_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vcl_017_climax_intensity_21d(volume), 252)

def vcl_043_climax_intensity_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vcl_018_climax_intensity_63d(volume), 252)

def vcl_044_climax_intensity_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vcl_019_climax_intensity_126d(volume), 252)

def vcl_045_climax_intensity_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vcl_020_climax_intensity_252d(volume), 252)

def vcl_046_vol_price_divergence_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(vcl_021_vol_price_divergence_5d(close, volume), 252)

def vcl_047_vol_price_divergence_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(vcl_022_vol_price_divergence_21d(close, volume), 252)

def vcl_048_vol_price_divergence_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(vcl_023_vol_price_divergence_63d(close, volume), 252)

def vcl_049_vol_price_divergence_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(vcl_024_vol_price_divergence_126d(close, volume), 252)

def vcl_050_vol_price_divergence_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(vcl_025_vol_price_divergence_252d(close, volume), 252)

def vcl_051_climax_magnitude_rank_5d(volume) -> pd.Series:
    return vcl_001_climax_magnitude_5d(volume).rolling(252).rank(pct=True)

def vcl_052_climax_magnitude_rank_21d(volume) -> pd.Series:
    return vcl_002_climax_magnitude_21d(volume).rolling(252).rank(pct=True)

def vcl_053_climax_magnitude_rank_63d(volume) -> pd.Series:
    return vcl_003_climax_magnitude_63d(volume).rolling(252).rank(pct=True)

def vcl_054_climax_magnitude_rank_126d(volume) -> pd.Series:
    return vcl_004_climax_magnitude_126d(volume).rolling(252).rank(pct=True)

def vcl_055_climax_magnitude_rank_252d(volume) -> pd.Series:
    return vcl_005_climax_magnitude_252d(volume).rolling(252).rank(pct=True)

def vcl_056_climax_exhaustion_rank_5d(high, low, volume) -> pd.Series:
    return vcl_006_climax_exhaustion_5d(high, low, volume).rolling(252).rank(pct=True)

def vcl_057_climax_exhaustion_rank_21d(high, low, volume) -> pd.Series:
    return vcl_007_climax_exhaustion_21d(high, low, volume).rolling(252).rank(pct=True)

def vcl_058_climax_exhaustion_rank_63d(high, low, volume) -> pd.Series:
    return vcl_008_climax_exhaustion_63d(high, low, volume).rolling(252).rank(pct=True)

def vcl_059_climax_exhaustion_rank_126d(high, low, volume) -> pd.Series:
    return vcl_009_climax_exhaustion_126d(high, low, volume).rolling(252).rank(pct=True)

def vcl_060_climax_exhaustion_rank_252d(high, low, volume) -> pd.Series:
    return vcl_010_climax_exhaustion_252d(high, low, volume).rolling(252).rank(pct=True)

def vcl_061_climax_reversal_rank_5d(close, volume) -> pd.Series:
    return vcl_011_climax_reversal_5d(close, volume).rolling(252).rank(pct=True)

def vcl_062_climax_reversal_rank_21d(close, volume) -> pd.Series:
    return vcl_012_climax_reversal_21d(close, volume).rolling(252).rank(pct=True)

def vcl_063_climax_reversal_rank_63d(close, volume) -> pd.Series:
    return vcl_013_climax_reversal_63d(close, volume).rolling(252).rank(pct=True)

def vcl_064_climax_reversal_rank_126d(close, volume) -> pd.Series:
    return vcl_014_climax_reversal_126d(close, volume).rolling(252).rank(pct=True)

def vcl_065_climax_reversal_rank_252d(close, volume) -> pd.Series:
    return vcl_015_climax_reversal_252d(close, volume).rolling(252).rank(pct=True)

def vcl_066_climax_intensity_rank_5d(volume) -> pd.Series:
    return vcl_016_climax_intensity_5d(volume).rolling(252).rank(pct=True)

def vcl_067_climax_intensity_rank_21d(volume) -> pd.Series:
    return vcl_017_climax_intensity_21d(volume).rolling(252).rank(pct=True)

def vcl_068_climax_intensity_rank_63d(volume) -> pd.Series:
    return vcl_018_climax_intensity_63d(volume).rolling(252).rank(pct=True)

def vcl_069_climax_intensity_rank_126d(volume) -> pd.Series:
    return vcl_019_climax_intensity_126d(volume).rolling(252).rank(pct=True)

def vcl_070_climax_intensity_rank_252d(volume) -> pd.Series:
    return vcl_020_climax_intensity_252d(volume).rolling(252).rank(pct=True)

def vcl_071_vol_price_divergence_rank_5d(close, volume) -> pd.Series:
    return vcl_021_vol_price_divergence_5d(close, volume).rolling(252).rank(pct=True)

def vcl_072_vol_price_divergence_rank_21d(close, volume) -> pd.Series:
    return vcl_022_vol_price_divergence_21d(close, volume).rolling(252).rank(pct=True)

def vcl_073_vol_price_divergence_rank_63d(close, volume) -> pd.Series:
    return vcl_023_vol_price_divergence_63d(close, volume).rolling(252).rank(pct=True)

def vcl_074_vol_price_divergence_rank_126d(close, volume) -> pd.Series:
    return vcl_024_vol_price_divergence_126d(close, volume).rolling(252).rank(pct=True)

def vcl_075_vol_price_divergence_rank_252d(close, volume) -> pd.Series:
    return vcl_025_vol_price_divergence_252d(close, volume).rolling(252).rank(pct=True)


# --- Registry ---
V17_REGISTRY = {
    "vcl_001_climax_magnitude_5d": {"inputs": ['volume'], "func": vcl_001_climax_magnitude_5d},
    "vcl_002_climax_magnitude_21d": {"inputs": ['volume'], "func": vcl_002_climax_magnitude_21d},
    "vcl_003_climax_magnitude_63d": {"inputs": ['volume'], "func": vcl_003_climax_magnitude_63d},
    "vcl_004_climax_magnitude_126d": {"inputs": ['volume'], "func": vcl_004_climax_magnitude_126d},
    "vcl_005_climax_magnitude_252d": {"inputs": ['volume'], "func": vcl_005_climax_magnitude_252d},
    "vcl_006_climax_exhaustion_5d": {"inputs": ['high', 'low', 'volume'], "func": vcl_006_climax_exhaustion_5d},
    "vcl_007_climax_exhaustion_21d": {"inputs": ['high', 'low', 'volume'], "func": vcl_007_climax_exhaustion_21d},
    "vcl_008_climax_exhaustion_63d": {"inputs": ['high', 'low', 'volume'], "func": vcl_008_climax_exhaustion_63d},
    "vcl_009_climax_exhaustion_126d": {"inputs": ['high', 'low', 'volume'], "func": vcl_009_climax_exhaustion_126d},
    "vcl_010_climax_exhaustion_252d": {"inputs": ['high', 'low', 'volume'], "func": vcl_010_climax_exhaustion_252d},
    "vcl_011_climax_reversal_5d": {"inputs": ['close', 'volume'], "func": vcl_011_climax_reversal_5d},
    "vcl_012_climax_reversal_21d": {"inputs": ['close', 'volume'], "func": vcl_012_climax_reversal_21d},
    "vcl_013_climax_reversal_63d": {"inputs": ['close', 'volume'], "func": vcl_013_climax_reversal_63d},
    "vcl_014_climax_reversal_126d": {"inputs": ['close', 'volume'], "func": vcl_014_climax_reversal_126d},
    "vcl_015_climax_reversal_252d": {"inputs": ['close', 'volume'], "func": vcl_015_climax_reversal_252d},
    "vcl_016_climax_intensity_5d": {"inputs": ['volume'], "func": vcl_016_climax_intensity_5d},
    "vcl_017_climax_intensity_21d": {"inputs": ['volume'], "func": vcl_017_climax_intensity_21d},
    "vcl_018_climax_intensity_63d": {"inputs": ['volume'], "func": vcl_018_climax_intensity_63d},
    "vcl_019_climax_intensity_126d": {"inputs": ['volume'], "func": vcl_019_climax_intensity_126d},
    "vcl_020_climax_intensity_252d": {"inputs": ['volume'], "func": vcl_020_climax_intensity_252d},
    "vcl_021_vol_price_divergence_5d": {"inputs": ['close', 'volume'], "func": vcl_021_vol_price_divergence_5d},
    "vcl_022_vol_price_divergence_21d": {"inputs": ['close', 'volume'], "func": vcl_022_vol_price_divergence_21d},
    "vcl_023_vol_price_divergence_63d": {"inputs": ['close', 'volume'], "func": vcl_023_vol_price_divergence_63d},
    "vcl_024_vol_price_divergence_126d": {"inputs": ['close', 'volume'], "func": vcl_024_vol_price_divergence_126d},
    "vcl_025_vol_price_divergence_252d": {"inputs": ['close', 'volume'], "func": vcl_025_vol_price_divergence_252d},
    "vcl_026_climax_magnitude_zscore_5d": {"inputs": ['volume'], "func": vcl_026_climax_magnitude_zscore_5d},
    "vcl_027_climax_magnitude_zscore_21d": {"inputs": ['volume'], "func": vcl_027_climax_magnitude_zscore_21d},
    "vcl_028_climax_magnitude_zscore_63d": {"inputs": ['volume'], "func": vcl_028_climax_magnitude_zscore_63d},
    "vcl_029_climax_magnitude_zscore_126d": {"inputs": ['volume'], "func": vcl_029_climax_magnitude_zscore_126d},
    "vcl_030_climax_magnitude_zscore_252d": {"inputs": ['volume'], "func": vcl_030_climax_magnitude_zscore_252d},
    "vcl_031_climax_exhaustion_zscore_5d": {"inputs": ['high', 'low', 'volume'], "func": vcl_031_climax_exhaustion_zscore_5d},
    "vcl_032_climax_exhaustion_zscore_21d": {"inputs": ['high', 'low', 'volume'], "func": vcl_032_climax_exhaustion_zscore_21d},
    "vcl_033_climax_exhaustion_zscore_63d": {"inputs": ['high', 'low', 'volume'], "func": vcl_033_climax_exhaustion_zscore_63d},
    "vcl_034_climax_exhaustion_zscore_126d": {"inputs": ['high', 'low', 'volume'], "func": vcl_034_climax_exhaustion_zscore_126d},
    "vcl_035_climax_exhaustion_zscore_252d": {"inputs": ['high', 'low', 'volume'], "func": vcl_035_climax_exhaustion_zscore_252d},
    "vcl_036_climax_reversal_zscore_5d": {"inputs": ['close', 'volume'], "func": vcl_036_climax_reversal_zscore_5d},
    "vcl_037_climax_reversal_zscore_21d": {"inputs": ['close', 'volume'], "func": vcl_037_climax_reversal_zscore_21d},
    "vcl_038_climax_reversal_zscore_63d": {"inputs": ['close', 'volume'], "func": vcl_038_climax_reversal_zscore_63d},
    "vcl_039_climax_reversal_zscore_126d": {"inputs": ['close', 'volume'], "func": vcl_039_climax_reversal_zscore_126d},
    "vcl_040_climax_reversal_zscore_252d": {"inputs": ['close', 'volume'], "func": vcl_040_climax_reversal_zscore_252d},
    "vcl_041_climax_intensity_zscore_5d": {"inputs": ['volume'], "func": vcl_041_climax_intensity_zscore_5d},
    "vcl_042_climax_intensity_zscore_21d": {"inputs": ['volume'], "func": vcl_042_climax_intensity_zscore_21d},
    "vcl_043_climax_intensity_zscore_63d": {"inputs": ['volume'], "func": vcl_043_climax_intensity_zscore_63d},
    "vcl_044_climax_intensity_zscore_126d": {"inputs": ['volume'], "func": vcl_044_climax_intensity_zscore_126d},
    "vcl_045_climax_intensity_zscore_252d": {"inputs": ['volume'], "func": vcl_045_climax_intensity_zscore_252d},
    "vcl_046_vol_price_divergence_zscore_5d": {"inputs": ['close', 'volume'], "func": vcl_046_vol_price_divergence_zscore_5d},
    "vcl_047_vol_price_divergence_zscore_21d": {"inputs": ['close', 'volume'], "func": vcl_047_vol_price_divergence_zscore_21d},
    "vcl_048_vol_price_divergence_zscore_63d": {"inputs": ['close', 'volume'], "func": vcl_048_vol_price_divergence_zscore_63d},
    "vcl_049_vol_price_divergence_zscore_126d": {"inputs": ['close', 'volume'], "func": vcl_049_vol_price_divergence_zscore_126d},
    "vcl_050_vol_price_divergence_zscore_252d": {"inputs": ['close', 'volume'], "func": vcl_050_vol_price_divergence_zscore_252d},
    "vcl_051_climax_magnitude_rank_5d": {"inputs": ['volume'], "func": vcl_051_climax_magnitude_rank_5d},
    "vcl_052_climax_magnitude_rank_21d": {"inputs": ['volume'], "func": vcl_052_climax_magnitude_rank_21d},
    "vcl_053_climax_magnitude_rank_63d": {"inputs": ['volume'], "func": vcl_053_climax_magnitude_rank_63d},
    "vcl_054_climax_magnitude_rank_126d": {"inputs": ['volume'], "func": vcl_054_climax_magnitude_rank_126d},
    "vcl_055_climax_magnitude_rank_252d": {"inputs": ['volume'], "func": vcl_055_climax_magnitude_rank_252d},
    "vcl_056_climax_exhaustion_rank_5d": {"inputs": ['high', 'low', 'volume'], "func": vcl_056_climax_exhaustion_rank_5d},
    "vcl_057_climax_exhaustion_rank_21d": {"inputs": ['high', 'low', 'volume'], "func": vcl_057_climax_exhaustion_rank_21d},
    "vcl_058_climax_exhaustion_rank_63d": {"inputs": ['high', 'low', 'volume'], "func": vcl_058_climax_exhaustion_rank_63d},
    "vcl_059_climax_exhaustion_rank_126d": {"inputs": ['high', 'low', 'volume'], "func": vcl_059_climax_exhaustion_rank_126d},
    "vcl_060_climax_exhaustion_rank_252d": {"inputs": ['high', 'low', 'volume'], "func": vcl_060_climax_exhaustion_rank_252d},
    "vcl_061_climax_reversal_rank_5d": {"inputs": ['close', 'volume'], "func": vcl_061_climax_reversal_rank_5d},
    "vcl_062_climax_reversal_rank_21d": {"inputs": ['close', 'volume'], "func": vcl_062_climax_reversal_rank_21d},
    "vcl_063_climax_reversal_rank_63d": {"inputs": ['close', 'volume'], "func": vcl_063_climax_reversal_rank_63d},
    "vcl_064_climax_reversal_rank_126d": {"inputs": ['close', 'volume'], "func": vcl_064_climax_reversal_rank_126d},
    "vcl_065_climax_reversal_rank_252d": {"inputs": ['close', 'volume'], "func": vcl_065_climax_reversal_rank_252d},
    "vcl_066_climax_intensity_rank_5d": {"inputs": ['volume'], "func": vcl_066_climax_intensity_rank_5d},
    "vcl_067_climax_intensity_rank_21d": {"inputs": ['volume'], "func": vcl_067_climax_intensity_rank_21d},
    "vcl_068_climax_intensity_rank_63d": {"inputs": ['volume'], "func": vcl_068_climax_intensity_rank_63d},
    "vcl_069_climax_intensity_rank_126d": {"inputs": ['volume'], "func": vcl_069_climax_intensity_rank_126d},
    "vcl_070_climax_intensity_rank_252d": {"inputs": ['volume'], "func": vcl_070_climax_intensity_rank_252d},
    "vcl_071_vol_price_divergence_rank_5d": {"inputs": ['close', 'volume'], "func": vcl_071_vol_price_divergence_rank_5d},
    "vcl_072_vol_price_divergence_rank_21d": {"inputs": ['close', 'volume'], "func": vcl_072_vol_price_divergence_rank_21d},
    "vcl_073_vol_price_divergence_rank_63d": {"inputs": ['close', 'volume'], "func": vcl_073_vol_price_divergence_rank_63d},
    "vcl_074_vol_price_divergence_rank_126d": {"inputs": ['close', 'volume'], "func": vcl_074_vol_price_divergence_rank_126d},
    "vcl_075_vol_price_divergence_rank_252d": {"inputs": ['close', 'volume'], "func": vcl_075_vol_price_divergence_rank_252d},
}
