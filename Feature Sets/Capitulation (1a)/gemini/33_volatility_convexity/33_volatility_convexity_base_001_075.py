"""
Domain 33: volatility_convexity (vcvx_)
Asset Class: US Equities
Target Context: Convexity and higher-order Greek proxies for vol.
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
def vcvx_001_vol_convexity_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5).diff().diff()

def vcvx_002_vol_convexity_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21).diff().diff()

def vcvx_003_vol_convexity_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63).diff().diff()

def vcvx_004_vol_convexity_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126).diff().diff()

def vcvx_005_vol_convexity_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252).diff().diff()

def vcvx_006_vol_gamma_proxy_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5).diff() / close.diff().replace(0, _EPS)

def vcvx_007_vol_gamma_proxy_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21).diff() / close.diff().replace(0, _EPS)

def vcvx_008_vol_gamma_proxy_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63).diff() / close.diff().replace(0, _EPS)

def vcvx_009_vol_gamma_proxy_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126).diff() / close.diff().replace(0, _EPS)

def vcvx_010_vol_gamma_proxy_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252).diff() / close.diff().replace(0, _EPS)

def vcvx_011_vol_vanna_proxy_5d(close, volume) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5).diff() / volume.diff().replace(0, _EPS)

def vcvx_012_vol_vanna_proxy_21d(close, volume) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21).diff() / volume.diff().replace(0, _EPS)

def vcvx_013_vol_vanna_proxy_63d(close, volume) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63).diff() / volume.diff().replace(0, _EPS)

def vcvx_014_vol_vanna_proxy_126d(close, volume) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126).diff() / volume.diff().replace(0, _EPS)

def vcvx_015_vol_vanna_proxy_252d(close, volume) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252).diff() / volume.diff().replace(0, _EPS)

def vcvx_016_vol_curvature_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5).rolling(5).apply(lambda x: np.polyfit(np.arange(len(x)), x, 2)[0] if len(x)>0 else np.nan, raw=True)

def vcvx_017_vol_curvature_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21).rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 2)[0] if len(x)>0 else np.nan, raw=True)

def vcvx_018_vol_curvature_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63).rolling(63).apply(lambda x: np.polyfit(np.arange(len(x)), x, 2)[0] if len(x)>0 else np.nan, raw=True)

def vcvx_019_vol_curvature_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126).rolling(126).apply(lambda x: np.polyfit(np.arange(len(x)), x, 2)[0] if len(x)>0 else np.nan, raw=True)

def vcvx_020_vol_curvature_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252).rolling(252).apply(lambda x: np.polyfit(np.arange(len(x)), x, 2)[0] if len(x)>0 else np.nan, raw=True)

def vcvx_021_vol_vomma_proxy_5d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 5).diff().diff()

def vcvx_022_vol_vomma_proxy_21d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 21).diff().diff()

def vcvx_023_vol_vomma_proxy_63d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 63).diff().diff()

def vcvx_024_vol_vomma_proxy_126d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 126).diff().diff()

def vcvx_025_vol_vomma_proxy_252d(close) -> pd.Series:
    return _rolling_std(_daily_ret(close), 252).diff().diff()

def vcvx_026_vol_convexity_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vcvx_001_vol_convexity_5d(close), 252)

def vcvx_027_vol_convexity_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vcvx_002_vol_convexity_21d(close), 252)

def vcvx_028_vol_convexity_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vcvx_003_vol_convexity_63d(close), 252)

def vcvx_029_vol_convexity_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vcvx_004_vol_convexity_126d(close), 252)

def vcvx_030_vol_convexity_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vcvx_005_vol_convexity_252d(close), 252)

def vcvx_031_vol_gamma_proxy_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vcvx_006_vol_gamma_proxy_5d(close), 252)

def vcvx_032_vol_gamma_proxy_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vcvx_007_vol_gamma_proxy_21d(close), 252)

def vcvx_033_vol_gamma_proxy_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vcvx_008_vol_gamma_proxy_63d(close), 252)

def vcvx_034_vol_gamma_proxy_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vcvx_009_vol_gamma_proxy_126d(close), 252)

def vcvx_035_vol_gamma_proxy_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vcvx_010_vol_gamma_proxy_252d(close), 252)

def vcvx_036_vol_vanna_proxy_zscore_5d(close, volume) -> pd.Series:
    return _zscore_rolling(vcvx_011_vol_vanna_proxy_5d(close, volume), 252)

def vcvx_037_vol_vanna_proxy_zscore_21d(close, volume) -> pd.Series:
    return _zscore_rolling(vcvx_012_vol_vanna_proxy_21d(close, volume), 252)

def vcvx_038_vol_vanna_proxy_zscore_63d(close, volume) -> pd.Series:
    return _zscore_rolling(vcvx_013_vol_vanna_proxy_63d(close, volume), 252)

def vcvx_039_vol_vanna_proxy_zscore_126d(close, volume) -> pd.Series:
    return _zscore_rolling(vcvx_014_vol_vanna_proxy_126d(close, volume), 252)

def vcvx_040_vol_vanna_proxy_zscore_252d(close, volume) -> pd.Series:
    return _zscore_rolling(vcvx_015_vol_vanna_proxy_252d(close, volume), 252)

def vcvx_041_vol_curvature_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vcvx_016_vol_curvature_5d(close), 252)

def vcvx_042_vol_curvature_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vcvx_017_vol_curvature_21d(close), 252)

def vcvx_043_vol_curvature_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vcvx_018_vol_curvature_63d(close), 252)

def vcvx_044_vol_curvature_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vcvx_019_vol_curvature_126d(close), 252)

def vcvx_045_vol_curvature_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vcvx_020_vol_curvature_252d(close), 252)

def vcvx_046_vol_vomma_proxy_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(vcvx_021_vol_vomma_proxy_5d(close), 252)

def vcvx_047_vol_vomma_proxy_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(vcvx_022_vol_vomma_proxy_21d(close), 252)

def vcvx_048_vol_vomma_proxy_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(vcvx_023_vol_vomma_proxy_63d(close), 252)

def vcvx_049_vol_vomma_proxy_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(vcvx_024_vol_vomma_proxy_126d(close), 252)

def vcvx_050_vol_vomma_proxy_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(vcvx_025_vol_vomma_proxy_252d(close), 252)

def vcvx_051_vol_convexity_rank_5d(close) -> pd.Series:
    return vcvx_001_vol_convexity_5d(close).rolling(252).rank(pct=True)

def vcvx_052_vol_convexity_rank_21d(close) -> pd.Series:
    return vcvx_002_vol_convexity_21d(close).rolling(252).rank(pct=True)

def vcvx_053_vol_convexity_rank_63d(close) -> pd.Series:
    return vcvx_003_vol_convexity_63d(close).rolling(252).rank(pct=True)

def vcvx_054_vol_convexity_rank_126d(close) -> pd.Series:
    return vcvx_004_vol_convexity_126d(close).rolling(252).rank(pct=True)

def vcvx_055_vol_convexity_rank_252d(close) -> pd.Series:
    return vcvx_005_vol_convexity_252d(close).rolling(252).rank(pct=True)

def vcvx_056_vol_gamma_proxy_rank_5d(close) -> pd.Series:
    return vcvx_006_vol_gamma_proxy_5d(close).rolling(252).rank(pct=True)

def vcvx_057_vol_gamma_proxy_rank_21d(close) -> pd.Series:
    return vcvx_007_vol_gamma_proxy_21d(close).rolling(252).rank(pct=True)

def vcvx_058_vol_gamma_proxy_rank_63d(close) -> pd.Series:
    return vcvx_008_vol_gamma_proxy_63d(close).rolling(252).rank(pct=True)

def vcvx_059_vol_gamma_proxy_rank_126d(close) -> pd.Series:
    return vcvx_009_vol_gamma_proxy_126d(close).rolling(252).rank(pct=True)

def vcvx_060_vol_gamma_proxy_rank_252d(close) -> pd.Series:
    return vcvx_010_vol_gamma_proxy_252d(close).rolling(252).rank(pct=True)

def vcvx_061_vol_vanna_proxy_rank_5d(close, volume) -> pd.Series:
    return vcvx_011_vol_vanna_proxy_5d(close, volume).rolling(252).rank(pct=True)

def vcvx_062_vol_vanna_proxy_rank_21d(close, volume) -> pd.Series:
    return vcvx_012_vol_vanna_proxy_21d(close, volume).rolling(252).rank(pct=True)

def vcvx_063_vol_vanna_proxy_rank_63d(close, volume) -> pd.Series:
    return vcvx_013_vol_vanna_proxy_63d(close, volume).rolling(252).rank(pct=True)

def vcvx_064_vol_vanna_proxy_rank_126d(close, volume) -> pd.Series:
    return vcvx_014_vol_vanna_proxy_126d(close, volume).rolling(252).rank(pct=True)

def vcvx_065_vol_vanna_proxy_rank_252d(close, volume) -> pd.Series:
    return vcvx_015_vol_vanna_proxy_252d(close, volume).rolling(252).rank(pct=True)

def vcvx_066_vol_curvature_rank_5d(close) -> pd.Series:
    return vcvx_016_vol_curvature_5d(close).rolling(252).rank(pct=True)

def vcvx_067_vol_curvature_rank_21d(close) -> pd.Series:
    return vcvx_017_vol_curvature_21d(close).rolling(252).rank(pct=True)

def vcvx_068_vol_curvature_rank_63d(close) -> pd.Series:
    return vcvx_018_vol_curvature_63d(close).rolling(252).rank(pct=True)

def vcvx_069_vol_curvature_rank_126d(close) -> pd.Series:
    return vcvx_019_vol_curvature_126d(close).rolling(252).rank(pct=True)

def vcvx_070_vol_curvature_rank_252d(close) -> pd.Series:
    return vcvx_020_vol_curvature_252d(close).rolling(252).rank(pct=True)

def vcvx_071_vol_vomma_proxy_rank_5d(close) -> pd.Series:
    return vcvx_021_vol_vomma_proxy_5d(close).rolling(252).rank(pct=True)

def vcvx_072_vol_vomma_proxy_rank_21d(close) -> pd.Series:
    return vcvx_022_vol_vomma_proxy_21d(close).rolling(252).rank(pct=True)

def vcvx_073_vol_vomma_proxy_rank_63d(close) -> pd.Series:
    return vcvx_023_vol_vomma_proxy_63d(close).rolling(252).rank(pct=True)

def vcvx_074_vol_vomma_proxy_rank_126d(close) -> pd.Series:
    return vcvx_024_vol_vomma_proxy_126d(close).rolling(252).rank(pct=True)

def vcvx_075_vol_vomma_proxy_rank_252d(close) -> pd.Series:
    return vcvx_025_vol_vomma_proxy_252d(close).rolling(252).rank(pct=True)


# --- Registry ---
V33_REGISTRY = {
    "vcvx_001_vol_convexity_5d": {"inputs": ['close'], "func": vcvx_001_vol_convexity_5d},
    "vcvx_002_vol_convexity_21d": {"inputs": ['close'], "func": vcvx_002_vol_convexity_21d},
    "vcvx_003_vol_convexity_63d": {"inputs": ['close'], "func": vcvx_003_vol_convexity_63d},
    "vcvx_004_vol_convexity_126d": {"inputs": ['close'], "func": vcvx_004_vol_convexity_126d},
    "vcvx_005_vol_convexity_252d": {"inputs": ['close'], "func": vcvx_005_vol_convexity_252d},
    "vcvx_006_vol_gamma_proxy_5d": {"inputs": ['close'], "func": vcvx_006_vol_gamma_proxy_5d},
    "vcvx_007_vol_gamma_proxy_21d": {"inputs": ['close'], "func": vcvx_007_vol_gamma_proxy_21d},
    "vcvx_008_vol_gamma_proxy_63d": {"inputs": ['close'], "func": vcvx_008_vol_gamma_proxy_63d},
    "vcvx_009_vol_gamma_proxy_126d": {"inputs": ['close'], "func": vcvx_009_vol_gamma_proxy_126d},
    "vcvx_010_vol_gamma_proxy_252d": {"inputs": ['close'], "func": vcvx_010_vol_gamma_proxy_252d},
    "vcvx_011_vol_vanna_proxy_5d": {"inputs": ['close', 'volume'], "func": vcvx_011_vol_vanna_proxy_5d},
    "vcvx_012_vol_vanna_proxy_21d": {"inputs": ['close', 'volume'], "func": vcvx_012_vol_vanna_proxy_21d},
    "vcvx_013_vol_vanna_proxy_63d": {"inputs": ['close', 'volume'], "func": vcvx_013_vol_vanna_proxy_63d},
    "vcvx_014_vol_vanna_proxy_126d": {"inputs": ['close', 'volume'], "func": vcvx_014_vol_vanna_proxy_126d},
    "vcvx_015_vol_vanna_proxy_252d": {"inputs": ['close', 'volume'], "func": vcvx_015_vol_vanna_proxy_252d},
    "vcvx_016_vol_curvature_5d": {"inputs": ['close'], "func": vcvx_016_vol_curvature_5d},
    "vcvx_017_vol_curvature_21d": {"inputs": ['close'], "func": vcvx_017_vol_curvature_21d},
    "vcvx_018_vol_curvature_63d": {"inputs": ['close'], "func": vcvx_018_vol_curvature_63d},
    "vcvx_019_vol_curvature_126d": {"inputs": ['close'], "func": vcvx_019_vol_curvature_126d},
    "vcvx_020_vol_curvature_252d": {"inputs": ['close'], "func": vcvx_020_vol_curvature_252d},
    "vcvx_021_vol_vomma_proxy_5d": {"inputs": ['close'], "func": vcvx_021_vol_vomma_proxy_5d},
    "vcvx_022_vol_vomma_proxy_21d": {"inputs": ['close'], "func": vcvx_022_vol_vomma_proxy_21d},
    "vcvx_023_vol_vomma_proxy_63d": {"inputs": ['close'], "func": vcvx_023_vol_vomma_proxy_63d},
    "vcvx_024_vol_vomma_proxy_126d": {"inputs": ['close'], "func": vcvx_024_vol_vomma_proxy_126d},
    "vcvx_025_vol_vomma_proxy_252d": {"inputs": ['close'], "func": vcvx_025_vol_vomma_proxy_252d},
    "vcvx_026_vol_convexity_zscore_5d": {"inputs": ['close'], "func": vcvx_026_vol_convexity_zscore_5d},
    "vcvx_027_vol_convexity_zscore_21d": {"inputs": ['close'], "func": vcvx_027_vol_convexity_zscore_21d},
    "vcvx_028_vol_convexity_zscore_63d": {"inputs": ['close'], "func": vcvx_028_vol_convexity_zscore_63d},
    "vcvx_029_vol_convexity_zscore_126d": {"inputs": ['close'], "func": vcvx_029_vol_convexity_zscore_126d},
    "vcvx_030_vol_convexity_zscore_252d": {"inputs": ['close'], "func": vcvx_030_vol_convexity_zscore_252d},
    "vcvx_031_vol_gamma_proxy_zscore_5d": {"inputs": ['close'], "func": vcvx_031_vol_gamma_proxy_zscore_5d},
    "vcvx_032_vol_gamma_proxy_zscore_21d": {"inputs": ['close'], "func": vcvx_032_vol_gamma_proxy_zscore_21d},
    "vcvx_033_vol_gamma_proxy_zscore_63d": {"inputs": ['close'], "func": vcvx_033_vol_gamma_proxy_zscore_63d},
    "vcvx_034_vol_gamma_proxy_zscore_126d": {"inputs": ['close'], "func": vcvx_034_vol_gamma_proxy_zscore_126d},
    "vcvx_035_vol_gamma_proxy_zscore_252d": {"inputs": ['close'], "func": vcvx_035_vol_gamma_proxy_zscore_252d},
    "vcvx_036_vol_vanna_proxy_zscore_5d": {"inputs": ['close', 'volume'], "func": vcvx_036_vol_vanna_proxy_zscore_5d},
    "vcvx_037_vol_vanna_proxy_zscore_21d": {"inputs": ['close', 'volume'], "func": vcvx_037_vol_vanna_proxy_zscore_21d},
    "vcvx_038_vol_vanna_proxy_zscore_63d": {"inputs": ['close', 'volume'], "func": vcvx_038_vol_vanna_proxy_zscore_63d},
    "vcvx_039_vol_vanna_proxy_zscore_126d": {"inputs": ['close', 'volume'], "func": vcvx_039_vol_vanna_proxy_zscore_126d},
    "vcvx_040_vol_vanna_proxy_zscore_252d": {"inputs": ['close', 'volume'], "func": vcvx_040_vol_vanna_proxy_zscore_252d},
    "vcvx_041_vol_curvature_zscore_5d": {"inputs": ['close'], "func": vcvx_041_vol_curvature_zscore_5d},
    "vcvx_042_vol_curvature_zscore_21d": {"inputs": ['close'], "func": vcvx_042_vol_curvature_zscore_21d},
    "vcvx_043_vol_curvature_zscore_63d": {"inputs": ['close'], "func": vcvx_043_vol_curvature_zscore_63d},
    "vcvx_044_vol_curvature_zscore_126d": {"inputs": ['close'], "func": vcvx_044_vol_curvature_zscore_126d},
    "vcvx_045_vol_curvature_zscore_252d": {"inputs": ['close'], "func": vcvx_045_vol_curvature_zscore_252d},
    "vcvx_046_vol_vomma_proxy_zscore_5d": {"inputs": ['close'], "func": vcvx_046_vol_vomma_proxy_zscore_5d},
    "vcvx_047_vol_vomma_proxy_zscore_21d": {"inputs": ['close'], "func": vcvx_047_vol_vomma_proxy_zscore_21d},
    "vcvx_048_vol_vomma_proxy_zscore_63d": {"inputs": ['close'], "func": vcvx_048_vol_vomma_proxy_zscore_63d},
    "vcvx_049_vol_vomma_proxy_zscore_126d": {"inputs": ['close'], "func": vcvx_049_vol_vomma_proxy_zscore_126d},
    "vcvx_050_vol_vomma_proxy_zscore_252d": {"inputs": ['close'], "func": vcvx_050_vol_vomma_proxy_zscore_252d},
    "vcvx_051_vol_convexity_rank_5d": {"inputs": ['close'], "func": vcvx_051_vol_convexity_rank_5d},
    "vcvx_052_vol_convexity_rank_21d": {"inputs": ['close'], "func": vcvx_052_vol_convexity_rank_21d},
    "vcvx_053_vol_convexity_rank_63d": {"inputs": ['close'], "func": vcvx_053_vol_convexity_rank_63d},
    "vcvx_054_vol_convexity_rank_126d": {"inputs": ['close'], "func": vcvx_054_vol_convexity_rank_126d},
    "vcvx_055_vol_convexity_rank_252d": {"inputs": ['close'], "func": vcvx_055_vol_convexity_rank_252d},
    "vcvx_056_vol_gamma_proxy_rank_5d": {"inputs": ['close'], "func": vcvx_056_vol_gamma_proxy_rank_5d},
    "vcvx_057_vol_gamma_proxy_rank_21d": {"inputs": ['close'], "func": vcvx_057_vol_gamma_proxy_rank_21d},
    "vcvx_058_vol_gamma_proxy_rank_63d": {"inputs": ['close'], "func": vcvx_058_vol_gamma_proxy_rank_63d},
    "vcvx_059_vol_gamma_proxy_rank_126d": {"inputs": ['close'], "func": vcvx_059_vol_gamma_proxy_rank_126d},
    "vcvx_060_vol_gamma_proxy_rank_252d": {"inputs": ['close'], "func": vcvx_060_vol_gamma_proxy_rank_252d},
    "vcvx_061_vol_vanna_proxy_rank_5d": {"inputs": ['close', 'volume'], "func": vcvx_061_vol_vanna_proxy_rank_5d},
    "vcvx_062_vol_vanna_proxy_rank_21d": {"inputs": ['close', 'volume'], "func": vcvx_062_vol_vanna_proxy_rank_21d},
    "vcvx_063_vol_vanna_proxy_rank_63d": {"inputs": ['close', 'volume'], "func": vcvx_063_vol_vanna_proxy_rank_63d},
    "vcvx_064_vol_vanna_proxy_rank_126d": {"inputs": ['close', 'volume'], "func": vcvx_064_vol_vanna_proxy_rank_126d},
    "vcvx_065_vol_vanna_proxy_rank_252d": {"inputs": ['close', 'volume'], "func": vcvx_065_vol_vanna_proxy_rank_252d},
    "vcvx_066_vol_curvature_rank_5d": {"inputs": ['close'], "func": vcvx_066_vol_curvature_rank_5d},
    "vcvx_067_vol_curvature_rank_21d": {"inputs": ['close'], "func": vcvx_067_vol_curvature_rank_21d},
    "vcvx_068_vol_curvature_rank_63d": {"inputs": ['close'], "func": vcvx_068_vol_curvature_rank_63d},
    "vcvx_069_vol_curvature_rank_126d": {"inputs": ['close'], "func": vcvx_069_vol_curvature_rank_126d},
    "vcvx_070_vol_curvature_rank_252d": {"inputs": ['close'], "func": vcvx_070_vol_curvature_rank_252d},
    "vcvx_071_vol_vomma_proxy_rank_5d": {"inputs": ['close'], "func": vcvx_071_vol_vomma_proxy_rank_5d},
    "vcvx_072_vol_vomma_proxy_rank_21d": {"inputs": ['close'], "func": vcvx_072_vol_vomma_proxy_rank_21d},
    "vcvx_073_vol_vomma_proxy_rank_63d": {"inputs": ['close'], "func": vcvx_073_vol_vomma_proxy_rank_63d},
    "vcvx_074_vol_vomma_proxy_rank_126d": {"inputs": ['close'], "func": vcvx_074_vol_vomma_proxy_rank_126d},
    "vcvx_075_vol_vomma_proxy_rank_252d": {"inputs": ['close'], "func": vcvx_075_vol_vomma_proxy_rank_252d},
}
