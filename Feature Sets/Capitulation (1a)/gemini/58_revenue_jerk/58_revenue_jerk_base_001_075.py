"""
58_revenue_jerk — Base Features 001-075
Domain: revenue_jerk
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

def revj_001_rev_accel_lvl_5d(revenue: pd.Series) -> pd.Series:
    """revj_001_rev_accel_lvl_5d"""
    base = revenue.pct_change(252).diff(63)
    return _rolling_mean(base, 5)

def revj_002_rev_accel_zscore_5d(revenue: pd.Series) -> pd.Series:
    """revj_002_rev_accel_zscore_5d"""
    base = revenue.pct_change(252).diff(63)
    return _zscore_rolling(base, 5)

def revj_003_rev_accel_rank_5d(revenue: pd.Series) -> pd.Series:
    """revj_003_rev_accel_rank_5d"""
    base = revenue.pct_change(252).diff(63)
    return _rank_pct(base, 5)

def revj_004_rev_accel_lvl_21d(revenue: pd.Series) -> pd.Series:
    """revj_004_rev_accel_lvl_21d"""
    base = revenue.pct_change(252).diff(63)
    return _rolling_mean(base, 21)

def revj_005_rev_accel_zscore_21d(revenue: pd.Series) -> pd.Series:
    """revj_005_rev_accel_zscore_21d"""
    base = revenue.pct_change(252).diff(63)
    return _zscore_rolling(base, 21)

def revj_006_rev_accel_rank_21d(revenue: pd.Series) -> pd.Series:
    """revj_006_rev_accel_rank_21d"""
    base = revenue.pct_change(252).diff(63)
    return _rank_pct(base, 21)

def revj_007_rev_accel_lvl_63d(revenue: pd.Series) -> pd.Series:
    """revj_007_rev_accel_lvl_63d"""
    base = revenue.pct_change(252).diff(63)
    return _rolling_mean(base, 63)

def revj_008_rev_accel_zscore_63d(revenue: pd.Series) -> pd.Series:
    """revj_008_rev_accel_zscore_63d"""
    base = revenue.pct_change(252).diff(63)
    return _zscore_rolling(base, 63)

def revj_009_rev_accel_rank_63d(revenue: pd.Series) -> pd.Series:
    """revj_009_rev_accel_rank_63d"""
    base = revenue.pct_change(252).diff(63)
    return _rank_pct(base, 63)

def revj_010_rev_accel_lvl_126d(revenue: pd.Series) -> pd.Series:
    """revj_010_rev_accel_lvl_126d"""
    base = revenue.pct_change(252).diff(63)
    return _rolling_mean(base, 126)

def revj_011_rev_accel_zscore_126d(revenue: pd.Series) -> pd.Series:
    """revj_011_rev_accel_zscore_126d"""
    base = revenue.pct_change(252).diff(63)
    return _zscore_rolling(base, 126)

def revj_012_rev_accel_rank_126d(revenue: pd.Series) -> pd.Series:
    """revj_012_rev_accel_rank_126d"""
    base = revenue.pct_change(252).diff(63)
    return _rank_pct(base, 126)

def revj_013_rev_accel_lvl_252d(revenue: pd.Series) -> pd.Series:
    """revj_013_rev_accel_lvl_252d"""
    base = revenue.pct_change(252).diff(63)
    return _rolling_mean(base, 252)

def revj_014_rev_accel_zscore_252d(revenue: pd.Series) -> pd.Series:
    """revj_014_rev_accel_zscore_252d"""
    base = revenue.pct_change(252).diff(63)
    return _zscore_rolling(base, 252)

def revj_015_rev_accel_rank_252d(revenue: pd.Series) -> pd.Series:
    """revj_015_rev_accel_rank_252d"""
    base = revenue.pct_change(252).diff(63)
    return _rank_pct(base, 252)

def revj_016_rev_jerk_lvl_5d(revenue: pd.Series) -> pd.Series:
    """revj_016_rev_jerk_lvl_5d"""
    base = revenue.pct_change(252).diff(63).diff(21)
    return _rolling_mean(base, 5)

def revj_017_rev_jerk_zscore_5d(revenue: pd.Series) -> pd.Series:
    """revj_017_rev_jerk_zscore_5d"""
    base = revenue.pct_change(252).diff(63).diff(21)
    return _zscore_rolling(base, 5)

def revj_018_rev_jerk_rank_5d(revenue: pd.Series) -> pd.Series:
    """revj_018_rev_jerk_rank_5d"""
    base = revenue.pct_change(252).diff(63).diff(21)
    return _rank_pct(base, 5)

def revj_019_rev_jerk_lvl_21d(revenue: pd.Series) -> pd.Series:
    """revj_019_rev_jerk_lvl_21d"""
    base = revenue.pct_change(252).diff(63).diff(21)
    return _rolling_mean(base, 21)

def revj_020_rev_jerk_zscore_21d(revenue: pd.Series) -> pd.Series:
    """revj_020_rev_jerk_zscore_21d"""
    base = revenue.pct_change(252).diff(63).diff(21)
    return _zscore_rolling(base, 21)

def revj_021_rev_jerk_rank_21d(revenue: pd.Series) -> pd.Series:
    """revj_021_rev_jerk_rank_21d"""
    base = revenue.pct_change(252).diff(63).diff(21)
    return _rank_pct(base, 21)

def revj_022_rev_jerk_lvl_63d(revenue: pd.Series) -> pd.Series:
    """revj_022_rev_jerk_lvl_63d"""
    base = revenue.pct_change(252).diff(63).diff(21)
    return _rolling_mean(base, 63)

def revj_023_rev_jerk_zscore_63d(revenue: pd.Series) -> pd.Series:
    """revj_023_rev_jerk_zscore_63d"""
    base = revenue.pct_change(252).diff(63).diff(21)
    return _zscore_rolling(base, 63)

def revj_024_rev_jerk_rank_63d(revenue: pd.Series) -> pd.Series:
    """revj_024_rev_jerk_rank_63d"""
    base = revenue.pct_change(252).diff(63).diff(21)
    return _rank_pct(base, 63)

def revj_025_rev_jerk_lvl_126d(revenue: pd.Series) -> pd.Series:
    """revj_025_rev_jerk_lvl_126d"""
    base = revenue.pct_change(252).diff(63).diff(21)
    return _rolling_mean(base, 126)

def revj_026_rev_jerk_zscore_126d(revenue: pd.Series) -> pd.Series:
    """revj_026_rev_jerk_zscore_126d"""
    base = revenue.pct_change(252).diff(63).diff(21)
    return _zscore_rolling(base, 126)

def revj_027_rev_jerk_rank_126d(revenue: pd.Series) -> pd.Series:
    """revj_027_rev_jerk_rank_126d"""
    base = revenue.pct_change(252).diff(63).diff(21)
    return _rank_pct(base, 126)

def revj_028_rev_jerk_lvl_252d(revenue: pd.Series) -> pd.Series:
    """revj_028_rev_jerk_lvl_252d"""
    base = revenue.pct_change(252).diff(63).diff(21)
    return _rolling_mean(base, 252)

def revj_029_rev_jerk_zscore_252d(revenue: pd.Series) -> pd.Series:
    """revj_029_rev_jerk_zscore_252d"""
    base = revenue.pct_change(252).diff(63).diff(21)
    return _zscore_rolling(base, 252)

def revj_030_rev_jerk_rank_252d(revenue: pd.Series) -> pd.Series:
    """revj_030_rev_jerk_rank_252d"""
    base = revenue.pct_change(252).diff(63).diff(21)
    return _rank_pct(base, 252)

def revj_031_rev_accel_z_lvl_5d(revenue: pd.Series) -> pd.Series:
    """revj_031_rev_accel_z_lvl_5d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 5)

def revj_032_rev_accel_z_zscore_5d(revenue: pd.Series) -> pd.Series:
    """revj_032_rev_accel_z_zscore_5d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 5)

def revj_033_rev_accel_z_rank_5d(revenue: pd.Series) -> pd.Series:
    """revj_033_rev_accel_z_rank_5d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63), 252)
    return _rank_pct(base, 5)

def revj_034_rev_accel_z_lvl_21d(revenue: pd.Series) -> pd.Series:
    """revj_034_rev_accel_z_lvl_21d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 21)

def revj_035_rev_accel_z_zscore_21d(revenue: pd.Series) -> pd.Series:
    """revj_035_rev_accel_z_zscore_21d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 21)

def revj_036_rev_accel_z_rank_21d(revenue: pd.Series) -> pd.Series:
    """revj_036_rev_accel_z_rank_21d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63), 252)
    return _rank_pct(base, 21)

def revj_037_rev_accel_z_lvl_63d(revenue: pd.Series) -> pd.Series:
    """revj_037_rev_accel_z_lvl_63d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 63)

def revj_038_rev_accel_z_zscore_63d(revenue: pd.Series) -> pd.Series:
    """revj_038_rev_accel_z_zscore_63d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 63)

def revj_039_rev_accel_z_rank_63d(revenue: pd.Series) -> pd.Series:
    """revj_039_rev_accel_z_rank_63d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63), 252)
    return _rank_pct(base, 63)

def revj_040_rev_accel_z_lvl_126d(revenue: pd.Series) -> pd.Series:
    """revj_040_rev_accel_z_lvl_126d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 126)

def revj_041_rev_accel_z_zscore_126d(revenue: pd.Series) -> pd.Series:
    """revj_041_rev_accel_z_zscore_126d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 126)

def revj_042_rev_accel_z_rank_126d(revenue: pd.Series) -> pd.Series:
    """revj_042_rev_accel_z_rank_126d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63), 252)
    return _rank_pct(base, 126)

def revj_043_rev_accel_z_lvl_252d(revenue: pd.Series) -> pd.Series:
    """revj_043_rev_accel_z_lvl_252d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 252)

def revj_044_rev_accel_z_zscore_252d(revenue: pd.Series) -> pd.Series:
    """revj_044_rev_accel_z_zscore_252d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 252)

def revj_045_rev_accel_z_rank_252d(revenue: pd.Series) -> pd.Series:
    """revj_045_rev_accel_z_rank_252d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63), 252)
    return _rank_pct(base, 252)

def revj_046_rev_jerk_z_lvl_5d(revenue: pd.Series) -> pd.Series:
    """revj_046_rev_jerk_z_lvl_5d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 5)

def revj_047_rev_jerk_z_zscore_5d(revenue: pd.Series) -> pd.Series:
    """revj_047_rev_jerk_z_zscore_5d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 5)

def revj_048_rev_jerk_z_rank_5d(revenue: pd.Series) -> pd.Series:
    """revj_048_rev_jerk_z_rank_5d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 5)

def revj_049_rev_jerk_z_lvl_21d(revenue: pd.Series) -> pd.Series:
    """revj_049_rev_jerk_z_lvl_21d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 21)

def revj_050_rev_jerk_z_zscore_21d(revenue: pd.Series) -> pd.Series:
    """revj_050_rev_jerk_z_zscore_21d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 21)

def revj_051_rev_jerk_z_rank_21d(revenue: pd.Series) -> pd.Series:
    """revj_051_rev_jerk_z_rank_21d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 21)

def revj_052_rev_jerk_z_lvl_63d(revenue: pd.Series) -> pd.Series:
    """revj_052_rev_jerk_z_lvl_63d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 63)

def revj_053_rev_jerk_z_zscore_63d(revenue: pd.Series) -> pd.Series:
    """revj_053_rev_jerk_z_zscore_63d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 63)

def revj_054_rev_jerk_z_rank_63d(revenue: pd.Series) -> pd.Series:
    """revj_054_rev_jerk_z_rank_63d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 63)

def revj_055_rev_jerk_z_lvl_126d(revenue: pd.Series) -> pd.Series:
    """revj_055_rev_jerk_z_lvl_126d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 126)

def revj_056_rev_jerk_z_zscore_126d(revenue: pd.Series) -> pd.Series:
    """revj_056_rev_jerk_z_zscore_126d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 126)

def revj_057_rev_jerk_z_rank_126d(revenue: pd.Series) -> pd.Series:
    """revj_057_rev_jerk_z_rank_126d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 126)

def revj_058_rev_jerk_z_lvl_252d(revenue: pd.Series) -> pd.Series:
    """revj_058_rev_jerk_z_lvl_252d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 252)

def revj_059_rev_jerk_z_zscore_252d(revenue: pd.Series) -> pd.Series:
    """revj_059_rev_jerk_z_zscore_252d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 252)

def revj_060_rev_jerk_z_rank_252d(revenue: pd.Series) -> pd.Series:
    """revj_060_rev_jerk_z_rank_252d"""
    base = _zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 252)

def revj_061_rev_accel_rank_lvl_5d(revenue: pd.Series) -> pd.Series:
    """revj_061_rev_accel_rank_lvl_5d"""
    base = _rank_pct(revenue.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 5)

def revj_062_rev_accel_rank_zscore_5d(revenue: pd.Series) -> pd.Series:
    """revj_062_rev_accel_rank_zscore_5d"""
    base = _rank_pct(revenue.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 5)

def revj_063_rev_accel_rank_rank_5d(revenue: pd.Series) -> pd.Series:
    """revj_063_rev_accel_rank_rank_5d"""
    base = _rank_pct(revenue.pct_change(252).diff(63), 252)
    return _rank_pct(base, 5)

def revj_064_rev_accel_rank_lvl_21d(revenue: pd.Series) -> pd.Series:
    """revj_064_rev_accel_rank_lvl_21d"""
    base = _rank_pct(revenue.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 21)

def revj_065_rev_accel_rank_zscore_21d(revenue: pd.Series) -> pd.Series:
    """revj_065_rev_accel_rank_zscore_21d"""
    base = _rank_pct(revenue.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 21)

def revj_066_rev_accel_rank_rank_21d(revenue: pd.Series) -> pd.Series:
    """revj_066_rev_accel_rank_rank_21d"""
    base = _rank_pct(revenue.pct_change(252).diff(63), 252)
    return _rank_pct(base, 21)

def revj_067_rev_accel_rank_lvl_63d(revenue: pd.Series) -> pd.Series:
    """revj_067_rev_accel_rank_lvl_63d"""
    base = _rank_pct(revenue.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 63)

def revj_068_rev_accel_rank_zscore_63d(revenue: pd.Series) -> pd.Series:
    """revj_068_rev_accel_rank_zscore_63d"""
    base = _rank_pct(revenue.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 63)

def revj_069_rev_accel_rank_rank_63d(revenue: pd.Series) -> pd.Series:
    """revj_069_rev_accel_rank_rank_63d"""
    base = _rank_pct(revenue.pct_change(252).diff(63), 252)
    return _rank_pct(base, 63)

def revj_070_rev_accel_rank_lvl_126d(revenue: pd.Series) -> pd.Series:
    """revj_070_rev_accel_rank_lvl_126d"""
    base = _rank_pct(revenue.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 126)

def revj_071_rev_accel_rank_zscore_126d(revenue: pd.Series) -> pd.Series:
    """revj_071_rev_accel_rank_zscore_126d"""
    base = _rank_pct(revenue.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 126)

def revj_072_rev_accel_rank_rank_126d(revenue: pd.Series) -> pd.Series:
    """revj_072_rev_accel_rank_rank_126d"""
    base = _rank_pct(revenue.pct_change(252).diff(63), 252)
    return _rank_pct(base, 126)

def revj_073_rev_accel_rank_lvl_252d(revenue: pd.Series) -> pd.Series:
    """revj_073_rev_accel_rank_lvl_252d"""
    base = _rank_pct(revenue.pct_change(252).diff(63), 252)
    return _rolling_mean(base, 252)

def revj_074_rev_accel_rank_zscore_252d(revenue: pd.Series) -> pd.Series:
    """revj_074_rev_accel_rank_zscore_252d"""
    base = _rank_pct(revenue.pct_change(252).diff(63), 252)
    return _zscore_rolling(base, 252)

def revj_075_rev_accel_rank_rank_252d(revenue: pd.Series) -> pd.Series:
    """revj_075_rev_accel_rank_rank_252d"""
    base = _rank_pct(revenue.pct_change(252).diff(63), 252)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V58_REGISTRY = {
    "revj_001_rev_accel_lvl_5d": {"inputs": ["revenue"], "func": revj_001_rev_accel_lvl_5d},
    "revj_002_rev_accel_zscore_5d": {"inputs": ["revenue"], "func": revj_002_rev_accel_zscore_5d},
    "revj_003_rev_accel_rank_5d": {"inputs": ["revenue"], "func": revj_003_rev_accel_rank_5d},
    "revj_004_rev_accel_lvl_21d": {"inputs": ["revenue"], "func": revj_004_rev_accel_lvl_21d},
    "revj_005_rev_accel_zscore_21d": {"inputs": ["revenue"], "func": revj_005_rev_accel_zscore_21d},
    "revj_006_rev_accel_rank_21d": {"inputs": ["revenue"], "func": revj_006_rev_accel_rank_21d},
    "revj_007_rev_accel_lvl_63d": {"inputs": ["revenue"], "func": revj_007_rev_accel_lvl_63d},
    "revj_008_rev_accel_zscore_63d": {"inputs": ["revenue"], "func": revj_008_rev_accel_zscore_63d},
    "revj_009_rev_accel_rank_63d": {"inputs": ["revenue"], "func": revj_009_rev_accel_rank_63d},
    "revj_010_rev_accel_lvl_126d": {"inputs": ["revenue"], "func": revj_010_rev_accel_lvl_126d},
    "revj_011_rev_accel_zscore_126d": {"inputs": ["revenue"], "func": revj_011_rev_accel_zscore_126d},
    "revj_012_rev_accel_rank_126d": {"inputs": ["revenue"], "func": revj_012_rev_accel_rank_126d},
    "revj_013_rev_accel_lvl_252d": {"inputs": ["revenue"], "func": revj_013_rev_accel_lvl_252d},
    "revj_014_rev_accel_zscore_252d": {"inputs": ["revenue"], "func": revj_014_rev_accel_zscore_252d},
    "revj_015_rev_accel_rank_252d": {"inputs": ["revenue"], "func": revj_015_rev_accel_rank_252d},
    "revj_016_rev_jerk_lvl_5d": {"inputs": ["revenue"], "func": revj_016_rev_jerk_lvl_5d},
    "revj_017_rev_jerk_zscore_5d": {"inputs": ["revenue"], "func": revj_017_rev_jerk_zscore_5d},
    "revj_018_rev_jerk_rank_5d": {"inputs": ["revenue"], "func": revj_018_rev_jerk_rank_5d},
    "revj_019_rev_jerk_lvl_21d": {"inputs": ["revenue"], "func": revj_019_rev_jerk_lvl_21d},
    "revj_020_rev_jerk_zscore_21d": {"inputs": ["revenue"], "func": revj_020_rev_jerk_zscore_21d},
    "revj_021_rev_jerk_rank_21d": {"inputs": ["revenue"], "func": revj_021_rev_jerk_rank_21d},
    "revj_022_rev_jerk_lvl_63d": {"inputs": ["revenue"], "func": revj_022_rev_jerk_lvl_63d},
    "revj_023_rev_jerk_zscore_63d": {"inputs": ["revenue"], "func": revj_023_rev_jerk_zscore_63d},
    "revj_024_rev_jerk_rank_63d": {"inputs": ["revenue"], "func": revj_024_rev_jerk_rank_63d},
    "revj_025_rev_jerk_lvl_126d": {"inputs": ["revenue"], "func": revj_025_rev_jerk_lvl_126d},
    "revj_026_rev_jerk_zscore_126d": {"inputs": ["revenue"], "func": revj_026_rev_jerk_zscore_126d},
    "revj_027_rev_jerk_rank_126d": {"inputs": ["revenue"], "func": revj_027_rev_jerk_rank_126d},
    "revj_028_rev_jerk_lvl_252d": {"inputs": ["revenue"], "func": revj_028_rev_jerk_lvl_252d},
    "revj_029_rev_jerk_zscore_252d": {"inputs": ["revenue"], "func": revj_029_rev_jerk_zscore_252d},
    "revj_030_rev_jerk_rank_252d": {"inputs": ["revenue"], "func": revj_030_rev_jerk_rank_252d},
    "revj_031_rev_accel_z_lvl_5d": {"inputs": ["revenue"], "func": revj_031_rev_accel_z_lvl_5d},
    "revj_032_rev_accel_z_zscore_5d": {"inputs": ["revenue"], "func": revj_032_rev_accel_z_zscore_5d},
    "revj_033_rev_accel_z_rank_5d": {"inputs": ["revenue"], "func": revj_033_rev_accel_z_rank_5d},
    "revj_034_rev_accel_z_lvl_21d": {"inputs": ["revenue"], "func": revj_034_rev_accel_z_lvl_21d},
    "revj_035_rev_accel_z_zscore_21d": {"inputs": ["revenue"], "func": revj_035_rev_accel_z_zscore_21d},
    "revj_036_rev_accel_z_rank_21d": {"inputs": ["revenue"], "func": revj_036_rev_accel_z_rank_21d},
    "revj_037_rev_accel_z_lvl_63d": {"inputs": ["revenue"], "func": revj_037_rev_accel_z_lvl_63d},
    "revj_038_rev_accel_z_zscore_63d": {"inputs": ["revenue"], "func": revj_038_rev_accel_z_zscore_63d},
    "revj_039_rev_accel_z_rank_63d": {"inputs": ["revenue"], "func": revj_039_rev_accel_z_rank_63d},
    "revj_040_rev_accel_z_lvl_126d": {"inputs": ["revenue"], "func": revj_040_rev_accel_z_lvl_126d},
    "revj_041_rev_accel_z_zscore_126d": {"inputs": ["revenue"], "func": revj_041_rev_accel_z_zscore_126d},
    "revj_042_rev_accel_z_rank_126d": {"inputs": ["revenue"], "func": revj_042_rev_accel_z_rank_126d},
    "revj_043_rev_accel_z_lvl_252d": {"inputs": ["revenue"], "func": revj_043_rev_accel_z_lvl_252d},
    "revj_044_rev_accel_z_zscore_252d": {"inputs": ["revenue"], "func": revj_044_rev_accel_z_zscore_252d},
    "revj_045_rev_accel_z_rank_252d": {"inputs": ["revenue"], "func": revj_045_rev_accel_z_rank_252d},
    "revj_046_rev_jerk_z_lvl_5d": {"inputs": ["revenue"], "func": revj_046_rev_jerk_z_lvl_5d},
    "revj_047_rev_jerk_z_zscore_5d": {"inputs": ["revenue"], "func": revj_047_rev_jerk_z_zscore_5d},
    "revj_048_rev_jerk_z_rank_5d": {"inputs": ["revenue"], "func": revj_048_rev_jerk_z_rank_5d},
    "revj_049_rev_jerk_z_lvl_21d": {"inputs": ["revenue"], "func": revj_049_rev_jerk_z_lvl_21d},
    "revj_050_rev_jerk_z_zscore_21d": {"inputs": ["revenue"], "func": revj_050_rev_jerk_z_zscore_21d},
    "revj_051_rev_jerk_z_rank_21d": {"inputs": ["revenue"], "func": revj_051_rev_jerk_z_rank_21d},
    "revj_052_rev_jerk_z_lvl_63d": {"inputs": ["revenue"], "func": revj_052_rev_jerk_z_lvl_63d},
    "revj_053_rev_jerk_z_zscore_63d": {"inputs": ["revenue"], "func": revj_053_rev_jerk_z_zscore_63d},
    "revj_054_rev_jerk_z_rank_63d": {"inputs": ["revenue"], "func": revj_054_rev_jerk_z_rank_63d},
    "revj_055_rev_jerk_z_lvl_126d": {"inputs": ["revenue"], "func": revj_055_rev_jerk_z_lvl_126d},
    "revj_056_rev_jerk_z_zscore_126d": {"inputs": ["revenue"], "func": revj_056_rev_jerk_z_zscore_126d},
    "revj_057_rev_jerk_z_rank_126d": {"inputs": ["revenue"], "func": revj_057_rev_jerk_z_rank_126d},
    "revj_058_rev_jerk_z_lvl_252d": {"inputs": ["revenue"], "func": revj_058_rev_jerk_z_lvl_252d},
    "revj_059_rev_jerk_z_zscore_252d": {"inputs": ["revenue"], "func": revj_059_rev_jerk_z_zscore_252d},
    "revj_060_rev_jerk_z_rank_252d": {"inputs": ["revenue"], "func": revj_060_rev_jerk_z_rank_252d},
    "revj_061_rev_accel_rank_lvl_5d": {"inputs": ["revenue"], "func": revj_061_rev_accel_rank_lvl_5d},
    "revj_062_rev_accel_rank_zscore_5d": {"inputs": ["revenue"], "func": revj_062_rev_accel_rank_zscore_5d},
    "revj_063_rev_accel_rank_rank_5d": {"inputs": ["revenue"], "func": revj_063_rev_accel_rank_rank_5d},
    "revj_064_rev_accel_rank_lvl_21d": {"inputs": ["revenue"], "func": revj_064_rev_accel_rank_lvl_21d},
    "revj_065_rev_accel_rank_zscore_21d": {"inputs": ["revenue"], "func": revj_065_rev_accel_rank_zscore_21d},
    "revj_066_rev_accel_rank_rank_21d": {"inputs": ["revenue"], "func": revj_066_rev_accel_rank_rank_21d},
    "revj_067_rev_accel_rank_lvl_63d": {"inputs": ["revenue"], "func": revj_067_rev_accel_rank_lvl_63d},
    "revj_068_rev_accel_rank_zscore_63d": {"inputs": ["revenue"], "func": revj_068_rev_accel_rank_zscore_63d},
    "revj_069_rev_accel_rank_rank_63d": {"inputs": ["revenue"], "func": revj_069_rev_accel_rank_rank_63d},
    "revj_070_rev_accel_rank_lvl_126d": {"inputs": ["revenue"], "func": revj_070_rev_accel_rank_lvl_126d},
    "revj_071_rev_accel_rank_zscore_126d": {"inputs": ["revenue"], "func": revj_071_rev_accel_rank_zscore_126d},
    "revj_072_rev_accel_rank_rank_126d": {"inputs": ["revenue"], "func": revj_072_rev_accel_rank_rank_126d},
    "revj_073_rev_accel_rank_lvl_252d": {"inputs": ["revenue"], "func": revj_073_rev_accel_rank_lvl_252d},
    "revj_074_rev_accel_rank_zscore_252d": {"inputs": ["revenue"], "func": revj_074_rev_accel_rank_zscore_252d},
    "revj_075_rev_accel_rank_rank_252d": {"inputs": ["revenue"], "func": revj_075_rev_accel_rank_rank_252d},
}
