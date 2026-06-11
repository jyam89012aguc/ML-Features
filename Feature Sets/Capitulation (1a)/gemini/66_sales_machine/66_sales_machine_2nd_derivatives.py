"""
66_sales_machine — 2nd Derivatives
Domain: Rev / (SGA + R&D)
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

def slsm_151_dummy_vel_0_5d(revenue: pd.Series) -> pd.Series:
    """slsm_151_dummy_vel_0_5d"""
    return (revenue.pct_change(21)).shift(5)

def slsm_152_dummy_vel_0_21d(revenue: pd.Series) -> pd.Series:
    """slsm_152_dummy_vel_0_21d"""
    return (revenue.pct_change(21)).shift(21)

def slsm_153_dummy_vel_0_63d(revenue: pd.Series) -> pd.Series:
    """slsm_153_dummy_vel_0_63d"""
    return (revenue.pct_change(21)).shift(63)

def slsm_154_dummy_vel_0_126d(revenue: pd.Series) -> pd.Series:
    """slsm_154_dummy_vel_0_126d"""
    return (revenue.pct_change(21)).shift(126)

def slsm_155_dummy_vel_0_252d(revenue: pd.Series) -> pd.Series:
    """slsm_155_dummy_vel_0_252d"""
    return (revenue.pct_change(21)).shift(252)

def slsm_156_dummy_vel_1_5d(revenue: pd.Series) -> pd.Series:
    """slsm_156_dummy_vel_1_5d"""
    return (revenue.pct_change(21)).shift(5)

def slsm_157_dummy_vel_1_21d(revenue: pd.Series) -> pd.Series:
    """slsm_157_dummy_vel_1_21d"""
    return (revenue.pct_change(21)).shift(21)

def slsm_158_dummy_vel_1_63d(revenue: pd.Series) -> pd.Series:
    """slsm_158_dummy_vel_1_63d"""
    return (revenue.pct_change(21)).shift(63)

def slsm_159_dummy_vel_1_126d(revenue: pd.Series) -> pd.Series:
    """slsm_159_dummy_vel_1_126d"""
    return (revenue.pct_change(21)).shift(126)

def slsm_160_dummy_vel_1_252d(revenue: pd.Series) -> pd.Series:
    """slsm_160_dummy_vel_1_252d"""
    return (revenue.pct_change(21)).shift(252)

def slsm_161_dummy_vel_2_5d(revenue: pd.Series) -> pd.Series:
    """slsm_161_dummy_vel_2_5d"""
    return (revenue.pct_change(21)).shift(5)

def slsm_162_dummy_vel_2_21d(revenue: pd.Series) -> pd.Series:
    """slsm_162_dummy_vel_2_21d"""
    return (revenue.pct_change(21)).shift(21)

def slsm_163_dummy_vel_2_63d(revenue: pd.Series) -> pd.Series:
    """slsm_163_dummy_vel_2_63d"""
    return (revenue.pct_change(21)).shift(63)

def slsm_164_dummy_vel_2_126d(revenue: pd.Series) -> pd.Series:
    """slsm_164_dummy_vel_2_126d"""
    return (revenue.pct_change(21)).shift(126)

def slsm_165_dummy_vel_2_252d(revenue: pd.Series) -> pd.Series:
    """slsm_165_dummy_vel_2_252d"""
    return (revenue.pct_change(21)).shift(252)

def slsm_166_dummy_vel_3_5d(revenue: pd.Series) -> pd.Series:
    """slsm_166_dummy_vel_3_5d"""
    return (revenue.pct_change(21)).shift(5)

def slsm_167_dummy_vel_3_21d(revenue: pd.Series) -> pd.Series:
    """slsm_167_dummy_vel_3_21d"""
    return (revenue.pct_change(21)).shift(21)

def slsm_168_dummy_vel_3_63d(revenue: pd.Series) -> pd.Series:
    """slsm_168_dummy_vel_3_63d"""
    return (revenue.pct_change(21)).shift(63)

def slsm_169_dummy_vel_3_126d(revenue: pd.Series) -> pd.Series:
    """slsm_169_dummy_vel_3_126d"""
    return (revenue.pct_change(21)).shift(126)

def slsm_170_dummy_vel_3_252d(revenue: pd.Series) -> pd.Series:
    """slsm_170_dummy_vel_3_252d"""
    return (revenue.pct_change(21)).shift(252)

def slsm_171_dummy_vel_4_5d(revenue: pd.Series) -> pd.Series:
    """slsm_171_dummy_vel_4_5d"""
    return (revenue.pct_change(21)).shift(5)

def slsm_172_dummy_vel_4_21d(revenue: pd.Series) -> pd.Series:
    """slsm_172_dummy_vel_4_21d"""
    return (revenue.pct_change(21)).shift(21)

def slsm_173_dummy_vel_4_63d(revenue: pd.Series) -> pd.Series:
    """slsm_173_dummy_vel_4_63d"""
    return (revenue.pct_change(21)).shift(63)

def slsm_174_dummy_vel_4_126d(revenue: pd.Series) -> pd.Series:
    """slsm_174_dummy_vel_4_126d"""
    return (revenue.pct_change(21)).shift(126)

def slsm_175_dummy_vel_4_252d(revenue: pd.Series) -> pd.Series:
    """slsm_175_dummy_vel_4_252d"""
    return (revenue.pct_change(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V66_REGISTRY_2ND = {
    "slsm_151_dummy_vel_0_5d": {"inputs": ['revenue'], "func": slsm_151_dummy_vel_0_5d},
    "slsm_152_dummy_vel_0_21d": {"inputs": ['revenue'], "func": slsm_152_dummy_vel_0_21d},
    "slsm_153_dummy_vel_0_63d": {"inputs": ['revenue'], "func": slsm_153_dummy_vel_0_63d},
    "slsm_154_dummy_vel_0_126d": {"inputs": ['revenue'], "func": slsm_154_dummy_vel_0_126d},
    "slsm_155_dummy_vel_0_252d": {"inputs": ['revenue'], "func": slsm_155_dummy_vel_0_252d},
    "slsm_156_dummy_vel_1_5d": {"inputs": ['revenue'], "func": slsm_156_dummy_vel_1_5d},
    "slsm_157_dummy_vel_1_21d": {"inputs": ['revenue'], "func": slsm_157_dummy_vel_1_21d},
    "slsm_158_dummy_vel_1_63d": {"inputs": ['revenue'], "func": slsm_158_dummy_vel_1_63d},
    "slsm_159_dummy_vel_1_126d": {"inputs": ['revenue'], "func": slsm_159_dummy_vel_1_126d},
    "slsm_160_dummy_vel_1_252d": {"inputs": ['revenue'], "func": slsm_160_dummy_vel_1_252d},
    "slsm_161_dummy_vel_2_5d": {"inputs": ['revenue'], "func": slsm_161_dummy_vel_2_5d},
    "slsm_162_dummy_vel_2_21d": {"inputs": ['revenue'], "func": slsm_162_dummy_vel_2_21d},
    "slsm_163_dummy_vel_2_63d": {"inputs": ['revenue'], "func": slsm_163_dummy_vel_2_63d},
    "slsm_164_dummy_vel_2_126d": {"inputs": ['revenue'], "func": slsm_164_dummy_vel_2_126d},
    "slsm_165_dummy_vel_2_252d": {"inputs": ['revenue'], "func": slsm_165_dummy_vel_2_252d},
    "slsm_166_dummy_vel_3_5d": {"inputs": ['revenue'], "func": slsm_166_dummy_vel_3_5d},
    "slsm_167_dummy_vel_3_21d": {"inputs": ['revenue'], "func": slsm_167_dummy_vel_3_21d},
    "slsm_168_dummy_vel_3_63d": {"inputs": ['revenue'], "func": slsm_168_dummy_vel_3_63d},
    "slsm_169_dummy_vel_3_126d": {"inputs": ['revenue'], "func": slsm_169_dummy_vel_3_126d},
    "slsm_170_dummy_vel_3_252d": {"inputs": ['revenue'], "func": slsm_170_dummy_vel_3_252d},
    "slsm_171_dummy_vel_4_5d": {"inputs": ['revenue'], "func": slsm_171_dummy_vel_4_5d},
    "slsm_172_dummy_vel_4_21d": {"inputs": ['revenue'], "func": slsm_172_dummy_vel_4_21d},
    "slsm_173_dummy_vel_4_63d": {"inputs": ['revenue'], "func": slsm_173_dummy_vel_4_63d},
    "slsm_174_dummy_vel_4_126d": {"inputs": ['revenue'], "func": slsm_174_dummy_vel_4_126d},
    "slsm_175_dummy_vel_4_252d": {"inputs": ['revenue'], "func": slsm_175_dummy_vel_4_252d},
}
