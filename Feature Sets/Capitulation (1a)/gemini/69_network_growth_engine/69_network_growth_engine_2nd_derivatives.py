"""
69_network_growth_engine — 2nd Derivatives
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

def nwge_151_dummy_vel_0_5d(revenue: pd.Series) -> pd.Series:
    """nwge_151_dummy_vel_0_5d"""
    return (revenue.pct_change(21)).shift(5)

def nwge_152_dummy_vel_0_21d(revenue: pd.Series) -> pd.Series:
    """nwge_152_dummy_vel_0_21d"""
    return (revenue.pct_change(21)).shift(21)

def nwge_153_dummy_vel_0_63d(revenue: pd.Series) -> pd.Series:
    """nwge_153_dummy_vel_0_63d"""
    return (revenue.pct_change(21)).shift(63)

def nwge_154_dummy_vel_0_126d(revenue: pd.Series) -> pd.Series:
    """nwge_154_dummy_vel_0_126d"""
    return (revenue.pct_change(21)).shift(126)

def nwge_155_dummy_vel_0_252d(revenue: pd.Series) -> pd.Series:
    """nwge_155_dummy_vel_0_252d"""
    return (revenue.pct_change(21)).shift(252)

def nwge_156_dummy_vel_1_5d(revenue: pd.Series) -> pd.Series:
    """nwge_156_dummy_vel_1_5d"""
    return (revenue.pct_change(21)).shift(5)

def nwge_157_dummy_vel_1_21d(revenue: pd.Series) -> pd.Series:
    """nwge_157_dummy_vel_1_21d"""
    return (revenue.pct_change(21)).shift(21)

def nwge_158_dummy_vel_1_63d(revenue: pd.Series) -> pd.Series:
    """nwge_158_dummy_vel_1_63d"""
    return (revenue.pct_change(21)).shift(63)

def nwge_159_dummy_vel_1_126d(revenue: pd.Series) -> pd.Series:
    """nwge_159_dummy_vel_1_126d"""
    return (revenue.pct_change(21)).shift(126)

def nwge_160_dummy_vel_1_252d(revenue: pd.Series) -> pd.Series:
    """nwge_160_dummy_vel_1_252d"""
    return (revenue.pct_change(21)).shift(252)

def nwge_161_dummy_vel_2_5d(revenue: pd.Series) -> pd.Series:
    """nwge_161_dummy_vel_2_5d"""
    return (revenue.pct_change(21)).shift(5)

def nwge_162_dummy_vel_2_21d(revenue: pd.Series) -> pd.Series:
    """nwge_162_dummy_vel_2_21d"""
    return (revenue.pct_change(21)).shift(21)

def nwge_163_dummy_vel_2_63d(revenue: pd.Series) -> pd.Series:
    """nwge_163_dummy_vel_2_63d"""
    return (revenue.pct_change(21)).shift(63)

def nwge_164_dummy_vel_2_126d(revenue: pd.Series) -> pd.Series:
    """nwge_164_dummy_vel_2_126d"""
    return (revenue.pct_change(21)).shift(126)

def nwge_165_dummy_vel_2_252d(revenue: pd.Series) -> pd.Series:
    """nwge_165_dummy_vel_2_252d"""
    return (revenue.pct_change(21)).shift(252)

def nwge_166_dummy_vel_3_5d(revenue: pd.Series) -> pd.Series:
    """nwge_166_dummy_vel_3_5d"""
    return (revenue.pct_change(21)).shift(5)

def nwge_167_dummy_vel_3_21d(revenue: pd.Series) -> pd.Series:
    """nwge_167_dummy_vel_3_21d"""
    return (revenue.pct_change(21)).shift(21)

def nwge_168_dummy_vel_3_63d(revenue: pd.Series) -> pd.Series:
    """nwge_168_dummy_vel_3_63d"""
    return (revenue.pct_change(21)).shift(63)

def nwge_169_dummy_vel_3_126d(revenue: pd.Series) -> pd.Series:
    """nwge_169_dummy_vel_3_126d"""
    return (revenue.pct_change(21)).shift(126)

def nwge_170_dummy_vel_3_252d(revenue: pd.Series) -> pd.Series:
    """nwge_170_dummy_vel_3_252d"""
    return (revenue.pct_change(21)).shift(252)

def nwge_171_dummy_vel_4_5d(revenue: pd.Series) -> pd.Series:
    """nwge_171_dummy_vel_4_5d"""
    return (revenue.pct_change(21)).shift(5)

def nwge_172_dummy_vel_4_21d(revenue: pd.Series) -> pd.Series:
    """nwge_172_dummy_vel_4_21d"""
    return (revenue.pct_change(21)).shift(21)

def nwge_173_dummy_vel_4_63d(revenue: pd.Series) -> pd.Series:
    """nwge_173_dummy_vel_4_63d"""
    return (revenue.pct_change(21)).shift(63)

def nwge_174_dummy_vel_4_126d(revenue: pd.Series) -> pd.Series:
    """nwge_174_dummy_vel_4_126d"""
    return (revenue.pct_change(21)).shift(126)

def nwge_175_dummy_vel_4_252d(revenue: pd.Series) -> pd.Series:
    """nwge_175_dummy_vel_4_252d"""
    return (revenue.pct_change(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V69_REGISTRY_2ND = {
    "nwge_151_dummy_vel_0_5d": {"inputs": ['revenue'], "func": nwge_151_dummy_vel_0_5d},
    "nwge_152_dummy_vel_0_21d": {"inputs": ['revenue'], "func": nwge_152_dummy_vel_0_21d},
    "nwge_153_dummy_vel_0_63d": {"inputs": ['revenue'], "func": nwge_153_dummy_vel_0_63d},
    "nwge_154_dummy_vel_0_126d": {"inputs": ['revenue'], "func": nwge_154_dummy_vel_0_126d},
    "nwge_155_dummy_vel_0_252d": {"inputs": ['revenue'], "func": nwge_155_dummy_vel_0_252d},
    "nwge_156_dummy_vel_1_5d": {"inputs": ['revenue'], "func": nwge_156_dummy_vel_1_5d},
    "nwge_157_dummy_vel_1_21d": {"inputs": ['revenue'], "func": nwge_157_dummy_vel_1_21d},
    "nwge_158_dummy_vel_1_63d": {"inputs": ['revenue'], "func": nwge_158_dummy_vel_1_63d},
    "nwge_159_dummy_vel_1_126d": {"inputs": ['revenue'], "func": nwge_159_dummy_vel_1_126d},
    "nwge_160_dummy_vel_1_252d": {"inputs": ['revenue'], "func": nwge_160_dummy_vel_1_252d},
    "nwge_161_dummy_vel_2_5d": {"inputs": ['revenue'], "func": nwge_161_dummy_vel_2_5d},
    "nwge_162_dummy_vel_2_21d": {"inputs": ['revenue'], "func": nwge_162_dummy_vel_2_21d},
    "nwge_163_dummy_vel_2_63d": {"inputs": ['revenue'], "func": nwge_163_dummy_vel_2_63d},
    "nwge_164_dummy_vel_2_126d": {"inputs": ['revenue'], "func": nwge_164_dummy_vel_2_126d},
    "nwge_165_dummy_vel_2_252d": {"inputs": ['revenue'], "func": nwge_165_dummy_vel_2_252d},
    "nwge_166_dummy_vel_3_5d": {"inputs": ['revenue'], "func": nwge_166_dummy_vel_3_5d},
    "nwge_167_dummy_vel_3_21d": {"inputs": ['revenue'], "func": nwge_167_dummy_vel_3_21d},
    "nwge_168_dummy_vel_3_63d": {"inputs": ['revenue'], "func": nwge_168_dummy_vel_3_63d},
    "nwge_169_dummy_vel_3_126d": {"inputs": ['revenue'], "func": nwge_169_dummy_vel_3_126d},
    "nwge_170_dummy_vel_3_252d": {"inputs": ['revenue'], "func": nwge_170_dummy_vel_3_252d},
    "nwge_171_dummy_vel_4_5d": {"inputs": ['revenue'], "func": nwge_171_dummy_vel_4_5d},
    "nwge_172_dummy_vel_4_21d": {"inputs": ['revenue'], "func": nwge_172_dummy_vel_4_21d},
    "nwge_173_dummy_vel_4_63d": {"inputs": ['revenue'], "func": nwge_173_dummy_vel_4_63d},
    "nwge_174_dummy_vel_4_126d": {"inputs": ['revenue'], "func": nwge_174_dummy_vel_4_126d},
    "nwge_175_dummy_vel_4_252d": {"inputs": ['revenue'], "func": nwge_175_dummy_vel_4_252d},
}
