"""
95_vort_dynamics — 3rd Derivatives (Acceleration)
Domain: vort_dynamics
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

def vort_176_vi_plus_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_176_vi_plus_accel_5d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(5).diff(21)

def vort_177_vi_plus_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_177_vi_plus_accel_21d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(21).diff(21)

def vort_178_vi_plus_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_178_vi_plus_accel_63d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(63).diff(21)

def vort_179_vi_plus_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_179_vi_plus_accel_126d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(126).diff(21)

def vort_180_vi_plus_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_180_vi_plus_accel_252d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(252).diff(21)

def vort_181_vi_minus_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_181_vi_minus_accel_5d"""
    return (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(5).diff(21)

def vort_182_vi_minus_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_182_vi_minus_accel_21d"""
    return (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(21).diff(21)

def vort_183_vi_minus_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_183_vi_minus_accel_63d"""
    return (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(63).diff(21)

def vort_184_vi_minus_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_184_vi_minus_accel_126d"""
    return (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(126).diff(21)

def vort_185_vi_minus_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_185_vi_minus_accel_252d"""
    return (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(252).diff(21)

def vort_186_vi_diff_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_186_vi_diff_accel_5d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(5).diff(21)

def vort_187_vi_diff_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_187_vi_diff_accel_21d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(21).diff(21)

def vort_188_vi_diff_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_188_vi_diff_accel_63d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(63).diff(21)

def vort_189_vi_diff_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_189_vi_diff_accel_126d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(126).diff(21)

def vort_190_vi_diff_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_190_vi_diff_accel_252d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(252).diff(21)

def vort_191_vi_z_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_191_vi_z_accel_5d"""
    return (_zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)).diff(5).diff(21)

def vort_192_vi_z_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_192_vi_z_accel_21d"""
    return (_zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)).diff(21).diff(21)

def vort_193_vi_z_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_193_vi_z_accel_63d"""
    return (_zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)).diff(63).diff(21)

def vort_194_vi_z_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_194_vi_z_accel_126d"""
    return (_zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)).diff(126).diff(21)

def vort_195_vi_z_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_195_vi_z_accel_252d"""
    return (_zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)).diff(252).diff(21)

def vort_196_vi_roc_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_196_vi_roc_accel_5d"""
    return ((_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()).diff(5).diff(21)

def vort_197_vi_roc_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_197_vi_roc_accel_21d"""
    return ((_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()).diff(21).diff(21)

def vort_198_vi_roc_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_198_vi_roc_accel_63d"""
    return ((_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()).diff(63).diff(21)

def vort_199_vi_roc_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_199_vi_roc_accel_126d"""
    return ((_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()).diff(126).diff(21)

def vort_200_vi_roc_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_200_vi_roc_accel_252d"""
    return ((_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V95_REGISTRY_ACCEL = {
    "vort_176_vi_plus_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_176_vi_plus_accel_5d},
    "vort_177_vi_plus_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_177_vi_plus_accel_21d},
    "vort_178_vi_plus_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_178_vi_plus_accel_63d},
    "vort_179_vi_plus_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_179_vi_plus_accel_126d},
    "vort_180_vi_plus_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_180_vi_plus_accel_252d},
    "vort_181_vi_minus_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_181_vi_minus_accel_5d},
    "vort_182_vi_minus_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_182_vi_minus_accel_21d},
    "vort_183_vi_minus_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_183_vi_minus_accel_63d},
    "vort_184_vi_minus_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_184_vi_minus_accel_126d},
    "vort_185_vi_minus_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_185_vi_minus_accel_252d},
    "vort_186_vi_diff_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_186_vi_diff_accel_5d},
    "vort_187_vi_diff_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_187_vi_diff_accel_21d},
    "vort_188_vi_diff_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_188_vi_diff_accel_63d},
    "vort_189_vi_diff_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_189_vi_diff_accel_126d},
    "vort_190_vi_diff_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_190_vi_diff_accel_252d},
    "vort_191_vi_z_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_191_vi_z_accel_5d},
    "vort_192_vi_z_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_192_vi_z_accel_21d},
    "vort_193_vi_z_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_193_vi_z_accel_63d},
    "vort_194_vi_z_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_194_vi_z_accel_126d},
    "vort_195_vi_z_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_195_vi_z_accel_252d},
    "vort_196_vi_roc_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_196_vi_roc_accel_5d},
    "vort_197_vi_roc_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_197_vi_roc_accel_21d},
    "vort_198_vi_roc_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_198_vi_roc_accel_63d},
    "vort_199_vi_roc_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_199_vi_roc_accel_126d},
    "vort_200_vi_roc_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_200_vi_roc_accel_252d},
}
