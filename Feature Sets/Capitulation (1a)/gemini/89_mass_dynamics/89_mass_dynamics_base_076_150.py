"""
89_mass_dynamics — Base Features 076-150
Domain: mass_dynamics
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

def mass_076_range_ratio_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_076_range_ratio_lvl_5d"""
    base = _safe_div(high - low, _rolling_mean(high - low, 252))
    return _rolling_mean(base, 5)

def mass_077_range_ratio_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_077_range_ratio_zscore_5d"""
    base = _safe_div(high - low, _rolling_mean(high - low, 252))
    return _zscore_rolling(base, 5)

def mass_078_range_ratio_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_078_range_ratio_rank_5d"""
    base = _safe_div(high - low, _rolling_mean(high - low, 252))
    return _rank_pct(base, 5)

def mass_079_range_ratio_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_079_range_ratio_lvl_21d"""
    base = _safe_div(high - low, _rolling_mean(high - low, 252))
    return _rolling_mean(base, 21)

def mass_080_range_ratio_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_080_range_ratio_zscore_21d"""
    base = _safe_div(high - low, _rolling_mean(high - low, 252))
    return _zscore_rolling(base, 21)

def mass_081_range_ratio_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_081_range_ratio_rank_21d"""
    base = _safe_div(high - low, _rolling_mean(high - low, 252))
    return _rank_pct(base, 21)

def mass_082_range_ratio_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_082_range_ratio_lvl_63d"""
    base = _safe_div(high - low, _rolling_mean(high - low, 252))
    return _rolling_mean(base, 63)

def mass_083_range_ratio_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_083_range_ratio_zscore_63d"""
    base = _safe_div(high - low, _rolling_mean(high - low, 252))
    return _zscore_rolling(base, 63)

def mass_084_range_ratio_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_084_range_ratio_rank_63d"""
    base = _safe_div(high - low, _rolling_mean(high - low, 252))
    return _rank_pct(base, 63)

def mass_085_range_ratio_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_085_range_ratio_lvl_126d"""
    base = _safe_div(high - low, _rolling_mean(high - low, 252))
    return _rolling_mean(base, 126)

def mass_086_range_ratio_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_086_range_ratio_zscore_126d"""
    base = _safe_div(high - low, _rolling_mean(high - low, 252))
    return _zscore_rolling(base, 126)

def mass_087_range_ratio_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_087_range_ratio_rank_126d"""
    base = _safe_div(high - low, _rolling_mean(high - low, 252))
    return _rank_pct(base, 126)

def mass_088_range_ratio_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_088_range_ratio_lvl_252d"""
    base = _safe_div(high - low, _rolling_mean(high - low, 252))
    return _rolling_mean(base, 252)

def mass_089_range_ratio_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_089_range_ratio_zscore_252d"""
    base = _safe_div(high - low, _rolling_mean(high - low, 252))
    return _zscore_rolling(base, 252)

def mass_090_range_ratio_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_090_range_ratio_rank_252d"""
    base = _safe_div(high - low, _rolling_mean(high - low, 252))
    return _rank_pct(base, 252)

def mass_091_range_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_091_range_z_lvl_5d"""
    base = _zscore_rolling(high - low, 21)
    return _rolling_mean(base, 5)

def mass_092_range_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_092_range_z_zscore_5d"""
    base = _zscore_rolling(high - low, 21)
    return _zscore_rolling(base, 5)

def mass_093_range_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_093_range_z_rank_5d"""
    base = _zscore_rolling(high - low, 21)
    return _rank_pct(base, 5)

def mass_094_range_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_094_range_z_lvl_21d"""
    base = _zscore_rolling(high - low, 21)
    return _rolling_mean(base, 21)

def mass_095_range_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_095_range_z_zscore_21d"""
    base = _zscore_rolling(high - low, 21)
    return _zscore_rolling(base, 21)

def mass_096_range_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_096_range_z_rank_21d"""
    base = _zscore_rolling(high - low, 21)
    return _rank_pct(base, 21)

def mass_097_range_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_097_range_z_lvl_63d"""
    base = _zscore_rolling(high - low, 21)
    return _rolling_mean(base, 63)

def mass_098_range_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_098_range_z_zscore_63d"""
    base = _zscore_rolling(high - low, 21)
    return _zscore_rolling(base, 63)

def mass_099_range_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_099_range_z_rank_63d"""
    base = _zscore_rolling(high - low, 21)
    return _rank_pct(base, 63)

def mass_100_range_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_100_range_z_lvl_126d"""
    base = _zscore_rolling(high - low, 21)
    return _rolling_mean(base, 126)

def mass_101_range_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_101_range_z_zscore_126d"""
    base = _zscore_rolling(high - low, 21)
    return _zscore_rolling(base, 126)

def mass_102_range_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_102_range_z_rank_126d"""
    base = _zscore_rolling(high - low, 21)
    return _rank_pct(base, 126)

def mass_103_range_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_103_range_z_lvl_252d"""
    base = _zscore_rolling(high - low, 21)
    return _rolling_mean(base, 252)

def mass_104_range_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_104_range_z_zscore_252d"""
    base = _zscore_rolling(high - low, 21)
    return _zscore_rolling(base, 252)

def mass_105_range_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_105_range_z_rank_252d"""
    base = _zscore_rolling(high - low, 21)
    return _rank_pct(base, 252)

def mass_106_range_pct_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_106_range_pct_lvl_5d"""
    base = _rank_pct(high - low, 252)
    return _rolling_mean(base, 5)

def mass_107_range_pct_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_107_range_pct_zscore_5d"""
    base = _rank_pct(high - low, 252)
    return _zscore_rolling(base, 5)

def mass_108_range_pct_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_108_range_pct_rank_5d"""
    base = _rank_pct(high - low, 252)
    return _rank_pct(base, 5)

def mass_109_range_pct_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_109_range_pct_lvl_21d"""
    base = _rank_pct(high - low, 252)
    return _rolling_mean(base, 21)

def mass_110_range_pct_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_110_range_pct_zscore_21d"""
    base = _rank_pct(high - low, 252)
    return _zscore_rolling(base, 21)

def mass_111_range_pct_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_111_range_pct_rank_21d"""
    base = _rank_pct(high - low, 252)
    return _rank_pct(base, 21)

def mass_112_range_pct_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_112_range_pct_lvl_63d"""
    base = _rank_pct(high - low, 252)
    return _rolling_mean(base, 63)

def mass_113_range_pct_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_113_range_pct_zscore_63d"""
    base = _rank_pct(high - low, 252)
    return _zscore_rolling(base, 63)

def mass_114_range_pct_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_114_range_pct_rank_63d"""
    base = _rank_pct(high - low, 252)
    return _rank_pct(base, 63)

def mass_115_range_pct_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_115_range_pct_lvl_126d"""
    base = _rank_pct(high - low, 252)
    return _rolling_mean(base, 126)

def mass_116_range_pct_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_116_range_pct_zscore_126d"""
    base = _rank_pct(high - low, 252)
    return _zscore_rolling(base, 126)

def mass_117_range_pct_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_117_range_pct_rank_126d"""
    base = _rank_pct(high - low, 252)
    return _rank_pct(base, 126)

def mass_118_range_pct_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_118_range_pct_lvl_252d"""
    base = _rank_pct(high - low, 252)
    return _rolling_mean(base, 252)

def mass_119_range_pct_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_119_range_pct_zscore_252d"""
    base = _rank_pct(high - low, 252)
    return _zscore_rolling(base, 252)

def mass_120_range_pct_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_120_range_pct_rank_252d"""
    base = _rank_pct(high - low, 252)
    return _rank_pct(base, 252)

def mass_121_range_accel_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_121_range_accel_lvl_5d"""
    base = (high - low).diff()
    return _rolling_mean(base, 5)

def mass_122_range_accel_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_122_range_accel_zscore_5d"""
    base = (high - low).diff()
    return _zscore_rolling(base, 5)

def mass_123_range_accel_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_123_range_accel_rank_5d"""
    base = (high - low).diff()
    return _rank_pct(base, 5)

def mass_124_range_accel_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_124_range_accel_lvl_21d"""
    base = (high - low).diff()
    return _rolling_mean(base, 21)

def mass_125_range_accel_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_125_range_accel_zscore_21d"""
    base = (high - low).diff()
    return _zscore_rolling(base, 21)

def mass_126_range_accel_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_126_range_accel_rank_21d"""
    base = (high - low).diff()
    return _rank_pct(base, 21)

def mass_127_range_accel_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_127_range_accel_lvl_63d"""
    base = (high - low).diff()
    return _rolling_mean(base, 63)

def mass_128_range_accel_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_128_range_accel_zscore_63d"""
    base = (high - low).diff()
    return _zscore_rolling(base, 63)

def mass_129_range_accel_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_129_range_accel_rank_63d"""
    base = (high - low).diff()
    return _rank_pct(base, 63)

def mass_130_range_accel_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_130_range_accel_lvl_126d"""
    base = (high - low).diff()
    return _rolling_mean(base, 126)

def mass_131_range_accel_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_131_range_accel_zscore_126d"""
    base = (high - low).diff()
    return _zscore_rolling(base, 126)

def mass_132_range_accel_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_132_range_accel_rank_126d"""
    base = (high - low).diff()
    return _rank_pct(base, 126)

def mass_133_range_accel_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_133_range_accel_lvl_252d"""
    base = (high - low).diff()
    return _rolling_mean(base, 252)

def mass_134_range_accel_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_134_range_accel_zscore_252d"""
    base = (high - low).diff()
    return _zscore_rolling(base, 252)

def mass_135_range_accel_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_135_range_accel_rank_252d"""
    base = (high - low).diff()
    return _rank_pct(base, 252)

def mass_136_range_log_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_136_range_log_lvl_5d"""
    base = np.log((high - low).clip(lower=_EPS))
    return _rolling_mean(base, 5)

def mass_137_range_log_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_137_range_log_zscore_5d"""
    base = np.log((high - low).clip(lower=_EPS))
    return _zscore_rolling(base, 5)

def mass_138_range_log_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_138_range_log_rank_5d"""
    base = np.log((high - low).clip(lower=_EPS))
    return _rank_pct(base, 5)

def mass_139_range_log_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_139_range_log_lvl_21d"""
    base = np.log((high - low).clip(lower=_EPS))
    return _rolling_mean(base, 21)

def mass_140_range_log_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_140_range_log_zscore_21d"""
    base = np.log((high - low).clip(lower=_EPS))
    return _zscore_rolling(base, 21)

def mass_141_range_log_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_141_range_log_rank_21d"""
    base = np.log((high - low).clip(lower=_EPS))
    return _rank_pct(base, 21)

def mass_142_range_log_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_142_range_log_lvl_63d"""
    base = np.log((high - low).clip(lower=_EPS))
    return _rolling_mean(base, 63)

def mass_143_range_log_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_143_range_log_zscore_63d"""
    base = np.log((high - low).clip(lower=_EPS))
    return _zscore_rolling(base, 63)

def mass_144_range_log_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_144_range_log_rank_63d"""
    base = np.log((high - low).clip(lower=_EPS))
    return _rank_pct(base, 63)

def mass_145_range_log_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_145_range_log_lvl_126d"""
    base = np.log((high - low).clip(lower=_EPS))
    return _rolling_mean(base, 126)

def mass_146_range_log_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_146_range_log_zscore_126d"""
    base = np.log((high - low).clip(lower=_EPS))
    return _zscore_rolling(base, 126)

def mass_147_range_log_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_147_range_log_rank_126d"""
    base = np.log((high - low).clip(lower=_EPS))
    return _rank_pct(base, 126)

def mass_148_range_log_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_148_range_log_lvl_252d"""
    base = np.log((high - low).clip(lower=_EPS))
    return _rolling_mean(base, 252)

def mass_149_range_log_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_149_range_log_zscore_252d"""
    base = np.log((high - low).clip(lower=_EPS))
    return _zscore_rolling(base, 252)

def mass_150_range_log_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_150_range_log_rank_252d"""
    base = np.log((high - low).clip(lower=_EPS))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V89_REGISTRY_2 = {
    "mass_076_range_ratio_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_076_range_ratio_lvl_5d},
    "mass_077_range_ratio_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_077_range_ratio_zscore_5d},
    "mass_078_range_ratio_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_078_range_ratio_rank_5d},
    "mass_079_range_ratio_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_079_range_ratio_lvl_21d},
    "mass_080_range_ratio_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_080_range_ratio_zscore_21d},
    "mass_081_range_ratio_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_081_range_ratio_rank_21d},
    "mass_082_range_ratio_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_082_range_ratio_lvl_63d},
    "mass_083_range_ratio_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_083_range_ratio_zscore_63d},
    "mass_084_range_ratio_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_084_range_ratio_rank_63d},
    "mass_085_range_ratio_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_085_range_ratio_lvl_126d},
    "mass_086_range_ratio_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_086_range_ratio_zscore_126d},
    "mass_087_range_ratio_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_087_range_ratio_rank_126d},
    "mass_088_range_ratio_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_088_range_ratio_lvl_252d},
    "mass_089_range_ratio_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_089_range_ratio_zscore_252d},
    "mass_090_range_ratio_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_090_range_ratio_rank_252d},
    "mass_091_range_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_091_range_z_lvl_5d},
    "mass_092_range_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_092_range_z_zscore_5d},
    "mass_093_range_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_093_range_z_rank_5d},
    "mass_094_range_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_094_range_z_lvl_21d},
    "mass_095_range_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_095_range_z_zscore_21d},
    "mass_096_range_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_096_range_z_rank_21d},
    "mass_097_range_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_097_range_z_lvl_63d},
    "mass_098_range_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_098_range_z_zscore_63d},
    "mass_099_range_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_099_range_z_rank_63d},
    "mass_100_range_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_100_range_z_lvl_126d},
    "mass_101_range_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_101_range_z_zscore_126d},
    "mass_102_range_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_102_range_z_rank_126d},
    "mass_103_range_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_103_range_z_lvl_252d},
    "mass_104_range_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_104_range_z_zscore_252d},
    "mass_105_range_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_105_range_z_rank_252d},
    "mass_106_range_pct_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_106_range_pct_lvl_5d},
    "mass_107_range_pct_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_107_range_pct_zscore_5d},
    "mass_108_range_pct_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_108_range_pct_rank_5d},
    "mass_109_range_pct_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_109_range_pct_lvl_21d},
    "mass_110_range_pct_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_110_range_pct_zscore_21d},
    "mass_111_range_pct_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_111_range_pct_rank_21d},
    "mass_112_range_pct_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_112_range_pct_lvl_63d},
    "mass_113_range_pct_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_113_range_pct_zscore_63d},
    "mass_114_range_pct_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_114_range_pct_rank_63d},
    "mass_115_range_pct_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_115_range_pct_lvl_126d},
    "mass_116_range_pct_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_116_range_pct_zscore_126d},
    "mass_117_range_pct_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_117_range_pct_rank_126d},
    "mass_118_range_pct_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_118_range_pct_lvl_252d},
    "mass_119_range_pct_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_119_range_pct_zscore_252d},
    "mass_120_range_pct_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_120_range_pct_rank_252d},
    "mass_121_range_accel_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_121_range_accel_lvl_5d},
    "mass_122_range_accel_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_122_range_accel_zscore_5d},
    "mass_123_range_accel_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_123_range_accel_rank_5d},
    "mass_124_range_accel_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_124_range_accel_lvl_21d},
    "mass_125_range_accel_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_125_range_accel_zscore_21d},
    "mass_126_range_accel_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_126_range_accel_rank_21d},
    "mass_127_range_accel_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_127_range_accel_lvl_63d},
    "mass_128_range_accel_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_128_range_accel_zscore_63d},
    "mass_129_range_accel_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_129_range_accel_rank_63d},
    "mass_130_range_accel_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_130_range_accel_lvl_126d},
    "mass_131_range_accel_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_131_range_accel_zscore_126d},
    "mass_132_range_accel_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_132_range_accel_rank_126d},
    "mass_133_range_accel_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_133_range_accel_lvl_252d},
    "mass_134_range_accel_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_134_range_accel_zscore_252d},
    "mass_135_range_accel_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_135_range_accel_rank_252d},
    "mass_136_range_log_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_136_range_log_lvl_5d},
    "mass_137_range_log_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_137_range_log_zscore_5d},
    "mass_138_range_log_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_138_range_log_rank_5d},
    "mass_139_range_log_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_139_range_log_lvl_21d},
    "mass_140_range_log_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_140_range_log_zscore_21d},
    "mass_141_range_log_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_141_range_log_rank_21d},
    "mass_142_range_log_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_142_range_log_lvl_63d},
    "mass_143_range_log_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_143_range_log_zscore_63d},
    "mass_144_range_log_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_144_range_log_rank_63d},
    "mass_145_range_log_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_145_range_log_lvl_126d},
    "mass_146_range_log_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_146_range_log_zscore_126d},
    "mass_147_range_log_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_147_range_log_rank_126d},
    "mass_148_range_log_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_148_range_log_lvl_252d},
    "mass_149_range_log_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_149_range_log_zscore_252d},
    "mass_150_range_log_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_150_range_log_rank_252d},
}
