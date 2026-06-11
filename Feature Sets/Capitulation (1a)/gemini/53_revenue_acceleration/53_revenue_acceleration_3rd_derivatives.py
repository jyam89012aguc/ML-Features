"""
53_revenue_acceleration — 3rd Derivatives (Acceleration)
Domain: revenue_acceleration
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

def reva_176_rev_growth_252_accel_5d(revenue: pd.Series) -> pd.Series:
    """reva_176_rev_growth_252_accel_5d"""
    return (revenue.pct_change(252)).diff(5).diff(21)

def reva_177_rev_growth_252_accel_21d(revenue: pd.Series) -> pd.Series:
    """reva_177_rev_growth_252_accel_21d"""
    return (revenue.pct_change(252)).diff(21).diff(21)

def reva_178_rev_growth_252_accel_63d(revenue: pd.Series) -> pd.Series:
    """reva_178_rev_growth_252_accel_63d"""
    return (revenue.pct_change(252)).diff(63).diff(21)

def reva_179_rev_growth_252_accel_126d(revenue: pd.Series) -> pd.Series:
    """reva_179_rev_growth_252_accel_126d"""
    return (revenue.pct_change(252)).diff(126).diff(21)

def reva_180_rev_growth_252_accel_252d(revenue: pd.Series) -> pd.Series:
    """reva_180_rev_growth_252_accel_252d"""
    return (revenue.pct_change(252)).diff(252).diff(21)

def reva_181_rev_growth_126_accel_5d(revenue: pd.Series) -> pd.Series:
    """reva_181_rev_growth_126_accel_5d"""
    return (revenue.pct_change(126)).diff(5).diff(21)

def reva_182_rev_growth_126_accel_21d(revenue: pd.Series) -> pd.Series:
    """reva_182_rev_growth_126_accel_21d"""
    return (revenue.pct_change(126)).diff(21).diff(21)

def reva_183_rev_growth_126_accel_63d(revenue: pd.Series) -> pd.Series:
    """reva_183_rev_growth_126_accel_63d"""
    return (revenue.pct_change(126)).diff(63).diff(21)

def reva_184_rev_growth_126_accel_126d(revenue: pd.Series) -> pd.Series:
    """reva_184_rev_growth_126_accel_126d"""
    return (revenue.pct_change(126)).diff(126).diff(21)

def reva_185_rev_growth_126_accel_252d(revenue: pd.Series) -> pd.Series:
    """reva_185_rev_growth_126_accel_252d"""
    return (revenue.pct_change(126)).diff(252).diff(21)

def reva_186_rev_growth_63_accel_5d(revenue: pd.Series) -> pd.Series:
    """reva_186_rev_growth_63_accel_5d"""
    return (revenue.pct_change(63)).diff(5).diff(21)

def reva_187_rev_growth_63_accel_21d(revenue: pd.Series) -> pd.Series:
    """reva_187_rev_growth_63_accel_21d"""
    return (revenue.pct_change(63)).diff(21).diff(21)

def reva_188_rev_growth_63_accel_63d(revenue: pd.Series) -> pd.Series:
    """reva_188_rev_growth_63_accel_63d"""
    return (revenue.pct_change(63)).diff(63).diff(21)

def reva_189_rev_growth_63_accel_126d(revenue: pd.Series) -> pd.Series:
    """reva_189_rev_growth_63_accel_126d"""
    return (revenue.pct_change(63)).diff(126).diff(21)

def reva_190_rev_growth_63_accel_252d(revenue: pd.Series) -> pd.Series:
    """reva_190_rev_growth_63_accel_252d"""
    return (revenue.pct_change(63)).diff(252).diff(21)

def reva_191_rev_growth_21_accel_5d(revenue: pd.Series) -> pd.Series:
    """reva_191_rev_growth_21_accel_5d"""
    return (revenue.pct_change(21)).diff(5).diff(21)

def reva_192_rev_growth_21_accel_21d(revenue: pd.Series) -> pd.Series:
    """reva_192_rev_growth_21_accel_21d"""
    return (revenue.pct_change(21)).diff(21).diff(21)

def reva_193_rev_growth_21_accel_63d(revenue: pd.Series) -> pd.Series:
    """reva_193_rev_growth_21_accel_63d"""
    return (revenue.pct_change(21)).diff(63).diff(21)

def reva_194_rev_growth_21_accel_126d(revenue: pd.Series) -> pd.Series:
    """reva_194_rev_growth_21_accel_126d"""
    return (revenue.pct_change(21)).diff(126).diff(21)

def reva_195_rev_growth_21_accel_252d(revenue: pd.Series) -> pd.Series:
    """reva_195_rev_growth_21_accel_252d"""
    return (revenue.pct_change(21)).diff(252).diff(21)

def reva_196_rev_growth_5_accel_5d(revenue: pd.Series) -> pd.Series:
    """reva_196_rev_growth_5_accel_5d"""
    return (revenue.pct_change(5)).diff(5).diff(21)

def reva_197_rev_growth_5_accel_21d(revenue: pd.Series) -> pd.Series:
    """reva_197_rev_growth_5_accel_21d"""
    return (revenue.pct_change(5)).diff(21).diff(21)

def reva_198_rev_growth_5_accel_63d(revenue: pd.Series) -> pd.Series:
    """reva_198_rev_growth_5_accel_63d"""
    return (revenue.pct_change(5)).diff(63).diff(21)

def reva_199_rev_growth_5_accel_126d(revenue: pd.Series) -> pd.Series:
    """reva_199_rev_growth_5_accel_126d"""
    return (revenue.pct_change(5)).diff(126).diff(21)

def reva_200_rev_growth_5_accel_252d(revenue: pd.Series) -> pd.Series:
    """reva_200_rev_growth_5_accel_252d"""
    return (revenue.pct_change(5)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V53_REGISTRY_ACCEL = {
    "reva_176_rev_growth_252_accel_5d": {"inputs": ["revenue"], "func": reva_176_rev_growth_252_accel_5d},
    "reva_177_rev_growth_252_accel_21d": {"inputs": ["revenue"], "func": reva_177_rev_growth_252_accel_21d},
    "reva_178_rev_growth_252_accel_63d": {"inputs": ["revenue"], "func": reva_178_rev_growth_252_accel_63d},
    "reva_179_rev_growth_252_accel_126d": {"inputs": ["revenue"], "func": reva_179_rev_growth_252_accel_126d},
    "reva_180_rev_growth_252_accel_252d": {"inputs": ["revenue"], "func": reva_180_rev_growth_252_accel_252d},
    "reva_181_rev_growth_126_accel_5d": {"inputs": ["revenue"], "func": reva_181_rev_growth_126_accel_5d},
    "reva_182_rev_growth_126_accel_21d": {"inputs": ["revenue"], "func": reva_182_rev_growth_126_accel_21d},
    "reva_183_rev_growth_126_accel_63d": {"inputs": ["revenue"], "func": reva_183_rev_growth_126_accel_63d},
    "reva_184_rev_growth_126_accel_126d": {"inputs": ["revenue"], "func": reva_184_rev_growth_126_accel_126d},
    "reva_185_rev_growth_126_accel_252d": {"inputs": ["revenue"], "func": reva_185_rev_growth_126_accel_252d},
    "reva_186_rev_growth_63_accel_5d": {"inputs": ["revenue"], "func": reva_186_rev_growth_63_accel_5d},
    "reva_187_rev_growth_63_accel_21d": {"inputs": ["revenue"], "func": reva_187_rev_growth_63_accel_21d},
    "reva_188_rev_growth_63_accel_63d": {"inputs": ["revenue"], "func": reva_188_rev_growth_63_accel_63d},
    "reva_189_rev_growth_63_accel_126d": {"inputs": ["revenue"], "func": reva_189_rev_growth_63_accel_126d},
    "reva_190_rev_growth_63_accel_252d": {"inputs": ["revenue"], "func": reva_190_rev_growth_63_accel_252d},
    "reva_191_rev_growth_21_accel_5d": {"inputs": ["revenue"], "func": reva_191_rev_growth_21_accel_5d},
    "reva_192_rev_growth_21_accel_21d": {"inputs": ["revenue"], "func": reva_192_rev_growth_21_accel_21d},
    "reva_193_rev_growth_21_accel_63d": {"inputs": ["revenue"], "func": reva_193_rev_growth_21_accel_63d},
    "reva_194_rev_growth_21_accel_126d": {"inputs": ["revenue"], "func": reva_194_rev_growth_21_accel_126d},
    "reva_195_rev_growth_21_accel_252d": {"inputs": ["revenue"], "func": reva_195_rev_growth_21_accel_252d},
    "reva_196_rev_growth_5_accel_5d": {"inputs": ["revenue"], "func": reva_196_rev_growth_5_accel_5d},
    "reva_197_rev_growth_5_accel_21d": {"inputs": ["revenue"], "func": reva_197_rev_growth_5_accel_21d},
    "reva_198_rev_growth_5_accel_63d": {"inputs": ["revenue"], "func": reva_198_rev_growth_5_accel_63d},
    "reva_199_rev_growth_5_accel_126d": {"inputs": ["revenue"], "func": reva_199_rev_growth_5_accel_126d},
    "reva_200_rev_growth_5_accel_252d": {"inputs": ["revenue"], "func": reva_200_rev_growth_5_accel_252d},
}
