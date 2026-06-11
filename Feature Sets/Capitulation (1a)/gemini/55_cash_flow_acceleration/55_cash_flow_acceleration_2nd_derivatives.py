"""
55_cash_flow_acceleration — 2nd Derivatives (Velocity)
Domain: cash_flow_acceleration
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

def cfa_151_ocf_growth_vel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_151_ocf_growth_vel_5d"""
    return (ocf.pct_change(252)).diff(5)

def cfa_152_ocf_growth_vel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_152_ocf_growth_vel_21d"""
    return (ocf.pct_change(252)).diff(21)

def cfa_153_ocf_growth_vel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_153_ocf_growth_vel_63d"""
    return (ocf.pct_change(252)).diff(63)

def cfa_154_ocf_growth_vel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_154_ocf_growth_vel_126d"""
    return (ocf.pct_change(252)).diff(126)

def cfa_155_ocf_growth_vel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_155_ocf_growth_vel_252d"""
    return (ocf.pct_change(252)).diff(252)

def cfa_156_fcf_growth_vel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_156_fcf_growth_vel_5d"""
    return (fcf.pct_change(252)).diff(5)

def cfa_157_fcf_growth_vel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_157_fcf_growth_vel_21d"""
    return (fcf.pct_change(252)).diff(21)

def cfa_158_fcf_growth_vel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_158_fcf_growth_vel_63d"""
    return (fcf.pct_change(252)).diff(63)

def cfa_159_fcf_growth_vel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_159_fcf_growth_vel_126d"""
    return (fcf.pct_change(252)).diff(126)

def cfa_160_fcf_growth_vel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_160_fcf_growth_vel_252d"""
    return (fcf.pct_change(252)).diff(252)

def cfa_161_ocf_margin_vel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_161_ocf_margin_vel_5d"""
    return (_safe_div(ocf, revenue)).diff(5)

def cfa_162_ocf_margin_vel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_162_ocf_margin_vel_21d"""
    return (_safe_div(ocf, revenue)).diff(21)

def cfa_163_ocf_margin_vel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_163_ocf_margin_vel_63d"""
    return (_safe_div(ocf, revenue)).diff(63)

def cfa_164_ocf_margin_vel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_164_ocf_margin_vel_126d"""
    return (_safe_div(ocf, revenue)).diff(126)

def cfa_165_ocf_margin_vel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_165_ocf_margin_vel_252d"""
    return (_safe_div(ocf, revenue)).diff(252)

def cfa_166_fcf_margin_vel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_166_fcf_margin_vel_5d"""
    return (_safe_div(fcf, revenue)).diff(5)

def cfa_167_fcf_margin_vel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_167_fcf_margin_vel_21d"""
    return (_safe_div(fcf, revenue)).diff(21)

def cfa_168_fcf_margin_vel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_168_fcf_margin_vel_63d"""
    return (_safe_div(fcf, revenue)).diff(63)

def cfa_169_fcf_margin_vel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_169_fcf_margin_vel_126d"""
    return (_safe_div(fcf, revenue)).diff(126)

def cfa_170_fcf_margin_vel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_170_fcf_margin_vel_252d"""
    return (_safe_div(fcf, revenue)).diff(252)

def cfa_171_cash_conversion_vel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_171_cash_conversion_vel_5d"""
    return (_safe_div(ocf, netinc)).diff(5)

def cfa_172_cash_conversion_vel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_172_cash_conversion_vel_21d"""
    return (_safe_div(ocf, netinc)).diff(21)

def cfa_173_cash_conversion_vel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_173_cash_conversion_vel_63d"""
    return (_safe_div(ocf, netinc)).diff(63)

def cfa_174_cash_conversion_vel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_174_cash_conversion_vel_126d"""
    return (_safe_div(ocf, netinc)).diff(126)

def cfa_175_cash_conversion_vel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_175_cash_conversion_vel_252d"""
    return (_safe_div(ocf, netinc)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V55_REGISTRY_VEL = {
    "cfa_151_ocf_growth_vel_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_151_ocf_growth_vel_5d},
    "cfa_152_ocf_growth_vel_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_152_ocf_growth_vel_21d},
    "cfa_153_ocf_growth_vel_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_153_ocf_growth_vel_63d},
    "cfa_154_ocf_growth_vel_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_154_ocf_growth_vel_126d},
    "cfa_155_ocf_growth_vel_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_155_ocf_growth_vel_252d},
    "cfa_156_fcf_growth_vel_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_156_fcf_growth_vel_5d},
    "cfa_157_fcf_growth_vel_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_157_fcf_growth_vel_21d},
    "cfa_158_fcf_growth_vel_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_158_fcf_growth_vel_63d},
    "cfa_159_fcf_growth_vel_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_159_fcf_growth_vel_126d},
    "cfa_160_fcf_growth_vel_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_160_fcf_growth_vel_252d},
    "cfa_161_ocf_margin_vel_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_161_ocf_margin_vel_5d},
    "cfa_162_ocf_margin_vel_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_162_ocf_margin_vel_21d},
    "cfa_163_ocf_margin_vel_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_163_ocf_margin_vel_63d},
    "cfa_164_ocf_margin_vel_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_164_ocf_margin_vel_126d},
    "cfa_165_ocf_margin_vel_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_165_ocf_margin_vel_252d},
    "cfa_166_fcf_margin_vel_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_166_fcf_margin_vel_5d},
    "cfa_167_fcf_margin_vel_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_167_fcf_margin_vel_21d},
    "cfa_168_fcf_margin_vel_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_168_fcf_margin_vel_63d},
    "cfa_169_fcf_margin_vel_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_169_fcf_margin_vel_126d},
    "cfa_170_fcf_margin_vel_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_170_fcf_margin_vel_252d},
    "cfa_171_cash_conversion_vel_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_171_cash_conversion_vel_5d},
    "cfa_172_cash_conversion_vel_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_172_cash_conversion_vel_21d},
    "cfa_173_cash_conversion_vel_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_173_cash_conversion_vel_63d},
    "cfa_174_cash_conversion_vel_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_174_cash_conversion_vel_126d},
    "cfa_175_cash_conversion_vel_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_175_cash_conversion_vel_252d},
}
