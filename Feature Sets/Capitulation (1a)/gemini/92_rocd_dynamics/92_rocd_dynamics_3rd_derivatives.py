"""
92_rocd_dynamics — 3rd Derivatives (Acceleration)
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

def rocd_176_roc_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_176_roc_accel_5d"""
    return (close.pct_change(21)).diff(5).diff(21)

def rocd_177_roc_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_177_roc_accel_21d"""
    return (close.pct_change(21)).diff(21).diff(21)

def rocd_178_roc_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_178_roc_accel_63d"""
    return (close.pct_change(21)).diff(63).diff(21)

def rocd_179_roc_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_179_roc_accel_126d"""
    return (close.pct_change(21)).diff(126).diff(21)

def rocd_180_roc_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_180_roc_accel_252d"""
    return (close.pct_change(21)).diff(252).diff(21)

def rocd_181_vroc_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_181_vroc_accel_5d"""
    return (volume.pct_change(21)).diff(5).diff(21)

def rocd_182_vroc_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_182_vroc_accel_21d"""
    return (volume.pct_change(21)).diff(21).diff(21)

def rocd_183_vroc_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_183_vroc_accel_63d"""
    return (volume.pct_change(21)).diff(63).diff(21)

def rocd_184_vroc_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_184_vroc_accel_126d"""
    return (volume.pct_change(21)).diff(126).diff(21)

def rocd_185_vroc_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_185_vroc_accel_252d"""
    return (volume.pct_change(21)).diff(252).diff(21)

def rocd_186_roc_z_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_186_roc_z_accel_5d"""
    return (_zscore_rolling(close.pct_change(21), 63)).diff(5).diff(21)

def rocd_187_roc_z_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_187_roc_z_accel_21d"""
    return (_zscore_rolling(close.pct_change(21), 63)).diff(21).diff(21)

def rocd_188_roc_z_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_188_roc_z_accel_63d"""
    return (_zscore_rolling(close.pct_change(21), 63)).diff(63).diff(21)

def rocd_189_roc_z_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_189_roc_z_accel_126d"""
    return (_zscore_rolling(close.pct_change(21), 63)).diff(126).diff(21)

def rocd_190_roc_z_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_190_roc_z_accel_252d"""
    return (_zscore_rolling(close.pct_change(21), 63)).diff(252).diff(21)

def rocd_191_vroc_z_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_191_vroc_z_accel_5d"""
    return (_zscore_rolling(volume.pct_change(21), 63)).diff(5).diff(21)

def rocd_192_vroc_z_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_192_vroc_z_accel_21d"""
    return (_zscore_rolling(volume.pct_change(21), 63)).diff(21).diff(21)

def rocd_193_vroc_z_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_193_vroc_z_accel_63d"""
    return (_zscore_rolling(volume.pct_change(21), 63)).diff(63).diff(21)

def rocd_194_vroc_z_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_194_vroc_z_accel_126d"""
    return (_zscore_rolling(volume.pct_change(21), 63)).diff(126).diff(21)

def rocd_195_vroc_z_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_195_vroc_z_accel_252d"""
    return (_zscore_rolling(volume.pct_change(21), 63)).diff(252).diff(21)

def rocd_196_roc_vol_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_196_roc_vol_accel_5d"""
    return (_safe_div(close.pct_change(21), volume.pct_change(21).abs())).diff(5).diff(21)

def rocd_197_roc_vol_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_197_roc_vol_accel_21d"""
    return (_safe_div(close.pct_change(21), volume.pct_change(21).abs())).diff(21).diff(21)

def rocd_198_roc_vol_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_198_roc_vol_accel_63d"""
    return (_safe_div(close.pct_change(21), volume.pct_change(21).abs())).diff(63).diff(21)

def rocd_199_roc_vol_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_199_roc_vol_accel_126d"""
    return (_safe_div(close.pct_change(21), volume.pct_change(21).abs())).diff(126).diff(21)

def rocd_200_roc_vol_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """rocd_200_roc_vol_accel_252d"""
    return (_safe_div(close.pct_change(21), volume.pct_change(21).abs())).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V92_REGISTRY_ACCEL = {
    "rocd_176_roc_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_176_roc_accel_5d},
    "rocd_177_roc_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_177_roc_accel_21d},
    "rocd_178_roc_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_178_roc_accel_63d},
    "rocd_179_roc_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_179_roc_accel_126d},
    "rocd_180_roc_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_180_roc_accel_252d},
    "rocd_181_vroc_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_181_vroc_accel_5d},
    "rocd_182_vroc_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_182_vroc_accel_21d},
    "rocd_183_vroc_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_183_vroc_accel_63d},
    "rocd_184_vroc_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_184_vroc_accel_126d},
    "rocd_185_vroc_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_185_vroc_accel_252d},
    "rocd_186_roc_z_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_186_roc_z_accel_5d},
    "rocd_187_roc_z_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_187_roc_z_accel_21d},
    "rocd_188_roc_z_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_188_roc_z_accel_63d},
    "rocd_189_roc_z_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_189_roc_z_accel_126d},
    "rocd_190_roc_z_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_190_roc_z_accel_252d},
    "rocd_191_vroc_z_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_191_vroc_z_accel_5d},
    "rocd_192_vroc_z_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_192_vroc_z_accel_21d},
    "rocd_193_vroc_z_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_193_vroc_z_accel_63d},
    "rocd_194_vroc_z_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_194_vroc_z_accel_126d},
    "rocd_195_vroc_z_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_195_vroc_z_accel_252d},
    "rocd_196_roc_vol_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_196_roc_vol_accel_5d},
    "rocd_197_roc_vol_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_197_roc_vol_accel_21d},
    "rocd_198_roc_vol_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_198_roc_vol_accel_63d},
    "rocd_199_roc_vol_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_199_roc_vol_accel_126d},
    "rocd_200_roc_vol_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": rocd_200_roc_vol_accel_252d},
}
