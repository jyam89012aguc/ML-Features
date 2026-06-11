"""
88_pvtd_dynamics — 2nd Derivatives (Velocity)
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

def pvtd_151_pvt_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_151_pvt_vel_5d"""
    return (volume * (close.pct_change())).diff(5)

def pvtd_152_pvt_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_152_pvt_vel_21d"""
    return (volume * (close.pct_change())).diff(21)

def pvtd_153_pvt_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_153_pvt_vel_63d"""
    return (volume * (close.pct_change())).diff(63)

def pvtd_154_pvt_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_154_pvt_vel_126d"""
    return (volume * (close.pct_change())).diff(126)

def pvtd_155_pvt_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_155_pvt_vel_252d"""
    return (volume * (close.pct_change())).diff(252)

def pvtd_156_pvt_cum_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_156_pvt_cum_vel_5d"""
    return ((volume * (close.pct_change())).cumsum()).diff(5)

def pvtd_157_pvt_cum_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_157_pvt_cum_vel_21d"""
    return ((volume * (close.pct_change())).cumsum()).diff(21)

def pvtd_158_pvt_cum_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_158_pvt_cum_vel_63d"""
    return ((volume * (close.pct_change())).cumsum()).diff(63)

def pvtd_159_pvt_cum_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_159_pvt_cum_vel_126d"""
    return ((volume * (close.pct_change())).cumsum()).diff(126)

def pvtd_160_pvt_cum_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_160_pvt_cum_vel_252d"""
    return ((volume * (close.pct_change())).cumsum()).diff(252)

def pvtd_161_pvt_rat_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_161_pvt_rat_vel_5d"""
    return (_safe_div(volume * (close.pct_change()), volume)).diff(5)

def pvtd_162_pvt_rat_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_162_pvt_rat_vel_21d"""
    return (_safe_div(volume * (close.pct_change()), volume)).diff(21)

def pvtd_163_pvt_rat_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_163_pvt_rat_vel_63d"""
    return (_safe_div(volume * (close.pct_change()), volume)).diff(63)

def pvtd_164_pvt_rat_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_164_pvt_rat_vel_126d"""
    return (_safe_div(volume * (close.pct_change()), volume)).diff(126)

def pvtd_165_pvt_rat_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_165_pvt_rat_vel_252d"""
    return (_safe_div(volume * (close.pct_change()), volume)).diff(252)

def pvtd_166_pvt_roc_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_166_pvt_roc_vel_5d"""
    return ((volume * (close.pct_change())).pct_change()).diff(5)

def pvtd_167_pvt_roc_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_167_pvt_roc_vel_21d"""
    return ((volume * (close.pct_change())).pct_change()).diff(21)

def pvtd_168_pvt_roc_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_168_pvt_roc_vel_63d"""
    return ((volume * (close.pct_change())).pct_change()).diff(63)

def pvtd_169_pvt_roc_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_169_pvt_roc_vel_126d"""
    return ((volume * (close.pct_change())).pct_change()).diff(126)

def pvtd_170_pvt_roc_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_170_pvt_roc_vel_252d"""
    return ((volume * (close.pct_change())).pct_change()).diff(252)

def pvtd_171_pvt_z_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_171_pvt_z_vel_5d"""
    return (_zscore_rolling(volume * (close.pct_change()), 21)).diff(5)

def pvtd_172_pvt_z_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_172_pvt_z_vel_21d"""
    return (_zscore_rolling(volume * (close.pct_change()), 21)).diff(21)

def pvtd_173_pvt_z_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_173_pvt_z_vel_63d"""
    return (_zscore_rolling(volume * (close.pct_change()), 21)).diff(63)

def pvtd_174_pvt_z_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_174_pvt_z_vel_126d"""
    return (_zscore_rolling(volume * (close.pct_change()), 21)).diff(126)

def pvtd_175_pvt_z_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_175_pvt_z_vel_252d"""
    return (_zscore_rolling(volume * (close.pct_change()), 21)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V88_REGISTRY_VEL = {
    "pvtd_151_pvt_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_151_pvt_vel_5d},
    "pvtd_152_pvt_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_152_pvt_vel_21d},
    "pvtd_153_pvt_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_153_pvt_vel_63d},
    "pvtd_154_pvt_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_154_pvt_vel_126d},
    "pvtd_155_pvt_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_155_pvt_vel_252d},
    "pvtd_156_pvt_cum_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_156_pvt_cum_vel_5d},
    "pvtd_157_pvt_cum_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_157_pvt_cum_vel_21d},
    "pvtd_158_pvt_cum_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_158_pvt_cum_vel_63d},
    "pvtd_159_pvt_cum_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_159_pvt_cum_vel_126d},
    "pvtd_160_pvt_cum_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_160_pvt_cum_vel_252d},
    "pvtd_161_pvt_rat_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_161_pvt_rat_vel_5d},
    "pvtd_162_pvt_rat_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_162_pvt_rat_vel_21d},
    "pvtd_163_pvt_rat_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_163_pvt_rat_vel_63d},
    "pvtd_164_pvt_rat_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_164_pvt_rat_vel_126d},
    "pvtd_165_pvt_rat_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_165_pvt_rat_vel_252d},
    "pvtd_166_pvt_roc_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_166_pvt_roc_vel_5d},
    "pvtd_167_pvt_roc_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_167_pvt_roc_vel_21d},
    "pvtd_168_pvt_roc_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_168_pvt_roc_vel_63d},
    "pvtd_169_pvt_roc_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_169_pvt_roc_vel_126d},
    "pvtd_170_pvt_roc_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_170_pvt_roc_vel_252d},
    "pvtd_171_pvt_z_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_171_pvt_z_vel_5d},
    "pvtd_172_pvt_z_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_172_pvt_z_vel_21d},
    "pvtd_173_pvt_z_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_173_pvt_z_vel_63d},
    "pvtd_174_pvt_z_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_174_pvt_z_vel_126d},
    "pvtd_175_pvt_z_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_175_pvt_z_vel_252d},
}
