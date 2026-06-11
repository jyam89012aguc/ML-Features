"""
60_cash_flow_jerk — Base Features 001-075
Domain: cash_flow_jerk
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

def cfjk_001_cf_accel_lvl_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_001_cf_accel_lvl_5d"""
    base = ocf.pct_change(252).diff(63)
    return _rolling_mean(base, 5)

def cfjk_002_cf_accel_zscore_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_002_cf_accel_zscore_5d"""
    base = ocf.pct_change(252).diff(63)
    return _zscore_rolling(base, 5)

def cfjk_003_cf_accel_rank_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_003_cf_accel_rank_5d"""
    base = ocf.pct_change(252).diff(63)
    return _rank_pct(base, 5)

def cfjk_004_cf_accel_lvl_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_004_cf_accel_lvl_21d"""
    base = ocf.pct_change(252).diff(63)
    return _rolling_mean(base, 21)

def cfjk_005_cf_accel_zscore_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_005_cf_accel_zscore_21d"""
    base = ocf.pct_change(252).diff(63)
    return _zscore_rolling(base, 21)

def cfjk_006_cf_accel_rank_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_006_cf_accel_rank_21d"""
    base = ocf.pct_change(252).diff(63)
    return _rank_pct(base, 21)

def cfjk_007_cf_accel_lvl_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_007_cf_accel_lvl_63d"""
    base = ocf.pct_change(252).diff(63)
    return _rolling_mean(base, 63)

def cfjk_008_cf_accel_zscore_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_008_cf_accel_zscore_63d"""
    base = ocf.pct_change(252).diff(63)
    return _zscore_rolling(base, 63)

def cfjk_009_cf_accel_rank_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_009_cf_accel_rank_63d"""
    base = ocf.pct_change(252).diff(63)
    return _rank_pct(base, 63)

def cfjk_010_cf_accel_lvl_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_010_cf_accel_lvl_126d"""
    base = ocf.pct_change(252).diff(63)
    return _rolling_mean(base, 126)

def cfjk_011_cf_accel_zscore_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_011_cf_accel_zscore_126d"""
    base = ocf.pct_change(252).diff(63)
    return _zscore_rolling(base, 126)

def cfjk_012_cf_accel_rank_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_012_cf_accel_rank_126d"""
    base = ocf.pct_change(252).diff(63)
    return _rank_pct(base, 126)

def cfjk_013_cf_accel_lvl_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_013_cf_accel_lvl_252d"""
    base = ocf.pct_change(252).diff(63)
    return _rolling_mean(base, 252)

def cfjk_014_cf_accel_zscore_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_014_cf_accel_zscore_252d"""
    base = ocf.pct_change(252).diff(63)
    return _zscore_rolling(base, 252)

def cfjk_015_cf_accel_rank_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_015_cf_accel_rank_252d"""
    base = ocf.pct_change(252).diff(63)
    return _rank_pct(base, 252)

def cfjk_016_cf_jerk_lvl_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_016_cf_jerk_lvl_5d"""
    base = ocf.pct_change(252).diff(63).diff(21)
    return _rolling_mean(base, 5)

def cfjk_017_cf_jerk_zscore_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_017_cf_jerk_zscore_5d"""
    base = ocf.pct_change(252).diff(63).diff(21)
    return _zscore_rolling(base, 5)

def cfjk_018_cf_jerk_rank_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_018_cf_jerk_rank_5d"""
    base = ocf.pct_change(252).diff(63).diff(21)
    return _rank_pct(base, 5)

def cfjk_019_cf_jerk_lvl_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_019_cf_jerk_lvl_21d"""
    base = ocf.pct_change(252).diff(63).diff(21)
    return _rolling_mean(base, 21)

def cfjk_020_cf_jerk_zscore_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_020_cf_jerk_zscore_21d"""
    base = ocf.pct_change(252).diff(63).diff(21)
    return _zscore_rolling(base, 21)

def cfjk_021_cf_jerk_rank_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_021_cf_jerk_rank_21d"""
    base = ocf.pct_change(252).diff(63).diff(21)
    return _rank_pct(base, 21)

def cfjk_022_cf_jerk_lvl_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_022_cf_jerk_lvl_63d"""
    base = ocf.pct_change(252).diff(63).diff(21)
    return _rolling_mean(base, 63)

def cfjk_023_cf_jerk_zscore_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_023_cf_jerk_zscore_63d"""
    base = ocf.pct_change(252).diff(63).diff(21)
    return _zscore_rolling(base, 63)

def cfjk_024_cf_jerk_rank_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_024_cf_jerk_rank_63d"""
    base = ocf.pct_change(252).diff(63).diff(21)
    return _rank_pct(base, 63)

def cfjk_025_cf_jerk_lvl_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_025_cf_jerk_lvl_126d"""
    base = ocf.pct_change(252).diff(63).diff(21)
    return _rolling_mean(base, 126)

def cfjk_026_cf_jerk_zscore_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_026_cf_jerk_zscore_126d"""
    base = ocf.pct_change(252).diff(63).diff(21)
    return _zscore_rolling(base, 126)

def cfjk_027_cf_jerk_rank_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_027_cf_jerk_rank_126d"""
    base = ocf.pct_change(252).diff(63).diff(21)
    return _rank_pct(base, 126)

def cfjk_028_cf_jerk_lvl_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_028_cf_jerk_lvl_252d"""
    base = ocf.pct_change(252).diff(63).diff(21)
    return _rolling_mean(base, 252)

def cfjk_029_cf_jerk_zscore_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_029_cf_jerk_zscore_252d"""
    base = ocf.pct_change(252).diff(63).diff(21)
    return _zscore_rolling(base, 252)

def cfjk_030_cf_jerk_rank_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_030_cf_jerk_rank_252d"""
    base = ocf.pct_change(252).diff(63).diff(21)
    return _rank_pct(base, 252)

def cfjk_031_cf_accel_z_lvl_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_031_cf_accel_z_lvl_5d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 5)

def cfjk_032_cf_accel_z_zscore_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_032_cf_accel_z_zscore_5d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 5)

def cfjk_033_cf_accel_z_rank_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_033_cf_accel_z_rank_5d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63), 252)
    return _rank_pct(base, 5)

def cfjk_034_cf_accel_z_lvl_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_034_cf_accel_z_lvl_21d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 21)

def cfjk_035_cf_accel_z_zscore_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_035_cf_accel_z_zscore_21d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 21)

def cfjk_036_cf_accel_z_rank_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_036_cf_accel_z_rank_21d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63), 252)
    return _rank_pct(base, 21)

def cfjk_037_cf_accel_z_lvl_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_037_cf_accel_z_lvl_63d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 63)

def cfjk_038_cf_accel_z_zscore_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_038_cf_accel_z_zscore_63d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 63)

def cfjk_039_cf_accel_z_rank_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_039_cf_accel_z_rank_63d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63), 252)
    return _rank_pct(base, 63)

def cfjk_040_cf_accel_z_lvl_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_040_cf_accel_z_lvl_126d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 126)

def cfjk_041_cf_accel_z_zscore_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_041_cf_accel_z_zscore_126d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 126)

def cfjk_042_cf_accel_z_rank_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_042_cf_accel_z_rank_126d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63), 252)
    return _rank_pct(base, 126)

def cfjk_043_cf_accel_z_lvl_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_043_cf_accel_z_lvl_252d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 252)

def cfjk_044_cf_accel_z_zscore_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_044_cf_accel_z_zscore_252d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 252)

def cfjk_045_cf_accel_z_rank_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_045_cf_accel_z_rank_252d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63), 252)
    return _rank_pct(base, 252)

def cfjk_046_cf_jerk_z_lvl_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_046_cf_jerk_z_lvl_5d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 5)

def cfjk_047_cf_jerk_z_zscore_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_047_cf_jerk_z_zscore_5d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 5)

def cfjk_048_cf_jerk_z_rank_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_048_cf_jerk_z_rank_5d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 5)

def cfjk_049_cf_jerk_z_lvl_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_049_cf_jerk_z_lvl_21d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 21)

def cfjk_050_cf_jerk_z_zscore_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_050_cf_jerk_z_zscore_21d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 21)

def cfjk_051_cf_jerk_z_rank_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_051_cf_jerk_z_rank_21d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 21)

def cfjk_052_cf_jerk_z_lvl_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_052_cf_jerk_z_lvl_63d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 63)

def cfjk_053_cf_jerk_z_zscore_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_053_cf_jerk_z_zscore_63d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 63)

def cfjk_054_cf_jerk_z_rank_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_054_cf_jerk_z_rank_63d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 63)

def cfjk_055_cf_jerk_z_lvl_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_055_cf_jerk_z_lvl_126d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 126)

def cfjk_056_cf_jerk_z_zscore_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_056_cf_jerk_z_zscore_126d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 126)

def cfjk_057_cf_jerk_z_rank_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_057_cf_jerk_z_rank_126d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 126)

def cfjk_058_cf_jerk_z_lvl_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_058_cf_jerk_z_lvl_252d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 252)

def cfjk_059_cf_jerk_z_zscore_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_059_cf_jerk_z_zscore_252d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 252)

def cfjk_060_cf_jerk_z_rank_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_060_cf_jerk_z_rank_252d"""
    base = _zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 252)

def cfjk_061_cf_accel_rank_lvl_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_061_cf_accel_rank_lvl_5d"""
    base = _rank_pct(ocf.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 5)

def cfjk_062_cf_accel_rank_zscore_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_062_cf_accel_rank_zscore_5d"""
    base = _rank_pct(ocf.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 5)

def cfjk_063_cf_accel_rank_rank_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_063_cf_accel_rank_rank_5d"""
    base = _rank_pct(ocf.pct_change(252).diff(63), 252)
    return _rank_pct(base, 5)

def cfjk_064_cf_accel_rank_lvl_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_064_cf_accel_rank_lvl_21d"""
    base = _rank_pct(ocf.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 21)

def cfjk_065_cf_accel_rank_zscore_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_065_cf_accel_rank_zscore_21d"""
    base = _rank_pct(ocf.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 21)

def cfjk_066_cf_accel_rank_rank_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_066_cf_accel_rank_rank_21d"""
    base = _rank_pct(ocf.pct_change(252).diff(63), 252)
    return _rank_pct(base, 21)

def cfjk_067_cf_accel_rank_lvl_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_067_cf_accel_rank_lvl_63d"""
    base = _rank_pct(ocf.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 63)

def cfjk_068_cf_accel_rank_zscore_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_068_cf_accel_rank_zscore_63d"""
    base = _rank_pct(ocf.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 63)

def cfjk_069_cf_accel_rank_rank_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_069_cf_accel_rank_rank_63d"""
    base = _rank_pct(ocf.pct_change(252).diff(63), 252)
    return _rank_pct(base, 63)

def cfjk_070_cf_accel_rank_lvl_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_070_cf_accel_rank_lvl_126d"""
    base = _rank_pct(ocf.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 126)

def cfjk_071_cf_accel_rank_zscore_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_071_cf_accel_rank_zscore_126d"""
    base = _rank_pct(ocf.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 126)

def cfjk_072_cf_accel_rank_rank_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_072_cf_accel_rank_rank_126d"""
    base = _rank_pct(ocf.pct_change(252).diff(63), 252)
    return _rank_pct(base, 126)

def cfjk_073_cf_accel_rank_lvl_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_073_cf_accel_rank_lvl_252d"""
    base = _rank_pct(ocf.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 252)

def cfjk_074_cf_accel_rank_zscore_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_074_cf_accel_rank_zscore_252d"""
    base = _rank_pct(ocf.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 252)

def cfjk_075_cf_accel_rank_rank_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_075_cf_accel_rank_rank_252d"""
    base = _rank_pct(ocf.pct_change(252).diff(63), 252)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V60_REGISTRY = {
    "cfjk_001_cf_accel_lvl_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_001_cf_accel_lvl_5d},
    "cfjk_002_cf_accel_zscore_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_002_cf_accel_zscore_5d},
    "cfjk_003_cf_accel_rank_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_003_cf_accel_rank_5d},
    "cfjk_004_cf_accel_lvl_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_004_cf_accel_lvl_21d},
    "cfjk_005_cf_accel_zscore_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_005_cf_accel_zscore_21d},
    "cfjk_006_cf_accel_rank_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_006_cf_accel_rank_21d},
    "cfjk_007_cf_accel_lvl_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_007_cf_accel_lvl_63d},
    "cfjk_008_cf_accel_zscore_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_008_cf_accel_zscore_63d},
    "cfjk_009_cf_accel_rank_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_009_cf_accel_rank_63d},
    "cfjk_010_cf_accel_lvl_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_010_cf_accel_lvl_126d},
    "cfjk_011_cf_accel_zscore_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_011_cf_accel_zscore_126d},
    "cfjk_012_cf_accel_rank_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_012_cf_accel_rank_126d},
    "cfjk_013_cf_accel_lvl_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_013_cf_accel_lvl_252d},
    "cfjk_014_cf_accel_zscore_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_014_cf_accel_zscore_252d},
    "cfjk_015_cf_accel_rank_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_015_cf_accel_rank_252d},
    "cfjk_016_cf_jerk_lvl_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_016_cf_jerk_lvl_5d},
    "cfjk_017_cf_jerk_zscore_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_017_cf_jerk_zscore_5d},
    "cfjk_018_cf_jerk_rank_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_018_cf_jerk_rank_5d},
    "cfjk_019_cf_jerk_lvl_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_019_cf_jerk_lvl_21d},
    "cfjk_020_cf_jerk_zscore_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_020_cf_jerk_zscore_21d},
    "cfjk_021_cf_jerk_rank_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_021_cf_jerk_rank_21d},
    "cfjk_022_cf_jerk_lvl_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_022_cf_jerk_lvl_63d},
    "cfjk_023_cf_jerk_zscore_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_023_cf_jerk_zscore_63d},
    "cfjk_024_cf_jerk_rank_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_024_cf_jerk_rank_63d},
    "cfjk_025_cf_jerk_lvl_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_025_cf_jerk_lvl_126d},
    "cfjk_026_cf_jerk_zscore_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_026_cf_jerk_zscore_126d},
    "cfjk_027_cf_jerk_rank_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_027_cf_jerk_rank_126d},
    "cfjk_028_cf_jerk_lvl_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_028_cf_jerk_lvl_252d},
    "cfjk_029_cf_jerk_zscore_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_029_cf_jerk_zscore_252d},
    "cfjk_030_cf_jerk_rank_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_030_cf_jerk_rank_252d},
    "cfjk_031_cf_accel_z_lvl_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_031_cf_accel_z_lvl_5d},
    "cfjk_032_cf_accel_z_zscore_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_032_cf_accel_z_zscore_5d},
    "cfjk_033_cf_accel_z_rank_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_033_cf_accel_z_rank_5d},
    "cfjk_034_cf_accel_z_lvl_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_034_cf_accel_z_lvl_21d},
    "cfjk_035_cf_accel_z_zscore_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_035_cf_accel_z_zscore_21d},
    "cfjk_036_cf_accel_z_rank_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_036_cf_accel_z_rank_21d},
    "cfjk_037_cf_accel_z_lvl_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_037_cf_accel_z_lvl_63d},
    "cfjk_038_cf_accel_z_zscore_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_038_cf_accel_z_zscore_63d},
    "cfjk_039_cf_accel_z_rank_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_039_cf_accel_z_rank_63d},
    "cfjk_040_cf_accel_z_lvl_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_040_cf_accel_z_lvl_126d},
    "cfjk_041_cf_accel_z_zscore_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_041_cf_accel_z_zscore_126d},
    "cfjk_042_cf_accel_z_rank_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_042_cf_accel_z_rank_126d},
    "cfjk_043_cf_accel_z_lvl_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_043_cf_accel_z_lvl_252d},
    "cfjk_044_cf_accel_z_zscore_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_044_cf_accel_z_zscore_252d},
    "cfjk_045_cf_accel_z_rank_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_045_cf_accel_z_rank_252d},
    "cfjk_046_cf_jerk_z_lvl_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_046_cf_jerk_z_lvl_5d},
    "cfjk_047_cf_jerk_z_zscore_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_047_cf_jerk_z_zscore_5d},
    "cfjk_048_cf_jerk_z_rank_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_048_cf_jerk_z_rank_5d},
    "cfjk_049_cf_jerk_z_lvl_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_049_cf_jerk_z_lvl_21d},
    "cfjk_050_cf_jerk_z_zscore_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_050_cf_jerk_z_zscore_21d},
    "cfjk_051_cf_jerk_z_rank_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_051_cf_jerk_z_rank_21d},
    "cfjk_052_cf_jerk_z_lvl_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_052_cf_jerk_z_lvl_63d},
    "cfjk_053_cf_jerk_z_zscore_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_053_cf_jerk_z_zscore_63d},
    "cfjk_054_cf_jerk_z_rank_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_054_cf_jerk_z_rank_63d},
    "cfjk_055_cf_jerk_z_lvl_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_055_cf_jerk_z_lvl_126d},
    "cfjk_056_cf_jerk_z_zscore_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_056_cf_jerk_z_zscore_126d},
    "cfjk_057_cf_jerk_z_rank_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_057_cf_jerk_z_rank_126d},
    "cfjk_058_cf_jerk_z_lvl_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_058_cf_jerk_z_lvl_252d},
    "cfjk_059_cf_jerk_z_zscore_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_059_cf_jerk_z_zscore_252d},
    "cfjk_060_cf_jerk_z_rank_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_060_cf_jerk_z_rank_252d},
    "cfjk_061_cf_accel_rank_lvl_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_061_cf_accel_rank_lvl_5d},
    "cfjk_062_cf_accel_rank_zscore_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_062_cf_accel_rank_zscore_5d},
    "cfjk_063_cf_accel_rank_rank_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_063_cf_accel_rank_rank_5d},
    "cfjk_064_cf_accel_rank_lvl_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_064_cf_accel_rank_lvl_21d},
    "cfjk_065_cf_accel_rank_zscore_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_065_cf_accel_rank_zscore_21d},
    "cfjk_066_cf_accel_rank_rank_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_066_cf_accel_rank_rank_21d},
    "cfjk_067_cf_accel_rank_lvl_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_067_cf_accel_rank_lvl_63d},
    "cfjk_068_cf_accel_rank_zscore_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_068_cf_accel_rank_zscore_63d},
    "cfjk_069_cf_accel_rank_rank_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_069_cf_accel_rank_rank_63d},
    "cfjk_070_cf_accel_rank_lvl_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_070_cf_accel_rank_lvl_126d},
    "cfjk_071_cf_accel_rank_zscore_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_071_cf_accel_rank_zscore_126d},
    "cfjk_072_cf_accel_rank_rank_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_072_cf_accel_rank_rank_126d},
    "cfjk_073_cf_accel_rank_lvl_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_073_cf_accel_rank_lvl_252d},
    "cfjk_074_cf_accel_rank_zscore_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_074_cf_accel_rank_zscore_252d},
    "cfjk_075_cf_accel_rank_rank_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_075_cf_accel_rank_rank_252d},
}
