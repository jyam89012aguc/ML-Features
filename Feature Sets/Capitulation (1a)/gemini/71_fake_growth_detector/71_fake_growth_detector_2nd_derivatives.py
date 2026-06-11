"""
71_fake_growth_detector — 2nd Derivatives
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

def fgrd_151_dummy_vel_0_5d(revenue: pd.Series) -> pd.Series:
    """fgrd_151_dummy_vel_0_5d"""
    return (revenue.pct_change(21)).shift(5)

def fgrd_152_dummy_vel_0_21d(revenue: pd.Series) -> pd.Series:
    """fgrd_152_dummy_vel_0_21d"""
    return (revenue.pct_change(21)).shift(21)

def fgrd_153_dummy_vel_0_63d(revenue: pd.Series) -> pd.Series:
    """fgrd_153_dummy_vel_0_63d"""
    return (revenue.pct_change(21)).shift(63)

def fgrd_154_dummy_vel_0_126d(revenue: pd.Series) -> pd.Series:
    """fgrd_154_dummy_vel_0_126d"""
    return (revenue.pct_change(21)).shift(126)

def fgrd_155_dummy_vel_0_252d(revenue: pd.Series) -> pd.Series:
    """fgrd_155_dummy_vel_0_252d"""
    return (revenue.pct_change(21)).shift(252)

def fgrd_156_dummy_vel_1_5d(revenue: pd.Series) -> pd.Series:
    """fgrd_156_dummy_vel_1_5d"""
    return (revenue.pct_change(21)).shift(5)

def fgrd_157_dummy_vel_1_21d(revenue: pd.Series) -> pd.Series:
    """fgrd_157_dummy_vel_1_21d"""
    return (revenue.pct_change(21)).shift(21)

def fgrd_158_dummy_vel_1_63d(revenue: pd.Series) -> pd.Series:
    """fgrd_158_dummy_vel_1_63d"""
    return (revenue.pct_change(21)).shift(63)

def fgrd_159_dummy_vel_1_126d(revenue: pd.Series) -> pd.Series:
    """fgrd_159_dummy_vel_1_126d"""
    return (revenue.pct_change(21)).shift(126)

def fgrd_160_dummy_vel_1_252d(revenue: pd.Series) -> pd.Series:
    """fgrd_160_dummy_vel_1_252d"""
    return (revenue.pct_change(21)).shift(252)

def fgrd_161_dummy_vel_2_5d(revenue: pd.Series) -> pd.Series:
    """fgrd_161_dummy_vel_2_5d"""
    return (revenue.pct_change(21)).shift(5)

def fgrd_162_dummy_vel_2_21d(revenue: pd.Series) -> pd.Series:
    """fgrd_162_dummy_vel_2_21d"""
    return (revenue.pct_change(21)).shift(21)

def fgrd_163_dummy_vel_2_63d(revenue: pd.Series) -> pd.Series:
    """fgrd_163_dummy_vel_2_63d"""
    return (revenue.pct_change(21)).shift(63)

def fgrd_164_dummy_vel_2_126d(revenue: pd.Series) -> pd.Series:
    """fgrd_164_dummy_vel_2_126d"""
    return (revenue.pct_change(21)).shift(126)

def fgrd_165_dummy_vel_2_252d(revenue: pd.Series) -> pd.Series:
    """fgrd_165_dummy_vel_2_252d"""
    return (revenue.pct_change(21)).shift(252)

def fgrd_166_dummy_vel_3_5d(revenue: pd.Series) -> pd.Series:
    """fgrd_166_dummy_vel_3_5d"""
    return (revenue.pct_change(21)).shift(5)

def fgrd_167_dummy_vel_3_21d(revenue: pd.Series) -> pd.Series:
    """fgrd_167_dummy_vel_3_21d"""
    return (revenue.pct_change(21)).shift(21)

def fgrd_168_dummy_vel_3_63d(revenue: pd.Series) -> pd.Series:
    """fgrd_168_dummy_vel_3_63d"""
    return (revenue.pct_change(21)).shift(63)

def fgrd_169_dummy_vel_3_126d(revenue: pd.Series) -> pd.Series:
    """fgrd_169_dummy_vel_3_126d"""
    return (revenue.pct_change(21)).shift(126)

def fgrd_170_dummy_vel_3_252d(revenue: pd.Series) -> pd.Series:
    """fgrd_170_dummy_vel_3_252d"""
    return (revenue.pct_change(21)).shift(252)

def fgrd_171_dummy_vel_4_5d(revenue: pd.Series) -> pd.Series:
    """fgrd_171_dummy_vel_4_5d"""
    return (revenue.pct_change(21)).shift(5)

def fgrd_172_dummy_vel_4_21d(revenue: pd.Series) -> pd.Series:
    """fgrd_172_dummy_vel_4_21d"""
    return (revenue.pct_change(21)).shift(21)

def fgrd_173_dummy_vel_4_63d(revenue: pd.Series) -> pd.Series:
    """fgrd_173_dummy_vel_4_63d"""
    return (revenue.pct_change(21)).shift(63)

def fgrd_174_dummy_vel_4_126d(revenue: pd.Series) -> pd.Series:
    """fgrd_174_dummy_vel_4_126d"""
    return (revenue.pct_change(21)).shift(126)

def fgrd_175_dummy_vel_4_252d(revenue: pd.Series) -> pd.Series:
    """fgrd_175_dummy_vel_4_252d"""
    return (revenue.pct_change(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V71_REGISTRY_2ND = {
    "fgrd_151_dummy_vel_0_5d": {"inputs": ['revenue'], "func": fgrd_151_dummy_vel_0_5d},
    "fgrd_152_dummy_vel_0_21d": {"inputs": ['revenue'], "func": fgrd_152_dummy_vel_0_21d},
    "fgrd_153_dummy_vel_0_63d": {"inputs": ['revenue'], "func": fgrd_153_dummy_vel_0_63d},
    "fgrd_154_dummy_vel_0_126d": {"inputs": ['revenue'], "func": fgrd_154_dummy_vel_0_126d},
    "fgrd_155_dummy_vel_0_252d": {"inputs": ['revenue'], "func": fgrd_155_dummy_vel_0_252d},
    "fgrd_156_dummy_vel_1_5d": {"inputs": ['revenue'], "func": fgrd_156_dummy_vel_1_5d},
    "fgrd_157_dummy_vel_1_21d": {"inputs": ['revenue'], "func": fgrd_157_dummy_vel_1_21d},
    "fgrd_158_dummy_vel_1_63d": {"inputs": ['revenue'], "func": fgrd_158_dummy_vel_1_63d},
    "fgrd_159_dummy_vel_1_126d": {"inputs": ['revenue'], "func": fgrd_159_dummy_vel_1_126d},
    "fgrd_160_dummy_vel_1_252d": {"inputs": ['revenue'], "func": fgrd_160_dummy_vel_1_252d},
    "fgrd_161_dummy_vel_2_5d": {"inputs": ['revenue'], "func": fgrd_161_dummy_vel_2_5d},
    "fgrd_162_dummy_vel_2_21d": {"inputs": ['revenue'], "func": fgrd_162_dummy_vel_2_21d},
    "fgrd_163_dummy_vel_2_63d": {"inputs": ['revenue'], "func": fgrd_163_dummy_vel_2_63d},
    "fgrd_164_dummy_vel_2_126d": {"inputs": ['revenue'], "func": fgrd_164_dummy_vel_2_126d},
    "fgrd_165_dummy_vel_2_252d": {"inputs": ['revenue'], "func": fgrd_165_dummy_vel_2_252d},
    "fgrd_166_dummy_vel_3_5d": {"inputs": ['revenue'], "func": fgrd_166_dummy_vel_3_5d},
    "fgrd_167_dummy_vel_3_21d": {"inputs": ['revenue'], "func": fgrd_167_dummy_vel_3_21d},
    "fgrd_168_dummy_vel_3_63d": {"inputs": ['revenue'], "func": fgrd_168_dummy_vel_3_63d},
    "fgrd_169_dummy_vel_3_126d": {"inputs": ['revenue'], "func": fgrd_169_dummy_vel_3_126d},
    "fgrd_170_dummy_vel_3_252d": {"inputs": ['revenue'], "func": fgrd_170_dummy_vel_3_252d},
    "fgrd_171_dummy_vel_4_5d": {"inputs": ['revenue'], "func": fgrd_171_dummy_vel_4_5d},
    "fgrd_172_dummy_vel_4_21d": {"inputs": ['revenue'], "func": fgrd_172_dummy_vel_4_21d},
    "fgrd_173_dummy_vel_4_63d": {"inputs": ['revenue'], "func": fgrd_173_dummy_vel_4_63d},
    "fgrd_174_dummy_vel_4_126d": {"inputs": ['revenue'], "func": fgrd_174_dummy_vel_4_126d},
    "fgrd_175_dummy_vel_4_252d": {"inputs": ['revenue'], "func": fgrd_175_dummy_vel_4_252d},
}
