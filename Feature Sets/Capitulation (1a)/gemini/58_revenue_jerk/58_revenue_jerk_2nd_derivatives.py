"""
58_revenue_jerk — 2nd Derivatives (Velocity)
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

def revj_151_rev_accel_vel_5d(revenue: pd.Series) -> pd.Series:
    """revj_151_rev_accel_vel_5d"""
    return (revenue.pct_change(252).diff(63)).diff(5)

def revj_152_rev_accel_vel_21d(revenue: pd.Series) -> pd.Series:
    """revj_152_rev_accel_vel_21d"""
    return (revenue.pct_change(252).diff(63)).diff(21)

def revj_153_rev_accel_vel_63d(revenue: pd.Series) -> pd.Series:
    """revj_153_rev_accel_vel_63d"""
    return (revenue.pct_change(252).diff(63)).diff(63)

def revj_154_rev_accel_vel_126d(revenue: pd.Series) -> pd.Series:
    """revj_154_rev_accel_vel_126d"""
    return (revenue.pct_change(252).diff(63)).diff(126)

def revj_155_rev_accel_vel_252d(revenue: pd.Series) -> pd.Series:
    """revj_155_rev_accel_vel_252d"""
    return (revenue.pct_change(252).diff(63)).diff(252)

def revj_156_rev_jerk_vel_5d(revenue: pd.Series) -> pd.Series:
    """revj_156_rev_jerk_vel_5d"""
    return (revenue.pct_change(252).diff(63).diff(21)).diff(5)

def revj_157_rev_jerk_vel_21d(revenue: pd.Series) -> pd.Series:
    """revj_157_rev_jerk_vel_21d"""
    return (revenue.pct_change(252).diff(63).diff(21)).diff(21)

def revj_158_rev_jerk_vel_63d(revenue: pd.Series) -> pd.Series:
    """revj_158_rev_jerk_vel_63d"""
    return (revenue.pct_change(252).diff(63).diff(21)).diff(63)

def revj_159_rev_jerk_vel_126d(revenue: pd.Series) -> pd.Series:
    """revj_159_rev_jerk_vel_126d"""
    return (revenue.pct_change(252).diff(63).diff(21)).diff(126)

def revj_160_rev_jerk_vel_252d(revenue: pd.Series) -> pd.Series:
    """revj_160_rev_jerk_vel_252d"""
    return (revenue.pct_change(252).diff(63).diff(21)).diff(252)

def revj_161_rev_accel_z_vel_5d(revenue: pd.Series) -> pd.Series:
    """revj_161_rev_accel_z_vel_5d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63), 252)).diff(5)

def revj_162_rev_accel_z_vel_21d(revenue: pd.Series) -> pd.Series:
    """revj_162_rev_accel_z_vel_21d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63), 252)).diff(21)

def revj_163_rev_accel_z_vel_63d(revenue: pd.Series) -> pd.Series:
    """revj_163_rev_accel_z_vel_63d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63), 252)).diff(63)

def revj_164_rev_accel_z_vel_126d(revenue: pd.Series) -> pd.Series:
    """revj_164_rev_accel_z_vel_126d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63), 252)).diff(126)

def revj_165_rev_accel_z_vel_252d(revenue: pd.Series) -> pd.Series:
    """revj_165_rev_accel_z_vel_252d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63), 252)).diff(252)

def revj_166_rev_jerk_z_vel_5d(revenue: pd.Series) -> pd.Series:
    """revj_166_rev_jerk_z_vel_5d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)).diff(5)

def revj_167_rev_jerk_z_vel_21d(revenue: pd.Series) -> pd.Series:
    """revj_167_rev_jerk_z_vel_21d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)).diff(21)

def revj_168_rev_jerk_z_vel_63d(revenue: pd.Series) -> pd.Series:
    """revj_168_rev_jerk_z_vel_63d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)).diff(63)

def revj_169_rev_jerk_z_vel_126d(revenue: pd.Series) -> pd.Series:
    """revj_169_rev_jerk_z_vel_126d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)).diff(126)

def revj_170_rev_jerk_z_vel_252d(revenue: pd.Series) -> pd.Series:
    """revj_170_rev_jerk_z_vel_252d"""
    return (_zscore_rolling(revenue.pct_change(252).diff(63).diff(21), 252)).diff(252)

def revj_171_rev_accel_rank_vel_5d(revenue: pd.Series) -> pd.Series:
    """revj_171_rev_accel_rank_vel_5d"""
    return (_rank_pct(revenue.pct_change(252).diff(63), 252)).diff(5)

def revj_172_rev_accel_rank_vel_21d(revenue: pd.Series) -> pd.Series:
    """revj_172_rev_accel_rank_vel_21d"""
    return (_rank_pct(revenue.pct_change(252).diff(63), 252)).diff(21)

def revj_173_rev_accel_rank_vel_63d(revenue: pd.Series) -> pd.Series:
    """revj_173_rev_accel_rank_vel_63d"""
    return (_rank_pct(revenue.pct_change(252).diff(63), 252)).diff(63)

def revj_174_rev_accel_rank_vel_126d(revenue: pd.Series) -> pd.Series:
    """revj_174_rev_accel_rank_vel_126d"""
    return (_rank_pct(revenue.pct_change(252).diff(63), 252)).diff(126)

def revj_175_rev_accel_rank_vel_252d(revenue: pd.Series) -> pd.Series:
    """revj_175_rev_accel_rank_vel_252d"""
    return (_rank_pct(revenue.pct_change(252).diff(63), 252)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V58_REGISTRY_VEL = {
    "revj_151_rev_accel_vel_5d": {"inputs": ["revenue"], "func": revj_151_rev_accel_vel_5d},
    "revj_152_rev_accel_vel_21d": {"inputs": ["revenue"], "func": revj_152_rev_accel_vel_21d},
    "revj_153_rev_accel_vel_63d": {"inputs": ["revenue"], "func": revj_153_rev_accel_vel_63d},
    "revj_154_rev_accel_vel_126d": {"inputs": ["revenue"], "func": revj_154_rev_accel_vel_126d},
    "revj_155_rev_accel_vel_252d": {"inputs": ["revenue"], "func": revj_155_rev_accel_vel_252d},
    "revj_156_rev_jerk_vel_5d": {"inputs": ["revenue"], "func": revj_156_rev_jerk_vel_5d},
    "revj_157_rev_jerk_vel_21d": {"inputs": ["revenue"], "func": revj_157_rev_jerk_vel_21d},
    "revj_158_rev_jerk_vel_63d": {"inputs": ["revenue"], "func": revj_158_rev_jerk_vel_63d},
    "revj_159_rev_jerk_vel_126d": {"inputs": ["revenue"], "func": revj_159_rev_jerk_vel_126d},
    "revj_160_rev_jerk_vel_252d": {"inputs": ["revenue"], "func": revj_160_rev_jerk_vel_252d},
    "revj_161_rev_accel_z_vel_5d": {"inputs": ["revenue"], "func": revj_161_rev_accel_z_vel_5d},
    "revj_162_rev_accel_z_vel_21d": {"inputs": ["revenue"], "func": revj_162_rev_accel_z_vel_21d},
    "revj_163_rev_accel_z_vel_63d": {"inputs": ["revenue"], "func": revj_163_rev_accel_z_vel_63d},
    "revj_164_rev_accel_z_vel_126d": {"inputs": ["revenue"], "func": revj_164_rev_accel_z_vel_126d},
    "revj_165_rev_accel_z_vel_252d": {"inputs": ["revenue"], "func": revj_165_rev_accel_z_vel_252d},
    "revj_166_rev_jerk_z_vel_5d": {"inputs": ["revenue"], "func": revj_166_rev_jerk_z_vel_5d},
    "revj_167_rev_jerk_z_vel_21d": {"inputs": ["revenue"], "func": revj_167_rev_jerk_z_vel_21d},
    "revj_168_rev_jerk_z_vel_63d": {"inputs": ["revenue"], "func": revj_168_rev_jerk_z_vel_63d},
    "revj_169_rev_jerk_z_vel_126d": {"inputs": ["revenue"], "func": revj_169_rev_jerk_z_vel_126d},
    "revj_170_rev_jerk_z_vel_252d": {"inputs": ["revenue"], "func": revj_170_rev_jerk_z_vel_252d},
    "revj_171_rev_accel_rank_vel_5d": {"inputs": ["revenue"], "func": revj_171_rev_accel_rank_vel_5d},
    "revj_172_rev_accel_rank_vel_21d": {"inputs": ["revenue"], "func": revj_172_rev_accel_rank_vel_21d},
    "revj_173_rev_accel_rank_vel_63d": {"inputs": ["revenue"], "func": revj_173_rev_accel_rank_vel_63d},
    "revj_174_rev_accel_rank_vel_126d": {"inputs": ["revenue"], "func": revj_174_rev_accel_rank_vel_126d},
    "revj_175_rev_accel_rank_vel_252d": {"inputs": ["revenue"], "func": revj_175_rev_accel_rank_vel_252d},
}
