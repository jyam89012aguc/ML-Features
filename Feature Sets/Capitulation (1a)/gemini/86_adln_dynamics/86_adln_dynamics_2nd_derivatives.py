"""
86_adln_dynamics — 2nd Derivatives (Velocity)
Domain: adln_dynamics
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

def adln_151_adl_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_151_adl_vel_5d"""
    return (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).diff(5)

def adln_152_adl_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_152_adl_vel_21d"""
    return (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).diff(21)

def adln_153_adl_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_153_adl_vel_63d"""
    return (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).diff(63)

def adln_154_adl_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_154_adl_vel_126d"""
    return (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).diff(126)

def adln_155_adl_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_155_adl_vel_252d"""
    return (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).diff(252)

def adln_156_adl_ps_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_156_adl_ps_vel_5d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()).diff(5)

def adln_157_adl_ps_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_157_adl_ps_vel_21d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()).diff(21)

def adln_158_adl_ps_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_158_adl_ps_vel_63d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()).diff(63)

def adln_159_adl_ps_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_159_adl_ps_vel_126d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()).diff(126)

def adln_160_adl_ps_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_160_adl_ps_vel_252d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()).diff(252)

def adln_161_chaikin_osc_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_161_chaikin_osc_vel_5d"""
    return (close.ewm(span=3).mean() - close.ewm(span=10).mean()).diff(5)

def adln_162_chaikin_osc_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_162_chaikin_osc_vel_21d"""
    return (close.ewm(span=3).mean() - close.ewm(span=10).mean()).diff(21)

def adln_163_chaikin_osc_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_163_chaikin_osc_vel_63d"""
    return (close.ewm(span=3).mean() - close.ewm(span=10).mean()).diff(63)

def adln_164_chaikin_osc_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_164_chaikin_osc_vel_126d"""
    return (close.ewm(span=3).mean() - close.ewm(span=10).mean()).diff(126)

def adln_165_chaikin_osc_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_165_chaikin_osc_vel_252d"""
    return (close.ewm(span=3).mean() - close.ewm(span=10).mean()).diff(252)

def adln_166_adl_roc_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_166_adl_roc_vel_5d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()).diff(5)

def adln_167_adl_roc_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_167_adl_roc_vel_21d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()).diff(21)

def adln_168_adl_roc_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_168_adl_roc_vel_63d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()).diff(63)

def adln_169_adl_roc_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_169_adl_roc_vel_126d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()).diff(126)

def adln_170_adl_roc_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_170_adl_roc_vel_252d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()).diff(252)

def adln_171_adl_mfi_vel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_171_adl_mfi_vel_5d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close).diff(5)

def adln_172_adl_mfi_vel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_172_adl_mfi_vel_21d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close).diff(21)

def adln_173_adl_mfi_vel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_173_adl_mfi_vel_63d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close).diff(63)

def adln_174_adl_mfi_vel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_174_adl_mfi_vel_126d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close).diff(126)

def adln_175_adl_mfi_vel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_175_adl_mfi_vel_252d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V86_REGISTRY_VEL = {
    "adln_151_adl_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_151_adl_vel_5d},
    "adln_152_adl_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_152_adl_vel_21d},
    "adln_153_adl_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_153_adl_vel_63d},
    "adln_154_adl_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_154_adl_vel_126d},
    "adln_155_adl_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_155_adl_vel_252d},
    "adln_156_adl_ps_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_156_adl_ps_vel_5d},
    "adln_157_adl_ps_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_157_adl_ps_vel_21d},
    "adln_158_adl_ps_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_158_adl_ps_vel_63d},
    "adln_159_adl_ps_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_159_adl_ps_vel_126d},
    "adln_160_adl_ps_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_160_adl_ps_vel_252d},
    "adln_161_chaikin_osc_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_161_chaikin_osc_vel_5d},
    "adln_162_chaikin_osc_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_162_chaikin_osc_vel_21d},
    "adln_163_chaikin_osc_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_163_chaikin_osc_vel_63d},
    "adln_164_chaikin_osc_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_164_chaikin_osc_vel_126d},
    "adln_165_chaikin_osc_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_165_chaikin_osc_vel_252d},
    "adln_166_adl_roc_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_166_adl_roc_vel_5d},
    "adln_167_adl_roc_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_167_adl_roc_vel_21d},
    "adln_168_adl_roc_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_168_adl_roc_vel_63d},
    "adln_169_adl_roc_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_169_adl_roc_vel_126d},
    "adln_170_adl_roc_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_170_adl_roc_vel_252d},
    "adln_171_adl_mfi_vel_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_171_adl_mfi_vel_5d},
    "adln_172_adl_mfi_vel_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_172_adl_mfi_vel_21d},
    "adln_173_adl_mfi_vel_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_173_adl_mfi_vel_63d},
    "adln_174_adl_mfi_vel_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_174_adl_mfi_vel_126d},
    "adln_175_adl_mfi_vel_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_175_adl_mfi_vel_252d},
}
