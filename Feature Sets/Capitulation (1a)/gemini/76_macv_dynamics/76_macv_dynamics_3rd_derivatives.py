"""
76_macv_dynamics — 3rd Derivatives (Acceleration)
Domain: macv_dynamics
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

def macv_176_macd_accel_5d(close: pd.Series) -> pd.Series:
    """macv_176_macd_accel_5d"""
    return (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(5).diff(21)

def macv_177_macd_accel_21d(close: pd.Series) -> pd.Series:
    """macv_177_macd_accel_21d"""
    return (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(21).diff(21)

def macv_178_macd_accel_63d(close: pd.Series) -> pd.Series:
    """macv_178_macd_accel_63d"""
    return (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(63).diff(21)

def macv_179_macd_accel_126d(close: pd.Series) -> pd.Series:
    """macv_179_macd_accel_126d"""
    return (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(126).diff(21)

def macv_180_macd_accel_252d(close: pd.Series) -> pd.Series:
    """macv_180_macd_accel_252d"""
    return (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(252).diff(21)

def macv_181_signal_accel_5d(close: pd.Series) -> pd.Series:
    """macv_181_signal_accel_5d"""
    return (_ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(5).diff(21)

def macv_182_signal_accel_21d(close: pd.Series) -> pd.Series:
    """macv_182_signal_accel_21d"""
    return (_ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(21).diff(21)

def macv_183_signal_accel_63d(close: pd.Series) -> pd.Series:
    """macv_183_signal_accel_63d"""
    return (_ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(63).diff(21)

def macv_184_signal_accel_126d(close: pd.Series) -> pd.Series:
    """macv_184_signal_accel_126d"""
    return (_ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(126).diff(21)

def macv_185_signal_accel_252d(close: pd.Series) -> pd.Series:
    """macv_185_signal_accel_252d"""
    return (_ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(252).diff(21)

def macv_186_hist_accel_5d(close: pd.Series) -> pd.Series:
    """macv_186_hist_accel_5d"""
    return ((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(5).diff(21)

def macv_187_hist_accel_21d(close: pd.Series) -> pd.Series:
    """macv_187_hist_accel_21d"""
    return ((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(21).diff(21)

def macv_188_hist_accel_63d(close: pd.Series) -> pd.Series:
    """macv_188_hist_accel_63d"""
    return ((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(63).diff(21)

def macv_189_hist_accel_126d(close: pd.Series) -> pd.Series:
    """macv_189_hist_accel_126d"""
    return ((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(126).diff(21)

def macv_190_hist_accel_252d(close: pd.Series) -> pd.Series:
    """macv_190_hist_accel_252d"""
    return ((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(252).diff(21)

def macv_191_macd_rat_accel_5d(close: pd.Series) -> pd.Series:
    """macv_191_macd_rat_accel_5d"""
    return (_safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)).diff(5).diff(21)

def macv_192_macd_rat_accel_21d(close: pd.Series) -> pd.Series:
    """macv_192_macd_rat_accel_21d"""
    return (_safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)).diff(21).diff(21)

def macv_193_macd_rat_accel_63d(close: pd.Series) -> pd.Series:
    """macv_193_macd_rat_accel_63d"""
    return (_safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)).diff(63).diff(21)

def macv_194_macd_rat_accel_126d(close: pd.Series) -> pd.Series:
    """macv_194_macd_rat_accel_126d"""
    return (_safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)).diff(126).diff(21)

def macv_195_macd_rat_accel_252d(close: pd.Series) -> pd.Series:
    """macv_195_macd_rat_accel_252d"""
    return (_safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)).diff(252).diff(21)

def macv_196_macd_z_accel_5d(close: pd.Series) -> pd.Series:
    """macv_196_macd_z_accel_5d"""
    return (_zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)).diff(5).diff(21)

def macv_197_macd_z_accel_21d(close: pd.Series) -> pd.Series:
    """macv_197_macd_z_accel_21d"""
    return (_zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)).diff(21).diff(21)

def macv_198_macd_z_accel_63d(close: pd.Series) -> pd.Series:
    """macv_198_macd_z_accel_63d"""
    return (_zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)).diff(63).diff(21)

def macv_199_macd_z_accel_126d(close: pd.Series) -> pd.Series:
    """macv_199_macd_z_accel_126d"""
    return (_zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)).diff(126).diff(21)

def macv_200_macd_z_accel_252d(close: pd.Series) -> pd.Series:
    """macv_200_macd_z_accel_252d"""
    return (_zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V76_REGISTRY_ACCEL = {
    "macv_176_macd_accel_5d": {"inputs": ["close"], "func": macv_176_macd_accel_5d},
    "macv_177_macd_accel_21d": {"inputs": ["close"], "func": macv_177_macd_accel_21d},
    "macv_178_macd_accel_63d": {"inputs": ["close"], "func": macv_178_macd_accel_63d},
    "macv_179_macd_accel_126d": {"inputs": ["close"], "func": macv_179_macd_accel_126d},
    "macv_180_macd_accel_252d": {"inputs": ["close"], "func": macv_180_macd_accel_252d},
    "macv_181_signal_accel_5d": {"inputs": ["close"], "func": macv_181_signal_accel_5d},
    "macv_182_signal_accel_21d": {"inputs": ["close"], "func": macv_182_signal_accel_21d},
    "macv_183_signal_accel_63d": {"inputs": ["close"], "func": macv_183_signal_accel_63d},
    "macv_184_signal_accel_126d": {"inputs": ["close"], "func": macv_184_signal_accel_126d},
    "macv_185_signal_accel_252d": {"inputs": ["close"], "func": macv_185_signal_accel_252d},
    "macv_186_hist_accel_5d": {"inputs": ["close"], "func": macv_186_hist_accel_5d},
    "macv_187_hist_accel_21d": {"inputs": ["close"], "func": macv_187_hist_accel_21d},
    "macv_188_hist_accel_63d": {"inputs": ["close"], "func": macv_188_hist_accel_63d},
    "macv_189_hist_accel_126d": {"inputs": ["close"], "func": macv_189_hist_accel_126d},
    "macv_190_hist_accel_252d": {"inputs": ["close"], "func": macv_190_hist_accel_252d},
    "macv_191_macd_rat_accel_5d": {"inputs": ["close"], "func": macv_191_macd_rat_accel_5d},
    "macv_192_macd_rat_accel_21d": {"inputs": ["close"], "func": macv_192_macd_rat_accel_21d},
    "macv_193_macd_rat_accel_63d": {"inputs": ["close"], "func": macv_193_macd_rat_accel_63d},
    "macv_194_macd_rat_accel_126d": {"inputs": ["close"], "func": macv_194_macd_rat_accel_126d},
    "macv_195_macd_rat_accel_252d": {"inputs": ["close"], "func": macv_195_macd_rat_accel_252d},
    "macv_196_macd_z_accel_5d": {"inputs": ["close"], "func": macv_196_macd_z_accel_5d},
    "macv_197_macd_z_accel_21d": {"inputs": ["close"], "func": macv_197_macd_z_accel_21d},
    "macv_198_macd_z_accel_63d": {"inputs": ["close"], "func": macv_198_macd_z_accel_63d},
    "macv_199_macd_z_accel_126d": {"inputs": ["close"], "func": macv_199_macd_z_accel_126d},
    "macv_200_macd_z_accel_252d": {"inputs": ["close"], "func": macv_200_macd_z_accel_252d},
}
