"""
77_bolp_dynamics — 3rd Derivatives (Acceleration)
Domain: bolp_dynamics
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

def bolp_176_bb_upper_accel_5d(close: pd.Series) -> pd.Series:
    """bolp_176_bb_upper_accel_5d"""
    return (_rolling_mean(close, 20) + 2 * _rolling_std(close, 20)).diff(5).diff(21)

def bolp_177_bb_upper_accel_21d(close: pd.Series) -> pd.Series:
    """bolp_177_bb_upper_accel_21d"""
    return (_rolling_mean(close, 20) + 2 * _rolling_std(close, 20)).diff(21).diff(21)

def bolp_178_bb_upper_accel_63d(close: pd.Series) -> pd.Series:
    """bolp_178_bb_upper_accel_63d"""
    return (_rolling_mean(close, 20) + 2 * _rolling_std(close, 20)).diff(63).diff(21)

def bolp_179_bb_upper_accel_126d(close: pd.Series) -> pd.Series:
    """bolp_179_bb_upper_accel_126d"""
    return (_rolling_mean(close, 20) + 2 * _rolling_std(close, 20)).diff(126).diff(21)

def bolp_180_bb_upper_accel_252d(close: pd.Series) -> pd.Series:
    """bolp_180_bb_upper_accel_252d"""
    return (_rolling_mean(close, 20) + 2 * _rolling_std(close, 20)).diff(252).diff(21)

def bolp_181_bb_lower_accel_5d(close: pd.Series) -> pd.Series:
    """bolp_181_bb_lower_accel_5d"""
    return (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)).diff(5).diff(21)

def bolp_182_bb_lower_accel_21d(close: pd.Series) -> pd.Series:
    """bolp_182_bb_lower_accel_21d"""
    return (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)).diff(21).diff(21)

def bolp_183_bb_lower_accel_63d(close: pd.Series) -> pd.Series:
    """bolp_183_bb_lower_accel_63d"""
    return (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)).diff(63).diff(21)

def bolp_184_bb_lower_accel_126d(close: pd.Series) -> pd.Series:
    """bolp_184_bb_lower_accel_126d"""
    return (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)).diff(126).diff(21)

def bolp_185_bb_lower_accel_252d(close: pd.Series) -> pd.Series:
    """bolp_185_bb_lower_accel_252d"""
    return (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)).diff(252).diff(21)

def bolp_186_bb_width_accel_5d(close: pd.Series) -> pd.Series:
    """bolp_186_bb_width_accel_5d"""
    return (_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))).diff(5).diff(21)

def bolp_187_bb_width_accel_21d(close: pd.Series) -> pd.Series:
    """bolp_187_bb_width_accel_21d"""
    return (_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))).diff(21).diff(21)

def bolp_188_bb_width_accel_63d(close: pd.Series) -> pd.Series:
    """bolp_188_bb_width_accel_63d"""
    return (_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))).diff(63).diff(21)

def bolp_189_bb_width_accel_126d(close: pd.Series) -> pd.Series:
    """bolp_189_bb_width_accel_126d"""
    return (_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))).diff(126).diff(21)

def bolp_190_bb_width_accel_252d(close: pd.Series) -> pd.Series:
    """bolp_190_bb_width_accel_252d"""
    return (_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))).diff(252).diff(21)

def bolp_191_bb_pctb_accel_5d(close: pd.Series) -> pd.Series:
    """bolp_191_bb_pctb_accel_5d"""
    return (_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))).diff(5).diff(21)

def bolp_192_bb_pctb_accel_21d(close: pd.Series) -> pd.Series:
    """bolp_192_bb_pctb_accel_21d"""
    return (_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))).diff(21).diff(21)

def bolp_193_bb_pctb_accel_63d(close: pd.Series) -> pd.Series:
    """bolp_193_bb_pctb_accel_63d"""
    return (_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))).diff(63).diff(21)

def bolp_194_bb_pctb_accel_126d(close: pd.Series) -> pd.Series:
    """bolp_194_bb_pctb_accel_126d"""
    return (_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))).diff(126).diff(21)

def bolp_195_bb_pctb_accel_252d(close: pd.Series) -> pd.Series:
    """bolp_195_bb_pctb_accel_252d"""
    return (_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))).diff(252).diff(21)

def bolp_196_bb_dist_u_accel_5d(close: pd.Series) -> pd.Series:
    """bolp_196_bb_dist_u_accel_5d"""
    return (_safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))).diff(5).diff(21)

def bolp_197_bb_dist_u_accel_21d(close: pd.Series) -> pd.Series:
    """bolp_197_bb_dist_u_accel_21d"""
    return (_safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))).diff(21).diff(21)

def bolp_198_bb_dist_u_accel_63d(close: pd.Series) -> pd.Series:
    """bolp_198_bb_dist_u_accel_63d"""
    return (_safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))).diff(63).diff(21)

def bolp_199_bb_dist_u_accel_126d(close: pd.Series) -> pd.Series:
    """bolp_199_bb_dist_u_accel_126d"""
    return (_safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))).diff(126).diff(21)

def bolp_200_bb_dist_u_accel_252d(close: pd.Series) -> pd.Series:
    """bolp_200_bb_dist_u_accel_252d"""
    return (_safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V77_REGISTRY_ACCEL = {
    "bolp_176_bb_upper_accel_5d": {"inputs": ["close"], "func": bolp_176_bb_upper_accel_5d},
    "bolp_177_bb_upper_accel_21d": {"inputs": ["close"], "func": bolp_177_bb_upper_accel_21d},
    "bolp_178_bb_upper_accel_63d": {"inputs": ["close"], "func": bolp_178_bb_upper_accel_63d},
    "bolp_179_bb_upper_accel_126d": {"inputs": ["close"], "func": bolp_179_bb_upper_accel_126d},
    "bolp_180_bb_upper_accel_252d": {"inputs": ["close"], "func": bolp_180_bb_upper_accel_252d},
    "bolp_181_bb_lower_accel_5d": {"inputs": ["close"], "func": bolp_181_bb_lower_accel_5d},
    "bolp_182_bb_lower_accel_21d": {"inputs": ["close"], "func": bolp_182_bb_lower_accel_21d},
    "bolp_183_bb_lower_accel_63d": {"inputs": ["close"], "func": bolp_183_bb_lower_accel_63d},
    "bolp_184_bb_lower_accel_126d": {"inputs": ["close"], "func": bolp_184_bb_lower_accel_126d},
    "bolp_185_bb_lower_accel_252d": {"inputs": ["close"], "func": bolp_185_bb_lower_accel_252d},
    "bolp_186_bb_width_accel_5d": {"inputs": ["close"], "func": bolp_186_bb_width_accel_5d},
    "bolp_187_bb_width_accel_21d": {"inputs": ["close"], "func": bolp_187_bb_width_accel_21d},
    "bolp_188_bb_width_accel_63d": {"inputs": ["close"], "func": bolp_188_bb_width_accel_63d},
    "bolp_189_bb_width_accel_126d": {"inputs": ["close"], "func": bolp_189_bb_width_accel_126d},
    "bolp_190_bb_width_accel_252d": {"inputs": ["close"], "func": bolp_190_bb_width_accel_252d},
    "bolp_191_bb_pctb_accel_5d": {"inputs": ["close"], "func": bolp_191_bb_pctb_accel_5d},
    "bolp_192_bb_pctb_accel_21d": {"inputs": ["close"], "func": bolp_192_bb_pctb_accel_21d},
    "bolp_193_bb_pctb_accel_63d": {"inputs": ["close"], "func": bolp_193_bb_pctb_accel_63d},
    "bolp_194_bb_pctb_accel_126d": {"inputs": ["close"], "func": bolp_194_bb_pctb_accel_126d},
    "bolp_195_bb_pctb_accel_252d": {"inputs": ["close"], "func": bolp_195_bb_pctb_accel_252d},
    "bolp_196_bb_dist_u_accel_5d": {"inputs": ["close"], "func": bolp_196_bb_dist_u_accel_5d},
    "bolp_197_bb_dist_u_accel_21d": {"inputs": ["close"], "func": bolp_197_bb_dist_u_accel_21d},
    "bolp_198_bb_dist_u_accel_63d": {"inputs": ["close"], "func": bolp_198_bb_dist_u_accel_63d},
    "bolp_199_bb_dist_u_accel_126d": {"inputs": ["close"], "func": bolp_199_bb_dist_u_accel_126d},
    "bolp_200_bb_dist_u_accel_252d": {"inputs": ["close"], "func": bolp_200_bb_dist_u_accel_252d},
}
