"""
Domain 15: volume_blowoff (vbol_)
Asset Class: US Equities
Target Context: Volume spikes and blowoff signatures.
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
def vbol_001_vol_spike_5d(volume) -> pd.Series:
    return _safe_div(volume, _rolling_mean(volume, 5))

def vbol_002_vol_spike_21d(volume) -> pd.Series:
    return _safe_div(volume, _rolling_mean(volume, 21))

def vbol_003_vol_spike_63d(volume) -> pd.Series:
    return _safe_div(volume, _rolling_mean(volume, 63))

def vbol_004_vol_spike_126d(volume) -> pd.Series:
    return _safe_div(volume, _rolling_mean(volume, 126))

def vbol_005_vol_spike_252d(volume) -> pd.Series:
    return _safe_div(volume, _rolling_mean(volume, 252))

def vbol_006_vol_price_ratio_5d(close, volume) -> pd.Series:
    return _safe_div(volume, close.diff().abs().rolling(5).sum())

def vbol_007_vol_price_ratio_21d(close, volume) -> pd.Series:
    return _safe_div(volume, close.diff().abs().rolling(21).sum())

def vbol_008_vol_price_ratio_63d(close, volume) -> pd.Series:
    return _safe_div(volume, close.diff().abs().rolling(63).sum())

def vbol_009_vol_price_ratio_126d(close, volume) -> pd.Series:
    return _safe_div(volume, close.diff().abs().rolling(126).sum())

def vbol_010_vol_price_ratio_252d(close, volume) -> pd.Series:
    return _safe_div(volume, close.diff().abs().rolling(252).sum())

def vbol_011_dollar_vol_surge_5d(close, volume) -> pd.Series:
    return _safe_div(volume * close, _rolling_mean(volume * close, 5))

def vbol_012_dollar_vol_surge_21d(close, volume) -> pd.Series:
    return _safe_div(volume * close, _rolling_mean(volume * close, 21))

def vbol_013_dollar_vol_surge_63d(close, volume) -> pd.Series:
    return _safe_div(volume * close, _rolling_mean(volume * close, 63))

def vbol_014_dollar_vol_surge_126d(close, volume) -> pd.Series:
    return _safe_div(volume * close, _rolling_mean(volume * close, 126))

def vbol_015_dollar_vol_surge_252d(close, volume) -> pd.Series:
    return _safe_div(volume * close, _rolling_mean(volume * close, 252))

def vbol_016_blowoff_index_5d(close, volume) -> pd.Series:
    return _safe_div(_daily_ret(close).abs() * volume, _rolling_mean(_daily_ret(close).abs() * volume, 5))

def vbol_017_blowoff_index_21d(close, volume) -> pd.Series:
    return _safe_div(_daily_ret(close).abs() * volume, _rolling_mean(_daily_ret(close).abs() * volume, 21))

def vbol_018_blowoff_index_63d(close, volume) -> pd.Series:
    return _safe_div(_daily_ret(close).abs() * volume, _rolling_mean(_daily_ret(close).abs() * volume, 63))

def vbol_019_blowoff_index_126d(close, volume) -> pd.Series:
    return _safe_div(_daily_ret(close).abs() * volume, _rolling_mean(_daily_ret(close).abs() * volume, 126))

def vbol_020_blowoff_index_252d(close, volume) -> pd.Series:
    return _safe_div(_daily_ret(close).abs() * volume, _rolling_mean(_daily_ret(close).abs() * volume, 252))

def vbol_021_vol_acceleration_5d(volume) -> pd.Series:
    return volume.diff().rolling(5).mean()

def vbol_022_vol_acceleration_21d(volume) -> pd.Series:
    return volume.diff().rolling(21).mean()

def vbol_023_vol_acceleration_63d(volume) -> pd.Series:
    return volume.diff().rolling(63).mean()

def vbol_024_vol_acceleration_126d(volume) -> pd.Series:
    return volume.diff().rolling(126).mean()

def vbol_025_vol_acceleration_252d(volume) -> pd.Series:
    return volume.diff().rolling(252).mean()

def vbol_026_vol_spike_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vbol_001_vol_spike_5d(volume), 252)

def vbol_027_vol_spike_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vbol_002_vol_spike_21d(volume), 252)

def vbol_028_vol_spike_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vbol_003_vol_spike_63d(volume), 252)

def vbol_029_vol_spike_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vbol_004_vol_spike_126d(volume), 252)

def vbol_030_vol_spike_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vbol_005_vol_spike_252d(volume), 252)

def vbol_031_vol_price_ratio_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(vbol_006_vol_price_ratio_5d(close, volume), 252)

def vbol_032_vol_price_ratio_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(vbol_007_vol_price_ratio_21d(close, volume), 252)

def vbol_033_vol_price_ratio_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(vbol_008_vol_price_ratio_63d(close, volume), 252)

def vbol_034_vol_price_ratio_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(vbol_009_vol_price_ratio_126d(close, volume), 252)

def vbol_035_vol_price_ratio_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(vbol_010_vol_price_ratio_252d(close, volume), 252)

def vbol_036_dollar_vol_surge_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(vbol_011_dollar_vol_surge_5d(close, volume), 252)

def vbol_037_dollar_vol_surge_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(vbol_012_dollar_vol_surge_21d(close, volume), 252)

def vbol_038_dollar_vol_surge_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(vbol_013_dollar_vol_surge_63d(close, volume), 252)

def vbol_039_dollar_vol_surge_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(vbol_014_dollar_vol_surge_126d(close, volume), 252)

def vbol_040_dollar_vol_surge_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(vbol_015_dollar_vol_surge_252d(close, volume), 252)

def vbol_041_blowoff_index_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(vbol_016_blowoff_index_5d(close, volume), 252)

def vbol_042_blowoff_index_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(vbol_017_blowoff_index_21d(close, volume), 252)

def vbol_043_blowoff_index_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(vbol_018_blowoff_index_63d(close, volume), 252)

def vbol_044_blowoff_index_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(vbol_019_blowoff_index_126d(close, volume), 252)

def vbol_045_blowoff_index_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(vbol_020_blowoff_index_252d(close, volume), 252)

def vbol_046_vol_acceleration_zscore_5d(volume) -> pd.Series:
    return _zscore_rolling(vbol_021_vol_acceleration_5d(volume), 252)

def vbol_047_vol_acceleration_zscore_21d(volume) -> pd.Series:
    return _zscore_rolling(vbol_022_vol_acceleration_21d(volume), 252)

def vbol_048_vol_acceleration_zscore_63d(volume) -> pd.Series:
    return _zscore_rolling(vbol_023_vol_acceleration_63d(volume), 252)

def vbol_049_vol_acceleration_zscore_126d(volume) -> pd.Series:
    return _zscore_rolling(vbol_024_vol_acceleration_126d(volume), 252)

def vbol_050_vol_acceleration_zscore_252d(volume) -> pd.Series:
    return _zscore_rolling(vbol_025_vol_acceleration_252d(volume), 252)

def vbol_051_vol_spike_rank_5d(volume) -> pd.Series:
    return vbol_001_vol_spike_5d(volume).rolling(252).rank(pct=True)

def vbol_052_vol_spike_rank_21d(volume) -> pd.Series:
    return vbol_002_vol_spike_21d(volume).rolling(252).rank(pct=True)

def vbol_053_vol_spike_rank_63d(volume) -> pd.Series:
    return vbol_003_vol_spike_63d(volume).rolling(252).rank(pct=True)

def vbol_054_vol_spike_rank_126d(volume) -> pd.Series:
    return vbol_004_vol_spike_126d(volume).rolling(252).rank(pct=True)

def vbol_055_vol_spike_rank_252d(volume) -> pd.Series:
    return vbol_005_vol_spike_252d(volume).rolling(252).rank(pct=True)

def vbol_056_vol_price_ratio_rank_5d(close, volume) -> pd.Series:
    return vbol_006_vol_price_ratio_5d(close, volume).rolling(252).rank(pct=True)

def vbol_057_vol_price_ratio_rank_21d(close, volume) -> pd.Series:
    return vbol_007_vol_price_ratio_21d(close, volume).rolling(252).rank(pct=True)

def vbol_058_vol_price_ratio_rank_63d(close, volume) -> pd.Series:
    return vbol_008_vol_price_ratio_63d(close, volume).rolling(252).rank(pct=True)

def vbol_059_vol_price_ratio_rank_126d(close, volume) -> pd.Series:
    return vbol_009_vol_price_ratio_126d(close, volume).rolling(252).rank(pct=True)

def vbol_060_vol_price_ratio_rank_252d(close, volume) -> pd.Series:
    return vbol_010_vol_price_ratio_252d(close, volume).rolling(252).rank(pct=True)

def vbol_061_dollar_vol_surge_rank_5d(close, volume) -> pd.Series:
    return vbol_011_dollar_vol_surge_5d(close, volume).rolling(252).rank(pct=True)

def vbol_062_dollar_vol_surge_rank_21d(close, volume) -> pd.Series:
    return vbol_012_dollar_vol_surge_21d(close, volume).rolling(252).rank(pct=True)

def vbol_063_dollar_vol_surge_rank_63d(close, volume) -> pd.Series:
    return vbol_013_dollar_vol_surge_63d(close, volume).rolling(252).rank(pct=True)

def vbol_064_dollar_vol_surge_rank_126d(close, volume) -> pd.Series:
    return vbol_014_dollar_vol_surge_126d(close, volume).rolling(252).rank(pct=True)

def vbol_065_dollar_vol_surge_rank_252d(close, volume) -> pd.Series:
    return vbol_015_dollar_vol_surge_252d(close, volume).rolling(252).rank(pct=True)

def vbol_066_blowoff_index_rank_5d(close, volume) -> pd.Series:
    return vbol_016_blowoff_index_5d(close, volume).rolling(252).rank(pct=True)

def vbol_067_blowoff_index_rank_21d(close, volume) -> pd.Series:
    return vbol_017_blowoff_index_21d(close, volume).rolling(252).rank(pct=True)

def vbol_068_blowoff_index_rank_63d(close, volume) -> pd.Series:
    return vbol_018_blowoff_index_63d(close, volume).rolling(252).rank(pct=True)

def vbol_069_blowoff_index_rank_126d(close, volume) -> pd.Series:
    return vbol_019_blowoff_index_126d(close, volume).rolling(252).rank(pct=True)

def vbol_070_blowoff_index_rank_252d(close, volume) -> pd.Series:
    return vbol_020_blowoff_index_252d(close, volume).rolling(252).rank(pct=True)

def vbol_071_vol_acceleration_rank_5d(volume) -> pd.Series:
    return vbol_021_vol_acceleration_5d(volume).rolling(252).rank(pct=True)

def vbol_072_vol_acceleration_rank_21d(volume) -> pd.Series:
    return vbol_022_vol_acceleration_21d(volume).rolling(252).rank(pct=True)

def vbol_073_vol_acceleration_rank_63d(volume) -> pd.Series:
    return vbol_023_vol_acceleration_63d(volume).rolling(252).rank(pct=True)

def vbol_074_vol_acceleration_rank_126d(volume) -> pd.Series:
    return vbol_024_vol_acceleration_126d(volume).rolling(252).rank(pct=True)

def vbol_075_vol_acceleration_rank_252d(volume) -> pd.Series:
    return vbol_025_vol_acceleration_252d(volume).rolling(252).rank(pct=True)


# --- Registry ---
V15_REGISTRY = {
    "vbol_001_vol_spike_5d": {"inputs": ['volume'], "func": vbol_001_vol_spike_5d},
    "vbol_002_vol_spike_21d": {"inputs": ['volume'], "func": vbol_002_vol_spike_21d},
    "vbol_003_vol_spike_63d": {"inputs": ['volume'], "func": vbol_003_vol_spike_63d},
    "vbol_004_vol_spike_126d": {"inputs": ['volume'], "func": vbol_004_vol_spike_126d},
    "vbol_005_vol_spike_252d": {"inputs": ['volume'], "func": vbol_005_vol_spike_252d},
    "vbol_006_vol_price_ratio_5d": {"inputs": ['close', 'volume'], "func": vbol_006_vol_price_ratio_5d},
    "vbol_007_vol_price_ratio_21d": {"inputs": ['close', 'volume'], "func": vbol_007_vol_price_ratio_21d},
    "vbol_008_vol_price_ratio_63d": {"inputs": ['close', 'volume'], "func": vbol_008_vol_price_ratio_63d},
    "vbol_009_vol_price_ratio_126d": {"inputs": ['close', 'volume'], "func": vbol_009_vol_price_ratio_126d},
    "vbol_010_vol_price_ratio_252d": {"inputs": ['close', 'volume'], "func": vbol_010_vol_price_ratio_252d},
    "vbol_011_dollar_vol_surge_5d": {"inputs": ['close', 'volume'], "func": vbol_011_dollar_vol_surge_5d},
    "vbol_012_dollar_vol_surge_21d": {"inputs": ['close', 'volume'], "func": vbol_012_dollar_vol_surge_21d},
    "vbol_013_dollar_vol_surge_63d": {"inputs": ['close', 'volume'], "func": vbol_013_dollar_vol_surge_63d},
    "vbol_014_dollar_vol_surge_126d": {"inputs": ['close', 'volume'], "func": vbol_014_dollar_vol_surge_126d},
    "vbol_015_dollar_vol_surge_252d": {"inputs": ['close', 'volume'], "func": vbol_015_dollar_vol_surge_252d},
    "vbol_016_blowoff_index_5d": {"inputs": ['close', 'volume'], "func": vbol_016_blowoff_index_5d},
    "vbol_017_blowoff_index_21d": {"inputs": ['close', 'volume'], "func": vbol_017_blowoff_index_21d},
    "vbol_018_blowoff_index_63d": {"inputs": ['close', 'volume'], "func": vbol_018_blowoff_index_63d},
    "vbol_019_blowoff_index_126d": {"inputs": ['close', 'volume'], "func": vbol_019_blowoff_index_126d},
    "vbol_020_blowoff_index_252d": {"inputs": ['close', 'volume'], "func": vbol_020_blowoff_index_252d},
    "vbol_021_vol_acceleration_5d": {"inputs": ['volume'], "func": vbol_021_vol_acceleration_5d},
    "vbol_022_vol_acceleration_21d": {"inputs": ['volume'], "func": vbol_022_vol_acceleration_21d},
    "vbol_023_vol_acceleration_63d": {"inputs": ['volume'], "func": vbol_023_vol_acceleration_63d},
    "vbol_024_vol_acceleration_126d": {"inputs": ['volume'], "func": vbol_024_vol_acceleration_126d},
    "vbol_025_vol_acceleration_252d": {"inputs": ['volume'], "func": vbol_025_vol_acceleration_252d},
    "vbol_026_vol_spike_zscore_5d": {"inputs": ['volume'], "func": vbol_026_vol_spike_zscore_5d},
    "vbol_027_vol_spike_zscore_21d": {"inputs": ['volume'], "func": vbol_027_vol_spike_zscore_21d},
    "vbol_028_vol_spike_zscore_63d": {"inputs": ['volume'], "func": vbol_028_vol_spike_zscore_63d},
    "vbol_029_vol_spike_zscore_126d": {"inputs": ['volume'], "func": vbol_029_vol_spike_zscore_126d},
    "vbol_030_vol_spike_zscore_252d": {"inputs": ['volume'], "func": vbol_030_vol_spike_zscore_252d},
    "vbol_031_vol_price_ratio_zscore_5d": {"inputs": ['close', 'volume'], "func": vbol_031_vol_price_ratio_zscore_5d},
    "vbol_032_vol_price_ratio_zscore_21d": {"inputs": ['close', 'volume'], "func": vbol_032_vol_price_ratio_zscore_21d},
    "vbol_033_vol_price_ratio_zscore_63d": {"inputs": ['close', 'volume'], "func": vbol_033_vol_price_ratio_zscore_63d},
    "vbol_034_vol_price_ratio_zscore_126d": {"inputs": ['close', 'volume'], "func": vbol_034_vol_price_ratio_zscore_126d},
    "vbol_035_vol_price_ratio_zscore_252d": {"inputs": ['close', 'volume'], "func": vbol_035_vol_price_ratio_zscore_252d},
    "vbol_036_dollar_vol_surge_zscore_5d": {"inputs": ['close', 'volume'], "func": vbol_036_dollar_vol_surge_zscore_5d},
    "vbol_037_dollar_vol_surge_zscore_21d": {"inputs": ['close', 'volume'], "func": vbol_037_dollar_vol_surge_zscore_21d},
    "vbol_038_dollar_vol_surge_zscore_63d": {"inputs": ['close', 'volume'], "func": vbol_038_dollar_vol_surge_zscore_63d},
    "vbol_039_dollar_vol_surge_zscore_126d": {"inputs": ['close', 'volume'], "func": vbol_039_dollar_vol_surge_zscore_126d},
    "vbol_040_dollar_vol_surge_zscore_252d": {"inputs": ['close', 'volume'], "func": vbol_040_dollar_vol_surge_zscore_252d},
    "vbol_041_blowoff_index_zscore_5d": {"inputs": ['close', 'volume'], "func": vbol_041_blowoff_index_zscore_5d},
    "vbol_042_blowoff_index_zscore_21d": {"inputs": ['close', 'volume'], "func": vbol_042_blowoff_index_zscore_21d},
    "vbol_043_blowoff_index_zscore_63d": {"inputs": ['close', 'volume'], "func": vbol_043_blowoff_index_zscore_63d},
    "vbol_044_blowoff_index_zscore_126d": {"inputs": ['close', 'volume'], "func": vbol_044_blowoff_index_zscore_126d},
    "vbol_045_blowoff_index_zscore_252d": {"inputs": ['close', 'volume'], "func": vbol_045_blowoff_index_zscore_252d},
    "vbol_046_vol_acceleration_zscore_5d": {"inputs": ['volume'], "func": vbol_046_vol_acceleration_zscore_5d},
    "vbol_047_vol_acceleration_zscore_21d": {"inputs": ['volume'], "func": vbol_047_vol_acceleration_zscore_21d},
    "vbol_048_vol_acceleration_zscore_63d": {"inputs": ['volume'], "func": vbol_048_vol_acceleration_zscore_63d},
    "vbol_049_vol_acceleration_zscore_126d": {"inputs": ['volume'], "func": vbol_049_vol_acceleration_zscore_126d},
    "vbol_050_vol_acceleration_zscore_252d": {"inputs": ['volume'], "func": vbol_050_vol_acceleration_zscore_252d},
    "vbol_051_vol_spike_rank_5d": {"inputs": ['volume'], "func": vbol_051_vol_spike_rank_5d},
    "vbol_052_vol_spike_rank_21d": {"inputs": ['volume'], "func": vbol_052_vol_spike_rank_21d},
    "vbol_053_vol_spike_rank_63d": {"inputs": ['volume'], "func": vbol_053_vol_spike_rank_63d},
    "vbol_054_vol_spike_rank_126d": {"inputs": ['volume'], "func": vbol_054_vol_spike_rank_126d},
    "vbol_055_vol_spike_rank_252d": {"inputs": ['volume'], "func": vbol_055_vol_spike_rank_252d},
    "vbol_056_vol_price_ratio_rank_5d": {"inputs": ['close', 'volume'], "func": vbol_056_vol_price_ratio_rank_5d},
    "vbol_057_vol_price_ratio_rank_21d": {"inputs": ['close', 'volume'], "func": vbol_057_vol_price_ratio_rank_21d},
    "vbol_058_vol_price_ratio_rank_63d": {"inputs": ['close', 'volume'], "func": vbol_058_vol_price_ratio_rank_63d},
    "vbol_059_vol_price_ratio_rank_126d": {"inputs": ['close', 'volume'], "func": vbol_059_vol_price_ratio_rank_126d},
    "vbol_060_vol_price_ratio_rank_252d": {"inputs": ['close', 'volume'], "func": vbol_060_vol_price_ratio_rank_252d},
    "vbol_061_dollar_vol_surge_rank_5d": {"inputs": ['close', 'volume'], "func": vbol_061_dollar_vol_surge_rank_5d},
    "vbol_062_dollar_vol_surge_rank_21d": {"inputs": ['close', 'volume'], "func": vbol_062_dollar_vol_surge_rank_21d},
    "vbol_063_dollar_vol_surge_rank_63d": {"inputs": ['close', 'volume'], "func": vbol_063_dollar_vol_surge_rank_63d},
    "vbol_064_dollar_vol_surge_rank_126d": {"inputs": ['close', 'volume'], "func": vbol_064_dollar_vol_surge_rank_126d},
    "vbol_065_dollar_vol_surge_rank_252d": {"inputs": ['close', 'volume'], "func": vbol_065_dollar_vol_surge_rank_252d},
    "vbol_066_blowoff_index_rank_5d": {"inputs": ['close', 'volume'], "func": vbol_066_blowoff_index_rank_5d},
    "vbol_067_blowoff_index_rank_21d": {"inputs": ['close', 'volume'], "func": vbol_067_blowoff_index_rank_21d},
    "vbol_068_blowoff_index_rank_63d": {"inputs": ['close', 'volume'], "func": vbol_068_blowoff_index_rank_63d},
    "vbol_069_blowoff_index_rank_126d": {"inputs": ['close', 'volume'], "func": vbol_069_blowoff_index_rank_126d},
    "vbol_070_blowoff_index_rank_252d": {"inputs": ['close', 'volume'], "func": vbol_070_blowoff_index_rank_252d},
    "vbol_071_vol_acceleration_rank_5d": {"inputs": ['volume'], "func": vbol_071_vol_acceleration_rank_5d},
    "vbol_072_vol_acceleration_rank_21d": {"inputs": ['volume'], "func": vbol_072_vol_acceleration_rank_21d},
    "vbol_073_vol_acceleration_rank_63d": {"inputs": ['volume'], "func": vbol_073_vol_acceleration_rank_63d},
    "vbol_074_vol_acceleration_rank_126d": {"inputs": ['volume'], "func": vbol_074_vol_acceleration_rank_126d},
    "vbol_075_vol_acceleration_rank_252d": {"inputs": ['volume'], "func": vbol_075_vol_acceleration_rank_252d},
}
