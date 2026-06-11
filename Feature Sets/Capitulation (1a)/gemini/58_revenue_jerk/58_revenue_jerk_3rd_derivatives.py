"""
58_revenue_jerk — 3rd Derivatives (Acceleration)
Domain: revenue_jerk
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

def revj_176_rev_accel_accel_5d(revenue: pd.Series) -> pd.Series:
    """revj_176_rev_accel_accel_5d"""
    return (revenue.pct_change(252).diff(63)).diff(5).diff(21)

def revj_177_rev_accel_accel_21d(revenue: pd.Series) -> pd.Series:
    """revj_177_rev_accel_accel_21d"""
    return (revenue.pct_change(252).diff(63)).diff(21).diff(21)

def revj_178_rev_accel_accel_63d(revenue: pd.Series) -> pd.Series:
    """revj_178_rev_accel_accel_63d"""
    return (revenue.pct_change(252).diff(63)).diff(63).diff(21)

def revj_179_rev_accel_accel_126d(revenue: pd.Series) -> pd.Series:
    """revj_179_rev_accel_accel_126d"""
    return (revenue.pct_change(252).diff(63)).diff(126).diff(21)

def revj_180_rev_accel_accel_252d(revenue: pd.Series) -> pd.Series:
    """revj_180_rev_accel_accel_252d"""
    return (revenue.pct_change(252).diff(63)).diff(252).diff(21)

def revj_181_rev_jerk_accel_5d(revenue: pd.Series) -> pd.Series:
    """revj_181_rev_jerk_accel_5d"""
    return (revenue.pct_change(252).diff(63).diff(21)).diff(5).diff(21)

def revj_182_rev_jerk_accel_21d(revenue: pd.Series) -> pd.Series:
    """revj_182_rev_jerk_accel_21d"""
    return (revenue.pct_change(252).diff(63).diff(21)).diff(21).diff(21)

def revj_183_rev_jerk_accel_63d(revenue: pd.Series) -> pd.Series:
    """revj_183_rev_jerk_accel_63d"""
    return (revenue.pct_change(252).diff(63).diff(21)).diff(63).diff(21)

def revj_184_rev_jerk_accel_126d(revenue: pd.Series) -> pd.Series:
    """revj_184_rev_jerk_accel_126d"""
    return (revenue.pct_change(252).diff(63).diff(21)).diff(126).diff(21)

def revj_185_rev_jerk_accel_252d(revenue: pd.Series) -> pd.Series:
    """revj_185_rev_jerk_accel_252d"""
    return (revenue.pct_change(252).diff(63).diff(21)).diff(252).diff(21)

def revj_186_rev_accel_z_accel_5d(revenue: pd.Series) -> pd.Series:
    """revj_186_rev_accel_z_accel_5d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63), 252)).diff(5).diff(21)

def revj_187_rev_accel_z_accel_21d(revenue: pd.Series) -> pd.Series:
    """revj_187_rev_accel_z_accel_21d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63), 252)).diff(21).diff(21)

def revj_188_rev_accel_z_accel_63d(revenue: pd.Series) -> pd.Series:
    """revj_188_rev_accel_z_accel_63d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63), 252)).diff(63).diff(21)

def revj_189_rev_accel_z_accel_126d(revenue: pd.Series) -> pd.Series:
    """revj_189_rev_accel_z_accel_126d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63), 252)).diff(126).diff(21)

def revj_190_rev_accel_z_accel_252d(revenue: pd.Series) -> pd.Series:
    """revj_190_rev_accel_z_accel_252d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63), 252)).diff(252).diff(21)

def revj_191_rev_jerk_z_accel_5d(revenue: pd.Series) -> pd.Series:
    """revj_191_rev_jerk_z_accel_5d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)).diff(5).diff(21)

def revj_192_rev_jerk_z_accel_21d(revenue: pd.Series) -> pd.Series:
    """revj_192_rev_jerk_z_accel_21d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)).diff(21).diff(21)

def revj_193_rev_jerk_z_accel_63d(revenue: pd.Series) -> pd.Series:
    """revj_193_rev_jerk_z_accel_63d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)).diff(63).diff(21)

def revj_194_rev_jerk_z_accel_126d(revenue: pd.Series) -> pd.Series:
    """revj_194_rev_jerk_z_accel_126d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)).diff(126).diff(21)

def revj_195_rev_jerk_z_accel_252d(revenue: pd.Series) -> pd.Series:
    """revj_195_rev_jerk_z_accel_252d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)).diff(252).diff(21)

def revj_196_rev_accel_rank_accel_5d(revenue: pd.Series) -> pd.Series:
    """revj_196_rev_accel_rank_accel_5d"""
    return (_rank_pct(revenue.pct_change(252).diff(63), 252)).diff(5).diff(21)

def revj_197_rev_accel_rank_accel_21d(revenue: pd.Series) -> pd.Series:
    """revj_197_rev_accel_rank_accel_21d"""
    return (_rank_pct(revenue.pct_change(252).diff(63), 252)).diff(21).diff(21)

def revj_198_rev_accel_rank_accel_63d(revenue: pd.Series) -> pd.Series:
    """revj_198_rev_accel_rank_accel_63d"""
    return (_rank_pct(revenue.pct_change(252).diff(63), 252)).diff(63).diff(21)

def revj_199_rev_accel_rank_accel_126d(revenue: pd.Series) -> pd.Series:
    """revj_199_rev_accel_rank_accel_126d"""
    return (_rank_pct(revenue.pct_change(252).diff(63), 252)).diff(126).diff(21)

def revj_200_rev_accel_rank_accel_252d(revenue: pd.Series) -> pd.Series:
    """revj_200_rev_accel_rank_accel_252d"""
    return (_rank_pct(revenue.pct_change(252).diff(63), 252)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V58_REGISTRY_ACCEL = {
    "revj_176_rev_accel_accel_5d": {"inputs": ["revenue"], "func": revj_176_rev_accel_accel_5d},
    "revj_177_rev_accel_accel_21d": {"inputs": ["revenue"], "func": revj_177_rev_accel_accel_21d},
    "revj_178_rev_accel_accel_63d": {"inputs": ["revenue"], "func": revj_178_rev_accel_accel_63d},
    "revj_179_rev_accel_accel_126d": {"inputs": ["revenue"], "func": revj_179_rev_accel_accel_126d},
    "revj_180_rev_accel_accel_252d": {"inputs": ["revenue"], "func": revj_180_rev_accel_accel_252d},
    "revj_181_rev_jerk_accel_5d": {"inputs": ["revenue"], "func": revj_181_rev_jerk_accel_5d},
    "revj_182_rev_jerk_accel_21d": {"inputs": ["revenue"], "func": revj_182_rev_jerk_accel_21d},
    "revj_183_rev_jerk_accel_63d": {"inputs": ["revenue"], "func": revj_183_rev_jerk_accel_63d},
    "revj_184_rev_jerk_accel_126d": {"inputs": ["revenue"], "func": revj_184_rev_jerk_accel_126d},
    "revj_185_rev_jerk_accel_252d": {"inputs": ["revenue"], "func": revj_185_rev_jerk_accel_252d},
    "revj_186_rev_accel_z_accel_5d": {"inputs": ["revenue"], "func": revj_186_rev_accel_z_accel_5d},
    "revj_187_rev_accel_z_accel_21d": {"inputs": ["revenue"], "func": revj_187_rev_accel_z_accel_21d},
    "revj_188_rev_accel_z_accel_63d": {"inputs": ["revenue"], "func": revj_188_rev_accel_z_accel_63d},
    "revj_189_rev_accel_z_accel_126d": {"inputs": ["revenue"], "func": revj_189_rev_accel_z_accel_126d},
    "revj_190_rev_accel_z_accel_252d": {"inputs": ["revenue"], "func": revj_190_rev_accel_z_accel_252d},
    "revj_191_rev_jerk_z_accel_5d": {"inputs": ["revenue"], "func": revj_191_rev_jerk_z_accel_5d},
    "revj_192_rev_jerk_z_accel_21d": {"inputs": ["revenue"], "func": revj_192_rev_jerk_z_accel_21d},
    "revj_193_rev_jerk_z_accel_63d": {"inputs": ["revenue"], "func": revj_193_rev_jerk_z_accel_63d},
    "revj_194_rev_jerk_z_accel_126d": {"inputs": ["revenue"], "func": revj_194_rev_jerk_z_accel_126d},
    "revj_195_rev_jerk_z_accel_252d": {"inputs": ["revenue"], "func": revj_195_rev_jerk_z_accel_252d},
    "revj_196_rev_accel_rank_accel_5d": {"inputs": ["revenue"], "func": revj_196_rev_accel_rank_accel_5d},
    "revj_197_rev_accel_rank_accel_21d": {"inputs": ["revenue"], "func": revj_197_rev_accel_rank_accel_21d},
    "revj_198_rev_accel_rank_accel_63d": {"inputs": ["revenue"], "func": revj_198_rev_accel_rank_accel_63d},
    "revj_199_rev_accel_rank_accel_126d": {"inputs": ["revenue"], "func": revj_199_rev_accel_rank_accel_126d},
    "revj_200_rev_accel_rank_accel_252d": {"inputs": ["revenue"], "func": revj_200_rev_accel_rank_accel_252d},
}
