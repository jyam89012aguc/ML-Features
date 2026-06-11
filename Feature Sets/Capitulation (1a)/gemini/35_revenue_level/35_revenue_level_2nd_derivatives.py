"""
35_revenue_level — 2nd Derivatives (Velocity)
Domain: revenue_level
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

def revl_151_level_vel_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_151_level_vel_5d"""
    return (revenue).diff(5)

def revl_152_level_vel_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_152_level_vel_21d"""
    return (revenue).diff(21)

def revl_153_level_vel_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_153_level_vel_63d"""
    return (revenue).diff(63)

def revl_154_level_vel_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_154_level_vel_126d"""
    return (revenue).diff(126)

def revl_155_level_vel_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_155_level_vel_252d"""
    return (revenue).diff(252)

def revl_156_ps_vel_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_156_ps_vel_5d"""
    return (_safe_div(revenue, sharesbas)).diff(5)

def revl_157_ps_vel_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_157_ps_vel_21d"""
    return (_safe_div(revenue, sharesbas)).diff(21)

def revl_158_ps_vel_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_158_ps_vel_63d"""
    return (_safe_div(revenue, sharesbas)).diff(63)

def revl_159_ps_vel_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_159_ps_vel_126d"""
    return (_safe_div(revenue, sharesbas)).diff(126)

def revl_160_ps_vel_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_160_ps_vel_252d"""
    return (_safe_div(revenue, sharesbas)).diff(252)

def revl_161_pa_vel_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_161_pa_vel_5d"""
    return (_safe_div(revenue, assets)).diff(5)

def revl_162_pa_vel_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_162_pa_vel_21d"""
    return (_safe_div(revenue, assets)).diff(21)

def revl_163_pa_vel_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_163_pa_vel_63d"""
    return (_safe_div(revenue, assets)).diff(63)

def revl_164_pa_vel_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_164_pa_vel_126d"""
    return (_safe_div(revenue, assets)).diff(126)

def revl_165_pa_vel_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_165_pa_vel_252d"""
    return (_safe_div(revenue, assets)).diff(252)

def revl_166_log_vel_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_166_log_vel_5d"""
    return (np.log(revenue.clip(lower=_EPS))).diff(5)

def revl_167_log_vel_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_167_log_vel_21d"""
    return (np.log(revenue.clip(lower=_EPS))).diff(21)

def revl_168_log_vel_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_168_log_vel_63d"""
    return (np.log(revenue.clip(lower=_EPS))).diff(63)

def revl_169_log_vel_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_169_log_vel_126d"""
    return (np.log(revenue.clip(lower=_EPS))).diff(126)

def revl_170_log_vel_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_170_log_vel_252d"""
    return (np.log(revenue.clip(lower=_EPS))).diff(252)

def revl_171_yield_vel_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_171_yield_vel_5d"""
    return (_safe_div(revenue, marketcap)).diff(5)

def revl_172_yield_vel_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_172_yield_vel_21d"""
    return (_safe_div(revenue, marketcap)).diff(21)

def revl_173_yield_vel_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_173_yield_vel_63d"""
    return (_safe_div(revenue, marketcap)).diff(63)

def revl_174_yield_vel_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_174_yield_vel_126d"""
    return (_safe_div(revenue, marketcap)).diff(126)

def revl_175_yield_vel_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_175_yield_vel_252d"""
    return (_safe_div(revenue, marketcap)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V35_REGISTRY_VEL = {
    "revl_151_level_vel_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_151_level_vel_5d},
    "revl_152_level_vel_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_152_level_vel_21d},
    "revl_153_level_vel_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_153_level_vel_63d},
    "revl_154_level_vel_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_154_level_vel_126d},
    "revl_155_level_vel_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_155_level_vel_252d},
    "revl_156_ps_vel_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_156_ps_vel_5d},
    "revl_157_ps_vel_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_157_ps_vel_21d},
    "revl_158_ps_vel_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_158_ps_vel_63d},
    "revl_159_ps_vel_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_159_ps_vel_126d},
    "revl_160_ps_vel_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_160_ps_vel_252d},
    "revl_161_pa_vel_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_161_pa_vel_5d},
    "revl_162_pa_vel_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_162_pa_vel_21d},
    "revl_163_pa_vel_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_163_pa_vel_63d},
    "revl_164_pa_vel_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_164_pa_vel_126d},
    "revl_165_pa_vel_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_165_pa_vel_252d},
    "revl_166_log_vel_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_166_log_vel_5d},
    "revl_167_log_vel_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_167_log_vel_21d},
    "revl_168_log_vel_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_168_log_vel_63d},
    "revl_169_log_vel_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_169_log_vel_126d},
    "revl_170_log_vel_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_170_log_vel_252d},
    "revl_171_yield_vel_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_171_yield_vel_5d},
    "revl_172_yield_vel_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_172_yield_vel_21d},
    "revl_173_yield_vel_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_173_yield_vel_63d},
    "revl_174_yield_vel_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_174_yield_vel_126d},
    "revl_175_yield_vel_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_175_yield_vel_252d},
}
