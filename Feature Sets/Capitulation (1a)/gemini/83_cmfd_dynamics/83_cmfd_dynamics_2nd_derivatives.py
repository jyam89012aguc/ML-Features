"""
83_cmfd_dynamics — 2nd Derivatives (Velocity)
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

def cmfd_151_mf_mult_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_151_mf_mult_vel_5d"""
    return (_safe_div((close - low) - (high - close), high - low)).diff(5)

def cmfd_152_mf_mult_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_152_mf_mult_vel_21d"""
    return (_safe_div((close - low) - (high - close), high - low)).diff(21)

def cmfd_153_mf_mult_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_153_mf_mult_vel_63d"""
    return (_safe_div((close - low) - (high - close), high - low)).diff(63)

def cmfd_154_mf_mult_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_154_mf_mult_vel_126d"""
    return (_safe_div((close - low) - (high - close), high - low)).diff(126)

def cmfd_155_mf_mult_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_155_mf_mult_vel_252d"""
    return (_safe_div((close - low) - (high - close), high - low)).diff(252)

def cmfd_156_mf_vol_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_156_mf_vol_vel_5d"""
    return (_safe_div((close - low) - (high - close), high - low) * volume).diff(5)

def cmfd_157_mf_vol_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_157_mf_vol_vel_21d"""
    return (_safe_div((close - low) - (high - close), high - low) * volume).diff(21)

def cmfd_158_mf_vol_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_158_mf_vol_vel_63d"""
    return (_safe_div((close - low) - (high - close), high - low) * volume).diff(63)

def cmfd_159_mf_vol_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_159_mf_vol_vel_126d"""
    return (_safe_div((close - low) - (high - close), high - low) * volume).diff(126)

def cmfd_160_mf_vol_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_160_mf_vol_vel_252d"""
    return (_safe_div((close - low) - (high - close), high - low) * volume).diff(252)

def cmfd_161_cmf20_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_161_cmf20_vel_5d"""
    return (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)

def cmfd_162_cmf20_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_162_cmf20_vel_21d"""
    return (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(21)

def cmfd_163_cmf20_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_163_cmf20_vel_63d"""
    return (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(63)

def cmfd_164_cmf20_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_164_cmf20_vel_126d"""
    return (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(126)

def cmfd_165_cmf20_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_165_cmf20_vel_252d"""
    return (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(252)

def cmfd_166_cmf_z_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_166_cmf_z_vel_5d"""
    return (_zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)).diff(5)

def cmfd_167_cmf_z_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_167_cmf_z_vel_21d"""
    return (_zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)).diff(21)

def cmfd_168_cmf_z_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_168_cmf_z_vel_63d"""
    return (_zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)).diff(63)

def cmfd_169_cmf_z_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_169_cmf_z_vel_126d"""
    return (_zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)).diff(126)

def cmfd_170_cmf_z_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_170_cmf_z_vel_252d"""
    return (_zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)).diff(252)

def cmfd_171_cmf_slope_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_171_cmf_slope_vel_5d"""
    return ((_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)).diff(5)

def cmfd_172_cmf_slope_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_172_cmf_slope_vel_21d"""
    return ((_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)).diff(21)

def cmfd_173_cmf_slope_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_173_cmf_slope_vel_63d"""
    return ((_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)).diff(63)

def cmfd_174_cmf_slope_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_174_cmf_slope_vel_126d"""
    return ((_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)).diff(126)

def cmfd_175_cmf_slope_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_175_cmf_slope_vel_252d"""
    return ((_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V83_REGISTRY_VEL = {
    "cmfd_151_mf_mult_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_151_mf_mult_vel_5d},
    "cmfd_152_mf_mult_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_152_mf_mult_vel_21d},
    "cmfd_153_mf_mult_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_153_mf_mult_vel_63d},
    "cmfd_154_mf_mult_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_154_mf_mult_vel_126d},
    "cmfd_155_mf_mult_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_155_mf_mult_vel_252d},
    "cmfd_156_mf_vol_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_156_mf_vol_vel_5d},
    "cmfd_157_mf_vol_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_157_mf_vol_vel_21d},
    "cmfd_158_mf_vol_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_158_mf_vol_vel_63d},
    "cmfd_159_mf_vol_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_159_mf_vol_vel_126d},
    "cmfd_160_mf_vol_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_160_mf_vol_vel_252d},
    "cmfd_161_cmf20_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_161_cmf20_vel_5d},
    "cmfd_162_cmf20_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_162_cmf20_vel_21d},
    "cmfd_163_cmf20_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_163_cmf20_vel_63d},
    "cmfd_164_cmf20_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_164_cmf20_vel_126d},
    "cmfd_165_cmf20_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_165_cmf20_vel_252d},
    "cmfd_166_cmf_z_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_166_cmf_z_vel_5d},
    "cmfd_167_cmf_z_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_167_cmf_z_vel_21d},
    "cmfd_168_cmf_z_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_168_cmf_z_vel_63d},
    "cmfd_169_cmf_z_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_169_cmf_z_vel_126d},
    "cmfd_170_cmf_z_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_170_cmf_z_vel_252d},
    "cmfd_171_cmf_slope_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_171_cmf_slope_vel_5d},
    "cmfd_172_cmf_slope_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_172_cmf_slope_vel_21d},
    "cmfd_173_cmf_slope_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_173_cmf_slope_vel_63d},
    "cmfd_174_cmf_slope_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_174_cmf_slope_vel_126d},
    "cmfd_175_cmf_slope_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_175_cmf_slope_vel_252d},
}
