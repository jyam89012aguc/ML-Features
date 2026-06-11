"""
84_mfid_dynamics — 2nd Derivatives (Velocity)
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

def mfid_151_tp_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_151_tp_vel_5d"""
    return ((high + low + close) / 3).diff(5)

def mfid_152_tp_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_152_tp_vel_21d"""
    return ((high + low + close) / 3).diff(21)

def mfid_153_tp_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_153_tp_vel_63d"""
    return ((high + low + close) / 3).diff(63)

def mfid_154_tp_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_154_tp_vel_126d"""
    return ((high + low + close) / 3).diff(126)

def mfid_155_tp_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_155_tp_vel_252d"""
    return ((high + low + close) / 3).diff(252)

def mfid_156_rmf_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_156_rmf_vel_5d"""
    return (((high + low + close) / 3) * volume).diff(5)

def mfid_157_rmf_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_157_rmf_vel_21d"""
    return (((high + low + close) / 3) * volume).diff(21)

def mfid_158_rmf_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_158_rmf_vel_63d"""
    return (((high + low + close) / 3) * volume).diff(63)

def mfid_159_rmf_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_159_rmf_vel_126d"""
    return (((high + low + close) / 3) * volume).diff(126)

def mfid_160_rmf_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_160_rmf_vel_252d"""
    return (((high + low + close) / 3) * volume).diff(252)

def mfid_161_mfi14_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_161_mfi14_vel_5d"""
    return (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(5)

def mfid_162_mfi14_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_162_mfi14_vel_21d"""
    return (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(21)

def mfid_163_mfi14_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_163_mfi14_vel_63d"""
    return (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(63)

def mfid_164_mfi14_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_164_mfi14_vel_126d"""
    return (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(126)

def mfid_165_mfi14_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_165_mfi14_vel_252d"""
    return (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(252)

def mfid_166_mfi_z_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_166_mfi_z_vel_5d"""
    return (_zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)).diff(5)

def mfid_167_mfi_z_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_167_mfi_z_vel_21d"""
    return (_zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)).diff(21)

def mfid_168_mfi_z_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_168_mfi_z_vel_63d"""
    return (_zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)).diff(63)

def mfid_169_mfi_z_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_169_mfi_z_vel_126d"""
    return (_zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)).diff(126)

def mfid_170_mfi_z_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_170_mfi_z_vel_252d"""
    return (_zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)).diff(252)

def mfid_171_mfi_dist_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_171_mfi_dist_vel_5d"""
    return ((100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50).diff(5)

def mfid_172_mfi_dist_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_172_mfi_dist_vel_21d"""
    return ((100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50).diff(21)

def mfid_173_mfi_dist_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_173_mfi_dist_vel_63d"""
    return ((100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50).diff(63)

def mfid_174_mfi_dist_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_174_mfi_dist_vel_126d"""
    return ((100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50).diff(126)

def mfid_175_mfi_dist_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_175_mfi_dist_vel_252d"""
    return ((100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V84_REGISTRY_VEL = {
    "mfid_151_tp_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_151_tp_vel_5d},
    "mfid_152_tp_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_152_tp_vel_21d},
    "mfid_153_tp_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_153_tp_vel_63d},
    "mfid_154_tp_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_154_tp_vel_126d},
    "mfid_155_tp_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_155_tp_vel_252d},
    "mfid_156_rmf_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_156_rmf_vel_5d},
    "mfid_157_rmf_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_157_rmf_vel_21d},
    "mfid_158_rmf_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_158_rmf_vel_63d},
    "mfid_159_rmf_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_159_rmf_vel_126d},
    "mfid_160_rmf_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_160_rmf_vel_252d},
    "mfid_161_mfi14_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_161_mfi14_vel_5d},
    "mfid_162_mfi14_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_162_mfi14_vel_21d},
    "mfid_163_mfi14_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_163_mfi14_vel_63d},
    "mfid_164_mfi14_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_164_mfi14_vel_126d},
    "mfid_165_mfi14_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_165_mfi14_vel_252d},
    "mfid_166_mfi_z_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_166_mfi_z_vel_5d},
    "mfid_167_mfi_z_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_167_mfi_z_vel_21d},
    "mfid_168_mfi_z_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_168_mfi_z_vel_63d},
    "mfid_169_mfi_z_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_169_mfi_z_vel_126d},
    "mfid_170_mfi_z_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_170_mfi_z_vel_252d},
    "mfid_171_mfi_dist_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_171_mfi_dist_vel_5d},
    "mfid_172_mfi_dist_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_172_mfi_dist_vel_21d},
    "mfid_173_mfi_dist_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_173_mfi_dist_vel_63d},
    "mfid_174_mfi_dist_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_174_mfi_dist_vel_126d},
    "mfid_175_mfi_dist_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_175_mfi_dist_vel_252d},
}
