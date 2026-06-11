"""
53_revenue_acceleration — Base Features 001-075
Domain: revenue_acceleration
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

def reva_001_rev_growth_252_lvl_5d(revenue: pd.Series) -> pd.Series:
    """reva_001_rev_growth_252_lvl_5d"""
    base = revenue.pct_change(252)
    return _rolling_mean(base, 5)

def reva_002_rev_growth_252_zscore_5d(revenue: pd.Series) -> pd.Series:
    """reva_002_rev_growth_252_zscore_5d"""
    base = revenue.pct_change(252)
    return _zscore_rolling(base, 5)

def reva_003_rev_growth_252_rank_5d(revenue: pd.Series) -> pd.Series:
    """reva_003_rev_growth_252_rank_5d"""
    base = revenue.pct_change(252)
    return _rank_pct(base, 5)

def reva_004_rev_growth_252_lvl_21d(revenue: pd.Series) -> pd.Series:
    """reva_004_rev_growth_252_lvl_21d"""
    base = revenue.pct_change(252)
    return _rolling_mean(base, 21)

def reva_005_rev_growth_252_zscore_21d(revenue: pd.Series) -> pd.Series:
    """reva_005_rev_growth_252_zscore_21d"""
    base = revenue.pct_change(252)
    return _zscore_rolling(base, 21)

def reva_006_rev_growth_252_rank_21d(revenue: pd.Series) -> pd.Series:
    """reva_006_rev_growth_252_rank_21d"""
    base = revenue.pct_change(252)
    return _rank_pct(base, 21)

def reva_007_rev_growth_252_lvl_63d(revenue: pd.Series) -> pd.Series:
    """reva_007_rev_growth_252_lvl_63d"""
    base = revenue.pct_change(252)
    return _rolling_mean(base, 63)

def reva_008_rev_growth_252_zscore_63d(revenue: pd.Series) -> pd.Series:
    """reva_008_rev_growth_252_zscore_63d"""
    base = revenue.pct_change(252)
    return _zscore_rolling(base, 63)

def reva_009_rev_growth_252_rank_63d(revenue: pd.Series) -> pd.Series:
    """reva_009_rev_growth_252_rank_63d"""
    base = revenue.pct_change(252)
    return _rank_pct(base, 63)

def reva_010_rev_growth_252_lvl_126d(revenue: pd.Series) -> pd.Series:
    """reva_010_rev_growth_252_lvl_126d"""
    base = revenue.pct_change(252)
    return _rolling_mean(base, 126)

def reva_011_rev_growth_252_zscore_126d(revenue: pd.Series) -> pd.Series:
    """reva_011_rev_growth_252_zscore_126d"""
    base = revenue.pct_change(252)
    return _zscore_rolling(base, 126)

def reva_012_rev_growth_252_rank_126d(revenue: pd.Series) -> pd.Series:
    """reva_012_rev_growth_252_rank_126d"""
    base = revenue.pct_change(252)
    return _rank_pct(base, 126)

def reva_013_rev_growth_252_lvl_252d(revenue: pd.Series) -> pd.Series:
    """reva_013_rev_growth_252_lvl_252d"""
    base = revenue.pct_change(252)
    return _rolling_mean(base, 252)

def reva_014_rev_growth_252_zscore_252d(revenue: pd.Series) -> pd.Series:
    """reva_014_rev_growth_252_zscore_252d"""
    base = revenue.pct_change(252)
    return _zscore_rolling(base, 252)

def reva_015_rev_growth_252_rank_252d(revenue: pd.Series) -> pd.Series:
    """reva_015_rev_growth_252_rank_252d"""
    base = revenue.pct_change(252)
    return _rank_pct(base, 252)

def reva_016_rev_growth_126_lvl_5d(revenue: pd.Series) -> pd.Series:
    """reva_016_rev_growth_126_lvl_5d"""
    base = revenue.pct_change(126)
    return _rolling_mean(base, 5)

def reva_017_rev_growth_126_zscore_5d(revenue: pd.Series) -> pd.Series:
    """reva_017_rev_growth_126_zscore_5d"""
    base = revenue.pct_change(126)
    return _zscore_rolling(base, 5)

def reva_018_rev_growth_126_rank_5d(revenue: pd.Series) -> pd.Series:
    """reva_018_rev_growth_126_rank_5d"""
    base = revenue.pct_change(126)
    return _rank_pct(base, 5)

def reva_019_rev_growth_126_lvl_21d(revenue: pd.Series) -> pd.Series:
    """reva_019_rev_growth_126_lvl_21d"""
    base = revenue.pct_change(126)
    return _rolling_mean(base, 21)

def reva_020_rev_growth_126_zscore_21d(revenue: pd.Series) -> pd.Series:
    """reva_020_rev_growth_126_zscore_21d"""
    base = revenue.pct_change(126)
    return _zscore_rolling(base, 21)

def reva_021_rev_growth_126_rank_21d(revenue: pd.Series) -> pd.Series:
    """reva_021_rev_growth_126_rank_21d"""
    base = revenue.pct_change(126)
    return _rank_pct(base, 21)

def reva_022_rev_growth_126_lvl_63d(revenue: pd.Series) -> pd.Series:
    """reva_022_rev_growth_126_lvl_63d"""
    base = revenue.pct_change(126)
    return _rolling_mean(base, 63)

def reva_023_rev_growth_126_zscore_63d(revenue: pd.Series) -> pd.Series:
    """reva_023_rev_growth_126_zscore_63d"""
    base = revenue.pct_change(126)
    return _zscore_rolling(base, 63)

def reva_024_rev_growth_126_rank_63d(revenue: pd.Series) -> pd.Series:
    """reva_024_rev_growth_126_rank_63d"""
    base = revenue.pct_change(126)
    return _rank_pct(base, 63)

def reva_025_rev_growth_126_lvl_126d(revenue: pd.Series) -> pd.Series:
    """reva_025_rev_growth_126_lvl_126d"""
    base = revenue.pct_change(126)
    return _rolling_mean(base, 126)

def reva_026_rev_growth_126_zscore_126d(revenue: pd.Series) -> pd.Series:
    """reva_026_rev_growth_126_zscore_126d"""
    base = revenue.pct_change(126)
    return _zscore_rolling(base, 126)

def reva_027_rev_growth_126_rank_126d(revenue: pd.Series) -> pd.Series:
    """reva_027_rev_growth_126_rank_126d"""
    base = revenue.pct_change(126)
    return _rank_pct(base, 126)

def reva_028_rev_growth_126_lvl_252d(revenue: pd.Series) -> pd.Series:
    """reva_028_rev_growth_126_lvl_252d"""
    base = revenue.pct_change(126)
    return _rolling_mean(base, 252)

def reva_029_rev_growth_126_zscore_252d(revenue: pd.Series) -> pd.Series:
    """reva_029_rev_growth_126_zscore_252d"""
    base = revenue.pct_change(126)
    return _zscore_rolling(base, 252)

def reva_030_rev_growth_126_rank_252d(revenue: pd.Series) -> pd.Series:
    """reva_030_rev_growth_126_rank_252d"""
    base = revenue.pct_change(126)
    return _rank_pct(base, 252)

def reva_031_rev_growth_63_lvl_5d(revenue: pd.Series) -> pd.Series:
    """reva_031_rev_growth_63_lvl_5d"""
    base = revenue.pct_change(63)
    return _rolling_mean(base, 5)

def reva_032_rev_growth_63_zscore_5d(revenue: pd.Series) -> pd.Series:
    """reva_032_rev_growth_63_zscore_5d"""
    base = revenue.pct_change(63)
    return _zscore_rolling(base, 5)

def reva_033_rev_growth_63_rank_5d(revenue: pd.Series) -> pd.Series:
    """reva_033_rev_growth_63_rank_5d"""
    base = revenue.pct_change(63)
    return _rank_pct(base, 5)

def reva_034_rev_growth_63_lvl_21d(revenue: pd.Series) -> pd.Series:
    """reva_034_rev_growth_63_lvl_21d"""
    base = revenue.pct_change(63)
    return _rolling_mean(base, 21)

def reva_035_rev_growth_63_zscore_21d(revenue: pd.Series) -> pd.Series:
    """reva_035_rev_growth_63_zscore_21d"""
    base = revenue.pct_change(63)
    return _zscore_rolling(base, 21)

def reva_036_rev_growth_63_rank_21d(revenue: pd.Series) -> pd.Series:
    """reva_036_rev_growth_63_rank_21d"""
    base = revenue.pct_change(63)
    return _rank_pct(base, 21)

def reva_037_rev_growth_63_lvl_63d(revenue: pd.Series) -> pd.Series:
    """reva_037_rev_growth_63_lvl_63d"""
    base = revenue.pct_change(63)
    return _rolling_mean(base, 63)

def reva_038_rev_growth_63_zscore_63d(revenue: pd.Series) -> pd.Series:
    """reva_038_rev_growth_63_zscore_63d"""
    base = revenue.pct_change(63)
    return _zscore_rolling(base, 63)

def reva_039_rev_growth_63_rank_63d(revenue: pd.Series) -> pd.Series:
    """reva_039_rev_growth_63_rank_63d"""
    base = revenue.pct_change(63)
    return _rank_pct(base, 63)

def reva_040_rev_growth_63_lvl_126d(revenue: pd.Series) -> pd.Series:
    """reva_040_rev_growth_63_lvl_126d"""
    base = revenue.pct_change(63)
    return _rolling_mean(base, 126)

def reva_041_rev_growth_63_zscore_126d(revenue: pd.Series) -> pd.Series:
    """reva_041_rev_growth_63_zscore_126d"""
    base = revenue.pct_change(63)
    return _zscore_rolling(base, 126)

def reva_042_rev_growth_63_rank_126d(revenue: pd.Series) -> pd.Series:
    """reva_042_rev_growth_63_rank_126d"""
    base = revenue.pct_change(63)
    return _rank_pct(base, 126)

def reva_043_rev_growth_63_lvl_252d(revenue: pd.Series) -> pd.Series:
    """reva_043_rev_growth_63_lvl_252d"""
    base = revenue.pct_change(63)
    return _rolling_mean(base, 252)

def reva_044_rev_growth_63_zscore_252d(revenue: pd.Series) -> pd.Series:
    """reva_044_rev_growth_63_zscore_252d"""
    base = revenue.pct_change(63)
    return _zscore_rolling(base, 252)

def reva_045_rev_growth_63_rank_252d(revenue: pd.Series) -> pd.Series:
    """reva_045_rev_growth_63_rank_252d"""
    base = revenue.pct_change(63)
    return _rank_pct(base, 252)

def reva_046_rev_growth_21_lvl_5d(revenue: pd.Series) -> pd.Series:
    """reva_046_rev_growth_21_lvl_5d"""
    base = revenue.pct_change(21)
    return _rolling_mean(base, 5)

def reva_047_rev_growth_21_zscore_5d(revenue: pd.Series) -> pd.Series:
    """reva_047_rev_growth_21_zscore_5d"""
    base = revenue.pct_change(21)
    return _zscore_rolling(base, 5)

def reva_048_rev_growth_21_rank_5d(revenue: pd.Series) -> pd.Series:
    """reva_048_rev_growth_21_rank_5d"""
    base = revenue.pct_change(21)
    return _rank_pct(base, 5)

def reva_049_rev_growth_21_lvl_21d(revenue: pd.Series) -> pd.Series:
    """reva_049_rev_growth_21_lvl_21d"""
    base = revenue.pct_change(21)
    return _rolling_mean(base, 21)

def reva_050_rev_growth_21_zscore_21d(revenue: pd.Series) -> pd.Series:
    """reva_050_rev_growth_21_zscore_21d"""
    base = revenue.pct_change(21)
    return _zscore_rolling(base, 21)

def reva_051_rev_growth_21_rank_21d(revenue: pd.Series) -> pd.Series:
    """reva_051_rev_growth_21_rank_21d"""
    base = revenue.pct_change(21)
    return _rank_pct(base, 21)

def reva_052_rev_growth_21_lvl_63d(revenue: pd.Series) -> pd.Series:
    """reva_052_rev_growth_21_lvl_63d"""
    base = revenue.pct_change(21)
    return _rolling_mean(base, 63)

def reva_053_rev_growth_21_zscore_63d(revenue: pd.Series) -> pd.Series:
    """reva_053_rev_growth_21_zscore_63d"""
    base = revenue.pct_change(21)
    return _zscore_rolling(base, 63)

def reva_054_rev_growth_21_rank_63d(revenue: pd.Series) -> pd.Series:
    """reva_054_rev_growth_21_rank_63d"""
    base = revenue.pct_change(21)
    return _rank_pct(base, 63)

def reva_055_rev_growth_21_lvl_126d(revenue: pd.Series) -> pd.Series:
    """reva_055_rev_growth_21_lvl_126d"""
    base = revenue.pct_change(21)
    return _rolling_mean(base, 126)

def reva_056_rev_growth_21_zscore_126d(revenue: pd.Series) -> pd.Series:
    """reva_056_rev_growth_21_zscore_126d"""
    base = revenue.pct_change(21)
    return _zscore_rolling(base, 126)

def reva_057_rev_growth_21_rank_126d(revenue: pd.Series) -> pd.Series:
    """reva_057_rev_growth_21_rank_126d"""
    base = revenue.pct_change(21)
    return _rank_pct(base, 126)

def reva_058_rev_growth_21_lvl_252d(revenue: pd.Series) -> pd.Series:
    """reva_058_rev_growth_21_lvl_252d"""
    base = revenue.pct_change(21)
    return _rolling_mean(base, 252)

def reva_059_rev_growth_21_zscore_252d(revenue: pd.Series) -> pd.Series:
    """reva_059_rev_growth_21_zscore_252d"""
    base = revenue.pct_change(21)
    return _zscore_rolling(base, 252)

def reva_060_rev_growth_21_rank_252d(revenue: pd.Series) -> pd.Series:
    """reva_060_rev_growth_21_rank_252d"""
    base = revenue.pct_change(21)
    return _rank_pct(base, 252)

def reva_061_rev_growth_5_lvl_5d(revenue: pd.Series) -> pd.Series:
    """reva_061_rev_growth_5_lvl_5d"""
    base = revenue.pct_change(5)
    return _rolling_mean(base, 5)

def reva_062_rev_growth_5_zscore_5d(revenue: pd.Series) -> pd.Series:
    """reva_062_rev_growth_5_zscore_5d"""
    base = revenue.pct_change(5)
    return _zscore_rolling(base, 5)

def reva_063_rev_growth_5_rank_5d(revenue: pd.Series) -> pd.Series:
    """reva_063_rev_growth_5_rank_5d"""
    base = revenue.pct_change(5)
    return _rank_pct(base, 5)

def reva_064_rev_growth_5_lvl_21d(revenue: pd.Series) -> pd.Series:
    """reva_064_rev_growth_5_lvl_21d"""
    base = revenue.pct_change(5)
    return _rolling_mean(base, 21)

def reva_065_rev_growth_5_zscore_21d(revenue: pd.Series) -> pd.Series:
    """reva_065_rev_growth_5_zscore_21d"""
    base = revenue.pct_change(5)
    return _zscore_rolling(base, 21)

def reva_066_rev_growth_5_rank_21d(revenue: pd.Series) -> pd.Series:
    """reva_066_rev_growth_5_rank_21d"""
    base = revenue.pct_change(5)
    return _rank_pct(base, 21)

def reva_067_rev_growth_5_lvl_63d(revenue: pd.Series) -> pd.Series:
    """reva_067_rev_growth_5_lvl_63d"""
    base = revenue.pct_change(5)
    return _rolling_mean(base, 63)

def reva_068_rev_growth_5_zscore_63d(revenue: pd.Series) -> pd.Series:
    """reva_068_rev_growth_5_zscore_63d"""
    base = revenue.pct_change(5)
    return _zscore_rolling(base, 63)

def reva_069_rev_growth_5_rank_63d(revenue: pd.Series) -> pd.Series:
    """reva_069_rev_growth_5_rank_63d"""
    base = revenue.pct_change(5)
    return _rank_pct(base, 63)

def reva_070_rev_growth_5_lvl_126d(revenue: pd.Series) -> pd.Series:
    """reva_070_rev_growth_5_lvl_126d"""
    base = revenue.pct_change(5)
    return _rolling_mean(base, 126)

def reva_071_rev_growth_5_zscore_126d(revenue: pd.Series) -> pd.Series:
    """reva_071_rev_growth_5_zscore_126d"""
    base = revenue.pct_change(5)
    return _zscore_rolling(base, 126)

def reva_072_rev_growth_5_rank_126d(revenue: pd.Series) -> pd.Series:
    """reva_072_rev_growth_5_rank_126d"""
    base = revenue.pct_change(5)
    return _rank_pct(base, 126)

def reva_073_rev_growth_5_lvl_252d(revenue: pd.Series) -> pd.Series:
    """reva_073_rev_growth_5_lvl_252d"""
    base = revenue.pct_change(5)
    return _rolling_mean(base, 252)

def reva_074_rev_growth_5_zscore_252d(revenue: pd.Series) -> pd.Series:
    """reva_074_rev_growth_5_zscore_252d"""
    base = revenue.pct_change(5)
    return _zscore_rolling(base, 252)

def reva_075_rev_growth_5_rank_252d(revenue: pd.Series) -> pd.Series:
    """reva_075_rev_growth_5_rank_252d"""
    base = revenue.pct_change(5)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V53_REGISTRY = {
    "reva_001_rev_growth_252_lvl_5d": {"inputs": ["revenue"], "func": reva_001_rev_growth_252_lvl_5d},
    "reva_002_rev_growth_252_zscore_5d": {"inputs": ["revenue"], "func": reva_002_rev_growth_252_zscore_5d},
    "reva_003_rev_growth_252_rank_5d": {"inputs": ["revenue"], "func": reva_003_rev_growth_252_rank_5d},
    "reva_004_rev_growth_252_lvl_21d": {"inputs": ["revenue"], "func": reva_004_rev_growth_252_lvl_21d},
    "reva_005_rev_growth_252_zscore_21d": {"inputs": ["revenue"], "func": reva_005_rev_growth_252_zscore_21d},
    "reva_006_rev_growth_252_rank_21d": {"inputs": ["revenue"], "func": reva_006_rev_growth_252_rank_21d},
    "reva_007_rev_growth_252_lvl_63d": {"inputs": ["revenue"], "func": reva_007_rev_growth_252_lvl_63d},
    "reva_008_rev_growth_252_zscore_63d": {"inputs": ["revenue"], "func": reva_008_rev_growth_252_zscore_63d},
    "reva_009_rev_growth_252_rank_63d": {"inputs": ["revenue"], "func": reva_009_rev_growth_252_rank_63d},
    "reva_010_rev_growth_252_lvl_126d": {"inputs": ["revenue"], "func": reva_010_rev_growth_252_lvl_126d},
    "reva_011_rev_growth_252_zscore_126d": {"inputs": ["revenue"], "func": reva_011_rev_growth_252_zscore_126d},
    "reva_012_rev_growth_252_rank_126d": {"inputs": ["revenue"], "func": reva_012_rev_growth_252_rank_126d},
    "reva_013_rev_growth_252_lvl_252d": {"inputs": ["revenue"], "func": reva_013_rev_growth_252_lvl_252d},
    "reva_014_rev_growth_252_zscore_252d": {"inputs": ["revenue"], "func": reva_014_rev_growth_252_zscore_252d},
    "reva_015_rev_growth_252_rank_252d": {"inputs": ["revenue"], "func": reva_015_rev_growth_252_rank_252d},
    "reva_016_rev_growth_126_lvl_5d": {"inputs": ["revenue"], "func": reva_016_rev_growth_126_lvl_5d},
    "reva_017_rev_growth_126_zscore_5d": {"inputs": ["revenue"], "func": reva_017_rev_growth_126_zscore_5d},
    "reva_018_rev_growth_126_rank_5d": {"inputs": ["revenue"], "func": reva_018_rev_growth_126_rank_5d},
    "reva_019_rev_growth_126_lvl_21d": {"inputs": ["revenue"], "func": reva_019_rev_growth_126_lvl_21d},
    "reva_020_rev_growth_126_zscore_21d": {"inputs": ["revenue"], "func": reva_020_rev_growth_126_zscore_21d},
    "reva_021_rev_growth_126_rank_21d": {"inputs": ["revenue"], "func": reva_021_rev_growth_126_rank_21d},
    "reva_022_rev_growth_126_lvl_63d": {"inputs": ["revenue"], "func": reva_022_rev_growth_126_lvl_63d},
    "reva_023_rev_growth_126_zscore_63d": {"inputs": ["revenue"], "func": reva_023_rev_growth_126_zscore_63d},
    "reva_024_rev_growth_126_rank_63d": {"inputs": ["revenue"], "func": reva_024_rev_growth_126_rank_63d},
    "reva_025_rev_growth_126_lvl_126d": {"inputs": ["revenue"], "func": reva_025_rev_growth_126_lvl_126d},
    "reva_026_rev_growth_126_zscore_126d": {"inputs": ["revenue"], "func": reva_026_rev_growth_126_zscore_126d},
    "reva_027_rev_growth_126_rank_126d": {"inputs": ["revenue"], "func": reva_027_rev_growth_126_rank_126d},
    "reva_028_rev_growth_126_lvl_252d": {"inputs": ["revenue"], "func": reva_028_rev_growth_126_lvl_252d},
    "reva_029_rev_growth_126_zscore_252d": {"inputs": ["revenue"], "func": reva_029_rev_growth_126_zscore_252d},
    "reva_030_rev_growth_126_rank_252d": {"inputs": ["revenue"], "func": reva_030_rev_growth_126_rank_252d},
    "reva_031_rev_growth_63_lvl_5d": {"inputs": ["revenue"], "func": reva_031_rev_growth_63_lvl_5d},
    "reva_032_rev_growth_63_zscore_5d": {"inputs": ["revenue"], "func": reva_032_rev_growth_63_zscore_5d},
    "reva_033_rev_growth_63_rank_5d": {"inputs": ["revenue"], "func": reva_033_rev_growth_63_rank_5d},
    "reva_034_rev_growth_63_lvl_21d": {"inputs": ["revenue"], "func": reva_034_rev_growth_63_lvl_21d},
    "reva_035_rev_growth_63_zscore_21d": {"inputs": ["revenue"], "func": reva_035_rev_growth_63_zscore_21d},
    "reva_036_rev_growth_63_rank_21d": {"inputs": ["revenue"], "func": reva_036_rev_growth_63_rank_21d},
    "reva_037_rev_growth_63_lvl_63d": {"inputs": ["revenue"], "func": reva_037_rev_growth_63_lvl_63d},
    "reva_038_rev_growth_63_zscore_63d": {"inputs": ["revenue"], "func": reva_038_rev_growth_63_zscore_63d},
    "reva_039_rev_growth_63_rank_63d": {"inputs": ["revenue"], "func": reva_039_rev_growth_63_rank_63d},
    "reva_040_rev_growth_63_lvl_126d": {"inputs": ["revenue"], "func": reva_040_rev_growth_63_lvl_126d},
    "reva_041_rev_growth_63_zscore_126d": {"inputs": ["revenue"], "func": reva_041_rev_growth_63_zscore_126d},
    "reva_042_rev_growth_63_rank_126d": {"inputs": ["revenue"], "func": reva_042_rev_growth_63_rank_126d},
    "reva_043_rev_growth_63_lvl_252d": {"inputs": ["revenue"], "func": reva_043_rev_growth_63_lvl_252d},
    "reva_044_rev_growth_63_zscore_252d": {"inputs": ["revenue"], "func": reva_044_rev_growth_63_zscore_252d},
    "reva_045_rev_growth_63_rank_252d": {"inputs": ["revenue"], "func": reva_045_rev_growth_63_rank_252d},
    "reva_046_rev_growth_21_lvl_5d": {"inputs": ["revenue"], "func": reva_046_rev_growth_21_lvl_5d},
    "reva_047_rev_growth_21_zscore_5d": {"inputs": ["revenue"], "func": reva_047_rev_growth_21_zscore_5d},
    "reva_048_rev_growth_21_rank_5d": {"inputs": ["revenue"], "func": reva_048_rev_growth_21_rank_5d},
    "reva_049_rev_growth_21_lvl_21d": {"inputs": ["revenue"], "func": reva_049_rev_growth_21_lvl_21d},
    "reva_050_rev_growth_21_zscore_21d": {"inputs": ["revenue"], "func": reva_050_rev_growth_21_zscore_21d},
    "reva_051_rev_growth_21_rank_21d": {"inputs": ["revenue"], "func": reva_051_rev_growth_21_rank_21d},
    "reva_052_rev_growth_21_lvl_63d": {"inputs": ["revenue"], "func": reva_052_rev_growth_21_lvl_63d},
    "reva_053_rev_growth_21_zscore_63d": {"inputs": ["revenue"], "func": reva_053_rev_growth_21_zscore_63d},
    "reva_054_rev_growth_21_rank_63d": {"inputs": ["revenue"], "func": reva_054_rev_growth_21_rank_63d},
    "reva_055_rev_growth_21_lvl_126d": {"inputs": ["revenue"], "func": reva_055_rev_growth_21_lvl_126d},
    "reva_056_rev_growth_21_zscore_126d": {"inputs": ["revenue"], "func": reva_056_rev_growth_21_zscore_126d},
    "reva_057_rev_growth_21_rank_126d": {"inputs": ["revenue"], "func": reva_057_rev_growth_21_rank_126d},
    "reva_058_rev_growth_21_lvl_252d": {"inputs": ["revenue"], "func": reva_058_rev_growth_21_lvl_252d},
    "reva_059_rev_growth_21_zscore_252d": {"inputs": ["revenue"], "func": reva_059_rev_growth_21_zscore_252d},
    "reva_060_rev_growth_21_rank_252d": {"inputs": ["revenue"], "func": reva_060_rev_growth_21_rank_252d},
    "reva_061_rev_growth_5_lvl_5d": {"inputs": ["revenue"], "func": reva_061_rev_growth_5_lvl_5d},
    "reva_062_rev_growth_5_zscore_5d": {"inputs": ["revenue"], "func": reva_062_rev_growth_5_zscore_5d},
    "reva_063_rev_growth_5_rank_5d": {"inputs": ["revenue"], "func": reva_063_rev_growth_5_rank_5d},
    "reva_064_rev_growth_5_lvl_21d": {"inputs": ["revenue"], "func": reva_064_rev_growth_5_lvl_21d},
    "reva_065_rev_growth_5_zscore_21d": {"inputs": ["revenue"], "func": reva_065_rev_growth_5_zscore_21d},
    "reva_066_rev_growth_5_rank_21d": {"inputs": ["revenue"], "func": reva_066_rev_growth_5_rank_21d},
    "reva_067_rev_growth_5_lvl_63d": {"inputs": ["revenue"], "func": reva_067_rev_growth_5_lvl_63d},
    "reva_068_rev_growth_5_zscore_63d": {"inputs": ["revenue"], "func": reva_068_rev_growth_5_zscore_63d},
    "reva_069_rev_growth_5_rank_63d": {"inputs": ["revenue"], "func": reva_069_rev_growth_5_rank_63d},
    "reva_070_rev_growth_5_lvl_126d": {"inputs": ["revenue"], "func": reva_070_rev_growth_5_lvl_126d},
    "reva_071_rev_growth_5_zscore_126d": {"inputs": ["revenue"], "func": reva_071_rev_growth_5_zscore_126d},
    "reva_072_rev_growth_5_rank_126d": {"inputs": ["revenue"], "func": reva_072_rev_growth_5_rank_126d},
    "reva_073_rev_growth_5_lvl_252d": {"inputs": ["revenue"], "func": reva_073_rev_growth_5_lvl_252d},
    "reva_074_rev_growth_5_zscore_252d": {"inputs": ["revenue"], "func": reva_074_rev_growth_5_zscore_252d},
    "reva_075_rev_growth_5_rank_252d": {"inputs": ["revenue"], "func": reva_075_rev_growth_5_rank_252d},
}
