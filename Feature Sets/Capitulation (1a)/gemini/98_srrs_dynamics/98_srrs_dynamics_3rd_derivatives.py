"""
98_srrs_dynamics — 3rd Derivatives (Acceleration)
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

def srrs_176_sec_rs_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_176_sec_rs_accel_5d"""
    return (_safe_div(close, mkt_close)).diff(5).diff(21)

def srrs_177_sec_rs_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_177_sec_rs_accel_21d"""
    return (_safe_div(close, mkt_close)).diff(21).diff(21)

def srrs_178_sec_rs_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_178_sec_rs_accel_63d"""
    return (_safe_div(close, mkt_close)).diff(63).diff(21)

def srrs_179_sec_rs_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_179_sec_rs_accel_126d"""
    return (_safe_div(close, mkt_close)).diff(126).diff(21)

def srrs_180_sec_rs_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_180_sec_rs_accel_252d"""
    return (_safe_div(close, mkt_close)).diff(252).diff(21)

def srrs_181_sec_rs_z_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_181_sec_rs_z_accel_5d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(5).diff(21)

def srrs_182_sec_rs_z_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_182_sec_rs_z_accel_21d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(21).diff(21)

def srrs_183_sec_rs_z_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_183_sec_rs_z_accel_63d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(63).diff(21)

def srrs_184_sec_rs_z_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_184_sec_rs_z_accel_126d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(126).diff(21)

def srrs_185_sec_rs_z_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_185_sec_rs_z_accel_252d"""
    return (_zscore_rolling(_safe_div(close, mkt_close), 252)).diff(252).diff(21)

def srrs_186_sec_rs_roc_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_186_sec_rs_roc_accel_5d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(5).diff(21)

def srrs_187_sec_rs_roc_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_187_sec_rs_roc_accel_21d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(21).diff(21)

def srrs_188_sec_rs_roc_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_188_sec_rs_roc_accel_63d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(63).diff(21)

def srrs_189_sec_rs_roc_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_189_sec_rs_roc_accel_126d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(126).diff(21)

def srrs_190_sec_rs_roc_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_190_sec_rs_roc_accel_252d"""
    return (_safe_div(close, mkt_close).pct_change(21)).diff(252).diff(21)

def srrs_191_sec_rs_mom_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_191_sec_rs_mom_accel_5d"""
    return (_safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))).diff(5).diff(21)

def srrs_192_sec_rs_mom_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_192_sec_rs_mom_accel_21d"""
    return (_safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))).diff(21).diff(21)

def srrs_193_sec_rs_mom_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_193_sec_rs_mom_accel_63d"""
    return (_safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))).diff(63).diff(21)

def srrs_194_sec_rs_mom_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_194_sec_rs_mom_accel_126d"""
    return (_safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))).diff(126).diff(21)

def srrs_195_sec_rs_mom_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_195_sec_rs_mom_accel_252d"""
    return (_safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))).diff(252).diff(21)

def srrs_196_sec_rs_rank_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_196_sec_rs_rank_accel_5d"""
    return (_rank_pct(_safe_div(close, mkt_close), 252)).diff(5).diff(21)

def srrs_197_sec_rs_rank_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_197_sec_rs_rank_accel_21d"""
    return (_rank_pct(_safe_div(close, mkt_close), 252)).diff(21).diff(21)

def srrs_198_sec_rs_rank_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_198_sec_rs_rank_accel_63d"""
    return (_rank_pct(_safe_div(close, mkt_close), 252)).diff(63).diff(21)

def srrs_199_sec_rs_rank_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_199_sec_rs_rank_accel_126d"""
    return (_rank_pct(_safe_div(close, mkt_close), 252)).diff(126).diff(21)

def srrs_200_sec_rs_rank_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_200_sec_rs_rank_accel_252d"""
    return (_rank_pct(_safe_div(close, mkt_close), 252)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V98_REGISTRY_ACCEL = {
    "srrs_176_sec_rs_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_176_sec_rs_accel_5d},
    "srrs_177_sec_rs_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_177_sec_rs_accel_21d},
    "srrs_178_sec_rs_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_178_sec_rs_accel_63d},
    "srrs_179_sec_rs_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_179_sec_rs_accel_126d},
    "srrs_180_sec_rs_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_180_sec_rs_accel_252d},
    "srrs_181_sec_rs_z_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_181_sec_rs_z_accel_5d},
    "srrs_182_sec_rs_z_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_182_sec_rs_z_accel_21d},
    "srrs_183_sec_rs_z_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_183_sec_rs_z_accel_63d},
    "srrs_184_sec_rs_z_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_184_sec_rs_z_accel_126d},
    "srrs_185_sec_rs_z_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_185_sec_rs_z_accel_252d},
    "srrs_186_sec_rs_roc_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_186_sec_rs_roc_accel_5d},
    "srrs_187_sec_rs_roc_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_187_sec_rs_roc_accel_21d},
    "srrs_188_sec_rs_roc_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_188_sec_rs_roc_accel_63d},
    "srrs_189_sec_rs_roc_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_189_sec_rs_roc_accel_126d},
    "srrs_190_sec_rs_roc_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_190_sec_rs_roc_accel_252d},
    "srrs_191_sec_rs_mom_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_191_sec_rs_mom_accel_5d},
    "srrs_192_sec_rs_mom_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_192_sec_rs_mom_accel_21d},
    "srrs_193_sec_rs_mom_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_193_sec_rs_mom_accel_63d},
    "srrs_194_sec_rs_mom_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_194_sec_rs_mom_accel_126d},
    "srrs_195_sec_rs_mom_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_195_sec_rs_mom_accel_252d},
    "srrs_196_sec_rs_rank_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_196_sec_rs_rank_accel_5d},
    "srrs_197_sec_rs_rank_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_197_sec_rs_rank_accel_21d},
    "srrs_198_sec_rs_rank_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_198_sec_rs_rank_accel_63d},
    "srrs_199_sec_rs_rank_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_199_sec_rs_rank_accel_126d},
    "srrs_200_sec_rs_rank_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_200_sec_rs_rank_accel_252d},
}
