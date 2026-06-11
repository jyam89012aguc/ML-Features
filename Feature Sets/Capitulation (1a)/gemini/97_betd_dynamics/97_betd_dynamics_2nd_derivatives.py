"""
97_betd_dynamics — 2nd Derivatives (Velocity)
Domain: betd_dynamics
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
    return s.rolling(w, min_periods=1).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

# ── Feature functions ────────────────────────────────────────────────────────

def betd_151_beta_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_151_beta_vel_5d"""
    return (_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())).diff(5)

def betd_152_beta_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_152_beta_vel_21d"""
    return (_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())).diff(21)

def betd_153_beta_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_153_beta_vel_63d"""
    return (_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())).diff(63)

def betd_154_beta_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_154_beta_vel_126d"""
    return (_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())).diff(126)

def betd_155_beta_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_155_beta_vel_252d"""
    return (_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())).diff(252)

def betd_156_corr_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_156_corr_vel_5d"""
    return (close.pct_change().rolling(252).corr(mkt_close.pct_change())).diff(5)

def betd_157_corr_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_157_corr_vel_21d"""
    return (close.pct_change().rolling(252).corr(mkt_close.pct_change())).diff(21)

def betd_158_corr_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_158_corr_vel_63d"""
    return (close.pct_change().rolling(252).corr(mkt_close.pct_change())).diff(63)

def betd_159_corr_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_159_corr_vel_126d"""
    return (close.pct_change().rolling(252).corr(mkt_close.pct_change())).diff(126)

def betd_160_corr_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_160_corr_vel_252d"""
    return (close.pct_change().rolling(252).corr(mkt_close.pct_change())).diff(252)

def betd_161_idio_vol_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_161_idio_vol_vel_5d"""
    return (_rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)).diff(5)

def betd_162_idio_vol_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_162_idio_vol_vel_21d"""
    return (_rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)).diff(21)

def betd_163_idio_vol_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_163_idio_vol_vel_63d"""
    return (_rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)).diff(63)

def betd_164_idio_vol_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_164_idio_vol_vel_126d"""
    return (_rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)).diff(126)

def betd_165_idio_vol_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_165_idio_vol_vel_252d"""
    return (_rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)).diff(252)

def betd_166_beta_63_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_166_beta_63_vel_5d"""
    return (_safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())).diff(5)

def betd_167_beta_63_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_167_beta_63_vel_21d"""
    return (_safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())).diff(21)

def betd_168_beta_63_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_168_beta_63_vel_63d"""
    return (_safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())).diff(63)

def betd_169_beta_63_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_169_beta_63_vel_126d"""
    return (_safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())).diff(126)

def betd_170_beta_63_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_170_beta_63_vel_252d"""
    return (_safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())).diff(252)

def betd_171_corr_63_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_171_corr_63_vel_5d"""
    return (close.pct_change().rolling(63).corr(mkt_close.pct_change())).diff(5)

def betd_172_corr_63_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_172_corr_63_vel_21d"""
    return (close.pct_change().rolling(63).corr(mkt_close.pct_change())).diff(21)

def betd_173_corr_63_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_173_corr_63_vel_63d"""
    return (close.pct_change().rolling(63).corr(mkt_close.pct_change())).diff(63)

def betd_174_corr_63_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_174_corr_63_vel_126d"""
    return (close.pct_change().rolling(63).corr(mkt_close.pct_change())).diff(126)

def betd_175_corr_63_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_175_corr_63_vel_252d"""
    return (close.pct_change().rolling(63).corr(mkt_close.pct_change())).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V97_REGISTRY_VEL = {
    "betd_151_beta_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_151_beta_vel_5d},
    "betd_152_beta_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_152_beta_vel_21d},
    "betd_153_beta_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_153_beta_vel_63d},
    "betd_154_beta_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_154_beta_vel_126d},
    "betd_155_beta_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_155_beta_vel_252d},
    "betd_156_corr_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_156_corr_vel_5d},
    "betd_157_corr_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_157_corr_vel_21d},
    "betd_158_corr_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_158_corr_vel_63d},
    "betd_159_corr_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_159_corr_vel_126d},
    "betd_160_corr_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_160_corr_vel_252d},
    "betd_161_idio_vol_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_161_idio_vol_vel_5d},
    "betd_162_idio_vol_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_162_idio_vol_vel_21d},
    "betd_163_idio_vol_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_163_idio_vol_vel_63d},
    "betd_164_idio_vol_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_164_idio_vol_vel_126d},
    "betd_165_idio_vol_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_165_idio_vol_vel_252d},
    "betd_166_beta_63_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_166_beta_63_vel_5d},
    "betd_167_beta_63_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_167_beta_63_vel_21d},
    "betd_168_beta_63_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_168_beta_63_vel_63d},
    "betd_169_beta_63_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_169_beta_63_vel_126d},
    "betd_170_beta_63_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_170_beta_63_vel_252d},
    "betd_171_corr_63_vel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_171_corr_63_vel_5d},
    "betd_172_corr_63_vel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_172_corr_63_vel_21d},
    "betd_173_corr_63_vel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_173_corr_63_vel_63d},
    "betd_174_corr_63_vel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_174_corr_63_vel_126d},
    "betd_175_corr_63_vel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_175_corr_63_vel_252d},
}
