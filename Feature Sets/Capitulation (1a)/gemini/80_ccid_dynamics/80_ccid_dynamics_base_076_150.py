"""
80_ccid_dynamics — Base Features 076-150
Domain: ccid_dynamics
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

def ccid_076_cci40_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_076_cci40_lvl_5d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 40), 0.015 * ((high + low + close) / 3).rolling(40).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rolling_mean(base, 5)

def ccid_077_cci40_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_077_cci40_zscore_5d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 40), 0.015 * ((high + low + close) / 3).rolling(40).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _zscore_rolling(base, 5)

def ccid_078_cci40_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_078_cci40_rank_5d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 40), 0.015 * ((high + low + close) / 3).rolling(40).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rank_pct(base, 5)

def ccid_079_cci40_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_079_cci40_lvl_21d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 40), 0.015 * ((high + low + close) / 3).rolling(40).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rolling_mean(base, 21)

def ccid_080_cci40_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_080_cci40_zscore_21d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 40), 0.015 * ((high + low + close) / 3).rolling(40).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _zscore_rolling(base, 21)

def ccid_081_cci40_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_081_cci40_rank_21d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 40), 0.015 * ((high + low + close) / 3).rolling(40).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rank_pct(base, 21)

def ccid_082_cci40_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_082_cci40_lvl_63d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 40), 0.015 * ((high + low + close) / 3).rolling(40).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rolling_mean(base, 63)

def ccid_083_cci40_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_083_cci40_zscore_63d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 40), 0.015 * ((high + low + close) / 3).rolling(40).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _zscore_rolling(base, 63)

def ccid_084_cci40_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_084_cci40_rank_63d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 40), 0.015 * ((high + low + close) / 3).rolling(40).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rank_pct(base, 63)

def ccid_085_cci40_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_085_cci40_lvl_126d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 40), 0.015 * ((high + low + close) / 3).rolling(40).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rolling_mean(base, 126)

def ccid_086_cci40_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_086_cci40_zscore_126d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 40), 0.015 * ((high + low + close) / 3).rolling(40).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _zscore_rolling(base, 126)

def ccid_087_cci40_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_087_cci40_rank_126d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 40), 0.015 * ((high + low + close) / 3).rolling(40).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rank_pct(base, 126)

def ccid_088_cci40_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_088_cci40_lvl_252d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 40), 0.015 * ((high + low + close) / 3).rolling(40).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rolling_mean(base, 252)

def ccid_089_cci40_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_089_cci40_zscore_252d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 40), 0.015 * ((high + low + close) / 3).rolling(40).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _zscore_rolling(base, 252)

def ccid_090_cci40_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_090_cci40_rank_252d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 40), 0.015 * ((high + low + close) / 3).rolling(40).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rank_pct(base, 252)

def ccid_091_cci_sma_rat_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_091_cci_sma_rat_lvl_5d"""
    base = _safe_div(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), _rolling_mean(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 14))
    return _rolling_mean(base, 5)

def ccid_092_cci_sma_rat_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_092_cci_sma_rat_zscore_5d"""
    base = _safe_div(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), _rolling_mean(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 14))
    return _zscore_rolling(base, 5)

def ccid_093_cci_sma_rat_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_093_cci_sma_rat_rank_5d"""
    base = _safe_div(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), _rolling_mean(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 14))
    return _rank_pct(base, 5)

def ccid_094_cci_sma_rat_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_094_cci_sma_rat_lvl_21d"""
    base = _safe_div(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), _rolling_mean(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 14))
    return _rolling_mean(base, 21)

def ccid_095_cci_sma_rat_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_095_cci_sma_rat_zscore_21d"""
    base = _safe_div(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), _rolling_mean(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 14))
    return _zscore_rolling(base, 21)

def ccid_096_cci_sma_rat_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_096_cci_sma_rat_rank_21d"""
    base = _safe_div(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), _rolling_mean(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 14))
    return _rank_pct(base, 21)

def ccid_097_cci_sma_rat_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_097_cci_sma_rat_lvl_63d"""
    base = _safe_div(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), _rolling_mean(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 14))
    return _rolling_mean(base, 63)

def ccid_098_cci_sma_rat_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_098_cci_sma_rat_zscore_63d"""
    base = _safe_div(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), _rolling_mean(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 14))
    return _zscore_rolling(base, 63)

def ccid_099_cci_sma_rat_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_099_cci_sma_rat_rank_63d"""
    base = _safe_div(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), _rolling_mean(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 14))
    return _rank_pct(base, 63)

def ccid_100_cci_sma_rat_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_100_cci_sma_rat_lvl_126d"""
    base = _safe_div(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), _rolling_mean(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 14))
    return _rolling_mean(base, 126)

def ccid_101_cci_sma_rat_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_101_cci_sma_rat_zscore_126d"""
    base = _safe_div(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), _rolling_mean(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 14))
    return _zscore_rolling(base, 126)

def ccid_102_cci_sma_rat_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_102_cci_sma_rat_rank_126d"""
    base = _safe_div(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), _rolling_mean(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 14))
    return _rank_pct(base, 126)

def ccid_103_cci_sma_rat_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_103_cci_sma_rat_lvl_252d"""
    base = _safe_div(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), _rolling_mean(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 14))
    return _rolling_mean(base, 252)

def ccid_104_cci_sma_rat_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_104_cci_sma_rat_zscore_252d"""
    base = _safe_div(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), _rolling_mean(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 14))
    return _zscore_rolling(base, 252)

def ccid_105_cci_sma_rat_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_105_cci_sma_rat_rank_252d"""
    base = _safe_div(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), _rolling_mean(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 14))
    return _rank_pct(base, 252)

def ccid_106_cci_abs_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_106_cci_abs_lvl_5d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).abs()
    return _rolling_mean(base, 5)

def ccid_107_cci_abs_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_107_cci_abs_zscore_5d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).abs()
    return _zscore_rolling(base, 5)

def ccid_108_cci_abs_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_108_cci_abs_rank_5d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).abs()
    return _rank_pct(base, 5)

def ccid_109_cci_abs_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_109_cci_abs_lvl_21d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).abs()
    return _rolling_mean(base, 21)

def ccid_110_cci_abs_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_110_cci_abs_zscore_21d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).abs()
    return _zscore_rolling(base, 21)

def ccid_111_cci_abs_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_111_cci_abs_rank_21d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).abs()
    return _rank_pct(base, 21)

def ccid_112_cci_abs_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_112_cci_abs_lvl_63d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).abs()
    return _rolling_mean(base, 63)

def ccid_113_cci_abs_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_113_cci_abs_zscore_63d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).abs()
    return _zscore_rolling(base, 63)

def ccid_114_cci_abs_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_114_cci_abs_rank_63d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).abs()
    return _rank_pct(base, 63)

def ccid_115_cci_abs_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_115_cci_abs_lvl_126d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).abs()
    return _rolling_mean(base, 126)

def ccid_116_cci_abs_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_116_cci_abs_zscore_126d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).abs()
    return _zscore_rolling(base, 126)

def ccid_117_cci_abs_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_117_cci_abs_rank_126d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).abs()
    return _rank_pct(base, 126)

def ccid_118_cci_abs_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_118_cci_abs_lvl_252d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).abs()
    return _rolling_mean(base, 252)

def ccid_119_cci_abs_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_119_cci_abs_zscore_252d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).abs()
    return _zscore_rolling(base, 252)

def ccid_120_cci_abs_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_120_cci_abs_rank_252d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).abs()
    return _rank_pct(base, 252)

def ccid_121_cci_vol_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_121_cci_vol_lvl_5d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)).rolling(20).std()
    return _rolling_mean(base, 5)

def ccid_122_cci_vol_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_122_cci_vol_zscore_5d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)).rolling(20).std()
    return _zscore_rolling(base, 5)

def ccid_123_cci_vol_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_123_cci_vol_rank_5d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)).rolling(20).std()
    return _rank_pct(base, 5)

def ccid_124_cci_vol_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_124_cci_vol_lvl_21d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)).rolling(20).std()
    return _rolling_mean(base, 21)

def ccid_125_cci_vol_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_125_cci_vol_zscore_21d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)).rolling(20).std()
    return _zscore_rolling(base, 21)

def ccid_126_cci_vol_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_126_cci_vol_rank_21d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)).rolling(20).std()
    return _rank_pct(base, 21)

def ccid_127_cci_vol_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_127_cci_vol_lvl_63d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)).rolling(20).std()
    return _rolling_mean(base, 63)

def ccid_128_cci_vol_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_128_cci_vol_zscore_63d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)).rolling(20).std()
    return _zscore_rolling(base, 63)

def ccid_129_cci_vol_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_129_cci_vol_rank_63d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)).rolling(20).std()
    return _rank_pct(base, 63)

def ccid_130_cci_vol_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_130_cci_vol_lvl_126d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)).rolling(20).std()
    return _rolling_mean(base, 126)

def ccid_131_cci_vol_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_131_cci_vol_zscore_126d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)).rolling(20).std()
    return _zscore_rolling(base, 126)

def ccid_132_cci_vol_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_132_cci_vol_rank_126d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)).rolling(20).std()
    return _rank_pct(base, 126)

def ccid_133_cci_vol_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_133_cci_vol_lvl_252d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)).rolling(20).std()
    return _rolling_mean(base, 252)

def ccid_134_cci_vol_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_134_cci_vol_zscore_252d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)).rolling(20).std()
    return _zscore_rolling(base, 252)

def ccid_135_cci_vol_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_135_cci_vol_rank_252d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)).rolling(20).std()
    return _rank_pct(base, 252)

def ccid_136_cci_hist_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_136_cci_hist_lvl_5d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))) - (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).shift(5)
    return _rolling_mean(base, 5)

def ccid_137_cci_hist_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_137_cci_hist_zscore_5d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))) - (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).shift(5)
    return _zscore_rolling(base, 5)

def ccid_138_cci_hist_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_138_cci_hist_rank_5d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))) - (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).shift(5)
    return _rank_pct(base, 5)

def ccid_139_cci_hist_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_139_cci_hist_lvl_21d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))) - (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).shift(5)
    return _rolling_mean(base, 21)

def ccid_140_cci_hist_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_140_cci_hist_zscore_21d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))) - (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).shift(5)
    return _zscore_rolling(base, 21)

def ccid_141_cci_hist_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_141_cci_hist_rank_21d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))) - (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).shift(5)
    return _rank_pct(base, 21)

def ccid_142_cci_hist_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_142_cci_hist_lvl_63d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))) - (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).shift(5)
    return _rolling_mean(base, 63)

def ccid_143_cci_hist_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_143_cci_hist_zscore_63d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))) - (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).shift(5)
    return _zscore_rolling(base, 63)

def ccid_144_cci_hist_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_144_cci_hist_rank_63d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))) - (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).shift(5)
    return _rank_pct(base, 63)

def ccid_145_cci_hist_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_145_cci_hist_lvl_126d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))) - (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).shift(5)
    return _rolling_mean(base, 126)

def ccid_146_cci_hist_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_146_cci_hist_zscore_126d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))) - (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).shift(5)
    return _zscore_rolling(base, 126)

def ccid_147_cci_hist_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_147_cci_hist_rank_126d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))) - (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).shift(5)
    return _rank_pct(base, 126)

def ccid_148_cci_hist_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_148_cci_hist_lvl_252d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))) - (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).shift(5)
    return _rolling_mean(base, 252)

def ccid_149_cci_hist_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_149_cci_hist_zscore_252d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))) - (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).shift(5)
    return _zscore_rolling(base, 252)

def ccid_150_cci_hist_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_150_cci_hist_rank_252d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))) - (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).shift(5)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V80_REGISTRY_2 = {
    "ccid_076_cci40_lvl_5d": {"inputs": ["high", "low", "close"], "func": ccid_076_cci40_lvl_5d},
    "ccid_077_cci40_zscore_5d": {"inputs": ["high", "low", "close"], "func": ccid_077_cci40_zscore_5d},
    "ccid_078_cci40_rank_5d": {"inputs": ["high", "low", "close"], "func": ccid_078_cci40_rank_5d},
    "ccid_079_cci40_lvl_21d": {"inputs": ["high", "low", "close"], "func": ccid_079_cci40_lvl_21d},
    "ccid_080_cci40_zscore_21d": {"inputs": ["high", "low", "close"], "func": ccid_080_cci40_zscore_21d},
    "ccid_081_cci40_rank_21d": {"inputs": ["high", "low", "close"], "func": ccid_081_cci40_rank_21d},
    "ccid_082_cci40_lvl_63d": {"inputs": ["high", "low", "close"], "func": ccid_082_cci40_lvl_63d},
    "ccid_083_cci40_zscore_63d": {"inputs": ["high", "low", "close"], "func": ccid_083_cci40_zscore_63d},
    "ccid_084_cci40_rank_63d": {"inputs": ["high", "low", "close"], "func": ccid_084_cci40_rank_63d},
    "ccid_085_cci40_lvl_126d": {"inputs": ["high", "low", "close"], "func": ccid_085_cci40_lvl_126d},
    "ccid_086_cci40_zscore_126d": {"inputs": ["high", "low", "close"], "func": ccid_086_cci40_zscore_126d},
    "ccid_087_cci40_rank_126d": {"inputs": ["high", "low", "close"], "func": ccid_087_cci40_rank_126d},
    "ccid_088_cci40_lvl_252d": {"inputs": ["high", "low", "close"], "func": ccid_088_cci40_lvl_252d},
    "ccid_089_cci40_zscore_252d": {"inputs": ["high", "low", "close"], "func": ccid_089_cci40_zscore_252d},
    "ccid_090_cci40_rank_252d": {"inputs": ["high", "low", "close"], "func": ccid_090_cci40_rank_252d},
    "ccid_091_cci_sma_rat_lvl_5d": {"inputs": ["high", "low", "close"], "func": ccid_091_cci_sma_rat_lvl_5d},
    "ccid_092_cci_sma_rat_zscore_5d": {"inputs": ["high", "low", "close"], "func": ccid_092_cci_sma_rat_zscore_5d},
    "ccid_093_cci_sma_rat_rank_5d": {"inputs": ["high", "low", "close"], "func": ccid_093_cci_sma_rat_rank_5d},
    "ccid_094_cci_sma_rat_lvl_21d": {"inputs": ["high", "low", "close"], "func": ccid_094_cci_sma_rat_lvl_21d},
    "ccid_095_cci_sma_rat_zscore_21d": {"inputs": ["high", "low", "close"], "func": ccid_095_cci_sma_rat_zscore_21d},
    "ccid_096_cci_sma_rat_rank_21d": {"inputs": ["high", "low", "close"], "func": ccid_096_cci_sma_rat_rank_21d},
    "ccid_097_cci_sma_rat_lvl_63d": {"inputs": ["high", "low", "close"], "func": ccid_097_cci_sma_rat_lvl_63d},
    "ccid_098_cci_sma_rat_zscore_63d": {"inputs": ["high", "low", "close"], "func": ccid_098_cci_sma_rat_zscore_63d},
    "ccid_099_cci_sma_rat_rank_63d": {"inputs": ["high", "low", "close"], "func": ccid_099_cci_sma_rat_rank_63d},
    "ccid_100_cci_sma_rat_lvl_126d": {"inputs": ["high", "low", "close"], "func": ccid_100_cci_sma_rat_lvl_126d},
    "ccid_101_cci_sma_rat_zscore_126d": {"inputs": ["high", "low", "close"], "func": ccid_101_cci_sma_rat_zscore_126d},
    "ccid_102_cci_sma_rat_rank_126d": {"inputs": ["high", "low", "close"], "func": ccid_102_cci_sma_rat_rank_126d},
    "ccid_103_cci_sma_rat_lvl_252d": {"inputs": ["high", "low", "close"], "func": ccid_103_cci_sma_rat_lvl_252d},
    "ccid_104_cci_sma_rat_zscore_252d": {"inputs": ["high", "low", "close"], "func": ccid_104_cci_sma_rat_zscore_252d},
    "ccid_105_cci_sma_rat_rank_252d": {"inputs": ["high", "low", "close"], "func": ccid_105_cci_sma_rat_rank_252d},
    "ccid_106_cci_abs_lvl_5d": {"inputs": ["high", "low", "close"], "func": ccid_106_cci_abs_lvl_5d},
    "ccid_107_cci_abs_zscore_5d": {"inputs": ["high", "low", "close"], "func": ccid_107_cci_abs_zscore_5d},
    "ccid_108_cci_abs_rank_5d": {"inputs": ["high", "low", "close"], "func": ccid_108_cci_abs_rank_5d},
    "ccid_109_cci_abs_lvl_21d": {"inputs": ["high", "low", "close"], "func": ccid_109_cci_abs_lvl_21d},
    "ccid_110_cci_abs_zscore_21d": {"inputs": ["high", "low", "close"], "func": ccid_110_cci_abs_zscore_21d},
    "ccid_111_cci_abs_rank_21d": {"inputs": ["high", "low", "close"], "func": ccid_111_cci_abs_rank_21d},
    "ccid_112_cci_abs_lvl_63d": {"inputs": ["high", "low", "close"], "func": ccid_112_cci_abs_lvl_63d},
    "ccid_113_cci_abs_zscore_63d": {"inputs": ["high", "low", "close"], "func": ccid_113_cci_abs_zscore_63d},
    "ccid_114_cci_abs_rank_63d": {"inputs": ["high", "low", "close"], "func": ccid_114_cci_abs_rank_63d},
    "ccid_115_cci_abs_lvl_126d": {"inputs": ["high", "low", "close"], "func": ccid_115_cci_abs_lvl_126d},
    "ccid_116_cci_abs_zscore_126d": {"inputs": ["high", "low", "close"], "func": ccid_116_cci_abs_zscore_126d},
    "ccid_117_cci_abs_rank_126d": {"inputs": ["high", "low", "close"], "func": ccid_117_cci_abs_rank_126d},
    "ccid_118_cci_abs_lvl_252d": {"inputs": ["high", "low", "close"], "func": ccid_118_cci_abs_lvl_252d},
    "ccid_119_cci_abs_zscore_252d": {"inputs": ["high", "low", "close"], "func": ccid_119_cci_abs_zscore_252d},
    "ccid_120_cci_abs_rank_252d": {"inputs": ["high", "low", "close"], "func": ccid_120_cci_abs_rank_252d},
    "ccid_121_cci_vol_lvl_5d": {"inputs": ["high", "low", "close"], "func": ccid_121_cci_vol_lvl_5d},
    "ccid_122_cci_vol_zscore_5d": {"inputs": ["high", "low", "close"], "func": ccid_122_cci_vol_zscore_5d},
    "ccid_123_cci_vol_rank_5d": {"inputs": ["high", "low", "close"], "func": ccid_123_cci_vol_rank_5d},
    "ccid_124_cci_vol_lvl_21d": {"inputs": ["high", "low", "close"], "func": ccid_124_cci_vol_lvl_21d},
    "ccid_125_cci_vol_zscore_21d": {"inputs": ["high", "low", "close"], "func": ccid_125_cci_vol_zscore_21d},
    "ccid_126_cci_vol_rank_21d": {"inputs": ["high", "low", "close"], "func": ccid_126_cci_vol_rank_21d},
    "ccid_127_cci_vol_lvl_63d": {"inputs": ["high", "low", "close"], "func": ccid_127_cci_vol_lvl_63d},
    "ccid_128_cci_vol_zscore_63d": {"inputs": ["high", "low", "close"], "func": ccid_128_cci_vol_zscore_63d},
    "ccid_129_cci_vol_rank_63d": {"inputs": ["high", "low", "close"], "func": ccid_129_cci_vol_rank_63d},
    "ccid_130_cci_vol_lvl_126d": {"inputs": ["high", "low", "close"], "func": ccid_130_cci_vol_lvl_126d},
    "ccid_131_cci_vol_zscore_126d": {"inputs": ["high", "low", "close"], "func": ccid_131_cci_vol_zscore_126d},
    "ccid_132_cci_vol_rank_126d": {"inputs": ["high", "low", "close"], "func": ccid_132_cci_vol_rank_126d},
    "ccid_133_cci_vol_lvl_252d": {"inputs": ["high", "low", "close"], "func": ccid_133_cci_vol_lvl_252d},
    "ccid_134_cci_vol_zscore_252d": {"inputs": ["high", "low", "close"], "func": ccid_134_cci_vol_zscore_252d},
    "ccid_135_cci_vol_rank_252d": {"inputs": ["high", "low", "close"], "func": ccid_135_cci_vol_rank_252d},
    "ccid_136_cci_hist_lvl_5d": {"inputs": ["high", "low", "close"], "func": ccid_136_cci_hist_lvl_5d},
    "ccid_137_cci_hist_zscore_5d": {"inputs": ["high", "low", "close"], "func": ccid_137_cci_hist_zscore_5d},
    "ccid_138_cci_hist_rank_5d": {"inputs": ["high", "low", "close"], "func": ccid_138_cci_hist_rank_5d},
    "ccid_139_cci_hist_lvl_21d": {"inputs": ["high", "low", "close"], "func": ccid_139_cci_hist_lvl_21d},
    "ccid_140_cci_hist_zscore_21d": {"inputs": ["high", "low", "close"], "func": ccid_140_cci_hist_zscore_21d},
    "ccid_141_cci_hist_rank_21d": {"inputs": ["high", "low", "close"], "func": ccid_141_cci_hist_rank_21d},
    "ccid_142_cci_hist_lvl_63d": {"inputs": ["high", "low", "close"], "func": ccid_142_cci_hist_lvl_63d},
    "ccid_143_cci_hist_zscore_63d": {"inputs": ["high", "low", "close"], "func": ccid_143_cci_hist_zscore_63d},
    "ccid_144_cci_hist_rank_63d": {"inputs": ["high", "low", "close"], "func": ccid_144_cci_hist_rank_63d},
    "ccid_145_cci_hist_lvl_126d": {"inputs": ["high", "low", "close"], "func": ccid_145_cci_hist_lvl_126d},
    "ccid_146_cci_hist_zscore_126d": {"inputs": ["high", "low", "close"], "func": ccid_146_cci_hist_zscore_126d},
    "ccid_147_cci_hist_rank_126d": {"inputs": ["high", "low", "close"], "func": ccid_147_cci_hist_rank_126d},
    "ccid_148_cci_hist_lvl_252d": {"inputs": ["high", "low", "close"], "func": ccid_148_cci_hist_lvl_252d},
    "ccid_149_cci_hist_zscore_252d": {"inputs": ["high", "low", "close"], "func": ccid_149_cci_hist_zscore_252d},
    "ccid_150_cci_hist_rank_252d": {"inputs": ["high", "low", "close"], "func": ccid_150_cci_hist_rank_252d},
}
