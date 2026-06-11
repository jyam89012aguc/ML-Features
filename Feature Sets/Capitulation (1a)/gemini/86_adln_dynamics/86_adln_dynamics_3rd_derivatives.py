"""
86_adln_dynamics — 3rd Derivatives (Acceleration)
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

def adln_176_adl_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_176_adl_accel_5d"""
    return (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).diff(5).diff(21)

def adln_177_adl_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_177_adl_accel_21d"""
    return (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).diff(21).diff(21)

def adln_178_adl_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_178_adl_accel_63d"""
    return (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).diff(63).diff(21)

def adln_179_adl_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_179_adl_accel_126d"""
    return (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).diff(126).diff(21)

def adln_180_adl_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_180_adl_accel_252d"""
    return (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).diff(252).diff(21)

def adln_181_adl_ps_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_181_adl_ps_accel_5d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()).diff(5).diff(21)

def adln_182_adl_ps_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_182_adl_ps_accel_21d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()).diff(21).diff(21)

def adln_183_adl_ps_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_183_adl_ps_accel_63d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()).diff(63).diff(21)

def adln_184_adl_ps_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_184_adl_ps_accel_126d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()).diff(126).diff(21)

def adln_185_adl_ps_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_185_adl_ps_accel_252d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()).diff(252).diff(21)

def adln_186_chaikin_osc_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_186_chaikin_osc_accel_5d"""
    return (close.ewm(span=3).mean() - close.ewm(span=10).mean()).diff(5).diff(21)

def adln_187_chaikin_osc_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_187_chaikin_osc_accel_21d"""
    return (close.ewm(span=3).mean() - close.ewm(span=10).mean()).diff(21).diff(21)

def adln_188_chaikin_osc_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_188_chaikin_osc_accel_63d"""
    return (close.ewm(span=3).mean() - close.ewm(span=10).mean()).diff(63).diff(21)

def adln_189_chaikin_osc_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_189_chaikin_osc_accel_126d"""
    return (close.ewm(span=3).mean() - close.ewm(span=10).mean()).diff(126).diff(21)

def adln_190_chaikin_osc_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_190_chaikin_osc_accel_252d"""
    return (close.ewm(span=3).mean() - close.ewm(span=10).mean()).diff(252).diff(21)

def adln_191_adl_roc_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_191_adl_roc_accel_5d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()).diff(5).diff(21)

def adln_192_adl_roc_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_192_adl_roc_accel_21d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()).diff(21).diff(21)

def adln_193_adl_roc_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_193_adl_roc_accel_63d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()).diff(63).diff(21)

def adln_194_adl_roc_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_194_adl_roc_accel_126d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()).diff(126).diff(21)

def adln_195_adl_roc_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_195_adl_roc_accel_252d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()).diff(252).diff(21)

def adln_196_adl_mfi_accel_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_196_adl_mfi_accel_5d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close).diff(5).diff(21)

def adln_197_adl_mfi_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_197_adl_mfi_accel_21d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close).diff(21).diff(21)

def adln_198_adl_mfi_accel_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_198_adl_mfi_accel_63d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close).diff(63).diff(21)

def adln_199_adl_mfi_accel_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_199_adl_mfi_accel_126d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close).diff(126).diff(21)

def adln_200_adl_mfi_accel_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_200_adl_mfi_accel_252d"""
    return ((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V86_REGISTRY_ACCEL = {
    "adln_176_adl_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_176_adl_accel_5d},
    "adln_177_adl_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_177_adl_accel_21d},
    "adln_178_adl_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_178_adl_accel_63d},
    "adln_179_adl_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_179_adl_accel_126d},
    "adln_180_adl_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_180_adl_accel_252d},
    "adln_181_adl_ps_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_181_adl_ps_accel_5d},
    "adln_182_adl_ps_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_182_adl_ps_accel_21d},
    "adln_183_adl_ps_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_183_adl_ps_accel_63d},
    "adln_184_adl_ps_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_184_adl_ps_accel_126d},
    "adln_185_adl_ps_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_185_adl_ps_accel_252d},
    "adln_186_chaikin_osc_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_186_chaikin_osc_accel_5d},
    "adln_187_chaikin_osc_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_187_chaikin_osc_accel_21d},
    "adln_188_chaikin_osc_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_188_chaikin_osc_accel_63d},
    "adln_189_chaikin_osc_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_189_chaikin_osc_accel_126d},
    "adln_190_chaikin_osc_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_190_chaikin_osc_accel_252d},
    "adln_191_adl_roc_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_191_adl_roc_accel_5d},
    "adln_192_adl_roc_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_192_adl_roc_accel_21d},
    "adln_193_adl_roc_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_193_adl_roc_accel_63d},
    "adln_194_adl_roc_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_194_adl_roc_accel_126d},
    "adln_195_adl_roc_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_195_adl_roc_accel_252d},
    "adln_196_adl_mfi_accel_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_196_adl_mfi_accel_5d},
    "adln_197_adl_mfi_accel_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_197_adl_mfi_accel_21d},
    "adln_198_adl_mfi_accel_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_198_adl_mfi_accel_63d},
    "adln_199_adl_mfi_accel_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_199_adl_mfi_accel_126d},
    "adln_200_adl_mfi_accel_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_200_adl_mfi_accel_252d},
}
