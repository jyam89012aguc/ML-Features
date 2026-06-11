"""
59_margin_jerk — Base Features 076-150
Domain: margin_jerk
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

def marj_076_margin_jerk_rank_lvl_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_076_margin_jerk_rank_lvl_5d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 5)

def marj_077_margin_jerk_rank_zscore_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_077_margin_jerk_rank_zscore_5d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 5)

def marj_078_margin_jerk_rank_rank_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_078_margin_jerk_rank_rank_5d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rank_pct(base, 5)

def marj_079_margin_jerk_rank_lvl_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_079_margin_jerk_rank_lvl_21d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 21)

def marj_080_margin_jerk_rank_zscore_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_080_margin_jerk_rank_zscore_21d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 21)

def marj_081_margin_jerk_rank_rank_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_081_margin_jerk_rank_rank_21d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rank_pct(base, 21)

def marj_082_margin_jerk_rank_lvl_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_082_margin_jerk_rank_lvl_63d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 63)

def marj_083_margin_jerk_rank_zscore_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_083_margin_jerk_rank_zscore_63d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 63)

def marj_084_margin_jerk_rank_rank_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_084_margin_jerk_rank_rank_63d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rank_pct(base, 63)

def marj_085_margin_jerk_rank_lvl_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_085_margin_jerk_rank_lvl_126d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 126)

def marj_086_margin_jerk_rank_zscore_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_086_margin_jerk_rank_zscore_126d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 126)

def marj_087_margin_jerk_rank_rank_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_087_margin_jerk_rank_rank_126d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rank_pct(base, 126)

def marj_088_margin_jerk_rank_lvl_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_088_margin_jerk_rank_lvl_252d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rolling_mean(base, 252)

def marj_089_margin_jerk_rank_zscore_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_089_margin_jerk_rank_zscore_252d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _zscore_rolling(base, 252)

def marj_090_margin_jerk_rank_rank_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_090_margin_jerk_rank_rank_252d"""
    base = _rank_pct(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)
    return _rank_pct(base, 252)

def marj_091_margin_accel_vol_lvl_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_091_margin_accel_vol_lvl_5d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63), 63)
    return _rolling_mean(base, 5)

def marj_092_margin_accel_vol_zscore_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_092_margin_accel_vol_zscore_5d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63), 63)
    return _zscore_rolling(base, 5)

def marj_093_margin_accel_vol_rank_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_093_margin_accel_vol_rank_5d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63), 63)
    return _rank_pct(base, 5)

def marj_094_margin_accel_vol_lvl_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_094_margin_accel_vol_lvl_21d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63), 63)
    return _rolling_mean(base, 21)

def marj_095_margin_accel_vol_zscore_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_095_margin_accel_vol_zscore_21d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63), 63)
    return _zscore_rolling(base, 21)

def marj_096_margin_accel_vol_rank_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_096_margin_accel_vol_rank_21d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63), 63)
    return _rank_pct(base, 21)

def marj_097_margin_accel_vol_lvl_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_097_margin_accel_vol_lvl_63d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63), 63)
    return _rolling_mean(base, 63)

def marj_098_margin_accel_vol_zscore_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_098_margin_accel_vol_zscore_63d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63), 63)
    return _zscore_rolling(base, 63)

def marj_099_margin_accel_vol_rank_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_099_margin_accel_vol_rank_63d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63), 63)
    return _rank_pct(base, 63)

def marj_100_margin_accel_vol_lvl_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_100_margin_accel_vol_lvl_126d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63), 63)
    return _rolling_mean(base, 126)

def marj_101_margin_accel_vol_zscore_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_101_margin_accel_vol_zscore_126d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63), 63)
    return _zscore_rolling(base, 126)

def marj_102_margin_accel_vol_rank_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_102_margin_accel_vol_rank_126d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63), 63)
    return _rank_pct(base, 126)

def marj_103_margin_accel_vol_lvl_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_103_margin_accel_vol_lvl_252d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63), 63)
    return _rolling_mean(base, 252)

def marj_104_margin_accel_vol_zscore_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_104_margin_accel_vol_zscore_252d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63), 63)
    return _zscore_rolling(base, 252)

def marj_105_margin_accel_vol_rank_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_105_margin_accel_vol_rank_252d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63), 63)
    return _rank_pct(base, 252)

def marj_106_margin_jerk_vol_lvl_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_106_margin_jerk_vol_lvl_5d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 63)
    return _rolling_mean(base, 5)

def marj_107_margin_jerk_vol_zscore_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_107_margin_jerk_vol_zscore_5d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 63)
    return _zscore_rolling(base, 5)

def marj_108_margin_jerk_vol_rank_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_108_margin_jerk_vol_rank_5d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 63)
    return _rank_pct(base, 5)

def marj_109_margin_jerk_vol_lvl_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_109_margin_jerk_vol_lvl_21d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 63)
    return _rolling_mean(base, 21)

def marj_110_margin_jerk_vol_zscore_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_110_margin_jerk_vol_zscore_21d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 63)
    return _zscore_rolling(base, 21)

def marj_111_margin_jerk_vol_rank_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_111_margin_jerk_vol_rank_21d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 63)
    return _rank_pct(base, 21)

def marj_112_margin_jerk_vol_lvl_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_112_margin_jerk_vol_lvl_63d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 63)
    return _rolling_mean(base, 63)

def marj_113_margin_jerk_vol_zscore_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_113_margin_jerk_vol_zscore_63d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 63)
    return _zscore_rolling(base, 63)

def marj_114_margin_jerk_vol_rank_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_114_margin_jerk_vol_rank_63d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 63)
    return _rank_pct(base, 63)

def marj_115_margin_jerk_vol_lvl_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_115_margin_jerk_vol_lvl_126d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 63)
    return _rolling_mean(base, 126)

def marj_116_margin_jerk_vol_zscore_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_116_margin_jerk_vol_zscore_126d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 63)
    return _zscore_rolling(base, 126)

def marj_117_margin_jerk_vol_rank_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_117_margin_jerk_vol_rank_126d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 63)
    return _rank_pct(base, 126)

def marj_118_margin_jerk_vol_lvl_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_118_margin_jerk_vol_lvl_252d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 63)
    return _rolling_mean(base, 252)

def marj_119_margin_jerk_vol_zscore_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_119_margin_jerk_vol_zscore_252d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 63)
    return _zscore_rolling(base, 252)

def marj_120_margin_jerk_vol_rank_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_120_margin_jerk_vol_rank_252d"""
    base = _rolling_std(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 63)
    return _rank_pct(base, 252)

def marj_121_margin_accel_mom_lvl_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_121_margin_accel_mom_lvl_5d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).pct_change(21)
    return _rolling_mean(base, 5)

def marj_122_margin_accel_mom_zscore_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_122_margin_accel_mom_zscore_5d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).pct_change(21)
    return _zscore_rolling(base, 5)

def marj_123_margin_accel_mom_rank_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_123_margin_accel_mom_rank_5d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).pct_change(21)
    return _rank_pct(base, 5)

def marj_124_margin_accel_mom_lvl_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_124_margin_accel_mom_lvl_21d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).pct_change(21)
    return _rolling_mean(base, 21)

def marj_125_margin_accel_mom_zscore_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_125_margin_accel_mom_zscore_21d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).pct_change(21)
    return _zscore_rolling(base, 21)

def marj_126_margin_accel_mom_rank_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_126_margin_accel_mom_rank_21d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).pct_change(21)
    return _rank_pct(base, 21)

def marj_127_margin_accel_mom_lvl_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_127_margin_accel_mom_lvl_63d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).pct_change(21)
    return _rolling_mean(base, 63)

def marj_128_margin_accel_mom_zscore_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_128_margin_accel_mom_zscore_63d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).pct_change(21)
    return _zscore_rolling(base, 63)

def marj_129_margin_accel_mom_rank_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_129_margin_accel_mom_rank_63d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).pct_change(21)
    return _rank_pct(base, 63)

def marj_130_margin_accel_mom_lvl_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_130_margin_accel_mom_lvl_126d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).pct_change(21)
    return _rolling_mean(base, 126)

def marj_131_margin_accel_mom_zscore_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_131_margin_accel_mom_zscore_126d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).pct_change(21)
    return _zscore_rolling(base, 126)

def marj_132_margin_accel_mom_rank_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_132_margin_accel_mom_rank_126d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).pct_change(21)
    return _rank_pct(base, 126)

def marj_133_margin_accel_mom_lvl_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_133_margin_accel_mom_lvl_252d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).pct_change(21)
    return _rolling_mean(base, 252)

def marj_134_margin_accel_mom_zscore_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_134_margin_accel_mom_zscore_252d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).pct_change(21)
    return _zscore_rolling(base, 252)

def marj_135_margin_accel_mom_rank_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_135_margin_accel_mom_rank_252d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).pct_change(21)
    return _rank_pct(base, 252)

def marj_136_margin_jerk_mom_lvl_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_136_margin_jerk_mom_lvl_5d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21).pct_change(5)
    return _rolling_mean(base, 5)

def marj_137_margin_jerk_mom_zscore_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_137_margin_jerk_mom_zscore_5d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21).pct_change(5)
    return _zscore_rolling(base, 5)

def marj_138_margin_jerk_mom_rank_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_138_margin_jerk_mom_rank_5d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21).pct_change(5)
    return _rank_pct(base, 5)

def marj_139_margin_jerk_mom_lvl_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_139_margin_jerk_mom_lvl_21d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21).pct_change(5)
    return _rolling_mean(base, 21)

def marj_140_margin_jerk_mom_zscore_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_140_margin_jerk_mom_zscore_21d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21).pct_change(5)
    return _zscore_rolling(base, 21)

def marj_141_margin_jerk_mom_rank_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_141_margin_jerk_mom_rank_21d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21).pct_change(5)
    return _rank_pct(base, 21)

def marj_142_margin_jerk_mom_lvl_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_142_margin_jerk_mom_lvl_63d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21).pct_change(5)
    return _rolling_mean(base, 63)

def marj_143_margin_jerk_mom_zscore_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_143_margin_jerk_mom_zscore_63d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21).pct_change(5)
    return _zscore_rolling(base, 63)

def marj_144_margin_jerk_mom_rank_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_144_margin_jerk_mom_rank_63d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21).pct_change(5)
    return _rank_pct(base, 63)

def marj_145_margin_jerk_mom_lvl_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_145_margin_jerk_mom_lvl_126d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21).pct_change(5)
    return _rolling_mean(base, 126)

def marj_146_margin_jerk_mom_zscore_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_146_margin_jerk_mom_zscore_126d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21).pct_change(5)
    return _zscore_rolling(base, 126)

def marj_147_margin_jerk_mom_rank_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_147_margin_jerk_mom_rank_126d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21).pct_change(5)
    return _rank_pct(base, 126)

def marj_148_margin_jerk_mom_lvl_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_148_margin_jerk_mom_lvl_252d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21).pct_change(5)
    return _rolling_mean(base, 252)

def marj_149_margin_jerk_mom_zscore_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_149_margin_jerk_mom_zscore_252d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21).pct_change(5)
    return _zscore_rolling(base, 252)

def marj_150_margin_jerk_mom_rank_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_150_margin_jerk_mom_rank_252d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63).diff(21).pct_change(5)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V59_REGISTRY_2 = {
    "marj_076_margin_jerk_rank_lvl_5d": {"inputs": ["netinc", "revenue"], "func": marj_076_margin_jerk_rank_lvl_5d},
    "marj_077_margin_jerk_rank_zscore_5d": {"inputs": ["netinc", "revenue"], "func": marj_077_margin_jerk_rank_zscore_5d},
    "marj_078_margin_jerk_rank_rank_5d": {"inputs": ["netinc", "revenue"], "func": marj_078_margin_jerk_rank_rank_5d},
    "marj_079_margin_jerk_rank_lvl_21d": {"inputs": ["netinc", "revenue"], "func": marj_079_margin_jerk_rank_lvl_21d},
    "marj_080_margin_jerk_rank_zscore_21d": {"inputs": ["netinc", "revenue"], "func": marj_080_margin_jerk_rank_zscore_21d},
    "marj_081_margin_jerk_rank_rank_21d": {"inputs": ["netinc", "revenue"], "func": marj_081_margin_jerk_rank_rank_21d},
    "marj_082_margin_jerk_rank_lvl_63d": {"inputs": ["netinc", "revenue"], "func": marj_082_margin_jerk_rank_lvl_63d},
    "marj_083_margin_jerk_rank_zscore_63d": {"inputs": ["netinc", "revenue"], "func": marj_083_margin_jerk_rank_zscore_63d},
    "marj_084_margin_jerk_rank_rank_63d": {"inputs": ["netinc", "revenue"], "func": marj_084_margin_jerk_rank_rank_63d},
    "marj_085_margin_jerk_rank_lvl_126d": {"inputs": ["netinc", "revenue"], "func": marj_085_margin_jerk_rank_lvl_126d},
    "marj_086_margin_jerk_rank_zscore_126d": {"inputs": ["netinc", "revenue"], "func": marj_086_margin_jerk_rank_zscore_126d},
    "marj_087_margin_jerk_rank_rank_126d": {"inputs": ["netinc", "revenue"], "func": marj_087_margin_jerk_rank_rank_126d},
    "marj_088_margin_jerk_rank_lvl_252d": {"inputs": ["netinc", "revenue"], "func": marj_088_margin_jerk_rank_lvl_252d},
    "marj_089_margin_jerk_rank_zscore_252d": {"inputs": ["netinc", "revenue"], "func": marj_089_margin_jerk_rank_zscore_252d},
    "marj_090_margin_jerk_rank_rank_252d": {"inputs": ["netinc", "revenue"], "func": marj_090_margin_jerk_rank_rank_252d},
    "marj_091_margin_accel_vol_lvl_5d": {"inputs": ["netinc", "revenue"], "func": marj_091_margin_accel_vol_lvl_5d},
    "marj_092_margin_accel_vol_zscore_5d": {"inputs": ["netinc", "revenue"], "func": marj_092_margin_accel_vol_zscore_5d},
    "marj_093_margin_accel_vol_rank_5d": {"inputs": ["netinc", "revenue"], "func": marj_093_margin_accel_vol_rank_5d},
    "marj_094_margin_accel_vol_lvl_21d": {"inputs": ["netinc", "revenue"], "func": marj_094_margin_accel_vol_lvl_21d},
    "marj_095_margin_accel_vol_zscore_21d": {"inputs": ["netinc", "revenue"], "func": marj_095_margin_accel_vol_zscore_21d},
    "marj_096_margin_accel_vol_rank_21d": {"inputs": ["netinc", "revenue"], "func": marj_096_margin_accel_vol_rank_21d},
    "marj_097_margin_accel_vol_lvl_63d": {"inputs": ["netinc", "revenue"], "func": marj_097_margin_accel_vol_lvl_63d},
    "marj_098_margin_accel_vol_zscore_63d": {"inputs": ["netinc", "revenue"], "func": marj_098_margin_accel_vol_zscore_63d},
    "marj_099_margin_accel_vol_rank_63d": {"inputs": ["netinc", "revenue"], "func": marj_099_margin_accel_vol_rank_63d},
    "marj_100_margin_accel_vol_lvl_126d": {"inputs": ["netinc", "revenue"], "func": marj_100_margin_accel_vol_lvl_126d},
    "marj_101_margin_accel_vol_zscore_126d": {"inputs": ["netinc", "revenue"], "func": marj_101_margin_accel_vol_zscore_126d},
    "marj_102_margin_accel_vol_rank_126d": {"inputs": ["netinc", "revenue"], "func": marj_102_margin_accel_vol_rank_126d},
    "marj_103_margin_accel_vol_lvl_252d": {"inputs": ["netinc", "revenue"], "func": marj_103_margin_accel_vol_lvl_252d},
    "marj_104_margin_accel_vol_zscore_252d": {"inputs": ["netinc", "revenue"], "func": marj_104_margin_accel_vol_zscore_252d},
    "marj_105_margin_accel_vol_rank_252d": {"inputs": ["netinc", "revenue"], "func": marj_105_margin_accel_vol_rank_252d},
    "marj_106_margin_jerk_vol_lvl_5d": {"inputs": ["netinc", "revenue"], "func": marj_106_margin_jerk_vol_lvl_5d},
    "marj_107_margin_jerk_vol_zscore_5d": {"inputs": ["netinc", "revenue"], "func": marj_107_margin_jerk_vol_zscore_5d},
    "marj_108_margin_jerk_vol_rank_5d": {"inputs": ["netinc", "revenue"], "func": marj_108_margin_jerk_vol_rank_5d},
    "marj_109_margin_jerk_vol_lvl_21d": {"inputs": ["netinc", "revenue"], "func": marj_109_margin_jerk_vol_lvl_21d},
    "marj_110_margin_jerk_vol_zscore_21d": {"inputs": ["netinc", "revenue"], "func": marj_110_margin_jerk_vol_zscore_21d},
    "marj_111_margin_jerk_vol_rank_21d": {"inputs": ["netinc", "revenue"], "func": marj_111_margin_jerk_vol_rank_21d},
    "marj_112_margin_jerk_vol_lvl_63d": {"inputs": ["netinc", "revenue"], "func": marj_112_margin_jerk_vol_lvl_63d},
    "marj_113_margin_jerk_vol_zscore_63d": {"inputs": ["netinc", "revenue"], "func": marj_113_margin_jerk_vol_zscore_63d},
    "marj_114_margin_jerk_vol_rank_63d": {"inputs": ["netinc", "revenue"], "func": marj_114_margin_jerk_vol_rank_63d},
    "marj_115_margin_jerk_vol_lvl_126d": {"inputs": ["netinc", "revenue"], "func": marj_115_margin_jerk_vol_lvl_126d},
    "marj_116_margin_jerk_vol_zscore_126d": {"inputs": ["netinc", "revenue"], "func": marj_116_margin_jerk_vol_zscore_126d},
    "marj_117_margin_jerk_vol_rank_126d": {"inputs": ["netinc", "revenue"], "func": marj_117_margin_jerk_vol_rank_126d},
    "marj_118_margin_jerk_vol_lvl_252d": {"inputs": ["netinc", "revenue"], "func": marj_118_margin_jerk_vol_lvl_252d},
    "marj_119_margin_jerk_vol_zscore_252d": {"inputs": ["netinc", "revenue"], "func": marj_119_margin_jerk_vol_zscore_252d},
    "marj_120_margin_jerk_vol_rank_252d": {"inputs": ["netinc", "revenue"], "func": marj_120_margin_jerk_vol_rank_252d},
    "marj_121_margin_accel_mom_lvl_5d": {"inputs": ["netinc", "revenue"], "func": marj_121_margin_accel_mom_lvl_5d},
    "marj_122_margin_accel_mom_zscore_5d": {"inputs": ["netinc", "revenue"], "func": marj_122_margin_accel_mom_zscore_5d},
    "marj_123_margin_accel_mom_rank_5d": {"inputs": ["netinc", "revenue"], "func": marj_123_margin_accel_mom_rank_5d},
    "marj_124_margin_accel_mom_lvl_21d": {"inputs": ["netinc", "revenue"], "func": marj_124_margin_accel_mom_lvl_21d},
    "marj_125_margin_accel_mom_zscore_21d": {"inputs": ["netinc", "revenue"], "func": marj_125_margin_accel_mom_zscore_21d},
    "marj_126_margin_accel_mom_rank_21d": {"inputs": ["netinc", "revenue"], "func": marj_126_margin_accel_mom_rank_21d},
    "marj_127_margin_accel_mom_lvl_63d": {"inputs": ["netinc", "revenue"], "func": marj_127_margin_accel_mom_lvl_63d},
    "marj_128_margin_accel_mom_zscore_63d": {"inputs": ["netinc", "revenue"], "func": marj_128_margin_accel_mom_zscore_63d},
    "marj_129_margin_accel_mom_rank_63d": {"inputs": ["netinc", "revenue"], "func": marj_129_margin_accel_mom_rank_63d},
    "marj_130_margin_accel_mom_lvl_126d": {"inputs": ["netinc", "revenue"], "func": marj_130_margin_accel_mom_lvl_126d},
    "marj_131_margin_accel_mom_zscore_126d": {"inputs": ["netinc", "revenue"], "func": marj_131_margin_accel_mom_zscore_126d},
    "marj_132_margin_accel_mom_rank_126d": {"inputs": ["netinc", "revenue"], "func": marj_132_margin_accel_mom_rank_126d},
    "marj_133_margin_accel_mom_lvl_252d": {"inputs": ["netinc", "revenue"], "func": marj_133_margin_accel_mom_lvl_252d},
    "marj_134_margin_accel_mom_zscore_252d": {"inputs": ["netinc", "revenue"], "func": marj_134_margin_accel_mom_zscore_252d},
    "marj_135_margin_accel_mom_rank_252d": {"inputs": ["netinc", "revenue"], "func": marj_135_margin_accel_mom_rank_252d},
    "marj_136_margin_jerk_mom_lvl_5d": {"inputs": ["netinc", "revenue"], "func": marj_136_margin_jerk_mom_lvl_5d},
    "marj_137_margin_jerk_mom_zscore_5d": {"inputs": ["netinc", "revenue"], "func": marj_137_margin_jerk_mom_zscore_5d},
    "marj_138_margin_jerk_mom_rank_5d": {"inputs": ["netinc", "revenue"], "func": marj_138_margin_jerk_mom_rank_5d},
    "marj_139_margin_jerk_mom_lvl_21d": {"inputs": ["netinc", "revenue"], "func": marj_139_margin_jerk_mom_lvl_21d},
    "marj_140_margin_jerk_mom_zscore_21d": {"inputs": ["netinc", "revenue"], "func": marj_140_margin_jerk_mom_zscore_21d},
    "marj_141_margin_jerk_mom_rank_21d": {"inputs": ["netinc", "revenue"], "func": marj_141_margin_jerk_mom_rank_21d},
    "marj_142_margin_jerk_mom_lvl_63d": {"inputs": ["netinc", "revenue"], "func": marj_142_margin_jerk_mom_lvl_63d},
    "marj_143_margin_jerk_mom_zscore_63d": {"inputs": ["netinc", "revenue"], "func": marj_143_margin_jerk_mom_zscore_63d},
    "marj_144_margin_jerk_mom_rank_63d": {"inputs": ["netinc", "revenue"], "func": marj_144_margin_jerk_mom_rank_63d},
    "marj_145_margin_jerk_mom_lvl_126d": {"inputs": ["netinc", "revenue"], "func": marj_145_margin_jerk_mom_lvl_126d},
    "marj_146_margin_jerk_mom_zscore_126d": {"inputs": ["netinc", "revenue"], "func": marj_146_margin_jerk_mom_zscore_126d},
    "marj_147_margin_jerk_mom_rank_126d": {"inputs": ["netinc", "revenue"], "func": marj_147_margin_jerk_mom_rank_126d},
    "marj_148_margin_jerk_mom_lvl_252d": {"inputs": ["netinc", "revenue"], "func": marj_148_margin_jerk_mom_lvl_252d},
    "marj_149_margin_jerk_mom_zscore_252d": {"inputs": ["netinc", "revenue"], "func": marj_149_margin_jerk_mom_zscore_252d},
    "marj_150_margin_jerk_mom_rank_252d": {"inputs": ["netinc", "revenue"], "func": marj_150_margin_jerk_mom_rank_252d},
}
