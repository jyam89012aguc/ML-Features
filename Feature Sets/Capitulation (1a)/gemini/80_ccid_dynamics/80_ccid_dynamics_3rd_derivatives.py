"""
80_ccid_dynamics — 3rd Derivatives (Acceleration)
Domain: ccid_dynamics
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

def ccid_176_tp_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_176_tp_accel_5d"""
    return ((high + low + close) / 3).diff(5).diff(21)

def ccid_177_tp_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_177_tp_accel_21d"""
    return ((high + low + close) / 3).diff(21).diff(21)

def ccid_178_tp_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_178_tp_accel_63d"""
    return ((high + low + close) / 3).diff(63).diff(21)

def ccid_179_tp_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_179_tp_accel_126d"""
    return ((high + low + close) / 3).diff(126).diff(21)

def ccid_180_tp_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_180_tp_accel_252d"""
    return ((high + low + close) / 3).diff(252).diff(21)

def ccid_181_cci20_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_181_cci20_accel_5d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5).diff(21)

def ccid_182_cci20_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_182_cci20_accel_21d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(21).diff(21)

def ccid_183_cci20_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_183_cci20_accel_63d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(63).diff(21)

def ccid_184_cci20_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_184_cci20_accel_126d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(126).diff(21)

def ccid_185_cci20_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_185_cci20_accel_252d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(252).diff(21)

def ccid_186_cci_dist_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_186_cci_dist_accel_5d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100).diff(5).diff(21)

def ccid_187_cci_dist_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_187_cci_dist_accel_21d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100).diff(21).diff(21)

def ccid_188_cci_dist_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_188_cci_dist_accel_63d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100).diff(63).diff(21)

def ccid_189_cci_dist_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_189_cci_dist_accel_126d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100).diff(126).diff(21)

def ccid_190_cci_dist_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_190_cci_dist_accel_252d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100).diff(252).diff(21)

def ccid_191_cci_z_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_191_cci_z_accel_5d"""
    return (_zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)).diff(5).diff(21)

def ccid_192_cci_z_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_192_cci_z_accel_21d"""
    return (_zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)).diff(21).diff(21)

def ccid_193_cci_z_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_193_cci_z_accel_63d"""
    return (_zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)).diff(63).diff(21)

def ccid_194_cci_z_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_194_cci_z_accel_126d"""
    return (_zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)).diff(126).diff(21)

def ccid_195_cci_z_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_195_cci_z_accel_252d"""
    return (_zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)).diff(252).diff(21)

def ccid_196_cci_slope_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_196_cci_slope_accel_5d"""
    return ((_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)).diff(5).diff(21)

def ccid_197_cci_slope_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_197_cci_slope_accel_21d"""
    return ((_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)).diff(21).diff(21)

def ccid_198_cci_slope_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_198_cci_slope_accel_63d"""
    return ((_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)).diff(63).diff(21)

def ccid_199_cci_slope_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_199_cci_slope_accel_126d"""
    return ((_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)).diff(126).diff(21)

def ccid_200_cci_slope_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_200_cci_slope_accel_252d"""
    return ((_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V80_REGISTRY_ACCEL = {
    "ccid_176_tp_accel_5d": {"inputs": ["high", "low", "close"], "func": ccid_176_tp_accel_5d},
    "ccid_177_tp_accel_21d": {"inputs": ["high", "low", "close"], "func": ccid_177_tp_accel_21d},
    "ccid_178_tp_accel_63d": {"inputs": ["high", "low", "close"], "func": ccid_178_tp_accel_63d},
    "ccid_179_tp_accel_126d": {"inputs": ["high", "low", "close"], "func": ccid_179_tp_accel_126d},
    "ccid_180_tp_accel_252d": {"inputs": ["high", "low", "close"], "func": ccid_180_tp_accel_252d},
    "ccid_181_cci20_accel_5d": {"inputs": ["high", "low", "close"], "func": ccid_181_cci20_accel_5d},
    "ccid_182_cci20_accel_21d": {"inputs": ["high", "low", "close"], "func": ccid_182_cci20_accel_21d},
    "ccid_183_cci20_accel_63d": {"inputs": ["high", "low", "close"], "func": ccid_183_cci20_accel_63d},
    "ccid_184_cci20_accel_126d": {"inputs": ["high", "low", "close"], "func": ccid_184_cci20_accel_126d},
    "ccid_185_cci20_accel_252d": {"inputs": ["high", "low", "close"], "func": ccid_185_cci20_accel_252d},
    "ccid_186_cci_dist_accel_5d": {"inputs": ["high", "low", "close"], "func": ccid_186_cci_dist_accel_5d},
    "ccid_187_cci_dist_accel_21d": {"inputs": ["high", "low", "close"], "func": ccid_187_cci_dist_accel_21d},
    "ccid_188_cci_dist_accel_63d": {"inputs": ["high", "low", "close"], "func": ccid_188_cci_dist_accel_63d},
    "ccid_189_cci_dist_accel_126d": {"inputs": ["high", "low", "close"], "func": ccid_189_cci_dist_accel_126d},
    "ccid_190_cci_dist_accel_252d": {"inputs": ["high", "low", "close"], "func": ccid_190_cci_dist_accel_252d},
    "ccid_191_cci_z_accel_5d": {"inputs": ["high", "low", "close"], "func": ccid_191_cci_z_accel_5d},
    "ccid_192_cci_z_accel_21d": {"inputs": ["high", "low", "close"], "func": ccid_192_cci_z_accel_21d},
    "ccid_193_cci_z_accel_63d": {"inputs": ["high", "low", "close"], "func": ccid_193_cci_z_accel_63d},
    "ccid_194_cci_z_accel_126d": {"inputs": ["high", "low", "close"], "func": ccid_194_cci_z_accel_126d},
    "ccid_195_cci_z_accel_252d": {"inputs": ["high", "low", "close"], "func": ccid_195_cci_z_accel_252d},
    "ccid_196_cci_slope_accel_5d": {"inputs": ["high", "low", "close"], "func": ccid_196_cci_slope_accel_5d},
    "ccid_197_cci_slope_accel_21d": {"inputs": ["high", "low", "close"], "func": ccid_197_cci_slope_accel_21d},
    "ccid_198_cci_slope_accel_63d": {"inputs": ["high", "low", "close"], "func": ccid_198_cci_slope_accel_63d},
    "ccid_199_cci_slope_accel_126d": {"inputs": ["high", "low", "close"], "func": ccid_199_cci_slope_accel_126d},
    "ccid_200_cci_slope_accel_252d": {"inputs": ["high", "low", "close"], "func": ccid_200_cci_slope_accel_252d},
}
