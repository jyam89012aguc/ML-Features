"""
89_mass_dynamics — 2nd Derivatives (Velocity)
Domain: mass_dynamics
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

def mass_151_range_ema_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_151_range_ema_vel_5d"""
    return ((high - low).ewm(span=9).mean()).diff(5)

def mass_152_range_ema_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_152_range_ema_vel_21d"""
    return ((high - low).ewm(span=9).mean()).diff(21)

def mass_153_range_ema_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_153_range_ema_vel_63d"""
    return ((high - low).ewm(span=9).mean()).diff(63)

def mass_154_range_ema_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_154_range_ema_vel_126d"""
    return ((high - low).ewm(span=9).mean()).diff(126)

def mass_155_range_ema_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_155_range_ema_vel_252d"""
    return ((high - low).ewm(span=9).mean()).diff(252)

def mass_156_range_dema_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_156_range_dema_vel_5d"""
    return ((high - low).ewm(span=9).mean().ewm(span=9).mean()).diff(5)

def mass_157_range_dema_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_157_range_dema_vel_21d"""
    return ((high - low).ewm(span=9).mean().ewm(span=9).mean()).diff(21)

def mass_158_range_dema_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_158_range_dema_vel_63d"""
    return ((high - low).ewm(span=9).mean().ewm(span=9).mean()).diff(63)

def mass_159_range_dema_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_159_range_dema_vel_126d"""
    return ((high - low).ewm(span=9).mean().ewm(span=9).mean()).diff(126)

def mass_160_range_dema_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_160_range_dema_vel_252d"""
    return ((high - low).ewm(span=9).mean().ewm(span=9).mean()).diff(252)

def mass_161_mass_idx_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_161_mass_idx_vel_5d"""
    return (_safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())).diff(5)

def mass_162_mass_idx_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_162_mass_idx_vel_21d"""
    return (_safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())).diff(21)

def mass_163_mass_idx_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_163_mass_idx_vel_63d"""
    return (_safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())).diff(63)

def mass_164_mass_idx_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_164_mass_idx_vel_126d"""
    return (_safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())).diff(126)

def mass_165_mass_idx_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_165_mass_idx_vel_252d"""
    return (_safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())).diff(252)

def mass_166_range_std_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_166_range_std_vel_5d"""
    return (_rolling_std(high - low, 9)).diff(5)

def mass_167_range_std_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_167_range_std_vel_21d"""
    return (_rolling_std(high - low, 9)).diff(21)

def mass_168_range_std_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_168_range_std_vel_63d"""
    return (_rolling_std(high - low, 9)).diff(63)

def mass_169_range_std_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_169_range_std_vel_126d"""
    return (_rolling_std(high - low, 9)).diff(126)

def mass_170_range_std_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_170_range_std_vel_252d"""
    return (_rolling_std(high - low, 9)).diff(252)

def mass_171_range_lvl_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_171_range_lvl_vel_5d"""
    return (high - low).diff(5)

def mass_172_range_lvl_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_172_range_lvl_vel_21d"""
    return (high - low).diff(21)

def mass_173_range_lvl_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_173_range_lvl_vel_63d"""
    return (high - low).diff(63)

def mass_174_range_lvl_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_174_range_lvl_vel_126d"""
    return (high - low).diff(126)

def mass_175_range_lvl_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_175_range_lvl_vel_252d"""
    return (high - low).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V89_REGISTRY_VEL = {
    "mass_151_range_ema_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_151_range_ema_vel_5d},
    "mass_152_range_ema_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_152_range_ema_vel_21d},
    "mass_153_range_ema_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_153_range_ema_vel_63d},
    "mass_154_range_ema_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_154_range_ema_vel_126d},
    "mass_155_range_ema_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_155_range_ema_vel_252d},
    "mass_156_range_dema_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_156_range_dema_vel_5d},
    "mass_157_range_dema_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_157_range_dema_vel_21d},
    "mass_158_range_dema_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_158_range_dema_vel_63d},
    "mass_159_range_dema_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_159_range_dema_vel_126d},
    "mass_160_range_dema_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_160_range_dema_vel_252d},
    "mass_161_mass_idx_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_161_mass_idx_vel_5d},
    "mass_162_mass_idx_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_162_mass_idx_vel_21d},
    "mass_163_mass_idx_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_163_mass_idx_vel_63d},
    "mass_164_mass_idx_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_164_mass_idx_vel_126d},
    "mass_165_mass_idx_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_165_mass_idx_vel_252d},
    "mass_166_range_std_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_166_range_std_vel_5d},
    "mass_167_range_std_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_167_range_std_vel_21d},
    "mass_168_range_std_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_168_range_std_vel_63d},
    "mass_169_range_std_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_169_range_std_vel_126d},
    "mass_170_range_std_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_170_range_std_vel_252d},
    "mass_171_range_lvl_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_171_range_lvl_vel_5d},
    "mass_172_range_lvl_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_172_range_lvl_vel_21d},
    "mass_173_range_lvl_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_173_range_lvl_vel_63d},
    "mass_174_range_lvl_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_174_range_lvl_vel_126d},
    "mass_175_range_lvl_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_175_range_lvl_vel_252d},
}
