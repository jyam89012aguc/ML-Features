"""
67_moat_trajectory — 2nd Derivatives
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

def moat_151_dummy_vel_0_5d(revenue: pd.Series) -> pd.Series:
    """moat_151_dummy_vel_0_5d"""
    return (revenue.pct_change(21)).shift(5)

def moat_152_dummy_vel_0_21d(revenue: pd.Series) -> pd.Series:
    """moat_152_dummy_vel_0_21d"""
    return (revenue.pct_change(21)).shift(21)

def moat_153_dummy_vel_0_63d(revenue: pd.Series) -> pd.Series:
    """moat_153_dummy_vel_0_63d"""
    return (revenue.pct_change(21)).shift(63)

def moat_154_dummy_vel_0_126d(revenue: pd.Series) -> pd.Series:
    """moat_154_dummy_vel_0_126d"""
    return (revenue.pct_change(21)).shift(126)

def moat_155_dummy_vel_0_252d(revenue: pd.Series) -> pd.Series:
    """moat_155_dummy_vel_0_252d"""
    return (revenue.pct_change(21)).shift(252)

def moat_156_dummy_vel_1_5d(revenue: pd.Series) -> pd.Series:
    """moat_156_dummy_vel_1_5d"""
    return (revenue.pct_change(21)).shift(5)

def moat_157_dummy_vel_1_21d(revenue: pd.Series) -> pd.Series:
    """moat_157_dummy_vel_1_21d"""
    return (revenue.pct_change(21)).shift(21)

def moat_158_dummy_vel_1_63d(revenue: pd.Series) -> pd.Series:
    """moat_158_dummy_vel_1_63d"""
    return (revenue.pct_change(21)).shift(63)

def moat_159_dummy_vel_1_126d(revenue: pd.Series) -> pd.Series:
    """moat_159_dummy_vel_1_126d"""
    return (revenue.pct_change(21)).shift(126)

def moat_160_dummy_vel_1_252d(revenue: pd.Series) -> pd.Series:
    """moat_160_dummy_vel_1_252d"""
    return (revenue.pct_change(21)).shift(252)

def moat_161_dummy_vel_2_5d(revenue: pd.Series) -> pd.Series:
    """moat_161_dummy_vel_2_5d"""
    return (revenue.pct_change(21)).shift(5)

def moat_162_dummy_vel_2_21d(revenue: pd.Series) -> pd.Series:
    """moat_162_dummy_vel_2_21d"""
    return (revenue.pct_change(21)).shift(21)

def moat_163_dummy_vel_2_63d(revenue: pd.Series) -> pd.Series:
    """moat_163_dummy_vel_2_63d"""
    return (revenue.pct_change(21)).shift(63)

def moat_164_dummy_vel_2_126d(revenue: pd.Series) -> pd.Series:
    """moat_164_dummy_vel_2_126d"""
    return (revenue.pct_change(21)).shift(126)

def moat_165_dummy_vel_2_252d(revenue: pd.Series) -> pd.Series:
    """moat_165_dummy_vel_2_252d"""
    return (revenue.pct_change(21)).shift(252)

def moat_166_dummy_vel_3_5d(revenue: pd.Series) -> pd.Series:
    """moat_166_dummy_vel_3_5d"""
    return (revenue.pct_change(21)).shift(5)

def moat_167_dummy_vel_3_21d(revenue: pd.Series) -> pd.Series:
    """moat_167_dummy_vel_3_21d"""
    return (revenue.pct_change(21)).shift(21)

def moat_168_dummy_vel_3_63d(revenue: pd.Series) -> pd.Series:
    """moat_168_dummy_vel_3_63d"""
    return (revenue.pct_change(21)).shift(63)

def moat_169_dummy_vel_3_126d(revenue: pd.Series) -> pd.Series:
    """moat_169_dummy_vel_3_126d"""
    return (revenue.pct_change(21)).shift(126)

def moat_170_dummy_vel_3_252d(revenue: pd.Series) -> pd.Series:
    """moat_170_dummy_vel_3_252d"""
    return (revenue.pct_change(21)).shift(252)

def moat_171_dummy_vel_4_5d(revenue: pd.Series) -> pd.Series:
    """moat_171_dummy_vel_4_5d"""
    return (revenue.pct_change(21)).shift(5)

def moat_172_dummy_vel_4_21d(revenue: pd.Series) -> pd.Series:
    """moat_172_dummy_vel_4_21d"""
    return (revenue.pct_change(21)).shift(21)

def moat_173_dummy_vel_4_63d(revenue: pd.Series) -> pd.Series:
    """moat_173_dummy_vel_4_63d"""
    return (revenue.pct_change(21)).shift(63)

def moat_174_dummy_vel_4_126d(revenue: pd.Series) -> pd.Series:
    """moat_174_dummy_vel_4_126d"""
    return (revenue.pct_change(21)).shift(126)

def moat_175_dummy_vel_4_252d(revenue: pd.Series) -> pd.Series:
    """moat_175_dummy_vel_4_252d"""
    return (revenue.pct_change(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V67_REGISTRY_2ND = {
    "moat_151_dummy_vel_0_5d": {"inputs": ['revenue'], "func": moat_151_dummy_vel_0_5d},
    "moat_152_dummy_vel_0_21d": {"inputs": ['revenue'], "func": moat_152_dummy_vel_0_21d},
    "moat_153_dummy_vel_0_63d": {"inputs": ['revenue'], "func": moat_153_dummy_vel_0_63d},
    "moat_154_dummy_vel_0_126d": {"inputs": ['revenue'], "func": moat_154_dummy_vel_0_126d},
    "moat_155_dummy_vel_0_252d": {"inputs": ['revenue'], "func": moat_155_dummy_vel_0_252d},
    "moat_156_dummy_vel_1_5d": {"inputs": ['revenue'], "func": moat_156_dummy_vel_1_5d},
    "moat_157_dummy_vel_1_21d": {"inputs": ['revenue'], "func": moat_157_dummy_vel_1_21d},
    "moat_158_dummy_vel_1_63d": {"inputs": ['revenue'], "func": moat_158_dummy_vel_1_63d},
    "moat_159_dummy_vel_1_126d": {"inputs": ['revenue'], "func": moat_159_dummy_vel_1_126d},
    "moat_160_dummy_vel_1_252d": {"inputs": ['revenue'], "func": moat_160_dummy_vel_1_252d},
    "moat_161_dummy_vel_2_5d": {"inputs": ['revenue'], "func": moat_161_dummy_vel_2_5d},
    "moat_162_dummy_vel_2_21d": {"inputs": ['revenue'], "func": moat_162_dummy_vel_2_21d},
    "moat_163_dummy_vel_2_63d": {"inputs": ['revenue'], "func": moat_163_dummy_vel_2_63d},
    "moat_164_dummy_vel_2_126d": {"inputs": ['revenue'], "func": moat_164_dummy_vel_2_126d},
    "moat_165_dummy_vel_2_252d": {"inputs": ['revenue'], "func": moat_165_dummy_vel_2_252d},
    "moat_166_dummy_vel_3_5d": {"inputs": ['revenue'], "func": moat_166_dummy_vel_3_5d},
    "moat_167_dummy_vel_3_21d": {"inputs": ['revenue'], "func": moat_167_dummy_vel_3_21d},
    "moat_168_dummy_vel_3_63d": {"inputs": ['revenue'], "func": moat_168_dummy_vel_3_63d},
    "moat_169_dummy_vel_3_126d": {"inputs": ['revenue'], "func": moat_169_dummy_vel_3_126d},
    "moat_170_dummy_vel_3_252d": {"inputs": ['revenue'], "func": moat_170_dummy_vel_3_252d},
    "moat_171_dummy_vel_4_5d": {"inputs": ['revenue'], "func": moat_171_dummy_vel_4_5d},
    "moat_172_dummy_vel_4_21d": {"inputs": ['revenue'], "func": moat_172_dummy_vel_4_21d},
    "moat_173_dummy_vel_4_63d": {"inputs": ['revenue'], "func": moat_173_dummy_vel_4_63d},
    "moat_174_dummy_vel_4_126d": {"inputs": ['revenue'], "func": moat_174_dummy_vel_4_126d},
    "moat_175_dummy_vel_4_252d": {"inputs": ['revenue'], "func": moat_175_dummy_vel_4_252d},
}
