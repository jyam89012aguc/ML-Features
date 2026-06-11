"""
91_wilr_dynamics — 3rd Derivatives (Acceleration)
Domain: wilr_dynamics
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

def wilr_176_williams_r_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_176_williams_r_accel_5d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))).diff(5).diff(21)

def wilr_177_williams_r_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_177_williams_r_accel_21d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))).diff(21).diff(21)

def wilr_178_williams_r_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_178_williams_r_accel_63d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))).diff(63).diff(21)

def wilr_179_williams_r_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_179_williams_r_accel_126d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))).diff(126).diff(21)

def wilr_180_williams_r_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_180_williams_r_accel_252d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))).diff(252).diff(21)

def wilr_181_wilr_z_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_181_wilr_z_accel_5d"""
    return (_zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)).diff(5).diff(21)

def wilr_182_wilr_z_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_182_wilr_z_accel_21d"""
    return (_zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)).diff(21).diff(21)

def wilr_183_wilr_z_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_183_wilr_z_accel_63d"""
    return (_zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)).diff(63).diff(21)

def wilr_184_wilr_z_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_184_wilr_z_accel_126d"""
    return (_zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)).diff(126).diff(21)

def wilr_185_wilr_z_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_185_wilr_z_accel_252d"""
    return (_zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)).diff(252).diff(21)

def wilr_186_wilr_roc_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_186_wilr_roc_accel_5d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()).diff(5).diff(21)

def wilr_187_wilr_roc_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_187_wilr_roc_accel_21d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()).diff(21).diff(21)

def wilr_188_wilr_roc_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_188_wilr_roc_accel_63d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()).diff(63).diff(21)

def wilr_189_wilr_roc_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_189_wilr_roc_accel_126d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()).diff(126).diff(21)

def wilr_190_wilr_roc_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_190_wilr_roc_accel_252d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()).diff(252).diff(21)

def wilr_191_wilr_ma_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_191_wilr_ma_accel_5d"""
    return (_rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)).diff(5).diff(21)

def wilr_192_wilr_ma_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_192_wilr_ma_accel_21d"""
    return (_rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)).diff(21).diff(21)

def wilr_193_wilr_ma_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_193_wilr_ma_accel_63d"""
    return (_rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)).diff(63).diff(21)

def wilr_194_wilr_ma_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_194_wilr_ma_accel_126d"""
    return (_rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)).diff(126).diff(21)

def wilr_195_wilr_ma_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_195_wilr_ma_accel_252d"""
    return (_rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)).diff(252).diff(21)

def wilr_196_wilr_dist_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_196_wilr_dist_accel_5d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5).diff(5).diff(21)

def wilr_197_wilr_dist_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_197_wilr_dist_accel_21d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5).diff(21).diff(21)

def wilr_198_wilr_dist_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_198_wilr_dist_accel_63d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5).diff(63).diff(21)

def wilr_199_wilr_dist_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_199_wilr_dist_accel_126d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5).diff(126).diff(21)

def wilr_200_wilr_dist_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_200_wilr_dist_accel_252d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V91_REGISTRY_ACCEL = {
    "wilr_176_williams_r_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_176_williams_r_accel_5d},
    "wilr_177_williams_r_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_177_williams_r_accel_21d},
    "wilr_178_williams_r_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_178_williams_r_accel_63d},
    "wilr_179_williams_r_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_179_williams_r_accel_126d},
    "wilr_180_williams_r_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_180_williams_r_accel_252d},
    "wilr_181_wilr_z_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_181_wilr_z_accel_5d},
    "wilr_182_wilr_z_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_182_wilr_z_accel_21d},
    "wilr_183_wilr_z_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_183_wilr_z_accel_63d},
    "wilr_184_wilr_z_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_184_wilr_z_accel_126d},
    "wilr_185_wilr_z_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_185_wilr_z_accel_252d},
    "wilr_186_wilr_roc_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_186_wilr_roc_accel_5d},
    "wilr_187_wilr_roc_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_187_wilr_roc_accel_21d},
    "wilr_188_wilr_roc_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_188_wilr_roc_accel_63d},
    "wilr_189_wilr_roc_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_189_wilr_roc_accel_126d},
    "wilr_190_wilr_roc_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_190_wilr_roc_accel_252d},
    "wilr_191_wilr_ma_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_191_wilr_ma_accel_5d},
    "wilr_192_wilr_ma_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_192_wilr_ma_accel_21d},
    "wilr_193_wilr_ma_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_193_wilr_ma_accel_63d},
    "wilr_194_wilr_ma_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_194_wilr_ma_accel_126d},
    "wilr_195_wilr_ma_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_195_wilr_ma_accel_252d},
    "wilr_196_wilr_dist_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_196_wilr_dist_accel_5d},
    "wilr_197_wilr_dist_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_197_wilr_dist_accel_21d},
    "wilr_198_wilr_dist_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_198_wilr_dist_accel_63d},
    "wilr_199_wilr_dist_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_199_wilr_dist_accel_126d},
    "wilr_200_wilr_dist_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_200_wilr_dist_accel_252d},
}
