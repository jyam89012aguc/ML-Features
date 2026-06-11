"""
89_mass_dynamics — 3rd Derivatives (Acceleration)
Domain: mass_dynamics
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

def mass_176_range_ema_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_176_range_ema_accel_5d"""
    return ((high - low).ewm(span=9).mean()).diff(5).diff(21)

def mass_177_range_ema_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_177_range_ema_accel_21d"""
    return ((high - low).ewm(span=9).mean()).diff(21).diff(21)

def mass_178_range_ema_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_178_range_ema_accel_63d"""
    return ((high - low).ewm(span=9).mean()).diff(63).diff(21)

def mass_179_range_ema_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_179_range_ema_accel_126d"""
    return ((high - low).ewm(span=9).mean()).diff(126).diff(21)

def mass_180_range_ema_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_180_range_ema_accel_252d"""
    return ((high - low).ewm(span=9).mean()).diff(252).diff(21)

def mass_181_range_dema_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_181_range_dema_accel_5d"""
    return ((high - low).ewm(span=9).mean().ewm(span=9).mean()).diff(5).diff(21)

def mass_182_range_dema_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_182_range_dema_accel_21d"""
    return ((high - low).ewm(span=9).mean().ewm(span=9).mean()).diff(21).diff(21)

def mass_183_range_dema_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_183_range_dema_accel_63d"""
    return ((high - low).ewm(span=9).mean().ewm(span=9).mean()).diff(63).diff(21)

def mass_184_range_dema_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_184_range_dema_accel_126d"""
    return ((high - low).ewm(span=9).mean().ewm(span=9).mean()).diff(126).diff(21)

def mass_185_range_dema_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_185_range_dema_accel_252d"""
    return ((high - low).ewm(span=9).mean().ewm(span=9).mean()).diff(252).diff(21)

def mass_186_mass_idx_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_186_mass_idx_accel_5d"""
    return (_safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())).diff(5).diff(21)

def mass_187_mass_idx_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_187_mass_idx_accel_21d"""
    return (_safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())).diff(21).diff(21)

def mass_188_mass_idx_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_188_mass_idx_accel_63d"""
    return (_safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())).diff(63).diff(21)

def mass_189_mass_idx_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_189_mass_idx_accel_126d"""
    return (_safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())).diff(126).diff(21)

def mass_190_mass_idx_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_190_mass_idx_accel_252d"""
    return (_safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())).diff(252).diff(21)

def mass_191_range_std_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_191_range_std_accel_5d"""
    return (_rolling_std(high - low, 9)).diff(5).diff(21)

def mass_192_range_std_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_192_range_std_accel_21d"""
    return (_rolling_std(high - low, 9)).diff(21).diff(21)

def mass_193_range_std_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_193_range_std_accel_63d"""
    return (_rolling_std(high - low, 9)).diff(63).diff(21)

def mass_194_range_std_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_194_range_std_accel_126d"""
    return (_rolling_std(high - low, 9)).diff(126).diff(21)

def mass_195_range_std_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_195_range_std_accel_252d"""
    return (_rolling_std(high - low, 9)).diff(252).diff(21)

def mass_196_range_lvl_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_196_range_lvl_accel_5d"""
    return (high - low).diff(5).diff(21)

def mass_197_range_lvl_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_197_range_lvl_accel_21d"""
    return (high - low).diff(21).diff(21)

def mass_198_range_lvl_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_198_range_lvl_accel_63d"""
    return (high - low).diff(63).diff(21)

def mass_199_range_lvl_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_199_range_lvl_accel_126d"""
    return (high - low).diff(126).diff(21)

def mass_200_range_lvl_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_200_range_lvl_accel_252d"""
    return (high - low).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V89_REGISTRY_ACCEL = {
    "mass_176_range_ema_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_176_range_ema_accel_5d},
    "mass_177_range_ema_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_177_range_ema_accel_21d},
    "mass_178_range_ema_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_178_range_ema_accel_63d},
    "mass_179_range_ema_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_179_range_ema_accel_126d},
    "mass_180_range_ema_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_180_range_ema_accel_252d},
    "mass_181_range_dema_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_181_range_dema_accel_5d},
    "mass_182_range_dema_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_182_range_dema_accel_21d},
    "mass_183_range_dema_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_183_range_dema_accel_63d},
    "mass_184_range_dema_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_184_range_dema_accel_126d},
    "mass_185_range_dema_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_185_range_dema_accel_252d},
    "mass_186_mass_idx_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_186_mass_idx_accel_5d},
    "mass_187_mass_idx_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_187_mass_idx_accel_21d},
    "mass_188_mass_idx_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_188_mass_idx_accel_63d},
    "mass_189_mass_idx_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_189_mass_idx_accel_126d},
    "mass_190_mass_idx_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_190_mass_idx_accel_252d},
    "mass_191_range_std_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_191_range_std_accel_5d},
    "mass_192_range_std_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_192_range_std_accel_21d},
    "mass_193_range_std_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_193_range_std_accel_63d},
    "mass_194_range_std_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_194_range_std_accel_126d},
    "mass_195_range_std_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_195_range_std_accel_252d},
    "mass_196_range_lvl_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_196_range_lvl_accel_5d},
    "mass_197_range_lvl_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_197_range_lvl_accel_21d},
    "mass_198_range_lvl_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_198_range_lvl_accel_63d},
    "mass_199_range_lvl_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_199_range_lvl_accel_126d},
    "mass_200_range_lvl_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_200_range_lvl_accel_252d},
}
