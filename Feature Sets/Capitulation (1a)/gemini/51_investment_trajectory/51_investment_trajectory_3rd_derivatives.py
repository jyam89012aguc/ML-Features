"""
51_investment_trajectory — 3rd Derivatives (Acceleration)
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

def invt_176_capex_abs_accel_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_176_capex_abs_accel_5d"""
    return (capex.abs()).diff(5).diff(21)

def invt_177_capex_abs_accel_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_177_capex_abs_accel_21d"""
    return (capex.abs()).diff(21).diff(21)

def invt_178_capex_abs_accel_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_178_capex_abs_accel_63d"""
    return (capex.abs()).diff(63).diff(21)

def invt_179_capex_abs_accel_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_179_capex_abs_accel_126d"""
    return (capex.abs()).diff(126).diff(21)

def invt_180_capex_abs_accel_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_180_capex_abs_accel_252d"""
    return (capex.abs()).diff(252).diff(21)

def invt_181_ncfi_abs_accel_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_181_ncfi_abs_accel_5d"""
    return (ncfi.abs()).diff(5).diff(21)

def invt_182_ncfi_abs_accel_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_182_ncfi_abs_accel_21d"""
    return (ncfi.abs()).diff(21).diff(21)

def invt_183_ncfi_abs_accel_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_183_ncfi_abs_accel_63d"""
    return (ncfi.abs()).diff(63).diff(21)

def invt_184_ncfi_abs_accel_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_184_ncfi_abs_accel_126d"""
    return (ncfi.abs()).diff(126).diff(21)

def invt_185_ncfi_abs_accel_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_185_ncfi_abs_accel_252d"""
    return (ncfi.abs()).diff(252).diff(21)

def invt_186_rnd_lvl_accel_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_186_rnd_lvl_accel_5d"""
    return (rnd.fillna(0)).diff(5).diff(21)

def invt_187_rnd_lvl_accel_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_187_rnd_lvl_accel_21d"""
    return (rnd.fillna(0)).diff(21).diff(21)

def invt_188_rnd_lvl_accel_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_188_rnd_lvl_accel_63d"""
    return (rnd.fillna(0)).diff(63).diff(21)

def invt_189_rnd_lvl_accel_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_189_rnd_lvl_accel_126d"""
    return (rnd.fillna(0)).diff(126).diff(21)

def invt_190_rnd_lvl_accel_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_190_rnd_lvl_accel_252d"""
    return (rnd.fillna(0)).diff(252).diff(21)

def invt_191_total_inv_accel_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_191_total_inv_accel_5d"""
    return (capex.abs().fillna(0) + rnd.fillna(0)).diff(5).diff(21)

def invt_192_total_inv_accel_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_192_total_inv_accel_21d"""
    return (capex.abs().fillna(0) + rnd.fillna(0)).diff(21).diff(21)

def invt_193_total_inv_accel_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_193_total_inv_accel_63d"""
    return (capex.abs().fillna(0) + rnd.fillna(0)).diff(63).diff(21)

def invt_194_total_inv_accel_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_194_total_inv_accel_126d"""
    return (capex.abs().fillna(0) + rnd.fillna(0)).diff(126).diff(21)

def invt_195_total_inv_accel_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_195_total_inv_accel_252d"""
    return (capex.abs().fillna(0) + rnd.fillna(0)).diff(252).diff(21)

def invt_196_inv_intensity_accel_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_196_inv_intensity_accel_5d"""
    return (_safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)).diff(5).diff(21)

def invt_197_inv_intensity_accel_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_197_inv_intensity_accel_21d"""
    return (_safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)).diff(21).diff(21)

def invt_198_inv_intensity_accel_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_198_inv_intensity_accel_63d"""
    return (_safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)).diff(63).diff(21)

def invt_199_inv_intensity_accel_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_199_inv_intensity_accel_126d"""
    return (_safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)).diff(126).diff(21)

def invt_200_inv_intensity_accel_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_200_inv_intensity_accel_252d"""
    return (_safe_div(capex.abs().fillna(0) + rnd.fillna(0), revenue)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V51_REGISTRY_ACCEL = {
    "invt_176_capex_abs_accel_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_176_capex_abs_accel_5d},
    "invt_177_capex_abs_accel_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_177_capex_abs_accel_21d},
    "invt_178_capex_abs_accel_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_178_capex_abs_accel_63d},
    "invt_179_capex_abs_accel_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_179_capex_abs_accel_126d},
    "invt_180_capex_abs_accel_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_180_capex_abs_accel_252d},
    "invt_181_ncfi_abs_accel_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_181_ncfi_abs_accel_5d},
    "invt_182_ncfi_abs_accel_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_182_ncfi_abs_accel_21d},
    "invt_183_ncfi_abs_accel_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_183_ncfi_abs_accel_63d},
    "invt_184_ncfi_abs_accel_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_184_ncfi_abs_accel_126d},
    "invt_185_ncfi_abs_accel_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_185_ncfi_abs_accel_252d},
    "invt_186_rnd_lvl_accel_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_186_rnd_lvl_accel_5d},
    "invt_187_rnd_lvl_accel_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_187_rnd_lvl_accel_21d},
    "invt_188_rnd_lvl_accel_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_188_rnd_lvl_accel_63d},
    "invt_189_rnd_lvl_accel_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_189_rnd_lvl_accel_126d},
    "invt_190_rnd_lvl_accel_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_190_rnd_lvl_accel_252d},
    "invt_191_total_inv_accel_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_191_total_inv_accel_5d},
    "invt_192_total_inv_accel_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_192_total_inv_accel_21d},
    "invt_193_total_inv_accel_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_193_total_inv_accel_63d},
    "invt_194_total_inv_accel_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_194_total_inv_accel_126d},
    "invt_195_total_inv_accel_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_195_total_inv_accel_252d},
    "invt_196_inv_intensity_accel_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_196_inv_intensity_accel_5d},
    "invt_197_inv_intensity_accel_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_197_inv_intensity_accel_21d},
    "invt_198_inv_intensity_accel_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_198_inv_intensity_accel_63d},
    "invt_199_inv_intensity_accel_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_199_inv_intensity_accel_126d},
    "invt_200_inv_intensity_accel_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_200_inv_intensity_accel_252d},
}
