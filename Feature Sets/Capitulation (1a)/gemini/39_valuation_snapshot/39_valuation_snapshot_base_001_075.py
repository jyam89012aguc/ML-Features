"""
39_valuation_snapshot — Base Features 001-075
Domain: valuation_snapshot
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

def valn_001_ps_lvl_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_001_ps_lvl_5d"""
    base = ps
    return _rolling_mean(base, 5)

def valn_002_ps_zscore_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_002_ps_zscore_5d"""
    base = ps
    return _zscore_rolling(base, 5)

def valn_003_ps_rank_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_003_ps_rank_5d"""
    base = ps
    return _rank_pct(base, 5)

def valn_004_ps_lvl_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_004_ps_lvl_21d"""
    base = ps
    return _rolling_mean(base, 21)

def valn_005_ps_zscore_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_005_ps_zscore_21d"""
    base = ps
    return _zscore_rolling(base, 21)

def valn_006_ps_rank_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_006_ps_rank_21d"""
    base = ps
    return _rank_pct(base, 21)

def valn_007_ps_lvl_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_007_ps_lvl_63d"""
    base = ps
    return _rolling_mean(base, 63)

def valn_008_ps_zscore_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_008_ps_zscore_63d"""
    base = ps
    return _zscore_rolling(base, 63)

def valn_009_ps_rank_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_009_ps_rank_63d"""
    base = ps
    return _rank_pct(base, 63)

def valn_010_ps_lvl_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_010_ps_lvl_126d"""
    base = ps
    return _rolling_mean(base, 126)

def valn_011_ps_zscore_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_011_ps_zscore_126d"""
    base = ps
    return _zscore_rolling(base, 126)

def valn_012_ps_rank_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_012_ps_rank_126d"""
    base = ps
    return _rank_pct(base, 126)

def valn_013_ps_lvl_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_013_ps_lvl_252d"""
    base = ps
    return _rolling_mean(base, 252)

def valn_014_ps_zscore_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_014_ps_zscore_252d"""
    base = ps
    return _zscore_rolling(base, 252)

def valn_015_ps_rank_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_015_ps_rank_252d"""
    base = ps
    return _rank_pct(base, 252)

def valn_016_pb_lvl_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_016_pb_lvl_5d"""
    base = pb
    return _rolling_mean(base, 5)

def valn_017_pb_zscore_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_017_pb_zscore_5d"""
    base = pb
    return _zscore_rolling(base, 5)

def valn_018_pb_rank_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_018_pb_rank_5d"""
    base = pb
    return _rank_pct(base, 5)

def valn_019_pb_lvl_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_019_pb_lvl_21d"""
    base = pb
    return _rolling_mean(base, 21)

def valn_020_pb_zscore_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_020_pb_zscore_21d"""
    base = pb
    return _zscore_rolling(base, 21)

def valn_021_pb_rank_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_021_pb_rank_21d"""
    base = pb
    return _rank_pct(base, 21)

def valn_022_pb_lvl_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_022_pb_lvl_63d"""
    base = pb
    return _rolling_mean(base, 63)

def valn_023_pb_zscore_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_023_pb_zscore_63d"""
    base = pb
    return _zscore_rolling(base, 63)

def valn_024_pb_rank_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_024_pb_rank_63d"""
    base = pb
    return _rank_pct(base, 63)

def valn_025_pb_lvl_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_025_pb_lvl_126d"""
    base = pb
    return _rolling_mean(base, 126)

def valn_026_pb_zscore_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_026_pb_zscore_126d"""
    base = pb
    return _zscore_rolling(base, 126)

def valn_027_pb_rank_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_027_pb_rank_126d"""
    base = pb
    return _rank_pct(base, 126)

def valn_028_pb_lvl_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_028_pb_lvl_252d"""
    base = pb
    return _rolling_mean(base, 252)

def valn_029_pb_zscore_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_029_pb_zscore_252d"""
    base = pb
    return _zscore_rolling(base, 252)

def valn_030_pb_rank_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_030_pb_rank_252d"""
    base = pb
    return _rank_pct(base, 252)

def valn_031_pe_lvl_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_031_pe_lvl_5d"""
    base = pe
    return _rolling_mean(base, 5)

def valn_032_pe_zscore_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_032_pe_zscore_5d"""
    base = pe
    return _zscore_rolling(base, 5)

def valn_033_pe_rank_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_033_pe_rank_5d"""
    base = pe
    return _rank_pct(base, 5)

def valn_034_pe_lvl_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_034_pe_lvl_21d"""
    base = pe
    return _rolling_mean(base, 21)

def valn_035_pe_zscore_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_035_pe_zscore_21d"""
    base = pe
    return _zscore_rolling(base, 21)

def valn_036_pe_rank_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_036_pe_rank_21d"""
    base = pe
    return _rank_pct(base, 21)

def valn_037_pe_lvl_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_037_pe_lvl_63d"""
    base = pe
    return _rolling_mean(base, 63)

def valn_038_pe_zscore_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_038_pe_zscore_63d"""
    base = pe
    return _zscore_rolling(base, 63)

def valn_039_pe_rank_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_039_pe_rank_63d"""
    base = pe
    return _rank_pct(base, 63)

def valn_040_pe_lvl_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_040_pe_lvl_126d"""
    base = pe
    return _rolling_mean(base, 126)

def valn_041_pe_zscore_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_041_pe_zscore_126d"""
    base = pe
    return _zscore_rolling(base, 126)

def valn_042_pe_rank_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_042_pe_rank_126d"""
    base = pe
    return _rank_pct(base, 126)

def valn_043_pe_lvl_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_043_pe_lvl_252d"""
    base = pe
    return _rolling_mean(base, 252)

def valn_044_pe_zscore_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_044_pe_zscore_252d"""
    base = pe
    return _zscore_rolling(base, 252)

def valn_045_pe_rank_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_045_pe_rank_252d"""
    base = pe
    return _rank_pct(base, 252)

def valn_046_evebitda_lvl_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_046_evebitda_lvl_5d"""
    base = evebitda
    return _rolling_mean(base, 5)

def valn_047_evebitda_zscore_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_047_evebitda_zscore_5d"""
    base = evebitda
    return _zscore_rolling(base, 5)

def valn_048_evebitda_rank_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_048_evebitda_rank_5d"""
    base = evebitda
    return _rank_pct(base, 5)

def valn_049_evebitda_lvl_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_049_evebitda_lvl_21d"""
    base = evebitda
    return _rolling_mean(base, 21)

def valn_050_evebitda_zscore_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_050_evebitda_zscore_21d"""
    base = evebitda
    return _zscore_rolling(base, 21)

def valn_051_evebitda_rank_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_051_evebitda_rank_21d"""
    base = evebitda
    return _rank_pct(base, 21)

def valn_052_evebitda_lvl_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_052_evebitda_lvl_63d"""
    base = evebitda
    return _rolling_mean(base, 63)

def valn_053_evebitda_zscore_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_053_evebitda_zscore_63d"""
    base = evebitda
    return _zscore_rolling(base, 63)

def valn_054_evebitda_rank_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_054_evebitda_rank_63d"""
    base = evebitda
    return _rank_pct(base, 63)

def valn_055_evebitda_lvl_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_055_evebitda_lvl_126d"""
    base = evebitda
    return _rolling_mean(base, 126)

def valn_056_evebitda_zscore_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_056_evebitda_zscore_126d"""
    base = evebitda
    return _zscore_rolling(base, 126)

def valn_057_evebitda_rank_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_057_evebitda_rank_126d"""
    base = evebitda
    return _rank_pct(base, 126)

def valn_058_evebitda_lvl_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_058_evebitda_lvl_252d"""
    base = evebitda
    return _rolling_mean(base, 252)

def valn_059_evebitda_zscore_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_059_evebitda_zscore_252d"""
    base = evebitda
    return _zscore_rolling(base, 252)

def valn_060_evebitda_rank_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_060_evebitda_rank_252d"""
    base = evebitda
    return _rank_pct(base, 252)

def valn_061_earn_yield_lvl_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_061_earn_yield_lvl_5d"""
    base = _safe_div(1.0, pe)
    return _rolling_mean(base, 5)

def valn_062_earn_yield_zscore_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_062_earn_yield_zscore_5d"""
    base = _safe_div(1.0, pe)
    return _zscore_rolling(base, 5)

def valn_063_earn_yield_rank_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_063_earn_yield_rank_5d"""
    base = _safe_div(1.0, pe)
    return _rank_pct(base, 5)

def valn_064_earn_yield_lvl_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_064_earn_yield_lvl_21d"""
    base = _safe_div(1.0, pe)
    return _rolling_mean(base, 21)

def valn_065_earn_yield_zscore_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_065_earn_yield_zscore_21d"""
    base = _safe_div(1.0, pe)
    return _zscore_rolling(base, 21)

def valn_066_earn_yield_rank_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_066_earn_yield_rank_21d"""
    base = _safe_div(1.0, pe)
    return _rank_pct(base, 21)

def valn_067_earn_yield_lvl_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_067_earn_yield_lvl_63d"""
    base = _safe_div(1.0, pe)
    return _rolling_mean(base, 63)

def valn_068_earn_yield_zscore_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_068_earn_yield_zscore_63d"""
    base = _safe_div(1.0, pe)
    return _zscore_rolling(base, 63)

def valn_069_earn_yield_rank_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_069_earn_yield_rank_63d"""
    base = _safe_div(1.0, pe)
    return _rank_pct(base, 63)

def valn_070_earn_yield_lvl_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_070_earn_yield_lvl_126d"""
    base = _safe_div(1.0, pe)
    return _rolling_mean(base, 126)

def valn_071_earn_yield_zscore_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_071_earn_yield_zscore_126d"""
    base = _safe_div(1.0, pe)
    return _zscore_rolling(base, 126)

def valn_072_earn_yield_rank_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_072_earn_yield_rank_126d"""
    base = _safe_div(1.0, pe)
    return _rank_pct(base, 126)

def valn_073_earn_yield_lvl_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_073_earn_yield_lvl_252d"""
    base = _safe_div(1.0, pe)
    return _rolling_mean(base, 252)

def valn_074_earn_yield_zscore_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_074_earn_yield_zscore_252d"""
    base = _safe_div(1.0, pe)
    return _zscore_rolling(base, 252)

def valn_075_earn_yield_rank_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_075_earn_yield_rank_252d"""
    base = _safe_div(1.0, pe)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V39_REGISTRY = {
    "valn_001_ps_lvl_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_001_ps_lvl_5d},
    "valn_002_ps_zscore_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_002_ps_zscore_5d},
    "valn_003_ps_rank_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_003_ps_rank_5d},
    "valn_004_ps_lvl_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_004_ps_lvl_21d},
    "valn_005_ps_zscore_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_005_ps_zscore_21d},
    "valn_006_ps_rank_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_006_ps_rank_21d},
    "valn_007_ps_lvl_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_007_ps_lvl_63d},
    "valn_008_ps_zscore_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_008_ps_zscore_63d},
    "valn_009_ps_rank_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_009_ps_rank_63d},
    "valn_010_ps_lvl_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_010_ps_lvl_126d},
    "valn_011_ps_zscore_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_011_ps_zscore_126d},
    "valn_012_ps_rank_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_012_ps_rank_126d},
    "valn_013_ps_lvl_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_013_ps_lvl_252d},
    "valn_014_ps_zscore_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_014_ps_zscore_252d},
    "valn_015_ps_rank_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_015_ps_rank_252d},
    "valn_016_pb_lvl_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_016_pb_lvl_5d},
    "valn_017_pb_zscore_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_017_pb_zscore_5d},
    "valn_018_pb_rank_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_018_pb_rank_5d},
    "valn_019_pb_lvl_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_019_pb_lvl_21d},
    "valn_020_pb_zscore_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_020_pb_zscore_21d},
    "valn_021_pb_rank_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_021_pb_rank_21d},
    "valn_022_pb_lvl_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_022_pb_lvl_63d},
    "valn_023_pb_zscore_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_023_pb_zscore_63d},
    "valn_024_pb_rank_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_024_pb_rank_63d},
    "valn_025_pb_lvl_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_025_pb_lvl_126d},
    "valn_026_pb_zscore_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_026_pb_zscore_126d},
    "valn_027_pb_rank_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_027_pb_rank_126d},
    "valn_028_pb_lvl_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_028_pb_lvl_252d},
    "valn_029_pb_zscore_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_029_pb_zscore_252d},
    "valn_030_pb_rank_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_030_pb_rank_252d},
    "valn_031_pe_lvl_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_031_pe_lvl_5d},
    "valn_032_pe_zscore_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_032_pe_zscore_5d},
    "valn_033_pe_rank_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_033_pe_rank_5d},
    "valn_034_pe_lvl_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_034_pe_lvl_21d},
    "valn_035_pe_zscore_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_035_pe_zscore_21d},
    "valn_036_pe_rank_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_036_pe_rank_21d},
    "valn_037_pe_lvl_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_037_pe_lvl_63d},
    "valn_038_pe_zscore_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_038_pe_zscore_63d},
    "valn_039_pe_rank_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_039_pe_rank_63d},
    "valn_040_pe_lvl_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_040_pe_lvl_126d},
    "valn_041_pe_zscore_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_041_pe_zscore_126d},
    "valn_042_pe_rank_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_042_pe_rank_126d},
    "valn_043_pe_lvl_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_043_pe_lvl_252d},
    "valn_044_pe_zscore_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_044_pe_zscore_252d},
    "valn_045_pe_rank_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_045_pe_rank_252d},
    "valn_046_evebitda_lvl_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_046_evebitda_lvl_5d},
    "valn_047_evebitda_zscore_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_047_evebitda_zscore_5d},
    "valn_048_evebitda_rank_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_048_evebitda_rank_5d},
    "valn_049_evebitda_lvl_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_049_evebitda_lvl_21d},
    "valn_050_evebitda_zscore_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_050_evebitda_zscore_21d},
    "valn_051_evebitda_rank_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_051_evebitda_rank_21d},
    "valn_052_evebitda_lvl_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_052_evebitda_lvl_63d},
    "valn_053_evebitda_zscore_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_053_evebitda_zscore_63d},
    "valn_054_evebitda_rank_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_054_evebitda_rank_63d},
    "valn_055_evebitda_lvl_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_055_evebitda_lvl_126d},
    "valn_056_evebitda_zscore_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_056_evebitda_zscore_126d},
    "valn_057_evebitda_rank_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_057_evebitda_rank_126d},
    "valn_058_evebitda_lvl_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_058_evebitda_lvl_252d},
    "valn_059_evebitda_zscore_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_059_evebitda_zscore_252d},
    "valn_060_evebitda_rank_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_060_evebitda_rank_252d},
    "valn_061_earn_yield_lvl_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_061_earn_yield_lvl_5d},
    "valn_062_earn_yield_zscore_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_062_earn_yield_zscore_5d},
    "valn_063_earn_yield_rank_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_063_earn_yield_rank_5d},
    "valn_064_earn_yield_lvl_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_064_earn_yield_lvl_21d},
    "valn_065_earn_yield_zscore_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_065_earn_yield_zscore_21d},
    "valn_066_earn_yield_rank_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_066_earn_yield_rank_21d},
    "valn_067_earn_yield_lvl_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_067_earn_yield_lvl_63d},
    "valn_068_earn_yield_zscore_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_068_earn_yield_zscore_63d},
    "valn_069_earn_yield_rank_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_069_earn_yield_rank_63d},
    "valn_070_earn_yield_lvl_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_070_earn_yield_lvl_126d},
    "valn_071_earn_yield_zscore_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_071_earn_yield_zscore_126d},
    "valn_072_earn_yield_rank_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_072_earn_yield_rank_126d},
    "valn_073_earn_yield_lvl_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_073_earn_yield_lvl_252d},
    "valn_074_earn_yield_zscore_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_074_earn_yield_zscore_252d},
    "valn_075_earn_yield_rank_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_075_earn_yield_rank_252d},
}
