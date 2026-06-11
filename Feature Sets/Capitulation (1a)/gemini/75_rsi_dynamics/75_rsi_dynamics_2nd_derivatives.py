"""
75_rsi_dynamics — 2nd Derivatives (Velocity)
Domain: rsi_dynamics
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

def rsid_151_rsi_14_vel_5d(close: pd.Series) -> pd.Series:
    """rsid_151_rsi_14_vel_5d"""
    return (_rsi(close, 14)).diff(5)

def rsid_152_rsi_14_vel_21d(close: pd.Series) -> pd.Series:
    """rsid_152_rsi_14_vel_21d"""
    return (_rsi(close, 14)).diff(21)

def rsid_153_rsi_14_vel_63d(close: pd.Series) -> pd.Series:
    """rsid_153_rsi_14_vel_63d"""
    return (_rsi(close, 14)).diff(63)

def rsid_154_rsi_14_vel_126d(close: pd.Series) -> pd.Series:
    """rsid_154_rsi_14_vel_126d"""
    return (_rsi(close, 14)).diff(126)

def rsid_155_rsi_14_vel_252d(close: pd.Series) -> pd.Series:
    """rsid_155_rsi_14_vel_252d"""
    return (_rsi(close, 14)).diff(252)

def rsid_156_rsi_5_vel_5d(close: pd.Series) -> pd.Series:
    """rsid_156_rsi_5_vel_5d"""
    return (_rsi(close, 5)).diff(5)

def rsid_157_rsi_5_vel_21d(close: pd.Series) -> pd.Series:
    """rsid_157_rsi_5_vel_21d"""
    return (_rsi(close, 5)).diff(21)

def rsid_158_rsi_5_vel_63d(close: pd.Series) -> pd.Series:
    """rsid_158_rsi_5_vel_63d"""
    return (_rsi(close, 5)).diff(63)

def rsid_159_rsi_5_vel_126d(close: pd.Series) -> pd.Series:
    """rsid_159_rsi_5_vel_126d"""
    return (_rsi(close, 5)).diff(126)

def rsid_160_rsi_5_vel_252d(close: pd.Series) -> pd.Series:
    """rsid_160_rsi_5_vel_252d"""
    return (_rsi(close, 5)).diff(252)

def rsid_161_rsi_21_vel_5d(close: pd.Series) -> pd.Series:
    """rsid_161_rsi_21_vel_5d"""
    return (_rsi(close, 21)).diff(5)

def rsid_162_rsi_21_vel_21d(close: pd.Series) -> pd.Series:
    """rsid_162_rsi_21_vel_21d"""
    return (_rsi(close, 21)).diff(21)

def rsid_163_rsi_21_vel_63d(close: pd.Series) -> pd.Series:
    """rsid_163_rsi_21_vel_63d"""
    return (_rsi(close, 21)).diff(63)

def rsid_164_rsi_21_vel_126d(close: pd.Series) -> pd.Series:
    """rsid_164_rsi_21_vel_126d"""
    return (_rsi(close, 21)).diff(126)

def rsid_165_rsi_21_vel_252d(close: pd.Series) -> pd.Series:
    """rsid_165_rsi_21_vel_252d"""
    return (_rsi(close, 21)).diff(252)

def rsid_166_rsi_dist_vel_5d(close: pd.Series) -> pd.Series:
    """rsid_166_rsi_dist_vel_5d"""
    return (_rsi(close, 14) - 50).diff(5)

def rsid_167_rsi_dist_vel_21d(close: pd.Series) -> pd.Series:
    """rsid_167_rsi_dist_vel_21d"""
    return (_rsi(close, 14) - 50).diff(21)

def rsid_168_rsi_dist_vel_63d(close: pd.Series) -> pd.Series:
    """rsid_168_rsi_dist_vel_63d"""
    return (_rsi(close, 14) - 50).diff(63)

def rsid_169_rsi_dist_vel_126d(close: pd.Series) -> pd.Series:
    """rsid_169_rsi_dist_vel_126d"""
    return (_rsi(close, 14) - 50).diff(126)

def rsid_170_rsi_dist_vel_252d(close: pd.Series) -> pd.Series:
    """rsid_170_rsi_dist_vel_252d"""
    return (_rsi(close, 14) - 50).diff(252)

def rsid_171_rsi_ob_vel_5d(close: pd.Series) -> pd.Series:
    """rsid_171_rsi_ob_vel_5d"""
    return (_rsi(close, 14) - 70).diff(5)

def rsid_172_rsi_ob_vel_21d(close: pd.Series) -> pd.Series:
    """rsid_172_rsi_ob_vel_21d"""
    return (_rsi(close, 14) - 70).diff(21)

def rsid_173_rsi_ob_vel_63d(close: pd.Series) -> pd.Series:
    """rsid_173_rsi_ob_vel_63d"""
    return (_rsi(close, 14) - 70).diff(63)

def rsid_174_rsi_ob_vel_126d(close: pd.Series) -> pd.Series:
    """rsid_174_rsi_ob_vel_126d"""
    return (_rsi(close, 14) - 70).diff(126)

def rsid_175_rsi_ob_vel_252d(close: pd.Series) -> pd.Series:
    """rsid_175_rsi_ob_vel_252d"""
    return (_rsi(close, 14) - 70).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V75_REGISTRY_VEL = {
    "rsid_151_rsi_14_vel_5d": {"inputs": ["close"], "func": rsid_151_rsi_14_vel_5d},
    "rsid_152_rsi_14_vel_21d": {"inputs": ["close"], "func": rsid_152_rsi_14_vel_21d},
    "rsid_153_rsi_14_vel_63d": {"inputs": ["close"], "func": rsid_153_rsi_14_vel_63d},
    "rsid_154_rsi_14_vel_126d": {"inputs": ["close"], "func": rsid_154_rsi_14_vel_126d},
    "rsid_155_rsi_14_vel_252d": {"inputs": ["close"], "func": rsid_155_rsi_14_vel_252d},
    "rsid_156_rsi_5_vel_5d": {"inputs": ["close"], "func": rsid_156_rsi_5_vel_5d},
    "rsid_157_rsi_5_vel_21d": {"inputs": ["close"], "func": rsid_157_rsi_5_vel_21d},
    "rsid_158_rsi_5_vel_63d": {"inputs": ["close"], "func": rsid_158_rsi_5_vel_63d},
    "rsid_159_rsi_5_vel_126d": {"inputs": ["close"], "func": rsid_159_rsi_5_vel_126d},
    "rsid_160_rsi_5_vel_252d": {"inputs": ["close"], "func": rsid_160_rsi_5_vel_252d},
    "rsid_161_rsi_21_vel_5d": {"inputs": ["close"], "func": rsid_161_rsi_21_vel_5d},
    "rsid_162_rsi_21_vel_21d": {"inputs": ["close"], "func": rsid_162_rsi_21_vel_21d},
    "rsid_163_rsi_21_vel_63d": {"inputs": ["close"], "func": rsid_163_rsi_21_vel_63d},
    "rsid_164_rsi_21_vel_126d": {"inputs": ["close"], "func": rsid_164_rsi_21_vel_126d},
    "rsid_165_rsi_21_vel_252d": {"inputs": ["close"], "func": rsid_165_rsi_21_vel_252d},
    "rsid_166_rsi_dist_vel_5d": {"inputs": ["close"], "func": rsid_166_rsi_dist_vel_5d},
    "rsid_167_rsi_dist_vel_21d": {"inputs": ["close"], "func": rsid_167_rsi_dist_vel_21d},
    "rsid_168_rsi_dist_vel_63d": {"inputs": ["close"], "func": rsid_168_rsi_dist_vel_63d},
    "rsid_169_rsi_dist_vel_126d": {"inputs": ["close"], "func": rsid_169_rsi_dist_vel_126d},
    "rsid_170_rsi_dist_vel_252d": {"inputs": ["close"], "func": rsid_170_rsi_dist_vel_252d},
    "rsid_171_rsi_ob_vel_5d": {"inputs": ["close"], "func": rsid_171_rsi_ob_vel_5d},
    "rsid_172_rsi_ob_vel_21d": {"inputs": ["close"], "func": rsid_172_rsi_ob_vel_21d},
    "rsid_173_rsi_ob_vel_63d": {"inputs": ["close"], "func": rsid_173_rsi_ob_vel_63d},
    "rsid_174_rsi_ob_vel_126d": {"inputs": ["close"], "func": rsid_174_rsi_ob_vel_126d},
    "rsid_175_rsi_ob_vel_252d": {"inputs": ["close"], "func": rsid_175_rsi_ob_vel_252d},
}
