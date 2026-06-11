"""
98_srrs_dynamics — 2nd Derivatives (Velocity)
Domain: srrs_dynamics
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

def srrs_151_sec_rs_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_151_sec_rs_vel_5d"""
    return (_safe_div(close, mkt_close)).diff(5)

def srrs_152_sec_rs_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_152_sec_rs_vel_21d"""
    return (_safe_div(close, mkt_close)).diff(21)

def srrs_153_sec_rs_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_153_sec_rs_vel_63d"""
    return (_safe_div(close, mkt_close)).diff(63)

def srrs_154_sec_rs_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_154_sec_rs_vel_126d"""
    return (_safe_div(close, mkt_close)).diff(126)

def srrs_155_sec_rs_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_155_sec_rs_vel_252d"""
    return (_safe_div(close, mkt_close)).diff(252)

def srrs_156_sec_rs_z_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_156_sec_rs_z_vel_5d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(5)

def srrs_157_sec_rs_z_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_157_sec_rs_z_vel_21d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(21)

def srrs_158_sec_rs_z_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_158_sec_rs_z_vel_63d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(63)

def srrs_159_sec_rs_z_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_159_sec_rs_z_vel_126d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(126)

def srrs_160_sec_rs_z_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_160_sec_rs_z_vel_252d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(252)

def srrs_161_sec_rs_roc_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_161_sec_rs_roc_vel_5d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(5)

def srrs_162_sec_rs_roc_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_162_sec_rs_roc_vel_21d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(21)

def srrs_163_sec_rs_roc_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_163_sec_rs_roc_vel_63d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(63)

def srrs_164_sec_rs_roc_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_164_sec_rs_roc_vel_126d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(126)

def srrs_165_sec_rs_roc_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_165_sec_rs_roc_vel_252d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(252)

def srrs_166_sec_rs_mom_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_166_sec_rs_mom_vel_5d"""
    return (_safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))).diff(5)

def srrs_167_sec_rs_mom_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_167_sec_rs_mom_vel_21d"""
    return (_safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))).diff(21)

def srrs_168_sec_rs_mom_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_168_sec_rs_mom_vel_63d"""
    return (_safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))).diff(63)

def srrs_169_sec_rs_mom_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_169_sec_rs_mom_vel_126d"""
    return (_safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))).diff(126)

def srrs_170_sec_rs_mom_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_170_sec_rs_mom_vel_252d"""
    return (_safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))).diff(252)

def srrs_171_sec_rs_rank_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_171_sec_rs_rank_vel_5d"""
    return (_rank_pct(_safe_div(close, mkt_close), 252)).diff(5)

def srrs_172_sec_rs_rank_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_172_sec_rs_rank_vel_21d"""
    return (_rank_pct(_safe_div(close, mkt_close), 252)).diff(21)

def srrs_173_sec_rs_rank_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_173_sec_rs_rank_vel_63d"""
    return (_rank_pct(_safe_div(close, mkt_close), 252)).diff(63)

def srrs_174_sec_rs_rank_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_174_sec_rs_rank_vel_126d"""
    return (_rank_pct(_safe_div(close, mkt_close), 252)).diff(126)

def srrs_175_sec_rs_rank_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_175_sec_rs_rank_vel_252d"""
    return (_rank_pct(_safe_div(close, mkt_close), 252)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V98_REGISTRY_VEL = {
    "srrs_151_sec_rs_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_151_sec_rs_vel_5d},
    "srrs_152_sec_rs_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_152_sec_rs_vel_21d},
    "srrs_153_sec_rs_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_153_sec_rs_vel_63d},
    "srrs_154_sec_rs_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_154_sec_rs_vel_126d},
    "srrs_155_sec_rs_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_155_sec_rs_vel_252d},
    "srrs_156_sec_rs_z_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_156_sec_rs_z_vel_5d},
    "srrs_157_sec_rs_z_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_157_sec_rs_z_vel_21d},
    "srrs_158_sec_rs_z_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_158_sec_rs_z_vel_63d},
    "srrs_159_sec_rs_z_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_159_sec_rs_z_vel_126d},
    "srrs_160_sec_rs_z_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_160_sec_rs_z_vel_252d},
    "srrs_161_sec_rs_roc_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_161_sec_rs_roc_vel_5d},
    "srrs_162_sec_rs_roc_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_162_sec_rs_roc_vel_21d},
    "srrs_163_sec_rs_roc_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_163_sec_rs_roc_vel_63d},
    "srrs_164_sec_rs_roc_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_164_sec_rs_roc_vel_126d},
    "srrs_165_sec_rs_roc_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_165_sec_rs_roc_vel_252d},
    "srrs_166_sec_rs_mom_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_166_sec_rs_mom_vel_5d},
    "srrs_167_sec_rs_mom_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_167_sec_rs_mom_vel_21d},
    "srrs_168_sec_rs_mom_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_168_sec_rs_mom_vel_63d},
    "srrs_169_sec_rs_mom_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_169_sec_rs_mom_vel_126d},
    "srrs_170_sec_rs_mom_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_170_sec_rs_mom_vel_252d},
    "srrs_171_sec_rs_rank_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_171_sec_rs_rank_vel_5d},
    "srrs_172_sec_rs_rank_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_172_sec_rs_rank_vel_21d},
    "srrs_173_sec_rs_rank_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_173_sec_rs_rank_vel_63d},
    "srrs_174_sec_rs_rank_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_174_sec_rs_rank_vel_126d},
    "srrs_175_sec_rs_rank_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_175_sec_rs_rank_vel_252d},
}
