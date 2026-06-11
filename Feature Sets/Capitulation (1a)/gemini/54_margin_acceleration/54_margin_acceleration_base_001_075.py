"""
54_margin_acceleration — Base Features 001-075
Domain: margin_acceleration
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

def maga_001_net_margin_lvl_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_001_net_margin_lvl_5d"""
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 5)

def maga_002_net_margin_zscore_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_002_net_margin_zscore_5d"""
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 5)

def maga_003_net_margin_rank_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_003_net_margin_rank_5d"""
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 5)

def maga_004_net_margin_lvl_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_004_net_margin_lvl_21d"""
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 21)

def maga_005_net_margin_zscore_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_005_net_margin_zscore_21d"""
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 21)

def maga_006_net_margin_rank_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_006_net_margin_rank_21d"""
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 21)

def maga_007_net_margin_lvl_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_007_net_margin_lvl_63d"""
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 63)

def maga_008_net_margin_zscore_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_008_net_margin_zscore_63d"""
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 63)

def maga_009_net_margin_rank_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_009_net_margin_rank_63d"""
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 63)

def maga_010_net_margin_lvl_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_010_net_margin_lvl_126d"""
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 126)

def maga_011_net_margin_zscore_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_011_net_margin_zscore_126d"""
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 126)

def maga_012_net_margin_rank_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_012_net_margin_rank_126d"""
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 126)

def maga_013_net_margin_lvl_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_013_net_margin_lvl_252d"""
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 252)

def maga_014_net_margin_zscore_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_014_net_margin_zscore_252d"""
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 252)

def maga_015_net_margin_rank_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_015_net_margin_rank_252d"""
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 252)

def maga_016_op_margin_lvl_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_016_op_margin_lvl_5d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 5)

def maga_017_op_margin_zscore_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_017_op_margin_zscore_5d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 5)

def maga_018_op_margin_rank_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_018_op_margin_rank_5d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 5)

def maga_019_op_margin_lvl_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_019_op_margin_lvl_21d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 21)

def maga_020_op_margin_zscore_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_020_op_margin_zscore_21d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 21)

def maga_021_op_margin_rank_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_021_op_margin_rank_21d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 21)

def maga_022_op_margin_lvl_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_022_op_margin_lvl_63d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 63)

def maga_023_op_margin_zscore_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_023_op_margin_zscore_63d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 63)

def maga_024_op_margin_rank_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_024_op_margin_rank_63d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 63)

def maga_025_op_margin_lvl_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_025_op_margin_lvl_126d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 126)

def maga_026_op_margin_zscore_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_026_op_margin_zscore_126d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 126)

def maga_027_op_margin_rank_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_027_op_margin_rank_126d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 126)

def maga_028_op_margin_lvl_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_028_op_margin_lvl_252d"""
    base = _safe_div(opinc, revenue)
    return _rolling_mean(base, 252)

def maga_029_op_margin_zscore_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_029_op_margin_zscore_252d"""
    base = _safe_div(opinc, revenue)
    return _zscore_rolling(base, 252)

def maga_030_op_margin_rank_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_030_op_margin_rank_252d"""
    base = _safe_div(opinc, revenue)
    return _rank_pct(base, 252)

def maga_031_gross_margin_lvl_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_031_gross_margin_lvl_5d"""
    base = _safe_div(revenue - cor, revenue)
    return _rolling_mean(base, 5)

def maga_032_gross_margin_zscore_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_032_gross_margin_zscore_5d"""
    base = _safe_div(revenue - cor, revenue)
    return _zscore_rolling(base, 5)

def maga_033_gross_margin_rank_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_033_gross_margin_rank_5d"""
    base = _safe_div(revenue - cor, revenue)
    return _rank_pct(base, 5)

def maga_034_gross_margin_lvl_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_034_gross_margin_lvl_21d"""
    base = _safe_div(revenue - cor, revenue)
    return _rolling_mean(base, 21)

def maga_035_gross_margin_zscore_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_035_gross_margin_zscore_21d"""
    base = _safe_div(revenue - cor, revenue)
    return _zscore_rolling(base, 21)

def maga_036_gross_margin_rank_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_036_gross_margin_rank_21d"""
    base = _safe_div(revenue - cor, revenue)
    return _rank_pct(base, 21)

def maga_037_gross_margin_lvl_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_037_gross_margin_lvl_63d"""
    base = _safe_div(revenue - cor, revenue)
    return _rolling_mean(base, 63)

def maga_038_gross_margin_zscore_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_038_gross_margin_zscore_63d"""
    base = _safe_div(revenue - cor, revenue)
    return _zscore_rolling(base, 63)

def maga_039_gross_margin_rank_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_039_gross_margin_rank_63d"""
    base = _safe_div(revenue - cor, revenue)
    return _rank_pct(base, 63)

def maga_040_gross_margin_lvl_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_040_gross_margin_lvl_126d"""
    base = _safe_div(revenue - cor, revenue)
    return _rolling_mean(base, 126)

def maga_041_gross_margin_zscore_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_041_gross_margin_zscore_126d"""
    base = _safe_div(revenue - cor, revenue)
    return _zscore_rolling(base, 126)

def maga_042_gross_margin_rank_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_042_gross_margin_rank_126d"""
    base = _safe_div(revenue - cor, revenue)
    return _rank_pct(base, 126)

def maga_043_gross_margin_lvl_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_043_gross_margin_lvl_252d"""
    base = _safe_div(revenue - cor, revenue)
    return _rolling_mean(base, 252)

def maga_044_gross_margin_zscore_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_044_gross_margin_zscore_252d"""
    base = _safe_div(revenue - cor, revenue)
    return _zscore_rolling(base, 252)

def maga_045_gross_margin_rank_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_045_gross_margin_rank_252d"""
    base = _safe_div(revenue - cor, revenue)
    return _rank_pct(base, 252)

def maga_046_margin_yoy_chg_lvl_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_046_margin_yoy_chg_lvl_5d"""
    base = _safe_div(netinc, revenue).diff(252)
    return _rolling_mean(base, 5)

def maga_047_margin_yoy_chg_zscore_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_047_margin_yoy_chg_zscore_5d"""
    base = _safe_div(netinc, revenue).diff(252)
    return _zscore_rolling(base, 5)

def maga_048_margin_yoy_chg_rank_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_048_margin_yoy_chg_rank_5d"""
    base = _safe_div(netinc, revenue).diff(252)
    return _rank_pct(base, 5)

def maga_049_margin_yoy_chg_lvl_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_049_margin_yoy_chg_lvl_21d"""
    base = _safe_div(netinc, revenue).diff(252)
    return _rolling_mean(base, 21)

def maga_050_margin_yoy_chg_zscore_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_050_margin_yoy_chg_zscore_21d"""
    base = _safe_div(netinc, revenue).diff(252)
    return _zscore_rolling(base, 21)

def maga_051_margin_yoy_chg_rank_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_051_margin_yoy_chg_rank_21d"""
    base = _safe_div(netinc, revenue).diff(252)
    return _rank_pct(base, 21)

def maga_052_margin_yoy_chg_lvl_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_052_margin_yoy_chg_lvl_63d"""
    base = _safe_div(netinc, revenue).diff(252)
    return _rolling_mean(base, 63)

def maga_053_margin_yoy_chg_zscore_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_053_margin_yoy_chg_zscore_63d"""
    base = _safe_div(netinc, revenue).diff(252)
    return _zscore_rolling(base, 63)

def maga_054_margin_yoy_chg_rank_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_054_margin_yoy_chg_rank_63d"""
    base = _safe_div(netinc, revenue).diff(252)
    return _rank_pct(base, 63)

def maga_055_margin_yoy_chg_lvl_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_055_margin_yoy_chg_lvl_126d"""
    base = _safe_div(netinc, revenue).diff(252)
    return _rolling_mean(base, 126)

def maga_056_margin_yoy_chg_zscore_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_056_margin_yoy_chg_zscore_126d"""
    base = _safe_div(netinc, revenue).diff(252)
    return _zscore_rolling(base, 126)

def maga_057_margin_yoy_chg_rank_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_057_margin_yoy_chg_rank_126d"""
    base = _safe_div(netinc, revenue).diff(252)
    return _rank_pct(base, 126)

def maga_058_margin_yoy_chg_lvl_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_058_margin_yoy_chg_lvl_252d"""
    base = _safe_div(netinc, revenue).diff(252)
    return _rolling_mean(base, 252)

def maga_059_margin_yoy_chg_zscore_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_059_margin_yoy_chg_zscore_252d"""
    base = _safe_div(netinc, revenue).diff(252)
    return _zscore_rolling(base, 252)

def maga_060_margin_yoy_chg_rank_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_060_margin_yoy_chg_rank_252d"""
    base = _safe_div(netinc, revenue).diff(252)
    return _rank_pct(base, 252)

def maga_061_margin_qoq_chg_lvl_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_061_margin_qoq_chg_lvl_5d"""
    base = _safe_div(netinc, revenue).diff(63)
    return _rolling_mean(base, 5)

def maga_062_margin_qoq_chg_zscore_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_062_margin_qoq_chg_zscore_5d"""
    base = _safe_div(netinc, revenue).diff(63)
    return _zscore_rolling(base, 5)

def maga_063_margin_qoq_chg_rank_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_063_margin_qoq_chg_rank_5d"""
    base = _safe_div(netinc, revenue).diff(63)
    return _rank_pct(base, 5)

def maga_064_margin_qoq_chg_lvl_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_064_margin_qoq_chg_lvl_21d"""
    base = _safe_div(netinc, revenue).diff(63)
    return _rolling_mean(base, 21)

def maga_065_margin_qoq_chg_zscore_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_065_margin_qoq_chg_zscore_21d"""
    base = _safe_div(netinc, revenue).diff(63)
    return _zscore_rolling(base, 21)

def maga_066_margin_qoq_chg_rank_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_066_margin_qoq_chg_rank_21d"""
    base = _safe_div(netinc, revenue).diff(63)
    return _rank_pct(base, 21)

def maga_067_margin_qoq_chg_lvl_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_067_margin_qoq_chg_lvl_63d"""
    base = _safe_div(netinc, revenue).diff(63)
    return _rolling_mean(base, 63)

def maga_068_margin_qoq_chg_zscore_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_068_margin_qoq_chg_zscore_63d"""
    base = _safe_div(netinc, revenue).diff(63)
    return _zscore_rolling(base, 63)

def maga_069_margin_qoq_chg_rank_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_069_margin_qoq_chg_rank_63d"""
    base = _safe_div(netinc, revenue).diff(63)
    return _rank_pct(base, 63)

def maga_070_margin_qoq_chg_lvl_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_070_margin_qoq_chg_lvl_126d"""
    base = _safe_div(netinc, revenue).diff(63)
    return _rolling_mean(base, 126)

def maga_071_margin_qoq_chg_zscore_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_071_margin_qoq_chg_zscore_126d"""
    base = _safe_div(netinc, revenue).diff(63)
    return _zscore_rolling(base, 126)

def maga_072_margin_qoq_chg_rank_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_072_margin_qoq_chg_rank_126d"""
    base = _safe_div(netinc, revenue).diff(63)
    return _rank_pct(base, 126)

def maga_073_margin_qoq_chg_lvl_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_073_margin_qoq_chg_lvl_252d"""
    base = _safe_div(netinc, revenue).diff(63)
    return _rolling_mean(base, 252)

def maga_074_margin_qoq_chg_zscore_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_074_margin_qoq_chg_zscore_252d"""
    base = _safe_div(netinc, revenue).diff(63)
    return _zscore_rolling(base, 252)

def maga_075_margin_qoq_chg_rank_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_075_margin_qoq_chg_rank_252d"""
    base = _safe_div(netinc, revenue).diff(63)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V54_REGISTRY = {
    "maga_001_net_margin_lvl_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_001_net_margin_lvl_5d},
    "maga_002_net_margin_zscore_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_002_net_margin_zscore_5d},
    "maga_003_net_margin_rank_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_003_net_margin_rank_5d},
    "maga_004_net_margin_lvl_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_004_net_margin_lvl_21d},
    "maga_005_net_margin_zscore_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_005_net_margin_zscore_21d},
    "maga_006_net_margin_rank_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_006_net_margin_rank_21d},
    "maga_007_net_margin_lvl_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_007_net_margin_lvl_63d},
    "maga_008_net_margin_zscore_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_008_net_margin_zscore_63d},
    "maga_009_net_margin_rank_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_009_net_margin_rank_63d},
    "maga_010_net_margin_lvl_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_010_net_margin_lvl_126d},
    "maga_011_net_margin_zscore_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_011_net_margin_zscore_126d},
    "maga_012_net_margin_rank_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_012_net_margin_rank_126d},
    "maga_013_net_margin_lvl_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_013_net_margin_lvl_252d},
    "maga_014_net_margin_zscore_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_014_net_margin_zscore_252d},
    "maga_015_net_margin_rank_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_015_net_margin_rank_252d},
    "maga_016_op_margin_lvl_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_016_op_margin_lvl_5d},
    "maga_017_op_margin_zscore_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_017_op_margin_zscore_5d},
    "maga_018_op_margin_rank_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_018_op_margin_rank_5d},
    "maga_019_op_margin_lvl_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_019_op_margin_lvl_21d},
    "maga_020_op_margin_zscore_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_020_op_margin_zscore_21d},
    "maga_021_op_margin_rank_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_021_op_margin_rank_21d},
    "maga_022_op_margin_lvl_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_022_op_margin_lvl_63d},
    "maga_023_op_margin_zscore_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_023_op_margin_zscore_63d},
    "maga_024_op_margin_rank_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_024_op_margin_rank_63d},
    "maga_025_op_margin_lvl_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_025_op_margin_lvl_126d},
    "maga_026_op_margin_zscore_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_026_op_margin_zscore_126d},
    "maga_027_op_margin_rank_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_027_op_margin_rank_126d},
    "maga_028_op_margin_lvl_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_028_op_margin_lvl_252d},
    "maga_029_op_margin_zscore_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_029_op_margin_zscore_252d},
    "maga_030_op_margin_rank_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_030_op_margin_rank_252d},
    "maga_031_gross_margin_lvl_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_031_gross_margin_lvl_5d},
    "maga_032_gross_margin_zscore_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_032_gross_margin_zscore_5d},
    "maga_033_gross_margin_rank_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_033_gross_margin_rank_5d},
    "maga_034_gross_margin_lvl_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_034_gross_margin_lvl_21d},
    "maga_035_gross_margin_zscore_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_035_gross_margin_zscore_21d},
    "maga_036_gross_margin_rank_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_036_gross_margin_rank_21d},
    "maga_037_gross_margin_lvl_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_037_gross_margin_lvl_63d},
    "maga_038_gross_margin_zscore_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_038_gross_margin_zscore_63d},
    "maga_039_gross_margin_rank_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_039_gross_margin_rank_63d},
    "maga_040_gross_margin_lvl_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_040_gross_margin_lvl_126d},
    "maga_041_gross_margin_zscore_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_041_gross_margin_zscore_126d},
    "maga_042_gross_margin_rank_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_042_gross_margin_rank_126d},
    "maga_043_gross_margin_lvl_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_043_gross_margin_lvl_252d},
    "maga_044_gross_margin_zscore_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_044_gross_margin_zscore_252d},
    "maga_045_gross_margin_rank_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_045_gross_margin_rank_252d},
    "maga_046_margin_yoy_chg_lvl_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_046_margin_yoy_chg_lvl_5d},
    "maga_047_margin_yoy_chg_zscore_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_047_margin_yoy_chg_zscore_5d},
    "maga_048_margin_yoy_chg_rank_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_048_margin_yoy_chg_rank_5d},
    "maga_049_margin_yoy_chg_lvl_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_049_margin_yoy_chg_lvl_21d},
    "maga_050_margin_yoy_chg_zscore_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_050_margin_yoy_chg_zscore_21d},
    "maga_051_margin_yoy_chg_rank_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_051_margin_yoy_chg_rank_21d},
    "maga_052_margin_yoy_chg_lvl_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_052_margin_yoy_chg_lvl_63d},
    "maga_053_margin_yoy_chg_zscore_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_053_margin_yoy_chg_zscore_63d},
    "maga_054_margin_yoy_chg_rank_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_054_margin_yoy_chg_rank_63d},
    "maga_055_margin_yoy_chg_lvl_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_055_margin_yoy_chg_lvl_126d},
    "maga_056_margin_yoy_chg_zscore_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_056_margin_yoy_chg_zscore_126d},
    "maga_057_margin_yoy_chg_rank_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_057_margin_yoy_chg_rank_126d},
    "maga_058_margin_yoy_chg_lvl_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_058_margin_yoy_chg_lvl_252d},
    "maga_059_margin_yoy_chg_zscore_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_059_margin_yoy_chg_zscore_252d},
    "maga_060_margin_yoy_chg_rank_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_060_margin_yoy_chg_rank_252d},
    "maga_061_margin_qoq_chg_lvl_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_061_margin_qoq_chg_lvl_5d},
    "maga_062_margin_qoq_chg_zscore_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_062_margin_qoq_chg_zscore_5d},
    "maga_063_margin_qoq_chg_rank_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_063_margin_qoq_chg_rank_5d},
    "maga_064_margin_qoq_chg_lvl_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_064_margin_qoq_chg_lvl_21d},
    "maga_065_margin_qoq_chg_zscore_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_065_margin_qoq_chg_zscore_21d},
    "maga_066_margin_qoq_chg_rank_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_066_margin_qoq_chg_rank_21d},
    "maga_067_margin_qoq_chg_lvl_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_067_margin_qoq_chg_lvl_63d},
    "maga_068_margin_qoq_chg_zscore_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_068_margin_qoq_chg_zscore_63d},
    "maga_069_margin_qoq_chg_rank_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_069_margin_qoq_chg_rank_63d},
    "maga_070_margin_qoq_chg_lvl_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_070_margin_qoq_chg_lvl_126d},
    "maga_071_margin_qoq_chg_zscore_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_071_margin_qoq_chg_zscore_126d},
    "maga_072_margin_qoq_chg_rank_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_072_margin_qoq_chg_rank_126d},
    "maga_073_margin_qoq_chg_lvl_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_073_margin_qoq_chg_lvl_252d},
    "maga_074_margin_qoq_chg_zscore_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_074_margin_qoq_chg_zscore_252d},
    "maga_075_margin_qoq_chg_rank_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_075_margin_qoq_chg_rank_252d},
}
