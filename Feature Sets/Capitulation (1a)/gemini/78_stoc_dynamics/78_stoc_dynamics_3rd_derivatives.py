"""
78_stoc_dynamics — 3rd Derivatives (Acceleration)
Domain: stoc_dynamics
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

def stoc_176_stok_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_176_stok_accel_5d"""
    return (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(5).diff(21)

def stoc_177_stok_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_177_stok_accel_21d"""
    return (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(21).diff(21)

def stoc_178_stok_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_178_stok_accel_63d"""
    return (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(63).diff(21)

def stoc_179_stok_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_179_stok_accel_126d"""
    return (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(126).diff(21)

def stoc_180_stok_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_180_stok_accel_252d"""
    return (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(252).diff(21)

def stoc_181_stod_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_181_stod_accel_5d"""
    return (_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)).diff(5).diff(21)

def stoc_182_stod_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_182_stod_accel_21d"""
    return (_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)).diff(21).diff(21)

def stoc_183_stod_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_183_stod_accel_63d"""
    return (_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)).diff(63).diff(21)

def stoc_184_stod_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_184_stod_accel_126d"""
    return (_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)).diff(126).diff(21)

def stoc_185_stod_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_185_stod_accel_252d"""
    return (_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)).diff(252).diff(21)

def stoc_186_stod_slow_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_186_stod_slow_accel_5d"""
    return (_rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)).diff(5).diff(21)

def stoc_187_stod_slow_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_187_stod_slow_accel_21d"""
    return (_rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)).diff(21).diff(21)

def stoc_188_stod_slow_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_188_stod_slow_accel_63d"""
    return (_rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)).diff(63).diff(21)

def stoc_189_stod_slow_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_189_stod_slow_accel_126d"""
    return (_rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)).diff(126).diff(21)

def stoc_190_stod_slow_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_190_stod_slow_accel_252d"""
    return (_rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)).diff(252).diff(21)

def stoc_191_stoc_range_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_191_stoc_range_accel_5d"""
    return (_rolling_max(high, 14) - _rolling_min(low, 14)).diff(5).diff(21)

def stoc_192_stoc_range_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_192_stoc_range_accel_21d"""
    return (_rolling_max(high, 14) - _rolling_min(low, 14)).diff(21).diff(21)

def stoc_193_stoc_range_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_193_stoc_range_accel_63d"""
    return (_rolling_max(high, 14) - _rolling_min(low, 14)).diff(63).diff(21)

def stoc_194_stoc_range_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_194_stoc_range_accel_126d"""
    return (_rolling_max(high, 14) - _rolling_min(low, 14)).diff(126).diff(21)

def stoc_195_stoc_range_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_195_stoc_range_accel_252d"""
    return (_rolling_max(high, 14) - _rolling_min(low, 14)).diff(252).diff(21)

def stoc_196_stoc_dist_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_196_stoc_dist_accel_5d"""
    return ((_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50).diff(5).diff(21)

def stoc_197_stoc_dist_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_197_stoc_dist_accel_21d"""
    return ((_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50).diff(21).diff(21)

def stoc_198_stoc_dist_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_198_stoc_dist_accel_63d"""
    return ((_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50).diff(63).diff(21)

def stoc_199_stoc_dist_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_199_stoc_dist_accel_126d"""
    return ((_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50).diff(126).diff(21)

def stoc_200_stoc_dist_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_200_stoc_dist_accel_252d"""
    return ((_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V78_REGISTRY_ACCEL = {
    "stoc_176_stok_accel_5d": {"inputs": ["high", "low", "close"], "func": stoc_176_stok_accel_5d},
    "stoc_177_stok_accel_21d": {"inputs": ["high", "low", "close"], "func": stoc_177_stok_accel_21d},
    "stoc_178_stok_accel_63d": {"inputs": ["high", "low", "close"], "func": stoc_178_stok_accel_63d},
    "stoc_179_stok_accel_126d": {"inputs": ["high", "low", "close"], "func": stoc_179_stok_accel_126d},
    "stoc_180_stok_accel_252d": {"inputs": ["high", "low", "close"], "func": stoc_180_stok_accel_252d},
    "stoc_181_stod_accel_5d": {"inputs": ["high", "low", "close"], "func": stoc_181_stod_accel_5d},
    "stoc_182_stod_accel_21d": {"inputs": ["high", "low", "close"], "func": stoc_182_stod_accel_21d},
    "stoc_183_stod_accel_63d": {"inputs": ["high", "low", "close"], "func": stoc_183_stod_accel_63d},
    "stoc_184_stod_accel_126d": {"inputs": ["high", "low", "close"], "func": stoc_184_stod_accel_126d},
    "stoc_185_stod_accel_252d": {"inputs": ["high", "low", "close"], "func": stoc_185_stod_accel_252d},
    "stoc_186_stod_slow_accel_5d": {"inputs": ["high", "low", "close"], "func": stoc_186_stod_slow_accel_5d},
    "stoc_187_stod_slow_accel_21d": {"inputs": ["high", "low", "close"], "func": stoc_187_stod_slow_accel_21d},
    "stoc_188_stod_slow_accel_63d": {"inputs": ["high", "low", "close"], "func": stoc_188_stod_slow_accel_63d},
    "stoc_189_stod_slow_accel_126d": {"inputs": ["high", "low", "close"], "func": stoc_189_stod_slow_accel_126d},
    "stoc_190_stod_slow_accel_252d": {"inputs": ["high", "low", "close"], "func": stoc_190_stod_slow_accel_252d},
    "stoc_191_stoc_range_accel_5d": {"inputs": ["high", "low", "close"], "func": stoc_191_stoc_range_accel_5d},
    "stoc_192_stoc_range_accel_21d": {"inputs": ["high", "low", "close"], "func": stoc_192_stoc_range_accel_21d},
    "stoc_193_stoc_range_accel_63d": {"inputs": ["high", "low", "close"], "func": stoc_193_stoc_range_accel_63d},
    "stoc_194_stoc_range_accel_126d": {"inputs": ["high", "low", "close"], "func": stoc_194_stoc_range_accel_126d},
    "stoc_195_stoc_range_accel_252d": {"inputs": ["high", "low", "close"], "func": stoc_195_stoc_range_accel_252d},
    "stoc_196_stoc_dist_accel_5d": {"inputs": ["high", "low", "close"], "func": stoc_196_stoc_dist_accel_5d},
    "stoc_197_stoc_dist_accel_21d": {"inputs": ["high", "low", "close"], "func": stoc_197_stoc_dist_accel_21d},
    "stoc_198_stoc_dist_accel_63d": {"inputs": ["high", "low", "close"], "func": stoc_198_stoc_dist_accel_63d},
    "stoc_199_stoc_dist_accel_126d": {"inputs": ["high", "low", "close"], "func": stoc_199_stoc_dist_accel_126d},
    "stoc_200_stoc_dist_accel_252d": {"inputs": ["high", "low", "close"], "func": stoc_200_stoc_dist_accel_252d},
}
