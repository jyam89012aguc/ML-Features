"""
72_cash_runway — 3rd Derivatives
Domain: Cash / Burn rate (OCF negative)
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

def runw_176_dummy_acc_0_5d(revenue: pd.Series) -> pd.Series:
    """runw_176_dummy_acc_0_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def runw_177_dummy_acc_0_21d(revenue: pd.Series) -> pd.Series:
    """runw_177_dummy_acc_0_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def runw_178_dummy_acc_0_63d(revenue: pd.Series) -> pd.Series:
    """runw_178_dummy_acc_0_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def runw_179_dummy_acc_0_126d(revenue: pd.Series) -> pd.Series:
    """runw_179_dummy_acc_0_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def runw_180_dummy_acc_0_252d(revenue: pd.Series) -> pd.Series:
    """runw_180_dummy_acc_0_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def runw_181_dummy_acc_1_5d(revenue: pd.Series) -> pd.Series:
    """runw_181_dummy_acc_1_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def runw_182_dummy_acc_1_21d(revenue: pd.Series) -> pd.Series:
    """runw_182_dummy_acc_1_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def runw_183_dummy_acc_1_63d(revenue: pd.Series) -> pd.Series:
    """runw_183_dummy_acc_1_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def runw_184_dummy_acc_1_126d(revenue: pd.Series) -> pd.Series:
    """runw_184_dummy_acc_1_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def runw_185_dummy_acc_1_252d(revenue: pd.Series) -> pd.Series:
    """runw_185_dummy_acc_1_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def runw_186_dummy_acc_2_5d(revenue: pd.Series) -> pd.Series:
    """runw_186_dummy_acc_2_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def runw_187_dummy_acc_2_21d(revenue: pd.Series) -> pd.Series:
    """runw_187_dummy_acc_2_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def runw_188_dummy_acc_2_63d(revenue: pd.Series) -> pd.Series:
    """runw_188_dummy_acc_2_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def runw_189_dummy_acc_2_126d(revenue: pd.Series) -> pd.Series:
    """runw_189_dummy_acc_2_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def runw_190_dummy_acc_2_252d(revenue: pd.Series) -> pd.Series:
    """runw_190_dummy_acc_2_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def runw_191_dummy_acc_3_5d(revenue: pd.Series) -> pd.Series:
    """runw_191_dummy_acc_3_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def runw_192_dummy_acc_3_21d(revenue: pd.Series) -> pd.Series:
    """runw_192_dummy_acc_3_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def runw_193_dummy_acc_3_63d(revenue: pd.Series) -> pd.Series:
    """runw_193_dummy_acc_3_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def runw_194_dummy_acc_3_126d(revenue: pd.Series) -> pd.Series:
    """runw_194_dummy_acc_3_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def runw_195_dummy_acc_3_252d(revenue: pd.Series) -> pd.Series:
    """runw_195_dummy_acc_3_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def runw_196_dummy_acc_4_5d(revenue: pd.Series) -> pd.Series:
    """runw_196_dummy_acc_4_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def runw_197_dummy_acc_4_21d(revenue: pd.Series) -> pd.Series:
    """runw_197_dummy_acc_4_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def runw_198_dummy_acc_4_63d(revenue: pd.Series) -> pd.Series:
    """runw_198_dummy_acc_4_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def runw_199_dummy_acc_4_126d(revenue: pd.Series) -> pd.Series:
    """runw_199_dummy_acc_4_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def runw_200_dummy_acc_4_252d(revenue: pd.Series) -> pd.Series:
    """runw_200_dummy_acc_4_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V72_REGISTRY_3RD = {
    "runw_176_dummy_acc_0_5d": {"inputs": ['revenue'], "func": runw_176_dummy_acc_0_5d},
    "runw_177_dummy_acc_0_21d": {"inputs": ['revenue'], "func": runw_177_dummy_acc_0_21d},
    "runw_178_dummy_acc_0_63d": {"inputs": ['revenue'], "func": runw_178_dummy_acc_0_63d},
    "runw_179_dummy_acc_0_126d": {"inputs": ['revenue'], "func": runw_179_dummy_acc_0_126d},
    "runw_180_dummy_acc_0_252d": {"inputs": ['revenue'], "func": runw_180_dummy_acc_0_252d},
    "runw_181_dummy_acc_1_5d": {"inputs": ['revenue'], "func": runw_181_dummy_acc_1_5d},
    "runw_182_dummy_acc_1_21d": {"inputs": ['revenue'], "func": runw_182_dummy_acc_1_21d},
    "runw_183_dummy_acc_1_63d": {"inputs": ['revenue'], "func": runw_183_dummy_acc_1_63d},
    "runw_184_dummy_acc_1_126d": {"inputs": ['revenue'], "func": runw_184_dummy_acc_1_126d},
    "runw_185_dummy_acc_1_252d": {"inputs": ['revenue'], "func": runw_185_dummy_acc_1_252d},
    "runw_186_dummy_acc_2_5d": {"inputs": ['revenue'], "func": runw_186_dummy_acc_2_5d},
    "runw_187_dummy_acc_2_21d": {"inputs": ['revenue'], "func": runw_187_dummy_acc_2_21d},
    "runw_188_dummy_acc_2_63d": {"inputs": ['revenue'], "func": runw_188_dummy_acc_2_63d},
    "runw_189_dummy_acc_2_126d": {"inputs": ['revenue'], "func": runw_189_dummy_acc_2_126d},
    "runw_190_dummy_acc_2_252d": {"inputs": ['revenue'], "func": runw_190_dummy_acc_2_252d},
    "runw_191_dummy_acc_3_5d": {"inputs": ['revenue'], "func": runw_191_dummy_acc_3_5d},
    "runw_192_dummy_acc_3_21d": {"inputs": ['revenue'], "func": runw_192_dummy_acc_3_21d},
    "runw_193_dummy_acc_3_63d": {"inputs": ['revenue'], "func": runw_193_dummy_acc_3_63d},
    "runw_194_dummy_acc_3_126d": {"inputs": ['revenue'], "func": runw_194_dummy_acc_3_126d},
    "runw_195_dummy_acc_3_252d": {"inputs": ['revenue'], "func": runw_195_dummy_acc_3_252d},
    "runw_196_dummy_acc_4_5d": {"inputs": ['revenue'], "func": runw_196_dummy_acc_4_5d},
    "runw_197_dummy_acc_4_21d": {"inputs": ['revenue'], "func": runw_197_dummy_acc_4_21d},
    "runw_198_dummy_acc_4_63d": {"inputs": ['revenue'], "func": runw_198_dummy_acc_4_63d},
    "runw_199_dummy_acc_4_126d": {"inputs": ['revenue'], "func": runw_199_dummy_acc_4_126d},
    "runw_200_dummy_acc_4_252d": {"inputs": ['revenue'], "func": runw_200_dummy_acc_4_252d},
}
