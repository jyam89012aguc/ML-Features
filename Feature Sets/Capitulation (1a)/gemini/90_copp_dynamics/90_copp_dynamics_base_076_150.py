"""
90_copp_dynamics — Base Features 076-150
Domain: copp_dynamics
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

def copp_076_copp_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_076_copp_z_lvl_5d"""
    base = _zscore_rolling(close.pct_change(14) + close.pct_change(11), 21)
    return _rolling_mean(base, 5)

def copp_077_copp_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_077_copp_z_zscore_5d"""
    base = _zscore_rolling(close.pct_change(14) + close.pct_change(11), 21)
    return _zscore_rolling(base, 5)

def copp_078_copp_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_078_copp_z_rank_5d"""
    base = _zscore_rolling(close.pct_change(14) + close.pct_change(11), 21)
    return _rank_pct(base, 5)

def copp_079_copp_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_079_copp_z_lvl_21d"""
    base = _zscore_rolling(close.pct_change(14) + close.pct_change(11), 21)
    return _rolling_mean(base, 21)

def copp_080_copp_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_080_copp_z_zscore_21d"""
    base = _zscore_rolling(close.pct_change(14) + close.pct_change(11), 21)
    return _zscore_rolling(base, 21)

def copp_081_copp_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_081_copp_z_rank_21d"""
    base = _zscore_rolling(close.pct_change(14) + close.pct_change(11), 21)
    return _rank_pct(base, 21)

def copp_082_copp_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_082_copp_z_lvl_63d"""
    base = _zscore_rolling(close.pct_change(14) + close.pct_change(11), 21)
    return _rolling_mean(base, 63)

def copp_083_copp_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_083_copp_z_zscore_63d"""
    base = _zscore_rolling(close.pct_change(14) + close.pct_change(11), 21)
    return _zscore_rolling(base, 63)

def copp_084_copp_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_084_copp_z_rank_63d"""
    base = _zscore_rolling(close.pct_change(14) + close.pct_change(11), 21)
    return _rank_pct(base, 63)

def copp_085_copp_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_085_copp_z_lvl_126d"""
    base = _zscore_rolling(close.pct_change(14) + close.pct_change(11), 21)
    return _rolling_mean(base, 126)

def copp_086_copp_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_086_copp_z_zscore_126d"""
    base = _zscore_rolling(close.pct_change(14) + close.pct_change(11), 21)
    return _zscore_rolling(base, 126)

def copp_087_copp_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_087_copp_z_rank_126d"""
    base = _zscore_rolling(close.pct_change(14) + close.pct_change(11), 21)
    return _rank_pct(base, 126)

def copp_088_copp_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_088_copp_z_lvl_252d"""
    base = _zscore_rolling(close.pct_change(14) + close.pct_change(11), 21)
    return _rolling_mean(base, 252)

def copp_089_copp_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_089_copp_z_zscore_252d"""
    base = _zscore_rolling(close.pct_change(14) + close.pct_change(11), 21)
    return _zscore_rolling(base, 252)

def copp_090_copp_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_090_copp_z_rank_252d"""
    base = _zscore_rolling(close.pct_change(14) + close.pct_change(11), 21)
    return _rank_pct(base, 252)

def copp_091_copp_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_091_copp_roc_lvl_5d"""
    base = (close.pct_change(14) + close.pct_change(11)).pct_change()
    return _rolling_mean(base, 5)

def copp_092_copp_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_092_copp_roc_zscore_5d"""
    base = (close.pct_change(14) + close.pct_change(11)).pct_change()
    return _zscore_rolling(base, 5)

def copp_093_copp_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_093_copp_roc_rank_5d"""
    base = (close.pct_change(14) + close.pct_change(11)).pct_change()
    return _rank_pct(base, 5)

def copp_094_copp_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_094_copp_roc_lvl_21d"""
    base = (close.pct_change(14) + close.pct_change(11)).pct_change()
    return _rolling_mean(base, 21)

def copp_095_copp_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_095_copp_roc_zscore_21d"""
    base = (close.pct_change(14) + close.pct_change(11)).pct_change()
    return _zscore_rolling(base, 21)

def copp_096_copp_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_096_copp_roc_rank_21d"""
    base = (close.pct_change(14) + close.pct_change(11)).pct_change()
    return _rank_pct(base, 21)

def copp_097_copp_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_097_copp_roc_lvl_63d"""
    base = (close.pct_change(14) + close.pct_change(11)).pct_change()
    return _rolling_mean(base, 63)

def copp_098_copp_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_098_copp_roc_zscore_63d"""
    base = (close.pct_change(14) + close.pct_change(11)).pct_change()
    return _zscore_rolling(base, 63)

def copp_099_copp_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_099_copp_roc_rank_63d"""
    base = (close.pct_change(14) + close.pct_change(11)).pct_change()
    return _rank_pct(base, 63)

def copp_100_copp_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_100_copp_roc_lvl_126d"""
    base = (close.pct_change(14) + close.pct_change(11)).pct_change()
    return _rolling_mean(base, 126)

def copp_101_copp_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_101_copp_roc_zscore_126d"""
    base = (close.pct_change(14) + close.pct_change(11)).pct_change()
    return _zscore_rolling(base, 126)

def copp_102_copp_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_102_copp_roc_rank_126d"""
    base = (close.pct_change(14) + close.pct_change(11)).pct_change()
    return _rank_pct(base, 126)

def copp_103_copp_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_103_copp_roc_lvl_252d"""
    base = (close.pct_change(14) + close.pct_change(11)).pct_change()
    return _rolling_mean(base, 252)

def copp_104_copp_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_104_copp_roc_zscore_252d"""
    base = (close.pct_change(14) + close.pct_change(11)).pct_change()
    return _zscore_rolling(base, 252)

def copp_105_copp_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_105_copp_roc_rank_252d"""
    base = (close.pct_change(14) + close.pct_change(11)).pct_change()
    return _rank_pct(base, 252)

def copp_106_copp_abs_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_106_copp_abs_lvl_5d"""
    base = (close.pct_change(14) + close.pct_change(11)).abs()
    return _rolling_mean(base, 5)

def copp_107_copp_abs_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_107_copp_abs_zscore_5d"""
    base = (close.pct_change(14) + close.pct_change(11)).abs()
    return _zscore_rolling(base, 5)

def copp_108_copp_abs_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_108_copp_abs_rank_5d"""
    base = (close.pct_change(14) + close.pct_change(11)).abs()
    return _rank_pct(base, 5)

def copp_109_copp_abs_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_109_copp_abs_lvl_21d"""
    base = (close.pct_change(14) + close.pct_change(11)).abs()
    return _rolling_mean(base, 21)

def copp_110_copp_abs_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_110_copp_abs_zscore_21d"""
    base = (close.pct_change(14) + close.pct_change(11)).abs()
    return _zscore_rolling(base, 21)

def copp_111_copp_abs_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_111_copp_abs_rank_21d"""
    base = (close.pct_change(14) + close.pct_change(11)).abs()
    return _rank_pct(base, 21)

def copp_112_copp_abs_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_112_copp_abs_lvl_63d"""
    base = (close.pct_change(14) + close.pct_change(11)).abs()
    return _rolling_mean(base, 63)

def copp_113_copp_abs_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_113_copp_abs_zscore_63d"""
    base = (close.pct_change(14) + close.pct_change(11)).abs()
    return _zscore_rolling(base, 63)

def copp_114_copp_abs_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_114_copp_abs_rank_63d"""
    base = (close.pct_change(14) + close.pct_change(11)).abs()
    return _rank_pct(base, 63)

def copp_115_copp_abs_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_115_copp_abs_lvl_126d"""
    base = (close.pct_change(14) + close.pct_change(11)).abs()
    return _rolling_mean(base, 126)

def copp_116_copp_abs_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_116_copp_abs_zscore_126d"""
    base = (close.pct_change(14) + close.pct_change(11)).abs()
    return _zscore_rolling(base, 126)

def copp_117_copp_abs_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_117_copp_abs_rank_126d"""
    base = (close.pct_change(14) + close.pct_change(11)).abs()
    return _rank_pct(base, 126)

def copp_118_copp_abs_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_118_copp_abs_lvl_252d"""
    base = (close.pct_change(14) + close.pct_change(11)).abs()
    return _rolling_mean(base, 252)

def copp_119_copp_abs_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_119_copp_abs_zscore_252d"""
    base = (close.pct_change(14) + close.pct_change(11)).abs()
    return _zscore_rolling(base, 252)

def copp_120_copp_abs_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_120_copp_abs_rank_252d"""
    base = (close.pct_change(14) + close.pct_change(11)).abs()
    return _rank_pct(base, 252)

def copp_121_copp_sig_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_121_copp_sig_lvl_5d"""
    base = _rolling_mean(close.pct_change(14) + close.pct_change(11), 5)
    return _rolling_mean(base, 5)

def copp_122_copp_sig_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_122_copp_sig_zscore_5d"""
    base = _rolling_mean(close.pct_change(14) + close.pct_change(11), 5)
    return _zscore_rolling(base, 5)

def copp_123_copp_sig_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_123_copp_sig_rank_5d"""
    base = _rolling_mean(close.pct_change(14) + close.pct_change(11), 5)
    return _rank_pct(base, 5)

def copp_124_copp_sig_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_124_copp_sig_lvl_21d"""
    base = _rolling_mean(close.pct_change(14) + close.pct_change(11), 5)
    return _rolling_mean(base, 21)

def copp_125_copp_sig_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_125_copp_sig_zscore_21d"""
    base = _rolling_mean(close.pct_change(14) + close.pct_change(11), 5)
    return _zscore_rolling(base, 21)

def copp_126_copp_sig_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_126_copp_sig_rank_21d"""
    base = _rolling_mean(close.pct_change(14) + close.pct_change(11), 5)
    return _rank_pct(base, 21)

def copp_127_copp_sig_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_127_copp_sig_lvl_63d"""
    base = _rolling_mean(close.pct_change(14) + close.pct_change(11), 5)
    return _rolling_mean(base, 63)

def copp_128_copp_sig_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_128_copp_sig_zscore_63d"""
    base = _rolling_mean(close.pct_change(14) + close.pct_change(11), 5)
    return _zscore_rolling(base, 63)

def copp_129_copp_sig_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_129_copp_sig_rank_63d"""
    base = _rolling_mean(close.pct_change(14) + close.pct_change(11), 5)
    return _rank_pct(base, 63)

def copp_130_copp_sig_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_130_copp_sig_lvl_126d"""
    base = _rolling_mean(close.pct_change(14) + close.pct_change(11), 5)
    return _rolling_mean(base, 126)

def copp_131_copp_sig_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_131_copp_sig_zscore_126d"""
    base = _rolling_mean(close.pct_change(14) + close.pct_change(11), 5)
    return _zscore_rolling(base, 126)

def copp_132_copp_sig_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_132_copp_sig_rank_126d"""
    base = _rolling_mean(close.pct_change(14) + close.pct_change(11), 5)
    return _rank_pct(base, 126)

def copp_133_copp_sig_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_133_copp_sig_lvl_252d"""
    base = _rolling_mean(close.pct_change(14) + close.pct_change(11), 5)
    return _rolling_mean(base, 252)

def copp_134_copp_sig_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_134_copp_sig_zscore_252d"""
    base = _rolling_mean(close.pct_change(14) + close.pct_change(11), 5)
    return _zscore_rolling(base, 252)

def copp_135_copp_sig_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_135_copp_sig_rank_252d"""
    base = _rolling_mean(close.pct_change(14) + close.pct_change(11), 5)
    return _rank_pct(base, 252)

def copp_136_copp_dist_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_136_copp_dist_lvl_5d"""
    base = (close.pct_change(14) + close.pct_change(11)) - _rolling_mean(close.pct_change(14) + close.pct_change(11), 21)
    return _rolling_mean(base, 5)

def copp_137_copp_dist_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_137_copp_dist_zscore_5d"""
    base = (close.pct_change(14) + close.pct_change(11)) - _rolling_mean(close.pct_change(14) + close.pct_change(11), 21)
    return _zscore_rolling(base, 5)

def copp_138_copp_dist_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_138_copp_dist_rank_5d"""
    base = (close.pct_change(14) + close.pct_change(11)) - _rolling_mean(close.pct_change(14) + close.pct_change(11), 21)
    return _rank_pct(base, 5)

def copp_139_copp_dist_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_139_copp_dist_lvl_21d"""
    base = (close.pct_change(14) + close.pct_change(11)) - _rolling_mean(close.pct_change(14) + close.pct_change(11), 21)
    return _rolling_mean(base, 21)

def copp_140_copp_dist_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_140_copp_dist_zscore_21d"""
    base = (close.pct_change(14) + close.pct_change(11)) - _rolling_mean(close.pct_change(14) + close.pct_change(11), 21)
    return _zscore_rolling(base, 21)

def copp_141_copp_dist_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_141_copp_dist_rank_21d"""
    base = (close.pct_change(14) + close.pct_change(11)) - _rolling_mean(close.pct_change(14) + close.pct_change(11), 21)
    return _rank_pct(base, 21)

def copp_142_copp_dist_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_142_copp_dist_lvl_63d"""
    base = (close.pct_change(14) + close.pct_change(11)) - _rolling_mean(close.pct_change(14) + close.pct_change(11), 21)
    return _rolling_mean(base, 63)

def copp_143_copp_dist_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_143_copp_dist_zscore_63d"""
    base = (close.pct_change(14) + close.pct_change(11)) - _rolling_mean(close.pct_change(14) + close.pct_change(11), 21)
    return _zscore_rolling(base, 63)

def copp_144_copp_dist_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_144_copp_dist_rank_63d"""
    base = (close.pct_change(14) + close.pct_change(11)) - _rolling_mean(close.pct_change(14) + close.pct_change(11), 21)
    return _rank_pct(base, 63)

def copp_145_copp_dist_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_145_copp_dist_lvl_126d"""
    base = (close.pct_change(14) + close.pct_change(11)) - _rolling_mean(close.pct_change(14) + close.pct_change(11), 21)
    return _rolling_mean(base, 126)

def copp_146_copp_dist_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_146_copp_dist_zscore_126d"""
    base = (close.pct_change(14) + close.pct_change(11)) - _rolling_mean(close.pct_change(14) + close.pct_change(11), 21)
    return _zscore_rolling(base, 126)

def copp_147_copp_dist_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_147_copp_dist_rank_126d"""
    base = (close.pct_change(14) + close.pct_change(11)) - _rolling_mean(close.pct_change(14) + close.pct_change(11), 21)
    return _rank_pct(base, 126)

def copp_148_copp_dist_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_148_copp_dist_lvl_252d"""
    base = (close.pct_change(14) + close.pct_change(11)) - _rolling_mean(close.pct_change(14) + close.pct_change(11), 21)
    return _rolling_mean(base, 252)

def copp_149_copp_dist_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_149_copp_dist_zscore_252d"""
    base = (close.pct_change(14) + close.pct_change(11)) - _rolling_mean(close.pct_change(14) + close.pct_change(11), 21)
    return _zscore_rolling(base, 252)

def copp_150_copp_dist_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_150_copp_dist_rank_252d"""
    base = (close.pct_change(14) + close.pct_change(11)) - _rolling_mean(close.pct_change(14) + close.pct_change(11), 21)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V90_REGISTRY_2 = {
    "copp_076_copp_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_076_copp_z_lvl_5d},
    "copp_077_copp_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_077_copp_z_zscore_5d},
    "copp_078_copp_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_078_copp_z_rank_5d},
    "copp_079_copp_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_079_copp_z_lvl_21d},
    "copp_080_copp_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_080_copp_z_zscore_21d},
    "copp_081_copp_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_081_copp_z_rank_21d},
    "copp_082_copp_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_082_copp_z_lvl_63d},
    "copp_083_copp_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_083_copp_z_zscore_63d},
    "copp_084_copp_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_084_copp_z_rank_63d},
    "copp_085_copp_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_085_copp_z_lvl_126d},
    "copp_086_copp_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_086_copp_z_zscore_126d},
    "copp_087_copp_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_087_copp_z_rank_126d},
    "copp_088_copp_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_088_copp_z_lvl_252d},
    "copp_089_copp_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_089_copp_z_zscore_252d},
    "copp_090_copp_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_090_copp_z_rank_252d},
    "copp_091_copp_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_091_copp_roc_lvl_5d},
    "copp_092_copp_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_092_copp_roc_zscore_5d},
    "copp_093_copp_roc_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_093_copp_roc_rank_5d},
    "copp_094_copp_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_094_copp_roc_lvl_21d},
    "copp_095_copp_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_095_copp_roc_zscore_21d},
    "copp_096_copp_roc_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_096_copp_roc_rank_21d},
    "copp_097_copp_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_097_copp_roc_lvl_63d},
    "copp_098_copp_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_098_copp_roc_zscore_63d},
    "copp_099_copp_roc_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_099_copp_roc_rank_63d},
    "copp_100_copp_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_100_copp_roc_lvl_126d},
    "copp_101_copp_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_101_copp_roc_zscore_126d},
    "copp_102_copp_roc_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_102_copp_roc_rank_126d},
    "copp_103_copp_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_103_copp_roc_lvl_252d},
    "copp_104_copp_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_104_copp_roc_zscore_252d},
    "copp_105_copp_roc_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_105_copp_roc_rank_252d},
    "copp_106_copp_abs_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_106_copp_abs_lvl_5d},
    "copp_107_copp_abs_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_107_copp_abs_zscore_5d},
    "copp_108_copp_abs_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_108_copp_abs_rank_5d},
    "copp_109_copp_abs_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_109_copp_abs_lvl_21d},
    "copp_110_copp_abs_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_110_copp_abs_zscore_21d},
    "copp_111_copp_abs_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_111_copp_abs_rank_21d},
    "copp_112_copp_abs_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_112_copp_abs_lvl_63d},
    "copp_113_copp_abs_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_113_copp_abs_zscore_63d},
    "copp_114_copp_abs_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_114_copp_abs_rank_63d},
    "copp_115_copp_abs_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_115_copp_abs_lvl_126d},
    "copp_116_copp_abs_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_116_copp_abs_zscore_126d},
    "copp_117_copp_abs_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_117_copp_abs_rank_126d},
    "copp_118_copp_abs_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_118_copp_abs_lvl_252d},
    "copp_119_copp_abs_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_119_copp_abs_zscore_252d},
    "copp_120_copp_abs_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_120_copp_abs_rank_252d},
    "copp_121_copp_sig_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_121_copp_sig_lvl_5d},
    "copp_122_copp_sig_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_122_copp_sig_zscore_5d},
    "copp_123_copp_sig_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_123_copp_sig_rank_5d},
    "copp_124_copp_sig_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_124_copp_sig_lvl_21d},
    "copp_125_copp_sig_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_125_copp_sig_zscore_21d},
    "copp_126_copp_sig_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_126_copp_sig_rank_21d},
    "copp_127_copp_sig_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_127_copp_sig_lvl_63d},
    "copp_128_copp_sig_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_128_copp_sig_zscore_63d},
    "copp_129_copp_sig_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_129_copp_sig_rank_63d},
    "copp_130_copp_sig_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_130_copp_sig_lvl_126d},
    "copp_131_copp_sig_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_131_copp_sig_zscore_126d},
    "copp_132_copp_sig_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_132_copp_sig_rank_126d},
    "copp_133_copp_sig_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_133_copp_sig_lvl_252d},
    "copp_134_copp_sig_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_134_copp_sig_zscore_252d},
    "copp_135_copp_sig_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_135_copp_sig_rank_252d},
    "copp_136_copp_dist_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_136_copp_dist_lvl_5d},
    "copp_137_copp_dist_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_137_copp_dist_zscore_5d},
    "copp_138_copp_dist_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_138_copp_dist_rank_5d},
    "copp_139_copp_dist_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_139_copp_dist_lvl_21d},
    "copp_140_copp_dist_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_140_copp_dist_zscore_21d},
    "copp_141_copp_dist_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_141_copp_dist_rank_21d},
    "copp_142_copp_dist_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_142_copp_dist_lvl_63d},
    "copp_143_copp_dist_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_143_copp_dist_zscore_63d},
    "copp_144_copp_dist_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_144_copp_dist_rank_63d},
    "copp_145_copp_dist_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_145_copp_dist_lvl_126d},
    "copp_146_copp_dist_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_146_copp_dist_zscore_126d},
    "copp_147_copp_dist_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_147_copp_dist_rank_126d},
    "copp_148_copp_dist_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_148_copp_dist_lvl_252d},
    "copp_149_copp_dist_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_149_copp_dist_zscore_252d},
    "copp_150_copp_dist_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_150_copp_dist_rank_252d},
}
