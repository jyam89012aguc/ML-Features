"""
73_balance_sheet_death_spiral — 3rd Derivatives
Domain: Assets shrinking + Liabs growing
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

def bsds_176_dummy_acc_0_5d(revenue: pd.Series) -> pd.Series:
    """bsds_176_dummy_acc_0_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def bsds_177_dummy_acc_0_21d(revenue: pd.Series) -> pd.Series:
    """bsds_177_dummy_acc_0_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def bsds_178_dummy_acc_0_63d(revenue: pd.Series) -> pd.Series:
    """bsds_178_dummy_acc_0_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def bsds_179_dummy_acc_0_126d(revenue: pd.Series) -> pd.Series:
    """bsds_179_dummy_acc_0_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def bsds_180_dummy_acc_0_252d(revenue: pd.Series) -> pd.Series:
    """bsds_180_dummy_acc_0_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def bsds_181_dummy_acc_1_5d(revenue: pd.Series) -> pd.Series:
    """bsds_181_dummy_acc_1_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def bsds_182_dummy_acc_1_21d(revenue: pd.Series) -> pd.Series:
    """bsds_182_dummy_acc_1_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def bsds_183_dummy_acc_1_63d(revenue: pd.Series) -> pd.Series:
    """bsds_183_dummy_acc_1_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def bsds_184_dummy_acc_1_126d(revenue: pd.Series) -> pd.Series:
    """bsds_184_dummy_acc_1_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def bsds_185_dummy_acc_1_252d(revenue: pd.Series) -> pd.Series:
    """bsds_185_dummy_acc_1_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def bsds_186_dummy_acc_2_5d(revenue: pd.Series) -> pd.Series:
    """bsds_186_dummy_acc_2_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def bsds_187_dummy_acc_2_21d(revenue: pd.Series) -> pd.Series:
    """bsds_187_dummy_acc_2_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def bsds_188_dummy_acc_2_63d(revenue: pd.Series) -> pd.Series:
    """bsds_188_dummy_acc_2_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def bsds_189_dummy_acc_2_126d(revenue: pd.Series) -> pd.Series:
    """bsds_189_dummy_acc_2_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def bsds_190_dummy_acc_2_252d(revenue: pd.Series) -> pd.Series:
    """bsds_190_dummy_acc_2_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def bsds_191_dummy_acc_3_5d(revenue: pd.Series) -> pd.Series:
    """bsds_191_dummy_acc_3_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def bsds_192_dummy_acc_3_21d(revenue: pd.Series) -> pd.Series:
    """bsds_192_dummy_acc_3_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def bsds_193_dummy_acc_3_63d(revenue: pd.Series) -> pd.Series:
    """bsds_193_dummy_acc_3_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def bsds_194_dummy_acc_3_126d(revenue: pd.Series) -> pd.Series:
    """bsds_194_dummy_acc_3_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def bsds_195_dummy_acc_3_252d(revenue: pd.Series) -> pd.Series:
    """bsds_195_dummy_acc_3_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def bsds_196_dummy_acc_4_5d(revenue: pd.Series) -> pd.Series:
    """bsds_196_dummy_acc_4_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def bsds_197_dummy_acc_4_21d(revenue: pd.Series) -> pd.Series:
    """bsds_197_dummy_acc_4_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def bsds_198_dummy_acc_4_63d(revenue: pd.Series) -> pd.Series:
    """bsds_198_dummy_acc_4_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def bsds_199_dummy_acc_4_126d(revenue: pd.Series) -> pd.Series:
    """bsds_199_dummy_acc_4_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def bsds_200_dummy_acc_4_252d(revenue: pd.Series) -> pd.Series:
    """bsds_200_dummy_acc_4_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V73_REGISTRY_3RD = {
    "bsds_176_dummy_acc_0_5d": {"inputs": ['revenue'], "func": bsds_176_dummy_acc_0_5d},
    "bsds_177_dummy_acc_0_21d": {"inputs": ['revenue'], "func": bsds_177_dummy_acc_0_21d},
    "bsds_178_dummy_acc_0_63d": {"inputs": ['revenue'], "func": bsds_178_dummy_acc_0_63d},
    "bsds_179_dummy_acc_0_126d": {"inputs": ['revenue'], "func": bsds_179_dummy_acc_0_126d},
    "bsds_180_dummy_acc_0_252d": {"inputs": ['revenue'], "func": bsds_180_dummy_acc_0_252d},
    "bsds_181_dummy_acc_1_5d": {"inputs": ['revenue'], "func": bsds_181_dummy_acc_1_5d},
    "bsds_182_dummy_acc_1_21d": {"inputs": ['revenue'], "func": bsds_182_dummy_acc_1_21d},
    "bsds_183_dummy_acc_1_63d": {"inputs": ['revenue'], "func": bsds_183_dummy_acc_1_63d},
    "bsds_184_dummy_acc_1_126d": {"inputs": ['revenue'], "func": bsds_184_dummy_acc_1_126d},
    "bsds_185_dummy_acc_1_252d": {"inputs": ['revenue'], "func": bsds_185_dummy_acc_1_252d},
    "bsds_186_dummy_acc_2_5d": {"inputs": ['revenue'], "func": bsds_186_dummy_acc_2_5d},
    "bsds_187_dummy_acc_2_21d": {"inputs": ['revenue'], "func": bsds_187_dummy_acc_2_21d},
    "bsds_188_dummy_acc_2_63d": {"inputs": ['revenue'], "func": bsds_188_dummy_acc_2_63d},
    "bsds_189_dummy_acc_2_126d": {"inputs": ['revenue'], "func": bsds_189_dummy_acc_2_126d},
    "bsds_190_dummy_acc_2_252d": {"inputs": ['revenue'], "func": bsds_190_dummy_acc_2_252d},
    "bsds_191_dummy_acc_3_5d": {"inputs": ['revenue'], "func": bsds_191_dummy_acc_3_5d},
    "bsds_192_dummy_acc_3_21d": {"inputs": ['revenue'], "func": bsds_192_dummy_acc_3_21d},
    "bsds_193_dummy_acc_3_63d": {"inputs": ['revenue'], "func": bsds_193_dummy_acc_3_63d},
    "bsds_194_dummy_acc_3_126d": {"inputs": ['revenue'], "func": bsds_194_dummy_acc_3_126d},
    "bsds_195_dummy_acc_3_252d": {"inputs": ['revenue'], "func": bsds_195_dummy_acc_3_252d},
    "bsds_196_dummy_acc_4_5d": {"inputs": ['revenue'], "func": bsds_196_dummy_acc_4_5d},
    "bsds_197_dummy_acc_4_21d": {"inputs": ['revenue'], "func": bsds_197_dummy_acc_4_21d},
    "bsds_198_dummy_acc_4_63d": {"inputs": ['revenue'], "func": bsds_198_dummy_acc_4_63d},
    "bsds_199_dummy_acc_4_126d": {"inputs": ['revenue'], "func": bsds_199_dummy_acc_4_126d},
    "bsds_200_dummy_acc_4_252d": {"inputs": ['revenue'], "func": bsds_200_dummy_acc_4_252d},
}
