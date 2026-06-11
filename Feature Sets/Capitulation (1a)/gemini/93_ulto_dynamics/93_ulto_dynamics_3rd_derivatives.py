"""
93_ulto_dynamics — 3rd Derivatives (Acceleration)
Domain: ulto_dynamics
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

def ulto_176_bp_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_176_bp_accel_5d"""
    return (close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(5).diff(21)

def ulto_177_bp_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_177_bp_accel_21d"""
    return (close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(21).diff(21)

def ulto_178_bp_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_178_bp_accel_63d"""
    return (close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(63).diff(21)

def ulto_179_bp_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_179_bp_accel_126d"""
    return (close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(126).diff(21)

def ulto_180_bp_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_180_bp_accel_252d"""
    return (close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(252).diff(21)

def ulto_181_tr_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_181_tr_accel_5d"""
    return (pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(5).diff(21)

def ulto_182_tr_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_182_tr_accel_21d"""
    return (pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(21).diff(21)

def ulto_183_tr_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_183_tr_accel_63d"""
    return (pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(63).diff(21)

def ulto_184_tr_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_184_tr_accel_126d"""
    return (pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(126).diff(21)

def ulto_185_tr_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_185_tr_accel_252d"""
    return (pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(252).diff(21)

def ulto_186_avg_7_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_186_avg_7_accel_5d"""
    return (_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))).diff(5).diff(21)

def ulto_187_avg_7_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_187_avg_7_accel_21d"""
    return (_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))).diff(21).diff(21)

def ulto_188_avg_7_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_188_avg_7_accel_63d"""
    return (_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))).diff(63).diff(21)

def ulto_189_avg_7_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_189_avg_7_accel_126d"""
    return (_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))).diff(126).diff(21)

def ulto_190_avg_7_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_190_avg_7_accel_252d"""
    return (_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))).diff(252).diff(21)

def ulto_191_ult_osc_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_191_ult_osc_accel_5d"""
    return (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).diff(5).diff(21)

def ulto_192_ult_osc_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_192_ult_osc_accel_21d"""
    return (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).diff(21).diff(21)

def ulto_193_ult_osc_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_193_ult_osc_accel_63d"""
    return (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).diff(63).diff(21)

def ulto_194_ult_osc_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_194_ult_osc_accel_126d"""
    return (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).diff(126).diff(21)

def ulto_195_ult_osc_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_195_ult_osc_accel_252d"""
    return (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).diff(252).diff(21)

def ulto_196_ult_z_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_196_ult_z_accel_5d"""
    return (_zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)).diff(5).diff(21)

def ulto_197_ult_z_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_197_ult_z_accel_21d"""
    return (_zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)).diff(21).diff(21)

def ulto_198_ult_z_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_198_ult_z_accel_63d"""
    return (_zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)).diff(63).diff(21)

def ulto_199_ult_z_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_199_ult_z_accel_126d"""
    return (_zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)).diff(126).diff(21)

def ulto_200_ult_z_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_200_ult_z_accel_252d"""
    return (_zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V93_REGISTRY_ACCEL = {
    "ulto_176_bp_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_176_bp_accel_5d},
    "ulto_177_bp_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_177_bp_accel_21d},
    "ulto_178_bp_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_178_bp_accel_63d},
    "ulto_179_bp_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_179_bp_accel_126d},
    "ulto_180_bp_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_180_bp_accel_252d},
    "ulto_181_tr_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_181_tr_accel_5d},
    "ulto_182_tr_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_182_tr_accel_21d},
    "ulto_183_tr_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_183_tr_accel_63d},
    "ulto_184_tr_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_184_tr_accel_126d},
    "ulto_185_tr_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_185_tr_accel_252d},
    "ulto_186_avg_7_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_186_avg_7_accel_5d},
    "ulto_187_avg_7_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_187_avg_7_accel_21d},
    "ulto_188_avg_7_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_188_avg_7_accel_63d},
    "ulto_189_avg_7_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_189_avg_7_accel_126d},
    "ulto_190_avg_7_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_190_avg_7_accel_252d},
    "ulto_191_ult_osc_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_191_ult_osc_accel_5d},
    "ulto_192_ult_osc_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_192_ult_osc_accel_21d},
    "ulto_193_ult_osc_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_193_ult_osc_accel_63d},
    "ulto_194_ult_osc_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_194_ult_osc_accel_126d},
    "ulto_195_ult_osc_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_195_ult_osc_accel_252d},
    "ulto_196_ult_z_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_196_ult_z_accel_5d},
    "ulto_197_ult_z_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_197_ult_z_accel_21d},
    "ulto_198_ult_z_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_198_ult_z_accel_63d},
    "ulto_199_ult_z_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_199_ult_z_accel_126d},
    "ulto_200_ult_z_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_200_ult_z_accel_252d},
}
