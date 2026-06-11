"""
83_cmfd_dynamics — 3rd Derivatives (Acceleration)
Domain: cmfd_dynamics
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

def cmfd_176_mf_mult_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_176_mf_mult_accel_5d"""
    return (_safe_div((close - low) - (high - close), high - low)).diff(5).diff(21)

def cmfd_177_mf_mult_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_177_mf_mult_accel_21d"""
    return (_safe_div((close - low) - (high - close), high - low)).diff(21).diff(21)

def cmfd_178_mf_mult_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_178_mf_mult_accel_63d"""
    return (_safe_div((close - low) - (high - close), high - low)).diff(63).diff(21)

def cmfd_179_mf_mult_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_179_mf_mult_accel_126d"""
    return (_safe_div((close - low) - (high - close), high - low)).diff(126).diff(21)

def cmfd_180_mf_mult_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_180_mf_mult_accel_252d"""
    return (_safe_div((close - low) - (high - close), high - low)).diff(252).diff(21)

def cmfd_181_mf_vol_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_181_mf_vol_accel_5d"""
    return (_safe_div((close - low) - (high - close), high - low) * volume).diff(5).diff(21)

def cmfd_182_mf_vol_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_182_mf_vol_accel_21d"""
    return (_safe_div((close - low) - (high - close), high - low) * volume).diff(21).diff(21)

def cmfd_183_mf_vol_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_183_mf_vol_accel_63d"""
    return (_safe_div((close - low) - (high - close), high - low) * volume).diff(63).diff(21)

def cmfd_184_mf_vol_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_184_mf_vol_accel_126d"""
    return (_safe_div((close - low) - (high - close), high - low) * volume).diff(126).diff(21)

def cmfd_185_mf_vol_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_185_mf_vol_accel_252d"""
    return (_safe_div((close - low) - (high - close), high - low) * volume).diff(252).diff(21)

def cmfd_186_cmf20_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_186_cmf20_accel_5d"""
    return (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5).diff(21)

def cmfd_187_cmf20_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_187_cmf20_accel_21d"""
    return (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(21).diff(21)

def cmfd_188_cmf20_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_188_cmf20_accel_63d"""
    return (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(63).diff(21)

def cmfd_189_cmf20_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_189_cmf20_accel_126d"""
    return (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(126).diff(21)

def cmfd_190_cmf20_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_190_cmf20_accel_252d"""
    return (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(252).diff(21)

def cmfd_191_cmf_z_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_191_cmf_z_accel_5d"""
    return (_zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)).diff(5).diff(21)

def cmfd_192_cmf_z_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_192_cmf_z_accel_21d"""
    return (_zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)).diff(21).diff(21)

def cmfd_193_cmf_z_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_193_cmf_z_accel_63d"""
    return (_zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)).diff(63).diff(21)

def cmfd_194_cmf_z_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_194_cmf_z_accel_126d"""
    return (_zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)).diff(126).diff(21)

def cmfd_195_cmf_z_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_195_cmf_z_accel_252d"""
    return (_zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)).diff(252).diff(21)

def cmfd_196_cmf_slope_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_196_cmf_slope_accel_5d"""
    return ((_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)).diff(5).diff(21)

def cmfd_197_cmf_slope_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_197_cmf_slope_accel_21d"""
    return ((_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)).diff(21).diff(21)

def cmfd_198_cmf_slope_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_198_cmf_slope_accel_63d"""
    return ((_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)).diff(63).diff(21)

def cmfd_199_cmf_slope_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_199_cmf_slope_accel_126d"""
    return ((_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)).diff(126).diff(21)

def cmfd_200_cmf_slope_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_200_cmf_slope_accel_252d"""
    return ((_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V83_REGISTRY_ACCEL = {
    "cmfd_176_mf_mult_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_176_mf_mult_accel_5d},
    "cmfd_177_mf_mult_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_177_mf_mult_accel_21d},
    "cmfd_178_mf_mult_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_178_mf_mult_accel_63d},
    "cmfd_179_mf_mult_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_179_mf_mult_accel_126d},
    "cmfd_180_mf_mult_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_180_mf_mult_accel_252d},
    "cmfd_181_mf_vol_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_181_mf_vol_accel_5d},
    "cmfd_182_mf_vol_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_182_mf_vol_accel_21d},
    "cmfd_183_mf_vol_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_183_mf_vol_accel_63d},
    "cmfd_184_mf_vol_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_184_mf_vol_accel_126d},
    "cmfd_185_mf_vol_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_185_mf_vol_accel_252d},
    "cmfd_186_cmf20_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_186_cmf20_accel_5d},
    "cmfd_187_cmf20_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_187_cmf20_accel_21d},
    "cmfd_188_cmf20_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_188_cmf20_accel_63d},
    "cmfd_189_cmf20_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_189_cmf20_accel_126d},
    "cmfd_190_cmf20_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_190_cmf20_accel_252d},
    "cmfd_191_cmf_z_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_191_cmf_z_accel_5d},
    "cmfd_192_cmf_z_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_192_cmf_z_accel_21d},
    "cmfd_193_cmf_z_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_193_cmf_z_accel_63d},
    "cmfd_194_cmf_z_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_194_cmf_z_accel_126d},
    "cmfd_195_cmf_z_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_195_cmf_z_accel_252d},
    "cmfd_196_cmf_slope_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_196_cmf_slope_accel_5d},
    "cmfd_197_cmf_slope_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_197_cmf_slope_accel_21d},
    "cmfd_198_cmf_slope_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_198_cmf_slope_accel_63d},
    "cmfd_199_cmf_slope_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_199_cmf_slope_accel_126d},
    "cmfd_200_cmf_slope_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_200_cmf_slope_accel_252d},
}
