"""
81_adxd_dynamics — 3rd Derivatives (Acceleration)
Domain: adxd_dynamics
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

def adxd_176_tr_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_176_tr_accel_5d"""
    return (_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]).diff(5).diff(21)

def adxd_177_tr_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_177_tr_accel_21d"""
    return (_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]).diff(21).diff(21)

def adxd_178_tr_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_178_tr_accel_63d"""
    return (_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]).diff(63).diff(21)

def adxd_179_tr_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_179_tr_accel_126d"""
    return (_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]).diff(126).diff(21)

def adxd_180_tr_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_180_tr_accel_252d"""
    return (_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]).diff(252).diff(21)

def adxd_181_pdm_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_181_pdm_accel_5d"""
    return ((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)).diff(5).diff(21)

def adxd_182_pdm_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_182_pdm_accel_21d"""
    return ((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)).diff(21).diff(21)

def adxd_183_pdm_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_183_pdm_accel_63d"""
    return ((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)).diff(63).diff(21)

def adxd_184_pdm_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_184_pdm_accel_126d"""
    return ((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)).diff(126).diff(21)

def adxd_185_pdm_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_185_pdm_accel_252d"""
    return ((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)).diff(252).diff(21)

def adxd_186_mdm_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_186_mdm_accel_5d"""
    return ((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)).diff(5).diff(21)

def adxd_187_mdm_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_187_mdm_accel_21d"""
    return ((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)).diff(21).diff(21)

def adxd_188_mdm_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_188_mdm_accel_63d"""
    return ((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)).diff(63).diff(21)

def adxd_189_mdm_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_189_mdm_accel_126d"""
    return ((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)).diff(126).diff(21)

def adxd_190_mdm_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_190_mdm_accel_252d"""
    return ((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)).diff(252).diff(21)

def adxd_191_pdi_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_191_pdi_accel_5d"""
    return (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(5).diff(21)

def adxd_192_pdi_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_192_pdi_accel_21d"""
    return (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(21).diff(21)

def adxd_193_pdi_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_193_pdi_accel_63d"""
    return (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(63).diff(21)

def adxd_194_pdi_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_194_pdi_accel_126d"""
    return (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(126).diff(21)

def adxd_195_pdi_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_195_pdi_accel_252d"""
    return (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(252).diff(21)

def adxd_196_mdi_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_196_mdi_accel_5d"""
    return (100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(5).diff(21)

def adxd_197_mdi_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_197_mdi_accel_21d"""
    return (100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(21).diff(21)

def adxd_198_mdi_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_198_mdi_accel_63d"""
    return (100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(63).diff(21)

def adxd_199_mdi_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_199_mdi_accel_126d"""
    return (100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(126).diff(21)

def adxd_200_mdi_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_200_mdi_accel_252d"""
    return (100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V81_REGISTRY_ACCEL = {
    "adxd_176_tr_accel_5d": {"inputs": ["high", "low", "close"], "func": adxd_176_tr_accel_5d},
    "adxd_177_tr_accel_21d": {"inputs": ["high", "low", "close"], "func": adxd_177_tr_accel_21d},
    "adxd_178_tr_accel_63d": {"inputs": ["high", "low", "close"], "func": adxd_178_tr_accel_63d},
    "adxd_179_tr_accel_126d": {"inputs": ["high", "low", "close"], "func": adxd_179_tr_accel_126d},
    "adxd_180_tr_accel_252d": {"inputs": ["high", "low", "close"], "func": adxd_180_tr_accel_252d},
    "adxd_181_pdm_accel_5d": {"inputs": ["high", "low", "close"], "func": adxd_181_pdm_accel_5d},
    "adxd_182_pdm_accel_21d": {"inputs": ["high", "low", "close"], "func": adxd_182_pdm_accel_21d},
    "adxd_183_pdm_accel_63d": {"inputs": ["high", "low", "close"], "func": adxd_183_pdm_accel_63d},
    "adxd_184_pdm_accel_126d": {"inputs": ["high", "low", "close"], "func": adxd_184_pdm_accel_126d},
    "adxd_185_pdm_accel_252d": {"inputs": ["high", "low", "close"], "func": adxd_185_pdm_accel_252d},
    "adxd_186_mdm_accel_5d": {"inputs": ["high", "low", "close"], "func": adxd_186_mdm_accel_5d},
    "adxd_187_mdm_accel_21d": {"inputs": ["high", "low", "close"], "func": adxd_187_mdm_accel_21d},
    "adxd_188_mdm_accel_63d": {"inputs": ["high", "low", "close"], "func": adxd_188_mdm_accel_63d},
    "adxd_189_mdm_accel_126d": {"inputs": ["high", "low", "close"], "func": adxd_189_mdm_accel_126d},
    "adxd_190_mdm_accel_252d": {"inputs": ["high", "low", "close"], "func": adxd_190_mdm_accel_252d},
    "adxd_191_pdi_accel_5d": {"inputs": ["high", "low", "close"], "func": adxd_191_pdi_accel_5d},
    "adxd_192_pdi_accel_21d": {"inputs": ["high", "low", "close"], "func": adxd_192_pdi_accel_21d},
    "adxd_193_pdi_accel_63d": {"inputs": ["high", "low", "close"], "func": adxd_193_pdi_accel_63d},
    "adxd_194_pdi_accel_126d": {"inputs": ["high", "low", "close"], "func": adxd_194_pdi_accel_126d},
    "adxd_195_pdi_accel_252d": {"inputs": ["high", "low", "close"], "func": adxd_195_pdi_accel_252d},
    "adxd_196_mdi_accel_5d": {"inputs": ["high", "low", "close"], "func": adxd_196_mdi_accel_5d},
    "adxd_197_mdi_accel_21d": {"inputs": ["high", "low", "close"], "func": adxd_197_mdi_accel_21d},
    "adxd_198_mdi_accel_63d": {"inputs": ["high", "low", "close"], "func": adxd_198_mdi_accel_63d},
    "adxd_199_mdi_accel_126d": {"inputs": ["high", "low", "close"], "func": adxd_199_mdi_accel_126d},
    "adxd_200_mdi_accel_252d": {"inputs": ["high", "low", "close"], "func": adxd_200_mdi_accel_252d},
}
