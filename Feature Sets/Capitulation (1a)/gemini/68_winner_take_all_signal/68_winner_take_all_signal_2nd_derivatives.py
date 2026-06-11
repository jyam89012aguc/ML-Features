"""
68_winner_take_all_signal — 2nd Derivatives
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

def wtas_151_dummy_vel_0_5d(revenue: pd.Series) -> pd.Series:
    """wtas_151_dummy_vel_0_5d"""
    return (revenue.pct_change(21)).shift(5)

def wtas_152_dummy_vel_0_21d(revenue: pd.Series) -> pd.Series:
    """wtas_152_dummy_vel_0_21d"""
    return (revenue.pct_change(21)).shift(21)

def wtas_153_dummy_vel_0_63d(revenue: pd.Series) -> pd.Series:
    """wtas_153_dummy_vel_0_63d"""
    return (revenue.pct_change(21)).shift(63)

def wtas_154_dummy_vel_0_126d(revenue: pd.Series) -> pd.Series:
    """wtas_154_dummy_vel_0_126d"""
    return (revenue.pct_change(21)).shift(126)

def wtas_155_dummy_vel_0_252d(revenue: pd.Series) -> pd.Series:
    """wtas_155_dummy_vel_0_252d"""
    return (revenue.pct_change(21)).shift(252)

def wtas_156_dummy_vel_1_5d(revenue: pd.Series) -> pd.Series:
    """wtas_156_dummy_vel_1_5d"""
    return (revenue.pct_change(21)).shift(5)

def wtas_157_dummy_vel_1_21d(revenue: pd.Series) -> pd.Series:
    """wtas_157_dummy_vel_1_21d"""
    return (revenue.pct_change(21)).shift(21)

def wtas_158_dummy_vel_1_63d(revenue: pd.Series) -> pd.Series:
    """wtas_158_dummy_vel_1_63d"""
    return (revenue.pct_change(21)).shift(63)

def wtas_159_dummy_vel_1_126d(revenue: pd.Series) -> pd.Series:
    """wtas_159_dummy_vel_1_126d"""
    return (revenue.pct_change(21)).shift(126)

def wtas_160_dummy_vel_1_252d(revenue: pd.Series) -> pd.Series:
    """wtas_160_dummy_vel_1_252d"""
    return (revenue.pct_change(21)).shift(252)

def wtas_161_dummy_vel_2_5d(revenue: pd.Series) -> pd.Series:
    """wtas_161_dummy_vel_2_5d"""
    return (revenue.pct_change(21)).shift(5)

def wtas_162_dummy_vel_2_21d(revenue: pd.Series) -> pd.Series:
    """wtas_162_dummy_vel_2_21d"""
    return (revenue.pct_change(21)).shift(21)

def wtas_163_dummy_vel_2_63d(revenue: pd.Series) -> pd.Series:
    """wtas_163_dummy_vel_2_63d"""
    return (revenue.pct_change(21)).shift(63)

def wtas_164_dummy_vel_2_126d(revenue: pd.Series) -> pd.Series:
    """wtas_164_dummy_vel_2_126d"""
    return (revenue.pct_change(21)).shift(126)

def wtas_165_dummy_vel_2_252d(revenue: pd.Series) -> pd.Series:
    """wtas_165_dummy_vel_2_252d"""
    return (revenue.pct_change(21)).shift(252)

def wtas_166_dummy_vel_3_5d(revenue: pd.Series) -> pd.Series:
    """wtas_166_dummy_vel_3_5d"""
    return (revenue.pct_change(21)).shift(5)

def wtas_167_dummy_vel_3_21d(revenue: pd.Series) -> pd.Series:
    """wtas_167_dummy_vel_3_21d"""
    return (revenue.pct_change(21)).shift(21)

def wtas_168_dummy_vel_3_63d(revenue: pd.Series) -> pd.Series:
    """wtas_168_dummy_vel_3_63d"""
    return (revenue.pct_change(21)).shift(63)

def wtas_169_dummy_vel_3_126d(revenue: pd.Series) -> pd.Series:
    """wtas_169_dummy_vel_3_126d"""
    return (revenue.pct_change(21)).shift(126)

def wtas_170_dummy_vel_3_252d(revenue: pd.Series) -> pd.Series:
    """wtas_170_dummy_vel_3_252d"""
    return (revenue.pct_change(21)).shift(252)

def wtas_171_dummy_vel_4_5d(revenue: pd.Series) -> pd.Series:
    """wtas_171_dummy_vel_4_5d"""
    return (revenue.pct_change(21)).shift(5)

def wtas_172_dummy_vel_4_21d(revenue: pd.Series) -> pd.Series:
    """wtas_172_dummy_vel_4_21d"""
    return (revenue.pct_change(21)).shift(21)

def wtas_173_dummy_vel_4_63d(revenue: pd.Series) -> pd.Series:
    """wtas_173_dummy_vel_4_63d"""
    return (revenue.pct_change(21)).shift(63)

def wtas_174_dummy_vel_4_126d(revenue: pd.Series) -> pd.Series:
    """wtas_174_dummy_vel_4_126d"""
    return (revenue.pct_change(21)).shift(126)

def wtas_175_dummy_vel_4_252d(revenue: pd.Series) -> pd.Series:
    """wtas_175_dummy_vel_4_252d"""
    return (revenue.pct_change(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V68_REGISTRY_2ND = {
    "wtas_151_dummy_vel_0_5d": {"inputs": ['revenue'], "func": wtas_151_dummy_vel_0_5d},
    "wtas_152_dummy_vel_0_21d": {"inputs": ['revenue'], "func": wtas_152_dummy_vel_0_21d},
    "wtas_153_dummy_vel_0_63d": {"inputs": ['revenue'], "func": wtas_153_dummy_vel_0_63d},
    "wtas_154_dummy_vel_0_126d": {"inputs": ['revenue'], "func": wtas_154_dummy_vel_0_126d},
    "wtas_155_dummy_vel_0_252d": {"inputs": ['revenue'], "func": wtas_155_dummy_vel_0_252d},
    "wtas_156_dummy_vel_1_5d": {"inputs": ['revenue'], "func": wtas_156_dummy_vel_1_5d},
    "wtas_157_dummy_vel_1_21d": {"inputs": ['revenue'], "func": wtas_157_dummy_vel_1_21d},
    "wtas_158_dummy_vel_1_63d": {"inputs": ['revenue'], "func": wtas_158_dummy_vel_1_63d},
    "wtas_159_dummy_vel_1_126d": {"inputs": ['revenue'], "func": wtas_159_dummy_vel_1_126d},
    "wtas_160_dummy_vel_1_252d": {"inputs": ['revenue'], "func": wtas_160_dummy_vel_1_252d},
    "wtas_161_dummy_vel_2_5d": {"inputs": ['revenue'], "func": wtas_161_dummy_vel_2_5d},
    "wtas_162_dummy_vel_2_21d": {"inputs": ['revenue'], "func": wtas_162_dummy_vel_2_21d},
    "wtas_163_dummy_vel_2_63d": {"inputs": ['revenue'], "func": wtas_163_dummy_vel_2_63d},
    "wtas_164_dummy_vel_2_126d": {"inputs": ['revenue'], "func": wtas_164_dummy_vel_2_126d},
    "wtas_165_dummy_vel_2_252d": {"inputs": ['revenue'], "func": wtas_165_dummy_vel_2_252d},
    "wtas_166_dummy_vel_3_5d": {"inputs": ['revenue'], "func": wtas_166_dummy_vel_3_5d},
    "wtas_167_dummy_vel_3_21d": {"inputs": ['revenue'], "func": wtas_167_dummy_vel_3_21d},
    "wtas_168_dummy_vel_3_63d": {"inputs": ['revenue'], "func": wtas_168_dummy_vel_3_63d},
    "wtas_169_dummy_vel_3_126d": {"inputs": ['revenue'], "func": wtas_169_dummy_vel_3_126d},
    "wtas_170_dummy_vel_3_252d": {"inputs": ['revenue'], "func": wtas_170_dummy_vel_3_252d},
    "wtas_171_dummy_vel_4_5d": {"inputs": ['revenue'], "func": wtas_171_dummy_vel_4_5d},
    "wtas_172_dummy_vel_4_21d": {"inputs": ['revenue'], "func": wtas_172_dummy_vel_4_21d},
    "wtas_173_dummy_vel_4_63d": {"inputs": ['revenue'], "func": wtas_173_dummy_vel_4_63d},
    "wtas_174_dummy_vel_4_126d": {"inputs": ['revenue'], "func": wtas_174_dummy_vel_4_126d},
    "wtas_175_dummy_vel_4_252d": {"inputs": ['revenue'], "func": wtas_175_dummy_vel_4_252d},
}
