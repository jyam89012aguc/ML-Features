"""
92_rocd_dynamics — Base Features 001-075
Domain: rocd_dynamics
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

def rocd_001_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_001_roc_lvl_5d"""
    base = close.pct_change(21)
    return _rolling_mean(base, 5)

def rocd_002_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_002_roc_zscore_5d"""
    base = close.pct_change(21)
    return _zscore_rolling(base, 5)

def rocd_003_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_003_roc_rank_5d"""
    base = close.pct_change(21)
    return _rank_pct(base, 5)

def rocd_004_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_004_roc_lvl_21d"""
    base = close.pct_change(21)
    return _rolling_mean(base, 21)

def rocd_005_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_005_roc_zscore_21d"""
    base = close.pct_change(21)
    return _zscore_rolling(base, 21)

def rocd_006_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_006_roc_rank_21d"""
    base = close.pct_change(21)
    return _rank_pct(base, 21)

def rocd_007_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_007_roc_lvl_63d"""
    base = close.pct_change(21)
    return _rolling_mean(base, 63)

def rocd_008_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_008_roc_zscore_63d"""
    base = close.pct_change(21)
    return _zscore_rolling(base, 63)

def rocd_009_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_009_roc_rank_63d"""
    base = close.pct_change(21)
    return _rank_pct(base, 63)

def rocd_010_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_010_roc_lvl_126d"""
    base = close.pct_change(21)
    return _rolling_mean(base, 126)

def rocd_011_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_011_roc_zscore_126d"""
    base = close.pct_change(21)
    return _zscore_rolling(base, 126)

def rocd_012_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_012_roc_rank_126d"""
    base = close.pct_change(21)
    return _rank_pct(base, 126)

def rocd_013_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_013_roc_lvl_252d"""
    base = close.pct_change(21)
    return _rolling_mean(base, 252)

def rocd_014_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_014_roc_zscore_252d"""
    base = close.pct_change(21)
    return _zscore_rolling(base, 252)

def rocd_015_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_015_roc_rank_252d"""
    base = close.pct_change(21)
    return _rank_pct(base, 252)

def rocd_016_vroc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_016_vroc_lvl_5d"""
    base = volume.pct_change(21)
    return _rolling_mean(base, 5)

def rocd_017_vroc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_017_vroc_zscore_5d"""
    base = volume.pct_change(21)
    return _zscore_rolling(base, 5)

def rocd_018_vroc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_018_vroc_rank_5d"""
    base = volume.pct_change(21)
    return _rank_pct(base, 5)

def rocd_019_vroc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_019_vroc_lvl_21d"""
    base = volume.pct_change(21)
    return _rolling_mean(base, 21)

def rocd_020_vroc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_020_vroc_zscore_21d"""
    base = volume.pct_change(21)
    return _zscore_rolling(base, 21)

def rocd_021_vroc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_021_vroc_rank_21d"""
    base = volume.pct_change(21)
    return _rank_pct(base, 21)

def rocd_022_vroc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_022_vroc_lvl_63d"""
    base = volume.pct_change(21)
    return _rolling_mean(base, 63)

def rocd_023_vroc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_023_vroc_zscore_63d"""
    base = volume.pct_change(21)
    return _zscore_rolling(base, 63)

def rocd_024_vroc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_024_vroc_rank_63d"""
    base = volume.pct_change(21)
    return _rank_pct(base, 63)

def rocd_025_vroc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_025_vroc_lvl_126d"""
    base = volume.pct_change(21)
    return _rolling_mean(base, 126)

def rocd_026_vroc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_026_vroc_zscore_126d"""
    base = volume.pct_change(21)
    return _zscore_rolling(base, 126)

def rocd_027_vroc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_027_vroc_rank_126d"""
    base = volume.pct_change(21)
    return _rank_pct(base, 126)

def rocd_028_vroc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_028_vroc_lvl_252d"""
    base = volume.pct_change(21)
    return _rolling_mean(base, 252)

def rocd_029_vroc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_029_vroc_zscore_252d"""
    base = volume.pct_change(21)
    return _zscore_rolling(base, 252)

def rocd_030_vroc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_030_vroc_rank_252d"""
    base = volume.pct_change(21)
    return _rank_pct(base, 252)

def rocd_031_roc_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_031_roc_z_lvl_5d"""
    base = _zscore_rolling(close.pct_change(21), 63)
    return _rolling_mean(base, 5)

def rocd_032_roc_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_032_roc_z_zscore_5d"""
    base = _zscore_rolling(close.pct_change(21), 63)
    return _zscore_rolling(base, 5)

def rocd_033_roc_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_033_roc_z_rank_5d"""
    base = _zscore_rolling(close.pct_change(21), 63)
    return _rank_pct(base, 5)

def rocd_034_roc_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_034_roc_z_lvl_21d"""
    base = _zscore_rolling(close.pct_change(21), 63)
    return _rolling_mean(base, 21)

def rocd_035_roc_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_035_roc_z_zscore_21d"""
    base = _zscore_rolling(close.pct_change(21), 63)
    return _zscore_rolling(base, 21)

def rocd_036_roc_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_036_roc_z_rank_21d"""
    base = _zscore_rolling(close.pct_change(21), 63)
    return _rank_pct(base, 21)

def rocd_037_roc_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_037_roc_z_lvl_63d"""
    base = _zscore_rolling(close.pct_change(21), 63)
    return _rolling_mean(base, 63)

def rocd_038_roc_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_038_roc_z_zscore_63d"""
    base = _zscore_rolling(close.pct_change(21), 63)
    return _zscore_rolling(base, 63)

def rocd_039_roc_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_039_roc_z_rank_63d"""
    base = _zscore_rolling(close.pct_change(21), 63)
    return _rank_pct(base, 63)

def rocd_040_roc_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_040_roc_z_lvl_126d"""
    base = _zscore_rolling(close.pct_change(21), 63)
    return _rolling_mean(base, 126)

def rocd_041_roc_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_041_roc_z_zscore_126d"""
    base = _zscore_rolling(close.pct_change(21), 63)
    return _zscore_rolling(base, 126)

def rocd_042_roc_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_042_roc_z_rank_126d"""
    base = _zscore_rolling(close.pct_change(21), 63)
    return _rank_pct(base, 126)

def rocd_043_roc_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_043_roc_z_lvl_252d"""
    base = _zscore_rolling(close.pct_change(21), 63)
    return _rolling_mean(base, 252)

def rocd_044_roc_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_044_roc_z_zscore_252d"""
    base = _zscore_rolling(close.pct_change(21), 63)
    return _zscore_rolling(base, 252)

def rocd_045_roc_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_045_roc_z_rank_252d"""
    base = _zscore_rolling(close.pct_change(21), 63)
    return _rank_pct(base, 252)

def rocd_046_vroc_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_046_vroc_z_lvl_5d"""
    base = _zscore_rolling(volume.pct_change(21), 63)
    return _rolling_mean(base, 5)

def rocd_047_vroc_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_047_vroc_z_zscore_5d"""
    base = _zscore_rolling(volume.pct_change(21), 63)
    return _zscore_rolling(base, 5)

def rocd_048_vroc_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_048_vroc_z_rank_5d"""
    base = _zscore_rolling(volume.pct_change(21), 63)
    return _rank_pct(base, 5)

def rocd_049_vroc_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_049_vroc_z_lvl_21d"""
    base = _zscore_rolling(volume.pct_change(21), 63)
    return _rolling_mean(base, 21)

def rocd_050_vroc_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_050_vroc_z_zscore_21d"""
    base = _zscore_rolling(volume.pct_change(21), 63)
    return _zscore_rolling(base, 21)

def rocd_051_vroc_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_051_vroc_z_rank_21d"""
    base = _zscore_rolling(volume.pct_change(21), 63)
    return _rank_pct(base, 21)

def rocd_052_vroc_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_052_vroc_z_lvl_63d"""
    base = _zscore_rolling(volume.pct_change(21), 63)
    return _rolling_mean(base, 63)

def rocd_053_vroc_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_053_vroc_z_zscore_63d"""
    base = _zscore_rolling(volume.pct_change(21), 63)
    return _zscore_rolling(base, 63)

def rocd_054_vroc_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_054_vroc_z_rank_63d"""
    base = _zscore_rolling(volume.pct_change(21), 63)
    return _rank_pct(base, 63)

def rocd_055_vroc_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_055_vroc_z_lvl_126d"""
    base = _zscore_rolling(volume.pct_change(21), 63)
    return _rolling_mean(base, 126)

def rocd_056_vroc_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_056_vroc_z_zscore_126d"""
    base = _zscore_rolling(volume.pct_change(21), 63)
    return _zscore_rolling(base, 126)

def rocd_057_vroc_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_057_vroc_z_rank_126d"""
    base = _zscore_rolling(volume.pct_change(21), 63)
    return _rank_pct(base, 126)

def rocd_058_vroc_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_058_vroc_z_lvl_252d"""
    base = _zscore_rolling(volume.pct_change(21), 63)
    return _rolling_mean(base, 252)

def rocd_059_vroc_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_059_vroc_z_zscore_252d"""
    base = _zscore_rolling(volume.pct_change(21), 63)
    return _zscore_rolling(base, 252)

def rocd_060_vroc_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_060_vroc_z_rank_252d"""
    base = _zscore_rolling(volume.pct_change(21), 63)
    return _rank_pct(base, 252)

def rocd_061_roc_vol_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_061_roc_vol_lvl_5d"""
    base = _safe_div(close.pct_change(21), volume.pct_change(21).abs())
    return _rolling_mean(base, 5)

def rocd_062_roc_vol_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_062_roc_vol_zscore_5d"""
    base = _safe_div(close.pct_change(21), volume.pct_change(21).abs())
    return _zscore_rolling(base, 5)

def rocd_063_roc_vol_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_063_roc_vol_rank_5d"""
    base = _safe_div(close.pct_change(21), volume.pct_change(21).abs())
    return _rank_pct(base, 5)

def rocd_064_roc_vol_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_064_roc_vol_lvl_21d"""
    base = _safe_div(close.pct_change(21), volume.pct_change(21).abs())
    return _rolling_mean(base, 21)

def rocd_065_roc_vol_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_065_roc_vol_zscore_21d"""
    base = _safe_div(close.pct_change(21), volume.pct_change(21).abs())
    return _zscore_rolling(base, 21)

def rocd_066_roc_vol_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_066_roc_vol_rank_21d"""
    base = _safe_div(close.pct_change(21), volume.pct_change(21).abs())
    return _rank_pct(base, 21)

def rocd_067_roc_vol_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_067_roc_vol_lvl_63d"""
    base = _safe_div(close.pct_change(21), volume.pct_change(21).abs())
    return _rolling_mean(base, 63)

def rocd_068_roc_vol_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_068_roc_vol_zscore_63d"""
    base = _safe_div(close.pct_change(21), volume.pct_change(21).abs())
    return _zscore_rolling(base, 63)

def rocd_069_roc_vol_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_069_roc_vol_rank_63d"""
    base = _safe_div(close.pct_change(21), volume.pct_change(21).abs())
    return _rank_pct(base, 63)

def rocd_070_roc_vol_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_070_roc_vol_lvl_126d"""
    base = _safe_div(close.pct_change(21), volume.pct_change(21).abs())
    return _rolling_mean(base, 126)

def rocd_071_roc_vol_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_071_roc_vol_zscore_126d"""
    base = _safe_div(close.pct_change(21), volume.pct_change(21).abs())
    return _zscore_rolling(base, 126)

def rocd_072_roc_vol_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_072_roc_vol_rank_126d"""
    base = _safe_div(close.pct_change(21), volume.pct_change(21).abs())
    return _rank_pct(base, 126)

def rocd_073_roc_vol_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_073_roc_vol_lvl_252d"""
    base = _safe_div(close.pct_change(21), volume.pct_change(21).abs())
    return _rolling_mean(base, 252)

def rocd_074_roc_vol_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_074_roc_vol_zscore_252d"""
    base = _safe_div(close.pct_change(21), volume.pct_change(21).abs())
    return _zscore_rolling(base, 252)

def rocd_075_roc_vol_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_075_roc_vol_rank_252d"""
    base = _safe_div(close.pct_change(21), volume.pct_change(21).abs())
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V92_REGISTRY = {
    "rocd_001_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_001_roc_lvl_5d},
    "rocd_002_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_002_roc_zscore_5d},
    "rocd_003_roc_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_003_roc_rank_5d},
    "rocd_004_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_004_roc_lvl_21d},
    "rocd_005_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_005_roc_zscore_21d},
    "rocd_006_roc_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_006_roc_rank_21d},
    "rocd_007_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_007_roc_lvl_63d},
    "rocd_008_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_008_roc_zscore_63d},
    "rocd_009_roc_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_009_roc_rank_63d},
    "rocd_010_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_010_roc_lvl_126d},
    "rocd_011_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_011_roc_zscore_126d},
    "rocd_012_roc_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_012_roc_rank_126d},
    "rocd_013_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_013_roc_lvl_252d},
    "rocd_014_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_014_roc_zscore_252d},
    "rocd_015_roc_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_015_roc_rank_252d},
    "rocd_016_vroc_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_016_vroc_lvl_5d},
    "rocd_017_vroc_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_017_vroc_zscore_5d},
    "rocd_018_vroc_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_018_vroc_rank_5d},
    "rocd_019_vroc_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_019_vroc_lvl_21d},
    "rocd_020_vroc_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_020_vroc_zscore_21d},
    "rocd_021_vroc_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_021_vroc_rank_21d},
    "rocd_022_vroc_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_022_vroc_lvl_63d},
    "rocd_023_vroc_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_023_vroc_zscore_63d},
    "rocd_024_vroc_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_024_vroc_rank_63d},
    "rocd_025_vroc_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_025_vroc_lvl_126d},
    "rocd_026_vroc_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_026_vroc_zscore_126d},
    "rocd_027_vroc_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_027_vroc_rank_126d},
    "rocd_028_vroc_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_028_vroc_lvl_252d},
    "rocd_029_vroc_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_029_vroc_zscore_252d},
    "rocd_030_vroc_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_030_vroc_rank_252d},
    "rocd_031_roc_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_031_roc_z_lvl_5d},
    "rocd_032_roc_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_032_roc_z_zscore_5d},
    "rocd_033_roc_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_033_roc_z_rank_5d},
    "rocd_034_roc_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_034_roc_z_lvl_21d},
    "rocd_035_roc_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_035_roc_z_zscore_21d},
    "rocd_036_roc_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_036_roc_z_rank_21d},
    "rocd_037_roc_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_037_roc_z_lvl_63d},
    "rocd_038_roc_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_038_roc_z_zscore_63d},
    "rocd_039_roc_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_039_roc_z_rank_63d},
    "rocd_040_roc_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_040_roc_z_lvl_126d},
    "rocd_041_roc_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_041_roc_z_zscore_126d},
    "rocd_042_roc_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_042_roc_z_rank_126d},
    "rocd_043_roc_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_043_roc_z_lvl_252d},
    "rocd_044_roc_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_044_roc_z_zscore_252d},
    "rocd_045_roc_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_045_roc_z_rank_252d},
    "rocd_046_vroc_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_046_vroc_z_lvl_5d},
    "rocd_047_vroc_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_047_vroc_z_zscore_5d},
    "rocd_048_vroc_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_048_vroc_z_rank_5d},
    "rocd_049_vroc_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_049_vroc_z_lvl_21d},
    "rocd_050_vroc_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_050_vroc_z_zscore_21d},
    "rocd_051_vroc_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_051_vroc_z_rank_21d},
    "rocd_052_vroc_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_052_vroc_z_lvl_63d},
    "rocd_053_vroc_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_053_vroc_z_zscore_63d},
    "rocd_054_vroc_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_054_vroc_z_rank_63d},
    "rocd_055_vroc_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_055_vroc_z_lvl_126d},
    "rocd_056_vroc_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_056_vroc_z_zscore_126d},
    "rocd_057_vroc_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_057_vroc_z_rank_126d},
    "rocd_058_vroc_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_058_vroc_z_lvl_252d},
    "rocd_059_vroc_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_059_vroc_z_zscore_252d},
    "rocd_060_vroc_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_060_vroc_z_rank_252d},
    "rocd_061_roc_vol_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_061_roc_vol_lvl_5d},
    "rocd_062_roc_vol_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_062_roc_vol_zscore_5d},
    "rocd_063_roc_vol_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_063_roc_vol_rank_5d},
    "rocd_064_roc_vol_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_064_roc_vol_lvl_21d},
    "rocd_065_roc_vol_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_065_roc_vol_zscore_21d},
    "rocd_066_roc_vol_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_066_roc_vol_rank_21d},
    "rocd_067_roc_vol_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_067_roc_vol_lvl_63d},
    "rocd_068_roc_vol_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_068_roc_vol_zscore_63d},
    "rocd_069_roc_vol_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_069_roc_vol_rank_63d},
    "rocd_070_roc_vol_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_070_roc_vol_lvl_126d},
    "rocd_071_roc_vol_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_071_roc_vol_zscore_126d},
    "rocd_072_roc_vol_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_072_roc_vol_rank_126d},
    "rocd_073_roc_vol_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_073_roc_vol_lvl_252d},
    "rocd_074_roc_vol_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_074_roc_vol_zscore_252d},
    "rocd_075_roc_vol_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_075_roc_vol_rank_252d},
}
