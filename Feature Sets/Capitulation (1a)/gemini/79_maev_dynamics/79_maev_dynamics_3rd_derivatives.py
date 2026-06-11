"""
79_maev_dynamics — 3rd Derivatives (Acceleration)
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

def maev_176_sma20_rat_accel_5d(close: pd.Series) -> pd.Series:
    """maev_176_sma20_rat_accel_5d"""
    return (_safe_div(close, _rolling_mean(close, 20))).diff(5).diff(21)

def maev_177_sma20_rat_accel_21d(close: pd.Series) -> pd.Series:
    """maev_177_sma20_rat_accel_21d"""
    return (_safe_div(close, _rolling_mean(close, 20))).diff(21).diff(21)

def maev_178_sma20_rat_accel_63d(close: pd.Series) -> pd.Series:
    """maev_178_sma20_rat_accel_63d"""
    return (_safe_div(close, _rolling_mean(close, 20))).diff(63).diff(21)

def maev_179_sma20_rat_accel_126d(close: pd.Series) -> pd.Series:
    """maev_179_sma20_rat_accel_126d"""
    return (_safe_div(close, _rolling_mean(close, 20))).diff(126).diff(21)

def maev_180_sma20_rat_accel_252d(close: pd.Series) -> pd.Series:
    """maev_180_sma20_rat_accel_252d"""
    return (_safe_div(close, _rolling_mean(close, 20))).diff(252).diff(21)

def maev_181_ema20_rat_accel_5d(close: pd.Series) -> pd.Series:
    """maev_181_ema20_rat_accel_5d"""
    return (_safe_div(close, _ewm_mean(close, 20))).diff(5).diff(21)

def maev_182_ema20_rat_accel_21d(close: pd.Series) -> pd.Series:
    """maev_182_ema20_rat_accel_21d"""
    return (_safe_div(close, _ewm_mean(close, 20))).diff(21).diff(21)

def maev_183_ema20_rat_accel_63d(close: pd.Series) -> pd.Series:
    """maev_183_ema20_rat_accel_63d"""
    return (_safe_div(close, _ewm_mean(close, 20))).diff(63).diff(21)

def maev_184_ema20_rat_accel_126d(close: pd.Series) -> pd.Series:
    """maev_184_ema20_rat_accel_126d"""
    return (_safe_div(close, _ewm_mean(close, 20))).diff(126).diff(21)

def maev_185_ema20_rat_accel_252d(close: pd.Series) -> pd.Series:
    """maev_185_ema20_rat_accel_252d"""
    return (_safe_div(close, _ewm_mean(close, 20))).diff(252).diff(21)

def maev_186_sma50_rat_accel_5d(close: pd.Series) -> pd.Series:
    """maev_186_sma50_rat_accel_5d"""
    return (_safe_div(close, _rolling_mean(close, 50))).diff(5).diff(21)

def maev_187_sma50_rat_accel_21d(close: pd.Series) -> pd.Series:
    """maev_187_sma50_rat_accel_21d"""
    return (_safe_div(close, _rolling_mean(close, 50))).diff(21).diff(21)

def maev_188_sma50_rat_accel_63d(close: pd.Series) -> pd.Series:
    """maev_188_sma50_rat_accel_63d"""
    return (_safe_div(close, _rolling_mean(close, 50))).diff(63).diff(21)

def maev_189_sma50_rat_accel_126d(close: pd.Series) -> pd.Series:
    """maev_189_sma50_rat_accel_126d"""
    return (_safe_div(close, _rolling_mean(close, 50))).diff(126).diff(21)

def maev_190_sma50_rat_accel_252d(close: pd.Series) -> pd.Series:
    """maev_190_sma50_rat_accel_252d"""
    return (_safe_div(close, _rolling_mean(close, 50))).diff(252).diff(21)

def maev_191_sma200_rat_accel_5d(close: pd.Series) -> pd.Series:
    """maev_191_sma200_rat_accel_5d"""
    return (_safe_div(close, _rolling_mean(close, 200))).diff(5).diff(21)

def maev_192_sma200_rat_accel_21d(close: pd.Series) -> pd.Series:
    """maev_192_sma200_rat_accel_21d"""
    return (_safe_div(close, _rolling_mean(close, 200))).diff(21).diff(21)

def maev_193_sma200_rat_accel_63d(close: pd.Series) -> pd.Series:
    """maev_193_sma200_rat_accel_63d"""
    return (_safe_div(close, _rolling_mean(close, 200))).diff(63).diff(21)

def maev_194_sma200_rat_accel_126d(close: pd.Series) -> pd.Series:
    """maev_194_sma200_rat_accel_126d"""
    return (_safe_div(close, _rolling_mean(close, 200))).diff(126).diff(21)

def maev_195_sma200_rat_accel_252d(close: pd.Series) -> pd.Series:
    """maev_195_sma200_rat_accel_252d"""
    return (_safe_div(close, _rolling_mean(close, 200))).diff(252).diff(21)

def maev_196_cross_rat_accel_5d(close: pd.Series) -> pd.Series:
    """maev_196_cross_rat_accel_5d"""
    return (_safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))).diff(5).diff(21)

def maev_197_cross_rat_accel_21d(close: pd.Series) -> pd.Series:
    """maev_197_cross_rat_accel_21d"""
    return (_safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))).diff(21).diff(21)

def maev_198_cross_rat_accel_63d(close: pd.Series) -> pd.Series:
    """maev_198_cross_rat_accel_63d"""
    return (_safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))).diff(63).diff(21)

def maev_199_cross_rat_accel_126d(close: pd.Series) -> pd.Series:
    """maev_199_cross_rat_accel_126d"""
    return (_safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))).diff(126).diff(21)

def maev_200_cross_rat_accel_252d(close: pd.Series) -> pd.Series:
    """maev_200_cross_rat_accel_252d"""
    return (_safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V79_REGISTRY_ACCEL = {
    "maev_176_sma20_rat_accel_5d": {"inputs": ["close"], "func": maev_176_sma20_rat_accel_5d},
    "maev_177_sma20_rat_accel_21d": {"inputs": ["close"], "func": maev_177_sma20_rat_accel_21d},
    "maev_178_sma20_rat_accel_63d": {"inputs": ["close"], "func": maev_178_sma20_rat_accel_63d},
    "maev_179_sma20_rat_accel_126d": {"inputs": ["close"], "func": maev_179_sma20_rat_accel_126d},
    "maev_180_sma20_rat_accel_252d": {"inputs": ["close"], "func": maev_180_sma20_rat_accel_252d},
    "maev_181_ema20_rat_accel_5d": {"inputs": ["close"], "func": maev_181_ema20_rat_accel_5d},
    "maev_182_ema20_rat_accel_21d": {"inputs": ["close"], "func": maev_182_ema20_rat_accel_21d},
    "maev_183_ema20_rat_accel_63d": {"inputs": ["close"], "func": maev_183_ema20_rat_accel_63d},
    "maev_184_ema20_rat_accel_126d": {"inputs": ["close"], "func": maev_184_ema20_rat_accel_126d},
    "maev_185_ema20_rat_accel_252d": {"inputs": ["close"], "func": maev_185_ema20_rat_accel_252d},
    "maev_186_sma50_rat_accel_5d": {"inputs": ["close"], "func": maev_186_sma50_rat_accel_5d},
    "maev_187_sma50_rat_accel_21d": {"inputs": ["close"], "func": maev_187_sma50_rat_accel_21d},
    "maev_188_sma50_rat_accel_63d": {"inputs": ["close"], "func": maev_188_sma50_rat_accel_63d},
    "maev_189_sma50_rat_accel_126d": {"inputs": ["close"], "func": maev_189_sma50_rat_accel_126d},
    "maev_190_sma50_rat_accel_252d": {"inputs": ["close"], "func": maev_190_sma50_rat_accel_252d},
    "maev_191_sma200_rat_accel_5d": {"inputs": ["close"], "func": maev_191_sma200_rat_accel_5d},
    "maev_192_sma200_rat_accel_21d": {"inputs": ["close"], "func": maev_192_sma200_rat_accel_21d},
    "maev_193_sma200_rat_accel_63d": {"inputs": ["close"], "func": maev_193_sma200_rat_accel_63d},
    "maev_194_sma200_rat_accel_126d": {"inputs": ["close"], "func": maev_194_sma200_rat_accel_126d},
    "maev_195_sma200_rat_accel_252d": {"inputs": ["close"], "func": maev_195_sma200_rat_accel_252d},
    "maev_196_cross_rat_accel_5d": {"inputs": ["close"], "func": maev_196_cross_rat_accel_5d},
    "maev_197_cross_rat_accel_21d": {"inputs": ["close"], "func": maev_197_cross_rat_accel_21d},
    "maev_198_cross_rat_accel_63d": {"inputs": ["close"], "func": maev_198_cross_rat_accel_63d},
    "maev_199_cross_rat_accel_126d": {"inputs": ["close"], "func": maev_199_cross_rat_accel_126d},
    "maev_200_cross_rat_accel_252d": {"inputs": ["close"], "func": maev_200_cross_rat_accel_252d},
}
