"""
100_trgc_composite — Base Features 076-150
Domain: trgc_composite
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

def trgc_076_comp_mom_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_076_comp_mom_z_lvl_5d"""
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rolling_mean(base, 5)

def trgc_077_comp_mom_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_077_comp_mom_z_zscore_5d"""
    base = _zscore_rolling(close.pct_change(21), 252)
    return _zscore_rolling(base, 5)

def trgc_078_comp_mom_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_078_comp_mom_z_rank_5d"""
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rank_pct(base, 5)

def trgc_079_comp_mom_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_079_comp_mom_z_lvl_21d"""
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rolling_mean(base, 21)

def trgc_080_comp_mom_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_080_comp_mom_z_zscore_21d"""
    base = _zscore_rolling(close.pct_change(21), 252)
    return _zscore_rolling(base, 21)

def trgc_081_comp_mom_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_081_comp_mom_z_rank_21d"""
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rank_pct(base, 21)

def trgc_082_comp_mom_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_082_comp_mom_z_lvl_63d"""
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rolling_mean(base, 63)

def trgc_083_comp_mom_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_083_comp_mom_z_zscore_63d"""
    base = _zscore_rolling(close.pct_change(21), 252)
    return _zscore_rolling(base, 63)

def trgc_084_comp_mom_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_084_comp_mom_z_rank_63d"""
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rank_pct(base, 63)

def trgc_085_comp_mom_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_085_comp_mom_z_lvl_126d"""
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rolling_mean(base, 126)

def trgc_086_comp_mom_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_086_comp_mom_z_zscore_126d"""
    base = _zscore_rolling(close.pct_change(21), 252)
    return _zscore_rolling(base, 126)

def trgc_087_comp_mom_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_087_comp_mom_z_rank_126d"""
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rank_pct(base, 126)

def trgc_088_comp_mom_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_088_comp_mom_z_lvl_252d"""
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rolling_mean(base, 252)

def trgc_089_comp_mom_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_089_comp_mom_z_zscore_252d"""
    base = _zscore_rolling(close.pct_change(21), 252)
    return _zscore_rolling(base, 252)

def trgc_090_comp_mom_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_090_comp_mom_z_rank_252d"""
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rank_pct(base, 252)

def trgc_091_comp_vol_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_091_comp_vol_z_lvl_5d"""
    base = _zscore_rolling(_rolling_std(close.pct_change(), 21), 252)
    return _rolling_mean(base, 5)

def trgc_092_comp_vol_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_092_comp_vol_z_zscore_5d"""
    base = _zscore_rolling(_rolling_std(close.pct_change(), 21), 252)
    return _zscore_rolling(base, 5)

def trgc_093_comp_vol_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_093_comp_vol_z_rank_5d"""
    base = _zscore_rolling(_rolling_std(close.pct_change(), 21), 252)
    return _rank_pct(base, 5)

def trgc_094_comp_vol_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_094_comp_vol_z_lvl_21d"""
    base = _zscore_rolling(_rolling_std(close.pct_change(), 21), 252)
    return _rolling_mean(base, 21)

def trgc_095_comp_vol_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_095_comp_vol_z_zscore_21d"""
    base = _zscore_rolling(_rolling_std(close.pct_change(), 21), 252)
    return _zscore_rolling(base, 21)

def trgc_096_comp_vol_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_096_comp_vol_z_rank_21d"""
    base = _zscore_rolling(_rolling_std(close.pct_change(), 21), 252)
    return _rank_pct(base, 21)

def trgc_097_comp_vol_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_097_comp_vol_z_lvl_63d"""
    base = _zscore_rolling(_rolling_std(close.pct_change(), 21), 252)
    return _rolling_mean(base, 63)

def trgc_098_comp_vol_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_098_comp_vol_z_zscore_63d"""
    base = _zscore_rolling(_rolling_std(close.pct_change(), 21), 252)
    return _zscore_rolling(base, 63)

def trgc_099_comp_vol_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_099_comp_vol_z_rank_63d"""
    base = _zscore_rolling(_rolling_std(close.pct_change(), 21), 252)
    return _rank_pct(base, 63)

def trgc_100_comp_vol_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_100_comp_vol_z_lvl_126d"""
    base = _zscore_rolling(_rolling_std(close.pct_change(), 21), 252)
    return _rolling_mean(base, 126)

def trgc_101_comp_vol_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_101_comp_vol_z_zscore_126d"""
    base = _zscore_rolling(_rolling_std(close.pct_change(), 21), 252)
    return _zscore_rolling(base, 126)

def trgc_102_comp_vol_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_102_comp_vol_z_rank_126d"""
    base = _zscore_rolling(_rolling_std(close.pct_change(), 21), 252)
    return _rank_pct(base, 126)

def trgc_103_comp_vol_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_103_comp_vol_z_lvl_252d"""
    base = _zscore_rolling(_rolling_std(close.pct_change(), 21), 252)
    return _rolling_mean(base, 252)

def trgc_104_comp_vol_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_104_comp_vol_z_zscore_252d"""
    base = _zscore_rolling(_rolling_std(close.pct_change(), 21), 252)
    return _zscore_rolling(base, 252)

def trgc_105_comp_vol_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_105_comp_vol_z_rank_252d"""
    base = _zscore_rolling(_rolling_std(close.pct_change(), 21), 252)
    return _rank_pct(base, 252)

def trgc_106_comp_adv_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_106_comp_adv_z_lvl_5d"""
    base = _zscore_rolling(volume * close, 252)
    return _rolling_mean(base, 5)

def trgc_107_comp_adv_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_107_comp_adv_z_zscore_5d"""
    base = _zscore_rolling(volume * close, 252)
    return _zscore_rolling(base, 5)

def trgc_108_comp_adv_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_108_comp_adv_z_rank_5d"""
    base = _zscore_rolling(volume * close, 252)
    return _rank_pct(base, 5)

def trgc_109_comp_adv_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_109_comp_adv_z_lvl_21d"""
    base = _zscore_rolling(volume * close, 252)
    return _rolling_mean(base, 21)

def trgc_110_comp_adv_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_110_comp_adv_z_zscore_21d"""
    base = _zscore_rolling(volume * close, 252)
    return _zscore_rolling(base, 21)

def trgc_111_comp_adv_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_111_comp_adv_z_rank_21d"""
    base = _zscore_rolling(volume * close, 252)
    return _rank_pct(base, 21)

def trgc_112_comp_adv_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_112_comp_adv_z_lvl_63d"""
    base = _zscore_rolling(volume * close, 252)
    return _rolling_mean(base, 63)

def trgc_113_comp_adv_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_113_comp_adv_z_zscore_63d"""
    base = _zscore_rolling(volume * close, 252)
    return _zscore_rolling(base, 63)

def trgc_114_comp_adv_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_114_comp_adv_z_rank_63d"""
    base = _zscore_rolling(volume * close, 252)
    return _rank_pct(base, 63)

def trgc_115_comp_adv_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_115_comp_adv_z_lvl_126d"""
    base = _zscore_rolling(volume * close, 252)
    return _rolling_mean(base, 126)

def trgc_116_comp_adv_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_116_comp_adv_z_zscore_126d"""
    base = _zscore_rolling(volume * close, 252)
    return _zscore_rolling(base, 126)

def trgc_117_comp_adv_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_117_comp_adv_z_rank_126d"""
    base = _zscore_rolling(volume * close, 252)
    return _rank_pct(base, 126)

def trgc_118_comp_adv_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_118_comp_adv_z_lvl_252d"""
    base = _zscore_rolling(volume * close, 252)
    return _rolling_mean(base, 252)

def trgc_119_comp_adv_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_119_comp_adv_z_zscore_252d"""
    base = _zscore_rolling(volume * close, 252)
    return _zscore_rolling(base, 252)

def trgc_120_comp_adv_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_120_comp_adv_z_rank_252d"""
    base = _zscore_rolling(volume * close, 252)
    return _rank_pct(base, 252)

def trgc_121_comp_range_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_121_comp_range_z_lvl_5d"""
    base = _zscore_rolling(high - low, 252)
    return _rolling_mean(base, 5)

def trgc_122_comp_range_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_122_comp_range_z_zscore_5d"""
    base = _zscore_rolling(high - low, 252)
    return _zscore_rolling(base, 5)

def trgc_123_comp_range_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_123_comp_range_z_rank_5d"""
    base = _zscore_rolling(high - low, 252)
    return _rank_pct(base, 5)

def trgc_124_comp_range_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_124_comp_range_z_lvl_21d"""
    base = _zscore_rolling(high - low, 252)
    return _rolling_mean(base, 21)

def trgc_125_comp_range_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_125_comp_range_z_zscore_21d"""
    base = _zscore_rolling(high - low, 252)
    return _zscore_rolling(base, 21)

def trgc_126_comp_range_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_126_comp_range_z_rank_21d"""
    base = _zscore_rolling(high - low, 252)
    return _rank_pct(base, 21)

def trgc_127_comp_range_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_127_comp_range_z_lvl_63d"""
    base = _zscore_rolling(high - low, 252)
    return _rolling_mean(base, 63)

def trgc_128_comp_range_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_128_comp_range_z_zscore_63d"""
    base = _zscore_rolling(high - low, 252)
    return _zscore_rolling(base, 63)

def trgc_129_comp_range_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_129_comp_range_z_rank_63d"""
    base = _zscore_rolling(high - low, 252)
    return _rank_pct(base, 63)

def trgc_130_comp_range_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_130_comp_range_z_lvl_126d"""
    base = _zscore_rolling(high - low, 252)
    return _rolling_mean(base, 126)

def trgc_131_comp_range_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_131_comp_range_z_zscore_126d"""
    base = _zscore_rolling(high - low, 252)
    return _zscore_rolling(base, 126)

def trgc_132_comp_range_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_132_comp_range_z_rank_126d"""
    base = _zscore_rolling(high - low, 252)
    return _rank_pct(base, 126)

def trgc_133_comp_range_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_133_comp_range_z_lvl_252d"""
    base = _zscore_rolling(high - low, 252)
    return _rolling_mean(base, 252)

def trgc_134_comp_range_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_134_comp_range_z_zscore_252d"""
    base = _zscore_rolling(high - low, 252)
    return _zscore_rolling(base, 252)

def trgc_135_comp_range_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_135_comp_range_z_rank_252d"""
    base = _zscore_rolling(high - low, 252)
    return _rank_pct(base, 252)

def trgc_136_comp_trend_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_136_comp_trend_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 252)), 252)
    return _rolling_mean(base, 5)

def trgc_137_comp_trend_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_137_comp_trend_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 252)), 252)
    return _zscore_rolling(base, 5)

def trgc_138_comp_trend_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_138_comp_trend_z_rank_5d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 252)), 252)
    return _rank_pct(base, 5)

def trgc_139_comp_trend_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_139_comp_trend_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 252)), 252)
    return _rolling_mean(base, 21)

def trgc_140_comp_trend_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_140_comp_trend_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 252)), 252)
    return _zscore_rolling(base, 21)

def trgc_141_comp_trend_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_141_comp_trend_z_rank_21d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 252)), 252)
    return _rank_pct(base, 21)

def trgc_142_comp_trend_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_142_comp_trend_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 252)), 252)
    return _rolling_mean(base, 63)

def trgc_143_comp_trend_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_143_comp_trend_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 252)), 252)
    return _zscore_rolling(base, 63)

def trgc_144_comp_trend_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_144_comp_trend_z_rank_63d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 252)), 252)
    return _rank_pct(base, 63)

def trgc_145_comp_trend_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_145_comp_trend_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 252)), 252)
    return _rolling_mean(base, 126)

def trgc_146_comp_trend_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_146_comp_trend_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 252)), 252)
    return _zscore_rolling(base, 126)

def trgc_147_comp_trend_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_147_comp_trend_z_rank_126d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 252)), 252)
    return _rank_pct(base, 126)

def trgc_148_comp_trend_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_148_comp_trend_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 252)), 252)
    return _rolling_mean(base, 252)

def trgc_149_comp_trend_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_149_comp_trend_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 252)), 252)
    return _zscore_rolling(base, 252)

def trgc_150_comp_trend_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_150_comp_trend_z_rank_252d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 252)), 252)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V100_REGISTRY_2 = {
    "trgc_076_comp_mom_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_076_comp_mom_z_lvl_5d},
    "trgc_077_comp_mom_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_077_comp_mom_z_zscore_5d},
    "trgc_078_comp_mom_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_078_comp_mom_z_rank_5d},
    "trgc_079_comp_mom_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_079_comp_mom_z_lvl_21d},
    "trgc_080_comp_mom_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_080_comp_mom_z_zscore_21d},
    "trgc_081_comp_mom_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_081_comp_mom_z_rank_21d},
    "trgc_082_comp_mom_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_082_comp_mom_z_lvl_63d},
    "trgc_083_comp_mom_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_083_comp_mom_z_zscore_63d},
    "trgc_084_comp_mom_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_084_comp_mom_z_rank_63d},
    "trgc_085_comp_mom_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_085_comp_mom_z_lvl_126d},
    "trgc_086_comp_mom_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_086_comp_mom_z_zscore_126d},
    "trgc_087_comp_mom_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_087_comp_mom_z_rank_126d},
    "trgc_088_comp_mom_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_088_comp_mom_z_lvl_252d},
    "trgc_089_comp_mom_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_089_comp_mom_z_zscore_252d},
    "trgc_090_comp_mom_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_090_comp_mom_z_rank_252d},
    "trgc_091_comp_vol_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_091_comp_vol_z_lvl_5d},
    "trgc_092_comp_vol_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_092_comp_vol_z_zscore_5d},
    "trgc_093_comp_vol_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_093_comp_vol_z_rank_5d},
    "trgc_094_comp_vol_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_094_comp_vol_z_lvl_21d},
    "trgc_095_comp_vol_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_095_comp_vol_z_zscore_21d},
    "trgc_096_comp_vol_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_096_comp_vol_z_rank_21d},
    "trgc_097_comp_vol_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_097_comp_vol_z_lvl_63d},
    "trgc_098_comp_vol_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_098_comp_vol_z_zscore_63d},
    "trgc_099_comp_vol_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_099_comp_vol_z_rank_63d},
    "trgc_100_comp_vol_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_100_comp_vol_z_lvl_126d},
    "trgc_101_comp_vol_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_101_comp_vol_z_zscore_126d},
    "trgc_102_comp_vol_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_102_comp_vol_z_rank_126d},
    "trgc_103_comp_vol_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_103_comp_vol_z_lvl_252d},
    "trgc_104_comp_vol_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_104_comp_vol_z_zscore_252d},
    "trgc_105_comp_vol_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_105_comp_vol_z_rank_252d},
    "trgc_106_comp_adv_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_106_comp_adv_z_lvl_5d},
    "trgc_107_comp_adv_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_107_comp_adv_z_zscore_5d},
    "trgc_108_comp_adv_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_108_comp_adv_z_rank_5d},
    "trgc_109_comp_adv_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_109_comp_adv_z_lvl_21d},
    "trgc_110_comp_adv_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_110_comp_adv_z_zscore_21d},
    "trgc_111_comp_adv_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_111_comp_adv_z_rank_21d},
    "trgc_112_comp_adv_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_112_comp_adv_z_lvl_63d},
    "trgc_113_comp_adv_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_113_comp_adv_z_zscore_63d},
    "trgc_114_comp_adv_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_114_comp_adv_z_rank_63d},
    "trgc_115_comp_adv_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_115_comp_adv_z_lvl_126d},
    "trgc_116_comp_adv_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_116_comp_adv_z_zscore_126d},
    "trgc_117_comp_adv_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_117_comp_adv_z_rank_126d},
    "trgc_118_comp_adv_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_118_comp_adv_z_lvl_252d},
    "trgc_119_comp_adv_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_119_comp_adv_z_zscore_252d},
    "trgc_120_comp_adv_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_120_comp_adv_z_rank_252d},
    "trgc_121_comp_range_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_121_comp_range_z_lvl_5d},
    "trgc_122_comp_range_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_122_comp_range_z_zscore_5d},
    "trgc_123_comp_range_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_123_comp_range_z_rank_5d},
    "trgc_124_comp_range_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_124_comp_range_z_lvl_21d},
    "trgc_125_comp_range_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_125_comp_range_z_zscore_21d},
    "trgc_126_comp_range_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_126_comp_range_z_rank_21d},
    "trgc_127_comp_range_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_127_comp_range_z_lvl_63d},
    "trgc_128_comp_range_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_128_comp_range_z_zscore_63d},
    "trgc_129_comp_range_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_129_comp_range_z_rank_63d},
    "trgc_130_comp_range_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_130_comp_range_z_lvl_126d},
    "trgc_131_comp_range_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_131_comp_range_z_zscore_126d},
    "trgc_132_comp_range_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_132_comp_range_z_rank_126d},
    "trgc_133_comp_range_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_133_comp_range_z_lvl_252d},
    "trgc_134_comp_range_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_134_comp_range_z_zscore_252d},
    "trgc_135_comp_range_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_135_comp_range_z_rank_252d},
    "trgc_136_comp_trend_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_136_comp_trend_z_lvl_5d},
    "trgc_137_comp_trend_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_137_comp_trend_z_zscore_5d},
    "trgc_138_comp_trend_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_138_comp_trend_z_rank_5d},
    "trgc_139_comp_trend_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_139_comp_trend_z_lvl_21d},
    "trgc_140_comp_trend_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_140_comp_trend_z_zscore_21d},
    "trgc_141_comp_trend_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_141_comp_trend_z_rank_21d},
    "trgc_142_comp_trend_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_142_comp_trend_z_lvl_63d},
    "trgc_143_comp_trend_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_143_comp_trend_z_zscore_63d},
    "trgc_144_comp_trend_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_144_comp_trend_z_rank_63d},
    "trgc_145_comp_trend_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_145_comp_trend_z_lvl_126d},
    "trgc_146_comp_trend_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_146_comp_trend_z_zscore_126d},
    "trgc_147_comp_trend_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_147_comp_trend_z_rank_126d},
    "trgc_148_comp_trend_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_148_comp_trend_z_lvl_252d},
    "trgc_149_comp_trend_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_149_comp_trend_z_zscore_252d},
    "trgc_150_comp_trend_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_150_comp_trend_z_rank_252d},
}
