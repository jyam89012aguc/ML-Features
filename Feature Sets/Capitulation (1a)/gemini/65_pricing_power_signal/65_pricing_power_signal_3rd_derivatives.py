"""
65_pricing_power_signal — 3rd Derivatives
Domain: Margin stability vs Cost growth
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

def prpw_176_dummy_acc_0_5d(revenue: pd.Series) -> pd.Series:
    """prpw_176_dummy_acc_0_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def prpw_177_dummy_acc_0_21d(revenue: pd.Series) -> pd.Series:
    """prpw_177_dummy_acc_0_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def prpw_178_dummy_acc_0_63d(revenue: pd.Series) -> pd.Series:
    """prpw_178_dummy_acc_0_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def prpw_179_dummy_acc_0_126d(revenue: pd.Series) -> pd.Series:
    """prpw_179_dummy_acc_0_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def prpw_180_dummy_acc_0_252d(revenue: pd.Series) -> pd.Series:
    """prpw_180_dummy_acc_0_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def prpw_181_dummy_acc_1_5d(revenue: pd.Series) -> pd.Series:
    """prpw_181_dummy_acc_1_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def prpw_182_dummy_acc_1_21d(revenue: pd.Series) -> pd.Series:
    """prpw_182_dummy_acc_1_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def prpw_183_dummy_acc_1_63d(revenue: pd.Series) -> pd.Series:
    """prpw_183_dummy_acc_1_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def prpw_184_dummy_acc_1_126d(revenue: pd.Series) -> pd.Series:
    """prpw_184_dummy_acc_1_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def prpw_185_dummy_acc_1_252d(revenue: pd.Series) -> pd.Series:
    """prpw_185_dummy_acc_1_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def prpw_186_dummy_acc_2_5d(revenue: pd.Series) -> pd.Series:
    """prpw_186_dummy_acc_2_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def prpw_187_dummy_acc_2_21d(revenue: pd.Series) -> pd.Series:
    """prpw_187_dummy_acc_2_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def prpw_188_dummy_acc_2_63d(revenue: pd.Series) -> pd.Series:
    """prpw_188_dummy_acc_2_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def prpw_189_dummy_acc_2_126d(revenue: pd.Series) -> pd.Series:
    """prpw_189_dummy_acc_2_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def prpw_190_dummy_acc_2_252d(revenue: pd.Series) -> pd.Series:
    """prpw_190_dummy_acc_2_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def prpw_191_dummy_acc_3_5d(revenue: pd.Series) -> pd.Series:
    """prpw_191_dummy_acc_3_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def prpw_192_dummy_acc_3_21d(revenue: pd.Series) -> pd.Series:
    """prpw_192_dummy_acc_3_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def prpw_193_dummy_acc_3_63d(revenue: pd.Series) -> pd.Series:
    """prpw_193_dummy_acc_3_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def prpw_194_dummy_acc_3_126d(revenue: pd.Series) -> pd.Series:
    """prpw_194_dummy_acc_3_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def prpw_195_dummy_acc_3_252d(revenue: pd.Series) -> pd.Series:
    """prpw_195_dummy_acc_3_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def prpw_196_dummy_acc_4_5d(revenue: pd.Series) -> pd.Series:
    """prpw_196_dummy_acc_4_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def prpw_197_dummy_acc_4_21d(revenue: pd.Series) -> pd.Series:
    """prpw_197_dummy_acc_4_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def prpw_198_dummy_acc_4_63d(revenue: pd.Series) -> pd.Series:
    """prpw_198_dummy_acc_4_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def prpw_199_dummy_acc_4_126d(revenue: pd.Series) -> pd.Series:
    """prpw_199_dummy_acc_4_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def prpw_200_dummy_acc_4_252d(revenue: pd.Series) -> pd.Series:
    """prpw_200_dummy_acc_4_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V65_REGISTRY_3RD = {
    "prpw_176_dummy_acc_0_5d": {"inputs": ['revenue'], "func": prpw_176_dummy_acc_0_5d},
    "prpw_177_dummy_acc_0_21d": {"inputs": ['revenue'], "func": prpw_177_dummy_acc_0_21d},
    "prpw_178_dummy_acc_0_63d": {"inputs": ['revenue'], "func": prpw_178_dummy_acc_0_63d},
    "prpw_179_dummy_acc_0_126d": {"inputs": ['revenue'], "func": prpw_179_dummy_acc_0_126d},
    "prpw_180_dummy_acc_0_252d": {"inputs": ['revenue'], "func": prpw_180_dummy_acc_0_252d},
    "prpw_181_dummy_acc_1_5d": {"inputs": ['revenue'], "func": prpw_181_dummy_acc_1_5d},
    "prpw_182_dummy_acc_1_21d": {"inputs": ['revenue'], "func": prpw_182_dummy_acc_1_21d},
    "prpw_183_dummy_acc_1_63d": {"inputs": ['revenue'], "func": prpw_183_dummy_acc_1_63d},
    "prpw_184_dummy_acc_1_126d": {"inputs": ['revenue'], "func": prpw_184_dummy_acc_1_126d},
    "prpw_185_dummy_acc_1_252d": {"inputs": ['revenue'], "func": prpw_185_dummy_acc_1_252d},
    "prpw_186_dummy_acc_2_5d": {"inputs": ['revenue'], "func": prpw_186_dummy_acc_2_5d},
    "prpw_187_dummy_acc_2_21d": {"inputs": ['revenue'], "func": prpw_187_dummy_acc_2_21d},
    "prpw_188_dummy_acc_2_63d": {"inputs": ['revenue'], "func": prpw_188_dummy_acc_2_63d},
    "prpw_189_dummy_acc_2_126d": {"inputs": ['revenue'], "func": prpw_189_dummy_acc_2_126d},
    "prpw_190_dummy_acc_2_252d": {"inputs": ['revenue'], "func": prpw_190_dummy_acc_2_252d},
    "prpw_191_dummy_acc_3_5d": {"inputs": ['revenue'], "func": prpw_191_dummy_acc_3_5d},
    "prpw_192_dummy_acc_3_21d": {"inputs": ['revenue'], "func": prpw_192_dummy_acc_3_21d},
    "prpw_193_dummy_acc_3_63d": {"inputs": ['revenue'], "func": prpw_193_dummy_acc_3_63d},
    "prpw_194_dummy_acc_3_126d": {"inputs": ['revenue'], "func": prpw_194_dummy_acc_3_126d},
    "prpw_195_dummy_acc_3_252d": {"inputs": ['revenue'], "func": prpw_195_dummy_acc_3_252d},
    "prpw_196_dummy_acc_4_5d": {"inputs": ['revenue'], "func": prpw_196_dummy_acc_4_5d},
    "prpw_197_dummy_acc_4_21d": {"inputs": ['revenue'], "func": prpw_197_dummy_acc_4_21d},
    "prpw_198_dummy_acc_4_63d": {"inputs": ['revenue'], "func": prpw_198_dummy_acc_4_63d},
    "prpw_199_dummy_acc_4_126d": {"inputs": ['revenue'], "func": prpw_199_dummy_acc_4_126d},
    "prpw_200_dummy_acc_4_252d": {"inputs": ['revenue'], "func": prpw_200_dummy_acc_4_252d},
}
