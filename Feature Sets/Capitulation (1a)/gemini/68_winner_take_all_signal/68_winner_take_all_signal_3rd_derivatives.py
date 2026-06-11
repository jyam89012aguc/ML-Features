"""
68_winner_take_all_signal — 3rd Derivatives
Domain: Market share growth proxy
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

def wtas_176_dummy_acc_0_5d(revenue: pd.Series) -> pd.Series:
    """wtas_176_dummy_acc_0_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def wtas_177_dummy_acc_0_21d(revenue: pd.Series) -> pd.Series:
    """wtas_177_dummy_acc_0_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def wtas_178_dummy_acc_0_63d(revenue: pd.Series) -> pd.Series:
    """wtas_178_dummy_acc_0_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def wtas_179_dummy_acc_0_126d(revenue: pd.Series) -> pd.Series:
    """wtas_179_dummy_acc_0_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def wtas_180_dummy_acc_0_252d(revenue: pd.Series) -> pd.Series:
    """wtas_180_dummy_acc_0_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def wtas_181_dummy_acc_1_5d(revenue: pd.Series) -> pd.Series:
    """wtas_181_dummy_acc_1_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def wtas_182_dummy_acc_1_21d(revenue: pd.Series) -> pd.Series:
    """wtas_182_dummy_acc_1_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def wtas_183_dummy_acc_1_63d(revenue: pd.Series) -> pd.Series:
    """wtas_183_dummy_acc_1_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def wtas_184_dummy_acc_1_126d(revenue: pd.Series) -> pd.Series:
    """wtas_184_dummy_acc_1_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def wtas_185_dummy_acc_1_252d(revenue: pd.Series) -> pd.Series:
    """wtas_185_dummy_acc_1_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def wtas_186_dummy_acc_2_5d(revenue: pd.Series) -> pd.Series:
    """wtas_186_dummy_acc_2_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def wtas_187_dummy_acc_2_21d(revenue: pd.Series) -> pd.Series:
    """wtas_187_dummy_acc_2_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def wtas_188_dummy_acc_2_63d(revenue: pd.Series) -> pd.Series:
    """wtas_188_dummy_acc_2_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def wtas_189_dummy_acc_2_126d(revenue: pd.Series) -> pd.Series:
    """wtas_189_dummy_acc_2_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def wtas_190_dummy_acc_2_252d(revenue: pd.Series) -> pd.Series:
    """wtas_190_dummy_acc_2_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def wtas_191_dummy_acc_3_5d(revenue: pd.Series) -> pd.Series:
    """wtas_191_dummy_acc_3_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def wtas_192_dummy_acc_3_21d(revenue: pd.Series) -> pd.Series:
    """wtas_192_dummy_acc_3_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def wtas_193_dummy_acc_3_63d(revenue: pd.Series) -> pd.Series:
    """wtas_193_dummy_acc_3_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def wtas_194_dummy_acc_3_126d(revenue: pd.Series) -> pd.Series:
    """wtas_194_dummy_acc_3_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def wtas_195_dummy_acc_3_252d(revenue: pd.Series) -> pd.Series:
    """wtas_195_dummy_acc_3_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

def wtas_196_dummy_acc_4_5d(revenue: pd.Series) -> pd.Series:
    """wtas_196_dummy_acc_4_5d"""
    return (revenue.pct_change(63).diff(21)).shift(5)

def wtas_197_dummy_acc_4_21d(revenue: pd.Series) -> pd.Series:
    """wtas_197_dummy_acc_4_21d"""
    return (revenue.pct_change(63).diff(21)).shift(21)

def wtas_198_dummy_acc_4_63d(revenue: pd.Series) -> pd.Series:
    """wtas_198_dummy_acc_4_63d"""
    return (revenue.pct_change(63).diff(21)).shift(63)

def wtas_199_dummy_acc_4_126d(revenue: pd.Series) -> pd.Series:
    """wtas_199_dummy_acc_4_126d"""
    return (revenue.pct_change(63).diff(21)).shift(126)

def wtas_200_dummy_acc_4_252d(revenue: pd.Series) -> pd.Series:
    """wtas_200_dummy_acc_4_252d"""
    return (revenue.pct_change(63).diff(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V68_REGISTRY_3RD = {
    "wtas_176_dummy_acc_0_5d": {"inputs": ['revenue'], "func": wtas_176_dummy_acc_0_5d},
    "wtas_177_dummy_acc_0_21d": {"inputs": ['revenue'], "func": wtas_177_dummy_acc_0_21d},
    "wtas_178_dummy_acc_0_63d": {"inputs": ['revenue'], "func": wtas_178_dummy_acc_0_63d},
    "wtas_179_dummy_acc_0_126d": {"inputs": ['revenue'], "func": wtas_179_dummy_acc_0_126d},
    "wtas_180_dummy_acc_0_252d": {"inputs": ['revenue'], "func": wtas_180_dummy_acc_0_252d},
    "wtas_181_dummy_acc_1_5d": {"inputs": ['revenue'], "func": wtas_181_dummy_acc_1_5d},
    "wtas_182_dummy_acc_1_21d": {"inputs": ['revenue'], "func": wtas_182_dummy_acc_1_21d},
    "wtas_183_dummy_acc_1_63d": {"inputs": ['revenue'], "func": wtas_183_dummy_acc_1_63d},
    "wtas_184_dummy_acc_1_126d": {"inputs": ['revenue'], "func": wtas_184_dummy_acc_1_126d},
    "wtas_185_dummy_acc_1_252d": {"inputs": ['revenue'], "func": wtas_185_dummy_acc_1_252d},
    "wtas_186_dummy_acc_2_5d": {"inputs": ['revenue'], "func": wtas_186_dummy_acc_2_5d},
    "wtas_187_dummy_acc_2_21d": {"inputs": ['revenue'], "func": wtas_187_dummy_acc_2_21d},
    "wtas_188_dummy_acc_2_63d": {"inputs": ['revenue'], "func": wtas_188_dummy_acc_2_63d},
    "wtas_189_dummy_acc_2_126d": {"inputs": ['revenue'], "func": wtas_189_dummy_acc_2_126d},
    "wtas_190_dummy_acc_2_252d": {"inputs": ['revenue'], "func": wtas_190_dummy_acc_2_252d},
    "wtas_191_dummy_acc_3_5d": {"inputs": ['revenue'], "func": wtas_191_dummy_acc_3_5d},
    "wtas_192_dummy_acc_3_21d": {"inputs": ['revenue'], "func": wtas_192_dummy_acc_3_21d},
    "wtas_193_dummy_acc_3_63d": {"inputs": ['revenue'], "func": wtas_193_dummy_acc_3_63d},
    "wtas_194_dummy_acc_3_126d": {"inputs": ['revenue'], "func": wtas_194_dummy_acc_3_126d},
    "wtas_195_dummy_acc_3_252d": {"inputs": ['revenue'], "func": wtas_195_dummy_acc_3_252d},
    "wtas_196_dummy_acc_4_5d": {"inputs": ['revenue'], "func": wtas_196_dummy_acc_4_5d},
    "wtas_197_dummy_acc_4_21d": {"inputs": ['revenue'], "func": wtas_197_dummy_acc_4_21d},
    "wtas_198_dummy_acc_4_63d": {"inputs": ['revenue'], "func": wtas_198_dummy_acc_4_63d},
    "wtas_199_dummy_acc_4_126d": {"inputs": ['revenue'], "func": wtas_199_dummy_acc_4_126d},
    "wtas_200_dummy_acc_4_252d": {"inputs": ['revenue'], "func": wtas_200_dummy_acc_4_252d},
}
