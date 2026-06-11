"""
74_terminal_decline_composite — 3rd Derivatives
Domain: Composite of all forensic decay signals
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

def tedc_176_dummy_acc_0_5d(revenue: pd.Series) -> pd.Series:
    """tedc_176_dummy_acc_0_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def tedc_177_dummy_acc_0_21d(revenue: pd.Series) -> pd.Series:
    """tedc_177_dummy_acc_0_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def tedc_178_dummy_acc_0_63d(revenue: pd.Series) -> pd.Series:
    """tedc_178_dummy_acc_0_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def tedc_179_dummy_acc_0_126d(revenue: pd.Series) -> pd.Series:
    """tedc_179_dummy_acc_0_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def tedc_180_dummy_acc_0_252d(revenue: pd.Series) -> pd.Series:
    """tedc_180_dummy_acc_0_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def tedc_181_dummy_acc_1_5d(revenue: pd.Series) -> pd.Series:
    """tedc_181_dummy_acc_1_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def tedc_182_dummy_acc_1_21d(revenue: pd.Series) -> pd.Series:
    """tedc_182_dummy_acc_1_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def tedc_183_dummy_acc_1_63d(revenue: pd.Series) -> pd.Series:
    """tedc_183_dummy_acc_1_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def tedc_184_dummy_acc_1_126d(revenue: pd.Series) -> pd.Series:
    """tedc_184_dummy_acc_1_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def tedc_185_dummy_acc_1_252d(revenue: pd.Series) -> pd.Series:
    """tedc_185_dummy_acc_1_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def tedc_186_dummy_acc_2_5d(revenue: pd.Series) -> pd.Series:
    """tedc_186_dummy_acc_2_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def tedc_187_dummy_acc_2_21d(revenue: pd.Series) -> pd.Series:
    """tedc_187_dummy_acc_2_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def tedc_188_dummy_acc_2_63d(revenue: pd.Series) -> pd.Series:
    """tedc_188_dummy_acc_2_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def tedc_189_dummy_acc_2_126d(revenue: pd.Series) -> pd.Series:
    """tedc_189_dummy_acc_2_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def tedc_190_dummy_acc_2_252d(revenue: pd.Series) -> pd.Series:
    """tedc_190_dummy_acc_2_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def tedc_191_dummy_acc_3_5d(revenue: pd.Series) -> pd.Series:
    """tedc_191_dummy_acc_3_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def tedc_192_dummy_acc_3_21d(revenue: pd.Series) -> pd.Series:
    """tedc_192_dummy_acc_3_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def tedc_193_dummy_acc_3_63d(revenue: pd.Series) -> pd.Series:
    """tedc_193_dummy_acc_3_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def tedc_194_dummy_acc_3_126d(revenue: pd.Series) -> pd.Series:
    """tedc_194_dummy_acc_3_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def tedc_195_dummy_acc_3_252d(revenue: pd.Series) -> pd.Series:
    """tedc_195_dummy_acc_3_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def tedc_196_dummy_acc_4_5d(revenue: pd.Series) -> pd.Series:
    """tedc_196_dummy_acc_4_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def tedc_197_dummy_acc_4_21d(revenue: pd.Series) -> pd.Series:
    """tedc_197_dummy_acc_4_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def tedc_198_dummy_acc_4_63d(revenue: pd.Series) -> pd.Series:
    """tedc_198_dummy_acc_4_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def tedc_199_dummy_acc_4_126d(revenue: pd.Series) -> pd.Series:
    """tedc_199_dummy_acc_4_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def tedc_200_dummy_acc_4_252d(revenue: pd.Series) -> pd.Series:
    """tedc_200_dummy_acc_4_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V74_REGISTRY_3RD = {
    "tedc_176_dummy_acc_0_5d": {"inputs": ['revenue'], "func": tedc_176_dummy_acc_0_5d},
    "tedc_177_dummy_acc_0_21d": {"inputs": ['revenue'], "func": tedc_177_dummy_acc_0_21d},
    "tedc_178_dummy_acc_0_63d": {"inputs": ['revenue'], "func": tedc_178_dummy_acc_0_63d},
    "tedc_179_dummy_acc_0_126d": {"inputs": ['revenue'], "func": tedc_179_dummy_acc_0_126d},
    "tedc_180_dummy_acc_0_252d": {"inputs": ['revenue'], "func": tedc_180_dummy_acc_0_252d},
    "tedc_181_dummy_acc_1_5d": {"inputs": ['revenue'], "func": tedc_181_dummy_acc_1_5d},
    "tedc_182_dummy_acc_1_21d": {"inputs": ['revenue'], "func": tedc_182_dummy_acc_1_21d},
    "tedc_183_dummy_acc_1_63d": {"inputs": ['revenue'], "func": tedc_183_dummy_acc_1_63d},
    "tedc_184_dummy_acc_1_126d": {"inputs": ['revenue'], "func": tedc_184_dummy_acc_1_126d},
    "tedc_185_dummy_acc_1_252d": {"inputs": ['revenue'], "func": tedc_185_dummy_acc_1_252d},
    "tedc_186_dummy_acc_2_5d": {"inputs": ['revenue'], "func": tedc_186_dummy_acc_2_5d},
    "tedc_187_dummy_acc_2_21d": {"inputs": ['revenue'], "func": tedc_187_dummy_acc_2_21d},
    "tedc_188_dummy_acc_2_63d": {"inputs": ['revenue'], "func": tedc_188_dummy_acc_2_63d},
    "tedc_189_dummy_acc_2_126d": {"inputs": ['revenue'], "func": tedc_189_dummy_acc_2_126d},
    "tedc_190_dummy_acc_2_252d": {"inputs": ['revenue'], "func": tedc_190_dummy_acc_2_252d},
    "tedc_191_dummy_acc_3_5d": {"inputs": ['revenue'], "func": tedc_191_dummy_acc_3_5d},
    "tedc_192_dummy_acc_3_21d": {"inputs": ['revenue'], "func": tedc_192_dummy_acc_3_21d},
    "tedc_193_dummy_acc_3_63d": {"inputs": ['revenue'], "func": tedc_193_dummy_acc_3_63d},
    "tedc_194_dummy_acc_3_126d": {"inputs": ['revenue'], "func": tedc_194_dummy_acc_3_126d},
    "tedc_195_dummy_acc_3_252d": {"inputs": ['revenue'], "func": tedc_195_dummy_acc_3_252d},
    "tedc_196_dummy_acc_4_5d": {"inputs": ['revenue'], "func": tedc_196_dummy_acc_4_5d},
    "tedc_197_dummy_acc_4_21d": {"inputs": ['revenue'], "func": tedc_197_dummy_acc_4_21d},
    "tedc_198_dummy_acc_4_63d": {"inputs": ['revenue'], "func": tedc_198_dummy_acc_4_63d},
    "tedc_199_dummy_acc_4_126d": {"inputs": ['revenue'], "func": tedc_199_dummy_acc_4_126d},
    "tedc_200_dummy_acc_4_252d": {"inputs": ['revenue'], "func": tedc_200_dummy_acc_4_252d},
}
