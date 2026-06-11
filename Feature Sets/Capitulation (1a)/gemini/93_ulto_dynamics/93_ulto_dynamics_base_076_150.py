"""
93_ulto_dynamics — Base Features 076-150
Domain: ulto_dynamics
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

def ulto_076_bp_lvl_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_076_bp_lvl_lvl_5d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 5)

def ulto_077_bp_lvl_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_077_bp_lvl_zscore_5d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 5)

def ulto_078_bp_lvl_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_078_bp_lvl_rank_5d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 5)

def ulto_079_bp_lvl_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_079_bp_lvl_lvl_21d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 21)

def ulto_080_bp_lvl_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_080_bp_lvl_zscore_21d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 21)

def ulto_081_bp_lvl_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_081_bp_lvl_rank_21d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 21)

def ulto_082_bp_lvl_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_082_bp_lvl_lvl_63d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 63)

def ulto_083_bp_lvl_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_083_bp_lvl_zscore_63d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 63)

def ulto_084_bp_lvl_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_084_bp_lvl_rank_63d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 63)

def ulto_085_bp_lvl_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_085_bp_lvl_lvl_126d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 126)

def ulto_086_bp_lvl_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_086_bp_lvl_zscore_126d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 126)

def ulto_087_bp_lvl_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_087_bp_lvl_rank_126d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 126)

def ulto_088_bp_lvl_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_088_bp_lvl_lvl_252d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 252)

def ulto_089_bp_lvl_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_089_bp_lvl_zscore_252d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 252)

def ulto_090_bp_lvl_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_090_bp_lvl_rank_252d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 252)

def ulto_091_tr_lvl_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_091_tr_lvl_lvl_5d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 5)

def ulto_092_tr_lvl_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_092_tr_lvl_zscore_5d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 5)

def ulto_093_tr_lvl_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_093_tr_lvl_rank_5d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 5)

def ulto_094_tr_lvl_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_094_tr_lvl_lvl_21d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 21)

def ulto_095_tr_lvl_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_095_tr_lvl_zscore_21d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 21)

def ulto_096_tr_lvl_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_096_tr_lvl_rank_21d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 21)

def ulto_097_tr_lvl_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_097_tr_lvl_lvl_63d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 63)

def ulto_098_tr_lvl_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_098_tr_lvl_zscore_63d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 63)

def ulto_099_tr_lvl_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_099_tr_lvl_rank_63d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 63)

def ulto_100_tr_lvl_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_100_tr_lvl_lvl_126d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 126)

def ulto_101_tr_lvl_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_101_tr_lvl_zscore_126d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 126)

def ulto_102_tr_lvl_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_102_tr_lvl_rank_126d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 126)

def ulto_103_tr_lvl_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_103_tr_lvl_lvl_252d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 252)

def ulto_104_tr_lvl_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_104_tr_lvl_zscore_252d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 252)

def ulto_105_tr_lvl_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_105_tr_lvl_rank_252d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 252)

def ulto_106_ult_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_106_ult_roc_lvl_5d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).pct_change()
    return _rolling_mean(base, 5)

def ulto_107_ult_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_107_ult_roc_zscore_5d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).pct_change()
    return _zscore_rolling(base, 5)

def ulto_108_ult_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_108_ult_roc_rank_5d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).pct_change()
    return _rank_pct(base, 5)

def ulto_109_ult_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_109_ult_roc_lvl_21d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).pct_change()
    return _rolling_mean(base, 21)

def ulto_110_ult_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_110_ult_roc_zscore_21d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).pct_change()
    return _zscore_rolling(base, 21)

def ulto_111_ult_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_111_ult_roc_rank_21d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).pct_change()
    return _rank_pct(base, 21)

def ulto_112_ult_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_112_ult_roc_lvl_63d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).pct_change()
    return _rolling_mean(base, 63)

def ulto_113_ult_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_113_ult_roc_zscore_63d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).pct_change()
    return _zscore_rolling(base, 63)

def ulto_114_ult_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_114_ult_roc_rank_63d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).pct_change()
    return _rank_pct(base, 63)

def ulto_115_ult_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_115_ult_roc_lvl_126d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).pct_change()
    return _rolling_mean(base, 126)

def ulto_116_ult_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_116_ult_roc_zscore_126d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).pct_change()
    return _zscore_rolling(base, 126)

def ulto_117_ult_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_117_ult_roc_rank_126d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).pct_change()
    return _rank_pct(base, 126)

def ulto_118_ult_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_118_ult_roc_lvl_252d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).pct_change()
    return _rolling_mean(base, 252)

def ulto_119_ult_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_119_ult_roc_zscore_252d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).pct_change()
    return _zscore_rolling(base, 252)

def ulto_120_ult_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_120_ult_roc_rank_252d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).pct_change()
    return _rank_pct(base, 252)

def ulto_121_ult_sig_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_121_ult_sig_lvl_5d"""
    base = _rolling_mean(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 5)
    return _rolling_mean(base, 5)

def ulto_122_ult_sig_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_122_ult_sig_zscore_5d"""
    base = _rolling_mean(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 5)
    return _zscore_rolling(base, 5)

def ulto_123_ult_sig_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_123_ult_sig_rank_5d"""
    base = _rolling_mean(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 5)
    return _rank_pct(base, 5)

def ulto_124_ult_sig_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_124_ult_sig_lvl_21d"""
    base = _rolling_mean(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 5)
    return _rolling_mean(base, 21)

def ulto_125_ult_sig_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_125_ult_sig_zscore_21d"""
    base = _rolling_mean(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 5)
    return _zscore_rolling(base, 21)

def ulto_126_ult_sig_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_126_ult_sig_rank_21d"""
    base = _rolling_mean(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 5)
    return _rank_pct(base, 21)

def ulto_127_ult_sig_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_127_ult_sig_lvl_63d"""
    base = _rolling_mean(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 5)
    return _rolling_mean(base, 63)

def ulto_128_ult_sig_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_128_ult_sig_zscore_63d"""
    base = _rolling_mean(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 5)
    return _zscore_rolling(base, 63)

def ulto_129_ult_sig_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_129_ult_sig_rank_63d"""
    base = _rolling_mean(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 5)
    return _rank_pct(base, 63)

def ulto_130_ult_sig_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_130_ult_sig_lvl_126d"""
    base = _rolling_mean(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 5)
    return _rolling_mean(base, 126)

def ulto_131_ult_sig_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_131_ult_sig_zscore_126d"""
    base = _rolling_mean(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 5)
    return _zscore_rolling(base, 126)

def ulto_132_ult_sig_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_132_ult_sig_rank_126d"""
    base = _rolling_mean(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 5)
    return _rank_pct(base, 126)

def ulto_133_ult_sig_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_133_ult_sig_lvl_252d"""
    base = _rolling_mean(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 5)
    return _rolling_mean(base, 252)

def ulto_134_ult_sig_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_134_ult_sig_zscore_252d"""
    base = _rolling_mean(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 5)
    return _zscore_rolling(base, 252)

def ulto_135_ult_sig_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_135_ult_sig_rank_252d"""
    base = _rolling_mean(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 5)
    return _rank_pct(base, 252)

def ulto_136_ult_abs_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_136_ult_abs_lvl_5d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).abs()
    return _rolling_mean(base, 5)

def ulto_137_ult_abs_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_137_ult_abs_zscore_5d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).abs()
    return _zscore_rolling(base, 5)

def ulto_138_ult_abs_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_138_ult_abs_rank_5d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).abs()
    return _rank_pct(base, 5)

def ulto_139_ult_abs_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_139_ult_abs_lvl_21d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).abs()
    return _rolling_mean(base, 21)

def ulto_140_ult_abs_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_140_ult_abs_zscore_21d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).abs()
    return _zscore_rolling(base, 21)

def ulto_141_ult_abs_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_141_ult_abs_rank_21d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).abs()
    return _rank_pct(base, 21)

def ulto_142_ult_abs_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_142_ult_abs_lvl_63d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).abs()
    return _rolling_mean(base, 63)

def ulto_143_ult_abs_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_143_ult_abs_zscore_63d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).abs()
    return _zscore_rolling(base, 63)

def ulto_144_ult_abs_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_144_ult_abs_rank_63d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).abs()
    return _rank_pct(base, 63)

def ulto_145_ult_abs_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_145_ult_abs_lvl_126d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).abs()
    return _rolling_mean(base, 126)

def ulto_146_ult_abs_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_146_ult_abs_zscore_126d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).abs()
    return _zscore_rolling(base, 126)

def ulto_147_ult_abs_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_147_ult_abs_rank_126d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).abs()
    return _rank_pct(base, 126)

def ulto_148_ult_abs_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_148_ult_abs_lvl_252d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).abs()
    return _rolling_mean(base, 252)

def ulto_149_ult_abs_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_149_ult_abs_zscore_252d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).abs()
    return _zscore_rolling(base, 252)

def ulto_150_ult_abs_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_150_ult_abs_rank_252d"""
    base = (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).abs()
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V93_REGISTRY_2 = {
    "ulto_076_bp_lvl_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_076_bp_lvl_lvl_5d},
    "ulto_077_bp_lvl_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_077_bp_lvl_zscore_5d},
    "ulto_078_bp_lvl_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_078_bp_lvl_rank_5d},
    "ulto_079_bp_lvl_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_079_bp_lvl_lvl_21d},
    "ulto_080_bp_lvl_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_080_bp_lvl_zscore_21d},
    "ulto_081_bp_lvl_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_081_bp_lvl_rank_21d},
    "ulto_082_bp_lvl_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_082_bp_lvl_lvl_63d},
    "ulto_083_bp_lvl_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_083_bp_lvl_zscore_63d},
    "ulto_084_bp_lvl_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_084_bp_lvl_rank_63d},
    "ulto_085_bp_lvl_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_085_bp_lvl_lvl_126d},
    "ulto_086_bp_lvl_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_086_bp_lvl_zscore_126d},
    "ulto_087_bp_lvl_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_087_bp_lvl_rank_126d},
    "ulto_088_bp_lvl_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_088_bp_lvl_lvl_252d},
    "ulto_089_bp_lvl_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_089_bp_lvl_zscore_252d},
    "ulto_090_bp_lvl_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_090_bp_lvl_rank_252d},
    "ulto_091_tr_lvl_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_091_tr_lvl_lvl_5d},
    "ulto_092_tr_lvl_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_092_tr_lvl_zscore_5d},
    "ulto_093_tr_lvl_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_093_tr_lvl_rank_5d},
    "ulto_094_tr_lvl_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_094_tr_lvl_lvl_21d},
    "ulto_095_tr_lvl_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_095_tr_lvl_zscore_21d},
    "ulto_096_tr_lvl_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_096_tr_lvl_rank_21d},
    "ulto_097_tr_lvl_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_097_tr_lvl_lvl_63d},
    "ulto_098_tr_lvl_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_098_tr_lvl_zscore_63d},
    "ulto_099_tr_lvl_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_099_tr_lvl_rank_63d},
    "ulto_100_tr_lvl_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_100_tr_lvl_lvl_126d},
    "ulto_101_tr_lvl_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_101_tr_lvl_zscore_126d},
    "ulto_102_tr_lvl_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_102_tr_lvl_rank_126d},
    "ulto_103_tr_lvl_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_103_tr_lvl_lvl_252d},
    "ulto_104_tr_lvl_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_104_tr_lvl_zscore_252d},
    "ulto_105_tr_lvl_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_105_tr_lvl_rank_252d},
    "ulto_106_ult_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_106_ult_roc_lvl_5d},
    "ulto_107_ult_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_107_ult_roc_zscore_5d},
    "ulto_108_ult_roc_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_108_ult_roc_rank_5d},
    "ulto_109_ult_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_109_ult_roc_lvl_21d},
    "ulto_110_ult_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_110_ult_roc_zscore_21d},
    "ulto_111_ult_roc_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_111_ult_roc_rank_21d},
    "ulto_112_ult_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_112_ult_roc_lvl_63d},
    "ulto_113_ult_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_113_ult_roc_zscore_63d},
    "ulto_114_ult_roc_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_114_ult_roc_rank_63d},
    "ulto_115_ult_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_115_ult_roc_lvl_126d},
    "ulto_116_ult_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_116_ult_roc_zscore_126d},
    "ulto_117_ult_roc_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_117_ult_roc_rank_126d},
    "ulto_118_ult_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_118_ult_roc_lvl_252d},
    "ulto_119_ult_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_119_ult_roc_zscore_252d},
    "ulto_120_ult_roc_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_120_ult_roc_rank_252d},
    "ulto_121_ult_sig_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_121_ult_sig_lvl_5d},
    "ulto_122_ult_sig_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_122_ult_sig_zscore_5d},
    "ulto_123_ult_sig_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_123_ult_sig_rank_5d},
    "ulto_124_ult_sig_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_124_ult_sig_lvl_21d},
    "ulto_125_ult_sig_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_125_ult_sig_zscore_21d},
    "ulto_126_ult_sig_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_126_ult_sig_rank_21d},
    "ulto_127_ult_sig_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_127_ult_sig_lvl_63d},
    "ulto_128_ult_sig_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_128_ult_sig_zscore_63d},
    "ulto_129_ult_sig_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_129_ult_sig_rank_63d},
    "ulto_130_ult_sig_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_130_ult_sig_lvl_126d},
    "ulto_131_ult_sig_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_131_ult_sig_zscore_126d},
    "ulto_132_ult_sig_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_132_ult_sig_rank_126d},
    "ulto_133_ult_sig_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_133_ult_sig_lvl_252d},
    "ulto_134_ult_sig_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_134_ult_sig_zscore_252d},
    "ulto_135_ult_sig_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_135_ult_sig_rank_252d},
    "ulto_136_ult_abs_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_136_ult_abs_lvl_5d},
    "ulto_137_ult_abs_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_137_ult_abs_zscore_5d},
    "ulto_138_ult_abs_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_138_ult_abs_rank_5d},
    "ulto_139_ult_abs_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_139_ult_abs_lvl_21d},
    "ulto_140_ult_abs_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_140_ult_abs_zscore_21d},
    "ulto_141_ult_abs_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_141_ult_abs_rank_21d},
    "ulto_142_ult_abs_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_142_ult_abs_lvl_63d},
    "ulto_143_ult_abs_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_143_ult_abs_zscore_63d},
    "ulto_144_ult_abs_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_144_ult_abs_rank_63d},
    "ulto_145_ult_abs_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_145_ult_abs_lvl_126d},
    "ulto_146_ult_abs_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_146_ult_abs_zscore_126d},
    "ulto_147_ult_abs_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_147_ult_abs_rank_126d},
    "ulto_148_ult_abs_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_148_ult_abs_lvl_252d},
    "ulto_149_ult_abs_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_149_ult_abs_zscore_252d},
    "ulto_150_ult_abs_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_150_ult_abs_rank_252d},
}
