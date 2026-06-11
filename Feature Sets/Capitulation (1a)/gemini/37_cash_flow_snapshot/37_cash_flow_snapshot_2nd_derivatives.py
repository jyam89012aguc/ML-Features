"""
37_cash_flow_snapshot — 2nd Derivatives (Velocity)
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

def cflo_151_ocf_lvl_vel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_151_ocf_lvl_vel_5d"""
    return (ocf).diff(5)

def cflo_152_ocf_lvl_vel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_152_ocf_lvl_vel_21d"""
    return (ocf).diff(21)

def cflo_153_ocf_lvl_vel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_153_ocf_lvl_vel_63d"""
    return (ocf).diff(63)

def cflo_154_ocf_lvl_vel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_154_ocf_lvl_vel_126d"""
    return (ocf).diff(126)

def cflo_155_ocf_lvl_vel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_155_ocf_lvl_vel_252d"""
    return (ocf).diff(252)

def cflo_156_fcf_lvl_vel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_156_fcf_lvl_vel_5d"""
    return (fcf).diff(5)

def cflo_157_fcf_lvl_vel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_157_fcf_lvl_vel_21d"""
    return (fcf).diff(21)

def cflo_158_fcf_lvl_vel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_158_fcf_lvl_vel_63d"""
    return (fcf).diff(63)

def cflo_159_fcf_lvl_vel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_159_fcf_lvl_vel_126d"""
    return (fcf).diff(126)

def cflo_160_fcf_lvl_vel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_160_fcf_lvl_vel_252d"""
    return (fcf).diff(252)

def cflo_161_ocf_margin_vel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_161_ocf_margin_vel_5d"""
    return (_safe_div(ocf, revenue)).diff(5)

def cflo_162_ocf_margin_vel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_162_ocf_margin_vel_21d"""
    return (_safe_div(ocf, revenue)).diff(21)

def cflo_163_ocf_margin_vel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_163_ocf_margin_vel_63d"""
    return (_safe_div(ocf, revenue)).diff(63)

def cflo_164_ocf_margin_vel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_164_ocf_margin_vel_126d"""
    return (_safe_div(ocf, revenue)).diff(126)

def cflo_165_ocf_margin_vel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_165_ocf_margin_vel_252d"""
    return (_safe_div(ocf, revenue)).diff(252)

def cflo_166_fcf_ps_vel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_166_fcf_ps_vel_5d"""
    return (_safe_div(fcf, sharesbas)).diff(5)

def cflo_167_fcf_ps_vel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_167_fcf_ps_vel_21d"""
    return (_safe_div(fcf, sharesbas)).diff(21)

def cflo_168_fcf_ps_vel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_168_fcf_ps_vel_63d"""
    return (_safe_div(fcf, sharesbas)).diff(63)

def cflo_169_fcf_ps_vel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_169_fcf_ps_vel_126d"""
    return (_safe_div(fcf, sharesbas)).diff(126)

def cflo_170_fcf_ps_vel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_170_fcf_ps_vel_252d"""
    return (_safe_div(fcf, sharesbas)).diff(252)

def cflo_171_fcf_yield_vel_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_171_fcf_yield_vel_5d"""
    return (_safe_div(fcf, marketcap)).diff(5)

def cflo_172_fcf_yield_vel_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_172_fcf_yield_vel_21d"""
    return (_safe_div(fcf, marketcap)).diff(21)

def cflo_173_fcf_yield_vel_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_173_fcf_yield_vel_63d"""
    return (_safe_div(fcf, marketcap)).diff(63)

def cflo_174_fcf_yield_vel_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_174_fcf_yield_vel_126d"""
    return (_safe_div(fcf, marketcap)).diff(126)

def cflo_175_fcf_yield_vel_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_175_fcf_yield_vel_252d"""
    return (_safe_div(fcf, marketcap)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V37_REGISTRY_VEL = {
    "cflo_151_ocf_lvl_vel_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_151_ocf_lvl_vel_5d},
    "cflo_152_ocf_lvl_vel_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_152_ocf_lvl_vel_21d},
    "cflo_153_ocf_lvl_vel_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_153_ocf_lvl_vel_63d},
    "cflo_154_ocf_lvl_vel_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_154_ocf_lvl_vel_126d},
    "cflo_155_ocf_lvl_vel_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_155_ocf_lvl_vel_252d},
    "cflo_156_fcf_lvl_vel_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_156_fcf_lvl_vel_5d},
    "cflo_157_fcf_lvl_vel_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_157_fcf_lvl_vel_21d},
    "cflo_158_fcf_lvl_vel_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_158_fcf_lvl_vel_63d},
    "cflo_159_fcf_lvl_vel_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_159_fcf_lvl_vel_126d},
    "cflo_160_fcf_lvl_vel_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_160_fcf_lvl_vel_252d},
    "cflo_161_ocf_margin_vel_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_161_ocf_margin_vel_5d},
    "cflo_162_ocf_margin_vel_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_162_ocf_margin_vel_21d},
    "cflo_163_ocf_margin_vel_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_163_ocf_margin_vel_63d},
    "cflo_164_ocf_margin_vel_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_164_ocf_margin_vel_126d},
    "cflo_165_ocf_margin_vel_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_165_ocf_margin_vel_252d},
    "cflo_166_fcf_ps_vel_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_166_fcf_ps_vel_5d},
    "cflo_167_fcf_ps_vel_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_167_fcf_ps_vel_21d},
    "cflo_168_fcf_ps_vel_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_168_fcf_ps_vel_63d},
    "cflo_169_fcf_ps_vel_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_169_fcf_ps_vel_126d},
    "cflo_170_fcf_ps_vel_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_170_fcf_ps_vel_252d},
    "cflo_171_fcf_yield_vel_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_171_fcf_yield_vel_5d},
    "cflo_172_fcf_yield_vel_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_172_fcf_yield_vel_21d},
    "cflo_173_fcf_yield_vel_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_173_fcf_yield_vel_63d},
    "cflo_174_fcf_yield_vel_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_174_fcf_yield_vel_126d},
    "cflo_175_fcf_yield_vel_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_175_fcf_yield_vel_252d},
}
