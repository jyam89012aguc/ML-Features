"""
55_cash_flow_acceleration — Base Features 076-150
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

def cfa_076_ocf_accel_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_076_ocf_accel_lvl_5d"""
    base = ocf.pct_change(252).diff(63)
    return _rolling_mean(base, 5)

def cfa_077_ocf_accel_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_077_ocf_accel_zscore_5d"""
    base = ocf.pct_change(252).diff(63)
    return _zscore_rolling(base, 5)

def cfa_078_ocf_accel_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_078_ocf_accel_rank_5d"""
    base = ocf.pct_change(252).diff(63)
    return _rank_pct(base, 5)

def cfa_079_ocf_accel_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_079_ocf_accel_lvl_21d"""
    base = ocf.pct_change(252).diff(63)
    return _rolling_mean(base, 21)

def cfa_080_ocf_accel_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_080_ocf_accel_zscore_21d"""
    base = ocf.pct_change(252).diff(63)
    return _zscore_rolling(base, 21)

def cfa_081_ocf_accel_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_081_ocf_accel_rank_21d"""
    base = ocf.pct_change(252).diff(63)
    return _rank_pct(base, 21)

def cfa_082_ocf_accel_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_082_ocf_accel_lvl_63d"""
    base = ocf.pct_change(252).diff(63)
    return _rolling_mean(base, 63)

def cfa_083_ocf_accel_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_083_ocf_accel_zscore_63d"""
    base = ocf.pct_change(252).diff(63)
    return _zscore_rolling(base, 63)

def cfa_084_ocf_accel_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_084_ocf_accel_rank_63d"""
    base = ocf.pct_change(252).diff(63)
    return _rank_pct(base, 63)

def cfa_085_ocf_accel_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_085_ocf_accel_lvl_126d"""
    base = ocf.pct_change(252).diff(63)
    return _rolling_mean(base, 126)

def cfa_086_ocf_accel_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_086_ocf_accel_zscore_126d"""
    base = ocf.pct_change(252).diff(63)
    return _zscore_rolling(base, 126)

def cfa_087_ocf_accel_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_087_ocf_accel_rank_126d"""
    base = ocf.pct_change(252).diff(63)
    return _rank_pct(base, 126)

def cfa_088_ocf_accel_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_088_ocf_accel_lvl_252d"""
    base = ocf.pct_change(252).diff(63)
    return _rolling_mean(base, 252)

def cfa_089_ocf_accel_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_089_ocf_accel_zscore_252d"""
    base = ocf.pct_change(252).diff(63)
    return _zscore_rolling(base, 252)

def cfa_090_ocf_accel_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_090_ocf_accel_rank_252d"""
    base = ocf.pct_change(252).diff(63)
    return _rank_pct(base, 252)

def cfa_091_fcf_accel_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_091_fcf_accel_lvl_5d"""
    base = fcf.pct_change(252).diff(63)
    return _rolling_mean(base, 5)

def cfa_092_fcf_accel_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_092_fcf_accel_zscore_5d"""
    base = fcf.pct_change(252).diff(63)
    return _zscore_rolling(base, 5)

def cfa_093_fcf_accel_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_093_fcf_accel_rank_5d"""
    base = fcf.pct_change(252).diff(63)
    return _rank_pct(base, 5)

def cfa_094_fcf_accel_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_094_fcf_accel_lvl_21d"""
    base = fcf.pct_change(252).diff(63)
    return _rolling_mean(base, 21)

def cfa_095_fcf_accel_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_095_fcf_accel_zscore_21d"""
    base = fcf.pct_change(252).diff(63)
    return _zscore_rolling(base, 21)

def cfa_096_fcf_accel_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_096_fcf_accel_rank_21d"""
    base = fcf.pct_change(252).diff(63)
    return _rank_pct(base, 21)

def cfa_097_fcf_accel_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_097_fcf_accel_lvl_63d"""
    base = fcf.pct_change(252).diff(63)
    return _rolling_mean(base, 63)

def cfa_098_fcf_accel_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_098_fcf_accel_zscore_63d"""
    base = fcf.pct_change(252).diff(63)
    return _zscore_rolling(base, 63)

def cfa_099_fcf_accel_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_099_fcf_accel_rank_63d"""
    base = fcf.pct_change(252).diff(63)
    return _rank_pct(base, 63)

def cfa_100_fcf_accel_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_100_fcf_accel_lvl_126d"""
    base = fcf.pct_change(252).diff(63)
    return _rolling_mean(base, 126)

def cfa_101_fcf_accel_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_101_fcf_accel_zscore_126d"""
    base = fcf.pct_change(252).diff(63)
    return _zscore_rolling(base, 126)

def cfa_102_fcf_accel_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_102_fcf_accel_rank_126d"""
    base = fcf.pct_change(252).diff(63)
    return _rank_pct(base, 126)

def cfa_103_fcf_accel_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_103_fcf_accel_lvl_252d"""
    base = fcf.pct_change(252).diff(63)
    return _rolling_mean(base, 252)

def cfa_104_fcf_accel_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_104_fcf_accel_zscore_252d"""
    base = fcf.pct_change(252).diff(63)
    return _zscore_rolling(base, 252)

def cfa_105_fcf_accel_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_105_fcf_accel_rank_252d"""
    base = fcf.pct_change(252).diff(63)
    return _rank_pct(base, 252)

def cfa_106_cf_margin_chg_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_106_cf_margin_chg_lvl_5d"""
    base = _safe_div(ocf, revenue).diff(252)
    return _rolling_mean(base, 5)

def cfa_107_cf_margin_chg_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_107_cf_margin_chg_zscore_5d"""
    base = _safe_div(ocf, revenue).diff(252)
    return _zscore_rolling(base, 5)

def cfa_108_cf_margin_chg_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_108_cf_margin_chg_rank_5d"""
    base = _safe_div(ocf, revenue).diff(252)
    return _rank_pct(base, 5)

def cfa_109_cf_margin_chg_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_109_cf_margin_chg_lvl_21d"""
    base = _safe_div(ocf, revenue).diff(252)
    return _rolling_mean(base, 21)

def cfa_110_cf_margin_chg_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_110_cf_margin_chg_zscore_21d"""
    base = _safe_div(ocf, revenue).diff(252)
    return _zscore_rolling(base, 21)

def cfa_111_cf_margin_chg_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_111_cf_margin_chg_rank_21d"""
    base = _safe_div(ocf, revenue).diff(252)
    return _rank_pct(base, 21)

def cfa_112_cf_margin_chg_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_112_cf_margin_chg_lvl_63d"""
    base = _safe_div(ocf, revenue).diff(252)
    return _rolling_mean(base, 63)

def cfa_113_cf_margin_chg_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_113_cf_margin_chg_zscore_63d"""
    base = _safe_div(ocf, revenue).diff(252)
    return _zscore_rolling(base, 63)

def cfa_114_cf_margin_chg_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_114_cf_margin_chg_rank_63d"""
    base = _safe_div(ocf, revenue).diff(252)
    return _rank_pct(base, 63)

def cfa_115_cf_margin_chg_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_115_cf_margin_chg_lvl_126d"""
    base = _safe_div(ocf, revenue).diff(252)
    return _rolling_mean(base, 126)

def cfa_116_cf_margin_chg_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_116_cf_margin_chg_zscore_126d"""
    base = _safe_div(ocf, revenue).diff(252)
    return _zscore_rolling(base, 126)

def cfa_117_cf_margin_chg_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_117_cf_margin_chg_rank_126d"""
    base = _safe_div(ocf, revenue).diff(252)
    return _rank_pct(base, 126)

def cfa_118_cf_margin_chg_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_118_cf_margin_chg_lvl_252d"""
    base = _safe_div(ocf, revenue).diff(252)
    return _rolling_mean(base, 252)

def cfa_119_cf_margin_chg_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_119_cf_margin_chg_zscore_252d"""
    base = _safe_div(ocf, revenue).diff(252)
    return _zscore_rolling(base, 252)

def cfa_120_cf_margin_chg_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_120_cf_margin_chg_rank_252d"""
    base = _safe_div(ocf, revenue).diff(252)
    return _rank_pct(base, 252)

def cfa_121_cf_z_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_121_cf_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(ocf, revenue), 252)
    return _rolling_mean(base, 5)

def cfa_122_cf_z_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_122_cf_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(ocf, revenue), 252)
    return _zscore_rolling(base, 5)

def cfa_123_cf_z_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_123_cf_z_rank_5d"""
    base = _zscore_rolling(_safe_div(ocf, revenue), 252)
    return _rank_pct(base, 5)

def cfa_124_cf_z_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_124_cf_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(ocf, revenue), 252)
    return _rolling_mean(base, 21)

def cfa_125_cf_z_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_125_cf_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(ocf, revenue), 252)
    return _zscore_rolling(base, 21)

def cfa_126_cf_z_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_126_cf_z_rank_21d"""
    base = _zscore_rolling(_safe_div(ocf, revenue), 252)
    return _rank_pct(base, 21)

def cfa_127_cf_z_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_127_cf_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(ocf, revenue), 252)
    return _rolling_mean(base, 63)

def cfa_128_cf_z_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_128_cf_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(ocf, revenue), 252)
    return _zscore_rolling(base, 63)

def cfa_129_cf_z_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_129_cf_z_rank_63d"""
    base = _zscore_rolling(_safe_div(ocf, revenue), 252)
    return _rank_pct(base, 63)

def cfa_130_cf_z_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_130_cf_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(ocf, revenue), 252)
    return _rolling_mean(base, 126)

def cfa_131_cf_z_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_131_cf_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(ocf, revenue), 252)
    return _zscore_rolling(base, 126)

def cfa_132_cf_z_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_132_cf_z_rank_126d"""
    base = _zscore_rolling(_safe_div(ocf, revenue), 252)
    return _rank_pct(base, 126)

def cfa_133_cf_z_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_133_cf_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(ocf, revenue), 252)
    return _rolling_mean(base, 252)

def cfa_134_cf_z_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_134_cf_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(ocf, revenue), 252)
    return _zscore_rolling(base, 252)

def cfa_135_cf_z_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_135_cf_z_rank_252d"""
    base = _zscore_rolling(_safe_div(ocf, revenue), 252)
    return _rank_pct(base, 252)

def cfa_136_cf_stability_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_136_cf_stability_lvl_5d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(ocf.pct_change(21), 63))
    return _rolling_mean(base, 5)

def cfa_137_cf_stability_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_137_cf_stability_zscore_5d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(ocf.pct_change(21), 63))
    return _zscore_rolling(base, 5)

def cfa_138_cf_stability_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_138_cf_stability_rank_5d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(ocf.pct_change(21), 63))
    return _rank_pct(base, 5)

def cfa_139_cf_stability_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_139_cf_stability_lvl_21d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(ocf.pct_change(21), 63))
    return _rolling_mean(base, 21)

def cfa_140_cf_stability_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_140_cf_stability_zscore_21d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(ocf.pct_change(21), 63))
    return _zscore_rolling(base, 21)

def cfa_141_cf_stability_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_141_cf_stability_rank_21d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(ocf.pct_change(21), 63))
    return _rank_pct(base, 21)

def cfa_142_cf_stability_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_142_cf_stability_lvl_63d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(ocf.pct_change(21), 63))
    return _rolling_mean(base, 63)

def cfa_143_cf_stability_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_143_cf_stability_zscore_63d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(ocf.pct_change(21), 63))
    return _zscore_rolling(base, 63)

def cfa_144_cf_stability_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_144_cf_stability_rank_63d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(ocf.pct_change(21), 63))
    return _rank_pct(base, 63)

def cfa_145_cf_stability_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_145_cf_stability_lvl_126d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(ocf.pct_change(21), 63))
    return _rolling_mean(base, 126)

def cfa_146_cf_stability_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_146_cf_stability_zscore_126d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(ocf.pct_change(21), 63))
    return _zscore_rolling(base, 126)

def cfa_147_cf_stability_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_147_cf_stability_rank_126d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(ocf.pct_change(21), 63))
    return _rank_pct(base, 126)

def cfa_148_cf_stability_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_148_cf_stability_lvl_252d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(ocf.pct_change(21), 63))
    return _rolling_mean(base, 252)

def cfa_149_cf_stability_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_149_cf_stability_zscore_252d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(ocf.pct_change(21), 63))
    return _zscore_rolling(base, 252)

def cfa_150_cf_stability_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_150_cf_stability_rank_252d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(ocf.pct_change(21), 63))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V55_REGISTRY_2 = {
    "cfa_076_ocf_accel_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_076_ocf_accel_lvl_5d},
    "cfa_077_ocf_accel_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_077_ocf_accel_zscore_5d},
    "cfa_078_ocf_accel_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_078_ocf_accel_rank_5d},
    "cfa_079_ocf_accel_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_079_ocf_accel_lvl_21d},
    "cfa_080_ocf_accel_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_080_ocf_accel_zscore_21d},
    "cfa_081_ocf_accel_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_081_ocf_accel_rank_21d},
    "cfa_082_ocf_accel_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_082_ocf_accel_lvl_63d},
    "cfa_083_ocf_accel_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_083_ocf_accel_zscore_63d},
    "cfa_084_ocf_accel_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_084_ocf_accel_rank_63d},
    "cfa_085_ocf_accel_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_085_ocf_accel_lvl_126d},
    "cfa_086_ocf_accel_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_086_ocf_accel_zscore_126d},
    "cfa_087_ocf_accel_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_087_ocf_accel_rank_126d},
    "cfa_088_ocf_accel_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_088_ocf_accel_lvl_252d},
    "cfa_089_ocf_accel_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_089_ocf_accel_zscore_252d},
    "cfa_090_ocf_accel_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_090_ocf_accel_rank_252d},
    "cfa_091_fcf_accel_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_091_fcf_accel_lvl_5d},
    "cfa_092_fcf_accel_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_092_fcf_accel_zscore_5d},
    "cfa_093_fcf_accel_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_093_fcf_accel_rank_5d},
    "cfa_094_fcf_accel_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_094_fcf_accel_lvl_21d},
    "cfa_095_fcf_accel_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_095_fcf_accel_zscore_21d},
    "cfa_096_fcf_accel_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_096_fcf_accel_rank_21d},
    "cfa_097_fcf_accel_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_097_fcf_accel_lvl_63d},
    "cfa_098_fcf_accel_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_098_fcf_accel_zscore_63d},
    "cfa_099_fcf_accel_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_099_fcf_accel_rank_63d},
    "cfa_100_fcf_accel_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_100_fcf_accel_lvl_126d},
    "cfa_101_fcf_accel_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_101_fcf_accel_zscore_126d},
    "cfa_102_fcf_accel_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_102_fcf_accel_rank_126d},
    "cfa_103_fcf_accel_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_103_fcf_accel_lvl_252d},
    "cfa_104_fcf_accel_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_104_fcf_accel_zscore_252d},
    "cfa_105_fcf_accel_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_105_fcf_accel_rank_252d},
    "cfa_106_cf_margin_chg_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_106_cf_margin_chg_lvl_5d},
    "cfa_107_cf_margin_chg_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_107_cf_margin_chg_zscore_5d},
    "cfa_108_cf_margin_chg_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_108_cf_margin_chg_rank_5d},
    "cfa_109_cf_margin_chg_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_109_cf_margin_chg_lvl_21d},
    "cfa_110_cf_margin_chg_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_110_cf_margin_chg_zscore_21d},
    "cfa_111_cf_margin_chg_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_111_cf_margin_chg_rank_21d},
    "cfa_112_cf_margin_chg_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_112_cf_margin_chg_lvl_63d},
    "cfa_113_cf_margin_chg_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_113_cf_margin_chg_zscore_63d},
    "cfa_114_cf_margin_chg_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_114_cf_margin_chg_rank_63d},
    "cfa_115_cf_margin_chg_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_115_cf_margin_chg_lvl_126d},
    "cfa_116_cf_margin_chg_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_116_cf_margin_chg_zscore_126d},
    "cfa_117_cf_margin_chg_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_117_cf_margin_chg_rank_126d},
    "cfa_118_cf_margin_chg_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_118_cf_margin_chg_lvl_252d},
    "cfa_119_cf_margin_chg_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_119_cf_margin_chg_zscore_252d},
    "cfa_120_cf_margin_chg_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_120_cf_margin_chg_rank_252d},
    "cfa_121_cf_z_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_121_cf_z_lvl_5d},
    "cfa_122_cf_z_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_122_cf_z_zscore_5d},
    "cfa_123_cf_z_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_123_cf_z_rank_5d},
    "cfa_124_cf_z_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_124_cf_z_lvl_21d},
    "cfa_125_cf_z_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_125_cf_z_zscore_21d},
    "cfa_126_cf_z_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_126_cf_z_rank_21d},
    "cfa_127_cf_z_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_127_cf_z_lvl_63d},
    "cfa_128_cf_z_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_128_cf_z_zscore_63d},
    "cfa_129_cf_z_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_129_cf_z_rank_63d},
    "cfa_130_cf_z_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_130_cf_z_lvl_126d},
    "cfa_131_cf_z_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_131_cf_z_zscore_126d},
    "cfa_132_cf_z_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_132_cf_z_rank_126d},
    "cfa_133_cf_z_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_133_cf_z_lvl_252d},
    "cfa_134_cf_z_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_134_cf_z_zscore_252d},
    "cfa_135_cf_z_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_135_cf_z_rank_252d},
    "cfa_136_cf_stability_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_136_cf_stability_lvl_5d},
    "cfa_137_cf_stability_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_137_cf_stability_zscore_5d},
    "cfa_138_cf_stability_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_138_cf_stability_rank_5d},
    "cfa_139_cf_stability_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_139_cf_stability_lvl_21d},
    "cfa_140_cf_stability_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_140_cf_stability_zscore_21d},
    "cfa_141_cf_stability_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_141_cf_stability_rank_21d},
    "cfa_142_cf_stability_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_142_cf_stability_lvl_63d},
    "cfa_143_cf_stability_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_143_cf_stability_zscore_63d},
    "cfa_144_cf_stability_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_144_cf_stability_rank_63d},
    "cfa_145_cf_stability_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_145_cf_stability_lvl_126d},
    "cfa_146_cf_stability_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_146_cf_stability_zscore_126d},
    "cfa_147_cf_stability_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_147_cf_stability_rank_126d},
    "cfa_148_cf_stability_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_148_cf_stability_lvl_252d},
    "cfa_149_cf_stability_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_149_cf_stability_zscore_252d},
    "cfa_150_cf_stability_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_150_cf_stability_rank_252d},
}
