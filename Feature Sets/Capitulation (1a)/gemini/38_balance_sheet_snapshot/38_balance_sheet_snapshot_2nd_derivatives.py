"""
38_balance_sheet_snapshot — 2nd Derivatives (Velocity)
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

def bals_151_assets_lvl_vel_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_151_assets_lvl_vel_5d"""
    return (assets).diff(5)

def bals_152_assets_lvl_vel_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_152_assets_lvl_vel_21d"""
    return (assets).diff(21)

def bals_153_assets_lvl_vel_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_153_assets_lvl_vel_63d"""
    return (assets).diff(63)

def bals_154_assets_lvl_vel_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_154_assets_lvl_vel_126d"""
    return (assets).diff(126)

def bals_155_assets_lvl_vel_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_155_assets_lvl_vel_252d"""
    return (assets).diff(252)

def bals_156_debt_eq_vel_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_156_debt_eq_vel_5d"""
    return (_safe_div(debt, equity)).diff(5)

def bals_157_debt_eq_vel_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_157_debt_eq_vel_21d"""
    return (_safe_div(debt, equity)).diff(21)

def bals_158_debt_eq_vel_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_158_debt_eq_vel_63d"""
    return (_safe_div(debt, equity)).diff(63)

def bals_159_debt_eq_vel_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_159_debt_eq_vel_126d"""
    return (_safe_div(debt, equity)).diff(126)

def bals_160_debt_eq_vel_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_160_debt_eq_vel_252d"""
    return (_safe_div(debt, equity)).diff(252)

def bals_161_curr_rat_vel_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_161_curr_rat_vel_5d"""
    return (_safe_div(assets, liabs)).diff(5)

def bals_162_curr_rat_vel_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_162_curr_rat_vel_21d"""
    return (_safe_div(assets, liabs)).diff(21)

def bals_163_curr_rat_vel_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_163_curr_rat_vel_63d"""
    return (_safe_div(assets, liabs)).diff(63)

def bals_164_curr_rat_vel_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_164_curr_rat_vel_126d"""
    return (_safe_div(assets, liabs)).diff(126)

def bals_165_curr_rat_vel_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_165_curr_rat_vel_252d"""
    return (_safe_div(assets, liabs)).diff(252)

def bals_166_cash_assets_vel_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_166_cash_assets_vel_5d"""
    return (_safe_div(cashnequiv, assets)).diff(5)

def bals_167_cash_assets_vel_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_167_cash_assets_vel_21d"""
    return (_safe_div(cashnequiv, assets)).diff(21)

def bals_168_cash_assets_vel_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_168_cash_assets_vel_63d"""
    return (_safe_div(cashnequiv, assets)).diff(63)

def bals_169_cash_assets_vel_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_169_cash_assets_vel_126d"""
    return (_safe_div(cashnequiv, assets)).diff(126)

def bals_170_cash_assets_vel_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_170_cash_assets_vel_252d"""
    return (_safe_div(cashnequiv, assets)).diff(252)

def bals_171_equity_assets_vel_5d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_171_equity_assets_vel_5d"""
    return (_safe_div(equity, assets)).diff(5)

def bals_172_equity_assets_vel_21d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_172_equity_assets_vel_21d"""
    return (_safe_div(equity, assets)).diff(21)

def bals_173_equity_assets_vel_63d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_173_equity_assets_vel_63d"""
    return (_safe_div(equity, assets)).diff(63)

def bals_174_equity_assets_vel_126d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_174_equity_assets_vel_126d"""
    return (_safe_div(equity, assets)).diff(126)

def bals_175_equity_assets_vel_252d(assets: pd.Series, liabs: pd.Series, equity: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """bals_175_equity_assets_vel_252d"""
    return (_safe_div(equity, assets)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V38_REGISTRY_VEL = {
    "bals_151_assets_lvl_vel_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_151_assets_lvl_vel_5d},
    "bals_152_assets_lvl_vel_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_152_assets_lvl_vel_21d},
    "bals_153_assets_lvl_vel_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_153_assets_lvl_vel_63d},
    "bals_154_assets_lvl_vel_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_154_assets_lvl_vel_126d},
    "bals_155_assets_lvl_vel_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_155_assets_lvl_vel_252d},
    "bals_156_debt_eq_vel_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_156_debt_eq_vel_5d},
    "bals_157_debt_eq_vel_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_157_debt_eq_vel_21d},
    "bals_158_debt_eq_vel_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_158_debt_eq_vel_63d},
    "bals_159_debt_eq_vel_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_159_debt_eq_vel_126d},
    "bals_160_debt_eq_vel_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_160_debt_eq_vel_252d},
    "bals_161_curr_rat_vel_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_161_curr_rat_vel_5d},
    "bals_162_curr_rat_vel_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_162_curr_rat_vel_21d},
    "bals_163_curr_rat_vel_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_163_curr_rat_vel_63d},
    "bals_164_curr_rat_vel_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_164_curr_rat_vel_126d},
    "bals_165_curr_rat_vel_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_165_curr_rat_vel_252d},
    "bals_166_cash_assets_vel_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_166_cash_assets_vel_5d},
    "bals_167_cash_assets_vel_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_167_cash_assets_vel_21d},
    "bals_168_cash_assets_vel_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_168_cash_assets_vel_63d},
    "bals_169_cash_assets_vel_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_169_cash_assets_vel_126d},
    "bals_170_cash_assets_vel_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_170_cash_assets_vel_252d},
    "bals_171_equity_assets_vel_5d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_171_equity_assets_vel_5d},
    "bals_172_equity_assets_vel_21d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_172_equity_assets_vel_21d},
    "bals_173_equity_assets_vel_63d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_173_equity_assets_vel_63d},
    "bals_174_equity_assets_vel_126d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_174_equity_assets_vel_126d},
    "bals_175_equity_assets_vel_252d": {"inputs": ["assets", "liabs", "equity", "cashnequiv", "debt"], "func": bals_175_equity_assets_vel_252d},
}
