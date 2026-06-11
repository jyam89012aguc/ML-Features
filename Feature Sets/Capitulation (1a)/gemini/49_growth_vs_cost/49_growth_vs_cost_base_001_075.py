"""
49_growth_vs_cost — Base Features 001-075
Domain: growth_vs_cost
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

def grco_001_op_leverage_lvl_5d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_001_op_leverage_lvl_5d"""
    base = _pct_change(revenue, 252) - _pct_change(opexp, 252)
    return _rolling_mean(base, 5)

def grco_002_op_leverage_zscore_5d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_002_op_leverage_zscore_5d"""
    base = _pct_change(revenue, 252) - _pct_change(opexp, 252)
    return _zscore_rolling(base, 5)

def grco_003_op_leverage_rank_5d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_003_op_leverage_rank_5d"""
    base = _pct_change(revenue, 252) - _pct_change(opexp, 252)
    return _rank_pct(base, 5)

def grco_004_op_leverage_lvl_21d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_004_op_leverage_lvl_21d"""
    base = _pct_change(revenue, 252) - _pct_change(opexp, 252)
    return _rolling_mean(base, 21)

def grco_005_op_leverage_zscore_21d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_005_op_leverage_zscore_21d"""
    base = _pct_change(revenue, 252) - _pct_change(opexp, 252)
    return _zscore_rolling(base, 21)

def grco_006_op_leverage_rank_21d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_006_op_leverage_rank_21d"""
    base = _pct_change(revenue, 252) - _pct_change(opexp, 252)
    return _rank_pct(base, 21)

def grco_007_op_leverage_lvl_63d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_007_op_leverage_lvl_63d"""
    base = _pct_change(revenue, 252) - _pct_change(opexp, 252)
    return _rolling_mean(base, 63)

def grco_008_op_leverage_zscore_63d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_008_op_leverage_zscore_63d"""
    base = _pct_change(revenue, 252) - _pct_change(opexp, 252)
    return _zscore_rolling(base, 63)

def grco_009_op_leverage_rank_63d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_009_op_leverage_rank_63d"""
    base = _pct_change(revenue, 252) - _pct_change(opexp, 252)
    return _rank_pct(base, 63)

def grco_010_op_leverage_lvl_126d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_010_op_leverage_lvl_126d"""
    base = _pct_change(revenue, 252) - _pct_change(opexp, 252)
    return _rolling_mean(base, 126)

def grco_011_op_leverage_zscore_126d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_011_op_leverage_zscore_126d"""
    base = _pct_change(revenue, 252) - _pct_change(opexp, 252)
    return _zscore_rolling(base, 126)

def grco_012_op_leverage_rank_126d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_012_op_leverage_rank_126d"""
    base = _pct_change(revenue, 252) - _pct_change(opexp, 252)
    return _rank_pct(base, 126)

def grco_013_op_leverage_lvl_252d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_013_op_leverage_lvl_252d"""
    base = _pct_change(revenue, 252) - _pct_change(opexp, 252)
    return _rolling_mean(base, 252)

def grco_014_op_leverage_zscore_252d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_014_op_leverage_zscore_252d"""
    base = _pct_change(revenue, 252) - _pct_change(opexp, 252)
    return _zscore_rolling(base, 252)

def grco_015_op_leverage_rank_252d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_015_op_leverage_rank_252d"""
    base = _pct_change(revenue, 252) - _pct_change(opexp, 252)
    return _rank_pct(base, 252)

def grco_016_gross_leverage_lvl_5d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_016_gross_leverage_lvl_5d"""
    base = _pct_change(revenue, 252) - _pct_change(cor, 252)
    return _rolling_mean(base, 5)

def grco_017_gross_leverage_zscore_5d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_017_gross_leverage_zscore_5d"""
    base = _pct_change(revenue, 252) - _pct_change(cor, 252)
    return _zscore_rolling(base, 5)

def grco_018_gross_leverage_rank_5d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_018_gross_leverage_rank_5d"""
    base = _pct_change(revenue, 252) - _pct_change(cor, 252)
    return _rank_pct(base, 5)

def grco_019_gross_leverage_lvl_21d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_019_gross_leverage_lvl_21d"""
    base = _pct_change(revenue, 252) - _pct_change(cor, 252)
    return _rolling_mean(base, 21)

def grco_020_gross_leverage_zscore_21d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_020_gross_leverage_zscore_21d"""
    base = _pct_change(revenue, 252) - _pct_change(cor, 252)
    return _zscore_rolling(base, 21)

def grco_021_gross_leverage_rank_21d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_021_gross_leverage_rank_21d"""
    base = _pct_change(revenue, 252) - _pct_change(cor, 252)
    return _rank_pct(base, 21)

def grco_022_gross_leverage_lvl_63d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_022_gross_leverage_lvl_63d"""
    base = _pct_change(revenue, 252) - _pct_change(cor, 252)
    return _rolling_mean(base, 63)

def grco_023_gross_leverage_zscore_63d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_023_gross_leverage_zscore_63d"""
    base = _pct_change(revenue, 252) - _pct_change(cor, 252)
    return _zscore_rolling(base, 63)

def grco_024_gross_leverage_rank_63d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_024_gross_leverage_rank_63d"""
    base = _pct_change(revenue, 252) - _pct_change(cor, 252)
    return _rank_pct(base, 63)

def grco_025_gross_leverage_lvl_126d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_025_gross_leverage_lvl_126d"""
    base = _pct_change(revenue, 252) - _pct_change(cor, 252)
    return _rolling_mean(base, 126)

def grco_026_gross_leverage_zscore_126d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_026_gross_leverage_zscore_126d"""
    base = _pct_change(revenue, 252) - _pct_change(cor, 252)
    return _zscore_rolling(base, 126)

def grco_027_gross_leverage_rank_126d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_027_gross_leverage_rank_126d"""
    base = _pct_change(revenue, 252) - _pct_change(cor, 252)
    return _rank_pct(base, 126)

def grco_028_gross_leverage_lvl_252d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_028_gross_leverage_lvl_252d"""
    base = _pct_change(revenue, 252) - _pct_change(cor, 252)
    return _rolling_mean(base, 252)

def grco_029_gross_leverage_zscore_252d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_029_gross_leverage_zscore_252d"""
    base = _pct_change(revenue, 252) - _pct_change(cor, 252)
    return _zscore_rolling(base, 252)

def grco_030_gross_leverage_rank_252d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_030_gross_leverage_rank_252d"""
    base = _pct_change(revenue, 252) - _pct_change(cor, 252)
    return _rank_pct(base, 252)

def grco_031_ebitda_leverage_lvl_5d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_031_ebitda_leverage_lvl_5d"""
    base = _pct_change(ebitda, 252) - _pct_change(revenue, 252)
    return _rolling_mean(base, 5)

def grco_032_ebitda_leverage_zscore_5d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_032_ebitda_leverage_zscore_5d"""
    base = _pct_change(ebitda, 252) - _pct_change(revenue, 252)
    return _zscore_rolling(base, 5)

def grco_033_ebitda_leverage_rank_5d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_033_ebitda_leverage_rank_5d"""
    base = _pct_change(ebitda, 252) - _pct_change(revenue, 252)
    return _rank_pct(base, 5)

def grco_034_ebitda_leverage_lvl_21d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_034_ebitda_leverage_lvl_21d"""
    base = _pct_change(ebitda, 252) - _pct_change(revenue, 252)
    return _rolling_mean(base, 21)

def grco_035_ebitda_leverage_zscore_21d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_035_ebitda_leverage_zscore_21d"""
    base = _pct_change(ebitda, 252) - _pct_change(revenue, 252)
    return _zscore_rolling(base, 21)

def grco_036_ebitda_leverage_rank_21d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_036_ebitda_leverage_rank_21d"""
    base = _pct_change(ebitda, 252) - _pct_change(revenue, 252)
    return _rank_pct(base, 21)

def grco_037_ebitda_leverage_lvl_63d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_037_ebitda_leverage_lvl_63d"""
    base = _pct_change(ebitda, 252) - _pct_change(revenue, 252)
    return _rolling_mean(base, 63)

def grco_038_ebitda_leverage_zscore_63d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_038_ebitda_leverage_zscore_63d"""
    base = _pct_change(ebitda, 252) - _pct_change(revenue, 252)
    return _zscore_rolling(base, 63)

def grco_039_ebitda_leverage_rank_63d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_039_ebitda_leverage_rank_63d"""
    base = _pct_change(ebitda, 252) - _pct_change(revenue, 252)
    return _rank_pct(base, 63)

def grco_040_ebitda_leverage_lvl_126d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_040_ebitda_leverage_lvl_126d"""
    base = _pct_change(ebitda, 252) - _pct_change(revenue, 252)
    return _rolling_mean(base, 126)

def grco_041_ebitda_leverage_zscore_126d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_041_ebitda_leverage_zscore_126d"""
    base = _pct_change(ebitda, 252) - _pct_change(revenue, 252)
    return _zscore_rolling(base, 126)

def grco_042_ebitda_leverage_rank_126d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_042_ebitda_leverage_rank_126d"""
    base = _pct_change(ebitda, 252) - _pct_change(revenue, 252)
    return _rank_pct(base, 126)

def grco_043_ebitda_leverage_lvl_252d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_043_ebitda_leverage_lvl_252d"""
    base = _pct_change(ebitda, 252) - _pct_change(revenue, 252)
    return _rolling_mean(base, 252)

def grco_044_ebitda_leverage_zscore_252d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_044_ebitda_leverage_zscore_252d"""
    base = _pct_change(ebitda, 252) - _pct_change(revenue, 252)
    return _zscore_rolling(base, 252)

def grco_045_ebitda_leverage_rank_252d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_045_ebitda_leverage_rank_252d"""
    base = _pct_change(ebitda, 252) - _pct_change(revenue, 252)
    return _rank_pct(base, 252)

def grco_046_rev_to_opexp_lvl_5d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_046_rev_to_opexp_lvl_5d"""
    base = _safe_div(revenue, opexp)
    return _rolling_mean(base, 5)

def grco_047_rev_to_opexp_zscore_5d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_047_rev_to_opexp_zscore_5d"""
    base = _safe_div(revenue, opexp)
    return _zscore_rolling(base, 5)

def grco_048_rev_to_opexp_rank_5d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_048_rev_to_opexp_rank_5d"""
    base = _safe_div(revenue, opexp)
    return _rank_pct(base, 5)

def grco_049_rev_to_opexp_lvl_21d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_049_rev_to_opexp_lvl_21d"""
    base = _safe_div(revenue, opexp)
    return _rolling_mean(base, 21)

def grco_050_rev_to_opexp_zscore_21d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_050_rev_to_opexp_zscore_21d"""
    base = _safe_div(revenue, opexp)
    return _zscore_rolling(base, 21)

def grco_051_rev_to_opexp_rank_21d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_051_rev_to_opexp_rank_21d"""
    base = _safe_div(revenue, opexp)
    return _rank_pct(base, 21)

def grco_052_rev_to_opexp_lvl_63d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_052_rev_to_opexp_lvl_63d"""
    base = _safe_div(revenue, opexp)
    return _rolling_mean(base, 63)

def grco_053_rev_to_opexp_zscore_63d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_053_rev_to_opexp_zscore_63d"""
    base = _safe_div(revenue, opexp)
    return _zscore_rolling(base, 63)

def grco_054_rev_to_opexp_rank_63d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_054_rev_to_opexp_rank_63d"""
    base = _safe_div(revenue, opexp)
    return _rank_pct(base, 63)

def grco_055_rev_to_opexp_lvl_126d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_055_rev_to_opexp_lvl_126d"""
    base = _safe_div(revenue, opexp)
    return _rolling_mean(base, 126)

def grco_056_rev_to_opexp_zscore_126d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_056_rev_to_opexp_zscore_126d"""
    base = _safe_div(revenue, opexp)
    return _zscore_rolling(base, 126)

def grco_057_rev_to_opexp_rank_126d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_057_rev_to_opexp_rank_126d"""
    base = _safe_div(revenue, opexp)
    return _rank_pct(base, 126)

def grco_058_rev_to_opexp_lvl_252d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_058_rev_to_opexp_lvl_252d"""
    base = _safe_div(revenue, opexp)
    return _rolling_mean(base, 252)

def grco_059_rev_to_opexp_zscore_252d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_059_rev_to_opexp_zscore_252d"""
    base = _safe_div(revenue, opexp)
    return _zscore_rolling(base, 252)

def grco_060_rev_to_opexp_rank_252d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_060_rev_to_opexp_rank_252d"""
    base = _safe_div(revenue, opexp)
    return _rank_pct(base, 252)

def grco_061_gp_to_opexp_lvl_5d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_061_gp_to_opexp_lvl_5d"""
    base = _safe_div(revenue - cor, opexp)
    return _rolling_mean(base, 5)

def grco_062_gp_to_opexp_zscore_5d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_062_gp_to_opexp_zscore_5d"""
    base = _safe_div(revenue - cor, opexp)
    return _zscore_rolling(base, 5)

def grco_063_gp_to_opexp_rank_5d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_063_gp_to_opexp_rank_5d"""
    base = _safe_div(revenue - cor, opexp)
    return _rank_pct(base, 5)

def grco_064_gp_to_opexp_lvl_21d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_064_gp_to_opexp_lvl_21d"""
    base = _safe_div(revenue - cor, opexp)
    return _rolling_mean(base, 21)

def grco_065_gp_to_opexp_zscore_21d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_065_gp_to_opexp_zscore_21d"""
    base = _safe_div(revenue - cor, opexp)
    return _zscore_rolling(base, 21)

def grco_066_gp_to_opexp_rank_21d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_066_gp_to_opexp_rank_21d"""
    base = _safe_div(revenue - cor, opexp)
    return _rank_pct(base, 21)

def grco_067_gp_to_opexp_lvl_63d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_067_gp_to_opexp_lvl_63d"""
    base = _safe_div(revenue - cor, opexp)
    return _rolling_mean(base, 63)

def grco_068_gp_to_opexp_zscore_63d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_068_gp_to_opexp_zscore_63d"""
    base = _safe_div(revenue - cor, opexp)
    return _zscore_rolling(base, 63)

def grco_069_gp_to_opexp_rank_63d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_069_gp_to_opexp_rank_63d"""
    base = _safe_div(revenue - cor, opexp)
    return _rank_pct(base, 63)

def grco_070_gp_to_opexp_lvl_126d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_070_gp_to_opexp_lvl_126d"""
    base = _safe_div(revenue - cor, opexp)
    return _rolling_mean(base, 126)

def grco_071_gp_to_opexp_zscore_126d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_071_gp_to_opexp_zscore_126d"""
    base = _safe_div(revenue - cor, opexp)
    return _zscore_rolling(base, 126)

def grco_072_gp_to_opexp_rank_126d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_072_gp_to_opexp_rank_126d"""
    base = _safe_div(revenue - cor, opexp)
    return _rank_pct(base, 126)

def grco_073_gp_to_opexp_lvl_252d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_073_gp_to_opexp_lvl_252d"""
    base = _safe_div(revenue - cor, opexp)
    return _rolling_mean(base, 252)

def grco_074_gp_to_opexp_zscore_252d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_074_gp_to_opexp_zscore_252d"""
    base = _safe_div(revenue - cor, opexp)
    return _zscore_rolling(base, 252)

def grco_075_gp_to_opexp_rank_252d(revenue: pd.Series, opexp: pd.Series, cor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """grco_075_gp_to_opexp_rank_252d"""
    base = _safe_div(revenue - cor, opexp)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V49_REGISTRY = {
    "grco_001_op_leverage_lvl_5d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_001_op_leverage_lvl_5d},
    "grco_002_op_leverage_zscore_5d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_002_op_leverage_zscore_5d},
    "grco_003_op_leverage_rank_5d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_003_op_leverage_rank_5d},
    "grco_004_op_leverage_lvl_21d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_004_op_leverage_lvl_21d},
    "grco_005_op_leverage_zscore_21d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_005_op_leverage_zscore_21d},
    "grco_006_op_leverage_rank_21d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_006_op_leverage_rank_21d},
    "grco_007_op_leverage_lvl_63d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_007_op_leverage_lvl_63d},
    "grco_008_op_leverage_zscore_63d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_008_op_leverage_zscore_63d},
    "grco_009_op_leverage_rank_63d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_009_op_leverage_rank_63d},
    "grco_010_op_leverage_lvl_126d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_010_op_leverage_lvl_126d},
    "grco_011_op_leverage_zscore_126d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_011_op_leverage_zscore_126d},
    "grco_012_op_leverage_rank_126d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_012_op_leverage_rank_126d},
    "grco_013_op_leverage_lvl_252d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_013_op_leverage_lvl_252d},
    "grco_014_op_leverage_zscore_252d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_014_op_leverage_zscore_252d},
    "grco_015_op_leverage_rank_252d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_015_op_leverage_rank_252d},
    "grco_016_gross_leverage_lvl_5d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_016_gross_leverage_lvl_5d},
    "grco_017_gross_leverage_zscore_5d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_017_gross_leverage_zscore_5d},
    "grco_018_gross_leverage_rank_5d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_018_gross_leverage_rank_5d},
    "grco_019_gross_leverage_lvl_21d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_019_gross_leverage_lvl_21d},
    "grco_020_gross_leverage_zscore_21d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_020_gross_leverage_zscore_21d},
    "grco_021_gross_leverage_rank_21d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_021_gross_leverage_rank_21d},
    "grco_022_gross_leverage_lvl_63d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_022_gross_leverage_lvl_63d},
    "grco_023_gross_leverage_zscore_63d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_023_gross_leverage_zscore_63d},
    "grco_024_gross_leverage_rank_63d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_024_gross_leverage_rank_63d},
    "grco_025_gross_leverage_lvl_126d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_025_gross_leverage_lvl_126d},
    "grco_026_gross_leverage_zscore_126d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_026_gross_leverage_zscore_126d},
    "grco_027_gross_leverage_rank_126d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_027_gross_leverage_rank_126d},
    "grco_028_gross_leverage_lvl_252d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_028_gross_leverage_lvl_252d},
    "grco_029_gross_leverage_zscore_252d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_029_gross_leverage_zscore_252d},
    "grco_030_gross_leverage_rank_252d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_030_gross_leverage_rank_252d},
    "grco_031_ebitda_leverage_lvl_5d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_031_ebitda_leverage_lvl_5d},
    "grco_032_ebitda_leverage_zscore_5d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_032_ebitda_leverage_zscore_5d},
    "grco_033_ebitda_leverage_rank_5d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_033_ebitda_leverage_rank_5d},
    "grco_034_ebitda_leverage_lvl_21d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_034_ebitda_leverage_lvl_21d},
    "grco_035_ebitda_leverage_zscore_21d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_035_ebitda_leverage_zscore_21d},
    "grco_036_ebitda_leverage_rank_21d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_036_ebitda_leverage_rank_21d},
    "grco_037_ebitda_leverage_lvl_63d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_037_ebitda_leverage_lvl_63d},
    "grco_038_ebitda_leverage_zscore_63d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_038_ebitda_leverage_zscore_63d},
    "grco_039_ebitda_leverage_rank_63d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_039_ebitda_leverage_rank_63d},
    "grco_040_ebitda_leverage_lvl_126d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_040_ebitda_leverage_lvl_126d},
    "grco_041_ebitda_leverage_zscore_126d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_041_ebitda_leverage_zscore_126d},
    "grco_042_ebitda_leverage_rank_126d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_042_ebitda_leverage_rank_126d},
    "grco_043_ebitda_leverage_lvl_252d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_043_ebitda_leverage_lvl_252d},
    "grco_044_ebitda_leverage_zscore_252d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_044_ebitda_leverage_zscore_252d},
    "grco_045_ebitda_leverage_rank_252d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_045_ebitda_leverage_rank_252d},
    "grco_046_rev_to_opexp_lvl_5d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_046_rev_to_opexp_lvl_5d},
    "grco_047_rev_to_opexp_zscore_5d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_047_rev_to_opexp_zscore_5d},
    "grco_048_rev_to_opexp_rank_5d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_048_rev_to_opexp_rank_5d},
    "grco_049_rev_to_opexp_lvl_21d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_049_rev_to_opexp_lvl_21d},
    "grco_050_rev_to_opexp_zscore_21d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_050_rev_to_opexp_zscore_21d},
    "grco_051_rev_to_opexp_rank_21d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_051_rev_to_opexp_rank_21d},
    "grco_052_rev_to_opexp_lvl_63d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_052_rev_to_opexp_lvl_63d},
    "grco_053_rev_to_opexp_zscore_63d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_053_rev_to_opexp_zscore_63d},
    "grco_054_rev_to_opexp_rank_63d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_054_rev_to_opexp_rank_63d},
    "grco_055_rev_to_opexp_lvl_126d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_055_rev_to_opexp_lvl_126d},
    "grco_056_rev_to_opexp_zscore_126d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_056_rev_to_opexp_zscore_126d},
    "grco_057_rev_to_opexp_rank_126d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_057_rev_to_opexp_rank_126d},
    "grco_058_rev_to_opexp_lvl_252d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_058_rev_to_opexp_lvl_252d},
    "grco_059_rev_to_opexp_zscore_252d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_059_rev_to_opexp_zscore_252d},
    "grco_060_rev_to_opexp_rank_252d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_060_rev_to_opexp_rank_252d},
    "grco_061_gp_to_opexp_lvl_5d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_061_gp_to_opexp_lvl_5d},
    "grco_062_gp_to_opexp_zscore_5d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_062_gp_to_opexp_zscore_5d},
    "grco_063_gp_to_opexp_rank_5d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_063_gp_to_opexp_rank_5d},
    "grco_064_gp_to_opexp_lvl_21d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_064_gp_to_opexp_lvl_21d},
    "grco_065_gp_to_opexp_zscore_21d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_065_gp_to_opexp_zscore_21d},
    "grco_066_gp_to_opexp_rank_21d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_066_gp_to_opexp_rank_21d},
    "grco_067_gp_to_opexp_lvl_63d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_067_gp_to_opexp_lvl_63d},
    "grco_068_gp_to_opexp_zscore_63d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_068_gp_to_opexp_zscore_63d},
    "grco_069_gp_to_opexp_rank_63d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_069_gp_to_opexp_rank_63d},
    "grco_070_gp_to_opexp_lvl_126d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_070_gp_to_opexp_lvl_126d},
    "grco_071_gp_to_opexp_zscore_126d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_071_gp_to_opexp_zscore_126d},
    "grco_072_gp_to_opexp_rank_126d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_072_gp_to_opexp_rank_126d},
    "grco_073_gp_to_opexp_lvl_252d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_073_gp_to_opexp_lvl_252d},
    "grco_074_gp_to_opexp_zscore_252d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_074_gp_to_opexp_zscore_252d},
    "grco_075_gp_to_opexp_rank_252d": {"inputs": ['revenue', 'opexp', 'cor', 'ebitda'], "func": grco_075_gp_to_opexp_rank_252d},
}
