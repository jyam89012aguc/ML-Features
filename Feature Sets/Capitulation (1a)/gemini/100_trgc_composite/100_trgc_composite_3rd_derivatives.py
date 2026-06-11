"""
100_trgc_composite — 3rd Derivatives (Acceleration)
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

def trgc_176_comp_mom_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_176_comp_mom_accel_5d"""
    return (close.pct_change(21) + close.pct_change(63) + close.pct_change(252)).diff(5).diff(21)

def trgc_177_comp_mom_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_177_comp_mom_accel_21d"""
    return (close.pct_change(21) + close.pct_change(63) + close.pct_change(252)).diff(21).diff(21)

def trgc_178_comp_mom_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_178_comp_mom_accel_63d"""
    return (close.pct_change(21) + close.pct_change(63) + close.pct_change(252)).diff(63).diff(21)

def trgc_179_comp_mom_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_179_comp_mom_accel_126d"""
    return (close.pct_change(21) + close.pct_change(63) + close.pct_change(252)).diff(126).diff(21)

def trgc_180_comp_mom_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_180_comp_mom_accel_252d"""
    return (close.pct_change(21) + close.pct_change(63) + close.pct_change(252)).diff(252).diff(21)

def trgc_181_comp_vol_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_181_comp_vol_accel_5d"""
    return (_rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)).diff(5).diff(21)

def trgc_182_comp_vol_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_182_comp_vol_accel_21d"""
    return (_rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)).diff(21).diff(21)

def trgc_183_comp_vol_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_183_comp_vol_accel_63d"""
    return (_rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)).diff(63).diff(21)

def trgc_184_comp_vol_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_184_comp_vol_accel_126d"""
    return (_rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)).diff(126).diff(21)

def trgc_185_comp_vol_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_185_comp_vol_accel_252d"""
    return (_rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)).diff(252).diff(21)

def trgc_186_comp_adv_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_186_comp_adv_accel_5d"""
    return (_safe_div(volume * close, _rolling_mean(volume * close, 252))).diff(5).diff(21)

def trgc_187_comp_adv_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_187_comp_adv_accel_21d"""
    return (_safe_div(volume * close, _rolling_mean(volume * close, 252))).diff(21).diff(21)

def trgc_188_comp_adv_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_188_comp_adv_accel_63d"""
    return (_safe_div(volume * close, _rolling_mean(volume * close, 252))).diff(63).diff(21)

def trgc_189_comp_adv_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_189_comp_adv_accel_126d"""
    return (_safe_div(volume * close, _rolling_mean(volume * close, 252))).diff(126).diff(21)

def trgc_190_comp_adv_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_190_comp_adv_accel_252d"""
    return (_safe_div(volume * close, _rolling_mean(volume * close, 252))).diff(252).diff(21)

def trgc_191_comp_range_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_191_comp_range_accel_5d"""
    return (_safe_div(high - low, close)).diff(5).diff(21)

def trgc_192_comp_range_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_192_comp_range_accel_21d"""
    return (_safe_div(high - low, close)).diff(21).diff(21)

def trgc_193_comp_range_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_193_comp_range_accel_63d"""
    return (_safe_div(high - low, close)).diff(63).diff(21)

def trgc_194_comp_range_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_194_comp_range_accel_126d"""
    return (_safe_div(high - low, close)).diff(126).diff(21)

def trgc_195_comp_range_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_195_comp_range_accel_252d"""
    return (_safe_div(high - low, close)).diff(252).diff(21)

def trgc_196_comp_trend_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_196_comp_trend_accel_5d"""
    return (_safe_div(close, _rolling_mean(close, 252))).diff(5).diff(21)

def trgc_197_comp_trend_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_197_comp_trend_accel_21d"""
    return (_safe_div(close, _rolling_mean(close, 252))).diff(21).diff(21)

def trgc_198_comp_trend_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_198_comp_trend_accel_63d"""
    return (_safe_div(close, _rolling_mean(close, 252))).diff(63).diff(21)

def trgc_199_comp_trend_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_199_comp_trend_accel_126d"""
    return (_safe_div(close, _rolling_mean(close, 252))).diff(126).diff(21)

def trgc_200_comp_trend_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_200_comp_trend_accel_252d"""
    return (_safe_div(close, _rolling_mean(close, 252))).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V100_REGISTRY_ACCEL = {
    "trgc_176_comp_mom_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_176_comp_mom_accel_5d},
    "trgc_177_comp_mom_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_177_comp_mom_accel_21d},
    "trgc_178_comp_mom_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_178_comp_mom_accel_63d},
    "trgc_179_comp_mom_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_179_comp_mom_accel_126d},
    "trgc_180_comp_mom_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_180_comp_mom_accel_252d},
    "trgc_181_comp_vol_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_181_comp_vol_accel_5d},
    "trgc_182_comp_vol_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_182_comp_vol_accel_21d},
    "trgc_183_comp_vol_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_183_comp_vol_accel_63d},
    "trgc_184_comp_vol_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_184_comp_vol_accel_126d},
    "trgc_185_comp_vol_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_185_comp_vol_accel_252d},
    "trgc_186_comp_adv_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_186_comp_adv_accel_5d},
    "trgc_187_comp_adv_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_187_comp_adv_accel_21d},
    "trgc_188_comp_adv_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_188_comp_adv_accel_63d},
    "trgc_189_comp_adv_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_189_comp_adv_accel_126d},
    "trgc_190_comp_adv_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_190_comp_adv_accel_252d},
    "trgc_191_comp_range_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_191_comp_range_accel_5d},
    "trgc_192_comp_range_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_192_comp_range_accel_21d},
    "trgc_193_comp_range_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_193_comp_range_accel_63d},
    "trgc_194_comp_range_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_194_comp_range_accel_126d},
    "trgc_195_comp_range_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_195_comp_range_accel_252d},
    "trgc_196_comp_trend_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_196_comp_trend_accel_5d},
    "trgc_197_comp_trend_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_197_comp_trend_accel_21d},
    "trgc_198_comp_trend_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_198_comp_trend_accel_63d},
    "trgc_199_comp_trend_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_199_comp_trend_accel_126d},
    "trgc_200_comp_trend_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_200_comp_trend_accel_252d},
}
