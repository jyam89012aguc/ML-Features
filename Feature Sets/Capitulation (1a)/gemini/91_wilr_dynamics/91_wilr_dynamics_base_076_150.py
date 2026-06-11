"""
91_wilr_dynamics — Base Features 076-150
Domain: wilr_dynamics
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

def wilr_076_wilr_extreme_up_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_076_wilr_extreme_up_lvl_5d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) > 0.8).astype(float)
    return _rolling_mean(base, 5)

def wilr_077_wilr_extreme_up_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_077_wilr_extreme_up_zscore_5d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) > 0.8).astype(float)
    return _zscore_rolling(base, 5)

def wilr_078_wilr_extreme_up_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_078_wilr_extreme_up_rank_5d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) > 0.8).astype(float)
    return _rank_pct(base, 5)

def wilr_079_wilr_extreme_up_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_079_wilr_extreme_up_lvl_21d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) > 0.8).astype(float)
    return _rolling_mean(base, 21)

def wilr_080_wilr_extreme_up_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_080_wilr_extreme_up_zscore_21d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) > 0.8).astype(float)
    return _zscore_rolling(base, 21)

def wilr_081_wilr_extreme_up_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_081_wilr_extreme_up_rank_21d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) > 0.8).astype(float)
    return _rank_pct(base, 21)

def wilr_082_wilr_extreme_up_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_082_wilr_extreme_up_lvl_63d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) > 0.8).astype(float)
    return _rolling_mean(base, 63)

def wilr_083_wilr_extreme_up_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_083_wilr_extreme_up_zscore_63d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) > 0.8).astype(float)
    return _zscore_rolling(base, 63)

def wilr_084_wilr_extreme_up_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_084_wilr_extreme_up_rank_63d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) > 0.8).astype(float)
    return _rank_pct(base, 63)

def wilr_085_wilr_extreme_up_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_085_wilr_extreme_up_lvl_126d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) > 0.8).astype(float)
    return _rolling_mean(base, 126)

def wilr_086_wilr_extreme_up_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_086_wilr_extreme_up_zscore_126d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) > 0.8).astype(float)
    return _zscore_rolling(base, 126)

def wilr_087_wilr_extreme_up_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_087_wilr_extreme_up_rank_126d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) > 0.8).astype(float)
    return _rank_pct(base, 126)

def wilr_088_wilr_extreme_up_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_088_wilr_extreme_up_lvl_252d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) > 0.8).astype(float)
    return _rolling_mean(base, 252)

def wilr_089_wilr_extreme_up_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_089_wilr_extreme_up_zscore_252d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) > 0.8).astype(float)
    return _zscore_rolling(base, 252)

def wilr_090_wilr_extreme_up_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_090_wilr_extreme_up_rank_252d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) > 0.8).astype(float)
    return _rank_pct(base, 252)

def wilr_091_wilr_extreme_dn_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_091_wilr_extreme_dn_lvl_5d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) < 0.2).astype(float)
    return _rolling_mean(base, 5)

def wilr_092_wilr_extreme_dn_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_092_wilr_extreme_dn_zscore_5d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) < 0.2).astype(float)
    return _zscore_rolling(base, 5)

def wilr_093_wilr_extreme_dn_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_093_wilr_extreme_dn_rank_5d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) < 0.2).astype(float)
    return _rank_pct(base, 5)

def wilr_094_wilr_extreme_dn_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_094_wilr_extreme_dn_lvl_21d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) < 0.2).astype(float)
    return _rolling_mean(base, 21)

def wilr_095_wilr_extreme_dn_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_095_wilr_extreme_dn_zscore_21d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) < 0.2).astype(float)
    return _zscore_rolling(base, 21)

def wilr_096_wilr_extreme_dn_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_096_wilr_extreme_dn_rank_21d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) < 0.2).astype(float)
    return _rank_pct(base, 21)

def wilr_097_wilr_extreme_dn_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_097_wilr_extreme_dn_lvl_63d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) < 0.2).astype(float)
    return _rolling_mean(base, 63)

def wilr_098_wilr_extreme_dn_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_098_wilr_extreme_dn_zscore_63d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) < 0.2).astype(float)
    return _zscore_rolling(base, 63)

def wilr_099_wilr_extreme_dn_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_099_wilr_extreme_dn_rank_63d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) < 0.2).astype(float)
    return _rank_pct(base, 63)

def wilr_100_wilr_extreme_dn_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_100_wilr_extreme_dn_lvl_126d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) < 0.2).astype(float)
    return _rolling_mean(base, 126)

def wilr_101_wilr_extreme_dn_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_101_wilr_extreme_dn_zscore_126d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) < 0.2).astype(float)
    return _zscore_rolling(base, 126)

def wilr_102_wilr_extreme_dn_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_102_wilr_extreme_dn_rank_126d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) < 0.2).astype(float)
    return _rank_pct(base, 126)

def wilr_103_wilr_extreme_dn_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_103_wilr_extreme_dn_lvl_252d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) < 0.2).astype(float)
    return _rolling_mean(base, 252)

def wilr_104_wilr_extreme_dn_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_104_wilr_extreme_dn_zscore_252d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) < 0.2).astype(float)
    return _zscore_rolling(base, 252)

def wilr_105_wilr_extreme_dn_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_105_wilr_extreme_dn_rank_252d"""
    base = (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) < 0.2).astype(float)
    return _rank_pct(base, 252)

def wilr_106_wilr_range_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_106_wilr_range_lvl_5d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rolling_mean(base, 5)

def wilr_107_wilr_range_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_107_wilr_range_zscore_5d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _zscore_rolling(base, 5)

def wilr_108_wilr_range_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_108_wilr_range_rank_5d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rank_pct(base, 5)

def wilr_109_wilr_range_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_109_wilr_range_lvl_21d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rolling_mean(base, 21)

def wilr_110_wilr_range_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_110_wilr_range_zscore_21d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _zscore_rolling(base, 21)

def wilr_111_wilr_range_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_111_wilr_range_rank_21d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rank_pct(base, 21)

def wilr_112_wilr_range_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_112_wilr_range_lvl_63d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rolling_mean(base, 63)

def wilr_113_wilr_range_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_113_wilr_range_zscore_63d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _zscore_rolling(base, 63)

def wilr_114_wilr_range_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_114_wilr_range_rank_63d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rank_pct(base, 63)

def wilr_115_wilr_range_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_115_wilr_range_lvl_126d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rolling_mean(base, 126)

def wilr_116_wilr_range_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_116_wilr_range_zscore_126d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _zscore_rolling(base, 126)

def wilr_117_wilr_range_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_117_wilr_range_rank_126d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rank_pct(base, 126)

def wilr_118_wilr_range_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_118_wilr_range_lvl_252d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rolling_mean(base, 252)

def wilr_119_wilr_range_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_119_wilr_range_zscore_252d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _zscore_rolling(base, 252)

def wilr_120_wilr_range_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_120_wilr_range_rank_252d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rank_pct(base, 252)

def wilr_121_wilr_close_pos_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_121_wilr_close_pos_lvl_5d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rolling_mean(base, 5)

def wilr_122_wilr_close_pos_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_122_wilr_close_pos_zscore_5d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14))
    return _zscore_rolling(base, 5)

def wilr_123_wilr_close_pos_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_123_wilr_close_pos_rank_5d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rank_pct(base, 5)

def wilr_124_wilr_close_pos_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_124_wilr_close_pos_lvl_21d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rolling_mean(base, 21)

def wilr_125_wilr_close_pos_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_125_wilr_close_pos_zscore_21d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14))
    return _zscore_rolling(base, 21)

def wilr_126_wilr_close_pos_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_126_wilr_close_pos_rank_21d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rank_pct(base, 21)

def wilr_127_wilr_close_pos_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_127_wilr_close_pos_lvl_63d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rolling_mean(base, 63)

def wilr_128_wilr_close_pos_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_128_wilr_close_pos_zscore_63d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14))
    return _zscore_rolling(base, 63)

def wilr_129_wilr_close_pos_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_129_wilr_close_pos_rank_63d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rank_pct(base, 63)

def wilr_130_wilr_close_pos_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_130_wilr_close_pos_lvl_126d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rolling_mean(base, 126)

def wilr_131_wilr_close_pos_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_131_wilr_close_pos_zscore_126d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14))
    return _zscore_rolling(base, 126)

def wilr_132_wilr_close_pos_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_132_wilr_close_pos_rank_126d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rank_pct(base, 126)

def wilr_133_wilr_close_pos_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_133_wilr_close_pos_lvl_252d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rolling_mean(base, 252)

def wilr_134_wilr_close_pos_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_134_wilr_close_pos_zscore_252d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14))
    return _zscore_rolling(base, 252)

def wilr_135_wilr_close_pos_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_135_wilr_close_pos_rank_252d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rank_pct(base, 252)

def wilr_136_wilr_vol_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_136_wilr_vol_lvl_5d"""
    base = _safe_div(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), volume)
    return _rolling_mean(base, 5)

def wilr_137_wilr_vol_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_137_wilr_vol_zscore_5d"""
    base = _safe_div(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), volume)
    return _zscore_rolling(base, 5)

def wilr_138_wilr_vol_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_138_wilr_vol_rank_5d"""
    base = _safe_div(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), volume)
    return _rank_pct(base, 5)

def wilr_139_wilr_vol_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_139_wilr_vol_lvl_21d"""
    base = _safe_div(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), volume)
    return _rolling_mean(base, 21)

def wilr_140_wilr_vol_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_140_wilr_vol_zscore_21d"""
    base = _safe_div(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), volume)
    return _zscore_rolling(base, 21)

def wilr_141_wilr_vol_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_141_wilr_vol_rank_21d"""
    base = _safe_div(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), volume)
    return _rank_pct(base, 21)

def wilr_142_wilr_vol_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_142_wilr_vol_lvl_63d"""
    base = _safe_div(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), volume)
    return _rolling_mean(base, 63)

def wilr_143_wilr_vol_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_143_wilr_vol_zscore_63d"""
    base = _safe_div(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), volume)
    return _zscore_rolling(base, 63)

def wilr_144_wilr_vol_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_144_wilr_vol_rank_63d"""
    base = _safe_div(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), volume)
    return _rank_pct(base, 63)

def wilr_145_wilr_vol_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_145_wilr_vol_lvl_126d"""
    base = _safe_div(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), volume)
    return _rolling_mean(base, 126)

def wilr_146_wilr_vol_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_146_wilr_vol_zscore_126d"""
    base = _safe_div(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), volume)
    return _zscore_rolling(base, 126)

def wilr_147_wilr_vol_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_147_wilr_vol_rank_126d"""
    base = _safe_div(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), volume)
    return _rank_pct(base, 126)

def wilr_148_wilr_vol_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_148_wilr_vol_lvl_252d"""
    base = _safe_div(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), volume)
    return _rolling_mean(base, 252)

def wilr_149_wilr_vol_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_149_wilr_vol_zscore_252d"""
    base = _safe_div(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), volume)
    return _zscore_rolling(base, 252)

def wilr_150_wilr_vol_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_150_wilr_vol_rank_252d"""
    base = _safe_div(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), volume)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V91_REGISTRY_2 = {
    "wilr_076_wilr_extreme_up_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_076_wilr_extreme_up_lvl_5d},
    "wilr_077_wilr_extreme_up_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_077_wilr_extreme_up_zscore_5d},
    "wilr_078_wilr_extreme_up_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_078_wilr_extreme_up_rank_5d},
    "wilr_079_wilr_extreme_up_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_079_wilr_extreme_up_lvl_21d},
    "wilr_080_wilr_extreme_up_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_080_wilr_extreme_up_zscore_21d},
    "wilr_081_wilr_extreme_up_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_081_wilr_extreme_up_rank_21d},
    "wilr_082_wilr_extreme_up_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_082_wilr_extreme_up_lvl_63d},
    "wilr_083_wilr_extreme_up_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_083_wilr_extreme_up_zscore_63d},
    "wilr_084_wilr_extreme_up_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_084_wilr_extreme_up_rank_63d},
    "wilr_085_wilr_extreme_up_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_085_wilr_extreme_up_lvl_126d},
    "wilr_086_wilr_extreme_up_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_086_wilr_extreme_up_zscore_126d},
    "wilr_087_wilr_extreme_up_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_087_wilr_extreme_up_rank_126d},
    "wilr_088_wilr_extreme_up_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_088_wilr_extreme_up_lvl_252d},
    "wilr_089_wilr_extreme_up_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_089_wilr_extreme_up_zscore_252d},
    "wilr_090_wilr_extreme_up_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_090_wilr_extreme_up_rank_252d},
    "wilr_091_wilr_extreme_dn_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_091_wilr_extreme_dn_lvl_5d},
    "wilr_092_wilr_extreme_dn_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_092_wilr_extreme_dn_zscore_5d},
    "wilr_093_wilr_extreme_dn_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_093_wilr_extreme_dn_rank_5d},
    "wilr_094_wilr_extreme_dn_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_094_wilr_extreme_dn_lvl_21d},
    "wilr_095_wilr_extreme_dn_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_095_wilr_extreme_dn_zscore_21d},
    "wilr_096_wilr_extreme_dn_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_096_wilr_extreme_dn_rank_21d},
    "wilr_097_wilr_extreme_dn_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_097_wilr_extreme_dn_lvl_63d},
    "wilr_098_wilr_extreme_dn_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_098_wilr_extreme_dn_zscore_63d},
    "wilr_099_wilr_extreme_dn_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_099_wilr_extreme_dn_rank_63d},
    "wilr_100_wilr_extreme_dn_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_100_wilr_extreme_dn_lvl_126d},
    "wilr_101_wilr_extreme_dn_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_101_wilr_extreme_dn_zscore_126d},
    "wilr_102_wilr_extreme_dn_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_102_wilr_extreme_dn_rank_126d},
    "wilr_103_wilr_extreme_dn_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_103_wilr_extreme_dn_lvl_252d},
    "wilr_104_wilr_extreme_dn_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_104_wilr_extreme_dn_zscore_252d},
    "wilr_105_wilr_extreme_dn_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_105_wilr_extreme_dn_rank_252d},
    "wilr_106_wilr_range_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_106_wilr_range_lvl_5d},
    "wilr_107_wilr_range_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_107_wilr_range_zscore_5d},
    "wilr_108_wilr_range_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_108_wilr_range_rank_5d},
    "wilr_109_wilr_range_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_109_wilr_range_lvl_21d},
    "wilr_110_wilr_range_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_110_wilr_range_zscore_21d},
    "wilr_111_wilr_range_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_111_wilr_range_rank_21d},
    "wilr_112_wilr_range_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_112_wilr_range_lvl_63d},
    "wilr_113_wilr_range_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_113_wilr_range_zscore_63d},
    "wilr_114_wilr_range_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_114_wilr_range_rank_63d},
    "wilr_115_wilr_range_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_115_wilr_range_lvl_126d},
    "wilr_116_wilr_range_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_116_wilr_range_zscore_126d},
    "wilr_117_wilr_range_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_117_wilr_range_rank_126d},
    "wilr_118_wilr_range_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_118_wilr_range_lvl_252d},
    "wilr_119_wilr_range_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_119_wilr_range_zscore_252d},
    "wilr_120_wilr_range_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_120_wilr_range_rank_252d},
    "wilr_121_wilr_close_pos_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_121_wilr_close_pos_lvl_5d},
    "wilr_122_wilr_close_pos_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_122_wilr_close_pos_zscore_5d},
    "wilr_123_wilr_close_pos_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_123_wilr_close_pos_rank_5d},
    "wilr_124_wilr_close_pos_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_124_wilr_close_pos_lvl_21d},
    "wilr_125_wilr_close_pos_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_125_wilr_close_pos_zscore_21d},
    "wilr_126_wilr_close_pos_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_126_wilr_close_pos_rank_21d},
    "wilr_127_wilr_close_pos_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_127_wilr_close_pos_lvl_63d},
    "wilr_128_wilr_close_pos_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_128_wilr_close_pos_zscore_63d},
    "wilr_129_wilr_close_pos_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_129_wilr_close_pos_rank_63d},
    "wilr_130_wilr_close_pos_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_130_wilr_close_pos_lvl_126d},
    "wilr_131_wilr_close_pos_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_131_wilr_close_pos_zscore_126d},
    "wilr_132_wilr_close_pos_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_132_wilr_close_pos_rank_126d},
    "wilr_133_wilr_close_pos_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_133_wilr_close_pos_lvl_252d},
    "wilr_134_wilr_close_pos_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_134_wilr_close_pos_zscore_252d},
    "wilr_135_wilr_close_pos_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_135_wilr_close_pos_rank_252d},
    "wilr_136_wilr_vol_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_136_wilr_vol_lvl_5d},
    "wilr_137_wilr_vol_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_137_wilr_vol_zscore_5d},
    "wilr_138_wilr_vol_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_138_wilr_vol_rank_5d},
    "wilr_139_wilr_vol_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_139_wilr_vol_lvl_21d},
    "wilr_140_wilr_vol_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_140_wilr_vol_zscore_21d},
    "wilr_141_wilr_vol_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_141_wilr_vol_rank_21d},
    "wilr_142_wilr_vol_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_142_wilr_vol_lvl_63d},
    "wilr_143_wilr_vol_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_143_wilr_vol_zscore_63d},
    "wilr_144_wilr_vol_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_144_wilr_vol_rank_63d},
    "wilr_145_wilr_vol_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_145_wilr_vol_lvl_126d},
    "wilr_146_wilr_vol_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_146_wilr_vol_zscore_126d},
    "wilr_147_wilr_vol_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_147_wilr_vol_rank_126d},
    "wilr_148_wilr_vol_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_148_wilr_vol_lvl_252d},
    "wilr_149_wilr_vol_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_149_wilr_vol_zscore_252d},
    "wilr_150_wilr_vol_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_150_wilr_vol_rank_252d},
}
