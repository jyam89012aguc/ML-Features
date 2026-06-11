"""
60_cash_flow_jerk — 2nd Derivatives (Velocity)
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

def cfjk_151_cf_accel_vel_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_151_cf_accel_vel_5d"""
    return (ocf.pct_change(252).diff(63)).diff(5)

def cfjk_152_cf_accel_vel_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_152_cf_accel_vel_21d"""
    return (ocf.pct_change(252).diff(63)).diff(21)

def cfjk_153_cf_accel_vel_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_153_cf_accel_vel_63d"""
    return (ocf.pct_change(252).diff(63)).diff(63)

def cfjk_154_cf_accel_vel_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_154_cf_accel_vel_126d"""
    return (ocf.pct_change(252).diff(63)).diff(126)

def cfjk_155_cf_accel_vel_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_155_cf_accel_vel_252d"""
    return (ocf.pct_change(252).diff(63)).diff(252)

def cfjk_156_cf_jerk_vel_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_156_cf_jerk_vel_5d"""
    return (ocf.pct_change(252).diff(63).diff(21)).diff(5)

def cfjk_157_cf_jerk_vel_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_157_cf_jerk_vel_21d"""
    return (ocf.pct_change(252).diff(63).diff(21)).diff(21)

def cfjk_158_cf_jerk_vel_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_158_cf_jerk_vel_63d"""
    return (ocf.pct_change(252).diff(63).diff(21)).diff(63)

def cfjk_159_cf_jerk_vel_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_159_cf_jerk_vel_126d"""
    return (ocf.pct_change(252).diff(63).diff(21)).diff(126)

def cfjk_160_cf_jerk_vel_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_160_cf_jerk_vel_252d"""
    return (ocf.pct_change(252).diff(63).diff(21)).diff(252)

def cfjk_161_cf_accel_z_vel_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_161_cf_accel_z_vel_5d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63), 252)).diff(5)

def cfjk_162_cf_accel_z_vel_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_162_cf_accel_z_vel_21d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63), 252)).diff(21)

def cfjk_163_cf_accel_z_vel_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_163_cf_accel_z_vel_63d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63), 252)).diff(63)

def cfjk_164_cf_accel_z_vel_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_164_cf_accel_z_vel_126d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63), 252)).diff(126)

def cfjk_165_cf_accel_z_vel_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_165_cf_accel_z_vel_252d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63), 252)).diff(252)

def cfjk_166_cf_jerk_z_vel_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_166_cf_jerk_z_vel_5d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)).diff(5)

def cfjk_167_cf_jerk_z_vel_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_167_cf_jerk_z_vel_21d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)).diff(21)

def cfjk_168_cf_jerk_z_vel_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_168_cf_jerk_z_vel_63d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)).diff(63)

def cfjk_169_cf_jerk_z_vel_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_169_cf_jerk_z_vel_126d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)).diff(126)

def cfjk_170_cf_jerk_z_vel_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_170_cf_jerk_z_vel_252d"""
    return (_zscore_rolling(ocf.pct_change(252).diff(63).diff(21), 252)).diff(252)

def cfjk_171_cf_accel_rank_vel_5d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_171_cf_accel_rank_vel_5d"""
    return (_rank_pct(ocf.pct_change(252).diff(63), 252)).diff(5)

def cfjk_172_cf_accel_rank_vel_21d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_172_cf_accel_rank_vel_21d"""
    return (_rank_pct(ocf.pct_change(252).diff(63), 252)).diff(21)

def cfjk_173_cf_accel_rank_vel_63d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_173_cf_accel_rank_vel_63d"""
    return (_rank_pct(ocf.pct_change(252).diff(63), 252)).diff(63)

def cfjk_174_cf_accel_rank_vel_126d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_174_cf_accel_rank_vel_126d"""
    return (_rank_pct(ocf.pct_change(252).diff(63), 252)).diff(126)

def cfjk_175_cf_accel_rank_vel_252d(ocf: pd.Series, revenue: pd.Series) -> pd.Series:
    """cfjk_175_cf_accel_rank_vel_252d"""
    return (_rank_pct(ocf.pct_change(252).diff(63), 252)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V60_REGISTRY_VEL = {
    "cfjk_151_cf_accel_vel_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_151_cf_accel_vel_5d},
    "cfjk_152_cf_accel_vel_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_152_cf_accel_vel_21d},
    "cfjk_153_cf_accel_vel_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_153_cf_accel_vel_63d},
    "cfjk_154_cf_accel_vel_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_154_cf_accel_vel_126d},
    "cfjk_155_cf_accel_vel_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_155_cf_accel_vel_252d},
    "cfjk_156_cf_jerk_vel_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_156_cf_jerk_vel_5d},
    "cfjk_157_cf_jerk_vel_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_157_cf_jerk_vel_21d},
    "cfjk_158_cf_jerk_vel_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_158_cf_jerk_vel_63d},
    "cfjk_159_cf_jerk_vel_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_159_cf_jerk_vel_126d},
    "cfjk_160_cf_jerk_vel_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_160_cf_jerk_vel_252d},
    "cfjk_161_cf_accel_z_vel_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_161_cf_accel_z_vel_5d},
    "cfjk_162_cf_accel_z_vel_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_162_cf_accel_z_vel_21d},
    "cfjk_163_cf_accel_z_vel_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_163_cf_accel_z_vel_63d},
    "cfjk_164_cf_accel_z_vel_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_164_cf_accel_z_vel_126d},
    "cfjk_165_cf_accel_z_vel_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_165_cf_accel_z_vel_252d},
    "cfjk_166_cf_jerk_z_vel_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_166_cf_jerk_z_vel_5d},
    "cfjk_167_cf_jerk_z_vel_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_167_cf_jerk_z_vel_21d},
    "cfjk_168_cf_jerk_z_vel_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_168_cf_jerk_z_vel_63d},
    "cfjk_169_cf_jerk_z_vel_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_169_cf_jerk_z_vel_126d},
    "cfjk_170_cf_jerk_z_vel_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_170_cf_jerk_z_vel_252d},
    "cfjk_171_cf_accel_rank_vel_5d": {"inputs": ["ocf", "revenue"], "func": cfjk_171_cf_accel_rank_vel_5d},
    "cfjk_172_cf_accel_rank_vel_21d": {"inputs": ["ocf", "revenue"], "func": cfjk_172_cf_accel_rank_vel_21d},
    "cfjk_173_cf_accel_rank_vel_63d": {"inputs": ["ocf", "revenue"], "func": cfjk_173_cf_accel_rank_vel_63d},
    "cfjk_174_cf_accel_rank_vel_126d": {"inputs": ["ocf", "revenue"], "func": cfjk_174_cf_accel_rank_vel_126d},
    "cfjk_175_cf_accel_rank_vel_252d": {"inputs": ["ocf", "revenue"], "func": cfjk_175_cf_accel_rank_vel_252d},
}
