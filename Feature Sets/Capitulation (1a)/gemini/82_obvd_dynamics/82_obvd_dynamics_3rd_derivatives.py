"""
82_obvd_dynamics — 3rd Derivatives (Acceleration)
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

def obvd_176_obv_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_176_obv_accel_5d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum()).diff(5).diff(21)

def obvd_177_obv_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_177_obv_accel_21d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum()).diff(21).diff(21)

def obvd_178_obv_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_178_obv_accel_63d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum()).diff(63).diff(21)

def obvd_179_obv_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_179_obv_accel_126d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum()).diff(126).diff(21)

def obvd_180_obv_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_180_obv_accel_252d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum()).diff(252).diff(21)

def obvd_181_obv_sma_rat_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_181_obv_sma_rat_accel_5d"""
    return (_safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))).diff(5).diff(21)

def obvd_182_obv_sma_rat_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_182_obv_sma_rat_accel_21d"""
    return (_safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))).diff(21).diff(21)

def obvd_183_obv_sma_rat_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_183_obv_sma_rat_accel_63d"""
    return (_safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))).diff(63).diff(21)

def obvd_184_obv_sma_rat_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_184_obv_sma_rat_accel_126d"""
    return (_safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))).diff(126).diff(21)

def obvd_185_obv_sma_rat_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_185_obv_sma_rat_accel_252d"""
    return (_safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))).diff(252).diff(21)

def obvd_186_obv_z_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_186_obv_z_accel_5d"""
    return (_zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)).diff(5).diff(21)

def obvd_187_obv_z_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_187_obv_z_accel_21d"""
    return (_zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)).diff(21).diff(21)

def obvd_188_obv_z_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_188_obv_z_accel_63d"""
    return (_zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)).diff(63).diff(21)

def obvd_189_obv_z_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_189_obv_z_accel_126d"""
    return (_zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)).diff(126).diff(21)

def obvd_190_obv_z_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_190_obv_z_accel_252d"""
    return (_zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)).diff(252).diff(21)

def obvd_191_obv_slope_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_191_obv_slope_accel_5d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)).diff(5).diff(21)

def obvd_192_obv_slope_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_192_obv_slope_accel_21d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)).diff(21).diff(21)

def obvd_193_obv_slope_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_193_obv_slope_accel_63d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)).diff(63).diff(21)

def obvd_194_obv_slope_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_194_obv_slope_accel_126d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)).diff(126).diff(21)

def obvd_195_obv_slope_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_195_obv_slope_accel_252d"""
    return ((volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)).diff(252).diff(21)

def obvd_196_obv_vol_rat_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_196_obv_vol_rat_accel_5d"""
    return (_safe_div(volume, _rolling_mean(volume, 20))).diff(5).diff(21)

def obvd_197_obv_vol_rat_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_197_obv_vol_rat_accel_21d"""
    return (_safe_div(volume, _rolling_mean(volume, 20))).diff(21).diff(21)

def obvd_198_obv_vol_rat_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_198_obv_vol_rat_accel_63d"""
    return (_safe_div(volume, _rolling_mean(volume, 20))).diff(63).diff(21)

def obvd_199_obv_vol_rat_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_199_obv_vol_rat_accel_126d"""
    return (_safe_div(volume, _rolling_mean(volume, 20))).diff(126).diff(21)

def obvd_200_obv_vol_rat_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_200_obv_vol_rat_accel_252d"""
    return (_safe_div(volume, _rolling_mean(volume, 20))).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V82_REGISTRY_ACCEL = {
    "obvd_176_obv_accel_5d": {"inputs": ["close", "volume"], "func": obvd_176_obv_accel_5d},
    "obvd_177_obv_accel_21d": {"inputs": ["close", "volume"], "func": obvd_177_obv_accel_21d},
    "obvd_178_obv_accel_63d": {"inputs": ["close", "volume"], "func": obvd_178_obv_accel_63d},
    "obvd_179_obv_accel_126d": {"inputs": ["close", "volume"], "func": obvd_179_obv_accel_126d},
    "obvd_180_obv_accel_252d": {"inputs": ["close", "volume"], "func": obvd_180_obv_accel_252d},
    "obvd_181_obv_sma_rat_accel_5d": {"inputs": ["close", "volume"], "func": obvd_181_obv_sma_rat_accel_5d},
    "obvd_182_obv_sma_rat_accel_21d": {"inputs": ["close", "volume"], "func": obvd_182_obv_sma_rat_accel_21d},
    "obvd_183_obv_sma_rat_accel_63d": {"inputs": ["close", "volume"], "func": obvd_183_obv_sma_rat_accel_63d},
    "obvd_184_obv_sma_rat_accel_126d": {"inputs": ["close", "volume"], "func": obvd_184_obv_sma_rat_accel_126d},
    "obvd_185_obv_sma_rat_accel_252d": {"inputs": ["close", "volume"], "func": obvd_185_obv_sma_rat_accel_252d},
    "obvd_186_obv_z_accel_5d": {"inputs": ["close", "volume"], "func": obvd_186_obv_z_accel_5d},
    "obvd_187_obv_z_accel_21d": {"inputs": ["close", "volume"], "func": obvd_187_obv_z_accel_21d},
    "obvd_188_obv_z_accel_63d": {"inputs": ["close", "volume"], "func": obvd_188_obv_z_accel_63d},
    "obvd_189_obv_z_accel_126d": {"inputs": ["close", "volume"], "func": obvd_189_obv_z_accel_126d},
    "obvd_190_obv_z_accel_252d": {"inputs": ["close", "volume"], "func": obvd_190_obv_z_accel_252d},
    "obvd_191_obv_slope_accel_5d": {"inputs": ["close", "volume"], "func": obvd_191_obv_slope_accel_5d},
    "obvd_192_obv_slope_accel_21d": {"inputs": ["close", "volume"], "func": obvd_192_obv_slope_accel_21d},
    "obvd_193_obv_slope_accel_63d": {"inputs": ["close", "volume"], "func": obvd_193_obv_slope_accel_63d},
    "obvd_194_obv_slope_accel_126d": {"inputs": ["close", "volume"], "func": obvd_194_obv_slope_accel_126d},
    "obvd_195_obv_slope_accel_252d": {"inputs": ["close", "volume"], "func": obvd_195_obv_slope_accel_252d},
    "obvd_196_obv_vol_rat_accel_5d": {"inputs": ["close", "volume"], "func": obvd_196_obv_vol_rat_accel_5d},
    "obvd_197_obv_vol_rat_accel_21d": {"inputs": ["close", "volume"], "func": obvd_197_obv_vol_rat_accel_21d},
    "obvd_198_obv_vol_rat_accel_63d": {"inputs": ["close", "volume"], "func": obvd_198_obv_vol_rat_accel_63d},
    "obvd_199_obv_vol_rat_accel_126d": {"inputs": ["close", "volume"], "func": obvd_199_obv_vol_rat_accel_126d},
    "obvd_200_obv_vol_rat_accel_252d": {"inputs": ["close", "volume"], "func": obvd_200_obv_vol_rat_accel_252d},
}
