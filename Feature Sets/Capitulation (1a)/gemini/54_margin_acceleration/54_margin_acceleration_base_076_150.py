"""
54_margin_acceleration — Base Features 076-150
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

def maga_076_margin_accel_lvl_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_076_margin_accel_lvl_5d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rolling_mean(base, 5)

def maga_077_margin_accel_zscore_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_077_margin_accel_zscore_5d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _zscore_rolling(base, 5)

def maga_078_margin_accel_rank_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_078_margin_accel_rank_5d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rank_pct(base, 5)

def maga_079_margin_accel_lvl_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_079_margin_accel_lvl_21d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rolling_mean(base, 21)

def maga_080_margin_accel_zscore_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_080_margin_accel_zscore_21d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _zscore_rolling(base, 21)

def maga_081_margin_accel_rank_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_081_margin_accel_rank_21d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rank_pct(base, 21)

def maga_082_margin_accel_lvl_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_082_margin_accel_lvl_63d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rolling_mean(base, 63)

def maga_083_margin_accel_zscore_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_083_margin_accel_zscore_63d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _zscore_rolling(base, 63)

def maga_084_margin_accel_rank_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_084_margin_accel_rank_63d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rank_pct(base, 63)

def maga_085_margin_accel_lvl_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_085_margin_accel_lvl_126d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rolling_mean(base, 126)

def maga_086_margin_accel_zscore_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_086_margin_accel_zscore_126d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _zscore_rolling(base, 126)

def maga_087_margin_accel_rank_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_087_margin_accel_rank_126d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rank_pct(base, 126)

def maga_088_margin_accel_lvl_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_088_margin_accel_lvl_252d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rolling_mean(base, 252)

def maga_089_margin_accel_zscore_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_089_margin_accel_zscore_252d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _zscore_rolling(base, 252)

def maga_090_margin_accel_rank_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_090_margin_accel_rank_252d"""
    base = _safe_div(netinc, revenue).diff(252).diff(63)
    return _rank_pct(base, 252)

def maga_091_op_margin_accel_lvl_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_091_op_margin_accel_lvl_5d"""
    base = _safe_div(opinc, revenue).diff(252).diff(63)
    return _rolling_mean(base, 5)

def maga_092_op_margin_accel_zscore_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_092_op_margin_accel_zscore_5d"""
    base = _safe_div(opinc, revenue).diff(252).diff(63)
    return _zscore_rolling(base, 5)

def maga_093_op_margin_accel_rank_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_093_op_margin_accel_rank_5d"""
    base = _safe_div(opinc, revenue).diff(252).diff(63)
    return _rank_pct(base, 5)

def maga_094_op_margin_accel_lvl_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_094_op_margin_accel_lvl_21d"""
    base = _safe_div(opinc, revenue).diff(252).diff(63)
    return _rolling_mean(base, 21)

def maga_095_op_margin_accel_zscore_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_095_op_margin_accel_zscore_21d"""
    base = _safe_div(opinc, revenue).diff(252).diff(63)
    return _zscore_rolling(base, 21)

def maga_096_op_margin_accel_rank_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_096_op_margin_accel_rank_21d"""
    base = _safe_div(opinc, revenue).diff(252).diff(63)
    return _rank_pct(base, 21)

def maga_097_op_margin_accel_lvl_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_097_op_margin_accel_lvl_63d"""
    base = _safe_div(opinc, revenue).diff(252).diff(63)
    return _rolling_mean(base, 63)

def maga_098_op_margin_accel_zscore_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_098_op_margin_accel_zscore_63d"""
    base = _safe_div(opinc, revenue).diff(252).diff(63)
    return _zscore_rolling(base, 63)

def maga_099_op_margin_accel_rank_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_099_op_margin_accel_rank_63d"""
    base = _safe_div(opinc, revenue).diff(252).diff(63)
    return _rank_pct(base, 63)

def maga_100_op_margin_accel_lvl_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_100_op_margin_accel_lvl_126d"""
    base = _safe_div(opinc, revenue).diff(252).diff(63)
    return _rolling_mean(base, 126)

def maga_101_op_margin_accel_zscore_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_101_op_margin_accel_zscore_126d"""
    base = _safe_div(opinc, revenue).diff(252).diff(63)
    return _zscore_rolling(base, 126)

def maga_102_op_margin_accel_rank_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_102_op_margin_accel_rank_126d"""
    base = _safe_div(opinc, revenue).diff(252).diff(63)
    return _rank_pct(base, 126)

def maga_103_op_margin_accel_lvl_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_103_op_margin_accel_lvl_252d"""
    base = _safe_div(opinc, revenue).diff(252).diff(63)
    return _rolling_mean(base, 252)

def maga_104_op_margin_accel_zscore_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_104_op_margin_accel_zscore_252d"""
    base = _safe_div(opinc, revenue).diff(252).diff(63)
    return _zscore_rolling(base, 252)

def maga_105_op_margin_accel_rank_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_105_op_margin_accel_rank_252d"""
    base = _safe_div(opinc, revenue).diff(252).diff(63)
    return _rank_pct(base, 252)

def maga_106_margin_z_lvl_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_106_margin_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(netinc, revenue), 252)
    return _rolling_mean(base, 5)

def maga_107_margin_z_zscore_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_107_margin_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(netinc, revenue), 252)
    return _zscore_rolling(base, 5)

def maga_108_margin_z_rank_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_108_margin_z_rank_5d"""
    base = _zscore_rolling(_safe_div(netinc, revenue), 252)
    return _rank_pct(base, 5)

def maga_109_margin_z_lvl_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_109_margin_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(netinc, revenue), 252)
    return _rolling_mean(base, 21)

def maga_110_margin_z_zscore_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_110_margin_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(netinc, revenue), 252)
    return _zscore_rolling(base, 21)

def maga_111_margin_z_rank_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_111_margin_z_rank_21d"""
    base = _zscore_rolling(_safe_div(netinc, revenue), 252)
    return _rank_pct(base, 21)

def maga_112_margin_z_lvl_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_112_margin_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(netinc, revenue), 252)
    return _rolling_mean(base, 63)

def maga_113_margin_z_zscore_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_113_margin_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(netinc, revenue), 252)
    return _zscore_rolling(base, 63)

def maga_114_margin_z_rank_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_114_margin_z_rank_63d"""
    base = _zscore_rolling(_safe_div(netinc, revenue), 252)
    return _rank_pct(base, 63)

def maga_115_margin_z_lvl_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_115_margin_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(netinc, revenue), 252)
    return _rolling_mean(base, 126)

def maga_116_margin_z_zscore_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_116_margin_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(netinc, revenue), 252)
    return _zscore_rolling(base, 126)

def maga_117_margin_z_rank_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_117_margin_z_rank_126d"""
    base = _zscore_rolling(_safe_div(netinc, revenue), 252)
    return _rank_pct(base, 126)

def maga_118_margin_z_lvl_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_118_margin_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(netinc, revenue), 252)
    return _rolling_mean(base, 252)

def maga_119_margin_z_zscore_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_119_margin_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(netinc, revenue), 252)
    return _zscore_rolling(base, 252)

def maga_120_margin_z_rank_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_120_margin_z_rank_252d"""
    base = _zscore_rolling(_safe_div(netinc, revenue), 252)
    return _rank_pct(base, 252)

def maga_121_margin_rank_lvl_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_121_margin_rank_lvl_5d"""
    base = _rank_pct(_safe_div(netinc, revenue), 252)
    return _rolling_mean(base, 5)

def maga_122_margin_rank_zscore_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_122_margin_rank_zscore_5d"""
    base = _rank_pct(_safe_div(netinc, revenue), 252)
    return _zscore_rolling(base, 5)

def maga_123_margin_rank_rank_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_123_margin_rank_rank_5d"""
    base = _rank_pct(_safe_div(netinc, revenue), 252)
    return _rank_pct(base, 5)

def maga_124_margin_rank_lvl_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_124_margin_rank_lvl_21d"""
    base = _rank_pct(_safe_div(netinc, revenue), 252)
    return _rolling_mean(base, 21)

def maga_125_margin_rank_zscore_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_125_margin_rank_zscore_21d"""
    base = _rank_pct(_safe_div(netinc, revenue), 252)
    return _zscore_rolling(base, 21)

def maga_126_margin_rank_rank_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_126_margin_rank_rank_21d"""
    base = _rank_pct(_safe_div(netinc, revenue), 252)
    return _rank_pct(base, 21)

def maga_127_margin_rank_lvl_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_127_margin_rank_lvl_63d"""
    base = _rank_pct(_safe_div(netinc, revenue), 252)
    return _rolling_mean(base, 63)

def maga_128_margin_rank_zscore_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_128_margin_rank_zscore_63d"""
    base = _rank_pct(_safe_div(netinc, revenue), 252)
    return _zscore_rolling(base, 63)

def maga_129_margin_rank_rank_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_129_margin_rank_rank_63d"""
    base = _rank_pct(_safe_div(netinc, revenue), 252)
    return _rank_pct(base, 63)

def maga_130_margin_rank_lvl_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_130_margin_rank_lvl_126d"""
    base = _rank_pct(_safe_div(netinc, revenue), 252)
    return _rolling_mean(base, 126)

def maga_131_margin_rank_zscore_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_131_margin_rank_zscore_126d"""
    base = _rank_pct(_safe_div(netinc, revenue), 252)
    return _zscore_rolling(base, 126)

def maga_132_margin_rank_rank_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_132_margin_rank_rank_126d"""
    base = _rank_pct(_safe_div(netinc, revenue), 252)
    return _rank_pct(base, 126)

def maga_133_margin_rank_lvl_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_133_margin_rank_lvl_252d"""
    base = _rank_pct(_safe_div(netinc, revenue), 252)
    return _rolling_mean(base, 252)

def maga_134_margin_rank_zscore_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_134_margin_rank_zscore_252d"""
    base = _rank_pct(_safe_div(netinc, revenue), 252)
    return _zscore_rolling(base, 252)

def maga_135_margin_rank_rank_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_135_margin_rank_rank_252d"""
    base = _rank_pct(_safe_div(netinc, revenue), 252)
    return _rank_pct(base, 252)

def maga_136_margin_vol_lvl_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_136_margin_vol_lvl_5d"""
    base = _rolling_std(_safe_div(netinc, revenue), 63)
    return _rolling_mean(base, 5)

def maga_137_margin_vol_zscore_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_137_margin_vol_zscore_5d"""
    base = _rolling_std(_safe_div(netinc, revenue), 63)
    return _zscore_rolling(base, 5)

def maga_138_margin_vol_rank_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_138_margin_vol_rank_5d"""
    base = _rolling_std(_safe_div(netinc, revenue), 63)
    return _rank_pct(base, 5)

def maga_139_margin_vol_lvl_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_139_margin_vol_lvl_21d"""
    base = _rolling_std(_safe_div(netinc, revenue), 63)
    return _rolling_mean(base, 21)

def maga_140_margin_vol_zscore_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_140_margin_vol_zscore_21d"""
    base = _rolling_std(_safe_div(netinc, revenue), 63)
    return _zscore_rolling(base, 21)

def maga_141_margin_vol_rank_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_141_margin_vol_rank_21d"""
    base = _rolling_std(_safe_div(netinc, revenue), 63)
    return _rank_pct(base, 21)

def maga_142_margin_vol_lvl_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_142_margin_vol_lvl_63d"""
    base = _rolling_std(_safe_div(netinc, revenue), 63)
    return _rolling_mean(base, 63)

def maga_143_margin_vol_zscore_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_143_margin_vol_zscore_63d"""
    base = _rolling_std(_safe_div(netinc, revenue), 63)
    return _zscore_rolling(base, 63)

def maga_144_margin_vol_rank_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_144_margin_vol_rank_63d"""
    base = _rolling_std(_safe_div(netinc, revenue), 63)
    return _rank_pct(base, 63)

def maga_145_margin_vol_lvl_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_145_margin_vol_lvl_126d"""
    base = _rolling_std(_safe_div(netinc, revenue), 63)
    return _rolling_mean(base, 126)

def maga_146_margin_vol_zscore_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_146_margin_vol_zscore_126d"""
    base = _rolling_std(_safe_div(netinc, revenue), 63)
    return _zscore_rolling(base, 126)

def maga_147_margin_vol_rank_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_147_margin_vol_rank_126d"""
    base = _rolling_std(_safe_div(netinc, revenue), 63)
    return _rank_pct(base, 126)

def maga_148_margin_vol_lvl_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_148_margin_vol_lvl_252d"""
    base = _rolling_std(_safe_div(netinc, revenue), 63)
    return _rolling_mean(base, 252)

def maga_149_margin_vol_zscore_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_149_margin_vol_zscore_252d"""
    base = _rolling_std(_safe_div(netinc, revenue), 63)
    return _zscore_rolling(base, 252)

def maga_150_margin_vol_rank_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_150_margin_vol_rank_252d"""
    base = _rolling_std(_safe_div(netinc, revenue), 63)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V54_REGISTRY_2 = {
    "maga_076_margin_accel_lvl_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_076_margin_accel_lvl_5d},
    "maga_077_margin_accel_zscore_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_077_margin_accel_zscore_5d},
    "maga_078_margin_accel_rank_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_078_margin_accel_rank_5d},
    "maga_079_margin_accel_lvl_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_079_margin_accel_lvl_21d},
    "maga_080_margin_accel_zscore_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_080_margin_accel_zscore_21d},
    "maga_081_margin_accel_rank_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_081_margin_accel_rank_21d},
    "maga_082_margin_accel_lvl_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_082_margin_accel_lvl_63d},
    "maga_083_margin_accel_zscore_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_083_margin_accel_zscore_63d},
    "maga_084_margin_accel_rank_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_084_margin_accel_rank_63d},
    "maga_085_margin_accel_lvl_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_085_margin_accel_lvl_126d},
    "maga_086_margin_accel_zscore_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_086_margin_accel_zscore_126d},
    "maga_087_margin_accel_rank_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_087_margin_accel_rank_126d},
    "maga_088_margin_accel_lvl_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_088_margin_accel_lvl_252d},
    "maga_089_margin_accel_zscore_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_089_margin_accel_zscore_252d},
    "maga_090_margin_accel_rank_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_090_margin_accel_rank_252d},
    "maga_091_op_margin_accel_lvl_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_091_op_margin_accel_lvl_5d},
    "maga_092_op_margin_accel_zscore_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_092_op_margin_accel_zscore_5d},
    "maga_093_op_margin_accel_rank_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_093_op_margin_accel_rank_5d},
    "maga_094_op_margin_accel_lvl_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_094_op_margin_accel_lvl_21d},
    "maga_095_op_margin_accel_zscore_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_095_op_margin_accel_zscore_21d},
    "maga_096_op_margin_accel_rank_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_096_op_margin_accel_rank_21d},
    "maga_097_op_margin_accel_lvl_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_097_op_margin_accel_lvl_63d},
    "maga_098_op_margin_accel_zscore_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_098_op_margin_accel_zscore_63d},
    "maga_099_op_margin_accel_rank_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_099_op_margin_accel_rank_63d},
    "maga_100_op_margin_accel_lvl_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_100_op_margin_accel_lvl_126d},
    "maga_101_op_margin_accel_zscore_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_101_op_margin_accel_zscore_126d},
    "maga_102_op_margin_accel_rank_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_102_op_margin_accel_rank_126d},
    "maga_103_op_margin_accel_lvl_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_103_op_margin_accel_lvl_252d},
    "maga_104_op_margin_accel_zscore_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_104_op_margin_accel_zscore_252d},
    "maga_105_op_margin_accel_rank_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_105_op_margin_accel_rank_252d},
    "maga_106_margin_z_lvl_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_106_margin_z_lvl_5d},
    "maga_107_margin_z_zscore_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_107_margin_z_zscore_5d},
    "maga_108_margin_z_rank_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_108_margin_z_rank_5d},
    "maga_109_margin_z_lvl_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_109_margin_z_lvl_21d},
    "maga_110_margin_z_zscore_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_110_margin_z_zscore_21d},
    "maga_111_margin_z_rank_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_111_margin_z_rank_21d},
    "maga_112_margin_z_lvl_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_112_margin_z_lvl_63d},
    "maga_113_margin_z_zscore_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_113_margin_z_zscore_63d},
    "maga_114_margin_z_rank_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_114_margin_z_rank_63d},
    "maga_115_margin_z_lvl_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_115_margin_z_lvl_126d},
    "maga_116_margin_z_zscore_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_116_margin_z_zscore_126d},
    "maga_117_margin_z_rank_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_117_margin_z_rank_126d},
    "maga_118_margin_z_lvl_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_118_margin_z_lvl_252d},
    "maga_119_margin_z_zscore_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_119_margin_z_zscore_252d},
    "maga_120_margin_z_rank_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_120_margin_z_rank_252d},
    "maga_121_margin_rank_lvl_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_121_margin_rank_lvl_5d},
    "maga_122_margin_rank_zscore_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_122_margin_rank_zscore_5d},
    "maga_123_margin_rank_rank_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_123_margin_rank_rank_5d},
    "maga_124_margin_rank_lvl_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_124_margin_rank_lvl_21d},
    "maga_125_margin_rank_zscore_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_125_margin_rank_zscore_21d},
    "maga_126_margin_rank_rank_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_126_margin_rank_rank_21d},
    "maga_127_margin_rank_lvl_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_127_margin_rank_lvl_63d},
    "maga_128_margin_rank_zscore_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_128_margin_rank_zscore_63d},
    "maga_129_margin_rank_rank_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_129_margin_rank_rank_63d},
    "maga_130_margin_rank_lvl_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_130_margin_rank_lvl_126d},
    "maga_131_margin_rank_zscore_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_131_margin_rank_zscore_126d},
    "maga_132_margin_rank_rank_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_132_margin_rank_rank_126d},
    "maga_133_margin_rank_lvl_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_133_margin_rank_lvl_252d},
    "maga_134_margin_rank_zscore_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_134_margin_rank_zscore_252d},
    "maga_135_margin_rank_rank_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_135_margin_rank_rank_252d},
    "maga_136_margin_vol_lvl_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_136_margin_vol_lvl_5d},
    "maga_137_margin_vol_zscore_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_137_margin_vol_zscore_5d},
    "maga_138_margin_vol_rank_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_138_margin_vol_rank_5d},
    "maga_139_margin_vol_lvl_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_139_margin_vol_lvl_21d},
    "maga_140_margin_vol_zscore_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_140_margin_vol_zscore_21d},
    "maga_141_margin_vol_rank_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_141_margin_vol_rank_21d},
    "maga_142_margin_vol_lvl_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_142_margin_vol_lvl_63d},
    "maga_143_margin_vol_zscore_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_143_margin_vol_zscore_63d},
    "maga_144_margin_vol_rank_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_144_margin_vol_rank_63d},
    "maga_145_margin_vol_lvl_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_145_margin_vol_lvl_126d},
    "maga_146_margin_vol_zscore_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_146_margin_vol_zscore_126d},
    "maga_147_margin_vol_rank_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_147_margin_vol_rank_126d},
    "maga_148_margin_vol_lvl_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_148_margin_vol_lvl_252d},
    "maga_149_margin_vol_zscore_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_149_margin_vol_zscore_252d},
    "maga_150_margin_vol_rank_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_150_margin_vol_rank_252d},
}
