"""
59_margin_jerk — 2nd Derivatives (Velocity)
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

def marj_151_margin_accel_vel_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_151_margin_accel_vel_5d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63)).diff(5)

def marj_152_margin_accel_vel_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_152_margin_accel_vel_21d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63)).diff(21)

def marj_153_margin_accel_vel_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_153_margin_accel_vel_63d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63)).diff(63)

def marj_154_margin_accel_vel_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_154_margin_accel_vel_126d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63)).diff(126)

def marj_155_margin_accel_vel_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_155_margin_accel_vel_252d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63)).diff(252)

def marj_156_margin_jerk_vel_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_156_margin_jerk_vel_5d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63).diff(21)).diff(5)

def marj_157_margin_jerk_vel_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_157_margin_jerk_vel_21d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63).diff(21)).diff(21)

def marj_158_margin_jerk_vel_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_158_margin_jerk_vel_63d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63).diff(21)).diff(63)

def marj_159_margin_jerk_vel_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_159_margin_jerk_vel_126d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63).diff(21)).diff(126)

def marj_160_margin_jerk_vel_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_160_margin_jerk_vel_252d"""
    return (_safe_div(netinc, revenue).diff(252).diff(63).diff(21)).diff(252)

def marj_161_margin_accel_z_vel_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_161_margin_accel_z_vel_5d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(5)

def marj_162_margin_accel_z_vel_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_162_margin_accel_z_vel_21d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(21)

def marj_163_margin_accel_z_vel_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_163_margin_accel_z_vel_63d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(63)

def marj_164_margin_accel_z_vel_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_164_margin_accel_z_vel_126d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(126)

def marj_165_margin_accel_z_vel_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_165_margin_accel_z_vel_252d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(252)

def marj_166_margin_jerk_z_vel_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_166_margin_jerk_z_vel_5d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)).diff(5)

def marj_167_margin_jerk_z_vel_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_167_margin_jerk_z_vel_21d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)).diff(21)

def marj_168_margin_jerk_z_vel_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_168_margin_jerk_z_vel_63d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)).diff(63)

def marj_169_margin_jerk_z_vel_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_169_margin_jerk_z_vel_126d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)).diff(126)

def marj_170_margin_jerk_z_vel_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_170_margin_jerk_z_vel_252d"""
    return (_zscore_rolling(_safe_div(netinc, revenue).diff(252).diff(63).diff(21), 252)).diff(252)

def marj_171_margin_accel_rank_vel_5d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_171_margin_accel_rank_vel_5d"""
    return (_rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(5)

def marj_172_margin_accel_rank_vel_21d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_172_margin_accel_rank_vel_21d"""
    return (_rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(21)

def marj_173_margin_accel_rank_vel_63d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_173_margin_accel_rank_vel_63d"""
    return (_rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(63)

def marj_174_margin_accel_rank_vel_126d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_174_margin_accel_rank_vel_126d"""
    return (_rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(126)

def marj_175_margin_accel_rank_vel_252d(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """marj_175_margin_accel_rank_vel_252d"""
    return (_rank_pct(_safe_div(netinc, revenue).diff(252).diff(63), 252)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V59_REGISTRY_VEL = {
    "marj_151_margin_accel_vel_5d": {"inputs": ["netinc", "revenue"], "func": marj_151_margin_accel_vel_5d},
    "marj_152_margin_accel_vel_21d": {"inputs": ["netinc", "revenue"], "func": marj_152_margin_accel_vel_21d},
    "marj_153_margin_accel_vel_63d": {"inputs": ["netinc", "revenue"], "func": marj_153_margin_accel_vel_63d},
    "marj_154_margin_accel_vel_126d": {"inputs": ["netinc", "revenue"], "func": marj_154_margin_accel_vel_126d},
    "marj_155_margin_accel_vel_252d": {"inputs": ["netinc", "revenue"], "func": marj_155_margin_accel_vel_252d},
    "marj_156_margin_jerk_vel_5d": {"inputs": ["netinc", "revenue"], "func": marj_156_margin_jerk_vel_5d},
    "marj_157_margin_jerk_vel_21d": {"inputs": ["netinc", "revenue"], "func": marj_157_margin_jerk_vel_21d},
    "marj_158_margin_jerk_vel_63d": {"inputs": ["netinc", "revenue"], "func": marj_158_margin_jerk_vel_63d},
    "marj_159_margin_jerk_vel_126d": {"inputs": ["netinc", "revenue"], "func": marj_159_margin_jerk_vel_126d},
    "marj_160_margin_jerk_vel_252d": {"inputs": ["netinc", "revenue"], "func": marj_160_margin_jerk_vel_252d},
    "marj_161_margin_accel_z_vel_5d": {"inputs": ["netinc", "revenue"], "func": marj_161_margin_accel_z_vel_5d},
    "marj_162_margin_accel_z_vel_21d": {"inputs": ["netinc", "revenue"], "func": marj_162_margin_accel_z_vel_21d},
    "marj_163_margin_accel_z_vel_63d": {"inputs": ["netinc", "revenue"], "func": marj_163_margin_accel_z_vel_63d},
    "marj_164_margin_accel_z_vel_126d": {"inputs": ["netinc", "revenue"], "func": marj_164_margin_accel_z_vel_126d},
    "marj_165_margin_accel_z_vel_252d": {"inputs": ["netinc", "revenue"], "func": marj_165_margin_accel_z_vel_252d},
    "marj_166_margin_jerk_z_vel_5d": {"inputs": ["netinc", "revenue"], "func": marj_166_margin_jerk_z_vel_5d},
    "marj_167_margin_jerk_z_vel_21d": {"inputs": ["netinc", "revenue"], "func": marj_167_margin_jerk_z_vel_21d},
    "marj_168_margin_jerk_z_vel_63d": {"inputs": ["netinc", "revenue"], "func": marj_168_margin_jerk_z_vel_63d},
    "marj_169_margin_jerk_z_vel_126d": {"inputs": ["netinc", "revenue"], "func": marj_169_margin_jerk_z_vel_126d},
    "marj_170_margin_jerk_z_vel_252d": {"inputs": ["netinc", "revenue"], "func": marj_170_margin_jerk_z_vel_252d},
    "marj_171_margin_accel_rank_vel_5d": {"inputs": ["netinc", "revenue"], "func": marj_171_margin_accel_rank_vel_5d},
    "marj_172_margin_accel_rank_vel_21d": {"inputs": ["netinc", "revenue"], "func": marj_172_margin_accel_rank_vel_21d},
    "marj_173_margin_accel_rank_vel_63d": {"inputs": ["netinc", "revenue"], "func": marj_173_margin_accel_rank_vel_63d},
    "marj_174_margin_accel_rank_vel_126d": {"inputs": ["netinc", "revenue"], "func": marj_174_margin_accel_rank_vel_126d},
    "marj_175_margin_accel_rank_vel_252d": {"inputs": ["netinc", "revenue"], "func": marj_175_margin_accel_rank_vel_252d},
}
