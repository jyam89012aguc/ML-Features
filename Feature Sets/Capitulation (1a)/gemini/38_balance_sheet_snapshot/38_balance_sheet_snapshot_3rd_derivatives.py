"""
38_balance_sheet_snapshot — 3rd Derivatives (Acceleration)
Domain: balance_sheet_snapshot
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

def bals_176_assets_lvl_accel_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_176_assets_lvl_accel_5d"""
    return (assets).diff(5).diff(21)

def bals_177_assets_lvl_accel_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_177_assets_lvl_accel_21d"""
    return (assets).diff(21).diff(21)

def bals_178_assets_lvl_accel_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_178_assets_lvl_accel_63d"""
    return (assets).diff(63).diff(21)

def bals_179_assets_lvl_accel_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_179_assets_lvl_accel_126d"""
    return (assets).diff(126).diff(21)

def bals_180_assets_lvl_accel_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_180_assets_lvl_accel_252d"""
    return (assets).diff(252).diff(21)

def bals_181_debt_eq_accel_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_181_debt_eq_accel_5d"""
    return (_safe_div(debt, equity)).diff(5).diff(21)

def bals_182_debt_eq_accel_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_182_debt_eq_accel_21d"""
    return (_safe_div(debt, equity)).diff(21).diff(21)

def bals_183_debt_eq_accel_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_183_debt_eq_accel_63d"""
    return (_safe_div(debt, equity)).diff(63).diff(21)

def bals_184_debt_eq_accel_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_184_debt_eq_accel_126d"""
    return (_safe_div(debt, equity)).diff(126).diff(21)

def bals_185_debt_eq_accel_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_185_debt_eq_accel_252d"""
    return (_safe_div(debt, equity)).diff(252).diff(21)

def bals_186_curr_rat_accel_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_186_curr_rat_accel_5d"""
    return (_safe_div(assets, liabs)).diff(5).diff(21)

def bals_187_curr_rat_accel_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_187_curr_rat_accel_21d"""
    return (_safe_div(assets, liabs)).diff(21).diff(21)

def bals_188_curr_rat_accel_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_188_curr_rat_accel_63d"""
    return (_safe_div(assets, liabs)).diff(63).diff(21)

def bals_189_curr_rat_accel_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_189_curr_rat_accel_126d"""
    return (_safe_div(assets, liabs)).diff(126).diff(21)

def bals_190_curr_rat_accel_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_190_curr_rat_accel_252d"""
    return (_safe_div(assets, liabs)).diff(252).diff(21)

def bals_191_cash_assets_accel_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_191_cash_assets_accel_5d"""
    return (_safe_div(cashnequiv, assets)).diff(5).diff(21)

def bals_192_cash_assets_accel_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_192_cash_assets_accel_21d"""
    return (_safe_div(cashnequiv, assets)).diff(21).diff(21)

def bals_193_cash_assets_accel_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_193_cash_assets_accel_63d"""
    return (_safe_div(cashnequiv, assets)).diff(63).diff(21)

def bals_194_cash_assets_accel_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_194_cash_assets_accel_126d"""
    return (_safe_div(cashnequiv, assets)).diff(126).diff(21)

def bals_195_cash_assets_accel_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_195_cash_assets_accel_252d"""
    return (_safe_div(cashnequiv, assets)).diff(252).diff(21)

def bals_196_equity_assets_accel_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_196_equity_assets_accel_5d"""
    return (_safe_div(equity, assets)).diff(5).diff(21)

def bals_197_equity_assets_accel_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_197_equity_assets_accel_21d"""
    return (_safe_div(equity, assets)).diff(21).diff(21)

def bals_198_equity_assets_accel_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_198_equity_assets_accel_63d"""
    return (_safe_div(equity, assets)).diff(63).diff(21)

def bals_199_equity_assets_accel_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_199_equity_assets_accel_126d"""
    return (_safe_div(equity, assets)).diff(126).diff(21)

def bals_200_equity_assets_accel_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_200_equity_assets_accel_252d"""
    return (_safe_div(equity, assets)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V38_REGISTRY_ACCEL = {
    "bals_176_assets_lvl_accel_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_176_assets_lvl_accel_5d},
    "bals_177_assets_lvl_accel_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_177_assets_lvl_accel_21d},
    "bals_178_assets_lvl_accel_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_178_assets_lvl_accel_63d},
    "bals_179_assets_lvl_accel_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_179_assets_lvl_accel_126d},
    "bals_180_assets_lvl_accel_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_180_assets_lvl_accel_252d},
    "bals_181_debt_eq_accel_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_181_debt_eq_accel_5d},
    "bals_182_debt_eq_accel_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_182_debt_eq_accel_21d},
    "bals_183_debt_eq_accel_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_183_debt_eq_accel_63d},
    "bals_184_debt_eq_accel_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_184_debt_eq_accel_126d},
    "bals_185_debt_eq_accel_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_185_debt_eq_accel_252d},
    "bals_186_curr_rat_accel_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_186_curr_rat_accel_5d},
    "bals_187_curr_rat_accel_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_187_curr_rat_accel_21d},
    "bals_188_curr_rat_accel_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_188_curr_rat_accel_63d},
    "bals_189_curr_rat_accel_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_189_curr_rat_accel_126d},
    "bals_190_curr_rat_accel_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_190_curr_rat_accel_252d},
    "bals_191_cash_assets_accel_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_191_cash_assets_accel_5d},
    "bals_192_cash_assets_accel_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_192_cash_assets_accel_21d},
    "bals_193_cash_assets_accel_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_193_cash_assets_accel_63d},
    "bals_194_cash_assets_accel_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_194_cash_assets_accel_126d},
    "bals_195_cash_assets_accel_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_195_cash_assets_accel_252d},
    "bals_196_equity_assets_accel_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_196_equity_assets_accel_5d},
    "bals_197_equity_assets_accel_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_197_equity_assets_accel_21d},
    "bals_198_equity_assets_accel_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_198_equity_assets_accel_63d},
    "bals_199_equity_assets_accel_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_199_equity_assets_accel_126d},
    "bals_200_equity_assets_accel_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_200_equity_assets_accel_252d},
}
