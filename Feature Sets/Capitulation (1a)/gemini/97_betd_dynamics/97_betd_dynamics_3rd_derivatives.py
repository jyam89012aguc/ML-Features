"""
97_betd_dynamics — 3rd Derivatives (Acceleration)
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

def betd_176_beta_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_176_beta_accel_5d"""
    return (_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())).diff(5).diff(21)

def betd_177_beta_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_177_beta_accel_21d"""
    return (_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())).diff(21).diff(21)

def betd_178_beta_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_178_beta_accel_63d"""
    return (_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())).diff(63).diff(21)

def betd_179_beta_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_179_beta_accel_126d"""
    return (_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())).diff(126).diff(21)

def betd_180_beta_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_180_beta_accel_252d"""
    return (_safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())).diff(252).diff(21)

def betd_181_corr_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_181_corr_accel_5d"""
    return (close.pct_change().rolling(252).corr(mkt_close.pct_change())).diff(5).diff(21)

def betd_182_corr_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_182_corr_accel_21d"""
    return (close.pct_change().rolling(252).corr(mkt_close.pct_change())).diff(21).diff(21)

def betd_183_corr_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_183_corr_accel_63d"""
    return (close.pct_change().rolling(252).corr(mkt_close.pct_change())).diff(63).diff(21)

def betd_184_corr_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_184_corr_accel_126d"""
    return (close.pct_change().rolling(252).corr(mkt_close.pct_change())).diff(126).diff(21)

def betd_185_corr_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_185_corr_accel_252d"""
    return (close.pct_change().rolling(252).corr(mkt_close.pct_change())).diff(252).diff(21)

def betd_186_idio_vol_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_186_idio_vol_accel_5d"""
    return (_rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)).diff(5).diff(21)

def betd_187_idio_vol_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_187_idio_vol_accel_21d"""
    return (_rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)).diff(21).diff(21)

def betd_188_idio_vol_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_188_idio_vol_accel_63d"""
    return (_rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)).diff(63).diff(21)

def betd_189_idio_vol_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_189_idio_vol_accel_126d"""
    return (_rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)).diff(126).diff(21)

def betd_190_idio_vol_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_190_idio_vol_accel_252d"""
    return (_rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)).diff(252).diff(21)

def betd_191_beta_63_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_191_beta_63_accel_5d"""
    return (_safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())).diff(5).diff(21)

def betd_192_beta_63_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_192_beta_63_accel_21d"""
    return (_safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())).diff(21).diff(21)

def betd_193_beta_63_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_193_beta_63_accel_63d"""
    return (_safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())).diff(63).diff(21)

def betd_194_beta_63_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_194_beta_63_accel_126d"""
    return (_safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())).diff(126).diff(21)

def betd_195_beta_63_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_195_beta_63_accel_252d"""
    return (_safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())).diff(252).diff(21)

def betd_196_corr_63_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_196_corr_63_accel_5d"""
    return (close.pct_change().rolling(63).corr(mkt_close.pct_change())).diff(5).diff(21)

def betd_197_corr_63_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_197_corr_63_accel_21d"""
    return (close.pct_change().rolling(63).corr(mkt_close.pct_change())).diff(21).diff(21)

def betd_198_corr_63_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_198_corr_63_accel_63d"""
    return (close.pct_change().rolling(63).corr(mkt_close.pct_change())).diff(63).diff(21)

def betd_199_corr_63_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_199_corr_63_accel_126d"""
    return (close.pct_change().rolling(63).corr(mkt_close.pct_change())).diff(126).diff(21)

def betd_200_corr_63_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_200_corr_63_accel_252d"""
    return (close.pct_change().rolling(63).corr(mkt_close.pct_change())).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V97_REGISTRY_ACCEL = {
    "betd_176_beta_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_176_beta_accel_5d},
    "betd_177_beta_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_177_beta_accel_21d},
    "betd_178_beta_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_178_beta_accel_63d},
    "betd_179_beta_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_179_beta_accel_126d},
    "betd_180_beta_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_180_beta_accel_252d},
    "betd_181_corr_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_181_corr_accel_5d},
    "betd_182_corr_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_182_corr_accel_21d},
    "betd_183_corr_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_183_corr_accel_63d},
    "betd_184_corr_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_184_corr_accel_126d},
    "betd_185_corr_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_185_corr_accel_252d},
    "betd_186_idio_vol_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_186_idio_vol_accel_5d},
    "betd_187_idio_vol_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_187_idio_vol_accel_21d},
    "betd_188_idio_vol_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_188_idio_vol_accel_63d},
    "betd_189_idio_vol_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_189_idio_vol_accel_126d},
    "betd_190_idio_vol_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_190_idio_vol_accel_252d},
    "betd_191_beta_63_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_191_beta_63_accel_5d},
    "betd_192_beta_63_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_192_beta_63_accel_21d},
    "betd_193_beta_63_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_193_beta_63_accel_63d},
    "betd_194_beta_63_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_194_beta_63_accel_126d},
    "betd_195_beta_63_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_195_beta_63_accel_252d},
    "betd_196_corr_63_accel_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_196_corr_63_accel_5d},
    "betd_197_corr_63_accel_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_197_corr_63_accel_21d},
    "betd_198_corr_63_accel_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_198_corr_63_accel_63d},
    "betd_199_corr_63_accel_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_199_corr_63_accel_126d},
    "betd_200_corr_63_accel_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_200_corr_63_accel_252d},
}
