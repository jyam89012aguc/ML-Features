"""
81_adxd_dynamics — Base Features 076-150
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

def adxd_076_adx_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_076_adx_lvl_5d"""
    base = 100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)
    return _rolling_mean(base, 5)

def adxd_077_adx_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_077_adx_zscore_5d"""
    base = 100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)
    return _zscore_rolling(base, 5)

def adxd_078_adx_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_078_adx_rank_5d"""
    base = 100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)
    return _rank_pct(base, 5)

def adxd_079_adx_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_079_adx_lvl_21d"""
    base = 100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)
    return _rolling_mean(base, 21)

def adxd_080_adx_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_080_adx_zscore_21d"""
    base = 100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)
    return _zscore_rolling(base, 21)

def adxd_081_adx_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_081_adx_rank_21d"""
    base = 100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)
    return _rank_pct(base, 21)

def adxd_082_adx_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_082_adx_lvl_63d"""
    base = 100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)
    return _rolling_mean(base, 63)

def adxd_083_adx_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_083_adx_zscore_63d"""
    base = 100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)
    return _zscore_rolling(base, 63)

def adxd_084_adx_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_084_adx_rank_63d"""
    base = 100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)
    return _rank_pct(base, 63)

def adxd_085_adx_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_085_adx_lvl_126d"""
    base = 100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)
    return _rolling_mean(base, 126)

def adxd_086_adx_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_086_adx_zscore_126d"""
    base = 100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)
    return _zscore_rolling(base, 126)

def adxd_087_adx_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_087_adx_rank_126d"""
    base = 100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)
    return _rank_pct(base, 126)

def adxd_088_adx_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_088_adx_lvl_252d"""
    base = 100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)
    return _rolling_mean(base, 252)

def adxd_089_adx_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_089_adx_zscore_252d"""
    base = 100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)
    return _zscore_rolling(base, 252)

def adxd_090_adx_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_090_adx_rank_252d"""
    base = 100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)
    return _rank_pct(base, 252)

def adxd_091_adx_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_091_adx_z_lvl_5d"""
    base = _zscore_rolling(100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14), 63)
    return _rolling_mean(base, 5)

def adxd_092_adx_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_092_adx_z_zscore_5d"""
    base = _zscore_rolling(100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14), 63)
    return _zscore_rolling(base, 5)

def adxd_093_adx_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_093_adx_z_rank_5d"""
    base = _zscore_rolling(100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14), 63)
    return _rank_pct(base, 5)

def adxd_094_adx_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_094_adx_z_lvl_21d"""
    base = _zscore_rolling(100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14), 63)
    return _rolling_mean(base, 21)

def adxd_095_adx_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_095_adx_z_zscore_21d"""
    base = _zscore_rolling(100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14), 63)
    return _zscore_rolling(base, 21)

def adxd_096_adx_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_096_adx_z_rank_21d"""
    base = _zscore_rolling(100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14), 63)
    return _rank_pct(base, 21)

def adxd_097_adx_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_097_adx_z_lvl_63d"""
    base = _zscore_rolling(100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14), 63)
    return _rolling_mean(base, 63)

def adxd_098_adx_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_098_adx_z_zscore_63d"""
    base = _zscore_rolling(100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14), 63)
    return _zscore_rolling(base, 63)

def adxd_099_adx_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_099_adx_z_rank_63d"""
    base = _zscore_rolling(100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14), 63)
    return _rank_pct(base, 63)

def adxd_100_adx_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_100_adx_z_lvl_126d"""
    base = _zscore_rolling(100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14), 63)
    return _rolling_mean(base, 126)

def adxd_101_adx_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_101_adx_z_zscore_126d"""
    base = _zscore_rolling(100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14), 63)
    return _zscore_rolling(base, 126)

def adxd_102_adx_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_102_adx_z_rank_126d"""
    base = _zscore_rolling(100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14), 63)
    return _rank_pct(base, 126)

def adxd_103_adx_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_103_adx_z_lvl_252d"""
    base = _zscore_rolling(100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14), 63)
    return _rolling_mean(base, 252)

def adxd_104_adx_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_104_adx_z_zscore_252d"""
    base = _zscore_rolling(100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14), 63)
    return _zscore_rolling(base, 252)

def adxd_105_adx_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_105_adx_z_rank_252d"""
    base = _zscore_rolling(100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14), 63)
    return _rank_pct(base, 252)

def adxd_106_di_diff_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_106_di_diff_lvl_5d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rolling_mean(base, 5)

def adxd_107_di_diff_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_107_di_diff_zscore_5d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _zscore_rolling(base, 5)

def adxd_108_di_diff_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_108_di_diff_rank_5d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rank_pct(base, 5)

def adxd_109_di_diff_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_109_di_diff_lvl_21d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rolling_mean(base, 21)

def adxd_110_di_diff_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_110_di_diff_zscore_21d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _zscore_rolling(base, 21)

def adxd_111_di_diff_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_111_di_diff_rank_21d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rank_pct(base, 21)

def adxd_112_di_diff_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_112_di_diff_lvl_63d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rolling_mean(base, 63)

def adxd_113_di_diff_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_113_di_diff_zscore_63d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _zscore_rolling(base, 63)

def adxd_114_di_diff_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_114_di_diff_rank_63d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rank_pct(base, 63)

def adxd_115_di_diff_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_115_di_diff_lvl_126d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rolling_mean(base, 126)

def adxd_116_di_diff_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_116_di_diff_zscore_126d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _zscore_rolling(base, 126)

def adxd_117_di_diff_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_117_di_diff_rank_126d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rank_pct(base, 126)

def adxd_118_di_diff_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_118_di_diff_lvl_252d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rolling_mean(base, 252)

def adxd_119_di_diff_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_119_di_diff_zscore_252d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _zscore_rolling(base, 252)

def adxd_120_di_diff_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_120_di_diff_rank_252d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rank_pct(base, 252)

def adxd_121_adx_slope_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_121_adx_slope_lvl_5d"""
    base = (100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)).diff(5)
    return _rolling_mean(base, 5)

def adxd_122_adx_slope_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_122_adx_slope_zscore_5d"""
    base = (100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)).diff(5)
    return _zscore_rolling(base, 5)

def adxd_123_adx_slope_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_123_adx_slope_rank_5d"""
    base = (100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)).diff(5)
    return _rank_pct(base, 5)

def adxd_124_adx_slope_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_124_adx_slope_lvl_21d"""
    base = (100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)).diff(5)
    return _rolling_mean(base, 21)

def adxd_125_adx_slope_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_125_adx_slope_zscore_21d"""
    base = (100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)).diff(5)
    return _zscore_rolling(base, 21)

def adxd_126_adx_slope_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_126_adx_slope_rank_21d"""
    base = (100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)).diff(5)
    return _rank_pct(base, 21)

def adxd_127_adx_slope_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_127_adx_slope_lvl_63d"""
    base = (100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)).diff(5)
    return _rolling_mean(base, 63)

def adxd_128_adx_slope_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_128_adx_slope_zscore_63d"""
    base = (100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)).diff(5)
    return _zscore_rolling(base, 63)

def adxd_129_adx_slope_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_129_adx_slope_rank_63d"""
    base = (100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)).diff(5)
    return _rank_pct(base, 63)

def adxd_130_adx_slope_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_130_adx_slope_lvl_126d"""
    base = (100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)).diff(5)
    return _rolling_mean(base, 126)

def adxd_131_adx_slope_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_131_adx_slope_zscore_126d"""
    base = (100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)).diff(5)
    return _zscore_rolling(base, 126)

def adxd_132_adx_slope_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_132_adx_slope_rank_126d"""
    base = (100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)).diff(5)
    return _rank_pct(base, 126)

def adxd_133_adx_slope_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_133_adx_slope_lvl_252d"""
    base = (100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)).diff(5)
    return _rolling_mean(base, 252)

def adxd_134_adx_slope_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_134_adx_slope_zscore_252d"""
    base = (100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)).diff(5)
    return _zscore_rolling(base, 252)

def adxd_135_adx_slope_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_135_adx_slope_rank_252d"""
    base = (100 * _rolling_mean(_safe_div((100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) - 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))).abs(), (100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)) + 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))), 14)).diff(5)
    return _rank_pct(base, 252)

def adxd_136_di_cross_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_136_di_cross_lvl_5d"""
    base = _safe_div(100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)), 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))
    return _rolling_mean(base, 5)

def adxd_137_di_cross_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_137_di_cross_zscore_5d"""
    base = _safe_div(100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)), 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))
    return _zscore_rolling(base, 5)

def adxd_138_di_cross_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_138_di_cross_rank_5d"""
    base = _safe_div(100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)), 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))
    return _rank_pct(base, 5)

def adxd_139_di_cross_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_139_di_cross_lvl_21d"""
    base = _safe_div(100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)), 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))
    return _rolling_mean(base, 21)

def adxd_140_di_cross_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_140_di_cross_zscore_21d"""
    base = _safe_div(100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)), 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))
    return _zscore_rolling(base, 21)

def adxd_141_di_cross_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_141_di_cross_rank_21d"""
    base = _safe_div(100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)), 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))
    return _rank_pct(base, 21)

def adxd_142_di_cross_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_142_di_cross_lvl_63d"""
    base = _safe_div(100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)), 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))
    return _rolling_mean(base, 63)

def adxd_143_di_cross_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_143_di_cross_zscore_63d"""
    base = _safe_div(100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)), 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))
    return _zscore_rolling(base, 63)

def adxd_144_di_cross_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_144_di_cross_rank_63d"""
    base = _safe_div(100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)), 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))
    return _rank_pct(base, 63)

def adxd_145_di_cross_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_145_di_cross_lvl_126d"""
    base = _safe_div(100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)), 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))
    return _rolling_mean(base, 126)

def adxd_146_di_cross_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_146_di_cross_zscore_126d"""
    base = _safe_div(100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)), 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))
    return _zscore_rolling(base, 126)

def adxd_147_di_cross_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_147_di_cross_rank_126d"""
    base = _safe_div(100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)), 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))
    return _rank_pct(base, 126)

def adxd_148_di_cross_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_148_di_cross_lvl_252d"""
    base = _safe_div(100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)), 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))
    return _rolling_mean(base, 252)

def adxd_149_di_cross_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_149_di_cross_zscore_252d"""
    base = _safe_div(100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)), 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))
    return _zscore_rolling(base, 252)

def adxd_150_di_cross_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_150_di_cross_rank_252d"""
    base = _safe_div(100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)), 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14)))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V81_REGISTRY_2 = {
    "adxd_076_adx_lvl_5d": {"inputs": ["high", "low", "close"], "func": adxd_076_adx_lvl_5d},
    "adxd_077_adx_zscore_5d": {"inputs": ["high", "low", "close"], "func": adxd_077_adx_zscore_5d},
    "adxd_078_adx_rank_5d": {"inputs": ["high", "low", "close"], "func": adxd_078_adx_rank_5d},
    "adxd_079_adx_lvl_21d": {"inputs": ["high", "low", "close"], "func": adxd_079_adx_lvl_21d},
    "adxd_080_adx_zscore_21d": {"inputs": ["high", "low", "close"], "func": adxd_080_adx_zscore_21d},
    "adxd_081_adx_rank_21d": {"inputs": ["high", "low", "close"], "func": adxd_081_adx_rank_21d},
    "adxd_082_adx_lvl_63d": {"inputs": ["high", "low", "close"], "func": adxd_082_adx_lvl_63d},
    "adxd_083_adx_zscore_63d": {"inputs": ["high", "low", "close"], "func": adxd_083_adx_zscore_63d},
    "adxd_084_adx_rank_63d": {"inputs": ["high", "low", "close"], "func": adxd_084_adx_rank_63d},
    "adxd_085_adx_lvl_126d": {"inputs": ["high", "low", "close"], "func": adxd_085_adx_lvl_126d},
    "adxd_086_adx_zscore_126d": {"inputs": ["high", "low", "close"], "func": adxd_086_adx_zscore_126d},
    "adxd_087_adx_rank_126d": {"inputs": ["high", "low", "close"], "func": adxd_087_adx_rank_126d},
    "adxd_088_adx_lvl_252d": {"inputs": ["high", "low", "close"], "func": adxd_088_adx_lvl_252d},
    "adxd_089_adx_zscore_252d": {"inputs": ["high", "low", "close"], "func": adxd_089_adx_zscore_252d},
    "adxd_090_adx_rank_252d": {"inputs": ["high", "low", "close"], "func": adxd_090_adx_rank_252d},
    "adxd_091_adx_z_lvl_5d": {"inputs": ["high", "low", "close"], "func": adxd_091_adx_z_lvl_5d},
    "adxd_092_adx_z_zscore_5d": {"inputs": ["high", "low", "close"], "func": adxd_092_adx_z_zscore_5d},
    "adxd_093_adx_z_rank_5d": {"inputs": ["high", "low", "close"], "func": adxd_093_adx_z_rank_5d},
    "adxd_094_adx_z_lvl_21d": {"inputs": ["high", "low", "close"], "func": adxd_094_adx_z_lvl_21d},
    "adxd_095_adx_z_zscore_21d": {"inputs": ["high", "low", "close"], "func": adxd_095_adx_z_zscore_21d},
    "adxd_096_adx_z_rank_21d": {"inputs": ["high", "low", "close"], "func": adxd_096_adx_z_rank_21d},
    "adxd_097_adx_z_lvl_63d": {"inputs": ["high", "low", "close"], "func": adxd_097_adx_z_lvl_63d},
    "adxd_098_adx_z_zscore_63d": {"inputs": ["high", "low", "close"], "func": adxd_098_adx_z_zscore_63d},
    "adxd_099_adx_z_rank_63d": {"inputs": ["high", "low", "close"], "func": adxd_099_adx_z_rank_63d},
    "adxd_100_adx_z_lvl_126d": {"inputs": ["high", "low", "close"], "func": adxd_100_adx_z_lvl_126d},
    "adxd_101_adx_z_zscore_126d": {"inputs": ["high", "low", "close"], "func": adxd_101_adx_z_zscore_126d},
    "adxd_102_adx_z_rank_126d": {"inputs": ["high", "low", "close"], "func": adxd_102_adx_z_rank_126d},
    "adxd_103_adx_z_lvl_252d": {"inputs": ["high", "low", "close"], "func": adxd_103_adx_z_lvl_252d},
    "adxd_104_adx_z_zscore_252d": {"inputs": ["high", "low", "close"], "func": adxd_104_adx_z_zscore_252d},
    "adxd_105_adx_z_rank_252d": {"inputs": ["high", "low", "close"], "func": adxd_105_adx_z_rank_252d},
    "adxd_106_di_diff_lvl_5d": {"inputs": ["high", "low", "close"], "func": adxd_106_di_diff_lvl_5d},
    "adxd_107_di_diff_zscore_5d": {"inputs": ["high", "low", "close"], "func": adxd_107_di_diff_zscore_5d},
    "adxd_108_di_diff_rank_5d": {"inputs": ["high", "low", "close"], "func": adxd_108_di_diff_rank_5d},
    "adxd_109_di_diff_lvl_21d": {"inputs": ["high", "low", "close"], "func": adxd_109_di_diff_lvl_21d},
    "adxd_110_di_diff_zscore_21d": {"inputs": ["high", "low", "close"], "func": adxd_110_di_diff_zscore_21d},
    "adxd_111_di_diff_rank_21d": {"inputs": ["high", "low", "close"], "func": adxd_111_di_diff_rank_21d},
    "adxd_112_di_diff_lvl_63d": {"inputs": ["high", "low", "close"], "func": adxd_112_di_diff_lvl_63d},
    "adxd_113_di_diff_zscore_63d": {"inputs": ["high", "low", "close"], "func": adxd_113_di_diff_zscore_63d},
    "adxd_114_di_diff_rank_63d": {"inputs": ["high", "low", "close"], "func": adxd_114_di_diff_rank_63d},
    "adxd_115_di_diff_lvl_126d": {"inputs": ["high", "low", "close"], "func": adxd_115_di_diff_lvl_126d},
    "adxd_116_di_diff_zscore_126d": {"inputs": ["high", "low", "close"], "func": adxd_116_di_diff_zscore_126d},
    "adxd_117_di_diff_rank_126d": {"inputs": ["high", "low", "close"], "func": adxd_117_di_diff_rank_126d},
    "adxd_118_di_diff_lvl_252d": {"inputs": ["high", "low", "close"], "func": adxd_118_di_diff_lvl_252d},
    "adxd_119_di_diff_zscore_252d": {"inputs": ["high", "low", "close"], "func": adxd_119_di_diff_zscore_252d},
    "adxd_120_di_diff_rank_252d": {"inputs": ["high", "low", "close"], "func": adxd_120_di_diff_rank_252d},
    "adxd_121_adx_slope_lvl_5d": {"inputs": ["high", "low", "close"], "func": adxd_121_adx_slope_lvl_5d},
    "adxd_122_adx_slope_zscore_5d": {"inputs": ["high", "low", "close"], "func": adxd_122_adx_slope_zscore_5d},
    "adxd_123_adx_slope_rank_5d": {"inputs": ["high", "low", "close"], "func": adxd_123_adx_slope_rank_5d},
    "adxd_124_adx_slope_lvl_21d": {"inputs": ["high", "low", "close"], "func": adxd_124_adx_slope_lvl_21d},
    "adxd_125_adx_slope_zscore_21d": {"inputs": ["high", "low", "close"], "func": adxd_125_adx_slope_zscore_21d},
    "adxd_126_adx_slope_rank_21d": {"inputs": ["high", "low", "close"], "func": adxd_126_adx_slope_rank_21d},
    "adxd_127_adx_slope_lvl_63d": {"inputs": ["high", "low", "close"], "func": adxd_127_adx_slope_lvl_63d},
    "adxd_128_adx_slope_zscore_63d": {"inputs": ["high", "low", "close"], "func": adxd_128_adx_slope_zscore_63d},
    "adxd_129_adx_slope_rank_63d": {"inputs": ["high", "low", "close"], "func": adxd_129_adx_slope_rank_63d},
    "adxd_130_adx_slope_lvl_126d": {"inputs": ["high", "low", "close"], "func": adxd_130_adx_slope_lvl_126d},
    "adxd_131_adx_slope_zscore_126d": {"inputs": ["high", "low", "close"], "func": adxd_131_adx_slope_zscore_126d},
    "adxd_132_adx_slope_rank_126d": {"inputs": ["high", "low", "close"], "func": adxd_132_adx_slope_rank_126d},
    "adxd_133_adx_slope_lvl_252d": {"inputs": ["high", "low", "close"], "func": adxd_133_adx_slope_lvl_252d},
    "adxd_134_adx_slope_zscore_252d": {"inputs": ["high", "low", "close"], "func": adxd_134_adx_slope_zscore_252d},
    "adxd_135_adx_slope_rank_252d": {"inputs": ["high", "low", "close"], "func": adxd_135_adx_slope_rank_252d},
    "adxd_136_di_cross_lvl_5d": {"inputs": ["high", "low", "close"], "func": adxd_136_di_cross_lvl_5d},
    "adxd_137_di_cross_zscore_5d": {"inputs": ["high", "low", "close"], "func": adxd_137_di_cross_zscore_5d},
    "adxd_138_di_cross_rank_5d": {"inputs": ["high", "low", "close"], "func": adxd_138_di_cross_rank_5d},
    "adxd_139_di_cross_lvl_21d": {"inputs": ["high", "low", "close"], "func": adxd_139_di_cross_lvl_21d},
    "adxd_140_di_cross_zscore_21d": {"inputs": ["high", "low", "close"], "func": adxd_140_di_cross_zscore_21d},
    "adxd_141_di_cross_rank_21d": {"inputs": ["high", "low", "close"], "func": adxd_141_di_cross_rank_21d},
    "adxd_142_di_cross_lvl_63d": {"inputs": ["high", "low", "close"], "func": adxd_142_di_cross_lvl_63d},
    "adxd_143_di_cross_zscore_63d": {"inputs": ["high", "low", "close"], "func": adxd_143_di_cross_zscore_63d},
    "adxd_144_di_cross_rank_63d": {"inputs": ["high", "low", "close"], "func": adxd_144_di_cross_rank_63d},
    "adxd_145_di_cross_lvl_126d": {"inputs": ["high", "low", "close"], "func": adxd_145_di_cross_lvl_126d},
    "adxd_146_di_cross_zscore_126d": {"inputs": ["high", "low", "close"], "func": adxd_146_di_cross_zscore_126d},
    "adxd_147_di_cross_rank_126d": {"inputs": ["high", "low", "close"], "func": adxd_147_di_cross_rank_126d},
    "adxd_148_di_cross_lvl_252d": {"inputs": ["high", "low", "close"], "func": adxd_148_di_cross_lvl_252d},
    "adxd_149_di_cross_zscore_252d": {"inputs": ["high", "low", "close"], "func": adxd_149_di_cross_zscore_252d},
    "adxd_150_di_cross_rank_252d": {"inputs": ["high", "low", "close"], "func": adxd_150_di_cross_rank_252d},
}
