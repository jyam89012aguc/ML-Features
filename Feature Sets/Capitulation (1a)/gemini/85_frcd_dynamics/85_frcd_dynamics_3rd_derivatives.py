"""
85_frcd_dynamics — 3rd Derivatives (Acceleration)
Domain: frcd_dynamics
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

def frcd_176_fi_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_176_fi_accel_5d"""
    return ((close - close.shift(1)) * volume).diff(5).diff(21)

def frcd_177_fi_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_177_fi_accel_21d"""
    return ((close - close.shift(1)) * volume).diff(21).diff(21)

def frcd_178_fi_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_178_fi_accel_63d"""
    return ((close - close.shift(1)) * volume).diff(63).diff(21)

def frcd_179_fi_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_179_fi_accel_126d"""
    return ((close - close.shift(1)) * volume).diff(126).diff(21)

def frcd_180_fi_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_180_fi_accel_252d"""
    return ((close - close.shift(1)) * volume).diff(252).diff(21)

def frcd_181_fi_ema13_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_181_fi_ema13_accel_5d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5).diff(21)

def frcd_182_fi_ema13_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_182_fi_ema13_accel_21d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(21).diff(21)

def frcd_183_fi_ema13_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_183_fi_ema13_accel_63d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(63).diff(21)

def frcd_184_fi_ema13_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_184_fi_ema13_accel_126d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(126).diff(21)

def frcd_185_fi_ema13_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_185_fi_ema13_accel_252d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(252).diff(21)

def frcd_186_fi_ema50_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_186_fi_ema50_accel_5d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 50)).diff(5).diff(21)

def frcd_187_fi_ema50_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_187_fi_ema50_accel_21d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 50)).diff(21).diff(21)

def frcd_188_fi_ema50_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_188_fi_ema50_accel_63d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 50)).diff(63).diff(21)

def frcd_189_fi_ema50_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_189_fi_ema50_accel_126d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 50)).diff(126).diff(21)

def frcd_190_fi_ema50_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_190_fi_ema50_accel_252d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 50)).diff(252).diff(21)

def frcd_191_fi_z_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_191_fi_z_accel_5d"""
    return (_zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)).diff(5).diff(21)

def frcd_192_fi_z_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_192_fi_z_accel_21d"""
    return (_zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)).diff(21).diff(21)

def frcd_193_fi_z_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_193_fi_z_accel_63d"""
    return (_zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)).diff(63).diff(21)

def frcd_194_fi_z_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_194_fi_z_accel_126d"""
    return (_zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)).diff(126).diff(21)

def frcd_195_fi_z_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_195_fi_z_accel_252d"""
    return (_zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)).diff(252).diff(21)

def frcd_196_fi_slope_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_196_fi_slope_accel_5d"""
    return ((_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)).diff(5).diff(21)

def frcd_197_fi_slope_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_197_fi_slope_accel_21d"""
    return ((_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)).diff(21).diff(21)

def frcd_198_fi_slope_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_198_fi_slope_accel_63d"""
    return ((_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)).diff(63).diff(21)

def frcd_199_fi_slope_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_199_fi_slope_accel_126d"""
    return ((_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)).diff(126).diff(21)

def frcd_200_fi_slope_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_200_fi_slope_accel_252d"""
    return ((_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V85_REGISTRY_ACCEL = {
    "frcd_176_fi_accel_5d": {"inputs": ["close", "volume"], "func": frcd_176_fi_accel_5d},
    "frcd_177_fi_accel_21d": {"inputs": ["close", "volume"], "func": frcd_177_fi_accel_21d},
    "frcd_178_fi_accel_63d": {"inputs": ["close", "volume"], "func": frcd_178_fi_accel_63d},
    "frcd_179_fi_accel_126d": {"inputs": ["close", "volume"], "func": frcd_179_fi_accel_126d},
    "frcd_180_fi_accel_252d": {"inputs": ["close", "volume"], "func": frcd_180_fi_accel_252d},
    "frcd_181_fi_ema13_accel_5d": {"inputs": ["close", "volume"], "func": frcd_181_fi_ema13_accel_5d},
    "frcd_182_fi_ema13_accel_21d": {"inputs": ["close", "volume"], "func": frcd_182_fi_ema13_accel_21d},
    "frcd_183_fi_ema13_accel_63d": {"inputs": ["close", "volume"], "func": frcd_183_fi_ema13_accel_63d},
    "frcd_184_fi_ema13_accel_126d": {"inputs": ["close", "volume"], "func": frcd_184_fi_ema13_accel_126d},
    "frcd_185_fi_ema13_accel_252d": {"inputs": ["close", "volume"], "func": frcd_185_fi_ema13_accel_252d},
    "frcd_186_fi_ema50_accel_5d": {"inputs": ["close", "volume"], "func": frcd_186_fi_ema50_accel_5d},
    "frcd_187_fi_ema50_accel_21d": {"inputs": ["close", "volume"], "func": frcd_187_fi_ema50_accel_21d},
    "frcd_188_fi_ema50_accel_63d": {"inputs": ["close", "volume"], "func": frcd_188_fi_ema50_accel_63d},
    "frcd_189_fi_ema50_accel_126d": {"inputs": ["close", "volume"], "func": frcd_189_fi_ema50_accel_126d},
    "frcd_190_fi_ema50_accel_252d": {"inputs": ["close", "volume"], "func": frcd_190_fi_ema50_accel_252d},
    "frcd_191_fi_z_accel_5d": {"inputs": ["close", "volume"], "func": frcd_191_fi_z_accel_5d},
    "frcd_192_fi_z_accel_21d": {"inputs": ["close", "volume"], "func": frcd_192_fi_z_accel_21d},
    "frcd_193_fi_z_accel_63d": {"inputs": ["close", "volume"], "func": frcd_193_fi_z_accel_63d},
    "frcd_194_fi_z_accel_126d": {"inputs": ["close", "volume"], "func": frcd_194_fi_z_accel_126d},
    "frcd_195_fi_z_accel_252d": {"inputs": ["close", "volume"], "func": frcd_195_fi_z_accel_252d},
    "frcd_196_fi_slope_accel_5d": {"inputs": ["close", "volume"], "func": frcd_196_fi_slope_accel_5d},
    "frcd_197_fi_slope_accel_21d": {"inputs": ["close", "volume"], "func": frcd_197_fi_slope_accel_21d},
    "frcd_198_fi_slope_accel_63d": {"inputs": ["close", "volume"], "func": frcd_198_fi_slope_accel_63d},
    "frcd_199_fi_slope_accel_126d": {"inputs": ["close", "volume"], "func": frcd_199_fi_slope_accel_126d},
    "frcd_200_fi_slope_accel_252d": {"inputs": ["close", "volume"], "func": frcd_200_fi_slope_accel_252d},
}
