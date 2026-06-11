"""
81_adxd_dynamics — 2nd Derivatives (Velocity)
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

def adxd_151_tr_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_151_tr_vel_5d"""
    return (_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]).diff(5)

def adxd_152_tr_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_152_tr_vel_21d"""
    return (_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]).diff(21)

def adxd_153_tr_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_153_tr_vel_63d"""
    return (_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]).diff(63)

def adxd_154_tr_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_154_tr_vel_126d"""
    return (_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]).diff(126)

def adxd_155_tr_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_155_tr_vel_252d"""
    return (_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]).diff(252)

def adxd_156_pdm_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_156_pdm_vel_5d"""
    return ((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)).diff(5)

def adxd_157_pdm_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_157_pdm_vel_21d"""
    return ((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)).diff(21)

def adxd_158_pdm_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_158_pdm_vel_63d"""
    return ((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)).diff(63)

def adxd_159_pdm_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_159_pdm_vel_126d"""
    return ((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)).diff(126)

def adxd_160_pdm_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_160_pdm_vel_252d"""
    return ((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)).diff(252)

def adxd_161_mdm_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_161_mdm_vel_5d"""
    return ((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)).diff(5)

def adxd_162_mdm_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_162_mdm_vel_21d"""
    return ((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)).diff(21)

def adxd_163_mdm_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_163_mdm_vel_63d"""
    return ((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)).diff(63)

def adxd_164_mdm_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_164_mdm_vel_126d"""
    return ((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)).diff(126)

def adxd_165_mdm_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_165_mdm_vel_252d"""
    return ((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)).diff(252)

def adxd_166_pdi_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_166_pdi_vel_5d"""
    return (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(5)

def adxd_167_pdi_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_167_pdi_vel_21d"""
    return (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(21)

def adxd_168_pdi_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_168_pdi_vel_63d"""
    return (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(63)

def adxd_169_pdi_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_169_pdi_vel_126d"""
    return (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(126)

def adxd_170_pdi_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_170_pdi_vel_252d"""
    return (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(252)

def adxd_171_mdi_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_171_mdi_vel_5d"""
    return (100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(5)

def adxd_172_mdi_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_172_mdi_vel_21d"""
    return (100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(21)

def adxd_173_mdi_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_173_mdi_vel_63d"""
    return (100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(63)

def adxd_174_mdi_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_174_mdi_vel_126d"""
    return (100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(126)

def adxd_175_mdi_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_175_mdi_vel_252d"""
    return (100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V81_REGISTRY_VEL = {
    "adxd_151_tr_vel_5d": {"inputs": ["high", "low", "close"], "func": adxd_151_tr_vel_5d},
    "adxd_152_tr_vel_21d": {"inputs": ["high", "low", "close"], "func": adxd_152_tr_vel_21d},
    "adxd_153_tr_vel_63d": {"inputs": ["high", "low", "close"], "func": adxd_153_tr_vel_63d},
    "adxd_154_tr_vel_126d": {"inputs": ["high", "low", "close"], "func": adxd_154_tr_vel_126d},
    "adxd_155_tr_vel_252d": {"inputs": ["high", "low", "close"], "func": adxd_155_tr_vel_252d},
    "adxd_156_pdm_vel_5d": {"inputs": ["high", "low", "close"], "func": adxd_156_pdm_vel_5d},
    "adxd_157_pdm_vel_21d": {"inputs": ["high", "low", "close"], "func": adxd_157_pdm_vel_21d},
    "adxd_158_pdm_vel_63d": {"inputs": ["high", "low", "close"], "func": adxd_158_pdm_vel_63d},
    "adxd_159_pdm_vel_126d": {"inputs": ["high", "low", "close"], "func": adxd_159_pdm_vel_126d},
    "adxd_160_pdm_vel_252d": {"inputs": ["high", "low", "close"], "func": adxd_160_pdm_vel_252d},
    "adxd_161_mdm_vel_5d": {"inputs": ["high", "low", "close"], "func": adxd_161_mdm_vel_5d},
    "adxd_162_mdm_vel_21d": {"inputs": ["high", "low", "close"], "func": adxd_162_mdm_vel_21d},
    "adxd_163_mdm_vel_63d": {"inputs": ["high", "low", "close"], "func": adxd_163_mdm_vel_63d},
    "adxd_164_mdm_vel_126d": {"inputs": ["high", "low", "close"], "func": adxd_164_mdm_vel_126d},
    "adxd_165_mdm_vel_252d": {"inputs": ["high", "low", "close"], "func": adxd_165_mdm_vel_252d},
    "adxd_166_pdi_vel_5d": {"inputs": ["high", "low", "close"], "func": adxd_166_pdi_vel_5d},
    "adxd_167_pdi_vel_21d": {"inputs": ["high", "low", "close"], "func": adxd_167_pdi_vel_21d},
    "adxd_168_pdi_vel_63d": {"inputs": ["high", "low", "close"], "func": adxd_168_pdi_vel_63d},
    "adxd_169_pdi_vel_126d": {"inputs": ["high", "low", "close"], "func": adxd_169_pdi_vel_126d},
    "adxd_170_pdi_vel_252d": {"inputs": ["high", "low", "close"], "func": adxd_170_pdi_vel_252d},
    "adxd_171_mdi_vel_5d": {"inputs": ["high", "low", "close"], "func": adxd_171_mdi_vel_5d},
    "adxd_172_mdi_vel_21d": {"inputs": ["high", "low", "close"], "func": adxd_172_mdi_vel_21d},
    "adxd_173_mdi_vel_63d": {"inputs": ["high", "low", "close"], "func": adxd_173_mdi_vel_63d},
    "adxd_174_mdi_vel_126d": {"inputs": ["high", "low", "close"], "func": adxd_174_mdi_vel_126d},
    "adxd_175_mdi_vel_252d": {"inputs": ["high", "low", "close"], "func": adxd_175_mdi_vel_252d},
}
