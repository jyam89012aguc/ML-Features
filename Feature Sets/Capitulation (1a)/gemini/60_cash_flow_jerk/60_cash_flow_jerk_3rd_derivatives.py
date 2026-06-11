"""
60_cash_flow_jerk — 3rd Derivatives (Acceleration)
Domain: cash_flow_jerk
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

def cfjk_176_cf_accel_accel_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_176_cf_accel_accel_5d"""
    return (ocf.pct_change(252).diff(63)).diff(5).diff(21)

def cfjk_177_cf_accel_accel_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_177_cf_accel_accel_21d"""
    return (ocf.pct_change(252).diff(63)).diff(21).diff(21)

def cfjk_178_cf_accel_accel_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_178_cf_accel_accel_63d"""
    return (ocf.pct_change(252).diff(63)).diff(63).diff(21)

def cfjk_179_cf_accel_accel_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_179_cf_accel_accel_126d"""
    return (ocf.pct_change(252).diff(63)).diff(126).diff(21)

def cfjk_180_cf_accel_accel_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_180_cf_accel_accel_252d"""
    return (ocf.pct_change(252).diff(63)).diff(252).diff(21)

def cfjk_181_cf_jerk_accel_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_181_cf_jerk_accel_5d"""
    return (ocf.pct_change(252).diff(63).diff(21)).diff(5).diff(21)

def cfjk_182_cf_jerk_accel_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_182_cf_jerk_accel_21d"""
    return (ocf.pct_change(252).diff(63).diff(21)).diff(21).diff(21)

def cfjk_183_cf_jerk_accel_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_183_cf_jerk_accel_63d"""
    return (ocf.pct_change(252).diff(63).diff(21)).diff(63).diff(21)

def cfjk_184_cf_jerk_accel_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_184_cf_jerk_accel_126d"""
    return (ocf.pct_change(252).diff(63).diff(21)).diff(126).diff(21)

def cfjk_185_cf_jerk_accel_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_185_cf_jerk_accel_252d"""
    return (ocf.pct_change(252).diff(63).diff(21)).diff(252).diff(21)

def cfjk_186_cf_accel_z_accel_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_186_cf_accel_z_accel_5d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63), 252)).diff(5).diff(21)

def cfjk_187_cf_accel_z_accel_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_187_cf_accel_z_accel_21d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63), 252)).diff(21).diff(21)

def cfjk_188_cf_accel_z_accel_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_188_cf_accel_z_accel_63d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63), 252)).diff(63).diff(21)

def cfjk_189_cf_accel_z_accel_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_189_cf_accel_z_accel_126d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63), 252)).diff(126).diff(21)

def cfjk_190_cf_accel_z_accel_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_190_cf_accel_z_accel_252d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63), 252)).diff(252).diff(21)

def cfjk_191_cf_jerk_z_accel_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_191_cf_jerk_z_accel_5d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)).diff(5).diff(21)

def cfjk_192_cf_jerk_z_accel_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_192_cf_jerk_z_accel_21d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)).diff(21).diff(21)

def cfjk_193_cf_jerk_z_accel_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_193_cf_jerk_z_accel_63d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)).diff(63).diff(21)

def cfjk_194_cf_jerk_z_accel_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_194_cf_jerk_z_accel_126d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)).diff(126).diff(21)

def cfjk_195_cf_jerk_z_accel_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_195_cf_jerk_z_accel_252d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)).diff(252).diff(21)

def cfjk_196_cf_accel_rank_accel_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_196_cf_accel_rank_accel_5d"""
    return (_rank_pct(ocf.pct_change(252).diff(63), 252)).diff(5).diff(21)

def cfjk_197_cf_accel_rank_accel_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_197_cf_accel_rank_accel_21d"""
    return (_rank_pct(ocf.pct_change(252).diff(63), 252)).diff(21).diff(21)

def cfjk_198_cf_accel_rank_accel_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_198_cf_accel_rank_accel_63d"""
    return (_rank_pct(ocf.pct_change(252).diff(63), 252)).diff(63).diff(21)

def cfjk_199_cf_accel_rank_accel_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_199_cf_accel_rank_accel_126d"""
    return (_rank_pct(ocf.pct_change(252).diff(63), 252)).diff(126).diff(21)

def cfjk_200_cf_accel_rank_accel_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_200_cf_accel_rank_accel_252d"""
    return (_rank_pct(ocf.pct_change(252).diff(63), 252)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V60_REGISTRY_ACCEL = {
    "cfjk_176_cf_accel_accel_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_176_cf_accel_accel_5d},
    "cfjk_177_cf_accel_accel_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_177_cf_accel_accel_21d},
    "cfjk_178_cf_accel_accel_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_178_cf_accel_accel_63d},
    "cfjk_179_cf_accel_accel_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_179_cf_accel_accel_126d},
    "cfjk_180_cf_accel_accel_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_180_cf_accel_accel_252d},
    "cfjk_181_cf_jerk_accel_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_181_cf_jerk_accel_5d},
    "cfjk_182_cf_jerk_accel_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_182_cf_jerk_accel_21d},
    "cfjk_183_cf_jerk_accel_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_183_cf_jerk_accel_63d},
    "cfjk_184_cf_jerk_accel_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_184_cf_jerk_accel_126d},
    "cfjk_185_cf_jerk_accel_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_185_cf_jerk_accel_252d},
    "cfjk_186_cf_accel_z_accel_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_186_cf_accel_z_accel_5d},
    "cfjk_187_cf_accel_z_accel_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_187_cf_accel_z_accel_21d},
    "cfjk_188_cf_accel_z_accel_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_188_cf_accel_z_accel_63d},
    "cfjk_189_cf_accel_z_accel_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_189_cf_accel_z_accel_126d},
    "cfjk_190_cf_accel_z_accel_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_190_cf_accel_z_accel_252d},
    "cfjk_191_cf_jerk_z_accel_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_191_cf_jerk_z_accel_5d},
    "cfjk_192_cf_jerk_z_accel_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_192_cf_jerk_z_accel_21d},
    "cfjk_193_cf_jerk_z_accel_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_193_cf_jerk_z_accel_63d},
    "cfjk_194_cf_jerk_z_accel_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_194_cf_jerk_z_accel_126d},
    "cfjk_195_cf_jerk_z_accel_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_195_cf_jerk_z_accel_252d},
    "cfjk_196_cf_accel_rank_accel_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_196_cf_accel_rank_accel_5d},
    "cfjk_197_cf_accel_rank_accel_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_197_cf_accel_rank_accel_21d},
    "cfjk_198_cf_accel_rank_accel_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_198_cf_accel_rank_accel_63d},
    "cfjk_199_cf_accel_rank_accel_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_199_cf_accel_rank_accel_126d},
    "cfjk_200_cf_accel_rank_accel_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_200_cf_accel_rank_accel_252d},
}
