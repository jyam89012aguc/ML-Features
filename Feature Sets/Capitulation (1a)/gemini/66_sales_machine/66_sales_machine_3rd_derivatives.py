"""
66_sales_machine — 3rd Derivatives
Domain: Rev / (SGA + R&D)
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

def slsm_176_dummy_acc_0_5d(revenue: pd.Series) -> pd.Series:
    """slsm_176_dummy_acc_0_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def slsm_177_dummy_acc_0_21d(revenue: pd.Series) -> pd.Series:
    """slsm_177_dummy_acc_0_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def slsm_178_dummy_acc_0_63d(revenue: pd.Series) -> pd.Series:
    """slsm_178_dummy_acc_0_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def slsm_179_dummy_acc_0_126d(revenue: pd.Series) -> pd.Series:
    """slsm_179_dummy_acc_0_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def slsm_180_dummy_acc_0_252d(revenue: pd.Series) -> pd.Series:
    """slsm_180_dummy_acc_0_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def slsm_181_dummy_acc_1_5d(revenue: pd.Series) -> pd.Series:
    """slsm_181_dummy_acc_1_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def slsm_182_dummy_acc_1_21d(revenue: pd.Series) -> pd.Series:
    """slsm_182_dummy_acc_1_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def slsm_183_dummy_acc_1_63d(revenue: pd.Series) -> pd.Series:
    """slsm_183_dummy_acc_1_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def slsm_184_dummy_acc_1_126d(revenue: pd.Series) -> pd.Series:
    """slsm_184_dummy_acc_1_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def slsm_185_dummy_acc_1_252d(revenue: pd.Series) -> pd.Series:
    """slsm_185_dummy_acc_1_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def slsm_186_dummy_acc_2_5d(revenue: pd.Series) -> pd.Series:
    """slsm_186_dummy_acc_2_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def slsm_187_dummy_acc_2_21d(revenue: pd.Series) -> pd.Series:
    """slsm_187_dummy_acc_2_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def slsm_188_dummy_acc_2_63d(revenue: pd.Series) -> pd.Series:
    """slsm_188_dummy_acc_2_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def slsm_189_dummy_acc_2_126d(revenue: pd.Series) -> pd.Series:
    """slsm_189_dummy_acc_2_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def slsm_190_dummy_acc_2_252d(revenue: pd.Series) -> pd.Series:
    """slsm_190_dummy_acc_2_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def slsm_191_dummy_acc_3_5d(revenue: pd.Series) -> pd.Series:
    """slsm_191_dummy_acc_3_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def slsm_192_dummy_acc_3_21d(revenue: pd.Series) -> pd.Series:
    """slsm_192_dummy_acc_3_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def slsm_193_dummy_acc_3_63d(revenue: pd.Series) -> pd.Series:
    """slsm_193_dummy_acc_3_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def slsm_194_dummy_acc_3_126d(revenue: pd.Series) -> pd.Series:
    """slsm_194_dummy_acc_3_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def slsm_195_dummy_acc_3_252d(revenue: pd.Series) -> pd.Series:
    """slsm_195_dummy_acc_3_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def slsm_196_dummy_acc_4_5d(revenue: pd.Series) -> pd.Series:
    """slsm_196_dummy_acc_4_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def slsm_197_dummy_acc_4_21d(revenue: pd.Series) -> pd.Series:
    """slsm_197_dummy_acc_4_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def slsm_198_dummy_acc_4_63d(revenue: pd.Series) -> pd.Series:
    """slsm_198_dummy_acc_4_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def slsm_199_dummy_acc_4_126d(revenue: pd.Series) -> pd.Series:
    """slsm_199_dummy_acc_4_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def slsm_200_dummy_acc_4_252d(revenue: pd.Series) -> pd.Series:
    """slsm_200_dummy_acc_4_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V66_REGISTRY_3RD = {
    "slsm_176_dummy_acc_0_5d": {"inputs": ['revenue'], "func": slsm_176_dummy_acc_0_5d},
    "slsm_177_dummy_acc_0_21d": {"inputs": ['revenue'], "func": slsm_177_dummy_acc_0_21d},
    "slsm_178_dummy_acc_0_63d": {"inputs": ['revenue'], "func": slsm_178_dummy_acc_0_63d},
    "slsm_179_dummy_acc_0_126d": {"inputs": ['revenue'], "func": slsm_179_dummy_acc_0_126d},
    "slsm_180_dummy_acc_0_252d": {"inputs": ['revenue'], "func": slsm_180_dummy_acc_0_252d},
    "slsm_181_dummy_acc_1_5d": {"inputs": ['revenue'], "func": slsm_181_dummy_acc_1_5d},
    "slsm_182_dummy_acc_1_21d": {"inputs": ['revenue'], "func": slsm_182_dummy_acc_1_21d},
    "slsm_183_dummy_acc_1_63d": {"inputs": ['revenue'], "func": slsm_183_dummy_acc_1_63d},
    "slsm_184_dummy_acc_1_126d": {"inputs": ['revenue'], "func": slsm_184_dummy_acc_1_126d},
    "slsm_185_dummy_acc_1_252d": {"inputs": ['revenue'], "func": slsm_185_dummy_acc_1_252d},
    "slsm_186_dummy_acc_2_5d": {"inputs": ['revenue'], "func": slsm_186_dummy_acc_2_5d},
    "slsm_187_dummy_acc_2_21d": {"inputs": ['revenue'], "func": slsm_187_dummy_acc_2_21d},
    "slsm_188_dummy_acc_2_63d": {"inputs": ['revenue'], "func": slsm_188_dummy_acc_2_63d},
    "slsm_189_dummy_acc_2_126d": {"inputs": ['revenue'], "func": slsm_189_dummy_acc_2_126d},
    "slsm_190_dummy_acc_2_252d": {"inputs": ['revenue'], "func": slsm_190_dummy_acc_2_252d},
    "slsm_191_dummy_acc_3_5d": {"inputs": ['revenue'], "func": slsm_191_dummy_acc_3_5d},
    "slsm_192_dummy_acc_3_21d": {"inputs": ['revenue'], "func": slsm_192_dummy_acc_3_21d},
    "slsm_193_dummy_acc_3_63d": {"inputs": ['revenue'], "func": slsm_193_dummy_acc_3_63d},
    "slsm_194_dummy_acc_3_126d": {"inputs": ['revenue'], "func": slsm_194_dummy_acc_3_126d},
    "slsm_195_dummy_acc_3_252d": {"inputs": ['revenue'], "func": slsm_195_dummy_acc_3_252d},
    "slsm_196_dummy_acc_4_5d": {"inputs": ['revenue'], "func": slsm_196_dummy_acc_4_5d},
    "slsm_197_dummy_acc_4_21d": {"inputs": ['revenue'], "func": slsm_197_dummy_acc_4_21d},
    "slsm_198_dummy_acc_4_63d": {"inputs": ['revenue'], "func": slsm_198_dummy_acc_4_63d},
    "slsm_199_dummy_acc_4_126d": {"inputs": ['revenue'], "func": slsm_199_dummy_acc_4_126d},
    "slsm_200_dummy_acc_4_252d": {"inputs": ['revenue'], "func": slsm_200_dummy_acc_4_252d},
}
