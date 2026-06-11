"""
51_investment_trajectory — 2nd Derivatives (Velocity)
Domain: investment_trajectory
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

def invt_151_capex_abs_vel_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_151_capex_abs_vel_5d"""
    return (capex.abs()).diff(5)

def invt_152_capex_abs_vel_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_152_capex_abs_vel_21d"""
    return (capex.abs()).diff(21)

def invt_153_capex_abs_vel_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_153_capex_abs_vel_63d"""
    return (capex.abs()).diff(63)

def invt_154_capex_abs_vel_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_154_capex_abs_vel_126d"""
    return (capex.abs()).diff(126)

def invt_155_capex_abs_vel_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_155_capex_abs_vel_252d"""
    return (capex.abs()).diff(252)

def invt_156_ncfi_abs_vel_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_156_ncfi_abs_vel_5d"""
    return (ncfi.abs()).diff(5)

def invt_157_ncfi_abs_vel_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_157_ncfi_abs_vel_21d"""
    return (ncfi.abs()).diff(21)

def invt_158_ncfi_abs_vel_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_158_ncfi_abs_vel_63d"""
    return (ncfi.abs()).diff(63)

def invt_159_ncfi_abs_vel_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_159_ncfi_abs_vel_126d"""
    return (ncfi.abs()).diff(126)

def invt_160_ncfi_abs_vel_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_160_ncfi_abs_vel_252d"""
    return (ncfi.abs()).diff(252)

def invt_161_rnd_lvl_vel_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_161_rnd_lvl_vel_5d"""
    return (rnd.fillna(0)).diff(5)

def invt_162_rnd_lvl_vel_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_162_rnd_lvl_vel_21d"""
    return (rnd.fillna(0)).diff(21)

def invt_163_rnd_lvl_vel_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_163_rnd_lvl_vel_63d"""
    return (rnd.fillna(0)).diff(63)

def invt_164_rnd_lvl_vel_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_164_rnd_lvl_vel_126d"""
    return (rnd.fillna(0)).diff(126)

def invt_165_rnd_lvl_vel_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_165_rnd_lvl_vel_252d"""
    return (rnd.fillna(0)).diff(252)

def invt_166_total_inv_vel_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_166_total_inv_vel_5d"""
    return (capex.abs().fillna(0) + rnd.fillna(0)).diff(5)

def invt_167_total_inv_vel_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_167_total_inv_vel_21d"""
    return (capex.abs().fillna(0) + rnd.fillna(0)).diff(21)

def invt_168_total_inv_vel_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_168_total_inv_vel_63d"""
    return (capex.abs().fillna(0) + rnd.fillna(0)).diff(63)

def invt_169_total_inv_vel_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_169_total_inv_vel_126d"""
    return (capex.abs().fillna(0) + rnd.fillna(0)).diff(126)

def invt_170_total_inv_vel_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_170_total_inv_vel_252d"""
    return (capex.abs().fillna(0) + rnd.fillna(0)).diff(252)

def invt_171_inv_intensity_vel_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_171_inv_intensity_vel_5d"""
    return (_safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)).diff(5)

def invt_172_inv_intensity_vel_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_172_inv_intensity_vel_21d"""
    return (_safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)).diff(21)

def invt_173_inv_intensity_vel_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_173_inv_intensity_vel_63d"""
    return (_safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)).diff(63)

def invt_174_inv_intensity_vel_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_174_inv_intensity_vel_126d"""
    return (_safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)).diff(126)

def invt_175_inv_intensity_vel_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_175_inv_intensity_vel_252d"""
    return (_safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V51_REGISTRY_VEL = {
    "invt_151_capex_abs_vel_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_151_capex_abs_vel_5d},
    "invt_152_capex_abs_vel_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_152_capex_abs_vel_21d},
    "invt_153_capex_abs_vel_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_153_capex_abs_vel_63d},
    "invt_154_capex_abs_vel_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_154_capex_abs_vel_126d},
    "invt_155_capex_abs_vel_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_155_capex_abs_vel_252d},
    "invt_156_ncfi_abs_vel_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_156_ncfi_abs_vel_5d},
    "invt_157_ncfi_abs_vel_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_157_ncfi_abs_vel_21d},
    "invt_158_ncfi_abs_vel_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_158_ncfi_abs_vel_63d},
    "invt_159_ncfi_abs_vel_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_159_ncfi_abs_vel_126d},
    "invt_160_ncfi_abs_vel_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_160_ncfi_abs_vel_252d},
    "invt_161_rnd_lvl_vel_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_161_rnd_lvl_vel_5d},
    "invt_162_rnd_lvl_vel_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_162_rnd_lvl_vel_21d},
    "invt_163_rnd_lvl_vel_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_163_rnd_lvl_vel_63d},
    "invt_164_rnd_lvl_vel_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_164_rnd_lvl_vel_126d},
    "invt_165_rnd_lvl_vel_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_165_rnd_lvl_vel_252d},
    "invt_166_total_inv_vel_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_166_total_inv_vel_5d},
    "invt_167_total_inv_vel_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_167_total_inv_vel_21d},
    "invt_168_total_inv_vel_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_168_total_inv_vel_63d},
    "invt_169_total_inv_vel_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_169_total_inv_vel_126d},
    "invt_170_total_inv_vel_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_170_total_inv_vel_252d},
    "invt_171_inv_intensity_vel_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_171_inv_intensity_vel_5d},
    "invt_172_inv_intensity_vel_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_172_inv_intensity_vel_21d},
    "invt_173_inv_intensity_vel_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_173_inv_intensity_vel_63d},
    "invt_174_inv_intensity_vel_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_174_inv_intensity_vel_126d},
    "invt_175_inv_intensity_vel_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_175_inv_intensity_vel_252d},
}
