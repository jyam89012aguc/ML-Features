"""
37_cash_flow_snapshot — 3rd Derivatives (Acceleration)
Domain: cash_flow_snapshot
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

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

# ── Feature functions ────────────────────────────────────────────────────────

def cflo_176_ocf_lvl_accel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_176_ocf_lvl_accel_5d"""
    return (ocf).diff(5).diff(21)

def cflo_177_ocf_lvl_accel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_177_ocf_lvl_accel_21d"""
    return (ocf).diff(21).diff(21)

def cflo_178_ocf_lvl_accel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_178_ocf_lvl_accel_63d"""
    return (ocf).diff(63).diff(21)

def cflo_179_ocf_lvl_accel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_179_ocf_lvl_accel_126d"""
    return (ocf).diff(126).diff(21)

def cflo_180_ocf_lvl_accel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_180_ocf_lvl_accel_252d"""
    return (ocf).diff(252).diff(21)

def cflo_181_fcf_lvl_accel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_181_fcf_lvl_accel_5d"""
    return (fcf).diff(5).diff(21)

def cflo_182_fcf_lvl_accel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_182_fcf_lvl_accel_21d"""
    return (fcf).diff(21).diff(21)

def cflo_183_fcf_lvl_accel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_183_fcf_lvl_accel_63d"""
    return (fcf).diff(63).diff(21)

def cflo_184_fcf_lvl_accel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_184_fcf_lvl_accel_126d"""
    return (fcf).diff(126).diff(21)

def cflo_185_fcf_lvl_accel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_185_fcf_lvl_accel_252d"""
    return (fcf).diff(252).diff(21)

def cflo_186_ocf_margin_accel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_186_ocf_margin_accel_5d"""
    return (_safe_div(ocf, revenue)).diff(5).diff(21)

def cflo_187_ocf_margin_accel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_187_ocf_margin_accel_21d"""
    return (_safe_div(ocf, revenue)).diff(21).diff(21)

def cflo_188_ocf_margin_accel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_188_ocf_margin_accel_63d"""
    return (_safe_div(ocf, revenue)).diff(63).diff(21)

def cflo_189_ocf_margin_accel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_189_ocf_margin_accel_126d"""
    return (_safe_div(ocf, revenue)).diff(126).diff(21)

def cflo_190_ocf_margin_accel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_190_ocf_margin_accel_252d"""
    return (_safe_div(ocf, revenue)).diff(252).diff(21)

def cflo_191_fcf_ps_accel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_191_fcf_ps_accel_5d"""
    return (_safe_div(fcf, sharesbas)).diff(5).diff(21)

def cflo_192_fcf_ps_accel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_192_fcf_ps_accel_21d"""
    return (_safe_div(fcf, sharesbas)).diff(21).diff(21)

def cflo_193_fcf_ps_accel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_193_fcf_ps_accel_63d"""
    return (_safe_div(fcf, sharesbas)).diff(63).diff(21)

def cflo_194_fcf_ps_accel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_194_fcf_ps_accel_126d"""
    return (_safe_div(fcf, sharesbas)).diff(126).diff(21)

def cflo_195_fcf_ps_accel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_195_fcf_ps_accel_252d"""
    return (_safe_div(fcf, sharesbas)).diff(252).diff(21)

def cflo_196_fcf_yield_accel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_196_fcf_yield_accel_5d"""
    return (_safe_div(fcf, marketcap)).diff(5).diff(21)

def cflo_197_fcf_yield_accel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_197_fcf_yield_accel_21d"""
    return (_safe_div(fcf, marketcap)).diff(21).diff(21)

def cflo_198_fcf_yield_accel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_198_fcf_yield_accel_63d"""
    return (_safe_div(fcf, marketcap)).diff(63).diff(21)

def cflo_199_fcf_yield_accel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_199_fcf_yield_accel_126d"""
    return (_safe_div(fcf, marketcap)).diff(126).diff(21)

def cflo_200_fcf_yield_accel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_200_fcf_yield_accel_252d"""
    return (_safe_div(fcf, marketcap)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V37_REGISTRY_ACCEL = {
    "cflo_176_ocf_lvl_accel_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_176_ocf_lvl_accel_5d},
    "cflo_177_ocf_lvl_accel_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_177_ocf_lvl_accel_21d},
    "cflo_178_ocf_lvl_accel_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_178_ocf_lvl_accel_63d},
    "cflo_179_ocf_lvl_accel_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_179_ocf_lvl_accel_126d},
    "cflo_180_ocf_lvl_accel_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_180_ocf_lvl_accel_252d},
    "cflo_181_fcf_lvl_accel_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_181_fcf_lvl_accel_5d},
    "cflo_182_fcf_lvl_accel_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_182_fcf_lvl_accel_21d},
    "cflo_183_fcf_lvl_accel_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_183_fcf_lvl_accel_63d},
    "cflo_184_fcf_lvl_accel_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_184_fcf_lvl_accel_126d},
    "cflo_185_fcf_lvl_accel_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_185_fcf_lvl_accel_252d},
    "cflo_186_ocf_margin_accel_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_186_ocf_margin_accel_5d},
    "cflo_187_ocf_margin_accel_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_187_ocf_margin_accel_21d},
    "cflo_188_ocf_margin_accel_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_188_ocf_margin_accel_63d},
    "cflo_189_ocf_margin_accel_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_189_ocf_margin_accel_126d},
    "cflo_190_ocf_margin_accel_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_190_ocf_margin_accel_252d},
    "cflo_191_fcf_ps_accel_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_191_fcf_ps_accel_5d},
    "cflo_192_fcf_ps_accel_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_192_fcf_ps_accel_21d},
    "cflo_193_fcf_ps_accel_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_193_fcf_ps_accel_63d},
    "cflo_194_fcf_ps_accel_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_194_fcf_ps_accel_126d},
    "cflo_195_fcf_ps_accel_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_195_fcf_ps_accel_252d},
    "cflo_196_fcf_yield_accel_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_196_fcf_yield_accel_5d},
    "cflo_197_fcf_yield_accel_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_197_fcf_yield_accel_21d},
    "cflo_198_fcf_yield_accel_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_198_fcf_yield_accel_63d},
    "cflo_199_fcf_yield_accel_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_199_fcf_yield_accel_126d},
    "cflo_200_fcf_yield_accel_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_200_fcf_yield_accel_252d},
}
