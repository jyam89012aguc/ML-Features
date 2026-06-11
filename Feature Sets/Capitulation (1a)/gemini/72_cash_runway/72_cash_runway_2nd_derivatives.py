"""
72_cash_runway — 2nd Derivatives
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

def runw_151_dummy_vel_0_5d(revenue: pd.Series) -> pd.Series:
    """runw_151_dummy_vel_0_5d"""
    return (revenue.pct_change(21)).shift(5)

def runw_152_dummy_vel_0_21d(revenue: pd.Series) -> pd.Series:
    """runw_152_dummy_vel_0_21d"""
    return (revenue.pct_change(21)).shift(21)

def runw_153_dummy_vel_0_63d(revenue: pd.Series) -> pd.Series:
    """runw_153_dummy_vel_0_63d"""
    return (revenue.pct_change(21)).shift(63)

def runw_154_dummy_vel_0_126d(revenue: pd.Series) -> pd.Series:
    """runw_154_dummy_vel_0_126d"""
    return (revenue.pct_change(21)).shift(126)

def runw_155_dummy_vel_0_252d(revenue: pd.Series) -> pd.Series:
    """runw_155_dummy_vel_0_252d"""
    return (revenue.pct_change(21)).shift(252)

def runw_156_dummy_vel_1_5d(revenue: pd.Series) -> pd.Series:
    """runw_156_dummy_vel_1_5d"""
    return (revenue.pct_change(21)).shift(5)

def runw_157_dummy_vel_1_21d(revenue: pd.Series) -> pd.Series:
    """runw_157_dummy_vel_1_21d"""
    return (revenue.pct_change(21)).shift(21)

def runw_158_dummy_vel_1_63d(revenue: pd.Series) -> pd.Series:
    """runw_158_dummy_vel_1_63d"""
    return (revenue.pct_change(21)).shift(63)

def runw_159_dummy_vel_1_126d(revenue: pd.Series) -> pd.Series:
    """runw_159_dummy_vel_1_126d"""
    return (revenue.pct_change(21)).shift(126)

def runw_160_dummy_vel_1_252d(revenue: pd.Series) -> pd.Series:
    """runw_160_dummy_vel_1_252d"""
    return (revenue.pct_change(21)).shift(252)

def runw_161_dummy_vel_2_5d(revenue: pd.Series) -> pd.Series:
    """runw_161_dummy_vel_2_5d"""
    return (revenue.pct_change(21)).shift(5)

def runw_162_dummy_vel_2_21d(revenue: pd.Series) -> pd.Series:
    """runw_162_dummy_vel_2_21d"""
    return (revenue.pct_change(21)).shift(21)

def runw_163_dummy_vel_2_63d(revenue: pd.Series) -> pd.Series:
    """runw_163_dummy_vel_2_63d"""
    return (revenue.pct_change(21)).shift(63)

def runw_164_dummy_vel_2_126d(revenue: pd.Series) -> pd.Series:
    """runw_164_dummy_vel_2_126d"""
    return (revenue.pct_change(21)).shift(126)

def runw_165_dummy_vel_2_252d(revenue: pd.Series) -> pd.Series:
    """runw_165_dummy_vel_2_252d"""
    return (revenue.pct_change(21)).shift(252)

def runw_166_dummy_vel_3_5d(revenue: pd.Series) -> pd.Series:
    """runw_166_dummy_vel_3_5d"""
    return (revenue.pct_change(21)).shift(5)

def runw_167_dummy_vel_3_21d(revenue: pd.Series) -> pd.Series:
    """runw_167_dummy_vel_3_21d"""
    return (revenue.pct_change(21)).shift(21)

def runw_168_dummy_vel_3_63d(revenue: pd.Series) -> pd.Series:
    """runw_168_dummy_vel_3_63d"""
    return (revenue.pct_change(21)).shift(63)

def runw_169_dummy_vel_3_126d(revenue: pd.Series) -> pd.Series:
    """runw_169_dummy_vel_3_126d"""
    return (revenue.pct_change(21)).shift(126)

def runw_170_dummy_vel_3_252d(revenue: pd.Series) -> pd.Series:
    """runw_170_dummy_vel_3_252d"""
    return (revenue.pct_change(21)).shift(252)

def runw_171_dummy_vel_4_5d(revenue: pd.Series) -> pd.Series:
    """runw_171_dummy_vel_4_5d"""
    return (revenue.pct_change(21)).shift(5)

def runw_172_dummy_vel_4_21d(revenue: pd.Series) -> pd.Series:
    """runw_172_dummy_vel_4_21d"""
    return (revenue.pct_change(21)).shift(21)

def runw_173_dummy_vel_4_63d(revenue: pd.Series) -> pd.Series:
    """runw_173_dummy_vel_4_63d"""
    return (revenue.pct_change(21)).shift(63)

def runw_174_dummy_vel_4_126d(revenue: pd.Series) -> pd.Series:
    """runw_174_dummy_vel_4_126d"""
    return (revenue.pct_change(21)).shift(126)

def runw_175_dummy_vel_4_252d(revenue: pd.Series) -> pd.Series:
    """runw_175_dummy_vel_4_252d"""
    return (revenue.pct_change(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V72_REGISTRY_2ND = {
    "runw_151_dummy_vel_0_5d": {"inputs": ['revenue'], "func": runw_151_dummy_vel_0_5d},
    "runw_152_dummy_vel_0_21d": {"inputs": ['revenue'], "func": runw_152_dummy_vel_0_21d},
    "runw_153_dummy_vel_0_63d": {"inputs": ['revenue'], "func": runw_153_dummy_vel_0_63d},
    "runw_154_dummy_vel_0_126d": {"inputs": ['revenue'], "func": runw_154_dummy_vel_0_126d},
    "runw_155_dummy_vel_0_252d": {"inputs": ['revenue'], "func": runw_155_dummy_vel_0_252d},
    "runw_156_dummy_vel_1_5d": {"inputs": ['revenue'], "func": runw_156_dummy_vel_1_5d},
    "runw_157_dummy_vel_1_21d": {"inputs": ['revenue'], "func": runw_157_dummy_vel_1_21d},
    "runw_158_dummy_vel_1_63d": {"inputs": ['revenue'], "func": runw_158_dummy_vel_1_63d},
    "runw_159_dummy_vel_1_126d": {"inputs": ['revenue'], "func": runw_159_dummy_vel_1_126d},
    "runw_160_dummy_vel_1_252d": {"inputs": ['revenue'], "func": runw_160_dummy_vel_1_252d},
    "runw_161_dummy_vel_2_5d": {"inputs": ['revenue'], "func": runw_161_dummy_vel_2_5d},
    "runw_162_dummy_vel_2_21d": {"inputs": ['revenue'], "func": runw_162_dummy_vel_2_21d},
    "runw_163_dummy_vel_2_63d": {"inputs": ['revenue'], "func": runw_163_dummy_vel_2_63d},
    "runw_164_dummy_vel_2_126d": {"inputs": ['revenue'], "func": runw_164_dummy_vel_2_126d},
    "runw_165_dummy_vel_2_252d": {"inputs": ['revenue'], "func": runw_165_dummy_vel_2_252d},
    "runw_166_dummy_vel_3_5d": {"inputs": ['revenue'], "func": runw_166_dummy_vel_3_5d},
    "runw_167_dummy_vel_3_21d": {"inputs": ['revenue'], "func": runw_167_dummy_vel_3_21d},
    "runw_168_dummy_vel_3_63d": {"inputs": ['revenue'], "func": runw_168_dummy_vel_3_63d},
    "runw_169_dummy_vel_3_126d": {"inputs": ['revenue'], "func": runw_169_dummy_vel_3_126d},
    "runw_170_dummy_vel_3_252d": {"inputs": ['revenue'], "func": runw_170_dummy_vel_3_252d},
    "runw_171_dummy_vel_4_5d": {"inputs": ['revenue'], "func": runw_171_dummy_vel_4_5d},
    "runw_172_dummy_vel_4_21d": {"inputs": ['revenue'], "func": runw_172_dummy_vel_4_21d},
    "runw_173_dummy_vel_4_63d": {"inputs": ['revenue'], "func": runw_173_dummy_vel_4_63d},
    "runw_174_dummy_vel_4_126d": {"inputs": ['revenue'], "func": runw_174_dummy_vel_4_126d},
    "runw_175_dummy_vel_4_252d": {"inputs": ['revenue'], "func": runw_175_dummy_vel_4_252d},
}
