"""
94_aroo_dynamics — 3rd Derivatives (Acceleration)
Domain: aroo_dynamics
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

def aroo_176_aroon_up_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_176_aroon_up_accel_5d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).diff(5).diff(21)

def aroo_177_aroon_up_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_177_aroon_up_accel_21d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).diff(21).diff(21)

def aroo_178_aroon_up_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_178_aroon_up_accel_63d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).diff(63).diff(21)

def aroo_179_aroon_up_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_179_aroon_up_accel_126d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).diff(126).diff(21)

def aroo_180_aroon_up_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_180_aroon_up_accel_252d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).diff(252).diff(21)

def aroo_181_aroon_dn_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_181_aroon_dn_accel_5d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(5).diff(21)

def aroo_182_aroon_dn_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_182_aroon_dn_accel_21d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(21).diff(21)

def aroo_183_aroon_dn_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_183_aroon_dn_accel_63d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(63).diff(21)

def aroo_184_aroon_dn_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_184_aroon_dn_accel_126d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(126).diff(21)

def aroo_185_aroon_dn_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_185_aroon_dn_accel_252d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(252).diff(21)

def aroo_186_aroon_osc_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_186_aroon_osc_accel_5d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(5).diff(21)

def aroo_187_aroon_osc_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_187_aroon_osc_accel_21d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(21).diff(21)

def aroo_188_aroon_osc_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_188_aroon_osc_accel_63d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(63).diff(21)

def aroo_189_aroon_osc_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_189_aroon_osc_accel_126d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(126).diff(21)

def aroo_190_aroon_osc_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_190_aroon_osc_accel_252d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(252).diff(21)

def aroo_191_aroo_z_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_191_aroo_z_accel_5d"""
    return (_zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)).diff(5).diff(21)

def aroo_192_aroo_z_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_192_aroo_z_accel_21d"""
    return (_zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)).diff(21).diff(21)

def aroo_193_aroo_z_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_193_aroo_z_accel_63d"""
    return (_zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)).diff(63).diff(21)

def aroo_194_aroo_z_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_194_aroo_z_accel_126d"""
    return (_zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)).diff(126).diff(21)

def aroo_195_aroo_z_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_195_aroo_z_accel_252d"""
    return (_zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)).diff(252).diff(21)

def aroo_196_aroo_roc_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_196_aroo_roc_accel_5d"""
    return ((100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()).diff(5).diff(21)

def aroo_197_aroo_roc_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_197_aroo_roc_accel_21d"""
    return ((100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()).diff(21).diff(21)

def aroo_198_aroo_roc_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_198_aroo_roc_accel_63d"""
    return ((100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()).diff(63).diff(21)

def aroo_199_aroo_roc_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_199_aroo_roc_accel_126d"""
    return ((100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()).diff(126).diff(21)

def aroo_200_aroo_roc_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_200_aroo_roc_accel_252d"""
    return ((100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V94_REGISTRY_ACCEL = {
    "aroo_176_aroon_up_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_176_aroon_up_accel_5d},
    "aroo_177_aroon_up_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_177_aroon_up_accel_21d},
    "aroo_178_aroon_up_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_178_aroon_up_accel_63d},
    "aroo_179_aroon_up_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_179_aroon_up_accel_126d},
    "aroo_180_aroon_up_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_180_aroon_up_accel_252d},
    "aroo_181_aroon_dn_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_181_aroon_dn_accel_5d},
    "aroo_182_aroon_dn_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_182_aroon_dn_accel_21d},
    "aroo_183_aroon_dn_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_183_aroon_dn_accel_63d},
    "aroo_184_aroon_dn_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_184_aroon_dn_accel_126d},
    "aroo_185_aroon_dn_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_185_aroon_dn_accel_252d},
    "aroo_186_aroon_osc_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_186_aroon_osc_accel_5d},
    "aroo_187_aroon_osc_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_187_aroon_osc_accel_21d},
    "aroo_188_aroon_osc_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_188_aroon_osc_accel_63d},
    "aroo_189_aroon_osc_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_189_aroon_osc_accel_126d},
    "aroo_190_aroon_osc_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_190_aroon_osc_accel_252d},
    "aroo_191_aroo_z_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_191_aroo_z_accel_5d},
    "aroo_192_aroo_z_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_192_aroo_z_accel_21d},
    "aroo_193_aroo_z_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_193_aroo_z_accel_63d},
    "aroo_194_aroo_z_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_194_aroo_z_accel_126d},
    "aroo_195_aroo_z_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_195_aroo_z_accel_252d},
    "aroo_196_aroo_roc_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_196_aroo_roc_accel_5d},
    "aroo_197_aroo_roc_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_197_aroo_roc_accel_21d},
    "aroo_198_aroo_roc_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_198_aroo_roc_accel_63d},
    "aroo_199_aroo_roc_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_199_aroo_roc_accel_126d},
    "aroo_200_aroo_roc_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_200_aroo_roc_accel_252d},
}
