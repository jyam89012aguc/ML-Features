"""
78_stoc_dynamics — Base Features 076-150
Domain: stoc_dynamics
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
    return s.rolling(w, min_periods=max(1, w // 2)).mean()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std().fillna(0)

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()

def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()

def _ewm_mean(s: pd.Series, w: int) -> pd.Series:
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)

def _rsi(s: pd.Series, w: int) -> pd.Series:
    delta = s.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=w).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=w).mean()
    rs = _safe_div(gain, loss)
    return 100 - (100 / (1 + rs))

# ── Feature functions ────────────────────────────────────────────────────────

def stoc_076_stoc_fast_k_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_076_stoc_fast_k_lvl_5d"""
    base = _safe_div(close - _rolling_min(low, 5), _rolling_max(high, 5) - _rolling_min(low, 5)) * 100
    return _rolling_mean(base, 5)

def stoc_077_stoc_fast_k_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_077_stoc_fast_k_zscore_5d"""
    base = _safe_div(close - _rolling_min(low, 5), _rolling_max(high, 5) - _rolling_min(low, 5)) * 100
    return _zscore_rolling(base, 5)

def stoc_078_stoc_fast_k_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_078_stoc_fast_k_rank_5d"""
    base = _safe_div(close - _rolling_min(low, 5), _rolling_max(high, 5) - _rolling_min(low, 5)) * 100
    return _rank_pct(base, 5)

def stoc_079_stoc_fast_k_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_079_stoc_fast_k_lvl_21d"""
    base = _safe_div(close - _rolling_min(low, 5), _rolling_max(high, 5) - _rolling_min(low, 5)) * 100
    return _rolling_mean(base, 21)

def stoc_080_stoc_fast_k_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_080_stoc_fast_k_zscore_21d"""
    base = _safe_div(close - _rolling_min(low, 5), _rolling_max(high, 5) - _rolling_min(low, 5)) * 100
    return _zscore_rolling(base, 21)

def stoc_081_stoc_fast_k_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_081_stoc_fast_k_rank_21d"""
    base = _safe_div(close - _rolling_min(low, 5), _rolling_max(high, 5) - _rolling_min(low, 5)) * 100
    return _rank_pct(base, 21)

def stoc_082_stoc_fast_k_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_082_stoc_fast_k_lvl_63d"""
    base = _safe_div(close - _rolling_min(low, 5), _rolling_max(high, 5) - _rolling_min(low, 5)) * 100
    return _rolling_mean(base, 63)

def stoc_083_stoc_fast_k_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_083_stoc_fast_k_zscore_63d"""
    base = _safe_div(close - _rolling_min(low, 5), _rolling_max(high, 5) - _rolling_min(low, 5)) * 100
    return _zscore_rolling(base, 63)

def stoc_084_stoc_fast_k_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_084_stoc_fast_k_rank_63d"""
    base = _safe_div(close - _rolling_min(low, 5), _rolling_max(high, 5) - _rolling_min(low, 5)) * 100
    return _rank_pct(base, 63)

def stoc_085_stoc_fast_k_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_085_stoc_fast_k_lvl_126d"""
    base = _safe_div(close - _rolling_min(low, 5), _rolling_max(high, 5) - _rolling_min(low, 5)) * 100
    return _rolling_mean(base, 126)

def stoc_086_stoc_fast_k_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_086_stoc_fast_k_zscore_126d"""
    base = _safe_div(close - _rolling_min(low, 5), _rolling_max(high, 5) - _rolling_min(low, 5)) * 100
    return _zscore_rolling(base, 126)

def stoc_087_stoc_fast_k_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_087_stoc_fast_k_rank_126d"""
    base = _safe_div(close - _rolling_min(low, 5), _rolling_max(high, 5) - _rolling_min(low, 5)) * 100
    return _rank_pct(base, 126)

def stoc_088_stoc_fast_k_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_088_stoc_fast_k_lvl_252d"""
    base = _safe_div(close - _rolling_min(low, 5), _rolling_max(high, 5) - _rolling_min(low, 5)) * 100
    return _rolling_mean(base, 252)

def stoc_089_stoc_fast_k_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_089_stoc_fast_k_zscore_252d"""
    base = _safe_div(close - _rolling_min(low, 5), _rolling_max(high, 5) - _rolling_min(low, 5)) * 100
    return _zscore_rolling(base, 252)

def stoc_090_stoc_fast_k_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_090_stoc_fast_k_rank_252d"""
    base = _safe_div(close - _rolling_min(low, 5), _rolling_max(high, 5) - _rolling_min(low, 5)) * 100
    return _rank_pct(base, 252)

def stoc_091_stoc_slow_k_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_091_stoc_slow_k_lvl_5d"""
    base = _safe_div(close - _rolling_min(low, 21), _rolling_max(high, 21) - _rolling_min(low, 21)) * 100
    return _rolling_mean(base, 5)

def stoc_092_stoc_slow_k_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_092_stoc_slow_k_zscore_5d"""
    base = _safe_div(close - _rolling_min(low, 21), _rolling_max(high, 21) - _rolling_min(low, 21)) * 100
    return _zscore_rolling(base, 5)

def stoc_093_stoc_slow_k_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_093_stoc_slow_k_rank_5d"""
    base = _safe_div(close - _rolling_min(low, 21), _rolling_max(high, 21) - _rolling_min(low, 21)) * 100
    return _rank_pct(base, 5)

def stoc_094_stoc_slow_k_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_094_stoc_slow_k_lvl_21d"""
    base = _safe_div(close - _rolling_min(low, 21), _rolling_max(high, 21) - _rolling_min(low, 21)) * 100
    return _rolling_mean(base, 21)

def stoc_095_stoc_slow_k_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_095_stoc_slow_k_zscore_21d"""
    base = _safe_div(close - _rolling_min(low, 21), _rolling_max(high, 21) - _rolling_min(low, 21)) * 100
    return _zscore_rolling(base, 21)

def stoc_096_stoc_slow_k_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_096_stoc_slow_k_rank_21d"""
    base = _safe_div(close - _rolling_min(low, 21), _rolling_max(high, 21) - _rolling_min(low, 21)) * 100
    return _rank_pct(base, 21)

def stoc_097_stoc_slow_k_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_097_stoc_slow_k_lvl_63d"""
    base = _safe_div(close - _rolling_min(low, 21), _rolling_max(high, 21) - _rolling_min(low, 21)) * 100
    return _rolling_mean(base, 63)

def stoc_098_stoc_slow_k_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_098_stoc_slow_k_zscore_63d"""
    base = _safe_div(close - _rolling_min(low, 21), _rolling_max(high, 21) - _rolling_min(low, 21)) * 100
    return _zscore_rolling(base, 63)

def stoc_099_stoc_slow_k_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_099_stoc_slow_k_rank_63d"""
    base = _safe_div(close - _rolling_min(low, 21), _rolling_max(high, 21) - _rolling_min(low, 21)) * 100
    return _rank_pct(base, 63)

def stoc_100_stoc_slow_k_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_100_stoc_slow_k_lvl_126d"""
    base = _safe_div(close - _rolling_min(low, 21), _rolling_max(high, 21) - _rolling_min(low, 21)) * 100
    return _rolling_mean(base, 126)

def stoc_101_stoc_slow_k_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_101_stoc_slow_k_zscore_126d"""
    base = _safe_div(close - _rolling_min(low, 21), _rolling_max(high, 21) - _rolling_min(low, 21)) * 100
    return _zscore_rolling(base, 126)

def stoc_102_stoc_slow_k_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_102_stoc_slow_k_rank_126d"""
    base = _safe_div(close - _rolling_min(low, 21), _rolling_max(high, 21) - _rolling_min(low, 21)) * 100
    return _rank_pct(base, 126)

def stoc_103_stoc_slow_k_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_103_stoc_slow_k_lvl_252d"""
    base = _safe_div(close - _rolling_min(low, 21), _rolling_max(high, 21) - _rolling_min(low, 21)) * 100
    return _rolling_mean(base, 252)

def stoc_104_stoc_slow_k_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_104_stoc_slow_k_zscore_252d"""
    base = _safe_div(close - _rolling_min(low, 21), _rolling_max(high, 21) - _rolling_min(low, 21)) * 100
    return _zscore_rolling(base, 252)

def stoc_105_stoc_slow_k_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_105_stoc_slow_k_rank_252d"""
    base = _safe_div(close - _rolling_min(low, 21), _rolling_max(high, 21) - _rolling_min(low, 21)) * 100
    return _rank_pct(base, 252)

def stoc_106_stoc_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_106_stoc_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 63)
    return _rolling_mean(base, 5)

def stoc_107_stoc_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_107_stoc_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 63)
    return _zscore_rolling(base, 5)

def stoc_108_stoc_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_108_stoc_z_rank_5d"""
    base = _zscore_rolling(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 63)
    return _rank_pct(base, 5)

def stoc_109_stoc_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_109_stoc_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 63)
    return _rolling_mean(base, 21)

def stoc_110_stoc_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_110_stoc_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 63)
    return _zscore_rolling(base, 21)

def stoc_111_stoc_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_111_stoc_z_rank_21d"""
    base = _zscore_rolling(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 63)
    return _rank_pct(base, 21)

def stoc_112_stoc_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_112_stoc_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 63)
    return _rolling_mean(base, 63)

def stoc_113_stoc_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_113_stoc_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 63)
    return _zscore_rolling(base, 63)

def stoc_114_stoc_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_114_stoc_z_rank_63d"""
    base = _zscore_rolling(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 63)
    return _rank_pct(base, 63)

def stoc_115_stoc_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_115_stoc_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 63)
    return _rolling_mean(base, 126)

def stoc_116_stoc_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_116_stoc_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 63)
    return _zscore_rolling(base, 126)

def stoc_117_stoc_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_117_stoc_z_rank_126d"""
    base = _zscore_rolling(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 63)
    return _rank_pct(base, 126)

def stoc_118_stoc_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_118_stoc_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 63)
    return _rolling_mean(base, 252)

def stoc_119_stoc_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_119_stoc_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 63)
    return _zscore_rolling(base, 252)

def stoc_120_stoc_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_120_stoc_z_rank_252d"""
    base = _zscore_rolling(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 63)
    return _rank_pct(base, 252)

def stoc_121_stoc_sma_rat_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_121_stoc_sma_rat_lvl_5d"""
    base = _safe_div(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 14))
    return _rolling_mean(base, 5)

def stoc_122_stoc_sma_rat_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_122_stoc_sma_rat_zscore_5d"""
    base = _safe_div(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 14))
    return _zscore_rolling(base, 5)

def stoc_123_stoc_sma_rat_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_123_stoc_sma_rat_rank_5d"""
    base = _safe_div(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 14))
    return _rank_pct(base, 5)

def stoc_124_stoc_sma_rat_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_124_stoc_sma_rat_lvl_21d"""
    base = _safe_div(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 14))
    return _rolling_mean(base, 21)

def stoc_125_stoc_sma_rat_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_125_stoc_sma_rat_zscore_21d"""
    base = _safe_div(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 14))
    return _zscore_rolling(base, 21)

def stoc_126_stoc_sma_rat_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_126_stoc_sma_rat_rank_21d"""
    base = _safe_div(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 14))
    return _rank_pct(base, 21)

def stoc_127_stoc_sma_rat_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_127_stoc_sma_rat_lvl_63d"""
    base = _safe_div(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 14))
    return _rolling_mean(base, 63)

def stoc_128_stoc_sma_rat_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_128_stoc_sma_rat_zscore_63d"""
    base = _safe_div(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 14))
    return _zscore_rolling(base, 63)

def stoc_129_stoc_sma_rat_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_129_stoc_sma_rat_rank_63d"""
    base = _safe_div(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 14))
    return _rank_pct(base, 63)

def stoc_130_stoc_sma_rat_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_130_stoc_sma_rat_lvl_126d"""
    base = _safe_div(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 14))
    return _rolling_mean(base, 126)

def stoc_131_stoc_sma_rat_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_131_stoc_sma_rat_zscore_126d"""
    base = _safe_div(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 14))
    return _zscore_rolling(base, 126)

def stoc_132_stoc_sma_rat_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_132_stoc_sma_rat_rank_126d"""
    base = _safe_div(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 14))
    return _rank_pct(base, 126)

def stoc_133_stoc_sma_rat_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_133_stoc_sma_rat_lvl_252d"""
    base = _safe_div(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 14))
    return _rolling_mean(base, 252)

def stoc_134_stoc_sma_rat_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_134_stoc_sma_rat_zscore_252d"""
    base = _safe_div(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 14))
    return _zscore_rolling(base, 252)

def stoc_135_stoc_sma_rat_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_135_stoc_sma_rat_rank_252d"""
    base = _safe_div(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 14))
    return _rank_pct(base, 252)

def stoc_136_stoc_diff_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_136_stoc_diff_lvl_5d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(5)
    return _rolling_mean(base, 5)

def stoc_137_stoc_diff_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_137_stoc_diff_zscore_5d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(5)
    return _zscore_rolling(base, 5)

def stoc_138_stoc_diff_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_138_stoc_diff_rank_5d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(5)
    return _rank_pct(base, 5)

def stoc_139_stoc_diff_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_139_stoc_diff_lvl_21d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(5)
    return _rolling_mean(base, 21)

def stoc_140_stoc_diff_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_140_stoc_diff_zscore_21d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(5)
    return _zscore_rolling(base, 21)

def stoc_141_stoc_diff_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_141_stoc_diff_rank_21d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(5)
    return _rank_pct(base, 21)

def stoc_142_stoc_diff_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_142_stoc_diff_lvl_63d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(5)
    return _rolling_mean(base, 63)

def stoc_143_stoc_diff_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_143_stoc_diff_zscore_63d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(5)
    return _zscore_rolling(base, 63)

def stoc_144_stoc_diff_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_144_stoc_diff_rank_63d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(5)
    return _rank_pct(base, 63)

def stoc_145_stoc_diff_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_145_stoc_diff_lvl_126d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(5)
    return _rolling_mean(base, 126)

def stoc_146_stoc_diff_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_146_stoc_diff_zscore_126d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(5)
    return _zscore_rolling(base, 126)

def stoc_147_stoc_diff_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_147_stoc_diff_rank_126d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(5)
    return _rank_pct(base, 126)

def stoc_148_stoc_diff_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_148_stoc_diff_lvl_252d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(5)
    return _rolling_mean(base, 252)

def stoc_149_stoc_diff_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_149_stoc_diff_zscore_252d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(5)
    return _zscore_rolling(base, 252)

def stoc_150_stoc_diff_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_150_stoc_diff_rank_252d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(5)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V78_REGISTRY_2 = {
    "stoc_076_stoc_fast_k_lvl_5d": {"inputs": ["high", "low", "close"], "func": stoc_076_stoc_fast_k_lvl_5d},
    "stoc_077_stoc_fast_k_zscore_5d": {"inputs": ["high", "low", "close"], "func": stoc_077_stoc_fast_k_zscore_5d},
    "stoc_078_stoc_fast_k_rank_5d": {"inputs": ["high", "low", "close"], "func": stoc_078_stoc_fast_k_rank_5d},
    "stoc_079_stoc_fast_k_lvl_21d": {"inputs": ["high", "low", "close"], "func": stoc_079_stoc_fast_k_lvl_21d},
    "stoc_080_stoc_fast_k_zscore_21d": {"inputs": ["high", "low", "close"], "func": stoc_080_stoc_fast_k_zscore_21d},
    "stoc_081_stoc_fast_k_rank_21d": {"inputs": ["high", "low", "close"], "func": stoc_081_stoc_fast_k_rank_21d},
    "stoc_082_stoc_fast_k_lvl_63d": {"inputs": ["high", "low", "close"], "func": stoc_082_stoc_fast_k_lvl_63d},
    "stoc_083_stoc_fast_k_zscore_63d": {"inputs": ["high", "low", "close"], "func": stoc_083_stoc_fast_k_zscore_63d},
    "stoc_084_stoc_fast_k_rank_63d": {"inputs": ["high", "low", "close"], "func": stoc_084_stoc_fast_k_rank_63d},
    "stoc_085_stoc_fast_k_lvl_126d": {"inputs": ["high", "low", "close"], "func": stoc_085_stoc_fast_k_lvl_126d},
    "stoc_086_stoc_fast_k_zscore_126d": {"inputs": ["high", "low", "close"], "func": stoc_086_stoc_fast_k_zscore_126d},
    "stoc_087_stoc_fast_k_rank_126d": {"inputs": ["high", "low", "close"], "func": stoc_087_stoc_fast_k_rank_126d},
    "stoc_088_stoc_fast_k_lvl_252d": {"inputs": ["high", "low", "close"], "func": stoc_088_stoc_fast_k_lvl_252d},
    "stoc_089_stoc_fast_k_zscore_252d": {"inputs": ["high", "low", "close"], "func": stoc_089_stoc_fast_k_zscore_252d},
    "stoc_090_stoc_fast_k_rank_252d": {"inputs": ["high", "low", "close"], "func": stoc_090_stoc_fast_k_rank_252d},
    "stoc_091_stoc_slow_k_lvl_5d": {"inputs": ["high", "low", "close"], "func": stoc_091_stoc_slow_k_lvl_5d},
    "stoc_092_stoc_slow_k_zscore_5d": {"inputs": ["high", "low", "close"], "func": stoc_092_stoc_slow_k_zscore_5d},
    "stoc_093_stoc_slow_k_rank_5d": {"inputs": ["high", "low", "close"], "func": stoc_093_stoc_slow_k_rank_5d},
    "stoc_094_stoc_slow_k_lvl_21d": {"inputs": ["high", "low", "close"], "func": stoc_094_stoc_slow_k_lvl_21d},
    "stoc_095_stoc_slow_k_zscore_21d": {"inputs": ["high", "low", "close"], "func": stoc_095_stoc_slow_k_zscore_21d},
    "stoc_096_stoc_slow_k_rank_21d": {"inputs": ["high", "low", "close"], "func": stoc_096_stoc_slow_k_rank_21d},
    "stoc_097_stoc_slow_k_lvl_63d": {"inputs": ["high", "low", "close"], "func": stoc_097_stoc_slow_k_lvl_63d},
    "stoc_098_stoc_slow_k_zscore_63d": {"inputs": ["high", "low", "close"], "func": stoc_098_stoc_slow_k_zscore_63d},
    "stoc_099_stoc_slow_k_rank_63d": {"inputs": ["high", "low", "close"], "func": stoc_099_stoc_slow_k_rank_63d},
    "stoc_100_stoc_slow_k_lvl_126d": {"inputs": ["high", "low", "close"], "func": stoc_100_stoc_slow_k_lvl_126d},
    "stoc_101_stoc_slow_k_zscore_126d": {"inputs": ["high", "low", "close"], "func": stoc_101_stoc_slow_k_zscore_126d},
    "stoc_102_stoc_slow_k_rank_126d": {"inputs": ["high", "low", "close"], "func": stoc_102_stoc_slow_k_rank_126d},
    "stoc_103_stoc_slow_k_lvl_252d": {"inputs": ["high", "low", "close"], "func": stoc_103_stoc_slow_k_lvl_252d},
    "stoc_104_stoc_slow_k_zscore_252d": {"inputs": ["high", "low", "close"], "func": stoc_104_stoc_slow_k_zscore_252d},
    "stoc_105_stoc_slow_k_rank_252d": {"inputs": ["high", "low", "close"], "func": stoc_105_stoc_slow_k_rank_252d},
    "stoc_106_stoc_z_lvl_5d": {"inputs": ["high", "low", "close"], "func": stoc_106_stoc_z_lvl_5d},
    "stoc_107_stoc_z_zscore_5d": {"inputs": ["high", "low", "close"], "func": stoc_107_stoc_z_zscore_5d},
    "stoc_108_stoc_z_rank_5d": {"inputs": ["high", "low", "close"], "func": stoc_108_stoc_z_rank_5d},
    "stoc_109_stoc_z_lvl_21d": {"inputs": ["high", "low", "close"], "func": stoc_109_stoc_z_lvl_21d},
    "stoc_110_stoc_z_zscore_21d": {"inputs": ["high", "low", "close"], "func": stoc_110_stoc_z_zscore_21d},
    "stoc_111_stoc_z_rank_21d": {"inputs": ["high", "low", "close"], "func": stoc_111_stoc_z_rank_21d},
    "stoc_112_stoc_z_lvl_63d": {"inputs": ["high", "low", "close"], "func": stoc_112_stoc_z_lvl_63d},
    "stoc_113_stoc_z_zscore_63d": {"inputs": ["high", "low", "close"], "func": stoc_113_stoc_z_zscore_63d},
    "stoc_114_stoc_z_rank_63d": {"inputs": ["high", "low", "close"], "func": stoc_114_stoc_z_rank_63d},
    "stoc_115_stoc_z_lvl_126d": {"inputs": ["high", "low", "close"], "func": stoc_115_stoc_z_lvl_126d},
    "stoc_116_stoc_z_zscore_126d": {"inputs": ["high", "low", "close"], "func": stoc_116_stoc_z_zscore_126d},
    "stoc_117_stoc_z_rank_126d": {"inputs": ["high", "low", "close"], "func": stoc_117_stoc_z_rank_126d},
    "stoc_118_stoc_z_lvl_252d": {"inputs": ["high", "low", "close"], "func": stoc_118_stoc_z_lvl_252d},
    "stoc_119_stoc_z_zscore_252d": {"inputs": ["high", "low", "close"], "func": stoc_119_stoc_z_zscore_252d},
    "stoc_120_stoc_z_rank_252d": {"inputs": ["high", "low", "close"], "func": stoc_120_stoc_z_rank_252d},
    "stoc_121_stoc_sma_rat_lvl_5d": {"inputs": ["high", "low", "close"], "func": stoc_121_stoc_sma_rat_lvl_5d},
    "stoc_122_stoc_sma_rat_zscore_5d": {"inputs": ["high", "low", "close"], "func": stoc_122_stoc_sma_rat_zscore_5d},
    "stoc_123_stoc_sma_rat_rank_5d": {"inputs": ["high", "low", "close"], "func": stoc_123_stoc_sma_rat_rank_5d},
    "stoc_124_stoc_sma_rat_lvl_21d": {"inputs": ["high", "low", "close"], "func": stoc_124_stoc_sma_rat_lvl_21d},
    "stoc_125_stoc_sma_rat_zscore_21d": {"inputs": ["high", "low", "close"], "func": stoc_125_stoc_sma_rat_zscore_21d},
    "stoc_126_stoc_sma_rat_rank_21d": {"inputs": ["high", "low", "close"], "func": stoc_126_stoc_sma_rat_rank_21d},
    "stoc_127_stoc_sma_rat_lvl_63d": {"inputs": ["high", "low", "close"], "func": stoc_127_stoc_sma_rat_lvl_63d},
    "stoc_128_stoc_sma_rat_zscore_63d": {"inputs": ["high", "low", "close"], "func": stoc_128_stoc_sma_rat_zscore_63d},
    "stoc_129_stoc_sma_rat_rank_63d": {"inputs": ["high", "low", "close"], "func": stoc_129_stoc_sma_rat_rank_63d},
    "stoc_130_stoc_sma_rat_lvl_126d": {"inputs": ["high", "low", "close"], "func": stoc_130_stoc_sma_rat_lvl_126d},
    "stoc_131_stoc_sma_rat_zscore_126d": {"inputs": ["high", "low", "close"], "func": stoc_131_stoc_sma_rat_zscore_126d},
    "stoc_132_stoc_sma_rat_rank_126d": {"inputs": ["high", "low", "close"], "func": stoc_132_stoc_sma_rat_rank_126d},
    "stoc_133_stoc_sma_rat_lvl_252d": {"inputs": ["high", "low", "close"], "func": stoc_133_stoc_sma_rat_lvl_252d},
    "stoc_134_stoc_sma_rat_zscore_252d": {"inputs": ["high", "low", "close"], "func": stoc_134_stoc_sma_rat_zscore_252d},
    "stoc_135_stoc_sma_rat_rank_252d": {"inputs": ["high", "low", "close"], "func": stoc_135_stoc_sma_rat_rank_252d},
    "stoc_136_stoc_diff_lvl_5d": {"inputs": ["high", "low", "close"], "func": stoc_136_stoc_diff_lvl_5d},
    "stoc_137_stoc_diff_zscore_5d": {"inputs": ["high", "low", "close"], "func": stoc_137_stoc_diff_zscore_5d},
    "stoc_138_stoc_diff_rank_5d": {"inputs": ["high", "low", "close"], "func": stoc_138_stoc_diff_rank_5d},
    "stoc_139_stoc_diff_lvl_21d": {"inputs": ["high", "low", "close"], "func": stoc_139_stoc_diff_lvl_21d},
    "stoc_140_stoc_diff_zscore_21d": {"inputs": ["high", "low", "close"], "func": stoc_140_stoc_diff_zscore_21d},
    "stoc_141_stoc_diff_rank_21d": {"inputs": ["high", "low", "close"], "func": stoc_141_stoc_diff_rank_21d},
    "stoc_142_stoc_diff_lvl_63d": {"inputs": ["high", "low", "close"], "func": stoc_142_stoc_diff_lvl_63d},
    "stoc_143_stoc_diff_zscore_63d": {"inputs": ["high", "low", "close"], "func": stoc_143_stoc_diff_zscore_63d},
    "stoc_144_stoc_diff_rank_63d": {"inputs": ["high", "low", "close"], "func": stoc_144_stoc_diff_rank_63d},
    "stoc_145_stoc_diff_lvl_126d": {"inputs": ["high", "low", "close"], "func": stoc_145_stoc_diff_lvl_126d},
    "stoc_146_stoc_diff_zscore_126d": {"inputs": ["high", "low", "close"], "func": stoc_146_stoc_diff_zscore_126d},
    "stoc_147_stoc_diff_rank_126d": {"inputs": ["high", "low", "close"], "func": stoc_147_stoc_diff_rank_126d},
    "stoc_148_stoc_diff_lvl_252d": {"inputs": ["high", "low", "close"], "func": stoc_148_stoc_diff_lvl_252d},
    "stoc_149_stoc_diff_zscore_252d": {"inputs": ["high", "low", "close"], "func": stoc_149_stoc_diff_zscore_252d},
    "stoc_150_stoc_diff_rank_252d": {"inputs": ["high", "low", "close"], "func": stoc_150_stoc_diff_rank_252d},
}
