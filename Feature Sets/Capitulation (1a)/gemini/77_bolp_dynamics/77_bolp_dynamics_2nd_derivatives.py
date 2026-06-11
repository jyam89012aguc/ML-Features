"""
77_bolp_dynamics — 2nd Derivatives (Velocity)
Domain: bolp_dynamics
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std().fillna(0)

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()

def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()

def _ewm_mean(s: pd.Series, w: int) -> pd.Series:
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)

def _rsi(s: pd.Series, w: int) -> pd.Series:
    delta = s.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=w).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=w).mean()
    rs = _safe_div(gain, loss)
    return 100 - (100 / (1 + rs))

# ── Feature functions ────────────────────────────────────────────────────────

def bolp_151_bb_upper_vel_5d(close: pd.Series) -> pd.Series:
    """bolp_151_bb_upper_vel_5d"""
    return (_rolling_mean(close, 20) + 2 * _rolling_std(close, 20)).diff(5)

def bolp_152_bb_upper_vel_21d(close: pd.Series) -> pd.Series:
    """bolp_152_bb_upper_vel_21d"""
    return (_rolling_mean(close, 20) + 2 * _rolling_std(close, 20)).diff(21)

def bolp_153_bb_upper_vel_63d(close: pd.Series) -> pd.Series:
    """bolp_153_bb_upper_vel_63d"""
    return (_rolling_mean(close, 20) + 2 * _rolling_std(close, 20)).diff(63)

def bolp_154_bb_upper_vel_126d(close: pd.Series) -> pd.Series:
    """bolp_154_bb_upper_vel_126d"""
    return (_rolling_mean(close, 20) + 2 * _rolling_std(close, 20)).diff(126)

def bolp_155_bb_upper_vel_252d(close: pd.Series) -> pd.Series:
    """bolp_155_bb_upper_vel_252d"""
    return (_rolling_mean(close, 20) + 2 * _rolling_std(close, 20)).diff(252)

def bolp_156_bb_lower_vel_5d(close: pd.Series) -> pd.Series:
    """bolp_156_bb_lower_vel_5d"""
    return (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)).diff(5)

def bolp_157_bb_lower_vel_21d(close: pd.Series) -> pd.Series:
    """bolp_157_bb_lower_vel_21d"""
    return (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)).diff(21)

def bolp_158_bb_lower_vel_63d(close: pd.Series) -> pd.Series:
    """bolp_158_bb_lower_vel_63d"""
    return (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)).diff(63)

def bolp_159_bb_lower_vel_126d(close: pd.Series) -> pd.Series:
    """bolp_159_bb_lower_vel_126d"""
    return (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)).diff(126)

def bolp_160_bb_lower_vel_252d(close: pd.Series) -> pd.Series:
    """bolp_160_bb_lower_vel_252d"""
    return (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)).diff(252)

def bolp_161_bb_width_vel_5d(close: pd.Series) -> pd.Series:
    """bolp_161_bb_width_vel_5d"""
    return (_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))).diff(5)

def bolp_162_bb_width_vel_21d(close: pd.Series) -> pd.Series:
    """bolp_162_bb_width_vel_21d"""
    return (_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))).diff(21)

def bolp_163_bb_width_vel_63d(close: pd.Series) -> pd.Series:
    """bolp_163_bb_width_vel_63d"""
    return (_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))).diff(63)

def bolp_164_bb_width_vel_126d(close: pd.Series) -> pd.Series:
    """bolp_164_bb_width_vel_126d"""
    return (_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))).diff(126)

def bolp_165_bb_width_vel_252d(close: pd.Series) -> pd.Series:
    """bolp_165_bb_width_vel_252d"""
    return (_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))).diff(252)

def bolp_166_bb_pctb_vel_5d(close: pd.Series) -> pd.Series:
    """bolp_166_bb_pctb_vel_5d"""
    return (_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))).diff(5)

def bolp_167_bb_pctb_vel_21d(close: pd.Series) -> pd.Series:
    """bolp_167_bb_pctb_vel_21d"""
    return (_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))).diff(21)

def bolp_168_bb_pctb_vel_63d(close: pd.Series) -> pd.Series:
    """bolp_168_bb_pctb_vel_63d"""
    return (_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))).diff(63)

def bolp_169_bb_pctb_vel_126d(close: pd.Series) -> pd.Series:
    """bolp_169_bb_pctb_vel_126d"""
    return (_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))).diff(126)

def bolp_170_bb_pctb_vel_252d(close: pd.Series) -> pd.Series:
    """bolp_170_bb_pctb_vel_252d"""
    return (_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))).diff(252)

def bolp_171_bb_dist_u_vel_5d(close: pd.Series) -> pd.Series:
    """bolp_171_bb_dist_u_vel_5d"""
    return (_safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))).diff(5)

def bolp_172_bb_dist_u_vel_21d(close: pd.Series) -> pd.Series:
    """bolp_172_bb_dist_u_vel_21d"""
    return (_safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))).diff(21)

def bolp_173_bb_dist_u_vel_63d(close: pd.Series) -> pd.Series:
    """bolp_173_bb_dist_u_vel_63d"""
    return (_safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))).diff(63)

def bolp_174_bb_dist_u_vel_126d(close: pd.Series) -> pd.Series:
    """bolp_174_bb_dist_u_vel_126d"""
    return (_safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))).diff(126)

def bolp_175_bb_dist_u_vel_252d(close: pd.Series) -> pd.Series:
    """bolp_175_bb_dist_u_vel_252d"""
    return (_safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V77_REGISTRY_VEL = {
    "bolp_151_bb_upper_vel_5d": {"inputs": ["close"], "func": bolp_151_bb_upper_vel_5d},
    "bolp_152_bb_upper_vel_21d": {"inputs": ["close"], "func": bolp_152_bb_upper_vel_21d},
    "bolp_153_bb_upper_vel_63d": {"inputs": ["close"], "func": bolp_153_bb_upper_vel_63d},
    "bolp_154_bb_upper_vel_126d": {"inputs": ["close"], "func": bolp_154_bb_upper_vel_126d},
    "bolp_155_bb_upper_vel_252d": {"inputs": ["close"], "func": bolp_155_bb_upper_vel_252d},
    "bolp_156_bb_lower_vel_5d": {"inputs": ["close"], "func": bolp_156_bb_lower_vel_5d},
    "bolp_157_bb_lower_vel_21d": {"inputs": ["close"], "func": bolp_157_bb_lower_vel_21d},
    "bolp_158_bb_lower_vel_63d": {"inputs": ["close"], "func": bolp_158_bb_lower_vel_63d},
    "bolp_159_bb_lower_vel_126d": {"inputs": ["close"], "func": bolp_159_bb_lower_vel_126d},
    "bolp_160_bb_lower_vel_252d": {"inputs": ["close"], "func": bolp_160_bb_lower_vel_252d},
    "bolp_161_bb_width_vel_5d": {"inputs": ["close"], "func": bolp_161_bb_width_vel_5d},
    "bolp_162_bb_width_vel_21d": {"inputs": ["close"], "func": bolp_162_bb_width_vel_21d},
    "bolp_163_bb_width_vel_63d": {"inputs": ["close"], "func": bolp_163_bb_width_vel_63d},
    "bolp_164_bb_width_vel_126d": {"inputs": ["close"], "func": bolp_164_bb_width_vel_126d},
    "bolp_165_bb_width_vel_252d": {"inputs": ["close"], "func": bolp_165_bb_width_vel_252d},
    "bolp_166_bb_pctb_vel_5d": {"inputs": ["close"], "func": bolp_166_bb_pctb_vel_5d},
    "bolp_167_bb_pctb_vel_21d": {"inputs": ["close"], "func": bolp_167_bb_pctb_vel_21d},
    "bolp_168_bb_pctb_vel_63d": {"inputs": ["close"], "func": bolp_168_bb_pctb_vel_63d},
    "bolp_169_bb_pctb_vel_126d": {"inputs": ["close"], "func": bolp_169_bb_pctb_vel_126d},
    "bolp_170_bb_pctb_vel_252d": {"inputs": ["close"], "func": bolp_170_bb_pctb_vel_252d},
    "bolp_171_bb_dist_u_vel_5d": {"inputs": ["close"], "func": bolp_171_bb_dist_u_vel_5d},
    "bolp_172_bb_dist_u_vel_21d": {"inputs": ["close"], "func": bolp_172_bb_dist_u_vel_21d},
    "bolp_173_bb_dist_u_vel_63d": {"inputs": ["close"], "func": bolp_173_bb_dist_u_vel_63d},
    "bolp_174_bb_dist_u_vel_126d": {"inputs": ["close"], "func": bolp_174_bb_dist_u_vel_126d},
    "bolp_175_bb_dist_u_vel_252d": {"inputs": ["close"], "func": bolp_175_bb_dist_u_vel_252d},
}
