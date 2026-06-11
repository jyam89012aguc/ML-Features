"""
90_copp_dynamics — Base Features 001-075
Domain: copp_dynamics
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

# ── Feature functions ────────────────────────────────────────────────────────

def copp_001_roc_14_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_001_roc_14_lvl_5d"""
    base = close.pct_change(14)
    return _rolling_mean(base, 5)

def copp_002_roc_14_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_002_roc_14_zscore_5d"""
    base = close.pct_change(14)
    return _zscore_rolling(base, 5)

def copp_003_roc_14_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_003_roc_14_rank_5d"""
    base = close.pct_change(14)
    return _rank_pct(base, 5)

def copp_004_roc_14_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_004_roc_14_lvl_21d"""
    base = close.pct_change(14)
    return _rolling_mean(base, 21)

def copp_005_roc_14_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_005_roc_14_zscore_21d"""
    base = close.pct_change(14)
    return _zscore_rolling(base, 21)

def copp_006_roc_14_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_006_roc_14_rank_21d"""
    base = close.pct_change(14)
    return _rank_pct(base, 21)

def copp_007_roc_14_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_007_roc_14_lvl_63d"""
    base = close.pct_change(14)
    return _rolling_mean(base, 63)

def copp_008_roc_14_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_008_roc_14_zscore_63d"""
    base = close.pct_change(14)
    return _zscore_rolling(base, 63)

def copp_009_roc_14_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_009_roc_14_rank_63d"""
    base = close.pct_change(14)
    return _rank_pct(base, 63)

def copp_010_roc_14_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_010_roc_14_lvl_126d"""
    base = close.pct_change(14)
    return _rolling_mean(base, 126)

def copp_011_roc_14_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_011_roc_14_zscore_126d"""
    base = close.pct_change(14)
    return _zscore_rolling(base, 126)

def copp_012_roc_14_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_012_roc_14_rank_126d"""
    base = close.pct_change(14)
    return _rank_pct(base, 126)

def copp_013_roc_14_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_013_roc_14_lvl_252d"""
    base = close.pct_change(14)
    return _rolling_mean(base, 252)

def copp_014_roc_14_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_014_roc_14_zscore_252d"""
    base = close.pct_change(14)
    return _zscore_rolling(base, 252)

def copp_015_roc_14_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_015_roc_14_rank_252d"""
    base = close.pct_change(14)
    return _rank_pct(base, 252)

def copp_016_roc_11_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_016_roc_11_lvl_5d"""
    base = close.pct_change(11)
    return _rolling_mean(base, 5)

def copp_017_roc_11_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_017_roc_11_zscore_5d"""
    base = close.pct_change(11)
    return _zscore_rolling(base, 5)

def copp_018_roc_11_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_018_roc_11_rank_5d"""
    base = close.pct_change(11)
    return _rank_pct(base, 5)

def copp_019_roc_11_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_019_roc_11_lvl_21d"""
    base = close.pct_change(11)
    return _rolling_mean(base, 21)

def copp_020_roc_11_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_020_roc_11_zscore_21d"""
    base = close.pct_change(11)
    return _zscore_rolling(base, 21)

def copp_021_roc_11_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_021_roc_11_rank_21d"""
    base = close.pct_change(11)
    return _rank_pct(base, 21)

def copp_022_roc_11_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_022_roc_11_lvl_63d"""
    base = close.pct_change(11)
    return _rolling_mean(base, 63)

def copp_023_roc_11_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_023_roc_11_zscore_63d"""
    base = close.pct_change(11)
    return _zscore_rolling(base, 63)

def copp_024_roc_11_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_024_roc_11_rank_63d"""
    base = close.pct_change(11)
    return _rank_pct(base, 63)

def copp_025_roc_11_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_025_roc_11_lvl_126d"""
    base = close.pct_change(11)
    return _rolling_mean(base, 126)

def copp_026_roc_11_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_026_roc_11_zscore_126d"""
    base = close.pct_change(11)
    return _zscore_rolling(base, 126)

def copp_027_roc_11_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_027_roc_11_rank_126d"""
    base = close.pct_change(11)
    return _rank_pct(base, 126)

def copp_028_roc_11_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_028_roc_11_lvl_252d"""
    base = close.pct_change(11)
    return _rolling_mean(base, 252)

def copp_029_roc_11_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_029_roc_11_zscore_252d"""
    base = close.pct_change(11)
    return _zscore_rolling(base, 252)

def copp_030_roc_11_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_030_roc_11_rank_252d"""
    base = close.pct_change(11)
    return _rank_pct(base, 252)

def copp_031_copp_sum_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_031_copp_sum_lvl_5d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rolling_mean(base, 5)

def copp_032_copp_sum_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_032_copp_sum_zscore_5d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _zscore_rolling(base, 5)

def copp_033_copp_sum_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_033_copp_sum_rank_5d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rank_pct(base, 5)

def copp_034_copp_sum_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_034_copp_sum_lvl_21d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rolling_mean(base, 21)

def copp_035_copp_sum_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_035_copp_sum_zscore_21d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _zscore_rolling(base, 21)

def copp_036_copp_sum_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_036_copp_sum_rank_21d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rank_pct(base, 21)

def copp_037_copp_sum_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_037_copp_sum_lvl_63d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rolling_mean(base, 63)

def copp_038_copp_sum_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_038_copp_sum_zscore_63d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _zscore_rolling(base, 63)

def copp_039_copp_sum_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_039_copp_sum_rank_63d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rank_pct(base, 63)

def copp_040_copp_sum_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_040_copp_sum_lvl_126d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rolling_mean(base, 126)

def copp_041_copp_sum_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_041_copp_sum_zscore_126d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _zscore_rolling(base, 126)

def copp_042_copp_sum_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_042_copp_sum_rank_126d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rank_pct(base, 126)

def copp_043_copp_sum_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_043_copp_sum_lvl_252d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rolling_mean(base, 252)

def copp_044_copp_sum_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_044_copp_sum_zscore_252d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _zscore_rolling(base, 252)

def copp_045_copp_sum_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_045_copp_sum_rank_252d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rank_pct(base, 252)

def copp_046_copp_wma_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_046_copp_wma_lvl_5d"""
    base = (close.pct_change(14) + close.pct_change(11)).rolling(10).mean()
    return _rolling_mean(base, 5)

def copp_047_copp_wma_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_047_copp_wma_zscore_5d"""
    base = (close.pct_change(14) + close.pct_change(11)).rolling(10).mean()
    return _zscore_rolling(base, 5)

def copp_048_copp_wma_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_048_copp_wma_rank_5d"""
    base = (close.pct_change(14) + close.pct_change(11)).rolling(10).mean()
    return _rank_pct(base, 5)

def copp_049_copp_wma_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_049_copp_wma_lvl_21d"""
    base = (close.pct_change(14) + close.pct_change(11)).rolling(10).mean()
    return _rolling_mean(base, 21)

def copp_050_copp_wma_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_050_copp_wma_zscore_21d"""
    base = (close.pct_change(14) + close.pct_change(11)).rolling(10).mean()
    return _zscore_rolling(base, 21)

def copp_051_copp_wma_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_051_copp_wma_rank_21d"""
    base = (close.pct_change(14) + close.pct_change(11)).rolling(10).mean()
    return _rank_pct(base, 21)

def copp_052_copp_wma_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_052_copp_wma_lvl_63d"""
    base = (close.pct_change(14) + close.pct_change(11)).rolling(10).mean()
    return _rolling_mean(base, 63)

def copp_053_copp_wma_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_053_copp_wma_zscore_63d"""
    base = (close.pct_change(14) + close.pct_change(11)).rolling(10).mean()
    return _zscore_rolling(base, 63)

def copp_054_copp_wma_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_054_copp_wma_rank_63d"""
    base = (close.pct_change(14) + close.pct_change(11)).rolling(10).mean()
    return _rank_pct(base, 63)

def copp_055_copp_wma_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_055_copp_wma_lvl_126d"""
    base = (close.pct_change(14) + close.pct_change(11)).rolling(10).mean()
    return _rolling_mean(base, 126)

def copp_056_copp_wma_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_056_copp_wma_zscore_126d"""
    base = (close.pct_change(14) + close.pct_change(11)).rolling(10).mean()
    return _zscore_rolling(base, 126)

def copp_057_copp_wma_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_057_copp_wma_rank_126d"""
    base = (close.pct_change(14) + close.pct_change(11)).rolling(10).mean()
    return _rank_pct(base, 126)

def copp_058_copp_wma_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_058_copp_wma_lvl_252d"""
    base = (close.pct_change(14) + close.pct_change(11)).rolling(10).mean()
    return _rolling_mean(base, 252)

def copp_059_copp_wma_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_059_copp_wma_zscore_252d"""
    base = (close.pct_change(14) + close.pct_change(11)).rolling(10).mean()
    return _zscore_rolling(base, 252)

def copp_060_copp_wma_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_060_copp_wma_rank_252d"""
    base = (close.pct_change(14) + close.pct_change(11)).rolling(10).mean()
    return _rank_pct(base, 252)

def copp_061_copp_lvl_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_061_copp_lvl_lvl_5d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rolling_mean(base, 5)

def copp_062_copp_lvl_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_062_copp_lvl_zscore_5d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _zscore_rolling(base, 5)

def copp_063_copp_lvl_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_063_copp_lvl_rank_5d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rank_pct(base, 5)

def copp_064_copp_lvl_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_064_copp_lvl_lvl_21d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rolling_mean(base, 21)

def copp_065_copp_lvl_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_065_copp_lvl_zscore_21d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _zscore_rolling(base, 21)

def copp_066_copp_lvl_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_066_copp_lvl_rank_21d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rank_pct(base, 21)

def copp_067_copp_lvl_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_067_copp_lvl_lvl_63d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rolling_mean(base, 63)

def copp_068_copp_lvl_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_068_copp_lvl_zscore_63d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _zscore_rolling(base, 63)

def copp_069_copp_lvl_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_069_copp_lvl_rank_63d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rank_pct(base, 63)

def copp_070_copp_lvl_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_070_copp_lvl_lvl_126d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rolling_mean(base, 126)

def copp_071_copp_lvl_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_071_copp_lvl_zscore_126d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _zscore_rolling(base, 126)

def copp_072_copp_lvl_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_072_copp_lvl_rank_126d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rank_pct(base, 126)

def copp_073_copp_lvl_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_073_copp_lvl_lvl_252d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rolling_mean(base, 252)

def copp_074_copp_lvl_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_074_copp_lvl_zscore_252d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _zscore_rolling(base, 252)

def copp_075_copp_lvl_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_075_copp_lvl_rank_252d"""
    base = close.pct_change(14) + close.pct_change(11)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V90_REGISTRY = {
    "copp_001_roc_14_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_001_roc_14_lvl_5d},
    "copp_002_roc_14_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_002_roc_14_zscore_5d},
    "copp_003_roc_14_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_003_roc_14_rank_5d},
    "copp_004_roc_14_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_004_roc_14_lvl_21d},
    "copp_005_roc_14_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_005_roc_14_zscore_21d},
    "copp_006_roc_14_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_006_roc_14_rank_21d},
    "copp_007_roc_14_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_007_roc_14_lvl_63d},
    "copp_008_roc_14_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_008_roc_14_zscore_63d},
    "copp_009_roc_14_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_009_roc_14_rank_63d},
    "copp_010_roc_14_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_010_roc_14_lvl_126d},
    "copp_011_roc_14_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_011_roc_14_zscore_126d},
    "copp_012_roc_14_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_012_roc_14_rank_126d},
    "copp_013_roc_14_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_013_roc_14_lvl_252d},
    "copp_014_roc_14_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_014_roc_14_zscore_252d},
    "copp_015_roc_14_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_015_roc_14_rank_252d},
    "copp_016_roc_11_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_016_roc_11_lvl_5d},
    "copp_017_roc_11_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_017_roc_11_zscore_5d},
    "copp_018_roc_11_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_018_roc_11_rank_5d},
    "copp_019_roc_11_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_019_roc_11_lvl_21d},
    "copp_020_roc_11_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_020_roc_11_zscore_21d},
    "copp_021_roc_11_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_021_roc_11_rank_21d},
    "copp_022_roc_11_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_022_roc_11_lvl_63d},
    "copp_023_roc_11_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_023_roc_11_zscore_63d},
    "copp_024_roc_11_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_024_roc_11_rank_63d},
    "copp_025_roc_11_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_025_roc_11_lvl_126d},
    "copp_026_roc_11_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_026_roc_11_zscore_126d},
    "copp_027_roc_11_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_027_roc_11_rank_126d},
    "copp_028_roc_11_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_028_roc_11_lvl_252d},
    "copp_029_roc_11_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_029_roc_11_zscore_252d},
    "copp_030_roc_11_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_030_roc_11_rank_252d},
    "copp_031_copp_sum_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_031_copp_sum_lvl_5d},
    "copp_032_copp_sum_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_032_copp_sum_zscore_5d},
    "copp_033_copp_sum_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_033_copp_sum_rank_5d},
    "copp_034_copp_sum_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_034_copp_sum_lvl_21d},
    "copp_035_copp_sum_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_035_copp_sum_zscore_21d},
    "copp_036_copp_sum_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_036_copp_sum_rank_21d},
    "copp_037_copp_sum_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_037_copp_sum_lvl_63d},
    "copp_038_copp_sum_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_038_copp_sum_zscore_63d},
    "copp_039_copp_sum_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_039_copp_sum_rank_63d},
    "copp_040_copp_sum_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_040_copp_sum_lvl_126d},
    "copp_041_copp_sum_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_041_copp_sum_zscore_126d},
    "copp_042_copp_sum_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_042_copp_sum_rank_126d},
    "copp_043_copp_sum_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_043_copp_sum_lvl_252d},
    "copp_044_copp_sum_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_044_copp_sum_zscore_252d},
    "copp_045_copp_sum_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_045_copp_sum_rank_252d},
    "copp_046_copp_wma_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_046_copp_wma_lvl_5d},
    "copp_047_copp_wma_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_047_copp_wma_zscore_5d},
    "copp_048_copp_wma_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_048_copp_wma_rank_5d},
    "copp_049_copp_wma_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_049_copp_wma_lvl_21d},
    "copp_050_copp_wma_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_050_copp_wma_zscore_21d},
    "copp_051_copp_wma_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_051_copp_wma_rank_21d},
    "copp_052_copp_wma_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_052_copp_wma_lvl_63d},
    "copp_053_copp_wma_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_053_copp_wma_zscore_63d},
    "copp_054_copp_wma_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_054_copp_wma_rank_63d},
    "copp_055_copp_wma_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_055_copp_wma_lvl_126d},
    "copp_056_copp_wma_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_056_copp_wma_zscore_126d},
    "copp_057_copp_wma_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_057_copp_wma_rank_126d},
    "copp_058_copp_wma_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_058_copp_wma_lvl_252d},
    "copp_059_copp_wma_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_059_copp_wma_zscore_252d},
    "copp_060_copp_wma_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_060_copp_wma_rank_252d},
    "copp_061_copp_lvl_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_061_copp_lvl_lvl_5d},
    "copp_062_copp_lvl_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_062_copp_lvl_zscore_5d},
    "copp_063_copp_lvl_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_063_copp_lvl_rank_5d},
    "copp_064_copp_lvl_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_064_copp_lvl_lvl_21d},
    "copp_065_copp_lvl_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_065_copp_lvl_zscore_21d},
    "copp_066_copp_lvl_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_066_copp_lvl_rank_21d},
    "copp_067_copp_lvl_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_067_copp_lvl_lvl_63d},
    "copp_068_copp_lvl_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_068_copp_lvl_zscore_63d},
    "copp_069_copp_lvl_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_069_copp_lvl_rank_63d},
    "copp_070_copp_lvl_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_070_copp_lvl_lvl_126d},
    "copp_071_copp_lvl_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_071_copp_lvl_zscore_126d},
    "copp_072_copp_lvl_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_072_copp_lvl_rank_126d},
    "copp_073_copp_lvl_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_073_copp_lvl_lvl_252d},
    "copp_074_copp_lvl_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_074_copp_lvl_zscore_252d},
    "copp_075_copp_lvl_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_075_copp_lvl_rank_252d},
}
