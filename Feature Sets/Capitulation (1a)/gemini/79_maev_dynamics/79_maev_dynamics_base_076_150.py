"""
79_maev_dynamics — Base Features 076-150
Domain: maev_dynamics
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

def maev_076_sma20_z_lvl_5d(close: pd.Series) -> pd.Series:
    """maev_076_sma20_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 20)), 63)
    return _rolling_mean(base, 5)

def maev_077_sma20_z_zscore_5d(close: pd.Series) -> pd.Series:
    """maev_077_sma20_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 20)), 63)
    return _zscore_rolling(base, 5)

def maev_078_sma20_z_rank_5d(close: pd.Series) -> pd.Series:
    """maev_078_sma20_z_rank_5d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 20)), 63)
    return _rank_pct(base, 5)

def maev_079_sma20_z_lvl_21d(close: pd.Series) -> pd.Series:
    """maev_079_sma20_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 20)), 63)
    return _rolling_mean(base, 21)

def maev_080_sma20_z_zscore_21d(close: pd.Series) -> pd.Series:
    """maev_080_sma20_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 20)), 63)
    return _zscore_rolling(base, 21)

def maev_081_sma20_z_rank_21d(close: pd.Series) -> pd.Series:
    """maev_081_sma20_z_rank_21d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 20)), 63)
    return _rank_pct(base, 21)

def maev_082_sma20_z_lvl_63d(close: pd.Series) -> pd.Series:
    """maev_082_sma20_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 20)), 63)
    return _rolling_mean(base, 63)

def maev_083_sma20_z_zscore_63d(close: pd.Series) -> pd.Series:
    """maev_083_sma20_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 20)), 63)
    return _zscore_rolling(base, 63)

def maev_084_sma20_z_rank_63d(close: pd.Series) -> pd.Series:
    """maev_084_sma20_z_rank_63d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 20)), 63)
    return _rank_pct(base, 63)

def maev_085_sma20_z_lvl_126d(close: pd.Series) -> pd.Series:
    """maev_085_sma20_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 20)), 63)
    return _rolling_mean(base, 126)

def maev_086_sma20_z_zscore_126d(close: pd.Series) -> pd.Series:
    """maev_086_sma20_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 20)), 63)
    return _zscore_rolling(base, 126)

def maev_087_sma20_z_rank_126d(close: pd.Series) -> pd.Series:
    """maev_087_sma20_z_rank_126d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 20)), 63)
    return _rank_pct(base, 126)

def maev_088_sma20_z_lvl_252d(close: pd.Series) -> pd.Series:
    """maev_088_sma20_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 20)), 63)
    return _rolling_mean(base, 252)

def maev_089_sma20_z_zscore_252d(close: pd.Series) -> pd.Series:
    """maev_089_sma20_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 20)), 63)
    return _zscore_rolling(base, 252)

def maev_090_sma20_z_rank_252d(close: pd.Series) -> pd.Series:
    """maev_090_sma20_z_rank_252d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 20)), 63)
    return _rank_pct(base, 252)

def maev_091_sma50_z_lvl_5d(close: pd.Series) -> pd.Series:
    """maev_091_sma50_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 50)), 63)
    return _rolling_mean(base, 5)

def maev_092_sma50_z_zscore_5d(close: pd.Series) -> pd.Series:
    """maev_092_sma50_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 50)), 63)
    return _zscore_rolling(base, 5)

def maev_093_sma50_z_rank_5d(close: pd.Series) -> pd.Series:
    """maev_093_sma50_z_rank_5d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 50)), 63)
    return _rank_pct(base, 5)

def maev_094_sma50_z_lvl_21d(close: pd.Series) -> pd.Series:
    """maev_094_sma50_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 50)), 63)
    return _rolling_mean(base, 21)

def maev_095_sma50_z_zscore_21d(close: pd.Series) -> pd.Series:
    """maev_095_sma50_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 50)), 63)
    return _zscore_rolling(base, 21)

def maev_096_sma50_z_rank_21d(close: pd.Series) -> pd.Series:
    """maev_096_sma50_z_rank_21d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 50)), 63)
    return _rank_pct(base, 21)

def maev_097_sma50_z_lvl_63d(close: pd.Series) -> pd.Series:
    """maev_097_sma50_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 50)), 63)
    return _rolling_mean(base, 63)

def maev_098_sma50_z_zscore_63d(close: pd.Series) -> pd.Series:
    """maev_098_sma50_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 50)), 63)
    return _zscore_rolling(base, 63)

def maev_099_sma50_z_rank_63d(close: pd.Series) -> pd.Series:
    """maev_099_sma50_z_rank_63d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 50)), 63)
    return _rank_pct(base, 63)

def maev_100_sma50_z_lvl_126d(close: pd.Series) -> pd.Series:
    """maev_100_sma50_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 50)), 63)
    return _rolling_mean(base, 126)

def maev_101_sma50_z_zscore_126d(close: pd.Series) -> pd.Series:
    """maev_101_sma50_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 50)), 63)
    return _zscore_rolling(base, 126)

def maev_102_sma50_z_rank_126d(close: pd.Series) -> pd.Series:
    """maev_102_sma50_z_rank_126d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 50)), 63)
    return _rank_pct(base, 126)

def maev_103_sma50_z_lvl_252d(close: pd.Series) -> pd.Series:
    """maev_103_sma50_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 50)), 63)
    return _rolling_mean(base, 252)

def maev_104_sma50_z_zscore_252d(close: pd.Series) -> pd.Series:
    """maev_104_sma50_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 50)), 63)
    return _zscore_rolling(base, 252)

def maev_105_sma50_z_rank_252d(close: pd.Series) -> pd.Series:
    """maev_105_sma50_z_rank_252d"""
    base = _zscore_rolling(_safe_div(close, _rolling_mean(close, 50)), 63)
    return _rank_pct(base, 252)

def maev_106_ema20_z_lvl_5d(close: pd.Series) -> pd.Series:
    """maev_106_ema20_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(close, _ewm_mean(close, 20)), 63)
    return _rolling_mean(base, 5)

def maev_107_ema20_z_zscore_5d(close: pd.Series) -> pd.Series:
    """maev_107_ema20_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(close, _ewm_mean(close, 20)), 63)
    return _zscore_rolling(base, 5)

def maev_108_ema20_z_rank_5d(close: pd.Series) -> pd.Series:
    """maev_108_ema20_z_rank_5d"""
    base = _zscore_rolling(_safe_div(close, _ewm_mean(close, 20)), 63)
    return _rank_pct(base, 5)

def maev_109_ema20_z_lvl_21d(close: pd.Series) -> pd.Series:
    """maev_109_ema20_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(close, _ewm_mean(close, 20)), 63)
    return _rolling_mean(base, 21)

def maev_110_ema20_z_zscore_21d(close: pd.Series) -> pd.Series:
    """maev_110_ema20_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(close, _ewm_mean(close, 20)), 63)
    return _zscore_rolling(base, 21)

def maev_111_ema20_z_rank_21d(close: pd.Series) -> pd.Series:
    """maev_111_ema20_z_rank_21d"""
    base = _zscore_rolling(_safe_div(close, _ewm_mean(close, 20)), 63)
    return _rank_pct(base, 21)

def maev_112_ema20_z_lvl_63d(close: pd.Series) -> pd.Series:
    """maev_112_ema20_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(close, _ewm_mean(close, 20)), 63)
    return _rolling_mean(base, 63)

def maev_113_ema20_z_zscore_63d(close: pd.Series) -> pd.Series:
    """maev_113_ema20_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(close, _ewm_mean(close, 20)), 63)
    return _zscore_rolling(base, 63)

def maev_114_ema20_z_rank_63d(close: pd.Series) -> pd.Series:
    """maev_114_ema20_z_rank_63d"""
    base = _zscore_rolling(_safe_div(close, _ewm_mean(close, 20)), 63)
    return _rank_pct(base, 63)

def maev_115_ema20_z_lvl_126d(close: pd.Series) -> pd.Series:
    """maev_115_ema20_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(close, _ewm_mean(close, 20)), 63)
    return _rolling_mean(base, 126)

def maev_116_ema20_z_zscore_126d(close: pd.Series) -> pd.Series:
    """maev_116_ema20_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(close, _ewm_mean(close, 20)), 63)
    return _zscore_rolling(base, 126)

def maev_117_ema20_z_rank_126d(close: pd.Series) -> pd.Series:
    """maev_117_ema20_z_rank_126d"""
    base = _zscore_rolling(_safe_div(close, _ewm_mean(close, 20)), 63)
    return _rank_pct(base, 126)

def maev_118_ema20_z_lvl_252d(close: pd.Series) -> pd.Series:
    """maev_118_ema20_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(close, _ewm_mean(close, 20)), 63)
    return _rolling_mean(base, 252)

def maev_119_ema20_z_zscore_252d(close: pd.Series) -> pd.Series:
    """maev_119_ema20_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(close, _ewm_mean(close, 20)), 63)
    return _zscore_rolling(base, 252)

def maev_120_ema20_z_rank_252d(close: pd.Series) -> pd.Series:
    """maev_120_ema20_z_rank_252d"""
    base = _zscore_rolling(_safe_div(close, _ewm_mean(close, 20)), 63)
    return _rank_pct(base, 252)

def maev_121_dist_spread_lvl_5d(close: pd.Series) -> pd.Series:
    """maev_121_dist_spread_lvl_5d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 200))
    return _rolling_mean(base, 5)

def maev_122_dist_spread_zscore_5d(close: pd.Series) -> pd.Series:
    """maev_122_dist_spread_zscore_5d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 200))
    return _zscore_rolling(base, 5)

def maev_123_dist_spread_rank_5d(close: pd.Series) -> pd.Series:
    """maev_123_dist_spread_rank_5d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 200))
    return _rank_pct(base, 5)

def maev_124_dist_spread_lvl_21d(close: pd.Series) -> pd.Series:
    """maev_124_dist_spread_lvl_21d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 200))
    return _rolling_mean(base, 21)

def maev_125_dist_spread_zscore_21d(close: pd.Series) -> pd.Series:
    """maev_125_dist_spread_zscore_21d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 200))
    return _zscore_rolling(base, 21)

def maev_126_dist_spread_rank_21d(close: pd.Series) -> pd.Series:
    """maev_126_dist_spread_rank_21d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 200))
    return _rank_pct(base, 21)

def maev_127_dist_spread_lvl_63d(close: pd.Series) -> pd.Series:
    """maev_127_dist_spread_lvl_63d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 200))
    return _rolling_mean(base, 63)

def maev_128_dist_spread_zscore_63d(close: pd.Series) -> pd.Series:
    """maev_128_dist_spread_zscore_63d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 200))
    return _zscore_rolling(base, 63)

def maev_129_dist_spread_rank_63d(close: pd.Series) -> pd.Series:
    """maev_129_dist_spread_rank_63d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 200))
    return _rank_pct(base, 63)

def maev_130_dist_spread_lvl_126d(close: pd.Series) -> pd.Series:
    """maev_130_dist_spread_lvl_126d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 200))
    return _rolling_mean(base, 126)

def maev_131_dist_spread_zscore_126d(close: pd.Series) -> pd.Series:
    """maev_131_dist_spread_zscore_126d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 200))
    return _zscore_rolling(base, 126)

def maev_132_dist_spread_rank_126d(close: pd.Series) -> pd.Series:
    """maev_132_dist_spread_rank_126d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 200))
    return _rank_pct(base, 126)

def maev_133_dist_spread_lvl_252d(close: pd.Series) -> pd.Series:
    """maev_133_dist_spread_lvl_252d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 200))
    return _rolling_mean(base, 252)

def maev_134_dist_spread_zscore_252d(close: pd.Series) -> pd.Series:
    """maev_134_dist_spread_zscore_252d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 200))
    return _zscore_rolling(base, 252)

def maev_135_dist_spread_rank_252d(close: pd.Series) -> pd.Series:
    """maev_135_dist_spread_rank_252d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 200))
    return _rank_pct(base, 252)

def maev_136_ma_slope_lvl_5d(close: pd.Series) -> pd.Series:
    """maev_136_ma_slope_lvl_5d"""
    base = _rolling_mean(close, 20).pct_change(5)
    return _rolling_mean(base, 5)

def maev_137_ma_slope_zscore_5d(close: pd.Series) -> pd.Series:
    """maev_137_ma_slope_zscore_5d"""
    base = _rolling_mean(close, 20).pct_change(5)
    return _zscore_rolling(base, 5)

def maev_138_ma_slope_rank_5d(close: pd.Series) -> pd.Series:
    """maev_138_ma_slope_rank_5d"""
    base = _rolling_mean(close, 20).pct_change(5)
    return _rank_pct(base, 5)

def maev_139_ma_slope_lvl_21d(close: pd.Series) -> pd.Series:
    """maev_139_ma_slope_lvl_21d"""
    base = _rolling_mean(close, 20).pct_change(5)
    return _rolling_mean(base, 21)

def maev_140_ma_slope_zscore_21d(close: pd.Series) -> pd.Series:
    """maev_140_ma_slope_zscore_21d"""
    base = _rolling_mean(close, 20).pct_change(5)
    return _zscore_rolling(base, 21)

def maev_141_ma_slope_rank_21d(close: pd.Series) -> pd.Series:
    """maev_141_ma_slope_rank_21d"""
    base = _rolling_mean(close, 20).pct_change(5)
    return _rank_pct(base, 21)

def maev_142_ma_slope_lvl_63d(close: pd.Series) -> pd.Series:
    """maev_142_ma_slope_lvl_63d"""
    base = _rolling_mean(close, 20).pct_change(5)
    return _rolling_mean(base, 63)

def maev_143_ma_slope_zscore_63d(close: pd.Series) -> pd.Series:
    """maev_143_ma_slope_zscore_63d"""
    base = _rolling_mean(close, 20).pct_change(5)
    return _zscore_rolling(base, 63)

def maev_144_ma_slope_rank_63d(close: pd.Series) -> pd.Series:
    """maev_144_ma_slope_rank_63d"""
    base = _rolling_mean(close, 20).pct_change(5)
    return _rank_pct(base, 63)

def maev_145_ma_slope_lvl_126d(close: pd.Series) -> pd.Series:
    """maev_145_ma_slope_lvl_126d"""
    base = _rolling_mean(close, 20).pct_change(5)
    return _rolling_mean(base, 126)

def maev_146_ma_slope_zscore_126d(close: pd.Series) -> pd.Series:
    """maev_146_ma_slope_zscore_126d"""
    base = _rolling_mean(close, 20).pct_change(5)
    return _zscore_rolling(base, 126)

def maev_147_ma_slope_rank_126d(close: pd.Series) -> pd.Series:
    """maev_147_ma_slope_rank_126d"""
    base = _rolling_mean(close, 20).pct_change(5)
    return _rank_pct(base, 126)

def maev_148_ma_slope_lvl_252d(close: pd.Series) -> pd.Series:
    """maev_148_ma_slope_lvl_252d"""
    base = _rolling_mean(close, 20).pct_change(5)
    return _rolling_mean(base, 252)

def maev_149_ma_slope_zscore_252d(close: pd.Series) -> pd.Series:
    """maev_149_ma_slope_zscore_252d"""
    base = _rolling_mean(close, 20).pct_change(5)
    return _zscore_rolling(base, 252)

def maev_150_ma_slope_rank_252d(close: pd.Series) -> pd.Series:
    """maev_150_ma_slope_rank_252d"""
    base = _rolling_mean(close, 20).pct_change(5)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V79_REGISTRY_2 = {
    "maev_076_sma20_z_lvl_5d": {"inputs": ["close"], "func": maev_076_sma20_z_lvl_5d},
    "maev_077_sma20_z_zscore_5d": {"inputs": ["close"], "func": maev_077_sma20_z_zscore_5d},
    "maev_078_sma20_z_rank_5d": {"inputs": ["close"], "func": maev_078_sma20_z_rank_5d},
    "maev_079_sma20_z_lvl_21d": {"inputs": ["close"], "func": maev_079_sma20_z_lvl_21d},
    "maev_080_sma20_z_zscore_21d": {"inputs": ["close"], "func": maev_080_sma20_z_zscore_21d},
    "maev_081_sma20_z_rank_21d": {"inputs": ["close"], "func": maev_081_sma20_z_rank_21d},
    "maev_082_sma20_z_lvl_63d": {"inputs": ["close"], "func": maev_082_sma20_z_lvl_63d},
    "maev_083_sma20_z_zscore_63d": {"inputs": ["close"], "func": maev_083_sma20_z_zscore_63d},
    "maev_084_sma20_z_rank_63d": {"inputs": ["close"], "func": maev_084_sma20_z_rank_63d},
    "maev_085_sma20_z_lvl_126d": {"inputs": ["close"], "func": maev_085_sma20_z_lvl_126d},
    "maev_086_sma20_z_zscore_126d": {"inputs": ["close"], "func": maev_086_sma20_z_zscore_126d},
    "maev_087_sma20_z_rank_126d": {"inputs": ["close"], "func": maev_087_sma20_z_rank_126d},
    "maev_088_sma20_z_lvl_252d": {"inputs": ["close"], "func": maev_088_sma20_z_lvl_252d},
    "maev_089_sma20_z_zscore_252d": {"inputs": ["close"], "func": maev_089_sma20_z_zscore_252d},
    "maev_090_sma20_z_rank_252d": {"inputs": ["close"], "func": maev_090_sma20_z_rank_252d},
    "maev_091_sma50_z_lvl_5d": {"inputs": ["close"], "func": maev_091_sma50_z_lvl_5d},
    "maev_092_sma50_z_zscore_5d": {"inputs": ["close"], "func": maev_092_sma50_z_zscore_5d},
    "maev_093_sma50_z_rank_5d": {"inputs": ["close"], "func": maev_093_sma50_z_rank_5d},
    "maev_094_sma50_z_lvl_21d": {"inputs": ["close"], "func": maev_094_sma50_z_lvl_21d},
    "maev_095_sma50_z_zscore_21d": {"inputs": ["close"], "func": maev_095_sma50_z_zscore_21d},
    "maev_096_sma50_z_rank_21d": {"inputs": ["close"], "func": maev_096_sma50_z_rank_21d},
    "maev_097_sma50_z_lvl_63d": {"inputs": ["close"], "func": maev_097_sma50_z_lvl_63d},
    "maev_098_sma50_z_zscore_63d": {"inputs": ["close"], "func": maev_098_sma50_z_zscore_63d},
    "maev_099_sma50_z_rank_63d": {"inputs": ["close"], "func": maev_099_sma50_z_rank_63d},
    "maev_100_sma50_z_lvl_126d": {"inputs": ["close"], "func": maev_100_sma50_z_lvl_126d},
    "maev_101_sma50_z_zscore_126d": {"inputs": ["close"], "func": maev_101_sma50_z_zscore_126d},
    "maev_102_sma50_z_rank_126d": {"inputs": ["close"], "func": maev_102_sma50_z_rank_126d},
    "maev_103_sma50_z_lvl_252d": {"inputs": ["close"], "func": maev_103_sma50_z_lvl_252d},
    "maev_104_sma50_z_zscore_252d": {"inputs": ["close"], "func": maev_104_sma50_z_zscore_252d},
    "maev_105_sma50_z_rank_252d": {"inputs": ["close"], "func": maev_105_sma50_z_rank_252d},
    "maev_106_ema20_z_lvl_5d": {"inputs": ["close"], "func": maev_106_ema20_z_lvl_5d},
    "maev_107_ema20_z_zscore_5d": {"inputs": ["close"], "func": maev_107_ema20_z_zscore_5d},
    "maev_108_ema20_z_rank_5d": {"inputs": ["close"], "func": maev_108_ema20_z_rank_5d},
    "maev_109_ema20_z_lvl_21d": {"inputs": ["close"], "func": maev_109_ema20_z_lvl_21d},
    "maev_110_ema20_z_zscore_21d": {"inputs": ["close"], "func": maev_110_ema20_z_zscore_21d},
    "maev_111_ema20_z_rank_21d": {"inputs": ["close"], "func": maev_111_ema20_z_rank_21d},
    "maev_112_ema20_z_lvl_63d": {"inputs": ["close"], "func": maev_112_ema20_z_lvl_63d},
    "maev_113_ema20_z_zscore_63d": {"inputs": ["close"], "func": maev_113_ema20_z_zscore_63d},
    "maev_114_ema20_z_rank_63d": {"inputs": ["close"], "func": maev_114_ema20_z_rank_63d},
    "maev_115_ema20_z_lvl_126d": {"inputs": ["close"], "func": maev_115_ema20_z_lvl_126d},
    "maev_116_ema20_z_zscore_126d": {"inputs": ["close"], "func": maev_116_ema20_z_zscore_126d},
    "maev_117_ema20_z_rank_126d": {"inputs": ["close"], "func": maev_117_ema20_z_rank_126d},
    "maev_118_ema20_z_lvl_252d": {"inputs": ["close"], "func": maev_118_ema20_z_lvl_252d},
    "maev_119_ema20_z_zscore_252d": {"inputs": ["close"], "func": maev_119_ema20_z_zscore_252d},
    "maev_120_ema20_z_rank_252d": {"inputs": ["close"], "func": maev_120_ema20_z_rank_252d},
    "maev_121_dist_spread_lvl_5d": {"inputs": ["close"], "func": maev_121_dist_spread_lvl_5d},
    "maev_122_dist_spread_zscore_5d": {"inputs": ["close"], "func": maev_122_dist_spread_zscore_5d},
    "maev_123_dist_spread_rank_5d": {"inputs": ["close"], "func": maev_123_dist_spread_rank_5d},
    "maev_124_dist_spread_lvl_21d": {"inputs": ["close"], "func": maev_124_dist_spread_lvl_21d},
    "maev_125_dist_spread_zscore_21d": {"inputs": ["close"], "func": maev_125_dist_spread_zscore_21d},
    "maev_126_dist_spread_rank_21d": {"inputs": ["close"], "func": maev_126_dist_spread_rank_21d},
    "maev_127_dist_spread_lvl_63d": {"inputs": ["close"], "func": maev_127_dist_spread_lvl_63d},
    "maev_128_dist_spread_zscore_63d": {"inputs": ["close"], "func": maev_128_dist_spread_zscore_63d},
    "maev_129_dist_spread_rank_63d": {"inputs": ["close"], "func": maev_129_dist_spread_rank_63d},
    "maev_130_dist_spread_lvl_126d": {"inputs": ["close"], "func": maev_130_dist_spread_lvl_126d},
    "maev_131_dist_spread_zscore_126d": {"inputs": ["close"], "func": maev_131_dist_spread_zscore_126d},
    "maev_132_dist_spread_rank_126d": {"inputs": ["close"], "func": maev_132_dist_spread_rank_126d},
    "maev_133_dist_spread_lvl_252d": {"inputs": ["close"], "func": maev_133_dist_spread_lvl_252d},
    "maev_134_dist_spread_zscore_252d": {"inputs": ["close"], "func": maev_134_dist_spread_zscore_252d},
    "maev_135_dist_spread_rank_252d": {"inputs": ["close"], "func": maev_135_dist_spread_rank_252d},
    "maev_136_ma_slope_lvl_5d": {"inputs": ["close"], "func": maev_136_ma_slope_lvl_5d},
    "maev_137_ma_slope_zscore_5d": {"inputs": ["close"], "func": maev_137_ma_slope_zscore_5d},
    "maev_138_ma_slope_rank_5d": {"inputs": ["close"], "func": maev_138_ma_slope_rank_5d},
    "maev_139_ma_slope_lvl_21d": {"inputs": ["close"], "func": maev_139_ma_slope_lvl_21d},
    "maev_140_ma_slope_zscore_21d": {"inputs": ["close"], "func": maev_140_ma_slope_zscore_21d},
    "maev_141_ma_slope_rank_21d": {"inputs": ["close"], "func": maev_141_ma_slope_rank_21d},
    "maev_142_ma_slope_lvl_63d": {"inputs": ["close"], "func": maev_142_ma_slope_lvl_63d},
    "maev_143_ma_slope_zscore_63d": {"inputs": ["close"], "func": maev_143_ma_slope_zscore_63d},
    "maev_144_ma_slope_rank_63d": {"inputs": ["close"], "func": maev_144_ma_slope_rank_63d},
    "maev_145_ma_slope_lvl_126d": {"inputs": ["close"], "func": maev_145_ma_slope_lvl_126d},
    "maev_146_ma_slope_zscore_126d": {"inputs": ["close"], "func": maev_146_ma_slope_zscore_126d},
    "maev_147_ma_slope_rank_126d": {"inputs": ["close"], "func": maev_147_ma_slope_rank_126d},
    "maev_148_ma_slope_lvl_252d": {"inputs": ["close"], "func": maev_148_ma_slope_lvl_252d},
    "maev_149_ma_slope_zscore_252d": {"inputs": ["close"], "func": maev_149_ma_slope_zscore_252d},
    "maev_150_ma_slope_rank_252d": {"inputs": ["close"], "func": maev_150_ma_slope_rank_252d},
}
