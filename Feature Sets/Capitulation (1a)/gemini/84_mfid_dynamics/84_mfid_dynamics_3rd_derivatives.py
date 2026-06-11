"""
84_mfid_dynamics — 3rd Derivatives (Acceleration)
Domain: mfid_dynamics
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

def mfid_176_tp_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_176_tp_accel_5d"""
    return ((high + low + close) / 3).diff(5).diff(21)

def mfid_177_tp_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_177_tp_accel_21d"""
    return ((high + low + close) / 3).diff(21).diff(21)

def mfid_178_tp_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_178_tp_accel_63d"""
    return ((high + low + close) / 3).diff(63).diff(21)

def mfid_179_tp_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_179_tp_accel_126d"""
    return ((high + low + close) / 3).diff(126).diff(21)

def mfid_180_tp_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_180_tp_accel_252d"""
    return ((high + low + close) / 3).diff(252).diff(21)

def mfid_181_rmf_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_181_rmf_accel_5d"""
    return (((high + low + close) / 3) * volume).diff(5).diff(21)

def mfid_182_rmf_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_182_rmf_accel_21d"""
    return (((high + low + close) / 3) * volume).diff(21).diff(21)

def mfid_183_rmf_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_183_rmf_accel_63d"""
    return (((high + low + close) / 3) * volume).diff(63).diff(21)

def mfid_184_rmf_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_184_rmf_accel_126d"""
    return (((high + low + close) / 3) * volume).diff(126).diff(21)

def mfid_185_rmf_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_185_rmf_accel_252d"""
    return (((high + low + close) / 3) * volume).diff(252).diff(21)

def mfid_186_mfi14_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_186_mfi14_accel_5d"""
    return (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(5).diff(21)

def mfid_187_mfi14_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_187_mfi14_accel_21d"""
    return (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(21).diff(21)

def mfid_188_mfi14_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_188_mfi14_accel_63d"""
    return (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(63).diff(21)

def mfid_189_mfi14_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_189_mfi14_accel_126d"""
    return (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(126).diff(21)

def mfid_190_mfi14_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_190_mfi14_accel_252d"""
    return (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(252).diff(21)

def mfid_191_mfi_z_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_191_mfi_z_accel_5d"""
    return (_zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)).diff(5).diff(21)

def mfid_192_mfi_z_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_192_mfi_z_accel_21d"""
    return (_zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)).diff(21).diff(21)

def mfid_193_mfi_z_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_193_mfi_z_accel_63d"""
    return (_zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)).diff(63).diff(21)

def mfid_194_mfi_z_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_194_mfi_z_accel_126d"""
    return (_zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)).diff(126).diff(21)

def mfid_195_mfi_z_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_195_mfi_z_accel_252d"""
    return (_zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)).diff(252).diff(21)

def mfid_196_mfi_dist_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_196_mfi_dist_accel_5d"""
    return ((100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50).diff(5).diff(21)

def mfid_197_mfi_dist_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_197_mfi_dist_accel_21d"""
    return ((100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50).diff(21).diff(21)

def mfid_198_mfi_dist_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_198_mfi_dist_accel_63d"""
    return ((100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50).diff(63).diff(21)

def mfid_199_mfi_dist_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_199_mfi_dist_accel_126d"""
    return ((100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50).diff(126).diff(21)

def mfid_200_mfi_dist_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_200_mfi_dist_accel_252d"""
    return ((100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V84_REGISTRY_ACCEL = {
    "mfid_176_tp_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_176_tp_accel_5d},
    "mfid_177_tp_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_177_tp_accel_21d},
    "mfid_178_tp_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_178_tp_accel_63d},
    "mfid_179_tp_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_179_tp_accel_126d},
    "mfid_180_tp_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_180_tp_accel_252d},
    "mfid_181_rmf_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_181_rmf_accel_5d},
    "mfid_182_rmf_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_182_rmf_accel_21d},
    "mfid_183_rmf_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_183_rmf_accel_63d},
    "mfid_184_rmf_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_184_rmf_accel_126d},
    "mfid_185_rmf_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_185_rmf_accel_252d},
    "mfid_186_mfi14_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_186_mfi14_accel_5d},
    "mfid_187_mfi14_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_187_mfi14_accel_21d},
    "mfid_188_mfi14_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_188_mfi14_accel_63d},
    "mfid_189_mfi14_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_189_mfi14_accel_126d},
    "mfid_190_mfi14_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_190_mfi14_accel_252d},
    "mfid_191_mfi_z_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_191_mfi_z_accel_5d},
    "mfid_192_mfi_z_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_192_mfi_z_accel_21d},
    "mfid_193_mfi_z_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_193_mfi_z_accel_63d},
    "mfid_194_mfi_z_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_194_mfi_z_accel_126d},
    "mfid_195_mfi_z_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_195_mfi_z_accel_252d},
    "mfid_196_mfi_dist_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_196_mfi_dist_accel_5d},
    "mfid_197_mfi_dist_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_197_mfi_dist_accel_21d},
    "mfid_198_mfi_dist_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_198_mfi_dist_accel_63d},
    "mfid_199_mfi_dist_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_199_mfi_dist_accel_126d},
    "mfid_200_mfi_dist_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_200_mfi_dist_accel_252d},
}
