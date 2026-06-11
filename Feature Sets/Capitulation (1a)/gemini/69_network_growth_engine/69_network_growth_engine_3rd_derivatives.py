"""
69_network_growth_engine — 3rd Derivatives
Domain: User/Scale proxy metrics
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

def nwge_176_dummy_acc_0_5d(revenue: pd.Series) -> pd.Series:
    """nwge_176_dummy_acc_0_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def nwge_177_dummy_acc_0_21d(revenue: pd.Series) -> pd.Series:
    """nwge_177_dummy_acc_0_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def nwge_178_dummy_acc_0_63d(revenue: pd.Series) -> pd.Series:
    """nwge_178_dummy_acc_0_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def nwge_179_dummy_acc_0_126d(revenue: pd.Series) -> pd.Series:
    """nwge_179_dummy_acc_0_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def nwge_180_dummy_acc_0_252d(revenue: pd.Series) -> pd.Series:
    """nwge_180_dummy_acc_0_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def nwge_181_dummy_acc_1_5d(revenue: pd.Series) -> pd.Series:
    """nwge_181_dummy_acc_1_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def nwge_182_dummy_acc_1_21d(revenue: pd.Series) -> pd.Series:
    """nwge_182_dummy_acc_1_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def nwge_183_dummy_acc_1_63d(revenue: pd.Series) -> pd.Series:
    """nwge_183_dummy_acc_1_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def nwge_184_dummy_acc_1_126d(revenue: pd.Series) -> pd.Series:
    """nwge_184_dummy_acc_1_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def nwge_185_dummy_acc_1_252d(revenue: pd.Series) -> pd.Series:
    """nwge_185_dummy_acc_1_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def nwge_186_dummy_acc_2_5d(revenue: pd.Series) -> pd.Series:
    """nwge_186_dummy_acc_2_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def nwge_187_dummy_acc_2_21d(revenue: pd.Series) -> pd.Series:
    """nwge_187_dummy_acc_2_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def nwge_188_dummy_acc_2_63d(revenue: pd.Series) -> pd.Series:
    """nwge_188_dummy_acc_2_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def nwge_189_dummy_acc_2_126d(revenue: pd.Series) -> pd.Series:
    """nwge_189_dummy_acc_2_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def nwge_190_dummy_acc_2_252d(revenue: pd.Series) -> pd.Series:
    """nwge_190_dummy_acc_2_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def nwge_191_dummy_acc_3_5d(revenue: pd.Series) -> pd.Series:
    """nwge_191_dummy_acc_3_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def nwge_192_dummy_acc_3_21d(revenue: pd.Series) -> pd.Series:
    """nwge_192_dummy_acc_3_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def nwge_193_dummy_acc_3_63d(revenue: pd.Series) -> pd.Series:
    """nwge_193_dummy_acc_3_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def nwge_194_dummy_acc_3_126d(revenue: pd.Series) -> pd.Series:
    """nwge_194_dummy_acc_3_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def nwge_195_dummy_acc_3_252d(revenue: pd.Series) -> pd.Series:
    """nwge_195_dummy_acc_3_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def nwge_196_dummy_acc_4_5d(revenue: pd.Series) -> pd.Series:
    """nwge_196_dummy_acc_4_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def nwge_197_dummy_acc_4_21d(revenue: pd.Series) -> pd.Series:
    """nwge_197_dummy_acc_4_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def nwge_198_dummy_acc_4_63d(revenue: pd.Series) -> pd.Series:
    """nwge_198_dummy_acc_4_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def nwge_199_dummy_acc_4_126d(revenue: pd.Series) -> pd.Series:
    """nwge_199_dummy_acc_4_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def nwge_200_dummy_acc_4_252d(revenue: pd.Series) -> pd.Series:
    """nwge_200_dummy_acc_4_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V69_REGISTRY_3RD = {
    "nwge_176_dummy_acc_0_5d": {"inputs": ['revenue'], "func": nwge_176_dummy_acc_0_5d},
    "nwge_177_dummy_acc_0_21d": {"inputs": ['revenue'], "func": nwge_177_dummy_acc_0_21d},
    "nwge_178_dummy_acc_0_63d": {"inputs": ['revenue'], "func": nwge_178_dummy_acc_0_63d},
    "nwge_179_dummy_acc_0_126d": {"inputs": ['revenue'], "func": nwge_179_dummy_acc_0_126d},
    "nwge_180_dummy_acc_0_252d": {"inputs": ['revenue'], "func": nwge_180_dummy_acc_0_252d},
    "nwge_181_dummy_acc_1_5d": {"inputs": ['revenue'], "func": nwge_181_dummy_acc_1_5d},
    "nwge_182_dummy_acc_1_21d": {"inputs": ['revenue'], "func": nwge_182_dummy_acc_1_21d},
    "nwge_183_dummy_acc_1_63d": {"inputs": ['revenue'], "func": nwge_183_dummy_acc_1_63d},
    "nwge_184_dummy_acc_1_126d": {"inputs": ['revenue'], "func": nwge_184_dummy_acc_1_126d},
    "nwge_185_dummy_acc_1_252d": {"inputs": ['revenue'], "func": nwge_185_dummy_acc_1_252d},
    "nwge_186_dummy_acc_2_5d": {"inputs": ['revenue'], "func": nwge_186_dummy_acc_2_5d},
    "nwge_187_dummy_acc_2_21d": {"inputs": ['revenue'], "func": nwge_187_dummy_acc_2_21d},
    "nwge_188_dummy_acc_2_63d": {"inputs": ['revenue'], "func": nwge_188_dummy_acc_2_63d},
    "nwge_189_dummy_acc_2_126d": {"inputs": ['revenue'], "func": nwge_189_dummy_acc_2_126d},
    "nwge_190_dummy_acc_2_252d": {"inputs": ['revenue'], "func": nwge_190_dummy_acc_2_252d},
    "nwge_191_dummy_acc_3_5d": {"inputs": ['revenue'], "func": nwge_191_dummy_acc_3_5d},
    "nwge_192_dummy_acc_3_21d": {"inputs": ['revenue'], "func": nwge_192_dummy_acc_3_21d},
    "nwge_193_dummy_acc_3_63d": {"inputs": ['revenue'], "func": nwge_193_dummy_acc_3_63d},
    "nwge_194_dummy_acc_3_126d": {"inputs": ['revenue'], "func": nwge_194_dummy_acc_3_126d},
    "nwge_195_dummy_acc_3_252d": {"inputs": ['revenue'], "func": nwge_195_dummy_acc_3_252d},
    "nwge_196_dummy_acc_4_5d": {"inputs": ['revenue'], "func": nwge_196_dummy_acc_4_5d},
    "nwge_197_dummy_acc_4_21d": {"inputs": ['revenue'], "func": nwge_197_dummy_acc_4_21d},
    "nwge_198_dummy_acc_4_63d": {"inputs": ['revenue'], "func": nwge_198_dummy_acc_4_63d},
    "nwge_199_dummy_acc_4_126d": {"inputs": ['revenue'], "func": nwge_199_dummy_acc_4_126d},
    "nwge_200_dummy_acc_4_252d": {"inputs": ['revenue'], "func": nwge_200_dummy_acc_4_252d},
}
