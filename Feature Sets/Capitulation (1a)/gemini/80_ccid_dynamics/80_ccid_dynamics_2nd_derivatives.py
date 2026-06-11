"""
80_ccid_dynamics — 2nd Derivatives (Velocity)
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

def ccid_151_tp_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_151_tp_vel_5d"""
    return ((high + low + close) / 3).diff(5)

def ccid_152_tp_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_152_tp_vel_21d"""
    return ((high + low + close) / 3).diff(21)

def ccid_153_tp_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_153_tp_vel_63d"""
    return ((high + low + close) / 3).diff(63)

def ccid_154_tp_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_154_tp_vel_126d"""
    return ((high + low + close) / 3).diff(126)

def ccid_155_tp_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_155_tp_vel_252d"""
    return ((high + low + close) / 3).diff(252)

def ccid_156_cci20_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_156_cci20_vel_5d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)

def ccid_157_cci20_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_157_cci20_vel_21d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(21)

def ccid_158_cci20_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_158_cci20_vel_63d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(63)

def ccid_159_cci20_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_159_cci20_vel_126d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(126)

def ccid_160_cci20_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_160_cci20_vel_252d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(252)

def ccid_161_cci_dist_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_161_cci_dist_vel_5d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100).diff(5)

def ccid_162_cci_dist_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_162_cci_dist_vel_21d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100).diff(21)

def ccid_163_cci_dist_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_163_cci_dist_vel_63d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100).diff(63)

def ccid_164_cci_dist_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_164_cci_dist_vel_126d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100).diff(126)

def ccid_165_cci_dist_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_165_cci_dist_vel_252d"""
    return (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100).diff(252)

def ccid_166_cci_z_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_166_cci_z_vel_5d"""
    return (_zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)).diff(5)

def ccid_167_cci_z_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_167_cci_z_vel_21d"""
    return (_zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)).diff(21)

def ccid_168_cci_z_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_168_cci_z_vel_63d"""
    return (_zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)).diff(63)

def ccid_169_cci_z_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_169_cci_z_vel_126d"""
    return (_zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)).diff(126)

def ccid_170_cci_z_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_170_cci_z_vel_252d"""
    return (_zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)).diff(252)

def ccid_171_cci_slope_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_171_cci_slope_vel_5d"""
    return ((_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)).diff(5)

def ccid_172_cci_slope_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_172_cci_slope_vel_21d"""
    return ((_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)).diff(21)

def ccid_173_cci_slope_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_173_cci_slope_vel_63d"""
    return ((_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)).diff(63)

def ccid_174_cci_slope_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_174_cci_slope_vel_126d"""
    return ((_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)).diff(126)

def ccid_175_cci_slope_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_175_cci_slope_vel_252d"""
    return ((_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V80_REGISTRY_VEL = {
    "ccid_151_tp_vel_5d": {"inputs": ["high", "low", "close"], "func": ccid_151_tp_vel_5d},
    "ccid_152_tp_vel_21d": {"inputs": ["high", "low", "close"], "func": ccid_152_tp_vel_21d},
    "ccid_153_tp_vel_63d": {"inputs": ["high", "low", "close"], "func": ccid_153_tp_vel_63d},
    "ccid_154_tp_vel_126d": {"inputs": ["high", "low", "close"], "func": ccid_154_tp_vel_126d},
    "ccid_155_tp_vel_252d": {"inputs": ["high", "low", "close"], "func": ccid_155_tp_vel_252d},
    "ccid_156_cci20_vel_5d": {"inputs": ["high", "low", "close"], "func": ccid_156_cci20_vel_5d},
    "ccid_157_cci20_vel_21d": {"inputs": ["high", "low", "close"], "func": ccid_157_cci20_vel_21d},
    "ccid_158_cci20_vel_63d": {"inputs": ["high", "low", "close"], "func": ccid_158_cci20_vel_63d},
    "ccid_159_cci20_vel_126d": {"inputs": ["high", "low", "close"], "func": ccid_159_cci20_vel_126d},
    "ccid_160_cci20_vel_252d": {"inputs": ["high", "low", "close"], "func": ccid_160_cci20_vel_252d},
    "ccid_161_cci_dist_vel_5d": {"inputs": ["high", "low", "close"], "func": ccid_161_cci_dist_vel_5d},
    "ccid_162_cci_dist_vel_21d": {"inputs": ["high", "low", "close"], "func": ccid_162_cci_dist_vel_21d},
    "ccid_163_cci_dist_vel_63d": {"inputs": ["high", "low", "close"], "func": ccid_163_cci_dist_vel_63d},
    "ccid_164_cci_dist_vel_126d": {"inputs": ["high", "low", "close"], "func": ccid_164_cci_dist_vel_126d},
    "ccid_165_cci_dist_vel_252d": {"inputs": ["high", "low", "close"], "func": ccid_165_cci_dist_vel_252d},
    "ccid_166_cci_z_vel_5d": {"inputs": ["high", "low", "close"], "func": ccid_166_cci_z_vel_5d},
    "ccid_167_cci_z_vel_21d": {"inputs": ["high", "low", "close"], "func": ccid_167_cci_z_vel_21d},
    "ccid_168_cci_z_vel_63d": {"inputs": ["high", "low", "close"], "func": ccid_168_cci_z_vel_63d},
    "ccid_169_cci_z_vel_126d": {"inputs": ["high", "low", "close"], "func": ccid_169_cci_z_vel_126d},
    "ccid_170_cci_z_vel_252d": {"inputs": ["high", "low", "close"], "func": ccid_170_cci_z_vel_252d},
    "ccid_171_cci_slope_vel_5d": {"inputs": ["high", "low", "close"], "func": ccid_171_cci_slope_vel_5d},
    "ccid_172_cci_slope_vel_21d": {"inputs": ["high", "low", "close"], "func": ccid_172_cci_slope_vel_21d},
    "ccid_173_cci_slope_vel_63d": {"inputs": ["high", "low", "close"], "func": ccid_173_cci_slope_vel_63d},
    "ccid_174_cci_slope_vel_126d": {"inputs": ["high", "low", "close"], "func": ccid_174_cci_slope_vel_126d},
    "ccid_175_cci_slope_vel_252d": {"inputs": ["high", "low", "close"], "func": ccid_175_cci_slope_vel_252d},
}
