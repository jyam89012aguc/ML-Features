"""
95_vort_dynamics — Base Features 076-150
Domain: vort_dynamics
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

def vort_076_vi_plus_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_076_vi_plus_roc_lvl_5d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rolling_mean(base, 5)

def vort_077_vi_plus_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_077_vi_plus_roc_zscore_5d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _zscore_rolling(base, 5)

def vort_078_vi_plus_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_078_vi_plus_roc_rank_5d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rank_pct(base, 5)

def vort_079_vi_plus_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_079_vi_plus_roc_lvl_21d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rolling_mean(base, 21)

def vort_080_vi_plus_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_080_vi_plus_roc_zscore_21d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _zscore_rolling(base, 21)

def vort_081_vi_plus_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_081_vi_plus_roc_rank_21d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rank_pct(base, 21)

def vort_082_vi_plus_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_082_vi_plus_roc_lvl_63d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rolling_mean(base, 63)

def vort_083_vi_plus_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_083_vi_plus_roc_zscore_63d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _zscore_rolling(base, 63)

def vort_084_vi_plus_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_084_vi_plus_roc_rank_63d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rank_pct(base, 63)

def vort_085_vi_plus_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_085_vi_plus_roc_lvl_126d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rolling_mean(base, 126)

def vort_086_vi_plus_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_086_vi_plus_roc_zscore_126d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _zscore_rolling(base, 126)

def vort_087_vi_plus_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_087_vi_plus_roc_rank_126d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rank_pct(base, 126)

def vort_088_vi_plus_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_088_vi_plus_roc_lvl_252d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rolling_mean(base, 252)

def vort_089_vi_plus_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_089_vi_plus_roc_zscore_252d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _zscore_rolling(base, 252)

def vort_090_vi_plus_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_090_vi_plus_roc_rank_252d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rank_pct(base, 252)

def vort_091_vi_minus_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_091_vi_minus_roc_lvl_5d"""
    base = (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rolling_mean(base, 5)

def vort_092_vi_minus_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_092_vi_minus_roc_zscore_5d"""
    base = (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _zscore_rolling(base, 5)

def vort_093_vi_minus_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_093_vi_minus_roc_rank_5d"""
    base = (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rank_pct(base, 5)

def vort_094_vi_minus_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_094_vi_minus_roc_lvl_21d"""
    base = (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rolling_mean(base, 21)

def vort_095_vi_minus_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_095_vi_minus_roc_zscore_21d"""
    base = (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _zscore_rolling(base, 21)

def vort_096_vi_minus_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_096_vi_minus_roc_rank_21d"""
    base = (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rank_pct(base, 21)

def vort_097_vi_minus_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_097_vi_minus_roc_lvl_63d"""
    base = (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rolling_mean(base, 63)

def vort_098_vi_minus_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_098_vi_minus_roc_zscore_63d"""
    base = (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _zscore_rolling(base, 63)

def vort_099_vi_minus_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_099_vi_minus_roc_rank_63d"""
    base = (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rank_pct(base, 63)

def vort_100_vi_minus_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_100_vi_minus_roc_lvl_126d"""
    base = (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rolling_mean(base, 126)

def vort_101_vi_minus_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_101_vi_minus_roc_zscore_126d"""
    base = (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _zscore_rolling(base, 126)

def vort_102_vi_minus_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_102_vi_minus_roc_rank_126d"""
    base = (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rank_pct(base, 126)

def vort_103_vi_minus_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_103_vi_minus_roc_lvl_252d"""
    base = (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rolling_mean(base, 252)

def vort_104_vi_minus_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_104_vi_minus_roc_zscore_252d"""
    base = (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _zscore_rolling(base, 252)

def vort_105_vi_minus_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_105_vi_minus_roc_rank_252d"""
    base = (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rank_pct(base, 252)

def vort_106_vi_abs_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_106_vi_abs_lvl_5d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).abs()
    return _rolling_mean(base, 5)

def vort_107_vi_abs_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_107_vi_abs_zscore_5d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).abs()
    return _zscore_rolling(base, 5)

def vort_108_vi_abs_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_108_vi_abs_rank_5d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).abs()
    return _rank_pct(base, 5)

def vort_109_vi_abs_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_109_vi_abs_lvl_21d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).abs()
    return _rolling_mean(base, 21)

def vort_110_vi_abs_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_110_vi_abs_zscore_21d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).abs()
    return _zscore_rolling(base, 21)

def vort_111_vi_abs_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_111_vi_abs_rank_21d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).abs()
    return _rank_pct(base, 21)

def vort_112_vi_abs_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_112_vi_abs_lvl_63d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).abs()
    return _rolling_mean(base, 63)

def vort_113_vi_abs_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_113_vi_abs_zscore_63d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).abs()
    return _zscore_rolling(base, 63)

def vort_114_vi_abs_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_114_vi_abs_rank_63d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).abs()
    return _rank_pct(base, 63)

def vort_115_vi_abs_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_115_vi_abs_lvl_126d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).abs()
    return _rolling_mean(base, 126)

def vort_116_vi_abs_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_116_vi_abs_zscore_126d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).abs()
    return _zscore_rolling(base, 126)

def vort_117_vi_abs_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_117_vi_abs_rank_126d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).abs()
    return _rank_pct(base, 126)

def vort_118_vi_abs_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_118_vi_abs_lvl_252d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).abs()
    return _rolling_mean(base, 252)

def vort_119_vi_abs_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_119_vi_abs_zscore_252d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).abs()
    return _zscore_rolling(base, 252)

def vort_120_vi_abs_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_120_vi_abs_rank_252d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).abs()
    return _rank_pct(base, 252)

def vort_121_vi_sig_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_121_vi_sig_lvl_5d"""
    base = _rolling_mean(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 5)
    return _rolling_mean(base, 5)

def vort_122_vi_sig_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_122_vi_sig_zscore_5d"""
    base = _rolling_mean(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 5)
    return _zscore_rolling(base, 5)

def vort_123_vi_sig_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_123_vi_sig_rank_5d"""
    base = _rolling_mean(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 5)
    return _rank_pct(base, 5)

def vort_124_vi_sig_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_124_vi_sig_lvl_21d"""
    base = _rolling_mean(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 5)
    return _rolling_mean(base, 21)

def vort_125_vi_sig_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_125_vi_sig_zscore_21d"""
    base = _rolling_mean(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 5)
    return _zscore_rolling(base, 21)

def vort_126_vi_sig_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_126_vi_sig_rank_21d"""
    base = _rolling_mean(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 5)
    return _rank_pct(base, 21)

def vort_127_vi_sig_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_127_vi_sig_lvl_63d"""
    base = _rolling_mean(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 5)
    return _rolling_mean(base, 63)

def vort_128_vi_sig_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_128_vi_sig_zscore_63d"""
    base = _rolling_mean(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 5)
    return _zscore_rolling(base, 63)

def vort_129_vi_sig_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_129_vi_sig_rank_63d"""
    base = _rolling_mean(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 5)
    return _rank_pct(base, 63)

def vort_130_vi_sig_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_130_vi_sig_lvl_126d"""
    base = _rolling_mean(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 5)
    return _rolling_mean(base, 126)

def vort_131_vi_sig_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_131_vi_sig_zscore_126d"""
    base = _rolling_mean(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 5)
    return _zscore_rolling(base, 126)

def vort_132_vi_sig_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_132_vi_sig_rank_126d"""
    base = _rolling_mean(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 5)
    return _rank_pct(base, 126)

def vort_133_vi_sig_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_133_vi_sig_lvl_252d"""
    base = _rolling_mean(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 5)
    return _rolling_mean(base, 252)

def vort_134_vi_sig_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_134_vi_sig_zscore_252d"""
    base = _rolling_mean(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 5)
    return _zscore_rolling(base, 252)

def vort_135_vi_sig_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_135_vi_sig_rank_252d"""
    base = _rolling_mean(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 5)
    return _rank_pct(base, 252)

def vort_136_vi_tr_sum_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_136_vi_tr_sum_lvl_5d"""
    base = _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)
    return _rolling_mean(base, 5)

def vort_137_vi_tr_sum_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_137_vi_tr_sum_zscore_5d"""
    base = _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)
    return _zscore_rolling(base, 5)

def vort_138_vi_tr_sum_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_138_vi_tr_sum_rank_5d"""
    base = _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)
    return _rank_pct(base, 5)

def vort_139_vi_tr_sum_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_139_vi_tr_sum_lvl_21d"""
    base = _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)
    return _rolling_mean(base, 21)

def vort_140_vi_tr_sum_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_140_vi_tr_sum_zscore_21d"""
    base = _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)
    return _zscore_rolling(base, 21)

def vort_141_vi_tr_sum_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_141_vi_tr_sum_rank_21d"""
    base = _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)
    return _rank_pct(base, 21)

def vort_142_vi_tr_sum_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_142_vi_tr_sum_lvl_63d"""
    base = _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)
    return _rolling_mean(base, 63)

def vort_143_vi_tr_sum_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_143_vi_tr_sum_zscore_63d"""
    base = _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)
    return _zscore_rolling(base, 63)

def vort_144_vi_tr_sum_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_144_vi_tr_sum_rank_63d"""
    base = _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)
    return _rank_pct(base, 63)

def vort_145_vi_tr_sum_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_145_vi_tr_sum_lvl_126d"""
    base = _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)
    return _rolling_mean(base, 126)

def vort_146_vi_tr_sum_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_146_vi_tr_sum_zscore_126d"""
    base = _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)
    return _zscore_rolling(base, 126)

def vort_147_vi_tr_sum_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_147_vi_tr_sum_rank_126d"""
    base = _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)
    return _rank_pct(base, 126)

def vort_148_vi_tr_sum_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_148_vi_tr_sum_lvl_252d"""
    base = _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)
    return _rolling_mean(base, 252)

def vort_149_vi_tr_sum_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_149_vi_tr_sum_zscore_252d"""
    base = _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)
    return _zscore_rolling(base, 252)

def vort_150_vi_tr_sum_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_150_vi_tr_sum_rank_252d"""
    base = _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V95_REGISTRY_2 = {
    "vort_076_vi_plus_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_076_vi_plus_roc_lvl_5d},
    "vort_077_vi_plus_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_077_vi_plus_roc_zscore_5d},
    "vort_078_vi_plus_roc_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_078_vi_plus_roc_rank_5d},
    "vort_079_vi_plus_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_079_vi_plus_roc_lvl_21d},
    "vort_080_vi_plus_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_080_vi_plus_roc_zscore_21d},
    "vort_081_vi_plus_roc_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_081_vi_plus_roc_rank_21d},
    "vort_082_vi_plus_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_082_vi_plus_roc_lvl_63d},
    "vort_083_vi_plus_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_083_vi_plus_roc_zscore_63d},
    "vort_084_vi_plus_roc_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_084_vi_plus_roc_rank_63d},
    "vort_085_vi_plus_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_085_vi_plus_roc_lvl_126d},
    "vort_086_vi_plus_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_086_vi_plus_roc_zscore_126d},
    "vort_087_vi_plus_roc_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_087_vi_plus_roc_rank_126d},
    "vort_088_vi_plus_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_088_vi_plus_roc_lvl_252d},
    "vort_089_vi_plus_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_089_vi_plus_roc_zscore_252d},
    "vort_090_vi_plus_roc_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_090_vi_plus_roc_rank_252d},
    "vort_091_vi_minus_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_091_vi_minus_roc_lvl_5d},
    "vort_092_vi_minus_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_092_vi_minus_roc_zscore_5d},
    "vort_093_vi_minus_roc_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_093_vi_minus_roc_rank_5d},
    "vort_094_vi_minus_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_094_vi_minus_roc_lvl_21d},
    "vort_095_vi_minus_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_095_vi_minus_roc_zscore_21d},
    "vort_096_vi_minus_roc_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_096_vi_minus_roc_rank_21d},
    "vort_097_vi_minus_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_097_vi_minus_roc_lvl_63d},
    "vort_098_vi_minus_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_098_vi_minus_roc_zscore_63d},
    "vort_099_vi_minus_roc_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_099_vi_minus_roc_rank_63d},
    "vort_100_vi_minus_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_100_vi_minus_roc_lvl_126d},
    "vort_101_vi_minus_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_101_vi_minus_roc_zscore_126d},
    "vort_102_vi_minus_roc_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_102_vi_minus_roc_rank_126d},
    "vort_103_vi_minus_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_103_vi_minus_roc_lvl_252d},
    "vort_104_vi_minus_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_104_vi_minus_roc_zscore_252d},
    "vort_105_vi_minus_roc_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_105_vi_minus_roc_rank_252d},
    "vort_106_vi_abs_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_106_vi_abs_lvl_5d},
    "vort_107_vi_abs_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_107_vi_abs_zscore_5d},
    "vort_108_vi_abs_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_108_vi_abs_rank_5d},
    "vort_109_vi_abs_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_109_vi_abs_lvl_21d},
    "vort_110_vi_abs_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_110_vi_abs_zscore_21d},
    "vort_111_vi_abs_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_111_vi_abs_rank_21d},
    "vort_112_vi_abs_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_112_vi_abs_lvl_63d},
    "vort_113_vi_abs_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_113_vi_abs_zscore_63d},
    "vort_114_vi_abs_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_114_vi_abs_rank_63d},
    "vort_115_vi_abs_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_115_vi_abs_lvl_126d},
    "vort_116_vi_abs_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_116_vi_abs_zscore_126d},
    "vort_117_vi_abs_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_117_vi_abs_rank_126d},
    "vort_118_vi_abs_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_118_vi_abs_lvl_252d},
    "vort_119_vi_abs_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_119_vi_abs_zscore_252d},
    "vort_120_vi_abs_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_120_vi_abs_rank_252d},
    "vort_121_vi_sig_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_121_vi_sig_lvl_5d},
    "vort_122_vi_sig_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_122_vi_sig_zscore_5d},
    "vort_123_vi_sig_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_123_vi_sig_rank_5d},
    "vort_124_vi_sig_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_124_vi_sig_lvl_21d},
    "vort_125_vi_sig_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_125_vi_sig_zscore_21d},
    "vort_126_vi_sig_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_126_vi_sig_rank_21d},
    "vort_127_vi_sig_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_127_vi_sig_lvl_63d},
    "vort_128_vi_sig_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_128_vi_sig_zscore_63d},
    "vort_129_vi_sig_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_129_vi_sig_rank_63d},
    "vort_130_vi_sig_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_130_vi_sig_lvl_126d},
    "vort_131_vi_sig_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_131_vi_sig_zscore_126d},
    "vort_132_vi_sig_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_132_vi_sig_rank_126d},
    "vort_133_vi_sig_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_133_vi_sig_lvl_252d},
    "vort_134_vi_sig_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_134_vi_sig_zscore_252d},
    "vort_135_vi_sig_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_135_vi_sig_rank_252d},
    "vort_136_vi_tr_sum_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_136_vi_tr_sum_lvl_5d},
    "vort_137_vi_tr_sum_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_137_vi_tr_sum_zscore_5d},
    "vort_138_vi_tr_sum_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_138_vi_tr_sum_rank_5d},
    "vort_139_vi_tr_sum_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_139_vi_tr_sum_lvl_21d},
    "vort_140_vi_tr_sum_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_140_vi_tr_sum_zscore_21d},
    "vort_141_vi_tr_sum_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_141_vi_tr_sum_rank_21d},
    "vort_142_vi_tr_sum_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_142_vi_tr_sum_lvl_63d},
    "vort_143_vi_tr_sum_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_143_vi_tr_sum_zscore_63d},
    "vort_144_vi_tr_sum_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_144_vi_tr_sum_rank_63d},
    "vort_145_vi_tr_sum_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_145_vi_tr_sum_lvl_126d},
    "vort_146_vi_tr_sum_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_146_vi_tr_sum_zscore_126d},
    "vort_147_vi_tr_sum_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_147_vi_tr_sum_rank_126d},
    "vort_148_vi_tr_sum_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_148_vi_tr_sum_lvl_252d},
    "vort_149_vi_tr_sum_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_149_vi_tr_sum_zscore_252d},
    "vort_150_vi_tr_sum_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_150_vi_tr_sum_rank_252d},
}
