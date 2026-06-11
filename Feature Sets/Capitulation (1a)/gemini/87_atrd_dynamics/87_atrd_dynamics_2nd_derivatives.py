"""
87_atrd_dynamics — 2nd Derivatives (Velocity)
Domain: atrd_dynamics
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

def atrd_151_tr_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_151_tr_vel_5d"""
    return (pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)).diff(5)

def atrd_152_tr_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_152_tr_vel_21d"""
    return (pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)).diff(21)

def atrd_153_tr_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_153_tr_vel_63d"""
    return (pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)).diff(63)

def atrd_154_tr_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_154_tr_vel_126d"""
    return (pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)).diff(126)

def atrd_155_tr_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_155_tr_vel_252d"""
    return (pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)).diff(252)

def atrd_156_atr_rat_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_156_atr_rat_vel_5d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)).diff(5)

def atrd_157_atr_rat_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_157_atr_rat_vel_21d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)).diff(21)

def atrd_158_atr_rat_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_158_atr_rat_vel_63d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)).diff(63)

def atrd_159_atr_rat_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_159_atr_rat_vel_126d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)).diff(126)

def atrd_160_atr_rat_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_160_atr_rat_vel_252d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)).diff(252)

def atrd_161_natr_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_161_natr_vel_5d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100).diff(5)

def atrd_162_natr_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_162_natr_vel_21d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100).diff(21)

def atrd_163_natr_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_163_natr_vel_63d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100).diff(63)

def atrd_164_natr_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_164_natr_vel_126d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100).diff(126)

def atrd_165_natr_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_165_natr_vel_252d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100).diff(252)

def atrd_166_tr_vol_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_166_tr_vol_vel_5d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)).diff(5)

def atrd_167_tr_vol_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_167_tr_vol_vel_21d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)).diff(21)

def atrd_168_tr_vol_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_168_tr_vol_vel_63d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)).diff(63)

def atrd_169_tr_vol_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_169_tr_vol_vel_126d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)).diff(126)

def atrd_170_tr_vol_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_170_tr_vol_vel_252d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)).diff(252)

def atrd_171_tr_log_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_171_tr_log_vel_5d"""
    return (np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))).diff(5)

def atrd_172_tr_log_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_172_tr_log_vel_21d"""
    return (np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))).diff(21)

def atrd_173_tr_log_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_173_tr_log_vel_63d"""
    return (np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))).diff(63)

def atrd_174_tr_log_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_174_tr_log_vel_126d"""
    return (np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))).diff(126)

def atrd_175_tr_log_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_175_tr_log_vel_252d"""
    return (np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V87_REGISTRY_VEL = {
    "atrd_151_tr_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_151_tr_vel_5d},
    "atrd_152_tr_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_152_tr_vel_21d},
    "atrd_153_tr_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_153_tr_vel_63d},
    "atrd_154_tr_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_154_tr_vel_126d},
    "atrd_155_tr_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_155_tr_vel_252d},
    "atrd_156_atr_rat_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_156_atr_rat_vel_5d},
    "atrd_157_atr_rat_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_157_atr_rat_vel_21d},
    "atrd_158_atr_rat_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_158_atr_rat_vel_63d},
    "atrd_159_atr_rat_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_159_atr_rat_vel_126d},
    "atrd_160_atr_rat_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_160_atr_rat_vel_252d},
    "atrd_161_natr_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_161_natr_vel_5d},
    "atrd_162_natr_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_162_natr_vel_21d},
    "atrd_163_natr_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_163_natr_vel_63d},
    "atrd_164_natr_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_164_natr_vel_126d},
    "atrd_165_natr_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_165_natr_vel_252d},
    "atrd_166_tr_vol_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_166_tr_vol_vel_5d},
    "atrd_167_tr_vol_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_167_tr_vol_vel_21d},
    "atrd_168_tr_vol_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_168_tr_vol_vel_63d},
    "atrd_169_tr_vol_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_169_tr_vol_vel_126d},
    "atrd_170_tr_vol_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_170_tr_vol_vel_252d},
    "atrd_171_tr_log_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_171_tr_log_vel_5d},
    "atrd_172_tr_log_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_172_tr_log_vel_21d},
    "atrd_173_tr_log_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_173_tr_log_vel_63d},
    "atrd_174_tr_log_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_174_tr_log_vel_126d},
    "atrd_175_tr_log_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_175_tr_log_vel_252d},
}
