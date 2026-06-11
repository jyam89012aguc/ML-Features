"""
99_vlrs_dynamics — 2nd Derivatives (Velocity)
Domain: vlrs_dynamics
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

def vlrs_151_vol_rs_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_151_vol_rs_vel_5d"""
    return (_safe_div(volume, mkt_volume)).diff(5)

def vlrs_152_vol_rs_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_152_vol_rs_vel_21d"""
    return (_safe_div(volume, mkt_volume)).diff(21)

def vlrs_153_vol_rs_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_153_vol_rs_vel_63d"""
    return (_safe_div(volume, mkt_volume)).diff(63)

def vlrs_154_vol_rs_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_154_vol_rs_vel_126d"""
    return (_safe_div(volume, mkt_volume)).diff(126)

def vlrs_155_vol_rs_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_155_vol_rs_vel_252d"""
    return (_safe_div(volume, mkt_volume)).diff(252)

def vlrs_156_vol_rs_z_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_156_vol_rs_z_vel_5d"""
    return (_zscore_rolling(_safe_div(volume, mkt_volume), 252)).diff(5)

def vlrs_157_vol_rs_z_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_157_vol_rs_z_vel_21d"""
    return (_zscore_rolling(_safe_div(volume, mkt_volume), 252)).diff(21)

def vlrs_158_vol_rs_z_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_158_vol_rs_z_vel_63d"""
    return (_zscore_rolling(_safe_div(volume, mkt_volume), 252)).diff(63)

def vlrs_159_vol_rs_z_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_159_vol_rs_z_vel_126d"""
    return (_zscore_rolling(_safe_div(volume, mkt_volume), 252)).diff(126)

def vlrs_160_vol_rs_z_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_160_vol_rs_z_vel_252d"""
    return (_zscore_rolling(_safe_div(volume, mkt_volume), 252)).diff(252)

def vlrs_161_vol_rs_roc_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_161_vol_rs_roc_vel_5d"""
    return (_safe_div(volume, mkt_volume).pct_change(21)).diff(5)

def vlrs_162_vol_rs_roc_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_162_vol_rs_roc_vel_21d"""
    return (_safe_div(volume, mkt_volume).pct_change(21)).diff(21)

def vlrs_163_vol_rs_roc_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_163_vol_rs_roc_vel_63d"""
    return (_safe_div(volume, mkt_volume).pct_change(21)).diff(63)

def vlrs_164_vol_rs_roc_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_164_vol_rs_roc_vel_126d"""
    return (_safe_div(volume, mkt_volume).pct_change(21)).diff(126)

def vlrs_165_vol_rs_roc_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_165_vol_rs_roc_vel_252d"""
    return (_safe_div(volume, mkt_volume).pct_change(21)).diff(252)

def vlrs_166_vol_rs_sma_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_166_vol_rs_sma_vel_5d"""
    return (_safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))).diff(5)

def vlrs_167_vol_rs_sma_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_167_vol_rs_sma_vel_21d"""
    return (_safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))).diff(21)

def vlrs_168_vol_rs_sma_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_168_vol_rs_sma_vel_63d"""
    return (_safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))).diff(63)

def vlrs_169_vol_rs_sma_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_169_vol_rs_sma_vel_126d"""
    return (_safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))).diff(126)

def vlrs_170_vol_rs_sma_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_170_vol_rs_sma_vel_252d"""
    return (_safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))).diff(252)

def vlrs_171_vol_rs_rank_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_171_vol_rs_rank_vel_5d"""
    return (_rank_pct(_safe_div(volume, mkt_volume), 252)).diff(5)

def vlrs_172_vol_rs_rank_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_172_vol_rs_rank_vel_21d"""
    return (_rank_pct(_safe_div(volume, mkt_volume), 252)).diff(21)

def vlrs_173_vol_rs_rank_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_173_vol_rs_rank_vel_63d"""
    return (_rank_pct(_safe_div(volume, mkt_volume), 252)).diff(63)

def vlrs_174_vol_rs_rank_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_174_vol_rs_rank_vel_126d"""
    return (_rank_pct(_safe_div(volume, mkt_volume), 252)).diff(126)

def vlrs_175_vol_rs_rank_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_175_vol_rs_rank_vel_252d"""
    return (_rank_pct(_safe_div(volume, mkt_volume), 252)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V99_REGISTRY_VEL = {
    "vlrs_151_vol_rs_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_151_vol_rs_vel_5d},
    "vlrs_152_vol_rs_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_152_vol_rs_vel_21d},
    "vlrs_153_vol_rs_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_153_vol_rs_vel_63d},
    "vlrs_154_vol_rs_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_154_vol_rs_vel_126d},
    "vlrs_155_vol_rs_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_155_vol_rs_vel_252d},
    "vlrs_156_vol_rs_z_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_156_vol_rs_z_vel_5d},
    "vlrs_157_vol_rs_z_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_157_vol_rs_z_vel_21d},
    "vlrs_158_vol_rs_z_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_158_vol_rs_z_vel_63d},
    "vlrs_159_vol_rs_z_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_159_vol_rs_z_vel_126d},
    "vlrs_160_vol_rs_z_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_160_vol_rs_z_vel_252d},
    "vlrs_161_vol_rs_roc_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_161_vol_rs_roc_vel_5d},
    "vlrs_162_vol_rs_roc_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_162_vol_rs_roc_vel_21d},
    "vlrs_163_vol_rs_roc_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_163_vol_rs_roc_vel_63d},
    "vlrs_164_vol_rs_roc_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_164_vol_rs_roc_vel_126d},
    "vlrs_165_vol_rs_roc_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_165_vol_rs_roc_vel_252d},
    "vlrs_166_vol_rs_sma_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_166_vol_rs_sma_vel_5d},
    "vlrs_167_vol_rs_sma_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_167_vol_rs_sma_vel_21d},
    "vlrs_168_vol_rs_sma_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_168_vol_rs_sma_vel_63d},
    "vlrs_169_vol_rs_sma_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_169_vol_rs_sma_vel_126d},
    "vlrs_170_vol_rs_sma_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_170_vol_rs_sma_vel_252d},
    "vlrs_171_vol_rs_rank_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_171_vol_rs_rank_vel_5d},
    "vlrs_172_vol_rs_rank_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_172_vol_rs_rank_vel_21d},
    "vlrs_173_vol_rs_rank_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_173_vol_rs_rank_vel_63d},
    "vlrs_174_vol_rs_rank_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_174_vol_rs_rank_vel_126d},
    "vlrs_175_vol_rs_rank_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_175_vol_rs_rank_vel_252d},
}
