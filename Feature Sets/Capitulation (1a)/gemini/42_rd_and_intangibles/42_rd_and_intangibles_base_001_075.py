"""
42_rd_and_intangibles — Base Features 001-075
Domain: rd_and_intangibles
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

def rdin_001_rnd_intensity_lvl_5d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_001_rnd_intensity_lvl_5d"""
    base = _safe_div(rnd, revenue)
    return _rolling_mean(base, 5)

def rdin_002_rnd_intensity_zscore_5d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_002_rnd_intensity_zscore_5d"""
    base = _safe_div(rnd, revenue)
    return _zscore_rolling(base, 5)

def rdin_003_rnd_intensity_rank_5d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_003_rnd_intensity_rank_5d"""
    base = _safe_div(rnd, revenue)
    return _rank_pct(base, 5)

def rdin_004_rnd_intensity_lvl_21d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_004_rnd_intensity_lvl_21d"""
    base = _safe_div(rnd, revenue)
    return _rolling_mean(base, 21)

def rdin_005_rnd_intensity_zscore_21d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_005_rnd_intensity_zscore_21d"""
    base = _safe_div(rnd, revenue)
    return _zscore_rolling(base, 21)

def rdin_006_rnd_intensity_rank_21d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_006_rnd_intensity_rank_21d"""
    base = _safe_div(rnd, revenue)
    return _rank_pct(base, 21)

def rdin_007_rnd_intensity_lvl_63d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_007_rnd_intensity_lvl_63d"""
    base = _safe_div(rnd, revenue)
    return _rolling_mean(base, 63)

def rdin_008_rnd_intensity_zscore_63d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_008_rnd_intensity_zscore_63d"""
    base = _safe_div(rnd, revenue)
    return _zscore_rolling(base, 63)

def rdin_009_rnd_intensity_rank_63d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_009_rnd_intensity_rank_63d"""
    base = _safe_div(rnd, revenue)
    return _rank_pct(base, 63)

def rdin_010_rnd_intensity_lvl_126d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_010_rnd_intensity_lvl_126d"""
    base = _safe_div(rnd, revenue)
    return _rolling_mean(base, 126)

def rdin_011_rnd_intensity_zscore_126d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_011_rnd_intensity_zscore_126d"""
    base = _safe_div(rnd, revenue)
    return _zscore_rolling(base, 126)

def rdin_012_rnd_intensity_rank_126d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_012_rnd_intensity_rank_126d"""
    base = _safe_div(rnd, revenue)
    return _rank_pct(base, 126)

def rdin_013_rnd_intensity_lvl_252d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_013_rnd_intensity_lvl_252d"""
    base = _safe_div(rnd, revenue)
    return _rolling_mean(base, 252)

def rdin_014_rnd_intensity_zscore_252d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_014_rnd_intensity_zscore_252d"""
    base = _safe_div(rnd, revenue)
    return _zscore_rolling(base, 252)

def rdin_015_rnd_intensity_rank_252d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_015_rnd_intensity_rank_252d"""
    base = _safe_div(rnd, revenue)
    return _rank_pct(base, 252)

def rdin_016_rnd_to_assets_lvl_5d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_016_rnd_to_assets_lvl_5d"""
    base = _safe_div(rnd, assets)
    return _rolling_mean(base, 5)

def rdin_017_rnd_to_assets_zscore_5d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_017_rnd_to_assets_zscore_5d"""
    base = _safe_div(rnd, assets)
    return _zscore_rolling(base, 5)

def rdin_018_rnd_to_assets_rank_5d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_018_rnd_to_assets_rank_5d"""
    base = _safe_div(rnd, assets)
    return _rank_pct(base, 5)

def rdin_019_rnd_to_assets_lvl_21d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_019_rnd_to_assets_lvl_21d"""
    base = _safe_div(rnd, assets)
    return _rolling_mean(base, 21)

def rdin_020_rnd_to_assets_zscore_21d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_020_rnd_to_assets_zscore_21d"""
    base = _safe_div(rnd, assets)
    return _zscore_rolling(base, 21)

def rdin_021_rnd_to_assets_rank_21d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_021_rnd_to_assets_rank_21d"""
    base = _safe_div(rnd, assets)
    return _rank_pct(base, 21)

def rdin_022_rnd_to_assets_lvl_63d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_022_rnd_to_assets_lvl_63d"""
    base = _safe_div(rnd, assets)
    return _rolling_mean(base, 63)

def rdin_023_rnd_to_assets_zscore_63d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_023_rnd_to_assets_zscore_63d"""
    base = _safe_div(rnd, assets)
    return _zscore_rolling(base, 63)

def rdin_024_rnd_to_assets_rank_63d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_024_rnd_to_assets_rank_63d"""
    base = _safe_div(rnd, assets)
    return _rank_pct(base, 63)

def rdin_025_rnd_to_assets_lvl_126d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_025_rnd_to_assets_lvl_126d"""
    base = _safe_div(rnd, assets)
    return _rolling_mean(base, 126)

def rdin_026_rnd_to_assets_zscore_126d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_026_rnd_to_assets_zscore_126d"""
    base = _safe_div(rnd, assets)
    return _zscore_rolling(base, 126)

def rdin_027_rnd_to_assets_rank_126d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_027_rnd_to_assets_rank_126d"""
    base = _safe_div(rnd, assets)
    return _rank_pct(base, 126)

def rdin_028_rnd_to_assets_lvl_252d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_028_rnd_to_assets_lvl_252d"""
    base = _safe_div(rnd, assets)
    return _rolling_mean(base, 252)

def rdin_029_rnd_to_assets_zscore_252d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_029_rnd_to_assets_zscore_252d"""
    base = _safe_div(rnd, assets)
    return _zscore_rolling(base, 252)

def rdin_030_rnd_to_assets_rank_252d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_030_rnd_to_assets_rank_252d"""
    base = _safe_div(rnd, assets)
    return _rank_pct(base, 252)

def rdin_031_intangible_ratio_lvl_5d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_031_intangible_ratio_lvl_5d"""
    base = _safe_div(intangibles, assets)
    return _rolling_mean(base, 5)

def rdin_032_intangible_ratio_zscore_5d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_032_intangible_ratio_zscore_5d"""
    base = _safe_div(intangibles, assets)
    return _zscore_rolling(base, 5)

def rdin_033_intangible_ratio_rank_5d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_033_intangible_ratio_rank_5d"""
    base = _safe_div(intangibles, assets)
    return _rank_pct(base, 5)

def rdin_034_intangible_ratio_lvl_21d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_034_intangible_ratio_lvl_21d"""
    base = _safe_div(intangibles, assets)
    return _rolling_mean(base, 21)

def rdin_035_intangible_ratio_zscore_21d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_035_intangible_ratio_zscore_21d"""
    base = _safe_div(intangibles, assets)
    return _zscore_rolling(base, 21)

def rdin_036_intangible_ratio_rank_21d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_036_intangible_ratio_rank_21d"""
    base = _safe_div(intangibles, assets)
    return _rank_pct(base, 21)

def rdin_037_intangible_ratio_lvl_63d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_037_intangible_ratio_lvl_63d"""
    base = _safe_div(intangibles, assets)
    return _rolling_mean(base, 63)

def rdin_038_intangible_ratio_zscore_63d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_038_intangible_ratio_zscore_63d"""
    base = _safe_div(intangibles, assets)
    return _zscore_rolling(base, 63)

def rdin_039_intangible_ratio_rank_63d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_039_intangible_ratio_rank_63d"""
    base = _safe_div(intangibles, assets)
    return _rank_pct(base, 63)

def rdin_040_intangible_ratio_lvl_126d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_040_intangible_ratio_lvl_126d"""
    base = _safe_div(intangibles, assets)
    return _rolling_mean(base, 126)

def rdin_041_intangible_ratio_zscore_126d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_041_intangible_ratio_zscore_126d"""
    base = _safe_div(intangibles, assets)
    return _zscore_rolling(base, 126)

def rdin_042_intangible_ratio_rank_126d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_042_intangible_ratio_rank_126d"""
    base = _safe_div(intangibles, assets)
    return _rank_pct(base, 126)

def rdin_043_intangible_ratio_lvl_252d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_043_intangible_ratio_lvl_252d"""
    base = _safe_div(intangibles, assets)
    return _rolling_mean(base, 252)

def rdin_044_intangible_ratio_zscore_252d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_044_intangible_ratio_zscore_252d"""
    base = _safe_div(intangibles, assets)
    return _zscore_rolling(base, 252)

def rdin_045_intangible_ratio_rank_252d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_045_intangible_ratio_rank_252d"""
    base = _safe_div(intangibles, assets)
    return _rank_pct(base, 252)

def rdin_046_intangible_to_revenue_lvl_5d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_046_intangible_to_revenue_lvl_5d"""
    base = _safe_div(intangibles, revenue)
    return _rolling_mean(base, 5)

def rdin_047_intangible_to_revenue_zscore_5d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_047_intangible_to_revenue_zscore_5d"""
    base = _safe_div(intangibles, revenue)
    return _zscore_rolling(base, 5)

def rdin_048_intangible_to_revenue_rank_5d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_048_intangible_to_revenue_rank_5d"""
    base = _safe_div(intangibles, revenue)
    return _rank_pct(base, 5)

def rdin_049_intangible_to_revenue_lvl_21d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_049_intangible_to_revenue_lvl_21d"""
    base = _safe_div(intangibles, revenue)
    return _rolling_mean(base, 21)

def rdin_050_intangible_to_revenue_zscore_21d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_050_intangible_to_revenue_zscore_21d"""
    base = _safe_div(intangibles, revenue)
    return _zscore_rolling(base, 21)

def rdin_051_intangible_to_revenue_rank_21d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_051_intangible_to_revenue_rank_21d"""
    base = _safe_div(intangibles, revenue)
    return _rank_pct(base, 21)

def rdin_052_intangible_to_revenue_lvl_63d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_052_intangible_to_revenue_lvl_63d"""
    base = _safe_div(intangibles, revenue)
    return _rolling_mean(base, 63)

def rdin_053_intangible_to_revenue_zscore_63d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_053_intangible_to_revenue_zscore_63d"""
    base = _safe_div(intangibles, revenue)
    return _zscore_rolling(base, 63)

def rdin_054_intangible_to_revenue_rank_63d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_054_intangible_to_revenue_rank_63d"""
    base = _safe_div(intangibles, revenue)
    return _rank_pct(base, 63)

def rdin_055_intangible_to_revenue_lvl_126d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_055_intangible_to_revenue_lvl_126d"""
    base = _safe_div(intangibles, revenue)
    return _rolling_mean(base, 126)

def rdin_056_intangible_to_revenue_zscore_126d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_056_intangible_to_revenue_zscore_126d"""
    base = _safe_div(intangibles, revenue)
    return _zscore_rolling(base, 126)

def rdin_057_intangible_to_revenue_rank_126d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_057_intangible_to_revenue_rank_126d"""
    base = _safe_div(intangibles, revenue)
    return _rank_pct(base, 126)

def rdin_058_intangible_to_revenue_lvl_252d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_058_intangible_to_revenue_lvl_252d"""
    base = _safe_div(intangibles, revenue)
    return _rolling_mean(base, 252)

def rdin_059_intangible_to_revenue_zscore_252d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_059_intangible_to_revenue_zscore_252d"""
    base = _safe_div(intangibles, revenue)
    return _zscore_rolling(base, 252)

def rdin_060_intangible_to_revenue_rank_252d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_060_intangible_to_revenue_rank_252d"""
    base = _safe_div(intangibles, revenue)
    return _rank_pct(base, 252)

def rdin_061_rnd_to_opexp_lvl_5d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_061_rnd_to_opexp_lvl_5d"""
    base = _safe_div(rnd, opexp)
    return _rolling_mean(base, 5)

def rdin_062_rnd_to_opexp_zscore_5d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_062_rnd_to_opexp_zscore_5d"""
    base = _safe_div(rnd, opexp)
    return _zscore_rolling(base, 5)

def rdin_063_rnd_to_opexp_rank_5d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_063_rnd_to_opexp_rank_5d"""
    base = _safe_div(rnd, opexp)
    return _rank_pct(base, 5)

def rdin_064_rnd_to_opexp_lvl_21d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_064_rnd_to_opexp_lvl_21d"""
    base = _safe_div(rnd, opexp)
    return _rolling_mean(base, 21)

def rdin_065_rnd_to_opexp_zscore_21d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_065_rnd_to_opexp_zscore_21d"""
    base = _safe_div(rnd, opexp)
    return _zscore_rolling(base, 21)

def rdin_066_rnd_to_opexp_rank_21d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_066_rnd_to_opexp_rank_21d"""
    base = _safe_div(rnd, opexp)
    return _rank_pct(base, 21)

def rdin_067_rnd_to_opexp_lvl_63d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_067_rnd_to_opexp_lvl_63d"""
    base = _safe_div(rnd, opexp)
    return _rolling_mean(base, 63)

def rdin_068_rnd_to_opexp_zscore_63d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_068_rnd_to_opexp_zscore_63d"""
    base = _safe_div(rnd, opexp)
    return _zscore_rolling(base, 63)

def rdin_069_rnd_to_opexp_rank_63d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_069_rnd_to_opexp_rank_63d"""
    base = _safe_div(rnd, opexp)
    return _rank_pct(base, 63)

def rdin_070_rnd_to_opexp_lvl_126d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_070_rnd_to_opexp_lvl_126d"""
    base = _safe_div(rnd, opexp)
    return _rolling_mean(base, 126)

def rdin_071_rnd_to_opexp_zscore_126d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_071_rnd_to_opexp_zscore_126d"""
    base = _safe_div(rnd, opexp)
    return _zscore_rolling(base, 126)

def rdin_072_rnd_to_opexp_rank_126d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_072_rnd_to_opexp_rank_126d"""
    base = _safe_div(rnd, opexp)
    return _rank_pct(base, 126)

def rdin_073_rnd_to_opexp_lvl_252d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_073_rnd_to_opexp_lvl_252d"""
    base = _safe_div(rnd, opexp)
    return _rolling_mean(base, 252)

def rdin_074_rnd_to_opexp_zscore_252d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_074_rnd_to_opexp_zscore_252d"""
    base = _safe_div(rnd, opexp)
    return _zscore_rolling(base, 252)

def rdin_075_rnd_to_opexp_rank_252d(rnd: pd.Series, intangibles: pd.Series, assets: pd.Series, revenue: pd.Series, opexp: pd.Series) -> pd.Series:
    """rdin_075_rnd_to_opexp_rank_252d"""
    base = _safe_div(rnd, opexp)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V42_REGISTRY = {
    "rdin_001_rnd_intensity_lvl_5d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_001_rnd_intensity_lvl_5d},
    "rdin_002_rnd_intensity_zscore_5d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_002_rnd_intensity_zscore_5d},
    "rdin_003_rnd_intensity_rank_5d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_003_rnd_intensity_rank_5d},
    "rdin_004_rnd_intensity_lvl_21d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_004_rnd_intensity_lvl_21d},
    "rdin_005_rnd_intensity_zscore_21d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_005_rnd_intensity_zscore_21d},
    "rdin_006_rnd_intensity_rank_21d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_006_rnd_intensity_rank_21d},
    "rdin_007_rnd_intensity_lvl_63d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_007_rnd_intensity_lvl_63d},
    "rdin_008_rnd_intensity_zscore_63d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_008_rnd_intensity_zscore_63d},
    "rdin_009_rnd_intensity_rank_63d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_009_rnd_intensity_rank_63d},
    "rdin_010_rnd_intensity_lvl_126d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_010_rnd_intensity_lvl_126d},
    "rdin_011_rnd_intensity_zscore_126d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_011_rnd_intensity_zscore_126d},
    "rdin_012_rnd_intensity_rank_126d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_012_rnd_intensity_rank_126d},
    "rdin_013_rnd_intensity_lvl_252d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_013_rnd_intensity_lvl_252d},
    "rdin_014_rnd_intensity_zscore_252d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_014_rnd_intensity_zscore_252d},
    "rdin_015_rnd_intensity_rank_252d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_015_rnd_intensity_rank_252d},
    "rdin_016_rnd_to_assets_lvl_5d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_016_rnd_to_assets_lvl_5d},
    "rdin_017_rnd_to_assets_zscore_5d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_017_rnd_to_assets_zscore_5d},
    "rdin_018_rnd_to_assets_rank_5d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_018_rnd_to_assets_rank_5d},
    "rdin_019_rnd_to_assets_lvl_21d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_019_rnd_to_assets_lvl_21d},
    "rdin_020_rnd_to_assets_zscore_21d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_020_rnd_to_assets_zscore_21d},
    "rdin_021_rnd_to_assets_rank_21d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_021_rnd_to_assets_rank_21d},
    "rdin_022_rnd_to_assets_lvl_63d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_022_rnd_to_assets_lvl_63d},
    "rdin_023_rnd_to_assets_zscore_63d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_023_rnd_to_assets_zscore_63d},
    "rdin_024_rnd_to_assets_rank_63d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_024_rnd_to_assets_rank_63d},
    "rdin_025_rnd_to_assets_lvl_126d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_025_rnd_to_assets_lvl_126d},
    "rdin_026_rnd_to_assets_zscore_126d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_026_rnd_to_assets_zscore_126d},
    "rdin_027_rnd_to_assets_rank_126d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_027_rnd_to_assets_rank_126d},
    "rdin_028_rnd_to_assets_lvl_252d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_028_rnd_to_assets_lvl_252d},
    "rdin_029_rnd_to_assets_zscore_252d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_029_rnd_to_assets_zscore_252d},
    "rdin_030_rnd_to_assets_rank_252d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_030_rnd_to_assets_rank_252d},
    "rdin_031_intangible_ratio_lvl_5d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_031_intangible_ratio_lvl_5d},
    "rdin_032_intangible_ratio_zscore_5d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_032_intangible_ratio_zscore_5d},
    "rdin_033_intangible_ratio_rank_5d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_033_intangible_ratio_rank_5d},
    "rdin_034_intangible_ratio_lvl_21d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_034_intangible_ratio_lvl_21d},
    "rdin_035_intangible_ratio_zscore_21d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_035_intangible_ratio_zscore_21d},
    "rdin_036_intangible_ratio_rank_21d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_036_intangible_ratio_rank_21d},
    "rdin_037_intangible_ratio_lvl_63d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_037_intangible_ratio_lvl_63d},
    "rdin_038_intangible_ratio_zscore_63d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_038_intangible_ratio_zscore_63d},
    "rdin_039_intangible_ratio_rank_63d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_039_intangible_ratio_rank_63d},
    "rdin_040_intangible_ratio_lvl_126d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_040_intangible_ratio_lvl_126d},
    "rdin_041_intangible_ratio_zscore_126d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_041_intangible_ratio_zscore_126d},
    "rdin_042_intangible_ratio_rank_126d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_042_intangible_ratio_rank_126d},
    "rdin_043_intangible_ratio_lvl_252d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_043_intangible_ratio_lvl_252d},
    "rdin_044_intangible_ratio_zscore_252d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_044_intangible_ratio_zscore_252d},
    "rdin_045_intangible_ratio_rank_252d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_045_intangible_ratio_rank_252d},
    "rdin_046_intangible_to_revenue_lvl_5d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_046_intangible_to_revenue_lvl_5d},
    "rdin_047_intangible_to_revenue_zscore_5d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_047_intangible_to_revenue_zscore_5d},
    "rdin_048_intangible_to_revenue_rank_5d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_048_intangible_to_revenue_rank_5d},
    "rdin_049_intangible_to_revenue_lvl_21d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_049_intangible_to_revenue_lvl_21d},
    "rdin_050_intangible_to_revenue_zscore_21d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_050_intangible_to_revenue_zscore_21d},
    "rdin_051_intangible_to_revenue_rank_21d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_051_intangible_to_revenue_rank_21d},
    "rdin_052_intangible_to_revenue_lvl_63d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_052_intangible_to_revenue_lvl_63d},
    "rdin_053_intangible_to_revenue_zscore_63d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_053_intangible_to_revenue_zscore_63d},
    "rdin_054_intangible_to_revenue_rank_63d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_054_intangible_to_revenue_rank_63d},
    "rdin_055_intangible_to_revenue_lvl_126d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_055_intangible_to_revenue_lvl_126d},
    "rdin_056_intangible_to_revenue_zscore_126d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_056_intangible_to_revenue_zscore_126d},
    "rdin_057_intangible_to_revenue_rank_126d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_057_intangible_to_revenue_rank_126d},
    "rdin_058_intangible_to_revenue_lvl_252d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_058_intangible_to_revenue_lvl_252d},
    "rdin_059_intangible_to_revenue_zscore_252d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_059_intangible_to_revenue_zscore_252d},
    "rdin_060_intangible_to_revenue_rank_252d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_060_intangible_to_revenue_rank_252d},
    "rdin_061_rnd_to_opexp_lvl_5d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_061_rnd_to_opexp_lvl_5d},
    "rdin_062_rnd_to_opexp_zscore_5d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_062_rnd_to_opexp_zscore_5d},
    "rdin_063_rnd_to_opexp_rank_5d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_063_rnd_to_opexp_rank_5d},
    "rdin_064_rnd_to_opexp_lvl_21d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_064_rnd_to_opexp_lvl_21d},
    "rdin_065_rnd_to_opexp_zscore_21d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_065_rnd_to_opexp_zscore_21d},
    "rdin_066_rnd_to_opexp_rank_21d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_066_rnd_to_opexp_rank_21d},
    "rdin_067_rnd_to_opexp_lvl_63d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_067_rnd_to_opexp_lvl_63d},
    "rdin_068_rnd_to_opexp_zscore_63d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_068_rnd_to_opexp_zscore_63d},
    "rdin_069_rnd_to_opexp_rank_63d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_069_rnd_to_opexp_rank_63d},
    "rdin_070_rnd_to_opexp_lvl_126d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_070_rnd_to_opexp_lvl_126d},
    "rdin_071_rnd_to_opexp_zscore_126d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_071_rnd_to_opexp_zscore_126d},
    "rdin_072_rnd_to_opexp_rank_126d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_072_rnd_to_opexp_rank_126d},
    "rdin_073_rnd_to_opexp_lvl_252d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_073_rnd_to_opexp_lvl_252d},
    "rdin_074_rnd_to_opexp_zscore_252d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_074_rnd_to_opexp_zscore_252d},
    "rdin_075_rnd_to_opexp_rank_252d": {"inputs": ['rnd', 'intangibles', 'assets', 'revenue', 'opexp'], "func": rdin_075_rnd_to_opexp_rank_252d},
}
