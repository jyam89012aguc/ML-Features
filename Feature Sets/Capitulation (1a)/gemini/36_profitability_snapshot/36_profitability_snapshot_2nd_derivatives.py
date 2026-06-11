"""
36_profitability_snapshot — 2nd Derivatives (Velocity)
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

def prof_151_net_margin_vel_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_151_net_margin_vel_5d"""
    return (_safe_div(netinc, revenue)).diff(5)

def prof_152_net_margin_vel_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_152_net_margin_vel_21d"""
    return (_safe_div(netinc, revenue)).diff(21)

def prof_153_net_margin_vel_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_153_net_margin_vel_63d"""
    return (_safe_div(netinc, revenue)).diff(63)

def prof_154_net_margin_vel_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_154_net_margin_vel_126d"""
    return (_safe_div(netinc, revenue)).diff(126)

def prof_155_net_margin_vel_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_155_net_margin_vel_252d"""
    return (_safe_div(netinc, revenue)).diff(252)

def prof_156_op_margin_vel_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_156_op_margin_vel_5d"""
    return (_safe_div(opinc, revenue)).diff(5)

def prof_157_op_margin_vel_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_157_op_margin_vel_21d"""
    return (_safe_div(opinc, revenue)).diff(21)

def prof_158_op_margin_vel_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_158_op_margin_vel_63d"""
    return (_safe_div(opinc, revenue)).diff(63)

def prof_159_op_margin_vel_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_159_op_margin_vel_126d"""
    return (_safe_div(opinc, revenue)).diff(126)

def prof_160_op_margin_vel_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_160_op_margin_vel_252d"""
    return (_safe_div(opinc, revenue)).diff(252)

def prof_161_netinc_lvl_vel_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_161_netinc_lvl_vel_5d"""
    return (netinc).diff(5)

def prof_162_netinc_lvl_vel_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_162_netinc_lvl_vel_21d"""
    return (netinc).diff(21)

def prof_163_netinc_lvl_vel_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_163_netinc_lvl_vel_63d"""
    return (netinc).diff(63)

def prof_164_netinc_lvl_vel_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_164_netinc_lvl_vel_126d"""
    return (netinc).diff(126)

def prof_165_netinc_lvl_vel_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_165_netinc_lvl_vel_252d"""
    return (netinc).diff(252)

def prof_166_roe_vel_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_166_roe_vel_5d"""
    return (_safe_div(netinc, equity)).diff(5)

def prof_167_roe_vel_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_167_roe_vel_21d"""
    return (_safe_div(netinc, equity)).diff(21)

def prof_168_roe_vel_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_168_roe_vel_63d"""
    return (_safe_div(netinc, equity)).diff(63)

def prof_169_roe_vel_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_169_roe_vel_126d"""
    return (_safe_div(netinc, equity)).diff(126)

def prof_170_roe_vel_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_170_roe_vel_252d"""
    return (_safe_div(netinc, equity)).diff(252)

def prof_171_roa_vel_5d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_171_roa_vel_5d"""
    return (_safe_div(netinc, assets)).diff(5)

def prof_172_roa_vel_21d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_172_roa_vel_21d"""
    return (_safe_div(netinc, assets)).diff(21)

def prof_173_roa_vel_63d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_173_roa_vel_63d"""
    return (_safe_div(netinc, assets)).diff(63)

def prof_174_roa_vel_126d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_174_roa_vel_126d"""
    return (_safe_div(netinc, assets)).diff(126)

def prof_175_roa_vel_252d(netinc: pd.Series, opinc: pd.Series, revenue: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """prof_175_roa_vel_252d"""
    return (_safe_div(netinc, assets)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V36_REGISTRY_VEL = {
    "prof_151_net_margin_vel_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_151_net_margin_vel_5d},
    "prof_152_net_margin_vel_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_152_net_margin_vel_21d},
    "prof_153_net_margin_vel_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_153_net_margin_vel_63d},
    "prof_154_net_margin_vel_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_154_net_margin_vel_126d},
    "prof_155_net_margin_vel_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_155_net_margin_vel_252d},
    "prof_156_op_margin_vel_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_156_op_margin_vel_5d},
    "prof_157_op_margin_vel_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_157_op_margin_vel_21d},
    "prof_158_op_margin_vel_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_158_op_margin_vel_63d},
    "prof_159_op_margin_vel_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_159_op_margin_vel_126d},
    "prof_160_op_margin_vel_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_160_op_margin_vel_252d},
    "prof_161_netinc_lvl_vel_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_161_netinc_lvl_vel_5d},
    "prof_162_netinc_lvl_vel_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_162_netinc_lvl_vel_21d},
    "prof_163_netinc_lvl_vel_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_163_netinc_lvl_vel_63d},
    "prof_164_netinc_lvl_vel_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_164_netinc_lvl_vel_126d},
    "prof_165_netinc_lvl_vel_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_165_netinc_lvl_vel_252d},
    "prof_166_roe_vel_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_166_roe_vel_5d},
    "prof_167_roe_vel_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_167_roe_vel_21d},
    "prof_168_roe_vel_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_168_roe_vel_63d},
    "prof_169_roe_vel_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_169_roe_vel_126d},
    "prof_170_roe_vel_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_170_roe_vel_252d},
    "prof_171_roa_vel_5d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_171_roa_vel_5d},
    "prof_172_roa_vel_21d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_172_roa_vel_21d},
    "prof_173_roa_vel_63d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_173_roa_vel_63d},
    "prof_174_roa_vel_126d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_174_roa_vel_126d},
    "prof_175_roa_vel_252d": {"inputs": ["netinc", "opinc", "revenue", "equity", "assets"], "func": prof_175_roa_vel_252d},
}
