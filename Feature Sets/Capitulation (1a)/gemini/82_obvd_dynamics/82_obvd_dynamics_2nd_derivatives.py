"""
82_obvd_dynamics — 2nd Derivatives (Velocity)
Domain: obvd_dynamics
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

def obvd_151_obv_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_151_obv_vel_5d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum()).diff(5)

def obvd_152_obv_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_152_obv_vel_21d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum()).diff(21)

def obvd_153_obv_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_153_obv_vel_63d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum()).diff(63)

def obvd_154_obv_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_154_obv_vel_126d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum()).diff(126)

def obvd_155_obv_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_155_obv_vel_252d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum()).diff(252)

def obvd_156_obv_sma_rat_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_156_obv_sma_rat_vel_5d"""
    return (_safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))).diff(5)

def obvd_157_obv_sma_rat_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_157_obv_sma_rat_vel_21d"""
    return (_safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))).diff(21)

def obvd_158_obv_sma_rat_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_158_obv_sma_rat_vel_63d"""
    return (_safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))).diff(63)

def obvd_159_obv_sma_rat_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_159_obv_sma_rat_vel_126d"""
    return (_safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))).diff(126)

def obvd_160_obv_sma_rat_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_160_obv_sma_rat_vel_252d"""
    return (_safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))).diff(252)

def obvd_161_obv_z_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_161_obv_z_vel_5d"""
    return (_zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)).diff(5)

def obvd_162_obv_z_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_162_obv_z_vel_21d"""
    return (_zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)).diff(21)

def obvd_163_obv_z_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_163_obv_z_vel_63d"""
    return (_zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)).diff(63)

def obvd_164_obv_z_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_164_obv_z_vel_126d"""
    return (_zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)).diff(126)

def obvd_165_obv_z_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_165_obv_z_vel_252d"""
    return (_zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)).diff(252)

def obvd_166_obv_slope_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_166_obv_slope_vel_5d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)).diff(5)

def obvd_167_obv_slope_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_167_obv_slope_vel_21d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)).diff(21)

def obvd_168_obv_slope_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_168_obv_slope_vel_63d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)).diff(63)

def obvd_169_obv_slope_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_169_obv_slope_vel_126d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)).diff(126)

def obvd_170_obv_slope_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_170_obv_slope_vel_252d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)).diff(252)

def obvd_171_obv_vol_rat_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_171_obv_vol_rat_vel_5d"""
    return (_safe_div(volume, _rolling_mean(volume, 20))).diff(5)

def obvd_172_obv_vol_rat_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_172_obv_vol_rat_vel_21d"""
    return (_safe_div(volume, _rolling_mean(volume, 20))).diff(21)

def obvd_173_obv_vol_rat_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_173_obv_vol_rat_vel_63d"""
    return (_safe_div(volume, _rolling_mean(volume, 20))).diff(63)

def obvd_174_obv_vol_rat_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_174_obv_vol_rat_vel_126d"""
    return (_safe_div(volume, _rolling_mean(volume, 20))).diff(126)

def obvd_175_obv_vol_rat_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_175_obv_vol_rat_vel_252d"""
    return (_safe_div(volume, _rolling_mean(volume, 20))).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V82_REGISTRY_VEL = {
    "obvd_151_obv_vel_5d": {"inputs": ["close", "volume"], "func": obvd_151_obv_vel_5d},
    "obvd_152_obv_vel_21d": {"inputs": ["close", "volume"], "func": obvd_152_obv_vel_21d},
    "obvd_153_obv_vel_63d": {"inputs": ["close", "volume"], "func": obvd_153_obv_vel_63d},
    "obvd_154_obv_vel_126d": {"inputs": ["close", "volume"], "func": obvd_154_obv_vel_126d},
    "obvd_155_obv_vel_252d": {"inputs": ["close", "volume"], "func": obvd_155_obv_vel_252d},
    "obvd_156_obv_sma_rat_vel_5d": {"inputs": ["close", "volume"], "func": obvd_156_obv_sma_rat_vel_5d},
    "obvd_157_obv_sma_rat_vel_21d": {"inputs": ["close", "volume"], "func": obvd_157_obv_sma_rat_vel_21d},
    "obvd_158_obv_sma_rat_vel_63d": {"inputs": ["close", "volume"], "func": obvd_158_obv_sma_rat_vel_63d},
    "obvd_159_obv_sma_rat_vel_126d": {"inputs": ["close", "volume"], "func": obvd_159_obv_sma_rat_vel_126d},
    "obvd_160_obv_sma_rat_vel_252d": {"inputs": ["close", "volume"], "func": obvd_160_obv_sma_rat_vel_252d},
    "obvd_161_obv_z_vel_5d": {"inputs": ["close", "volume"], "func": obvd_161_obv_z_vel_5d},
    "obvd_162_obv_z_vel_21d": {"inputs": ["close", "volume"], "func": obvd_162_obv_z_vel_21d},
    "obvd_163_obv_z_vel_63d": {"inputs": ["close", "volume"], "func": obvd_163_obv_z_vel_63d},
    "obvd_164_obv_z_vel_126d": {"inputs": ["close", "volume"], "func": obvd_164_obv_z_vel_126d},
    "obvd_165_obv_z_vel_252d": {"inputs": ["close", "volume"], "func": obvd_165_obv_z_vel_252d},
    "obvd_166_obv_slope_vel_5d": {"inputs": ["close", "volume"], "func": obvd_166_obv_slope_vel_5d},
    "obvd_167_obv_slope_vel_21d": {"inputs": ["close", "volume"], "func": obvd_167_obv_slope_vel_21d},
    "obvd_168_obv_slope_vel_63d": {"inputs": ["close", "volume"], "func": obvd_168_obv_slope_vel_63d},
    "obvd_169_obv_slope_vel_126d": {"inputs": ["close", "volume"], "func": obvd_169_obv_slope_vel_126d},
    "obvd_170_obv_slope_vel_252d": {"inputs": ["close", "volume"], "func": obvd_170_obv_slope_vel_252d},
    "obvd_171_obv_vol_rat_vel_5d": {"inputs": ["close", "volume"], "func": obvd_171_obv_vol_rat_vel_5d},
    "obvd_172_obv_vol_rat_vel_21d": {"inputs": ["close", "volume"], "func": obvd_172_obv_vol_rat_vel_21d},
    "obvd_173_obv_vol_rat_vel_63d": {"inputs": ["close", "volume"], "func": obvd_173_obv_vol_rat_vel_63d},
    "obvd_174_obv_vol_rat_vel_126d": {"inputs": ["close", "volume"], "func": obvd_174_obv_vol_rat_vel_126d},
    "obvd_175_obv_vol_rat_vel_252d": {"inputs": ["close", "volume"], "func": obvd_175_obv_vol_rat_vel_252d},
}
