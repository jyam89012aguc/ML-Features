"""
85_frcd_dynamics — 2nd Derivatives (Velocity)
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

def frcd_151_fi_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_151_fi_vel_5d"""
    return ((close - close.shift(1)) * volume).diff(5)

def frcd_152_fi_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_152_fi_vel_21d"""
    return ((close - close.shift(1)) * volume).diff(21)

def frcd_153_fi_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_153_fi_vel_63d"""
    return ((close - close.shift(1)) * volume).diff(63)

def frcd_154_fi_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_154_fi_vel_126d"""
    return ((close - close.shift(1)) * volume).diff(126)

def frcd_155_fi_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_155_fi_vel_252d"""
    return ((close - close.shift(1)) * volume).diff(252)

def frcd_156_fi_ema13_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_156_fi_ema13_vel_5d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)

def frcd_157_fi_ema13_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_157_fi_ema13_vel_21d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(21)

def frcd_158_fi_ema13_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_158_fi_ema13_vel_63d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(63)

def frcd_159_fi_ema13_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_159_fi_ema13_vel_126d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(126)

def frcd_160_fi_ema13_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_160_fi_ema13_vel_252d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(252)

def frcd_161_fi_ema50_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_161_fi_ema50_vel_5d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 50)).diff(5)

def frcd_162_fi_ema50_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_162_fi_ema50_vel_21d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 50)).diff(21)

def frcd_163_fi_ema50_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_163_fi_ema50_vel_63d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 50)).diff(63)

def frcd_164_fi_ema50_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_164_fi_ema50_vel_126d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 50)).diff(126)

def frcd_165_fi_ema50_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_165_fi_ema50_vel_252d"""
    return (_ewm_mean((close - close.shift(1)) * volume, 50)).diff(252)

def frcd_166_fi_z_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_166_fi_z_vel_5d"""
    return (_zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)).diff(5)

def frcd_167_fi_z_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_167_fi_z_vel_21d"""
    return (_zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)).diff(21)

def frcd_168_fi_z_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_168_fi_z_vel_63d"""
    return (_zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)).diff(63)

def frcd_169_fi_z_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_169_fi_z_vel_126d"""
    return (_zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)).diff(126)

def frcd_170_fi_z_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_170_fi_z_vel_252d"""
    return (_zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)).diff(252)

def frcd_171_fi_slope_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_171_fi_slope_vel_5d"""
    return ((_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)).diff(5)

def frcd_172_fi_slope_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_172_fi_slope_vel_21d"""
    return ((_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)).diff(21)

def frcd_173_fi_slope_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_173_fi_slope_vel_63d"""
    return ((_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)).diff(63)

def frcd_174_fi_slope_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_174_fi_slope_vel_126d"""
    return ((_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)).diff(126)

def frcd_175_fi_slope_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_175_fi_slope_vel_252d"""
    return ((_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V85_REGISTRY_VEL = {
    "frcd_151_fi_vel_5d": {"inputs": ["close", "volume"], "func": frcd_151_fi_vel_5d},
    "frcd_152_fi_vel_21d": {"inputs": ["close", "volume"], "func": frcd_152_fi_vel_21d},
    "frcd_153_fi_vel_63d": {"inputs": ["close", "volume"], "func": frcd_153_fi_vel_63d},
    "frcd_154_fi_vel_126d": {"inputs": ["close", "volume"], "func": frcd_154_fi_vel_126d},
    "frcd_155_fi_vel_252d": {"inputs": ["close", "volume"], "func": frcd_155_fi_vel_252d},
    "frcd_156_fi_ema13_vel_5d": {"inputs": ["close", "volume"], "func": frcd_156_fi_ema13_vel_5d},
    "frcd_157_fi_ema13_vel_21d": {"inputs": ["close", "volume"], "func": frcd_157_fi_ema13_vel_21d},
    "frcd_158_fi_ema13_vel_63d": {"inputs": ["close", "volume"], "func": frcd_158_fi_ema13_vel_63d},
    "frcd_159_fi_ema13_vel_126d": {"inputs": ["close", "volume"], "func": frcd_159_fi_ema13_vel_126d},
    "frcd_160_fi_ema13_vel_252d": {"inputs": ["close", "volume"], "func": frcd_160_fi_ema13_vel_252d},
    "frcd_161_fi_ema50_vel_5d": {"inputs": ["close", "volume"], "func": frcd_161_fi_ema50_vel_5d},
    "frcd_162_fi_ema50_vel_21d": {"inputs": ["close", "volume"], "func": frcd_162_fi_ema50_vel_21d},
    "frcd_163_fi_ema50_vel_63d": {"inputs": ["close", "volume"], "func": frcd_163_fi_ema50_vel_63d},
    "frcd_164_fi_ema50_vel_126d": {"inputs": ["close", "volume"], "func": frcd_164_fi_ema50_vel_126d},
    "frcd_165_fi_ema50_vel_252d": {"inputs": ["close", "volume"], "func": frcd_165_fi_ema50_vel_252d},
    "frcd_166_fi_z_vel_5d": {"inputs": ["close", "volume"], "func": frcd_166_fi_z_vel_5d},
    "frcd_167_fi_z_vel_21d": {"inputs": ["close", "volume"], "func": frcd_167_fi_z_vel_21d},
    "frcd_168_fi_z_vel_63d": {"inputs": ["close", "volume"], "func": frcd_168_fi_z_vel_63d},
    "frcd_169_fi_z_vel_126d": {"inputs": ["close", "volume"], "func": frcd_169_fi_z_vel_126d},
    "frcd_170_fi_z_vel_252d": {"inputs": ["close", "volume"], "func": frcd_170_fi_z_vel_252d},
    "frcd_171_fi_slope_vel_5d": {"inputs": ["close", "volume"], "func": frcd_171_fi_slope_vel_5d},
    "frcd_172_fi_slope_vel_21d": {"inputs": ["close", "volume"], "func": frcd_172_fi_slope_vel_21d},
    "frcd_173_fi_slope_vel_63d": {"inputs": ["close", "volume"], "func": frcd_173_fi_slope_vel_63d},
    "frcd_174_fi_slope_vel_126d": {"inputs": ["close", "volume"], "func": frcd_174_fi_slope_vel_126d},
    "frcd_175_fi_slope_vel_252d": {"inputs": ["close", "volume"], "func": frcd_175_fi_slope_vel_252d},
}
