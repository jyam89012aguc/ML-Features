"""
73_balance_sheet_death_spiral — 2nd Derivatives
Domain: Assets shrinking + Liabs growing
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

def bsds_151_dummy_vel_0_5d(revenue: pd.Series) -> pd.Series:
    """bsds_151_dummy_vel_0_5d"""
    return (revenue.pct_change(21)).shift(5)

def bsds_152_dummy_vel_0_21d(revenue: pd.Series) -> pd.Series:
    """bsds_152_dummy_vel_0_21d"""
    return (revenue.pct_change(21)).shift(21)

def bsds_153_dummy_vel_0_63d(revenue: pd.Series) -> pd.Series:
    """bsds_153_dummy_vel_0_63d"""
    return (revenue.pct_change(21)).shift(63)

def bsds_154_dummy_vel_0_126d(revenue: pd.Series) -> pd.Series:
    """bsds_154_dummy_vel_0_126d"""
    return (revenue.pct_change(21)).shift(126)

def bsds_155_dummy_vel_0_252d(revenue: pd.Series) -> pd.Series:
    """bsds_155_dummy_vel_0_252d"""
    return (revenue.pct_change(21)).shift(252)

def bsds_156_dummy_vel_1_5d(revenue: pd.Series) -> pd.Series:
    """bsds_156_dummy_vel_1_5d"""
    return (revenue.pct_change(21)).shift(5)

def bsds_157_dummy_vel_1_21d(revenue: pd.Series) -> pd.Series:
    """bsds_157_dummy_vel_1_21d"""
    return (revenue.pct_change(21)).shift(21)

def bsds_158_dummy_vel_1_63d(revenue: pd.Series) -> pd.Series:
    """bsds_158_dummy_vel_1_63d"""
    return (revenue.pct_change(21)).shift(63)

def bsds_159_dummy_vel_1_126d(revenue: pd.Series) -> pd.Series:
    """bsds_159_dummy_vel_1_126d"""
    return (revenue.pct_change(21)).shift(126)

def bsds_160_dummy_vel_1_252d(revenue: pd.Series) -> pd.Series:
    """bsds_160_dummy_vel_1_252d"""
    return (revenue.pct_change(21)).shift(252)

def bsds_161_dummy_vel_2_5d(revenue: pd.Series) -> pd.Series:
    """bsds_161_dummy_vel_2_5d"""
    return (revenue.pct_change(21)).shift(5)

def bsds_162_dummy_vel_2_21d(revenue: pd.Series) -> pd.Series:
    """bsds_162_dummy_vel_2_21d"""
    return (revenue.pct_change(21)).shift(21)

def bsds_163_dummy_vel_2_63d(revenue: pd.Series) -> pd.Series:
    """bsds_163_dummy_vel_2_63d"""
    return (revenue.pct_change(21)).shift(63)

def bsds_164_dummy_vel_2_126d(revenue: pd.Series) -> pd.Series:
    """bsds_164_dummy_vel_2_126d"""
    return (revenue.pct_change(21)).shift(126)

def bsds_165_dummy_vel_2_252d(revenue: pd.Series) -> pd.Series:
    """bsds_165_dummy_vel_2_252d"""
    return (revenue.pct_change(21)).shift(252)

def bsds_166_dummy_vel_3_5d(revenue: pd.Series) -> pd.Series:
    """bsds_166_dummy_vel_3_5d"""
    return (revenue.pct_change(21)).shift(5)

def bsds_167_dummy_vel_3_21d(revenue: pd.Series) -> pd.Series:
    """bsds_167_dummy_vel_3_21d"""
    return (revenue.pct_change(21)).shift(21)

def bsds_168_dummy_vel_3_63d(revenue: pd.Series) -> pd.Series:
    """bsds_168_dummy_vel_3_63d"""
    return (revenue.pct_change(21)).shift(63)

def bsds_169_dummy_vel_3_126d(revenue: pd.Series) -> pd.Series:
    """bsds_169_dummy_vel_3_126d"""
    return (revenue.pct_change(21)).shift(126)

def bsds_170_dummy_vel_3_252d(revenue: pd.Series) -> pd.Series:
    """bsds_170_dummy_vel_3_252d"""
    return (revenue.pct_change(21)).shift(252)

def bsds_171_dummy_vel_4_5d(revenue: pd.Series) -> pd.Series:
    """bsds_171_dummy_vel_4_5d"""
    return (revenue.pct_change(21)).shift(5)

def bsds_172_dummy_vel_4_21d(revenue: pd.Series) -> pd.Series:
    """bsds_172_dummy_vel_4_21d"""
    return (revenue.pct_change(21)).shift(21)

def bsds_173_dummy_vel_4_63d(revenue: pd.Series) -> pd.Series:
    """bsds_173_dummy_vel_4_63d"""
    return (revenue.pct_change(21)).shift(63)

def bsds_174_dummy_vel_4_126d(revenue: pd.Series) -> pd.Series:
    """bsds_174_dummy_vel_4_126d"""
    return (revenue.pct_change(21)).shift(126)

def bsds_175_dummy_vel_4_252d(revenue: pd.Series) -> pd.Series:
    """bsds_175_dummy_vel_4_252d"""
    return (revenue.pct_change(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V73_REGISTRY_2ND = {
    "bsds_151_dummy_vel_0_5d": {"inputs": ['revenue'], "func": bsds_151_dummy_vel_0_5d},
    "bsds_152_dummy_vel_0_21d": {"inputs": ['revenue'], "func": bsds_152_dummy_vel_0_21d},
    "bsds_153_dummy_vel_0_63d": {"inputs": ['revenue'], "func": bsds_153_dummy_vel_0_63d},
    "bsds_154_dummy_vel_0_126d": {"inputs": ['revenue'], "func": bsds_154_dummy_vel_0_126d},
    "bsds_155_dummy_vel_0_252d": {"inputs": ['revenue'], "func": bsds_155_dummy_vel_0_252d},
    "bsds_156_dummy_vel_1_5d": {"inputs": ['revenue'], "func": bsds_156_dummy_vel_1_5d},
    "bsds_157_dummy_vel_1_21d": {"inputs": ['revenue'], "func": bsds_157_dummy_vel_1_21d},
    "bsds_158_dummy_vel_1_63d": {"inputs": ['revenue'], "func": bsds_158_dummy_vel_1_63d},
    "bsds_159_dummy_vel_1_126d": {"inputs": ['revenue'], "func": bsds_159_dummy_vel_1_126d},
    "bsds_160_dummy_vel_1_252d": {"inputs": ['revenue'], "func": bsds_160_dummy_vel_1_252d},
    "bsds_161_dummy_vel_2_5d": {"inputs": ['revenue'], "func": bsds_161_dummy_vel_2_5d},
    "bsds_162_dummy_vel_2_21d": {"inputs": ['revenue'], "func": bsds_162_dummy_vel_2_21d},
    "bsds_163_dummy_vel_2_63d": {"inputs": ['revenue'], "func": bsds_163_dummy_vel_2_63d},
    "bsds_164_dummy_vel_2_126d": {"inputs": ['revenue'], "func": bsds_164_dummy_vel_2_126d},
    "bsds_165_dummy_vel_2_252d": {"inputs": ['revenue'], "func": bsds_165_dummy_vel_2_252d},
    "bsds_166_dummy_vel_3_5d": {"inputs": ['revenue'], "func": bsds_166_dummy_vel_3_5d},
    "bsds_167_dummy_vel_3_21d": {"inputs": ['revenue'], "func": bsds_167_dummy_vel_3_21d},
    "bsds_168_dummy_vel_3_63d": {"inputs": ['revenue'], "func": bsds_168_dummy_vel_3_63d},
    "bsds_169_dummy_vel_3_126d": {"inputs": ['revenue'], "func": bsds_169_dummy_vel_3_126d},
    "bsds_170_dummy_vel_3_252d": {"inputs": ['revenue'], "func": bsds_170_dummy_vel_3_252d},
    "bsds_171_dummy_vel_4_5d": {"inputs": ['revenue'], "func": bsds_171_dummy_vel_4_5d},
    "bsds_172_dummy_vel_4_21d": {"inputs": ['revenue'], "func": bsds_172_dummy_vel_4_21d},
    "bsds_173_dummy_vel_4_63d": {"inputs": ['revenue'], "func": bsds_173_dummy_vel_4_63d},
    "bsds_174_dummy_vel_4_126d": {"inputs": ['revenue'], "func": bsds_174_dummy_vel_4_126d},
    "bsds_175_dummy_vel_4_252d": {"inputs": ['revenue'], "func": bsds_175_dummy_vel_4_252d},
}
