"""
47_cash_flow_trajectory — Base Features 001-075
Domain: cash_flow_trajectory
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

def cflt_001_ocf_to_revenue_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_001_ocf_to_revenue_lvl_5d"""
    base = _safe_div(ocf, revenue)
    return _rolling_mean(base, 5)

def cflt_002_ocf_to_revenue_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_002_ocf_to_revenue_zscore_5d"""
    base = _safe_div(ocf, revenue)
    return _zscore_rolling(base, 5)

def cflt_003_ocf_to_revenue_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_003_ocf_to_revenue_rank_5d"""
    base = _safe_div(ocf, revenue)
    return _rank_pct(base, 5)

def cflt_004_ocf_to_revenue_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_004_ocf_to_revenue_lvl_21d"""
    base = _safe_div(ocf, revenue)
    return _rolling_mean(base, 21)

def cflt_005_ocf_to_revenue_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_005_ocf_to_revenue_zscore_21d"""
    base = _safe_div(ocf, revenue)
    return _zscore_rolling(base, 21)

def cflt_006_ocf_to_revenue_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_006_ocf_to_revenue_rank_21d"""
    base = _safe_div(ocf, revenue)
    return _rank_pct(base, 21)

def cflt_007_ocf_to_revenue_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_007_ocf_to_revenue_lvl_63d"""
    base = _safe_div(ocf, revenue)
    return _rolling_mean(base, 63)

def cflt_008_ocf_to_revenue_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_008_ocf_to_revenue_zscore_63d"""
    base = _safe_div(ocf, revenue)
    return _zscore_rolling(base, 63)

def cflt_009_ocf_to_revenue_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_009_ocf_to_revenue_rank_63d"""
    base = _safe_div(ocf, revenue)
    return _rank_pct(base, 63)

def cflt_010_ocf_to_revenue_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_010_ocf_to_revenue_lvl_126d"""
    base = _safe_div(ocf, revenue)
    return _rolling_mean(base, 126)

def cflt_011_ocf_to_revenue_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_011_ocf_to_revenue_zscore_126d"""
    base = _safe_div(ocf, revenue)
    return _zscore_rolling(base, 126)

def cflt_012_ocf_to_revenue_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_012_ocf_to_revenue_rank_126d"""
    base = _safe_div(ocf, revenue)
    return _rank_pct(base, 126)

def cflt_013_ocf_to_revenue_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_013_ocf_to_revenue_lvl_252d"""
    base = _safe_div(ocf, revenue)
    return _rolling_mean(base, 252)

def cflt_014_ocf_to_revenue_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_014_ocf_to_revenue_zscore_252d"""
    base = _safe_div(ocf, revenue)
    return _zscore_rolling(base, 252)

def cflt_015_ocf_to_revenue_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_015_ocf_to_revenue_rank_252d"""
    base = _safe_div(ocf, revenue)
    return _rank_pct(base, 252)

def cflt_016_fcf_to_revenue_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_016_fcf_to_revenue_lvl_5d"""
    base = _safe_div(fcf, revenue)
    return _rolling_mean(base, 5)

def cflt_017_fcf_to_revenue_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_017_fcf_to_revenue_zscore_5d"""
    base = _safe_div(fcf, revenue)
    return _zscore_rolling(base, 5)

def cflt_018_fcf_to_revenue_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_018_fcf_to_revenue_rank_5d"""
    base = _safe_div(fcf, revenue)
    return _rank_pct(base, 5)

def cflt_019_fcf_to_revenue_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_019_fcf_to_revenue_lvl_21d"""
    base = _safe_div(fcf, revenue)
    return _rolling_mean(base, 21)

def cflt_020_fcf_to_revenue_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_020_fcf_to_revenue_zscore_21d"""
    base = _safe_div(fcf, revenue)
    return _zscore_rolling(base, 21)

def cflt_021_fcf_to_revenue_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_021_fcf_to_revenue_rank_21d"""
    base = _safe_div(fcf, revenue)
    return _rank_pct(base, 21)

def cflt_022_fcf_to_revenue_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_022_fcf_to_revenue_lvl_63d"""
    base = _safe_div(fcf, revenue)
    return _rolling_mean(base, 63)

def cflt_023_fcf_to_revenue_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_023_fcf_to_revenue_zscore_63d"""
    base = _safe_div(fcf, revenue)
    return _zscore_rolling(base, 63)

def cflt_024_fcf_to_revenue_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_024_fcf_to_revenue_rank_63d"""
    base = _safe_div(fcf, revenue)
    return _rank_pct(base, 63)

def cflt_025_fcf_to_revenue_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_025_fcf_to_revenue_lvl_126d"""
    base = _safe_div(fcf, revenue)
    return _rolling_mean(base, 126)

def cflt_026_fcf_to_revenue_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_026_fcf_to_revenue_zscore_126d"""
    base = _safe_div(fcf, revenue)
    return _zscore_rolling(base, 126)

def cflt_027_fcf_to_revenue_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_027_fcf_to_revenue_rank_126d"""
    base = _safe_div(fcf, revenue)
    return _rank_pct(base, 126)

def cflt_028_fcf_to_revenue_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_028_fcf_to_revenue_lvl_252d"""
    base = _safe_div(fcf, revenue)
    return _rolling_mean(base, 252)

def cflt_029_fcf_to_revenue_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_029_fcf_to_revenue_zscore_252d"""
    base = _safe_div(fcf, revenue)
    return _zscore_rolling(base, 252)

def cflt_030_fcf_to_revenue_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_030_fcf_to_revenue_rank_252d"""
    base = _safe_div(fcf, revenue)
    return _rank_pct(base, 252)

def cflt_031_ocf_to_assets_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_031_ocf_to_assets_lvl_5d"""
    base = _safe_div(ocf, assets)
    return _rolling_mean(base, 5)

def cflt_032_ocf_to_assets_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_032_ocf_to_assets_zscore_5d"""
    base = _safe_div(ocf, assets)
    return _zscore_rolling(base, 5)

def cflt_033_ocf_to_assets_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_033_ocf_to_assets_rank_5d"""
    base = _safe_div(ocf, assets)
    return _rank_pct(base, 5)

def cflt_034_ocf_to_assets_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_034_ocf_to_assets_lvl_21d"""
    base = _safe_div(ocf, assets)
    return _rolling_mean(base, 21)

def cflt_035_ocf_to_assets_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_035_ocf_to_assets_zscore_21d"""
    base = _safe_div(ocf, assets)
    return _zscore_rolling(base, 21)

def cflt_036_ocf_to_assets_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_036_ocf_to_assets_rank_21d"""
    base = _safe_div(ocf, assets)
    return _rank_pct(base, 21)

def cflt_037_ocf_to_assets_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_037_ocf_to_assets_lvl_63d"""
    base = _safe_div(ocf, assets)
    return _rolling_mean(base, 63)

def cflt_038_ocf_to_assets_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_038_ocf_to_assets_zscore_63d"""
    base = _safe_div(ocf, assets)
    return _zscore_rolling(base, 63)

def cflt_039_ocf_to_assets_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_039_ocf_to_assets_rank_63d"""
    base = _safe_div(ocf, assets)
    return _rank_pct(base, 63)

def cflt_040_ocf_to_assets_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_040_ocf_to_assets_lvl_126d"""
    base = _safe_div(ocf, assets)
    return _rolling_mean(base, 126)

def cflt_041_ocf_to_assets_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_041_ocf_to_assets_zscore_126d"""
    base = _safe_div(ocf, assets)
    return _zscore_rolling(base, 126)

def cflt_042_ocf_to_assets_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_042_ocf_to_assets_rank_126d"""
    base = _safe_div(ocf, assets)
    return _rank_pct(base, 126)

def cflt_043_ocf_to_assets_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_043_ocf_to_assets_lvl_252d"""
    base = _safe_div(ocf, assets)
    return _rolling_mean(base, 252)

def cflt_044_ocf_to_assets_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_044_ocf_to_assets_zscore_252d"""
    base = _safe_div(ocf, assets)
    return _zscore_rolling(base, 252)

def cflt_045_ocf_to_assets_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_045_ocf_to_assets_rank_252d"""
    base = _safe_div(ocf, assets)
    return _rank_pct(base, 252)

def cflt_046_fcf_to_assets_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_046_fcf_to_assets_lvl_5d"""
    base = _safe_div(fcf, assets)
    return _rolling_mean(base, 5)

def cflt_047_fcf_to_assets_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_047_fcf_to_assets_zscore_5d"""
    base = _safe_div(fcf, assets)
    return _zscore_rolling(base, 5)

def cflt_048_fcf_to_assets_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_048_fcf_to_assets_rank_5d"""
    base = _safe_div(fcf, assets)
    return _rank_pct(base, 5)

def cflt_049_fcf_to_assets_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_049_fcf_to_assets_lvl_21d"""
    base = _safe_div(fcf, assets)
    return _rolling_mean(base, 21)

def cflt_050_fcf_to_assets_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_050_fcf_to_assets_zscore_21d"""
    base = _safe_div(fcf, assets)
    return _zscore_rolling(base, 21)

def cflt_051_fcf_to_assets_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_051_fcf_to_assets_rank_21d"""
    base = _safe_div(fcf, assets)
    return _rank_pct(base, 21)

def cflt_052_fcf_to_assets_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_052_fcf_to_assets_lvl_63d"""
    base = _safe_div(fcf, assets)
    return _rolling_mean(base, 63)

def cflt_053_fcf_to_assets_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_053_fcf_to_assets_zscore_63d"""
    base = _safe_div(fcf, assets)
    return _zscore_rolling(base, 63)

def cflt_054_fcf_to_assets_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_054_fcf_to_assets_rank_63d"""
    base = _safe_div(fcf, assets)
    return _rank_pct(base, 63)

def cflt_055_fcf_to_assets_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_055_fcf_to_assets_lvl_126d"""
    base = _safe_div(fcf, assets)
    return _rolling_mean(base, 126)

def cflt_056_fcf_to_assets_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_056_fcf_to_assets_zscore_126d"""
    base = _safe_div(fcf, assets)
    return _zscore_rolling(base, 126)

def cflt_057_fcf_to_assets_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_057_fcf_to_assets_rank_126d"""
    base = _safe_div(fcf, assets)
    return _rank_pct(base, 126)

def cflt_058_fcf_to_assets_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_058_fcf_to_assets_lvl_252d"""
    base = _safe_div(fcf, assets)
    return _rolling_mean(base, 252)

def cflt_059_fcf_to_assets_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_059_fcf_to_assets_zscore_252d"""
    base = _safe_div(fcf, assets)
    return _zscore_rolling(base, 252)

def cflt_060_fcf_to_assets_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_060_fcf_to_assets_rank_252d"""
    base = _safe_div(fcf, assets)
    return _rank_pct(base, 252)

def cflt_061_cash_flow_margin_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_061_cash_flow_margin_lvl_5d"""
    base = _safe_div(ocf, netinc)
    return _rolling_mean(base, 5)

def cflt_062_cash_flow_margin_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_062_cash_flow_margin_zscore_5d"""
    base = _safe_div(ocf, netinc)
    return _zscore_rolling(base, 5)

def cflt_063_cash_flow_margin_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_063_cash_flow_margin_rank_5d"""
    base = _safe_div(ocf, netinc)
    return _rank_pct(base, 5)

def cflt_064_cash_flow_margin_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_064_cash_flow_margin_lvl_21d"""
    base = _safe_div(ocf, netinc)
    return _rolling_mean(base, 21)

def cflt_065_cash_flow_margin_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_065_cash_flow_margin_zscore_21d"""
    base = _safe_div(ocf, netinc)
    return _zscore_rolling(base, 21)

def cflt_066_cash_flow_margin_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_066_cash_flow_margin_rank_21d"""
    base = _safe_div(ocf, netinc)
    return _rank_pct(base, 21)

def cflt_067_cash_flow_margin_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_067_cash_flow_margin_lvl_63d"""
    base = _safe_div(ocf, netinc)
    return _rolling_mean(base, 63)

def cflt_068_cash_flow_margin_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_068_cash_flow_margin_zscore_63d"""
    base = _safe_div(ocf, netinc)
    return _zscore_rolling(base, 63)

def cflt_069_cash_flow_margin_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_069_cash_flow_margin_rank_63d"""
    base = _safe_div(ocf, netinc)
    return _rank_pct(base, 63)

def cflt_070_cash_flow_margin_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_070_cash_flow_margin_lvl_126d"""
    base = _safe_div(ocf, netinc)
    return _rolling_mean(base, 126)

def cflt_071_cash_flow_margin_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_071_cash_flow_margin_zscore_126d"""
    base = _safe_div(ocf, netinc)
    return _zscore_rolling(base, 126)

def cflt_072_cash_flow_margin_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_072_cash_flow_margin_rank_126d"""
    base = _safe_div(ocf, netinc)
    return _rank_pct(base, 126)

def cflt_073_cash_flow_margin_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_073_cash_flow_margin_lvl_252d"""
    base = _safe_div(ocf, netinc)
    return _rolling_mean(base, 252)

def cflt_074_cash_flow_margin_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_074_cash_flow_margin_zscore_252d"""
    base = _safe_div(ocf, netinc)
    return _zscore_rolling(base, 252)

def cflt_075_cash_flow_margin_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """cflt_075_cash_flow_margin_rank_252d"""
    base = _safe_div(ocf, netinc)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V47_REGISTRY = {
    "cflt_001_ocf_to_revenue_lvl_5d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_001_ocf_to_revenue_lvl_5d},
    "cflt_002_ocf_to_revenue_zscore_5d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_002_ocf_to_revenue_zscore_5d},
    "cflt_003_ocf_to_revenue_rank_5d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_003_ocf_to_revenue_rank_5d},
    "cflt_004_ocf_to_revenue_lvl_21d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_004_ocf_to_revenue_lvl_21d},
    "cflt_005_ocf_to_revenue_zscore_21d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_005_ocf_to_revenue_zscore_21d},
    "cflt_006_ocf_to_revenue_rank_21d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_006_ocf_to_revenue_rank_21d},
    "cflt_007_ocf_to_revenue_lvl_63d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_007_ocf_to_revenue_lvl_63d},
    "cflt_008_ocf_to_revenue_zscore_63d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_008_ocf_to_revenue_zscore_63d},
    "cflt_009_ocf_to_revenue_rank_63d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_009_ocf_to_revenue_rank_63d},
    "cflt_010_ocf_to_revenue_lvl_126d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_010_ocf_to_revenue_lvl_126d},
    "cflt_011_ocf_to_revenue_zscore_126d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_011_ocf_to_revenue_zscore_126d},
    "cflt_012_ocf_to_revenue_rank_126d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_012_ocf_to_revenue_rank_126d},
    "cflt_013_ocf_to_revenue_lvl_252d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_013_ocf_to_revenue_lvl_252d},
    "cflt_014_ocf_to_revenue_zscore_252d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_014_ocf_to_revenue_zscore_252d},
    "cflt_015_ocf_to_revenue_rank_252d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_015_ocf_to_revenue_rank_252d},
    "cflt_016_fcf_to_revenue_lvl_5d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_016_fcf_to_revenue_lvl_5d},
    "cflt_017_fcf_to_revenue_zscore_5d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_017_fcf_to_revenue_zscore_5d},
    "cflt_018_fcf_to_revenue_rank_5d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_018_fcf_to_revenue_rank_5d},
    "cflt_019_fcf_to_revenue_lvl_21d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_019_fcf_to_revenue_lvl_21d},
    "cflt_020_fcf_to_revenue_zscore_21d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_020_fcf_to_revenue_zscore_21d},
    "cflt_021_fcf_to_revenue_rank_21d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_021_fcf_to_revenue_rank_21d},
    "cflt_022_fcf_to_revenue_lvl_63d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_022_fcf_to_revenue_lvl_63d},
    "cflt_023_fcf_to_revenue_zscore_63d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_023_fcf_to_revenue_zscore_63d},
    "cflt_024_fcf_to_revenue_rank_63d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_024_fcf_to_revenue_rank_63d},
    "cflt_025_fcf_to_revenue_lvl_126d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_025_fcf_to_revenue_lvl_126d},
    "cflt_026_fcf_to_revenue_zscore_126d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_026_fcf_to_revenue_zscore_126d},
    "cflt_027_fcf_to_revenue_rank_126d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_027_fcf_to_revenue_rank_126d},
    "cflt_028_fcf_to_revenue_lvl_252d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_028_fcf_to_revenue_lvl_252d},
    "cflt_029_fcf_to_revenue_zscore_252d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_029_fcf_to_revenue_zscore_252d},
    "cflt_030_fcf_to_revenue_rank_252d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_030_fcf_to_revenue_rank_252d},
    "cflt_031_ocf_to_assets_lvl_5d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_031_ocf_to_assets_lvl_5d},
    "cflt_032_ocf_to_assets_zscore_5d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_032_ocf_to_assets_zscore_5d},
    "cflt_033_ocf_to_assets_rank_5d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_033_ocf_to_assets_rank_5d},
    "cflt_034_ocf_to_assets_lvl_21d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_034_ocf_to_assets_lvl_21d},
    "cflt_035_ocf_to_assets_zscore_21d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_035_ocf_to_assets_zscore_21d},
    "cflt_036_ocf_to_assets_rank_21d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_036_ocf_to_assets_rank_21d},
    "cflt_037_ocf_to_assets_lvl_63d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_037_ocf_to_assets_lvl_63d},
    "cflt_038_ocf_to_assets_zscore_63d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_038_ocf_to_assets_zscore_63d},
    "cflt_039_ocf_to_assets_rank_63d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_039_ocf_to_assets_rank_63d},
    "cflt_040_ocf_to_assets_lvl_126d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_040_ocf_to_assets_lvl_126d},
    "cflt_041_ocf_to_assets_zscore_126d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_041_ocf_to_assets_zscore_126d},
    "cflt_042_ocf_to_assets_rank_126d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_042_ocf_to_assets_rank_126d},
    "cflt_043_ocf_to_assets_lvl_252d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_043_ocf_to_assets_lvl_252d},
    "cflt_044_ocf_to_assets_zscore_252d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_044_ocf_to_assets_zscore_252d},
    "cflt_045_ocf_to_assets_rank_252d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_045_ocf_to_assets_rank_252d},
    "cflt_046_fcf_to_assets_lvl_5d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_046_fcf_to_assets_lvl_5d},
    "cflt_047_fcf_to_assets_zscore_5d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_047_fcf_to_assets_zscore_5d},
    "cflt_048_fcf_to_assets_rank_5d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_048_fcf_to_assets_rank_5d},
    "cflt_049_fcf_to_assets_lvl_21d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_049_fcf_to_assets_lvl_21d},
    "cflt_050_fcf_to_assets_zscore_21d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_050_fcf_to_assets_zscore_21d},
    "cflt_051_fcf_to_assets_rank_21d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_051_fcf_to_assets_rank_21d},
    "cflt_052_fcf_to_assets_lvl_63d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_052_fcf_to_assets_lvl_63d},
    "cflt_053_fcf_to_assets_zscore_63d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_053_fcf_to_assets_zscore_63d},
    "cflt_054_fcf_to_assets_rank_63d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_054_fcf_to_assets_rank_63d},
    "cflt_055_fcf_to_assets_lvl_126d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_055_fcf_to_assets_lvl_126d},
    "cflt_056_fcf_to_assets_zscore_126d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_056_fcf_to_assets_zscore_126d},
    "cflt_057_fcf_to_assets_rank_126d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_057_fcf_to_assets_rank_126d},
    "cflt_058_fcf_to_assets_lvl_252d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_058_fcf_to_assets_lvl_252d},
    "cflt_059_fcf_to_assets_zscore_252d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_059_fcf_to_assets_zscore_252d},
    "cflt_060_fcf_to_assets_rank_252d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_060_fcf_to_assets_rank_252d},
    "cflt_061_cash_flow_margin_lvl_5d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_061_cash_flow_margin_lvl_5d},
    "cflt_062_cash_flow_margin_zscore_5d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_062_cash_flow_margin_zscore_5d},
    "cflt_063_cash_flow_margin_rank_5d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_063_cash_flow_margin_rank_5d},
    "cflt_064_cash_flow_margin_lvl_21d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_064_cash_flow_margin_lvl_21d},
    "cflt_065_cash_flow_margin_zscore_21d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_065_cash_flow_margin_zscore_21d},
    "cflt_066_cash_flow_margin_rank_21d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_066_cash_flow_margin_rank_21d},
    "cflt_067_cash_flow_margin_lvl_63d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_067_cash_flow_margin_lvl_63d},
    "cflt_068_cash_flow_margin_zscore_63d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_068_cash_flow_margin_zscore_63d},
    "cflt_069_cash_flow_margin_rank_63d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_069_cash_flow_margin_rank_63d},
    "cflt_070_cash_flow_margin_lvl_126d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_070_cash_flow_margin_lvl_126d},
    "cflt_071_cash_flow_margin_zscore_126d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_071_cash_flow_margin_zscore_126d},
    "cflt_072_cash_flow_margin_rank_126d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_072_cash_flow_margin_rank_126d},
    "cflt_073_cash_flow_margin_lvl_252d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_073_cash_flow_margin_lvl_252d},
    "cflt_074_cash_flow_margin_zscore_252d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_074_cash_flow_margin_zscore_252d},
    "cflt_075_cash_flow_margin_rank_252d": {"inputs": ['ocf', 'fcf', 'revenue', 'assets', 'netinc'], "func": cflt_075_cash_flow_margin_rank_252d},
}
