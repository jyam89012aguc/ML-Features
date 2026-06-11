"""
Domain 11: decline_path_entropy (dpe_)
Asset Class: US Equities
Target Context: Structural complexity and chaos in price decline paths.
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
def dpe_001_ret_entropy_5d(close) -> pd.Series:
    return (_daily_ret(close)).rolling(5).apply(_entropy_calc, raw=False)

def dpe_002_ret_entropy_21d(close) -> pd.Series:
    return (_daily_ret(close)).rolling(21).apply(_entropy_calc, raw=False)

def dpe_003_ret_entropy_63d(close) -> pd.Series:
    return (_daily_ret(close)).rolling(63).apply(_entropy_calc, raw=False)

def dpe_004_ret_entropy_126d(close) -> pd.Series:
    return (_daily_ret(close)).rolling(126).apply(_entropy_calc, raw=False)

def dpe_005_ret_entropy_252d(close) -> pd.Series:
    return (_daily_ret(close)).rolling(252).apply(_entropy_calc, raw=False)

def dpe_006_efficiency_ratio_5d(close) -> pd.Series:
    return _safe_div((close - close.shift(5)).abs(), close.diff().abs().rolling(5).sum())

def dpe_007_efficiency_ratio_21d(close) -> pd.Series:
    return _safe_div((close - close.shift(21)).abs(), close.diff().abs().rolling(21).sum())

def dpe_008_efficiency_ratio_63d(close) -> pd.Series:
    return _safe_div((close - close.shift(63)).abs(), close.diff().abs().rolling(63).sum())

def dpe_009_efficiency_ratio_126d(close) -> pd.Series:
    return _safe_div((close - close.shift(126)).abs(), close.diff().abs().rolling(126).sum())

def dpe_010_efficiency_ratio_252d(close) -> pd.Series:
    return _safe_div((close - close.shift(252)).abs(), close.diff().abs().rolling(252).sum())

def dpe_011_fractal_dim_5d(close) -> pd.Series:
    return _safe_div(np.log(close.diff().abs().rolling(5).sum() + _EPS), np.log(5))

def dpe_012_fractal_dim_21d(close) -> pd.Series:
    return _safe_div(np.log(close.diff().abs().rolling(21).sum() + _EPS), np.log(21))

def dpe_013_fractal_dim_63d(close) -> pd.Series:
    return _safe_div(np.log(close.diff().abs().rolling(63).sum() + _EPS), np.log(63))

def dpe_014_fractal_dim_126d(close) -> pd.Series:
    return _safe_div(np.log(close.diff().abs().rolling(126).sum() + _EPS), np.log(126))

def dpe_015_fractal_dim_252d(close) -> pd.Series:
    return _safe_div(np.log(close.diff().abs().rolling(252).sum() + _EPS), np.log(252))

def dpe_016_dd_jaggedness_5d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).diff().rolling(5).var())(close)

def dpe_017_dd_jaggedness_21d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).diff().rolling(21).var())(close)

def dpe_018_dd_jaggedness_63d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).diff().rolling(63).var())(close)

def dpe_019_dd_jaggedness_126d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).diff().rolling(126).var())(close)

def dpe_020_dd_jaggedness_252d(close) -> pd.Series:
    return (lambda x: _safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max()).diff().rolling(252).var())(close)

def dpe_021_zigzag_index_5d(close) -> pd.Series:
    return (lambda x: (lambda uw: (np.sign(uw.diff()) != np.sign(uw.diff().shift(1))).astype(int).rolling(5).sum())(_safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max())))(close)

def dpe_022_zigzag_index_21d(close) -> pd.Series:
    return (lambda x: (lambda uw: (np.sign(uw.diff()) != np.sign(uw.diff().shift(1))).astype(int).rolling(21).sum())(_safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max())))(close)

def dpe_023_zigzag_index_63d(close) -> pd.Series:
    return (lambda x: (lambda uw: (np.sign(uw.diff()) != np.sign(uw.diff().shift(1))).astype(int).rolling(63).sum())(_safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max())))(close)

def dpe_024_zigzag_index_126d(close) -> pd.Series:
    return (lambda x: (lambda uw: (np.sign(uw.diff()) != np.sign(uw.diff().shift(1))).astype(int).rolling(126).sum())(_safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max())))(close)

def dpe_025_zigzag_index_252d(close) -> pd.Series:
    return (lambda x: (lambda uw: (np.sign(uw.diff()) != np.sign(uw.diff().shift(1))).astype(int).rolling(252).sum())(_safe_div(x - x.rolling(252, min_periods=1).max(), x.rolling(252, min_periods=1).max())))(close)

def dpe_026_ret_entropy_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(dpe_001_ret_entropy_5d(close), 252)

def dpe_027_ret_entropy_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(dpe_002_ret_entropy_21d(close), 252)

def dpe_028_ret_entropy_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(dpe_003_ret_entropy_63d(close), 252)

def dpe_029_ret_entropy_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(dpe_004_ret_entropy_126d(close), 252)

def dpe_030_ret_entropy_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(dpe_005_ret_entropy_252d(close), 252)

def dpe_031_efficiency_ratio_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(dpe_006_efficiency_ratio_5d(close), 252)

def dpe_032_efficiency_ratio_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(dpe_007_efficiency_ratio_21d(close), 252)

def dpe_033_efficiency_ratio_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(dpe_008_efficiency_ratio_63d(close), 252)

def dpe_034_efficiency_ratio_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(dpe_009_efficiency_ratio_126d(close), 252)

def dpe_035_efficiency_ratio_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(dpe_010_efficiency_ratio_252d(close), 252)

def dpe_036_fractal_dim_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(dpe_011_fractal_dim_5d(close), 252)

def dpe_037_fractal_dim_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(dpe_012_fractal_dim_21d(close), 252)

def dpe_038_fractal_dim_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(dpe_013_fractal_dim_63d(close), 252)

def dpe_039_fractal_dim_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(dpe_014_fractal_dim_126d(close), 252)

def dpe_040_fractal_dim_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(dpe_015_fractal_dim_252d(close), 252)

def dpe_041_dd_jaggedness_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(dpe_016_dd_jaggedness_5d(close), 252)

def dpe_042_dd_jaggedness_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(dpe_017_dd_jaggedness_21d(close), 252)

def dpe_043_dd_jaggedness_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(dpe_018_dd_jaggedness_63d(close), 252)

def dpe_044_dd_jaggedness_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(dpe_019_dd_jaggedness_126d(close), 252)

def dpe_045_dd_jaggedness_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(dpe_020_dd_jaggedness_252d(close), 252)

def dpe_046_zigzag_index_zscore_5d(close) -> pd.Series:
    return _zscore_rolling(dpe_021_zigzag_index_5d(close), 252)

def dpe_047_zigzag_index_zscore_21d(close) -> pd.Series:
    return _zscore_rolling(dpe_022_zigzag_index_21d(close), 252)

def dpe_048_zigzag_index_zscore_63d(close) -> pd.Series:
    return _zscore_rolling(dpe_023_zigzag_index_63d(close), 252)

def dpe_049_zigzag_index_zscore_126d(close) -> pd.Series:
    return _zscore_rolling(dpe_024_zigzag_index_126d(close), 252)

def dpe_050_zigzag_index_zscore_252d(close) -> pd.Series:
    return _zscore_rolling(dpe_025_zigzag_index_252d(close), 252)

def dpe_051_ret_entropy_rank_5d(close) -> pd.Series:
    return dpe_001_ret_entropy_5d(close).rolling(252).rank(pct=True)

def dpe_052_ret_entropy_rank_21d(close) -> pd.Series:
    return dpe_002_ret_entropy_21d(close).rolling(252).rank(pct=True)

def dpe_053_ret_entropy_rank_63d(close) -> pd.Series:
    return dpe_003_ret_entropy_63d(close).rolling(252).rank(pct=True)

def dpe_054_ret_entropy_rank_126d(close) -> pd.Series:
    return dpe_004_ret_entropy_126d(close).rolling(252).rank(pct=True)

def dpe_055_ret_entropy_rank_252d(close) -> pd.Series:
    return dpe_005_ret_entropy_252d(close).rolling(252).rank(pct=True)

def dpe_056_efficiency_ratio_rank_5d(close) -> pd.Series:
    return dpe_006_efficiency_ratio_5d(close).rolling(252).rank(pct=True)

def dpe_057_efficiency_ratio_rank_21d(close) -> pd.Series:
    return dpe_007_efficiency_ratio_21d(close).rolling(252).rank(pct=True)

def dpe_058_efficiency_ratio_rank_63d(close) -> pd.Series:
    return dpe_008_efficiency_ratio_63d(close).rolling(252).rank(pct=True)

def dpe_059_efficiency_ratio_rank_126d(close) -> pd.Series:
    return dpe_009_efficiency_ratio_126d(close).rolling(252).rank(pct=True)

def dpe_060_efficiency_ratio_rank_252d(close) -> pd.Series:
    return dpe_010_efficiency_ratio_252d(close).rolling(252).rank(pct=True)

def dpe_061_fractal_dim_rank_5d(close) -> pd.Series:
    return dpe_011_fractal_dim_5d(close).rolling(252).rank(pct=True)

def dpe_062_fractal_dim_rank_21d(close) -> pd.Series:
    return dpe_012_fractal_dim_21d(close).rolling(252).rank(pct=True)

def dpe_063_fractal_dim_rank_63d(close) -> pd.Series:
    return dpe_013_fractal_dim_63d(close).rolling(252).rank(pct=True)

def dpe_064_fractal_dim_rank_126d(close) -> pd.Series:
    return dpe_014_fractal_dim_126d(close).rolling(252).rank(pct=True)

def dpe_065_fractal_dim_rank_252d(close) -> pd.Series:
    return dpe_015_fractal_dim_252d(close).rolling(252).rank(pct=True)

def dpe_066_dd_jaggedness_rank_5d(close) -> pd.Series:
    return dpe_016_dd_jaggedness_5d(close).rolling(252).rank(pct=True)

def dpe_067_dd_jaggedness_rank_21d(close) -> pd.Series:
    return dpe_017_dd_jaggedness_21d(close).rolling(252).rank(pct=True)

def dpe_068_dd_jaggedness_rank_63d(close) -> pd.Series:
    return dpe_018_dd_jaggedness_63d(close).rolling(252).rank(pct=True)

def dpe_069_dd_jaggedness_rank_126d(close) -> pd.Series:
    return dpe_019_dd_jaggedness_126d(close).rolling(252).rank(pct=True)

def dpe_070_dd_jaggedness_rank_252d(close) -> pd.Series:
    return dpe_020_dd_jaggedness_252d(close).rolling(252).rank(pct=True)

def dpe_071_zigzag_index_rank_5d(close) -> pd.Series:
    return dpe_021_zigzag_index_5d(close).rolling(252).rank(pct=True)

def dpe_072_zigzag_index_rank_21d(close) -> pd.Series:
    return dpe_022_zigzag_index_21d(close).rolling(252).rank(pct=True)

def dpe_073_zigzag_index_rank_63d(close) -> pd.Series:
    return dpe_023_zigzag_index_63d(close).rolling(252).rank(pct=True)

def dpe_074_zigzag_index_rank_126d(close) -> pd.Series:
    return dpe_024_zigzag_index_126d(close).rolling(252).rank(pct=True)

def dpe_075_zigzag_index_rank_252d(close) -> pd.Series:
    return dpe_025_zigzag_index_252d(close).rolling(252).rank(pct=True)


# --- Registry ---
V11_REGISTRY = {
    "dpe_001_ret_entropy_5d": {"inputs": ['close'], "func": dpe_001_ret_entropy_5d},
    "dpe_002_ret_entropy_21d": {"inputs": ['close'], "func": dpe_002_ret_entropy_21d},
    "dpe_003_ret_entropy_63d": {"inputs": ['close'], "func": dpe_003_ret_entropy_63d},
    "dpe_004_ret_entropy_126d": {"inputs": ['close'], "func": dpe_004_ret_entropy_126d},
    "dpe_005_ret_entropy_252d": {"inputs": ['close'], "func": dpe_005_ret_entropy_252d},
    "dpe_006_efficiency_ratio_5d": {"inputs": ['close'], "func": dpe_006_efficiency_ratio_5d},
    "dpe_007_efficiency_ratio_21d": {"inputs": ['close'], "func": dpe_007_efficiency_ratio_21d},
    "dpe_008_efficiency_ratio_63d": {"inputs": ['close'], "func": dpe_008_efficiency_ratio_63d},
    "dpe_009_efficiency_ratio_126d": {"inputs": ['close'], "func": dpe_009_efficiency_ratio_126d},
    "dpe_010_efficiency_ratio_252d": {"inputs": ['close'], "func": dpe_010_efficiency_ratio_252d},
    "dpe_011_fractal_dim_5d": {"inputs": ['close'], "func": dpe_011_fractal_dim_5d},
    "dpe_012_fractal_dim_21d": {"inputs": ['close'], "func": dpe_012_fractal_dim_21d},
    "dpe_013_fractal_dim_63d": {"inputs": ['close'], "func": dpe_013_fractal_dim_63d},
    "dpe_014_fractal_dim_126d": {"inputs": ['close'], "func": dpe_014_fractal_dim_126d},
    "dpe_015_fractal_dim_252d": {"inputs": ['close'], "func": dpe_015_fractal_dim_252d},
    "dpe_016_dd_jaggedness_5d": {"inputs": ['close'], "func": dpe_016_dd_jaggedness_5d},
    "dpe_017_dd_jaggedness_21d": {"inputs": ['close'], "func": dpe_017_dd_jaggedness_21d},
    "dpe_018_dd_jaggedness_63d": {"inputs": ['close'], "func": dpe_018_dd_jaggedness_63d},
    "dpe_019_dd_jaggedness_126d": {"inputs": ['close'], "func": dpe_019_dd_jaggedness_126d},
    "dpe_020_dd_jaggedness_252d": {"inputs": ['close'], "func": dpe_020_dd_jaggedness_252d},
    "dpe_021_zigzag_index_5d": {"inputs": ['close'], "func": dpe_021_zigzag_index_5d},
    "dpe_022_zigzag_index_21d": {"inputs": ['close'], "func": dpe_022_zigzag_index_21d},
    "dpe_023_zigzag_index_63d": {"inputs": ['close'], "func": dpe_023_zigzag_index_63d},
    "dpe_024_zigzag_index_126d": {"inputs": ['close'], "func": dpe_024_zigzag_index_126d},
    "dpe_025_zigzag_index_252d": {"inputs": ['close'], "func": dpe_025_zigzag_index_252d},
    "dpe_026_ret_entropy_zscore_5d": {"inputs": ['close'], "func": dpe_026_ret_entropy_zscore_5d},
    "dpe_027_ret_entropy_zscore_21d": {"inputs": ['close'], "func": dpe_027_ret_entropy_zscore_21d},
    "dpe_028_ret_entropy_zscore_63d": {"inputs": ['close'], "func": dpe_028_ret_entropy_zscore_63d},
    "dpe_029_ret_entropy_zscore_126d": {"inputs": ['close'], "func": dpe_029_ret_entropy_zscore_126d},
    "dpe_030_ret_entropy_zscore_252d": {"inputs": ['close'], "func": dpe_030_ret_entropy_zscore_252d},
    "dpe_031_efficiency_ratio_zscore_5d": {"inputs": ['close'], "func": dpe_031_efficiency_ratio_zscore_5d},
    "dpe_032_efficiency_ratio_zscore_21d": {"inputs": ['close'], "func": dpe_032_efficiency_ratio_zscore_21d},
    "dpe_033_efficiency_ratio_zscore_63d": {"inputs": ['close'], "func": dpe_033_efficiency_ratio_zscore_63d},
    "dpe_034_efficiency_ratio_zscore_126d": {"inputs": ['close'], "func": dpe_034_efficiency_ratio_zscore_126d},
    "dpe_035_efficiency_ratio_zscore_252d": {"inputs": ['close'], "func": dpe_035_efficiency_ratio_zscore_252d},
    "dpe_036_fractal_dim_zscore_5d": {"inputs": ['close'], "func": dpe_036_fractal_dim_zscore_5d},
    "dpe_037_fractal_dim_zscore_21d": {"inputs": ['close'], "func": dpe_037_fractal_dim_zscore_21d},
    "dpe_038_fractal_dim_zscore_63d": {"inputs": ['close'], "func": dpe_038_fractal_dim_zscore_63d},
    "dpe_039_fractal_dim_zscore_126d": {"inputs": ['close'], "func": dpe_039_fractal_dim_zscore_126d},
    "dpe_040_fractal_dim_zscore_252d": {"inputs": ['close'], "func": dpe_040_fractal_dim_zscore_252d},
    "dpe_041_dd_jaggedness_zscore_5d": {"inputs": ['close'], "func": dpe_041_dd_jaggedness_zscore_5d},
    "dpe_042_dd_jaggedness_zscore_21d": {"inputs": ['close'], "func": dpe_042_dd_jaggedness_zscore_21d},
    "dpe_043_dd_jaggedness_zscore_63d": {"inputs": ['close'], "func": dpe_043_dd_jaggedness_zscore_63d},
    "dpe_044_dd_jaggedness_zscore_126d": {"inputs": ['close'], "func": dpe_044_dd_jaggedness_zscore_126d},
    "dpe_045_dd_jaggedness_zscore_252d": {"inputs": ['close'], "func": dpe_045_dd_jaggedness_zscore_252d},
    "dpe_046_zigzag_index_zscore_5d": {"inputs": ['close'], "func": dpe_046_zigzag_index_zscore_5d},
    "dpe_047_zigzag_index_zscore_21d": {"inputs": ['close'], "func": dpe_047_zigzag_index_zscore_21d},
    "dpe_048_zigzag_index_zscore_63d": {"inputs": ['close'], "func": dpe_048_zigzag_index_zscore_63d},
    "dpe_049_zigzag_index_zscore_126d": {"inputs": ['close'], "func": dpe_049_zigzag_index_zscore_126d},
    "dpe_050_zigzag_index_zscore_252d": {"inputs": ['close'], "func": dpe_050_zigzag_index_zscore_252d},
    "dpe_051_ret_entropy_rank_5d": {"inputs": ['close'], "func": dpe_051_ret_entropy_rank_5d},
    "dpe_052_ret_entropy_rank_21d": {"inputs": ['close'], "func": dpe_052_ret_entropy_rank_21d},
    "dpe_053_ret_entropy_rank_63d": {"inputs": ['close'], "func": dpe_053_ret_entropy_rank_63d},
    "dpe_054_ret_entropy_rank_126d": {"inputs": ['close'], "func": dpe_054_ret_entropy_rank_126d},
    "dpe_055_ret_entropy_rank_252d": {"inputs": ['close'], "func": dpe_055_ret_entropy_rank_252d},
    "dpe_056_efficiency_ratio_rank_5d": {"inputs": ['close'], "func": dpe_056_efficiency_ratio_rank_5d},
    "dpe_057_efficiency_ratio_rank_21d": {"inputs": ['close'], "func": dpe_057_efficiency_ratio_rank_21d},
    "dpe_058_efficiency_ratio_rank_63d": {"inputs": ['close'], "func": dpe_058_efficiency_ratio_rank_63d},
    "dpe_059_efficiency_ratio_rank_126d": {"inputs": ['close'], "func": dpe_059_efficiency_ratio_rank_126d},
    "dpe_060_efficiency_ratio_rank_252d": {"inputs": ['close'], "func": dpe_060_efficiency_ratio_rank_252d},
    "dpe_061_fractal_dim_rank_5d": {"inputs": ['close'], "func": dpe_061_fractal_dim_rank_5d},
    "dpe_062_fractal_dim_rank_21d": {"inputs": ['close'], "func": dpe_062_fractal_dim_rank_21d},
    "dpe_063_fractal_dim_rank_63d": {"inputs": ['close'], "func": dpe_063_fractal_dim_rank_63d},
    "dpe_064_fractal_dim_rank_126d": {"inputs": ['close'], "func": dpe_064_fractal_dim_rank_126d},
    "dpe_065_fractal_dim_rank_252d": {"inputs": ['close'], "func": dpe_065_fractal_dim_rank_252d},
    "dpe_066_dd_jaggedness_rank_5d": {"inputs": ['close'], "func": dpe_066_dd_jaggedness_rank_5d},
    "dpe_067_dd_jaggedness_rank_21d": {"inputs": ['close'], "func": dpe_067_dd_jaggedness_rank_21d},
    "dpe_068_dd_jaggedness_rank_63d": {"inputs": ['close'], "func": dpe_068_dd_jaggedness_rank_63d},
    "dpe_069_dd_jaggedness_rank_126d": {"inputs": ['close'], "func": dpe_069_dd_jaggedness_rank_126d},
    "dpe_070_dd_jaggedness_rank_252d": {"inputs": ['close'], "func": dpe_070_dd_jaggedness_rank_252d},
    "dpe_071_zigzag_index_rank_5d": {"inputs": ['close'], "func": dpe_071_zigzag_index_rank_5d},
    "dpe_072_zigzag_index_rank_21d": {"inputs": ['close'], "func": dpe_072_zigzag_index_rank_21d},
    "dpe_073_zigzag_index_rank_63d": {"inputs": ['close'], "func": dpe_073_zigzag_index_rank_63d},
    "dpe_074_zigzag_index_rank_126d": {"inputs": ['close'], "func": dpe_074_zigzag_index_rank_126d},
    "dpe_075_zigzag_index_rank_252d": {"inputs": ['close'], "func": dpe_075_zigzag_index_rank_252d},
}
