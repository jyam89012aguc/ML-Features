"""
40_leverage_and_solvency — 2nd Derivatives (Velocity)
Domain: leverage_and_solvency
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

def solv_151_debt_lvl_vel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_151_debt_lvl_vel_5d"""
    return (debt).diff(5)

def solv_152_debt_lvl_vel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_152_debt_lvl_vel_21d"""
    return (debt).diff(21)

def solv_153_debt_lvl_vel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_153_debt_lvl_vel_63d"""
    return (debt).diff(63)

def solv_154_debt_lvl_vel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_154_debt_lvl_vel_126d"""
    return (debt).diff(126)

def solv_155_debt_lvl_vel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_155_debt_lvl_vel_252d"""
    return (debt).diff(252)

def solv_156_debt_assets_vel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_156_debt_assets_vel_5d"""
    return (_safe_div(debt, assets)).diff(5)

def solv_157_debt_assets_vel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_157_debt_assets_vel_21d"""
    return (_safe_div(debt, assets)).diff(21)

def solv_158_debt_assets_vel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_158_debt_assets_vel_63d"""
    return (_safe_div(debt, assets)).diff(63)

def solv_159_debt_assets_vel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_159_debt_assets_vel_126d"""
    return (_safe_div(debt, assets)).diff(126)

def solv_160_debt_assets_vel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_160_debt_assets_vel_252d"""
    return (_safe_div(debt, assets)).diff(252)

def solv_161_int_cov_vel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_161_int_cov_vel_5d"""
    return (_safe_div(opinc, debt)).diff(5)

def solv_162_int_cov_vel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_162_int_cov_vel_21d"""
    return (_safe_div(opinc, debt)).diff(21)

def solv_163_int_cov_vel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_163_int_cov_vel_63d"""
    return (_safe_div(opinc, debt)).diff(63)

def solv_164_int_cov_vel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_164_int_cov_vel_126d"""
    return (_safe_div(opinc, debt)).diff(126)

def solv_165_int_cov_vel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_165_int_cov_vel_252d"""
    return (_safe_div(opinc, debt)).diff(252)

def solv_166_debt_eq_vel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_166_debt_eq_vel_5d"""
    return (_safe_div(debt, equity)).diff(5)

def solv_167_debt_eq_vel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_167_debt_eq_vel_21d"""
    return (_safe_div(debt, equity)).diff(21)

def solv_168_debt_eq_vel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_168_debt_eq_vel_63d"""
    return (_safe_div(debt, equity)).diff(63)

def solv_169_debt_eq_vel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_169_debt_eq_vel_126d"""
    return (_safe_div(debt, equity)).diff(126)

def solv_170_debt_eq_vel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_170_debt_eq_vel_252d"""
    return (_safe_div(debt, equity)).diff(252)

def solv_171_altman_wc_ta_vel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_171_altman_wc_ta_vel_5d"""
    return (_safe_div(assets - liabs, assets)).diff(5)

def solv_172_altman_wc_ta_vel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_172_altman_wc_ta_vel_21d"""
    return (_safe_div(assets - liabs, assets)).diff(21)

def solv_173_altman_wc_ta_vel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_173_altman_wc_ta_vel_63d"""
    return (_safe_div(assets - liabs, assets)).diff(63)

def solv_174_altman_wc_ta_vel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_174_altman_wc_ta_vel_126d"""
    return (_safe_div(assets - liabs, assets)).diff(126)

def solv_175_altman_wc_ta_vel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_175_altman_wc_ta_vel_252d"""
    return (_safe_div(assets - liabs, assets)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V40_REGISTRY_VEL = {
    "solv_151_debt_lvl_vel_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_151_debt_lvl_vel_5d},
    "solv_152_debt_lvl_vel_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_152_debt_lvl_vel_21d},
    "solv_153_debt_lvl_vel_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_153_debt_lvl_vel_63d},
    "solv_154_debt_lvl_vel_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_154_debt_lvl_vel_126d},
    "solv_155_debt_lvl_vel_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_155_debt_lvl_vel_252d},
    "solv_156_debt_assets_vel_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_156_debt_assets_vel_5d},
    "solv_157_debt_assets_vel_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_157_debt_assets_vel_21d},
    "solv_158_debt_assets_vel_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_158_debt_assets_vel_63d},
    "solv_159_debt_assets_vel_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_159_debt_assets_vel_126d},
    "solv_160_debt_assets_vel_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_160_debt_assets_vel_252d},
    "solv_161_int_cov_vel_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_161_int_cov_vel_5d},
    "solv_162_int_cov_vel_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_162_int_cov_vel_21d},
    "solv_163_int_cov_vel_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_163_int_cov_vel_63d},
    "solv_164_int_cov_vel_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_164_int_cov_vel_126d},
    "solv_165_int_cov_vel_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_165_int_cov_vel_252d},
    "solv_166_debt_eq_vel_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_166_debt_eq_vel_5d},
    "solv_167_debt_eq_vel_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_167_debt_eq_vel_21d},
    "solv_168_debt_eq_vel_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_168_debt_eq_vel_63d},
    "solv_169_debt_eq_vel_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_169_debt_eq_vel_126d},
    "solv_170_debt_eq_vel_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_170_debt_eq_vel_252d},
    "solv_171_altman_wc_ta_vel_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_171_altman_wc_ta_vel_5d},
    "solv_172_altman_wc_ta_vel_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_172_altman_wc_ta_vel_21d},
    "solv_173_altman_wc_ta_vel_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_173_altman_wc_ta_vel_63d},
    "solv_174_altman_wc_ta_vel_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_174_altman_wc_ta_vel_126d},
    "solv_175_altman_wc_ta_vel_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_175_altman_wc_ta_vel_252d},
}
