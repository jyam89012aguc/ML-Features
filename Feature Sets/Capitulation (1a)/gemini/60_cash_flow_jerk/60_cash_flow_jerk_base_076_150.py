"""
60_cash_flow_jerk — Base Features 076-150
Domain: cash_flow_jerk
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

def cfjk_076_cf_jerk_rank_lvl_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_076_cf_jerk_rank_lvl_5d"""
    base = _rank_pct(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 5)

def cfjk_077_cf_jerk_rank_zscore_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_077_cf_jerk_rank_zscore_5d"""
    base = _rank_pct(ocf.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 5)

def cfjk_078_cf_jerk_rank_rank_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_078_cf_jerk_rank_rank_5d"""
    base = _rank_pct(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 5)

def cfjk_079_cf_jerk_rank_lvl_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_079_cf_jerk_rank_lvl_21d"""
    base = _rank_pct(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 21)

def cfjk_080_cf_jerk_rank_zscore_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_080_cf_jerk_rank_zscore_21d"""
    base = _rank_pct(ocf.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 21)

def cfjk_081_cf_jerk_rank_rank_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_081_cf_jerk_rank_rank_21d"""
    base = _rank_pct(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 21)

def cfjk_082_cf_jerk_rank_lvl_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_082_cf_jerk_rank_lvl_63d"""
    base = _rank_pct(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 63)

def cfjk_083_cf_jerk_rank_zscore_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_083_cf_jerk_rank_zscore_63d"""
    base = _rank_pct(ocf.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 63)

def cfjk_084_cf_jerk_rank_rank_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_084_cf_jerk_rank_rank_63d"""
    base = _rank_pct(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 63)

def cfjk_085_cf_jerk_rank_lvl_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_085_cf_jerk_rank_lvl_126d"""
    base = _rank_pct(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 126)

def cfjk_086_cf_jerk_rank_zscore_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_086_cf_jerk_rank_zscore_126d"""
    base = _rank_pct(ocf.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 126)

def cfjk_087_cf_jerk_rank_rank_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_087_cf_jerk_rank_rank_126d"""
    base = _rank_pct(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 126)

def cfjk_088_cf_jerk_rank_lvl_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_088_cf_jerk_rank_lvl_252d"""
    base = _rank_pct(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 252)

def cfjk_089_cf_jerk_rank_zscore_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_089_cf_jerk_rank_zscore_252d"""
    base = _rank_pct(ocf.pct_change(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 252)

def cfjk_090_cf_jerk_rank_rank_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_090_cf_jerk_rank_rank_252d"""
    base = _rank_pct(ocf.pct_change(252).diff(63).diff(21), 252)
    return _rank_pct(base, 252)

def cfjk_091_cf_accel_vol_lvl_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_091_cf_accel_vol_lvl_5d"""
    base = _rolling_std(ocf.pct_change(252).diff(63), 63)
    return _rolling_mean(base, 5)

def cfjk_092_cf_accel_vol_zscore_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_092_cf_accel_vol_zscore_5d"""
    base = _rolling_std(ocf.pct_change(252).diff(63), 63)
    return _zscore_rolling(base, 5)

def cfjk_093_cf_accel_vol_rank_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_093_cf_accel_vol_rank_5d"""
    base = _rolling_std(ocf.pct_change(252).diff(63), 63)
    return _rank_pct(base, 5)

def cfjk_094_cf_accel_vol_lvl_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_094_cf_accel_vol_lvl_21d"""
    base = _rolling_std(ocf.pct_change(252).diff(63), 63)
    return _rolling_mean(base, 21)

def cfjk_095_cf_accel_vol_zscore_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_095_cf_accel_vol_zscore_21d"""
    base = _rolling_std(ocf.pct_change(252).diff(63), 63)
    return _zscore_rolling(base, 21)

def cfjk_096_cf_accel_vol_rank_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_096_cf_accel_vol_rank_21d"""
    base = _rolling_std(ocf.pct_change(252).diff(63), 63)
    return _rank_pct(base, 21)

def cfjk_097_cf_accel_vol_lvl_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_097_cf_accel_vol_lvl_63d"""
    base = _rolling_std(ocf.pct_change(252).diff(63), 63)
    return _rolling_mean(base, 63)

def cfjk_098_cf_accel_vol_zscore_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_098_cf_accel_vol_zscore_63d"""
    base = _rolling_std(ocf.pct_change(252).diff(63), 63)
    return _zscore_rolling(base, 63)

def cfjk_099_cf_accel_vol_rank_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_099_cf_accel_vol_rank_63d"""
    base = _rolling_std(ocf.pct_change(252).diff(63), 63)
    return _rank_pct(base, 63)

def cfjk_100_cf_accel_vol_lvl_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_100_cf_accel_vol_lvl_126d"""
    base = _rolling_std(ocf.pct_change(252).diff(63), 63)
    return _rolling_mean(base, 126)

def cfjk_101_cf_accel_vol_zscore_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_101_cf_accel_vol_zscore_126d"""
    base = _rolling_std(ocf.pct_change(252).diff(63), 63)
    return _zscore_rolling(base, 126)

def cfjk_102_cf_accel_vol_rank_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_102_cf_accel_vol_rank_126d"""
    base = _rolling_std(ocf.pct_change(252).diff(63), 63)
    return _rank_pct(base, 126)

def cfjk_103_cf_accel_vol_lvl_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_103_cf_accel_vol_lvl_252d"""
    base = _rolling_std(ocf.pct_change(252).diff(63), 63)
    return _rolling_mean(base, 252)

def cfjk_104_cf_accel_vol_zscore_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_104_cf_accel_vol_zscore_252d"""
    base = _rolling_std(ocf.pct_change(252).diff(63), 63)
    return _zscore_rolling(base, 252)

def cfjk_105_cf_accel_vol_rank_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_105_cf_accel_vol_rank_252d"""
    base = _rolling_std(ocf.pct_change(252).diff(63), 63)
    return _rank_pct(base, 252)

def cfjk_106_cf_jerk_vol_lvl_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_106_cf_jerk_vol_lvl_5d"""
    base = _rolling_std(ocf.pct_change(252).diff(63).diff(21), 63)
    return _rolling_mean(base, 5)

def cfjk_107_cf_jerk_vol_zscore_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_107_cf_jerk_vol_zscore_5d"""
    base = _rolling_std(ocf.pct_change(252).diff(63).diff(21), 63)
    return _zscore_rolling(base, 5)

def cfjk_108_cf_jerk_vol_rank_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_108_cf_jerk_vol_rank_5d"""
    base = _rolling_std(ocf.pct_change(252).diff(63).diff(21), 63)
    return _rank_pct(base, 5)

def cfjk_109_cf_jerk_vol_lvl_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_109_cf_jerk_vol_lvl_21d"""
    base = _rolling_std(ocf.pct_change(252).diff(63).diff(21), 63)
    return _rolling_mean(base, 21)

def cfjk_110_cf_jerk_vol_zscore_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_110_cf_jerk_vol_zscore_21d"""
    base = _rolling_std(ocf.pct_change(252).diff(63).diff(21), 63)
    return _zscore_rolling(base, 21)

def cfjk_111_cf_jerk_vol_rank_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_111_cf_jerk_vol_rank_21d"""
    base = _rolling_std(ocf.pct_change(252).diff(63).diff(21), 63)
    return _rank_pct(base, 21)

def cfjk_112_cf_jerk_vol_lvl_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_112_cf_jerk_vol_lvl_63d"""
    base = _rolling_std(ocf.pct_change(252).diff(63).diff(21), 63)
    return _rolling_mean(base, 63)

def cfjk_113_cf_jerk_vol_zscore_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_113_cf_jerk_vol_zscore_63d"""
    base = _rolling_std(ocf.pct_change(252).diff(63).diff(21), 63)
    return _zscore_rolling(base, 63)

def cfjk_114_cf_jerk_vol_rank_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_114_cf_jerk_vol_rank_63d"""
    base = _rolling_std(ocf.pct_change(252).diff(63).diff(21), 63)
    return _rank_pct(base, 63)

def cfjk_115_cf_jerk_vol_lvl_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_115_cf_jerk_vol_lvl_126d"""
    base = _rolling_std(ocf.pct_change(252).diff(63).diff(21), 63)
    return _rolling_mean(base, 126)

def cfjk_116_cf_jerk_vol_zscore_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_116_cf_jerk_vol_zscore_126d"""
    base = _rolling_std(ocf.pct_change(252).diff(63).diff(21), 63)
    return _zscore_rolling(base, 126)

def cfjk_117_cf_jerk_vol_rank_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_117_cf_jerk_vol_rank_126d"""
    base = _rolling_std(ocf.pct_change(252).diff(63).diff(21), 63)
    return _rank_pct(base, 126)

def cfjk_118_cf_jerk_vol_lvl_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_118_cf_jerk_vol_lvl_252d"""
    base = _rolling_std(ocf.pct_change(252).diff(63).diff(21), 63)
    return _rolling_mean(base, 252)

def cfjk_119_cf_jerk_vol_zscore_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_119_cf_jerk_vol_zscore_252d"""
    base = _rolling_std(ocf.pct_change(252).diff(63).diff(21), 63)
    return _zscore_rolling(base, 252)

def cfjk_120_cf_jerk_vol_rank_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_120_cf_jerk_vol_rank_252d"""
    base = _rolling_std(ocf.pct_change(252).diff(63).diff(21), 63)
    return _rank_pct(base, 252)

def cfjk_121_cf_accel_mom_lvl_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_121_cf_accel_mom_lvl_5d"""
    base = ocf.pct_change(252).diff(63).pct_change(21)
    return _rolling_mean(base, 5)

def cfjk_122_cf_accel_mom_zscore_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_122_cf_accel_mom_zscore_5d"""
    base = ocf.pct_change(252).diff(63).pct_change(21)
    return _zscore_rolling(base, 5)

def cfjk_123_cf_accel_mom_rank_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_123_cf_accel_mom_rank_5d"""
    base = ocf.pct_change(252).diff(63).pct_change(21)
    return _rank_pct(base, 5)

def cfjk_124_cf_accel_mom_lvl_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_124_cf_accel_mom_lvl_21d"""
    base = ocf.pct_change(252).diff(63).pct_change(21)
    return _rolling_mean(base, 21)

def cfjk_125_cf_accel_mom_zscore_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_125_cf_accel_mom_zscore_21d"""
    base = ocf.pct_change(252).diff(63).pct_change(21)
    return _zscore_rolling(base, 21)

def cfjk_126_cf_accel_mom_rank_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_126_cf_accel_mom_rank_21d"""
    base = ocf.pct_change(252).diff(63).pct_change(21)
    return _rank_pct(base, 21)

def cfjk_127_cf_accel_mom_lvl_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_127_cf_accel_mom_lvl_63d"""
    base = ocf.pct_change(252).diff(63).pct_change(21)
    return _rolling_mean(base, 63)

def cfjk_128_cf_accel_mom_zscore_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_128_cf_accel_mom_zscore_63d"""
    base = ocf.pct_change(252).diff(63).pct_change(21)
    return _zscore_rolling(base, 63)

def cfjk_129_cf_accel_mom_rank_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_129_cf_accel_mom_rank_63d"""
    base = ocf.pct_change(252).diff(63).pct_change(21)
    return _rank_pct(base, 63)

def cfjk_130_cf_accel_mom_lvl_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_130_cf_accel_mom_lvl_126d"""
    base = ocf.pct_change(252).diff(63).pct_change(21)
    return _rolling_mean(base, 126)

def cfjk_131_cf_accel_mom_zscore_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_131_cf_accel_mom_zscore_126d"""
    base = ocf.pct_change(252).diff(63).pct_change(21)
    return _zscore_rolling(base, 126)

def cfjk_132_cf_accel_mom_rank_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_132_cf_accel_mom_rank_126d"""
    base = ocf.pct_change(252).diff(63).pct_change(21)
    return _rank_pct(base, 126)

def cfjk_133_cf_accel_mom_lvl_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_133_cf_accel_mom_lvl_252d"""
    base = ocf.pct_change(252).diff(63).pct_change(21)
    return _rolling_mean(base, 252)

def cfjk_134_cf_accel_mom_zscore_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_134_cf_accel_mom_zscore_252d"""
    base = ocf.pct_change(252).diff(63).pct_change(21)
    return _zscore_rolling(base, 252)

def cfjk_135_cf_accel_mom_rank_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_135_cf_accel_mom_rank_252d"""
    base = ocf.pct_change(252).diff(63).pct_change(21)
    return _rank_pct(base, 252)

def cfjk_136_cf_jerk_mom_lvl_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_136_cf_jerk_mom_lvl_5d"""
    base = ocf.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rolling_mean(base, 5)

def cfjk_137_cf_jerk_mom_zscore_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_137_cf_jerk_mom_zscore_5d"""
    base = ocf.pct_change(252).diff(63).diff(21).pct_change(5)
    return _zscore_rolling(base, 5)

def cfjk_138_cf_jerk_mom_rank_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_138_cf_jerk_mom_rank_5d"""
    base = ocf.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rank_pct(base, 5)

def cfjk_139_cf_jerk_mom_lvl_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_139_cf_jerk_mom_lvl_21d"""
    base = ocf.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rolling_mean(base, 21)

def cfjk_140_cf_jerk_mom_zscore_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_140_cf_jerk_mom_zscore_21d"""
    base = ocf.pct_change(252).diff(63).diff(21).pct_change(5)
    return _zscore_rolling(base, 21)

def cfjk_141_cf_jerk_mom_rank_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_141_cf_jerk_mom_rank_21d"""
    base = ocf.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rank_pct(base, 21)

def cfjk_142_cf_jerk_mom_lvl_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_142_cf_jerk_mom_lvl_63d"""
    base = ocf.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rolling_mean(base, 63)

def cfjk_143_cf_jerk_mom_zscore_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_143_cf_jerk_mom_zscore_63d"""
    base = ocf.pct_change(252).diff(63).diff(21).pct_change(5)
    return _zscore_rolling(base, 63)

def cfjk_144_cf_jerk_mom_rank_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_144_cf_jerk_mom_rank_63d"""
    base = ocf.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rank_pct(base, 63)

def cfjk_145_cf_jerk_mom_lvl_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_145_cf_jerk_mom_lvl_126d"""
    base = ocf.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rolling_mean(base, 126)

def cfjk_146_cf_jerk_mom_zscore_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_146_cf_jerk_mom_zscore_126d"""
    base = ocf.pct_change(252).diff(63).diff(21).pct_change(5)
    return _zscore_rolling(base, 126)

def cfjk_147_cf_jerk_mom_rank_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_147_cf_jerk_mom_rank_126d"""
    base = ocf.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rank_pct(base, 126)

def cfjk_148_cf_jerk_mom_lvl_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_148_cf_jerk_mom_lvl_252d"""
    base = ocf.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rolling_mean(base, 252)

def cfjk_149_cf_jerk_mom_zscore_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_149_cf_jerk_mom_zscore_252d"""
    base = ocf.pct_change(252).diff(63).diff(21).pct_change(5)
    return _zscore_rolling(base, 252)

def cfjk_150_cf_jerk_mom_rank_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_150_cf_jerk_mom_rank_252d"""
    base = ocf.pct_change(252).diff(63).diff(21).pct_change(5)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V60_REGISTRY_2 = {
    "cfjk_076_cf_jerk_rank_lvl_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_076_cf_jerk_rank_lvl_5d},
    "cfjk_077_cf_jerk_rank_zscore_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_077_cf_jerk_rank_zscore_5d},
    "cfjk_078_cf_jerk_rank_rank_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_078_cf_jerk_rank_rank_5d},
    "cfjk_079_cf_jerk_rank_lvl_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_079_cf_jerk_rank_lvl_21d},
    "cfjk_080_cf_jerk_rank_zscore_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_080_cf_jerk_rank_zscore_21d},
    "cfjk_081_cf_jerk_rank_rank_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_081_cf_jerk_rank_rank_21d},
    "cfjk_082_cf_jerk_rank_lvl_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_082_cf_jerk_rank_lvl_63d},
    "cfjk_083_cf_jerk_rank_zscore_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_083_cf_jerk_rank_zscore_63d},
    "cfjk_084_cf_jerk_rank_rank_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_084_cf_jerk_rank_rank_63d},
    "cfjk_085_cf_jerk_rank_lvl_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_085_cf_jerk_rank_lvl_126d},
    "cfjk_086_cf_jerk_rank_zscore_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_086_cf_jerk_rank_zscore_126d},
    "cfjk_087_cf_jerk_rank_rank_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_087_cf_jerk_rank_rank_126d},
    "cfjk_088_cf_jerk_rank_lvl_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_088_cf_jerk_rank_lvl_252d},
    "cfjk_089_cf_jerk_rank_zscore_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_089_cf_jerk_rank_zscore_252d},
    "cfjk_090_cf_jerk_rank_rank_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_090_cf_jerk_rank_rank_252d},
    "cfjk_091_cf_accel_vol_lvl_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_091_cf_accel_vol_lvl_5d},
    "cfjk_092_cf_accel_vol_zscore_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_092_cf_accel_vol_zscore_5d},
    "cfjk_093_cf_accel_vol_rank_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_093_cf_accel_vol_rank_5d},
    "cfjk_094_cf_accel_vol_lvl_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_094_cf_accel_vol_lvl_21d},
    "cfjk_095_cf_accel_vol_zscore_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_095_cf_accel_vol_zscore_21d},
    "cfjk_096_cf_accel_vol_rank_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_096_cf_accel_vol_rank_21d},
    "cfjk_097_cf_accel_vol_lvl_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_097_cf_accel_vol_lvl_63d},
    "cfjk_098_cf_accel_vol_zscore_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_098_cf_accel_vol_zscore_63d},
    "cfjk_099_cf_accel_vol_rank_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_099_cf_accel_vol_rank_63d},
    "cfjk_100_cf_accel_vol_lvl_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_100_cf_accel_vol_lvl_126d},
    "cfjk_101_cf_accel_vol_zscore_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_101_cf_accel_vol_zscore_126d},
    "cfjk_102_cf_accel_vol_rank_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_102_cf_accel_vol_rank_126d},
    "cfjk_103_cf_accel_vol_lvl_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_103_cf_accel_vol_lvl_252d},
    "cfjk_104_cf_accel_vol_zscore_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_104_cf_accel_vol_zscore_252d},
    "cfjk_105_cf_accel_vol_rank_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_105_cf_accel_vol_rank_252d},
    "cfjk_106_cf_jerk_vol_lvl_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_106_cf_jerk_vol_lvl_5d},
    "cfjk_107_cf_jerk_vol_zscore_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_107_cf_jerk_vol_zscore_5d},
    "cfjk_108_cf_jerk_vol_rank_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_108_cf_jerk_vol_rank_5d},
    "cfjk_109_cf_jerk_vol_lvl_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_109_cf_jerk_vol_lvl_21d},
    "cfjk_110_cf_jerk_vol_zscore_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_110_cf_jerk_vol_zscore_21d},
    "cfjk_111_cf_jerk_vol_rank_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_111_cf_jerk_vol_rank_21d},
    "cfjk_112_cf_jerk_vol_lvl_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_112_cf_jerk_vol_lvl_63d},
    "cfjk_113_cf_jerk_vol_zscore_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_113_cf_jerk_vol_zscore_63d},
    "cfjk_114_cf_jerk_vol_rank_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_114_cf_jerk_vol_rank_63d},
    "cfjk_115_cf_jerk_vol_lvl_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_115_cf_jerk_vol_lvl_126d},
    "cfjk_116_cf_jerk_vol_zscore_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_116_cf_jerk_vol_zscore_126d},
    "cfjk_117_cf_jerk_vol_rank_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_117_cf_jerk_vol_rank_126d},
    "cfjk_118_cf_jerk_vol_lvl_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_118_cf_jerk_vol_lvl_252d},
    "cfjk_119_cf_jerk_vol_zscore_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_119_cf_jerk_vol_zscore_252d},
    "cfjk_120_cf_jerk_vol_rank_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_120_cf_jerk_vol_rank_252d},
    "cfjk_121_cf_accel_mom_lvl_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_121_cf_accel_mom_lvl_5d},
    "cfjk_122_cf_accel_mom_zscore_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_122_cf_accel_mom_zscore_5d},
    "cfjk_123_cf_accel_mom_rank_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_123_cf_accel_mom_rank_5d},
    "cfjk_124_cf_accel_mom_lvl_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_124_cf_accel_mom_lvl_21d},
    "cfjk_125_cf_accel_mom_zscore_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_125_cf_accel_mom_zscore_21d},
    "cfjk_126_cf_accel_mom_rank_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_126_cf_accel_mom_rank_21d},
    "cfjk_127_cf_accel_mom_lvl_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_127_cf_accel_mom_lvl_63d},
    "cfjk_128_cf_accel_mom_zscore_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_128_cf_accel_mom_zscore_63d},
    "cfjk_129_cf_accel_mom_rank_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_129_cf_accel_mom_rank_63d},
    "cfjk_130_cf_accel_mom_lvl_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_130_cf_accel_mom_lvl_126d},
    "cfjk_131_cf_accel_mom_zscore_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_131_cf_accel_mom_zscore_126d},
    "cfjk_132_cf_accel_mom_rank_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_132_cf_accel_mom_rank_126d},
    "cfjk_133_cf_accel_mom_lvl_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_133_cf_accel_mom_lvl_252d},
    "cfjk_134_cf_accel_mom_zscore_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_134_cf_accel_mom_zscore_252d},
    "cfjk_135_cf_accel_mom_rank_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_135_cf_accel_mom_rank_252d},
    "cfjk_136_cf_jerk_mom_lvl_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_136_cf_jerk_mom_lvl_5d},
    "cfjk_137_cf_jerk_mom_zscore_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_137_cf_jerk_mom_zscore_5d},
    "cfjk_138_cf_jerk_mom_rank_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_138_cf_jerk_mom_rank_5d},
    "cfjk_139_cf_jerk_mom_lvl_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_139_cf_jerk_mom_lvl_21d},
    "cfjk_140_cf_jerk_mom_zscore_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_140_cf_jerk_mom_zscore_21d},
    "cfjk_141_cf_jerk_mom_rank_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_141_cf_jerk_mom_rank_21d},
    "cfjk_142_cf_jerk_mom_lvl_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_142_cf_jerk_mom_lvl_63d},
    "cfjk_143_cf_jerk_mom_zscore_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_143_cf_jerk_mom_zscore_63d},
    "cfjk_144_cf_jerk_mom_rank_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_144_cf_jerk_mom_rank_63d},
    "cfjk_145_cf_jerk_mom_lvl_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_145_cf_jerk_mom_lvl_126d},
    "cfjk_146_cf_jerk_mom_zscore_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_146_cf_jerk_mom_zscore_126d},
    "cfjk_147_cf_jerk_mom_rank_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_147_cf_jerk_mom_rank_126d},
    "cfjk_148_cf_jerk_mom_lvl_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_148_cf_jerk_mom_lvl_252d},
    "cfjk_149_cf_jerk_mom_zscore_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_149_cf_jerk_mom_zscore_252d},
    "cfjk_150_cf_jerk_mom_rank_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_150_cf_jerk_mom_rank_252d},
}
