"""
91_wilr_dynamics — 2nd Derivatives (Velocity)
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

def wilr_151_williams_r_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_151_williams_r_vel_5d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))).diff(5)

def wilr_152_williams_r_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_152_williams_r_vel_21d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))).diff(21)

def wilr_153_williams_r_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_153_williams_r_vel_63d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))).diff(63)

def wilr_154_williams_r_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_154_williams_r_vel_126d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))).diff(126)

def wilr_155_williams_r_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_155_williams_r_vel_252d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))).diff(252)

def wilr_156_wilr_z_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_156_wilr_z_vel_5d"""
    return (_zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)).diff(5)

def wilr_157_wilr_z_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_157_wilr_z_vel_21d"""
    return (_zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)).diff(21)

def wilr_158_wilr_z_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_158_wilr_z_vel_63d"""
    return (_zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)).diff(63)

def wilr_159_wilr_z_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_159_wilr_z_vel_126d"""
    return (_zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)).diff(126)

def wilr_160_wilr_z_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_160_wilr_z_vel_252d"""
    return (_zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)).diff(252)

def wilr_161_wilr_roc_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_161_wilr_roc_vel_5d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()).diff(5)

def wilr_162_wilr_roc_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_162_wilr_roc_vel_21d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()).diff(21)

def wilr_163_wilr_roc_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_163_wilr_roc_vel_63d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()).diff(63)

def wilr_164_wilr_roc_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_164_wilr_roc_vel_126d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()).diff(126)

def wilr_165_wilr_roc_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_165_wilr_roc_vel_252d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()).diff(252)

def wilr_166_wilr_ma_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_166_wilr_ma_vel_5d"""
    return (_rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)).diff(5)

def wilr_167_wilr_ma_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_167_wilr_ma_vel_21d"""
    return (_rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)).diff(21)

def wilr_168_wilr_ma_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_168_wilr_ma_vel_63d"""
    return (_rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)).diff(63)

def wilr_169_wilr_ma_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_169_wilr_ma_vel_126d"""
    return (_rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)).diff(126)

def wilr_170_wilr_ma_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_170_wilr_ma_vel_252d"""
    return (_rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)).diff(252)

def wilr_171_wilr_dist_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_171_wilr_dist_vel_5d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5).diff(5)

def wilr_172_wilr_dist_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_172_wilr_dist_vel_21d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5).diff(21)

def wilr_173_wilr_dist_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_173_wilr_dist_vel_63d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5).diff(63)

def wilr_174_wilr_dist_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_174_wilr_dist_vel_126d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5).diff(126)

def wilr_175_wilr_dist_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_175_wilr_dist_vel_252d"""
    return (_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V91_REGISTRY_VEL = {
    "wilr_151_williams_r_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_151_williams_r_vel_5d},
    "wilr_152_williams_r_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_152_williams_r_vel_21d},
    "wilr_153_williams_r_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_153_williams_r_vel_63d},
    "wilr_154_williams_r_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_154_williams_r_vel_126d},
    "wilr_155_williams_r_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_155_williams_r_vel_252d},
    "wilr_156_wilr_z_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_156_wilr_z_vel_5d},
    "wilr_157_wilr_z_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_157_wilr_z_vel_21d},
    "wilr_158_wilr_z_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_158_wilr_z_vel_63d},
    "wilr_159_wilr_z_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_159_wilr_z_vel_126d},
    "wilr_160_wilr_z_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_160_wilr_z_vel_252d},
    "wilr_161_wilr_roc_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_161_wilr_roc_vel_5d},
    "wilr_162_wilr_roc_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_162_wilr_roc_vel_21d},
    "wilr_163_wilr_roc_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_163_wilr_roc_vel_63d},
    "wilr_164_wilr_roc_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_164_wilr_roc_vel_126d},
    "wilr_165_wilr_roc_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_165_wilr_roc_vel_252d},
    "wilr_166_wilr_ma_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_166_wilr_ma_vel_5d},
    "wilr_167_wilr_ma_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_167_wilr_ma_vel_21d},
    "wilr_168_wilr_ma_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_168_wilr_ma_vel_63d},
    "wilr_169_wilr_ma_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_169_wilr_ma_vel_126d},
    "wilr_170_wilr_ma_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_170_wilr_ma_vel_252d},
    "wilr_171_wilr_dist_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_171_wilr_dist_vel_5d},
    "wilr_172_wilr_dist_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_172_wilr_dist_vel_21d},
    "wilr_173_wilr_dist_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_173_wilr_dist_vel_63d},
    "wilr_174_wilr_dist_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_174_wilr_dist_vel_126d},
    "wilr_175_wilr_dist_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_175_wilr_dist_vel_252d},
}
