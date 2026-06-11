"""
71_fake_growth_detector — 3rd Derivatives
Domain: Debt-funded revenue growth signals
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

def fgrd_176_dummy_acc_0_5d(revenue: pd.Series) -> pd.Series:
    """fgrd_176_dummy_acc_0_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def fgrd_177_dummy_acc_0_21d(revenue: pd.Series) -> pd.Series:
    """fgrd_177_dummy_acc_0_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def fgrd_178_dummy_acc_0_63d(revenue: pd.Series) -> pd.Series:
    """fgrd_178_dummy_acc_0_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def fgrd_179_dummy_acc_0_126d(revenue: pd.Series) -> pd.Series:
    """fgrd_179_dummy_acc_0_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def fgrd_180_dummy_acc_0_252d(revenue: pd.Series) -> pd.Series:
    """fgrd_180_dummy_acc_0_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def fgrd_181_dummy_acc_1_5d(revenue: pd.Series) -> pd.Series:
    """fgrd_181_dummy_acc_1_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def fgrd_182_dummy_acc_1_21d(revenue: pd.Series) -> pd.Series:
    """fgrd_182_dummy_acc_1_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def fgrd_183_dummy_acc_1_63d(revenue: pd.Series) -> pd.Series:
    """fgrd_183_dummy_acc_1_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def fgrd_184_dummy_acc_1_126d(revenue: pd.Series) -> pd.Series:
    """fgrd_184_dummy_acc_1_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def fgrd_185_dummy_acc_1_252d(revenue: pd.Series) -> pd.Series:
    """fgrd_185_dummy_acc_1_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def fgrd_186_dummy_acc_2_5d(revenue: pd.Series) -> pd.Series:
    """fgrd_186_dummy_acc_2_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def fgrd_187_dummy_acc_2_21d(revenue: pd.Series) -> pd.Series:
    """fgrd_187_dummy_acc_2_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def fgrd_188_dummy_acc_2_63d(revenue: pd.Series) -> pd.Series:
    """fgrd_188_dummy_acc_2_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def fgrd_189_dummy_acc_2_126d(revenue: pd.Series) -> pd.Series:
    """fgrd_189_dummy_acc_2_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def fgrd_190_dummy_acc_2_252d(revenue: pd.Series) -> pd.Series:
    """fgrd_190_dummy_acc_2_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def fgrd_191_dummy_acc_3_5d(revenue: pd.Series) -> pd.Series:
    """fgrd_191_dummy_acc_3_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def fgrd_192_dummy_acc_3_21d(revenue: pd.Series) -> pd.Series:
    """fgrd_192_dummy_acc_3_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def fgrd_193_dummy_acc_3_63d(revenue: pd.Series) -> pd.Series:
    """fgrd_193_dummy_acc_3_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def fgrd_194_dummy_acc_3_126d(revenue: pd.Series) -> pd.Series:
    """fgrd_194_dummy_acc_3_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def fgrd_195_dummy_acc_3_252d(revenue: pd.Series) -> pd.Series:
    """fgrd_195_dummy_acc_3_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def fgrd_196_dummy_acc_4_5d(revenue: pd.Series) -> pd.Series:
    """fgrd_196_dummy_acc_4_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def fgrd_197_dummy_acc_4_21d(revenue: pd.Series) -> pd.Series:
    """fgrd_197_dummy_acc_4_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def fgrd_198_dummy_acc_4_63d(revenue: pd.Series) -> pd.Series:
    """fgrd_198_dummy_acc_4_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def fgrd_199_dummy_acc_4_126d(revenue: pd.Series) -> pd.Series:
    """fgrd_199_dummy_acc_4_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def fgrd_200_dummy_acc_4_252d(revenue: pd.Series) -> pd.Series:
    """fgrd_200_dummy_acc_4_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V71_REGISTRY_3RD = {
    "fgrd_176_dummy_acc_0_5d": {"inputs": ['revenue'], "func": fgrd_176_dummy_acc_0_5d},
    "fgrd_177_dummy_acc_0_21d": {"inputs": ['revenue'], "func": fgrd_177_dummy_acc_0_21d},
    "fgrd_178_dummy_acc_0_63d": {"inputs": ['revenue'], "func": fgrd_178_dummy_acc_0_63d},
    "fgrd_179_dummy_acc_0_126d": {"inputs": ['revenue'], "func": fgrd_179_dummy_acc_0_126d},
    "fgrd_180_dummy_acc_0_252d": {"inputs": ['revenue'], "func": fgrd_180_dummy_acc_0_252d},
    "fgrd_181_dummy_acc_1_5d": {"inputs": ['revenue'], "func": fgrd_181_dummy_acc_1_5d},
    "fgrd_182_dummy_acc_1_21d": {"inputs": ['revenue'], "func": fgrd_182_dummy_acc_1_21d},
    "fgrd_183_dummy_acc_1_63d": {"inputs": ['revenue'], "func": fgrd_183_dummy_acc_1_63d},
    "fgrd_184_dummy_acc_1_126d": {"inputs": ['revenue'], "func": fgrd_184_dummy_acc_1_126d},
    "fgrd_185_dummy_acc_1_252d": {"inputs": ['revenue'], "func": fgrd_185_dummy_acc_1_252d},
    "fgrd_186_dummy_acc_2_5d": {"inputs": ['revenue'], "func": fgrd_186_dummy_acc_2_5d},
    "fgrd_187_dummy_acc_2_21d": {"inputs": ['revenue'], "func": fgrd_187_dummy_acc_2_21d},
    "fgrd_188_dummy_acc_2_63d": {"inputs": ['revenue'], "func": fgrd_188_dummy_acc_2_63d},
    "fgrd_189_dummy_acc_2_126d": {"inputs": ['revenue'], "func": fgrd_189_dummy_acc_2_126d},
    "fgrd_190_dummy_acc_2_252d": {"inputs": ['revenue'], "func": fgrd_190_dummy_acc_2_252d},
    "fgrd_191_dummy_acc_3_5d": {"inputs": ['revenue'], "func": fgrd_191_dummy_acc_3_5d},
    "fgrd_192_dummy_acc_3_21d": {"inputs": ['revenue'], "func": fgrd_192_dummy_acc_3_21d},
    "fgrd_193_dummy_acc_3_63d": {"inputs": ['revenue'], "func": fgrd_193_dummy_acc_3_63d},
    "fgrd_194_dummy_acc_3_126d": {"inputs": ['revenue'], "func": fgrd_194_dummy_acc_3_126d},
    "fgrd_195_dummy_acc_3_252d": {"inputs": ['revenue'], "func": fgrd_195_dummy_acc_3_252d},
    "fgrd_196_dummy_acc_4_5d": {"inputs": ['revenue'], "func": fgrd_196_dummy_acc_4_5d},
    "fgrd_197_dummy_acc_4_21d": {"inputs": ['revenue'], "func": fgrd_197_dummy_acc_4_21d},
    "fgrd_198_dummy_acc_4_63d": {"inputs": ['revenue'], "func": fgrd_198_dummy_acc_4_63d},
    "fgrd_199_dummy_acc_4_126d": {"inputs": ['revenue'], "func": fgrd_199_dummy_acc_4_126d},
    "fgrd_200_dummy_acc_4_252d": {"inputs": ['revenue'], "func": fgrd_200_dummy_acc_4_252d},
}
