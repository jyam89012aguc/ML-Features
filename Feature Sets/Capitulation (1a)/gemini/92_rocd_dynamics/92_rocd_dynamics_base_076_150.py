"""
92_rocd_dynamics — Base Features 076-150
Domain: rocd_dynamics
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

def rocd_076_roc_abs_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_076_roc_abs_lvl_5d"""
    base = close.pct_change(21).abs()
    return _rolling_mean(base, 5)

def rocd_077_roc_abs_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_077_roc_abs_zscore_5d"""
    base = close.pct_change(21).abs()
    return _zscore_rolling(base, 5)

def rocd_078_roc_abs_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_078_roc_abs_rank_5d"""
    base = close.pct_change(21).abs()
    return _rank_pct(base, 5)

def rocd_079_roc_abs_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_079_roc_abs_lvl_21d"""
    base = close.pct_change(21).abs()
    return _rolling_mean(base, 21)

def rocd_080_roc_abs_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_080_roc_abs_zscore_21d"""
    base = close.pct_change(21).abs()
    return _zscore_rolling(base, 21)

def rocd_081_roc_abs_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_081_roc_abs_rank_21d"""
    base = close.pct_change(21).abs()
    return _rank_pct(base, 21)

def rocd_082_roc_abs_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_082_roc_abs_lvl_63d"""
    base = close.pct_change(21).abs()
    return _rolling_mean(base, 63)

def rocd_083_roc_abs_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_083_roc_abs_zscore_63d"""
    base = close.pct_change(21).abs()
    return _zscore_rolling(base, 63)

def rocd_084_roc_abs_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_084_roc_abs_rank_63d"""
    base = close.pct_change(21).abs()
    return _rank_pct(base, 63)

def rocd_085_roc_abs_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_085_roc_abs_lvl_126d"""
    base = close.pct_change(21).abs()
    return _rolling_mean(base, 126)

def rocd_086_roc_abs_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_086_roc_abs_zscore_126d"""
    base = close.pct_change(21).abs()
    return _zscore_rolling(base, 126)

def rocd_087_roc_abs_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_087_roc_abs_rank_126d"""
    base = close.pct_change(21).abs()
    return _rank_pct(base, 126)

def rocd_088_roc_abs_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_088_roc_abs_lvl_252d"""
    base = close.pct_change(21).abs()
    return _rolling_mean(base, 252)

def rocd_089_roc_abs_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_089_roc_abs_zscore_252d"""
    base = close.pct_change(21).abs()
    return _zscore_rolling(base, 252)

def rocd_090_roc_abs_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_090_roc_abs_rank_252d"""
    base = close.pct_change(21).abs()
    return _rank_pct(base, 252)

def rocd_091_roc_accel_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_091_roc_accel_lvl_5d"""
    base = close.pct_change(21).diff()
    return _rolling_mean(base, 5)

def rocd_092_roc_accel_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_092_roc_accel_zscore_5d"""
    base = close.pct_change(21).diff()
    return _zscore_rolling(base, 5)

def rocd_093_roc_accel_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_093_roc_accel_rank_5d"""
    base = close.pct_change(21).diff()
    return _rank_pct(base, 5)

def rocd_094_roc_accel_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_094_roc_accel_lvl_21d"""
    base = close.pct_change(21).diff()
    return _rolling_mean(base, 21)

def rocd_095_roc_accel_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_095_roc_accel_zscore_21d"""
    base = close.pct_change(21).diff()
    return _zscore_rolling(base, 21)

def rocd_096_roc_accel_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_096_roc_accel_rank_21d"""
    base = close.pct_change(21).diff()
    return _rank_pct(base, 21)

def rocd_097_roc_accel_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_097_roc_accel_lvl_63d"""
    base = close.pct_change(21).diff()
    return _rolling_mean(base, 63)

def rocd_098_roc_accel_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_098_roc_accel_zscore_63d"""
    base = close.pct_change(21).diff()
    return _zscore_rolling(base, 63)

def rocd_099_roc_accel_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_099_roc_accel_rank_63d"""
    base = close.pct_change(21).diff()
    return _rank_pct(base, 63)

def rocd_100_roc_accel_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_100_roc_accel_lvl_126d"""
    base = close.pct_change(21).diff()
    return _rolling_mean(base, 126)

def rocd_101_roc_accel_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_101_roc_accel_zscore_126d"""
    base = close.pct_change(21).diff()
    return _zscore_rolling(base, 126)

def rocd_102_roc_accel_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_102_roc_accel_rank_126d"""
    base = close.pct_change(21).diff()
    return _rank_pct(base, 126)

def rocd_103_roc_accel_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_103_roc_accel_lvl_252d"""
    base = close.pct_change(21).diff()
    return _rolling_mean(base, 252)

def rocd_104_roc_accel_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_104_roc_accel_zscore_252d"""
    base = close.pct_change(21).diff()
    return _zscore_rolling(base, 252)

def rocd_105_roc_accel_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_105_roc_accel_rank_252d"""
    base = close.pct_change(21).diff()
    return _rank_pct(base, 252)

def rocd_106_roc_log_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_106_roc_log_lvl_5d"""
    base = np.log(close.pct_change(21).abs().clip(lower=_EPS))
    return _rolling_mean(base, 5)

def rocd_107_roc_log_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_107_roc_log_zscore_5d"""
    base = np.log(close.pct_change(21).abs().clip(lower=_EPS))
    return _zscore_rolling(base, 5)

def rocd_108_roc_log_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_108_roc_log_rank_5d"""
    base = np.log(close.pct_change(21).abs().clip(lower=_EPS))
    return _rank_pct(base, 5)

def rocd_109_roc_log_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_109_roc_log_lvl_21d"""
    base = np.log(close.pct_change(21).abs().clip(lower=_EPS))
    return _rolling_mean(base, 21)

def rocd_110_roc_log_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_110_roc_log_zscore_21d"""
    base = np.log(close.pct_change(21).abs().clip(lower=_EPS))
    return _zscore_rolling(base, 21)

def rocd_111_roc_log_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_111_roc_log_rank_21d"""
    base = np.log(close.pct_change(21).abs().clip(lower=_EPS))
    return _rank_pct(base, 21)

def rocd_112_roc_log_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_112_roc_log_lvl_63d"""
    base = np.log(close.pct_change(21).abs().clip(lower=_EPS))
    return _rolling_mean(base, 63)

def rocd_113_roc_log_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_113_roc_log_zscore_63d"""
    base = np.log(close.pct_change(21).abs().clip(lower=_EPS))
    return _zscore_rolling(base, 63)

def rocd_114_roc_log_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_114_roc_log_rank_63d"""
    base = np.log(close.pct_change(21).abs().clip(lower=_EPS))
    return _rank_pct(base, 63)

def rocd_115_roc_log_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_115_roc_log_lvl_126d"""
    base = np.log(close.pct_change(21).abs().clip(lower=_EPS))
    return _rolling_mean(base, 126)

def rocd_116_roc_log_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_116_roc_log_zscore_126d"""
    base = np.log(close.pct_change(21).abs().clip(lower=_EPS))
    return _zscore_rolling(base, 126)

def rocd_117_roc_log_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_117_roc_log_rank_126d"""
    base = np.log(close.pct_change(21).abs().clip(lower=_EPS))
    return _rank_pct(base, 126)

def rocd_118_roc_log_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_118_roc_log_lvl_252d"""
    base = np.log(close.pct_change(21).abs().clip(lower=_EPS))
    return _rolling_mean(base, 252)

def rocd_119_roc_log_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_119_roc_log_zscore_252d"""
    base = np.log(close.pct_change(21).abs().clip(lower=_EPS))
    return _zscore_rolling(base, 252)

def rocd_120_roc_log_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_120_roc_log_rank_252d"""
    base = np.log(close.pct_change(21).abs().clip(lower=_EPS))
    return _rank_pct(base, 252)

def rocd_121_roc_skew_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_121_roc_skew_lvl_5d"""
    base = close.pct_change(1).rolling(21).skew()
    return _rolling_mean(base, 5)

def rocd_122_roc_skew_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_122_roc_skew_zscore_5d"""
    base = close.pct_change(1).rolling(21).skew()
    return _zscore_rolling(base, 5)

def rocd_123_roc_skew_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_123_roc_skew_rank_5d"""
    base = close.pct_change(1).rolling(21).skew()
    return _rank_pct(base, 5)

def rocd_124_roc_skew_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_124_roc_skew_lvl_21d"""
    base = close.pct_change(1).rolling(21).skew()
    return _rolling_mean(base, 21)

def rocd_125_roc_skew_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_125_roc_skew_zscore_21d"""
    base = close.pct_change(1).rolling(21).skew()
    return _zscore_rolling(base, 21)

def rocd_126_roc_skew_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_126_roc_skew_rank_21d"""
    base = close.pct_change(1).rolling(21).skew()
    return _rank_pct(base, 21)

def rocd_127_roc_skew_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_127_roc_skew_lvl_63d"""
    base = close.pct_change(1).rolling(21).skew()
    return _rolling_mean(base, 63)

def rocd_128_roc_skew_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_128_roc_skew_zscore_63d"""
    base = close.pct_change(1).rolling(21).skew()
    return _zscore_rolling(base, 63)

def rocd_129_roc_skew_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_129_roc_skew_rank_63d"""
    base = close.pct_change(1).rolling(21).skew()
    return _rank_pct(base, 63)

def rocd_130_roc_skew_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_130_roc_skew_lvl_126d"""
    base = close.pct_change(1).rolling(21).skew()
    return _rolling_mean(base, 126)

def rocd_131_roc_skew_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_131_roc_skew_zscore_126d"""
    base = close.pct_change(1).rolling(21).skew()
    return _zscore_rolling(base, 126)

def rocd_132_roc_skew_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_132_roc_skew_rank_126d"""
    base = close.pct_change(1).rolling(21).skew()
    return _rank_pct(base, 126)

def rocd_133_roc_skew_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_133_roc_skew_lvl_252d"""
    base = close.pct_change(1).rolling(21).skew()
    return _rolling_mean(base, 252)

def rocd_134_roc_skew_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_134_roc_skew_zscore_252d"""
    base = close.pct_change(1).rolling(21).skew()
    return _zscore_rolling(base, 252)

def rocd_135_roc_skew_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_135_roc_skew_rank_252d"""
    base = close.pct_change(1).rolling(21).skew()
    return _rank_pct(base, 252)

def rocd_136_roc_kurt_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_136_roc_kurt_lvl_5d"""
    base = close.pct_change(1).rolling(21).kurt()
    return _rolling_mean(base, 5)

def rocd_137_roc_kurt_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_137_roc_kurt_zscore_5d"""
    base = close.pct_change(1).rolling(21).kurt()
    return _zscore_rolling(base, 5)

def rocd_138_roc_kurt_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_138_roc_kurt_rank_5d"""
    base = close.pct_change(1).rolling(21).kurt()
    return _rank_pct(base, 5)

def rocd_139_roc_kurt_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_139_roc_kurt_lvl_21d"""
    base = close.pct_change(1).rolling(21).kurt()
    return _rolling_mean(base, 21)

def rocd_140_roc_kurt_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_140_roc_kurt_zscore_21d"""
    base = close.pct_change(1).rolling(21).kurt()
    return _zscore_rolling(base, 21)

def rocd_141_roc_kurt_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_141_roc_kurt_rank_21d"""
    base = close.pct_change(1).rolling(21).kurt()
    return _rank_pct(base, 21)

def rocd_142_roc_kurt_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_142_roc_kurt_lvl_63d"""
    base = close.pct_change(1).rolling(21).kurt()
    return _rolling_mean(base, 63)

def rocd_143_roc_kurt_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_143_roc_kurt_zscore_63d"""
    base = close.pct_change(1).rolling(21).kurt()
    return _zscore_rolling(base, 63)

def rocd_144_roc_kurt_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_144_roc_kurt_rank_63d"""
    base = close.pct_change(1).rolling(21).kurt()
    return _rank_pct(base, 63)

def rocd_145_roc_kurt_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_145_roc_kurt_lvl_126d"""
    base = close.pct_change(1).rolling(21).kurt()
    return _rolling_mean(base, 126)

def rocd_146_roc_kurt_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_146_roc_kurt_zscore_126d"""
    base = close.pct_change(1).rolling(21).kurt()
    return _zscore_rolling(base, 126)

def rocd_147_roc_kurt_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_147_roc_kurt_rank_126d"""
    base = close.pct_change(1).rolling(21).kurt()
    return _rank_pct(base, 126)

def rocd_148_roc_kurt_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_148_roc_kurt_lvl_252d"""
    base = close.pct_change(1).rolling(21).kurt()
    return _rolling_mean(base, 252)

def rocd_149_roc_kurt_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_149_roc_kurt_zscore_252d"""
    base = close.pct_change(1).rolling(21).kurt()
    return _zscore_rolling(base, 252)

def rocd_150_roc_kurt_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_150_roc_kurt_rank_252d"""
    base = close.pct_change(1).rolling(21).kurt()
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V92_REGISTRY_2 = {
    "rocd_076_roc_abs_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_076_roc_abs_lvl_5d},
    "rocd_077_roc_abs_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_077_roc_abs_zscore_5d},
    "rocd_078_roc_abs_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_078_roc_abs_rank_5d},
    "rocd_079_roc_abs_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_079_roc_abs_lvl_21d},
    "rocd_080_roc_abs_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_080_roc_abs_zscore_21d},
    "rocd_081_roc_abs_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_081_roc_abs_rank_21d},
    "rocd_082_roc_abs_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_082_roc_abs_lvl_63d},
    "rocd_083_roc_abs_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_083_roc_abs_zscore_63d},
    "rocd_084_roc_abs_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_084_roc_abs_rank_63d},
    "rocd_085_roc_abs_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_085_roc_abs_lvl_126d},
    "rocd_086_roc_abs_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_086_roc_abs_zscore_126d},
    "rocd_087_roc_abs_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_087_roc_abs_rank_126d},
    "rocd_088_roc_abs_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_088_roc_abs_lvl_252d},
    "rocd_089_roc_abs_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_089_roc_abs_zscore_252d},
    "rocd_090_roc_abs_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_090_roc_abs_rank_252d},
    "rocd_091_roc_accel_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_091_roc_accel_lvl_5d},
    "rocd_092_roc_accel_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_092_roc_accel_zscore_5d},
    "rocd_093_roc_accel_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_093_roc_accel_rank_5d},
    "rocd_094_roc_accel_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_094_roc_accel_lvl_21d},
    "rocd_095_roc_accel_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_095_roc_accel_zscore_21d},
    "rocd_096_roc_accel_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_096_roc_accel_rank_21d},
    "rocd_097_roc_accel_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_097_roc_accel_lvl_63d},
    "rocd_098_roc_accel_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_098_roc_accel_zscore_63d},
    "rocd_099_roc_accel_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_099_roc_accel_rank_63d},
    "rocd_100_roc_accel_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_100_roc_accel_lvl_126d},
    "rocd_101_roc_accel_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_101_roc_accel_zscore_126d},
    "rocd_102_roc_accel_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_102_roc_accel_rank_126d},
    "rocd_103_roc_accel_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_103_roc_accel_lvl_252d},
    "rocd_104_roc_accel_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_104_roc_accel_zscore_252d},
    "rocd_105_roc_accel_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_105_roc_accel_rank_252d},
    "rocd_106_roc_log_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_106_roc_log_lvl_5d},
    "rocd_107_roc_log_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_107_roc_log_zscore_5d},
    "rocd_108_roc_log_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_108_roc_log_rank_5d},
    "rocd_109_roc_log_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_109_roc_log_lvl_21d},
    "rocd_110_roc_log_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_110_roc_log_zscore_21d},
    "rocd_111_roc_log_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_111_roc_log_rank_21d},
    "rocd_112_roc_log_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_112_roc_log_lvl_63d},
    "rocd_113_roc_log_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_113_roc_log_zscore_63d},
    "rocd_114_roc_log_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_114_roc_log_rank_63d},
    "rocd_115_roc_log_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_115_roc_log_lvl_126d},
    "rocd_116_roc_log_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_116_roc_log_zscore_126d},
    "rocd_117_roc_log_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_117_roc_log_rank_126d},
    "rocd_118_roc_log_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_118_roc_log_lvl_252d},
    "rocd_119_roc_log_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_119_roc_log_zscore_252d},
    "rocd_120_roc_log_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_120_roc_log_rank_252d},
    "rocd_121_roc_skew_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_121_roc_skew_lvl_5d},
    "rocd_122_roc_skew_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_122_roc_skew_zscore_5d},
    "rocd_123_roc_skew_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_123_roc_skew_rank_5d},
    "rocd_124_roc_skew_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_124_roc_skew_lvl_21d},
    "rocd_125_roc_skew_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_125_roc_skew_zscore_21d},
    "rocd_126_roc_skew_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_126_roc_skew_rank_21d},
    "rocd_127_roc_skew_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_127_roc_skew_lvl_63d},
    "rocd_128_roc_skew_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_128_roc_skew_zscore_63d},
    "rocd_129_roc_skew_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_129_roc_skew_rank_63d},
    "rocd_130_roc_skew_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_130_roc_skew_lvl_126d},
    "rocd_131_roc_skew_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_131_roc_skew_zscore_126d},
    "rocd_132_roc_skew_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_132_roc_skew_rank_126d},
    "rocd_133_roc_skew_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_133_roc_skew_lvl_252d},
    "rocd_134_roc_skew_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_134_roc_skew_zscore_252d},
    "rocd_135_roc_skew_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_135_roc_skew_rank_252d},
    "rocd_136_roc_kurt_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_136_roc_kurt_lvl_5d},
    "rocd_137_roc_kurt_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_137_roc_kurt_zscore_5d},
    "rocd_138_roc_kurt_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_138_roc_kurt_rank_5d},
    "rocd_139_roc_kurt_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_139_roc_kurt_lvl_21d},
    "rocd_140_roc_kurt_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_140_roc_kurt_zscore_21d},
    "rocd_141_roc_kurt_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_141_roc_kurt_rank_21d},
    "rocd_142_roc_kurt_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_142_roc_kurt_lvl_63d},
    "rocd_143_roc_kurt_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_143_roc_kurt_zscore_63d},
    "rocd_144_roc_kurt_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_144_roc_kurt_rank_63d},
    "rocd_145_roc_kurt_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_145_roc_kurt_lvl_126d},
    "rocd_146_roc_kurt_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_146_roc_kurt_zscore_126d},
    "rocd_147_roc_kurt_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_147_roc_kurt_rank_126d},
    "rocd_148_roc_kurt_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_148_roc_kurt_lvl_252d},
    "rocd_149_roc_kurt_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_149_roc_kurt_zscore_252d},
    "rocd_150_roc_kurt_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_150_roc_kurt_rank_252d},
}
