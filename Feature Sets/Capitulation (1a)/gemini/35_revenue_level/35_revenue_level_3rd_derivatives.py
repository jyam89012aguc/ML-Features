"""
35_revenue_level — 3rd Derivatives (Acceleration)
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

def revl_176_level_accel_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_176_level_accel_5d"""
    return (revenue).diff(5).diff(21)

def revl_177_level_accel_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_177_level_accel_21d"""
    return (revenue).diff(21).diff(21)

def revl_178_level_accel_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_178_level_accel_63d"""
    return (revenue).diff(63).diff(21)

def revl_179_level_accel_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_179_level_accel_126d"""
    return (revenue).diff(126).diff(21)

def revl_180_level_accel_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_180_level_accel_252d"""
    return (revenue).diff(252).diff(21)

def revl_181_ps_accel_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_181_ps_accel_5d"""
    return (_safe_div(revenue, sharesbas)).diff(5).diff(21)

def revl_182_ps_accel_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_182_ps_accel_21d"""
    return (_safe_div(revenue, sharesbas)).diff(21).diff(21)

def revl_183_ps_accel_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_183_ps_accel_63d"""
    return (_safe_div(revenue, sharesbas)).diff(63).diff(21)

def revl_184_ps_accel_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_184_ps_accel_126d"""
    return (_safe_div(revenue, sharesbas)).diff(126).diff(21)

def revl_185_ps_accel_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_185_ps_accel_252d"""
    return (_safe_div(revenue, sharesbas)).diff(252).diff(21)

def revl_186_pa_accel_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_186_pa_accel_5d"""
    return (_safe_div(revenue, assets)).diff(5).diff(21)

def revl_187_pa_accel_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_187_pa_accel_21d"""
    return (_safe_div(revenue, assets)).diff(21).diff(21)

def revl_188_pa_accel_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_188_pa_accel_63d"""
    return (_safe_div(revenue, assets)).diff(63).diff(21)

def revl_189_pa_accel_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_189_pa_accel_126d"""
    return (_safe_div(revenue, assets)).diff(126).diff(21)

def revl_190_pa_accel_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_190_pa_accel_252d"""
    return (_safe_div(revenue, assets)).diff(252).diff(21)

def revl_191_log_accel_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_191_log_accel_5d"""
    return (np.log(revenue.clip(lower=_EPS))).diff(5).diff(21)

def revl_192_log_accel_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_192_log_accel_21d"""
    return (np.log(revenue.clip(lower=_EPS))).diff(21).diff(21)

def revl_193_log_accel_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_193_log_accel_63d"""
    return (np.log(revenue.clip(lower=_EPS))).diff(63).diff(21)

def revl_194_log_accel_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_194_log_accel_126d"""
    return (np.log(revenue.clip(lower=_EPS))).diff(126).diff(21)

def revl_195_log_accel_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_195_log_accel_252d"""
    return (np.log(revenue.clip(lower=_EPS))).diff(252).diff(21)

def revl_196_yield_accel_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_196_yield_accel_5d"""
    return (_safe_div(revenue, marketcap)).diff(5).diff(21)

def revl_197_yield_accel_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_197_yield_accel_21d"""
    return (_safe_div(revenue, marketcap)).diff(21).diff(21)

def revl_198_yield_accel_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_198_yield_accel_63d"""
    return (_safe_div(revenue, marketcap)).diff(63).diff(21)

def revl_199_yield_accel_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_199_yield_accel_126d"""
    return (_safe_div(revenue, marketcap)).diff(126).diff(21)

def revl_200_yield_accel_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_200_yield_accel_252d"""
    return (_safe_div(revenue, marketcap)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V35_REGISTRY_ACCEL = {
    "revl_176_level_accel_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_176_level_accel_5d},
    "revl_177_level_accel_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_177_level_accel_21d},
    "revl_178_level_accel_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_178_level_accel_63d},
    "revl_179_level_accel_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_179_level_accel_126d},
    "revl_180_level_accel_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_180_level_accel_252d},
    "revl_181_ps_accel_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_181_ps_accel_5d},
    "revl_182_ps_accel_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_182_ps_accel_21d},
    "revl_183_ps_accel_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_183_ps_accel_63d},
    "revl_184_ps_accel_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_184_ps_accel_126d},
    "revl_185_ps_accel_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_185_ps_accel_252d},
    "revl_186_pa_accel_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_186_pa_accel_5d},
    "revl_187_pa_accel_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_187_pa_accel_21d},
    "revl_188_pa_accel_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_188_pa_accel_63d},
    "revl_189_pa_accel_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_189_pa_accel_126d},
    "revl_190_pa_accel_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_190_pa_accel_252d},
    "revl_191_log_accel_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_191_log_accel_5d},
    "revl_192_log_accel_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_192_log_accel_21d},
    "revl_193_log_accel_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_193_log_accel_63d},
    "revl_194_log_accel_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_194_log_accel_126d},
    "revl_195_log_accel_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_195_log_accel_252d},
    "revl_196_yield_accel_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_196_yield_accel_5d},
    "revl_197_yield_accel_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_197_yield_accel_21d},
    "revl_198_yield_accel_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_198_yield_accel_63d},
    "revl_199_yield_accel_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_199_yield_accel_126d},
    "revl_200_yield_accel_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_200_yield_accel_252d},
}
