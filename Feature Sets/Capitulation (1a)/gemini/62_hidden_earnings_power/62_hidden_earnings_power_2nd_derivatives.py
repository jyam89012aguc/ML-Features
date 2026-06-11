"""
62_hidden_earnings_power — 2nd Derivatives
Domain: OpInc vs NetInc divergence, tax rate anomalies
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

def herp_151_margin_div_vel_5d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_151_margin_div_vel_5d"""
    return ((_safe_div(ebit, revenue) - _safe_div(netinc, revenue)).diff(21)).shift(5)

def herp_152_margin_div_vel_21d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_152_margin_div_vel_21d"""
    return ((_safe_div(ebit, revenue) - _safe_div(netinc, revenue)).diff(21)).shift(21)

def herp_153_margin_div_vel_63d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_153_margin_div_vel_63d"""
    return ((_safe_div(ebit, revenue) - _safe_div(netinc, revenue)).diff(21)).shift(63)

def herp_154_margin_div_vel_126d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_154_margin_div_vel_126d"""
    return ((_safe_div(ebit, revenue) - _safe_div(netinc, revenue)).diff(21)).shift(126)

def herp_155_margin_div_vel_252d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_155_margin_div_vel_252d"""
    return ((_safe_div(ebit, revenue) - _safe_div(netinc, revenue)).diff(21)).shift(252)

def herp_156_tax_vel_5d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_156_tax_vel_5d"""
    return ((_safe_div(taxexp, ebt)).diff(21)).shift(5)

def herp_157_tax_vel_21d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_157_tax_vel_21d"""
    return ((_safe_div(taxexp, ebt)).diff(21)).shift(21)

def herp_158_tax_vel_63d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_158_tax_vel_63d"""
    return ((_safe_div(taxexp, ebt)).diff(21)).shift(63)

def herp_159_tax_vel_126d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_159_tax_vel_126d"""
    return ((_safe_div(taxexp, ebt)).diff(21)).shift(126)

def herp_160_tax_vel_252d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_160_tax_vel_252d"""
    return ((_safe_div(taxexp, ebt)).diff(21)).shift(252)

def herp_161_op_eff_vel_5d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """herp_161_op_eff_vel_5d"""
    return ((_safe_div(revenue, sga)).pct_change(21)).shift(5)

def herp_162_op_eff_vel_21d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """herp_162_op_eff_vel_21d"""
    return ((_safe_div(revenue, sga)).pct_change(21)).shift(21)

def herp_163_op_eff_vel_63d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """herp_163_op_eff_vel_63d"""
    return ((_safe_div(revenue, sga)).pct_change(21)).shift(63)

def herp_164_op_eff_vel_126d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """herp_164_op_eff_vel_126d"""
    return ((_safe_div(revenue, sga)).pct_change(21)).shift(126)

def herp_165_op_eff_vel_252d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """herp_165_op_eff_vel_252d"""
    return ((_safe_div(revenue, sga)).pct_change(21)).shift(252)

def herp_166_ni_vel_5d(netinc: pd.Series) -> pd.Series:
    """herp_166_ni_vel_5d"""
    return (netinc.pct_change(21)).shift(5)

def herp_167_ni_vel_21d(netinc: pd.Series) -> pd.Series:
    """herp_167_ni_vel_21d"""
    return (netinc.pct_change(21)).shift(21)

def herp_168_ni_vel_63d(netinc: pd.Series) -> pd.Series:
    """herp_168_ni_vel_63d"""
    return (netinc.pct_change(21)).shift(63)

def herp_169_ni_vel_126d(netinc: pd.Series) -> pd.Series:
    """herp_169_ni_vel_126d"""
    return (netinc.pct_change(21)).shift(126)

def herp_170_ni_vel_252d(netinc: pd.Series) -> pd.Series:
    """herp_170_ni_vel_252d"""
    return (netinc.pct_change(21)).shift(252)

def herp_171_ebit_vel_5d(ebit: pd.Series) -> pd.Series:
    """herp_171_ebit_vel_5d"""
    return (ebit.pct_change(21)).shift(5)

def herp_172_ebit_vel_21d(ebit: pd.Series) -> pd.Series:
    """herp_172_ebit_vel_21d"""
    return (ebit.pct_change(21)).shift(21)

def herp_173_ebit_vel_63d(ebit: pd.Series) -> pd.Series:
    """herp_173_ebit_vel_63d"""
    return (ebit.pct_change(21)).shift(63)

def herp_174_ebit_vel_126d(ebit: pd.Series) -> pd.Series:
    """herp_174_ebit_vel_126d"""
    return (ebit.pct_change(21)).shift(126)

def herp_175_ebit_vel_252d(ebit: pd.Series) -> pd.Series:
    """herp_175_ebit_vel_252d"""
    return (ebit.pct_change(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V62_REGISTRY_2ND = {
    "herp_151_margin_div_vel_5d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_151_margin_div_vel_5d},
    "herp_152_margin_div_vel_21d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_152_margin_div_vel_21d},
    "herp_153_margin_div_vel_63d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_153_margin_div_vel_63d},
    "herp_154_margin_div_vel_126d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_154_margin_div_vel_126d},
    "herp_155_margin_div_vel_252d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_155_margin_div_vel_252d},
    "herp_156_tax_vel_5d": {"inputs": ['taxexp', 'ebt'], "func": herp_156_tax_vel_5d},
    "herp_157_tax_vel_21d": {"inputs": ['taxexp', 'ebt'], "func": herp_157_tax_vel_21d},
    "herp_158_tax_vel_63d": {"inputs": ['taxexp', 'ebt'], "func": herp_158_tax_vel_63d},
    "herp_159_tax_vel_126d": {"inputs": ['taxexp', 'ebt'], "func": herp_159_tax_vel_126d},
    "herp_160_tax_vel_252d": {"inputs": ['taxexp', 'ebt'], "func": herp_160_tax_vel_252d},
    "herp_161_op_eff_vel_5d": {"inputs": ['revenue', 'sga'], "func": herp_161_op_eff_vel_5d},
    "herp_162_op_eff_vel_21d": {"inputs": ['revenue', 'sga'], "func": herp_162_op_eff_vel_21d},
    "herp_163_op_eff_vel_63d": {"inputs": ['revenue', 'sga'], "func": herp_163_op_eff_vel_63d},
    "herp_164_op_eff_vel_126d": {"inputs": ['revenue', 'sga'], "func": herp_164_op_eff_vel_126d},
    "herp_165_op_eff_vel_252d": {"inputs": ['revenue', 'sga'], "func": herp_165_op_eff_vel_252d},
    "herp_166_ni_vel_5d": {"inputs": ['netinc'], "func": herp_166_ni_vel_5d},
    "herp_167_ni_vel_21d": {"inputs": ['netinc'], "func": herp_167_ni_vel_21d},
    "herp_168_ni_vel_63d": {"inputs": ['netinc'], "func": herp_168_ni_vel_63d},
    "herp_169_ni_vel_126d": {"inputs": ['netinc'], "func": herp_169_ni_vel_126d},
    "herp_170_ni_vel_252d": {"inputs": ['netinc'], "func": herp_170_ni_vel_252d},
    "herp_171_ebit_vel_5d": {"inputs": ['ebit'], "func": herp_171_ebit_vel_5d},
    "herp_172_ebit_vel_21d": {"inputs": ['ebit'], "func": herp_172_ebit_vel_21d},
    "herp_173_ebit_vel_63d": {"inputs": ['ebit'], "func": herp_173_ebit_vel_63d},
    "herp_174_ebit_vel_126d": {"inputs": ['ebit'], "func": herp_174_ebit_vel_126d},
    "herp_175_ebit_vel_252d": {"inputs": ['ebit'], "func": herp_175_ebit_vel_252d},
}
