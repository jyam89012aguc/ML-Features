"""
56_leverage_acceleration — 3rd Derivatives (Acceleration)
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

def leva_176_debt_equity_accel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_176_debt_equity_accel_5d"""
    return (_safe_div(debt, equity)).diff(5).diff(21)

def leva_177_debt_equity_accel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_177_debt_equity_accel_21d"""
    return (_safe_div(debt, equity)).diff(21).diff(21)

def leva_178_debt_equity_accel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_178_debt_equity_accel_63d"""
    return (_safe_div(debt, equity)).diff(63).diff(21)

def leva_179_debt_equity_accel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_179_debt_equity_accel_126d"""
    return (_safe_div(debt, equity)).diff(126).diff(21)

def leva_180_debt_equity_accel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_180_debt_equity_accel_252d"""
    return (_safe_div(debt, equity)).diff(252).diff(21)

def leva_181_debt_assets_accel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_181_debt_assets_accel_5d"""
    return (_safe_div(debt, assets)).diff(5).diff(21)

def leva_182_debt_assets_accel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_182_debt_assets_accel_21d"""
    return (_safe_div(debt, assets)).diff(21).diff(21)

def leva_183_debt_assets_accel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_183_debt_assets_accel_63d"""
    return (_safe_div(debt, assets)).diff(63).diff(21)

def leva_184_debt_assets_accel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_184_debt_assets_accel_126d"""
    return (_safe_div(debt, assets)).diff(126).diff(21)

def leva_185_debt_assets_accel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_185_debt_assets_accel_252d"""
    return (_safe_div(debt, assets)).diff(252).diff(21)

def leva_186_leverage_ratio_accel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_186_leverage_ratio_accel_5d"""
    return (_safe_div(assets, equity)).diff(5).diff(21)

def leva_187_leverage_ratio_accel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_187_leverage_ratio_accel_21d"""
    return (_safe_div(assets, equity)).diff(21).diff(21)

def leva_188_leverage_ratio_accel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_188_leverage_ratio_accel_63d"""
    return (_safe_div(assets, equity)).diff(63).diff(21)

def leva_189_leverage_ratio_accel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_189_leverage_ratio_accel_126d"""
    return (_safe_div(assets, equity)).diff(126).diff(21)

def leva_190_leverage_ratio_accel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_190_leverage_ratio_accel_252d"""
    return (_safe_div(assets, equity)).diff(252).diff(21)

def leva_191_debt_ebitda_accel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_191_debt_ebitda_accel_5d"""
    return (_safe_div(debt, ebitda)).diff(5).diff(21)

def leva_192_debt_ebitda_accel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_192_debt_ebitda_accel_21d"""
    return (_safe_div(debt, ebitda)).diff(21).diff(21)

def leva_193_debt_ebitda_accel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_193_debt_ebitda_accel_63d"""
    return (_safe_div(debt, ebitda)).diff(63).diff(21)

def leva_194_debt_ebitda_accel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_194_debt_ebitda_accel_126d"""
    return (_safe_div(debt, ebitda)).diff(126).diff(21)

def leva_195_debt_ebitda_accel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_195_debt_ebitda_accel_252d"""
    return (_safe_div(debt, ebitda)).diff(252).diff(21)

def leva_196_debt_chg_yoy_accel_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_196_debt_chg_yoy_accel_5d"""
    return (debt.pct_change(252)).diff(5).diff(21)

def leva_197_debt_chg_yoy_accel_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_197_debt_chg_yoy_accel_21d"""
    return (debt.pct_change(252)).diff(21).diff(21)

def leva_198_debt_chg_yoy_accel_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_198_debt_chg_yoy_accel_63d"""
    return (debt.pct_change(252)).diff(63).diff(21)

def leva_199_debt_chg_yoy_accel_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_199_debt_chg_yoy_accel_126d"""
    return (debt.pct_change(252)).diff(126).diff(21)

def leva_200_debt_chg_yoy_accel_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """leva_200_debt_chg_yoy_accel_252d"""
    return (debt.pct_change(252)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V56_REGISTRY_ACCEL = {
    "leva_176_debt_equity_accel_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_176_debt_equity_accel_5d},
    "leva_177_debt_equity_accel_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_177_debt_equity_accel_21d},
    "leva_178_debt_equity_accel_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_178_debt_equity_accel_63d},
    "leva_179_debt_equity_accel_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_179_debt_equity_accel_126d},
    "leva_180_debt_equity_accel_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_180_debt_equity_accel_252d},
    "leva_181_debt_assets_accel_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_181_debt_assets_accel_5d},
    "leva_182_debt_assets_accel_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_182_debt_assets_accel_21d},
    "leva_183_debt_assets_accel_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_183_debt_assets_accel_63d},
    "leva_184_debt_assets_accel_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_184_debt_assets_accel_126d},
    "leva_185_debt_assets_accel_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_185_debt_assets_accel_252d},
    "leva_186_leverage_ratio_accel_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_186_leverage_ratio_accel_5d},
    "leva_187_leverage_ratio_accel_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_187_leverage_ratio_accel_21d},
    "leva_188_leverage_ratio_accel_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_188_leverage_ratio_accel_63d},
    "leva_189_leverage_ratio_accel_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_189_leverage_ratio_accel_126d},
    "leva_190_leverage_ratio_accel_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_190_leverage_ratio_accel_252d},
    "leva_191_debt_ebitda_accel_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_191_debt_ebitda_accel_5d},
    "leva_192_debt_ebitda_accel_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_192_debt_ebitda_accel_21d},
    "leva_193_debt_ebitda_accel_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_193_debt_ebitda_accel_63d},
    "leva_194_debt_ebitda_accel_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_194_debt_ebitda_accel_126d},
    "leva_195_debt_ebitda_accel_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_195_debt_ebitda_accel_252d},
    "leva_196_debt_chg_yoy_accel_5d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_196_debt_chg_yoy_accel_5d},
    "leva_197_debt_chg_yoy_accel_21d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_197_debt_chg_yoy_accel_21d},
    "leva_198_debt_chg_yoy_accel_63d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_198_debt_chg_yoy_accel_63d},
    "leva_199_debt_chg_yoy_accel_126d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_199_debt_chg_yoy_accel_126d},
    "leva_200_debt_chg_yoy_accel_252d": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": leva_200_debt_chg_yoy_accel_252d},
}
