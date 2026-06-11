"""
55_cash_flow_acceleration — Base Features 001-075
Domain: cash_flow_acceleration
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

def cfa_001_ocf_growth_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_001_ocf_growth_lvl_5d"""
    base = ocf.pct_change(252)
    return _rolling_mean(base, 5)

def cfa_002_ocf_growth_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_002_ocf_growth_zscore_5d"""
    base = ocf.pct_change(252)
    return _zscore_rolling(base, 5)

def cfa_003_ocf_growth_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_003_ocf_growth_rank_5d"""
    base = ocf.pct_change(252)
    return _rank_pct(base, 5)

def cfa_004_ocf_growth_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_004_ocf_growth_lvl_21d"""
    base = ocf.pct_change(252)
    return _rolling_mean(base, 21)

def cfa_005_ocf_growth_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_005_ocf_growth_zscore_21d"""
    base = ocf.pct_change(252)
    return _zscore_rolling(base, 21)

def cfa_006_ocf_growth_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_006_ocf_growth_rank_21d"""
    base = ocf.pct_change(252)
    return _rank_pct(base, 21)

def cfa_007_ocf_growth_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_007_ocf_growth_lvl_63d"""
    base = ocf.pct_change(252)
    return _rolling_mean(base, 63)

def cfa_008_ocf_growth_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_008_ocf_growth_zscore_63d"""
    base = ocf.pct_change(252)
    return _zscore_rolling(base, 63)

def cfa_009_ocf_growth_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_009_ocf_growth_rank_63d"""
    base = ocf.pct_change(252)
    return _rank_pct(base, 63)

def cfa_010_ocf_growth_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_010_ocf_growth_lvl_126d"""
    base = ocf.pct_change(252)
    return _rolling_mean(base, 126)

def cfa_011_ocf_growth_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_011_ocf_growth_zscore_126d"""
    base = ocf.pct_change(252)
    return _zscore_rolling(base, 126)

def cfa_012_ocf_growth_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_012_ocf_growth_rank_126d"""
    base = ocf.pct_change(252)
    return _rank_pct(base, 126)

def cfa_013_ocf_growth_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_013_ocf_growth_lvl_252d"""
    base = ocf.pct_change(252)
    return _rolling_mean(base, 252)

def cfa_014_ocf_growth_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_014_ocf_growth_zscore_252d"""
    base = ocf.pct_change(252)
    return _zscore_rolling(base, 252)

def cfa_015_ocf_growth_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_015_ocf_growth_rank_252d"""
    base = ocf.pct_change(252)
    return _rank_pct(base, 252)

def cfa_016_fcf_growth_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_016_fcf_growth_lvl_5d"""
    base = fcf.pct_change(252)
    return _rolling_mean(base, 5)

def cfa_017_fcf_growth_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_017_fcf_growth_zscore_5d"""
    base = fcf.pct_change(252)
    return _zscore_rolling(base, 5)

def cfa_018_fcf_growth_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_018_fcf_growth_rank_5d"""
    base = fcf.pct_change(252)
    return _rank_pct(base, 5)

def cfa_019_fcf_growth_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_019_fcf_growth_lvl_21d"""
    base = fcf.pct_change(252)
    return _rolling_mean(base, 21)

def cfa_020_fcf_growth_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_020_fcf_growth_zscore_21d"""
    base = fcf.pct_change(252)
    return _zscore_rolling(base, 21)

def cfa_021_fcf_growth_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_021_fcf_growth_rank_21d"""
    base = fcf.pct_change(252)
    return _rank_pct(base, 21)

def cfa_022_fcf_growth_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_022_fcf_growth_lvl_63d"""
    base = fcf.pct_change(252)
    return _rolling_mean(base, 63)

def cfa_023_fcf_growth_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_023_fcf_growth_zscore_63d"""
    base = fcf.pct_change(252)
    return _zscore_rolling(base, 63)

def cfa_024_fcf_growth_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_024_fcf_growth_rank_63d"""
    base = fcf.pct_change(252)
    return _rank_pct(base, 63)

def cfa_025_fcf_growth_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_025_fcf_growth_lvl_126d"""
    base = fcf.pct_change(252)
    return _rolling_mean(base, 126)

def cfa_026_fcf_growth_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_026_fcf_growth_zscore_126d"""
    base = fcf.pct_change(252)
    return _zscore_rolling(base, 126)

def cfa_027_fcf_growth_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_027_fcf_growth_rank_126d"""
    base = fcf.pct_change(252)
    return _rank_pct(base, 126)

def cfa_028_fcf_growth_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_028_fcf_growth_lvl_252d"""
    base = fcf.pct_change(252)
    return _rolling_mean(base, 252)

def cfa_029_fcf_growth_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_029_fcf_growth_zscore_252d"""
    base = fcf.pct_change(252)
    return _zscore_rolling(base, 252)

def cfa_030_fcf_growth_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_030_fcf_growth_rank_252d"""
    base = fcf.pct_change(252)
    return _rank_pct(base, 252)

def cfa_031_ocf_margin_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_031_ocf_margin_lvl_5d"""
    base = _safe_div(ocf, revenue)
    return _rolling_mean(base, 5)

def cfa_032_ocf_margin_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_032_ocf_margin_zscore_5d"""
    base = _safe_div(ocf, revenue)
    return _zscore_rolling(base, 5)

def cfa_033_ocf_margin_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_033_ocf_margin_rank_5d"""
    base = _safe_div(ocf, revenue)
    return _rank_pct(base, 5)

def cfa_034_ocf_margin_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_034_ocf_margin_lvl_21d"""
    base = _safe_div(ocf, revenue)
    return _rolling_mean(base, 21)

def cfa_035_ocf_margin_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_035_ocf_margin_zscore_21d"""
    base = _safe_div(ocf, revenue)
    return _zscore_rolling(base, 21)

def cfa_036_ocf_margin_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_036_ocf_margin_rank_21d"""
    base = _safe_div(ocf, revenue)
    return _rank_pct(base, 21)

def cfa_037_ocf_margin_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_037_ocf_margin_lvl_63d"""
    base = _safe_div(ocf, revenue)
    return _rolling_mean(base, 63)

def cfa_038_ocf_margin_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_038_ocf_margin_zscore_63d"""
    base = _safe_div(ocf, revenue)
    return _zscore_rolling(base, 63)

def cfa_039_ocf_margin_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_039_ocf_margin_rank_63d"""
    base = _safe_div(ocf, revenue)
    return _rank_pct(base, 63)

def cfa_040_ocf_margin_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_040_ocf_margin_lvl_126d"""
    base = _safe_div(ocf, revenue)
    return _rolling_mean(base, 126)

def cfa_041_ocf_margin_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_041_ocf_margin_zscore_126d"""
    base = _safe_div(ocf, revenue)
    return _zscore_rolling(base, 126)

def cfa_042_ocf_margin_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_042_ocf_margin_rank_126d"""
    base = _safe_div(ocf, revenue)
    return _rank_pct(base, 126)

def cfa_043_ocf_margin_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_043_ocf_margin_lvl_252d"""
    base = _safe_div(ocf, revenue)
    return _rolling_mean(base, 252)

def cfa_044_ocf_margin_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_044_ocf_margin_zscore_252d"""
    base = _safe_div(ocf, revenue)
    return _zscore_rolling(base, 252)

def cfa_045_ocf_margin_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_045_ocf_margin_rank_252d"""
    base = _safe_div(ocf, revenue)
    return _rank_pct(base, 252)

def cfa_046_fcf_margin_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_046_fcf_margin_lvl_5d"""
    base = _safe_div(fcf, revenue)
    return _rolling_mean(base, 5)

def cfa_047_fcf_margin_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_047_fcf_margin_zscore_5d"""
    base = _safe_div(fcf, revenue)
    return _zscore_rolling(base, 5)

def cfa_048_fcf_margin_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_048_fcf_margin_rank_5d"""
    base = _safe_div(fcf, revenue)
    return _rank_pct(base, 5)

def cfa_049_fcf_margin_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_049_fcf_margin_lvl_21d"""
    base = _safe_div(fcf, revenue)
    return _rolling_mean(base, 21)

def cfa_050_fcf_margin_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_050_fcf_margin_zscore_21d"""
    base = _safe_div(fcf, revenue)
    return _zscore_rolling(base, 21)

def cfa_051_fcf_margin_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_051_fcf_margin_rank_21d"""
    base = _safe_div(fcf, revenue)
    return _rank_pct(base, 21)

def cfa_052_fcf_margin_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_052_fcf_margin_lvl_63d"""
    base = _safe_div(fcf, revenue)
    return _rolling_mean(base, 63)

def cfa_053_fcf_margin_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_053_fcf_margin_zscore_63d"""
    base = _safe_div(fcf, revenue)
    return _zscore_rolling(base, 63)

def cfa_054_fcf_margin_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_054_fcf_margin_rank_63d"""
    base = _safe_div(fcf, revenue)
    return _rank_pct(base, 63)

def cfa_055_fcf_margin_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_055_fcf_margin_lvl_126d"""
    base = _safe_div(fcf, revenue)
    return _rolling_mean(base, 126)

def cfa_056_fcf_margin_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_056_fcf_margin_zscore_126d"""
    base = _safe_div(fcf, revenue)
    return _zscore_rolling(base, 126)

def cfa_057_fcf_margin_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_057_fcf_margin_rank_126d"""
    base = _safe_div(fcf, revenue)
    return _rank_pct(base, 126)

def cfa_058_fcf_margin_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_058_fcf_margin_lvl_252d"""
    base = _safe_div(fcf, revenue)
    return _rolling_mean(base, 252)

def cfa_059_fcf_margin_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_059_fcf_margin_zscore_252d"""
    base = _safe_div(fcf, revenue)
    return _zscore_rolling(base, 252)

def cfa_060_fcf_margin_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_060_fcf_margin_rank_252d"""
    base = _safe_div(fcf, revenue)
    return _rank_pct(base, 252)

def cfa_061_cash_conversion_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_061_cash_conversion_lvl_5d"""
    base = _safe_div(ocf, netinc)
    return _rolling_mean(base, 5)

def cfa_062_cash_conversion_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_062_cash_conversion_zscore_5d"""
    base = _safe_div(ocf, netinc)
    return _zscore_rolling(base, 5)

def cfa_063_cash_conversion_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_063_cash_conversion_rank_5d"""
    base = _safe_div(ocf, netinc)
    return _rank_pct(base, 5)

def cfa_064_cash_conversion_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_064_cash_conversion_lvl_21d"""
    base = _safe_div(ocf, netinc)
    return _rolling_mean(base, 21)

def cfa_065_cash_conversion_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_065_cash_conversion_zscore_21d"""
    base = _safe_div(ocf, netinc)
    return _zscore_rolling(base, 21)

def cfa_066_cash_conversion_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_066_cash_conversion_rank_21d"""
    base = _safe_div(ocf, netinc)
    return _rank_pct(base, 21)

def cfa_067_cash_conversion_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_067_cash_conversion_lvl_63d"""
    base = _safe_div(ocf, netinc)
    return _rolling_mean(base, 63)

def cfa_068_cash_conversion_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_068_cash_conversion_zscore_63d"""
    base = _safe_div(ocf, netinc)
    return _zscore_rolling(base, 63)

def cfa_069_cash_conversion_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_069_cash_conversion_rank_63d"""
    base = _safe_div(ocf, netinc)
    return _rank_pct(base, 63)

def cfa_070_cash_conversion_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_070_cash_conversion_lvl_126d"""
    base = _safe_div(ocf, netinc)
    return _rolling_mean(base, 126)

def cfa_071_cash_conversion_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_071_cash_conversion_zscore_126d"""
    base = _safe_div(ocf, netinc)
    return _zscore_rolling(base, 126)

def cfa_072_cash_conversion_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_072_cash_conversion_rank_126d"""
    base = _safe_div(ocf, netinc)
    return _rank_pct(base, 126)

def cfa_073_cash_conversion_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_073_cash_conversion_lvl_252d"""
    base = _safe_div(ocf, netinc)
    return _rolling_mean(base, 252)

def cfa_074_cash_conversion_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_074_cash_conversion_zscore_252d"""
    base = _safe_div(ocf, netinc)
    return _zscore_rolling(base, 252)

def cfa_075_cash_conversion_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_075_cash_conversion_rank_252d"""
    base = _safe_div(ocf, netinc)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V55_REGISTRY = {
    "cfa_001_ocf_growth_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_001_ocf_growth_lvl_5d},
    "cfa_002_ocf_growth_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_002_ocf_growth_zscore_5d},
    "cfa_003_ocf_growth_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_003_ocf_growth_rank_5d},
    "cfa_004_ocf_growth_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_004_ocf_growth_lvl_21d},
    "cfa_005_ocf_growth_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_005_ocf_growth_zscore_21d},
    "cfa_006_ocf_growth_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_006_ocf_growth_rank_21d},
    "cfa_007_ocf_growth_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_007_ocf_growth_lvl_63d},
    "cfa_008_ocf_growth_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_008_ocf_growth_zscore_63d},
    "cfa_009_ocf_growth_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_009_ocf_growth_rank_63d},
    "cfa_010_ocf_growth_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_010_ocf_growth_lvl_126d},
    "cfa_011_ocf_growth_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_011_ocf_growth_zscore_126d},
    "cfa_012_ocf_growth_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_012_ocf_growth_rank_126d},
    "cfa_013_ocf_growth_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_013_ocf_growth_lvl_252d},
    "cfa_014_ocf_growth_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_014_ocf_growth_zscore_252d},
    "cfa_015_ocf_growth_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_015_ocf_growth_rank_252d},
    "cfa_016_fcf_growth_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_016_fcf_growth_lvl_5d},
    "cfa_017_fcf_growth_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_017_fcf_growth_zscore_5d},
    "cfa_018_fcf_growth_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_018_fcf_growth_rank_5d},
    "cfa_019_fcf_growth_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_019_fcf_growth_lvl_21d},
    "cfa_020_fcf_growth_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_020_fcf_growth_zscore_21d},
    "cfa_021_fcf_growth_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_021_fcf_growth_rank_21d},
    "cfa_022_fcf_growth_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_022_fcf_growth_lvl_63d},
    "cfa_023_fcf_growth_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_023_fcf_growth_zscore_63d},
    "cfa_024_fcf_growth_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_024_fcf_growth_rank_63d},
    "cfa_025_fcf_growth_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_025_fcf_growth_lvl_126d},
    "cfa_026_fcf_growth_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_026_fcf_growth_zscore_126d},
    "cfa_027_fcf_growth_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_027_fcf_growth_rank_126d},
    "cfa_028_fcf_growth_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_028_fcf_growth_lvl_252d},
    "cfa_029_fcf_growth_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_029_fcf_growth_zscore_252d},
    "cfa_030_fcf_growth_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_030_fcf_growth_rank_252d},
    "cfa_031_ocf_margin_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_031_ocf_margin_lvl_5d},
    "cfa_032_ocf_margin_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_032_ocf_margin_zscore_5d},
    "cfa_033_ocf_margin_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_033_ocf_margin_rank_5d},
    "cfa_034_ocf_margin_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_034_ocf_margin_lvl_21d},
    "cfa_035_ocf_margin_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_035_ocf_margin_zscore_21d},
    "cfa_036_ocf_margin_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_036_ocf_margin_rank_21d},
    "cfa_037_ocf_margin_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_037_ocf_margin_lvl_63d},
    "cfa_038_ocf_margin_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_038_ocf_margin_zscore_63d},
    "cfa_039_ocf_margin_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_039_ocf_margin_rank_63d},
    "cfa_040_ocf_margin_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_040_ocf_margin_lvl_126d},
    "cfa_041_ocf_margin_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_041_ocf_margin_zscore_126d},
    "cfa_042_ocf_margin_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_042_ocf_margin_rank_126d},
    "cfa_043_ocf_margin_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_043_ocf_margin_lvl_252d},
    "cfa_044_ocf_margin_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_044_ocf_margin_zscore_252d},
    "cfa_045_ocf_margin_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_045_ocf_margin_rank_252d},
    "cfa_046_fcf_margin_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_046_fcf_margin_lvl_5d},
    "cfa_047_fcf_margin_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_047_fcf_margin_zscore_5d},
    "cfa_048_fcf_margin_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_048_fcf_margin_rank_5d},
    "cfa_049_fcf_margin_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_049_fcf_margin_lvl_21d},
    "cfa_050_fcf_margin_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_050_fcf_margin_zscore_21d},
    "cfa_051_fcf_margin_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_051_fcf_margin_rank_21d},
    "cfa_052_fcf_margin_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_052_fcf_margin_lvl_63d},
    "cfa_053_fcf_margin_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_053_fcf_margin_zscore_63d},
    "cfa_054_fcf_margin_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_054_fcf_margin_rank_63d},
    "cfa_055_fcf_margin_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_055_fcf_margin_lvl_126d},
    "cfa_056_fcf_margin_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_056_fcf_margin_zscore_126d},
    "cfa_057_fcf_margin_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_057_fcf_margin_rank_126d},
    "cfa_058_fcf_margin_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_058_fcf_margin_lvl_252d},
    "cfa_059_fcf_margin_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_059_fcf_margin_zscore_252d},
    "cfa_060_fcf_margin_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_060_fcf_margin_rank_252d},
    "cfa_061_cash_conversion_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_061_cash_conversion_lvl_5d},
    "cfa_062_cash_conversion_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_062_cash_conversion_zscore_5d},
    "cfa_063_cash_conversion_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_063_cash_conversion_rank_5d},
    "cfa_064_cash_conversion_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_064_cash_conversion_lvl_21d},
    "cfa_065_cash_conversion_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_065_cash_conversion_zscore_21d},
    "cfa_066_cash_conversion_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_066_cash_conversion_rank_21d},
    "cfa_067_cash_conversion_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_067_cash_conversion_lvl_63d},
    "cfa_068_cash_conversion_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_068_cash_conversion_zscore_63d},
    "cfa_069_cash_conversion_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_069_cash_conversion_rank_63d},
    "cfa_070_cash_conversion_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_070_cash_conversion_lvl_126d},
    "cfa_071_cash_conversion_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_071_cash_conversion_zscore_126d},
    "cfa_072_cash_conversion_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_072_cash_conversion_rank_126d},
    "cfa_073_cash_conversion_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_073_cash_conversion_lvl_252d},
    "cfa_074_cash_conversion_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_074_cash_conversion_zscore_252d},
    "cfa_075_cash_conversion_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_075_cash_conversion_rank_252d},
}
