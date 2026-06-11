"""
88_pvtd_dynamics — 3rd Derivatives (Acceleration)
Domain: pvtd_dynamics
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

def pvtd_176_pvt_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_176_pvt_accel_5d"""
    return (volume * (close.pct_change())).diff(5).diff(21)

def pvtd_177_pvt_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_177_pvt_accel_21d"""
    return (volume * (close.pct_change())).diff(21).diff(21)

def pvtd_178_pvt_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_178_pvt_accel_63d"""
    return (volume * (close.pct_change())).diff(63).diff(21)

def pvtd_179_pvt_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_179_pvt_accel_126d"""
    return (volume * (close.pct_change())).diff(126).diff(21)

def pvtd_180_pvt_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_180_pvt_accel_252d"""
    return (volume * (close.pct_change())).diff(252).diff(21)

def pvtd_181_pvt_cum_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_181_pvt_cum_accel_5d"""
    return ((volume * (close.pct_change())).cumsum()).diff(5).diff(21)

def pvtd_182_pvt_cum_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_182_pvt_cum_accel_21d"""
    return ((volume * (close.pct_change())).cumsum()).diff(21).diff(21)

def pvtd_183_pvt_cum_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_183_pvt_cum_accel_63d"""
    return ((volume * (close.pct_change())).cumsum()).diff(63).diff(21)

def pvtd_184_pvt_cum_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_184_pvt_cum_accel_126d"""
    return ((volume * (close.pct_change())).cumsum()).diff(126).diff(21)

def pvtd_185_pvt_cum_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_185_pvt_cum_accel_252d"""
    return ((volume * (close.pct_change())).cumsum()).diff(252).diff(21)

def pvtd_186_pvt_rat_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_186_pvt_rat_accel_5d"""
    return (_safe_div(volume * (close.pct_change()), volume)).diff(5).diff(21)

def pvtd_187_pvt_rat_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_187_pvt_rat_accel_21d"""
    return (_safe_div(volume * (close.pct_change()), volume)).diff(21).diff(21)

def pvtd_188_pvt_rat_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_188_pvt_rat_accel_63d"""
    return (_safe_div(volume * (close.pct_change()), volume)).diff(63).diff(21)

def pvtd_189_pvt_rat_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_189_pvt_rat_accel_126d"""
    return (_safe_div(volume * (close.pct_change()), volume)).diff(126).diff(21)

def pvtd_190_pvt_rat_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_190_pvt_rat_accel_252d"""
    return (_safe_div(volume * (close.pct_change()), volume)).diff(252).diff(21)

def pvtd_191_pvt_roc_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_191_pvt_roc_accel_5d"""
    return ((volume * (close.pct_change())).pct_change()).diff(5).diff(21)

def pvtd_192_pvt_roc_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_192_pvt_roc_accel_21d"""
    return ((volume * (close.pct_change())).pct_change()).diff(21).diff(21)

def pvtd_193_pvt_roc_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_193_pvt_roc_accel_63d"""
    return ((volume * (close.pct_change())).pct_change()).diff(63).diff(21)

def pvtd_194_pvt_roc_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_194_pvt_roc_accel_126d"""
    return ((volume * (close.pct_change())).pct_change()).diff(126).diff(21)

def pvtd_195_pvt_roc_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_195_pvt_roc_accel_252d"""
    return ((volume * (close.pct_change())).pct_change()).diff(252).diff(21)

def pvtd_196_pvt_z_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_196_pvt_z_accel_5d"""
    return (_zscore_rolling(volume * (close.pct_change()), 21)).diff(5).diff(21)

def pvtd_197_pvt_z_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_197_pvt_z_accel_21d"""
    return (_zscore_rolling(volume * (close.pct_change()), 21)).diff(21).diff(21)

def pvtd_198_pvt_z_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_198_pvt_z_accel_63d"""
    return (_zscore_rolling(volume * (close.pct_change()), 21)).diff(63).diff(21)

def pvtd_199_pvt_z_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_199_pvt_z_accel_126d"""
    return (_zscore_rolling(volume * (close.pct_change()), 21)).diff(126).diff(21)

def pvtd_200_pvt_z_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_200_pvt_z_accel_252d"""
    return (_zscore_rolling(volume * (close.pct_change()), 21)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V88_REGISTRY_ACCEL = {
    "pvtd_176_pvt_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_176_pvt_accel_5d},
    "pvtd_177_pvt_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_177_pvt_accel_21d},
    "pvtd_178_pvt_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_178_pvt_accel_63d},
    "pvtd_179_pvt_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_179_pvt_accel_126d},
    "pvtd_180_pvt_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_180_pvt_accel_252d},
    "pvtd_181_pvt_cum_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_181_pvt_cum_accel_5d},
    "pvtd_182_pvt_cum_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_182_pvt_cum_accel_21d},
    "pvtd_183_pvt_cum_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_183_pvt_cum_accel_63d},
    "pvtd_184_pvt_cum_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_184_pvt_cum_accel_126d},
    "pvtd_185_pvt_cum_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_185_pvt_cum_accel_252d},
    "pvtd_186_pvt_rat_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_186_pvt_rat_accel_5d},
    "pvtd_187_pvt_rat_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_187_pvt_rat_accel_21d},
    "pvtd_188_pvt_rat_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_188_pvt_rat_accel_63d},
    "pvtd_189_pvt_rat_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_189_pvt_rat_accel_126d},
    "pvtd_190_pvt_rat_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_190_pvt_rat_accel_252d},
    "pvtd_191_pvt_roc_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_191_pvt_roc_accel_5d},
    "pvtd_192_pvt_roc_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_192_pvt_roc_accel_21d},
    "pvtd_193_pvt_roc_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_193_pvt_roc_accel_63d},
    "pvtd_194_pvt_roc_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_194_pvt_roc_accel_126d},
    "pvtd_195_pvt_roc_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_195_pvt_roc_accel_252d},
    "pvtd_196_pvt_z_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_196_pvt_z_accel_5d},
    "pvtd_197_pvt_z_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_197_pvt_z_accel_21d},
    "pvtd_198_pvt_z_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_198_pvt_z_accel_63d},
    "pvtd_199_pvt_z_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_199_pvt_z_accel_126d},
    "pvtd_200_pvt_z_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_200_pvt_z_accel_252d},
}
