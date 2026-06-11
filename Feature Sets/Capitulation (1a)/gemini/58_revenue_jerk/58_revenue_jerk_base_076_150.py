"""
58_revenue_jerk — Base Features 076-150
Domain: revenue_jerk
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

def revj_076_rev_jerk_rank_lvl_5d(revenue: pd.Series) -> pd.Series:
    """revj_076_rev_jerk_rank_lvl_5d"""
    base = _rank_pct(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 5)

def revj_077_rev_jerk_rank_zscore_5d(revenue: pd.Series) -> pd.Series:
    """revj_077_rev_jerk_rank_zscore_5d"""
    base = _rank_pct(revenue.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 5)

def revj_078_rev_jerk_rank_rank_5d(revenue: pd.Series) -> pd.Series:
    """revj_078_rev_jerk_rank_rank_5d"""
    base = _rank_pct(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 5)

def revj_079_rev_jerk_rank_lvl_21d(revenue: pd.Series) -> pd.Series:
    """revj_079_rev_jerk_rank_lvl_21d"""
    base = _rank_pct(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 21)

def revj_080_rev_jerk_rank_zscore_21d(revenue: pd.Series) -> pd.Series:
    """revj_080_rev_jerk_rank_zscore_21d"""
    base = _rank_pct(revenue.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 21)

def revj_081_rev_jerk_rank_rank_21d(revenue: pd.Series) -> pd.Series:
    """revj_081_rev_jerk_rank_rank_21d"""
    base = _rank_pct(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 21)

def revj_082_rev_jerk_rank_lvl_63d(revenue: pd.Series) -> pd.Series:
    """revj_082_rev_jerk_rank_lvl_63d"""
    base = _rank_pct(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 63)

def revj_083_rev_jerk_rank_zscore_63d(revenue: pd.Series) -> pd.Series:
    """revj_083_rev_jerk_rank_zscore_63d"""
    base = _rank_pct(revenue.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 63)

def revj_084_rev_jerk_rank_rank_63d(revenue: pd.Series) -> pd.Series:
    """revj_084_rev_jerk_rank_rank_63d"""
    base = _rank_pct(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 63)

def revj_085_rev_jerk_rank_lvl_126d(revenue: pd.Series) -> pd.Series:
    """revj_085_rev_jerk_rank_lvl_126d"""
    base = _rank_pct(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 126)

def revj_086_rev_jerk_rank_zscore_126d(revenue: pd.Series) -> pd.Series:
    """revj_086_rev_jerk_rank_zscore_126d"""
    base = _rank_pct(revenue.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 126)

def revj_087_rev_jerk_rank_rank_126d(revenue: pd.Series) -> pd.Series:
    """revj_087_rev_jerk_rank_rank_126d"""
    base = _rank_pct(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 126)

def revj_088_rev_jerk_rank_lvl_252d(revenue: pd.Series) -> pd.Series:
    """revj_088_rev_jerk_rank_lvl_252d"""
    base = _rank_pct(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 252)

def revj_089_rev_jerk_rank_zscore_252d(revenue: pd.Series) -> pd.Series:
    """revj_089_rev_jerk_rank_zscore_252d"""
    base = _rank_pct(revenue.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 252)

def revj_090_rev_jerk_rank_rank_252d(revenue: pd.Series) -> pd.Series:
    """revj_090_rev_jerk_rank_rank_252d"""
    base = _rank_pct(revenue.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 252)

def revj_091_rev_accel_vol_lvl_5d(revenue: pd.Series) -> pd.Series:
    """revj_091_rev_accel_vol_lvl_5d"""
    base = _rolling_std(revenue.pct_change(252).diff(63), 63)
    return _rolling_mean(base, 5)

def revj_092_rev_accel_vol_zscore_5d(revenue: pd.Series) -> pd.Series:
    """revj_092_rev_accel_vol_zscore_5d"""
    base = _rolling_std(revenue.pct_change(252).diff(63), 63)
    return _zscore_rolling(base, 5)

def revj_093_rev_accel_vol_rank_5d(revenue: pd.Series) -> pd.Series:
    """revj_093_rev_accel_vol_rank_5d"""
    base = _rolling_std(revenue.pct_change(252).diff(63), 63)
    return _rank_pct(base, 5)

def revj_094_rev_accel_vol_lvl_21d(revenue: pd.Series) -> pd.Series:
    """revj_094_rev_accel_vol_lvl_21d"""
    base = _rolling_std(revenue.pct_change(252).diff(63), 63)
    return _rolling_mean(base, 21)

def revj_095_rev_accel_vol_zscore_21d(revenue: pd.Series) -> pd.Series:
    """revj_095_rev_accel_vol_zscore_21d"""
    base = _rolling_std(revenue.pct_change(252).diff(63), 63)
    return _zscore_rolling(base, 21)

def revj_096_rev_accel_vol_rank_21d(revenue: pd.Series) -> pd.Series:
    """revj_096_rev_accel_vol_rank_21d"""
    base = _rolling_std(revenue.pct_change(252).diff(63), 63)
    return _rank_pct(base, 21)

def revj_097_rev_accel_vol_lvl_63d(revenue: pd.Series) -> pd.Series:
    """revj_097_rev_accel_vol_lvl_63d"""
    base = _rolling_std(revenue.pct_change(252).diff(63), 63)
    return _rolling_mean(base, 63)

def revj_098_rev_accel_vol_zscore_63d(revenue: pd.Series) -> pd.Series:
    """revj_098_rev_accel_vol_zscore_63d"""
    base = _rolling_std(revenue.pct_change(252).diff(63), 63)
    return _zscore_rolling(base, 63)

def revj_099_rev_accel_vol_rank_63d(revenue: pd.Series) -> pd.Series:
    """revj_099_rev_accel_vol_rank_63d"""
    base = _rolling_std(revenue.pct_change(252).diff(63), 63)
    return _rank_pct(base, 63)

def revj_100_rev_accel_vol_lvl_126d(revenue: pd.Series) -> pd.Series:
    """revj_100_rev_accel_vol_lvl_126d"""
    base = _rolling_std(revenue.pct_change(252).diff(63), 63)
    return _rolling_mean(base, 126)

def revj_101_rev_accel_vol_zscore_126d(revenue: pd.Series) -> pd.Series:
    """revj_101_rev_accel_vol_zscore_126d"""
    base = _rolling_std(revenue.pct_change(252).diff(63), 63)
    return _zscore_rolling(base, 126)

def revj_102_rev_accel_vol_rank_126d(revenue: pd.Series) -> pd.Series:
    """revj_102_rev_accel_vol_rank_126d"""
    base = _rolling_std(revenue.pct_change(252).diff(63), 63)
    return _rank_pct(base, 126)

def revj_103_rev_accel_vol_lvl_252d(revenue: pd.Series) -> pd.Series:
    """revj_103_rev_accel_vol_lvl_252d"""
    base = _rolling_std(revenue.pct_change(252).diff(63), 63)
    return _rolling_mean(base, 252)

def revj_104_rev_accel_vol_zscore_252d(revenue: pd.Series) -> pd.Series:
    """revj_104_rev_accel_vol_zscore_252d"""
    base = _rolling_std(revenue.pct_change(252).diff(63), 63)
    return _zscore_rolling(base, 252)

def revj_105_rev_accel_vol_rank_252d(revenue: pd.Series) -> pd.Series:
    """revj_105_rev_accel_vol_rank_252d"""
    base = _rolling_std(revenue.pct_change(252).diff(63), 63)
    return _rank_pct(base, 252)

def revj_106_rev_jerk_vol_lvl_5d(revenue: pd.Series) -> pd.Series:
    """revj_106_rev_jerk_vol_lvl_5d"""
    base = _rolling_std(revenue.pct_change(252).diff(63).diff(21), 63)
    return _rolling_mean(base, 5)

def revj_107_rev_jerk_vol_zscore_5d(revenue: pd.Series) -> pd.Series:
    """revj_107_rev_jerk_vol_zscore_5d"""
    base = _rolling_std(revenue.pct_change(252).diff(63).diff(21), 63)
    return _zscore_rolling(base, 5)

def revj_108_rev_jerk_vol_rank_5d(revenue: pd.Series) -> pd.Series:
    """revj_108_rev_jerk_vol_rank_5d"""
    base = _rolling_std(revenue.pct_change(252).diff(63).diff(21), 63)
    return _rank_pct(base, 5)

def revj_109_rev_jerk_vol_lvl_21d(revenue: pd.Series) -> pd.Series:
    """revj_109_rev_jerk_vol_lvl_21d"""
    base = _rolling_std(revenue.pct_change(252).diff(63).diff(21), 63)
    return _rolling_mean(base, 21)

def revj_110_rev_jerk_vol_zscore_21d(revenue: pd.Series) -> pd.Series:
    """revj_110_rev_jerk_vol_zscore_21d"""
    base = _rolling_std(revenue.pct_change(252).diff(63).diff(21), 63)
    return _zscore_rolling(base, 21)

def revj_111_rev_jerk_vol_rank_21d(revenue: pd.Series) -> pd.Series:
    """revj_111_rev_jerk_vol_rank_21d"""
    base = _rolling_std(revenue.pct_change(252).diff(63).diff(21), 63)
    return _rank_pct(base, 21)

def revj_112_rev_jerk_vol_lvl_63d(revenue: pd.Series) -> pd.Series:
    """revj_112_rev_jerk_vol_lvl_63d"""
    base = _rolling_std(revenue.pct_change(252).diff(63).diff(21), 63)
    return _rolling_mean(base, 63)

def revj_113_rev_jerk_vol_zscore_63d(revenue: pd.Series) -> pd.Series:
    """revj_113_rev_jerk_vol_zscore_63d"""
    base = _rolling_std(revenue.pct_change(252).diff(63).diff(21), 63)
    return _zscore_rolling(base, 63)

def revj_114_rev_jerk_vol_rank_63d(revenue: pd.Series) -> pd.Series:
    """revj_114_rev_jerk_vol_rank_63d"""
    base = _rolling_std(revenue.pct_change(252).diff(63).diff(21), 63)
    return _rank_pct(base, 63)

def revj_115_rev_jerk_vol_lvl_126d(revenue: pd.Series) -> pd.Series:
    """revj_115_rev_jerk_vol_lvl_126d"""
    base = _rolling_std(revenue.pct_change(252).diff(63).diff(21), 63)
    return _rolling_mean(base, 126)

def revj_116_rev_jerk_vol_zscore_126d(revenue: pd.Series) -> pd.Series:
    """revj_116_rev_jerk_vol_zscore_126d"""
    base = _rolling_std(revenue.pct_change(252).diff(63).diff(21), 63)
    return _zscore_rolling(base, 126)

def revj_117_rev_jerk_vol_rank_126d(revenue: pd.Series) -> pd.Series:
    """revj_117_rev_jerk_vol_rank_126d"""
    base = _rolling_std(revenue.pct_change(252).diff(63).diff(21), 63)
    return _rank_pct(base, 126)

def revj_118_rev_jerk_vol_lvl_252d(revenue: pd.Series) -> pd.Series:
    """revj_118_rev_jerk_vol_lvl_252d"""
    base = _rolling_std(revenue.pct_change(252).diff(63).diff(21), 63)
    return _rolling_mean(base, 252)

def revj_119_rev_jerk_vol_zscore_252d(revenue: pd.Series) -> pd.Series:
    """revj_119_rev_jerk_vol_zscore_252d"""
    base = _rolling_std(revenue.pct_change(252).diff(63).diff(21), 63)
    return _zscore_rolling(base, 252)

def revj_120_rev_jerk_vol_rank_252d(revenue: pd.Series) -> pd.Series:
    """revj_120_rev_jerk_vol_rank_252d"""
    base = _rolling_std(revenue.pct_change(252).diff(63).diff(21), 63)
    return _rank_pct(base, 252)

def revj_121_rev_accel_mom_lvl_5d(revenue: pd.Series) -> pd.Series:
    """revj_121_rev_accel_mom_lvl_5d"""
    base = revenue.pct_change(252).diff(63).pct_change(21)
    return _rolling_mean(base, 5)

def revj_122_rev_accel_mom_zscore_5d(revenue: pd.Series) -> pd.Series:
    """revj_122_rev_accel_mom_zscore_5d"""
    base = revenue.pct_change(252).diff(63).pct_change(21)
    return _zscore_rolling(base, 5)

def revj_123_rev_accel_mom_rank_5d(revenue: pd.Series) -> pd.Series:
    """revj_123_rev_accel_mom_rank_5d"""
    base = revenue.pct_change(252).diff(63).pct_change(21)
    return _rank_pct(base, 5)

def revj_124_rev_accel_mom_lvl_21d(revenue: pd.Series) -> pd.Series:
    """revj_124_rev_accel_mom_lvl_21d"""
    base = revenue.pct_change(252).diff(63).pct_change(21)
    return _rolling_mean(base, 21)

def revj_125_rev_accel_mom_zscore_21d(revenue: pd.Series) -> pd.Series:
    """revj_125_rev_accel_mom_zscore_21d"""
    base = revenue.pct_change(252).diff(63).pct_change(21)
    return _zscore_rolling(base, 21)

def revj_126_rev_accel_mom_rank_21d(revenue: pd.Series) -> pd.Series:
    """revj_126_rev_accel_mom_rank_21d"""
    base = revenue.pct_change(252).diff(63).pct_change(21)
    return _rank_pct(base, 21)

def revj_127_rev_accel_mom_lvl_63d(revenue: pd.Series) -> pd.Series:
    """revj_127_rev_accel_mom_lvl_63d"""
    base = revenue.pct_change(252).diff(63).pct_change(21)
    return _rolling_mean(base, 63)

def revj_128_rev_accel_mom_zscore_63d(revenue: pd.Series) -> pd.Series:
    """revj_128_rev_accel_mom_zscore_63d"""
    base = revenue.pct_change(252).diff(63).pct_change(21)
    return _zscore_rolling(base, 63)

def revj_129_rev_accel_mom_rank_63d(revenue: pd.Series) -> pd.Series:
    """revj_129_rev_accel_mom_rank_63d"""
    base = revenue.pct_change(252).diff(63).pct_change(21)
    return _rank_pct(base, 63)

def revj_130_rev_accel_mom_lvl_126d(revenue: pd.Series) -> pd.Series:
    """revj_130_rev_accel_mom_lvl_126d"""
    base = revenue.pct_change(252).diff(63).pct_change(21)
    return _rolling_mean(base, 126)

def revj_131_rev_accel_mom_zscore_126d(revenue: pd.Series) -> pd.Series:
    """revj_131_rev_accel_mom_zscore_126d"""
    base = revenue.pct_change(252).diff(63).pct_change(21)
    return _zscore_rolling(base, 126)

def revj_132_rev_accel_mom_rank_126d(revenue: pd.Series) -> pd.Series:
    """revj_132_rev_accel_mom_rank_126d"""
    base = revenue.pct_change(252).diff(63).pct_change(21)
    return _rank_pct(base, 126)

def revj_133_rev_accel_mom_lvl_252d(revenue: pd.Series) -> pd.Series:
    """revj_133_rev_accel_mom_lvl_252d"""
    base = revenue.pct_change(252).diff(63).pct_change(21)
    return _rolling_mean(base, 252)

def revj_134_rev_accel_mom_zscore_252d(revenue: pd.Series) -> pd.Series:
    """revj_134_rev_accel_mom_zscore_252d"""
    base = revenue.pct_change(252).diff(63).pct_change(21)
    return _zscore_rolling(base, 252)

def revj_135_rev_accel_mom_rank_252d(revenue: pd.Series) -> pd.Series:
    """revj_135_rev_accel_mom_rank_252d"""
    base = revenue.pct_change(252).diff(63).pct_change(21)
    return _rank_pct(base, 252)

def revj_136_rev_jerk_mom_lvl_5d(revenue: pd.Series) -> pd.Series:
    """revj_136_rev_jerk_mom_lvl_5d"""
    base = revenue.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rolling_mean(base, 5)

def revj_137_rev_jerk_mom_zscore_5d(revenue: pd.Series) -> pd.Series:
    """revj_137_rev_jerk_mom_zscore_5d"""
    base = revenue.pct_change(252).diff(63).diff(21).pct_change(5)
    return _zscore_rolling(base, 5)

def revj_138_rev_jerk_mom_rank_5d(revenue: pd.Series) -> pd.Series:
    """revj_138_rev_jerk_mom_rank_5d"""
    base = revenue.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rank_pct(base, 5)

def revj_139_rev_jerk_mom_lvl_21d(revenue: pd.Series) -> pd.Series:
    """revj_139_rev_jerk_mom_lvl_21d"""
    base = revenue.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rolling_mean(base, 21)

def revj_140_rev_jerk_mom_zscore_21d(revenue: pd.Series) -> pd.Series:
    """revj_140_rev_jerk_mom_zscore_21d"""
    base = revenue.pct_change(252).diff(63).diff(21).pct_change(5)
    return _zscore_rolling(base, 21)

def revj_141_rev_jerk_mom_rank_21d(revenue: pd.Series) -> pd.Series:
    """revj_141_rev_jerk_mom_rank_21d"""
    base = revenue.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rank_pct(base, 21)

def revj_142_rev_jerk_mom_lvl_63d(revenue: pd.Series) -> pd.Series:
    """revj_142_rev_jerk_mom_lvl_63d"""
    base = revenue.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rolling_mean(base, 63)

def revj_143_rev_jerk_mom_zscore_63d(revenue: pd.Series) -> pd.Series:
    """revj_143_rev_jerk_mom_zscore_63d"""
    base = revenue.pct_change(252).diff(63).diff(21).pct_change(5)
    return _zscore_rolling(base, 63)

def revj_144_rev_jerk_mom_rank_63d(revenue: pd.Series) -> pd.Series:
    """revj_144_rev_jerk_mom_rank_63d"""
    base = revenue.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rank_pct(base, 63)

def revj_145_rev_jerk_mom_lvl_126d(revenue: pd.Series) -> pd.Series:
    """revj_145_rev_jerk_mom_lvl_126d"""
    base = revenue.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rolling_mean(base, 126)

def revj_146_rev_jerk_mom_zscore_126d(revenue: pd.Series) -> pd.Series:
    """revj_146_rev_jerk_mom_zscore_126d"""
    base = revenue.pct_change(252).diff(63).diff(21).pct_change(5)
    return _zscore_rolling(base, 126)

def revj_147_rev_jerk_mom_rank_126d(revenue: pd.Series) -> pd.Series:
    """revj_147_rev_jerk_mom_rank_126d"""
    base = revenue.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rank_pct(base, 126)

def revj_148_rev_jerk_mom_lvl_252d(revenue: pd.Series) -> pd.Series:
    """revj_148_rev_jerk_mom_lvl_252d"""
    base = revenue.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rolling_mean(base, 252)

def revj_149_rev_jerk_mom_zscore_252d(revenue: pd.Series) -> pd.Series:
    """revj_149_rev_jerk_mom_zscore_252d"""
    base = revenue.pct_change(252).diff(63).diff(21).pct_change(5)
    return _zscore_rolling(base, 252)

def revj_150_rev_jerk_mom_rank_252d(revenue: pd.Series) -> pd.Series:
    """revj_150_rev_jerk_mom_rank_252d"""
    base = revenue.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V58_REGISTRY_2 = {
    "revj_076_rev_jerk_rank_lvl_5d": {"inputs": ["revenue"], "func": revj_076_rev_jerk_rank_lvl_5d},
    "revj_077_rev_jerk_rank_zscore_5d": {"inputs": ["revenue"], "func": revj_077_rev_jerk_rank_zscore_5d},
    "revj_078_rev_jerk_rank_rank_5d": {"inputs": ["revenue"], "func": revj_078_rev_jerk_rank_rank_5d},
    "revj_079_rev_jerk_rank_lvl_21d": {"inputs": ["revenue"], "func": revj_079_rev_jerk_rank_lvl_21d},
    "revj_080_rev_jerk_rank_zscore_21d": {"inputs": ["revenue"], "func": revj_080_rev_jerk_rank_zscore_21d},
    "revj_081_rev_jerk_rank_rank_21d": {"inputs": ["revenue"], "func": revj_081_rev_jerk_rank_rank_21d},
    "revj_082_rev_jerk_rank_lvl_63d": {"inputs": ["revenue"], "func": revj_082_rev_jerk_rank_lvl_63d},
    "revj_083_rev_jerk_rank_zscore_63d": {"inputs": ["revenue"], "func": revj_083_rev_jerk_rank_zscore_63d},
    "revj_084_rev_jerk_rank_rank_63d": {"inputs": ["revenue"], "func": revj_084_rev_jerk_rank_rank_63d},
    "revj_085_rev_jerk_rank_lvl_126d": {"inputs": ["revenue"], "func": revj_085_rev_jerk_rank_lvl_126d},
    "revj_086_rev_jerk_rank_zscore_126d": {"inputs": ["revenue"], "func": revj_086_rev_jerk_rank_zscore_126d},
    "revj_087_rev_jerk_rank_rank_126d": {"inputs": ["revenue"], "func": revj_087_rev_jerk_rank_rank_126d},
    "revj_088_rev_jerk_rank_lvl_252d": {"inputs": ["revenue"], "func": revj_088_rev_jerk_rank_lvl_252d},
    "revj_089_rev_jerk_rank_zscore_252d": {"inputs": ["revenue"], "func": revj_089_rev_jerk_rank_zscore_252d},
    "revj_090_rev_jerk_rank_rank_252d": {"inputs": ["revenue"], "func": revj_090_rev_jerk_rank_rank_252d},
    "revj_091_rev_accel_vol_lvl_5d": {"inputs": ["revenue"], "func": revj_091_rev_accel_vol_lvl_5d},
    "revj_092_rev_accel_vol_zscore_5d": {"inputs": ["revenue"], "func": revj_092_rev_accel_vol_zscore_5d},
    "revj_093_rev_accel_vol_rank_5d": {"inputs": ["revenue"], "func": revj_093_rev_accel_vol_rank_5d},
    "revj_094_rev_accel_vol_lvl_21d": {"inputs": ["revenue"], "func": revj_094_rev_accel_vol_lvl_21d},
    "revj_095_rev_accel_vol_zscore_21d": {"inputs": ["revenue"], "func": revj_095_rev_accel_vol_zscore_21d},
    "revj_096_rev_accel_vol_rank_21d": {"inputs": ["revenue"], "func": revj_096_rev_accel_vol_rank_21d},
    "revj_097_rev_accel_vol_lvl_63d": {"inputs": ["revenue"], "func": revj_097_rev_accel_vol_lvl_63d},
    "revj_098_rev_accel_vol_zscore_63d": {"inputs": ["revenue"], "func": revj_098_rev_accel_vol_zscore_63d},
    "revj_099_rev_accel_vol_rank_63d": {"inputs": ["revenue"], "func": revj_099_rev_accel_vol_rank_63d},
    "revj_100_rev_accel_vol_lvl_126d": {"inputs": ["revenue"], "func": revj_100_rev_accel_vol_lvl_126d},
    "revj_101_rev_accel_vol_zscore_126d": {"inputs": ["revenue"], "func": revj_101_rev_accel_vol_zscore_126d},
    "revj_102_rev_accel_vol_rank_126d": {"inputs": ["revenue"], "func": revj_102_rev_accel_vol_rank_126d},
    "revj_103_rev_accel_vol_lvl_252d": {"inputs": ["revenue"], "func": revj_103_rev_accel_vol_lvl_252d},
    "revj_104_rev_accel_vol_zscore_252d": {"inputs": ["revenue"], "func": revj_104_rev_accel_vol_zscore_252d},
    "revj_105_rev_accel_vol_rank_252d": {"inputs": ["revenue"], "func": revj_105_rev_accel_vol_rank_252d},
    "revj_106_rev_jerk_vol_lvl_5d": {"inputs": ["revenue"], "func": revj_106_rev_jerk_vol_lvl_5d},
    "revj_107_rev_jerk_vol_zscore_5d": {"inputs": ["revenue"], "func": revj_107_rev_jerk_vol_zscore_5d},
    "revj_108_rev_jerk_vol_rank_5d": {"inputs": ["revenue"], "func": revj_108_rev_jerk_vol_rank_5d},
    "revj_109_rev_jerk_vol_lvl_21d": {"inputs": ["revenue"], "func": revj_109_rev_jerk_vol_lvl_21d},
    "revj_110_rev_jerk_vol_zscore_21d": {"inputs": ["revenue"], "func": revj_110_rev_jerk_vol_zscore_21d},
    "revj_111_rev_jerk_vol_rank_21d": {"inputs": ["revenue"], "func": revj_111_rev_jerk_vol_rank_21d},
    "revj_112_rev_jerk_vol_lvl_63d": {"inputs": ["revenue"], "func": revj_112_rev_jerk_vol_lvl_63d},
    "revj_113_rev_jerk_vol_zscore_63d": {"inputs": ["revenue"], "func": revj_113_rev_jerk_vol_zscore_63d},
    "revj_114_rev_jerk_vol_rank_63d": {"inputs": ["revenue"], "func": revj_114_rev_jerk_vol_rank_63d},
    "revj_115_rev_jerk_vol_lvl_126d": {"inputs": ["revenue"], "func": revj_115_rev_jerk_vol_lvl_126d},
    "revj_116_rev_jerk_vol_zscore_126d": {"inputs": ["revenue"], "func": revj_116_rev_jerk_vol_zscore_126d},
    "revj_117_rev_jerk_vol_rank_126d": {"inputs": ["revenue"], "func": revj_117_rev_jerk_vol_rank_126d},
    "revj_118_rev_jerk_vol_lvl_252d": {"inputs": ["revenue"], "func": revj_118_rev_jerk_vol_lvl_252d},
    "revj_119_rev_jerk_vol_zscore_252d": {"inputs": ["revenue"], "func": revj_119_rev_jerk_vol_zscore_252d},
    "revj_120_rev_jerk_vol_rank_252d": {"inputs": ["revenue"], "func": revj_120_rev_jerk_vol_rank_252d},
    "revj_121_rev_accel_mom_lvl_5d": {"inputs": ["revenue"], "func": revj_121_rev_accel_mom_lvl_5d},
    "revj_122_rev_accel_mom_zscore_5d": {"inputs": ["revenue"], "func": revj_122_rev_accel_mom_zscore_5d},
    "revj_123_rev_accel_mom_rank_5d": {"inputs": ["revenue"], "func": revj_123_rev_accel_mom_rank_5d},
    "revj_124_rev_accel_mom_lvl_21d": {"inputs": ["revenue"], "func": revj_124_rev_accel_mom_lvl_21d},
    "revj_125_rev_accel_mom_zscore_21d": {"inputs": ["revenue"], "func": revj_125_rev_accel_mom_zscore_21d},
    "revj_126_rev_accel_mom_rank_21d": {"inputs": ["revenue"], "func": revj_126_rev_accel_mom_rank_21d},
    "revj_127_rev_accel_mom_lvl_63d": {"inputs": ["revenue"], "func": revj_127_rev_accel_mom_lvl_63d},
    "revj_128_rev_accel_mom_zscore_63d": {"inputs": ["revenue"], "func": revj_128_rev_accel_mom_zscore_63d},
    "revj_129_rev_accel_mom_rank_63d": {"inputs": ["revenue"], "func": revj_129_rev_accel_mom_rank_63d},
    "revj_130_rev_accel_mom_lvl_126d": {"inputs": ["revenue"], "func": revj_130_rev_accel_mom_lvl_126d},
    "revj_131_rev_accel_mom_zscore_126d": {"inputs": ["revenue"], "func": revj_131_rev_accel_mom_zscore_126d},
    "revj_132_rev_accel_mom_rank_126d": {"inputs": ["revenue"], "func": revj_132_rev_accel_mom_rank_126d},
    "revj_133_rev_accel_mom_lvl_252d": {"inputs": ["revenue"], "func": revj_133_rev_accel_mom_lvl_252d},
    "revj_134_rev_accel_mom_zscore_252d": {"inputs": ["revenue"], "func": revj_134_rev_accel_mom_zscore_252d},
    "revj_135_rev_accel_mom_rank_252d": {"inputs": ["revenue"], "func": revj_135_rev_accel_mom_rank_252d},
    "revj_136_rev_jerk_mom_lvl_5d": {"inputs": ["revenue"], "func": revj_136_rev_jerk_mom_lvl_5d},
    "revj_137_rev_jerk_mom_zscore_5d": {"inputs": ["revenue"], "func": revj_137_rev_jerk_mom_zscore_5d},
    "revj_138_rev_jerk_mom_rank_5d": {"inputs": ["revenue"], "func": revj_138_rev_jerk_mom_rank_5d},
    "revj_139_rev_jerk_mom_lvl_21d": {"inputs": ["revenue"], "func": revj_139_rev_jerk_mom_lvl_21d},
    "revj_140_rev_jerk_mom_zscore_21d": {"inputs": ["revenue"], "func": revj_140_rev_jerk_mom_zscore_21d},
    "revj_141_rev_jerk_mom_rank_21d": {"inputs": ["revenue"], "func": revj_141_rev_jerk_mom_rank_21d},
    "revj_142_rev_jerk_mom_lvl_63d": {"inputs": ["revenue"], "func": revj_142_rev_jerk_mom_lvl_63d},
    "revj_143_rev_jerk_mom_zscore_63d": {"inputs": ["revenue"], "func": revj_143_rev_jerk_mom_zscore_63d},
    "revj_144_rev_jerk_mom_rank_63d": {"inputs": ["revenue"], "func": revj_144_rev_jerk_mom_rank_63d},
    "revj_145_rev_jerk_mom_lvl_126d": {"inputs": ["revenue"], "func": revj_145_rev_jerk_mom_lvl_126d},
    "revj_146_rev_jerk_mom_zscore_126d": {"inputs": ["revenue"], "func": revj_146_rev_jerk_mom_zscore_126d},
    "revj_147_rev_jerk_mom_rank_126d": {"inputs": ["revenue"], "func": revj_147_rev_jerk_mom_rank_126d},
    "revj_148_rev_jerk_mom_lvl_252d": {"inputs": ["revenue"], "func": revj_148_rev_jerk_mom_lvl_252d},
    "revj_149_rev_jerk_mom_zscore_252d": {"inputs": ["revenue"], "func": revj_149_rev_jerk_mom_zscore_252d},
    "revj_150_rev_jerk_mom_rank_252d": {"inputs": ["revenue"], "func": revj_150_rev_jerk_mom_rank_252d},
}
