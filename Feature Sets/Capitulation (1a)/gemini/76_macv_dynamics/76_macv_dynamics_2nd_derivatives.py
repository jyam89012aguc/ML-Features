"""
76_macv_dynamics — 2nd Derivatives (Velocity)
Domain: macv_dynamics
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

def macv_151_macd_vel_5d(close: pd.Series) -> pd.Series:
    """macv_151_macd_vel_5d"""
    return (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(5)

def macv_152_macd_vel_21d(close: pd.Series) -> pd.Series:
    """macv_152_macd_vel_21d"""
    return (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(21)

def macv_153_macd_vel_63d(close: pd.Series) -> pd.Series:
    """macv_153_macd_vel_63d"""
    return (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(63)

def macv_154_macd_vel_126d(close: pd.Series) -> pd.Series:
    """macv_154_macd_vel_126d"""
    return (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(126)

def macv_155_macd_vel_252d(close: pd.Series) -> pd.Series:
    """macv_155_macd_vel_252d"""
    return (_ewm_mean(close, 12) - _ewm_mean(close, 26)).diff(252)

def macv_156_signal_vel_5d(close: pd.Series) -> pd.Series:
    """macv_156_signal_vel_5d"""
    return (_ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(5)

def macv_157_signal_vel_21d(close: pd.Series) -> pd.Series:
    """macv_157_signal_vel_21d"""
    return (_ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(21)

def macv_158_signal_vel_63d(close: pd.Series) -> pd.Series:
    """macv_158_signal_vel_63d"""
    return (_ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(63)

def macv_159_signal_vel_126d(close: pd.Series) -> pd.Series:
    """macv_159_signal_vel_126d"""
    return (_ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(126)

def macv_160_signal_vel_252d(close: pd.Series) -> pd.Series:
    """macv_160_signal_vel_252d"""
    return (_ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(252)

def macv_161_hist_vel_5d(close: pd.Series) -> pd.Series:
    """macv_161_hist_vel_5d"""
    return ((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(5)

def macv_162_hist_vel_21d(close: pd.Series) -> pd.Series:
    """macv_162_hist_vel_21d"""
    return ((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(21)

def macv_163_hist_vel_63d(close: pd.Series) -> pd.Series:
    """macv_163_hist_vel_63d"""
    return ((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(63)

def macv_164_hist_vel_126d(close: pd.Series) -> pd.Series:
    """macv_164_hist_vel_126d"""
    return ((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(126)

def macv_165_hist_vel_252d(close: pd.Series) -> pd.Series:
    """macv_165_hist_vel_252d"""
    return ((_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)).diff(252)

def macv_166_macd_rat_vel_5d(close: pd.Series) -> pd.Series:
    """macv_166_macd_rat_vel_5d"""
    return (_safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)).diff(5)

def macv_167_macd_rat_vel_21d(close: pd.Series) -> pd.Series:
    """macv_167_macd_rat_vel_21d"""
    return (_safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)).diff(21)

def macv_168_macd_rat_vel_63d(close: pd.Series) -> pd.Series:
    """macv_168_macd_rat_vel_63d"""
    return (_safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)).diff(63)

def macv_169_macd_rat_vel_126d(close: pd.Series) -> pd.Series:
    """macv_169_macd_rat_vel_126d"""
    return (_safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)).diff(126)

def macv_170_macd_rat_vel_252d(close: pd.Series) -> pd.Series:
    """macv_170_macd_rat_vel_252d"""
    return (_safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)).diff(252)

def macv_171_macd_z_vel_5d(close: pd.Series) -> pd.Series:
    """macv_171_macd_z_vel_5d"""
    return (_zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)).diff(5)

def macv_172_macd_z_vel_21d(close: pd.Series) -> pd.Series:
    """macv_172_macd_z_vel_21d"""
    return (_zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)).diff(21)

def macv_173_macd_z_vel_63d(close: pd.Series) -> pd.Series:
    """macv_173_macd_z_vel_63d"""
    return (_zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)).diff(63)

def macv_174_macd_z_vel_126d(close: pd.Series) -> pd.Series:
    """macv_174_macd_z_vel_126d"""
    return (_zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)).diff(126)

def macv_175_macd_z_vel_252d(close: pd.Series) -> pd.Series:
    """macv_175_macd_z_vel_252d"""
    return (_zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V76_REGISTRY_VEL = {
    "macv_151_macd_vel_5d": {"inputs": ["close"], "func": macv_151_macd_vel_5d},
    "macv_152_macd_vel_21d": {"inputs": ["close"], "func": macv_152_macd_vel_21d},
    "macv_153_macd_vel_63d": {"inputs": ["close"], "func": macv_153_macd_vel_63d},
    "macv_154_macd_vel_126d": {"inputs": ["close"], "func": macv_154_macd_vel_126d},
    "macv_155_macd_vel_252d": {"inputs": ["close"], "func": macv_155_macd_vel_252d},
    "macv_156_signal_vel_5d": {"inputs": ["close"], "func": macv_156_signal_vel_5d},
    "macv_157_signal_vel_21d": {"inputs": ["close"], "func": macv_157_signal_vel_21d},
    "macv_158_signal_vel_63d": {"inputs": ["close"], "func": macv_158_signal_vel_63d},
    "macv_159_signal_vel_126d": {"inputs": ["close"], "func": macv_159_signal_vel_126d},
    "macv_160_signal_vel_252d": {"inputs": ["close"], "func": macv_160_signal_vel_252d},
    "macv_161_hist_vel_5d": {"inputs": ["close"], "func": macv_161_hist_vel_5d},
    "macv_162_hist_vel_21d": {"inputs": ["close"], "func": macv_162_hist_vel_21d},
    "macv_163_hist_vel_63d": {"inputs": ["close"], "func": macv_163_hist_vel_63d},
    "macv_164_hist_vel_126d": {"inputs": ["close"], "func": macv_164_hist_vel_126d},
    "macv_165_hist_vel_252d": {"inputs": ["close"], "func": macv_165_hist_vel_252d},
    "macv_166_macd_rat_vel_5d": {"inputs": ["close"], "func": macv_166_macd_rat_vel_5d},
    "macv_167_macd_rat_vel_21d": {"inputs": ["close"], "func": macv_167_macd_rat_vel_21d},
    "macv_168_macd_rat_vel_63d": {"inputs": ["close"], "func": macv_168_macd_rat_vel_63d},
    "macv_169_macd_rat_vel_126d": {"inputs": ["close"], "func": macv_169_macd_rat_vel_126d},
    "macv_170_macd_rat_vel_252d": {"inputs": ["close"], "func": macv_170_macd_rat_vel_252d},
    "macv_171_macd_z_vel_5d": {"inputs": ["close"], "func": macv_171_macd_z_vel_5d},
    "macv_172_macd_z_vel_21d": {"inputs": ["close"], "func": macv_172_macd_z_vel_21d},
    "macv_173_macd_z_vel_63d": {"inputs": ["close"], "func": macv_173_macd_z_vel_63d},
    "macv_174_macd_z_vel_126d": {"inputs": ["close"], "func": macv_174_macd_z_vel_126d},
    "macv_175_macd_z_vel_252d": {"inputs": ["close"], "func": macv_175_macd_z_vel_252d},
}
