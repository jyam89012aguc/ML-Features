"""
Domain 26: volatility_clustering (vcl_)
Asset Class: US Equities
Target Context: Volatility clustering and persistence.
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
def vcl_001_vol_clustering_5d(close) -> pd.Series:
    return _daily_ret(close).abs().rolling(5).corr(_daily_ret(close).abs().shift(1))

def vcl_002_vol_clustering_21d(close) -> pd.Series:
    return _daily_ret(close).abs().rolling(21).corr(_daily_ret(close).abs().shift(1))

def vcl_003_vol_clustering_63d(close) -> pd.Series:
    return _daily_ret(close).abs().rolling(63).corr(_daily_ret(close).abs().shift(1))

def vcl_004_vol_clustering_126d(close) -> pd.Series:
    return _daily_ret(close).abs().rolling(126).corr(_daily_ret(close).abs().shift(1))

def vcl_005_vol_clustering_252d(close) -> pd.Series:
    return _daily_ret(close).abs().rolling(252).corr(_daily_ret(close).abs().shift(1))

def vcl_006_vol_persistence_5d(close) -> pd.Series:
    return ((_daily_ret(close).abs() > _rolling_mean(_daily_ret(close).abs(), 5)).astype(float)).rolling(5).sum()

def vcl_007_vol_persistence_21d(close) -> pd.Series:
    return ((_daily_ret(close).abs() > _rolling_mean(_daily_ret(close).abs(), 21)).astype(float)).rolling(21).sum()

def vcl_008_vol_persistence_63d(close) -> pd.Series:
    return ((_daily_ret(close).abs() > _rolling_mean(_daily_ret(close).abs(), 63)).astype(float)).rolling(63).sum()

def vcl_009_vol_persistence_126d(close) -> pd.Series:
    return ((_daily_ret(close).abs() > _rolling_mean(_daily_ret(close).abs(), 126)).astype(float)).rolling(126).sum()

def vcl_010_vol_persistence_252d(close) -> pd.Series:
    return ((_daily_ret(close).abs() > _rolling_mean(_daily_ret(close).abs(), 252)).astype(float)).rolling(252).sum()

def vcl_011_vol_autocorr_5d(close) -> pd.Series:
    return _daily_ret(close).rolling(5).apply(lambda x: x.autocorr(), raw=False)

def vcl_012_vol_autocorr_21d(close) -> pd.Series:
    return _daily_ret(close).rolling(21).apply(lambda x: x.autocorr(), raw=False)

def vcl_013_vol_autocorr_63d(close) -> pd.Series:
    return _daily_ret(close).rolling(63).apply(lambda x: x.autocorr(), raw=False)

def vcl_014_vol_autocorr_126d(close) -> pd.Series:
    return _daily_ret(close).rolling(126).apply(lambda x: x.autocorr(), raw=False)

def vcl_015_vol_autocorr_252d(close) -> pd.Series:
    return _daily_ret(close).rolling(252).apply(lambda x: x.autocorr(), raw=False)

def vcl_016_vol_regime_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5) / _rolling_std(_daily_ret(close), 252)

def vcl_017_vol_regime_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21) / _rolling_std(_daily_ret(close), 252)

def vcl_018_vol_regime_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63) / _rolling_std(_daily_ret(close), 252)

def vcl_019_vol_regime_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126) / _rolling_std(_daily_ret(close), 252)

def vcl_020_vol_regime_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252) / _rolling_std(_daily_ret(close), 252)

def vcl_021_vol_entropy_5d(close) -> pd.Series:
    return _daily_ret(close).rolling(5).apply(_entropy_calc, raw=False)

def vcl_022_vol_entropy_21d(close) -> pd.Series:
    return _daily_ret(close).rolling(21).apply(_entropy_calc, raw=False)

def vcl_023_vol_entropy_63d(close) -> pd.Series:
    return _daily_ret(close).rolling(63).apply(_entropy_calc, raw=False)

def vcl_024_vol_entropy_126d(close) -> pd.Series:
    return _daily_ret(close).rolling(126).apply(_entropy_calc, raw=False)

def vcl_025_vol_entropy_252d(close) -> pd.Series:
    return _daily_ret(close).rolling(252).apply(_entropy_calc, raw=False)

def vcl_026_vol_clustering_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vcl_001_vol_clustering_5d(close), 252)

def vcl_027_vol_clustering_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vcl_002_vol_clustering_21d(close), 252)

def vcl_028_vol_clustering_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vcl_003_vol_clustering_63d(close), 252)

def vcl_029_vol_clustering_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vcl_004_vol_clustering_126d(close), 252)

def vcl_030_vol_clustering_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vcl_005_vol_clustering_252d(close), 252)

def vcl_031_vol_persistence_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vcl_006_vol_persistence_5d(close), 252)

def vcl_032_vol_persistence_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vcl_007_vol_persistence_21d(close), 252)

def vcl_033_vol_persistence_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vcl_008_vol_persistence_63d(close), 252)

def vcl_034_vol_persistence_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vcl_009_vol_persistence_126d(close), 252)

def vcl_035_vol_persistence_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vcl_010_vol_persistence_252d(close), 252)

def vcl_036_vol_autocorr_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vcl_011_vol_autocorr_5d(close), 252)

def vcl_037_vol_autocorr_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vcl_012_vol_autocorr_21d(close), 252)

def vcl_038_vol_autocorr_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vcl_013_vol_autocorr_63d(close), 252)

def vcl_039_vol_autocorr_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vcl_014_vol_autocorr_126d(close), 252)

def vcl_040_vol_autocorr_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vcl_015_vol_autocorr_252d(close), 252)

def vcl_041_vol_regime_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vcl_016_vol_regime_5d(close), 252)

def vcl_042_vol_regime_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vcl_017_vol_regime_21d(close), 252)

def vcl_043_vol_regime_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vcl_018_vol_regime_63d(close), 252)

def vcl_044_vol_regime_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vcl_019_vol_regime_126d(close), 252)

def vcl_045_vol_regime_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vcl_020_vol_regime_252d(close), 252)

def vcl_046_vol_entropy_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vcl_021_vol_entropy_5d(close), 252)

def vcl_047_vol_entropy_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vcl_022_vol_entropy_21d(close), 252)

def vcl_048_vol_entropy_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vcl_023_vol_entropy_63d(close), 252)

def vcl_049_vol_entropy_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vcl_024_vol_entropy_126d(close), 252)

def vcl_050_vol_entropy_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vcl_025_vol_entropy_252d(close), 252)

def vcl_051_vol_clustering_rank_5d(close) -> pd.Series:
    return vcl_001_vol_clustering_5d(close).rolling(252).rank(pct=True)

def vcl_052_vol_clustering_rank_21d(close) -> pd.Series:
    return vcl_002_vol_clustering_21d(close).rolling(252).rank(pct=True)

def vcl_053_vol_clustering_rank_63d(close) -> pd.Series:
    return vcl_003_vol_clustering_63d(close).rolling(252).rank(pct=True)

def vcl_054_vol_clustering_rank_126d(close) -> pd.Series:
    return vcl_004_vol_clustering_126d(close).rolling(252).rank(pct=True)

def vcl_055_vol_clustering_rank_252d(close) -> pd.Series:
    return vcl_005_vol_clustering_252d(close).rolling(252).rank(pct=True)

def vcl_056_vol_persistence_rank_5d(close) -> pd.Series:
    return vcl_006_vol_persistence_5d(close).rolling(252).rank(pct=True)

def vcl_057_vol_persistence_rank_21d(close) -> pd.Series:
    return vcl_007_vol_persistence_21d(close).rolling(252).rank(pct=True)

def vcl_058_vol_persistence_rank_63d(close) -> pd.Series:
    return vcl_008_vol_persistence_63d(close).rolling(252).rank(pct=True)

def vcl_059_vol_persistence_rank_126d(close) -> pd.Series:
    return vcl_009_vol_persistence_126d(close).rolling(252).rank(pct=True)

def vcl_060_vol_persistence_rank_252d(close) -> pd.Series:
    return vcl_010_vol_persistence_252d(close).rolling(252).rank(pct=True)

def vcl_061_vol_autocorr_rank_5d(close) -> pd.Series:
    return vcl_011_vol_autocorr_5d(close).rolling(252).rank(pct=True)

def vcl_062_vol_autocorr_rank_21d(close) -> pd.Series:
    return vcl_012_vol_autocorr_21d(close).rolling(252).rank(pct=True)

def vcl_063_vol_autocorr_rank_63d(close) -> pd.Series:
    return vcl_013_vol_autocorr_63d(close).rolling(252).rank(pct=True)

def vcl_064_vol_autocorr_rank_126d(close) -> pd.Series:
    return vcl_014_vol_autocorr_126d(close).rolling(252).rank(pct=True)

def vcl_065_vol_autocorr_rank_252d(close) -> pd.Series:
    return vcl_015_vol_autocorr_252d(close).rolling(252).rank(pct=True)

def vcl_066_vol_regime_rank_5d(close) -> pd.Series:
    return vcl_016_vol_regime_5d(close).rolling(252).rank(pct=True)

def vcl_067_vol_regime_rank_21d(close) -> pd.Series:
    return vcl_017_vol_regime_21d(close).rolling(252).rank(pct=True)

def vcl_068_vol_regime_rank_63d(close) -> pd.Series:
    return vcl_018_vol_regime_63d(close).rolling(252).rank(pct=True)

def vcl_069_vol_regime_rank_126d(close) -> pd.Series:
    return vcl_019_vol_regime_126d(close).rolling(252).rank(pct=True)

def vcl_070_vol_regime_rank_252d(close) -> pd.Series:
    return vcl_020_vol_regime_252d(close).rolling(252).rank(pct=True)

def vcl_071_vol_entropy_rank_5d(close) -> pd.Series:
    return vcl_021_vol_entropy_5d(close).rolling(252).rank(pct=True)

def vcl_072_vol_entropy_rank_21d(close) -> pd.Series:
    return vcl_022_vol_entropy_21d(close).rolling(252).rank(pct=True)

def vcl_073_vol_entropy_rank_63d(close) -> pd.Series:
    return vcl_023_vol_entropy_63d(close).rolling(252).rank(pct=True)

def vcl_074_vol_entropy_rank_126d(close) -> pd.Series:
    return vcl_024_vol_entropy_126d(close).rolling(252).rank(pct=True)

def vcl_075_vol_entropy_rank_252d(close) -> pd.Series:
    return vcl_025_vol_entropy_252d(close).rolling(252).rank(pct=True)


# --- Registry ---
V26_REGISTRY = {
    "vcl_001_vol_clustering_5d": {"inputs": ['close'], "func": vcl_001_vol_clustering_5d},
    "vcl_002_vol_clustering_21d": {"inputs": ['close'], "func": vcl_002_vol_clustering_21d},
    "vcl_003_vol_clustering_63d": {"inputs": ['close'], "func": vcl_003_vol_clustering_63d},
    "vcl_004_vol_clustering_126d": {"inputs": ['close'], "func": vcl_004_vol_clustering_126d},
    "vcl_005_vol_clustering_252d": {"inputs": ['close'], "func": vcl_005_vol_clustering_252d},
    "vcl_006_vol_persistence_5d": {"inputs": ['close'], "func": vcl_006_vol_persistence_5d},
    "vcl_007_vol_persistence_21d": {"inputs": ['close'], "func": vcl_007_vol_persistence_21d},
    "vcl_008_vol_persistence_63d": {"inputs": ['close'], "func": vcl_008_vol_persistence_63d},
    "vcl_009_vol_persistence_126d": {"inputs": ['close'], "func": vcl_009_vol_persistence_126d},
    "vcl_010_vol_persistence_252d": {"inputs": ['close'], "func": vcl_010_vol_persistence_252d},
    "vcl_011_vol_autocorr_5d": {"inputs": ['close'], "func": vcl_011_vol_autocorr_5d},
    "vcl_012_vol_autocorr_21d": {"inputs": ['close'], "func": vcl_012_vol_autocorr_21d},
    "vcl_013_vol_autocorr_63d": {"inputs": ['close'], "func": vcl_013_vol_autocorr_63d},
    "vcl_014_vol_autocorr_126d": {"inputs": ['close'], "func": vcl_014_vol_autocorr_126d},
    "vcl_015_vol_autocorr_252d": {"inputs": ['close'], "func": vcl_015_vol_autocorr_252d},
    "vcl_016_vol_regime_5d": {"inputs": ['close'], "func": vcl_016_vol_regime_5d},
    "vcl_017_vol_regime_21d": {"inputs": ['close'], "func": vcl_017_vol_regime_21d},
    "vcl_018_vol_regime_63d": {"inputs": ['close'], "func": vcl_018_vol_regime_63d},
    "vcl_019_vol_regime_126d": {"inputs": ['close'], "func": vcl_019_vol_regime_126d},
    "vcl_020_vol_regime_252d": {"inputs": ['close'], "func": vcl_020_vol_regime_252d},
    "vcl_021_vol_entropy_5d": {"inputs": ['close'], "func": vcl_021_vol_entropy_5d},
    "vcl_022_vol_entropy_21d": {"inputs": ['close'], "func": vcl_022_vol_entropy_21d},
    "vcl_023_vol_entropy_63d": {"inputs": ['close'], "func": vcl_023_vol_entropy_63d},
    "vcl_024_vol_entropy_126d": {"inputs": ['close'], "func": vcl_024_vol_entropy_126d},
    "vcl_025_vol_entropy_252d": {"inputs": ['close'], "func": vcl_025_vol_entropy_252d},
    "vcl_026_vol_clustering_zscore_5d": {"inputs": ['close'], "func": vcl_026_vol_clustering_zscore_5d},
    "vcl_027_vol_clustering_zscore_21d": {"inputs": ['close'], "func": vcl_027_vol_clustering_zscore_21d},
    "vcl_028_vol_clustering_zscore_63d": {"inputs": ['close'], "func": vcl_028_vol_clustering_zscore_63d},
    "vcl_029_vol_clustering_zscore_126d": {"inputs": ['close'], "func": vcl_029_vol_clustering_zscore_126d},
    "vcl_030_vol_clustering_zscore_252d": {"inputs": ['close'], "func": vcl_030_vol_clustering_zscore_252d},
    "vcl_031_vol_persistence_zscore_5d": {"inputs": ['close'], "func": vcl_031_vol_persistence_zscore_5d},
    "vcl_032_vol_persistence_zscore_21d": {"inputs": ['close'], "func": vcl_032_vol_persistence_zscore_21d},
    "vcl_033_vol_persistence_zscore_63d": {"inputs": ['close'], "func": vcl_033_vol_persistence_zscore_63d},
    "vcl_034_vol_persistence_zscore_126d": {"inputs": ['close'], "func": vcl_034_vol_persistence_zscore_126d},
    "vcl_035_vol_persistence_zscore_252d": {"inputs": ['close'], "func": vcl_035_vol_persistence_zscore_252d},
    "vcl_036_vol_autocorr_zscore_5d": {"inputs": ['close'], "func": vcl_036_vol_autocorr_zscore_5d},
    "vcl_037_vol_autocorr_zscore_21d": {"inputs": ['close'], "func": vcl_037_vol_autocorr_zscore_21d},
    "vcl_038_vol_autocorr_zscore_63d": {"inputs": ['close'], "func": vcl_038_vol_autocorr_zscore_63d},
    "vcl_039_vol_autocorr_zscore_126d": {"inputs": ['close'], "func": vcl_039_vol_autocorr_zscore_126d},
    "vcl_040_vol_autocorr_zscore_252d": {"inputs": ['close'], "func": vcl_040_vol_autocorr_zscore_252d},
    "vcl_041_vol_regime_zscore_5d": {"inputs": ['close'], "func": vcl_041_vol_regime_zscore_5d},
    "vcl_042_vol_regime_zscore_21d": {"inputs": ['close'], "func": vcl_042_vol_regime_zscore_21d},
    "vcl_043_vol_regime_zscore_63d": {"inputs": ['close'], "func": vcl_043_vol_regime_zscore_63d},
    "vcl_044_vol_regime_zscore_126d": {"inputs": ['close'], "func": vcl_044_vol_regime_zscore_126d},
    "vcl_045_vol_regime_zscore_252d": {"inputs": ['close'], "func": vcl_045_vol_regime_zscore_252d},
    "vcl_046_vol_entropy_zscore_5d": {"inputs": ['close'], "func": vcl_046_vol_entropy_zscore_5d},
    "vcl_047_vol_entropy_zscore_21d": {"inputs": ['close'], "func": vcl_047_vol_entropy_zscore_21d},
    "vcl_048_vol_entropy_zscore_63d": {"inputs": ['close'], "func": vcl_048_vol_entropy_zscore_63d},
    "vcl_049_vol_entropy_zscore_126d": {"inputs": ['close'], "func": vcl_049_vol_entropy_zscore_126d},
    "vcl_050_vol_entropy_zscore_252d": {"inputs": ['close'], "func": vcl_050_vol_entropy_zscore_252d},
    "vcl_051_vol_clustering_rank_5d": {"inputs": ['close'], "func": vcl_051_vol_clustering_rank_5d},
    "vcl_052_vol_clustering_rank_21d": {"inputs": ['close'], "func": vcl_052_vol_clustering_rank_21d},
    "vcl_053_vol_clustering_rank_63d": {"inputs": ['close'], "func": vcl_053_vol_clustering_rank_63d},
    "vcl_054_vol_clustering_rank_126d": {"inputs": ['close'], "func": vcl_054_vol_clustering_rank_126d},
    "vcl_055_vol_clustering_rank_252d": {"inputs": ['close'], "func": vcl_055_vol_clustering_rank_252d},
    "vcl_056_vol_persistence_rank_5d": {"inputs": ['close'], "func": vcl_056_vol_persistence_rank_5d},
    "vcl_057_vol_persistence_rank_21d": {"inputs": ['close'], "func": vcl_057_vol_persistence_rank_21d},
    "vcl_058_vol_persistence_rank_63d": {"inputs": ['close'], "func": vcl_058_vol_persistence_rank_63d},
    "vcl_059_vol_persistence_rank_126d": {"inputs": ['close'], "func": vcl_059_vol_persistence_rank_126d},
    "vcl_060_vol_persistence_rank_252d": {"inputs": ['close'], "func": vcl_060_vol_persistence_rank_252d},
    "vcl_061_vol_autocorr_rank_5d": {"inputs": ['close'], "func": vcl_061_vol_autocorr_rank_5d},
    "vcl_062_vol_autocorr_rank_21d": {"inputs": ['close'], "func": vcl_062_vol_autocorr_rank_21d},
    "vcl_063_vol_autocorr_rank_63d": {"inputs": ['close'], "func": vcl_063_vol_autocorr_rank_63d},
    "vcl_064_vol_autocorr_rank_126d": {"inputs": ['close'], "func": vcl_064_vol_autocorr_rank_126d},
    "vcl_065_vol_autocorr_rank_252d": {"inputs": ['close'], "func": vcl_065_vol_autocorr_rank_252d},
    "vcl_066_vol_regime_rank_5d": {"inputs": ['close'], "func": vcl_066_vol_regime_rank_5d},
    "vcl_067_vol_regime_rank_21d": {"inputs": ['close'], "func": vcl_067_vol_regime_rank_21d},
    "vcl_068_vol_regime_rank_63d": {"inputs": ['close'], "func": vcl_068_vol_regime_rank_63d},
    "vcl_069_vol_regime_rank_126d": {"inputs": ['close'], "func": vcl_069_vol_regime_rank_126d},
    "vcl_070_vol_regime_rank_252d": {"inputs": ['close'], "func": vcl_070_vol_regime_rank_252d},
    "vcl_071_vol_entropy_rank_5d": {"inputs": ['close'], "func": vcl_071_vol_entropy_rank_5d},
    "vcl_072_vol_entropy_rank_21d": {"inputs": ['close'], "func": vcl_072_vol_entropy_rank_21d},
    "vcl_073_vol_entropy_rank_63d": {"inputs": ['close'], "func": vcl_073_vol_entropy_rank_63d},
    "vcl_074_vol_entropy_rank_126d": {"inputs": ['close'], "func": vcl_074_vol_entropy_rank_126d},
    "vcl_075_vol_entropy_rank_252d": {"inputs": ['close'], "func": vcl_075_vol_entropy_rank_252d},
}
