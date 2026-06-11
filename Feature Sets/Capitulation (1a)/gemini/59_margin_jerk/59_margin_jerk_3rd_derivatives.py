"""
59_margin_jerk — 3rd Derivatives (Acceleration)
Domain: margin_jerk
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

def marj_176_margin_accel_accel_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_176_margin_accel_accel_5d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63)).diff(5).diff(21)

def marj_177_margin_accel_accel_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_177_margin_accel_accel_21d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63)).diff(21).diff(21)

def marj_178_margin_accel_accel_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_178_margin_accel_accel_63d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63)).diff(63).diff(21)

def marj_179_margin_accel_accel_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_179_margin_accel_accel_126d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63)).diff(126).diff(21)

def marj_180_margin_accel_accel_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_180_margin_accel_accel_252d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63)).diff(252).diff(21)

def marj_181_margin_jerk_accel_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_181_margin_jerk_accel_5d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63).diff(21)).diff(5).diff(21)

def marj_182_margin_jerk_accel_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_182_margin_jerk_accel_21d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63).diff(21)).diff(21).diff(21)

def marj_183_margin_jerk_accel_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_183_margin_jerk_accel_63d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63).diff(21)).diff(63).diff(21)

def marj_184_margin_jerk_accel_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_184_margin_jerk_accel_126d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63).diff(21)).diff(126).diff(21)

def marj_185_margin_jerk_accel_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_185_margin_jerk_accel_252d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63).diff(21)).diff(252).diff(21)

def marj_186_margin_accel_z_accel_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_186_margin_accel_z_accel_5d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(5).diff(21)

def marj_187_margin_accel_z_accel_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_187_margin_accel_z_accel_21d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(21).diff(21)

def marj_188_margin_accel_z_accel_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_188_margin_accel_z_accel_63d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(63).diff(21)

def marj_189_margin_accel_z_accel_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_189_margin_accel_z_accel_126d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(126).diff(21)

def marj_190_margin_accel_z_accel_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_190_margin_accel_z_accel_252d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(252).diff(21)

def marj_191_margin_jerk_z_accel_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_191_margin_jerk_z_accel_5d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)).diff(5).diff(21)

def marj_192_margin_jerk_z_accel_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_192_margin_jerk_z_accel_21d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)).diff(21).diff(21)

def marj_193_margin_jerk_z_accel_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_193_margin_jerk_z_accel_63d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)).diff(63).diff(21)

def marj_194_margin_jerk_z_accel_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_194_margin_jerk_z_accel_126d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)).diff(126).diff(21)

def marj_195_margin_jerk_z_accel_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_195_margin_jerk_z_accel_252d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)).diff(252).diff(21)

def marj_196_margin_accel_rank_accel_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_196_margin_accel_rank_accel_5d"""
    return (_rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(5).diff(21)

def marj_197_margin_accel_rank_accel_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_197_margin_accel_rank_accel_21d"""
    return (_rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(21).diff(21)

def marj_198_margin_accel_rank_accel_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_198_margin_accel_rank_accel_63d"""
    return (_rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(63).diff(21)

def marj_199_margin_accel_rank_accel_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_199_margin_accel_rank_accel_126d"""
    return (_rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(126).diff(21)

def marj_200_margin_accel_rank_accel_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_200_margin_accel_rank_accel_252d"""
    return (_rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V59_REGISTRY_ACCEL = {
    "marj_176_margin_accel_accel_5d": {"inputs": ["netinc", "revenue"], "func": marj_176_margin_accel_accel_5d},
    "marj_177_margin_accel_accel_21d": {"inputs": ["netinc", "revenue"], "func": marj_177_margin_accel_accel_21d},
    "marj_178_margin_accel_accel_63d": {"inputs": ["netinc", "revenue"], "func": marj_178_margin_accel_accel_63d},
    "marj_179_margin_accel_accel_126d": {"inputs": ["netinc", "revenue"], "func": marj_179_margin_accel_accel_126d},
    "marj_180_margin_accel_accel_252d": {"inputs": ["netinc", "revenue"], "func": marj_180_margin_accel_accel_252d},
    "marj_181_margin_jerk_accel_5d": {"inputs": ["netinc", "revenue"], "func": marj_181_margin_jerk_accel_5d},
    "marj_182_margin_jerk_accel_21d": {"inputs": ["netinc", "revenue"], "func": marj_182_margin_jerk_accel_21d},
    "marj_183_margin_jerk_accel_63d": {"inputs": ["netinc", "revenue"], "func": marj_183_margin_jerk_accel_63d},
    "marj_184_margin_jerk_accel_126d": {"inputs": ["netinc", "revenue"], "func": marj_184_margin_jerk_accel_126d},
    "marj_185_margin_jerk_accel_252d": {"inputs": ["netinc", "revenue"], "func": marj_185_margin_jerk_accel_252d},
    "marj_186_margin_accel_z_accel_5d": {"inputs": ["netinc", "revenue"], "func": marj_186_margin_accel_z_accel_5d},
    "marj_187_margin_accel_z_accel_21d": {"inputs": ["netinc", "revenue"], "func": marj_187_margin_accel_z_accel_21d},
    "marj_188_margin_accel_z_accel_63d": {"inputs": ["netinc", "revenue"], "func": marj_188_margin_accel_z_accel_63d},
    "marj_189_margin_accel_z_accel_126d": {"inputs": ["netinc", "revenue"], "func": marj_189_margin_accel_z_accel_126d},
    "marj_190_margin_accel_z_accel_252d": {"inputs": ["netinc", "revenue"], "func": marj_190_margin_accel_z_accel_252d},
    "marj_191_margin_jerk_z_accel_5d": {"inputs": ["netinc", "revenue"], "func": marj_191_margin_jerk_z_accel_5d},
    "marj_192_margin_jerk_z_accel_21d": {"inputs": ["netinc", "revenue"], "func": marj_192_margin_jerk_z_accel_21d},
    "marj_193_margin_jerk_z_accel_63d": {"inputs": ["netinc", "revenue"], "func": marj_193_margin_jerk_z_accel_63d},
    "marj_194_margin_jerk_z_accel_126d": {"inputs": ["netinc", "revenue"], "func": marj_194_margin_jerk_z_accel_126d},
    "marj_195_margin_jerk_z_accel_252d": {"inputs": ["netinc", "revenue"], "func": marj_195_margin_jerk_z_accel_252d},
    "marj_196_margin_accel_rank_accel_5d": {"inputs": ["netinc", "revenue"], "func": marj_196_margin_accel_rank_accel_5d},
    "marj_197_margin_accel_rank_accel_21d": {"inputs": ["netinc", "revenue"], "func": marj_197_margin_accel_rank_accel_21d},
    "marj_198_margin_accel_rank_accel_63d": {"inputs": ["netinc", "revenue"], "func": marj_198_margin_accel_rank_accel_63d},
    "marj_199_margin_accel_rank_accel_126d": {"inputs": ["netinc", "revenue"], "func": marj_199_margin_accel_rank_accel_126d},
    "marj_200_margin_accel_rank_accel_252d": {"inputs": ["netinc", "revenue"], "func": marj_200_margin_accel_rank_accel_252d},
}
