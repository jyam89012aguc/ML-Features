"""
46_margin_trajectory — Base Features 001-075
Domain: margin_trajectory
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

def marg_001_net_margin_lvl_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_001_net_margin_lvl_5d"""
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 5)

def marg_002_net_margin_zscore_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_002_net_margin_zscore_5d"""
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 5)

def marg_003_net_margin_rank_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_003_net_margin_rank_5d"""
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 5)

def marg_004_net_margin_lvl_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_004_net_margin_lvl_21d"""
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 21)

def marg_005_net_margin_zscore_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_005_net_margin_zscore_21d"""
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 21)

def marg_006_net_margin_rank_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_006_net_margin_rank_21d"""
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 21)

def marg_007_net_margin_lvl_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_007_net_margin_lvl_63d"""
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 63)

def marg_008_net_margin_zscore_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_008_net_margin_zscore_63d"""
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 63)

def marg_009_net_margin_rank_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_009_net_margin_rank_63d"""
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 63)

def marg_010_net_margin_lvl_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_010_net_margin_lvl_126d"""
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 126)

def marg_011_net_margin_zscore_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_011_net_margin_zscore_126d"""
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 126)

def marg_012_net_margin_rank_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_012_net_margin_rank_126d"""
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 126)

def marg_013_net_margin_lvl_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_013_net_margin_lvl_252d"""
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 252)

def marg_014_net_margin_zscore_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_014_net_margin_zscore_252d"""
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 252)

def marg_015_net_margin_rank_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_015_net_margin_rank_252d"""
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 252)

def marg_016_op_margin_lvl_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_016_op_margin_lvl_5d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 5)

def marg_017_op_margin_zscore_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_017_op_margin_zscore_5d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 5)

def marg_018_op_margin_rank_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_018_op_margin_rank_5d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 5)

def marg_019_op_margin_lvl_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_019_op_margin_lvl_21d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 21)

def marg_020_op_margin_zscore_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_020_op_margin_zscore_21d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 21)

def marg_021_op_margin_rank_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_021_op_margin_rank_21d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 21)

def marg_022_op_margin_lvl_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_022_op_margin_lvl_63d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 63)

def marg_023_op_margin_zscore_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_023_op_margin_zscore_63d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 63)

def marg_024_op_margin_rank_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_024_op_margin_rank_63d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 63)

def marg_025_op_margin_lvl_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_025_op_margin_lvl_126d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 126)

def marg_026_op_margin_zscore_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_026_op_margin_zscore_126d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 126)

def marg_027_op_margin_rank_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_027_op_margin_rank_126d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 126)

def marg_028_op_margin_lvl_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_028_op_margin_lvl_252d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 252)

def marg_029_op_margin_zscore_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_029_op_margin_zscore_252d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 252)

def marg_030_op_margin_rank_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_030_op_margin_rank_252d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 252)

def marg_031_gross_margin_lvl_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_031_gross_margin_lvl_5d"""
    base = _safe_div(revenue - cor, revenue)
    return _rolling_mean(base, 5)

def marg_032_gross_margin_zscore_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_032_gross_margin_zscore_5d"""
    base = _safe_div(revenue - cor, revenue)
    return _zscore_rolling(base, 5)

def marg_033_gross_margin_rank_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_033_gross_margin_rank_5d"""
    base = _safe_div(revenue - cor, revenue)
    return _rank_pct(base, 5)

def marg_034_gross_margin_lvl_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_034_gross_margin_lvl_21d"""
    base = _safe_div(revenue - cor, revenue)
    return _rolling_mean(base, 21)

def marg_035_gross_margin_zscore_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_035_gross_margin_zscore_21d"""
    base = _safe_div(revenue - cor, revenue)
    return _zscore_rolling(base, 21)

def marg_036_gross_margin_rank_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_036_gross_margin_rank_21d"""
    base = _safe_div(revenue - cor, revenue)
    return _rank_pct(base, 21)

def marg_037_gross_margin_lvl_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_037_gross_margin_lvl_63d"""
    base = _safe_div(revenue - cor, revenue)
    return _rolling_mean(base, 63)

def marg_038_gross_margin_zscore_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_038_gross_margin_zscore_63d"""
    base = _safe_div(revenue - cor, revenue)
    return _zscore_rolling(base, 63)

def marg_039_gross_margin_rank_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_039_gross_margin_rank_63d"""
    base = _safe_div(revenue - cor, revenue)
    return _rank_pct(base, 63)

def marg_040_gross_margin_lvl_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_040_gross_margin_lvl_126d"""
    base = _safe_div(revenue - cor, revenue)
    return _rolling_mean(base, 126)

def marg_041_gross_margin_zscore_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_041_gross_margin_zscore_126d"""
    base = _safe_div(revenue - cor, revenue)
    return _zscore_rolling(base, 126)

def marg_042_gross_margin_rank_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_042_gross_margin_rank_126d"""
    base = _safe_div(revenue - cor, revenue)
    return _rank_pct(base, 126)

def marg_043_gross_margin_lvl_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_043_gross_margin_lvl_252d"""
    base = _safe_div(revenue - cor, revenue)
    return _rolling_mean(base, 252)

def marg_044_gross_margin_zscore_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_044_gross_margin_zscore_252d"""
    base = _safe_div(revenue - cor, revenue)
    return _zscore_rolling(base, 252)

def marg_045_gross_margin_rank_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_045_gross_margin_rank_252d"""
    base = _safe_div(revenue - cor, revenue)
    return _rank_pct(base, 252)

def marg_046_ebitda_margin_lvl_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_046_ebitda_margin_lvl_5d"""
    base = _safe_div(ebitda, revenue)
    return _rolling_mean(base, 5)

def marg_047_ebitda_margin_zscore_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_047_ebitda_margin_zscore_5d"""
    base = _safe_div(ebitda, revenue)
    return _zscore_rolling(base, 5)

def marg_048_ebitda_margin_rank_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_048_ebitda_margin_rank_5d"""
    base = _safe_div(ebitda, revenue)
    return _rank_pct(base, 5)

def marg_049_ebitda_margin_lvl_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_049_ebitda_margin_lvl_21d"""
    base = _safe_div(ebitda, revenue)
    return _rolling_mean(base, 21)

def marg_050_ebitda_margin_zscore_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_050_ebitda_margin_zscore_21d"""
    base = _safe_div(ebitda, revenue)
    return _zscore_rolling(base, 21)

def marg_051_ebitda_margin_rank_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_051_ebitda_margin_rank_21d"""
    base = _safe_div(ebitda, revenue)
    return _rank_pct(base, 21)

def marg_052_ebitda_margin_lvl_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_052_ebitda_margin_lvl_63d"""
    base = _safe_div(ebitda, revenue)
    return _rolling_mean(base, 63)

def marg_053_ebitda_margin_zscore_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_053_ebitda_margin_zscore_63d"""
    base = _safe_div(ebitda, revenue)
    return _zscore_rolling(base, 63)

def marg_054_ebitda_margin_rank_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_054_ebitda_margin_rank_63d"""
    base = _safe_div(ebitda, revenue)
    return _rank_pct(base, 63)

def marg_055_ebitda_margin_lvl_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_055_ebitda_margin_lvl_126d"""
    base = _safe_div(ebitda, revenue)
    return _rolling_mean(base, 126)

def marg_056_ebitda_margin_zscore_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_056_ebitda_margin_zscore_126d"""
    base = _safe_div(ebitda, revenue)
    return _zscore_rolling(base, 126)

def marg_057_ebitda_margin_rank_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_057_ebitda_margin_rank_126d"""
    base = _safe_div(ebitda, revenue)
    return _rank_pct(base, 126)

def marg_058_ebitda_margin_lvl_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_058_ebitda_margin_lvl_252d"""
    base = _safe_div(ebitda, revenue)
    return _rolling_mean(base, 252)

def marg_059_ebitda_margin_zscore_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_059_ebitda_margin_zscore_252d"""
    base = _safe_div(ebitda, revenue)
    return _zscore_rolling(base, 252)

def marg_060_ebitda_margin_rank_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_060_ebitda_margin_rank_252d"""
    base = _safe_div(ebitda, revenue)
    return _rank_pct(base, 252)

def marg_061_ebit_margin_lvl_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_061_ebit_margin_lvl_5d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 5)

def marg_062_ebit_margin_zscore_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_062_ebit_margin_zscore_5d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 5)

def marg_063_ebit_margin_rank_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_063_ebit_margin_rank_5d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 5)

def marg_064_ebit_margin_lvl_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_064_ebit_margin_lvl_21d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 21)

def marg_065_ebit_margin_zscore_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_065_ebit_margin_zscore_21d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 21)

def marg_066_ebit_margin_rank_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_066_ebit_margin_rank_21d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 21)

def marg_067_ebit_margin_lvl_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_067_ebit_margin_lvl_63d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 63)

def marg_068_ebit_margin_zscore_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_068_ebit_margin_zscore_63d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 63)

def marg_069_ebit_margin_rank_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_069_ebit_margin_rank_63d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 63)

def marg_070_ebit_margin_lvl_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_070_ebit_margin_lvl_126d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 126)

def marg_071_ebit_margin_zscore_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_071_ebit_margin_zscore_126d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 126)

def marg_072_ebit_margin_rank_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_072_ebit_margin_rank_126d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 126)

def marg_073_ebit_margin_lvl_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_073_ebit_margin_lvl_252d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 252)

def marg_074_ebit_margin_zscore_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_074_ebit_margin_zscore_252d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 252)

def marg_075_ebit_margin_rank_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, ebitda: pd.Series, cor: pd.Series) -> pd.Series:
    """marg_075_ebit_margin_rank_252d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V46_REGISTRY = {
    "marg_001_net_margin_lvl_5d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_001_net_margin_lvl_5d},
    "marg_002_net_margin_zscore_5d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_002_net_margin_zscore_5d},
    "marg_003_net_margin_rank_5d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_003_net_margin_rank_5d},
    "marg_004_net_margin_lvl_21d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_004_net_margin_lvl_21d},
    "marg_005_net_margin_zscore_21d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_005_net_margin_zscore_21d},
    "marg_006_net_margin_rank_21d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_006_net_margin_rank_21d},
    "marg_007_net_margin_lvl_63d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_007_net_margin_lvl_63d},
    "marg_008_net_margin_zscore_63d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_008_net_margin_zscore_63d},
    "marg_009_net_margin_rank_63d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_009_net_margin_rank_63d},
    "marg_010_net_margin_lvl_126d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_010_net_margin_lvl_126d},
    "marg_011_net_margin_zscore_126d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_011_net_margin_zscore_126d},
    "marg_012_net_margin_rank_126d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_012_net_margin_rank_126d},
    "marg_013_net_margin_lvl_252d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_013_net_margin_lvl_252d},
    "marg_014_net_margin_zscore_252d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_014_net_margin_zscore_252d},
    "marg_015_net_margin_rank_252d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_015_net_margin_rank_252d},
    "marg_016_op_margin_lvl_5d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_016_op_margin_lvl_5d},
    "marg_017_op_margin_zscore_5d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_017_op_margin_zscore_5d},
    "marg_018_op_margin_rank_5d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_018_op_margin_rank_5d},
    "marg_019_op_margin_lvl_21d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_019_op_margin_lvl_21d},
    "marg_020_op_margin_zscore_21d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_020_op_margin_zscore_21d},
    "marg_021_op_margin_rank_21d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_021_op_margin_rank_21d},
    "marg_022_op_margin_lvl_63d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_022_op_margin_lvl_63d},
    "marg_023_op_margin_zscore_63d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_023_op_margin_zscore_63d},
    "marg_024_op_margin_rank_63d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_024_op_margin_rank_63d},
    "marg_025_op_margin_lvl_126d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_025_op_margin_lvl_126d},
    "marg_026_op_margin_zscore_126d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_026_op_margin_zscore_126d},
    "marg_027_op_margin_rank_126d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_027_op_margin_rank_126d},
    "marg_028_op_margin_lvl_252d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_028_op_margin_lvl_252d},
    "marg_029_op_margin_zscore_252d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_029_op_margin_zscore_252d},
    "marg_030_op_margin_rank_252d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_030_op_margin_rank_252d},
    "marg_031_gross_margin_lvl_5d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_031_gross_margin_lvl_5d},
    "marg_032_gross_margin_zscore_5d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_032_gross_margin_zscore_5d},
    "marg_033_gross_margin_rank_5d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_033_gross_margin_rank_5d},
    "marg_034_gross_margin_lvl_21d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_034_gross_margin_lvl_21d},
    "marg_035_gross_margin_zscore_21d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_035_gross_margin_zscore_21d},
    "marg_036_gross_margin_rank_21d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_036_gross_margin_rank_21d},
    "marg_037_gross_margin_lvl_63d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_037_gross_margin_lvl_63d},
    "marg_038_gross_margin_zscore_63d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_038_gross_margin_zscore_63d},
    "marg_039_gross_margin_rank_63d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_039_gross_margin_rank_63d},
    "marg_040_gross_margin_lvl_126d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_040_gross_margin_lvl_126d},
    "marg_041_gross_margin_zscore_126d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_041_gross_margin_zscore_126d},
    "marg_042_gross_margin_rank_126d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_042_gross_margin_rank_126d},
    "marg_043_gross_margin_lvl_252d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_043_gross_margin_lvl_252d},
    "marg_044_gross_margin_zscore_252d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_044_gross_margin_zscore_252d},
    "marg_045_gross_margin_rank_252d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_045_gross_margin_rank_252d},
    "marg_046_ebitda_margin_lvl_5d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_046_ebitda_margin_lvl_5d},
    "marg_047_ebitda_margin_zscore_5d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_047_ebitda_margin_zscore_5d},
    "marg_048_ebitda_margin_rank_5d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_048_ebitda_margin_rank_5d},
    "marg_049_ebitda_margin_lvl_21d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_049_ebitda_margin_lvl_21d},
    "marg_050_ebitda_margin_zscore_21d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_050_ebitda_margin_zscore_21d},
    "marg_051_ebitda_margin_rank_21d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_051_ebitda_margin_rank_21d},
    "marg_052_ebitda_margin_lvl_63d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_052_ebitda_margin_lvl_63d},
    "marg_053_ebitda_margin_zscore_63d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_053_ebitda_margin_zscore_63d},
    "marg_054_ebitda_margin_rank_63d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_054_ebitda_margin_rank_63d},
    "marg_055_ebitda_margin_lvl_126d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_055_ebitda_margin_lvl_126d},
    "marg_056_ebitda_margin_zscore_126d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_056_ebitda_margin_zscore_126d},
    "marg_057_ebitda_margin_rank_126d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_057_ebitda_margin_rank_126d},
    "marg_058_ebitda_margin_lvl_252d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_058_ebitda_margin_lvl_252d},
    "marg_059_ebitda_margin_zscore_252d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_059_ebitda_margin_zscore_252d},
    "marg_060_ebitda_margin_rank_252d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_060_ebitda_margin_rank_252d},
    "marg_061_ebit_margin_lvl_5d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_061_ebit_margin_lvl_5d},
    "marg_062_ebit_margin_zscore_5d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_062_ebit_margin_zscore_5d},
    "marg_063_ebit_margin_rank_5d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_063_ebit_margin_rank_5d},
    "marg_064_ebit_margin_lvl_21d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_064_ebit_margin_lvl_21d},
    "marg_065_ebit_margin_zscore_21d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_065_ebit_margin_zscore_21d},
    "marg_066_ebit_margin_rank_21d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_066_ebit_margin_rank_21d},
    "marg_067_ebit_margin_lvl_63d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_067_ebit_margin_lvl_63d},
    "marg_068_ebit_margin_zscore_63d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_068_ebit_margin_zscore_63d},
    "marg_069_ebit_margin_rank_63d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_069_ebit_margin_rank_63d},
    "marg_070_ebit_margin_lvl_126d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_070_ebit_margin_lvl_126d},
    "marg_071_ebit_margin_zscore_126d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_071_ebit_margin_zscore_126d},
    "marg_072_ebit_margin_rank_126d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_072_ebit_margin_rank_126d},
    "marg_073_ebit_margin_lvl_252d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_073_ebit_margin_lvl_252d},
    "marg_074_ebit_margin_zscore_252d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_074_ebit_margin_zscore_252d},
    "marg_075_ebit_margin_rank_252d": {"inputs": ['netinc', 'opinc', 'revenue', 'ebitda', 'cor'], "func": marg_075_ebit_margin_rank_252d},
}
