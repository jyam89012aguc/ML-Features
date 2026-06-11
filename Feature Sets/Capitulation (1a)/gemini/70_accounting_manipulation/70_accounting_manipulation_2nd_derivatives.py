"""
70_accounting_manipulation — 2nd Derivatives
Domain: Beneish M-score proxies, Accruals/Assets
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

def acmn_151_dummy_vel_0_5d(revenue: pd.Series) -> pd.Series:
    """acmn_151_dummy_vel_0_5d"""
    return (revenue.pct_change(21)).shift(5)

def acmn_152_dummy_vel_0_21d(revenue: pd.Series) -> pd.Series:
    """acmn_152_dummy_vel_0_21d"""
    return (revenue.pct_change(21)).shift(21)

def acmn_153_dummy_vel_0_63d(revenue: pd.Series) -> pd.Series:
    """acmn_153_dummy_vel_0_63d"""
    return (revenue.pct_change(21)).shift(63)

def acmn_154_dummy_vel_0_126d(revenue: pd.Series) -> pd.Series:
    """acmn_154_dummy_vel_0_126d"""
    return (revenue.pct_change(21)).shift(126)

def acmn_155_dummy_vel_0_252d(revenue: pd.Series) -> pd.Series:
    """acmn_155_dummy_vel_0_252d"""
    return (revenue.pct_change(21)).shift(252)

def acmn_156_dummy_vel_1_5d(revenue: pd.Series) -> pd.Series:
    """acmn_156_dummy_vel_1_5d"""
    return (revenue.pct_change(21)).shift(5)

def acmn_157_dummy_vel_1_21d(revenue: pd.Series) -> pd.Series:
    """acmn_157_dummy_vel_1_21d"""
    return (revenue.pct_change(21)).shift(21)

def acmn_158_dummy_vel_1_63d(revenue: pd.Series) -> pd.Series:
    """acmn_158_dummy_vel_1_63d"""
    return (revenue.pct_change(21)).shift(63)

def acmn_159_dummy_vel_1_126d(revenue: pd.Series) -> pd.Series:
    """acmn_159_dummy_vel_1_126d"""
    return (revenue.pct_change(21)).shift(126)

def acmn_160_dummy_vel_1_252d(revenue: pd.Series) -> pd.Series:
    """acmn_160_dummy_vel_1_252d"""
    return (revenue.pct_change(21)).shift(252)

def acmn_161_dummy_vel_2_5d(revenue: pd.Series) -> pd.Series:
    """acmn_161_dummy_vel_2_5d"""
    return (revenue.pct_change(21)).shift(5)

def acmn_162_dummy_vel_2_21d(revenue: pd.Series) -> pd.Series:
    """acmn_162_dummy_vel_2_21d"""
    return (revenue.pct_change(21)).shift(21)

def acmn_163_dummy_vel_2_63d(revenue: pd.Series) -> pd.Series:
    """acmn_163_dummy_vel_2_63d"""
    return (revenue.pct_change(21)).shift(63)

def acmn_164_dummy_vel_2_126d(revenue: pd.Series) -> pd.Series:
    """acmn_164_dummy_vel_2_126d"""
    return (revenue.pct_change(21)).shift(126)

def acmn_165_dummy_vel_2_252d(revenue: pd.Series) -> pd.Series:
    """acmn_165_dummy_vel_2_252d"""
    return (revenue.pct_change(21)).shift(252)

def acmn_166_dummy_vel_3_5d(revenue: pd.Series) -> pd.Series:
    """acmn_166_dummy_vel_3_5d"""
    return (revenue.pct_change(21)).shift(5)

def acmn_167_dummy_vel_3_21d(revenue: pd.Series) -> pd.Series:
    """acmn_167_dummy_vel_3_21d"""
    return (revenue.pct_change(21)).shift(21)

def acmn_168_dummy_vel_3_63d(revenue: pd.Series) -> pd.Series:
    """acmn_168_dummy_vel_3_63d"""
    return (revenue.pct_change(21)).shift(63)

def acmn_169_dummy_vel_3_126d(revenue: pd.Series) -> pd.Series:
    """acmn_169_dummy_vel_3_126d"""
    return (revenue.pct_change(21)).shift(126)

def acmn_170_dummy_vel_3_252d(revenue: pd.Series) -> pd.Series:
    """acmn_170_dummy_vel_3_252d"""
    return (revenue.pct_change(21)).shift(252)

def acmn_171_dummy_vel_4_5d(revenue: pd.Series) -> pd.Series:
    """acmn_171_dummy_vel_4_5d"""
    return (revenue.pct_change(21)).shift(5)

def acmn_172_dummy_vel_4_21d(revenue: pd.Series) -> pd.Series:
    """acmn_172_dummy_vel_4_21d"""
    return (revenue.pct_change(21)).shift(21)

def acmn_173_dummy_vel_4_63d(revenue: pd.Series) -> pd.Series:
    """acmn_173_dummy_vel_4_63d"""
    return (revenue.pct_change(21)).shift(63)

def acmn_174_dummy_vel_4_126d(revenue: pd.Series) -> pd.Series:
    """acmn_174_dummy_vel_4_126d"""
    return (revenue.pct_change(21)).shift(126)

def acmn_175_dummy_vel_4_252d(revenue: pd.Series) -> pd.Series:
    """acmn_175_dummy_vel_4_252d"""
    return (revenue.pct_change(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V70_REGISTRY_2ND = {
    "acmn_151_dummy_vel_0_5d": {"inputs": ['revenue'], "func": acmn_151_dummy_vel_0_5d},
    "acmn_152_dummy_vel_0_21d": {"inputs": ['revenue'], "func": acmn_152_dummy_vel_0_21d},
    "acmn_153_dummy_vel_0_63d": {"inputs": ['revenue'], "func": acmn_153_dummy_vel_0_63d},
    "acmn_154_dummy_vel_0_126d": {"inputs": ['revenue'], "func": acmn_154_dummy_vel_0_126d},
    "acmn_155_dummy_vel_0_252d": {"inputs": ['revenue'], "func": acmn_155_dummy_vel_0_252d},
    "acmn_156_dummy_vel_1_5d": {"inputs": ['revenue'], "func": acmn_156_dummy_vel_1_5d},
    "acmn_157_dummy_vel_1_21d": {"inputs": ['revenue'], "func": acmn_157_dummy_vel_1_21d},
    "acmn_158_dummy_vel_1_63d": {"inputs": ['revenue'], "func": acmn_158_dummy_vel_1_63d},
    "acmn_159_dummy_vel_1_126d": {"inputs": ['revenue'], "func": acmn_159_dummy_vel_1_126d},
    "acmn_160_dummy_vel_1_252d": {"inputs": ['revenue'], "func": acmn_160_dummy_vel_1_252d},
    "acmn_161_dummy_vel_2_5d": {"inputs": ['revenue'], "func": acmn_161_dummy_vel_2_5d},
    "acmn_162_dummy_vel_2_21d": {"inputs": ['revenue'], "func": acmn_162_dummy_vel_2_21d},
    "acmn_163_dummy_vel_2_63d": {"inputs": ['revenue'], "func": acmn_163_dummy_vel_2_63d},
    "acmn_164_dummy_vel_2_126d": {"inputs": ['revenue'], "func": acmn_164_dummy_vel_2_126d},
    "acmn_165_dummy_vel_2_252d": {"inputs": ['revenue'], "func": acmn_165_dummy_vel_2_252d},
    "acmn_166_dummy_vel_3_5d": {"inputs": ['revenue'], "func": acmn_166_dummy_vel_3_5d},
    "acmn_167_dummy_vel_3_21d": {"inputs": ['revenue'], "func": acmn_167_dummy_vel_3_21d},
    "acmn_168_dummy_vel_3_63d": {"inputs": ['revenue'], "func": acmn_168_dummy_vel_3_63d},
    "acmn_169_dummy_vel_3_126d": {"inputs": ['revenue'], "func": acmn_169_dummy_vel_3_126d},
    "acmn_170_dummy_vel_3_252d": {"inputs": ['revenue'], "func": acmn_170_dummy_vel_3_252d},
    "acmn_171_dummy_vel_4_5d": {"inputs": ['revenue'], "func": acmn_171_dummy_vel_4_5d},
    "acmn_172_dummy_vel_4_21d": {"inputs": ['revenue'], "func": acmn_172_dummy_vel_4_21d},
    "acmn_173_dummy_vel_4_63d": {"inputs": ['revenue'], "func": acmn_173_dummy_vel_4_63d},
    "acmn_174_dummy_vel_4_126d": {"inputs": ['revenue'], "func": acmn_174_dummy_vel_4_126d},
    "acmn_175_dummy_vel_4_252d": {"inputs": ['revenue'], "func": acmn_175_dummy_vel_4_252d},
}
