"""
70_accounting_manipulation — 3rd Derivatives
Domain: Beneish M-score proxies, Accruals/Assets
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

def acmn_176_dummy_acc_0_5d(revenue: pd.Series) -> pd.Series:
    """acmn_176_dummy_acc_0_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def acmn_177_dummy_acc_0_21d(revenue: pd.Series) -> pd.Series:
    """acmn_177_dummy_acc_0_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def acmn_178_dummy_acc_0_63d(revenue: pd.Series) -> pd.Series:
    """acmn_178_dummy_acc_0_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def acmn_179_dummy_acc_0_126d(revenue: pd.Series) -> pd.Series:
    """acmn_179_dummy_acc_0_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def acmn_180_dummy_acc_0_252d(revenue: pd.Series) -> pd.Series:
    """acmn_180_dummy_acc_0_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def acmn_181_dummy_acc_1_5d(revenue: pd.Series) -> pd.Series:
    """acmn_181_dummy_acc_1_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def acmn_182_dummy_acc_1_21d(revenue: pd.Series) -> pd.Series:
    """acmn_182_dummy_acc_1_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def acmn_183_dummy_acc_1_63d(revenue: pd.Series) -> pd.Series:
    """acmn_183_dummy_acc_1_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def acmn_184_dummy_acc_1_126d(revenue: pd.Series) -> pd.Series:
    """acmn_184_dummy_acc_1_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def acmn_185_dummy_acc_1_252d(revenue: pd.Series) -> pd.Series:
    """acmn_185_dummy_acc_1_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def acmn_186_dummy_acc_2_5d(revenue: pd.Series) -> pd.Series:
    """acmn_186_dummy_acc_2_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def acmn_187_dummy_acc_2_21d(revenue: pd.Series) -> pd.Series:
    """acmn_187_dummy_acc_2_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def acmn_188_dummy_acc_2_63d(revenue: pd.Series) -> pd.Series:
    """acmn_188_dummy_acc_2_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def acmn_189_dummy_acc_2_126d(revenue: pd.Series) -> pd.Series:
    """acmn_189_dummy_acc_2_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def acmn_190_dummy_acc_2_252d(revenue: pd.Series) -> pd.Series:
    """acmn_190_dummy_acc_2_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def acmn_191_dummy_acc_3_5d(revenue: pd.Series) -> pd.Series:
    """acmn_191_dummy_acc_3_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def acmn_192_dummy_acc_3_21d(revenue: pd.Series) -> pd.Series:
    """acmn_192_dummy_acc_3_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def acmn_193_dummy_acc_3_63d(revenue: pd.Series) -> pd.Series:
    """acmn_193_dummy_acc_3_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def acmn_194_dummy_acc_3_126d(revenue: pd.Series) -> pd.Series:
    """acmn_194_dummy_acc_3_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def acmn_195_dummy_acc_3_252d(revenue: pd.Series) -> pd.Series:
    """acmn_195_dummy_acc_3_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def acmn_196_dummy_acc_4_5d(revenue: pd.Series) -> pd.Series:
    """acmn_196_dummy_acc_4_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def acmn_197_dummy_acc_4_21d(revenue: pd.Series) -> pd.Series:
    """acmn_197_dummy_acc_4_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def acmn_198_dummy_acc_4_63d(revenue: pd.Series) -> pd.Series:
    """acmn_198_dummy_acc_4_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def acmn_199_dummy_acc_4_126d(revenue: pd.Series) -> pd.Series:
    """acmn_199_dummy_acc_4_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def acmn_200_dummy_acc_4_252d(revenue: pd.Series) -> pd.Series:
    """acmn_200_dummy_acc_4_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V70_REGISTRY_3RD = {
    "acmn_176_dummy_acc_0_5d": {"inputs": ['revenue'], "func": acmn_176_dummy_acc_0_5d},
    "acmn_177_dummy_acc_0_21d": {"inputs": ['revenue'], "func": acmn_177_dummy_acc_0_21d},
    "acmn_178_dummy_acc_0_63d": {"inputs": ['revenue'], "func": acmn_178_dummy_acc_0_63d},
    "acmn_179_dummy_acc_0_126d": {"inputs": ['revenue'], "func": acmn_179_dummy_acc_0_126d},
    "acmn_180_dummy_acc_0_252d": {"inputs": ['revenue'], "func": acmn_180_dummy_acc_0_252d},
    "acmn_181_dummy_acc_1_5d": {"inputs": ['revenue'], "func": acmn_181_dummy_acc_1_5d},
    "acmn_182_dummy_acc_1_21d": {"inputs": ['revenue'], "func": acmn_182_dummy_acc_1_21d},
    "acmn_183_dummy_acc_1_63d": {"inputs": ['revenue'], "func": acmn_183_dummy_acc_1_63d},
    "acmn_184_dummy_acc_1_126d": {"inputs": ['revenue'], "func": acmn_184_dummy_acc_1_126d},
    "acmn_185_dummy_acc_1_252d": {"inputs": ['revenue'], "func": acmn_185_dummy_acc_1_252d},
    "acmn_186_dummy_acc_2_5d": {"inputs": ['revenue'], "func": acmn_186_dummy_acc_2_5d},
    "acmn_187_dummy_acc_2_21d": {"inputs": ['revenue'], "func": acmn_187_dummy_acc_2_21d},
    "acmn_188_dummy_acc_2_63d": {"inputs": ['revenue'], "func": acmn_188_dummy_acc_2_63d},
    "acmn_189_dummy_acc_2_126d": {"inputs": ['revenue'], "func": acmn_189_dummy_acc_2_126d},
    "acmn_190_dummy_acc_2_252d": {"inputs": ['revenue'], "func": acmn_190_dummy_acc_2_252d},
    "acmn_191_dummy_acc_3_5d": {"inputs": ['revenue'], "func": acmn_191_dummy_acc_3_5d},
    "acmn_192_dummy_acc_3_21d": {"inputs": ['revenue'], "func": acmn_192_dummy_acc_3_21d},
    "acmn_193_dummy_acc_3_63d": {"inputs": ['revenue'], "func": acmn_193_dummy_acc_3_63d},
    "acmn_194_dummy_acc_3_126d": {"inputs": ['revenue'], "func": acmn_194_dummy_acc_3_126d},
    "acmn_195_dummy_acc_3_252d": {"inputs": ['revenue'], "func": acmn_195_dummy_acc_3_252d},
    "acmn_196_dummy_acc_4_5d": {"inputs": ['revenue'], "func": acmn_196_dummy_acc_4_5d},
    "acmn_197_dummy_acc_4_21d": {"inputs": ['revenue'], "func": acmn_197_dummy_acc_4_21d},
    "acmn_198_dummy_acc_4_63d": {"inputs": ['revenue'], "func": acmn_198_dummy_acc_4_63d},
    "acmn_199_dummy_acc_4_126d": {"inputs": ['revenue'], "func": acmn_199_dummy_acc_4_126d},
    "acmn_200_dummy_acc_4_252d": {"inputs": ['revenue'], "func": acmn_200_dummy_acc_4_252d},
}
