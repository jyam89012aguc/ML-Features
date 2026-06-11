"""
61_hypergrowth_signature — 2nd Derivatives
Domain: High RevG + High Multiples persistence
Asset class: US equities | Daily SF1 Fundamentals
Target context: capitulation
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd
from typing import Dict, Any

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────
def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, np.nan)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).std()

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w); sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)

# ── Feature functions ────────────────────────────────────────────────────────

def hygr_151_rev_g_vel_5d(revenue: pd.Series) -> pd.Series:
    """hygr_151_rev_g_vel_5d"""
    return (revenue.pct_change(252).diff(21)).shift(5)

def hygr_152_rev_g_vel_21d(revenue: pd.Series) -> pd.Series:
    """hygr_152_rev_g_vel_21d"""
    return (revenue.pct_change(252).diff(21)).shift(21)

def hygr_153_rev_g_vel_63d(revenue: pd.Series) -> pd.Series:
    """hygr_153_rev_g_vel_63d"""
    return (revenue.pct_change(252).diff(21)).shift(63)

def hygr_154_rev_g_vel_126d(revenue: pd.Series) -> pd.Series:
    """hygr_154_rev_g_vel_126d"""
    return (revenue.pct_change(252).diff(21)).shift(126)

def hygr_155_rev_g_vel_252d(revenue: pd.Series) -> pd.Series:
    """hygr_155_rev_g_vel_252d"""
    return (revenue.pct_change(252).diff(21)).shift(252)

def hygr_156_rule40_vel_5d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_156_rule40_vel_5d"""
    return ((_safe_div(ebitda, revenue) + revenue.pct_change(252)).diff(21)).shift(5)

def hygr_157_rule40_vel_21d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_157_rule40_vel_21d"""
    return ((_safe_div(ebitda, revenue) + revenue.pct_change(252)).diff(21)).shift(21)

def hygr_158_rule40_vel_63d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_158_rule40_vel_63d"""
    return ((_safe_div(ebitda, revenue) + revenue.pct_change(252)).diff(21)).shift(63)

def hygr_159_rule40_vel_126d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_159_rule40_vel_126d"""
    return ((_safe_div(ebitda, revenue) + revenue.pct_change(252)).diff(21)).shift(126)

def hygr_160_rule40_vel_252d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_160_rule40_vel_252d"""
    return ((_safe_div(ebitda, revenue) + revenue.pct_change(252)).diff(21)).shift(252)

def hygr_161_ps_vel_5d(ps: pd.Series) -> pd.Series:
    """hygr_161_ps_vel_5d"""
    return (ps.pct_change(21)).shift(5)

def hygr_162_ps_vel_21d(ps: pd.Series) -> pd.Series:
    """hygr_162_ps_vel_21d"""
    return (ps.pct_change(21)).shift(21)

def hygr_163_ps_vel_63d(ps: pd.Series) -> pd.Series:
    """hygr_163_ps_vel_63d"""
    return (ps.pct_change(21)).shift(63)

def hygr_164_ps_vel_126d(ps: pd.Series) -> pd.Series:
    """hygr_164_ps_vel_126d"""
    return (ps.pct_change(21)).shift(126)

def hygr_165_ps_vel_252d(ps: pd.Series) -> pd.Series:
    """hygr_165_ps_vel_252d"""
    return (ps.pct_change(21)).shift(252)

def hygr_166_margin_vel_5d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_166_margin_vel_5d"""
    return ((_safe_div(ebitda, revenue)).diff(21)).shift(5)

def hygr_167_margin_vel_21d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_167_margin_vel_21d"""
    return ((_safe_div(ebitda, revenue)).diff(21)).shift(21)

def hygr_168_margin_vel_63d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_168_margin_vel_63d"""
    return ((_safe_div(ebitda, revenue)).diff(21)).shift(63)

def hygr_169_margin_vel_126d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_169_margin_vel_126d"""
    return ((_safe_div(ebitda, revenue)).diff(21)).shift(126)

def hygr_170_margin_vel_252d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_170_margin_vel_252d"""
    return ((_safe_div(ebitda, revenue)).diff(21)).shift(252)

def hygr_171_rps_vel_5d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_171_rps_vel_5d"""
    return ((_safe_div(revenue, shareswa)).pct_change(21)).shift(5)

def hygr_172_rps_vel_21d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_172_rps_vel_21d"""
    return ((_safe_div(revenue, shareswa)).pct_change(21)).shift(21)

def hygr_173_rps_vel_63d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_173_rps_vel_63d"""
    return ((_safe_div(revenue, shareswa)).pct_change(21)).shift(63)

def hygr_174_rps_vel_126d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_174_rps_vel_126d"""
    return ((_safe_div(revenue, shareswa)).pct_change(21)).shift(126)

def hygr_175_rps_vel_252d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_175_rps_vel_252d"""
    return ((_safe_div(revenue, shareswa)).pct_change(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V61_REGISTRY_2ND = {
    "hygr_151_rev_g_vel_5d": {"inputs": ['revenue'], "func": hygr_151_rev_g_vel_5d},
    "hygr_152_rev_g_vel_21d": {"inputs": ['revenue'], "func": hygr_152_rev_g_vel_21d},
    "hygr_153_rev_g_vel_63d": {"inputs": ['revenue'], "func": hygr_153_rev_g_vel_63d},
    "hygr_154_rev_g_vel_126d": {"inputs": ['revenue'], "func": hygr_154_rev_g_vel_126d},
    "hygr_155_rev_g_vel_252d": {"inputs": ['revenue'], "func": hygr_155_rev_g_vel_252d},
    "hygr_156_rule40_vel_5d": {"inputs": ['revenue', 'ebitda'], "func": hygr_156_rule40_vel_5d},
    "hygr_157_rule40_vel_21d": {"inputs": ['revenue', 'ebitda'], "func": hygr_157_rule40_vel_21d},
    "hygr_158_rule40_vel_63d": {"inputs": ['revenue', 'ebitda'], "func": hygr_158_rule40_vel_63d},
    "hygr_159_rule40_vel_126d": {"inputs": ['revenue', 'ebitda'], "func": hygr_159_rule40_vel_126d},
    "hygr_160_rule40_vel_252d": {"inputs": ['revenue', 'ebitda'], "func": hygr_160_rule40_vel_252d},
    "hygr_161_ps_vel_5d": {"inputs": ['ps'], "func": hygr_161_ps_vel_5d},
    "hygr_162_ps_vel_21d": {"inputs": ['ps'], "func": hygr_162_ps_vel_21d},
    "hygr_163_ps_vel_63d": {"inputs": ['ps'], "func": hygr_163_ps_vel_63d},
    "hygr_164_ps_vel_126d": {"inputs": ['ps'], "func": hygr_164_ps_vel_126d},
    "hygr_165_ps_vel_252d": {"inputs": ['ps'], "func": hygr_165_ps_vel_252d},
    "hygr_166_margin_vel_5d": {"inputs": ['revenue', 'ebitda'], "func": hygr_166_margin_vel_5d},
    "hygr_167_margin_vel_21d": {"inputs": ['revenue', 'ebitda'], "func": hygr_167_margin_vel_21d},
    "hygr_168_margin_vel_63d": {"inputs": ['revenue', 'ebitda'], "func": hygr_168_margin_vel_63d},
    "hygr_169_margin_vel_126d": {"inputs": ['revenue', 'ebitda'], "func": hygr_169_margin_vel_126d},
    "hygr_170_margin_vel_252d": {"inputs": ['revenue', 'ebitda'], "func": hygr_170_margin_vel_252d},
    "hygr_171_rps_vel_5d": {"inputs": ['revenue', 'shareswa'], "func": hygr_171_rps_vel_5d},
    "hygr_172_rps_vel_21d": {"inputs": ['revenue', 'shareswa'], "func": hygr_172_rps_vel_21d},
    "hygr_173_rps_vel_63d": {"inputs": ['revenue', 'shareswa'], "func": hygr_173_rps_vel_63d},
    "hygr_174_rps_vel_126d": {"inputs": ['revenue', 'shareswa'], "func": hygr_174_rps_vel_126d},
    "hygr_175_rps_vel_252d": {"inputs": ['revenue', 'shareswa'], "func": hygr_175_rps_vel_252d},
}
