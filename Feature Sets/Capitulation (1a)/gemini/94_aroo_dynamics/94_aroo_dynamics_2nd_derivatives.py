"""
94_aroo_dynamics — 2nd Derivatives (Velocity)
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

def aroo_151_aroon_up_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_151_aroon_up_vel_5d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).diff(5)

def aroo_152_aroon_up_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_152_aroon_up_vel_21d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).diff(21)

def aroo_153_aroon_up_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_153_aroon_up_vel_63d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).diff(63)

def aroo_154_aroon_up_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_154_aroon_up_vel_126d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).diff(126)

def aroo_155_aroon_up_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_155_aroon_up_vel_252d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25).diff(252)

def aroo_156_aroon_dn_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_156_aroon_dn_vel_5d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(5)

def aroo_157_aroon_dn_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_157_aroon_dn_vel_21d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(21)

def aroo_158_aroon_dn_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_158_aroon_dn_vel_63d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(63)

def aroo_159_aroon_dn_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_159_aroon_dn_vel_126d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(126)

def aroo_160_aroon_dn_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_160_aroon_dn_vel_252d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(252)

def aroo_161_aroon_osc_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_161_aroon_osc_vel_5d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(5)

def aroo_162_aroon_osc_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_162_aroon_osc_vel_21d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(21)

def aroo_163_aroon_osc_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_163_aroon_osc_vel_63d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(63)

def aroo_164_aroon_osc_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_164_aroon_osc_vel_126d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(126)

def aroo_165_aroon_osc_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_165_aroon_osc_vel_252d"""
    return (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).diff(252)

def aroo_166_aroo_z_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_166_aroo_z_vel_5d"""
    return (_zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)).diff(5)

def aroo_167_aroo_z_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_167_aroo_z_vel_21d"""
    return (_zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)).diff(21)

def aroo_168_aroo_z_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_168_aroo_z_vel_63d"""
    return (_zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)).diff(63)

def aroo_169_aroo_z_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_169_aroo_z_vel_126d"""
    return (_zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)).diff(126)

def aroo_170_aroo_z_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_170_aroo_z_vel_252d"""
    return (_zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)).diff(252)

def aroo_171_aroo_roc_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_171_aroo_roc_vel_5d"""
    return ((100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()).diff(5)

def aroo_172_aroo_roc_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_172_aroo_roc_vel_21d"""
    return ((100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()).diff(21)

def aroo_173_aroo_roc_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_173_aroo_roc_vel_63d"""
    return ((100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()).diff(63)

def aroo_174_aroo_roc_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_174_aroo_roc_vel_126d"""
    return ((100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()).diff(126)

def aroo_175_aroo_roc_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_175_aroo_roc_vel_252d"""
    return ((100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V94_REGISTRY_VEL = {
    "aroo_151_aroon_up_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_151_aroon_up_vel_5d},
    "aroo_152_aroon_up_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_152_aroon_up_vel_21d},
    "aroo_153_aroon_up_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_153_aroon_up_vel_63d},
    "aroo_154_aroon_up_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_154_aroon_up_vel_126d},
    "aroo_155_aroon_up_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_155_aroon_up_vel_252d},
    "aroo_156_aroon_dn_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_156_aroon_dn_vel_5d},
    "aroo_157_aroon_dn_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_157_aroon_dn_vel_21d},
    "aroo_158_aroon_dn_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_158_aroon_dn_vel_63d},
    "aroo_159_aroon_dn_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_159_aroon_dn_vel_126d},
    "aroo_160_aroon_dn_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_160_aroon_dn_vel_252d},
    "aroo_161_aroon_osc_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_161_aroon_osc_vel_5d},
    "aroo_162_aroon_osc_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_162_aroon_osc_vel_21d},
    "aroo_163_aroon_osc_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_163_aroon_osc_vel_63d},
    "aroo_164_aroon_osc_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_164_aroon_osc_vel_126d},
    "aroo_165_aroon_osc_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_165_aroon_osc_vel_252d},
    "aroo_166_aroo_z_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_166_aroo_z_vel_5d},
    "aroo_167_aroo_z_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_167_aroo_z_vel_21d},
    "aroo_168_aroo_z_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_168_aroo_z_vel_63d},
    "aroo_169_aroo_z_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_169_aroo_z_vel_126d},
    "aroo_170_aroo_z_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_170_aroo_z_vel_252d},
    "aroo_171_aroo_roc_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_171_aroo_roc_vel_5d},
    "aroo_172_aroo_roc_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_172_aroo_roc_vel_21d},
    "aroo_173_aroo_roc_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_173_aroo_roc_vel_63d},
    "aroo_174_aroo_roc_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_174_aroo_roc_vel_126d},
    "aroo_175_aroo_roc_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_175_aroo_roc_vel_252d},
}
