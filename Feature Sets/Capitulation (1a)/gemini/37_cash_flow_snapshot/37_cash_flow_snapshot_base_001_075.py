"""
37_cash_flow_snapshot — Base Features 001-075
Domain: cash_flow_snapshot
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

# ── Feature functions ────────────────────────────────────────────────────────

def cflo_001_ocf_lvl_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_001_ocf_lvl_lvl_5d"""
    base = ocf
    return _rolling_mean(base, 5)

def cflo_002_ocf_lvl_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_002_ocf_lvl_zscore_5d"""
    base = ocf
    return _zscore_rolling(base, 5)

def cflo_003_ocf_lvl_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_003_ocf_lvl_rank_5d"""
    base = ocf
    return _rank_pct(base, 5)

def cflo_004_ocf_lvl_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_004_ocf_lvl_lvl_21d"""
    base = ocf
    return _rolling_mean(base, 21)

def cflo_005_ocf_lvl_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_005_ocf_lvl_zscore_21d"""
    base = ocf
    return _zscore_rolling(base, 21)

def cflo_006_ocf_lvl_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_006_ocf_lvl_rank_21d"""
    base = ocf
    return _rank_pct(base, 21)

def cflo_007_ocf_lvl_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_007_ocf_lvl_lvl_63d"""
    base = ocf
    return _rolling_mean(base, 63)

def cflo_008_ocf_lvl_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_008_ocf_lvl_zscore_63d"""
    base = ocf
    return _zscore_rolling(base, 63)

def cflo_009_ocf_lvl_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_009_ocf_lvl_rank_63d"""
    base = ocf
    return _rank_pct(base, 63)

def cflo_010_ocf_lvl_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_010_ocf_lvl_lvl_126d"""
    base = ocf
    return _rolling_mean(base, 126)

def cflo_011_ocf_lvl_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_011_ocf_lvl_zscore_126d"""
    base = ocf
    return _zscore_rolling(base, 126)

def cflo_012_ocf_lvl_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_012_ocf_lvl_rank_126d"""
    base = ocf
    return _rank_pct(base, 126)

def cflo_013_ocf_lvl_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_013_ocf_lvl_lvl_252d"""
    base = ocf
    return _rolling_mean(base, 252)

def cflo_014_ocf_lvl_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_014_ocf_lvl_zscore_252d"""
    base = ocf
    return _zscore_rolling(base, 252)

def cflo_015_ocf_lvl_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_015_ocf_lvl_rank_252d"""
    base = ocf
    return _rank_pct(base, 252)

def cflo_016_fcf_lvl_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_016_fcf_lvl_lvl_5d"""
    base = fcf
    return _rolling_mean(base, 5)

def cflo_017_fcf_lvl_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_017_fcf_lvl_zscore_5d"""
    base = fcf
    return _zscore_rolling(base, 5)

def cflo_018_fcf_lvl_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_018_fcf_lvl_rank_5d"""
    base = fcf
    return _rank_pct(base, 5)

def cflo_019_fcf_lvl_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_019_fcf_lvl_lvl_21d"""
    base = fcf
    return _rolling_mean(base, 21)

def cflo_020_fcf_lvl_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_020_fcf_lvl_zscore_21d"""
    base = fcf
    return _zscore_rolling(base, 21)

def cflo_021_fcf_lvl_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_021_fcf_lvl_rank_21d"""
    base = fcf
    return _rank_pct(base, 21)

def cflo_022_fcf_lvl_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_022_fcf_lvl_lvl_63d"""
    base = fcf
    return _rolling_mean(base, 63)

def cflo_023_fcf_lvl_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_023_fcf_lvl_zscore_63d"""
    base = fcf
    return _zscore_rolling(base, 63)

def cflo_024_fcf_lvl_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_024_fcf_lvl_rank_63d"""
    base = fcf
    return _rank_pct(base, 63)

def cflo_025_fcf_lvl_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_025_fcf_lvl_lvl_126d"""
    base = fcf
    return _rolling_mean(base, 126)

def cflo_026_fcf_lvl_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_026_fcf_lvl_zscore_126d"""
    base = fcf
    return _zscore_rolling(base, 126)

def cflo_027_fcf_lvl_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_027_fcf_lvl_rank_126d"""
    base = fcf
    return _rank_pct(base, 126)

def cflo_028_fcf_lvl_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_028_fcf_lvl_lvl_252d"""
    base = fcf
    return _rolling_mean(base, 252)

def cflo_029_fcf_lvl_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_029_fcf_lvl_zscore_252d"""
    base = fcf
    return _zscore_rolling(base, 252)

def cflo_030_fcf_lvl_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_030_fcf_lvl_rank_252d"""
    base = fcf
    return _rank_pct(base, 252)

def cflo_031_ocf_margin_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_031_ocf_margin_lvl_5d"""
    base = _safe_div(ocf, revenue)
    return _rolling_mean(base, 5)

def cflo_032_ocf_margin_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_032_ocf_margin_zscore_5d"""
    base = _safe_div(ocf, revenue)
    return _zscore_rolling(base, 5)

def cflo_033_ocf_margin_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_033_ocf_margin_rank_5d"""
    base = _safe_div(ocf, revenue)
    return _rank_pct(base, 5)

def cflo_034_ocf_margin_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_034_ocf_margin_lvl_21d"""
    base = _safe_div(ocf, revenue)
    return _rolling_mean(base, 21)

def cflo_035_ocf_margin_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_035_ocf_margin_zscore_21d"""
    base = _safe_div(ocf, revenue)
    return _zscore_rolling(base, 21)

def cflo_036_ocf_margin_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_036_ocf_margin_rank_21d"""
    base = _safe_div(ocf, revenue)
    return _rank_pct(base, 21)

def cflo_037_ocf_margin_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_037_ocf_margin_lvl_63d"""
    base = _safe_div(ocf, revenue)
    return _rolling_mean(base, 63)

def cflo_038_ocf_margin_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_038_ocf_margin_zscore_63d"""
    base = _safe_div(ocf, revenue)
    return _zscore_rolling(base, 63)

def cflo_039_ocf_margin_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_039_ocf_margin_rank_63d"""
    base = _safe_div(ocf, revenue)
    return _rank_pct(base, 63)

def cflo_040_ocf_margin_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_040_ocf_margin_lvl_126d"""
    base = _safe_div(ocf, revenue)
    return _rolling_mean(base, 126)

def cflo_041_ocf_margin_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_041_ocf_margin_zscore_126d"""
    base = _safe_div(ocf, revenue)
    return _zscore_rolling(base, 126)

def cflo_042_ocf_margin_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_042_ocf_margin_rank_126d"""
    base = _safe_div(ocf, revenue)
    return _rank_pct(base, 126)

def cflo_043_ocf_margin_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_043_ocf_margin_lvl_252d"""
    base = _safe_div(ocf, revenue)
    return _rolling_mean(base, 252)

def cflo_044_ocf_margin_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_044_ocf_margin_zscore_252d"""
    base = _safe_div(ocf, revenue)
    return _zscore_rolling(base, 252)

def cflo_045_ocf_margin_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_045_ocf_margin_rank_252d"""
    base = _safe_div(ocf, revenue)
    return _rank_pct(base, 252)

def cflo_046_fcf_ps_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_046_fcf_ps_lvl_5d"""
    base = _safe_div(fcf, sharesbas)
    return _rolling_mean(base, 5)

def cflo_047_fcf_ps_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_047_fcf_ps_zscore_5d"""
    base = _safe_div(fcf, sharesbas)
    return _zscore_rolling(base, 5)

def cflo_048_fcf_ps_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_048_fcf_ps_rank_5d"""
    base = _safe_div(fcf, sharesbas)
    return _rank_pct(base, 5)

def cflo_049_fcf_ps_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_049_fcf_ps_lvl_21d"""
    base = _safe_div(fcf, sharesbas)
    return _rolling_mean(base, 21)

def cflo_050_fcf_ps_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_050_fcf_ps_zscore_21d"""
    base = _safe_div(fcf, sharesbas)
    return _zscore_rolling(base, 21)

def cflo_051_fcf_ps_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_051_fcf_ps_rank_21d"""
    base = _safe_div(fcf, sharesbas)
    return _rank_pct(base, 21)

def cflo_052_fcf_ps_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_052_fcf_ps_lvl_63d"""
    base = _safe_div(fcf, sharesbas)
    return _rolling_mean(base, 63)

def cflo_053_fcf_ps_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_053_fcf_ps_zscore_63d"""
    base = _safe_div(fcf, sharesbas)
    return _zscore_rolling(base, 63)

def cflo_054_fcf_ps_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_054_fcf_ps_rank_63d"""
    base = _safe_div(fcf, sharesbas)
    return _rank_pct(base, 63)

def cflo_055_fcf_ps_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_055_fcf_ps_lvl_126d"""
    base = _safe_div(fcf, sharesbas)
    return _rolling_mean(base, 126)

def cflo_056_fcf_ps_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_056_fcf_ps_zscore_126d"""
    base = _safe_div(fcf, sharesbas)
    return _zscore_rolling(base, 126)

def cflo_057_fcf_ps_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_057_fcf_ps_rank_126d"""
    base = _safe_div(fcf, sharesbas)
    return _rank_pct(base, 126)

def cflo_058_fcf_ps_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_058_fcf_ps_lvl_252d"""
    base = _safe_div(fcf, sharesbas)
    return _rolling_mean(base, 252)

def cflo_059_fcf_ps_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_059_fcf_ps_zscore_252d"""
    base = _safe_div(fcf, sharesbas)
    return _zscore_rolling(base, 252)

def cflo_060_fcf_ps_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_060_fcf_ps_rank_252d"""
    base = _safe_div(fcf, sharesbas)
    return _rank_pct(base, 252)

def cflo_061_fcf_yield_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_061_fcf_yield_lvl_5d"""
    base = _safe_div(fcf, marketcap)
    return _rolling_mean(base, 5)

def cflo_062_fcf_yield_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_062_fcf_yield_zscore_5d"""
    base = _safe_div(fcf, marketcap)
    return _zscore_rolling(base, 5)

def cflo_063_fcf_yield_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_063_fcf_yield_rank_5d"""
    base = _safe_div(fcf, marketcap)
    return _rank_pct(base, 5)

def cflo_064_fcf_yield_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_064_fcf_yield_lvl_21d"""
    base = _safe_div(fcf, marketcap)
    return _rolling_mean(base, 21)

def cflo_065_fcf_yield_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_065_fcf_yield_zscore_21d"""
    base = _safe_div(fcf, marketcap)
    return _zscore_rolling(base, 21)

def cflo_066_fcf_yield_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_066_fcf_yield_rank_21d"""
    base = _safe_div(fcf, marketcap)
    return _rank_pct(base, 21)

def cflo_067_fcf_yield_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_067_fcf_yield_lvl_63d"""
    base = _safe_div(fcf, marketcap)
    return _rolling_mean(base, 63)

def cflo_068_fcf_yield_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_068_fcf_yield_zscore_63d"""
    base = _safe_div(fcf, marketcap)
    return _zscore_rolling(base, 63)

def cflo_069_fcf_yield_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_069_fcf_yield_rank_63d"""
    base = _safe_div(fcf, marketcap)
    return _rank_pct(base, 63)

def cflo_070_fcf_yield_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_070_fcf_yield_lvl_126d"""
    base = _safe_div(fcf, marketcap)
    return _rolling_mean(base, 126)

def cflo_071_fcf_yield_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_071_fcf_yield_zscore_126d"""
    base = _safe_div(fcf, marketcap)
    return _zscore_rolling(base, 126)

def cflo_072_fcf_yield_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_072_fcf_yield_rank_126d"""
    base = _safe_div(fcf, marketcap)
    return _rank_pct(base, 126)

def cflo_073_fcf_yield_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_073_fcf_yield_lvl_252d"""
    base = _safe_div(fcf, marketcap)
    return _rolling_mean(base, 252)

def cflo_074_fcf_yield_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_074_fcf_yield_zscore_252d"""
    base = _safe_div(fcf, marketcap)
    return _zscore_rolling(base, 252)

def cflo_075_fcf_yield_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_075_fcf_yield_rank_252d"""
    base = _safe_div(fcf, marketcap)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V37_REGISTRY = {
    "cflo_001_ocf_lvl_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_001_ocf_lvl_lvl_5d},
    "cflo_002_ocf_lvl_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_002_ocf_lvl_zscore_5d},
    "cflo_003_ocf_lvl_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_003_ocf_lvl_rank_5d},
    "cflo_004_ocf_lvl_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_004_ocf_lvl_lvl_21d},
    "cflo_005_ocf_lvl_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_005_ocf_lvl_zscore_21d},
    "cflo_006_ocf_lvl_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_006_ocf_lvl_rank_21d},
    "cflo_007_ocf_lvl_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_007_ocf_lvl_lvl_63d},
    "cflo_008_ocf_lvl_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_008_ocf_lvl_zscore_63d},
    "cflo_009_ocf_lvl_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_009_ocf_lvl_rank_63d},
    "cflo_010_ocf_lvl_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_010_ocf_lvl_lvl_126d},
    "cflo_011_ocf_lvl_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_011_ocf_lvl_zscore_126d},
    "cflo_012_ocf_lvl_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_012_ocf_lvl_rank_126d},
    "cflo_013_ocf_lvl_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_013_ocf_lvl_lvl_252d},
    "cflo_014_ocf_lvl_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_014_ocf_lvl_zscore_252d},
    "cflo_015_ocf_lvl_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_015_ocf_lvl_rank_252d},
    "cflo_016_fcf_lvl_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_016_fcf_lvl_lvl_5d},
    "cflo_017_fcf_lvl_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_017_fcf_lvl_zscore_5d},
    "cflo_018_fcf_lvl_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_018_fcf_lvl_rank_5d},
    "cflo_019_fcf_lvl_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_019_fcf_lvl_lvl_21d},
    "cflo_020_fcf_lvl_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_020_fcf_lvl_zscore_21d},
    "cflo_021_fcf_lvl_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_021_fcf_lvl_rank_21d},
    "cflo_022_fcf_lvl_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_022_fcf_lvl_lvl_63d},
    "cflo_023_fcf_lvl_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_023_fcf_lvl_zscore_63d},
    "cflo_024_fcf_lvl_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_024_fcf_lvl_rank_63d},
    "cflo_025_fcf_lvl_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_025_fcf_lvl_lvl_126d},
    "cflo_026_fcf_lvl_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_026_fcf_lvl_zscore_126d},
    "cflo_027_fcf_lvl_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_027_fcf_lvl_rank_126d},
    "cflo_028_fcf_lvl_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_028_fcf_lvl_lvl_252d},
    "cflo_029_fcf_lvl_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_029_fcf_lvl_zscore_252d},
    "cflo_030_fcf_lvl_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_030_fcf_lvl_rank_252d},
    "cflo_031_ocf_margin_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_031_ocf_margin_lvl_5d},
    "cflo_032_ocf_margin_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_032_ocf_margin_zscore_5d},
    "cflo_033_ocf_margin_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_033_ocf_margin_rank_5d},
    "cflo_034_ocf_margin_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_034_ocf_margin_lvl_21d},
    "cflo_035_ocf_margin_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_035_ocf_margin_zscore_21d},
    "cflo_036_ocf_margin_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_036_ocf_margin_rank_21d},
    "cflo_037_ocf_margin_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_037_ocf_margin_lvl_63d},
    "cflo_038_ocf_margin_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_038_ocf_margin_zscore_63d},
    "cflo_039_ocf_margin_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_039_ocf_margin_rank_63d},
    "cflo_040_ocf_margin_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_040_ocf_margin_lvl_126d},
    "cflo_041_ocf_margin_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_041_ocf_margin_zscore_126d},
    "cflo_042_ocf_margin_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_042_ocf_margin_rank_126d},
    "cflo_043_ocf_margin_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_043_ocf_margin_lvl_252d},
    "cflo_044_ocf_margin_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_044_ocf_margin_zscore_252d},
    "cflo_045_ocf_margin_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_045_ocf_margin_rank_252d},
    "cflo_046_fcf_ps_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_046_fcf_ps_lvl_5d},
    "cflo_047_fcf_ps_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_047_fcf_ps_zscore_5d},
    "cflo_048_fcf_ps_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_048_fcf_ps_rank_5d},
    "cflo_049_fcf_ps_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_049_fcf_ps_lvl_21d},
    "cflo_050_fcf_ps_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_050_fcf_ps_zscore_21d},
    "cflo_051_fcf_ps_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_051_fcf_ps_rank_21d},
    "cflo_052_fcf_ps_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_052_fcf_ps_lvl_63d},
    "cflo_053_fcf_ps_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_053_fcf_ps_zscore_63d},
    "cflo_054_fcf_ps_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_054_fcf_ps_rank_63d},
    "cflo_055_fcf_ps_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_055_fcf_ps_lvl_126d},
    "cflo_056_fcf_ps_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_056_fcf_ps_zscore_126d},
    "cflo_057_fcf_ps_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_057_fcf_ps_rank_126d},
    "cflo_058_fcf_ps_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_058_fcf_ps_lvl_252d},
    "cflo_059_fcf_ps_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_059_fcf_ps_zscore_252d},
    "cflo_060_fcf_ps_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_060_fcf_ps_rank_252d},
    "cflo_061_fcf_yield_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_061_fcf_yield_lvl_5d},
    "cflo_062_fcf_yield_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_062_fcf_yield_zscore_5d},
    "cflo_063_fcf_yield_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_063_fcf_yield_rank_5d},
    "cflo_064_fcf_yield_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_064_fcf_yield_lvl_21d},
    "cflo_065_fcf_yield_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_065_fcf_yield_zscore_21d},
    "cflo_066_fcf_yield_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_066_fcf_yield_rank_21d},
    "cflo_067_fcf_yield_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_067_fcf_yield_lvl_63d},
    "cflo_068_fcf_yield_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_068_fcf_yield_zscore_63d},
    "cflo_069_fcf_yield_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_069_fcf_yield_rank_63d},
    "cflo_070_fcf_yield_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_070_fcf_yield_lvl_126d},
    "cflo_071_fcf_yield_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_071_fcf_yield_zscore_126d},
    "cflo_072_fcf_yield_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_072_fcf_yield_rank_126d},
    "cflo_073_fcf_yield_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_073_fcf_yield_lvl_252d},
    "cflo_074_fcf_yield_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_074_fcf_yield_zscore_252d},
    "cflo_075_fcf_yield_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_075_fcf_yield_rank_252d},
}
