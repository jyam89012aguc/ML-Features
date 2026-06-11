"""
36_profitability_snapshot — 3rd Derivatives (Acceleration)
Domain: profitability_snapshot
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

def prof_176_net_margin_accel_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_176_net_margin_accel_5d"""
    return (_safe_div(netinc, revenue)).diff(5).diff(21)

def prof_177_net_margin_accel_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_177_net_margin_accel_21d"""
    return (_safe_div(netinc, revenue)).diff(21).diff(21)

def prof_178_net_margin_accel_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_178_net_margin_accel_63d"""
    return (_safe_div(netinc, revenue)).diff(63).diff(21)

def prof_179_net_margin_accel_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_179_net_margin_accel_126d"""
    return (_safe_div(netinc, revenue)).diff(126).diff(21)

def prof_180_net_margin_accel_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_180_net_margin_accel_252d"""
    return (_safe_div(netinc, revenue)).diff(252).diff(21)

def prof_181_op_margin_accel_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_181_op_margin_accel_5d"""
    return (_safe_div(opinc, revenue)).diff(5).diff(21)

def prof_182_op_margin_accel_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_182_op_margin_accel_21d"""
    return (_safe_div(opinc, revenue)).diff(21).diff(21)

def prof_183_op_margin_accel_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_183_op_margin_accel_63d"""
    return (_safe_div(opinc, revenue)).diff(63).diff(21)

def prof_184_op_margin_accel_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_184_op_margin_accel_126d"""
    return (_safe_div(opinc, revenue)).diff(126).diff(21)

def prof_185_op_margin_accel_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_185_op_margin_accel_252d"""
    return (_safe_div(opinc, revenue)).diff(252).diff(21)

def prof_186_netinc_lvl_accel_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_186_netinc_lvl_accel_5d"""
    return (netinc).diff(5).diff(21)

def prof_187_netinc_lvl_accel_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_187_netinc_lvl_accel_21d"""
    return (netinc).diff(21).diff(21)

def prof_188_netinc_lvl_accel_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_188_netinc_lvl_accel_63d"""
    return (netinc).diff(63).diff(21)

def prof_189_netinc_lvl_accel_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_189_netinc_lvl_accel_126d"""
    return (netinc).diff(126).diff(21)

def prof_190_netinc_lvl_accel_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_190_netinc_lvl_accel_252d"""
    return (netinc).diff(252).diff(21)

def prof_191_roe_accel_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_191_roe_accel_5d"""
    return (_safe_div(netinc, equity)).diff(5).diff(21)

def prof_192_roe_accel_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_192_roe_accel_21d"""
    return (_safe_div(netinc, equity)).diff(21).diff(21)

def prof_193_roe_accel_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_193_roe_accel_63d"""
    return (_safe_div(netinc, equity)).diff(63).diff(21)

def prof_194_roe_accel_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_194_roe_accel_126d"""
    return (_safe_div(netinc, equity)).diff(126).diff(21)

def prof_195_roe_accel_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_195_roe_accel_252d"""
    return (_safe_div(netinc, equity)).diff(252).diff(21)

def prof_196_roa_accel_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_196_roa_accel_5d"""
    return (_safe_div(netinc, assets)).diff(5).diff(21)

def prof_197_roa_accel_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_197_roa_accel_21d"""
    return (_safe_div(netinc, assets)).diff(21).diff(21)

def prof_198_roa_accel_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_198_roa_accel_63d"""
    return (_safe_div(netinc, assets)).diff(63).diff(21)

def prof_199_roa_accel_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_199_roa_accel_126d"""
    return (_safe_div(netinc, assets)).diff(126).diff(21)

def prof_200_roa_accel_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_200_roa_accel_252d"""
    return (_safe_div(netinc, assets)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V36_REGISTRY_ACCEL = {
    "prof_176_net_margin_accel_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_176_net_margin_accel_5d},
    "prof_177_net_margin_accel_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_177_net_margin_accel_21d},
    "prof_178_net_margin_accel_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_178_net_margin_accel_63d},
    "prof_179_net_margin_accel_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_179_net_margin_accel_126d},
    "prof_180_net_margin_accel_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_180_net_margin_accel_252d},
    "prof_181_op_margin_accel_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_181_op_margin_accel_5d},
    "prof_182_op_margin_accel_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_182_op_margin_accel_21d},
    "prof_183_op_margin_accel_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_183_op_margin_accel_63d},
    "prof_184_op_margin_accel_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_184_op_margin_accel_126d},
    "prof_185_op_margin_accel_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_185_op_margin_accel_252d},
    "prof_186_netinc_lvl_accel_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_186_netinc_lvl_accel_5d},
    "prof_187_netinc_lvl_accel_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_187_netinc_lvl_accel_21d},
    "prof_188_netinc_lvl_accel_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_188_netinc_lvl_accel_63d},
    "prof_189_netinc_lvl_accel_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_189_netinc_lvl_accel_126d},
    "prof_190_netinc_lvl_accel_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_190_netinc_lvl_accel_252d},
    "prof_191_roe_accel_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_191_roe_accel_5d},
    "prof_192_roe_accel_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_192_roe_accel_21d},
    "prof_193_roe_accel_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_193_roe_accel_63d},
    "prof_194_roe_accel_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_194_roe_accel_126d},
    "prof_195_roe_accel_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_195_roe_accel_252d},
    "prof_196_roa_accel_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_196_roa_accel_5d},
    "prof_197_roa_accel_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_197_roa_accel_21d},
    "prof_198_roa_accel_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_198_roa_accel_63d},
    "prof_199_roa_accel_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_199_roa_accel_126d},
    "prof_200_roa_accel_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_200_roa_accel_252d},
}
