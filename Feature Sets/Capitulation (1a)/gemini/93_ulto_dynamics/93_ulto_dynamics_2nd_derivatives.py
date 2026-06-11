"""
93_ulto_dynamics — 2nd Derivatives (Velocity)
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

def ulto_151_bp_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_151_bp_vel_5d"""
    return (close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(5)

def ulto_152_bp_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_152_bp_vel_21d"""
    return (close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(21)

def ulto_153_bp_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_153_bp_vel_63d"""
    return (close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(63)

def ulto_154_bp_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_154_bp_vel_126d"""
    return (close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(126)

def ulto_155_bp_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_155_bp_vel_252d"""
    return (close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(252)

def ulto_156_tr_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_156_tr_vel_5d"""
    return (pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(5)

def ulto_157_tr_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_157_tr_vel_21d"""
    return (pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(21)

def ulto_158_tr_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_158_tr_vel_63d"""
    return (pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(63)

def ulto_159_tr_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_159_tr_vel_126d"""
    return (pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(126)

def ulto_160_tr_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_160_tr_vel_252d"""
    return (pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)).diff(252)

def ulto_161_avg_7_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_161_avg_7_vel_5d"""
    return (_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))).diff(5)

def ulto_162_avg_7_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_162_avg_7_vel_21d"""
    return (_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))).diff(21)

def ulto_163_avg_7_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_163_avg_7_vel_63d"""
    return (_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))).diff(63)

def ulto_164_avg_7_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_164_avg_7_vel_126d"""
    return (_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))).diff(126)

def ulto_165_avg_7_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_165_avg_7_vel_252d"""
    return (_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))).diff(252)

def ulto_166_ult_osc_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_166_ult_osc_vel_5d"""
    return (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).diff(5)

def ulto_167_ult_osc_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_167_ult_osc_vel_21d"""
    return (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).diff(21)

def ulto_168_ult_osc_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_168_ult_osc_vel_63d"""
    return (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).diff(63)

def ulto_169_ult_osc_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_169_ult_osc_vel_126d"""
    return (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).diff(126)

def ulto_170_ult_osc_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_170_ult_osc_vel_252d"""
    return (100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7).diff(252)

def ulto_171_ult_z_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_171_ult_z_vel_5d"""
    return (_zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)).diff(5)

def ulto_172_ult_z_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_172_ult_z_vel_21d"""
    return (_zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)).diff(21)

def ulto_173_ult_z_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_173_ult_z_vel_63d"""
    return (_zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)).diff(63)

def ulto_174_ult_z_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_174_ult_z_vel_126d"""
    return (_zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)).diff(126)

def ulto_175_ult_z_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_175_ult_z_vel_252d"""
    return (_zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V93_REGISTRY_VEL = {
    "ulto_151_bp_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_151_bp_vel_5d},
    "ulto_152_bp_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_152_bp_vel_21d},
    "ulto_153_bp_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_153_bp_vel_63d},
    "ulto_154_bp_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_154_bp_vel_126d},
    "ulto_155_bp_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_155_bp_vel_252d},
    "ulto_156_tr_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_156_tr_vel_5d},
    "ulto_157_tr_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_157_tr_vel_21d},
    "ulto_158_tr_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_158_tr_vel_63d},
    "ulto_159_tr_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_159_tr_vel_126d},
    "ulto_160_tr_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_160_tr_vel_252d},
    "ulto_161_avg_7_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_161_avg_7_vel_5d},
    "ulto_162_avg_7_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_162_avg_7_vel_21d},
    "ulto_163_avg_7_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_163_avg_7_vel_63d},
    "ulto_164_avg_7_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_164_avg_7_vel_126d},
    "ulto_165_avg_7_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_165_avg_7_vel_252d},
    "ulto_166_ult_osc_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_166_ult_osc_vel_5d},
    "ulto_167_ult_osc_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_167_ult_osc_vel_21d},
    "ulto_168_ult_osc_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_168_ult_osc_vel_63d},
    "ulto_169_ult_osc_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_169_ult_osc_vel_126d},
    "ulto_170_ult_osc_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_170_ult_osc_vel_252d},
    "ulto_171_ult_z_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_171_ult_z_vel_5d},
    "ulto_172_ult_z_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_172_ult_z_vel_21d},
    "ulto_173_ult_z_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_173_ult_z_vel_63d},
    "ulto_174_ult_z_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_174_ult_z_vel_126d},
    "ulto_175_ult_z_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_175_ult_z_vel_252d},
}
