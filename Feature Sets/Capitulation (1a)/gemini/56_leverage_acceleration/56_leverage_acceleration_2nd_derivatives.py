"""
56_leverage_acceleration — 2nd Derivatives (Velocity)
Domain: leverage_acceleration
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

def leva_151_debt_equity_vel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_151_debt_equity_vel_5d"""
    return (_safe_div(debt, equity)).diff(5)

def leva_152_debt_equity_vel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_152_debt_equity_vel_21d"""
    return (_safe_div(debt, equity)).diff(21)

def leva_153_debt_equity_vel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_153_debt_equity_vel_63d"""
    return (_safe_div(debt, equity)).diff(63)

def leva_154_debt_equity_vel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_154_debt_equity_vel_126d"""
    return (_safe_div(debt, equity)).diff(126)

def leva_155_debt_equity_vel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_155_debt_equity_vel_252d"""
    return (_safe_div(debt, equity)).diff(252)

def leva_156_debt_assets_vel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_156_debt_assets_vel_5d"""
    return (_safe_div(debt, assets)).diff(5)

def leva_157_debt_assets_vel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_157_debt_assets_vel_21d"""
    return (_safe_div(debt, assets)).diff(21)

def leva_158_debt_assets_vel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_158_debt_assets_vel_63d"""
    return (_safe_div(debt, assets)).diff(63)

def leva_159_debt_assets_vel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_159_debt_assets_vel_126d"""
    return (_safe_div(debt, assets)).diff(126)

def leva_160_debt_assets_vel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_160_debt_assets_vel_252d"""
    return (_safe_div(debt, assets)).diff(252)

def leva_161_leverage_ratio_vel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_161_leverage_ratio_vel_5d"""
    return (_safe_div(assets, equity)).diff(5)

def leva_162_leverage_ratio_vel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_162_leverage_ratio_vel_21d"""
    return (_safe_div(assets, equity)).diff(21)

def leva_163_leverage_ratio_vel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_163_leverage_ratio_vel_63d"""
    return (_safe_div(assets, equity)).diff(63)

def leva_164_leverage_ratio_vel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_164_leverage_ratio_vel_126d"""
    return (_safe_div(assets, equity)).diff(126)

def leva_165_leverage_ratio_vel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_165_leverage_ratio_vel_252d"""
    return (_safe_div(assets, equity)).diff(252)

def leva_166_debt_ebitda_vel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_166_debt_ebitda_vel_5d"""
    return (_safe_div(debt, ebitda)).diff(5)

def leva_167_debt_ebitda_vel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_167_debt_ebitda_vel_21d"""
    return (_safe_div(debt, ebitda)).diff(21)

def leva_168_debt_ebitda_vel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_168_debt_ebitda_vel_63d"""
    return (_safe_div(debt, ebitda)).diff(63)

def leva_169_debt_ebitda_vel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_169_debt_ebitda_vel_126d"""
    return (_safe_div(debt, ebitda)).diff(126)

def leva_170_debt_ebitda_vel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_170_debt_ebitda_vel_252d"""
    return (_safe_div(debt, ebitda)).diff(252)

def leva_171_debt_chg_yoy_vel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_171_debt_chg_yoy_vel_5d"""
    return (debt.pct_change(252)).diff(5)

def leva_172_debt_chg_yoy_vel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_172_debt_chg_yoy_vel_21d"""
    return (debt.pct_change(252)).diff(21)

def leva_173_debt_chg_yoy_vel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_173_debt_chg_yoy_vel_63d"""
    return (debt.pct_change(252)).diff(63)

def leva_174_debt_chg_yoy_vel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_174_debt_chg_yoy_vel_126d"""
    return (debt.pct_change(252)).diff(126)

def leva_175_debt_chg_yoy_vel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_175_debt_chg_yoy_vel_252d"""
    return (debt.pct_change(252)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V56_REGISTRY_VEL = {
    "leva_151_debt_equity_vel_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_151_debt_equity_vel_5d},
    "leva_152_debt_equity_vel_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_152_debt_equity_vel_21d},
    "leva_153_debt_equity_vel_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_153_debt_equity_vel_63d},
    "leva_154_debt_equity_vel_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_154_debt_equity_vel_126d},
    "leva_155_debt_equity_vel_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_155_debt_equity_vel_252d},
    "leva_156_debt_assets_vel_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_156_debt_assets_vel_5d},
    "leva_157_debt_assets_vel_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_157_debt_assets_vel_21d},
    "leva_158_debt_assets_vel_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_158_debt_assets_vel_63d},
    "leva_159_debt_assets_vel_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_159_debt_assets_vel_126d},
    "leva_160_debt_assets_vel_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_160_debt_assets_vel_252d},
    "leva_161_leverage_ratio_vel_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_161_leverage_ratio_vel_5d},
    "leva_162_leverage_ratio_vel_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_162_leverage_ratio_vel_21d},
    "leva_163_leverage_ratio_vel_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_163_leverage_ratio_vel_63d},
    "leva_164_leverage_ratio_vel_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_164_leverage_ratio_vel_126d},
    "leva_165_leverage_ratio_vel_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_165_leverage_ratio_vel_252d},
    "leva_166_debt_ebitda_vel_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_166_debt_ebitda_vel_5d},
    "leva_167_debt_ebitda_vel_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_167_debt_ebitda_vel_21d},
    "leva_168_debt_ebitda_vel_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_168_debt_ebitda_vel_63d},
    "leva_169_debt_ebitda_vel_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_169_debt_ebitda_vel_126d},
    "leva_170_debt_ebitda_vel_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_170_debt_ebitda_vel_252d},
    "leva_171_debt_chg_yoy_vel_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_171_debt_chg_yoy_vel_5d},
    "leva_172_debt_chg_yoy_vel_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_172_debt_chg_yoy_vel_21d},
    "leva_173_debt_chg_yoy_vel_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_173_debt_chg_yoy_vel_63d},
    "leva_174_debt_chg_yoy_vel_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_174_debt_chg_yoy_vel_126d},
    "leva_175_debt_chg_yoy_vel_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_175_debt_chg_yoy_vel_252d},
}
