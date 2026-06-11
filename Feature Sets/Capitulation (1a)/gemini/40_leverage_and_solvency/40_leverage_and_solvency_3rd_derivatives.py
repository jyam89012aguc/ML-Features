"""
40_leverage_and_solvency — 3rd Derivatives (Acceleration)
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

def solv_176_debt_lvl_accel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_176_debt_lvl_accel_5d"""
    return (debt).diff(5).diff(21)

def solv_177_debt_lvl_accel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_177_debt_lvl_accel_21d"""
    return (debt).diff(21).diff(21)

def solv_178_debt_lvl_accel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_178_debt_lvl_accel_63d"""
    return (debt).diff(63).diff(21)

def solv_179_debt_lvl_accel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_179_debt_lvl_accel_126d"""
    return (debt).diff(126).diff(21)

def solv_180_debt_lvl_accel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_180_debt_lvl_accel_252d"""
    return (debt).diff(252).diff(21)

def solv_181_debt_assets_accel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_181_debt_assets_accel_5d"""
    return (_safe_div(debt, assets)).diff(5).diff(21)

def solv_182_debt_assets_accel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_182_debt_assets_accel_21d"""
    return (_safe_div(debt, assets)).diff(21).diff(21)

def solv_183_debt_assets_accel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_183_debt_assets_accel_63d"""
    return (_safe_div(debt, assets)).diff(63).diff(21)

def solv_184_debt_assets_accel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_184_debt_assets_accel_126d"""
    return (_safe_div(debt, assets)).diff(126).diff(21)

def solv_185_debt_assets_accel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_185_debt_assets_accel_252d"""
    return (_safe_div(debt, assets)).diff(252).diff(21)

def solv_186_int_cov_accel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_186_int_cov_accel_5d"""
    return (_safe_div(opinc, debt)).diff(5).diff(21)

def solv_187_int_cov_accel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_187_int_cov_accel_21d"""
    return (_safe_div(opinc, debt)).diff(21).diff(21)

def solv_188_int_cov_accel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_188_int_cov_accel_63d"""
    return (_safe_div(opinc, debt)).diff(63).diff(21)

def solv_189_int_cov_accel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_189_int_cov_accel_126d"""
    return (_safe_div(opinc, debt)).diff(126).diff(21)

def solv_190_int_cov_accel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_190_int_cov_accel_252d"""
    return (_safe_div(opinc, debt)).diff(252).diff(21)

def solv_191_debt_eq_accel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_191_debt_eq_accel_5d"""
    return (_safe_div(debt, equity)).diff(5).diff(21)

def solv_192_debt_eq_accel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_192_debt_eq_accel_21d"""
    return (_safe_div(debt, equity)).diff(21).diff(21)

def solv_193_debt_eq_accel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_193_debt_eq_accel_63d"""
    return (_safe_div(debt, equity)).diff(63).diff(21)

def solv_194_debt_eq_accel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_194_debt_eq_accel_126d"""
    return (_safe_div(debt, equity)).diff(126).diff(21)

def solv_195_debt_eq_accel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_195_debt_eq_accel_252d"""
    return (_safe_div(debt, equity)).diff(252).diff(21)

def solv_196_altman_wc_ta_accel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_196_altman_wc_ta_accel_5d"""
    return (_safe_div(assets - liabs, assets)).diff(5).diff(21)

def solv_197_altman_wc_ta_accel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_197_altman_wc_ta_accel_21d"""
    return (_safe_div(assets - liabs, assets)).diff(21).diff(21)

def solv_198_altman_wc_ta_accel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_198_altman_wc_ta_accel_63d"""
    return (_safe_div(assets - liabs, assets)).diff(63).diff(21)

def solv_199_altman_wc_ta_accel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_199_altman_wc_ta_accel_126d"""
    return (_safe_div(assets - liabs, assets)).diff(126).diff(21)

def solv_200_altman_wc_ta_accel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_200_altman_wc_ta_accel_252d"""
    return (_safe_div(assets - liabs, assets)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V40_REGISTRY_ACCEL = {
    "solv_176_debt_lvl_accel_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_176_debt_lvl_accel_5d},
    "solv_177_debt_lvl_accel_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_177_debt_lvl_accel_21d},
    "solv_178_debt_lvl_accel_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_178_debt_lvl_accel_63d},
    "solv_179_debt_lvl_accel_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_179_debt_lvl_accel_126d},
    "solv_180_debt_lvl_accel_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_180_debt_lvl_accel_252d},
    "solv_181_debt_assets_accel_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_181_debt_assets_accel_5d},
    "solv_182_debt_assets_accel_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_182_debt_assets_accel_21d},
    "solv_183_debt_assets_accel_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_183_debt_assets_accel_63d},
    "solv_184_debt_assets_accel_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_184_debt_assets_accel_126d},
    "solv_185_debt_assets_accel_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_185_debt_assets_accel_252d},
    "solv_186_int_cov_accel_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_186_int_cov_accel_5d},
    "solv_187_int_cov_accel_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_187_int_cov_accel_21d},
    "solv_188_int_cov_accel_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_188_int_cov_accel_63d},
    "solv_189_int_cov_accel_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_189_int_cov_accel_126d},
    "solv_190_int_cov_accel_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_190_int_cov_accel_252d},
    "solv_191_debt_eq_accel_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_191_debt_eq_accel_5d},
    "solv_192_debt_eq_accel_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_192_debt_eq_accel_21d},
    "solv_193_debt_eq_accel_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_193_debt_eq_accel_63d},
    "solv_194_debt_eq_accel_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_194_debt_eq_accel_126d},
    "solv_195_debt_eq_accel_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_195_debt_eq_accel_252d},
    "solv_196_altman_wc_ta_accel_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_196_altman_wc_ta_accel_5d},
    "solv_197_altman_wc_ta_accel_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_197_altman_wc_ta_accel_21d},
    "solv_198_altman_wc_ta_accel_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_198_altman_wc_ta_accel_63d},
    "solv_199_altman_wc_ta_accel_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_199_altman_wc_ta_accel_126d},
    "solv_200_altman_wc_ta_accel_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_200_altman_wc_ta_accel_252d},
}
