"""
87_atrd_dynamics — 3rd Derivatives (Acceleration)
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

def atrd_176_tr_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_176_tr_accel_5d"""
    return (pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)).diff(5).diff(21)

def atrd_177_tr_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_177_tr_accel_21d"""
    return (pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)).diff(21).diff(21)

def atrd_178_tr_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_178_tr_accel_63d"""
    return (pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)).diff(63).diff(21)

def atrd_179_tr_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_179_tr_accel_126d"""
    return (pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)).diff(126).diff(21)

def atrd_180_tr_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_180_tr_accel_252d"""
    return (pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)).diff(252).diff(21)

def atrd_181_atr_rat_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_181_atr_rat_accel_5d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)).diff(5).diff(21)

def atrd_182_atr_rat_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_182_atr_rat_accel_21d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)).diff(21).diff(21)

def atrd_183_atr_rat_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_183_atr_rat_accel_63d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)).diff(63).diff(21)

def atrd_184_atr_rat_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_184_atr_rat_accel_126d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)).diff(126).diff(21)

def atrd_185_atr_rat_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_185_atr_rat_accel_252d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)).diff(252).diff(21)

def atrd_186_natr_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_186_natr_accel_5d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100).diff(5).diff(21)

def atrd_187_natr_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_187_natr_accel_21d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100).diff(21).diff(21)

def atrd_188_natr_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_188_natr_accel_63d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100).diff(63).diff(21)

def atrd_189_natr_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_189_natr_accel_126d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100).diff(126).diff(21)

def atrd_190_natr_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_190_natr_accel_252d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100).diff(252).diff(21)

def atrd_191_tr_vol_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_191_tr_vol_accel_5d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)).diff(5).diff(21)

def atrd_192_tr_vol_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_192_tr_vol_accel_21d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)).diff(21).diff(21)

def atrd_193_tr_vol_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_193_tr_vol_accel_63d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)).diff(63).diff(21)

def atrd_194_tr_vol_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_194_tr_vol_accel_126d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)).diff(126).diff(21)

def atrd_195_tr_vol_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_195_tr_vol_accel_252d"""
    return (_safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)).diff(252).diff(21)

def atrd_196_tr_log_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_196_tr_log_accel_5d"""
    return (np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))).diff(5).diff(21)

def atrd_197_tr_log_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_197_tr_log_accel_21d"""
    return (np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))).diff(21).diff(21)

def atrd_198_tr_log_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_198_tr_log_accel_63d"""
    return (np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))).diff(63).diff(21)

def atrd_199_tr_log_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_199_tr_log_accel_126d"""
    return (np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))).diff(126).diff(21)

def atrd_200_tr_log_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_200_tr_log_accel_252d"""
    return (np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V87_REGISTRY_ACCEL = {
    "atrd_176_tr_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_176_tr_accel_5d},
    "atrd_177_tr_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_177_tr_accel_21d},
    "atrd_178_tr_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_178_tr_accel_63d},
    "atrd_179_tr_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_179_tr_accel_126d},
    "atrd_180_tr_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_180_tr_accel_252d},
    "atrd_181_atr_rat_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_181_atr_rat_accel_5d},
    "atrd_182_atr_rat_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_182_atr_rat_accel_21d},
    "atrd_183_atr_rat_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_183_atr_rat_accel_63d},
    "atrd_184_atr_rat_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_184_atr_rat_accel_126d},
    "atrd_185_atr_rat_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_185_atr_rat_accel_252d},
    "atrd_186_natr_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_186_natr_accel_5d},
    "atrd_187_natr_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_187_natr_accel_21d},
    "atrd_188_natr_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_188_natr_accel_63d},
    "atrd_189_natr_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_189_natr_accel_126d},
    "atrd_190_natr_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_190_natr_accel_252d},
    "atrd_191_tr_vol_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_191_tr_vol_accel_5d},
    "atrd_192_tr_vol_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_192_tr_vol_accel_21d},
    "atrd_193_tr_vol_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_193_tr_vol_accel_63d},
    "atrd_194_tr_vol_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_194_tr_vol_accel_126d},
    "atrd_195_tr_vol_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_195_tr_vol_accel_252d},
    "atrd_196_tr_log_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_196_tr_log_accel_5d},
    "atrd_197_tr_log_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_197_tr_log_accel_21d},
    "atrd_198_tr_log_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_198_tr_log_accel_63d},
    "atrd_199_tr_log_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_199_tr_log_accel_126d},
    "atrd_200_tr_log_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_200_tr_log_accel_252d},
}
