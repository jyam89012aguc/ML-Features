"""
100_trgc_composite — 2nd Derivatives (Velocity)
Domain: trgc_composite
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

def trgc_151_comp_mom_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_151_comp_mom_vel_5d"""
    return (close.pct_change(21) + close.pct_change(63) + close.pct_change(252)).diff(5)

def trgc_152_comp_mom_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_152_comp_mom_vel_21d"""
    return (close.pct_change(21) + close.pct_change(63) + close.pct_change(252)).diff(21)

def trgc_153_comp_mom_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_153_comp_mom_vel_63d"""
    return (close.pct_change(21) + close.pct_change(63) + close.pct_change(252)).diff(63)

def trgc_154_comp_mom_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_154_comp_mom_vel_126d"""
    return (close.pct_change(21) + close.pct_change(63) + close.pct_change(252)).diff(126)

def trgc_155_comp_mom_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_155_comp_mom_vel_252d"""
    return (close.pct_change(21) + close.pct_change(63) + close.pct_change(252)).diff(252)

def trgc_156_comp_vol_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_156_comp_vol_vel_5d"""
    return (_rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)).diff(5)

def trgc_157_comp_vol_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_157_comp_vol_vel_21d"""
    return (_rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)).diff(21)

def trgc_158_comp_vol_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_158_comp_vol_vel_63d"""
    return (_rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)).diff(63)

def trgc_159_comp_vol_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_159_comp_vol_vel_126d"""
    return (_rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)).diff(126)

def trgc_160_comp_vol_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_160_comp_vol_vel_252d"""
    return (_rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)).diff(252)

def trgc_161_comp_adv_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_161_comp_adv_vel_5d"""
    return (_safe_div(volume * close, _rolling_mean(volume * close, 252))).diff(5)

def trgc_162_comp_adv_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_162_comp_adv_vel_21d"""
    return (_safe_div(volume * close, _rolling_mean(volume * close, 252))).diff(21)

def trgc_163_comp_adv_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_163_comp_adv_vel_63d"""
    return (_safe_div(volume * close, _rolling_mean(volume * close, 252))).diff(63)

def trgc_164_comp_adv_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_164_comp_adv_vel_126d"""
    return (_safe_div(volume * close, _rolling_mean(volume * close, 252))).diff(126)

def trgc_165_comp_adv_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_165_comp_adv_vel_252d"""
    return (_safe_div(volume * close, _rolling_mean(volume * close, 252))).diff(252)

def trgc_166_comp_range_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_166_comp_range_vel_5d"""
    return (_safe_div(high - low, close)).diff(5)

def trgc_167_comp_range_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_167_comp_range_vel_21d"""
    return (_safe_div(high - low, close)).diff(21)

def trgc_168_comp_range_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_168_comp_range_vel_63d"""
    return (_safe_div(high - low, close)).diff(63)

def trgc_169_comp_range_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_169_comp_range_vel_126d"""
    return (_safe_div(high - low, close)).diff(126)

def trgc_170_comp_range_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_170_comp_range_vel_252d"""
    return (_safe_div(high - low, close)).diff(252)

def trgc_171_comp_trend_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_171_comp_trend_vel_5d"""
    return (_safe_div(close, _rolling_mean(close, 252))).diff(5)

def trgc_172_comp_trend_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_172_comp_trend_vel_21d"""
    return (_safe_div(close, _rolling_mean(close, 252))).diff(21)

def trgc_173_comp_trend_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_173_comp_trend_vel_63d"""
    return (_safe_div(close, _rolling_mean(close, 252))).diff(63)

def trgc_174_comp_trend_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_174_comp_trend_vel_126d"""
    return (_safe_div(close, _rolling_mean(close, 252))).diff(126)

def trgc_175_comp_trend_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_175_comp_trend_vel_252d"""
    return (_safe_div(close, _rolling_mean(close, 252))).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V100_REGISTRY_VEL = {
    "trgc_151_comp_mom_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_151_comp_mom_vel_5d},
    "trgc_152_comp_mom_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_152_comp_mom_vel_21d},
    "trgc_153_comp_mom_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_153_comp_mom_vel_63d},
    "trgc_154_comp_mom_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_154_comp_mom_vel_126d},
    "trgc_155_comp_mom_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_155_comp_mom_vel_252d},
    "trgc_156_comp_vol_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_156_comp_vol_vel_5d},
    "trgc_157_comp_vol_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_157_comp_vol_vel_21d},
    "trgc_158_comp_vol_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_158_comp_vol_vel_63d},
    "trgc_159_comp_vol_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_159_comp_vol_vel_126d},
    "trgc_160_comp_vol_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_160_comp_vol_vel_252d},
    "trgc_161_comp_adv_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_161_comp_adv_vel_5d},
    "trgc_162_comp_adv_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_162_comp_adv_vel_21d},
    "trgc_163_comp_adv_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_163_comp_adv_vel_63d},
    "trgc_164_comp_adv_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_164_comp_adv_vel_126d},
    "trgc_165_comp_adv_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_165_comp_adv_vel_252d},
    "trgc_166_comp_range_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_166_comp_range_vel_5d},
    "trgc_167_comp_range_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_167_comp_range_vel_21d},
    "trgc_168_comp_range_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_168_comp_range_vel_63d},
    "trgc_169_comp_range_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_169_comp_range_vel_126d},
    "trgc_170_comp_range_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_170_comp_range_vel_252d},
    "trgc_171_comp_trend_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_171_comp_trend_vel_5d},
    "trgc_172_comp_trend_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_172_comp_trend_vel_21d},
    "trgc_173_comp_trend_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_173_comp_trend_vel_63d},
    "trgc_174_comp_trend_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_174_comp_trend_vel_126d},
    "trgc_175_comp_trend_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_175_comp_trend_vel_252d},
}
