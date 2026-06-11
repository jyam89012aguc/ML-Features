"""
96_mrrs_dynamics — 3rd Derivatives (Acceleration)
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

def mrrs_176_rs_ratio_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_176_rs_ratio_accel_5d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).diff(5).diff(21)

def mrrs_177_rs_ratio_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_177_rs_ratio_accel_21d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).diff(21).diff(21)

def mrrs_178_rs_ratio_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_178_rs_ratio_accel_63d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).diff(63).diff(21)

def mrrs_179_rs_ratio_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_179_rs_ratio_accel_126d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).diff(126).diff(21)

def mrrs_180_rs_ratio_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_180_rs_ratio_accel_252d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))).diff(252).diff(21)

def mrrs_181_rs_mom_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_181_rs_mom_accel_5d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).diff(5).diff(21)

def mrrs_182_rs_mom_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_182_rs_mom_accel_21d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).diff(21).diff(21)

def mrrs_183_rs_mom_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_183_rs_mom_accel_63d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).diff(63).diff(21)

def mrrs_184_rs_mom_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_184_rs_mom_accel_126d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).diff(126).diff(21)

def mrrs_185_rs_mom_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_185_rs_mom_accel_252d"""
    return (100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))).diff(252).diff(21)

def mrrs_186_rs_lvl_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_186_rs_lvl_accel_5d"""
    return (_safe_div(close, mkt_close)).diff(5).diff(21)

def mrrs_187_rs_lvl_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_187_rs_lvl_accel_21d"""
    return (_safe_div(close, mkt_close)).diff(21).diff(21)

def mrrs_188_rs_lvl_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_188_rs_lvl_accel_63d"""
    return (_safe_div(close, mkt_close)).diff(63).diff(21)

def mrrs_189_rs_lvl_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_189_rs_lvl_accel_126d"""
    return (_safe_div(close, mkt_close)).diff(126).diff(21)

def mrrs_190_rs_lvl_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_190_rs_lvl_accel_252d"""
    return (_safe_div(close, mkt_close)).diff(252).diff(21)

def mrrs_191_rs_z_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_191_rs_z_accel_5d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(5).diff(21)

def mrrs_192_rs_z_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_192_rs_z_accel_21d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(21).diff(21)

def mrrs_193_rs_z_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_193_rs_z_accel_63d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(63).diff(21)

def mrrs_194_rs_z_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_194_rs_z_accel_126d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(126).diff(21)

def mrrs_195_rs_z_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_195_rs_z_accel_252d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(252).diff(21)

def mrrs_196_rs_roc_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_196_rs_roc_accel_5d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(5).diff(21)

def mrrs_197_rs_roc_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_197_rs_roc_accel_21d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(21).diff(21)

def mrrs_198_rs_roc_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_198_rs_roc_accel_63d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(63).diff(21)

def mrrs_199_rs_roc_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_199_rs_roc_accel_126d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(126).diff(21)

def mrrs_200_rs_roc_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_200_rs_roc_accel_252d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V96_REGISTRY_ACCEL = {
    "mrrs_176_rs_ratio_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_176_rs_ratio_accel_5d},
    "mrrs_177_rs_ratio_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_177_rs_ratio_accel_21d},
    "mrrs_178_rs_ratio_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_178_rs_ratio_accel_63d},
    "mrrs_179_rs_ratio_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_179_rs_ratio_accel_126d},
    "mrrs_180_rs_ratio_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_180_rs_ratio_accel_252d},
    "mrrs_181_rs_mom_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_181_rs_mom_accel_5d},
    "mrrs_182_rs_mom_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_182_rs_mom_accel_21d},
    "mrrs_183_rs_mom_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_183_rs_mom_accel_63d},
    "mrrs_184_rs_mom_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_184_rs_mom_accel_126d},
    "mrrs_185_rs_mom_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_185_rs_mom_accel_252d},
    "mrrs_186_rs_lvl_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_186_rs_lvl_accel_5d},
    "mrrs_187_rs_lvl_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_187_rs_lvl_accel_21d},
    "mrrs_188_rs_lvl_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_188_rs_lvl_accel_63d},
    "mrrs_189_rs_lvl_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_189_rs_lvl_accel_126d},
    "mrrs_190_rs_lvl_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_190_rs_lvl_accel_252d},
    "mrrs_191_rs_z_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_191_rs_z_accel_5d},
    "mrrs_192_rs_z_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_192_rs_z_accel_21d},
    "mrrs_193_rs_z_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_193_rs_z_accel_63d},
    "mrrs_194_rs_z_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_194_rs_z_accel_126d},
    "mrrs_195_rs_z_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_195_rs_z_accel_252d},
    "mrrs_196_rs_roc_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_196_rs_roc_accel_5d},
    "mrrs_197_rs_roc_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_197_rs_roc_accel_21d},
    "mrrs_198_rs_roc_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_198_rs_roc_accel_63d},
    "mrrs_199_rs_roc_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_199_rs_roc_accel_126d},
    "mrrs_200_rs_roc_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_200_rs_roc_accel_252d},
}
