"""
83_cmfd_dynamics — Base Features 076-150
Domain: cmfd_dynamics
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

def cmfd_076_cmf60_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_076_cmf60_lvl_5d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 60), _rolling_sum(volume, 60))
    return _rolling_mean(base, 5)

def cmfd_077_cmf60_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_077_cmf60_zscore_5d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 60), _rolling_sum(volume, 60))
    return _zscore_rolling(base, 5)

def cmfd_078_cmf60_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_078_cmf60_rank_5d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 60), _rolling_sum(volume, 60))
    return _rank_pct(base, 5)

def cmfd_079_cmf60_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_079_cmf60_lvl_21d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 60), _rolling_sum(volume, 60))
    return _rolling_mean(base, 21)

def cmfd_080_cmf60_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_080_cmf60_zscore_21d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 60), _rolling_sum(volume, 60))
    return _zscore_rolling(base, 21)

def cmfd_081_cmf60_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_081_cmf60_rank_21d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 60), _rolling_sum(volume, 60))
    return _rank_pct(base, 21)

def cmfd_082_cmf60_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_082_cmf60_lvl_63d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 60), _rolling_sum(volume, 60))
    return _rolling_mean(base, 63)

def cmfd_083_cmf60_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_083_cmf60_zscore_63d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 60), _rolling_sum(volume, 60))
    return _zscore_rolling(base, 63)

def cmfd_084_cmf60_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_084_cmf60_rank_63d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 60), _rolling_sum(volume, 60))
    return _rank_pct(base, 63)

def cmfd_085_cmf60_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_085_cmf60_lvl_126d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 60), _rolling_sum(volume, 60))
    return _rolling_mean(base, 126)

def cmfd_086_cmf60_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_086_cmf60_zscore_126d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 60), _rolling_sum(volume, 60))
    return _zscore_rolling(base, 126)

def cmfd_087_cmf60_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_087_cmf60_rank_126d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 60), _rolling_sum(volume, 60))
    return _rank_pct(base, 126)

def cmfd_088_cmf60_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_088_cmf60_lvl_252d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 60), _rolling_sum(volume, 60))
    return _rolling_mean(base, 252)

def cmfd_089_cmf60_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_089_cmf60_zscore_252d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 60), _rolling_sum(volume, 60))
    return _zscore_rolling(base, 252)

def cmfd_090_cmf60_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_090_cmf60_rank_252d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 60), _rolling_sum(volume, 60))
    return _rank_pct(base, 252)

def cmfd_091_cmf_sma_rat_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_091_cmf_sma_rat_lvl_5d"""
    base = _safe_div(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 20))
    return _rolling_mean(base, 5)

def cmfd_092_cmf_sma_rat_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_092_cmf_sma_rat_zscore_5d"""
    base = _safe_div(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 20))
    return _zscore_rolling(base, 5)

def cmfd_093_cmf_sma_rat_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_093_cmf_sma_rat_rank_5d"""
    base = _safe_div(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 20))
    return _rank_pct(base, 5)

def cmfd_094_cmf_sma_rat_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_094_cmf_sma_rat_lvl_21d"""
    base = _safe_div(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 20))
    return _rolling_mean(base, 21)

def cmfd_095_cmf_sma_rat_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_095_cmf_sma_rat_zscore_21d"""
    base = _safe_div(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 20))
    return _zscore_rolling(base, 21)

def cmfd_096_cmf_sma_rat_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_096_cmf_sma_rat_rank_21d"""
    base = _safe_div(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 20))
    return _rank_pct(base, 21)

def cmfd_097_cmf_sma_rat_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_097_cmf_sma_rat_lvl_63d"""
    base = _safe_div(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 20))
    return _rolling_mean(base, 63)

def cmfd_098_cmf_sma_rat_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_098_cmf_sma_rat_zscore_63d"""
    base = _safe_div(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 20))
    return _zscore_rolling(base, 63)

def cmfd_099_cmf_sma_rat_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_099_cmf_sma_rat_rank_63d"""
    base = _safe_div(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 20))
    return _rank_pct(base, 63)

def cmfd_100_cmf_sma_rat_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_100_cmf_sma_rat_lvl_126d"""
    base = _safe_div(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 20))
    return _rolling_mean(base, 126)

def cmfd_101_cmf_sma_rat_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_101_cmf_sma_rat_zscore_126d"""
    base = _safe_div(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 20))
    return _zscore_rolling(base, 126)

def cmfd_102_cmf_sma_rat_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_102_cmf_sma_rat_rank_126d"""
    base = _safe_div(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 20))
    return _rank_pct(base, 126)

def cmfd_103_cmf_sma_rat_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_103_cmf_sma_rat_lvl_252d"""
    base = _safe_div(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 20))
    return _rolling_mean(base, 252)

def cmfd_104_cmf_sma_rat_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_104_cmf_sma_rat_zscore_252d"""
    base = _safe_div(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 20))
    return _zscore_rolling(base, 252)

def cmfd_105_cmf_sma_rat_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_105_cmf_sma_rat_rank_252d"""
    base = _safe_div(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 20))
    return _rank_pct(base, 252)

def cmfd_106_cmf_abs_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_106_cmf_abs_lvl_5d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).abs()
    return _rolling_mean(base, 5)

def cmfd_107_cmf_abs_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_107_cmf_abs_zscore_5d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).abs()
    return _zscore_rolling(base, 5)

def cmfd_108_cmf_abs_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_108_cmf_abs_rank_5d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).abs()
    return _rank_pct(base, 5)

def cmfd_109_cmf_abs_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_109_cmf_abs_lvl_21d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).abs()
    return _rolling_mean(base, 21)

def cmfd_110_cmf_abs_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_110_cmf_abs_zscore_21d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).abs()
    return _zscore_rolling(base, 21)

def cmfd_111_cmf_abs_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_111_cmf_abs_rank_21d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).abs()
    return _rank_pct(base, 21)

def cmfd_112_cmf_abs_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_112_cmf_abs_lvl_63d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).abs()
    return _rolling_mean(base, 63)

def cmfd_113_cmf_abs_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_113_cmf_abs_zscore_63d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).abs()
    return _zscore_rolling(base, 63)

def cmfd_114_cmf_abs_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_114_cmf_abs_rank_63d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).abs()
    return _rank_pct(base, 63)

def cmfd_115_cmf_abs_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_115_cmf_abs_lvl_126d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).abs()
    return _rolling_mean(base, 126)

def cmfd_116_cmf_abs_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_116_cmf_abs_zscore_126d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).abs()
    return _zscore_rolling(base, 126)

def cmfd_117_cmf_abs_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_117_cmf_abs_rank_126d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).abs()
    return _rank_pct(base, 126)

def cmfd_118_cmf_abs_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_118_cmf_abs_lvl_252d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).abs()
    return _rolling_mean(base, 252)

def cmfd_119_cmf_abs_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_119_cmf_abs_zscore_252d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).abs()
    return _zscore_rolling(base, 252)

def cmfd_120_cmf_abs_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_120_cmf_abs_rank_252d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).abs()
    return _rank_pct(base, 252)

def cmfd_121_mf_vol_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_121_mf_vol_z_lvl_5d"""
    base = _zscore_rolling(_safe_div((close - low) - (high - close), high - low) * volume, 63)
    return _rolling_mean(base, 5)

def cmfd_122_mf_vol_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_122_mf_vol_z_zscore_5d"""
    base = _zscore_rolling(_safe_div((close - low) - (high - close), high - low) * volume, 63)
    return _zscore_rolling(base, 5)

def cmfd_123_mf_vol_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_123_mf_vol_z_rank_5d"""
    base = _zscore_rolling(_safe_div((close - low) - (high - close), high - low) * volume, 63)
    return _rank_pct(base, 5)

def cmfd_124_mf_vol_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_124_mf_vol_z_lvl_21d"""
    base = _zscore_rolling(_safe_div((close - low) - (high - close), high - low) * volume, 63)
    return _rolling_mean(base, 21)

def cmfd_125_mf_vol_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_125_mf_vol_z_zscore_21d"""
    base = _zscore_rolling(_safe_div((close - low) - (high - close), high - low) * volume, 63)
    return _zscore_rolling(base, 21)

def cmfd_126_mf_vol_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_126_mf_vol_z_rank_21d"""
    base = _zscore_rolling(_safe_div((close - low) - (high - close), high - low) * volume, 63)
    return _rank_pct(base, 21)

def cmfd_127_mf_vol_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_127_mf_vol_z_lvl_63d"""
    base = _zscore_rolling(_safe_div((close - low) - (high - close), high - low) * volume, 63)
    return _rolling_mean(base, 63)

def cmfd_128_mf_vol_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_128_mf_vol_z_zscore_63d"""
    base = _zscore_rolling(_safe_div((close - low) - (high - close), high - low) * volume, 63)
    return _zscore_rolling(base, 63)

def cmfd_129_mf_vol_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_129_mf_vol_z_rank_63d"""
    base = _zscore_rolling(_safe_div((close - low) - (high - close), high - low) * volume, 63)
    return _rank_pct(base, 63)

def cmfd_130_mf_vol_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_130_mf_vol_z_lvl_126d"""
    base = _zscore_rolling(_safe_div((close - low) - (high - close), high - low) * volume, 63)
    return _rolling_mean(base, 126)

def cmfd_131_mf_vol_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_131_mf_vol_z_zscore_126d"""
    base = _zscore_rolling(_safe_div((close - low) - (high - close), high - low) * volume, 63)
    return _zscore_rolling(base, 126)

def cmfd_132_mf_vol_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_132_mf_vol_z_rank_126d"""
    base = _zscore_rolling(_safe_div((close - low) - (high - close), high - low) * volume, 63)
    return _rank_pct(base, 126)

def cmfd_133_mf_vol_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_133_mf_vol_z_lvl_252d"""
    base = _zscore_rolling(_safe_div((close - low) - (high - close), high - low) * volume, 63)
    return _rolling_mean(base, 252)

def cmfd_134_mf_vol_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_134_mf_vol_z_zscore_252d"""
    base = _zscore_rolling(_safe_div((close - low) - (high - close), high - low) * volume, 63)
    return _zscore_rolling(base, 252)

def cmfd_135_mf_vol_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_135_mf_vol_z_rank_252d"""
    base = _zscore_rolling(_safe_div((close - low) - (high - close), high - low) * volume, 63)
    return _rank_pct(base, 252)

def cmfd_136_cmf_sig_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_136_cmf_sig_lvl_5d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))) - _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 9)
    return _rolling_mean(base, 5)

def cmfd_137_cmf_sig_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_137_cmf_sig_zscore_5d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))) - _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 9)
    return _zscore_rolling(base, 5)

def cmfd_138_cmf_sig_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_138_cmf_sig_rank_5d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))) - _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 9)
    return _rank_pct(base, 5)

def cmfd_139_cmf_sig_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_139_cmf_sig_lvl_21d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))) - _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 9)
    return _rolling_mean(base, 21)

def cmfd_140_cmf_sig_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_140_cmf_sig_zscore_21d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))) - _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 9)
    return _zscore_rolling(base, 21)

def cmfd_141_cmf_sig_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_141_cmf_sig_rank_21d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))) - _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 9)
    return _rank_pct(base, 21)

def cmfd_142_cmf_sig_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_142_cmf_sig_lvl_63d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))) - _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 9)
    return _rolling_mean(base, 63)

def cmfd_143_cmf_sig_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_143_cmf_sig_zscore_63d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))) - _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 9)
    return _zscore_rolling(base, 63)

def cmfd_144_cmf_sig_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_144_cmf_sig_rank_63d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))) - _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 9)
    return _rank_pct(base, 63)

def cmfd_145_cmf_sig_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_145_cmf_sig_lvl_126d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))) - _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 9)
    return _rolling_mean(base, 126)

def cmfd_146_cmf_sig_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_146_cmf_sig_zscore_126d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))) - _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 9)
    return _zscore_rolling(base, 126)

def cmfd_147_cmf_sig_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_147_cmf_sig_rank_126d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))) - _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 9)
    return _rank_pct(base, 126)

def cmfd_148_cmf_sig_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_148_cmf_sig_lvl_252d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))) - _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 9)
    return _rolling_mean(base, 252)

def cmfd_149_cmf_sig_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_149_cmf_sig_zscore_252d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))) - _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 9)
    return _zscore_rolling(base, 252)

def cmfd_150_cmf_sig_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_150_cmf_sig_rank_252d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))) - _rolling_mean(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 9)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V83_REGISTRY_2 = {
    "cmfd_076_cmf60_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_076_cmf60_lvl_5d},
    "cmfd_077_cmf60_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_077_cmf60_zscore_5d},
    "cmfd_078_cmf60_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_078_cmf60_rank_5d},
    "cmfd_079_cmf60_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_079_cmf60_lvl_21d},
    "cmfd_080_cmf60_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_080_cmf60_zscore_21d},
    "cmfd_081_cmf60_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_081_cmf60_rank_21d},
    "cmfd_082_cmf60_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_082_cmf60_lvl_63d},
    "cmfd_083_cmf60_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_083_cmf60_zscore_63d},
    "cmfd_084_cmf60_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_084_cmf60_rank_63d},
    "cmfd_085_cmf60_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_085_cmf60_lvl_126d},
    "cmfd_086_cmf60_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_086_cmf60_zscore_126d},
    "cmfd_087_cmf60_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_087_cmf60_rank_126d},
    "cmfd_088_cmf60_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_088_cmf60_lvl_252d},
    "cmfd_089_cmf60_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_089_cmf60_zscore_252d},
    "cmfd_090_cmf60_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_090_cmf60_rank_252d},
    "cmfd_091_cmf_sma_rat_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_091_cmf_sma_rat_lvl_5d},
    "cmfd_092_cmf_sma_rat_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_092_cmf_sma_rat_zscore_5d},
    "cmfd_093_cmf_sma_rat_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_093_cmf_sma_rat_rank_5d},
    "cmfd_094_cmf_sma_rat_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_094_cmf_sma_rat_lvl_21d},
    "cmfd_095_cmf_sma_rat_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_095_cmf_sma_rat_zscore_21d},
    "cmfd_096_cmf_sma_rat_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_096_cmf_sma_rat_rank_21d},
    "cmfd_097_cmf_sma_rat_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_097_cmf_sma_rat_lvl_63d},
    "cmfd_098_cmf_sma_rat_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_098_cmf_sma_rat_zscore_63d},
    "cmfd_099_cmf_sma_rat_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_099_cmf_sma_rat_rank_63d},
    "cmfd_100_cmf_sma_rat_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_100_cmf_sma_rat_lvl_126d},
    "cmfd_101_cmf_sma_rat_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_101_cmf_sma_rat_zscore_126d},
    "cmfd_102_cmf_sma_rat_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_102_cmf_sma_rat_rank_126d},
    "cmfd_103_cmf_sma_rat_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_103_cmf_sma_rat_lvl_252d},
    "cmfd_104_cmf_sma_rat_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_104_cmf_sma_rat_zscore_252d},
    "cmfd_105_cmf_sma_rat_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_105_cmf_sma_rat_rank_252d},
    "cmfd_106_cmf_abs_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_106_cmf_abs_lvl_5d},
    "cmfd_107_cmf_abs_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_107_cmf_abs_zscore_5d},
    "cmfd_108_cmf_abs_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_108_cmf_abs_rank_5d},
    "cmfd_109_cmf_abs_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_109_cmf_abs_lvl_21d},
    "cmfd_110_cmf_abs_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_110_cmf_abs_zscore_21d},
    "cmfd_111_cmf_abs_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_111_cmf_abs_rank_21d},
    "cmfd_112_cmf_abs_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_112_cmf_abs_lvl_63d},
    "cmfd_113_cmf_abs_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_113_cmf_abs_zscore_63d},
    "cmfd_114_cmf_abs_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_114_cmf_abs_rank_63d},
    "cmfd_115_cmf_abs_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_115_cmf_abs_lvl_126d},
    "cmfd_116_cmf_abs_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_116_cmf_abs_zscore_126d},
    "cmfd_117_cmf_abs_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_117_cmf_abs_rank_126d},
    "cmfd_118_cmf_abs_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_118_cmf_abs_lvl_252d},
    "cmfd_119_cmf_abs_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_119_cmf_abs_zscore_252d},
    "cmfd_120_cmf_abs_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_120_cmf_abs_rank_252d},
    "cmfd_121_mf_vol_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_121_mf_vol_z_lvl_5d},
    "cmfd_122_mf_vol_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_122_mf_vol_z_zscore_5d},
    "cmfd_123_mf_vol_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_123_mf_vol_z_rank_5d},
    "cmfd_124_mf_vol_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_124_mf_vol_z_lvl_21d},
    "cmfd_125_mf_vol_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_125_mf_vol_z_zscore_21d},
    "cmfd_126_mf_vol_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_126_mf_vol_z_rank_21d},
    "cmfd_127_mf_vol_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_127_mf_vol_z_lvl_63d},
    "cmfd_128_mf_vol_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_128_mf_vol_z_zscore_63d},
    "cmfd_129_mf_vol_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_129_mf_vol_z_rank_63d},
    "cmfd_130_mf_vol_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_130_mf_vol_z_lvl_126d},
    "cmfd_131_mf_vol_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_131_mf_vol_z_zscore_126d},
    "cmfd_132_mf_vol_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_132_mf_vol_z_rank_126d},
    "cmfd_133_mf_vol_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_133_mf_vol_z_lvl_252d},
    "cmfd_134_mf_vol_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_134_mf_vol_z_zscore_252d},
    "cmfd_135_mf_vol_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_135_mf_vol_z_rank_252d},
    "cmfd_136_cmf_sig_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_136_cmf_sig_lvl_5d},
    "cmfd_137_cmf_sig_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_137_cmf_sig_zscore_5d},
    "cmfd_138_cmf_sig_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_138_cmf_sig_rank_5d},
    "cmfd_139_cmf_sig_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_139_cmf_sig_lvl_21d},
    "cmfd_140_cmf_sig_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_140_cmf_sig_zscore_21d},
    "cmfd_141_cmf_sig_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_141_cmf_sig_rank_21d},
    "cmfd_142_cmf_sig_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_142_cmf_sig_lvl_63d},
    "cmfd_143_cmf_sig_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_143_cmf_sig_zscore_63d},
    "cmfd_144_cmf_sig_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_144_cmf_sig_rank_63d},
    "cmfd_145_cmf_sig_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_145_cmf_sig_lvl_126d},
    "cmfd_146_cmf_sig_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_146_cmf_sig_zscore_126d},
    "cmfd_147_cmf_sig_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_147_cmf_sig_rank_126d},
    "cmfd_148_cmf_sig_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_148_cmf_sig_lvl_252d},
    "cmfd_149_cmf_sig_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_149_cmf_sig_zscore_252d},
    "cmfd_150_cmf_sig_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_150_cmf_sig_rank_252d},
}
