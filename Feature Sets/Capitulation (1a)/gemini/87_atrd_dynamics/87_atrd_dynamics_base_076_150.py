"""
87_atrd_dynamics — Base Features 076-150
Domain: atrd_dynamics
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

def atrd_076_tr_range_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_076_tr_range_lvl_5d"""
    base = high - low
    return _rolling_mean(base, 5)

def atrd_077_tr_range_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_077_tr_range_zscore_5d"""
    base = high - low
    return _zscore_rolling(base, 5)

def atrd_078_tr_range_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_078_tr_range_rank_5d"""
    base = high - low
    return _rank_pct(base, 5)

def atrd_079_tr_range_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_079_tr_range_lvl_21d"""
    base = high - low
    return _rolling_mean(base, 21)

def atrd_080_tr_range_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_080_tr_range_zscore_21d"""
    base = high - low
    return _zscore_rolling(base, 21)

def atrd_081_tr_range_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_081_tr_range_rank_21d"""
    base = high - low
    return _rank_pct(base, 21)

def atrd_082_tr_range_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_082_tr_range_lvl_63d"""
    base = high - low
    return _rolling_mean(base, 63)

def atrd_083_tr_range_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_083_tr_range_zscore_63d"""
    base = high - low
    return _zscore_rolling(base, 63)

def atrd_084_tr_range_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_084_tr_range_rank_63d"""
    base = high - low
    return _rank_pct(base, 63)

def atrd_085_tr_range_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_085_tr_range_lvl_126d"""
    base = high - low
    return _rolling_mean(base, 126)

def atrd_086_tr_range_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_086_tr_range_zscore_126d"""
    base = high - low
    return _zscore_rolling(base, 126)

def atrd_087_tr_range_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_087_tr_range_rank_126d"""
    base = high - low
    return _rank_pct(base, 126)

def atrd_088_tr_range_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_088_tr_range_lvl_252d"""
    base = high - low
    return _rolling_mean(base, 252)

def atrd_089_tr_range_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_089_tr_range_zscore_252d"""
    base = high - low
    return _zscore_rolling(base, 252)

def atrd_090_tr_range_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_090_tr_range_rank_252d"""
    base = high - low
    return _rank_pct(base, 252)

def atrd_091_tr_gap_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_091_tr_gap_lvl_5d"""
    base = (high - close.shift(1)).abs()
    return _rolling_mean(base, 5)

def atrd_092_tr_gap_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_092_tr_gap_zscore_5d"""
    base = (high - close.shift(1)).abs()
    return _zscore_rolling(base, 5)

def atrd_093_tr_gap_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_093_tr_gap_rank_5d"""
    base = (high - close.shift(1)).abs()
    return _rank_pct(base, 5)

def atrd_094_tr_gap_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_094_tr_gap_lvl_21d"""
    base = (high - close.shift(1)).abs()
    return _rolling_mean(base, 21)

def atrd_095_tr_gap_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_095_tr_gap_zscore_21d"""
    base = (high - close.shift(1)).abs()
    return _zscore_rolling(base, 21)

def atrd_096_tr_gap_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_096_tr_gap_rank_21d"""
    base = (high - close.shift(1)).abs()
    return _rank_pct(base, 21)

def atrd_097_tr_gap_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_097_tr_gap_lvl_63d"""
    base = (high - close.shift(1)).abs()
    return _rolling_mean(base, 63)

def atrd_098_tr_gap_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_098_tr_gap_zscore_63d"""
    base = (high - close.shift(1)).abs()
    return _zscore_rolling(base, 63)

def atrd_099_tr_gap_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_099_tr_gap_rank_63d"""
    base = (high - close.shift(1)).abs()
    return _rank_pct(base, 63)

def atrd_100_tr_gap_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_100_tr_gap_lvl_126d"""
    base = (high - close.shift(1)).abs()
    return _rolling_mean(base, 126)

def atrd_101_tr_gap_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_101_tr_gap_zscore_126d"""
    base = (high - close.shift(1)).abs()
    return _zscore_rolling(base, 126)

def atrd_102_tr_gap_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_102_tr_gap_rank_126d"""
    base = (high - close.shift(1)).abs()
    return _rank_pct(base, 126)

def atrd_103_tr_gap_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_103_tr_gap_lvl_252d"""
    base = (high - close.shift(1)).abs()
    return _rolling_mean(base, 252)

def atrd_104_tr_gap_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_104_tr_gap_zscore_252d"""
    base = (high - close.shift(1)).abs()
    return _zscore_rolling(base, 252)

def atrd_105_tr_gap_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_105_tr_gap_rank_252d"""
    base = (high - close.shift(1)).abs()
    return _rank_pct(base, 252)

def atrd_106_tr_low_gap_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_106_tr_low_gap_lvl_5d"""
    base = (low - close.shift(1)).abs()
    return _rolling_mean(base, 5)

def atrd_107_tr_low_gap_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_107_tr_low_gap_zscore_5d"""
    base = (low - close.shift(1)).abs()
    return _zscore_rolling(base, 5)

def atrd_108_tr_low_gap_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_108_tr_low_gap_rank_5d"""
    base = (low - close.shift(1)).abs()
    return _rank_pct(base, 5)

def atrd_109_tr_low_gap_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_109_tr_low_gap_lvl_21d"""
    base = (low - close.shift(1)).abs()
    return _rolling_mean(base, 21)

def atrd_110_tr_low_gap_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_110_tr_low_gap_zscore_21d"""
    base = (low - close.shift(1)).abs()
    return _zscore_rolling(base, 21)

def atrd_111_tr_low_gap_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_111_tr_low_gap_rank_21d"""
    base = (low - close.shift(1)).abs()
    return _rank_pct(base, 21)

def atrd_112_tr_low_gap_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_112_tr_low_gap_lvl_63d"""
    base = (low - close.shift(1)).abs()
    return _rolling_mean(base, 63)

def atrd_113_tr_low_gap_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_113_tr_low_gap_zscore_63d"""
    base = (low - close.shift(1)).abs()
    return _zscore_rolling(base, 63)

def atrd_114_tr_low_gap_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_114_tr_low_gap_rank_63d"""
    base = (low - close.shift(1)).abs()
    return _rank_pct(base, 63)

def atrd_115_tr_low_gap_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_115_tr_low_gap_lvl_126d"""
    base = (low - close.shift(1)).abs()
    return _rolling_mean(base, 126)

def atrd_116_tr_low_gap_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_116_tr_low_gap_zscore_126d"""
    base = (low - close.shift(1)).abs()
    return _zscore_rolling(base, 126)

def atrd_117_tr_low_gap_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_117_tr_low_gap_rank_126d"""
    base = (low - close.shift(1)).abs()
    return _rank_pct(base, 126)

def atrd_118_tr_low_gap_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_118_tr_low_gap_lvl_252d"""
    base = (low - close.shift(1)).abs()
    return _rolling_mean(base, 252)

def atrd_119_tr_low_gap_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_119_tr_low_gap_zscore_252d"""
    base = (low - close.shift(1)).abs()
    return _zscore_rolling(base, 252)

def atrd_120_tr_low_gap_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_120_tr_low_gap_rank_252d"""
    base = (low - close.shift(1)).abs()
    return _rank_pct(base, 252)

def atrd_121_tr_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_121_tr_z_lvl_5d"""
    base = _zscore_rolling(high - low, 21)
    return _rolling_mean(base, 5)

def atrd_122_tr_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_122_tr_z_zscore_5d"""
    base = _zscore_rolling(high - low, 21)
    return _zscore_rolling(base, 5)

def atrd_123_tr_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_123_tr_z_rank_5d"""
    base = _zscore_rolling(high - low, 21)
    return _rank_pct(base, 5)

def atrd_124_tr_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_124_tr_z_lvl_21d"""
    base = _zscore_rolling(high - low, 21)
    return _rolling_mean(base, 21)

def atrd_125_tr_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_125_tr_z_zscore_21d"""
    base = _zscore_rolling(high - low, 21)
    return _zscore_rolling(base, 21)

def atrd_126_tr_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_126_tr_z_rank_21d"""
    base = _zscore_rolling(high - low, 21)
    return _rank_pct(base, 21)

def atrd_127_tr_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_127_tr_z_lvl_63d"""
    base = _zscore_rolling(high - low, 21)
    return _rolling_mean(base, 63)

def atrd_128_tr_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_128_tr_z_zscore_63d"""
    base = _zscore_rolling(high - low, 21)
    return _zscore_rolling(base, 63)

def atrd_129_tr_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_129_tr_z_rank_63d"""
    base = _zscore_rolling(high - low, 21)
    return _rank_pct(base, 63)

def atrd_130_tr_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_130_tr_z_lvl_126d"""
    base = _zscore_rolling(high - low, 21)
    return _rolling_mean(base, 126)

def atrd_131_tr_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_131_tr_z_zscore_126d"""
    base = _zscore_rolling(high - low, 21)
    return _zscore_rolling(base, 126)

def atrd_132_tr_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_132_tr_z_rank_126d"""
    base = _zscore_rolling(high - low, 21)
    return _rank_pct(base, 126)

def atrd_133_tr_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_133_tr_z_lvl_252d"""
    base = _zscore_rolling(high - low, 21)
    return _rolling_mean(base, 252)

def atrd_134_tr_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_134_tr_z_zscore_252d"""
    base = _zscore_rolling(high - low, 21)
    return _zscore_rolling(base, 252)

def atrd_135_tr_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_135_tr_z_rank_252d"""
    base = _zscore_rolling(high - low, 21)
    return _rank_pct(base, 252)

def atrd_136_tr_sma_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_136_tr_sma_lvl_5d"""
    base = _safe_div(high-low, _rolling_mean(high-low, 21))
    return _rolling_mean(base, 5)

def atrd_137_tr_sma_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_137_tr_sma_zscore_5d"""
    base = _safe_div(high-low, _rolling_mean(high-low, 21))
    return _zscore_rolling(base, 5)

def atrd_138_tr_sma_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_138_tr_sma_rank_5d"""
    base = _safe_div(high-low, _rolling_mean(high-low, 21))
    return _rank_pct(base, 5)

def atrd_139_tr_sma_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_139_tr_sma_lvl_21d"""
    base = _safe_div(high-low, _rolling_mean(high-low, 21))
    return _rolling_mean(base, 21)

def atrd_140_tr_sma_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_140_tr_sma_zscore_21d"""
    base = _safe_div(high-low, _rolling_mean(high-low, 21))
    return _zscore_rolling(base, 21)

def atrd_141_tr_sma_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_141_tr_sma_rank_21d"""
    base = _safe_div(high-low, _rolling_mean(high-low, 21))
    return _rank_pct(base, 21)

def atrd_142_tr_sma_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_142_tr_sma_lvl_63d"""
    base = _safe_div(high-low, _rolling_mean(high-low, 21))
    return _rolling_mean(base, 63)

def atrd_143_tr_sma_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_143_tr_sma_zscore_63d"""
    base = _safe_div(high-low, _rolling_mean(high-low, 21))
    return _zscore_rolling(base, 63)

def atrd_144_tr_sma_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_144_tr_sma_rank_63d"""
    base = _safe_div(high-low, _rolling_mean(high-low, 21))
    return _rank_pct(base, 63)

def atrd_145_tr_sma_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_145_tr_sma_lvl_126d"""
    base = _safe_div(high-low, _rolling_mean(high-low, 21))
    return _rolling_mean(base, 126)

def atrd_146_tr_sma_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_146_tr_sma_zscore_126d"""
    base = _safe_div(high-low, _rolling_mean(high-low, 21))
    return _zscore_rolling(base, 126)

def atrd_147_tr_sma_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_147_tr_sma_rank_126d"""
    base = _safe_div(high-low, _rolling_mean(high-low, 21))
    return _rank_pct(base, 126)

def atrd_148_tr_sma_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_148_tr_sma_lvl_252d"""
    base = _safe_div(high-low, _rolling_mean(high-low, 21))
    return _rolling_mean(base, 252)

def atrd_149_tr_sma_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_149_tr_sma_zscore_252d"""
    base = _safe_div(high-low, _rolling_mean(high-low, 21))
    return _zscore_rolling(base, 252)

def atrd_150_tr_sma_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_150_tr_sma_rank_252d"""
    base = _safe_div(high-low, _rolling_mean(high-low, 21))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V87_REGISTRY_2 = {
    "atrd_076_tr_range_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_076_tr_range_lvl_5d},
    "atrd_077_tr_range_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_077_tr_range_zscore_5d},
    "atrd_078_tr_range_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_078_tr_range_rank_5d},
    "atrd_079_tr_range_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_079_tr_range_lvl_21d},
    "atrd_080_tr_range_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_080_tr_range_zscore_21d},
    "atrd_081_tr_range_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_081_tr_range_rank_21d},
    "atrd_082_tr_range_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_082_tr_range_lvl_63d},
    "atrd_083_tr_range_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_083_tr_range_zscore_63d},
    "atrd_084_tr_range_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_084_tr_range_rank_63d},
    "atrd_085_tr_range_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_085_tr_range_lvl_126d},
    "atrd_086_tr_range_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_086_tr_range_zscore_126d},
    "atrd_087_tr_range_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_087_tr_range_rank_126d},
    "atrd_088_tr_range_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_088_tr_range_lvl_252d},
    "atrd_089_tr_range_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_089_tr_range_zscore_252d},
    "atrd_090_tr_range_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_090_tr_range_rank_252d},
    "atrd_091_tr_gap_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_091_tr_gap_lvl_5d},
    "atrd_092_tr_gap_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_092_tr_gap_zscore_5d},
    "atrd_093_tr_gap_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_093_tr_gap_rank_5d},
    "atrd_094_tr_gap_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_094_tr_gap_lvl_21d},
    "atrd_095_tr_gap_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_095_tr_gap_zscore_21d},
    "atrd_096_tr_gap_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_096_tr_gap_rank_21d},
    "atrd_097_tr_gap_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_097_tr_gap_lvl_63d},
    "atrd_098_tr_gap_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_098_tr_gap_zscore_63d},
    "atrd_099_tr_gap_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_099_tr_gap_rank_63d},
    "atrd_100_tr_gap_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_100_tr_gap_lvl_126d},
    "atrd_101_tr_gap_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_101_tr_gap_zscore_126d},
    "atrd_102_tr_gap_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_102_tr_gap_rank_126d},
    "atrd_103_tr_gap_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_103_tr_gap_lvl_252d},
    "atrd_104_tr_gap_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_104_tr_gap_zscore_252d},
    "atrd_105_tr_gap_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_105_tr_gap_rank_252d},
    "atrd_106_tr_low_gap_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_106_tr_low_gap_lvl_5d},
    "atrd_107_tr_low_gap_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_107_tr_low_gap_zscore_5d},
    "atrd_108_tr_low_gap_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_108_tr_low_gap_rank_5d},
    "atrd_109_tr_low_gap_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_109_tr_low_gap_lvl_21d},
    "atrd_110_tr_low_gap_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_110_tr_low_gap_zscore_21d},
    "atrd_111_tr_low_gap_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_111_tr_low_gap_rank_21d},
    "atrd_112_tr_low_gap_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_112_tr_low_gap_lvl_63d},
    "atrd_113_tr_low_gap_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_113_tr_low_gap_zscore_63d},
    "atrd_114_tr_low_gap_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_114_tr_low_gap_rank_63d},
    "atrd_115_tr_low_gap_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_115_tr_low_gap_lvl_126d},
    "atrd_116_tr_low_gap_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_116_tr_low_gap_zscore_126d},
    "atrd_117_tr_low_gap_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_117_tr_low_gap_rank_126d},
    "atrd_118_tr_low_gap_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_118_tr_low_gap_lvl_252d},
    "atrd_119_tr_low_gap_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_119_tr_low_gap_zscore_252d},
    "atrd_120_tr_low_gap_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_120_tr_low_gap_rank_252d},
    "atrd_121_tr_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_121_tr_z_lvl_5d},
    "atrd_122_tr_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_122_tr_z_zscore_5d},
    "atrd_123_tr_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_123_tr_z_rank_5d},
    "atrd_124_tr_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_124_tr_z_lvl_21d},
    "atrd_125_tr_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_125_tr_z_zscore_21d},
    "atrd_126_tr_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_126_tr_z_rank_21d},
    "atrd_127_tr_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_127_tr_z_lvl_63d},
    "atrd_128_tr_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_128_tr_z_zscore_63d},
    "atrd_129_tr_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_129_tr_z_rank_63d},
    "atrd_130_tr_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_130_tr_z_lvl_126d},
    "atrd_131_tr_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_131_tr_z_zscore_126d},
    "atrd_132_tr_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_132_tr_z_rank_126d},
    "atrd_133_tr_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_133_tr_z_lvl_252d},
    "atrd_134_tr_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_134_tr_z_zscore_252d},
    "atrd_135_tr_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_135_tr_z_rank_252d},
    "atrd_136_tr_sma_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_136_tr_sma_lvl_5d},
    "atrd_137_tr_sma_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_137_tr_sma_zscore_5d},
    "atrd_138_tr_sma_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_138_tr_sma_rank_5d},
    "atrd_139_tr_sma_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_139_tr_sma_lvl_21d},
    "atrd_140_tr_sma_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_140_tr_sma_zscore_21d},
    "atrd_141_tr_sma_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_141_tr_sma_rank_21d},
    "atrd_142_tr_sma_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_142_tr_sma_lvl_63d},
    "atrd_143_tr_sma_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_143_tr_sma_zscore_63d},
    "atrd_144_tr_sma_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_144_tr_sma_rank_63d},
    "atrd_145_tr_sma_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_145_tr_sma_lvl_126d},
    "atrd_146_tr_sma_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_146_tr_sma_zscore_126d},
    "atrd_147_tr_sma_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_147_tr_sma_rank_126d},
    "atrd_148_tr_sma_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_148_tr_sma_lvl_252d},
    "atrd_149_tr_sma_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_149_tr_sma_zscore_252d},
    "atrd_150_tr_sma_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_150_tr_sma_rank_252d},
}
