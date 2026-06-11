"""
94_aroo_dynamics — Base Features 076-150
Domain: aroo_dynamics
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

def aroo_076_aroo_up_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_076_aroo_up_roc_lvl_5d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).pct_change()
    return _rolling_mean(base, 5)

def aroo_077_aroo_up_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_077_aroo_up_roc_zscore_5d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).pct_change()
    return _zscore_rolling(base, 5)

def aroo_078_aroo_up_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_078_aroo_up_roc_rank_5d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).pct_change()
    return _rank_pct(base, 5)

def aroo_079_aroo_up_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_079_aroo_up_roc_lvl_21d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).pct_change()
    return _rolling_mean(base, 21)

def aroo_080_aroo_up_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_080_aroo_up_roc_zscore_21d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).pct_change()
    return _zscore_rolling(base, 21)

def aroo_081_aroo_up_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_081_aroo_up_roc_rank_21d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).pct_change()
    return _rank_pct(base, 21)

def aroo_082_aroo_up_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_082_aroo_up_roc_lvl_63d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).pct_change()
    return _rolling_mean(base, 63)

def aroo_083_aroo_up_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_083_aroo_up_roc_zscore_63d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).pct_change()
    return _zscore_rolling(base, 63)

def aroo_084_aroo_up_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_084_aroo_up_roc_rank_63d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).pct_change()
    return _rank_pct(base, 63)

def aroo_085_aroo_up_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_085_aroo_up_roc_lvl_126d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).pct_change()
    return _rolling_mean(base, 126)

def aroo_086_aroo_up_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_086_aroo_up_roc_zscore_126d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).pct_change()
    return _zscore_rolling(base, 126)

def aroo_087_aroo_up_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_087_aroo_up_roc_rank_126d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).pct_change()
    return _rank_pct(base, 126)

def aroo_088_aroo_up_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_088_aroo_up_roc_lvl_252d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).pct_change()
    return _rolling_mean(base, 252)

def aroo_089_aroo_up_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_089_aroo_up_roc_zscore_252d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).pct_change()
    return _zscore_rolling(base, 252)

def aroo_090_aroo_up_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_090_aroo_up_roc_rank_252d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).pct_change()
    return _rank_pct(base, 252)

def aroo_091_aroo_dn_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_091_aroo_dn_roc_lvl_5d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rolling_mean(base, 5)

def aroo_092_aroo_dn_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_092_aroo_dn_roc_zscore_5d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _zscore_rolling(base, 5)

def aroo_093_aroo_dn_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_093_aroo_dn_roc_rank_5d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rank_pct(base, 5)

def aroo_094_aroo_dn_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_094_aroo_dn_roc_lvl_21d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rolling_mean(base, 21)

def aroo_095_aroo_dn_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_095_aroo_dn_roc_zscore_21d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _zscore_rolling(base, 21)

def aroo_096_aroo_dn_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_096_aroo_dn_roc_rank_21d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rank_pct(base, 21)

def aroo_097_aroo_dn_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_097_aroo_dn_roc_lvl_63d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rolling_mean(base, 63)

def aroo_098_aroo_dn_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_098_aroo_dn_roc_zscore_63d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _zscore_rolling(base, 63)

def aroo_099_aroo_dn_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_099_aroo_dn_roc_rank_63d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rank_pct(base, 63)

def aroo_100_aroo_dn_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_100_aroo_dn_roc_lvl_126d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rolling_mean(base, 126)

def aroo_101_aroo_dn_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_101_aroo_dn_roc_zscore_126d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _zscore_rolling(base, 126)

def aroo_102_aroo_dn_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_102_aroo_dn_roc_rank_126d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rank_pct(base, 126)

def aroo_103_aroo_dn_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_103_aroo_dn_roc_lvl_252d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rolling_mean(base, 252)

def aroo_104_aroo_dn_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_104_aroo_dn_roc_zscore_252d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _zscore_rolling(base, 252)

def aroo_105_aroo_dn_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_105_aroo_dn_roc_rank_252d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rank_pct(base, 252)

def aroo_106_aroo_abs_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_106_aroo_abs_lvl_5d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).abs()
    return _rolling_mean(base, 5)

def aroo_107_aroo_abs_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_107_aroo_abs_zscore_5d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).abs()
    return _zscore_rolling(base, 5)

def aroo_108_aroo_abs_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_108_aroo_abs_rank_5d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).abs()
    return _rank_pct(base, 5)

def aroo_109_aroo_abs_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_109_aroo_abs_lvl_21d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).abs()
    return _rolling_mean(base, 21)

def aroo_110_aroo_abs_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_110_aroo_abs_zscore_21d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).abs()
    return _zscore_rolling(base, 21)

def aroo_111_aroo_abs_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_111_aroo_abs_rank_21d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).abs()
    return _rank_pct(base, 21)

def aroo_112_aroo_abs_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_112_aroo_abs_lvl_63d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).abs()
    return _rolling_mean(base, 63)

def aroo_113_aroo_abs_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_113_aroo_abs_zscore_63d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).abs()
    return _zscore_rolling(base, 63)

def aroo_114_aroo_abs_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_114_aroo_abs_rank_63d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).abs()
    return _rank_pct(base, 63)

def aroo_115_aroo_abs_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_115_aroo_abs_lvl_126d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).abs()
    return _rolling_mean(base, 126)

def aroo_116_aroo_abs_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_116_aroo_abs_zscore_126d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).abs()
    return _zscore_rolling(base, 126)

def aroo_117_aroo_abs_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_117_aroo_abs_rank_126d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).abs()
    return _rank_pct(base, 126)

def aroo_118_aroo_abs_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_118_aroo_abs_lvl_252d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).abs()
    return _rolling_mean(base, 252)

def aroo_119_aroo_abs_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_119_aroo_abs_zscore_252d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).abs()
    return _zscore_rolling(base, 252)

def aroo_120_aroo_abs_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_120_aroo_abs_rank_252d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).abs()
    return _rank_pct(base, 252)

def aroo_121_aroo_sig_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_121_aroo_sig_lvl_5d"""
    base = _rolling_mean(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 5)
    return _rolling_mean(base, 5)

def aroo_122_aroo_sig_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_122_aroo_sig_zscore_5d"""
    base = _rolling_mean(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 5)
    return _zscore_rolling(base, 5)

def aroo_123_aroo_sig_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_123_aroo_sig_rank_5d"""
    base = _rolling_mean(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 5)
    return _rank_pct(base, 5)

def aroo_124_aroo_sig_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_124_aroo_sig_lvl_21d"""
    base = _rolling_mean(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 5)
    return _rolling_mean(base, 21)

def aroo_125_aroo_sig_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_125_aroo_sig_zscore_21d"""
    base = _rolling_mean(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 5)
    return _zscore_rolling(base, 21)

def aroo_126_aroo_sig_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_126_aroo_sig_rank_21d"""
    base = _rolling_mean(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 5)
    return _rank_pct(base, 21)

def aroo_127_aroo_sig_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_127_aroo_sig_lvl_63d"""
    base = _rolling_mean(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 5)
    return _rolling_mean(base, 63)

def aroo_128_aroo_sig_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_128_aroo_sig_zscore_63d"""
    base = _rolling_mean(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 5)
    return _zscore_rolling(base, 63)

def aroo_129_aroo_sig_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_129_aroo_sig_rank_63d"""
    base = _rolling_mean(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 5)
    return _rank_pct(base, 63)

def aroo_130_aroo_sig_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_130_aroo_sig_lvl_126d"""
    base = _rolling_mean(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 5)
    return _rolling_mean(base, 126)

def aroo_131_aroo_sig_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_131_aroo_sig_zscore_126d"""
    base = _rolling_mean(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 5)
    return _zscore_rolling(base, 126)

def aroo_132_aroo_sig_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_132_aroo_sig_rank_126d"""
    base = _rolling_mean(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 5)
    return _rank_pct(base, 126)

def aroo_133_aroo_sig_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_133_aroo_sig_lvl_252d"""
    base = _rolling_mean(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 5)
    return _rolling_mean(base, 252)

def aroo_134_aroo_sig_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_134_aroo_sig_zscore_252d"""
    base = _rolling_mean(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 5)
    return _zscore_rolling(base, 252)

def aroo_135_aroo_sig_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_135_aroo_sig_rank_252d"""
    base = _rolling_mean(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 5)
    return _rank_pct(base, 252)

def aroo_136_aroo_dist_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_136_aroo_dist_lvl_5d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 50
    return _rolling_mean(base, 5)

def aroo_137_aroo_dist_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_137_aroo_dist_zscore_5d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 50
    return _zscore_rolling(base, 5)

def aroo_138_aroo_dist_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_138_aroo_dist_rank_5d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 50
    return _rank_pct(base, 5)

def aroo_139_aroo_dist_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_139_aroo_dist_lvl_21d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 50
    return _rolling_mean(base, 21)

def aroo_140_aroo_dist_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_140_aroo_dist_zscore_21d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 50
    return _zscore_rolling(base, 21)

def aroo_141_aroo_dist_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_141_aroo_dist_rank_21d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 50
    return _rank_pct(base, 21)

def aroo_142_aroo_dist_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_142_aroo_dist_lvl_63d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 50
    return _rolling_mean(base, 63)

def aroo_143_aroo_dist_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_143_aroo_dist_zscore_63d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 50
    return _zscore_rolling(base, 63)

def aroo_144_aroo_dist_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_144_aroo_dist_rank_63d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 50
    return _rank_pct(base, 63)

def aroo_145_aroo_dist_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_145_aroo_dist_lvl_126d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 50
    return _rolling_mean(base, 126)

def aroo_146_aroo_dist_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_146_aroo_dist_zscore_126d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 50
    return _zscore_rolling(base, 126)

def aroo_147_aroo_dist_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_147_aroo_dist_rank_126d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 50
    return _rank_pct(base, 126)

def aroo_148_aroo_dist_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_148_aroo_dist_lvl_252d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 50
    return _rolling_mean(base, 252)

def aroo_149_aroo_dist_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_149_aroo_dist_zscore_252d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 50
    return _zscore_rolling(base, 252)

def aroo_150_aroo_dist_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_150_aroo_dist_rank_252d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 50
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V94_REGISTRY_2 = {
    "aroo_076_aroo_up_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_076_aroo_up_roc_lvl_5d},
    "aroo_077_aroo_up_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_077_aroo_up_roc_zscore_5d},
    "aroo_078_aroo_up_roc_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_078_aroo_up_roc_rank_5d},
    "aroo_079_aroo_up_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_079_aroo_up_roc_lvl_21d},
    "aroo_080_aroo_up_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_080_aroo_up_roc_zscore_21d},
    "aroo_081_aroo_up_roc_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_081_aroo_up_roc_rank_21d},
    "aroo_082_aroo_up_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_082_aroo_up_roc_lvl_63d},
    "aroo_083_aroo_up_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_083_aroo_up_roc_zscore_63d},
    "aroo_084_aroo_up_roc_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_084_aroo_up_roc_rank_63d},
    "aroo_085_aroo_up_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_085_aroo_up_roc_lvl_126d},
    "aroo_086_aroo_up_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_086_aroo_up_roc_zscore_126d},
    "aroo_087_aroo_up_roc_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_087_aroo_up_roc_rank_126d},
    "aroo_088_aroo_up_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_088_aroo_up_roc_lvl_252d},
    "aroo_089_aroo_up_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_089_aroo_up_roc_zscore_252d},
    "aroo_090_aroo_up_roc_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_090_aroo_up_roc_rank_252d},
    "aroo_091_aroo_dn_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_091_aroo_dn_roc_lvl_5d},
    "aroo_092_aroo_dn_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_092_aroo_dn_roc_zscore_5d},
    "aroo_093_aroo_dn_roc_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_093_aroo_dn_roc_rank_5d},
    "aroo_094_aroo_dn_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_094_aroo_dn_roc_lvl_21d},
    "aroo_095_aroo_dn_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_095_aroo_dn_roc_zscore_21d},
    "aroo_096_aroo_dn_roc_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_096_aroo_dn_roc_rank_21d},
    "aroo_097_aroo_dn_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_097_aroo_dn_roc_lvl_63d},
    "aroo_098_aroo_dn_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_098_aroo_dn_roc_zscore_63d},
    "aroo_099_aroo_dn_roc_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_099_aroo_dn_roc_rank_63d},
    "aroo_100_aroo_dn_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_100_aroo_dn_roc_lvl_126d},
    "aroo_101_aroo_dn_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_101_aroo_dn_roc_zscore_126d},
    "aroo_102_aroo_dn_roc_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_102_aroo_dn_roc_rank_126d},
    "aroo_103_aroo_dn_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_103_aroo_dn_roc_lvl_252d},
    "aroo_104_aroo_dn_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_104_aroo_dn_roc_zscore_252d},
    "aroo_105_aroo_dn_roc_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_105_aroo_dn_roc_rank_252d},
    "aroo_106_aroo_abs_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_106_aroo_abs_lvl_5d},
    "aroo_107_aroo_abs_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_107_aroo_abs_zscore_5d},
    "aroo_108_aroo_abs_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_108_aroo_abs_rank_5d},
    "aroo_109_aroo_abs_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_109_aroo_abs_lvl_21d},
    "aroo_110_aroo_abs_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_110_aroo_abs_zscore_21d},
    "aroo_111_aroo_abs_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_111_aroo_abs_rank_21d},
    "aroo_112_aroo_abs_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_112_aroo_abs_lvl_63d},
    "aroo_113_aroo_abs_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_113_aroo_abs_zscore_63d},
    "aroo_114_aroo_abs_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_114_aroo_abs_rank_63d},
    "aroo_115_aroo_abs_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_115_aroo_abs_lvl_126d},
    "aroo_116_aroo_abs_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_116_aroo_abs_zscore_126d},
    "aroo_117_aroo_abs_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_117_aroo_abs_rank_126d},
    "aroo_118_aroo_abs_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_118_aroo_abs_lvl_252d},
    "aroo_119_aroo_abs_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_119_aroo_abs_zscore_252d},
    "aroo_120_aroo_abs_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_120_aroo_abs_rank_252d},
    "aroo_121_aroo_sig_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_121_aroo_sig_lvl_5d},
    "aroo_122_aroo_sig_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_122_aroo_sig_zscore_5d},
    "aroo_123_aroo_sig_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_123_aroo_sig_rank_5d},
    "aroo_124_aroo_sig_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_124_aroo_sig_lvl_21d},
    "aroo_125_aroo_sig_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_125_aroo_sig_zscore_21d},
    "aroo_126_aroo_sig_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_126_aroo_sig_rank_21d},
    "aroo_127_aroo_sig_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_127_aroo_sig_lvl_63d},
    "aroo_128_aroo_sig_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_128_aroo_sig_zscore_63d},
    "aroo_129_aroo_sig_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_129_aroo_sig_rank_63d},
    "aroo_130_aroo_sig_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_130_aroo_sig_lvl_126d},
    "aroo_131_aroo_sig_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_131_aroo_sig_zscore_126d},
    "aroo_132_aroo_sig_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_132_aroo_sig_rank_126d},
    "aroo_133_aroo_sig_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_133_aroo_sig_lvl_252d},
    "aroo_134_aroo_sig_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_134_aroo_sig_zscore_252d},
    "aroo_135_aroo_sig_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_135_aroo_sig_rank_252d},
    "aroo_136_aroo_dist_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_136_aroo_dist_lvl_5d},
    "aroo_137_aroo_dist_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_137_aroo_dist_zscore_5d},
    "aroo_138_aroo_dist_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_138_aroo_dist_rank_5d},
    "aroo_139_aroo_dist_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_139_aroo_dist_lvl_21d},
    "aroo_140_aroo_dist_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_140_aroo_dist_zscore_21d},
    "aroo_141_aroo_dist_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_141_aroo_dist_rank_21d},
    "aroo_142_aroo_dist_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_142_aroo_dist_lvl_63d},
    "aroo_143_aroo_dist_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_143_aroo_dist_zscore_63d},
    "aroo_144_aroo_dist_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_144_aroo_dist_rank_63d},
    "aroo_145_aroo_dist_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_145_aroo_dist_lvl_126d},
    "aroo_146_aroo_dist_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_146_aroo_dist_zscore_126d},
    "aroo_147_aroo_dist_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_147_aroo_dist_rank_126d},
    "aroo_148_aroo_dist_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_148_aroo_dist_lvl_252d},
    "aroo_149_aroo_dist_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_149_aroo_dist_zscore_252d},
    "aroo_150_aroo_dist_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_150_aroo_dist_rank_252d},
}
