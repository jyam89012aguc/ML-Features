"""
95_vort_dynamics — 2nd Derivatives (Velocity)
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

def vort_151_vi_plus_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_151_vi_plus_vel_5d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(5)

def vort_152_vi_plus_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_152_vi_plus_vel_21d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(21)

def vort_153_vi_plus_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_153_vi_plus_vel_63d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(63)

def vort_154_vi_plus_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_154_vi_plus_vel_126d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(126)

def vort_155_vi_plus_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_155_vi_plus_vel_252d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(252)

def vort_156_vi_minus_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_156_vi_minus_vel_5d"""
    return (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(5)

def vort_157_vi_minus_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_157_vi_minus_vel_21d"""
    return (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(21)

def vort_158_vi_minus_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_158_vi_minus_vel_63d"""
    return (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(63)

def vort_159_vi_minus_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_159_vi_minus_vel_126d"""
    return (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(126)

def vort_160_vi_minus_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_160_vi_minus_vel_252d"""
    return (_safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(252)

def vort_161_vi_diff_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_161_vi_diff_vel_5d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(5)

def vort_162_vi_diff_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_162_vi_diff_vel_21d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(21)

def vort_163_vi_diff_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_163_vi_diff_vel_63d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(63)

def vort_164_vi_diff_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_164_vi_diff_vel_126d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(126)

def vort_165_vi_diff_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_165_vi_diff_vel_252d"""
    return (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).diff(252)

def vort_166_vi_z_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_166_vi_z_vel_5d"""
    return (_zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)).diff(5)

def vort_167_vi_z_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_167_vi_z_vel_21d"""
    return (_zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)).diff(21)

def vort_168_vi_z_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_168_vi_z_vel_63d"""
    return (_zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)).diff(63)

def vort_169_vi_z_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_169_vi_z_vel_126d"""
    return (_zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)).diff(126)

def vort_170_vi_z_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_170_vi_z_vel_252d"""
    return (_zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)).diff(252)

def vort_171_vi_roc_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_171_vi_roc_vel_5d"""
    return ((_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()).diff(5)

def vort_172_vi_roc_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_172_vi_roc_vel_21d"""
    return ((_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()).diff(21)

def vort_173_vi_roc_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_173_vi_roc_vel_63d"""
    return ((_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()).diff(63)

def vort_174_vi_roc_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_174_vi_roc_vel_126d"""
    return ((_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()).diff(126)

def vort_175_vi_roc_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_175_vi_roc_vel_252d"""
    return ((_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V95_REGISTRY_VEL = {
    "vort_151_vi_plus_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_151_vi_plus_vel_5d},
    "vort_152_vi_plus_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_152_vi_plus_vel_21d},
    "vort_153_vi_plus_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_153_vi_plus_vel_63d},
    "vort_154_vi_plus_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_154_vi_plus_vel_126d},
    "vort_155_vi_plus_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_155_vi_plus_vel_252d},
    "vort_156_vi_minus_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_156_vi_minus_vel_5d},
    "vort_157_vi_minus_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_157_vi_minus_vel_21d},
    "vort_158_vi_minus_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_158_vi_minus_vel_63d},
    "vort_159_vi_minus_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_159_vi_minus_vel_126d},
    "vort_160_vi_minus_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_160_vi_minus_vel_252d},
    "vort_161_vi_diff_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_161_vi_diff_vel_5d},
    "vort_162_vi_diff_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_162_vi_diff_vel_21d},
    "vort_163_vi_diff_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_163_vi_diff_vel_63d},
    "vort_164_vi_diff_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_164_vi_diff_vel_126d},
    "vort_165_vi_diff_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_165_vi_diff_vel_252d},
    "vort_166_vi_z_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_166_vi_z_vel_5d},
    "vort_167_vi_z_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_167_vi_z_vel_21d},
    "vort_168_vi_z_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_168_vi_z_vel_63d},
    "vort_169_vi_z_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_169_vi_z_vel_126d},
    "vort_170_vi_z_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_170_vi_z_vel_252d},
    "vort_171_vi_roc_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_171_vi_roc_vel_5d},
    "vort_172_vi_roc_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_172_vi_roc_vel_21d},
    "vort_173_vi_roc_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_173_vi_roc_vel_63d},
    "vort_174_vi_roc_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_174_vi_roc_vel_126d},
    "vort_175_vi_roc_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_175_vi_roc_vel_252d},
}
