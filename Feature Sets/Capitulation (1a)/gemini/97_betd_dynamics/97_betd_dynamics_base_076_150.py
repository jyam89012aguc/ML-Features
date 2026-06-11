"""
97_betd_dynamics — Base Features 076-150
Domain: betd_dynamics
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

def betd_076_beta_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_076_beta_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 252)
    return _rolling_mean(base, 5)

def betd_077_beta_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_077_beta_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 252)
    return _zscore_rolling(base, 5)

def betd_078_beta_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_078_beta_z_rank_5d"""
    base = _zscore_rolling(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 252)
    return _rank_pct(base, 5)

def betd_079_beta_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_079_beta_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 252)
    return _rolling_mean(base, 21)

def betd_080_beta_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_080_beta_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 252)
    return _zscore_rolling(base, 21)

def betd_081_beta_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_081_beta_z_rank_21d"""
    base = _zscore_rolling(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 252)
    return _rank_pct(base, 21)

def betd_082_beta_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_082_beta_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 252)
    return _rolling_mean(base, 63)

def betd_083_beta_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_083_beta_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 252)
    return _zscore_rolling(base, 63)

def betd_084_beta_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_084_beta_z_rank_63d"""
    base = _zscore_rolling(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 252)
    return _rank_pct(base, 63)

def betd_085_beta_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_085_beta_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 252)
    return _rolling_mean(base, 126)

def betd_086_beta_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_086_beta_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 252)
    return _zscore_rolling(base, 126)

def betd_087_beta_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_087_beta_z_rank_126d"""
    base = _zscore_rolling(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 252)
    return _rank_pct(base, 126)

def betd_088_beta_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_088_beta_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 252)
    return _rolling_mean(base, 252)

def betd_089_beta_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_089_beta_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 252)
    return _zscore_rolling(base, 252)

def betd_090_beta_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_090_beta_z_rank_252d"""
    base = _zscore_rolling(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 252)
    return _rank_pct(base, 252)

def betd_091_beta_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_091_beta_roc_lvl_5d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).pct_change()
    return _rolling_mean(base, 5)

def betd_092_beta_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_092_beta_roc_zscore_5d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).pct_change()
    return _zscore_rolling(base, 5)

def betd_093_beta_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_093_beta_roc_rank_5d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).pct_change()
    return _rank_pct(base, 5)

def betd_094_beta_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_094_beta_roc_lvl_21d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).pct_change()
    return _rolling_mean(base, 21)

def betd_095_beta_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_095_beta_roc_zscore_21d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).pct_change()
    return _zscore_rolling(base, 21)

def betd_096_beta_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_096_beta_roc_rank_21d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).pct_change()
    return _rank_pct(base, 21)

def betd_097_beta_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_097_beta_roc_lvl_63d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).pct_change()
    return _rolling_mean(base, 63)

def betd_098_beta_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_098_beta_roc_zscore_63d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).pct_change()
    return _zscore_rolling(base, 63)

def betd_099_beta_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_099_beta_roc_rank_63d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).pct_change()
    return _rank_pct(base, 63)

def betd_100_beta_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_100_beta_roc_lvl_126d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).pct_change()
    return _rolling_mean(base, 126)

def betd_101_beta_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_101_beta_roc_zscore_126d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).pct_change()
    return _zscore_rolling(base, 126)

def betd_102_beta_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_102_beta_roc_rank_126d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).pct_change()
    return _rank_pct(base, 126)

def betd_103_beta_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_103_beta_roc_lvl_252d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).pct_change()
    return _rolling_mean(base, 252)

def betd_104_beta_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_104_beta_roc_zscore_252d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).pct_change()
    return _zscore_rolling(base, 252)

def betd_105_beta_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_105_beta_roc_rank_252d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).pct_change()
    return _rank_pct(base, 252)

def betd_106_beta_abs_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_106_beta_abs_lvl_5d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).abs()
    return _rolling_mean(base, 5)

def betd_107_beta_abs_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_107_beta_abs_zscore_5d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).abs()
    return _zscore_rolling(base, 5)

def betd_108_beta_abs_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_108_beta_abs_rank_5d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).abs()
    return _rank_pct(base, 5)

def betd_109_beta_abs_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_109_beta_abs_lvl_21d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).abs()
    return _rolling_mean(base, 21)

def betd_110_beta_abs_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_110_beta_abs_zscore_21d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).abs()
    return _zscore_rolling(base, 21)

def betd_111_beta_abs_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_111_beta_abs_rank_21d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).abs()
    return _rank_pct(base, 21)

def betd_112_beta_abs_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_112_beta_abs_lvl_63d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).abs()
    return _rolling_mean(base, 63)

def betd_113_beta_abs_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_113_beta_abs_zscore_63d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).abs()
    return _zscore_rolling(base, 63)

def betd_114_beta_abs_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_114_beta_abs_rank_63d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).abs()
    return _rank_pct(base, 63)

def betd_115_beta_abs_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_115_beta_abs_lvl_126d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).abs()
    return _rolling_mean(base, 126)

def betd_116_beta_abs_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_116_beta_abs_zscore_126d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).abs()
    return _zscore_rolling(base, 126)

def betd_117_beta_abs_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_117_beta_abs_rank_126d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).abs()
    return _rank_pct(base, 126)

def betd_118_beta_abs_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_118_beta_abs_lvl_252d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).abs()
    return _rolling_mean(base, 252)

def betd_119_beta_abs_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_119_beta_abs_zscore_252d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).abs()
    return _zscore_rolling(base, 252)

def betd_120_beta_abs_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_120_beta_abs_rank_252d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()).abs()
    return _rank_pct(base, 252)

def betd_121_beta_sig_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_121_beta_sig_lvl_5d"""
    base = _rolling_mean(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 5)
    return _rolling_mean(base, 5)

def betd_122_beta_sig_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_122_beta_sig_zscore_5d"""
    base = _rolling_mean(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 5)
    return _zscore_rolling(base, 5)

def betd_123_beta_sig_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_123_beta_sig_rank_5d"""
    base = _rolling_mean(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 5)
    return _rank_pct(base, 5)

def betd_124_beta_sig_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_124_beta_sig_lvl_21d"""
    base = _rolling_mean(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 5)
    return _rolling_mean(base, 21)

def betd_125_beta_sig_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_125_beta_sig_zscore_21d"""
    base = _rolling_mean(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 5)
    return _zscore_rolling(base, 21)

def betd_126_beta_sig_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_126_beta_sig_rank_21d"""
    base = _rolling_mean(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 5)
    return _rank_pct(base, 21)

def betd_127_beta_sig_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_127_beta_sig_lvl_63d"""
    base = _rolling_mean(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 5)
    return _rolling_mean(base, 63)

def betd_128_beta_sig_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_128_beta_sig_zscore_63d"""
    base = _rolling_mean(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 5)
    return _zscore_rolling(base, 63)

def betd_129_beta_sig_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_129_beta_sig_rank_63d"""
    base = _rolling_mean(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 5)
    return _rank_pct(base, 63)

def betd_130_beta_sig_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_130_beta_sig_lvl_126d"""
    base = _rolling_mean(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 5)
    return _rolling_mean(base, 126)

def betd_131_beta_sig_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_131_beta_sig_zscore_126d"""
    base = _rolling_mean(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 5)
    return _zscore_rolling(base, 126)

def betd_132_beta_sig_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_132_beta_sig_rank_126d"""
    base = _rolling_mean(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 5)
    return _rank_pct(base, 126)

def betd_133_beta_sig_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_133_beta_sig_lvl_252d"""
    base = _rolling_mean(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 5)
    return _rolling_mean(base, 252)

def betd_134_beta_sig_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_134_beta_sig_zscore_252d"""
    base = _rolling_mean(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 5)
    return _zscore_rolling(base, 252)

def betd_135_beta_sig_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_135_beta_sig_rank_252d"""
    base = _rolling_mean(_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()), 5)
    return _rank_pct(base, 252)

def betd_136_beta_dist_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_136_beta_dist_lvl_5d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) - 1.0
    return _rolling_mean(base, 5)

def betd_137_beta_dist_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_137_beta_dist_zscore_5d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) - 1.0
    return _zscore_rolling(base, 5)

def betd_138_beta_dist_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_138_beta_dist_rank_5d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) - 1.0
    return _rank_pct(base, 5)

def betd_139_beta_dist_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_139_beta_dist_lvl_21d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) - 1.0
    return _rolling_mean(base, 21)

def betd_140_beta_dist_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_140_beta_dist_zscore_21d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) - 1.0
    return _zscore_rolling(base, 21)

def betd_141_beta_dist_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_141_beta_dist_rank_21d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) - 1.0
    return _rank_pct(base, 21)

def betd_142_beta_dist_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_142_beta_dist_lvl_63d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) - 1.0
    return _rolling_mean(base, 63)

def betd_143_beta_dist_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_143_beta_dist_zscore_63d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) - 1.0
    return _zscore_rolling(base, 63)

def betd_144_beta_dist_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_144_beta_dist_rank_63d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) - 1.0
    return _rank_pct(base, 63)

def betd_145_beta_dist_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_145_beta_dist_lvl_126d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) - 1.0
    return _rolling_mean(base, 126)

def betd_146_beta_dist_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_146_beta_dist_zscore_126d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) - 1.0
    return _zscore_rolling(base, 126)

def betd_147_beta_dist_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_147_beta_dist_rank_126d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) - 1.0
    return _rank_pct(base, 126)

def betd_148_beta_dist_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_148_beta_dist_lvl_252d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) - 1.0
    return _rolling_mean(base, 252)

def betd_149_beta_dist_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_149_beta_dist_zscore_252d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) - 1.0
    return _zscore_rolling(base, 252)

def betd_150_beta_dist_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_150_beta_dist_rank_252d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) - 1.0
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V97_REGISTRY_2 = {
    "betd_076_beta_z_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_076_beta_z_lvl_5d},
    "betd_077_beta_z_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_077_beta_z_zscore_5d},
    "betd_078_beta_z_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_078_beta_z_rank_5d},
    "betd_079_beta_z_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_079_beta_z_lvl_21d},
    "betd_080_beta_z_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_080_beta_z_zscore_21d},
    "betd_081_beta_z_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_081_beta_z_rank_21d},
    "betd_082_beta_z_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_082_beta_z_lvl_63d},
    "betd_083_beta_z_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_083_beta_z_zscore_63d},
    "betd_084_beta_z_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_084_beta_z_rank_63d},
    "betd_085_beta_z_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_085_beta_z_lvl_126d},
    "betd_086_beta_z_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_086_beta_z_zscore_126d},
    "betd_087_beta_z_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_087_beta_z_rank_126d},
    "betd_088_beta_z_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_088_beta_z_lvl_252d},
    "betd_089_beta_z_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_089_beta_z_zscore_252d},
    "betd_090_beta_z_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_090_beta_z_rank_252d},
    "betd_091_beta_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_091_beta_roc_lvl_5d},
    "betd_092_beta_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_092_beta_roc_zscore_5d},
    "betd_093_beta_roc_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_093_beta_roc_rank_5d},
    "betd_094_beta_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_094_beta_roc_lvl_21d},
    "betd_095_beta_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_095_beta_roc_zscore_21d},
    "betd_096_beta_roc_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_096_beta_roc_rank_21d},
    "betd_097_beta_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_097_beta_roc_lvl_63d},
    "betd_098_beta_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_098_beta_roc_zscore_63d},
    "betd_099_beta_roc_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_099_beta_roc_rank_63d},
    "betd_100_beta_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_100_beta_roc_lvl_126d},
    "betd_101_beta_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_101_beta_roc_zscore_126d},
    "betd_102_beta_roc_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_102_beta_roc_rank_126d},
    "betd_103_beta_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_103_beta_roc_lvl_252d},
    "betd_104_beta_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_104_beta_roc_zscore_252d},
    "betd_105_beta_roc_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_105_beta_roc_rank_252d},
    "betd_106_beta_abs_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_106_beta_abs_lvl_5d},
    "betd_107_beta_abs_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_107_beta_abs_zscore_5d},
    "betd_108_beta_abs_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_108_beta_abs_rank_5d},
    "betd_109_beta_abs_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_109_beta_abs_lvl_21d},
    "betd_110_beta_abs_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_110_beta_abs_zscore_21d},
    "betd_111_beta_abs_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_111_beta_abs_rank_21d},
    "betd_112_beta_abs_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_112_beta_abs_lvl_63d},
    "betd_113_beta_abs_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_113_beta_abs_zscore_63d},
    "betd_114_beta_abs_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_114_beta_abs_rank_63d},
    "betd_115_beta_abs_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_115_beta_abs_lvl_126d},
    "betd_116_beta_abs_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_116_beta_abs_zscore_126d},
    "betd_117_beta_abs_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_117_beta_abs_rank_126d},
    "betd_118_beta_abs_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_118_beta_abs_lvl_252d},
    "betd_119_beta_abs_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_119_beta_abs_zscore_252d},
    "betd_120_beta_abs_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_120_beta_abs_rank_252d},
    "betd_121_beta_sig_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_121_beta_sig_lvl_5d},
    "betd_122_beta_sig_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_122_beta_sig_zscore_5d},
    "betd_123_beta_sig_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_123_beta_sig_rank_5d},
    "betd_124_beta_sig_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_124_beta_sig_lvl_21d},
    "betd_125_beta_sig_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_125_beta_sig_zscore_21d},
    "betd_126_beta_sig_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_126_beta_sig_rank_21d},
    "betd_127_beta_sig_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_127_beta_sig_lvl_63d},
    "betd_128_beta_sig_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_128_beta_sig_zscore_63d},
    "betd_129_beta_sig_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_129_beta_sig_rank_63d},
    "betd_130_beta_sig_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_130_beta_sig_lvl_126d},
    "betd_131_beta_sig_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_131_beta_sig_zscore_126d},
    "betd_132_beta_sig_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_132_beta_sig_rank_126d},
    "betd_133_beta_sig_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_133_beta_sig_lvl_252d},
    "betd_134_beta_sig_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_134_beta_sig_zscore_252d},
    "betd_135_beta_sig_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_135_beta_sig_rank_252d},
    "betd_136_beta_dist_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_136_beta_dist_lvl_5d},
    "betd_137_beta_dist_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_137_beta_dist_zscore_5d},
    "betd_138_beta_dist_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_138_beta_dist_rank_5d},
    "betd_139_beta_dist_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_139_beta_dist_lvl_21d},
    "betd_140_beta_dist_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_140_beta_dist_zscore_21d},
    "betd_141_beta_dist_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_141_beta_dist_rank_21d},
    "betd_142_beta_dist_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_142_beta_dist_lvl_63d},
    "betd_143_beta_dist_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_143_beta_dist_zscore_63d},
    "betd_144_beta_dist_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_144_beta_dist_rank_63d},
    "betd_145_beta_dist_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_145_beta_dist_lvl_126d},
    "betd_146_beta_dist_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_146_beta_dist_zscore_126d},
    "betd_147_beta_dist_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_147_beta_dist_rank_126d},
    "betd_148_beta_dist_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_148_beta_dist_lvl_252d},
    "betd_149_beta_dist_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_149_beta_dist_zscore_252d},
    "betd_150_beta_dist_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_150_beta_dist_rank_252d},
}
