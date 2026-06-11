"""
55_cash_flow_acceleration — 3rd Derivatives (Acceleration)
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

def cfa_176_ocf_growth_accel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_176_ocf_growth_accel_5d"""
    return (ocf.pct_change(252)).diff(5).diff(21)

def cfa_177_ocf_growth_accel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_177_ocf_growth_accel_21d"""
    return (ocf.pct_change(252)).diff(21).diff(21)

def cfa_178_ocf_growth_accel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_178_ocf_growth_accel_63d"""
    return (ocf.pct_change(252)).diff(63).diff(21)

def cfa_179_ocf_growth_accel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_179_ocf_growth_accel_126d"""
    return (ocf.pct_change(252)).diff(126).diff(21)

def cfa_180_ocf_growth_accel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_180_ocf_growth_accel_252d"""
    return (ocf.pct_change(252)).diff(252).diff(21)

def cfa_181_fcf_growth_accel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_181_fcf_growth_accel_5d"""
    return (fcf.pct_change(252)).diff(5).diff(21)

def cfa_182_fcf_growth_accel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_182_fcf_growth_accel_21d"""
    return (fcf.pct_change(252)).diff(21).diff(21)

def cfa_183_fcf_growth_accel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_183_fcf_growth_accel_63d"""
    return (fcf.pct_change(252)).diff(63).diff(21)

def cfa_184_fcf_growth_accel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_184_fcf_growth_accel_126d"""
    return (fcf.pct_change(252)).diff(126).diff(21)

def cfa_185_fcf_growth_accel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_185_fcf_growth_accel_252d"""
    return (fcf.pct_change(252)).diff(252).diff(21)

def cfa_186_ocf_margin_accel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_186_ocf_margin_accel_5d"""
    return (_safe_div(ocf, revenue)).diff(5).diff(21)

def cfa_187_ocf_margin_accel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_187_ocf_margin_accel_21d"""
    return (_safe_div(ocf, revenue)).diff(21).diff(21)

def cfa_188_ocf_margin_accel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_188_ocf_margin_accel_63d"""
    return (_safe_div(ocf, revenue)).diff(63).diff(21)

def cfa_189_ocf_margin_accel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_189_ocf_margin_accel_126d"""
    return (_safe_div(ocf, revenue)).diff(126).diff(21)

def cfa_190_ocf_margin_accel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_190_ocf_margin_accel_252d"""
    return (_safe_div(ocf, revenue)).diff(252).diff(21)

def cfa_191_fcf_margin_accel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_191_fcf_margin_accel_5d"""
    return (_safe_div(fcf, revenue)).diff(5).diff(21)

def cfa_192_fcf_margin_accel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_192_fcf_margin_accel_21d"""
    return (_safe_div(fcf, revenue)).diff(21).diff(21)

def cfa_193_fcf_margin_accel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_193_fcf_margin_accel_63d"""
    return (_safe_div(fcf, revenue)).diff(63).diff(21)

def cfa_194_fcf_margin_accel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_194_fcf_margin_accel_126d"""
    return (_safe_div(fcf, revenue)).diff(126).diff(21)

def cfa_195_fcf_margin_accel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_195_fcf_margin_accel_252d"""
    return (_safe_div(fcf, revenue)).diff(252).diff(21)

def cfa_196_cash_conversion_accel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_196_cash_conversion_accel_5d"""
    return (_safe_div(ocf, netinc)).diff(5).diff(21)

def cfa_197_cash_conversion_accel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_197_cash_conversion_accel_21d"""
    return (_safe_div(ocf, netinc)).diff(21).diff(21)

def cfa_198_cash_conversion_accel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_198_cash_conversion_accel_63d"""
    return (_safe_div(ocf, netinc)).diff(63).diff(21)

def cfa_199_cash_conversion_accel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_199_cash_conversion_accel_126d"""
    return (_safe_div(ocf, netinc)).diff(126).diff(21)

def cfa_200_cash_conversion_accel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cfa_200_cash_conversion_accel_252d"""
    return (_safe_div(ocf, netinc)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V55_REGISTRY_ACCEL = {
    "cfa_176_ocf_growth_accel_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_176_ocf_growth_accel_5d},
    "cfa_177_ocf_growth_accel_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_177_ocf_growth_accel_21d},
    "cfa_178_ocf_growth_accel_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_178_ocf_growth_accel_63d},
    "cfa_179_ocf_growth_accel_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_179_ocf_growth_accel_126d},
    "cfa_180_ocf_growth_accel_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_180_ocf_growth_accel_252d},
    "cfa_181_fcf_growth_accel_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_181_fcf_growth_accel_5d},
    "cfa_182_fcf_growth_accel_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_182_fcf_growth_accel_21d},
    "cfa_183_fcf_growth_accel_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_183_fcf_growth_accel_63d},
    "cfa_184_fcf_growth_accel_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_184_fcf_growth_accel_126d},
    "cfa_185_fcf_growth_accel_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_185_fcf_growth_accel_252d},
    "cfa_186_ocf_margin_accel_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_186_ocf_margin_accel_5d},
    "cfa_187_ocf_margin_accel_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_187_ocf_margin_accel_21d},
    "cfa_188_ocf_margin_accel_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_188_ocf_margin_accel_63d},
    "cfa_189_ocf_margin_accel_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_189_ocf_margin_accel_126d},
    "cfa_190_ocf_margin_accel_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_190_ocf_margin_accel_252d},
    "cfa_191_fcf_margin_accel_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_191_fcf_margin_accel_5d},
    "cfa_192_fcf_margin_accel_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_192_fcf_margin_accel_21d},
    "cfa_193_fcf_margin_accel_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_193_fcf_margin_accel_63d},
    "cfa_194_fcf_margin_accel_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_194_fcf_margin_accel_126d},
    "cfa_195_fcf_margin_accel_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_195_fcf_margin_accel_252d},
    "cfa_196_cash_conversion_accel_5d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_196_cash_conversion_accel_5d},
    "cfa_197_cash_conversion_accel_21d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_197_cash_conversion_accel_21d},
    "cfa_198_cash_conversion_accel_63d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_198_cash_conversion_accel_63d},
    "cfa_199_cash_conversion_accel_126d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_199_cash_conversion_accel_126d},
    "cfa_200_cash_conversion_accel_252d": {"inputs": ["ocf", "fcf", "revenue", "netinc"], "func": cfa_200_cash_conversion_accel_252d},
}
