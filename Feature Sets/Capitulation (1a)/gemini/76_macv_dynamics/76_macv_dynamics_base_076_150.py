"""
76_macv_dynamics — Base Features 076-150
Domain: macv_dynamics
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

def macv_076_hist_z_lvl_5d(close: pd.Series) -> pd.Series:
    """macv_076_hist_z_lvl_5d"""
    base = _zscore_rolling((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9), 63)
    return _rolling_mean(base, 5)

def macv_077_hist_z_zscore_5d(close: pd.Series) -> pd.Series:
    """macv_077_hist_z_zscore_5d"""
    base = _zscore_rolling((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9), 63)
    return _zscore_rolling(base, 5)

def macv_078_hist_z_rank_5d(close: pd.Series) -> pd.Series:
    """macv_078_hist_z_rank_5d"""
    base = _zscore_rolling((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9), 63)
    return _rank_pct(base, 5)

def macv_079_hist_z_lvl_21d(close: pd.Series) -> pd.Series:
    """macv_079_hist_z_lvl_21d"""
    base = _zscore_rolling((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9), 63)
    return _rolling_mean(base, 21)

def macv_080_hist_z_zscore_21d(close: pd.Series) -> pd.Series:
    """macv_080_hist_z_zscore_21d"""
    base = _zscore_rolling((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9), 63)
    return _zscore_rolling(base, 21)

def macv_081_hist_z_rank_21d(close: pd.Series) -> pd.Series:
    """macv_081_hist_z_rank_21d"""
    base = _zscore_rolling((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9), 63)
    return _rank_pct(base, 21)

def macv_082_hist_z_lvl_63d(close: pd.Series) -> pd.Series:
    """macv_082_hist_z_lvl_63d"""
    base = _zscore_rolling((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9), 63)
    return _rolling_mean(base, 63)

def macv_083_hist_z_zscore_63d(close: pd.Series) -> pd.Series:
    """macv_083_hist_z_zscore_63d"""
    base = _zscore_rolling((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9), 63)
    return _zscore_rolling(base, 63)

def macv_084_hist_z_rank_63d(close: pd.Series) -> pd.Series:
    """macv_084_hist_z_rank_63d"""
    base = _zscore_rolling((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9), 63)
    return _rank_pct(base, 63)

def macv_085_hist_z_lvl_126d(close: pd.Series) -> pd.Series:
    """macv_085_hist_z_lvl_126d"""
    base = _zscore_rolling((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9), 63)
    return _rolling_mean(base, 126)

def macv_086_hist_z_zscore_126d(close: pd.Series) -> pd.Series:
    """macv_086_hist_z_zscore_126d"""
    base = _zscore_rolling((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9), 63)
    return _zscore_rolling(base, 126)

def macv_087_hist_z_rank_126d(close: pd.Series) -> pd.Series:
    """macv_087_hist_z_rank_126d"""
    base = _zscore_rolling((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9), 63)
    return _rank_pct(base, 126)

def macv_088_hist_z_lvl_252d(close: pd.Series) -> pd.Series:
    """macv_088_hist_z_lvl_252d"""
    base = _zscore_rolling((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9), 63)
    return _rolling_mean(base, 252)

def macv_089_hist_z_zscore_252d(close: pd.Series) -> pd.Series:
    """macv_089_hist_z_zscore_252d"""
    base = _zscore_rolling((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9), 63)
    return _zscore_rolling(base, 252)

def macv_090_hist_z_rank_252d(close: pd.Series) -> pd.Series:
    """macv_090_hist_z_rank_252d"""
    base = _zscore_rolling((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9), 63)
    return _rank_pct(base, 252)

def macv_091_macd_fast_lvl_5d(close: pd.Series) -> pd.Series:
    """macv_091_macd_fast_lvl_5d"""
    base = _ewm_mean(close, 5) - _ewm_mean(close, 13)
    return _rolling_mean(base, 5)

def macv_092_macd_fast_zscore_5d(close: pd.Series) -> pd.Series:
    """macv_092_macd_fast_zscore_5d"""
    base = _ewm_mean(close, 5) - _ewm_mean(close, 13)
    return _zscore_rolling(base, 5)

def macv_093_macd_fast_rank_5d(close: pd.Series) -> pd.Series:
    """macv_093_macd_fast_rank_5d"""
    base = _ewm_mean(close, 5) - _ewm_mean(close, 13)
    return _rank_pct(base, 5)

def macv_094_macd_fast_lvl_21d(close: pd.Series) -> pd.Series:
    """macv_094_macd_fast_lvl_21d"""
    base = _ewm_mean(close, 5) - _ewm_mean(close, 13)
    return _rolling_mean(base, 21)

def macv_095_macd_fast_zscore_21d(close: pd.Series) -> pd.Series:
    """macv_095_macd_fast_zscore_21d"""
    base = _ewm_mean(close, 5) - _ewm_mean(close, 13)
    return _zscore_rolling(base, 21)

def macv_096_macd_fast_rank_21d(close: pd.Series) -> pd.Series:
    """macv_096_macd_fast_rank_21d"""
    base = _ewm_mean(close, 5) - _ewm_mean(close, 13)
    return _rank_pct(base, 21)

def macv_097_macd_fast_lvl_63d(close: pd.Series) -> pd.Series:
    """macv_097_macd_fast_lvl_63d"""
    base = _ewm_mean(close, 5) - _ewm_mean(close, 13)
    return _rolling_mean(base, 63)

def macv_098_macd_fast_zscore_63d(close: pd.Series) -> pd.Series:
    """macv_098_macd_fast_zscore_63d"""
    base = _ewm_mean(close, 5) - _ewm_mean(close, 13)
    return _zscore_rolling(base, 63)

def macv_099_macd_fast_rank_63d(close: pd.Series) -> pd.Series:
    """macv_099_macd_fast_rank_63d"""
    base = _ewm_mean(close, 5) - _ewm_mean(close, 13)
    return _rank_pct(base, 63)

def macv_100_macd_fast_lvl_126d(close: pd.Series) -> pd.Series:
    """macv_100_macd_fast_lvl_126d"""
    base = _ewm_mean(close, 5) - _ewm_mean(close, 13)
    return _rolling_mean(base, 126)

def macv_101_macd_fast_zscore_126d(close: pd.Series) -> pd.Series:
    """macv_101_macd_fast_zscore_126d"""
    base = _ewm_mean(close, 5) - _ewm_mean(close, 13)
    return _zscore_rolling(base, 126)

def macv_102_macd_fast_rank_126d(close: pd.Series) -> pd.Series:
    """macv_102_macd_fast_rank_126d"""
    base = _ewm_mean(close, 5) - _ewm_mean(close, 13)
    return _rank_pct(base, 126)

def macv_103_macd_fast_lvl_252d(close: pd.Series) -> pd.Series:
    """macv_103_macd_fast_lvl_252d"""
    base = _ewm_mean(close, 5) - _ewm_mean(close, 13)
    return _rolling_mean(base, 252)

def macv_104_macd_fast_zscore_252d(close: pd.Series) -> pd.Series:
    """macv_104_macd_fast_zscore_252d"""
    base = _ewm_mean(close, 5) - _ewm_mean(close, 13)
    return _zscore_rolling(base, 252)

def macv_105_macd_fast_rank_252d(close: pd.Series) -> pd.Series:
    """macv_105_macd_fast_rank_252d"""
    base = _ewm_mean(close, 5) - _ewm_mean(close, 13)
    return _rank_pct(base, 252)

def macv_106_macd_slow_lvl_5d(close: pd.Series) -> pd.Series:
    """macv_106_macd_slow_lvl_5d"""
    base = _ewm_mean(close, 24) - _ewm_mean(close, 52)
    return _rolling_mean(base, 5)

def macv_107_macd_slow_zscore_5d(close: pd.Series) -> pd.Series:
    """macv_107_macd_slow_zscore_5d"""
    base = _ewm_mean(close, 24) - _ewm_mean(close, 52)
    return _zscore_rolling(base, 5)

def macv_108_macd_slow_rank_5d(close: pd.Series) -> pd.Series:
    """macv_108_macd_slow_rank_5d"""
    base = _ewm_mean(close, 24) - _ewm_mean(close, 52)
    return _rank_pct(base, 5)

def macv_109_macd_slow_lvl_21d(close: pd.Series) -> pd.Series:
    """macv_109_macd_slow_lvl_21d"""
    base = _ewm_mean(close, 24) - _ewm_mean(close, 52)
    return _rolling_mean(base, 21)

def macv_110_macd_slow_zscore_21d(close: pd.Series) -> pd.Series:
    """macv_110_macd_slow_zscore_21d"""
    base = _ewm_mean(close, 24) - _ewm_mean(close, 52)
    return _zscore_rolling(base, 21)

def macv_111_macd_slow_rank_21d(close: pd.Series) -> pd.Series:
    """macv_111_macd_slow_rank_21d"""
    base = _ewm_mean(close, 24) - _ewm_mean(close, 52)
    return _rank_pct(base, 21)

def macv_112_macd_slow_lvl_63d(close: pd.Series) -> pd.Series:
    """macv_112_macd_slow_lvl_63d"""
    base = _ewm_mean(close, 24) - _ewm_mean(close, 52)
    return _rolling_mean(base, 63)

def macv_113_macd_slow_zscore_63d(close: pd.Series) -> pd.Series:
    """macv_113_macd_slow_zscore_63d"""
    base = _ewm_mean(close, 24) - _ewm_mean(close, 52)
    return _zscore_rolling(base, 63)

def macv_114_macd_slow_rank_63d(close: pd.Series) -> pd.Series:
    """macv_114_macd_slow_rank_63d"""
    base = _ewm_mean(close, 24) - _ewm_mean(close, 52)
    return _rank_pct(base, 63)

def macv_115_macd_slow_lvl_126d(close: pd.Series) -> pd.Series:
    """macv_115_macd_slow_lvl_126d"""
    base = _ewm_mean(close, 24) - _ewm_mean(close, 52)
    return _rolling_mean(base, 126)

def macv_116_macd_slow_zscore_126d(close: pd.Series) -> pd.Series:
    """macv_116_macd_slow_zscore_126d"""
    base = _ewm_mean(close, 24) - _ewm_mean(close, 52)
    return _zscore_rolling(base, 126)

def macv_117_macd_slow_rank_126d(close: pd.Series) -> pd.Series:
    """macv_117_macd_slow_rank_126d"""
    base = _ewm_mean(close, 24) - _ewm_mean(close, 52)
    return _rank_pct(base, 126)

def macv_118_macd_slow_lvl_252d(close: pd.Series) -> pd.Series:
    """macv_118_macd_slow_lvl_252d"""
    base = _ewm_mean(close, 24) - _ewm_mean(close, 52)
    return _rolling_mean(base, 252)

def macv_119_macd_slow_zscore_252d(close: pd.Series) -> pd.Series:
    """macv_119_macd_slow_zscore_252d"""
    base = _ewm_mean(close, 24) - _ewm_mean(close, 52)
    return _zscore_rolling(base, 252)

def macv_120_macd_slow_rank_252d(close: pd.Series) -> pd.Series:
    """macv_120_macd_slow_rank_252d"""
    base = _ewm_mean(close, 24) - _ewm_mean(close, 52)
    return _rank_pct(base, 252)

def macv_121_macd_slope_lvl_5d(close: pd.Series) -> pd.Series:
    """macv_121_macd_slope_lvl_5d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(5)
    return _rolling_mean(base, 5)

def macv_122_macd_slope_zscore_5d(close: pd.Series) -> pd.Series:
    """macv_122_macd_slope_zscore_5d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(5)
    return _zscore_rolling(base, 5)

def macv_123_macd_slope_rank_5d(close: pd.Series) -> pd.Series:
    """macv_123_macd_slope_rank_5d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(5)
    return _rank_pct(base, 5)

def macv_124_macd_slope_lvl_21d(close: pd.Series) -> pd.Series:
    """macv_124_macd_slope_lvl_21d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(5)
    return _rolling_mean(base, 21)

def macv_125_macd_slope_zscore_21d(close: pd.Series) -> pd.Series:
    """macv_125_macd_slope_zscore_21d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(5)
    return _zscore_rolling(base, 21)

def macv_126_macd_slope_rank_21d(close: pd.Series) -> pd.Series:
    """macv_126_macd_slope_rank_21d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(5)
    return _rank_pct(base, 21)

def macv_127_macd_slope_lvl_63d(close: pd.Series) -> pd.Series:
    """macv_127_macd_slope_lvl_63d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(5)
    return _rolling_mean(base, 63)

def macv_128_macd_slope_zscore_63d(close: pd.Series) -> pd.Series:
    """macv_128_macd_slope_zscore_63d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(5)
    return _zscore_rolling(base, 63)

def macv_129_macd_slope_rank_63d(close: pd.Series) -> pd.Series:
    """macv_129_macd_slope_rank_63d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(5)
    return _rank_pct(base, 63)

def macv_130_macd_slope_lvl_126d(close: pd.Series) -> pd.Series:
    """macv_130_macd_slope_lvl_126d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(5)
    return _rolling_mean(base, 126)

def macv_131_macd_slope_zscore_126d(close: pd.Series) -> pd.Series:
    """macv_131_macd_slope_zscore_126d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(5)
    return _zscore_rolling(base, 126)

def macv_132_macd_slope_rank_126d(close: pd.Series) -> pd.Series:
    """macv_132_macd_slope_rank_126d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(5)
    return _rank_pct(base, 126)

def macv_133_macd_slope_lvl_252d(close: pd.Series) -> pd.Series:
    """macv_133_macd_slope_lvl_252d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(5)
    return _rolling_mean(base, 252)

def macv_134_macd_slope_zscore_252d(close: pd.Series) -> pd.Series:
    """macv_134_macd_slope_zscore_252d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(5)
    return _zscore_rolling(base, 252)

def macv_135_macd_slope_rank_252d(close: pd.Series) -> pd.Series:
    """macv_135_macd_slope_rank_252d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(5)
    return _rank_pct(base, 252)

def macv_136_macd_cross_lvl_5d(close: pd.Series) -> pd.Series:
    """macv_136_macd_cross_lvl_5d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9))
    return _rolling_mean(base, 5)

def macv_137_macd_cross_zscore_5d(close: pd.Series) -> pd.Series:
    """macv_137_macd_cross_zscore_5d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9))
    return _zscore_rolling(base, 5)

def macv_138_macd_cross_rank_5d(close: pd.Series) -> pd.Series:
    """macv_138_macd_cross_rank_5d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9))
    return _rank_pct(base, 5)

def macv_139_macd_cross_lvl_21d(close: pd.Series) -> pd.Series:
    """macv_139_macd_cross_lvl_21d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9))
    return _rolling_mean(base, 21)

def macv_140_macd_cross_zscore_21d(close: pd.Series) -> pd.Series:
    """macv_140_macd_cross_zscore_21d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9))
    return _zscore_rolling(base, 21)

def macv_141_macd_cross_rank_21d(close: pd.Series) -> pd.Series:
    """macv_141_macd_cross_rank_21d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9))
    return _rank_pct(base, 21)

def macv_142_macd_cross_lvl_63d(close: pd.Series) -> pd.Series:
    """macv_142_macd_cross_lvl_63d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9))
    return _rolling_mean(base, 63)

def macv_143_macd_cross_zscore_63d(close: pd.Series) -> pd.Series:
    """macv_143_macd_cross_zscore_63d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9))
    return _zscore_rolling(base, 63)

def macv_144_macd_cross_rank_63d(close: pd.Series) -> pd.Series:
    """macv_144_macd_cross_rank_63d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9))
    return _rank_pct(base, 63)

def macv_145_macd_cross_lvl_126d(close: pd.Series) -> pd.Series:
    """macv_145_macd_cross_lvl_126d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9))
    return _rolling_mean(base, 126)

def macv_146_macd_cross_zscore_126d(close: pd.Series) -> pd.Series:
    """macv_146_macd_cross_zscore_126d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9))
    return _zscore_rolling(base, 126)

def macv_147_macd_cross_rank_126d(close: pd.Series) -> pd.Series:
    """macv_147_macd_cross_rank_126d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9))
    return _rank_pct(base, 126)

def macv_148_macd_cross_lvl_252d(close: pd.Series) -> pd.Series:
    """macv_148_macd_cross_lvl_252d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9))
    return _rolling_mean(base, 252)

def macv_149_macd_cross_zscore_252d(close: pd.Series) -> pd.Series:
    """macv_149_macd_cross_zscore_252d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9))
    return _zscore_rolling(base, 252)

def macv_150_macd_cross_rank_252d(close: pd.Series) -> pd.Series:
    """macv_150_macd_cross_rank_252d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V76_REGISTRY_2 = {
    "macv_076_hist_z_lvl_5d": {"inputs": ["close"], "func": macv_076_hist_z_lvl_5d},
    "macv_077_hist_z_zscore_5d": {"inputs": ["close"], "func": macv_077_hist_z_zscore_5d},
    "macv_078_hist_z_rank_5d": {"inputs": ["close"], "func": macv_078_hist_z_rank_5d},
    "macv_079_hist_z_lvl_21d": {"inputs": ["close"], "func": macv_079_hist_z_lvl_21d},
    "macv_080_hist_z_zscore_21d": {"inputs": ["close"], "func": macv_080_hist_z_zscore_21d},
    "macv_081_hist_z_rank_21d": {"inputs": ["close"], "func": macv_081_hist_z_rank_21d},
    "macv_082_hist_z_lvl_63d": {"inputs": ["close"], "func": macv_082_hist_z_lvl_63d},
    "macv_083_hist_z_zscore_63d": {"inputs": ["close"], "func": macv_083_hist_z_zscore_63d},
    "macv_084_hist_z_rank_63d": {"inputs": ["close"], "func": macv_084_hist_z_rank_63d},
    "macv_085_hist_z_lvl_126d": {"inputs": ["close"], "func": macv_085_hist_z_lvl_126d},
    "macv_086_hist_z_zscore_126d": {"inputs": ["close"], "func": macv_086_hist_z_zscore_126d},
    "macv_087_hist_z_rank_126d": {"inputs": ["close"], "func": macv_087_hist_z_rank_126d},
    "macv_088_hist_z_lvl_252d": {"inputs": ["close"], "func": macv_088_hist_z_lvl_252d},
    "macv_089_hist_z_zscore_252d": {"inputs": ["close"], "func": macv_089_hist_z_zscore_252d},
    "macv_090_hist_z_rank_252d": {"inputs": ["close"], "func": macv_090_hist_z_rank_252d},
    "macv_091_macd_fast_lvl_5d": {"inputs": ["close"], "func": macv_091_macd_fast_lvl_5d},
    "macv_092_macd_fast_zscore_5d": {"inputs": ["close"], "func": macv_092_macd_fast_zscore_5d},
    "macv_093_macd_fast_rank_5d": {"inputs": ["close"], "func": macv_093_macd_fast_rank_5d},
    "macv_094_macd_fast_lvl_21d": {"inputs": ["close"], "func": macv_094_macd_fast_lvl_21d},
    "macv_095_macd_fast_zscore_21d": {"inputs": ["close"], "func": macv_095_macd_fast_zscore_21d},
    "macv_096_macd_fast_rank_21d": {"inputs": ["close"], "func": macv_096_macd_fast_rank_21d},
    "macv_097_macd_fast_lvl_63d": {"inputs": ["close"], "func": macv_097_macd_fast_lvl_63d},
    "macv_098_macd_fast_zscore_63d": {"inputs": ["close"], "func": macv_098_macd_fast_zscore_63d},
    "macv_099_macd_fast_rank_63d": {"inputs": ["close"], "func": macv_099_macd_fast_rank_63d},
    "macv_100_macd_fast_lvl_126d": {"inputs": ["close"], "func": macv_100_macd_fast_lvl_126d},
    "macv_101_macd_fast_zscore_126d": {"inputs": ["close"], "func": macv_101_macd_fast_zscore_126d},
    "macv_102_macd_fast_rank_126d": {"inputs": ["close"], "func": macv_102_macd_fast_rank_126d},
    "macv_103_macd_fast_lvl_252d": {"inputs": ["close"], "func": macv_103_macd_fast_lvl_252d},
    "macv_104_macd_fast_zscore_252d": {"inputs": ["close"], "func": macv_104_macd_fast_zscore_252d},
    "macv_105_macd_fast_rank_252d": {"inputs": ["close"], "func": macv_105_macd_fast_rank_252d},
    "macv_106_macd_slow_lvl_5d": {"inputs": ["close"], "func": macv_106_macd_slow_lvl_5d},
    "macv_107_macd_slow_zscore_5d": {"inputs": ["close"], "func": macv_107_macd_slow_zscore_5d},
    "macv_108_macd_slow_rank_5d": {"inputs": ["close"], "func": macv_108_macd_slow_rank_5d},
    "macv_109_macd_slow_lvl_21d": {"inputs": ["close"], "func": macv_109_macd_slow_lvl_21d},
    "macv_110_macd_slow_zscore_21d": {"inputs": ["close"], "func": macv_110_macd_slow_zscore_21d},
    "macv_111_macd_slow_rank_21d": {"inputs": ["close"], "func": macv_111_macd_slow_rank_21d},
    "macv_112_macd_slow_lvl_63d": {"inputs": ["close"], "func": macv_112_macd_slow_lvl_63d},
    "macv_113_macd_slow_zscore_63d": {"inputs": ["close"], "func": macv_113_macd_slow_zscore_63d},
    "macv_114_macd_slow_rank_63d": {"inputs": ["close"], "func": macv_114_macd_slow_rank_63d},
    "macv_115_macd_slow_lvl_126d": {"inputs": ["close"], "func": macv_115_macd_slow_lvl_126d},
    "macv_116_macd_slow_zscore_126d": {"inputs": ["close"], "func": macv_116_macd_slow_zscore_126d},
    "macv_117_macd_slow_rank_126d": {"inputs": ["close"], "func": macv_117_macd_slow_rank_126d},
    "macv_118_macd_slow_lvl_252d": {"inputs": ["close"], "func": macv_118_macd_slow_lvl_252d},
    "macv_119_macd_slow_zscore_252d": {"inputs": ["close"], "func": macv_119_macd_slow_zscore_252d},
    "macv_120_macd_slow_rank_252d": {"inputs": ["close"], "func": macv_120_macd_slow_rank_252d},
    "macv_121_macd_slope_lvl_5d": {"inputs": ["close"], "func": macv_121_macd_slope_lvl_5d},
    "macv_122_macd_slope_zscore_5d": {"inputs": ["close"], "func": macv_122_macd_slope_zscore_5d},
    "macv_123_macd_slope_rank_5d": {"inputs": ["close"], "func": macv_123_macd_slope_rank_5d},
    "macv_124_macd_slope_lvl_21d": {"inputs": ["close"], "func": macv_124_macd_slope_lvl_21d},
    "macv_125_macd_slope_zscore_21d": {"inputs": ["close"], "func": macv_125_macd_slope_zscore_21d},
    "macv_126_macd_slope_rank_21d": {"inputs": ["close"], "func": macv_126_macd_slope_rank_21d},
    "macv_127_macd_slope_lvl_63d": {"inputs": ["close"], "func": macv_127_macd_slope_lvl_63d},
    "macv_128_macd_slope_zscore_63d": {"inputs": ["close"], "func": macv_128_macd_slope_zscore_63d},
    "macv_129_macd_slope_rank_63d": {"inputs": ["close"], "func": macv_129_macd_slope_rank_63d},
    "macv_130_macd_slope_lvl_126d": {"inputs": ["close"], "func": macv_130_macd_slope_lvl_126d},
    "macv_131_macd_slope_zscore_126d": {"inputs": ["close"], "func": macv_131_macd_slope_zscore_126d},
    "macv_132_macd_slope_rank_126d": {"inputs": ["close"], "func": macv_132_macd_slope_rank_126d},
    "macv_133_macd_slope_lvl_252d": {"inputs": ["close"], "func": macv_133_macd_slope_lvl_252d},
    "macv_134_macd_slope_zscore_252d": {"inputs": ["close"], "func": macv_134_macd_slope_zscore_252d},
    "macv_135_macd_slope_rank_252d": {"inputs": ["close"], "func": macv_135_macd_slope_rank_252d},
    "macv_136_macd_cross_lvl_5d": {"inputs": ["close"], "func": macv_136_macd_cross_lvl_5d},
    "macv_137_macd_cross_zscore_5d": {"inputs": ["close"], "func": macv_137_macd_cross_zscore_5d},
    "macv_138_macd_cross_rank_5d": {"inputs": ["close"], "func": macv_138_macd_cross_rank_5d},
    "macv_139_macd_cross_lvl_21d": {"inputs": ["close"], "func": macv_139_macd_cross_lvl_21d},
    "macv_140_macd_cross_zscore_21d": {"inputs": ["close"], "func": macv_140_macd_cross_zscore_21d},
    "macv_141_macd_cross_rank_21d": {"inputs": ["close"], "func": macv_141_macd_cross_rank_21d},
    "macv_142_macd_cross_lvl_63d": {"inputs": ["close"], "func": macv_142_macd_cross_lvl_63d},
    "macv_143_macd_cross_zscore_63d": {"inputs": ["close"], "func": macv_143_macd_cross_zscore_63d},
    "macv_144_macd_cross_rank_63d": {"inputs": ["close"], "func": macv_144_macd_cross_rank_63d},
    "macv_145_macd_cross_lvl_126d": {"inputs": ["close"], "func": macv_145_macd_cross_lvl_126d},
    "macv_146_macd_cross_zscore_126d": {"inputs": ["close"], "func": macv_146_macd_cross_zscore_126d},
    "macv_147_macd_cross_rank_126d": {"inputs": ["close"], "func": macv_147_macd_cross_rank_126d},
    "macv_148_macd_cross_lvl_252d": {"inputs": ["close"], "func": macv_148_macd_cross_lvl_252d},
    "macv_149_macd_cross_zscore_252d": {"inputs": ["close"], "func": macv_149_macd_cross_zscore_252d},
    "macv_150_macd_cross_rank_252d": {"inputs": ["close"], "func": macv_150_macd_cross_rank_252d},
}
