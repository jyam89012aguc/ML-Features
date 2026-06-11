"""
96_mrrs_dynamics — 2nd Derivatives (Velocity)
Domain: mrrs_dynamics
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

def mrrs_151_rs_ratio_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_151_rs_ratio_vel_5d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).diff(5)

def mrrs_152_rs_ratio_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_152_rs_ratio_vel_21d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).diff(21)

def mrrs_153_rs_ratio_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_153_rs_ratio_vel_63d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).diff(63)

def mrrs_154_rs_ratio_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_154_rs_ratio_vel_126d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).diff(126)

def mrrs_155_rs_ratio_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_155_rs_ratio_vel_252d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).diff(252)

def mrrs_156_rs_mom_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_156_rs_mom_vel_5d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).diff(5)

def mrrs_157_rs_mom_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_157_rs_mom_vel_21d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).diff(21)

def mrrs_158_rs_mom_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_158_rs_mom_vel_63d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).diff(63)

def mrrs_159_rs_mom_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_159_rs_mom_vel_126d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).diff(126)

def mrrs_160_rs_mom_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_160_rs_mom_vel_252d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).diff(252)

def mrrs_161_rs_lvl_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_161_rs_lvl_vel_5d"""
    return (_safe_div(close, mkt_close)).diff(5)

def mrrs_162_rs_lvl_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_162_rs_lvl_vel_21d"""
    return (_safe_div(close, mkt_close)).diff(21)

def mrrs_163_rs_lvl_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_163_rs_lvl_vel_63d"""
    return (_safe_div(close, mkt_close)).diff(63)

def mrrs_164_rs_lvl_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_164_rs_lvl_vel_126d"""
    return (_safe_div(close, mkt_close)).diff(126)

def mrrs_165_rs_lvl_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_165_rs_lvl_vel_252d"""
    return (_safe_div(close, mkt_close)).diff(252)

def mrrs_166_rs_z_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_166_rs_z_vel_5d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(5)

def mrrs_167_rs_z_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_167_rs_z_vel_21d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(21)

def mrrs_168_rs_z_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_168_rs_z_vel_63d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(63)

def mrrs_169_rs_z_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_169_rs_z_vel_126d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(126)

def mrrs_170_rs_z_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_170_rs_z_vel_252d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(252)

def mrrs_171_rs_roc_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_171_rs_roc_vel_5d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(5)

def mrrs_172_rs_roc_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_172_rs_roc_vel_21d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(21)

def mrrs_173_rs_roc_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_173_rs_roc_vel_63d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(63)

def mrrs_174_rs_roc_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_174_rs_roc_vel_126d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(126)

def mrrs_175_rs_roc_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_175_rs_roc_vel_252d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V96_REGISTRY_VEL = {
    "mrrs_151_rs_ratio_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_151_rs_ratio_vel_5d},
    "mrrs_152_rs_ratio_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_152_rs_ratio_vel_21d},
    "mrrs_153_rs_ratio_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_153_rs_ratio_vel_63d},
    "mrrs_154_rs_ratio_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_154_rs_ratio_vel_126d},
    "mrrs_155_rs_ratio_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_155_rs_ratio_vel_252d},
    "mrrs_156_rs_mom_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_156_rs_mom_vel_5d},
    "mrrs_157_rs_mom_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_157_rs_mom_vel_21d},
    "mrrs_158_rs_mom_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_158_rs_mom_vel_63d},
    "mrrs_159_rs_mom_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_159_rs_mom_vel_126d},
    "mrrs_160_rs_mom_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_160_rs_mom_vel_252d},
    "mrrs_161_rs_lvl_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_161_rs_lvl_vel_5d},
    "mrrs_162_rs_lvl_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_162_rs_lvl_vel_21d},
    "mrrs_163_rs_lvl_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_163_rs_lvl_vel_63d},
    "mrrs_164_rs_lvl_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_164_rs_lvl_vel_126d},
    "mrrs_165_rs_lvl_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_165_rs_lvl_vel_252d},
    "mrrs_166_rs_z_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_166_rs_z_vel_5d},
    "mrrs_167_rs_z_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_167_rs_z_vel_21d},
    "mrrs_168_rs_z_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_168_rs_z_vel_63d},
    "mrrs_169_rs_z_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_169_rs_z_vel_126d},
    "mrrs_170_rs_z_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_170_rs_z_vel_252d},
    "mrrs_171_rs_roc_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_171_rs_roc_vel_5d},
    "mrrs_172_rs_roc_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_172_rs_roc_vel_21d},
    "mrrs_173_rs_roc_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_173_rs_roc_vel_63d},
    "mrrs_174_rs_roc_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_174_rs_roc_vel_126d},
    "mrrs_175_rs_roc_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_175_rs_roc_vel_252d},
}
