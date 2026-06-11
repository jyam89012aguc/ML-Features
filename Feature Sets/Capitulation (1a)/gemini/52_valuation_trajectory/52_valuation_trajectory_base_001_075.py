"""
52_valuation_trajectory — Base Features 001-075
Domain: valuation_trajectory
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

def valt_001_ps_ratio_lvl_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_001_ps_ratio_lvl_5d"""
    base = ps
    return _rolling_mean(base, 5)

def valt_002_ps_ratio_zscore_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_002_ps_ratio_zscore_5d"""
    base = ps
    return _zscore_rolling(base, 5)

def valt_003_ps_ratio_rank_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_003_ps_ratio_rank_5d"""
    base = ps
    return _rank_pct(base, 5)

def valt_004_ps_ratio_lvl_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_004_ps_ratio_lvl_21d"""
    base = ps
    return _rolling_mean(base, 21)

def valt_005_ps_ratio_zscore_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_005_ps_ratio_zscore_21d"""
    base = ps
    return _zscore_rolling(base, 21)

def valt_006_ps_ratio_rank_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_006_ps_ratio_rank_21d"""
    base = ps
    return _rank_pct(base, 21)

def valt_007_ps_ratio_lvl_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_007_ps_ratio_lvl_63d"""
    base = ps
    return _rolling_mean(base, 63)

def valt_008_ps_ratio_zscore_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_008_ps_ratio_zscore_63d"""
    base = ps
    return _zscore_rolling(base, 63)

def valt_009_ps_ratio_rank_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_009_ps_ratio_rank_63d"""
    base = ps
    return _rank_pct(base, 63)

def valt_010_ps_ratio_lvl_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_010_ps_ratio_lvl_126d"""
    base = ps
    return _rolling_mean(base, 126)

def valt_011_ps_ratio_zscore_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_011_ps_ratio_zscore_126d"""
    base = ps
    return _zscore_rolling(base, 126)

def valt_012_ps_ratio_rank_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_012_ps_ratio_rank_126d"""
    base = ps
    return _rank_pct(base, 126)

def valt_013_ps_ratio_lvl_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_013_ps_ratio_lvl_252d"""
    base = ps
    return _rolling_mean(base, 252)

def valt_014_ps_ratio_zscore_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_014_ps_ratio_zscore_252d"""
    base = ps
    return _zscore_rolling(base, 252)

def valt_015_ps_ratio_rank_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_015_ps_ratio_rank_252d"""
    base = ps
    return _rank_pct(base, 252)

def valt_016_pb_ratio_lvl_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_016_pb_ratio_lvl_5d"""
    base = pb
    return _rolling_mean(base, 5)

def valt_017_pb_ratio_zscore_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_017_pb_ratio_zscore_5d"""
    base = pb
    return _zscore_rolling(base, 5)

def valt_018_pb_ratio_rank_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_018_pb_ratio_rank_5d"""
    base = pb
    return _rank_pct(base, 5)

def valt_019_pb_ratio_lvl_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_019_pb_ratio_lvl_21d"""
    base = pb
    return _rolling_mean(base, 21)

def valt_020_pb_ratio_zscore_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_020_pb_ratio_zscore_21d"""
    base = pb
    return _zscore_rolling(base, 21)

def valt_021_pb_ratio_rank_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_021_pb_ratio_rank_21d"""
    base = pb
    return _rank_pct(base, 21)

def valt_022_pb_ratio_lvl_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_022_pb_ratio_lvl_63d"""
    base = pb
    return _rolling_mean(base, 63)

def valt_023_pb_ratio_zscore_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_023_pb_ratio_zscore_63d"""
    base = pb
    return _zscore_rolling(base, 63)

def valt_024_pb_ratio_rank_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_024_pb_ratio_rank_63d"""
    base = pb
    return _rank_pct(base, 63)

def valt_025_pb_ratio_lvl_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_025_pb_ratio_lvl_126d"""
    base = pb
    return _rolling_mean(base, 126)

def valt_026_pb_ratio_zscore_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_026_pb_ratio_zscore_126d"""
    base = pb
    return _zscore_rolling(base, 126)

def valt_027_pb_ratio_rank_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_027_pb_ratio_rank_126d"""
    base = pb
    return _rank_pct(base, 126)

def valt_028_pb_ratio_lvl_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_028_pb_ratio_lvl_252d"""
    base = pb
    return _rolling_mean(base, 252)

def valt_029_pb_ratio_zscore_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_029_pb_ratio_zscore_252d"""
    base = pb
    return _zscore_rolling(base, 252)

def valt_030_pb_ratio_rank_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_030_pb_ratio_rank_252d"""
    base = pb
    return _rank_pct(base, 252)

def valt_031_pe_ratio_lvl_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_031_pe_ratio_lvl_5d"""
    base = _safe_div(marketcap, netinc)
    return _rolling_mean(base, 5)

def valt_032_pe_ratio_zscore_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_032_pe_ratio_zscore_5d"""
    base = _safe_div(marketcap, netinc)
    return _zscore_rolling(base, 5)

def valt_033_pe_ratio_rank_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_033_pe_ratio_rank_5d"""
    base = _safe_div(marketcap, netinc)
    return _rank_pct(base, 5)

def valt_034_pe_ratio_lvl_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_034_pe_ratio_lvl_21d"""
    base = _safe_div(marketcap, netinc)
    return _rolling_mean(base, 21)

def valt_035_pe_ratio_zscore_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_035_pe_ratio_zscore_21d"""
    base = _safe_div(marketcap, netinc)
    return _zscore_rolling(base, 21)

def valt_036_pe_ratio_rank_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_036_pe_ratio_rank_21d"""
    base = _safe_div(marketcap, netinc)
    return _rank_pct(base, 21)

def valt_037_pe_ratio_lvl_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_037_pe_ratio_lvl_63d"""
    base = _safe_div(marketcap, netinc)
    return _rolling_mean(base, 63)

def valt_038_pe_ratio_zscore_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_038_pe_ratio_zscore_63d"""
    base = _safe_div(marketcap, netinc)
    return _zscore_rolling(base, 63)

def valt_039_pe_ratio_rank_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_039_pe_ratio_rank_63d"""
    base = _safe_div(marketcap, netinc)
    return _rank_pct(base, 63)

def valt_040_pe_ratio_lvl_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_040_pe_ratio_lvl_126d"""
    base = _safe_div(marketcap, netinc)
    return _rolling_mean(base, 126)

def valt_041_pe_ratio_zscore_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_041_pe_ratio_zscore_126d"""
    base = _safe_div(marketcap, netinc)
    return _zscore_rolling(base, 126)

def valt_042_pe_ratio_rank_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_042_pe_ratio_rank_126d"""
    base = _safe_div(marketcap, netinc)
    return _rank_pct(base, 126)

def valt_043_pe_ratio_lvl_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_043_pe_ratio_lvl_252d"""
    base = _safe_div(marketcap, netinc)
    return _rolling_mean(base, 252)

def valt_044_pe_ratio_zscore_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_044_pe_ratio_zscore_252d"""
    base = _safe_div(marketcap, netinc)
    return _zscore_rolling(base, 252)

def valt_045_pe_ratio_rank_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_045_pe_ratio_rank_252d"""
    base = _safe_div(marketcap, netinc)
    return _rank_pct(base, 252)

def valt_046_ev_rev_lvl_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_046_ev_rev_lvl_5d"""
    base = _safe_div(marketcap, revenue)
    return _rolling_mean(base, 5)

def valt_047_ev_rev_zscore_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_047_ev_rev_zscore_5d"""
    base = _safe_div(marketcap, revenue)
    return _zscore_rolling(base, 5)

def valt_048_ev_rev_rank_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_048_ev_rev_rank_5d"""
    base = _safe_div(marketcap, revenue)
    return _rank_pct(base, 5)

def valt_049_ev_rev_lvl_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_049_ev_rev_lvl_21d"""
    base = _safe_div(marketcap, revenue)
    return _rolling_mean(base, 21)

def valt_050_ev_rev_zscore_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_050_ev_rev_zscore_21d"""
    base = _safe_div(marketcap, revenue)
    return _zscore_rolling(base, 21)

def valt_051_ev_rev_rank_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_051_ev_rev_rank_21d"""
    base = _safe_div(marketcap, revenue)
    return _rank_pct(base, 21)

def valt_052_ev_rev_lvl_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_052_ev_rev_lvl_63d"""
    base = _safe_div(marketcap, revenue)
    return _rolling_mean(base, 63)

def valt_053_ev_rev_zscore_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_053_ev_rev_zscore_63d"""
    base = _safe_div(marketcap, revenue)
    return _zscore_rolling(base, 63)

def valt_054_ev_rev_rank_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_054_ev_rev_rank_63d"""
    base = _safe_div(marketcap, revenue)
    return _rank_pct(base, 63)

def valt_055_ev_rev_lvl_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_055_ev_rev_lvl_126d"""
    base = _safe_div(marketcap, revenue)
    return _rolling_mean(base, 126)

def valt_056_ev_rev_zscore_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_056_ev_rev_zscore_126d"""
    base = _safe_div(marketcap, revenue)
    return _zscore_rolling(base, 126)

def valt_057_ev_rev_rank_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_057_ev_rev_rank_126d"""
    base = _safe_div(marketcap, revenue)
    return _rank_pct(base, 126)

def valt_058_ev_rev_lvl_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_058_ev_rev_lvl_252d"""
    base = _safe_div(marketcap, revenue)
    return _rolling_mean(base, 252)

def valt_059_ev_rev_zscore_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_059_ev_rev_zscore_252d"""
    base = _safe_div(marketcap, revenue)
    return _zscore_rolling(base, 252)

def valt_060_ev_rev_rank_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_060_ev_rev_rank_252d"""
    base = _safe_div(marketcap, revenue)
    return _rank_pct(base, 252)

def valt_061_yield_ocf_lvl_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_061_yield_ocf_lvl_5d"""
    base = _safe_div(ocf, marketcap)
    return _rolling_mean(base, 5)

def valt_062_yield_ocf_zscore_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_062_yield_ocf_zscore_5d"""
    base = _safe_div(ocf, marketcap)
    return _zscore_rolling(base, 5)

def valt_063_yield_ocf_rank_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_063_yield_ocf_rank_5d"""
    base = _safe_div(ocf, marketcap)
    return _rank_pct(base, 5)

def valt_064_yield_ocf_lvl_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_064_yield_ocf_lvl_21d"""
    base = _safe_div(ocf, marketcap)
    return _rolling_mean(base, 21)

def valt_065_yield_ocf_zscore_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_065_yield_ocf_zscore_21d"""
    base = _safe_div(ocf, marketcap)
    return _zscore_rolling(base, 21)

def valt_066_yield_ocf_rank_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_066_yield_ocf_rank_21d"""
    base = _safe_div(ocf, marketcap)
    return _rank_pct(base, 21)

def valt_067_yield_ocf_lvl_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_067_yield_ocf_lvl_63d"""
    base = _safe_div(ocf, marketcap)
    return _rolling_mean(base, 63)

def valt_068_yield_ocf_zscore_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_068_yield_ocf_zscore_63d"""
    base = _safe_div(ocf, marketcap)
    return _zscore_rolling(base, 63)

def valt_069_yield_ocf_rank_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_069_yield_ocf_rank_63d"""
    base = _safe_div(ocf, marketcap)
    return _rank_pct(base, 63)

def valt_070_yield_ocf_lvl_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_070_yield_ocf_lvl_126d"""
    base = _safe_div(ocf, marketcap)
    return _rolling_mean(base, 126)

def valt_071_yield_ocf_zscore_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_071_yield_ocf_zscore_126d"""
    base = _safe_div(ocf, marketcap)
    return _zscore_rolling(base, 126)

def valt_072_yield_ocf_rank_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_072_yield_ocf_rank_126d"""
    base = _safe_div(ocf, marketcap)
    return _rank_pct(base, 126)

def valt_073_yield_ocf_lvl_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_073_yield_ocf_lvl_252d"""
    base = _safe_div(ocf, marketcap)
    return _rolling_mean(base, 252)

def valt_074_yield_ocf_zscore_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_074_yield_ocf_zscore_252d"""
    base = _safe_div(ocf, marketcap)
    return _zscore_rolling(base, 252)

def valt_075_yield_ocf_rank_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_075_yield_ocf_rank_252d"""
    base = _safe_div(ocf, marketcap)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V52_REGISTRY = {
    "valt_001_ps_ratio_lvl_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_001_ps_ratio_lvl_5d},
    "valt_002_ps_ratio_zscore_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_002_ps_ratio_zscore_5d},
    "valt_003_ps_ratio_rank_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_003_ps_ratio_rank_5d},
    "valt_004_ps_ratio_lvl_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_004_ps_ratio_lvl_21d},
    "valt_005_ps_ratio_zscore_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_005_ps_ratio_zscore_21d},
    "valt_006_ps_ratio_rank_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_006_ps_ratio_rank_21d},
    "valt_007_ps_ratio_lvl_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_007_ps_ratio_lvl_63d},
    "valt_008_ps_ratio_zscore_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_008_ps_ratio_zscore_63d},
    "valt_009_ps_ratio_rank_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_009_ps_ratio_rank_63d},
    "valt_010_ps_ratio_lvl_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_010_ps_ratio_lvl_126d},
    "valt_011_ps_ratio_zscore_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_011_ps_ratio_zscore_126d},
    "valt_012_ps_ratio_rank_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_012_ps_ratio_rank_126d},
    "valt_013_ps_ratio_lvl_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_013_ps_ratio_lvl_252d},
    "valt_014_ps_ratio_zscore_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_014_ps_ratio_zscore_252d},
    "valt_015_ps_ratio_rank_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_015_ps_ratio_rank_252d},
    "valt_016_pb_ratio_lvl_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_016_pb_ratio_lvl_5d},
    "valt_017_pb_ratio_zscore_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_017_pb_ratio_zscore_5d},
    "valt_018_pb_ratio_rank_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_018_pb_ratio_rank_5d},
    "valt_019_pb_ratio_lvl_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_019_pb_ratio_lvl_21d},
    "valt_020_pb_ratio_zscore_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_020_pb_ratio_zscore_21d},
    "valt_021_pb_ratio_rank_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_021_pb_ratio_rank_21d},
    "valt_022_pb_ratio_lvl_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_022_pb_ratio_lvl_63d},
    "valt_023_pb_ratio_zscore_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_023_pb_ratio_zscore_63d},
    "valt_024_pb_ratio_rank_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_024_pb_ratio_rank_63d},
    "valt_025_pb_ratio_lvl_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_025_pb_ratio_lvl_126d},
    "valt_026_pb_ratio_zscore_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_026_pb_ratio_zscore_126d},
    "valt_027_pb_ratio_rank_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_027_pb_ratio_rank_126d},
    "valt_028_pb_ratio_lvl_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_028_pb_ratio_lvl_252d},
    "valt_029_pb_ratio_zscore_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_029_pb_ratio_zscore_252d},
    "valt_030_pb_ratio_rank_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_030_pb_ratio_rank_252d},
    "valt_031_pe_ratio_lvl_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_031_pe_ratio_lvl_5d},
    "valt_032_pe_ratio_zscore_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_032_pe_ratio_zscore_5d},
    "valt_033_pe_ratio_rank_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_033_pe_ratio_rank_5d},
    "valt_034_pe_ratio_lvl_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_034_pe_ratio_lvl_21d},
    "valt_035_pe_ratio_zscore_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_035_pe_ratio_zscore_21d},
    "valt_036_pe_ratio_rank_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_036_pe_ratio_rank_21d},
    "valt_037_pe_ratio_lvl_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_037_pe_ratio_lvl_63d},
    "valt_038_pe_ratio_zscore_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_038_pe_ratio_zscore_63d},
    "valt_039_pe_ratio_rank_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_039_pe_ratio_rank_63d},
    "valt_040_pe_ratio_lvl_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_040_pe_ratio_lvl_126d},
    "valt_041_pe_ratio_zscore_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_041_pe_ratio_zscore_126d},
    "valt_042_pe_ratio_rank_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_042_pe_ratio_rank_126d},
    "valt_043_pe_ratio_lvl_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_043_pe_ratio_lvl_252d},
    "valt_044_pe_ratio_zscore_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_044_pe_ratio_zscore_252d},
    "valt_045_pe_ratio_rank_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_045_pe_ratio_rank_252d},
    "valt_046_ev_rev_lvl_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_046_ev_rev_lvl_5d},
    "valt_047_ev_rev_zscore_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_047_ev_rev_zscore_5d},
    "valt_048_ev_rev_rank_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_048_ev_rev_rank_5d},
    "valt_049_ev_rev_lvl_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_049_ev_rev_lvl_21d},
    "valt_050_ev_rev_zscore_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_050_ev_rev_zscore_21d},
    "valt_051_ev_rev_rank_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_051_ev_rev_rank_21d},
    "valt_052_ev_rev_lvl_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_052_ev_rev_lvl_63d},
    "valt_053_ev_rev_zscore_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_053_ev_rev_zscore_63d},
    "valt_054_ev_rev_rank_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_054_ev_rev_rank_63d},
    "valt_055_ev_rev_lvl_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_055_ev_rev_lvl_126d},
    "valt_056_ev_rev_zscore_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_056_ev_rev_zscore_126d},
    "valt_057_ev_rev_rank_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_057_ev_rev_rank_126d},
    "valt_058_ev_rev_lvl_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_058_ev_rev_lvl_252d},
    "valt_059_ev_rev_zscore_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_059_ev_rev_zscore_252d},
    "valt_060_ev_rev_rank_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_060_ev_rev_rank_252d},
    "valt_061_yield_ocf_lvl_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_061_yield_ocf_lvl_5d},
    "valt_062_yield_ocf_zscore_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_062_yield_ocf_zscore_5d},
    "valt_063_yield_ocf_rank_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_063_yield_ocf_rank_5d},
    "valt_064_yield_ocf_lvl_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_064_yield_ocf_lvl_21d},
    "valt_065_yield_ocf_zscore_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_065_yield_ocf_zscore_21d},
    "valt_066_yield_ocf_rank_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_066_yield_ocf_rank_21d},
    "valt_067_yield_ocf_lvl_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_067_yield_ocf_lvl_63d},
    "valt_068_yield_ocf_zscore_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_068_yield_ocf_zscore_63d},
    "valt_069_yield_ocf_rank_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_069_yield_ocf_rank_63d},
    "valt_070_yield_ocf_lvl_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_070_yield_ocf_lvl_126d},
    "valt_071_yield_ocf_zscore_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_071_yield_ocf_zscore_126d},
    "valt_072_yield_ocf_rank_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_072_yield_ocf_rank_126d},
    "valt_073_yield_ocf_lvl_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_073_yield_ocf_lvl_252d},
    "valt_074_yield_ocf_zscore_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_074_yield_ocf_zscore_252d},
    "valt_075_yield_ocf_rank_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_075_yield_ocf_rank_252d},
}
