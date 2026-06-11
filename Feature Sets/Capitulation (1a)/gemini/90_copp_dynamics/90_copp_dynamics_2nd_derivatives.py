"""
90_copp_dynamics — 2nd Derivatives (Velocity)
Domain: copp_dynamics
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

def copp_151_roc_14_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_151_roc_14_vel_5d"""
    return (close.pct_change(14)).diff(5)

def copp_152_roc_14_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_152_roc_14_vel_21d"""
    return (close.pct_change(14)).diff(21)

def copp_153_roc_14_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_153_roc_14_vel_63d"""
    return (close.pct_change(14)).diff(63)

def copp_154_roc_14_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_154_roc_14_vel_126d"""
    return (close.pct_change(14)).diff(126)

def copp_155_roc_14_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_155_roc_14_vel_252d"""
    return (close.pct_change(14)).diff(252)

def copp_156_roc_11_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_156_roc_11_vel_5d"""
    return (close.pct_change(11)).diff(5)

def copp_157_roc_11_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_157_roc_11_vel_21d"""
    return (close.pct_change(11)).diff(21)

def copp_158_roc_11_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_158_roc_11_vel_63d"""
    return (close.pct_change(11)).diff(63)

def copp_159_roc_11_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_159_roc_11_vel_126d"""
    return (close.pct_change(11)).diff(126)

def copp_160_roc_11_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_160_roc_11_vel_252d"""
    return (close.pct_change(11)).diff(252)

def copp_161_copp_sum_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_161_copp_sum_vel_5d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(5)

def copp_162_copp_sum_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_162_copp_sum_vel_21d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(21)

def copp_163_copp_sum_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_163_copp_sum_vel_63d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(63)

def copp_164_copp_sum_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_164_copp_sum_vel_126d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(126)

def copp_165_copp_sum_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_165_copp_sum_vel_252d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(252)

def copp_166_copp_wma_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_166_copp_wma_vel_5d"""
    return ((close.pct_change(14) + close.pct_change(11)).rolling(10).mean()).diff(5)

def copp_167_copp_wma_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_167_copp_wma_vel_21d"""
    return ((close.pct_change(14) + close.pct_change(11)).rolling(10).mean()).diff(21)

def copp_168_copp_wma_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_168_copp_wma_vel_63d"""
    return ((close.pct_change(14) + close.pct_change(11)).rolling(10).mean()).diff(63)

def copp_169_copp_wma_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_169_copp_wma_vel_126d"""
    return ((close.pct_change(14) + close.pct_change(11)).rolling(10).mean()).diff(126)

def copp_170_copp_wma_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_170_copp_wma_vel_252d"""
    return ((close.pct_change(14) + close.pct_change(11)).rolling(10).mean()).diff(252)

def copp_171_copp_lvl_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_171_copp_lvl_vel_5d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(5)

def copp_172_copp_lvl_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_172_copp_lvl_vel_21d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(21)

def copp_173_copp_lvl_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_173_copp_lvl_vel_63d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(63)

def copp_174_copp_lvl_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_174_copp_lvl_vel_126d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(126)

def copp_175_copp_lvl_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_175_copp_lvl_vel_252d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V90_REGISTRY_VEL = {
    "copp_151_roc_14_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_151_roc_14_vel_5d},
    "copp_152_roc_14_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_152_roc_14_vel_21d},
    "copp_153_roc_14_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_153_roc_14_vel_63d},
    "copp_154_roc_14_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_154_roc_14_vel_126d},
    "copp_155_roc_14_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_155_roc_14_vel_252d},
    "copp_156_roc_11_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_156_roc_11_vel_5d},
    "copp_157_roc_11_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_157_roc_11_vel_21d},
    "copp_158_roc_11_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_158_roc_11_vel_63d},
    "copp_159_roc_11_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_159_roc_11_vel_126d},
    "copp_160_roc_11_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_160_roc_11_vel_252d},
    "copp_161_copp_sum_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_161_copp_sum_vel_5d},
    "copp_162_copp_sum_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_162_copp_sum_vel_21d},
    "copp_163_copp_sum_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_163_copp_sum_vel_63d},
    "copp_164_copp_sum_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_164_copp_sum_vel_126d},
    "copp_165_copp_sum_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_165_copp_sum_vel_252d},
    "copp_166_copp_wma_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_166_copp_wma_vel_5d},
    "copp_167_copp_wma_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_167_copp_wma_vel_21d},
    "copp_168_copp_wma_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_168_copp_wma_vel_63d},
    "copp_169_copp_wma_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_169_copp_wma_vel_126d},
    "copp_170_copp_wma_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_170_copp_wma_vel_252d},
    "copp_171_copp_lvl_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_171_copp_lvl_vel_5d},
    "copp_172_copp_lvl_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_172_copp_lvl_vel_21d},
    "copp_173_copp_lvl_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_173_copp_lvl_vel_63d},
    "copp_174_copp_lvl_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_174_copp_lvl_vel_126d},
    "copp_175_copp_lvl_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_175_copp_lvl_vel_252d},
}
