"""
50_dilution_rate — Base Features 001-075
Domain: dilution_rate
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

def dlrt_001_sharesbas_yoy_lvl_5d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_001_sharesbas_yoy_lvl_5d"""
    base = _pct_change(sharesbas, 252)
    return _rolling_mean(base, 5)

def dlrt_002_sharesbas_yoy_zscore_5d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_002_sharesbas_yoy_zscore_5d"""
    base = _pct_change(sharesbas, 252)
    return _zscore_rolling(base, 5)

def dlrt_003_sharesbas_yoy_rank_5d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_003_sharesbas_yoy_rank_5d"""
    base = _pct_change(sharesbas, 252)
    return _rank_pct(base, 5)

def dlrt_004_sharesbas_yoy_lvl_21d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_004_sharesbas_yoy_lvl_21d"""
    base = _pct_change(sharesbas, 252)
    return _rolling_mean(base, 21)

def dlrt_005_sharesbas_yoy_zscore_21d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_005_sharesbas_yoy_zscore_21d"""
    base = _pct_change(sharesbas, 252)
    return _zscore_rolling(base, 21)

def dlrt_006_sharesbas_yoy_rank_21d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_006_sharesbas_yoy_rank_21d"""
    base = _pct_change(sharesbas, 252)
    return _rank_pct(base, 21)

def dlrt_007_sharesbas_yoy_lvl_63d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_007_sharesbas_yoy_lvl_63d"""
    base = _pct_change(sharesbas, 252)
    return _rolling_mean(base, 63)

def dlrt_008_sharesbas_yoy_zscore_63d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_008_sharesbas_yoy_zscore_63d"""
    base = _pct_change(sharesbas, 252)
    return _zscore_rolling(base, 63)

def dlrt_009_sharesbas_yoy_rank_63d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_009_sharesbas_yoy_rank_63d"""
    base = _pct_change(sharesbas, 252)
    return _rank_pct(base, 63)

def dlrt_010_sharesbas_yoy_lvl_126d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_010_sharesbas_yoy_lvl_126d"""
    base = _pct_change(sharesbas, 252)
    return _rolling_mean(base, 126)

def dlrt_011_sharesbas_yoy_zscore_126d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_011_sharesbas_yoy_zscore_126d"""
    base = _pct_change(sharesbas, 252)
    return _zscore_rolling(base, 126)

def dlrt_012_sharesbas_yoy_rank_126d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_012_sharesbas_yoy_rank_126d"""
    base = _pct_change(sharesbas, 252)
    return _rank_pct(base, 126)

def dlrt_013_sharesbas_yoy_lvl_252d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_013_sharesbas_yoy_lvl_252d"""
    base = _pct_change(sharesbas, 252)
    return _rolling_mean(base, 252)

def dlrt_014_sharesbas_yoy_zscore_252d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_014_sharesbas_yoy_zscore_252d"""
    base = _pct_change(sharesbas, 252)
    return _zscore_rolling(base, 252)

def dlrt_015_sharesbas_yoy_rank_252d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_015_sharesbas_yoy_rank_252d"""
    base = _pct_change(sharesbas, 252)
    return _rank_pct(base, 252)

def dlrt_016_shareswa_yoy_lvl_5d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_016_shareswa_yoy_lvl_5d"""
    base = _pct_change(shareswa, 252)
    return _rolling_mean(base, 5)

def dlrt_017_shareswa_yoy_zscore_5d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_017_shareswa_yoy_zscore_5d"""
    base = _pct_change(shareswa, 252)
    return _zscore_rolling(base, 5)

def dlrt_018_shareswa_yoy_rank_5d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_018_shareswa_yoy_rank_5d"""
    base = _pct_change(shareswa, 252)
    return _rank_pct(base, 5)

def dlrt_019_shareswa_yoy_lvl_21d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_019_shareswa_yoy_lvl_21d"""
    base = _pct_change(shareswa, 252)
    return _rolling_mean(base, 21)

def dlrt_020_shareswa_yoy_zscore_21d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_020_shareswa_yoy_zscore_21d"""
    base = _pct_change(shareswa, 252)
    return _zscore_rolling(base, 21)

def dlrt_021_shareswa_yoy_rank_21d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_021_shareswa_yoy_rank_21d"""
    base = _pct_change(shareswa, 252)
    return _rank_pct(base, 21)

def dlrt_022_shareswa_yoy_lvl_63d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_022_shareswa_yoy_lvl_63d"""
    base = _pct_change(shareswa, 252)
    return _rolling_mean(base, 63)

def dlrt_023_shareswa_yoy_zscore_63d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_023_shareswa_yoy_zscore_63d"""
    base = _pct_change(shareswa, 252)
    return _zscore_rolling(base, 63)

def dlrt_024_shareswa_yoy_rank_63d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_024_shareswa_yoy_rank_63d"""
    base = _pct_change(shareswa, 252)
    return _rank_pct(base, 63)

def dlrt_025_shareswa_yoy_lvl_126d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_025_shareswa_yoy_lvl_126d"""
    base = _pct_change(shareswa, 252)
    return _rolling_mean(base, 126)

def dlrt_026_shareswa_yoy_zscore_126d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_026_shareswa_yoy_zscore_126d"""
    base = _pct_change(shareswa, 252)
    return _zscore_rolling(base, 126)

def dlrt_027_shareswa_yoy_rank_126d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_027_shareswa_yoy_rank_126d"""
    base = _pct_change(shareswa, 252)
    return _rank_pct(base, 126)

def dlrt_028_shareswa_yoy_lvl_252d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_028_shareswa_yoy_lvl_252d"""
    base = _pct_change(shareswa, 252)
    return _rolling_mean(base, 252)

def dlrt_029_shareswa_yoy_zscore_252d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_029_shareswa_yoy_zscore_252d"""
    base = _pct_change(shareswa, 252)
    return _zscore_rolling(base, 252)

def dlrt_030_shareswa_yoy_rank_252d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_030_shareswa_yoy_rank_252d"""
    base = _pct_change(shareswa, 252)
    return _rank_pct(base, 252)

def dlrt_031_sharesbas_qoq_lvl_5d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_031_sharesbas_qoq_lvl_5d"""
    base = _pct_change(sharesbas, 63)
    return _rolling_mean(base, 5)

def dlrt_032_sharesbas_qoq_zscore_5d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_032_sharesbas_qoq_zscore_5d"""
    base = _pct_change(sharesbas, 63)
    return _zscore_rolling(base, 5)

def dlrt_033_sharesbas_qoq_rank_5d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_033_sharesbas_qoq_rank_5d"""
    base = _pct_change(sharesbas, 63)
    return _rank_pct(base, 5)

def dlrt_034_sharesbas_qoq_lvl_21d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_034_sharesbas_qoq_lvl_21d"""
    base = _pct_change(sharesbas, 63)
    return _rolling_mean(base, 21)

def dlrt_035_sharesbas_qoq_zscore_21d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_035_sharesbas_qoq_zscore_21d"""
    base = _pct_change(sharesbas, 63)
    return _zscore_rolling(base, 21)

def dlrt_036_sharesbas_qoq_rank_21d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_036_sharesbas_qoq_rank_21d"""
    base = _pct_change(sharesbas, 63)
    return _rank_pct(base, 21)

def dlrt_037_sharesbas_qoq_lvl_63d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_037_sharesbas_qoq_lvl_63d"""
    base = _pct_change(sharesbas, 63)
    return _rolling_mean(base, 63)

def dlrt_038_sharesbas_qoq_zscore_63d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_038_sharesbas_qoq_zscore_63d"""
    base = _pct_change(sharesbas, 63)
    return _zscore_rolling(base, 63)

def dlrt_039_sharesbas_qoq_rank_63d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_039_sharesbas_qoq_rank_63d"""
    base = _pct_change(sharesbas, 63)
    return _rank_pct(base, 63)

def dlrt_040_sharesbas_qoq_lvl_126d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_040_sharesbas_qoq_lvl_126d"""
    base = _pct_change(sharesbas, 63)
    return _rolling_mean(base, 126)

def dlrt_041_sharesbas_qoq_zscore_126d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_041_sharesbas_qoq_zscore_126d"""
    base = _pct_change(sharesbas, 63)
    return _zscore_rolling(base, 126)

def dlrt_042_sharesbas_qoq_rank_126d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_042_sharesbas_qoq_rank_126d"""
    base = _pct_change(sharesbas, 63)
    return _rank_pct(base, 126)

def dlrt_043_sharesbas_qoq_lvl_252d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_043_sharesbas_qoq_lvl_252d"""
    base = _pct_change(sharesbas, 63)
    return _rolling_mean(base, 252)

def dlrt_044_sharesbas_qoq_zscore_252d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_044_sharesbas_qoq_zscore_252d"""
    base = _pct_change(sharesbas, 63)
    return _zscore_rolling(base, 252)

def dlrt_045_sharesbas_qoq_rank_252d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_045_sharesbas_qoq_rank_252d"""
    base = _pct_change(sharesbas, 63)
    return _rank_pct(base, 252)

def dlrt_046_shareswa_qoq_lvl_5d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_046_shareswa_qoq_lvl_5d"""
    base = _pct_change(shareswa, 63)
    return _rolling_mean(base, 5)

def dlrt_047_shareswa_qoq_zscore_5d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_047_shareswa_qoq_zscore_5d"""
    base = _pct_change(shareswa, 63)
    return _zscore_rolling(base, 5)

def dlrt_048_shareswa_qoq_rank_5d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_048_shareswa_qoq_rank_5d"""
    base = _pct_change(shareswa, 63)
    return _rank_pct(base, 5)

def dlrt_049_shareswa_qoq_lvl_21d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_049_shareswa_qoq_lvl_21d"""
    base = _pct_change(shareswa, 63)
    return _rolling_mean(base, 21)

def dlrt_050_shareswa_qoq_zscore_21d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_050_shareswa_qoq_zscore_21d"""
    base = _pct_change(shareswa, 63)
    return _zscore_rolling(base, 21)

def dlrt_051_shareswa_qoq_rank_21d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_051_shareswa_qoq_rank_21d"""
    base = _pct_change(shareswa, 63)
    return _rank_pct(base, 21)

def dlrt_052_shareswa_qoq_lvl_63d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_052_shareswa_qoq_lvl_63d"""
    base = _pct_change(shareswa, 63)
    return _rolling_mean(base, 63)

def dlrt_053_shareswa_qoq_zscore_63d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_053_shareswa_qoq_zscore_63d"""
    base = _pct_change(shareswa, 63)
    return _zscore_rolling(base, 63)

def dlrt_054_shareswa_qoq_rank_63d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_054_shareswa_qoq_rank_63d"""
    base = _pct_change(shareswa, 63)
    return _rank_pct(base, 63)

def dlrt_055_shareswa_qoq_lvl_126d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_055_shareswa_qoq_lvl_126d"""
    base = _pct_change(shareswa, 63)
    return _rolling_mean(base, 126)

def dlrt_056_shareswa_qoq_zscore_126d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_056_shareswa_qoq_zscore_126d"""
    base = _pct_change(shareswa, 63)
    return _zscore_rolling(base, 126)

def dlrt_057_shareswa_qoq_rank_126d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_057_shareswa_qoq_rank_126d"""
    base = _pct_change(shareswa, 63)
    return _rank_pct(base, 126)

def dlrt_058_shareswa_qoq_lvl_252d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_058_shareswa_qoq_lvl_252d"""
    base = _pct_change(shareswa, 63)
    return _rolling_mean(base, 252)

def dlrt_059_shareswa_qoq_zscore_252d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_059_shareswa_qoq_zscore_252d"""
    base = _pct_change(shareswa, 63)
    return _zscore_rolling(base, 252)

def dlrt_060_shareswa_qoq_rank_252d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_060_shareswa_qoq_rank_252d"""
    base = _pct_change(shareswa, 63)
    return _rank_pct(base, 252)

def dlrt_061_dilution_accel_lvl_5d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_061_dilution_accel_lvl_5d"""
    base = _pct_change(sharesbas, 252) - _pct_change(sharesbas, 252).shift(63)
    return _rolling_mean(base, 5)

def dlrt_062_dilution_accel_zscore_5d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_062_dilution_accel_zscore_5d"""
    base = _pct_change(sharesbas, 252) - _pct_change(sharesbas, 252).shift(63)
    return _zscore_rolling(base, 5)

def dlrt_063_dilution_accel_rank_5d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_063_dilution_accel_rank_5d"""
    base = _pct_change(sharesbas, 252) - _pct_change(sharesbas, 252).shift(63)
    return _rank_pct(base, 5)

def dlrt_064_dilution_accel_lvl_21d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_064_dilution_accel_lvl_21d"""
    base = _pct_change(sharesbas, 252) - _pct_change(sharesbas, 252).shift(63)
    return _rolling_mean(base, 21)

def dlrt_065_dilution_accel_zscore_21d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_065_dilution_accel_zscore_21d"""
    base = _pct_change(sharesbas, 252) - _pct_change(sharesbas, 252).shift(63)
    return _zscore_rolling(base, 21)

def dlrt_066_dilution_accel_rank_21d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_066_dilution_accel_rank_21d"""
    base = _pct_change(sharesbas, 252) - _pct_change(sharesbas, 252).shift(63)
    return _rank_pct(base, 21)

def dlrt_067_dilution_accel_lvl_63d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_067_dilution_accel_lvl_63d"""
    base = _pct_change(sharesbas, 252) - _pct_change(sharesbas, 252).shift(63)
    return _rolling_mean(base, 63)

def dlrt_068_dilution_accel_zscore_63d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_068_dilution_accel_zscore_63d"""
    base = _pct_change(sharesbas, 252) - _pct_change(sharesbas, 252).shift(63)
    return _zscore_rolling(base, 63)

def dlrt_069_dilution_accel_rank_63d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_069_dilution_accel_rank_63d"""
    base = _pct_change(sharesbas, 252) - _pct_change(sharesbas, 252).shift(63)
    return _rank_pct(base, 63)

def dlrt_070_dilution_accel_lvl_126d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_070_dilution_accel_lvl_126d"""
    base = _pct_change(sharesbas, 252) - _pct_change(sharesbas, 252).shift(63)
    return _rolling_mean(base, 126)

def dlrt_071_dilution_accel_zscore_126d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_071_dilution_accel_zscore_126d"""
    base = _pct_change(sharesbas, 252) - _pct_change(sharesbas, 252).shift(63)
    return _zscore_rolling(base, 126)

def dlrt_072_dilution_accel_rank_126d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_072_dilution_accel_rank_126d"""
    base = _pct_change(sharesbas, 252) - _pct_change(sharesbas, 252).shift(63)
    return _rank_pct(base, 126)

def dlrt_073_dilution_accel_lvl_252d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_073_dilution_accel_lvl_252d"""
    base = _pct_change(sharesbas, 252) - _pct_change(sharesbas, 252).shift(63)
    return _rolling_mean(base, 252)

def dlrt_074_dilution_accel_zscore_252d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_074_dilution_accel_zscore_252d"""
    base = _pct_change(sharesbas, 252) - _pct_change(sharesbas, 252).shift(63)
    return _zscore_rolling(base, 252)

def dlrt_075_dilution_accel_rank_252d(sharesbas: pd.Series, shareswa: pd.Series) -> pd.Series:
    """dlrt_075_dilution_accel_rank_252d"""
    base = _pct_change(sharesbas, 252) - _pct_change(sharesbas, 252).shift(63)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V50_REGISTRY = {
    "dlrt_001_sharesbas_yoy_lvl_5d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_001_sharesbas_yoy_lvl_5d},
    "dlrt_002_sharesbas_yoy_zscore_5d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_002_sharesbas_yoy_zscore_5d},
    "dlrt_003_sharesbas_yoy_rank_5d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_003_sharesbas_yoy_rank_5d},
    "dlrt_004_sharesbas_yoy_lvl_21d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_004_sharesbas_yoy_lvl_21d},
    "dlrt_005_sharesbas_yoy_zscore_21d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_005_sharesbas_yoy_zscore_21d},
    "dlrt_006_sharesbas_yoy_rank_21d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_006_sharesbas_yoy_rank_21d},
    "dlrt_007_sharesbas_yoy_lvl_63d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_007_sharesbas_yoy_lvl_63d},
    "dlrt_008_sharesbas_yoy_zscore_63d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_008_sharesbas_yoy_zscore_63d},
    "dlrt_009_sharesbas_yoy_rank_63d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_009_sharesbas_yoy_rank_63d},
    "dlrt_010_sharesbas_yoy_lvl_126d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_010_sharesbas_yoy_lvl_126d},
    "dlrt_011_sharesbas_yoy_zscore_126d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_011_sharesbas_yoy_zscore_126d},
    "dlrt_012_sharesbas_yoy_rank_126d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_012_sharesbas_yoy_rank_126d},
    "dlrt_013_sharesbas_yoy_lvl_252d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_013_sharesbas_yoy_lvl_252d},
    "dlrt_014_sharesbas_yoy_zscore_252d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_014_sharesbas_yoy_zscore_252d},
    "dlrt_015_sharesbas_yoy_rank_252d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_015_sharesbas_yoy_rank_252d},
    "dlrt_016_shareswa_yoy_lvl_5d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_016_shareswa_yoy_lvl_5d},
    "dlrt_017_shareswa_yoy_zscore_5d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_017_shareswa_yoy_zscore_5d},
    "dlrt_018_shareswa_yoy_rank_5d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_018_shareswa_yoy_rank_5d},
    "dlrt_019_shareswa_yoy_lvl_21d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_019_shareswa_yoy_lvl_21d},
    "dlrt_020_shareswa_yoy_zscore_21d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_020_shareswa_yoy_zscore_21d},
    "dlrt_021_shareswa_yoy_rank_21d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_021_shareswa_yoy_rank_21d},
    "dlrt_022_shareswa_yoy_lvl_63d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_022_shareswa_yoy_lvl_63d},
    "dlrt_023_shareswa_yoy_zscore_63d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_023_shareswa_yoy_zscore_63d},
    "dlrt_024_shareswa_yoy_rank_63d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_024_shareswa_yoy_rank_63d},
    "dlrt_025_shareswa_yoy_lvl_126d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_025_shareswa_yoy_lvl_126d},
    "dlrt_026_shareswa_yoy_zscore_126d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_026_shareswa_yoy_zscore_126d},
    "dlrt_027_shareswa_yoy_rank_126d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_027_shareswa_yoy_rank_126d},
    "dlrt_028_shareswa_yoy_lvl_252d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_028_shareswa_yoy_lvl_252d},
    "dlrt_029_shareswa_yoy_zscore_252d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_029_shareswa_yoy_zscore_252d},
    "dlrt_030_shareswa_yoy_rank_252d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_030_shareswa_yoy_rank_252d},
    "dlrt_031_sharesbas_qoq_lvl_5d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_031_sharesbas_qoq_lvl_5d},
    "dlrt_032_sharesbas_qoq_zscore_5d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_032_sharesbas_qoq_zscore_5d},
    "dlrt_033_sharesbas_qoq_rank_5d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_033_sharesbas_qoq_rank_5d},
    "dlrt_034_sharesbas_qoq_lvl_21d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_034_sharesbas_qoq_lvl_21d},
    "dlrt_035_sharesbas_qoq_zscore_21d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_035_sharesbas_qoq_zscore_21d},
    "dlrt_036_sharesbas_qoq_rank_21d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_036_sharesbas_qoq_rank_21d},
    "dlrt_037_sharesbas_qoq_lvl_63d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_037_sharesbas_qoq_lvl_63d},
    "dlrt_038_sharesbas_qoq_zscore_63d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_038_sharesbas_qoq_zscore_63d},
    "dlrt_039_sharesbas_qoq_rank_63d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_039_sharesbas_qoq_rank_63d},
    "dlrt_040_sharesbas_qoq_lvl_126d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_040_sharesbas_qoq_lvl_126d},
    "dlrt_041_sharesbas_qoq_zscore_126d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_041_sharesbas_qoq_zscore_126d},
    "dlrt_042_sharesbas_qoq_rank_126d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_042_sharesbas_qoq_rank_126d},
    "dlrt_043_sharesbas_qoq_lvl_252d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_043_sharesbas_qoq_lvl_252d},
    "dlrt_044_sharesbas_qoq_zscore_252d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_044_sharesbas_qoq_zscore_252d},
    "dlrt_045_sharesbas_qoq_rank_252d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_045_sharesbas_qoq_rank_252d},
    "dlrt_046_shareswa_qoq_lvl_5d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_046_shareswa_qoq_lvl_5d},
    "dlrt_047_shareswa_qoq_zscore_5d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_047_shareswa_qoq_zscore_5d},
    "dlrt_048_shareswa_qoq_rank_5d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_048_shareswa_qoq_rank_5d},
    "dlrt_049_shareswa_qoq_lvl_21d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_049_shareswa_qoq_lvl_21d},
    "dlrt_050_shareswa_qoq_zscore_21d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_050_shareswa_qoq_zscore_21d},
    "dlrt_051_shareswa_qoq_rank_21d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_051_shareswa_qoq_rank_21d},
    "dlrt_052_shareswa_qoq_lvl_63d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_052_shareswa_qoq_lvl_63d},
    "dlrt_053_shareswa_qoq_zscore_63d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_053_shareswa_qoq_zscore_63d},
    "dlrt_054_shareswa_qoq_rank_63d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_054_shareswa_qoq_rank_63d},
    "dlrt_055_shareswa_qoq_lvl_126d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_055_shareswa_qoq_lvl_126d},
    "dlrt_056_shareswa_qoq_zscore_126d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_056_shareswa_qoq_zscore_126d},
    "dlrt_057_shareswa_qoq_rank_126d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_057_shareswa_qoq_rank_126d},
    "dlrt_058_shareswa_qoq_lvl_252d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_058_shareswa_qoq_lvl_252d},
    "dlrt_059_shareswa_qoq_zscore_252d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_059_shareswa_qoq_zscore_252d},
    "dlrt_060_shareswa_qoq_rank_252d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_060_shareswa_qoq_rank_252d},
    "dlrt_061_dilution_accel_lvl_5d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_061_dilution_accel_lvl_5d},
    "dlrt_062_dilution_accel_zscore_5d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_062_dilution_accel_zscore_5d},
    "dlrt_063_dilution_accel_rank_5d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_063_dilution_accel_rank_5d},
    "dlrt_064_dilution_accel_lvl_21d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_064_dilution_accel_lvl_21d},
    "dlrt_065_dilution_accel_zscore_21d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_065_dilution_accel_zscore_21d},
    "dlrt_066_dilution_accel_rank_21d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_066_dilution_accel_rank_21d},
    "dlrt_067_dilution_accel_lvl_63d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_067_dilution_accel_lvl_63d},
    "dlrt_068_dilution_accel_zscore_63d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_068_dilution_accel_zscore_63d},
    "dlrt_069_dilution_accel_rank_63d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_069_dilution_accel_rank_63d},
    "dlrt_070_dilution_accel_lvl_126d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_070_dilution_accel_lvl_126d},
    "dlrt_071_dilution_accel_zscore_126d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_071_dilution_accel_zscore_126d},
    "dlrt_072_dilution_accel_rank_126d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_072_dilution_accel_rank_126d},
    "dlrt_073_dilution_accel_lvl_252d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_073_dilution_accel_lvl_252d},
    "dlrt_074_dilution_accel_zscore_252d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_074_dilution_accel_zscore_252d},
    "dlrt_075_dilution_accel_rank_252d": {"inputs": ['sharesbas', 'shareswa'], "func": dlrt_075_dilution_accel_rank_252d},
}
