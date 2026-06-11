"""
59_margin_jerk — Base Features 001-075
Domain: margin_jerk
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

def marj_001_margin_accel_lvl_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_001_margin_accel_lvl_5d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rolling_mean(base, 5)

def marj_002_margin_accel_zscore_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_002_margin_accel_zscore_5d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _zscore_rolling(base, 5)

def marj_003_margin_accel_rank_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_003_margin_accel_rank_5d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rank_pct(base, 5)

def marj_004_margin_accel_lvl_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_004_margin_accel_lvl_21d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rolling_mean(base, 21)

def marj_005_margin_accel_zscore_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_005_margin_accel_zscore_21d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _zscore_rolling(base, 21)

def marj_006_margin_accel_rank_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_006_margin_accel_rank_21d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rank_pct(base, 21)

def marj_007_margin_accel_lvl_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_007_margin_accel_lvl_63d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rolling_mean(base, 63)

def marj_008_margin_accel_zscore_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_008_margin_accel_zscore_63d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _zscore_rolling(base, 63)

def marj_009_margin_accel_rank_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_009_margin_accel_rank_63d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rank_pct(base, 63)

def marj_010_margin_accel_lvl_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_010_margin_accel_lvl_126d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rolling_mean(base, 126)

def marj_011_margin_accel_zscore_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_011_margin_accel_zscore_126d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _zscore_rolling(base, 126)

def marj_012_margin_accel_rank_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_012_margin_accel_rank_126d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rank_pct(base, 126)

def marj_013_margin_accel_lvl_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_013_margin_accel_lvl_252d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rolling_mean(base, 252)

def marj_014_margin_accel_zscore_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_014_margin_accel_zscore_252d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _zscore_rolling(base, 252)

def marj_015_margin_accel_rank_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_015_margin_accel_rank_252d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rank_pct(base, 252)

def marj_016_margin_jerk_lvl_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_016_margin_jerk_lvl_5d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21)
    return _rolling_mean(base, 5)

def marj_017_margin_jerk_zscore_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_017_margin_jerk_zscore_5d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21)
    return _zscore_rolling(base, 5)

def marj_018_margin_jerk_rank_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_018_margin_jerk_rank_5d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21)
    return _rank_pct(base, 5)

def marj_019_margin_jerk_lvl_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_019_margin_jerk_lvl_21d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21)
    return _rolling_mean(base, 21)

def marj_020_margin_jerk_zscore_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_020_margin_jerk_zscore_21d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21)
    return _zscore_rolling(base, 21)

def marj_021_margin_jerk_rank_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_021_margin_jerk_rank_21d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21)
    return _rank_pct(base, 21)

def marj_022_margin_jerk_lvl_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_022_margin_jerk_lvl_63d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21)
    return _rolling_mean(base, 63)

def marj_023_margin_jerk_zscore_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_023_margin_jerk_zscore_63d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21)
    return _zscore_rolling(base, 63)

def marj_024_margin_jerk_rank_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_024_margin_jerk_rank_63d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21)
    return _rank_pct(base, 63)

def marj_025_margin_jerk_lvl_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_025_margin_jerk_lvl_126d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21)
    return _rolling_mean(base, 126)

def marj_026_margin_jerk_zscore_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_026_margin_jerk_zscore_126d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21)
    return _zscore_rolling(base, 126)

def marj_027_margin_jerk_rank_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_027_margin_jerk_rank_126d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21)
    return _rank_pct(base, 126)

def marj_028_margin_jerk_lvl_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_028_margin_jerk_lvl_252d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21)
    return _rolling_mean(base, 252)

def marj_029_margin_jerk_zscore_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_029_margin_jerk_zscore_252d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21)
    return _zscore_rolling(base, 252)

def marj_030_margin_jerk_rank_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_030_margin_jerk_rank_252d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21)
    return _rank_pct(base, 252)

def marj_031_margin_accel_z_lvl_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_031_margin_accel_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rolling_mean(base, 5)

def marj_032_margin_accel_z_zscore_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_032_margin_accel_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _zscore_rolling(base, 5)

def marj_033_margin_accel_z_rank_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_033_margin_accel_z_rank_5d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rank_pct(base, 5)

def marj_034_margin_accel_z_lvl_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_034_margin_accel_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rolling_mean(base, 21)

def marj_035_margin_accel_z_zscore_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_035_margin_accel_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _zscore_rolling(base, 21)

def marj_036_margin_accel_z_rank_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_036_margin_accel_z_rank_21d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rank_pct(base, 21)

def marj_037_margin_accel_z_lvl_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_037_margin_accel_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rolling_mean(base, 63)

def marj_038_margin_accel_z_zscore_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_038_margin_accel_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _zscore_rolling(base, 63)

def marj_039_margin_accel_z_rank_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_039_margin_accel_z_rank_63d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rank_pct(base, 63)

def marj_040_margin_accel_z_lvl_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_040_margin_accel_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rolling_mean(base, 126)

def marj_041_margin_accel_z_zscore_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_041_margin_accel_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _zscore_rolling(base, 126)

def marj_042_margin_accel_z_rank_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_042_margin_accel_z_rank_126d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rank_pct(base, 126)

def marj_043_margin_accel_z_lvl_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_043_margin_accel_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rolling_mean(base, 252)

def marj_044_margin_accel_z_zscore_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_044_margin_accel_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _zscore_rolling(base, 252)

def marj_045_margin_accel_z_rank_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_045_margin_accel_z_rank_252d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rank_pct(base, 252)

def marj_046_margin_jerk_z_lvl_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_046_margin_jerk_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 5)

def marj_047_margin_jerk_z_zscore_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_047_margin_jerk_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 5)

def marj_048_margin_jerk_z_rank_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_048_margin_jerk_z_rank_5d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rank_pct(base, 5)

def marj_049_margin_jerk_z_lvl_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_049_margin_jerk_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 21)

def marj_050_margin_jerk_z_zscore_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_050_margin_jerk_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 21)

def marj_051_margin_jerk_z_rank_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_051_margin_jerk_z_rank_21d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rank_pct(base, 21)

def marj_052_margin_jerk_z_lvl_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_052_margin_jerk_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 63)

def marj_053_margin_jerk_z_zscore_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_053_margin_jerk_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 63)

def marj_054_margin_jerk_z_rank_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_054_margin_jerk_z_rank_63d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rank_pct(base, 63)

def marj_055_margin_jerk_z_lvl_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_055_margin_jerk_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 126)

def marj_056_margin_jerk_z_zscore_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_056_margin_jerk_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 126)

def marj_057_margin_jerk_z_rank_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_057_margin_jerk_z_rank_126d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rank_pct(base, 126)

def marj_058_margin_jerk_z_lvl_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_058_margin_jerk_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 252)

def marj_059_margin_jerk_z_zscore_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_059_margin_jerk_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 252)

def marj_060_margin_jerk_z_rank_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_060_margin_jerk_z_rank_252d"""
    base = _zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rank_pct(base, 252)

def marj_061_margin_accel_rank_lvl_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_061_margin_accel_rank_lvl_5d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rolling_mean(base, 5)

def marj_062_margin_accel_rank_zscore_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_062_margin_accel_rank_zscore_5d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _zscore_rolling(base, 5)

def marj_063_margin_accel_rank_rank_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_063_margin_accel_rank_rank_5d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rank_pct(base, 5)

def marj_064_margin_accel_rank_lvl_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_064_margin_accel_rank_lvl_21d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rolling_mean(base, 21)

def marj_065_margin_accel_rank_zscore_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_065_margin_accel_rank_zscore_21d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _zscore_rolling(base, 21)

def marj_066_margin_accel_rank_rank_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_066_margin_accel_rank_rank_21d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rank_pct(base, 21)

def marj_067_margin_accel_rank_lvl_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_067_margin_accel_rank_lvl_63d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rolling_mean(base, 63)

def marj_068_margin_accel_rank_zscore_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_068_margin_accel_rank_zscore_63d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _zscore_rolling(base, 63)

def marj_069_margin_accel_rank_rank_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_069_margin_accel_rank_rank_63d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rank_pct(base, 63)

def marj_070_margin_accel_rank_lvl_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_070_margin_accel_rank_lvl_126d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rolling_mean(base, 126)

def marj_071_margin_accel_rank_zscore_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_071_margin_accel_rank_zscore_126d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _zscore_rolling(base, 126)

def marj_072_margin_accel_rank_rank_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_072_margin_accel_rank_rank_126d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rank_pct(base, 126)

def marj_073_margin_accel_rank_lvl_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_073_margin_accel_rank_lvl_252d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rolling_mean(base, 252)

def marj_074_margin_accel_rank_zscore_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_074_margin_accel_rank_zscore_252d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _zscore_rolling(base, 252)

def marj_075_margin_accel_rank_rank_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_075_margin_accel_rank_rank_252d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V59_REGISTRY = {
    "marj_001_margin_accel_lvl_5d": {"inputs": ["netinc", "revenue"], "func": marj_001_margin_accel_lvl_5d},
    "marj_002_margin_accel_zscore_5d": {"inputs": ["netinc", "revenue"], "func": marj_002_margin_accel_zscore_5d},
    "marj_003_margin_accel_rank_5d": {"inputs": ["netinc", "revenue"], "func": marj_003_margin_accel_rank_5d},
    "marj_004_margin_accel_lvl_21d": {"inputs": ["netinc", "revenue"], "func": marj_004_margin_accel_lvl_21d},
    "marj_005_margin_accel_zscore_21d": {"inputs": ["netinc", "revenue"], "func": marj_005_margin_accel_zscore_21d},
    "marj_006_margin_accel_rank_21d": {"inputs": ["netinc", "revenue"], "func": marj_006_margin_accel_rank_21d},
    "marj_007_margin_accel_lvl_63d": {"inputs": ["netinc", "revenue"], "func": marj_007_margin_accel_lvl_63d},
    "marj_008_margin_accel_zscore_63d": {"inputs": ["netinc", "revenue"], "func": marj_008_margin_accel_zscore_63d},
    "marj_009_margin_accel_rank_63d": {"inputs": ["netinc", "revenue"], "func": marj_009_margin_accel_rank_63d},
    "marj_010_margin_accel_lvl_126d": {"inputs": ["netinc", "revenue"], "func": marj_010_margin_accel_lvl_126d},
    "marj_011_margin_accel_zscore_126d": {"inputs": ["netinc", "revenue"], "func": marj_011_margin_accel_zscore_126d},
    "marj_012_margin_accel_rank_126d": {"inputs": ["netinc", "revenue"], "func": marj_012_margin_accel_rank_126d},
    "marj_013_margin_accel_lvl_252d": {"inputs": ["netinc", "revenue"], "func": marj_013_margin_accel_lvl_252d},
    "marj_014_margin_accel_zscore_252d": {"inputs": ["netinc", "revenue"], "func": marj_014_margin_accel_zscore_252d},
    "marj_015_margin_accel_rank_252d": {"inputs": ["netinc", "revenue"], "func": marj_015_margin_accel_rank_252d},
    "marj_016_margin_jerk_lvl_5d": {"inputs": ["netinc", "revenue"], "func": marj_016_margin_jerk_lvl_5d},
    "marj_017_margin_jerk_zscore_5d": {"inputs": ["netinc", "revenue"], "func": marj_017_margin_jerk_zscore_5d},
    "marj_018_margin_jerk_rank_5d": {"inputs": ["netinc", "revenue"], "func": marj_018_margin_jerk_rank_5d},
    "marj_019_margin_jerk_lvl_21d": {"inputs": ["netinc", "revenue"], "func": marj_019_margin_jerk_lvl_21d},
    "marj_020_margin_jerk_zscore_21d": {"inputs": ["netinc", "revenue"], "func": marj_020_margin_jerk_zscore_21d},
    "marj_021_margin_jerk_rank_21d": {"inputs": ["netinc", "revenue"], "func": marj_021_margin_jerk_rank_21d},
    "marj_022_margin_jerk_lvl_63d": {"inputs": ["netinc", "revenue"], "func": marj_022_margin_jerk_lvl_63d},
    "marj_023_margin_jerk_zscore_63d": {"inputs": ["netinc", "revenue"], "func": marj_023_margin_jerk_zscore_63d},
    "marj_024_margin_jerk_rank_63d": {"inputs": ["netinc", "revenue"], "func": marj_024_margin_jerk_rank_63d},
    "marj_025_margin_jerk_lvl_126d": {"inputs": ["netinc", "revenue"], "func": marj_025_margin_jerk_lvl_126d},
    "marj_026_margin_jerk_zscore_126d": {"inputs": ["netinc", "revenue"], "func": marj_026_margin_jerk_zscore_126d},
    "marj_027_margin_jerk_rank_126d": {"inputs": ["netinc", "revenue"], "func": marj_027_margin_jerk_rank_126d},
    "marj_028_margin_jerk_lvl_252d": {"inputs": ["netinc", "revenue"], "func": marj_028_margin_jerk_lvl_252d},
    "marj_029_margin_jerk_zscore_252d": {"inputs": ["netinc", "revenue"], "func": marj_029_margin_jerk_zscore_252d},
    "marj_030_margin_jerk_rank_252d": {"inputs": ["netinc", "revenue"], "func": marj_030_margin_jerk_rank_252d},
    "marj_031_margin_accel_z_lvl_5d": {"inputs": ["netinc", "revenue"], "func": marj_031_margin_accel_z_lvl_5d},
    "marj_032_margin_accel_z_zscore_5d": {"inputs": ["netinc", "revenue"], "func": marj_032_margin_accel_z_zscore_5d},
    "marj_033_margin_accel_z_rank_5d": {"inputs": ["netinc", "revenue"], "func": marj_033_margin_accel_z_rank_5d},
    "marj_034_margin_accel_z_lvl_21d": {"inputs": ["netinc", "revenue"], "func": marj_034_margin_accel_z_lvl_21d},
    "marj_035_margin_accel_z_zscore_21d": {"inputs": ["netinc", "revenue"], "func": marj_035_margin_accel_z_zscore_21d},
    "marj_036_margin_accel_z_rank_21d": {"inputs": ["netinc", "revenue"], "func": marj_036_margin_accel_z_rank_21d},
    "marj_037_margin_accel_z_lvl_63d": {"inputs": ["netinc", "revenue"], "func": marj_037_margin_accel_z_lvl_63d},
    "marj_038_margin_accel_z_zscore_63d": {"inputs": ["netinc", "revenue"], "func": marj_038_margin_accel_z_zscore_63d},
    "marj_039_margin_accel_z_rank_63d": {"inputs": ["netinc", "revenue"], "func": marj_039_margin_accel_z_rank_63d},
    "marj_040_margin_accel_z_lvl_126d": {"inputs": ["netinc", "revenue"], "func": marj_040_margin_accel_z_lvl_126d},
    "marj_041_margin_accel_z_zscore_126d": {"inputs": ["netinc", "revenue"], "func": marj_041_margin_accel_z_zscore_126d},
    "marj_042_margin_accel_z_rank_126d": {"inputs": ["netinc", "revenue"], "func": marj_042_margin_accel_z_rank_126d},
    "marj_043_margin_accel_z_lvl_252d": {"inputs": ["netinc", "revenue"], "func": marj_043_margin_accel_z_lvl_252d},
    "marj_044_margin_accel_z_zscore_252d": {"inputs": ["netinc", "revenue"], "func": marj_044_margin_accel_z_zscore_252d},
    "marj_045_margin_accel_z_rank_252d": {"inputs": ["netinc", "revenue"], "func": marj_045_margin_accel_z_rank_252d},
    "marj_046_margin_jerk_z_lvl_5d": {"inputs": ["netinc", "revenue"], "func": marj_046_margin_jerk_z_lvl_5d},
    "marj_047_margin_jerk_z_zscore_5d": {"inputs": ["netinc", "revenue"], "func": marj_047_margin_jerk_z_zscore_5d},
    "marj_048_margin_jerk_z_rank_5d": {"inputs": ["netinc", "revenue"], "func": marj_048_margin_jerk_z_rank_5d},
    "marj_049_margin_jerk_z_lvl_21d": {"inputs": ["netinc", "revenue"], "func": marj_049_margin_jerk_z_lvl_21d},
    "marj_050_margin_jerk_z_zscore_21d": {"inputs": ["netinc", "revenue"], "func": marj_050_margin_jerk_z_zscore_21d},
    "marj_051_margin_jerk_z_rank_21d": {"inputs": ["netinc", "revenue"], "func": marj_051_margin_jerk_z_rank_21d},
    "marj_052_margin_jerk_z_lvl_63d": {"inputs": ["netinc", "revenue"], "func": marj_052_margin_jerk_z_lvl_63d},
    "marj_053_margin_jerk_z_zscore_63d": {"inputs": ["netinc", "revenue"], "func": marj_053_margin_jerk_z_zscore_63d},
    "marj_054_margin_jerk_z_rank_63d": {"inputs": ["netinc", "revenue"], "func": marj_054_margin_jerk_z_rank_63d},
    "marj_055_margin_jerk_z_lvl_126d": {"inputs": ["netinc", "revenue"], "func": marj_055_margin_jerk_z_lvl_126d},
    "marj_056_margin_jerk_z_zscore_126d": {"inputs": ["netinc", "revenue"], "func": marj_056_margin_jerk_z_zscore_126d},
    "marj_057_margin_jerk_z_rank_126d": {"inputs": ["netinc", "revenue"], "func": marj_057_margin_jerk_z_rank_126d},
    "marj_058_margin_jerk_z_lvl_252d": {"inputs": ["netinc", "revenue"], "func": marj_058_margin_jerk_z_lvl_252d},
    "marj_059_margin_jerk_z_zscore_252d": {"inputs": ["netinc", "revenue"], "func": marj_059_margin_jerk_z_zscore_252d},
    "marj_060_margin_jerk_z_rank_252d": {"inputs": ["netinc", "revenue"], "func": marj_060_margin_jerk_z_rank_252d},
    "marj_061_margin_accel_rank_lvl_5d": {"inputs": ["netinc", "revenue"], "func": marj_061_margin_accel_rank_lvl_5d},
    "marj_062_margin_accel_rank_zscore_5d": {"inputs": ["netinc", "revenue"], "func": marj_062_margin_accel_rank_zscore_5d},
    "marj_063_margin_accel_rank_rank_5d": {"inputs": ["netinc", "revenue"], "func": marj_063_margin_accel_rank_rank_5d},
    "marj_064_margin_accel_rank_lvl_21d": {"inputs": ["netinc", "revenue"], "func": marj_064_margin_accel_rank_lvl_21d},
    "marj_065_margin_accel_rank_zscore_21d": {"inputs": ["netinc", "revenue"], "func": marj_065_margin_accel_rank_zscore_21d},
    "marj_066_margin_accel_rank_rank_21d": {"inputs": ["netinc", "revenue"], "func": marj_066_margin_accel_rank_rank_21d},
    "marj_067_margin_accel_rank_lvl_63d": {"inputs": ["netinc", "revenue"], "func": marj_067_margin_accel_rank_lvl_63d},
    "marj_068_margin_accel_rank_zscore_63d": {"inputs": ["netinc", "revenue"], "func": marj_068_margin_accel_rank_zscore_63d},
    "marj_069_margin_accel_rank_rank_63d": {"inputs": ["netinc", "revenue"], "func": marj_069_margin_accel_rank_rank_63d},
    "marj_070_margin_accel_rank_lvl_126d": {"inputs": ["netinc", "revenue"], "func": marj_070_margin_accel_rank_lvl_126d},
    "marj_071_margin_accel_rank_zscore_126d": {"inputs": ["netinc", "revenue"], "func": marj_071_margin_accel_rank_zscore_126d},
    "marj_072_margin_accel_rank_rank_126d": {"inputs": ["netinc", "revenue"], "func": marj_072_margin_accel_rank_rank_126d},
    "marj_073_margin_accel_rank_lvl_252d": {"inputs": ["netinc", "revenue"], "func": marj_073_margin_accel_rank_lvl_252d},
    "marj_074_margin_accel_rank_zscore_252d": {"inputs": ["netinc", "revenue"], "func": marj_074_margin_accel_rank_zscore_252d},
    "marj_075_margin_accel_rank_rank_252d": {"inputs": ["netinc", "revenue"], "func": marj_075_margin_accel_rank_rank_252d},
}
