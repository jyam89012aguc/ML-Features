"""
75_rsi_dynamics — 3rd Derivatives (Acceleration)
Domain: rsi_dynamics
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

def rsid_176_rsi_14_accel_5d(close: pd.Series) -> pd.Series:
    """rsid_176_rsi_14_accel_5d"""
    return (_rsi(close, 14)).diff(5).diff(21)

def rsid_177_rsi_14_accel_21d(close: pd.Series) -> pd.Series:
    """rsid_177_rsi_14_accel_21d"""
    return (_rsi(close, 14)).diff(21).diff(21)

def rsid_178_rsi_14_accel_63d(close: pd.Series) -> pd.Series:
    """rsid_178_rsi_14_accel_63d"""
    return (_rsi(close, 14)).diff(63).diff(21)

def rsid_179_rsi_14_accel_126d(close: pd.Series) -> pd.Series:
    """rsid_179_rsi_14_accel_126d"""
    return (_rsi(close, 14)).diff(126).diff(21)

def rsid_180_rsi_14_accel_252d(close: pd.Series) -> pd.Series:
    """rsid_180_rsi_14_accel_252d"""
    return (_rsi(close, 14)).diff(252).diff(21)

def rsid_181_rsi_5_accel_5d(close: pd.Series) -> pd.Series:
    """rsid_181_rsi_5_accel_5d"""
    return (_rsi(close, 5)).diff(5).diff(21)

def rsid_182_rsi_5_accel_21d(close: pd.Series) -> pd.Series:
    """rsid_182_rsi_5_accel_21d"""
    return (_rsi(close, 5)).diff(21).diff(21)

def rsid_183_rsi_5_accel_63d(close: pd.Series) -> pd.Series:
    """rsid_183_rsi_5_accel_63d"""
    return (_rsi(close, 5)).diff(63).diff(21)

def rsid_184_rsi_5_accel_126d(close: pd.Series) -> pd.Series:
    """rsid_184_rsi_5_accel_126d"""
    return (_rsi(close, 5)).diff(126).diff(21)

def rsid_185_rsi_5_accel_252d(close: pd.Series) -> pd.Series:
    """rsid_185_rsi_5_accel_252d"""
    return (_rsi(close, 5)).diff(252).diff(21)

def rsid_186_rsi_21_accel_5d(close: pd.Series) -> pd.Series:
    """rsid_186_rsi_21_accel_5d"""
    return (_rsi(close, 21)).diff(5).diff(21)

def rsid_187_rsi_21_accel_21d(close: pd.Series) -> pd.Series:
    """rsid_187_rsi_21_accel_21d"""
    return (_rsi(close, 21)).diff(21).diff(21)

def rsid_188_rsi_21_accel_63d(close: pd.Series) -> pd.Series:
    """rsid_188_rsi_21_accel_63d"""
    return (_rsi(close, 21)).diff(63).diff(21)

def rsid_189_rsi_21_accel_126d(close: pd.Series) -> pd.Series:
    """rsid_189_rsi_21_accel_126d"""
    return (_rsi(close, 21)).diff(126).diff(21)

def rsid_190_rsi_21_accel_252d(close: pd.Series) -> pd.Series:
    """rsid_190_rsi_21_accel_252d"""
    return (_rsi(close, 21)).diff(252).diff(21)

def rsid_191_rsi_dist_accel_5d(close: pd.Series) -> pd.Series:
    """rsid_191_rsi_dist_accel_5d"""
    return (_rsi(close, 14) - 50).diff(5).diff(21)

def rsid_192_rsi_dist_accel_21d(close: pd.Series) -> pd.Series:
    """rsid_192_rsi_dist_accel_21d"""
    return (_rsi(close, 14) - 50).diff(21).diff(21)

def rsid_193_rsi_dist_accel_63d(close: pd.Series) -> pd.Series:
    """rsid_193_rsi_dist_accel_63d"""
    return (_rsi(close, 14) - 50).diff(63).diff(21)

def rsid_194_rsi_dist_accel_126d(close: pd.Series) -> pd.Series:
    """rsid_194_rsi_dist_accel_126d"""
    return (_rsi(close, 14) - 50).diff(126).diff(21)

def rsid_195_rsi_dist_accel_252d(close: pd.Series) -> pd.Series:
    """rsid_195_rsi_dist_accel_252d"""
    return (_rsi(close, 14) - 50).diff(252).diff(21)

def rsid_196_rsi_ob_accel_5d(close: pd.Series) -> pd.Series:
    """rsid_196_rsi_ob_accel_5d"""
    return (_rsi(close, 14) - 70).diff(5).diff(21)

def rsid_197_rsi_ob_accel_21d(close: pd.Series) -> pd.Series:
    """rsid_197_rsi_ob_accel_21d"""
    return (_rsi(close, 14) - 70).diff(21).diff(21)

def rsid_198_rsi_ob_accel_63d(close: pd.Series) -> pd.Series:
    """rsid_198_rsi_ob_accel_63d"""
    return (_rsi(close, 14) - 70).diff(63).diff(21)

def rsid_199_rsi_ob_accel_126d(close: pd.Series) -> pd.Series:
    """rsid_199_rsi_ob_accel_126d"""
    return (_rsi(close, 14) - 70).diff(126).diff(21)

def rsid_200_rsi_ob_accel_252d(close: pd.Series) -> pd.Series:
    """rsid_200_rsi_ob_accel_252d"""
    return (_rsi(close, 14) - 70).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V75_REGISTRY_ACCEL = {
    "rsid_176_rsi_14_accel_5d": {"inputs": ["close"], "func": rsid_176_rsi_14_accel_5d},
    "rsid_177_rsi_14_accel_21d": {"inputs": ["close"], "func": rsid_177_rsi_14_accel_21d},
    "rsid_178_rsi_14_accel_63d": {"inputs": ["close"], "func": rsid_178_rsi_14_accel_63d},
    "rsid_179_rsi_14_accel_126d": {"inputs": ["close"], "func": rsid_179_rsi_14_accel_126d},
    "rsid_180_rsi_14_accel_252d": {"inputs": ["close"], "func": rsid_180_rsi_14_accel_252d},
    "rsid_181_rsi_5_accel_5d": {"inputs": ["close"], "func": rsid_181_rsi_5_accel_5d},
    "rsid_182_rsi_5_accel_21d": {"inputs": ["close"], "func": rsid_182_rsi_5_accel_21d},
    "rsid_183_rsi_5_accel_63d": {"inputs": ["close"], "func": rsid_183_rsi_5_accel_63d},
    "rsid_184_rsi_5_accel_126d": {"inputs": ["close"], "func": rsid_184_rsi_5_accel_126d},
    "rsid_185_rsi_5_accel_252d": {"inputs": ["close"], "func": rsid_185_rsi_5_accel_252d},
    "rsid_186_rsi_21_accel_5d": {"inputs": ["close"], "func": rsid_186_rsi_21_accel_5d},
    "rsid_187_rsi_21_accel_21d": {"inputs": ["close"], "func": rsid_187_rsi_21_accel_21d},
    "rsid_188_rsi_21_accel_63d": {"inputs": ["close"], "func": rsid_188_rsi_21_accel_63d},
    "rsid_189_rsi_21_accel_126d": {"inputs": ["close"], "func": rsid_189_rsi_21_accel_126d},
    "rsid_190_rsi_21_accel_252d": {"inputs": ["close"], "func": rsid_190_rsi_21_accel_252d},
    "rsid_191_rsi_dist_accel_5d": {"inputs": ["close"], "func": rsid_191_rsi_dist_accel_5d},
    "rsid_192_rsi_dist_accel_21d": {"inputs": ["close"], "func": rsid_192_rsi_dist_accel_21d},
    "rsid_193_rsi_dist_accel_63d": {"inputs": ["close"], "func": rsid_193_rsi_dist_accel_63d},
    "rsid_194_rsi_dist_accel_126d": {"inputs": ["close"], "func": rsid_194_rsi_dist_accel_126d},
    "rsid_195_rsi_dist_accel_252d": {"inputs": ["close"], "func": rsid_195_rsi_dist_accel_252d},
    "rsid_196_rsi_ob_accel_5d": {"inputs": ["close"], "func": rsid_196_rsi_ob_accel_5d},
    "rsid_197_rsi_ob_accel_21d": {"inputs": ["close"], "func": rsid_197_rsi_ob_accel_21d},
    "rsid_198_rsi_ob_accel_63d": {"inputs": ["close"], "func": rsid_198_rsi_ob_accel_63d},
    "rsid_199_rsi_ob_accel_126d": {"inputs": ["close"], "func": rsid_199_rsi_ob_accel_126d},
    "rsid_200_rsi_ob_accel_252d": {"inputs": ["close"], "func": rsid_200_rsi_ob_accel_252d},
}
