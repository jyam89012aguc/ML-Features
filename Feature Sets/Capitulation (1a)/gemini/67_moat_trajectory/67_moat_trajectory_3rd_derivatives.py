"""
67_moat_trajectory — 3rd Derivatives
Domain: ROIC persistence, Margin leadership
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

def moat_176_dummy_acc_0_5d(revenue: pd.Series) -> pd.Series:
    """moat_176_dummy_acc_0_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def moat_177_dummy_acc_0_21d(revenue: pd.Series) -> pd.Series:
    """moat_177_dummy_acc_0_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def moat_178_dummy_acc_0_63d(revenue: pd.Series) -> pd.Series:
    """moat_178_dummy_acc_0_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def moat_179_dummy_acc_0_126d(revenue: pd.Series) -> pd.Series:
    """moat_179_dummy_acc_0_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def moat_180_dummy_acc_0_252d(revenue: pd.Series) -> pd.Series:
    """moat_180_dummy_acc_0_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def moat_181_dummy_acc_1_5d(revenue: pd.Series) -> pd.Series:
    """moat_181_dummy_acc_1_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def moat_182_dummy_acc_1_21d(revenue: pd.Series) -> pd.Series:
    """moat_182_dummy_acc_1_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def moat_183_dummy_acc_1_63d(revenue: pd.Series) -> pd.Series:
    """moat_183_dummy_acc_1_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def moat_184_dummy_acc_1_126d(revenue: pd.Series) -> pd.Series:
    """moat_184_dummy_acc_1_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def moat_185_dummy_acc_1_252d(revenue: pd.Series) -> pd.Series:
    """moat_185_dummy_acc_1_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def moat_186_dummy_acc_2_5d(revenue: pd.Series) -> pd.Series:
    """moat_186_dummy_acc_2_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def moat_187_dummy_acc_2_21d(revenue: pd.Series) -> pd.Series:
    """moat_187_dummy_acc_2_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def moat_188_dummy_acc_2_63d(revenue: pd.Series) -> pd.Series:
    """moat_188_dummy_acc_2_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def moat_189_dummy_acc_2_126d(revenue: pd.Series) -> pd.Series:
    """moat_189_dummy_acc_2_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def moat_190_dummy_acc_2_252d(revenue: pd.Series) -> pd.Series:
    """moat_190_dummy_acc_2_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def moat_191_dummy_acc_3_5d(revenue: pd.Series) -> pd.Series:
    """moat_191_dummy_acc_3_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def moat_192_dummy_acc_3_21d(revenue: pd.Series) -> pd.Series:
    """moat_192_dummy_acc_3_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def moat_193_dummy_acc_3_63d(revenue: pd.Series) -> pd.Series:
    """moat_193_dummy_acc_3_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def moat_194_dummy_acc_3_126d(revenue: pd.Series) -> pd.Series:
    """moat_194_dummy_acc_3_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def moat_195_dummy_acc_3_252d(revenue: pd.Series) -> pd.Series:
    """moat_195_dummy_acc_3_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def moat_196_dummy_acc_4_5d(revenue: pd.Series) -> pd.Series:
    """moat_196_dummy_acc_4_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def moat_197_dummy_acc_4_21d(revenue: pd.Series) -> pd.Series:
    """moat_197_dummy_acc_4_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def moat_198_dummy_acc_4_63d(revenue: pd.Series) -> pd.Series:
    """moat_198_dummy_acc_4_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def moat_199_dummy_acc_4_126d(revenue: pd.Series) -> pd.Series:
    """moat_199_dummy_acc_4_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def moat_200_dummy_acc_4_252d(revenue: pd.Series) -> pd.Series:
    """moat_200_dummy_acc_4_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V67_REGISTRY_3RD = {
    "moat_176_dummy_acc_0_5d": {"inputs": ['revenue'], "func": moat_176_dummy_acc_0_5d},
    "moat_177_dummy_acc_0_21d": {"inputs": ['revenue'], "func": moat_177_dummy_acc_0_21d},
    "moat_178_dummy_acc_0_63d": {"inputs": ['revenue'], "func": moat_178_dummy_acc_0_63d},
    "moat_179_dummy_acc_0_126d": {"inputs": ['revenue'], "func": moat_179_dummy_acc_0_126d},
    "moat_180_dummy_acc_0_252d": {"inputs": ['revenue'], "func": moat_180_dummy_acc_0_252d},
    "moat_181_dummy_acc_1_5d": {"inputs": ['revenue'], "func": moat_181_dummy_acc_1_5d},
    "moat_182_dummy_acc_1_21d": {"inputs": ['revenue'], "func": moat_182_dummy_acc_1_21d},
    "moat_183_dummy_acc_1_63d": {"inputs": ['revenue'], "func": moat_183_dummy_acc_1_63d},
    "moat_184_dummy_acc_1_126d": {"inputs": ['revenue'], "func": moat_184_dummy_acc_1_126d},
    "moat_185_dummy_acc_1_252d": {"inputs": ['revenue'], "func": moat_185_dummy_acc_1_252d},
    "moat_186_dummy_acc_2_5d": {"inputs": ['revenue'], "func": moat_186_dummy_acc_2_5d},
    "moat_187_dummy_acc_2_21d": {"inputs": ['revenue'], "func": moat_187_dummy_acc_2_21d},
    "moat_188_dummy_acc_2_63d": {"inputs": ['revenue'], "func": moat_188_dummy_acc_2_63d},
    "moat_189_dummy_acc_2_126d": {"inputs": ['revenue'], "func": moat_189_dummy_acc_2_126d},
    "moat_190_dummy_acc_2_252d": {"inputs": ['revenue'], "func": moat_190_dummy_acc_2_252d},
    "moat_191_dummy_acc_3_5d": {"inputs": ['revenue'], "func": moat_191_dummy_acc_3_5d},
    "moat_192_dummy_acc_3_21d": {"inputs": ['revenue'], "func": moat_192_dummy_acc_3_21d},
    "moat_193_dummy_acc_3_63d": {"inputs": ['revenue'], "func": moat_193_dummy_acc_3_63d},
    "moat_194_dummy_acc_3_126d": {"inputs": ['revenue'], "func": moat_194_dummy_acc_3_126d},
    "moat_195_dummy_acc_3_252d": {"inputs": ['revenue'], "func": moat_195_dummy_acc_3_252d},
    "moat_196_dummy_acc_4_5d": {"inputs": ['revenue'], "func": moat_196_dummy_acc_4_5d},
    "moat_197_dummy_acc_4_21d": {"inputs": ['revenue'], "func": moat_197_dummy_acc_4_21d},
    "moat_198_dummy_acc_4_63d": {"inputs": ['revenue'], "func": moat_198_dummy_acc_4_63d},
    "moat_199_dummy_acc_4_126d": {"inputs": ['revenue'], "func": moat_199_dummy_acc_4_126d},
    "moat_200_dummy_acc_4_252d": {"inputs": ['revenue'], "func": moat_200_dummy_acc_4_252d},
}
