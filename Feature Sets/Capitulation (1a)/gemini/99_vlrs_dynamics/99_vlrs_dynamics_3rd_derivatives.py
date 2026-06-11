"""
99_vlrs_dynamics — 3rd Derivatives (Acceleration)
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

def vlrs_176_vol_rs_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_176_vol_rs_accel_5d"""
    return (_safe_div(volume, mkt_volume)).diff(5).diff(21)

def vlrs_177_vol_rs_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_177_vol_rs_accel_21d"""
    return (_safe_div(volume, mkt_volume)).diff(21).diff(21)

def vlrs_178_vol_rs_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_178_vol_rs_accel_63d"""
    return (_safe_div(volume, mkt_volume)).diff(63).diff(21)

def vlrs_179_vol_rs_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_179_vol_rs_accel_126d"""
    return (_safe_div(volume, mkt_volume)).diff(126).diff(21)

def vlrs_180_vol_rs_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_180_vol_rs_accel_252d"""
    return (_safe_div(volume, mkt_volume)).diff(252).diff(21)

def vlrs_181_vol_rs_z_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_181_vol_rs_z_accel_5d"""
    return (_zscore_rolling(_safe_div(volume, mkt_volume), 252)).diff(5).diff(21)

def vlrs_182_vol_rs_z_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_182_vol_rs_z_accel_21d"""
    return (_zscore_rolling(_safe_div(volume, mkt_volume), 252)).diff(21).diff(21)

def vlrs_183_vol_rs_z_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_183_vol_rs_z_accel_63d"""
    return (_zscore_rolling(_safe_div(volume, mkt_volume), 252)).diff(63).diff(21)

def vlrs_184_vol_rs_z_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_184_vol_rs_z_accel_126d"""
    return (_zscore_rolling(_safe_div(volume, mkt_volume), 252)).diff(126).diff(21)

def vlrs_185_vol_rs_z_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_185_vol_rs_z_accel_252d"""
    return (_zscore_rolling(_safe_div(volume, mkt_volume), 252)).diff(252).diff(21)

def vlrs_186_vol_rs_roc_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_186_vol_rs_roc_accel_5d"""
    return (_safe_div(volume, mkt_volume).pct_change(21)).diff(5).diff(21)

def vlrs_187_vol_rs_roc_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_187_vol_rs_roc_accel_21d"""
    return (_safe_div(volume, mkt_volume).pct_change(21)).diff(21).diff(21)

def vlrs_188_vol_rs_roc_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_188_vol_rs_roc_accel_63d"""
    return (_safe_div(volume, mkt_volume).pct_change(21)).diff(63).diff(21)

def vlrs_189_vol_rs_roc_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_189_vol_rs_roc_accel_126d"""
    return (_safe_div(volume, mkt_volume).pct_change(21)).diff(126).diff(21)

def vlrs_190_vol_rs_roc_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_190_vol_rs_roc_accel_252d"""
    return (_safe_div(volume, mkt_volume).pct_change(21)).diff(252).diff(21)

def vlrs_191_vol_rs_sma_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_191_vol_rs_sma_accel_5d"""
    return (_safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))).diff(5).diff(21)

def vlrs_192_vol_rs_sma_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_192_vol_rs_sma_accel_21d"""
    return (_safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))).diff(21).diff(21)

def vlrs_193_vol_rs_sma_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_193_vol_rs_sma_accel_63d"""
    return (_safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))).diff(63).diff(21)

def vlrs_194_vol_rs_sma_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_194_vol_rs_sma_accel_126d"""
    return (_safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))).diff(126).diff(21)

def vlrs_195_vol_rs_sma_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_195_vol_rs_sma_accel_252d"""
    return (_safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))).diff(252).diff(21)

def vlrs_196_vol_rs_rank_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_196_vol_rs_rank_accel_5d"""
    return (_rank_pct(_safe_div(volume, mkt_volume), 252)).diff(5).diff(21)

def vlrs_197_vol_rs_rank_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_197_vol_rs_rank_accel_21d"""
    return (_rank_pct(_safe_div(volume, mkt_volume), 252)).diff(21).diff(21)

def vlrs_198_vol_rs_rank_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_198_vol_rs_rank_accel_63d"""
    return (_rank_pct(_safe_div(volume, mkt_volume), 252)).diff(63).diff(21)

def vlrs_199_vol_rs_rank_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_199_vol_rs_rank_accel_126d"""
    return (_rank_pct(_safe_div(volume, mkt_volume), 252)).diff(126).diff(21)

def vlrs_200_vol_rs_rank_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_200_vol_rs_rank_accel_252d"""
    return (_rank_pct(_safe_div(volume, mkt_volume), 252)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V99_REGISTRY_ACCEL = {
    "vlrs_176_vol_rs_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_176_vol_rs_accel_5d},
    "vlrs_177_vol_rs_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_177_vol_rs_accel_21d},
    "vlrs_178_vol_rs_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_178_vol_rs_accel_63d},
    "vlrs_179_vol_rs_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_179_vol_rs_accel_126d},
    "vlrs_180_vol_rs_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_180_vol_rs_accel_252d},
    "vlrs_181_vol_rs_z_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_181_vol_rs_z_accel_5d},
    "vlrs_182_vol_rs_z_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_182_vol_rs_z_accel_21d},
    "vlrs_183_vol_rs_z_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_183_vol_rs_z_accel_63d},
    "vlrs_184_vol_rs_z_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_184_vol_rs_z_accel_126d},
    "vlrs_185_vol_rs_z_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_185_vol_rs_z_accel_252d},
    "vlrs_186_vol_rs_roc_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_186_vol_rs_roc_accel_5d},
    "vlrs_187_vol_rs_roc_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_187_vol_rs_roc_accel_21d},
    "vlrs_188_vol_rs_roc_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_188_vol_rs_roc_accel_63d},
    "vlrs_189_vol_rs_roc_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_189_vol_rs_roc_accel_126d},
    "vlrs_190_vol_rs_roc_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_190_vol_rs_roc_accel_252d},
    "vlrs_191_vol_rs_sma_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_191_vol_rs_sma_accel_5d},
    "vlrs_192_vol_rs_sma_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_192_vol_rs_sma_accel_21d},
    "vlrs_193_vol_rs_sma_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_193_vol_rs_sma_accel_63d},
    "vlrs_194_vol_rs_sma_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_194_vol_rs_sma_accel_126d},
    "vlrs_195_vol_rs_sma_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_195_vol_rs_sma_accel_252d},
    "vlrs_196_vol_rs_rank_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_196_vol_rs_rank_accel_5d},
    "vlrs_197_vol_rs_rank_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_197_vol_rs_rank_accel_21d},
    "vlrs_198_vol_rs_rank_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_198_vol_rs_rank_accel_63d},
    "vlrs_199_vol_rs_rank_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_199_vol_rs_rank_accel_126d},
    "vlrs_200_vol_rs_rank_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_200_vol_rs_rank_accel_252d},
}
