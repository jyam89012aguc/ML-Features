"""
84_mfid_dynamics — Base Features 076-150
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

def mfid_076_mfi_slope_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_076_mfi_slope_lvl_5d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(5)
    return _rolling_mean(base, 5)

def mfid_077_mfi_slope_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_077_mfi_slope_zscore_5d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(5)
    return _zscore_rolling(base, 5)

def mfid_078_mfi_slope_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_078_mfi_slope_rank_5d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(5)
    return _rank_pct(base, 5)

def mfid_079_mfi_slope_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_079_mfi_slope_lvl_21d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(5)
    return _rolling_mean(base, 21)

def mfid_080_mfi_slope_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_080_mfi_slope_zscore_21d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(5)
    return _zscore_rolling(base, 21)

def mfid_081_mfi_slope_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_081_mfi_slope_rank_21d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(5)
    return _rank_pct(base, 21)

def mfid_082_mfi_slope_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_082_mfi_slope_lvl_63d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(5)
    return _rolling_mean(base, 63)

def mfid_083_mfi_slope_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_083_mfi_slope_zscore_63d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(5)
    return _zscore_rolling(base, 63)

def mfid_084_mfi_slope_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_084_mfi_slope_rank_63d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(5)
    return _rank_pct(base, 63)

def mfid_085_mfi_slope_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_085_mfi_slope_lvl_126d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(5)
    return _rolling_mean(base, 126)

def mfid_086_mfi_slope_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_086_mfi_slope_zscore_126d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(5)
    return _zscore_rolling(base, 126)

def mfid_087_mfi_slope_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_087_mfi_slope_rank_126d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(5)
    return _rank_pct(base, 126)

def mfid_088_mfi_slope_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_088_mfi_slope_lvl_252d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(5)
    return _rolling_mean(base, 252)

def mfid_089_mfi_slope_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_089_mfi_slope_zscore_252d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(5)
    return _zscore_rolling(base, 252)

def mfid_090_mfi_slope_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_090_mfi_slope_rank_252d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).diff(5)
    return _rank_pct(base, 252)

def mfid_091_mfi_sma_rat_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_091_mfi_sma_rat_lvl_5d"""
    base = _safe_div(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 14))
    return _rolling_mean(base, 5)

def mfid_092_mfi_sma_rat_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_092_mfi_sma_rat_zscore_5d"""
    base = _safe_div(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 14))
    return _zscore_rolling(base, 5)

def mfid_093_mfi_sma_rat_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_093_mfi_sma_rat_rank_5d"""
    base = _safe_div(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 14))
    return _rank_pct(base, 5)

def mfid_094_mfi_sma_rat_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_094_mfi_sma_rat_lvl_21d"""
    base = _safe_div(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 14))
    return _rolling_mean(base, 21)

def mfid_095_mfi_sma_rat_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_095_mfi_sma_rat_zscore_21d"""
    base = _safe_div(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 14))
    return _zscore_rolling(base, 21)

def mfid_096_mfi_sma_rat_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_096_mfi_sma_rat_rank_21d"""
    base = _safe_div(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 14))
    return _rank_pct(base, 21)

def mfid_097_mfi_sma_rat_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_097_mfi_sma_rat_lvl_63d"""
    base = _safe_div(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 14))
    return _rolling_mean(base, 63)

def mfid_098_mfi_sma_rat_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_098_mfi_sma_rat_zscore_63d"""
    base = _safe_div(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 14))
    return _zscore_rolling(base, 63)

def mfid_099_mfi_sma_rat_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_099_mfi_sma_rat_rank_63d"""
    base = _safe_div(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 14))
    return _rank_pct(base, 63)

def mfid_100_mfi_sma_rat_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_100_mfi_sma_rat_lvl_126d"""
    base = _safe_div(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 14))
    return _rolling_mean(base, 126)

def mfid_101_mfi_sma_rat_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_101_mfi_sma_rat_zscore_126d"""
    base = _safe_div(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 14))
    return _zscore_rolling(base, 126)

def mfid_102_mfi_sma_rat_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_102_mfi_sma_rat_rank_126d"""
    base = _safe_div(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 14))
    return _rank_pct(base, 126)

def mfid_103_mfi_sma_rat_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_103_mfi_sma_rat_lvl_252d"""
    base = _safe_div(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 14))
    return _rolling_mean(base, 252)

def mfid_104_mfi_sma_rat_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_104_mfi_sma_rat_zscore_252d"""
    base = _safe_div(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 14))
    return _zscore_rolling(base, 252)

def mfid_105_mfi_sma_rat_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_105_mfi_sma_rat_rank_252d"""
    base = _safe_div(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 14))
    return _rank_pct(base, 252)

def mfid_106_mfi_abs_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_106_mfi_abs_lvl_5d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).abs()
    return _rolling_mean(base, 5)

def mfid_107_mfi_abs_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_107_mfi_abs_zscore_5d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).abs()
    return _zscore_rolling(base, 5)

def mfid_108_mfi_abs_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_108_mfi_abs_rank_5d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).abs()
    return _rank_pct(base, 5)

def mfid_109_mfi_abs_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_109_mfi_abs_lvl_21d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).abs()
    return _rolling_mean(base, 21)

def mfid_110_mfi_abs_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_110_mfi_abs_zscore_21d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).abs()
    return _zscore_rolling(base, 21)

def mfid_111_mfi_abs_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_111_mfi_abs_rank_21d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).abs()
    return _rank_pct(base, 21)

def mfid_112_mfi_abs_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_112_mfi_abs_lvl_63d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).abs()
    return _rolling_mean(base, 63)

def mfid_113_mfi_abs_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_113_mfi_abs_zscore_63d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).abs()
    return _zscore_rolling(base, 63)

def mfid_114_mfi_abs_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_114_mfi_abs_rank_63d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).abs()
    return _rank_pct(base, 63)

def mfid_115_mfi_abs_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_115_mfi_abs_lvl_126d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).abs()
    return _rolling_mean(base, 126)

def mfid_116_mfi_abs_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_116_mfi_abs_zscore_126d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).abs()
    return _zscore_rolling(base, 126)

def mfid_117_mfi_abs_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_117_mfi_abs_rank_126d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).abs()
    return _rank_pct(base, 126)

def mfid_118_mfi_abs_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_118_mfi_abs_lvl_252d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).abs()
    return _rolling_mean(base, 252)

def mfid_119_mfi_abs_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_119_mfi_abs_zscore_252d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).abs()
    return _zscore_rolling(base, 252)

def mfid_120_mfi_abs_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_120_mfi_abs_rank_252d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))).abs()
    return _rank_pct(base, 252)

def mfid_121_mfi_sig_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_121_mfi_sig_lvl_5d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 9)
    return _rolling_mean(base, 5)

def mfid_122_mfi_sig_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_122_mfi_sig_zscore_5d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 9)
    return _zscore_rolling(base, 5)

def mfid_123_mfi_sig_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_123_mfi_sig_rank_5d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 9)
    return _rank_pct(base, 5)

def mfid_124_mfi_sig_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_124_mfi_sig_lvl_21d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 9)
    return _rolling_mean(base, 21)

def mfid_125_mfi_sig_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_125_mfi_sig_zscore_21d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 9)
    return _zscore_rolling(base, 21)

def mfid_126_mfi_sig_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_126_mfi_sig_rank_21d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 9)
    return _rank_pct(base, 21)

def mfid_127_mfi_sig_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_127_mfi_sig_lvl_63d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 9)
    return _rolling_mean(base, 63)

def mfid_128_mfi_sig_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_128_mfi_sig_zscore_63d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 9)
    return _zscore_rolling(base, 63)

def mfid_129_mfi_sig_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_129_mfi_sig_rank_63d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 9)
    return _rank_pct(base, 63)

def mfid_130_mfi_sig_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_130_mfi_sig_lvl_126d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 9)
    return _rolling_mean(base, 126)

def mfid_131_mfi_sig_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_131_mfi_sig_zscore_126d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 9)
    return _zscore_rolling(base, 126)

def mfid_132_mfi_sig_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_132_mfi_sig_rank_126d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 9)
    return _rank_pct(base, 126)

def mfid_133_mfi_sig_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_133_mfi_sig_lvl_252d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 9)
    return _rolling_mean(base, 252)

def mfid_134_mfi_sig_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_134_mfi_sig_zscore_252d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 9)
    return _zscore_rolling(base, 252)

def mfid_135_mfi_sig_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_135_mfi_sig_rank_252d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - _rolling_mean(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 9)
    return _rank_pct(base, 252)

def mfid_136_rmf_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_136_rmf_z_lvl_5d"""
    base = _zscore_rolling(((high + low + close) / 3) * volume, 63)
    return _rolling_mean(base, 5)

def mfid_137_rmf_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_137_rmf_z_zscore_5d"""
    base = _zscore_rolling(((high + low + close) / 3) * volume, 63)
    return _zscore_rolling(base, 5)

def mfid_138_rmf_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_138_rmf_z_rank_5d"""
    base = _zscore_rolling(((high + low + close) / 3) * volume, 63)
    return _rank_pct(base, 5)

def mfid_139_rmf_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_139_rmf_z_lvl_21d"""
    base = _zscore_rolling(((high + low + close) / 3) * volume, 63)
    return _rolling_mean(base, 21)

def mfid_140_rmf_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_140_rmf_z_zscore_21d"""
    base = _zscore_rolling(((high + low + close) / 3) * volume, 63)
    return _zscore_rolling(base, 21)

def mfid_141_rmf_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_141_rmf_z_rank_21d"""
    base = _zscore_rolling(((high + low + close) / 3) * volume, 63)
    return _rank_pct(base, 21)

def mfid_142_rmf_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_142_rmf_z_lvl_63d"""
    base = _zscore_rolling(((high + low + close) / 3) * volume, 63)
    return _rolling_mean(base, 63)

def mfid_143_rmf_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_143_rmf_z_zscore_63d"""
    base = _zscore_rolling(((high + low + close) / 3) * volume, 63)
    return _zscore_rolling(base, 63)

def mfid_144_rmf_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_144_rmf_z_rank_63d"""
    base = _zscore_rolling(((high + low + close) / 3) * volume, 63)
    return _rank_pct(base, 63)

def mfid_145_rmf_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_145_rmf_z_lvl_126d"""
    base = _zscore_rolling(((high + low + close) / 3) * volume, 63)
    return _rolling_mean(base, 126)

def mfid_146_rmf_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_146_rmf_z_zscore_126d"""
    base = _zscore_rolling(((high + low + close) / 3) * volume, 63)
    return _zscore_rolling(base, 126)

def mfid_147_rmf_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_147_rmf_z_rank_126d"""
    base = _zscore_rolling(((high + low + close) / 3) * volume, 63)
    return _rank_pct(base, 126)

def mfid_148_rmf_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_148_rmf_z_lvl_252d"""
    base = _zscore_rolling(((high + low + close) / 3) * volume, 63)
    return _rolling_mean(base, 252)

def mfid_149_rmf_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_149_rmf_z_zscore_252d"""
    base = _zscore_rolling(((high + low + close) / 3) * volume, 63)
    return _zscore_rolling(base, 252)

def mfid_150_rmf_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_150_rmf_z_rank_252d"""
    base = _zscore_rolling(((high + low + close) / 3) * volume, 63)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V84_REGISTRY_2 = {
    "mfid_076_mfi_slope_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_076_mfi_slope_lvl_5d},
    "mfid_077_mfi_slope_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_077_mfi_slope_zscore_5d},
    "mfid_078_mfi_slope_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_078_mfi_slope_rank_5d},
    "mfid_079_mfi_slope_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_079_mfi_slope_lvl_21d},
    "mfid_080_mfi_slope_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_080_mfi_slope_zscore_21d},
    "mfid_081_mfi_slope_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_081_mfi_slope_rank_21d},
    "mfid_082_mfi_slope_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_082_mfi_slope_lvl_63d},
    "mfid_083_mfi_slope_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_083_mfi_slope_zscore_63d},
    "mfid_084_mfi_slope_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_084_mfi_slope_rank_63d},
    "mfid_085_mfi_slope_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_085_mfi_slope_lvl_126d},
    "mfid_086_mfi_slope_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_086_mfi_slope_zscore_126d},
    "mfid_087_mfi_slope_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_087_mfi_slope_rank_126d},
    "mfid_088_mfi_slope_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_088_mfi_slope_lvl_252d},
    "mfid_089_mfi_slope_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_089_mfi_slope_zscore_252d},
    "mfid_090_mfi_slope_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_090_mfi_slope_rank_252d},
    "mfid_091_mfi_sma_rat_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_091_mfi_sma_rat_lvl_5d},
    "mfid_092_mfi_sma_rat_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_092_mfi_sma_rat_zscore_5d},
    "mfid_093_mfi_sma_rat_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_093_mfi_sma_rat_rank_5d},
    "mfid_094_mfi_sma_rat_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_094_mfi_sma_rat_lvl_21d},
    "mfid_095_mfi_sma_rat_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_095_mfi_sma_rat_zscore_21d},
    "mfid_096_mfi_sma_rat_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_096_mfi_sma_rat_rank_21d},
    "mfid_097_mfi_sma_rat_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_097_mfi_sma_rat_lvl_63d},
    "mfid_098_mfi_sma_rat_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_098_mfi_sma_rat_zscore_63d},
    "mfid_099_mfi_sma_rat_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_099_mfi_sma_rat_rank_63d},
    "mfid_100_mfi_sma_rat_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_100_mfi_sma_rat_lvl_126d},
    "mfid_101_mfi_sma_rat_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_101_mfi_sma_rat_zscore_126d},
    "mfid_102_mfi_sma_rat_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_102_mfi_sma_rat_rank_126d},
    "mfid_103_mfi_sma_rat_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_103_mfi_sma_rat_lvl_252d},
    "mfid_104_mfi_sma_rat_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_104_mfi_sma_rat_zscore_252d},
    "mfid_105_mfi_sma_rat_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_105_mfi_sma_rat_rank_252d},
    "mfid_106_mfi_abs_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_106_mfi_abs_lvl_5d},
    "mfid_107_mfi_abs_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_107_mfi_abs_zscore_5d},
    "mfid_108_mfi_abs_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_108_mfi_abs_rank_5d},
    "mfid_109_mfi_abs_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_109_mfi_abs_lvl_21d},
    "mfid_110_mfi_abs_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_110_mfi_abs_zscore_21d},
    "mfid_111_mfi_abs_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_111_mfi_abs_rank_21d},
    "mfid_112_mfi_abs_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_112_mfi_abs_lvl_63d},
    "mfid_113_mfi_abs_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_113_mfi_abs_zscore_63d},
    "mfid_114_mfi_abs_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_114_mfi_abs_rank_63d},
    "mfid_115_mfi_abs_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_115_mfi_abs_lvl_126d},
    "mfid_116_mfi_abs_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_116_mfi_abs_zscore_126d},
    "mfid_117_mfi_abs_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_117_mfi_abs_rank_126d},
    "mfid_118_mfi_abs_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_118_mfi_abs_lvl_252d},
    "mfid_119_mfi_abs_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_119_mfi_abs_zscore_252d},
    "mfid_120_mfi_abs_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_120_mfi_abs_rank_252d},
    "mfid_121_mfi_sig_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_121_mfi_sig_lvl_5d},
    "mfid_122_mfi_sig_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_122_mfi_sig_zscore_5d},
    "mfid_123_mfi_sig_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_123_mfi_sig_rank_5d},
    "mfid_124_mfi_sig_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_124_mfi_sig_lvl_21d},
    "mfid_125_mfi_sig_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_125_mfi_sig_zscore_21d},
    "mfid_126_mfi_sig_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_126_mfi_sig_rank_21d},
    "mfid_127_mfi_sig_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_127_mfi_sig_lvl_63d},
    "mfid_128_mfi_sig_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_128_mfi_sig_zscore_63d},
    "mfid_129_mfi_sig_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_129_mfi_sig_rank_63d},
    "mfid_130_mfi_sig_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_130_mfi_sig_lvl_126d},
    "mfid_131_mfi_sig_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_131_mfi_sig_zscore_126d},
    "mfid_132_mfi_sig_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_132_mfi_sig_rank_126d},
    "mfid_133_mfi_sig_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_133_mfi_sig_lvl_252d},
    "mfid_134_mfi_sig_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_134_mfi_sig_zscore_252d},
    "mfid_135_mfi_sig_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_135_mfi_sig_rank_252d},
    "mfid_136_rmf_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_136_rmf_z_lvl_5d},
    "mfid_137_rmf_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_137_rmf_z_zscore_5d},
    "mfid_138_rmf_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_138_rmf_z_rank_5d},
    "mfid_139_rmf_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_139_rmf_z_lvl_21d},
    "mfid_140_rmf_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_140_rmf_z_zscore_21d},
    "mfid_141_rmf_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_141_rmf_z_rank_21d},
    "mfid_142_rmf_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_142_rmf_z_lvl_63d},
    "mfid_143_rmf_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_143_rmf_z_zscore_63d},
    "mfid_144_rmf_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_144_rmf_z_rank_63d},
    "mfid_145_rmf_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_145_rmf_z_lvl_126d},
    "mfid_146_rmf_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_146_rmf_z_zscore_126d},
    "mfid_147_rmf_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_147_rmf_z_rank_126d},
    "mfid_148_rmf_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_148_rmf_z_lvl_252d},
    "mfid_149_rmf_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_149_rmf_z_zscore_252d},
    "mfid_150_rmf_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_150_rmf_z_rank_252d},
}
