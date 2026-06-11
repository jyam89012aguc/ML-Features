"""
90_copp_dynamics — 3rd Derivatives (Acceleration)
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

def copp_176_roc_14_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_176_roc_14_accel_5d"""
    return (close.pct_change(14)).diff(5).diff(21)

def copp_177_roc_14_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_177_roc_14_accel_21d"""
    return (close.pct_change(14)).diff(21).diff(21)

def copp_178_roc_14_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_178_roc_14_accel_63d"""
    return (close.pct_change(14)).diff(63).diff(21)

def copp_179_roc_14_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_179_roc_14_accel_126d"""
    return (close.pct_change(14)).diff(126).diff(21)

def copp_180_roc_14_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_180_roc_14_accel_252d"""
    return (close.pct_change(14)).diff(252).diff(21)

def copp_181_roc_11_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_181_roc_11_accel_5d"""
    return (close.pct_change(11)).diff(5).diff(21)

def copp_182_roc_11_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_182_roc_11_accel_21d"""
    return (close.pct_change(11)).diff(21).diff(21)

def copp_183_roc_11_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_183_roc_11_accel_63d"""
    return (close.pct_change(11)).diff(63).diff(21)

def copp_184_roc_11_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_184_roc_11_accel_126d"""
    return (close.pct_change(11)).diff(126).diff(21)

def copp_185_roc_11_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_185_roc_11_accel_252d"""
    return (close.pct_change(11)).diff(252).diff(21)

def copp_186_copp_sum_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_186_copp_sum_accel_5d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(5).diff(21)

def copp_187_copp_sum_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_187_copp_sum_accel_21d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(21).diff(21)

def copp_188_copp_sum_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_188_copp_sum_accel_63d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(63).diff(21)

def copp_189_copp_sum_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_189_copp_sum_accel_126d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(126).diff(21)

def copp_190_copp_sum_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_190_copp_sum_accel_252d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(252).diff(21)

def copp_191_copp_wma_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_191_copp_wma_accel_5d"""
    return ((close.pct_change(14) + close.pct_change(11)).rolling(10).mean()).diff(5).diff(21)

def copp_192_copp_wma_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_192_copp_wma_accel_21d"""
    return ((close.pct_change(14) + close.pct_change(11)).rolling(10).mean()).diff(21).diff(21)

def copp_193_copp_wma_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_193_copp_wma_accel_63d"""
    return ((close.pct_change(14) + close.pct_change(11)).rolling(10).mean()).diff(63).diff(21)

def copp_194_copp_wma_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_194_copp_wma_accel_126d"""
    return ((close.pct_change(14) + close.pct_change(11)).rolling(10).mean()).diff(126).diff(21)

def copp_195_copp_wma_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_195_copp_wma_accel_252d"""
    return ((close.pct_change(14) + close.pct_change(11)).rolling(10).mean()).diff(252).diff(21)

def copp_196_copp_lvl_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_196_copp_lvl_accel_5d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(5).diff(21)

def copp_197_copp_lvl_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_197_copp_lvl_accel_21d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(21).diff(21)

def copp_198_copp_lvl_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_198_copp_lvl_accel_63d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(63).diff(21)

def copp_199_copp_lvl_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_199_copp_lvl_accel_126d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(126).diff(21)

def copp_200_copp_lvl_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """copp_200_copp_lvl_accel_252d"""
    return (close.pct_change(14) + close.pct_change(11)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V90_REGISTRY_ACCEL = {
    "copp_176_roc_14_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_176_roc_14_accel_5d},
    "copp_177_roc_14_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_177_roc_14_accel_21d},
    "copp_178_roc_14_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_178_roc_14_accel_63d},
    "copp_179_roc_14_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_179_roc_14_accel_126d},
    "copp_180_roc_14_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_180_roc_14_accel_252d},
    "copp_181_roc_11_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_181_roc_11_accel_5d},
    "copp_182_roc_11_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_182_roc_11_accel_21d},
    "copp_183_roc_11_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_183_roc_11_accel_63d},
    "copp_184_roc_11_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_184_roc_11_accel_126d},
    "copp_185_roc_11_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_185_roc_11_accel_252d},
    "copp_186_copp_sum_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_186_copp_sum_accel_5d},
    "copp_187_copp_sum_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_187_copp_sum_accel_21d},
    "copp_188_copp_sum_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_188_copp_sum_accel_63d},
    "copp_189_copp_sum_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_189_copp_sum_accel_126d},
    "copp_190_copp_sum_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_190_copp_sum_accel_252d},
    "copp_191_copp_wma_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_191_copp_wma_accel_5d},
    "copp_192_copp_wma_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_192_copp_wma_accel_21d},
    "copp_193_copp_wma_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_193_copp_wma_accel_63d},
    "copp_194_copp_wma_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_194_copp_wma_accel_126d},
    "copp_195_copp_wma_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_195_copp_wma_accel_252d},
    "copp_196_copp_lvl_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": copp_196_copp_lvl_accel_5d},
    "copp_197_copp_lvl_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": copp_197_copp_lvl_accel_21d},
    "copp_198_copp_lvl_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": copp_198_copp_lvl_accel_63d},
    "copp_199_copp_lvl_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": copp_199_copp_lvl_accel_126d},
    "copp_200_copp_lvl_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": copp_200_copp_lvl_accel_252d},
}
