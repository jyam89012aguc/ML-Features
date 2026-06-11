"""
62_hidden_earnings_power — 3rd Derivatives
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

def herp_176_margin_div_acc_5d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_176_margin_div_acc_5d"""
    return ((_safe_div(ebit, revenue) - _safe_div(netinc, revenue)).diff(63).diff(21)).shift(5)

def herp_177_margin_div_acc_21d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_177_margin_div_acc_21d"""
    return ((_safe_div(ebit, revenue) - _safe_div(netinc, revenue)).diff(63).diff(21)).shift(21)

def herp_178_margin_div_acc_63d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_178_margin_div_acc_63d"""
    return ((_safe_div(ebit, revenue) - _safe_div(netinc, revenue)).diff(63).diff(21)).shift(63)

def herp_179_margin_div_acc_126d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_179_margin_div_acc_126d"""
    return ((_safe_div(ebit, revenue) - _safe_div(netinc, revenue)).diff(63).diff(21)).shift(126)

def herp_180_margin_div_acc_252d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_180_margin_div_acc_252d"""
    return ((_safe_div(ebit, revenue) - _safe_div(netinc, revenue)).diff(63).diff(21)).shift(252)

def herp_181_tax_acc_5d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_181_tax_acc_5d"""
    return ((_safe_div(taxexp, ebt)).diff(63).diff(21)).shift(5)

def herp_182_tax_acc_21d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_182_tax_acc_21d"""
    return ((_safe_div(taxexp, ebt)).diff(63).diff(21)).shift(21)

def herp_183_tax_acc_63d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_183_tax_acc_63d"""
    return ((_safe_div(taxexp, ebt)).diff(63).diff(21)).shift(63)

def herp_184_tax_acc_126d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_184_tax_acc_126d"""
    return ((_safe_div(taxexp, ebt)).diff(63).diff(21)).shift(126)

def herp_185_tax_acc_252d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_185_tax_acc_252d"""
    return ((_safe_div(taxexp, ebt)).diff(63).diff(21)).shift(252)

def herp_186_op_eff_acc_5d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """herp_186_op_eff_acc_5d"""
    return ((_safe_div(revenue, sga)).pct_change(63).diff(21)).shift(5)

def herp_187_op_eff_acc_21d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """herp_187_op_eff_acc_21d"""
    return ((_safe_div(revenue, sga)).pct_change(63).diff(21)).shift(21)

def herp_188_op_eff_acc_63d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """herp_188_op_eff_acc_63d"""
    return ((_safe_div(revenue, sga)).pct_change(63).diff(21)).shift(63)

def herp_189_op_eff_acc_126d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """herp_189_op_eff_acc_126d"""
    return ((_safe_div(revenue, sga)).pct_change(63).diff(21)).shift(126)

def herp_190_op_eff_acc_252d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """herp_190_op_eff_acc_252d"""
    return ((_safe_div(revenue, sga)).pct_change(63).diff(21)).shift(252)

def herp_191_ni_acc_5d(netinc: pd.Series) -> pd.Series:
    """herp_191_ni_acc_5d"""
    return (netinc.pct_change(63).diff(21)).shift(5)

def herp_192_ni_acc_21d(netinc: pd.Series) -> pd.Series:
    """herp_192_ni_acc_21d"""
    return (netinc.pct_change(63).diff(21)).shift(21)

def herp_193_ni_acc_63d(netinc: pd.Series) -> pd.Series:
    """herp_193_ni_acc_63d"""
    return (netinc.pct_change(63).diff(21)).shift(63)

def herp_194_ni_acc_126d(netinc: pd.Series) -> pd.Series:
    """herp_194_ni_acc_126d"""
    return (netinc.pct_change(63).diff(21)).shift(126)

def herp_195_ni_acc_252d(netinc: pd.Series) -> pd.Series:
    """herp_195_ni_acc_252d"""
    return (netinc.pct_change(63).diff(21)).shift(252)

def herp_196_ebit_acc_5d(ebit: pd.Series) -> pd.Series:
    """herp_196_ebit_acc_5d"""
    return (ebit.pct_change(63).diff(21)).shift(5)

def herp_197_ebit_acc_21d(ebit: pd.Series) -> pd.Series:
    """herp_197_ebit_acc_21d"""
    return (ebit.pct_change(63).diff(21)).shift(21)

def herp_198_ebit_acc_63d(ebit: pd.Series) -> pd.Series:
    """herp_198_ebit_acc_63d"""
    return (ebit.pct_change(63).diff(21)).shift(63)

def herp_199_ebit_acc_126d(ebit: pd.Series) -> pd.Series:
    """herp_199_ebit_acc_126d"""
    return (ebit.pct_change(63).diff(21)).shift(126)

def herp_200_ebit_acc_252d(ebit: pd.Series) -> pd.Series:
    """herp_200_ebit_acc_252d"""
    return (ebit.pct_change(63).diff(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V62_REGISTRY_3RD = {
    "herp_176_margin_div_acc_5d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_176_margin_div_acc_5d},
    "herp_177_margin_div_acc_21d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_177_margin_div_acc_21d},
    "herp_178_margin_div_acc_63d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_178_margin_div_acc_63d},
    "herp_179_margin_div_acc_126d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_179_margin_div_acc_126d},
    "herp_180_margin_div_acc_252d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_180_margin_div_acc_252d},
    "herp_181_tax_acc_5d": {"inputs": ['taxexp', 'ebt'], "func": herp_181_tax_acc_5d},
    "herp_182_tax_acc_21d": {"inputs": ['taxexp', 'ebt'], "func": herp_182_tax_acc_21d},
    "herp_183_tax_acc_63d": {"inputs": ['taxexp', 'ebt'], "func": herp_183_tax_acc_63d},
    "herp_184_tax_acc_126d": {"inputs": ['taxexp', 'ebt'], "func": herp_184_tax_acc_126d},
    "herp_185_tax_acc_252d": {"inputs": ['taxexp', 'ebt'], "func": herp_185_tax_acc_252d},
    "herp_186_op_eff_acc_5d": {"inputs": ['revenue', 'sga'], "func": herp_186_op_eff_acc_5d},
    "herp_187_op_eff_acc_21d": {"inputs": ['revenue', 'sga'], "func": herp_187_op_eff_acc_21d},
    "herp_188_op_eff_acc_63d": {"inputs": ['revenue', 'sga'], "func": herp_188_op_eff_acc_63d},
    "herp_189_op_eff_acc_126d": {"inputs": ['revenue', 'sga'], "func": herp_189_op_eff_acc_126d},
    "herp_190_op_eff_acc_252d": {"inputs": ['revenue', 'sga'], "func": herp_190_op_eff_acc_252d},
    "herp_191_ni_acc_5d": {"inputs": ['netinc'], "func": herp_191_ni_acc_5d},
    "herp_192_ni_acc_21d": {"inputs": ['netinc'], "func": herp_192_ni_acc_21d},
    "herp_193_ni_acc_63d": {"inputs": ['netinc'], "func": herp_193_ni_acc_63d},
    "herp_194_ni_acc_126d": {"inputs": ['netinc'], "func": herp_194_ni_acc_126d},
    "herp_195_ni_acc_252d": {"inputs": ['netinc'], "func": herp_195_ni_acc_252d},
    "herp_196_ebit_acc_5d": {"inputs": ['ebit'], "func": herp_196_ebit_acc_5d},
    "herp_197_ebit_acc_21d": {"inputs": ['ebit'], "func": herp_197_ebit_acc_21d},
    "herp_198_ebit_acc_63d": {"inputs": ['ebit'], "func": herp_198_ebit_acc_63d},
    "herp_199_ebit_acc_126d": {"inputs": ['ebit'], "func": herp_199_ebit_acc_126d},
    "herp_200_ebit_acc_252d": {"inputs": ['ebit'], "func": herp_200_ebit_acc_252d},
}
