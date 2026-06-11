"""
96_mrrs_dynamics — Base Features 076-150
Domain: mrrs_dynamics
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

def mrrs_076_rs_ratio_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_076_rs_ratio_roc_lvl_5d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).pct_change()
    return _rolling_mean(base, 5)

def mrrs_077_rs_ratio_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_077_rs_ratio_roc_zscore_5d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).pct_change()
    return _zscore_rolling(base, 5)

def mrrs_078_rs_ratio_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_078_rs_ratio_roc_rank_5d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).pct_change()
    return _rank_pct(base, 5)

def mrrs_079_rs_ratio_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_079_rs_ratio_roc_lvl_21d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).pct_change()
    return _rolling_mean(base, 21)

def mrrs_080_rs_ratio_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_080_rs_ratio_roc_zscore_21d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).pct_change()
    return _zscore_rolling(base, 21)

def mrrs_081_rs_ratio_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_081_rs_ratio_roc_rank_21d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).pct_change()
    return _rank_pct(base, 21)

def mrrs_082_rs_ratio_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_082_rs_ratio_roc_lvl_63d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).pct_change()
    return _rolling_mean(base, 63)

def mrrs_083_rs_ratio_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_083_rs_ratio_roc_zscore_63d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).pct_change()
    return _zscore_rolling(base, 63)

def mrrs_084_rs_ratio_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_084_rs_ratio_roc_rank_63d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).pct_change()
    return _rank_pct(base, 63)

def mrrs_085_rs_ratio_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_085_rs_ratio_roc_lvl_126d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).pct_change()
    return _rolling_mean(base, 126)

def mrrs_086_rs_ratio_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_086_rs_ratio_roc_zscore_126d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).pct_change()
    return _zscore_rolling(base, 126)

def mrrs_087_rs_ratio_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_087_rs_ratio_roc_rank_126d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).pct_change()
    return _rank_pct(base, 126)

def mrrs_088_rs_ratio_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_088_rs_ratio_roc_lvl_252d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).pct_change()
    return _rolling_mean(base, 252)

def mrrs_089_rs_ratio_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_089_rs_ratio_roc_zscore_252d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).pct_change()
    return _zscore_rolling(base, 252)

def mrrs_090_rs_ratio_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_090_rs_ratio_roc_rank_252d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).pct_change()
    return _rank_pct(base, 252)

def mrrs_091_rs_mom_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_091_rs_mom_roc_lvl_5d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).pct_change()
    return _rolling_mean(base, 5)

def mrrs_092_rs_mom_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_092_rs_mom_roc_zscore_5d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).pct_change()
    return _zscore_rolling(base, 5)

def mrrs_093_rs_mom_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_093_rs_mom_roc_rank_5d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).pct_change()
    return _rank_pct(base, 5)

def mrrs_094_rs_mom_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_094_rs_mom_roc_lvl_21d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).pct_change()
    return _rolling_mean(base, 21)

def mrrs_095_rs_mom_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_095_rs_mom_roc_zscore_21d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).pct_change()
    return _zscore_rolling(base, 21)

def mrrs_096_rs_mom_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_096_rs_mom_roc_rank_21d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).pct_change()
    return _rank_pct(base, 21)

def mrrs_097_rs_mom_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_097_rs_mom_roc_lvl_63d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).pct_change()
    return _rolling_mean(base, 63)

def mrrs_098_rs_mom_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_098_rs_mom_roc_zscore_63d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).pct_change()
    return _zscore_rolling(base, 63)

def mrrs_099_rs_mom_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_099_rs_mom_roc_rank_63d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).pct_change()
    return _rank_pct(base, 63)

def mrrs_100_rs_mom_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_100_rs_mom_roc_lvl_126d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).pct_change()
    return _rolling_mean(base, 126)

def mrrs_101_rs_mom_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_101_rs_mom_roc_zscore_126d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).pct_change()
    return _zscore_rolling(base, 126)

def mrrs_102_rs_mom_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_102_rs_mom_roc_rank_126d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).pct_change()
    return _rank_pct(base, 126)

def mrrs_103_rs_mom_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_103_rs_mom_roc_lvl_252d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).pct_change()
    return _rolling_mean(base, 252)

def mrrs_104_rs_mom_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_104_rs_mom_roc_zscore_252d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).pct_change()
    return _zscore_rolling(base, 252)

def mrrs_105_rs_mom_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_105_rs_mom_roc_rank_252d"""
    base = (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).pct_change()
    return _rank_pct(base, 252)

def mrrs_106_rs_abs_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_106_rs_abs_lvl_5d"""
    base = _safe_div(close, mkt_close).abs()
    return _rolling_mean(base, 5)

def mrrs_107_rs_abs_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_107_rs_abs_zscore_5d"""
    base = _safe_div(close, mkt_close).abs()
    return _zscore_rolling(base, 5)

def mrrs_108_rs_abs_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_108_rs_abs_rank_5d"""
    base = _safe_div(close, mkt_close).abs()
    return _rank_pct(base, 5)

def mrrs_109_rs_abs_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_109_rs_abs_lvl_21d"""
    base = _safe_div(close, mkt_close).abs()
    return _rolling_mean(base, 21)

def mrrs_110_rs_abs_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_110_rs_abs_zscore_21d"""
    base = _safe_div(close, mkt_close).abs()
    return _zscore_rolling(base, 21)

def mrrs_111_rs_abs_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_111_rs_abs_rank_21d"""
    base = _safe_div(close, mkt_close).abs()
    return _rank_pct(base, 21)

def mrrs_112_rs_abs_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_112_rs_abs_lvl_63d"""
    base = _safe_div(close, mkt_close).abs()
    return _rolling_mean(base, 63)

def mrrs_113_rs_abs_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_113_rs_abs_zscore_63d"""
    base = _safe_div(close, mkt_close).abs()
    return _zscore_rolling(base, 63)

def mrrs_114_rs_abs_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_114_rs_abs_rank_63d"""
    base = _safe_div(close, mkt_close).abs()
    return _rank_pct(base, 63)

def mrrs_115_rs_abs_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_115_rs_abs_lvl_126d"""
    base = _safe_div(close, mkt_close).abs()
    return _rolling_mean(base, 126)

def mrrs_116_rs_abs_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_116_rs_abs_zscore_126d"""
    base = _safe_div(close, mkt_close).abs()
    return _zscore_rolling(base, 126)

def mrrs_117_rs_abs_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_117_rs_abs_rank_126d"""
    base = _safe_div(close, mkt_close).abs()
    return _rank_pct(base, 126)

def mrrs_118_rs_abs_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_118_rs_abs_lvl_252d"""
    base = _safe_div(close, mkt_close).abs()
    return _rolling_mean(base, 252)

def mrrs_119_rs_abs_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_119_rs_abs_zscore_252d"""
    base = _safe_div(close, mkt_close).abs()
    return _zscore_rolling(base, 252)

def mrrs_120_rs_abs_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_120_rs_abs_rank_252d"""
    base = _safe_div(close, mkt_close).abs()
    return _rank_pct(base, 252)

def mrrs_121_rs_sig_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_121_rs_sig_lvl_5d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rolling_mean(base, 5)

def mrrs_122_rs_sig_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_122_rs_sig_zscore_5d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _zscore_rolling(base, 5)

def mrrs_123_rs_sig_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_123_rs_sig_rank_5d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rank_pct(base, 5)

def mrrs_124_rs_sig_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_124_rs_sig_lvl_21d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rolling_mean(base, 21)

def mrrs_125_rs_sig_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_125_rs_sig_zscore_21d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _zscore_rolling(base, 21)

def mrrs_126_rs_sig_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_126_rs_sig_rank_21d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rank_pct(base, 21)

def mrrs_127_rs_sig_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_127_rs_sig_lvl_63d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rolling_mean(base, 63)

def mrrs_128_rs_sig_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_128_rs_sig_zscore_63d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _zscore_rolling(base, 63)

def mrrs_129_rs_sig_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_129_rs_sig_rank_63d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rank_pct(base, 63)

def mrrs_130_rs_sig_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_130_rs_sig_lvl_126d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rolling_mean(base, 126)

def mrrs_131_rs_sig_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_131_rs_sig_zscore_126d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _zscore_rolling(base, 126)

def mrrs_132_rs_sig_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_132_rs_sig_rank_126d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rank_pct(base, 126)

def mrrs_133_rs_sig_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_133_rs_sig_lvl_252d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rolling_mean(base, 252)

def mrrs_134_rs_sig_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_134_rs_sig_zscore_252d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _zscore_rolling(base, 252)

def mrrs_135_rs_sig_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_135_rs_sig_rank_252d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rank_pct(base, 252)

def mrrs_136_rs_dist_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_136_rs_dist_lvl_5d"""
    base = _safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 5)

def mrrs_137_rs_dist_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_137_rs_dist_zscore_5d"""
    base = _safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 5)

def mrrs_138_rs_dist_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_138_rs_dist_rank_5d"""
    base = _safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 5)

def mrrs_139_rs_dist_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_139_rs_dist_lvl_21d"""
    base = _safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 21)

def mrrs_140_rs_dist_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_140_rs_dist_zscore_21d"""
    base = _safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 21)

def mrrs_141_rs_dist_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_141_rs_dist_rank_21d"""
    base = _safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 21)

def mrrs_142_rs_dist_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_142_rs_dist_lvl_63d"""
    base = _safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 63)

def mrrs_143_rs_dist_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_143_rs_dist_zscore_63d"""
    base = _safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 63)

def mrrs_144_rs_dist_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_144_rs_dist_rank_63d"""
    base = _safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 63)

def mrrs_145_rs_dist_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_145_rs_dist_lvl_126d"""
    base = _safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 126)

def mrrs_146_rs_dist_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_146_rs_dist_zscore_126d"""
    base = _safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 126)

def mrrs_147_rs_dist_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_147_rs_dist_rank_126d"""
    base = _safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 126)

def mrrs_148_rs_dist_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_148_rs_dist_lvl_252d"""
    base = _safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 252)

def mrrs_149_rs_dist_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_149_rs_dist_zscore_252d"""
    base = _safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 252)

def mrrs_150_rs_dist_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_150_rs_dist_rank_252d"""
    base = _safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V96_REGISTRY_2 = {
    "mrrs_076_rs_ratio_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_076_rs_ratio_roc_lvl_5d},
    "mrrs_077_rs_ratio_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_077_rs_ratio_roc_zscore_5d},
    "mrrs_078_rs_ratio_roc_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_078_rs_ratio_roc_rank_5d},
    "mrrs_079_rs_ratio_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_079_rs_ratio_roc_lvl_21d},
    "mrrs_080_rs_ratio_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_080_rs_ratio_roc_zscore_21d},
    "mrrs_081_rs_ratio_roc_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_081_rs_ratio_roc_rank_21d},
    "mrrs_082_rs_ratio_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_082_rs_ratio_roc_lvl_63d},
    "mrrs_083_rs_ratio_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_083_rs_ratio_roc_zscore_63d},
    "mrrs_084_rs_ratio_roc_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_084_rs_ratio_roc_rank_63d},
    "mrrs_085_rs_ratio_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_085_rs_ratio_roc_lvl_126d},
    "mrrs_086_rs_ratio_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_086_rs_ratio_roc_zscore_126d},
    "mrrs_087_rs_ratio_roc_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_087_rs_ratio_roc_rank_126d},
    "mrrs_088_rs_ratio_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_088_rs_ratio_roc_lvl_252d},
    "mrrs_089_rs_ratio_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_089_rs_ratio_roc_zscore_252d},
    "mrrs_090_rs_ratio_roc_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_090_rs_ratio_roc_rank_252d},
    "mrrs_091_rs_mom_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_091_rs_mom_roc_lvl_5d},
    "mrrs_092_rs_mom_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_092_rs_mom_roc_zscore_5d},
    "mrrs_093_rs_mom_roc_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_093_rs_mom_roc_rank_5d},
    "mrrs_094_rs_mom_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_094_rs_mom_roc_lvl_21d},
    "mrrs_095_rs_mom_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_095_rs_mom_roc_zscore_21d},
    "mrrs_096_rs_mom_roc_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_096_rs_mom_roc_rank_21d},
    "mrrs_097_rs_mom_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_097_rs_mom_roc_lvl_63d},
    "mrrs_098_rs_mom_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_098_rs_mom_roc_zscore_63d},
    "mrrs_099_rs_mom_roc_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_099_rs_mom_roc_rank_63d},
    "mrrs_100_rs_mom_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_100_rs_mom_roc_lvl_126d},
    "mrrs_101_rs_mom_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_101_rs_mom_roc_zscore_126d},
    "mrrs_102_rs_mom_roc_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_102_rs_mom_roc_rank_126d},
    "mrrs_103_rs_mom_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_103_rs_mom_roc_lvl_252d},
    "mrrs_104_rs_mom_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_104_rs_mom_roc_zscore_252d},
    "mrrs_105_rs_mom_roc_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_105_rs_mom_roc_rank_252d},
    "mrrs_106_rs_abs_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_106_rs_abs_lvl_5d},
    "mrrs_107_rs_abs_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_107_rs_abs_zscore_5d},
    "mrrs_108_rs_abs_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_108_rs_abs_rank_5d},
    "mrrs_109_rs_abs_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_109_rs_abs_lvl_21d},
    "mrrs_110_rs_abs_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_110_rs_abs_zscore_21d},
    "mrrs_111_rs_abs_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_111_rs_abs_rank_21d},
    "mrrs_112_rs_abs_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_112_rs_abs_lvl_63d},
    "mrrs_113_rs_abs_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_113_rs_abs_zscore_63d},
    "mrrs_114_rs_abs_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_114_rs_abs_rank_63d},
    "mrrs_115_rs_abs_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_115_rs_abs_lvl_126d},
    "mrrs_116_rs_abs_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_116_rs_abs_zscore_126d},
    "mrrs_117_rs_abs_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_117_rs_abs_rank_126d},
    "mrrs_118_rs_abs_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_118_rs_abs_lvl_252d},
    "mrrs_119_rs_abs_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_119_rs_abs_zscore_252d},
    "mrrs_120_rs_abs_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_120_rs_abs_rank_252d},
    "mrrs_121_rs_sig_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_121_rs_sig_lvl_5d},
    "mrrs_122_rs_sig_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_122_rs_sig_zscore_5d},
    "mrrs_123_rs_sig_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_123_rs_sig_rank_5d},
    "mrrs_124_rs_sig_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_124_rs_sig_lvl_21d},
    "mrrs_125_rs_sig_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_125_rs_sig_zscore_21d},
    "mrrs_126_rs_sig_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_126_rs_sig_rank_21d},
    "mrrs_127_rs_sig_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_127_rs_sig_lvl_63d},
    "mrrs_128_rs_sig_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_128_rs_sig_zscore_63d},
    "mrrs_129_rs_sig_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_129_rs_sig_rank_63d},
    "mrrs_130_rs_sig_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_130_rs_sig_lvl_126d},
    "mrrs_131_rs_sig_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_131_rs_sig_zscore_126d},
    "mrrs_132_rs_sig_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_132_rs_sig_rank_126d},
    "mrrs_133_rs_sig_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_133_rs_sig_lvl_252d},
    "mrrs_134_rs_sig_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_134_rs_sig_zscore_252d},
    "mrrs_135_rs_sig_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_135_rs_sig_rank_252d},
    "mrrs_136_rs_dist_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_136_rs_dist_lvl_5d},
    "mrrs_137_rs_dist_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_137_rs_dist_zscore_5d},
    "mrrs_138_rs_dist_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_138_rs_dist_rank_5d},
    "mrrs_139_rs_dist_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_139_rs_dist_lvl_21d},
    "mrrs_140_rs_dist_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_140_rs_dist_zscore_21d},
    "mrrs_141_rs_dist_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_141_rs_dist_rank_21d},
    "mrrs_142_rs_dist_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_142_rs_dist_lvl_63d},
    "mrrs_143_rs_dist_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_143_rs_dist_zscore_63d},
    "mrrs_144_rs_dist_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_144_rs_dist_rank_63d},
    "mrrs_145_rs_dist_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_145_rs_dist_lvl_126d},
    "mrrs_146_rs_dist_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_146_rs_dist_zscore_126d},
    "mrrs_147_rs_dist_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_147_rs_dist_rank_126d},
    "mrrs_148_rs_dist_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_148_rs_dist_lvl_252d},
    "mrrs_149_rs_dist_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_149_rs_dist_zscore_252d},
    "mrrs_150_rs_dist_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_150_rs_dist_rank_252d},
}
