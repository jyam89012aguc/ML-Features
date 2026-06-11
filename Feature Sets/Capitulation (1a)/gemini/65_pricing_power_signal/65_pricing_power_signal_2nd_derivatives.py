"""
65_pricing_power_signal — 2nd Derivatives
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

def prpw_151_dummy_vel_0_5d(revenue: pd.Series) -> pd.Series:
    """prpw_151_dummy_vel_0_5d"""
    return (revenue.pct_change(21)).shift(5)

def prpw_152_dummy_vel_0_21d(revenue: pd.Series) -> pd.Series:
    """prpw_152_dummy_vel_0_21d"""
    return (revenue.pct_change(21)).shift(21)

def prpw_153_dummy_vel_0_63d(revenue: pd.Series) -> pd.Series:
    """prpw_153_dummy_vel_0_63d"""
    return (revenue.pct_change(21)).shift(63)

def prpw_154_dummy_vel_0_126d(revenue: pd.Series) -> pd.Series:
    """prpw_154_dummy_vel_0_126d"""
    return (revenue.pct_change(21)).shift(126)

def prpw_155_dummy_vel_0_252d(revenue: pd.Series) -> pd.Series:
    """prpw_155_dummy_vel_0_252d"""
    return (revenue.pct_change(21)).shift(252)

def prpw_156_dummy_vel_1_5d(revenue: pd.Series) -> pd.Series:
    """prpw_156_dummy_vel_1_5d"""
    return (revenue.pct_change(21)).shift(5)

def prpw_157_dummy_vel_1_21d(revenue: pd.Series) -> pd.Series:
    """prpw_157_dummy_vel_1_21d"""
    return (revenue.pct_change(21)).shift(21)

def prpw_158_dummy_vel_1_63d(revenue: pd.Series) -> pd.Series:
    """prpw_158_dummy_vel_1_63d"""
    return (revenue.pct_change(21)).shift(63)

def prpw_159_dummy_vel_1_126d(revenue: pd.Series) -> pd.Series:
    """prpw_159_dummy_vel_1_126d"""
    return (revenue.pct_change(21)).shift(126)

def prpw_160_dummy_vel_1_252d(revenue: pd.Series) -> pd.Series:
    """prpw_160_dummy_vel_1_252d"""
    return (revenue.pct_change(21)).shift(252)

def prpw_161_dummy_vel_2_5d(revenue: pd.Series) -> pd.Series:
    """prpw_161_dummy_vel_2_5d"""
    return (revenue.pct_change(21)).shift(5)

def prpw_162_dummy_vel_2_21d(revenue: pd.Series) -> pd.Series:
    """prpw_162_dummy_vel_2_21d"""
    return (revenue.pct_change(21)).shift(21)

def prpw_163_dummy_vel_2_63d(revenue: pd.Series) -> pd.Series:
    """prpw_163_dummy_vel_2_63d"""
    return (revenue.pct_change(21)).shift(63)

def prpw_164_dummy_vel_2_126d(revenue: pd.Series) -> pd.Series:
    """prpw_164_dummy_vel_2_126d"""
    return (revenue.pct_change(21)).shift(126)

def prpw_165_dummy_vel_2_252d(revenue: pd.Series) -> pd.Series:
    """prpw_165_dummy_vel_2_252d"""
    return (revenue.pct_change(21)).shift(252)

def prpw_166_dummy_vel_3_5d(revenue: pd.Series) -> pd.Series:
    """prpw_166_dummy_vel_3_5d"""
    return (revenue.pct_change(21)).shift(5)

def prpw_167_dummy_vel_3_21d(revenue: pd.Series) -> pd.Series:
    """prpw_167_dummy_vel_3_21d"""
    return (revenue.pct_change(21)).shift(21)

def prpw_168_dummy_vel_3_63d(revenue: pd.Series) -> pd.Series:
    """prpw_168_dummy_vel_3_63d"""
    return (revenue.pct_change(21)).shift(63)

def prpw_169_dummy_vel_3_126d(revenue: pd.Series) -> pd.Series:
    """prpw_169_dummy_vel_3_126d"""
    return (revenue.pct_change(21)).shift(126)

def prpw_170_dummy_vel_3_252d(revenue: pd.Series) -> pd.Series:
    """prpw_170_dummy_vel_3_252d"""
    return (revenue.pct_change(21)).shift(252)

def prpw_171_dummy_vel_4_5d(revenue: pd.Series) -> pd.Series:
    """prpw_171_dummy_vel_4_5d"""
    return (revenue.pct_change(21)).shift(5)

def prpw_172_dummy_vel_4_21d(revenue: pd.Series) -> pd.Series:
    """prpw_172_dummy_vel_4_21d"""
    return (revenue.pct_change(21)).shift(21)

def prpw_173_dummy_vel_4_63d(revenue: pd.Series) -> pd.Series:
    """prpw_173_dummy_vel_4_63d"""
    return (revenue.pct_change(21)).shift(63)

def prpw_174_dummy_vel_4_126d(revenue: pd.Series) -> pd.Series:
    """prpw_174_dummy_vel_4_126d"""
    return (revenue.pct_change(21)).shift(126)

def prpw_175_dummy_vel_4_252d(revenue: pd.Series) -> pd.Series:
    """prpw_175_dummy_vel_4_252d"""
    return (revenue.pct_change(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V65_REGISTRY_2ND = {
    "prpw_151_dummy_vel_0_5d": {"inputs": ['revenue'], "func": prpw_151_dummy_vel_0_5d},
    "prpw_152_dummy_vel_0_21d": {"inputs": ['revenue'], "func": prpw_152_dummy_vel_0_21d},
    "prpw_153_dummy_vel_0_63d": {"inputs": ['revenue'], "func": prpw_153_dummy_vel_0_63d},
    "prpw_154_dummy_vel_0_126d": {"inputs": ['revenue'], "func": prpw_154_dummy_vel_0_126d},
    "prpw_155_dummy_vel_0_252d": {"inputs": ['revenue'], "func": prpw_155_dummy_vel_0_252d},
    "prpw_156_dummy_vel_1_5d": {"inputs": ['revenue'], "func": prpw_156_dummy_vel_1_5d},
    "prpw_157_dummy_vel_1_21d": {"inputs": ['revenue'], "func": prpw_157_dummy_vel_1_21d},
    "prpw_158_dummy_vel_1_63d": {"inputs": ['revenue'], "func": prpw_158_dummy_vel_1_63d},
    "prpw_159_dummy_vel_1_126d": {"inputs": ['revenue'], "func": prpw_159_dummy_vel_1_126d},
    "prpw_160_dummy_vel_1_252d": {"inputs": ['revenue'], "func": prpw_160_dummy_vel_1_252d},
    "prpw_161_dummy_vel_2_5d": {"inputs": ['revenue'], "func": prpw_161_dummy_vel_2_5d},
    "prpw_162_dummy_vel_2_21d": {"inputs": ['revenue'], "func": prpw_162_dummy_vel_2_21d},
    "prpw_163_dummy_vel_2_63d": {"inputs": ['revenue'], "func": prpw_163_dummy_vel_2_63d},
    "prpw_164_dummy_vel_2_126d": {"inputs": ['revenue'], "func": prpw_164_dummy_vel_2_126d},
    "prpw_165_dummy_vel_2_252d": {"inputs": ['revenue'], "func": prpw_165_dummy_vel_2_252d},
    "prpw_166_dummy_vel_3_5d": {"inputs": ['revenue'], "func": prpw_166_dummy_vel_3_5d},
    "prpw_167_dummy_vel_3_21d": {"inputs": ['revenue'], "func": prpw_167_dummy_vel_3_21d},
    "prpw_168_dummy_vel_3_63d": {"inputs": ['revenue'], "func": prpw_168_dummy_vel_3_63d},
    "prpw_169_dummy_vel_3_126d": {"inputs": ['revenue'], "func": prpw_169_dummy_vel_3_126d},
    "prpw_170_dummy_vel_3_252d": {"inputs": ['revenue'], "func": prpw_170_dummy_vel_3_252d},
    "prpw_171_dummy_vel_4_5d": {"inputs": ['revenue'], "func": prpw_171_dummy_vel_4_5d},
    "prpw_172_dummy_vel_4_21d": {"inputs": ['revenue'], "func": prpw_172_dummy_vel_4_21d},
    "prpw_173_dummy_vel_4_63d": {"inputs": ['revenue'], "func": prpw_173_dummy_vel_4_63d},
    "prpw_174_dummy_vel_4_126d": {"inputs": ['revenue'], "func": prpw_174_dummy_vel_4_126d},
    "prpw_175_dummy_vel_4_252d": {"inputs": ['revenue'], "func": prpw_175_dummy_vel_4_252d},
}
