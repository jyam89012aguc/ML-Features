"""
78_stoc_dynamics — 2nd Derivatives (Velocity)
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

def stoc_151_stok_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_151_stok_vel_5d"""
    return (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(5)

def stoc_152_stok_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_152_stok_vel_21d"""
    return (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(21)

def stoc_153_stok_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_153_stok_vel_63d"""
    return (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(63)

def stoc_154_stok_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_154_stok_vel_126d"""
    return (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(126)

def stoc_155_stok_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_155_stok_vel_252d"""
    return (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100).diff(252)

def stoc_156_stod_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_156_stod_vel_5d"""
    return (_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)).diff(5)

def stoc_157_stod_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_157_stod_vel_21d"""
    return (_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)).diff(21)

def stoc_158_stod_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_158_stod_vel_63d"""
    return (_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)).diff(63)

def stoc_159_stod_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_159_stod_vel_126d"""
    return (_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)).diff(126)

def stoc_160_stod_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_160_stod_vel_252d"""
    return (_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)).diff(252)

def stoc_161_stod_slow_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_161_stod_slow_vel_5d"""
    return (_rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)).diff(5)

def stoc_162_stod_slow_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_162_stod_slow_vel_21d"""
    return (_rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)).diff(21)

def stoc_163_stod_slow_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_163_stod_slow_vel_63d"""
    return (_rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)).diff(63)

def stoc_164_stod_slow_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_164_stod_slow_vel_126d"""
    return (_rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)).diff(126)

def stoc_165_stod_slow_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_165_stod_slow_vel_252d"""
    return (_rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)).diff(252)

def stoc_166_stoc_range_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_166_stoc_range_vel_5d"""
    return (_rolling_max(high, 14) - _rolling_min(low, 14)).diff(5)

def stoc_167_stoc_range_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_167_stoc_range_vel_21d"""
    return (_rolling_max(high, 14) - _rolling_min(low, 14)).diff(21)

def stoc_168_stoc_range_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_168_stoc_range_vel_63d"""
    return (_rolling_max(high, 14) - _rolling_min(low, 14)).diff(63)

def stoc_169_stoc_range_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_169_stoc_range_vel_126d"""
    return (_rolling_max(high, 14) - _rolling_min(low, 14)).diff(126)

def stoc_170_stoc_range_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_170_stoc_range_vel_252d"""
    return (_rolling_max(high, 14) - _rolling_min(low, 14)).diff(252)

def stoc_171_stoc_dist_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_171_stoc_dist_vel_5d"""
    return ((_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50).diff(5)

def stoc_172_stoc_dist_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_172_stoc_dist_vel_21d"""
    return ((_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50).diff(21)

def stoc_173_stoc_dist_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_173_stoc_dist_vel_63d"""
    return ((_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50).diff(63)

def stoc_174_stoc_dist_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_174_stoc_dist_vel_126d"""
    return ((_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50).diff(126)

def stoc_175_stoc_dist_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_175_stoc_dist_vel_252d"""
    return ((_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V78_REGISTRY_VEL = {
    "stoc_151_stok_vel_5d": {"inputs": ["high", "low", "close"], "func": stoc_151_stok_vel_5d},
    "stoc_152_stok_vel_21d": {"inputs": ["high", "low", "close"], "func": stoc_152_stok_vel_21d},
    "stoc_153_stok_vel_63d": {"inputs": ["high", "low", "close"], "func": stoc_153_stok_vel_63d},
    "stoc_154_stok_vel_126d": {"inputs": ["high", "low", "close"], "func": stoc_154_stok_vel_126d},
    "stoc_155_stok_vel_252d": {"inputs": ["high", "low", "close"], "func": stoc_155_stok_vel_252d},
    "stoc_156_stod_vel_5d": {"inputs": ["high", "low", "close"], "func": stoc_156_stod_vel_5d},
    "stoc_157_stod_vel_21d": {"inputs": ["high", "low", "close"], "func": stoc_157_stod_vel_21d},
    "stoc_158_stod_vel_63d": {"inputs": ["high", "low", "close"], "func": stoc_158_stod_vel_63d},
    "stoc_159_stod_vel_126d": {"inputs": ["high", "low", "close"], "func": stoc_159_stod_vel_126d},
    "stoc_160_stod_vel_252d": {"inputs": ["high", "low", "close"], "func": stoc_160_stod_vel_252d},
    "stoc_161_stod_slow_vel_5d": {"inputs": ["high", "low", "close"], "func": stoc_161_stod_slow_vel_5d},
    "stoc_162_stod_slow_vel_21d": {"inputs": ["high", "low", "close"], "func": stoc_162_stod_slow_vel_21d},
    "stoc_163_stod_slow_vel_63d": {"inputs": ["high", "low", "close"], "func": stoc_163_stod_slow_vel_63d},
    "stoc_164_stod_slow_vel_126d": {"inputs": ["high", "low", "close"], "func": stoc_164_stod_slow_vel_126d},
    "stoc_165_stod_slow_vel_252d": {"inputs": ["high", "low", "close"], "func": stoc_165_stod_slow_vel_252d},
    "stoc_166_stoc_range_vel_5d": {"inputs": ["high", "low", "close"], "func": stoc_166_stoc_range_vel_5d},
    "stoc_167_stoc_range_vel_21d": {"inputs": ["high", "low", "close"], "func": stoc_167_stoc_range_vel_21d},
    "stoc_168_stoc_range_vel_63d": {"inputs": ["high", "low", "close"], "func": stoc_168_stoc_range_vel_63d},
    "stoc_169_stoc_range_vel_126d": {"inputs": ["high", "low", "close"], "func": stoc_169_stoc_range_vel_126d},
    "stoc_170_stoc_range_vel_252d": {"inputs": ["high", "low", "close"], "func": stoc_170_stoc_range_vel_252d},
    "stoc_171_stoc_dist_vel_5d": {"inputs": ["high", "low", "close"], "func": stoc_171_stoc_dist_vel_5d},
    "stoc_172_stoc_dist_vel_21d": {"inputs": ["high", "low", "close"], "func": stoc_172_stoc_dist_vel_21d},
    "stoc_173_stoc_dist_vel_63d": {"inputs": ["high", "low", "close"], "func": stoc_173_stoc_dist_vel_63d},
    "stoc_174_stoc_dist_vel_126d": {"inputs": ["high", "low", "close"], "func": stoc_174_stoc_dist_vel_126d},
    "stoc_175_stoc_dist_vel_252d": {"inputs": ["high", "low", "close"], "func": stoc_175_stoc_dist_vel_252d},
}
