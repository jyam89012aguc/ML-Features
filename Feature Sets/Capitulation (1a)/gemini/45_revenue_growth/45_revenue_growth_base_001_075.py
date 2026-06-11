"""
45_revenue_growth — Base Features 001-075
Domain: revenue_growth
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

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

def _pct_change(s: pd.Series, periods: int) -> pd.Series:
    return _safe_div(s - s.shift(periods), s.shift(periods).abs())

# ── Feature functions ────────────────────────────────────────────────────────

def revg_001_rev_yoy_lvl_5d(revenue: pd.Series) -> pd.Series:
    """revg_001_rev_yoy_lvl_5d"""
    base = _pct_change(revenue, 252)
    return _rolling_mean(base, 5)

def revg_002_rev_yoy_zscore_5d(revenue: pd.Series) -> pd.Series:
    """revg_002_rev_yoy_zscore_5d"""
    base = _pct_change(revenue, 252)
    return _zscore_rolling(base, 5)

def revg_003_rev_yoy_rank_5d(revenue: pd.Series) -> pd.Series:
    """revg_003_rev_yoy_rank_5d"""
    base = _pct_change(revenue, 252)
    return _rank_pct(base, 5)

def revg_004_rev_yoy_lvl_21d(revenue: pd.Series) -> pd.Series:
    """revg_004_rev_yoy_lvl_21d"""
    base = _pct_change(revenue, 252)
    return _rolling_mean(base, 21)

def revg_005_rev_yoy_zscore_21d(revenue: pd.Series) -> pd.Series:
    """revg_005_rev_yoy_zscore_21d"""
    base = _pct_change(revenue, 252)
    return _zscore_rolling(base, 21)

def revg_006_rev_yoy_rank_21d(revenue: pd.Series) -> pd.Series:
    """revg_006_rev_yoy_rank_21d"""
    base = _pct_change(revenue, 252)
    return _rank_pct(base, 21)

def revg_007_rev_yoy_lvl_63d(revenue: pd.Series) -> pd.Series:
    """revg_007_rev_yoy_lvl_63d"""
    base = _pct_change(revenue, 252)
    return _rolling_mean(base, 63)

def revg_008_rev_yoy_zscore_63d(revenue: pd.Series) -> pd.Series:
    """revg_008_rev_yoy_zscore_63d"""
    base = _pct_change(revenue, 252)
    return _zscore_rolling(base, 63)

def revg_009_rev_yoy_rank_63d(revenue: pd.Series) -> pd.Series:
    """revg_009_rev_yoy_rank_63d"""
    base = _pct_change(revenue, 252)
    return _rank_pct(base, 63)

def revg_010_rev_yoy_lvl_126d(revenue: pd.Series) -> pd.Series:
    """revg_010_rev_yoy_lvl_126d"""
    base = _pct_change(revenue, 252)
    return _rolling_mean(base, 126)

def revg_011_rev_yoy_zscore_126d(revenue: pd.Series) -> pd.Series:
    """revg_011_rev_yoy_zscore_126d"""
    base = _pct_change(revenue, 252)
    return _zscore_rolling(base, 126)

def revg_012_rev_yoy_rank_126d(revenue: pd.Series) -> pd.Series:
    """revg_012_rev_yoy_rank_126d"""
    base = _pct_change(revenue, 252)
    return _rank_pct(base, 126)

def revg_013_rev_yoy_lvl_252d(revenue: pd.Series) -> pd.Series:
    """revg_013_rev_yoy_lvl_252d"""
    base = _pct_change(revenue, 252)
    return _rolling_mean(base, 252)

def revg_014_rev_yoy_zscore_252d(revenue: pd.Series) -> pd.Series:
    """revg_014_rev_yoy_zscore_252d"""
    base = _pct_change(revenue, 252)
    return _zscore_rolling(base, 252)

def revg_015_rev_yoy_rank_252d(revenue: pd.Series) -> pd.Series:
    """revg_015_rev_yoy_rank_252d"""
    base = _pct_change(revenue, 252)
    return _rank_pct(base, 252)

def revg_016_rev_qoq_lvl_5d(revenue: pd.Series) -> pd.Series:
    """revg_016_rev_qoq_lvl_5d"""
    base = _pct_change(revenue, 63)
    return _rolling_mean(base, 5)

def revg_017_rev_qoq_zscore_5d(revenue: pd.Series) -> pd.Series:
    """revg_017_rev_qoq_zscore_5d"""
    base = _pct_change(revenue, 63)
    return _zscore_rolling(base, 5)

def revg_018_rev_qoq_rank_5d(revenue: pd.Series) -> pd.Series:
    """revg_018_rev_qoq_rank_5d"""
    base = _pct_change(revenue, 63)
    return _rank_pct(base, 5)

def revg_019_rev_qoq_lvl_21d(revenue: pd.Series) -> pd.Series:
    """revg_019_rev_qoq_lvl_21d"""
    base = _pct_change(revenue, 63)
    return _rolling_mean(base, 21)

def revg_020_rev_qoq_zscore_21d(revenue: pd.Series) -> pd.Series:
    """revg_020_rev_qoq_zscore_21d"""
    base = _pct_change(revenue, 63)
    return _zscore_rolling(base, 21)

def revg_021_rev_qoq_rank_21d(revenue: pd.Series) -> pd.Series:
    """revg_021_rev_qoq_rank_21d"""
    base = _pct_change(revenue, 63)
    return _rank_pct(base, 21)

def revg_022_rev_qoq_lvl_63d(revenue: pd.Series) -> pd.Series:
    """revg_022_rev_qoq_lvl_63d"""
    base = _pct_change(revenue, 63)
    return _rolling_mean(base, 63)

def revg_023_rev_qoq_zscore_63d(revenue: pd.Series) -> pd.Series:
    """revg_023_rev_qoq_zscore_63d"""
    base = _pct_change(revenue, 63)
    return _zscore_rolling(base, 63)

def revg_024_rev_qoq_rank_63d(revenue: pd.Series) -> pd.Series:
    """revg_024_rev_qoq_rank_63d"""
    base = _pct_change(revenue, 63)
    return _rank_pct(base, 63)

def revg_025_rev_qoq_lvl_126d(revenue: pd.Series) -> pd.Series:
    """revg_025_rev_qoq_lvl_126d"""
    base = _pct_change(revenue, 63)
    return _rolling_mean(base, 126)

def revg_026_rev_qoq_zscore_126d(revenue: pd.Series) -> pd.Series:
    """revg_026_rev_qoq_zscore_126d"""
    base = _pct_change(revenue, 63)
    return _zscore_rolling(base, 126)

def revg_027_rev_qoq_rank_126d(revenue: pd.Series) -> pd.Series:
    """revg_027_rev_qoq_rank_126d"""
    base = _pct_change(revenue, 63)
    return _rank_pct(base, 126)

def revg_028_rev_qoq_lvl_252d(revenue: pd.Series) -> pd.Series:
    """revg_028_rev_qoq_lvl_252d"""
    base = _pct_change(revenue, 63)
    return _rolling_mean(base, 252)

def revg_029_rev_qoq_zscore_252d(revenue: pd.Series) -> pd.Series:
    """revg_029_rev_qoq_zscore_252d"""
    base = _pct_change(revenue, 63)
    return _zscore_rolling(base, 252)

def revg_030_rev_qoq_rank_252d(revenue: pd.Series) -> pd.Series:
    """revg_030_rev_qoq_rank_252d"""
    base = _pct_change(revenue, 63)
    return _rank_pct(base, 252)

def revg_031_rev_mom_lvl_5d(revenue: pd.Series) -> pd.Series:
    """revg_031_rev_mom_lvl_5d"""
    base = _pct_change(revenue, 21)
    return _rolling_mean(base, 5)

def revg_032_rev_mom_zscore_5d(revenue: pd.Series) -> pd.Series:
    """revg_032_rev_mom_zscore_5d"""
    base = _pct_change(revenue, 21)
    return _zscore_rolling(base, 5)

def revg_033_rev_mom_rank_5d(revenue: pd.Series) -> pd.Series:
    """revg_033_rev_mom_rank_5d"""
    base = _pct_change(revenue, 21)
    return _rank_pct(base, 5)

def revg_034_rev_mom_lvl_21d(revenue: pd.Series) -> pd.Series:
    """revg_034_rev_mom_lvl_21d"""
    base = _pct_change(revenue, 21)
    return _rolling_mean(base, 21)

def revg_035_rev_mom_zscore_21d(revenue: pd.Series) -> pd.Series:
    """revg_035_rev_mom_zscore_21d"""
    base = _pct_change(revenue, 21)
    return _zscore_rolling(base, 21)

def revg_036_rev_mom_rank_21d(revenue: pd.Series) -> pd.Series:
    """revg_036_rev_mom_rank_21d"""
    base = _pct_change(revenue, 21)
    return _rank_pct(base, 21)

def revg_037_rev_mom_lvl_63d(revenue: pd.Series) -> pd.Series:
    """revg_037_rev_mom_lvl_63d"""
    base = _pct_change(revenue, 21)
    return _rolling_mean(base, 63)

def revg_038_rev_mom_zscore_63d(revenue: pd.Series) -> pd.Series:
    """revg_038_rev_mom_zscore_63d"""
    base = _pct_change(revenue, 21)
    return _zscore_rolling(base, 63)

def revg_039_rev_mom_rank_63d(revenue: pd.Series) -> pd.Series:
    """revg_039_rev_mom_rank_63d"""
    base = _pct_change(revenue, 21)
    return _rank_pct(base, 63)

def revg_040_rev_mom_lvl_126d(revenue: pd.Series) -> pd.Series:
    """revg_040_rev_mom_lvl_126d"""
    base = _pct_change(revenue, 21)
    return _rolling_mean(base, 126)

def revg_041_rev_mom_zscore_126d(revenue: pd.Series) -> pd.Series:
    """revg_041_rev_mom_zscore_126d"""
    base = _pct_change(revenue, 21)
    return _zscore_rolling(base, 126)

def revg_042_rev_mom_rank_126d(revenue: pd.Series) -> pd.Series:
    """revg_042_rev_mom_rank_126d"""
    base = _pct_change(revenue, 21)
    return _rank_pct(base, 126)

def revg_043_rev_mom_lvl_252d(revenue: pd.Series) -> pd.Series:
    """revg_043_rev_mom_lvl_252d"""
    base = _pct_change(revenue, 21)
    return _rolling_mean(base, 252)

def revg_044_rev_mom_zscore_252d(revenue: pd.Series) -> pd.Series:
    """revg_044_rev_mom_zscore_252d"""
    base = _pct_change(revenue, 21)
    return _zscore_rolling(base, 252)

def revg_045_rev_mom_rank_252d(revenue: pd.Series) -> pd.Series:
    """revg_045_rev_mom_rank_252d"""
    base = _pct_change(revenue, 21)
    return _rank_pct(base, 252)

def revg_046_rev_growth_accel_lvl_5d(revenue: pd.Series) -> pd.Series:
    """revg_046_rev_growth_accel_lvl_5d"""
    base = _pct_change(revenue, 252) - _pct_change(revenue, 252).shift(63)
    return _rolling_mean(base, 5)

def revg_047_rev_growth_accel_zscore_5d(revenue: pd.Series) -> pd.Series:
    """revg_047_rev_growth_accel_zscore_5d"""
    base = _pct_change(revenue, 252) - _pct_change(revenue, 252).shift(63)
    return _zscore_rolling(base, 5)

def revg_048_rev_growth_accel_rank_5d(revenue: pd.Series) -> pd.Series:
    """revg_048_rev_growth_accel_rank_5d"""
    base = _pct_change(revenue, 252) - _pct_change(revenue, 252).shift(63)
    return _rank_pct(base, 5)

def revg_049_rev_growth_accel_lvl_21d(revenue: pd.Series) -> pd.Series:
    """revg_049_rev_growth_accel_lvl_21d"""
    base = _pct_change(revenue, 252) - _pct_change(revenue, 252).shift(63)
    return _rolling_mean(base, 21)

def revg_050_rev_growth_accel_zscore_21d(revenue: pd.Series) -> pd.Series:
    """revg_050_rev_growth_accel_zscore_21d"""
    base = _pct_change(revenue, 252) - _pct_change(revenue, 252).shift(63)
    return _zscore_rolling(base, 21)

def revg_051_rev_growth_accel_rank_21d(revenue: pd.Series) -> pd.Series:
    """revg_051_rev_growth_accel_rank_21d"""
    base = _pct_change(revenue, 252) - _pct_change(revenue, 252).shift(63)
    return _rank_pct(base, 21)

def revg_052_rev_growth_accel_lvl_63d(revenue: pd.Series) -> pd.Series:
    """revg_052_rev_growth_accel_lvl_63d"""
    base = _pct_change(revenue, 252) - _pct_change(revenue, 252).shift(63)
    return _rolling_mean(base, 63)

def revg_053_rev_growth_accel_zscore_63d(revenue: pd.Series) -> pd.Series:
    """revg_053_rev_growth_accel_zscore_63d"""
    base = _pct_change(revenue, 252) - _pct_change(revenue, 252).shift(63)
    return _zscore_rolling(base, 63)

def revg_054_rev_growth_accel_rank_63d(revenue: pd.Series) -> pd.Series:
    """revg_054_rev_growth_accel_rank_63d"""
    base = _pct_change(revenue, 252) - _pct_change(revenue, 252).shift(63)
    return _rank_pct(base, 63)

def revg_055_rev_growth_accel_lvl_126d(revenue: pd.Series) -> pd.Series:
    """revg_055_rev_growth_accel_lvl_126d"""
    base = _pct_change(revenue, 252) - _pct_change(revenue, 252).shift(63)
    return _rolling_mean(base, 126)

def revg_056_rev_growth_accel_zscore_126d(revenue: pd.Series) -> pd.Series:
    """revg_056_rev_growth_accel_zscore_126d"""
    base = _pct_change(revenue, 252) - _pct_change(revenue, 252).shift(63)
    return _zscore_rolling(base, 126)

def revg_057_rev_growth_accel_rank_126d(revenue: pd.Series) -> pd.Series:
    """revg_057_rev_growth_accel_rank_126d"""
    base = _pct_change(revenue, 252) - _pct_change(revenue, 252).shift(63)
    return _rank_pct(base, 126)

def revg_058_rev_growth_accel_lvl_252d(revenue: pd.Series) -> pd.Series:
    """revg_058_rev_growth_accel_lvl_252d"""
    base = _pct_change(revenue, 252) - _pct_change(revenue, 252).shift(63)
    return _rolling_mean(base, 252)

def revg_059_rev_growth_accel_zscore_252d(revenue: pd.Series) -> pd.Series:
    """revg_059_rev_growth_accel_zscore_252d"""
    base = _pct_change(revenue, 252) - _pct_change(revenue, 252).shift(63)
    return _zscore_rolling(base, 252)

def revg_060_rev_growth_accel_rank_252d(revenue: pd.Series) -> pd.Series:
    """revg_060_rev_growth_accel_rank_252d"""
    base = _pct_change(revenue, 252) - _pct_change(revenue, 252).shift(63)
    return _rank_pct(base, 252)

def revg_061_rev_growth_stability_lvl_5d(revenue: pd.Series) -> pd.Series:
    """revg_061_rev_growth_stability_lvl_5d"""
    base = _rolling_std(_pct_change(revenue, 21), 63)
    return _rolling_mean(base, 5)

def revg_062_rev_growth_stability_zscore_5d(revenue: pd.Series) -> pd.Series:
    """revg_062_rev_growth_stability_zscore_5d"""
    base = _rolling_std(_pct_change(revenue, 21), 63)
    return _zscore_rolling(base, 5)

def revg_063_rev_growth_stability_rank_5d(revenue: pd.Series) -> pd.Series:
    """revg_063_rev_growth_stability_rank_5d"""
    base = _rolling_std(_pct_change(revenue, 21), 63)
    return _rank_pct(base, 5)

def revg_064_rev_growth_stability_lvl_21d(revenue: pd.Series) -> pd.Series:
    """revg_064_rev_growth_stability_lvl_21d"""
    base = _rolling_std(_pct_change(revenue, 21), 63)
    return _rolling_mean(base, 21)

def revg_065_rev_growth_stability_zscore_21d(revenue: pd.Series) -> pd.Series:
    """revg_065_rev_growth_stability_zscore_21d"""
    base = _rolling_std(_pct_change(revenue, 21), 63)
    return _zscore_rolling(base, 21)

def revg_066_rev_growth_stability_rank_21d(revenue: pd.Series) -> pd.Series:
    """revg_066_rev_growth_stability_rank_21d"""
    base = _rolling_std(_pct_change(revenue, 21), 63)
    return _rank_pct(base, 21)

def revg_067_rev_growth_stability_lvl_63d(revenue: pd.Series) -> pd.Series:
    """revg_067_rev_growth_stability_lvl_63d"""
    base = _rolling_std(_pct_change(revenue, 21), 63)
    return _rolling_mean(base, 63)

def revg_068_rev_growth_stability_zscore_63d(revenue: pd.Series) -> pd.Series:
    """revg_068_rev_growth_stability_zscore_63d"""
    base = _rolling_std(_pct_change(revenue, 21), 63)
    return _zscore_rolling(base, 63)

def revg_069_rev_growth_stability_rank_63d(revenue: pd.Series) -> pd.Series:
    """revg_069_rev_growth_stability_rank_63d"""
    base = _rolling_std(_pct_change(revenue, 21), 63)
    return _rank_pct(base, 63)

def revg_070_rev_growth_stability_lvl_126d(revenue: pd.Series) -> pd.Series:
    """revg_070_rev_growth_stability_lvl_126d"""
    base = _rolling_std(_pct_change(revenue, 21), 63)
    return _rolling_mean(base, 126)

def revg_071_rev_growth_stability_zscore_126d(revenue: pd.Series) -> pd.Series:
    """revg_071_rev_growth_stability_zscore_126d"""
    base = _rolling_std(_pct_change(revenue, 21), 63)
    return _zscore_rolling(base, 126)

def revg_072_rev_growth_stability_rank_126d(revenue: pd.Series) -> pd.Series:
    """revg_072_rev_growth_stability_rank_126d"""
    base = _rolling_std(_pct_change(revenue, 21), 63)
    return _rank_pct(base, 126)

def revg_073_rev_growth_stability_lvl_252d(revenue: pd.Series) -> pd.Series:
    """revg_073_rev_growth_stability_lvl_252d"""
    base = _rolling_std(_pct_change(revenue, 21), 63)
    return _rolling_mean(base, 252)

def revg_074_rev_growth_stability_zscore_252d(revenue: pd.Series) -> pd.Series:
    """revg_074_rev_growth_stability_zscore_252d"""
    base = _rolling_std(_pct_change(revenue, 21), 63)
    return _zscore_rolling(base, 252)

def revg_075_rev_growth_stability_rank_252d(revenue: pd.Series) -> pd.Series:
    """revg_075_rev_growth_stability_rank_252d"""
    base = _rolling_std(_pct_change(revenue, 21), 63)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V45_REGISTRY = {
    "revg_001_rev_yoy_lvl_5d": {"inputs": ['revenue'], "func": revg_001_rev_yoy_lvl_5d},
    "revg_002_rev_yoy_zscore_5d": {"inputs": ['revenue'], "func": revg_002_rev_yoy_zscore_5d},
    "revg_003_rev_yoy_rank_5d": {"inputs": ['revenue'], "func": revg_003_rev_yoy_rank_5d},
    "revg_004_rev_yoy_lvl_21d": {"inputs": ['revenue'], "func": revg_004_rev_yoy_lvl_21d},
    "revg_005_rev_yoy_zscore_21d": {"inputs": ['revenue'], "func": revg_005_rev_yoy_zscore_21d},
    "revg_006_rev_yoy_rank_21d": {"inputs": ['revenue'], "func": revg_006_rev_yoy_rank_21d},
    "revg_007_rev_yoy_lvl_63d": {"inputs": ['revenue'], "func": revg_007_rev_yoy_lvl_63d},
    "revg_008_rev_yoy_zscore_63d": {"inputs": ['revenue'], "func": revg_008_rev_yoy_zscore_63d},
    "revg_009_rev_yoy_rank_63d": {"inputs": ['revenue'], "func": revg_009_rev_yoy_rank_63d},
    "revg_010_rev_yoy_lvl_126d": {"inputs": ['revenue'], "func": revg_010_rev_yoy_lvl_126d},
    "revg_011_rev_yoy_zscore_126d": {"inputs": ['revenue'], "func": revg_011_rev_yoy_zscore_126d},
    "revg_012_rev_yoy_rank_126d": {"inputs": ['revenue'], "func": revg_012_rev_yoy_rank_126d},
    "revg_013_rev_yoy_lvl_252d": {"inputs": ['revenue'], "func": revg_013_rev_yoy_lvl_252d},
    "revg_014_rev_yoy_zscore_252d": {"inputs": ['revenue'], "func": revg_014_rev_yoy_zscore_252d},
    "revg_015_rev_yoy_rank_252d": {"inputs": ['revenue'], "func": revg_015_rev_yoy_rank_252d},
    "revg_016_rev_qoq_lvl_5d": {"inputs": ['revenue'], "func": revg_016_rev_qoq_lvl_5d},
    "revg_017_rev_qoq_zscore_5d": {"inputs": ['revenue'], "func": revg_017_rev_qoq_zscore_5d},
    "revg_018_rev_qoq_rank_5d": {"inputs": ['revenue'], "func": revg_018_rev_qoq_rank_5d},
    "revg_019_rev_qoq_lvl_21d": {"inputs": ['revenue'], "func": revg_019_rev_qoq_lvl_21d},
    "revg_020_rev_qoq_zscore_21d": {"inputs": ['revenue'], "func": revg_020_rev_qoq_zscore_21d},
    "revg_021_rev_qoq_rank_21d": {"inputs": ['revenue'], "func": revg_021_rev_qoq_rank_21d},
    "revg_022_rev_qoq_lvl_63d": {"inputs": ['revenue'], "func": revg_022_rev_qoq_lvl_63d},
    "revg_023_rev_qoq_zscore_63d": {"inputs": ['revenue'], "func": revg_023_rev_qoq_zscore_63d},
    "revg_024_rev_qoq_rank_63d": {"inputs": ['revenue'], "func": revg_024_rev_qoq_rank_63d},
    "revg_025_rev_qoq_lvl_126d": {"inputs": ['revenue'], "func": revg_025_rev_qoq_lvl_126d},
    "revg_026_rev_qoq_zscore_126d": {"inputs": ['revenue'], "func": revg_026_rev_qoq_zscore_126d},
    "revg_027_rev_qoq_rank_126d": {"inputs": ['revenue'], "func": revg_027_rev_qoq_rank_126d},
    "revg_028_rev_qoq_lvl_252d": {"inputs": ['revenue'], "func": revg_028_rev_qoq_lvl_252d},
    "revg_029_rev_qoq_zscore_252d": {"inputs": ['revenue'], "func": revg_029_rev_qoq_zscore_252d},
    "revg_030_rev_qoq_rank_252d": {"inputs": ['revenue'], "func": revg_030_rev_qoq_rank_252d},
    "revg_031_rev_mom_lvl_5d": {"inputs": ['revenue'], "func": revg_031_rev_mom_lvl_5d},
    "revg_032_rev_mom_zscore_5d": {"inputs": ['revenue'], "func": revg_032_rev_mom_zscore_5d},
    "revg_033_rev_mom_rank_5d": {"inputs": ['revenue'], "func": revg_033_rev_mom_rank_5d},
    "revg_034_rev_mom_lvl_21d": {"inputs": ['revenue'], "func": revg_034_rev_mom_lvl_21d},
    "revg_035_rev_mom_zscore_21d": {"inputs": ['revenue'], "func": revg_035_rev_mom_zscore_21d},
    "revg_036_rev_mom_rank_21d": {"inputs": ['revenue'], "func": revg_036_rev_mom_rank_21d},
    "revg_037_rev_mom_lvl_63d": {"inputs": ['revenue'], "func": revg_037_rev_mom_lvl_63d},
    "revg_038_rev_mom_zscore_63d": {"inputs": ['revenue'], "func": revg_038_rev_mom_zscore_63d},
    "revg_039_rev_mom_rank_63d": {"inputs": ['revenue'], "func": revg_039_rev_mom_rank_63d},
    "revg_040_rev_mom_lvl_126d": {"inputs": ['revenue'], "func": revg_040_rev_mom_lvl_126d},
    "revg_041_rev_mom_zscore_126d": {"inputs": ['revenue'], "func": revg_041_rev_mom_zscore_126d},
    "revg_042_rev_mom_rank_126d": {"inputs": ['revenue'], "func": revg_042_rev_mom_rank_126d},
    "revg_043_rev_mom_lvl_252d": {"inputs": ['revenue'], "func": revg_043_rev_mom_lvl_252d},
    "revg_044_rev_mom_zscore_252d": {"inputs": ['revenue'], "func": revg_044_rev_mom_zscore_252d},
    "revg_045_rev_mom_rank_252d": {"inputs": ['revenue'], "func": revg_045_rev_mom_rank_252d},
    "revg_046_rev_growth_accel_lvl_5d": {"inputs": ['revenue'], "func": revg_046_rev_growth_accel_lvl_5d},
    "revg_047_rev_growth_accel_zscore_5d": {"inputs": ['revenue'], "func": revg_047_rev_growth_accel_zscore_5d},
    "revg_048_rev_growth_accel_rank_5d": {"inputs": ['revenue'], "func": revg_048_rev_growth_accel_rank_5d},
    "revg_049_rev_growth_accel_lvl_21d": {"inputs": ['revenue'], "func": revg_049_rev_growth_accel_lvl_21d},
    "revg_050_rev_growth_accel_zscore_21d": {"inputs": ['revenue'], "func": revg_050_rev_growth_accel_zscore_21d},
    "revg_051_rev_growth_accel_rank_21d": {"inputs": ['revenue'], "func": revg_051_rev_growth_accel_rank_21d},
    "revg_052_rev_growth_accel_lvl_63d": {"inputs": ['revenue'], "func": revg_052_rev_growth_accel_lvl_63d},
    "revg_053_rev_growth_accel_zscore_63d": {"inputs": ['revenue'], "func": revg_053_rev_growth_accel_zscore_63d},
    "revg_054_rev_growth_accel_rank_63d": {"inputs": ['revenue'], "func": revg_054_rev_growth_accel_rank_63d},
    "revg_055_rev_growth_accel_lvl_126d": {"inputs": ['revenue'], "func": revg_055_rev_growth_accel_lvl_126d},
    "revg_056_rev_growth_accel_zscore_126d": {"inputs": ['revenue'], "func": revg_056_rev_growth_accel_zscore_126d},
    "revg_057_rev_growth_accel_rank_126d": {"inputs": ['revenue'], "func": revg_057_rev_growth_accel_rank_126d},
    "revg_058_rev_growth_accel_lvl_252d": {"inputs": ['revenue'], "func": revg_058_rev_growth_accel_lvl_252d},
    "revg_059_rev_growth_accel_zscore_252d": {"inputs": ['revenue'], "func": revg_059_rev_growth_accel_zscore_252d},
    "revg_060_rev_growth_accel_rank_252d": {"inputs": ['revenue'], "func": revg_060_rev_growth_accel_rank_252d},
    "revg_061_rev_growth_stability_lvl_5d": {"inputs": ['revenue'], "func": revg_061_rev_growth_stability_lvl_5d},
    "revg_062_rev_growth_stability_zscore_5d": {"inputs": ['revenue'], "func": revg_062_rev_growth_stability_zscore_5d},
    "revg_063_rev_growth_stability_rank_5d": {"inputs": ['revenue'], "func": revg_063_rev_growth_stability_rank_5d},
    "revg_064_rev_growth_stability_lvl_21d": {"inputs": ['revenue'], "func": revg_064_rev_growth_stability_lvl_21d},
    "revg_065_rev_growth_stability_zscore_21d": {"inputs": ['revenue'], "func": revg_065_rev_growth_stability_zscore_21d},
    "revg_066_rev_growth_stability_rank_21d": {"inputs": ['revenue'], "func": revg_066_rev_growth_stability_rank_21d},
    "revg_067_rev_growth_stability_lvl_63d": {"inputs": ['revenue'], "func": revg_067_rev_growth_stability_lvl_63d},
    "revg_068_rev_growth_stability_zscore_63d": {"inputs": ['revenue'], "func": revg_068_rev_growth_stability_zscore_63d},
    "revg_069_rev_growth_stability_rank_63d": {"inputs": ['revenue'], "func": revg_069_rev_growth_stability_rank_63d},
    "revg_070_rev_growth_stability_lvl_126d": {"inputs": ['revenue'], "func": revg_070_rev_growth_stability_lvl_126d},
    "revg_071_rev_growth_stability_zscore_126d": {"inputs": ['revenue'], "func": revg_071_rev_growth_stability_zscore_126d},
    "revg_072_rev_growth_stability_rank_126d": {"inputs": ['revenue'], "func": revg_072_rev_growth_stability_rank_126d},
    "revg_073_rev_growth_stability_lvl_252d": {"inputs": ['revenue'], "func": revg_073_rev_growth_stability_lvl_252d},
    "revg_074_rev_growth_stability_zscore_252d": {"inputs": ['revenue'], "func": revg_074_rev_growth_stability_zscore_252d},
    "revg_075_rev_growth_stability_rank_252d": {"inputs": ['revenue'], "func": revg_075_rev_growth_stability_rank_252d},
}
