"""
79_maev_dynamics — 2nd Derivatives (Velocity)
Domain: maev_dynamics
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

def maev_151_sma20_rat_vel_5d(close: pd.Series) -> pd.Series:
    """maev_151_sma20_rat_vel_5d"""
    return (_safe_div(close, _rolling_mean(close, 20))).diff(5)

def maev_152_sma20_rat_vel_21d(close: pd.Series) -> pd.Series:
    """maev_152_sma20_rat_vel_21d"""
    return (_safe_div(close, _rolling_mean(close, 20))).diff(21)

def maev_153_sma20_rat_vel_63d(close: pd.Series) -> pd.Series:
    """maev_153_sma20_rat_vel_63d"""
    return (_safe_div(close, _rolling_mean(close, 20))).diff(63)

def maev_154_sma20_rat_vel_126d(close: pd.Series) -> pd.Series:
    """maev_154_sma20_rat_vel_126d"""
    return (_safe_div(close, _rolling_mean(close, 20))).diff(126)

def maev_155_sma20_rat_vel_252d(close: pd.Series) -> pd.Series:
    """maev_155_sma20_rat_vel_252d"""
    return (_safe_div(close, _rolling_mean(close, 20))).diff(252)

def maev_156_ema20_rat_vel_5d(close: pd.Series) -> pd.Series:
    """maev_156_ema20_rat_vel_5d"""
    return (_safe_div(close, _ewm_mean(close, 20))).diff(5)

def maev_157_ema20_rat_vel_21d(close: pd.Series) -> pd.Series:
    """maev_157_ema20_rat_vel_21d"""
    return (_safe_div(close, _ewm_mean(close, 20))).diff(21)

def maev_158_ema20_rat_vel_63d(close: pd.Series) -> pd.Series:
    """maev_158_ema20_rat_vel_63d"""
    return (_safe_div(close, _ewm_mean(close, 20))).diff(63)

def maev_159_ema20_rat_vel_126d(close: pd.Series) -> pd.Series:
    """maev_159_ema20_rat_vel_126d"""
    return (_safe_div(close, _ewm_mean(close, 20))).diff(126)

def maev_160_ema20_rat_vel_252d(close: pd.Series) -> pd.Series:
    """maev_160_ema20_rat_vel_252d"""
    return (_safe_div(close, _ewm_mean(close, 20))).diff(252)

def maev_161_sma50_rat_vel_5d(close: pd.Series) -> pd.Series:
    """maev_161_sma50_rat_vel_5d"""
    return (_safe_div(close, _rolling_mean(close, 50))).diff(5)

def maev_162_sma50_rat_vel_21d(close: pd.Series) -> pd.Series:
    """maev_162_sma50_rat_vel_21d"""
    return (_safe_div(close, _rolling_mean(close, 50))).diff(21)

def maev_163_sma50_rat_vel_63d(close: pd.Series) -> pd.Series:
    """maev_163_sma50_rat_vel_63d"""
    return (_safe_div(close, _rolling_mean(close, 50))).diff(63)

def maev_164_sma50_rat_vel_126d(close: pd.Series) -> pd.Series:
    """maev_164_sma50_rat_vel_126d"""
    return (_safe_div(close, _rolling_mean(close, 50))).diff(126)

def maev_165_sma50_rat_vel_252d(close: pd.Series) -> pd.Series:
    """maev_165_sma50_rat_vel_252d"""
    return (_safe_div(close, _rolling_mean(close, 50))).diff(252)

def maev_166_sma200_rat_vel_5d(close: pd.Series) -> pd.Series:
    """maev_166_sma200_rat_vel_5d"""
    return (_safe_div(close, _rolling_mean(close, 200))).diff(5)

def maev_167_sma200_rat_vel_21d(close: pd.Series) -> pd.Series:
    """maev_167_sma200_rat_vel_21d"""
    return (_safe_div(close, _rolling_mean(close, 200))).diff(21)

def maev_168_sma200_rat_vel_63d(close: pd.Series) -> pd.Series:
    """maev_168_sma200_rat_vel_63d"""
    return (_safe_div(close, _rolling_mean(close, 200))).diff(63)

def maev_169_sma200_rat_vel_126d(close: pd.Series) -> pd.Series:
    """maev_169_sma200_rat_vel_126d"""
    return (_safe_div(close, _rolling_mean(close, 200))).diff(126)

def maev_170_sma200_rat_vel_252d(close: pd.Series) -> pd.Series:
    """maev_170_sma200_rat_vel_252d"""
    return (_safe_div(close, _rolling_mean(close, 200))).diff(252)

def maev_171_cross_rat_vel_5d(close: pd.Series) -> pd.Series:
    """maev_171_cross_rat_vel_5d"""
    return (_safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))).diff(5)

def maev_172_cross_rat_vel_21d(close: pd.Series) -> pd.Series:
    """maev_172_cross_rat_vel_21d"""
    return (_safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))).diff(21)

def maev_173_cross_rat_vel_63d(close: pd.Series) -> pd.Series:
    """maev_173_cross_rat_vel_63d"""
    return (_safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))).diff(63)

def maev_174_cross_rat_vel_126d(close: pd.Series) -> pd.Series:
    """maev_174_cross_rat_vel_126d"""
    return (_safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))).diff(126)

def maev_175_cross_rat_vel_252d(close: pd.Series) -> pd.Series:
    """maev_175_cross_rat_vel_252d"""
    return (_safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V79_REGISTRY_VEL = {
    "maev_151_sma20_rat_vel_5d": {"inputs": ["close"], "func": maev_151_sma20_rat_vel_5d},
    "maev_152_sma20_rat_vel_21d": {"inputs": ["close"], "func": maev_152_sma20_rat_vel_21d},
    "maev_153_sma20_rat_vel_63d": {"inputs": ["close"], "func": maev_153_sma20_rat_vel_63d},
    "maev_154_sma20_rat_vel_126d": {"inputs": ["close"], "func": maev_154_sma20_rat_vel_126d},
    "maev_155_sma20_rat_vel_252d": {"inputs": ["close"], "func": maev_155_sma20_rat_vel_252d},
    "maev_156_ema20_rat_vel_5d": {"inputs": ["close"], "func": maev_156_ema20_rat_vel_5d},
    "maev_157_ema20_rat_vel_21d": {"inputs": ["close"], "func": maev_157_ema20_rat_vel_21d},
    "maev_158_ema20_rat_vel_63d": {"inputs": ["close"], "func": maev_158_ema20_rat_vel_63d},
    "maev_159_ema20_rat_vel_126d": {"inputs": ["close"], "func": maev_159_ema20_rat_vel_126d},
    "maev_160_ema20_rat_vel_252d": {"inputs": ["close"], "func": maev_160_ema20_rat_vel_252d},
    "maev_161_sma50_rat_vel_5d": {"inputs": ["close"], "func": maev_161_sma50_rat_vel_5d},
    "maev_162_sma50_rat_vel_21d": {"inputs": ["close"], "func": maev_162_sma50_rat_vel_21d},
    "maev_163_sma50_rat_vel_63d": {"inputs": ["close"], "func": maev_163_sma50_rat_vel_63d},
    "maev_164_sma50_rat_vel_126d": {"inputs": ["close"], "func": maev_164_sma50_rat_vel_126d},
    "maev_165_sma50_rat_vel_252d": {"inputs": ["close"], "func": maev_165_sma50_rat_vel_252d},
    "maev_166_sma200_rat_vel_5d": {"inputs": ["close"], "func": maev_166_sma200_rat_vel_5d},
    "maev_167_sma200_rat_vel_21d": {"inputs": ["close"], "func": maev_167_sma200_rat_vel_21d},
    "maev_168_sma200_rat_vel_63d": {"inputs": ["close"], "func": maev_168_sma200_rat_vel_63d},
    "maev_169_sma200_rat_vel_126d": {"inputs": ["close"], "func": maev_169_sma200_rat_vel_126d},
    "maev_170_sma200_rat_vel_252d": {"inputs": ["close"], "func": maev_170_sma200_rat_vel_252d},
    "maev_171_cross_rat_vel_5d": {"inputs": ["close"], "func": maev_171_cross_rat_vel_5d},
    "maev_172_cross_rat_vel_21d": {"inputs": ["close"], "func": maev_172_cross_rat_vel_21d},
    "maev_173_cross_rat_vel_63d": {"inputs": ["close"], "func": maev_173_cross_rat_vel_63d},
    "maev_174_cross_rat_vel_126d": {"inputs": ["close"], "func": maev_174_cross_rat_vel_126d},
    "maev_175_cross_rat_vel_252d": {"inputs": ["close"], "func": maev_175_cross_rat_vel_252d},
}
