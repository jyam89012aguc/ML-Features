"""
74_terminal_decline_composite — 2nd Derivatives
Domain: Composite of all forensic decay signals
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

def tedc_151_dummy_vel_0_5d(revenue: pd.Series) -> pd.Series:
    """tedc_151_dummy_vel_0_5d"""
    return (revenue.pct_change(21)).shift(5)

def tedc_152_dummy_vel_0_21d(revenue: pd.Series) -> pd.Series:
    """tedc_152_dummy_vel_0_21d"""
    return (revenue.pct_change(21)).shift(21)

def tedc_153_dummy_vel_0_63d(revenue: pd.Series) -> pd.Series:
    """tedc_153_dummy_vel_0_63d"""
    return (revenue.pct_change(21)).shift(63)

def tedc_154_dummy_vel_0_126d(revenue: pd.Series) -> pd.Series:
    """tedc_154_dummy_vel_0_126d"""
    return (revenue.pct_change(21)).shift(126)

def tedc_155_dummy_vel_0_252d(revenue: pd.Series) -> pd.Series:
    """tedc_155_dummy_vel_0_252d"""
    return (revenue.pct_change(21)).shift(252)

def tedc_156_dummy_vel_1_5d(revenue: pd.Series) -> pd.Series:
    """tedc_156_dummy_vel_1_5d"""
    return (revenue.pct_change(21)).shift(5)

def tedc_157_dummy_vel_1_21d(revenue: pd.Series) -> pd.Series:
    """tedc_157_dummy_vel_1_21d"""
    return (revenue.pct_change(21)).shift(21)

def tedc_158_dummy_vel_1_63d(revenue: pd.Series) -> pd.Series:
    """tedc_158_dummy_vel_1_63d"""
    return (revenue.pct_change(21)).shift(63)

def tedc_159_dummy_vel_1_126d(revenue: pd.Series) -> pd.Series:
    """tedc_159_dummy_vel_1_126d"""
    return (revenue.pct_change(21)).shift(126)

def tedc_160_dummy_vel_1_252d(revenue: pd.Series) -> pd.Series:
    """tedc_160_dummy_vel_1_252d"""
    return (revenue.pct_change(21)).shift(252)

def tedc_161_dummy_vel_2_5d(revenue: pd.Series) -> pd.Series:
    """tedc_161_dummy_vel_2_5d"""
    return (revenue.pct_change(21)).shift(5)

def tedc_162_dummy_vel_2_21d(revenue: pd.Series) -> pd.Series:
    """tedc_162_dummy_vel_2_21d"""
    return (revenue.pct_change(21)).shift(21)

def tedc_163_dummy_vel_2_63d(revenue: pd.Series) -> pd.Series:
    """tedc_163_dummy_vel_2_63d"""
    return (revenue.pct_change(21)).shift(63)

def tedc_164_dummy_vel_2_126d(revenue: pd.Series) -> pd.Series:
    """tedc_164_dummy_vel_2_126d"""
    return (revenue.pct_change(21)).shift(126)

def tedc_165_dummy_vel_2_252d(revenue: pd.Series) -> pd.Series:
    """tedc_165_dummy_vel_2_252d"""
    return (revenue.pct_change(21)).shift(252)

def tedc_166_dummy_vel_3_5d(revenue: pd.Series) -> pd.Series:
    """tedc_166_dummy_vel_3_5d"""
    return (revenue.pct_change(21)).shift(5)

def tedc_167_dummy_vel_3_21d(revenue: pd.Series) -> pd.Series:
    """tedc_167_dummy_vel_3_21d"""
    return (revenue.pct_change(21)).shift(21)

def tedc_168_dummy_vel_3_63d(revenue: pd.Series) -> pd.Series:
    """tedc_168_dummy_vel_3_63d"""
    return (revenue.pct_change(21)).shift(63)

def tedc_169_dummy_vel_3_126d(revenue: pd.Series) -> pd.Series:
    """tedc_169_dummy_vel_3_126d"""
    return (revenue.pct_change(21)).shift(126)

def tedc_170_dummy_vel_3_252d(revenue: pd.Series) -> pd.Series:
    """tedc_170_dummy_vel_3_252d"""
    return (revenue.pct_change(21)).shift(252)

def tedc_171_dummy_vel_4_5d(revenue: pd.Series) -> pd.Series:
    """tedc_171_dummy_vel_4_5d"""
    return (revenue.pct_change(21)).shift(5)

def tedc_172_dummy_vel_4_21d(revenue: pd.Series) -> pd.Series:
    """tedc_172_dummy_vel_4_21d"""
    return (revenue.pct_change(21)).shift(21)

def tedc_173_dummy_vel_4_63d(revenue: pd.Series) -> pd.Series:
    """tedc_173_dummy_vel_4_63d"""
    return (revenue.pct_change(21)).shift(63)

def tedc_174_dummy_vel_4_126d(revenue: pd.Series) -> pd.Series:
    """tedc_174_dummy_vel_4_126d"""
    return (revenue.pct_change(21)).shift(126)

def tedc_175_dummy_vel_4_252d(revenue: pd.Series) -> pd.Series:
    """tedc_175_dummy_vel_4_252d"""
    return (revenue.pct_change(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V74_REGISTRY_2ND = {
    "tedc_151_dummy_vel_0_5d": {"inputs": ['revenue'], "func": tedc_151_dummy_vel_0_5d},
    "tedc_152_dummy_vel_0_21d": {"inputs": ['revenue'], "func": tedc_152_dummy_vel_0_21d},
    "tedc_153_dummy_vel_0_63d": {"inputs": ['revenue'], "func": tedc_153_dummy_vel_0_63d},
    "tedc_154_dummy_vel_0_126d": {"inputs": ['revenue'], "func": tedc_154_dummy_vel_0_126d},
    "tedc_155_dummy_vel_0_252d": {"inputs": ['revenue'], "func": tedc_155_dummy_vel_0_252d},
    "tedc_156_dummy_vel_1_5d": {"inputs": ['revenue'], "func": tedc_156_dummy_vel_1_5d},
    "tedc_157_dummy_vel_1_21d": {"inputs": ['revenue'], "func": tedc_157_dummy_vel_1_21d},
    "tedc_158_dummy_vel_1_63d": {"inputs": ['revenue'], "func": tedc_158_dummy_vel_1_63d},
    "tedc_159_dummy_vel_1_126d": {"inputs": ['revenue'], "func": tedc_159_dummy_vel_1_126d},
    "tedc_160_dummy_vel_1_252d": {"inputs": ['revenue'], "func": tedc_160_dummy_vel_1_252d},
    "tedc_161_dummy_vel_2_5d": {"inputs": ['revenue'], "func": tedc_161_dummy_vel_2_5d},
    "tedc_162_dummy_vel_2_21d": {"inputs": ['revenue'], "func": tedc_162_dummy_vel_2_21d},
    "tedc_163_dummy_vel_2_63d": {"inputs": ['revenue'], "func": tedc_163_dummy_vel_2_63d},
    "tedc_164_dummy_vel_2_126d": {"inputs": ['revenue'], "func": tedc_164_dummy_vel_2_126d},
    "tedc_165_dummy_vel_2_252d": {"inputs": ['revenue'], "func": tedc_165_dummy_vel_2_252d},
    "tedc_166_dummy_vel_3_5d": {"inputs": ['revenue'], "func": tedc_166_dummy_vel_3_5d},
    "tedc_167_dummy_vel_3_21d": {"inputs": ['revenue'], "func": tedc_167_dummy_vel_3_21d},
    "tedc_168_dummy_vel_3_63d": {"inputs": ['revenue'], "func": tedc_168_dummy_vel_3_63d},
    "tedc_169_dummy_vel_3_126d": {"inputs": ['revenue'], "func": tedc_169_dummy_vel_3_126d},
    "tedc_170_dummy_vel_3_252d": {"inputs": ['revenue'], "func": tedc_170_dummy_vel_3_252d},
    "tedc_171_dummy_vel_4_5d": {"inputs": ['revenue'], "func": tedc_171_dummy_vel_4_5d},
    "tedc_172_dummy_vel_4_21d": {"inputs": ['revenue'], "func": tedc_172_dummy_vel_4_21d},
    "tedc_173_dummy_vel_4_63d": {"inputs": ['revenue'], "func": tedc_173_dummy_vel_4_63d},
    "tedc_174_dummy_vel_4_126d": {"inputs": ['revenue'], "func": tedc_174_dummy_vel_4_126d},
    "tedc_175_dummy_vel_4_252d": {"inputs": ['revenue'], "func": tedc_175_dummy_vel_4_252d},
}
