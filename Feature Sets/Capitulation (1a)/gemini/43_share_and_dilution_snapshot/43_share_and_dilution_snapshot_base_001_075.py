"""
43_share_and_dilution_snapshot — Base Features 001-075
Domain: share_and_dilution_snapshot
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

def dilu_001_sharesbas_level_lvl_5d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_001_sharesbas_level_lvl_5d"""
    base = sharesbas
    return _rolling_mean(base, 5)

def dilu_002_sharesbas_level_zscore_5d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_002_sharesbas_level_zscore_5d"""
    base = sharesbas
    return _zscore_rolling(base, 5)

def dilu_003_sharesbas_level_rank_5d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_003_sharesbas_level_rank_5d"""
    base = sharesbas
    return _rank_pct(base, 5)

def dilu_004_sharesbas_level_lvl_21d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_004_sharesbas_level_lvl_21d"""
    base = sharesbas
    return _rolling_mean(base, 21)

def dilu_005_sharesbas_level_zscore_21d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_005_sharesbas_level_zscore_21d"""
    base = sharesbas
    return _zscore_rolling(base, 21)

def dilu_006_sharesbas_level_rank_21d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_006_sharesbas_level_rank_21d"""
    base = sharesbas
    return _rank_pct(base, 21)

def dilu_007_sharesbas_level_lvl_63d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_007_sharesbas_level_lvl_63d"""
    base = sharesbas
    return _rolling_mean(base, 63)

def dilu_008_sharesbas_level_zscore_63d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_008_sharesbas_level_zscore_63d"""
    base = sharesbas
    return _zscore_rolling(base, 63)

def dilu_009_sharesbas_level_rank_63d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_009_sharesbas_level_rank_63d"""
    base = sharesbas
    return _rank_pct(base, 63)

def dilu_010_sharesbas_level_lvl_126d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_010_sharesbas_level_lvl_126d"""
    base = sharesbas
    return _rolling_mean(base, 126)

def dilu_011_sharesbas_level_zscore_126d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_011_sharesbas_level_zscore_126d"""
    base = sharesbas
    return _zscore_rolling(base, 126)

def dilu_012_sharesbas_level_rank_126d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_012_sharesbas_level_rank_126d"""
    base = sharesbas
    return _rank_pct(base, 126)

def dilu_013_sharesbas_level_lvl_252d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_013_sharesbas_level_lvl_252d"""
    base = sharesbas
    return _rolling_mean(base, 252)

def dilu_014_sharesbas_level_zscore_252d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_014_sharesbas_level_zscore_252d"""
    base = sharesbas
    return _zscore_rolling(base, 252)

def dilu_015_sharesbas_level_rank_252d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_015_sharesbas_level_rank_252d"""
    base = sharesbas
    return _rank_pct(base, 252)

def dilu_016_shareswa_level_lvl_5d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_016_shareswa_level_lvl_5d"""
    base = shareswa
    return _rolling_mean(base, 5)

def dilu_017_shareswa_level_zscore_5d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_017_shareswa_level_zscore_5d"""
    base = shareswa
    return _zscore_rolling(base, 5)

def dilu_018_shareswa_level_rank_5d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_018_shareswa_level_rank_5d"""
    base = shareswa
    return _rank_pct(base, 5)

def dilu_019_shareswa_level_lvl_21d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_019_shareswa_level_lvl_21d"""
    base = shareswa
    return _rolling_mean(base, 21)

def dilu_020_shareswa_level_zscore_21d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_020_shareswa_level_zscore_21d"""
    base = shareswa
    return _zscore_rolling(base, 21)

def dilu_021_shareswa_level_rank_21d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_021_shareswa_level_rank_21d"""
    base = shareswa
    return _rank_pct(base, 21)

def dilu_022_shareswa_level_lvl_63d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_022_shareswa_level_lvl_63d"""
    base = shareswa
    return _rolling_mean(base, 63)

def dilu_023_shareswa_level_zscore_63d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_023_shareswa_level_zscore_63d"""
    base = shareswa
    return _zscore_rolling(base, 63)

def dilu_024_shareswa_level_rank_63d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_024_shareswa_level_rank_63d"""
    base = shareswa
    return _rank_pct(base, 63)

def dilu_025_shareswa_level_lvl_126d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_025_shareswa_level_lvl_126d"""
    base = shareswa
    return _rolling_mean(base, 126)

def dilu_026_shareswa_level_zscore_126d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_026_shareswa_level_zscore_126d"""
    base = shareswa
    return _zscore_rolling(base, 126)

def dilu_027_shareswa_level_rank_126d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_027_shareswa_level_rank_126d"""
    base = shareswa
    return _rank_pct(base, 126)

def dilu_028_shareswa_level_lvl_252d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_028_shareswa_level_lvl_252d"""
    base = shareswa
    return _rolling_mean(base, 252)

def dilu_029_shareswa_level_zscore_252d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_029_shareswa_level_zscore_252d"""
    base = shareswa
    return _zscore_rolling(base, 252)

def dilu_030_shareswa_level_rank_252d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_030_shareswa_level_rank_252d"""
    base = shareswa
    return _rank_pct(base, 252)

def dilu_031_sharesbas_to_assets_lvl_5d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_031_sharesbas_to_assets_lvl_5d"""
    base = _safe_div(sharesbas, assets)
    return _rolling_mean(base, 5)

def dilu_032_sharesbas_to_assets_zscore_5d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_032_sharesbas_to_assets_zscore_5d"""
    base = _safe_div(sharesbas, assets)
    return _zscore_rolling(base, 5)

def dilu_033_sharesbas_to_assets_rank_5d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_033_sharesbas_to_assets_rank_5d"""
    base = _safe_div(sharesbas, assets)
    return _rank_pct(base, 5)

def dilu_034_sharesbas_to_assets_lvl_21d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_034_sharesbas_to_assets_lvl_21d"""
    base = _safe_div(sharesbas, assets)
    return _rolling_mean(base, 21)

def dilu_035_sharesbas_to_assets_zscore_21d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_035_sharesbas_to_assets_zscore_21d"""
    base = _safe_div(sharesbas, assets)
    return _zscore_rolling(base, 21)

def dilu_036_sharesbas_to_assets_rank_21d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_036_sharesbas_to_assets_rank_21d"""
    base = _safe_div(sharesbas, assets)
    return _rank_pct(base, 21)

def dilu_037_sharesbas_to_assets_lvl_63d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_037_sharesbas_to_assets_lvl_63d"""
    base = _safe_div(sharesbas, assets)
    return _rolling_mean(base, 63)

def dilu_038_sharesbas_to_assets_zscore_63d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_038_sharesbas_to_assets_zscore_63d"""
    base = _safe_div(sharesbas, assets)
    return _zscore_rolling(base, 63)

def dilu_039_sharesbas_to_assets_rank_63d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_039_sharesbas_to_assets_rank_63d"""
    base = _safe_div(sharesbas, assets)
    return _rank_pct(base, 63)

def dilu_040_sharesbas_to_assets_lvl_126d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_040_sharesbas_to_assets_lvl_126d"""
    base = _safe_div(sharesbas, assets)
    return _rolling_mean(base, 126)

def dilu_041_sharesbas_to_assets_zscore_126d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_041_sharesbas_to_assets_zscore_126d"""
    base = _safe_div(sharesbas, assets)
    return _zscore_rolling(base, 126)

def dilu_042_sharesbas_to_assets_rank_126d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_042_sharesbas_to_assets_rank_126d"""
    base = _safe_div(sharesbas, assets)
    return _rank_pct(base, 126)

def dilu_043_sharesbas_to_assets_lvl_252d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_043_sharesbas_to_assets_lvl_252d"""
    base = _safe_div(sharesbas, assets)
    return _rolling_mean(base, 252)

def dilu_044_sharesbas_to_assets_zscore_252d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_044_sharesbas_to_assets_zscore_252d"""
    base = _safe_div(sharesbas, assets)
    return _zscore_rolling(base, 252)

def dilu_045_sharesbas_to_assets_rank_252d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_045_sharesbas_to_assets_rank_252d"""
    base = _safe_div(sharesbas, assets)
    return _rank_pct(base, 252)

def dilu_046_shareswa_to_assets_lvl_5d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_046_shareswa_to_assets_lvl_5d"""
    base = _safe_div(shareswa, assets)
    return _rolling_mean(base, 5)

def dilu_047_shareswa_to_assets_zscore_5d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_047_shareswa_to_assets_zscore_5d"""
    base = _safe_div(shareswa, assets)
    return _zscore_rolling(base, 5)

def dilu_048_shareswa_to_assets_rank_5d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_048_shareswa_to_assets_rank_5d"""
    base = _safe_div(shareswa, assets)
    return _rank_pct(base, 5)

def dilu_049_shareswa_to_assets_lvl_21d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_049_shareswa_to_assets_lvl_21d"""
    base = _safe_div(shareswa, assets)
    return _rolling_mean(base, 21)

def dilu_050_shareswa_to_assets_zscore_21d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_050_shareswa_to_assets_zscore_21d"""
    base = _safe_div(shareswa, assets)
    return _zscore_rolling(base, 21)

def dilu_051_shareswa_to_assets_rank_21d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_051_shareswa_to_assets_rank_21d"""
    base = _safe_div(shareswa, assets)
    return _rank_pct(base, 21)

def dilu_052_shareswa_to_assets_lvl_63d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_052_shareswa_to_assets_lvl_63d"""
    base = _safe_div(shareswa, assets)
    return _rolling_mean(base, 63)

def dilu_053_shareswa_to_assets_zscore_63d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_053_shareswa_to_assets_zscore_63d"""
    base = _safe_div(shareswa, assets)
    return _zscore_rolling(base, 63)

def dilu_054_shareswa_to_assets_rank_63d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_054_shareswa_to_assets_rank_63d"""
    base = _safe_div(shareswa, assets)
    return _rank_pct(base, 63)

def dilu_055_shareswa_to_assets_lvl_126d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_055_shareswa_to_assets_lvl_126d"""
    base = _safe_div(shareswa, assets)
    return _rolling_mean(base, 126)

def dilu_056_shareswa_to_assets_zscore_126d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_056_shareswa_to_assets_zscore_126d"""
    base = _safe_div(shareswa, assets)
    return _zscore_rolling(base, 126)

def dilu_057_shareswa_to_assets_rank_126d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_057_shareswa_to_assets_rank_126d"""
    base = _safe_div(shareswa, assets)
    return _rank_pct(base, 126)

def dilu_058_shareswa_to_assets_lvl_252d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_058_shareswa_to_assets_lvl_252d"""
    base = _safe_div(shareswa, assets)
    return _rolling_mean(base, 252)

def dilu_059_shareswa_to_assets_zscore_252d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_059_shareswa_to_assets_zscore_252d"""
    base = _safe_div(shareswa, assets)
    return _zscore_rolling(base, 252)

def dilu_060_shareswa_to_assets_rank_252d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_060_shareswa_to_assets_rank_252d"""
    base = _safe_div(shareswa, assets)
    return _rank_pct(base, 252)

def dilu_061_sharesbas_to_revenue_lvl_5d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_061_sharesbas_to_revenue_lvl_5d"""
    base = _safe_div(sharesbas, revenue)
    return _rolling_mean(base, 5)

def dilu_062_sharesbas_to_revenue_zscore_5d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_062_sharesbas_to_revenue_zscore_5d"""
    base = _safe_div(sharesbas, revenue)
    return _zscore_rolling(base, 5)

def dilu_063_sharesbas_to_revenue_rank_5d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_063_sharesbas_to_revenue_rank_5d"""
    base = _safe_div(sharesbas, revenue)
    return _rank_pct(base, 5)

def dilu_064_sharesbas_to_revenue_lvl_21d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_064_sharesbas_to_revenue_lvl_21d"""
    base = _safe_div(sharesbas, revenue)
    return _rolling_mean(base, 21)

def dilu_065_sharesbas_to_revenue_zscore_21d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_065_sharesbas_to_revenue_zscore_21d"""
    base = _safe_div(sharesbas, revenue)
    return _zscore_rolling(base, 21)

def dilu_066_sharesbas_to_revenue_rank_21d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_066_sharesbas_to_revenue_rank_21d"""
    base = _safe_div(sharesbas, revenue)
    return _rank_pct(base, 21)

def dilu_067_sharesbas_to_revenue_lvl_63d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_067_sharesbas_to_revenue_lvl_63d"""
    base = _safe_div(sharesbas, revenue)
    return _rolling_mean(base, 63)

def dilu_068_sharesbas_to_revenue_zscore_63d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_068_sharesbas_to_revenue_zscore_63d"""
    base = _safe_div(sharesbas, revenue)
    return _zscore_rolling(base, 63)

def dilu_069_sharesbas_to_revenue_rank_63d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_069_sharesbas_to_revenue_rank_63d"""
    base = _safe_div(sharesbas, revenue)
    return _rank_pct(base, 63)

def dilu_070_sharesbas_to_revenue_lvl_126d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_070_sharesbas_to_revenue_lvl_126d"""
    base = _safe_div(sharesbas, revenue)
    return _rolling_mean(base, 126)

def dilu_071_sharesbas_to_revenue_zscore_126d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_071_sharesbas_to_revenue_zscore_126d"""
    base = _safe_div(sharesbas, revenue)
    return _zscore_rolling(base, 126)

def dilu_072_sharesbas_to_revenue_rank_126d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_072_sharesbas_to_revenue_rank_126d"""
    base = _safe_div(sharesbas, revenue)
    return _rank_pct(base, 126)

def dilu_073_sharesbas_to_revenue_lvl_252d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_073_sharesbas_to_revenue_lvl_252d"""
    base = _safe_div(sharesbas, revenue)
    return _rolling_mean(base, 252)

def dilu_074_sharesbas_to_revenue_zscore_252d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_074_sharesbas_to_revenue_zscore_252d"""
    base = _safe_div(sharesbas, revenue)
    return _zscore_rolling(base, 252)

def dilu_075_sharesbas_to_revenue_rank_252d(sharesbas: pd.Series, shareswa: pd.Series, assets: pd.Series, revenue: pd.Series) -> pd.Series:
    """dilu_075_sharesbas_to_revenue_rank_252d"""
    base = _safe_div(sharesbas, revenue)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V43_REGISTRY = {
    "dilu_001_sharesbas_level_lvl_5d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_001_sharesbas_level_lvl_5d},
    "dilu_002_sharesbas_level_zscore_5d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_002_sharesbas_level_zscore_5d},
    "dilu_003_sharesbas_level_rank_5d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_003_sharesbas_level_rank_5d},
    "dilu_004_sharesbas_level_lvl_21d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_004_sharesbas_level_lvl_21d},
    "dilu_005_sharesbas_level_zscore_21d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_005_sharesbas_level_zscore_21d},
    "dilu_006_sharesbas_level_rank_21d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_006_sharesbas_level_rank_21d},
    "dilu_007_sharesbas_level_lvl_63d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_007_sharesbas_level_lvl_63d},
    "dilu_008_sharesbas_level_zscore_63d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_008_sharesbas_level_zscore_63d},
    "dilu_009_sharesbas_level_rank_63d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_009_sharesbas_level_rank_63d},
    "dilu_010_sharesbas_level_lvl_126d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_010_sharesbas_level_lvl_126d},
    "dilu_011_sharesbas_level_zscore_126d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_011_sharesbas_level_zscore_126d},
    "dilu_012_sharesbas_level_rank_126d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_012_sharesbas_level_rank_126d},
    "dilu_013_sharesbas_level_lvl_252d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_013_sharesbas_level_lvl_252d},
    "dilu_014_sharesbas_level_zscore_252d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_014_sharesbas_level_zscore_252d},
    "dilu_015_sharesbas_level_rank_252d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_015_sharesbas_level_rank_252d},
    "dilu_016_shareswa_level_lvl_5d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_016_shareswa_level_lvl_5d},
    "dilu_017_shareswa_level_zscore_5d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_017_shareswa_level_zscore_5d},
    "dilu_018_shareswa_level_rank_5d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_018_shareswa_level_rank_5d},
    "dilu_019_shareswa_level_lvl_21d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_019_shareswa_level_lvl_21d},
    "dilu_020_shareswa_level_zscore_21d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_020_shareswa_level_zscore_21d},
    "dilu_021_shareswa_level_rank_21d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_021_shareswa_level_rank_21d},
    "dilu_022_shareswa_level_lvl_63d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_022_shareswa_level_lvl_63d},
    "dilu_023_shareswa_level_zscore_63d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_023_shareswa_level_zscore_63d},
    "dilu_024_shareswa_level_rank_63d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_024_shareswa_level_rank_63d},
    "dilu_025_shareswa_level_lvl_126d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_025_shareswa_level_lvl_126d},
    "dilu_026_shareswa_level_zscore_126d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_026_shareswa_level_zscore_126d},
    "dilu_027_shareswa_level_rank_126d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_027_shareswa_level_rank_126d},
    "dilu_028_shareswa_level_lvl_252d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_028_shareswa_level_lvl_252d},
    "dilu_029_shareswa_level_zscore_252d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_029_shareswa_level_zscore_252d},
    "dilu_030_shareswa_level_rank_252d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_030_shareswa_level_rank_252d},
    "dilu_031_sharesbas_to_assets_lvl_5d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_031_sharesbas_to_assets_lvl_5d},
    "dilu_032_sharesbas_to_assets_zscore_5d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_032_sharesbas_to_assets_zscore_5d},
    "dilu_033_sharesbas_to_assets_rank_5d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_033_sharesbas_to_assets_rank_5d},
    "dilu_034_sharesbas_to_assets_lvl_21d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_034_sharesbas_to_assets_lvl_21d},
    "dilu_035_sharesbas_to_assets_zscore_21d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_035_sharesbas_to_assets_zscore_21d},
    "dilu_036_sharesbas_to_assets_rank_21d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_036_sharesbas_to_assets_rank_21d},
    "dilu_037_sharesbas_to_assets_lvl_63d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_037_sharesbas_to_assets_lvl_63d},
    "dilu_038_sharesbas_to_assets_zscore_63d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_038_sharesbas_to_assets_zscore_63d},
    "dilu_039_sharesbas_to_assets_rank_63d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_039_sharesbas_to_assets_rank_63d},
    "dilu_040_sharesbas_to_assets_lvl_126d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_040_sharesbas_to_assets_lvl_126d},
    "dilu_041_sharesbas_to_assets_zscore_126d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_041_sharesbas_to_assets_zscore_126d},
    "dilu_042_sharesbas_to_assets_rank_126d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_042_sharesbas_to_assets_rank_126d},
    "dilu_043_sharesbas_to_assets_lvl_252d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_043_sharesbas_to_assets_lvl_252d},
    "dilu_044_sharesbas_to_assets_zscore_252d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_044_sharesbas_to_assets_zscore_252d},
    "dilu_045_sharesbas_to_assets_rank_252d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_045_sharesbas_to_assets_rank_252d},
    "dilu_046_shareswa_to_assets_lvl_5d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_046_shareswa_to_assets_lvl_5d},
    "dilu_047_shareswa_to_assets_zscore_5d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_047_shareswa_to_assets_zscore_5d},
    "dilu_048_shareswa_to_assets_rank_5d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_048_shareswa_to_assets_rank_5d},
    "dilu_049_shareswa_to_assets_lvl_21d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_049_shareswa_to_assets_lvl_21d},
    "dilu_050_shareswa_to_assets_zscore_21d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_050_shareswa_to_assets_zscore_21d},
    "dilu_051_shareswa_to_assets_rank_21d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_051_shareswa_to_assets_rank_21d},
    "dilu_052_shareswa_to_assets_lvl_63d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_052_shareswa_to_assets_lvl_63d},
    "dilu_053_shareswa_to_assets_zscore_63d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_053_shareswa_to_assets_zscore_63d},
    "dilu_054_shareswa_to_assets_rank_63d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_054_shareswa_to_assets_rank_63d},
    "dilu_055_shareswa_to_assets_lvl_126d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_055_shareswa_to_assets_lvl_126d},
    "dilu_056_shareswa_to_assets_zscore_126d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_056_shareswa_to_assets_zscore_126d},
    "dilu_057_shareswa_to_assets_rank_126d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_057_shareswa_to_assets_rank_126d},
    "dilu_058_shareswa_to_assets_lvl_252d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_058_shareswa_to_assets_lvl_252d},
    "dilu_059_shareswa_to_assets_zscore_252d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_059_shareswa_to_assets_zscore_252d},
    "dilu_060_shareswa_to_assets_rank_252d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_060_shareswa_to_assets_rank_252d},
    "dilu_061_sharesbas_to_revenue_lvl_5d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_061_sharesbas_to_revenue_lvl_5d},
    "dilu_062_sharesbas_to_revenue_zscore_5d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_062_sharesbas_to_revenue_zscore_5d},
    "dilu_063_sharesbas_to_revenue_rank_5d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_063_sharesbas_to_revenue_rank_5d},
    "dilu_064_sharesbas_to_revenue_lvl_21d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_064_sharesbas_to_revenue_lvl_21d},
    "dilu_065_sharesbas_to_revenue_zscore_21d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_065_sharesbas_to_revenue_zscore_21d},
    "dilu_066_sharesbas_to_revenue_rank_21d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_066_sharesbas_to_revenue_rank_21d},
    "dilu_067_sharesbas_to_revenue_lvl_63d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_067_sharesbas_to_revenue_lvl_63d},
    "dilu_068_sharesbas_to_revenue_zscore_63d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_068_sharesbas_to_revenue_zscore_63d},
    "dilu_069_sharesbas_to_revenue_rank_63d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_069_sharesbas_to_revenue_rank_63d},
    "dilu_070_sharesbas_to_revenue_lvl_126d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_070_sharesbas_to_revenue_lvl_126d},
    "dilu_071_sharesbas_to_revenue_zscore_126d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_071_sharesbas_to_revenue_zscore_126d},
    "dilu_072_sharesbas_to_revenue_rank_126d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_072_sharesbas_to_revenue_rank_126d},
    "dilu_073_sharesbas_to_revenue_lvl_252d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_073_sharesbas_to_revenue_lvl_252d},
    "dilu_074_sharesbas_to_revenue_zscore_252d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_074_sharesbas_to_revenue_zscore_252d},
    "dilu_075_sharesbas_to_revenue_rank_252d": {"inputs": ['sharesbas', 'shareswa', 'assets', 'revenue'], "func": dilu_075_sharesbas_to_revenue_rank_252d},
}
