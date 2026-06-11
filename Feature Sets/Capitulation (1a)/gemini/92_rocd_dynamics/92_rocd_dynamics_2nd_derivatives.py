"""
92_rocd_dynamics — 2nd Derivatives (Velocity)
Domain: rocd_dynamics
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

def rocd_151_roc_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_151_roc_vel_5d"""
    return (close.pct_change(21)).diff(5)

def rocd_152_roc_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_152_roc_vel_21d"""
    return (close.pct_change(21)).diff(21)

def rocd_153_roc_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_153_roc_vel_63d"""
    return (close.pct_change(21)).diff(63)

def rocd_154_roc_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_154_roc_vel_126d"""
    return (close.pct_change(21)).diff(126)

def rocd_155_roc_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_155_roc_vel_252d"""
    return (close.pct_change(21)).diff(252)

def rocd_156_vroc_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_156_vroc_vel_5d"""
    return (volume.pct_change(21)).diff(5)

def rocd_157_vroc_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_157_vroc_vel_21d"""
    return (volume.pct_change(21)).diff(21)

def rocd_158_vroc_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_158_vroc_vel_63d"""
    return (volume.pct_change(21)).diff(63)

def rocd_159_vroc_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_159_vroc_vel_126d"""
    return (volume.pct_change(21)).diff(126)

def rocd_160_vroc_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_160_vroc_vel_252d"""
    return (volume.pct_change(21)).diff(252)

def rocd_161_roc_z_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_161_roc_z_vel_5d"""
    return (_zscore_rolling(close.pct_change(21), 63)).diff(5)

def rocd_162_roc_z_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_162_roc_z_vel_21d"""
    return (_zscore_rolling(close.pct_change(21), 63)).diff(21)

def rocd_163_roc_z_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_163_roc_z_vel_63d"""
    return (_zscore_rolling(close.pct_change(21), 63)).diff(63)

def rocd_164_roc_z_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_164_roc_z_vel_126d"""
    return (_zscore_rolling(close.pct_change(21), 63)).diff(126)

def rocd_165_roc_z_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_165_roc_z_vel_252d"""
    return (_zscore_rolling(close.pct_change(21), 63)).diff(252)

def rocd_166_vroc_z_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_166_vroc_z_vel_5d"""
    return (_zscore_rolling(volume.pct_change(21), 63)).diff(5)

def rocd_167_vroc_z_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_167_vroc_z_vel_21d"""
    return (_zscore_rolling(volume.pct_change(21), 63)).diff(21)

def rocd_168_vroc_z_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_168_vroc_z_vel_63d"""
    return (_zscore_rolling(volume.pct_change(21), 63)).diff(63)

def rocd_169_vroc_z_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_169_vroc_z_vel_126d"""
    return (_zscore_rolling(volume.pct_change(21), 63)).diff(126)

def rocd_170_vroc_z_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_170_vroc_z_vel_252d"""
    return (_zscore_rolling(volume.pct_change(21), 63)).diff(252)

def rocd_171_roc_vol_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_171_roc_vol_vel_5d"""
    return (_safe_div(close.pct_change(21), volume.pct_change(21).abs())).diff(5)

def rocd_172_roc_vol_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_172_roc_vol_vel_21d"""
    return (_safe_div(close.pct_change(21), volume.pct_change(21).abs())).diff(21)

def rocd_173_roc_vol_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_173_roc_vol_vel_63d"""
    return (_safe_div(close.pct_change(21), volume.pct_change(21).abs())).diff(63)

def rocd_174_roc_vol_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_174_roc_vol_vel_126d"""
    return (_safe_div(close.pct_change(21), volume.pct_change(21).abs())).diff(126)

def rocd_175_roc_vol_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_175_roc_vol_vel_252d"""
    return (_safe_div(close.pct_change(21), volume.pct_change(21).abs())).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V92_REGISTRY_VEL = {
    "rocd_151_roc_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_151_roc_vel_5d},
    "rocd_152_roc_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_152_roc_vel_21d},
    "rocd_153_roc_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_153_roc_vel_63d},
    "rocd_154_roc_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_154_roc_vel_126d},
    "rocd_155_roc_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_155_roc_vel_252d},
    "rocd_156_vroc_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_156_vroc_vel_5d},
    "rocd_157_vroc_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_157_vroc_vel_21d},
    "rocd_158_vroc_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_158_vroc_vel_63d},
    "rocd_159_vroc_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_159_vroc_vel_126d},
    "rocd_160_vroc_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_160_vroc_vel_252d},
    "rocd_161_roc_z_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_161_roc_z_vel_5d},
    "rocd_162_roc_z_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_162_roc_z_vel_21d},
    "rocd_163_roc_z_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_163_roc_z_vel_63d},
    "rocd_164_roc_z_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_164_roc_z_vel_126d},
    "rocd_165_roc_z_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_165_roc_z_vel_252d},
    "rocd_166_vroc_z_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_166_vroc_z_vel_5d},
    "rocd_167_vroc_z_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_167_vroc_z_vel_21d},
    "rocd_168_vroc_z_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_168_vroc_z_vel_63d},
    "rocd_169_vroc_z_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_169_vroc_z_vel_126d},
    "rocd_170_vroc_z_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_170_vroc_z_vel_252d},
    "rocd_171_roc_vol_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_171_roc_vol_vel_5d},
    "rocd_172_roc_vol_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_172_roc_vol_vel_21d},
    "rocd_173_roc_vol_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_173_roc_vol_vel_63d},
    "rocd_174_roc_vol_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_174_roc_vol_vel_126d},
    "rocd_175_roc_vol_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_175_roc_vol_vel_252d},
}
