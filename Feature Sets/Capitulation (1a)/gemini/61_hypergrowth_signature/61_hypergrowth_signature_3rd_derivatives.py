"""
61_hypergrowth_signature — 3rd Derivatives
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

def hygr_176_rev_g_acc_5d(revenue: pd.Series) -> pd.Series:
    """hygr_176_rev_g_acc_5d"""
    return (revenue.pct_change(252).diff(63).diff(21)).shift(5)

def hygr_177_rev_g_acc_21d(revenue: pd.Series) -> pd.Series:
    """hygr_177_rev_g_acc_21d"""
    return (revenue.pct_change(252).diff(63).diff(21)).shift(21)

def hygr_178_rev_g_acc_63d(revenue: pd.Series) -> pd.Series:
    """hygr_178_rev_g_acc_63d"""
    return (revenue.pct_change(252).diff(63).diff(21)).shift(63)

def hygr_179_rev_g_acc_126d(revenue: pd.Series) -> pd.Series:
    """hygr_179_rev_g_acc_126d"""
    return (revenue.pct_change(252).diff(63).diff(21)).shift(126)

def hygr_180_rev_g_acc_252d(revenue: pd.Series) -> pd.Series:
    """hygr_180_rev_g_acc_252d"""
    return (revenue.pct_change(252).diff(63).diff(21)).shift(252)

def hygr_181_rule40_acc_5d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_181_rule40_acc_5d"""
    return ((_safe_div(ebitda, revenue) + revenue.pct_change(252)).diff(63).diff(21)).shift(5)

def hygr_182_rule40_acc_21d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_182_rule40_acc_21d"""
    return ((_safe_div(ebitda, revenue) + revenue.pct_change(252)).diff(63).diff(21)).shift(21)

def hygr_183_rule40_acc_63d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_183_rule40_acc_63d"""
    return ((_safe_div(ebitda, revenue) + revenue.pct_change(252)).diff(63).diff(21)).shift(63)

def hygr_184_rule40_acc_126d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_184_rule40_acc_126d"""
    return ((_safe_div(ebitda, revenue) + revenue.pct_change(252)).diff(63).diff(21)).shift(126)

def hygr_185_rule40_acc_252d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_185_rule40_acc_252d"""
    return ((_safe_div(ebitda, revenue) + revenue.pct_change(252)).diff(63).diff(21)).shift(252)

def hygr_186_ps_acc_5d(ps: pd.Series) -> pd.Series:
    """hygr_186_ps_acc_5d"""
    return (ps.pct_change(63).diff(21)).shift(5)

def hygr_187_ps_acc_21d(ps: pd.Series) -> pd.Series:
    """hygr_187_ps_acc_21d"""
    return (ps.pct_change(63).diff(21)).shift(21)

def hygr_188_ps_acc_63d(ps: pd.Series) -> pd.Series:
    """hygr_188_ps_acc_63d"""
    return (ps.pct_change(63).diff(21)).shift(63)

def hygr_189_ps_acc_126d(ps: pd.Series) -> pd.Series:
    """hygr_189_ps_acc_126d"""
    return (ps.pct_change(63).diff(21)).shift(126)

def hygr_190_ps_acc_252d(ps: pd.Series) -> pd.Series:
    """hygr_190_ps_acc_252d"""
    return (ps.pct_change(63).diff(21)).shift(252)

def hygr_191_margin_acc_5d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_191_margin_acc_5d"""
    return ((_safe_div(ebitda, revenue)).diff(63).diff(21)).shift(5)

def hygr_192_margin_acc_21d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_192_margin_acc_21d"""
    return ((_safe_div(ebitda, revenue)).diff(63).diff(21)).shift(21)

def hygr_193_margin_acc_63d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_193_margin_acc_63d"""
    return ((_safe_div(ebitda, revenue)).diff(63).diff(21)).shift(63)

def hygr_194_margin_acc_126d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_194_margin_acc_126d"""
    return ((_safe_div(ebitda, revenue)).diff(63).diff(21)).shift(126)

def hygr_195_margin_acc_252d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_195_margin_acc_252d"""
    return ((_safe_div(ebitda, revenue)).diff(63).diff(21)).shift(252)

def hygr_196_rps_acc_5d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_196_rps_acc_5d"""
    return ((_safe_div(revenue, shareswa)).pct_change(63).diff(21)).shift(5)

def hygr_197_rps_acc_21d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_197_rps_acc_21d"""
    return ((_safe_div(revenue, shareswa)).pct_change(63).diff(21)).shift(21)

def hygr_198_rps_acc_63d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_198_rps_acc_63d"""
    return ((_safe_div(revenue, shareswa)).pct_change(63).diff(21)).shift(63)

def hygr_199_rps_acc_126d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_199_rps_acc_126d"""
    return ((_safe_div(revenue, shareswa)).pct_change(63).diff(21)).shift(126)

def hygr_200_rps_acc_252d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_200_rps_acc_252d"""
    return ((_safe_div(revenue, shareswa)).pct_change(63).diff(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V61_REGISTRY_3RD = {
    "hygr_176_rev_g_acc_5d": {"inputs": ['revenue'], "func": hygr_176_rev_g_acc_5d},
    "hygr_177_rev_g_acc_21d": {"inputs": ['revenue'], "func": hygr_177_rev_g_acc_21d},
    "hygr_178_rev_g_acc_63d": {"inputs": ['revenue'], "func": hygr_178_rev_g_acc_63d},
    "hygr_179_rev_g_acc_126d": {"inputs": ['revenue'], "func": hygr_179_rev_g_acc_126d},
    "hygr_180_rev_g_acc_252d": {"inputs": ['revenue'], "func": hygr_180_rev_g_acc_252d},
    "hygr_181_rule40_acc_5d": {"inputs": ['revenue', 'ebitda'], "func": hygr_181_rule40_acc_5d},
    "hygr_182_rule40_acc_21d": {"inputs": ['revenue', 'ebitda'], "func": hygr_182_rule40_acc_21d},
    "hygr_183_rule40_acc_63d": {"inputs": ['revenue', 'ebitda'], "func": hygr_183_rule40_acc_63d},
    "hygr_184_rule40_acc_126d": {"inputs": ['revenue', 'ebitda'], "func": hygr_184_rule40_acc_126d},
    "hygr_185_rule40_acc_252d": {"inputs": ['revenue', 'ebitda'], "func": hygr_185_rule40_acc_252d},
    "hygr_186_ps_acc_5d": {"inputs": ['ps'], "func": hygr_186_ps_acc_5d},
    "hygr_187_ps_acc_21d": {"inputs": ['ps'], "func": hygr_187_ps_acc_21d},
    "hygr_188_ps_acc_63d": {"inputs": ['ps'], "func": hygr_188_ps_acc_63d},
    "hygr_189_ps_acc_126d": {"inputs": ['ps'], "func": hygr_189_ps_acc_126d},
    "hygr_190_ps_acc_252d": {"inputs": ['ps'], "func": hygr_190_ps_acc_252d},
    "hygr_191_margin_acc_5d": {"inputs": ['revenue', 'ebitda'], "func": hygr_191_margin_acc_5d},
    "hygr_192_margin_acc_21d": {"inputs": ['revenue', 'ebitda'], "func": hygr_192_margin_acc_21d},
    "hygr_193_margin_acc_63d": {"inputs": ['revenue', 'ebitda'], "func": hygr_193_margin_acc_63d},
    "hygr_194_margin_acc_126d": {"inputs": ['revenue', 'ebitda'], "func": hygr_194_margin_acc_126d},
    "hygr_195_margin_acc_252d": {"inputs": ['revenue', 'ebitda'], "func": hygr_195_margin_acc_252d},
    "hygr_196_rps_acc_5d": {"inputs": ['revenue', 'shareswa'], "func": hygr_196_rps_acc_5d},
    "hygr_197_rps_acc_21d": {"inputs": ['revenue', 'shareswa'], "func": hygr_197_rps_acc_21d},
    "hygr_198_rps_acc_63d": {"inputs": ['revenue', 'shareswa'], "func": hygr_198_rps_acc_63d},
    "hygr_199_rps_acc_126d": {"inputs": ['revenue', 'shareswa'], "func": hygr_199_rps_acc_126d},
    "hygr_200_rps_acc_252d": {"inputs": ['revenue', 'shareswa'], "func": hygr_200_rps_acc_252d},
}
