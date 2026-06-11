"""
53_revenue_acceleration — 2nd Derivatives (Velocity)
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

def reva_151_rev_growth_252_vel_5d(revenue: pd.Series) -> pd.Series:
    """reva_151_rev_growth_252_vel_5d"""
    return (revenue.pct_change(252)).diff(5)

def reva_152_rev_growth_252_vel_21d(revenue: pd.Series) -> pd.Series:
    """reva_152_rev_growth_252_vel_21d"""
    return (revenue.pct_change(252)).diff(21)

def reva_153_rev_growth_252_vel_63d(revenue: pd.Series) -> pd.Series:
    """reva_153_rev_growth_252_vel_63d"""
    return (revenue.pct_change(252)).diff(63)

def reva_154_rev_growth_252_vel_126d(revenue: pd.Series) -> pd.Series:
    """reva_154_rev_growth_252_vel_126d"""
    return (revenue.pct_change(252)).diff(126)

def reva_155_rev_growth_252_vel_252d(revenue: pd.Series) -> pd.Series:
    """reva_155_rev_growth_252_vel_252d"""
    return (revenue.pct_change(252)).diff(252)

def reva_156_rev_growth_126_vel_5d(revenue: pd.Series) -> pd.Series:
    """reva_156_rev_growth_126_vel_5d"""
    return (revenue.pct_change(126)).diff(5)

def reva_157_rev_growth_126_vel_21d(revenue: pd.Series) -> pd.Series:
    """reva_157_rev_growth_126_vel_21d"""
    return (revenue.pct_change(126)).diff(21)

def reva_158_rev_growth_126_vel_63d(revenue: pd.Series) -> pd.Series:
    """reva_158_rev_growth_126_vel_63d"""
    return (revenue.pct_change(126)).diff(63)

def reva_159_rev_growth_126_vel_126d(revenue: pd.Series) -> pd.Series:
    """reva_159_rev_growth_126_vel_126d"""
    return (revenue.pct_change(126)).diff(126)

def reva_160_rev_growth_126_vel_252d(revenue: pd.Series) -> pd.Series:
    """reva_160_rev_growth_126_vel_252d"""
    return (revenue.pct_change(126)).diff(252)

def reva_161_rev_growth_63_vel_5d(revenue: pd.Series) -> pd.Series:
    """reva_161_rev_growth_63_vel_5d"""
    return (revenue.pct_change(63)).diff(5)

def reva_162_rev_growth_63_vel_21d(revenue: pd.Series) -> pd.Series:
    """reva_162_rev_growth_63_vel_21d"""
    return (revenue.pct_change(63)).diff(21)

def reva_163_rev_growth_63_vel_63d(revenue: pd.Series) -> pd.Series:
    """reva_163_rev_growth_63_vel_63d"""
    return (revenue.pct_change(63)).diff(63)

def reva_164_rev_growth_63_vel_126d(revenue: pd.Series) -> pd.Series:
    """reva_164_rev_growth_63_vel_126d"""
    return (revenue.pct_change(63)).diff(126)

def reva_165_rev_growth_63_vel_252d(revenue: pd.Series) -> pd.Series:
    """reva_165_rev_growth_63_vel_252d"""
    return (revenue.pct_change(63)).diff(252)

def reva_166_rev_growth_21_vel_5d(revenue: pd.Series) -> pd.Series:
    """reva_166_rev_growth_21_vel_5d"""
    return (revenue.pct_change(21)).diff(5)

def reva_167_rev_growth_21_vel_21d(revenue: pd.Series) -> pd.Series:
    """reva_167_rev_growth_21_vel_21d"""
    return (revenue.pct_change(21)).diff(21)

def reva_168_rev_growth_21_vel_63d(revenue: pd.Series) -> pd.Series:
    """reva_168_rev_growth_21_vel_63d"""
    return (revenue.pct_change(21)).diff(63)

def reva_169_rev_growth_21_vel_126d(revenue: pd.Series) -> pd.Series:
    """reva_169_rev_growth_21_vel_126d"""
    return (revenue.pct_change(21)).diff(126)

def reva_170_rev_growth_21_vel_252d(revenue: pd.Series) -> pd.Series:
    """reva_170_rev_growth_21_vel_252d"""
    return (revenue.pct_change(21)).diff(252)

def reva_171_rev_growth_5_vel_5d(revenue: pd.Series) -> pd.Series:
    """reva_171_rev_growth_5_vel_5d"""
    return (revenue.pct_change(5)).diff(5)

def reva_172_rev_growth_5_vel_21d(revenue: pd.Series) -> pd.Series:
    """reva_172_rev_growth_5_vel_21d"""
    return (revenue.pct_change(5)).diff(21)

def reva_173_rev_growth_5_vel_63d(revenue: pd.Series) -> pd.Series:
    """reva_173_rev_growth_5_vel_63d"""
    return (revenue.pct_change(5)).diff(63)

def reva_174_rev_growth_5_vel_126d(revenue: pd.Series) -> pd.Series:
    """reva_174_rev_growth_5_vel_126d"""
    return (revenue.pct_change(5)).diff(126)

def reva_175_rev_growth_5_vel_252d(revenue: pd.Series) -> pd.Series:
    """reva_175_rev_growth_5_vel_252d"""
    return (revenue.pct_change(5)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V53_REGISTRY_VEL = {
    "reva_151_rev_growth_252_vel_5d": {"inputs": ["revenue"], "func": reva_151_rev_growth_252_vel_5d},
    "reva_152_rev_growth_252_vel_21d": {"inputs": ["revenue"], "func": reva_152_rev_growth_252_vel_21d},
    "reva_153_rev_growth_252_vel_63d": {"inputs": ["revenue"], "func": reva_153_rev_growth_252_vel_63d},
    "reva_154_rev_growth_252_vel_126d": {"inputs": ["revenue"], "func": reva_154_rev_growth_252_vel_126d},
    "reva_155_rev_growth_252_vel_252d": {"inputs": ["revenue"], "func": reva_155_rev_growth_252_vel_252d},
    "reva_156_rev_growth_126_vel_5d": {"inputs": ["revenue"], "func": reva_156_rev_growth_126_vel_5d},
    "reva_157_rev_growth_126_vel_21d": {"inputs": ["revenue"], "func": reva_157_rev_growth_126_vel_21d},
    "reva_158_rev_growth_126_vel_63d": {"inputs": ["revenue"], "func": reva_158_rev_growth_126_vel_63d},
    "reva_159_rev_growth_126_vel_126d": {"inputs": ["revenue"], "func": reva_159_rev_growth_126_vel_126d},
    "reva_160_rev_growth_126_vel_252d": {"inputs": ["revenue"], "func": reva_160_rev_growth_126_vel_252d},
    "reva_161_rev_growth_63_vel_5d": {"inputs": ["revenue"], "func": reva_161_rev_growth_63_vel_5d},
    "reva_162_rev_growth_63_vel_21d": {"inputs": ["revenue"], "func": reva_162_rev_growth_63_vel_21d},
    "reva_163_rev_growth_63_vel_63d": {"inputs": ["revenue"], "func": reva_163_rev_growth_63_vel_63d},
    "reva_164_rev_growth_63_vel_126d": {"inputs": ["revenue"], "func": reva_164_rev_growth_63_vel_126d},
    "reva_165_rev_growth_63_vel_252d": {"inputs": ["revenue"], "func": reva_165_rev_growth_63_vel_252d},
    "reva_166_rev_growth_21_vel_5d": {"inputs": ["revenue"], "func": reva_166_rev_growth_21_vel_5d},
    "reva_167_rev_growth_21_vel_21d": {"inputs": ["revenue"], "func": reva_167_rev_growth_21_vel_21d},
    "reva_168_rev_growth_21_vel_63d": {"inputs": ["revenue"], "func": reva_168_rev_growth_21_vel_63d},
    "reva_169_rev_growth_21_vel_126d": {"inputs": ["revenue"], "func": reva_169_rev_growth_21_vel_126d},
    "reva_170_rev_growth_21_vel_252d": {"inputs": ["revenue"], "func": reva_170_rev_growth_21_vel_252d},
    "reva_171_rev_growth_5_vel_5d": {"inputs": ["revenue"], "func": reva_171_rev_growth_5_vel_5d},
    "reva_172_rev_growth_5_vel_21d": {"inputs": ["revenue"], "func": reva_172_rev_growth_5_vel_21d},
    "reva_173_rev_growth_5_vel_63d": {"inputs": ["revenue"], "func": reva_173_rev_growth_5_vel_63d},
    "reva_174_rev_growth_5_vel_126d": {"inputs": ["revenue"], "func": reva_174_rev_growth_5_vel_126d},
    "reva_175_rev_growth_5_vel_252d": {"inputs": ["revenue"], "func": reva_175_rev_growth_5_vel_252d},
}
